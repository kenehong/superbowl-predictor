"""
Window screen recorder — captures frames at intervals and compiles into an animated GIF.

Usage:
    python screen_record.py <window_title> [output_path] [--fps N] [--duration N] [--max-width N]

The recorder captures the target window at the given FPS until:
  - The specified duration (seconds) elapses, OR
  - The user presses Enter (interactive mode), OR
  - The process receives SIGINT (Ctrl+C)

Security: Uses the same PrintWindow API as screenshot.py — only captures the
specified window, no full-screen capture, no input recording, local storage only.

Requires: Pillow (pip install Pillow)
"""

import ctypes
import ctypes.wintypes
import sys
import os
import time
import argparse
import threading
from PIL import Image

# ---------------------------------------------------------------------------
# DPI awareness
# ---------------------------------------------------------------------------
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    ctypes.windll.user32.SetProcessDPIAware()

# ---------------------------------------------------------------------------
# Win32 constants & signatures (same as screenshot.py)
# ---------------------------------------------------------------------------
PW_RENDERFULLCONTENT = 0x00000002

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32


class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ("biSize", ctypes.wintypes.DWORD),
        ("biWidth", ctypes.wintypes.LONG),
        ("biHeight", ctypes.wintypes.LONG),
        ("biPlanes", ctypes.wintypes.WORD),
        ("biBitCount", ctypes.wintypes.WORD),
        ("biCompression", ctypes.wintypes.DWORD),
        ("biSizeImage", ctypes.wintypes.DWORD),
        ("biXPelsPerMeter", ctypes.wintypes.LONG),
        ("biYPelsPerMeter", ctypes.wintypes.LONG),
        ("biClrUsed", ctypes.wintypes.DWORD),
        ("biClrImportant", ctypes.wintypes.DWORD),
    ]


class BITMAPINFO(ctypes.Structure):
    _fields_ = [
        ("bmiHeader", BITMAPINFOHEADER),
        ("bmiColors", ctypes.wintypes.DWORD * 3),
    ]


# Type signatures
user32.GetWindowTextLengthW.argtypes = [ctypes.wintypes.HWND]
user32.GetWindowTextLengthW.restype = ctypes.c_int

user32.GetWindowTextW.argtypes = [ctypes.wintypes.HWND, ctypes.c_wchar_p, ctypes.c_int]
user32.GetWindowTextW.restype = ctypes.c_int

user32.IsWindowVisible.argtypes = [ctypes.wintypes.HWND]
user32.IsWindowVisible.restype = ctypes.wintypes.BOOL

user32.GetWindowRect.argtypes = [ctypes.wintypes.HWND, ctypes.POINTER(ctypes.wintypes.RECT)]
user32.GetWindowRect.restype = ctypes.wintypes.BOOL

user32.GetWindowDC.argtypes = [ctypes.wintypes.HWND]
user32.GetWindowDC.restype = ctypes.wintypes.HDC

user32.ReleaseDC.argtypes = [ctypes.wintypes.HWND, ctypes.wintypes.HDC]
user32.ReleaseDC.restype = ctypes.c_int

user32.PrintWindow.argtypes = [ctypes.wintypes.HWND, ctypes.wintypes.HDC, ctypes.wintypes.UINT]
user32.PrintWindow.restype = ctypes.wintypes.BOOL

gdi32.CreateCompatibleDC.argtypes = [ctypes.wintypes.HDC]
gdi32.CreateCompatibleDC.restype = ctypes.wintypes.HDC

gdi32.CreateCompatibleBitmap.argtypes = [ctypes.wintypes.HDC, ctypes.c_int, ctypes.c_int]
gdi32.CreateCompatibleBitmap.restype = ctypes.wintypes.HBITMAP

gdi32.SelectObject.argtypes = [ctypes.wintypes.HDC, ctypes.wintypes.HGDIOBJ]
gdi32.SelectObject.restype = ctypes.wintypes.HGDIOBJ

