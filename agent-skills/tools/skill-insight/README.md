# skill-insight

CLI 도구 — Claude Code 메모리 시스템에서 인사이트를 추출하고 스킬에 적용

---

## Overview

### 문제 상황

스킬이 계속 생성되고 변화하는 환경에서:
- `LEARNINGS.md`에 좋은 패턴을 기록해도 **스킬에 적용하는 것은 수동 작업**
- `MEMORY.md`, `project-notes/`에 인사이트가 쌓여도 **어느 스킬에 적용할지 판단 어려움**
- 리서치로 발견한 커뮤니티 베스트 프랙티스를 **일일이 찾아서 적용하기 번거로움**

### 해결책

`skill-insight`는 **인사이트 발견부터 스킬 적용까지 자동화**하는 CLI 도구입니다.

```bash
# 1. 인사이트 스캔
$ skill-insight scan
✓ Scanned LEARNINGS.md: 5 insights
✓ Scanned MEMORY.md: 2 insights
✓ Total: 7 insights (3 new)

# 2. 대화형 리뷰
$ skill-insight review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1/3] New Insight

  Category: DOM
  Source: LEARNINGS.md:23

  "innerHTML 교체 전 activeElement 저장
   → 교체 후 focus 복원"

  Suggested skills: code, quality

  Apply to which skill? (code/quality/skip/later): code

✓ Applied to ~/agent-skills/skills/workflow/code/
```

### 핵심 기능

1. **자동 스캔**: `LEARNINGS.md`, `MEMORY.md`, `project-notes/` 파싱
2. **스킬 매칭**: 인사이트 내용 분석 → 관련 스킬 제안
3. **대화형 리뷰**: 인사이트 하나씩 보여주고 승인/스킵 선택
4. **구조화 적용**: 스킬 파일에 자동으로 적절한 섹션에 추가 (출처/날짜 포함)
5. **중복 체크**: 이미 적용된 인사이트는 스킵

### 작동 방식

```
┌─────────────────┐
│  Insight Sources │  LEARNINGS.md, MEMORY.md, project-notes/
└────────┬────────┘
         │ scan
         ↓
┌─────────────────┐
│  insights.json  │  인사이트 DB (메타데이터 포함)
└────────┬────────┘
         │ review
         ↓
┌─────────────────┐
│  User Review    │  승인/스킵 선택
└────────┬────────┘
         │ apply
         ↓
┌─────────────────┐
│   SKILL.md      │  구조화된 섹션에 자동 추가
└─────────────────┘
```

### 왜 CLI인가?

- ✅ **파일 시스템 직접 접근** (스킬 파일 자동 수정)
- ✅ **자동화 가능** (cron으로 주기적 스캔)
- ✅ **배치 처리** (여러 인사이트 한 번에 적용)
- ✅ **Git 연동** (변경 이력 추적)

HTML 대시보드는 나중에 시각적 탐색용으로 추가 가능.

---

## Quick Start

> 5분 안에 시작하기

### 1. 설치

```bash
cd ~/agent-skills/tools/skill-insight
chmod +x skill-insight.sh

# PATH에 추가 (선택)
ln -s ~/agent-skills/tools/skill-insight/skill-insight.sh /usr/local/bin/skill-insight
```

### 2. 첫 스캔

```bash
skill-insight scan
```

### 3. 인사이트 리뷰

```bash
skill-insight review
```

- 인사이트가 하나씩 표시됨
- 어느 스킬에 적용할지 선택
- 미리보기 확인 후 승인

### 4. 결과 확인

```bash
git diff ~/agent-skills/skills/workflow/code/SKILL.md
```

### 완료!

이제 Claude Code를 열고 스킬을 사용해보세요. 새로 추가된 인사이트가 자동으로 반영됩니다.

