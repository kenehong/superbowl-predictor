# Figma-to-Code Workflow

Use when implementing UI from a Figma design file.

## Core Rule
**If Figma data has a value, use it — do not guess.**

## Priority
**Figma spec > Reference rules > Personal experience.**
- References (ui-ux.md, etc.) apply only to areas not specified in Figma (accessibility, performance, patterns).
- When Figma conflicts with a reference (e.g., NavigationView vs custom rail), follow Figma.

## Visual Reference: The agent can see images, but Figma MCP does not provide them
- **The agent can visually analyze images (PNG, screenshots, etc.).**
- **However, Figma MCP (`get_figma_data`) only returns a JSON tree. It does not provide rendered images.**
- Therefore, using Figma MCP alone means implementing from JSON data without ever "seeing" the design.
- **Solution:** Provide Figma screenshots (PNG) alongside the link so the agent can reference both visuals and JSON — this is the most accurate workflow.
- Screenshots are essential for icon glyphs, overall layout feel, and detecting elements that should NOT exist.

## Step 1: Deep Fetch First
- Fetch from Figma API at `depth=6` or higher to capture layout properties.
- Do not guess structure from component names using a shallow depth fetch.
- On the first fetch, always read layout, padding, gap, and dimensions from globalVars/styles.

## Step 2: Extract Before Coding
Extract the following from Figma data before writing any code:

### Layout structure
- Which containers are row vs column
- Sizing mode for each area (fixed, fill, hug)
- Nesting structure (what's inside what)

### Exact values
- Padding (each side individually)
- Gap / spacing
- Dimensions (width, height)
- Border radius
- Font size, weight

### Component mapping
- Decide the Figma component → WinUI control mapping first
- Figma custom components may differ from WinUI built-in controls (e.g., Side Nav ≠ NavigationView)
- Check variant properties to determine which control fits each state

### Colors and fills
- Extract exact color codes from fill values
- Distinguish what can map to ThemeResource vs what needs custom definitions

## Step 3: Build with Values, Not Guesses
- No "close enough" values like padding="20,12"
- If Figma says `padding: 12px 12px 12px 24px`, use `Padding="24,12,12,12"` exactly in XAML
- If avatar is 32px, use 32px. No "40 would look better" overrides.

## Step 4: Verify After Build
- Build success ≠ design match
- After building, always compare against Figma values
- Especially: spacing, size, alignment, color

## Common Figma→WinUI Pitfalls
| Figma | Wrong assumption | Correct mapping |
|---|---|---|
| Custom collapsed side nav | NavigationView LeftCompact | Build a custom 48px Grid rail |
| Search=Off in title bar | Add AutoSuggestBox | Title bar without search |
| PersonPicture Size=32 | Width="40" | Width="32" |
| Subtle button style | SubtleButtonStyle (doesn't exist) | Define a custom Style |
| flex-end alignment | Default top alignment | VerticalAlignment="Bottom" |
| `rgba(0,0,0,0.08)` divider | CardStrokeColor | DividerStrokeColorDefaultBrush |

## Figma Layout → XAML Cheat Sheet
| Figma layout mode | XAML equivalent |
|---|---|
| `mode: row` | `StackPanel Orientation="Horizontal"` or `Grid` with columns |
| `mode: column` | `StackPanel` or `Grid` with rows |
| `sizing: fill` | Star sizing (`*`) or `HorizontalAlignment="Stretch"` |
| `sizing: hug` | `Auto` sizing |
| `sizing: fixed` | Explicit Width/Height |
| `justifyContent: flex-end` | `VerticalAlignment="Bottom"` or `HorizontalAlignment="Right"` |
| `gap: 12px` | `Spacing="12"` |
| `padding: 12px 24px` | `Padding="24,12"` (WinUI order: left,top,right,bottom) |

Source: Learned from ChatPrototype build session (2025-02-25)
