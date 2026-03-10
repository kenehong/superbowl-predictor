# pptxgenjs Code Examples

Complete code snippets for common presentation slides.

---

## Setup Boilerplate

```javascript
const pptxgen = require("pptxgenjs");

// Create presentation
let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';  // 10" × 5.625"
pres.author = 'Your Name';
pres.title = 'Presentation Title';
pres.subject = 'Project Demo';

// Define color palette (reuse across slides)
const colors = {
  primary: '1E2761',    // Navy
  secondary: 'CADCFC',  // Ice blue
  accent: 'FFFFFF',     // White
  text: '363636',       // Dark gray
  textLight: '808080'   // Light gray
};

// ... Add slides ...

// Save
pres.writeFile({ fileName: "presentation.pptx" });
console.log("✅ Presentation created: presentation.pptx");
```

---

## Slide 1: Title Slide

```javascript
let slide1 = pres.addSlide();
slide1.background = { color: colors.primary };

// Project name
slide1.addText("Super Bowl LX Predictor", {
  x: 0.5, y: 2.0, w: 9, h: 1,
  fontSize: 44, bold: true, color: colors.accent, align: 'center'
});

// Tagline
slide1.addText("A vibe coding experiment in rapid iteration", {
  x: 0.5, y: 3.0, w: 9, h: 0.5,
  fontSize: 20, color: colors.secondary, align: 'center', italic: true
});

// Metadata
slide1.addText("Kenny Hong • February 2026", {
  x: 0.5, y: 4.8, w: 9, h: 0.3,
  fontSize: 12, color: colors.secondary, align: 'center'
});
```

---

## Slide 2: Problem Slide with Callout

```javascript
let slide2 = pres.addSlide();

// Title
slide2.addText("The Problem", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.primary, margin: 0
});

// Callout box background
slide2.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.3, w: 9, h: 3.5,
  fill: { color: colors.secondary, transparency: 70 },
  line: { color: colors.primary, width: 2 }
});

// Problem statement (bold)
slide2.addText("Super Bowl parties are fun, but tracking predictions on paper is messy", {
  x: 0.7, y: 1.5, w: 8.6, h: 0.8,
  fontSize: 20, bold: true, color: colors.primary
});

// Pain points (bullets)
slide2.addText([
  { text: "Manual score checking interrupts the game 📝", options: { bullet: true, breakLine: true } },
  { text: "Paper predictions get lost or disputed 🤷", options: { bullet: true, breakLine: true } },
  { text: "No easy way to see live rankings 📊", options: { bullet: true } }
], {
  x: 0.7, y: 2.5, w: 8.6, h: 2,
  fontSize: 16, color: colors.text
});
```

---

## Slide 3: Three-Column Features

```javascript
let slide3 = pres.addSlide();

slide3.addText("The Solution", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.primary, margin: 0
});

// Feature boxes configuration
const features = [
  { emoji: "🎯", title: "Live Scores", desc: "ESPN API integration for real-time game updates", x: 0.7 },
  { emoji: "⚡", title: "Auto Ranking", desc: "Smart scoring algorithm ranks predictions by accuracy", x: 3.6 },
  { emoji: "🚀", title: "Persistence", desc: "localStorage saves everything — no backend needed", x: 6.5 }
];

features.forEach(feature => {
  // Background card
  slide3.addShape(pres.shapes.RECTANGLE, {
    x: feature.x, y: 1.5, w: 2.6, h: 3.0,
    fill: { color: 'F8F9FA' },
    line: { width: 0 }
  });

  // Icon circle
  slide3.addShape(pres.shapes.OVAL, {
    x: feature.x + 0.8, y: 1.8, w: 1, h: 1,
    fill: { color: '028090' }
  });

  // Emoji
  slide3.addText(feature.emoji, {
    x: feature.x + 0.95, y: 2.05, w: 0.7, h: 0.5,
    fontSize: 32, align: 'center'
  });

  // Title
  slide3.addText(feature.title, {
    x: feature.x + 0.1, y: 3.0, w: 2.4, h: 0.4,
    fontSize: 18, bold: true, color: colors.primary, align: 'center'
  });

  // Description
  slide3.addText(feature.desc, {
    x: feature.x + 0.1, y: 3.5, w: 2.4, h: 0.8,
    fontSize: 13, color: colors.text, align: 'center'
  });
});
```

---

## Slide 4: Code Snippet