gdi32.GetDIBits.argtypes = [
    ctypes.wintypes.HDC, ctypes.wintypes.HBITMAP, ctypes.wintypes.UINT,
    ctypes.wintypes.UINT, ctypes.c_void_p, ctypes.c_void_p, ctypes.wintypes.UINT,
]
gdi32.GetDIBits.restype = ctypes.c_int

gdi32.DeleteObject.argtypes = [ctypes.wintypes.HGDIOBJ]
gdi32.DeleteObject.restype = ctypes.wintypes.BOOL

gdi32.DeleteDC.argtypes = [ctypes.wintypes.HDC]
gdi32.DeleteDC.restype = ctypes.wintypes.BOOL


# ---------------------------------------------------------------------------
# Window helpers
# ---------------------------------------------------------------------------
def find_window(title_substring: str):
    """Find visible windows whose title contains the given substring."""
    results = []

    def callback(hwnd, _):
        length = user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            buf = ctypes.create_unicode_buffer(length + 1)
            user32.GetWindowTextW(hwnd, buf, length + 1)
            if title_substring.lower() in buf.value.lower():
                if user32.IsWindowVisible(hwnd):
                    results.append((hwnd, buf.value))
        return True

    WNDENUMPROC = ctypes.WINFUNCTYPE(
        ctypes.wintypes.BOOL, ctypes.wintypes.HWND, ctypes.wintypes.LPARAM
    )
    user32.EnumWindows(WNDENUMPROC(callback), 0)
    return results


def capture_window(hwnd) -> Image.Image:
    """Capture a window via PrintWindow and return as a PIL Image."""
    rect = ctypes.wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(rect))
    width = rect.right - rect.left
    height = rect.bottom - rect.top

    if width <= 0 or height <= 0:
        raise ValueError(f"Invalid window dimensions: {width}x{height}")

    wdc = user32.GetWindowDC(hwnd)
    mdc = gdi32.CreateCompatibleDC(wdc)
    bitmap = gdi32.CreateCompatibleBitmap(wdc, width, height)
    old_bitmap = gdi32.SelectObject(mdc, bitmap)

    result = user32.PrintWindow(hwnd, mdc, PW_RENDERFULLCONTENT)
    if not result:
        user32.PrintWindow(hwnd, mdc, 0)

    bmi = BITMAPINFO()
    bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.bmiHeader.biWidth = width
    bmi.bmiHeader.biHeight = -height  # top-down
    bmi.bmiHeader.biPlanes = 1
    bmi.bmiHeader.biBitCount = 32
    bmi.bmiHeader.biCompression = 0

    buf_size = width * height * 4
    buf = ctypes.create_string_buffer(buf_size)
    gdi32.GetDIBits(mdc, bitmap, 0, height, buf, ctypes.byref(bmi), 0)

    gdi32.SelectObject(mdc, old_bitmap)
    gdi32.DeleteObject(bitmap)
    gdi32.DeleteDC(mdc)
    user32.ReleaseDC(hwnd, wdc)

    return Image.frombuffer("RGBA", (width, height), buf, "raw", "BGRA", 0, 1)


# ---------------------------------------------------------------------------
# Duplicate frame detection
# ---------------------------------------------------------------------------
def frames_differ(img_a: Image.Image, img_b: Image.Image, threshold: int = 500) -> bool:
    """Return True if two images differ by more than `threshold` pixels."""
    if img_a.size != img_b.size:
        return True
    pixels_a = img_a.tobytes()
    pixels_b = img_b.tobytes()
    if pixels_a == pixels_b:
        return False
    # Quick byte-level diff: count bytes that differ
    diff_count = sum(1 for a, b in zip(pixels_a[::16], pixels_b[::16]) if a != b)
    return diff_count > threshold


