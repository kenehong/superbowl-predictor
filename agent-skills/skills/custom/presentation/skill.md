---
name: presentation
description: |
  Analyze project work history and generate professional PowerPoint presentations (.pptx) with speaker scripts. Parses git commits, project logs, and code to create compelling story-driven presentations for demos, pitches, or retrospectives.
---

# Presentation Skill

## When to Use

Use this skill when you need to:
- Create PowerPoint slides from completed projects
- Generate speaker scripts for demos or pitches
- Analyze project journey and technical decisions
- Prepare retrospectives or case studies
- Document project for portfolio presentations

**Trigger**: "Create a presentation for [project]" or "Generate slides for [project]"

---

## Core Principles

1. **Story-driven**: Every presentation tells a coherent story (Problem → Solution → Impact)
2. **Evidence-based**: Use actual git history, logs, and code as proof points
3. **Visual**: Include data visualizations, icons, and visual hierarchy
4. **Actionable**: Provide ready-to-use .pptx + speaker scripts
5. **Professional**: Follow design best practices (color, typography, spacing)

---

## Dependencies

**Required**:
```bash
npm install -g pptxgenjs
pip install "markitdown[pptx]"
pip install Pillow
```

**For visual QA** (optional but recommended):
```bash
# LibreOffice for PDF conversion
brew install --cask libreoffice  # Mac
# or sudo apt-get install libreoffice  # Linux

# Poppler for PDF to images
brew install poppler  # Mac
# or sudo apt-get install poppler-utils  # Linux
```

---

## Workflow

### Phase 1: Project Discovery

**Gather all available project data**:
- [ ] Git commit history (timeline, key iterations)
- [ ] `project-log.md` or `LEARNINGS.md` (if exists)
- [ ] Dev Story documents (if exists)
- [ ] README and documentation
- [ ] Screenshots or assets
- [ ] Tech stack (from code/config files)

**Commands to run**:
```bash
# Git analysis
cd project-folder/
git log --oneline --all
git log --pretty=format:"%ci - %s" --reverse
git rev-list --count HEAD

# File discovery
ls -la
cat project-log.md 2>/dev/null
cat README.md 2>/dev/null
find . -name "*.png" -o -name "*.jpg" | head -5
```

### Phase 2: Story Structure Selection

**Choose the appropriate narrative** (see `references/story-structures.md`):

1. **Problem-Solution** (most common)
   - For product demos, case studies, portfolio

2. **Journey/Timeline** (for retrospectives)
   - For team updates, progress reports

3. **Technical Deep-Dive** (for technical audiences)
   - For architecture reviews, engineering talks

4. **Demo-Driven** (for product showcases)
   - For launches, investor pitches

### Phase 3: Slide Outline Generation

**Create presentation outline** (7-12 slides typical):

```
1. Title Slide
   - Project name, tagline, presenter, date

2. The Hook (Problem/Opportunity)
   - What problem exists? Why it matters

3. The Solution
   - What we built, 3-4 key features

4. Technical Approach (optional for technical audiences)
   - Tech stack, key decisions, challenges

5. The Journey
   - Timeline from git, major iterations

6. Demo/Screenshots
   - Visual proof, key user flows

7. Impact & Learnings
   - Metrics, key takeaways

8. Key Takeaway
   - One memorable sentence

9. Q&A
```

**Present outline to user for approval before generating**

### Phase 4: Design Selection

**Choose design theme** (see `references/pptx-design.md`):

From marketplace pptx skill design ideas:
- Color palette matching project theme
- Typography pairing (header + body fonts)
- Layout patterns (two-column, icon grids, etc.)
- Visual motifs (rounded corners, colored circles, etc.)

**Default theme for code projects**:
- **Colors**: Midnight Executive (navy `1E2761`, ice blue `CADCFC`, white)
- **Fonts**: Arial Bold (headers), Calibri (body)
- **Layout**: 16:9, clean, generous spacing

### Phase 5: Generate PPTX with pptxgenjs

**Create presentation script**:

```javascript
const pptxgen = require("pptxgenjs");

let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';
pres.author = 'Your Name';
pres.title = 'Project Name';

// Slide 1: Title
let slide1 = pres.addSlide();
slide1.background = { color: '1E2761' };
slide1.addText("Project Name", {
  x: 0.5, y: 2.0, w: 9, h: 1,
  fontSize: 44, bold: true, color: 'FFFFFF', align: 'center'
});
slide1.addText("One-liner description", {
  x: 0.5, y: 3.0, w: 9, h: 0.5,
  fontSize: 20, color: 'CADCFC', align: 'center'
});

// More slides...

pres.writeFile({ fileName: "presentation.pptx" });
```

