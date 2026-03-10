"""
Window screenshot capture tool for visual verification of WinUI 3 apps.

Usage:
    python screenshot.py [window_title] [output_path]

Defaults:
    window_title: "Frog Markdown"
    output_path:  screenshot.png (in current directory)

Uses Win32 PrintWindow API — captures the window even if partially occluded.
Requires: Pillow (pip install Pillow)
"""

import ctypes
import ctypes.wintypes
import sys
import os
from PIL import Image

# Enable per-monitor DPI awareness so GetWindowRect returns physical pixels
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # PROCESS_PER_MONITOR_DPI_AWARE
except Exception:
    ctypes.windll.user32.SetProcessDPIAware()

# Win32 constants
SRCCOPY = 0x00CC0020
PW_RENDERFULLCONTENT = 0x00000002
DWMWA_EXTENDED_FRAME_BOUNDS = 9

# Win32 function signatures
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
dwmapi = ctypes.windll.dwmapi

user32.FindWindowW.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p]
user32.FindWindowW.restype = ctypes.wintypes.HWND

user32.GetWindowRect.argtypes = [ctypes.wintypes.HWND, ctypes.POINTER(ctypes.wintypes.RECT)]
user32.GetWindowRect.restype = ctypes.wintypes.BOOL

user32.GetWindowDC.argtypes = [ctypes.wintypes.HWND]
user32.GetWindowDC.restype = ctypes.wintypes.HDC

user32.ReleaseDC.argtypes = [ctypes.wintypes.HWND, ctypes.wintypes.HDC]
user32.ReleaseDC.restype = ctypes.c_int

user32.PrintWindow.argtypes = [ctypes.wintypes.HWND, ctypes.wintypes.HDC, ctypes.wintypes.UINT]
user32.PrintWindow.restype = ctypes.wintypes.BOOL

user32.SetForegroundWindow.argtypes = [ctypes.wintypes.HWND]
user32.SetForegroundWindow.restype = ctypes.wintypes.BOOL

gdi32.CreateCompatibleDC.argtypes = [ctypes.wintypes.HDC]
gdi32.CreateCompatibleDC.restype = ctypes.wintypes.HDC

gdi32.CreateCompatibleBitmap.argtypes = [ctypes.wintypes.HDC, ctypes.c_int, ctypes.c_int]
gdi32.CreateCompatibleBitmap.restype = ctypes.wintypes.HBITMAP

gdi32.SelectObject.argtypes = [ctypes.wintypes.HDC, ctypes.wintypes.HGDIOBJ]
gdi32.SelectObject.restype = ctypes.wintypes.HGDIOBJ

gdi32.GetDIBits.argtypes = [
    ctypes.wintypes.HDC, ctypes.wintypes.HBITMAP, ctypes.wintypes.UINT,
    ctypes.wintypes.UINT, ctypes.c_void_p, ctypes.c_void_p, ctypes.wintypes.UINT
]
gdi32.GetDIBits.restype = ctypes.c_int

gdi32.DeleteObject.argtypes = [ctypes.wintypes.HGDIOBJ]
gdi32.DeleteObject.restype = ctypes.wintypes.BOOL

gdi32.DeleteDC.argtypes = [ctypes.wintypes.HDC]
gdi32.DeleteDC.restype = ctypes.wintypes.BOOL


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


def find_window(title_substring):
    """Find a window whose title contains the given substring."""
    result = []

    def callback(hwnd, _):
        length = user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            buf = ctypes.create_unicode_buffer(length + 1)
            user32.GetWindowTextW(hwnd, buf, length + 1)
            if title_substring.lower() in buf.value.lower():
                if user32.IsWindowVisible(hwnd):
                    result.append((hwnd, buf.value))
        return True

    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.wintypes.BOOL, ctypes.wintypes.HWND, ctypes.wintypes.LPARAM)
    user32.EnumWindows(WNDENUMPROC(callback), 0)
    return result


def capture_window(hwnd):
    """Capture a window using PrintWindow and return as PIL Image."""
    # Get window dimensions
    rect = ctypes.wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(rect))
    width = rect.right - rect.left
    height = rect.bottom - rect.top

    if width <= 0 or height <= 0:
        raise ValueError(f"Invalid window dimensions: {width}x{height}")

    # Create compatible DC and bitmap
    wdc = user32.GetWindowDC(hwnd)
    mdc = gdi32.CreateCompatibleDC(wdc)
    bitmap = gdi32.CreateCompatibleBitmap(wdc, width, height)
    old_bitmap = gdi32.SelectObject(mdc, bitmap)

    # Capture using PrintWindow (works even if occluded)
    result = user32.PrintWindow(hwnd, mdc, PW_RENDERFULLCONTENT)
    if not result:
        # Fallback: try without PW_RENDERFULLCONTENT
        result = user32.PrintWindow(hwnd, mdc, 0)

    # Extract pixel data
    bmi = BITMAPINFO()
    bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.bmiHeader.biWidth = width
    bmi.bmiHeader.biHeight = -height  # Top-down
    bmi.bmiHeader.biPlanes = 1
    bmi.bmiHeader.biBitCount = 32
    bmi.bmiHeader.biCompression = 0  # BI_RGB

    buf_size = width * height * 4
    buf = ctypes.create_string_buffer(buf_size)
    gdi32.GetDIBits(mdc, bitmap, 0, height, buf, ctypes.byref(bmi), 0)

    # Cleanup
    gdi32.SelectObject(mdc, old_bitmap)
    gdi32.DeleteObject(bitmap)
    gdi32.DeleteDC(mdc)
    user32.ReleaseDC(hwnd, wdc)

    # Convert BGRA to RGBA
    img = Image.frombuffer("RGBA", (width, height), buf, "raw", "BGRA", 0, 1)
    return img


def main():
    title = sys.argv[1] if len(sys.argv) > 1 else "Frog Markdown"
    output = sys.argv[2] if len(sys.argv) > 2 else "screenshot.png"

    # Find the window
    windows = find_window(title)
    if not windows:
        print(f"ERROR: No visible window found matching '{title}'")
        print("Available windows:")
        all_windows = find_window("")
        for _, t in all_windows[:15]:
            print(f"  - {t}")
        sys.exit(1)

    hwnd, actual_title = windows[0]
    print(f"Capturing: '{actual_title}' (HWND: {hwnd})")

    # Capture
    img = capture_window(hwnd)
    img.save(output, "PNG")

    print(f"Saved: {output} ({img.size[0]}x{img.size[1]})")
    return output


if __name__ == "__main__":
    main()
