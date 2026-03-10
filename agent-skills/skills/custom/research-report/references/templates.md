# Project Templates Guide

프로젝트 유형별 템플릿과 사용 가이드입니다.

## 📍 Template Locations

### Design System
```
~/claude/design-system/
├── index.html                       # Component library
└── research-report-template.html    # Research report template
```

**용도**: 모든 앱과 리포트의 기본 스타일

---

## 🎨 Design System

### Quick Reference

**Colors**:
```css
--primary: #0d6efd    /* Blue - actions */
--success: #198754    /* Green - success */
--danger: #dc3545     /* Red - errors */
--warning: #ffc107    /* Yellow - warnings */
```

**Typography**:
```css
--font-sans: -apple-system, BlinkMacSystemFont, 'Pretendard', 'Segoe UI', Roboto, sans-serif
--font-mono: 'SF Mono', Consolas, 'Liberation Mono', monospace
```

**Spacing** (4px base):
```css
--space-1: 0.25rem   /* 4px */
--space-2: 0.5rem    /* 8px */
--space-4: 1rem      /* 16px */
--space-6: 1.5rem    /* 24px */
--space-8: 2rem      /* 32px */
```

**Components**:
```css
--radius: 0.5rem     /* 8px border radius */
--shadow: 0 1px 3px rgba(0,0,0,0.1)
```

### Usage

모든 앱/리포트는 `~/claude/design-system/index.html`의 스타일을 따릅니다:
1. 파일 열기 → 스타일 확인
2. `<style>` 섹션 복사
3. 필요한 컴포넌트 HTML 복사

---

## 📊 Research Report Template

### Location
```
~/claude/design-system/research-report-template.html
```

### Structure

```html
1. Header (제목, 부제, 메타정보)
2. Executive Summary (핵심 요약)
3. Table of Contents (자동 링크)
4. Sections:
   - Introduction
   - Background & Context
   - Analysis
   - Key Findings
   - Implications
   - Conclusion
5. References (Tier 분류)
```

### Usage

**Step 1: 복사**
```bash
cp ~/claude/design-system/research-report-template.html \
   ~/claude/_report/my-research/index.html
```

**Step 2: 수정**
- Header: 제목, 날짜, 참조 수
- Executive Summary: 2-3문장 요약
- Sections: 내용 채우기
- References: 출처 추가 (Tier 표시)

**Step 3: Tier 분류**
```html
<!-- Tier 1: Primary sources -->
<span class="reference-tier tier1">Tier 1</span>

<!-- Tier 2: Secondary sources -->
<span class="reference-tier tier2">Tier 2</span>

<!-- Tier 3: Tertiary sources -->
<span class="reference-tier tier3">Tier 3</span>
```

**Step 4: Confidence 표시**
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

**Step 5: In-text Citations**
```html
Research shows that AI adoption is growing
<a href="#ref1" class="citation">[1]</a>.
```

---

## 🛠️ App Templates (by Category)

### _tool/ (도구/유틸리티)

**예시**: 타이머, 계산기, 변환기

**Starter Code**:
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tool Name</title>
  <style>
    /* Copy from ~/claude/design-system/index.html */
    :root {
      --primary: #0d6efd;
      /* ... rest of design tokens */
    }
    /* ... component styles */
  </style>
</head>
<body>
  <div class="container">
    <div class="card">
      <h1>Tool Name</h1>
      <!-- Your tool UI here -->
    </div>
  </div>
  <script>
    // Your tool logic here
  </script>