**Save to project folder**:
```
project-folder/
├── presentation/
│   ├── presentation.pptx
│   ├── generate.js (pptxgenjs script)
│   ├── script.md (speaker notes)
│   └── assets/ (screenshots, if any)
```

### Phase 6: Content Guidelines

**For each slide**:

- **Text**: Max 6 lines, 14-16pt body text
- **Titles**: 36-44pt, bold, navy color
- **Layout**: Use grids (2-column, 3-column, 2x2)
- **Visuals**: Every slide needs a visual element
- **Spacing**: 0.5" margins, 0.3-0.5" between elements
- **Icons**: Use emoji or shapes (colored circles with text)

**Avoid**:
- Text-only slides
- Low contrast (light text on light backgrounds)
- Centered body text (left-align paragraphs)
- Accent lines under titles (AI hallmark)
- Leftover placeholder text

### Phase 7: Quality Assurance

**CRITICAL: Always run QA before delivering**

**Content QA**:
```bash
python -m markitdown presentation.pptx

# Check for placeholder text
python -m markitdown presentation.pptx | grep -iE "xxxx|lorem|ipsum|placeholder"
```

**Visual QA** (recommended):
```bash
# Convert to PDF then images
cd ~/agent-skills/skills/marketplace/pptx
python scripts/office/soffice.py --headless --convert-to pdf /path/to/presentation.pptx
pdftoppm -jpeg -r 150 presentation.pdf slide

# Inspect slide-01.jpg, slide-02.jpg, etc.
```

**Use subagent for visual inspection**:
- Check for overlapping elements
- Verify text isn't cut off
- Ensure consistent spacing
- Confirm sufficient contrast
- Look for alignment issues

**Iterate until clean**: Fix issues → Re-generate → Re-verify

### Phase 8: Speaker Script Generation

**Create detailed script** (`templates/script-template.md`):

```markdown
# Slide 1: Title [30 sec]

**On Screen**: Project name + tagline

**Say**: "Hi everyone, I'm [name]. Today I'm presenting [project]..."

**Notes**: Pause after intro, make eye contact
```

Include:
- Timing per slide (30-90 sec each)
- What to say (conversational, not reading bullets)
- Presenter notes (reminders, anecdotes)
- Expected Q&A with answers

### Phase 9: Delivery

**Final deliverables**:
```
project-folder/presentation/
├── presentation.pptx (Open in PowerPoint/Keynote/Google Slides)
├── generate.js (pptxgenjs source code, for edits)
├── script.md (Speaker script with timing)
└── assets/ (Images/screenshots used)
```

**Usage instructions for user**:
```
To present:
1. Open presentation.pptx in PowerPoint, Keynote, or Google Slides
2. Enter Presenter Mode (Keynote: Option+Return, PowerPoint: Slideshow → Presenter View)
3. Use script.md as reference for talking points

To edit:
1. Open presentation.pptx directly in PowerPoint/Keynote
2. Click and edit text, drag elements, change colors
3. Or modify generate.js and re-run: node generate.js

To share:
- Email the .pptx file (works everywhere)
- Or export to PDF for read-only sharing
```

---

## Analysis Guidelines

### Git History Analysis

**Extract**:
- Total commits: `git rev-list --count HEAD`
- Timeline: `git log --pretty=format:"%ci - %s" --reverse`
- Duration: First commit date → Last commit date
- Key iterations: Cluster commits by message patterns

**Example parsing**:
```bash
# Get commit timeline
git log --oneline | wc -l  # Total commits
git log --pretty=format:"%ci" | head -1  # First commit date
git log --pretty=format:"%ci" -n 1  # Last commit date

# Find key milestones
git log --oneline | grep -iE "initial|refactor|add|fix"
```

### Project Log Analysis

**Look for**:
- Stated goals ("Why we built this")
- Timeline markers ("10-15 min", "Phase 1")
- Key learnings ("The real work is...")
- Challenges overcome
- Success metrics

**Extract quotes** for slides:
- Problem statements → Slide 2
- Key learnings → Slide 7
- Memorable quotes → Slide 8

### Screenshot Collection

**Find existing screenshots**:
```bash
find project-folder/ -name "*.png" -o -name "*.jpg"
```

**If no screenshots exist**:
- Note in script.md: "Add screenshot here"
- Or take screenshots manually before presenting
- For web apps: Use browser dev tools screenshot feature

