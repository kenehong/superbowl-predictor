# PPTX Design Guide

Professional design patterns for PowerPoint presentations using pptxgenjs.

---

## Design Philosophy

**From marketplace pptx skill**:
> "Don't create boring slides. Plain bullets on a white background won't impress anyone."

**Core principles**:
1. **Bold, content-informed color palette** - Colors should reflect the topic
2. **Dominance over equality** - One color dominates (60-70%), others support
3. **Dark/light contrast** - Dark for title/conclusion, light for content
4. **Visual motif** - Pick ONE distinctive element and repeat it
5. **Every slide needs a visual** - Image, chart, icon, or shape

---

## Color Palettes

Choose colors that match your project theme.

### Tech/Code Projects

| Theme | Primary | Secondary | Accent | Use For |
|-------|---------|-----------|--------|---------|
| **Midnight Executive** | `1E2761` (navy) | `CADCFC` (ice blue) | `FFFFFF` (white) | Code projects, technical demos |
| **Charcoal Minimal** | `36454F` (charcoal) | `F2F2F2` (off-white) | `212121` (black) | Architecture, system design |
| **Teal Trust** | `028090` (teal) | `00A896` (seafoam) | `02C39A` (mint) | Data projects, analytics |

### Product/Demo

| Theme | Primary | Secondary | Accent | Use For |
|-------|---------|-----------|--------|---------|
| **Coral Energy** | `F96167` (coral) | `F9E795` (gold) | `2F3C7E` (navy) | Fun products, games |
| **Ocean Gradient** | `065A82` (deep blue) | `1C7293` (teal) | `21295C` (midnight) | Apps, SaaS products |
| **Cherry Bold** | `990011` (cherry) | `FCF6F5` (off-white) | `2F3C7E` (navy) | Bold launches, announcements |

### Business/Portfolio

| Theme | Primary | Secondary | Accent | Use For |
|-------|---------|-----------|--------|---------|
| **Forest & Moss** | `2C5F2D` (forest) | `97BC62` (moss) | `F5F5F5` (cream) | Sustainability, growth |
| **Warm Terracotta** | `B85042` (terracotta) | `E7E8D1` (sand) | `A7BEAE` (sage) | Creative, design-focused |
| **Sage Calm** | `84B59F` (sage) | `69A297` (eucalyptus) | `50808E` (slate) | Calm, professional |

**Usage in pptxgenjs**:
```javascript
slide.background = { color: '1E2761' };  // Primary
slide.addText("Title", { color: 'CADCFC' });  // Secondary
slide.addShape(pres.shapes.RECTANGLE, { fill: { color: 'FFFFFF' } });  // Accent
```

---

## Typography

### Font Pairings

**Don't default to Arial.** Pick a pairing with personality.

| Header Font | Body Font | Personality |
|-------------|-----------|-------------|
| **Arial Black** | **Calibri** | Bold, modern (default for code) |
| Georgia | Calibri | Classic, elegant |
| Trebuchet MS | Calibri | Friendly, approachable |
| Cambria | Calibri | Professional, refined |
| Impact | Arial | Loud, attention-grabbing |

**Usage in pptxgenjs**:
```javascript
// Title
slide.addText("Project Name", {
  fontSize: 44, bold: true, fontFace: "Arial Black"
});

// Body
slide.addText("Description text", {
  fontSize: 16, fontFace: "Calibri"
});
```

### Size Guidelines

| Element | Size | Weight |
|---------|------|--------|
| Slide title | 36-44pt | Bold |
| Section header | 20-24pt | Bold |
| Body text | 14-16pt | Regular |
| Captions | 10-12pt | Regular/Italic |
| Big numbers (stats) | 60-72pt | Bold |

---

## Layout Patterns

### 1. Title Slide

```javascript
let slide = pres.addSlide();
slide.background = { color: '1E2761' };  // Dark background

// Title
slide.addText("Project Name", {
  x: 0.5, y: 2.0, w: 9, h: 1,
  fontSize: 44, bold: true, color: 'FFFFFF', align: 'center'
});

// Subtitle
slide.addText("One-liner description", {
  x: 0.5, y: 3.0, w: 9, h: 0.5,
  fontSize: 20, color: 'CADCFC', align: 'center', italic: true
});

// Metadata
slide.addText("Your Name • March 2026", {
  x: 0.5, y: 4.8, w: 9, h: 0.3,
  fontSize: 12, color: 'CADCFC', align: 'center'
});
```

