---
name: research-report
description: |
  Create professional HTML research reports with Tier-classified sources, confidence levels, and consistent formatting. Use when converting research findings into publication-ready reports for ~/claude/_report/ or ~/claude/_invest/ projects.
---

# Research Report Skill

## When to Use

Use this skill when you need to:
- Convert research findings into HTML reports
- Apply consistent formatting and structure
- Classify sources by tier (Tier 1/2/3)
- Display confidence levels (HIGH/MEDIUM/LOW)
- Create publication-ready research documents

**Trigger**: "Create a research report on [topic]" or after research data collection is complete.

---

## Core Principles

1. **Evidence-based**: All claims must have sources
2. **Tier classification**: Sources must be evaluated (Tier 1/2/3)
3. **Confidence transparency**: Display confidence levels clearly
4. **Counterarguments**: Include opposing views
5. **User confirmation**: Get approval before generating HTML

---

## Workflow

### Phase 1: Research Completion Check

**Before starting report creation**:
- [ ] Research data collected (via `/research` skill or manual)
- [ ] Sources identified and URLs documented
- [ ] Counterarguments included
- [ ] Key findings summarized

### Phase 2: Source Evaluation

**Classify all sources using `references/source-tiers.md`**:

- 🟢 **Tier 1**: Academic papers, government data, primary sources
- 🔵 **Tier 2**: Industry reports, expert analysis, reputable journalism
- ⚫ **Tier 3**: Company blogs, opinion pieces, aggregated content

**Determine confidence levels**:
- 🟢 **HIGH**: Multiple Tier 1 sources agree
- 🟡 **MEDIUM**: Single Tier 1 or multiple Tier 2 sources
- 🔴 **LOW**: Tier 3 only or insufficient evidence

### Phase 3: Report Structure

**Use template from `~/claude/design-system/research-report-template.html`**:

```
1. Header (Title, subtitle, metadata)
2. Executive Summary (2-3 sentences)
3. Table of Contents (auto-linked)
4. Introduction
5. Background & Context
6. Analysis
7. Key Findings
8. Implications
9. Conclusion
10. References (Tier-classified)
```

### Phase 4: Content Assembly

**For each section**:
- Write clear, concise content
- Add in-text citations: `<a href="#ref1" class="citation">[1]</a>`
- Include confidence badges where appropriate
- Add callouts for key findings
- Include tables/data where relevant

**Counterarguments section**:
```html
<div class="callout callout-danger">
  <h4>⚠️ Alternative Perspectives</h4>
  <p>Not all sources agree. Some researchers argue...<a href="#ref6" class="citation">[6]</a></p>
  <p><strong>Response:</strong> While these concerns are valid...</p>
</div>
```

### Phase 5: Reference Formatting

**Format each reference with Tier badge**:

```html
<div class="reference-item" id="ref1">
  <span class="reference-number">[1]</span>
  Smith, J. (2024). "Paper Title." <em>Journal Name</em>, 45(3), 123-145.
  <span class="reference-tier tier1">Tier 1</span>
  <br><small>DOI: 10.1234/example</small>
</div>
```

### Phase 6: Quality Check

**Before finalizing**:
- [ ] All claims have citations
- [ ] All sources are Tier-classified
- [ ] Confidence levels displayed where needed
- [ ] Counterarguments included
- [ ] Minimum 10 references (for comprehensive reports)
- [ ] Executive summary complete
- [ ] No broken citation links

### Phase 7: User Confirmation

**IMPORTANT**: Present findings in Markdown first:
```markdown
# [Topic] Research Report
## Key Findings
- Finding 1 (HIGH confidence, 5 Tier 1 sources)
- Finding 2 (MEDIUM confidence, 1 Tier 1 + 3 Tier 2)
- Finding 3 (LOW confidence, Tier 3 only)

## Sources Summary
- Tier 1: 15 sources
- Tier 2: 18 sources
- Tier 3: 9 sources
```

**Get user approval before generating HTML**

### Phase 8: HTML Generation

**Once approved**:
1. Copy `~/claude/design-system/research-report-template.html`
2. Save to appropriate location:
   - Investment topics: `~/claude/_invest/[topic]-report/index.html`
   - General research: `~/claude/_report/[topic]-report/index.html`
3. Fill in all sections with researched content
4. Apply Tier badges and confidence levels
5. Test in browser (check citations, TOC links)

---

## Quick Reference

### Confidence Badges

```html
<div class="confidence confidence-high">
  🟢 HIGH CONFIDENCE: Based on 15+ Tier 1 sources
</div>

<div class="confidence confidence-medium">
  🟡 MEDIUM CONFIDENCE: Single Tier 1 source
</div>

<div class="confidence confidence-low">
  🔴 LOW CONFIDENCE: Tier 3 only, requires verification
</div>
```

### Source Tier Badges

```html
<span class="reference-tier tier1">Tier 1</span>
<span class="reference-tier tier2">Tier 2</span>
<span class="reference-tier tier3">Tier 3</span>
```

### Callouts

```html
<!-- Key Finding -->
<div class="callout">
  <h4>🎯 Key Finding</h4>
  <p>Content...</p>
</div>

<!-- Success/Positive -->
<div class="callout callout-success">
  <h4>✅ Confirmed</h4>
  <p>Content...</p>
</div>

<!-- Warning/Counterargument -->
<div class="callout callout-danger">
  <h4>⚠️ Alternative Perspectives</h4>
  <p>Content...</p>
</div>
```

---

## Reference Files

- **Source evaluation**: `references/source-tiers.md`
  - Tier definitions
  - Evaluation criteria
  - Cross-verification methods
  - Confidence level guidelines

- **Templates guide**: `references/templates.md`
  - HTML template location
  - Step-by-step usage
  - Project structure
  - Quality checklist

---

## Output Locations

| Report Type | Location |
|-------------|----------|
| Investment/Finance | `~/claude/_invest/[topic]-report/` |
| Technology | `~/claude/_report/[topic]-report/` |
| Health/Medical | `~/claude/_report/[topic]-report/` |
| General Research | `~/claude/_report/[topic]-report/` |

---

## Common Mistakes to Avoid

- ❌ Generating HTML without user confirmation
- ❌ Missing Tier classification on sources
- ❌ No confidence levels displayed
- ❌ Omitting counterarguments
- ❌ Broken citation links
- ❌ Using Tier 3 sources for key conclusions
- ❌ No executive summary

---

## Example Usage

**User request**: "Create a research report on AI trends 2026"

```
1. Check: Research data ready? ✓
2. Classify sources:
   - OpenAI paper (Tier 1)
   - Gartner report (Tier 2)
   - TechCrunch article (Tier 3)
3. Determine confidence:
   - Finding 1: HIGH (3 Tier 1 sources)
   - Finding 2: MEDIUM (1 Tier 1, 2 Tier 2)
4. Draft Markdown summary → User confirms ✓
5. Generate HTML from template
6. Save to ~/claude/_report/ai-trends-2026/index.html
7. Test in browser
```

---

## Integration with /research Skill

This skill complements `/research`:
- `/research` → Data collection, multi-agent analysis
- `research-report` → Format into HTML, apply styling, classify sources

**Workflow**:
```
User request
  ↓
/research skill (data gathering)
  ↓
Markdown findings
  ↓
User confirmation
  ↓
research-report skill (HTML generation) ← YOU ARE HERE
  ↓
Published report
```