---

## Presentation Length Templates

### 3-Minute Lightning Talk
```
6 slides total
- Title (15s)
- Problem (45s)
- Solution (60s)
- Demo (45s)
- Takeaway (15s)
```

### 5-Minute Demo
```
8 slides total
- Title (20s)
- Problem (40s)
- Solution (60s)
- Technical Approach (60s)
- Journey (60s)
- Impact (40s)
- Takeaway (20s)
- Q&A (20s)
```

### 10-Minute Deep Dive
```
10-12 slides total
- Title (30s)
- Problem (90s)
- Solution (90s)
- Technical Approach (120s)
- Journey (90s)
- Demo (90s)
- Impact & Learnings (60s)
- Takeaway (30s)
- Q&A (120s)
```

---

## Reference Files

- **Story structures**: `references/story-structures.md`
  - Problem-Solution, Journey, Technical Deep-Dive, Demo-Driven narratives

- **PPTX design guide**: `references/pptx-design.md`
  - Color palettes, typography, layouts
  - Based on marketplace pptx skill design ideas

- **pptxgenjs examples**: `references/pptxgenjs-examples.md`
  - Common slide patterns (title, two-column, stats grid, etc.)
  - Code snippets for each layout

- **Script template**: `templates/script-template.md`
  - Slide-by-slide talking points
  - Timing guidelines, presenter notes, Q&A prep

---

## Common Mistakes to Avoid

- ❌ No QA (assume there are issues, find them)
- ❌ Text-only slides (add visuals!)
- ❌ Generating without user outline approval
- ❌ Low contrast text/icons
- ❌ Too much text per slide (max 6 lines)
- ❌ Centered body text (left-align!)
- ❌ Accent lines under titles (AI hallmark)
- ❌ Skipping speaker script (winging it = disaster)
- ❌ No timing rehearsal

---

## Example Usage

**User request**: "Create a presentation for superbowl project"

```
Phase 1: Discovery
  - cd ~/claude/_game/superbowl
  - git log --oneline (9 commits) ✓
  - cat project-log.md ✓
  - find screenshots (main-view.png) ✓
  - Tech: HTML/JS, ESPN API, localStorage ✓

Phase 2: Story Structure
  - Choose: Problem-Solution ✓
  - Audience: General ✓

Phase 3: Outline (9 slides)
  1. Title: Super Bowl LX Predictor
  2. Why: Paper predictions are messy
  3. Solution: Live scores, auto-ranking, persistence
  4. Tech: Accuracy algorithm
  5. Journey: 15min → 30min → 1-2hrs
  6. Iterations: 6 key improvements from git
  7. Demo: Screenshot
  8. Impact: Stats + quote
  9. Takeaway + Q&A

Phase 4: Design
  - Midnight Executive theme (navy/ice blue)
  - Arial Bold + Calibri
  - 16:9 layout

Phase 5: Generate
  - Create generate.js with pptxgenjs ✓
  - Run: node generate.js ✓
  - Output: presentation.pptx ✓

Phase 6: QA
  - python -m markitdown presentation.pptx ✓
  - Convert to images, visual inspection ✓
  - Fix issues (if any) ✓

Phase 7: Script
  - Generate script.md with timing ✓
  - Include 8 expected Q&A ✓

Phase 8: Deliver
  - Save to ~/claude/_game/superbowl/presentation/ ✓
```

---

## Integration with Other Skills

This skill complements:
- `/research` → Present research findings as slides
- `technical-writer` agent → Document project, then present
- Marketplace `pptx` skill → Can use its scripts for advanced editing

**Workflow**:
```
Build project
  ↓
Document in project-log.md
  ↓
/presentation skill (generate slides) ← YOU ARE HERE
  ↓
Present/pitch to audience
  ↓
(Optional) Edit .pptx in PowerPoint for refinements
```

---

## Output Locations

| Project Type | Location |
|-------------|----------|
| Tools | `~/claude/_tool/[project]/presentation/` |
| Games | `~/claude/_game/[project]/presentation/` |
| Work | `~/claude/_work/[project]/presentation/` |
| Investment | `~/claude/_invest/[project]/presentation/` |
| General | `~/claude/[project]/presentation/` |

---

## Future Enhancements

- [ ] Auto-capture screenshots from running web apps
- [ ] Generate presenter notes inside .pptx (not just script.md)
- [ ] Support for animations and transitions
- [ ] PDF export automation
- [ ] LinkedIn summary post generation from slides