**Result**: Centered, dark background, clear hierarchy.

---

### 2. Problem Slide

```javascript
let slide = pres.addSlide();

// Title
slide.addText("The Problem", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: '1E2761'
});

// Callout box
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.3, w: 9, h: 3.5,
  fill: { color: 'CADCFC', transparency: 70 },
  line: { color: '1E2761', width: 2 }
});

// Problem statement (inside box)
slide.addText("Current situation is painful because...", {
  x: 0.7, y: 1.5, w: 8.6, h: 0.8,
  fontSize: 20, bold: true, color: '1E2761'
});

// Bullet points
slide.addText([
  { text: "Pain point 1", options: { bullet: true, breakLine: true } },
  { text: "Pain point 2", options: { bullet: true, breakLine: true } },
  { text: "Pain point 3", options: { bullet: true } }
], {
  x: 0.7, y: 2.5, w: 8.6, h: 2,
  fontSize: 16, color: '212121'
});
```

---

### 3. Three-Column Features

```javascript
let slide = pres.addSlide();

slide.addText("The Solution", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: '1E2761'
});

// Feature 1
slide.addShape(pres.shapes.OVAL, {
  x: 1.0, y: 1.5, w: 0.6, h: 0.6,
  fill: { color: '028090' }
});
slide.addText("🎯", { x: 1.15, y: 1.65, fontSize: 24 });
slide.addText("Feature 1", {
  x: 0.7, y: 2.3, w: 2.3, h: 0.4,
  fontSize: 20, bold: true, color: '1E2761', align: 'center'
});
slide.addText("Benefit in one sentence", {
  x: 0.7, y: 2.8, w: 2.3, h: 1,
  fontSize: 14, color: '363636', align: 'center'
});

// Feature 2 (x: 3.85)
// Feature 3 (x: 6.7)
// [Repeat pattern]
```

---

### 4. Two-Column Layout

```javascript
let slide = pres.addSlide();

slide.addText("Technical Approach", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: '1E2761'
});

// Left column: Text
slide.addText([
  { text: "Key decision: ", options: { bold: true } },
  { text: "We chose localStorage over backend because...\n\n", options: { breakLine: true } },
  { text: "Benefits:", options: { bold: true, breakLine: true } },
  { text: "• No server needed", options: { bullet: true, breakLine: true } },
  { text: "• Works offline", options: { bullet: true, breakLine: true } },
  { text: "• Zero latency", options: { bullet: true } }
], {
  x: 0.5, y: 1.5, w: 4.5, h: 3.5,
  fontSize: 14, color: '363636'
});

// Right column: Code or diagram
slide.addShape(pres.shapes.RECTANGLE, {
  x: 5.5, y: 1.5, w: 4, h: 3.5,
  fill: { color: '2C2C2C' }
});
slide.addText("localStorage.setItem(\n  'predictions',\n  JSON.stringify(data)\n);", {
  x: 5.7, y: 2.5, w: 3.6, h: 1.5,
  fontSize: 14, fontFace: 'Courier New', color: 'FFFFFF'
});
```

---

### 5. Timeline

```javascript
let slide = pres.addSlide();

slide.addText("The Journey", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: '1E2761'
});

// Phase 1
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.5, w: 9, h: 0.8,
  fill: { color: 'CADCFC', transparency: 30 },
  line: { color: '028090', width: 3, dashType: 'solid' }
});
slide.addText("10-15 min", {
  x: 0.7, y: 1.65, w: 1.5, h: 0.5,
  fontSize: 16, bold: true, color: '028090'
});
slide.addText("Core functionality built", {
  x: 2.5, y: 1.65, w: 6.5, h: 0.5,
  fontSize: 14, color: '363636'
});

// Phase 2 (y: 2.5)
// Phase 3 (y: 3.5)
// [Repeat pattern]
```

---

### 6. Stats Grid