**다음 단계**:
- 전체 시나리오는 [Usage Scenarios](#usage-scenarios) 참고
- 명령어 상세는 [Commands Reference](#commands-reference) 참고

---

## Usage Scenarios

> 실제 사용 사례별 Step-by-step 가이드

---

### Scenario 1: 첫 설치 & 초기 스캔

**상황**: skill-insight를 처음 설치하고 기존에 쌓인 인사이트들을 한 번에 스캔하고 싶음

**목표**:
- 도구 설치
- 첫 스캔으로 인사이트 DB 생성
- 전체 인사이트 현황 파악

#### Step 1: 설치

```bash
# 프로젝트 폴더로 이동
$ cd ~/agent-skills/tools/skill-insight

# 실행 권한 부여
$ chmod +x skill-insight.sh

# PATH에 추가 (선택사항)
$ ln -s ~/agent-skills/tools/skill-insight/skill-insight.sh /usr/local/bin/skill-insight
```

#### Step 2: 첫 스캔

```bash
$ skill-insight scan
```

**예상 출력**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scanning insight sources...

✓ LEARNINGS.md
  - Found 12 learnings
  - Extracted 8 actionable insights

✓ MEMORY.md
  - Found 4 patterns
  - Extracted 3 actionable insights

✓ project-notes/
  - stock-analyzer.md: 2 insights
  - car-calculator.md: 1 insight
  - portfolio.md: 1 insight

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Summary:
- Total insights: 15
- New: 15
- Already applied: 0
- Pending review: 15

Insight DB saved to:
~/.claude/insights.json
```

#### Step 3: 인사이트 목록 확인

```bash
$ skill-insight list
```

**예상 출력**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pending Insights (15)

[001] DOM focus 복원 패턴
      Source: LEARNINGS.md:23
      Suggested: code, quality

[002] CORS proxy fallback
      Source: LEARNINGS.md:47
      Suggested: code

[003] localStorage 청크 저장
      Source: LEARNINGS.md:89
      Suggested: code, data

...

Use `skill-insight review` to start reviewing.
```

#### Step 4: 통계 확인

```bash
$ skill-insight stats
```

**예상 출력**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Insight Statistics

By Source:
  LEARNINGS.md:     8 insights
  MEMORY.md:        3 insights
  project-notes/:   4 insights

By Category:
  DOM:              4 insights
  Security:         3 insights
  Performance:      2 insights
  API:              2 insights
  Other:            4 insights

By Status:
  Pending:         15 insights
  Applied:          0 insights
  Skipped:          0 insights
```

**팁**:
- 첫 스캔 후 바로 리뷰하지 말고, 먼저 `list`로 전체 현황 파악
- 인사이트가 너무 많으면 (50+) 카테고리별로 나눠서 리뷰 권장

---

### Scenario 2: 주간 인사이트 리뷰 (⭐ 가장 일반적)

**상황**: 일주일간 작업하며 `LEARNINGS.md`에 새로운 교훈을 기록했고, 이제 스킬에 반영하고 싶음

**목표**:
- 새 인사이트만 스캔
- 대화형으로 하나씩 리뷰
- 적절한 스킬에 적용
- 적용 결과 확인

#### Step 1: 새 인사이트 스캔

```bash
$ skill-insight scan
```

**예상 출력**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scanning insight sources...

✓ LEARNINGS.md
  - Found 15 learnings (3 new since last scan)
  - Extracted 2 new actionable insights

✓ MEMORY.md
  - No changes

✓ project-notes/
  - car-calculator.md: 1 new insight

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Summary:
- New insights: 3
- Total pending: 18
```

#### Step 2: 대화형 리뷰 시작

```bash
$ skill-insight review
```

**대화형 프로세스** (각 인사이트마다):

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1/3] New Insight

  ID: 016
  Category: DOM
  Source: LEARNINGS.md:23 (2026-03-09)

  Content:
  ┌─────────────────────────────────────┐
  │ innerHTML 교체 전 activeElement 저장│
  │ → 교체 후 focus 복원                │
  │                                     │
  │ Context: 타이핑 중 DOM 교체로       │
  │ input focus 사라짐                  │
  │                                     │
  │ Next time: innerHTML 교체 전        │
  │ activeElement 저장 → 교체 후 복원  │
  └─────────────────────────────────────┘

  Suggested skills: code, quality
  Confidence: HIGH (검증된 패턴)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Options:
  [c] Apply to code skill
  [q] Apply to quality skill
  [b] Apply to both
  [s] Skip (not relevant)
  [l] Later (review next time)
  [?] Show current skill content

Your choice:
```

**의사결정 포인트 1**: 어느 스킬에 적용할지 선택

```
Your choice: c
```

**프로세스**:
1. `code/SKILL.md` 읽기
2. 적절한 섹션 찾기 (또는 새 섹션 생성)
3. 인사이트 추가
4. 출처/날짜 메타데이터 포함

**예상 출력**:
```
✓ Reading code/SKILL.md...
✓ Found section: "### Phase 4: Self-Review"
✓ Adding insight to "Common Mistakes" subsection...

Preview:
┌─────────────────────────────────────────────────────
│ ### Phase 4: Self-Review
│
│ **Common Mistakes:**
│ - [ ] innerHTML에 escapeHtml 적용됨
│ - [ ] 이벤트 리스너 중복 등록 확인
│ + - [ ] **DOM focus 복원**: innerHTML 교체 전
│ +   activeElement 저장 → 교체 후 focus 복원
│ +   (Source: LEARNINGS.md:23, 2026-03-09)
└─────────────────────────────────────────────────────

Apply this change? [y/n]:
```

**의사결정 포인트 2**: 적용 미리보기 확인

```
Apply this change? [y/n]: y
```

**예상 출력**:
```
✓ Applied to ~/agent-skills/skills/workflow/code/SKILL.md
✓ Marked insight #016 as applied

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[2/3] New Insight

  ID: 017
  Category: Security
  Source: LEARNINGS.md:47

  Content:
  ┌─────────────────────────────────────┐
  │ CORS proxy는 항상 2개 이상 fallback│
  │ 체인 구성                           │
  └─────────────────────────────────────┘

  Suggested skills: code

Your choice: c

✓ Applied to code/SKILL.md
  Added to "### Phase 2: Pattern" section

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[3/3] New Insight

  ID: 018
  Category: Performance
  Source: project-notes/car-calculator.md

  Content:
  ┌─────────────────────────────────────┐
  │ Chart.js 데이터 업데이트 시         │
  │ destroy() → new Chart() 말고        │
  │ chart.data.datasets[0].data = ...   │
  │ chart.update() 사용                 │
  └─────────────────────────────────────┘

  Suggested skills: data, design

Your choice: d

✓ Applied to data/SKILL.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Review Complete!

Summary:
- Reviewed: 3 insights
- Applied: 3 insights
- Skipped: 0 insights
- Later: 0 insights

Changed files:
- ~/agent-skills/skills/workflow/code/SKILL.md
- ~/agent-skills/skills/workflow/data/SKILL.md

Next steps:
1. Review the changed files
2. Test the skills with Claude Code
3. Commit changes: git add . && git commit -m "feat: apply insights from weekly review"
```

#### Step 3: 변경 사항 확인

```bash
$ git diff ~/agent-skills/skills/workflow/code/SKILL.md
```

**예상 출력**:
```diff
diff --git a/skills/workflow/code/SKILL.md b/skills/workflow/code/SKILL.md
index 1234567..abcdefg 100644
--- a/skills/workflow/code/SKILL.md
+++ b/skills/workflow/code/SKILL.md
@@ -48,6 +48,9 @@
 **Common Mistakes:**
 - [ ] innerHTML에 escapeHtml 적용됨
 - [ ] 이벤트 리스너 중복 등록 확인
+- [ ] **DOM focus 복원**: innerHTML 교체 전 activeElement 저장 → 교체 후 focus 복원
+  (Source: LEARNINGS.md:23, 2026-03-09)
+- [ ] **CORS proxy fallback**: 단일 프록시 의존 금지. 2개 이상 fallback 체인 구성
+  (Source: LEARNINGS.md:47, 2026-03-09)
```

#### Step 4: 적용 결과 테스트

```bash
# Claude Code로 테스트
$ code ~/agent-skills/skills/workflow/code/SKILL.md

# 새 Claude Code 세션에서:
# "파일 업로드 기능 구현해줘"라고 요청
# → code 스킬이 자동 호출되고, 새로 추가된 체크리스트 항목이 반영되는지 확인
```

**팁**:
- 한 번에 너무 많은 인사이트 (20+) 리뷰하지 말기. 10개 단위로 끊어서 진행
- `later` 옵션 활용: 지금 판단하기 애매한 인사이트는 나중으로 미루기
- Preview를 꼭 확인: 섹션 위치가 적절한지 체크

**주의사항**:
- 인사이트가 이미 스킬에 비슷한 내용으로 존재하면 → 중복 경고 표시
- 출처가 오래된 인사이트 (6개월+) → 여전히 유효한지 재확인 권장

---

### Scenario 3: 특정 스킬에 급하게 인사이트 적용

**상황**: 방금 발견한 중요한 패턴을 특정 스킬에 즉시 적용하고 싶음 (리뷰 프로세스 생략)

**목표**:
- 특정 인사이트만 선택
- 특정 스킬에 바로 적용
- 빠른 적용

#### Step 1: 인사이트 ID 확인

```bash
$ skill-insight list --status=pending
```

**예상 출력**:
```
[023] Claude API 브라우저 호출 시 필수 헤더
      Source: LEARNINGS.md:134
      Suggested: code
```

#### Step 2: 직접 적용

```bash
$ skill-insight apply --id=023 --skill=code
```

**예상 출력**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Applying insight #023 to code skill...

Content:
  "Claude API 브라우저 호출 시
   anthropic-dangerous-direct-browser-access: true
   헤더 필수 추가"

✓ Applied to code/SKILL.md
  Section: ### Phase 2: Pattern
  Location: Line 37

View changes:
  git diff ~/agent-skills/skills/workflow/code/SKILL.md
```

#### Step 3: 즉시 확인 & 커밋

```bash
$ git diff ~/agent-skills/skills/workflow/code/SKILL.md
$ git add ~/agent-skills/skills/workflow/code/SKILL.md
$ git commit -m "fix(code): add Claude API browser header requirement"
```

**팁**:
- 급한 경우에만 사용. 보통은 `review`로 전체 컨텍스트 파악 후 적용 권장
- `--force` 플래그로 중복 체크 우회 가능 (주의해서 사용)

---

### Scenario 4: 인사이트 충돌 해결

**상황**: 새 인사이트가 기존 스킬 내용과 충돌하거나 중복됨

**목표**:
- 충돌 감지
- 병합 또는 교체 결정
- 일관성 유지

#### Step 1: 리뷰 중 충돌 감지

```bash
$ skill-insight review
```

**예상 출력**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[5/8] New Insight

  ID: 034
  Content: "localStorage 5MB 제한 → 청크로 나눠 저장"

  ⚠️  CONFLICT DETECTED

  Existing content in code/SKILL.md:
  ┌─────────────────────────────────────┐
  │ localStorage → loadState()/saveState()│
  │ + try/catch + 5000자 제한           │
  └─────────────────────────────────────┘

  New insight:
  ┌─────────────────────────────────────┐
  │ localStorage 5MB 제한 초과 시       │
  │ 청크로 나눠서 저장하거나            │
  │ IndexedDB 사용                      │
  └─────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Options:
  [m] Merge (combine both)
  [r] Replace (use new, remove old)
  [k] Keep both separately
  [s] Skip new insight
  [?] Show full context

Your choice:
```

#### Step 2: 병합 선택

```
Your choice: m
```

**예상 출력**:
```
Merging insights...

Preview:
┌─────────────────────────────────────────────────────
│ **검증된 패턴 체크리스트:**
│ - [ ] localStorage → loadState()/saveState() + try/catch
│ -     + 5000자 제한
│ +     **Storage 전략:**
│ +     - 5000자 이하: 단일 저장
│ +     - 5000자~5MB: 청크로 분할 (chunk-001, chunk-002...)
│ +     - 5MB 초과: IndexedDB 사용
│ +     (Updated: LEARNINGS.md:89, 2026-03-09)
└─────────────────────────────────────────────────────

Apply merged version? [y/n]:
```

#### Step 3: 병합 승인

```
Apply merged version? [y/n]: y

✓ Merged and applied to code/SKILL.md
✓ Original insight marked as superseded
✓ New insight marked as applied
```

**팁**:
- `[?]` 옵션으로 충돌 전후 맥락을 충분히 확인
- 불확실하면 `[s]` Skip 후 수동으로 편집
- 병합 후 스킬이 여전히 일관성 있는지 전체 읽어보기

---

### Scenario 5: 새 스킬 생성 후 관련 인사이트 연결

**상황**: 새로운 스킬을 만들었고, 기존 인사이트 중 관련된 것들을 찾아서 적용하고 싶음

**목표**:
- 새 스킬에 적용 가능한 인사이트 필터링
- 한 번에 여러 인사이트 적용
- 새 스킬 빠른 부트스트래핑

#### Step 1: 새 스킬 생성

```bash
$ mkdir ~/agent-skills/skills/workflow/deploy
$ touch ~/agent-skills/skills/workflow/deploy/SKILL.md

# SKILL.md에 기본 구조 작성
```

#### Step 2: 관련 인사이트 검색

```bash
$ skill-insight search --keyword="deploy OR ci OR docker OR kubernetes"
```

**예상 출력**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Found 4 insights matching "deploy OR ci OR docker OR kubernetes"

[012] Docker 빌드 캐시 활용
      Source: project-notes/stock-analyzer.md
      Status: Pending

[027] GitHub Actions matrix 전략
      Source: LEARNINGS.md:156
      Status: Pending

[031] 롤백 전략 문서화
      Source: MEMORY.md:89
      Status: Pending

[045] Secret 환경변수 검증
      Source: LEARNINGS.md:203
      Status: Applied to ops

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### Step 3: 배치 적용

```bash
$ skill-insight apply --ids=012,027,031 --skill=deploy
```

**예상 출력**:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Batch applying 3 insights to deploy skill...

[1/3] Insight #012: Docker 빌드 캐시 활용
      ✓ Added to "Performance Optimization" section

[2/3] Insight #027: GitHub Actions matrix 전략
      ✓ Created new section "CI/CD Best Practices"
      ✓ Added insight

[3/3] Insight #031: 롤백 전략 문서화
      ✓ Added to "Safety Checklist" section

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Summary:
- Applied: 3 insights
- Created sections: 1
- Modified sections: 2

File: ~/agent-skills/skills/workflow/deploy/SKILL.md
Lines added: 18

Review changes:
  code ~/agent-skills/skills/workflow/deploy/SKILL.md
```

#### Step 4: 새 스킬 테스트

```bash
# Claude Code에서 새 스킬 테스트
$ claude "도커 이미지 빌드 최적화해줘"

# deploy 스킬이 자동 호출되는지 확인
# 적용된 인사이트가 반영되는지 확인
```

**팁**:
- 검색 키워드를 넓게 시작 → 점차 좁히기
- 다른 스킬에 이미 적용된 인사이트도 새 스킬에 복사 가능 (`--include-applied`)
- 배치 적용 후 섹션 순서/구조 정리 필요할 수 있음

**주의사항**:
- 너무 많은 인사이트 (10+)를 한 번에 적용하면 스킬이 비대해짐
- 새 스킬의 핵심 목적과 관련 없는 인사이트는 과감히 제외

---

### 시나리오 비교표

| 시나리오 | 빈도 | 소요시간 | 적용 개수 | 승인 필요 |
|---------|------|---------|----------|----------|
| 1. 첫 설치 | 1회 | 10분 | 0 (스캔만) | - |
| 2. 주간 리뷰 | 주 1회 | 15~30분 | 3~10개 | O |
| 3. 급한 적용 | 필요시 | 2분 | 1개 | X |
| 4. 충돌 해결 | 월 1~2회 | 5~10분 | 1~2개 | O |
| 5. 새 스킬 | 분기 1회 | 10분 | 3~5개 | △|

**추천 워크플로우**:
- **매주**: Scenario 2 (주간 리뷰)
- **필요시**: Scenario 3 (급한 적용)
- **월간**: 충돌/중복 인사이트 정리
- **분기**: 전체 스킬 재검토 + 오래된 인사이트 정리

---

## Commands Reference

### scan

인사이트 소스를 스캔하고 인사이트 DB를 업데이트합니다.

**사용법**:
```bash
skill-insight scan [options]
```

**옵션**:
- `--sources=<path>` - 특정 파일만 스캔 (기본: 전체)
- `--force` - 이미 스캔한 파일도 다시 스캔
- `--dry-run` - 실제 저장 없이 미리보기만

**예시**:
```bash
# 전체 스캔
$ skill-insight scan

# LEARNINGS.md만 스캔
$ skill-insight scan --sources=~/.claude/projects/-Users-kennyhong/memory/LEARNINGS.md

# Dry run
$ skill-insight scan --dry-run
```

**스캔 대상**:
- `~/.claude/projects/-Users-kennyhong/memory/LEARNINGS.md`
- `~/.claude/projects/-Users-kennyhong/memory/MEMORY.md`
- `~/.claude/projects/-Users-kennyhong/memory/project-notes/*.md`

**출력**:
- 소스별 발견된 인사이트 개수
- 새로운 인사이트 개수
- 인사이트 DB 경로

---

### review

대화형으로 인사이트를 하나씩 리뷰하고 스킬에 적용합니다.

**사용법**:
```bash
skill-insight review [options]
```

**옵션**:
- `--status=<status>` - 특정 상태만 리뷰 (기본: pending)
  - `pending` - 아직 적용 안 된 것
  - `later` - 나중으로 미룬 것
  - `all` - 전체
- `--skill=<skill>` - 특정 스킬 관련만 리뷰
- `--limit=<n>` - 최대 n개만 리뷰 (기본: 무제한)
- `--category=<category>` - 특정 카테고리만 리뷰

**예시**:
```bash
# 전체 리뷰
$ skill-insight review

# code 스킬 관련만 리뷰
$ skill-insight review --skill=code

# 최대 5개만 리뷰
$ skill-insight review --limit=5

# DOM 카테고리만 리뷰
$ skill-insight review --category=DOM

# 나중으로 미룬 것 리뷰
$ skill-insight review --status=later
```

**대화형 옵션** (각 인사이트마다):
- `[스킬명]` - 해당 스킬에 적용 (예: `code`, `quality`)
- `[b]` - 여러 스킬에 적용
- `[s]` - 스킵
- `[l]` - 나중에 (later)
- `[?]` - 현재 스킬 내용 보기
- `[q]` - 리뷰 종료

---

### list

저장된 인사이트 목록을 표시합니다.

**사용법**:
```bash
skill-insight list [options]
```

**옵션**:
- `--status=<status>` - 상태별 필터
  - `pending` - 적용 대기 중
  - `applied` - 이미 적용됨
  - `skipped` - 스킵됨
  - `later` - 나중으로 미룸
  - `all` - 전체 (기본)
- `--skill=<skill>` - 특정 스킬에 적용된/제안된 것만
- `--category=<category>` - 카테고리별 필터
- `--source=<source>` - 소스별 필터
- `--format=<format>` - 출력 포맷
  - `table` - 테이블 (기본)
  - `json` - JSON
  - `csv` - CSV

**예시**:
```bash
# 전체 목록
$ skill-insight list

# 적용 대기 중인 것만
$ skill-insight list --status=pending

# code 스킬 관련
$ skill-insight list --skill=code

# LEARNINGS.md 출처만
$ skill-insight list --source=LEARNINGS.md

# JSON 포맷
$ skill-insight list --format=json
```

**출력 컬럼**:
- ID
- Content (요약)
- Source
- Category
- Suggested Skills
- Status

---

### apply

특정 인사이트를 특정 스킬에 바로 적용합니다. (리뷰 프로세스 생략)

**사용법**:
```bash
skill-insight apply --id=<id> --skill=<skill> [options]
```

**필수 옵션**:
- `--id=<id>` - 인사이트 ID (또는 `--ids=<id1,id2,...>` 배치 적용)
- `--skill=<skill>` - 적용할 스킬 이름

**선택 옵션**:
- `--section=<section>` - 적용할 섹션 지정 (기본: 자동 선택)
- `--force` - 중복 체크 우회
- `--dry-run` - 실제 적용 없이 미리보기만

**예시**:
```bash
# 단일 적용
$ skill-insight apply --id=023 --skill=code

# 배치 적용
$ skill-insight apply --ids=012,027,031 --skill=deploy

# 특정 섹션에 적용
$ skill-insight apply --id=023 --skill=code --section="Phase 2: Pattern"

# Dry run
$ skill-insight apply --id=023 --skill=code --dry-run

# 강제 적용 (중복 무시)
$ skill-insight apply --id=023 --skill=code --force
```

**적용 규칙**:
1. 스킬 파일 읽기
2. 적절한 섹션 찾기 (또는 새 섹션 생성)
3. 인사이트 추가 (출처/날짜 포함)
4. 파일 저장
5. DB에 상태 업데이트

---

### stats

인사이트 통계를 표시합니다.

**사용법**:
```bash
skill-insight stats [options]
```

**옵션**:
- `--breakdown=<type>` - 분류 방식
  - `source` - 소스별
  - `category` - 카테고리별
  - `status` - 상태별
  - `skill` - 스킬별
  - `all` - 전체 (기본)

**예시**:
```bash
# 전체 통계
$ skill-insight stats

# 소스별만
$ skill-insight stats --breakdown=source

# 스킬별만
$ skill-insight stats --breakdown=skill
```

**출력**:
- 총 인사이트 개수
- 상태별 분포
- 소스별 분포
- 카테고리별 분포
- 스킬별 적용 현황

---

### search

키워드로 인사이트를 검색합니다.

**사용법**:
```bash
skill-insight search --keyword=<keyword> [options]
```

**필수 옵션**:
- `--keyword=<keyword>` - 검색 키워드 (OR/AND 지원)

**선택 옵션**:
- `--in=<field>` - 검색 대상 필드
  - `content` - 내용 (기본)
  - `source` - 출처
  - `all` - 전체
- `--status=<status>` - 상태 필터

**예시**:
```bash
# 단순 검색
$ skill-insight search --keyword="DOM"

# OR 검색
$ skill-insight search --keyword="deploy OR ci OR docker"

# AND 검색
$ skill-insight search --keyword="localStorage AND chunk"

# 출처에서 검색
$ skill-insight search --keyword="car-calculator" --in=source

# 적용된 것만 검색
$ skill-insight search --keyword="focus" --status=applied
```

---

### 전역 옵션

모든 명령어에서 사용 가능:

- `--help` - 도움말 표시
- `--version` - 버전 표시
- `--verbose` - 상세 출력
- `--quiet` - 최소 출력만
- `--db=<path>` - 인사이트 DB 경로 (기본: `~/.claude/insights.json`)

**예시**:
```bash
$ skill-insight scan --verbose
$ skill-insight list --quiet
$ skill-insight --version
```

---

## Top Insights from Research

> 커뮤니티 30+ 출처 분석에서 추출한 핵심 인사이트 (출처: claude-code-memory-research, 2026-02-24)

### 카테고리별 인사이트

#### 1. SKILL.md 작성 원칙

**⭐ description이 스킬 선택의 핵심**
- Claude는 알고리즘이 아닌 **의미적 매칭**으로 스킬 선택
- description을 구체적으로: "코드 작성 시 사용" ❌ → "보안, 패턴, 성능 검증. 코드 작성 및 리뷰 시 자동 사용" ✅
- 출처: [Inside Claude Code Skills](https://mikhail.io/2025/10/claude-code-skills/) + [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

**불릿 리스트 > 산문**
- Claude Code는 서술형 문단보다 **불릿 리스트를 훨씬 효율적으로 파싱**
- 산문: "코드를 작성할 때는 포맷팅을 잘 해주세요" ❌
- 리스트: "- 2-space 들여쓰기 사용" ✅
- 토큰 효율: 리스트가 산문 대비 30~40% 적은 토큰 사용
- 출처: [You don't understand Claude Code memory](https://joseparreogarcia.substack.com/p/claude-code-memory-explained)

**구체적 지시 > 추상적 지시**
- "잘 작성하세요" ❌ → "max 100 chars/line" ✅
- 수정 요청 40% 감소 효과
- 출처: awesome-claude-code, claude-code-best-practice

**금지 사항 명시**
- "X를 하지 마라" 형태가 긍정형 권고보다 **에러 방지에 더 효과적**
- 예: "NEVER use `any` type", "innerHTML에 유저 데이터 직접 삽입 금지"
- 출처: 커뮤니티 합의 (24.9k star repo)

**코드 예시 3~5개 포함**
- 원하는 출력 포맷의 코드 예시를 보여주면 설명 대비 **수정 요청이 40% 감소**
- Before/After 비교 예시가 가장 효과적
- 출처: claude-md-examples

---

#### 2. 스킬 구조 최적화

**온디맨드 로딩 활용**
- 스킬은 name/description만 상시 로드, 호출 시에만 전체 SKILL.md 주입
- 상세 프로토콜을 스킬로 분리하면 **세션당 15,000 토큰 절약** 가능
- 출처: [Optimization Guide](https://institute.sfeir.com/en/claude-code/claude-code-memory-system-claude-md/optimization/)

**Confidence Levels 표준화**
- 🟢 HIGH (테스트 통과) / 🟡 MEDIUM (공식 문서) / 🔴 LOW (미검증)
- 환각 방지 효과: 40% 감소
- 출처: obra/superpowers, Trail of Bits Security skills

**Phase 기반 워크플로우**
- Analyze → Pattern → Implement → Review 구조
- RIPER 패턴: Research → Innovate → Plan → Execute → Review
- 출처: [Claude Agent Skills Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)

---

#### 3. 토큰 최적화 전략

**모듈형 규칙 분리**
- `.claude/rules/*.md`에 주제별 파일 분리
- 조건부 로딩 (glob 패턴) 사용 시 **컨텍스트 노이즈 30~40% 감소**
- 예: `testing.md`는 `**/*.test.ts` 파일에서만 로드
- 출처: [Modular Rules in Claude Code](https://claude-blog.setec.rs/blog/claude-code-rules-directory)

**트리거 테이블 치환**
- 서술형 트리거 설명을 테이블로 치환: 54% 토큰 절감 사례
- Before: "When the user mentions tasks..." (수백 줄)
- After: `| Triggers | Skill | Tools |` 테이블
- 출처: [54% Context Reduction Gist](https://gist.github.com/johnlindquist/849b813e76039a908d962b2f0923dc9a)

**SKILL.md 길이 권장**
- 스킬 하나당 **1,500~3,000 토큰** 이내
- 전체 스킬 합산 **10,000 토큰 이내** (200K 윈도우의 5%)
- 출처: 커뮤니티 합의

---

#### 4. 메모리 시스템 이해

**메모리는 "텍스트 주입"**
- Claude의 메모리는 "기억"이 아니라 **"매번 다시 읽는 지시서"**
- 매 세션마다 관련 마크다운 파일이 프롬프트 컨텍스트에 로드됨
- 이 근본적 이해가 최적화의 출발점
- 출처: [You don't understand Claude Code memory](https://joseparreogarcia.substack.com/p/claude-code-memory-explained)

**Auto Memory 첫 200줄만 로드**
- MEMORY.md는 첫 200줄만 시스템 프롬프트에 포함
- 상세 내용은 토픽 파일로 분리 (`memory/debugging.md`, `memory/patterns.md`)
- 필요 시에만 Claude가 Read 도구로 읽음
- 출처: [Manage Claude's memory](https://code.claude.com/docs/en/memory)

---

#### 5. 창의적 활용 패턴

**Memory Bank 패턴**
- CLAUDE.md를 **"살아있는 문서"**로 활용
- 4단계 지식 루프: Understand → Plan → Execute → **Update Memory**
- 매 세션 종료 시 `/update-memory`로 학습 내용 기록
- 출처: [claude-code-memory-bank](https://github.com/hudrazine/claude-code-memory-bank)

**Hooks 자동화**
- PreToolUse / PostToolUse 훅으로 워크플로우 자동화
- 예: 코드 저장 시 자동 포맷팅, 커밋 전 자동 typecheck
- 출처: 공식 문서 + 커뮤니티 best practices

---

### 적용 우선순위

| 순위 | 인사이트 | 난이도 | 임팩트 |
|------|---------|--------|--------|
| 1 | description 구체화 | 낮음 | 높음 (스킬 선택 정확도) |
| 2 | 불릿 리스트 변환 | 낮음 | 중간 (토큰 30% 절감) |
| 3 | 금지 사항 명시 | 낮음 | 높음 (에러 방지) |
| 4 | Confidence Levels 추가 | 중간 | 높음 (환각 40% 감소) |
| 5 | 코드 예시 3~5개 | 중간 | 중간 (수정 요청 40% 감소) |
| 6 | Phase 워크플로우 | 높음 | 높음 (일관성 보장) |
| 7 | 모듈형 규칙 분리 | 높음 | 중간 (토큰 절감) |

**추천 시작점:** 1~3번 (낮은 난이도, 높은 임팩트)

---

## Architecture

### File Structure

```
~/agent-skills/tools/skill-insight/
├── skill-insight.sh           # 메인 실행 파일
├── lib/
│   ├── scanner.sh            # 인사이트 스캔 로직
│   ├── matcher.sh            # 스킬 매칭 알고리즘
│   ├── applier.sh            # 스킬 파일 업데이트
│   ├── reviewer.sh           # 대화형 리뷰 UI
│   └── utils.sh              # 공통 유틸리티
├── data/
│   └── .gitkeep              # (insights.json은 ~/.claude/에 저장)
├── tests/
│   ├── test_scanner.sh
│   ├── test_matcher.sh
│   └── test_applier.sh
├── README.md                  # 이 문서
└── CHANGELOG.md

~/.claude/
└── insights.json              # 인사이트 DB (실제 저장 위치)
```

### Data Model

#### insights.json 구조

```json
{
  "version": "1.0.0",
  "lastScan": "2026-03-09T22:30:00Z",
  "insights": [
    {
      "id": "001",
      "content": "innerHTML 교체 전 activeElement 저장 → 교체 후 focus 복원",
      "source": {
        "file": "LEARNINGS.md",
        "line": 23,
        "extractedAt": "2026-03-09T22:00:00Z"
      },
      "category": "DOM",
      "suggestedSkills": ["code", "quality"],
      "confidence": "HIGH",
      "status": "pending",
      "appliedTo": [],
      "metadata": {
        "context": "Context: 타이핑 중 DOM 교체로 input focus 사라짐",
        "nextTime": "Next time: innerHTML 교체 전 activeElement 저장 → 교체 후 복원",
        "keywords": ["DOM", "focus", "innerHTML", "activeElement"]
      }
    },
    {
      "id": "002",
      "content": "CORS proxy는 항상 2개 이상 fallback 체인 구성",
      "source": {
        "file": "LEARNINGS.md",
        "line": 47,
        "extractedAt": "2026-03-09T22:00:00Z"
      },
      "category": "Network",
      "suggestedSkills": ["code"],
      "confidence": "HIGH",
      "status": "applied",
      "appliedTo": [
        {
          "skill": "code",
          "section": "Phase 2: Pattern",
          "appliedAt": "2026-03-09T22:15:00Z"
        }
      ],
      "metadata": {
        "outcome": "Outcome: proxy 서버 다운 시 전체 기능 불가",
        "nextTime": "Next time: CORS proxy는 항상 2개 이상 fallback 체인 구성",
        "keywords": ["CORS", "proxy", "fallback", "network"]
      }
    }
  ]
}
```

#### 필드 설명

| 필드 | 타입 | 설명 |
|------|------|------|
| `id` | string | 인사이트 고유 ID (3자리 숫자) |
| `content` | string | 인사이트 핵심 내용 (1~2줄) |
| `source` | object | 출처 정보 (파일, 라인, 추출 시각) |
| `category` | string | 카테고리 (DOM, Security, Performance 등) |
| `suggestedSkills` | array | 추천 스킬 목록 |
| `confidence` | enum | HIGH/MEDIUM/LOW |
| `status` | enum | pending/applied/skipped/later |
| `appliedTo` | array | 적용된 스킬 목록 (스킬명, 섹션, 적용 시각) |
| `metadata` | object | 추가 정보 (컨텍스트, 키워드 등) |

### Components

#### 1. Scanner (lib/scanner.sh)

**책임**:
- 인사이트 소스 파일 읽기
- 패턴 매칭으로 인사이트 추출
- 메타데이터 파싱
- insights.json 업데이트

**핵심 함수**:
```bash
scan_learnings()      # LEARNINGS.md 스캔
scan_memory()         # MEMORY.md 스캔
scan_project_notes()  # project-notes/*.md 스캔
extract_insight()     # 인사이트 추출 로직
parse_metadata()      # Context/Outcome/Next time 파싱
```

**추출 규칙**:
- `LEARNINGS.md`: "- Context: ... Next time: ..." 패턴
- `MEMORY.md`: 프로젝트별 섹션
- `project-notes/*.md`: 커스텀 마커 (예: `## Learnings`)

---

#### 2. Matcher (lib/matcher.sh)

**책임**:
- 인사이트 내용 분석
- 관련 스킬 제안
- 신뢰도 점수 계산

**핵심 함수**:
```bash
suggest_skills()           # 스킬 추천
calculate_confidence()     # 신뢰도 계산
extract_keywords()         # 키워드 추출
match_category()           # 카테고리 매칭
```

**매칭 알고리즘**:
1. **키워드 기반 매칭**
   - 인사이트에서 키워드 추출 (DOM, API, localStorage 등)
   - 각 스킬의 SKILL.md에서 키워드 빈도 계산
   - 점수 높은 순으로 정렬

2. **카테고리 매핑**
   ```bash
   DOM          → code, quality
   Security     → code
   Performance  → code, data
   Network      → code
   Testing      → quality
   UI/UX        → design
   Data         → data
   Deploy       → ops
   ```

3. **신뢰도 계산**
   - HIGH: "검증된 패턴", "테스트 통과" 언급
   - MEDIUM: "공식 문서" 언급
   - LOW: "Stack Overflow", "추측" 언급

---

#### 3. Applier (lib/applier.sh)

**책임**:
- 스킬 파일 읽기
- 적절한 섹션 찾기/생성
- 인사이트 추가 (포맷팅 포함)
- 파일 저장
- DB 상태 업데이트

**핵심 함수**:
```bash
apply_insight()           # 메인 적용 함수
find_section()           # 섹션 찾기
create_section()         # 새 섹션 생성
format_insight()         # 마크다운 포맷팅
check_duplicate()        # 중복 체크
update_db_status()       # DB 업데이트
```

**적용 규칙**:
1. **섹션 우선순위** (code 스킬 예시)
   - `Phase 4: Self-Review` > `Common Mistakes`
   - `Phase 2: Pattern` > `검증된 패턴 체크리스트`
   - `Phase 3: Implement` > 구현 팁
   - 없으면 새 섹션 `## Learnings from Projects` 생성

2. **포맷팅**
   ```markdown
   - [ ] **키워드**: 인사이트 내용
     (Source: LEARNINGS.md:23, 2026-03-09)
   ```

3. **중복 체크**
   - 기존 내용과 유사도 계산 (키워드 기반)
   - 80% 이상 유사 → 중복 경고
   - 사용자 확인 후 병합/교체/스킵

---

#### 4. Reviewer (lib/reviewer.sh)

**책임**:
- 대화형 UI 제공
- 인사이트 하나씩 표시
- 사용자 입력 처리
- 적용 프로세스 오케스트레이션

**핵심 함수**:
```bash
start_review()            # 리뷰 시작
show_insight()           # 인사이트 표시
get_user_choice()        # 사용자 선택
show_preview()           # 적용 미리보기
confirm_apply()          # 적용 확인
handle_conflict()        # 충돌 처리
show_summary()           # 리뷰 요약
```

**UI 컴포넌트**:
- Progress bar: `[1/3]`
- Box drawing: `┌─────┐`
- Color coding: 카테고리별 색상
- Interactive prompt: 선택지 표시

---

### 데이터 흐름

```
┌─────────────┐
│   Sources   │  LEARNINGS.md, MEMORY.md, project-notes/
└──────┬──────┘
       │
       ↓ scan (Scanner)
┌─────────────┐
│ Raw Insights│  추출된 텍스트
└──────┬──────┘
       │
       ↓ parse + match (Matcher)
┌─────────────┐
│insights.json│  구조화된 인사이트 + 메타데이터
└──────┬──────┘
       │
       ↓ review (Reviewer)
┌─────────────┐
│ User Input  │  승인/스킵/나중에
└──────┬──────┘
       │
       ↓ apply (Applier)
┌─────────────┐
│  SKILL.md   │  업데이트된 스킬
└─────────────┘
       │
       ↓ update status
┌─────────────┐
│insights.json│  상태 업데이트
└─────────────┘
```

---

## Implementation Guide

> 각 Phase별 구현 가이드 (Bash 스크립트 기반)

---

### Phase 1: Scanner

**목표**: 인사이트 소스 파일을 파싱하고 구조화된 데이터로 변환

#### 1.1 LEARNINGS.md 파싱

**패턴**:
```
- Context: [작업 맥락]
  What I tried: [시도한 방법]
  Outcome: [결과]
  Next time: [다음에 기억할 것]
```

**구현 로직**:
```bash
# lib/scanner.sh

scan_learnings() {
  local file="$HOME/.claude/projects/-Users-kennyhong/memory/LEARNINGS.md"
  local current_block=""
  local line_num=0

  while IFS= read -r line; do
    ((line_num++))

    # Context로 시작하는 새 블록
    if [[ "$line" =~ ^[[:space:]]*-[[:space:]]*Context: ]]; then
      # 이전 블록 저장
      if [[ -n "$current_block" ]]; then
        extract_insight "$current_block" "$file" "$((line_num - 1))"
      fi
      current_block="$line"
    else
      current_block+=$'\n'"$line"
    fi
  done < "$file"

  # 마지막 블록 저장
  if [[ -n "$current_block" ]]; then
    extract_insight "$current_block" "$file" "$line_num"
  fi
}

extract_insight() {
  local block="$1"
  local file="$2"
  local line_num="$3"

  # Next time 추출
  local next_time=$(echo "$block" | grep "Next time:" | sed 's/.*Next time: //')

  if [[ -z "$next_time" ]]; then
    return  # Next time 없으면 스킵
  fi

  # Context 추출
  local context=$(echo "$block" | grep "Context:" | sed 's/.*Context: //')

  # Outcome 추출
  local outcome=$(echo "$block" | grep "Outcome:" | sed 's/.*Outcome: //')

  # 키워드 추출 (간단한 방식)
  local keywords=$(echo "$next_time" | grep -oE '\b[A-Z][a-z]+\b|\b[a-z]+\b' | sort -u | head -5)

  # 카테고리 자동 감지
  local category=$(detect_category "$next_time")

  # insights.json에 추가
  add_insight "$next_time" "$file:$line_num" "$category" "$context" "$outcome" "$keywords"
}

detect_category() {
  local text="$1"

  # 키워드 기반 카테고리 매칭
  if [[ "$text" =~ (DOM|innerHTML|focus|element) ]]; then
    echo "DOM"
  elif [[ "$text" =~ (XSS|CORS|security|escape) ]]; then
    echo "Security"
  elif [[ "$text" =~ (performance|cache|optimize) ]]; then
    echo "Performance"
  elif [[ "$text" =~ (API|fetch|request) ]]; then
    echo "Network"
  elif [[ "$text" =~ (test|assert|mock) ]]; then
    echo "Testing"
  else
    echo "Other"
  fi
}
```

#### 1.2 insights.json 관리

**구현**:
```bash
# lib/scanner.sh

INSIGHTS_DB="$HOME/.claude/insights.json"

init_db() {
  if [[ ! -f "$INSIGHTS_DB" ]]; then
    cat > "$INSIGHTS_DB" <<'EOF'
{
  "version": "1.0.0",
  "lastScan": "",
  "insights": []
}
EOF
  fi
}

add_insight() {
  local content="$1"
  local source="$2"
  local category="$3"
  local context="$4"
  local outcome="$5"
  local keywords="$6"

  # 중복 체크 (content 기준)
  local exists=$(jq --arg c "$content" '.insights[] | select(.content == $c) | .id' "$INSIGHTS_DB")
  if [[ -n "$exists" ]]; then
    return  # 이미 존재
  fi

  # 새 ID 생성
  local new_id=$(printf "%03d" $(($(jq '.insights | length' "$INSIGHTS_DB") + 1)))

  # JSON 추가
  jq --arg id "$new_id" \
     --arg content "$content" \
     --arg source "$source" \
     --arg category "$category" \
     --arg context "$context" \
     --arg outcome "$outcome" \
     --arg keywords "$keywords" \
     --arg timestamp "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
     '.insights += [{
       "id": $id,
       "content": $content,
       "source": {"file": ($source | split(":")[0]), "line": ($source | split(":")[1] | tonumber), "extractedAt": $timestamp},
       "category": $category,
       "suggestedSkills": [],
       "confidence": "MEDIUM",
       "status": "pending",
       "appliedTo": [],
       "metadata": {"context": $context, "outcome": $outcome, "keywords": ($keywords | split("\n"))}
     }]' "$INSIGHTS_DB" > "${INSIGHTS_DB}.tmp" && mv "${INSIGHTS_DB}.tmp" "$INSIGHTS_DB"
}
```

**테스트**:
```bash
# tests/test_scanner.sh
./skill-insight.sh scan --dry-run
# 출력 확인: 추출된 인사이트 개수, 내용 샘플
```

---

### Phase 2: Matcher

**목표**: 인사이트 내용을 분석하고 관련 스킬을 제안

#### 2.1 스킬 매칭 알고리즘

**구현**:
```bash
# lib/matcher.sh

suggest_skills() {
  local insight_id="$1"
  local content=$(jq -r --arg id "$insight_id" '.insights[] | select(.id == $id) | .content' "$INSIGHTS_DB")
  local category=$(jq -r --arg id "$insight_id" '.insights[] | select(.id == $id) | .category' "$INSIGHTS_DB")

  # 키워드 추출
  local keywords=$(echo "$content" | grep -oE '\b[a-zA-Z]{3,}\b' | tr '[:upper:]' '[:lower:]' | sort -u)

  # 스킬별 점수 계산
  declare -A scores
  for skill in $(ls ~/agent-skills/skills/workflow/); do
    local skill_content=$(cat ~/agent-skills/skills/workflow/$skill/SKILL.md 2>/dev/null || echo "")
    local score=0

    # 키워드 매칭
    for keyword in $keywords; do
      local count=$(echo "$skill_content" | grep -i -c "$keyword" || echo 0)
      score=$((score + count))
    done

    # 카테고리 보너스
    case "$category" in
      "DOM"|"Security"|"Performance"|"Network")
        if [[ "$skill" == "code" ]]; then
          score=$((score + 10))
        fi
        ;;
      "Testing")
        if [[ "$skill" == "quality" ]]; then
          score=$((score + 10))
        fi
        ;;
      "UI/UX")
        if [[ "$skill" == "design" ]]; then
          score=$((score + 10))
        fi
        ;;
    esac

    scores[$skill]=$score
  done

  # 점수 높은 순 정렬 (상위 3개)
  local suggested=$(for skill in "${!scores[@]}"; do
    echo "${scores[$skill]} $skill"
  done | sort -rn | head -3 | awk '{print $2}' | paste -sd "," -)

  # DB 업데이트
  jq --arg id "$insight_id" --arg skills "$suggested" \
     '(.insights[] | select(.id == $id) | .suggestedSkills) = ($skills | split(","))' \
     "$INSIGHTS_DB" > "${INSIGHTS_DB}.tmp" && mv "${INSIGHTS_DB}.tmp" "$INSIGHTS_DB"

  echo "$suggested"
}

calculate_confidence() {
  local insight_id="$1"
  local content=$(jq -r --arg id "$insight_id" '.insights[] | select(.id == $id) | .content' "$INSIGHTS_DB")
  local metadata=$(jq -r --arg id "$insight_id" '.insights[] | select(.id == $id) | .metadata' "$INSIGHTS_DB")

  local confidence="MEDIUM"  # 기본값

  # HIGH 조건
  if echo "$content $metadata" | grep -qE "(검증된|테스트 통과|Worked)"; then
    confidence="HIGH"
  # LOW 조건
  elif echo "$content $metadata" | grep -qE "(Stack Overflow|추측|미테스트|Failed)"; then
    confidence="LOW"
  fi

  # DB 업데이트
  jq --arg id "$insight_id" --arg conf "$confidence" \
     '(.insights[] | select(.id == $id) | .confidence) = $conf' \
     "$INSIGHTS_DB" > "${INSIGHTS_DB}.tmp" && mv "${INSIGHTS_DB}.tmp" "$INSIGHTS_DB"

  echo "$confidence"
}
```

**테스트**:
```bash
# 특정 인사이트 매칭 테스트
./skill-insight.sh match --id=001
# 출력: code, quality (점수: 45, 12)
```

---

### Phase 3: Applier

**목표**: 스킬 파일을 읽고 적절한 위치에 인사이트를 추가

#### 3.1 섹션 찾기 & 추가

**구현**:
```bash
# lib/applier.sh

apply_insight() {
  local insight_id="$1"
  local skill="$2"
  local section="${3:-auto}"  # 섹션 지정 또는 자동

  local skill_file="$HOME/agent-skills/skills/workflow/$skill/SKILL.md"

  if [[ ! -f "$skill_file" ]]; then
    echo "Error: Skill file not found: $skill_file"
    return 1
  fi

  # 인사이트 정보 가져오기
  local content=$(jq -r --arg id "$insight_id" '.insights[] | select(.id == $id) | .content' "$INSIGHTS_DB")
  local source_file=$(jq -r --arg id "$insight_id" '.insights[] | select(.id == $id) | .source.file' "$INSIGHTS_DB")
  local source_line=$(jq -r --arg id "$insight_id" '.insights[] | select(.id == $id) | .source.line' "$INSIGHTS_DB")
  local extracted_at=$(jq -r --arg id "$insight_id" '.insights[] | select(.id == $id) | .source.extractedAt' "$INSIGHTS_DB")
  local category=$(jq -r --arg id "$insight_id" '.insights[] | select(.id == $id) | .category' "$INSIGHTS_DB")

  # 중복 체크
  if grep -qF "$content" "$skill_file"; then
    echo "Warning: Similar content already exists in $skill_file"
    read -p "Continue anyway? [y/N]: " confirm
    [[ "$confirm" != "y" ]] && return 1
  fi

  # 섹션 찾기
  if [[ "$section" == "auto" ]]; then
    section=$(find_best_section "$skill_file" "$category")
  fi

  # 인사이트 포맷팅
  local formatted=$(format_insight "$content" "$source_file" "$source_line" "$extracted_at" "$category")

  # 파일에 삽입
  insert_into_section "$skill_file" "$section" "$formatted"

  # DB 상태 업데이트
  update_applied_status "$insight_id" "$skill" "$section"

  echo "✓ Applied to $skill_file"
}

find_best_section() {
  local file="$1"
  local category="$2"

  # code 스킬의 경우
  if [[ "$file" =~ code/SKILL.md ]]; then
    if [[ "$category" == "DOM" || "$category" == "Security" ]]; then
      echo "### Phase 4: Self-Review"
    elif [[ "$category" == "Performance" || "$category" == "Network" ]]; then
      echo "### Phase 2: Pattern"
    else
      echo "### Phase 3: Implement"
    fi
  else
    # 다른 스킬은 "## Learnings from Projects" 섹션
    echo "## Learnings from Projects"
  fi
}

format_insight() {
  local content="$1"
  local source_file="$2"
  local source_line="$3"
  local extracted_at="$4"
  local category="$5"

  local date=$(echo "$extracted_at" | cut -d'T' -f1)

  cat <<EOF
- [ ] **$category**: $content
  (Source: $source_file:$source_line, $date)
EOF
}

insert_into_section() {
  local file="$1"
  local section="$2"
  local content="$3"

  # 섹션 찾기 (정규식)
  local section_line=$(grep -n "^$section" "$file" | head -1 | cut -d: -f1)

  if [[ -z "$section_line" ]]; then
    # 섹션 없으면 파일 끝에 추가
    echo "" >> "$file"
    echo "$section" >> "$file"
    echo "$content" >> "$file"
  else
    # 섹션 바로 다음 줄에 추가
    sed -i.bak "${section_line}a\\
$content
" "$file"
    rm "${file}.bak"
  fi
}

update_applied_status() {
  local insight_id="$1"
  local skill="$2"
  local section="$3"
  local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)

  jq --arg id "$insight_id" \
     --arg skill "$skill" \
     --arg section "$section" \
     --arg timestamp "$timestamp" \
     '(.insights[] | select(.id == $id) | .status) = "applied" |
      (.insights[] | select(.id == $id) | .appliedTo) += [{"skill": $skill, "section": $section, "appliedAt": $timestamp}]' \
     "$INSIGHTS_DB" > "${INSIGHTS_DB}.tmp" && mv "${INSIGHTS_DB}.tmp" "$INSIGHTS_DB"
}
```

**테스트**:
```bash
# Dry run으로 미리보기
./skill-insight.sh apply --id=001 --skill=code --dry-run

# 실제 적용
./skill-insight.sh apply --id=001 --skill=code

# 결과 확인
git diff ~/agent-skills/skills/workflow/code/SKILL.md
```

---

### Phase 4: Review Interface

**목표**: 대화형 UI로 인사이트를 하나씩 리뷰하고 적용

#### 4.1 대화형 프롬프트

**구현**:
```bash
# lib/reviewer.sh

start_review() {
  local status="${1:-pending}"

  # pending 인사이트 목록
  local ids=$(jq -r --arg status "$status" '.insights[] | select(.status == $status) | .id' "$INSIGHTS_DB")
  local total=$(echo "$ids" | wc -l | tr -d ' ')

  if [[ "$total" -eq 0 ]]; then
    echo "No insights to review."
    return
  fi

  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Starting review: $total insights"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  local count=0
  for id in $ids; do
    ((count++))
    show_insight "$id" "$count" "$total"

    local choice=$(get_user_choice "$id")
    handle_choice "$id" "$choice"
  done

  show_summary
}

show_insight() {
  local id="$1"
  local current="$2"
  local total="$3"

  local content=$(jq -r --arg id "$id" '.insights[] | select(.id == $id) | .content' "$INSIGHTS_DB")
  local source=$(jq -r --arg id "$id" '.insights[] | select(.id == $id) | .source.file' "$INSIGHTS_DB")
  local line=$(jq -r --arg id "$id" '.insights[] | select(.id == $id) | .source.line' "$INSIGHTS_DB")
  local category=$(jq -r --arg id "$id" '.insights[] | select(.id == $id) | .category' "$INSIGHTS_DB")
  local suggested=$(jq -r --arg id "$id" '.insights[] | select(.id == $id) | .suggestedSkills | join(", ")' "$INSIGHTS_DB")
  local confidence=$(jq -r --arg id "$id" '.insights[] | select(.id == $id) | .confidence' "$INSIGHTS_DB")

  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "[$current/$total] New Insight"
  echo ""
  echo "  ID: $id"
  echo "  Category: $category"
  echo "  Source: $source:$line"
  echo ""
  echo "  Content:"
  echo "  ┌─────────────────────────────────────┐"
  echo "  │ $content"
  echo "  └─────────────────────────────────────┘"
  echo ""
  echo "  Suggested skills: $suggested"
  echo "  Confidence: $confidence"
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

get_user_choice() {
  local id="$1"
  local suggested=$(jq -r --arg id "$id" '.insights[] | select(.id == $id) | .suggestedSkills[]' "$INSIGHTS_DB")

  echo "Options:"
  for skill in $suggested; do
    echo "  [$skill] Apply to $skill skill"
  done
  echo "  [b] Apply to both/multiple"
  echo "  [s] Skip (not relevant)"
  echo "  [l] Later (review next time)"
  echo "  [?] Show current skill content"
  echo ""
  read -p "Your choice: " choice
  echo "$choice"
}

handle_choice() {
  local id="$1"
  local choice="$2"

  case "$choice" in
    s)
      jq --arg id "$id" '(.insights[] | select(.id == $id) | .status) = "skipped"' \
         "$INSIGHTS_DB" > "${INSIGHTS_DB}.tmp" && mv "${INSIGHTS_DB}.tmp" "$INSIGHTS_DB"
      echo "✓ Skipped"
      ;;
    l)
      jq --arg id "$id" '(.insights[] | select(.id == $id) | .status) = "later"' \
         "$INSIGHTS_DB" > "${INSIGHTS_DB}.tmp" && mv "${INSIGHTS_DB}.tmp" "$INSIGHTS_DB"
      echo "✓ Marked for later"
      ;;
    \?)
      # TODO: 현재 스킬 내용 표시
      ;;
    b)
      # TODO: 여러 스킬 선택
      ;;
    *)
      # 스킬명으로 간주
      apply_insight "$id" "$choice"
      ;;
  esac
}

show_summary() {
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Review Complete!"
  echo ""
  echo "Summary:"
  echo "  Applied: $(jq '[.insights[] | select(.status == "applied")] | length' "$INSIGHTS_DB")"
  echo "  Skipped: $(jq '[.insights[] | select(.status == "skipped")] | length' "$INSIGHTS_DB")"
  echo "  Later: $(jq '[.insights[] | select(.status == "later")] | length' "$INSIGHTS_DB")"
  echo ""
  echo "Changed files:"
  git diff --name-only ~/agent-skills/skills/workflow/
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}
```

**테스트**:
```bash
# 대화형 리뷰 테스트
./skill-insight.sh review --limit=3

# 특정 스킬만 리뷰
./skill-insight.sh review --skill=code
```

---

### 개발 체크리스트

**Phase 1: Scanner**
- [ ] LEARNINGS.md 파싱
- [ ] MEMORY.md 파싱
- [ ] project-notes/ 파싱
- [ ] insights.json 생성/업데이트
- [ ] 중복 체크
- [ ] 카테고리 자동 감지

**Phase 2: Matcher**
- [ ] 키워드 추출
- [ ] 스킬 매칭 알고리즘
- [ ] 신뢰도 계산
- [ ] suggestedSkills 업데이트

**Phase 3: Applier**
- [ ] 스킬 파일 읽기
- [ ] 섹션 찾기/생성
- [ ] 인사이트 포맷팅
- [ ] 파일 저장
- [ ] 중복 체크
- [ ] DB 상태 업데이트

**Phase 4: Reviewer**
- [ ] 대화형 프롬프트
- [ ] 인사이트 표시 (박스 그리기)
- [ ] 사용자 입력 처리
- [ ] 미리보기 표시
- [ ] 충돌 처리
- [ ] 요약 표시

**공통**
- [ ] 에러 핸들링
- [ ] 로깅
- [ ] 테스트 작성
- [ ] 문서화
- [ ] Git 연동

---

### 다음 단계

1. **MVP (Minimum Viable Product)**
   - Phase 1 (Scanner) 완성
   - 간단한 list 명령어
   - 수동 apply (--id, --skill)

2. **v1.0**
   - Phase 2 (Matcher) 추가
   - Phase 3 (Applier) 완성
   - 기본 review 인터페이스

3. **v2.0**
   - Phase 4 (Review) 고도화
   - 충돌 처리
   - 배치 적용
   - stats/search 명령어

4. **Future**
   - HTML 대시보드
   - Webhook 연동
   - AI 기반 매칭 (Claude API)

---

## Appendix

### References
- [Claude Code Memory Research](~/agent-skills/skills/custom/claude-code-memory-research/)
- [LEARNINGS.md](~/.claude/projects/-Users-kennyhong/memory/LEARNINGS.md)
- [Skills System](~/.claude/skills/)