# ---------------------------------------------------------------------------
# Recorder
# ---------------------------------------------------------------------------
def record(
    hwnd,
    window_title: str,
    output_path: str,
    fps: int = 2,
    duration: float | None = None,
    max_width: int = 800,
):
    """Record frames and save as animated GIF."""
    interval = 1.0 / fps
    frames: list[Image.Image] = []
    stop_event = threading.Event()

    # In non-interactive (agent) mode, rely on duration or Ctrl+C
    # In interactive mode, also allow Enter to stop
    if duration is None and sys.stdin.isatty():
        def wait_for_enter():
            input()
            stop_event.set()

        t = threading.Thread(target=wait_for_enter, daemon=True)
        t.start()
        print(f"Recording '{window_title}' at {fps} FPS. Press Enter to stop...")
    elif duration:
        print(f"Recording '{window_title}' at {fps} FPS for {duration}s...")
    else:
        print(f"Recording '{window_title}' at {fps} FPS. Send Ctrl+C to stop...")

    start_time = time.monotonic()
    last_frame: Image.Image | None = None

    try:
        while not stop_event.is_set():
            if duration and (time.monotonic() - start_time) >= duration:
                break

            frame_start = time.monotonic()
            try:
                frame = capture_window(hwnd)

                # Skip duplicate frames to keep GIF small
                if last_frame is not None and not frames_differ(frame, last_frame):
                    # Still count time but don't store duplicate
                    elapsed = time.monotonic() - frame_start
                    if elapsed < interval:
                        time.sleep(interval - elapsed)
                    continue

                last_frame = frame
                frames.append(frame)

                elapsed_total = time.monotonic() - start_time
                sys.stdout.write(f"\r  Frames: {len(frames)} | Elapsed: {elapsed_total:.1f}s")
                sys.stdout.flush()

            except Exception as e:
                print(f"\n  Warning: Frame capture failed: {e}")

            elapsed = time.monotonic() - frame_start
            if elapsed < interval:
                time.sleep(interval - elapsed)

    except KeyboardInterrupt:
        pass

    print(f"\n\nCapture complete. {len(frames)} unique frames.")

    if not frames:
        print("ERROR: No frames captured.")
        sys.exit(1)

    # Resize for GIF (keep aspect ratio)
    resized: list[Image.Image] = []
    for f in frames:
        if f.width > max_width:
            ratio = max_width / f.width
            new_size = (max_width, int(f.height * ratio))
            resized.append(f.resize(new_size, Image.LANCZOS))
        else:
            resized.append(f)

    # Convert RGBA → RGB (GIF doesn't support alpha well) with white background
    rgb_frames: list[Image.Image] = []
    for f in resized:
        bg = Image.new("RGB", f.size, (255, 255, 255))
        bg.paste(f, mask=f.split()[3] if f.mode == "RGBA" else None)
        rgb_frames.append(bg)

    # Save animated GIF
    frame_duration_ms = int(1000 / fps)
    rgb_frames[0].save(
        output_path,
        save_all=True,
        append_images=rgb_frames[1:],
        duration=frame_duration_ms,
        loop=0,
        optimize=True,
    )

    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"Saved: {output_path} ({rgb_frames[0].size[0]}x{rgb_frames[0].size[1]}, {file_size_kb:.0f} KB)")
    return output_path


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Record a window as animated GIF")
    parser.add_argument("window_title", help="Substring to match in window title")
    parser.add_argument("output", nargs="?", default="recording.gif", help="Output GIF path")
    parser.add_argument("--fps", type=int, default=2, help="Frames per second (default: 2)")
    parser.add_argument("--duration", type=float, default=None, help="Recording duration in seconds (default: until Enter/Ctrl+C)")
    parser.add_argument("--max-width", type=int, default=800, help="Max width for GIF frames (default: 800)")
    args = parser.parse_args()

    windows = find_window(args.window_title)
    if not windows:
        print(f"ERROR: No visible window found matching '{args.window_title}'")
        print("Available windows:")
        for _, t in find_window("")[:15]:
            print(f"  - {t}")
        sys.exit(1)

    hwnd, actual_title = windows[0]
    record(
        hwnd=hwnd,
        window_title=actual_title,
        output_path=args.output,
        fps=args.fps,
        duration=args.duration,
        max_width=args.max_width,
    )


if __name__ == "__main__":
    main()
