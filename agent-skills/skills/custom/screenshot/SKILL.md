---
name: screenshot
description: Use this skill to capture screenshots or screen recordings of windows on the user's desktop. Captures a specific window by title using Win32 PrintWindow API — works even if the window is partially occluded. Supports single screenshots (PNG) and animated screen recordings (GIF) for reviewing multi-page flows and interactions. Trigger phrases include "take a screenshot", "capture the window", "show me what it looks like", "screenshot of [app name]", "record the screen", "screen recording", "record interactions", "capture a walkthrough".
---

# Window Screenshot & Screen Recorder

Captures screenshots and animated screen recordings of desktop windows using the Win32 PrintWindow API.

## Prerequisites

- **Pillow**: `pip install Pillow`
- Windows only (uses Win32 APIs)
- DPI-aware: automatically calls `SetProcessDpiAwareness(2)` so full window is captured correctly on high-DPI displays

---

## Screenshot (Single Frame)

```bash
python scripts/screenshot.py [window_title] [output_path]
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `window_title` | `"Frog Markdown"` | Substring to match in window title (case-insensitive) |
| `output_path` | `screenshot.png` | Output file path for the PNG |

### Examples

```bash
python scripts/screenshot.py "Phone Link" screenshot.png
python scripts/screenshot.py  # default title
```

---

## Screen Recording (Animated GIF)

Records frames at a configurable interval and compiles them into an animated GIF.
Duplicate frames are automatically skipped to keep file size small.

```bash
python scripts/screen_record.py <window_title> [output_path] [--fps N] [--duration N] [--max-width N]
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `window_title` | *(required)* | Substring to match in window title |
| `output_path` | `recording.gif` | Output file path for the GIF |
| `--fps` | `2` | Frames per second (1–5 recommended) |
| `--duration` | *(until stopped)* | Recording duration in seconds |
| `--max-width` | `800` | Max width for GIF frames (auto aspect ratio) |

### Stopping the recording

- **Duration mode**: stops automatically after `--duration` seconds
- **Interactive mode**: press Enter to stop
- **Agent mode**: use Ctrl+C or set `--duration`

### Examples

```bash
# Record for 10 seconds at 2 FPS
python scripts/screen_record.py "Phone Link" recording.gif --duration 10

# Record at higher FPS (smoother but larger file)
python scripts/screen_record.py "My App" walkthrough.gif --fps 4 --duration 15

# Record until manually stopped
python scripts/screen_record.py "My App" recording.gif
```

---

## How It Works

1. Sets per-monitor DPI awareness so window dimensions are in physical pixels
2. Enumerates visible windows and matches by title substring
3. Uses `PrintWindow` with `PW_RENDERFULLCONTENT` for accurate capture (works even if occluded)
4. **Screenshot**: Converts BGRA → RGBA, saves as PNG
5. **Recording**: Captures frames at interval, skips duplicates, resizes, converts RGBA → RGB, saves as animated GIF

## Security

- **Window-scoped**: Only captures the specified window, not the entire screen
- **Local only**: All data stays on disk, no network transmission
- **No input capture**: Records visual frames only — no keystrokes or mouse events
- **Same session**: Can only access windows in the current user session
- ⚠️ If the app displays sensitive info, it will appear in the capture — treat output files accordingly

## Agent Instructions

### For screenshots:
1. Run: `python "C:\Users\kehong\source\repos\agent-skills\screenshot\scripts\screenshot.py" "<window_title>" "<output_path>"`
2. After capturing, use `view` on the saved PNG.

### For screen recordings:
1. **Always use `--duration`** when running from the agent (no interactive Enter to stop).
2. Run with `mode="sync"` and adequate `initial_wait` (duration + 5s buffer):
   ```
   python "C:\Users\kehong\source\repos\agent-skills\screenshot\scripts\screen_record.py" "<window_title>" "<output_path>" --duration <seconds> --fps 2
   ```
3. After recording, the GIF can be viewed with the `view` tool or opened in a browser.
4. For reviewing multi-page flows: ask the user to navigate through pages during the recording window.
5. Recommended: `--duration 10 --fps 2` for quick reviews, `--duration 20 --fps 3` for detailed walkthroughs.
6. If no matching window is found, the script lists available windows — relay those to the user.