</body>
</html>
```

**Save to**: `~/claude/_tool/[tool-name]/index.html`

---

### _game/ (게임)

**예시**: 퀴즈, 퍼즐, 교육 게임

**특징**:
- 점수 시스템
- 레벨/진행도
- 시각적 피드백
- localStorage 저장

**Kids 게임이면**: `skills/custom/kids/` 참조
- UI 컨벤션 (큰 버튼, 밝은 색상)
- 한영 병기
- 44px+ 터치 타겟

**Save to**: `~/claude/_game/[game-name]/index.html`

---

### _invest/ (투자/금융 리포트)

**예시**: 종목 분석, 시장 리포트, 가이드

**템플릿**: Research Report Template 사용
- Financial data는 Tier 1 (10-K, Bloomberg)
- 분석 리포트는 Tier 2 (Goldman Sachs 등)
- 뉴스 기사는 Tier 3

**추가 요소**:
- 차트/그래프 (Chart.js)
- 재무표 (table)
- 리스크 경고

**Save to**: `~/claude/_invest/[topic]-report/index.html`

---

### _report/ (일반 리서치)

**예시**: 기술 리포트, 건강 리포트, 산업 분석

**템플릿**: Research Report Template 사용

**분야별 출처**:
- 의료: CDC, WHO, NIH (Tier 1)
- 기술: arXiv, IEEE (Tier 1)
- 산업: McKinsey, Gartner (Tier 2)

**Save to**: `~/claude/_report/[topic]-report/index.html`

---

## 📁 Project Structure

### Standard Layout

```
~/claude/[category]/[project-name]/
├── index.html           # Main file
├── README.md            # Description, usage
├── screenshots/         # (Optional) UI screenshots
└── data/               # (Optional) Static data files
```

### Example: Investment Report

```
~/claude/_invest/tesla-analysis/
├── index.html          # Research report (HTML template)
├── README.md           # Summary + sources
└── screenshots/
    └── main-view.png
```

### Example: Tool App

```
~/claude/_tool/pomodoro-timer/
├── index.html          # Single-file app
└── README.md
```

---

## 🎯 Quick Start Workflow

### Creating a New Research Report

```bash
# 1. Create directory
mkdir -p ~/claude/_report/ai-trends-2026

# 2. Copy template
cp ~/claude/design-system/research-report-template.html \
   ~/claude/_report/ai-trends-2026/index.html

# 3. Edit in VSCode
code ~/claude/_report/ai-trends-2026/index.html

# 4. Fill in:
#    - Title, date, author
#    - Executive summary
#    - Sections (research content)
#    - References (with Tier tags)
#    - Confidence badges

# 5. Open in browser
open ~/claude/_report/ai-trends-2026/index.html
```

### Creating a New App

```bash
# 1. Create directory
mkdir -p ~/claude/_tool/my-app

# 2. Start from design system
cp ~/claude/design-system/index.html \
   ~/claude/_tool/my-app/index.html

# 3. Edit
code ~/claude/_tool/my-app/index.html

# 4. Remove demo sections
# 5. Add your app logic
# 6. Test
open ~/claude/_tool/my-app/index.html
```

---

## 🔧 Common Customizations

### Dark Mode Only

```css
/* Remove @media query, set dark colors as default */
:root {
  --bg: #1a1a1a;
  --text: #f0f0f0;
  /* ... */
}
```

### Custom Color Scheme

```css
:root {
  --primary: #your-color;
  --success: #your-color;
  /* Keep spacing/typography the same */
}
```

### Print Optimization (Reports)

```css
@media print {
  body { font-size: 12pt; }
  .no-print { display: none; }
  /* Already included in research template */
}
```

---

## 📋 Checklist Before Committing

### All Projects
- [ ] Follows design system (colors, spacing, typography)
- [ ] Mobile responsive (test on small screen)
- [ ] Dark mode works (if applicable)
- [ ] No external dependencies (self-contained)
- [ ] README.md exists

### Research Reports
- [ ] All claims have citations
- [ ] Sources are Tier-classified
- [ ] Confidence levels displayed
- [ ] Counterarguments included
- [ ] 10+ references minimum
- [ ] Executive summary complete
- [ ] Print-friendly

### Apps/Tools
- [ ] 44px+ touch targets
- [ ] Focus states on inputs/buttons
- [ ] localStorage usage (if needed)
- [ ] Error handling
- [ ] Works in file:// protocol

---

## 🔗 Related Files

- Design tokens: `~/claude/design-system/index.html`
- Source evaluation: `~/agent-skills/references/source-tiers.md`
- Project structure: `~/.claude/rules/projects.md`
- Common mistakes: `~/agent-skills/LEARNINGS.md`

---

## 💡 Tips

1. **Start simple**: Copy template → minimal edits → verify it works → add features
2. **Reuse components**: Design system has ready-made buttons, cards, forms
3. **Consistent naming**: `[topic]-[type]` (e.g., `ai-trends-report`, `pomodoro-timer`)
4. **Test early**: Open in browser frequently, test on mobile
5. **file:// constraint**: All data must be inline (no fetch/XHR)