```javascript
let slide4 = pres.addSlide();

slide4.addText("Technical Approach", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.primary, margin: 0
});

// Code background
slide4.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.3, w: 9, h: 3.2,
  fill: { color: '2C2C2C' }
});

// Code text
slide4.addText([
  { text: "// Calculate prediction accuracy\n", options: { color: '6A9955', breakLine: true } },
  { text: "function calculateAccuracy(prediction, actual) {\n", options: { color: 'DCDCAA', breakLine: true } },
  { text: "  const totalDistance = ", options: { color: 'D4D4D4' } },
  { text: "Math.abs", options: { color: '4EC9B0' } },
  { text: "(pred - actual);\n", options: { color: 'D4D4D4', breakLine: true } },
  { text: "\n  ", options: { breakLine: true } },
  { text: "// Penalize wrong winner prediction\n", options: { color: '6A9955', breakLine: true } },
  { text: "  const wrongWinner = (pred.winner !== actual.winner);\n", options: { color: 'D4D4D4', breakLine: true } },
  { text: "  return wrongWinner ? totalDistance + ", options: { color: 'D4D4D4' } },
  { text: "100", options: { color: 'B5CEA8' } },
  { text: " : totalDistance;\n", options: { color: 'D4D4D4', breakLine: true } },
  { text: "}", options: { color: 'DCDCAA' } }
], {
  x: 0.7, y: 1.5, w: 8.6, h: 2.8,
  fontSize: 13, fontFace: 'Courier New'
});

// Caption
slide4.addText("Smart scoring: proximity + winner penalty", {
  x: 0.5, y: 4.8, w: 9, h: 0.3,
  fontSize: 12, italic: true, color: colors.textLight, align: 'center'
});
```

---

## Slide 5: Timeline

```javascript
let slide5 = pres.addSlide();

slide5.addText("The Journey", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.primary, margin: 0
});

// Timeline items
const timeline = [
  { time: "10-15 min", desc: "Core functional — Prediction form, scoring, API, leaderboard", y: 1.5 },
  { time: "+30 min", desc: "Design polish — UI improvements, styling, responsive layout", y: 2.5 },
  { time: "+1-2 hrs", desc: "Iteration hell — Edge cases, game rules, UX refinement", y: 3.5 }
];

timeline.forEach(item => {
  // Background bar
  slide5.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: item.y, w: 9, h: 0.8,
    fill: { color: colors.secondary, transparency: 40 },
    line: { color: '028090', width: 3, dashType: 'solid' }
  });

  // Time label
  slide5.addText(item.time, {
    x: 0.7, y: item.y + 0.15, w: 1.5, h: 0.5,
    fontSize: 16, bold: true, color: '028090'
  });

  // Description
  slide5.addText(item.desc, {
    x: 2.5, y: item.y + 0.15, w: 6.5, h: 0.5,
    fontSize: 14, color: colors.text
  });
});

// Summary
slide5.addText("Total: ~2 hours | 9 commits | 6 major iterations", {
  x: 0.5, y: 4.8, w: 9, h: 0.3,
  fontSize: 12, italic: true, color: colors.textLight, align: 'center'
});
```

---

## Slide 6: Bullet List with Icons

```javascript
let slide6 = pres.addSlide();

slide6.addText("Key Iterations", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.primary, margin: 0
});

// Iterations with checkmarks
const iterations = [
  "Simplify UI & scoring — Less is more",
  "Unsaved input confirmation — Don't lose work",
  "Prevent tie predictions — Super Bowl can't tie!",
  "Hide winner at 0:0 — Don't show nonsense",
  "Rankings only when scores exist — Context matters"
];

iterations.forEach((text, i) => {
  const y = 1.5 + (i * 0.65);

  // Checkmark circle
  slide6.addShape(pres.shapes.OVAL, {
    x: 0.7, y: y, w: 0.4, h: 0.4,
    fill: { color: '28A745' }
  });
  slide6.addText("✓", {
    x: 0.75, y: y + 0.05, w: 0.3, h: 0.3,
    fontSize: 20, bold: true, color: colors.accent, align: 'center'
  });

  // Text
  slide6.addText(text, {
    x: 1.3, y: y + 0.05, w: 8, h: 0.35,
    fontSize: 16, color: colors.text
  });
});
```

---

## Slide 7: Screenshot/Image

```javascript
let slide7 = pres.addSlide();

slide7.addText("What It Looks Like", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.primary, margin: 0
});

// Image (if available)
slide7.addImage({
  path: "../screenshots/main-view.png",
  x: 1, y: 1.5, w: 8, h: 3.2
});

// Caption
slide7.addText("Clean UI, live scores, auto-ranked leaderboard with confetti 🎉", {
  x: 0.5, y: 5.0, w: 9, h: 0.3,
  fontSize: 12, italic: true, color: colors.textLight, align: 'center'
});
```

**Note**: If screenshot doesn't exist, replace with text description or remove image line.

---

## Slide 8: Stats Grid

