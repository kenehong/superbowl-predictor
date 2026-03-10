# Screenshot Skill

Capture screenshots of running WinUI 3 app windows for visual verification using the Win32 PrintWindow API. Works even when the window is partially occluded.

## Prerequisites

- Python 3.8+
- **Pillow**: `pip install Pillow`
- Windows only (uses Win32 APIs)
- DPI-aware: auto-sets `SetProcessDpiAwareness(2)` for correct high-DPI capture

## Setup

The screenshot script is located at `skills/screenshot/screenshot.py` in this project.

## Usage

```bash
python skills/screenshot/screenshot.py "<window_title>" "<output_path>"
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `window_title` | `"Frog Markdown"` | Substring match in window title (case-insensitive) |
| `output_path` | `screenshot.png` | Output file path for the PNG |

## Examples

```bash
# Capture your running WinUI 3 app
python skills/screenshot/screenshot.py "My App" screenshot.png

# List available windows (use a non-matching title)
python skills/screenshot/screenshot.py "???"
```

## Agent Workflow

1. **Capture**: Run the script with the app's window title
2. **View**: Use the `view` tool on the saved PNG to see it
3. **Compare**: Check against Figma designs or expected layout
4. **Iterate**: Make XAML/code changes and re-capture to verify

## When to Use

- Visual feedback from user ("looks wrong", "spacing is off", "check the UI")
- Verifying layout after XAML changes
- Comparing implementation against Figma designs
- Debugging visual regressions
- Any time you need to see the current state of the running app

## How It Works

1. Sets per-monitor DPI awareness for physical-pixel accuracy
2. Enumerates visible windows and matches by title substring
3. Uses `PrintWindow` with `PW_RENDERFULLCONTENT` for capture
4. Converts BGRA → RGBA and saves as PNG via Pillow