```javascript
let slide = pres.addSlide();

slide.addText("Impact & Learnings", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: '1E2761'
});

// Stat 1
slide.addText("50+", {
  x: 0.5, y: 1.8, w: 3, h: 1,
  fontSize: 72, bold: true, color: '028090', align: 'center'
});
slide.addText("GIT COMMITS", {
  x: 0.5, y: 2.9, w: 3, h: 0.4,
  fontSize: 14, color: '808080', align: 'center', charSpacing: 2
});

// Stat 2 (x: 3.5)
// Stat 3 (x: 6.5)
// [Repeat pattern]

// Quote below
slide.addShape(pres.shapes.RECTANGLE, {
  x: 1, y: 3.8, w: 8, h: 1.2,
  fill: { color: '1E2761', transparency: 10 },
  line: { color: '1E2761', width: 2 }
});
slide.addText(""Building fast is easy. The real work is relentless iteration."", {
  x: 1.3, y: 4, w: 7.4, h: 0.8,
  fontSize: 18, italic: true, color: '1E2761', align: 'center'
});
```

---

### 7. Key Takeaway (Closing)

```javascript
let slide = pres.addSlide();
slide.background = { color: '028090' };  // Accent color background

slide.addText("Key Takeaway", {
  x: 0.5, y: 1.5, w: 9, h: 0.6,
  fontSize: 32, bold: true, color: 'FFFFFF', align: 'center'
});

slide.addText("Ship fast, iterate relentlessly, capture learnings.", {
  x: 1, y: 2.5, w: 8, h: 1.5,
  fontSize: 28, bold: true, color: 'FFFFFF', align: 'center', valign: 'middle'
});
```

---

### 8. Q&A Slide

```javascript
let slide = pres.addSlide();

slide.addText("?", {
  x: 4.5, y: 1.5, w: 1, h: 1,
  fontSize: 120, bold: true, color: '1E2761', align: 'center'
});

slide.addText("Questions?", {
  x: 0.5, y: 3, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: '1E2761', align: 'center'
});

slide.addText("your.email@example.com", {
  x: 0.5, y: 4.5, w: 9, h: 0.3,
  fontSize: 14, color: '808080', align: 'center'
});
```

---

## Spacing Rules

### Margins
- **Slide edges**: 0.5" minimum from all sides
- **Between sections**: 0.3-0.5" gaps
- **Text box padding**: Set `margin: 0` when aligning with shapes

### Positioning (16:9 layout)

Slide dimensions: **10" × 5.625"**

```
Safe zones:
- X: 0.5" to 9.5" (9" wide content area)
- Y: 0.5" to 5.125" (4.625" tall content area)

Typical positions:
- Title: y: 0.5
- Content start: y: 1.3 or 1.5
- Footer/source: y: 5.0 or 5.2
```

---

## Common Mistakes to Avoid

### ❌ Don't Do This

- **Text-only slides** - Add visuals!
- **Low contrast** - Light text on light bg, dark icons on dark bg
- **Centered body text** - Left-align paragraphs and lists
- **Accent lines under titles** - This screams "AI-generated"
- **Equal color weight** - One color should dominate
- **Random spacing** - Be consistent (0.3" or 0.5" gaps)
- **Tiny text** - Body text minimum 14pt
- **No text box margin consideration** - Set `margin: 0` when aligning

### ✅ Do This Instead

- **Every slide has a visual** - Image, chart, icon, shape
- **High contrast** - Dark text on light, light text on dark
- **Left-align body text** - Easier to scan
- **Use whitespace or background color** - No accent lines
- **One dominant color** - 60-70% visual weight
- **Consistent spacing** - Pick 0.3" or 0.5", use everywhere
- **Readable fonts** - Body 14-16pt, titles 36-44pt
- **Plan for padding** - Text boxes have internal margins

---

## Visual Hierarchy Checklist

- [ ] Title stands out (36-44pt, bold, color)
- [ ] Body text is readable (14-16pt, high contrast)
- [ ] Consistent spacing (0.5" margins, 0.3-0.5" gaps)
- [ ] Visual element on every slide
- [ ] One dominant color (60-70% weight)
- [ ] Left-aligned paragraphs/lists
- [ ] No accent lines under titles
- [ ] High contrast text and icons

---

## Resources

- **Marketplace pptx skill**: `~/.claude/skills/marketplace/pptx/SKILL.md`
  - Full design ideas, color palettes, common mistakes
- **pptxgenjs docs**: https://gitbrent.github.io/PptxGenJS/
- **User's design system**: `~/claude/design-system/index.html`
  - Can reference for color/spacing consistency