```javascript
let slide8 = pres.addSlide();

slide8.addText("Impact & Learnings", {
  x: 0.5, y: 0.5, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.primary, margin: 0
});

// Stats
const stats = [
  { number: "2", label: "HOURS", x: 0.7 },
  { number: "9", label: "COMMITS", x: 3.7 },
  { number: "6", label: "ITERATIONS", x: 6.7 }
];

stats.forEach(stat => {
  // Big number
  slide8.addText(stat.number, {
    x: stat.x, y: 1.8, w: 2.6, h: 1,
    fontSize: 72, bold: true, color: '028090', align: 'center'
  });

  // Label
  slide8.addText(stat.label, {
    x: stat.x, y: 2.9, w: 2.6, h: 0.4,
    fontSize: 14, color: colors.textLight, align: 'center', charSpacing: 2
  });
});

// Quote box
slide8.addShape(pres.shapes.RECTANGLE, {
  x: 1, y: 3.8, w: 8, h: 1.2,
  fill: { color: colors.primary, transparency: 90 },
  line: { color: colors.primary, width: 2 }
});

slide8.addText(""Building something functional is fast. The real work is relentless iteration."", {
  x: 1.3, y: 4, w: 7.4, h: 0.8,
  fontSize: 18, italic: true, color: colors.primary, align: 'center', valign: 'middle'
});
```

---

## Slide 9: Key Takeaway (Colored Background)

```javascript
let slide9 = pres.addSlide();
slide9.background = { color: '028090' };  // Teal accent

slide9.addText("Key Takeaway", {
  x: 0.5, y: 1.5, w: 9, h: 0.6,
  fontSize: 32, bold: true, color: colors.accent, align: 'center'
});

slide9.addText("Ship fast, simulate relentlessly, capture learnings.", {
  x: 1, y: 2.5, w: 8, h: 1.5,
  fontSize: 28, bold: true, color: colors.accent, align: 'center', valign: 'middle'
});
```

---

## Slide 10: Q&A

```javascript
let slide10 = pres.addSlide();

// Giant question mark
slide10.addText("?", {
  x: 4.5, y: 1.5, w: 1, h: 1,
  fontSize: 120, bold: true, color: colors.primary, align: 'center'
});

// Questions?
slide10.addText("Questions?", {
  x: 0.5, y: 3, w: 9, h: 0.6,
  fontSize: 36, bold: true, color: colors.primary, align: 'center'
});

// Contact info
slide10.addText("GitHub: ~/claude/_game/superbowl", {
  x: 0.5, y: 4.5, w: 9, h: 0.3,
  fontSize: 14, color: colors.textLight, align: 'center'
});
```

---

## Complete Example Script

Save as `generate.js`:

```javascript
const pptxgen = require("pptxgenjs");

// Create presentation
let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';
pres.author = 'Kenny Hong';
pres.title = 'Super Bowl LX Predictor';

// Color palette
const colors = {
  primary: '1E2761',
  secondary: 'CADCFC',
  accent: 'FFFFFF',
  text: '363636',
  textLight: '808080'
};

// Slide 1: Title
let slide1 = pres.addSlide();
slide1.background = { color: colors.primary };
slide1.addText("Super Bowl LX Predictor", {
  x: 0.5, y: 2.0, w: 9, h: 1,
  fontSize: 44, bold: true, color: colors.accent, align: 'center'
});
slide1.addText("A vibe coding experiment", {
  x: 0.5, y: 3.0, w: 9, h: 0.5,
  fontSize: 20, color: colors.secondary, align: 'center', italic: true
});
slide1.addText("Kenny Hong • February 2026", {
  x: 0.5, y: 4.8, w: 9, h: 0.3,
  fontSize: 12, color: colors.secondary, align: 'center'
});

// ... Add more slides (use examples above) ...

// Save
pres.writeFile({ fileName: "presentation.pptx" });
console.log("✅ Presentation created: presentation.pptx");
```

**Run**:
```bash
node generate.js
```

---

## Tips

### Text Alignment
- **Titles**: `margin: 0` to align with other elements
- **Bullets**: Use `bullet: true` + `breakLine: true`
- **Multi-line**: Use text arrays with `breakLine: true`

### Colors
- **No `#` prefix**: Use `1E2761` not `#1E2761`
- **Transparency**: 0-100 (0 = opaque, 100 = fully transparent)

### Positioning
- **16:9 layout**: 10" wide × 5.625" tall
- **Safe zones**: x: 0.5-9.5, y: 0.5-5.125
- **Consistent spacing**: 0.3" or 0.5" gaps

### Common Mistakes
- ❌ Unicode bullets (`• Text`) → Use `bullet: true`
- ❌ Forgetting `breakLine: true` → Multi-line won't work
- ❌ Using `#` in colors → Just hex digits
- ❌ Not setting `margin: 0` → Text won't align with shapes

---

## Resources

- **pptxgenjs docs**: https://gitbrent.github.io/PptxGenJS/
- **Marketplace pptx examples**: `~/.claude/skills/marketplace/pptx/pptxgenjs.md`
