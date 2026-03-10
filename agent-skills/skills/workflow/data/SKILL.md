---
name: data
description: 데이터 분석/시각화. 수집, 정제, 분석, Chart.js 시각화, 인사이트 도출.
argument-hint: "[data source or analysis topic]"
---

# Data Skill

## Core Rules
- **Data first, opinion later** — 데이터 없이 결론 내리지 않음
- **Verify the source** — 데이터 출처와 수집 시점 명시. 오래된 데이터 경고
- **Visualize for clarity** — 표보다 차트, 차트보다 핵심 숫자 1개

## Confidence Levels
| Level | 기준 | 행동 |
|-------|------|------|
| 🟢 HIGH | 공식 API/DB, 샘플 충분, 교차 검증됨 | 결론에 활용 |
| 🟡 MEDIUM | 단일 소스, 샘플 적음, 시점 오래됨 | "제한적 데이터" 명시 |
| 🔴 LOW | 추정, 비공식, 수동 수집, 미검증 | 참고용으로만. 결론 도출 금지 |

## Protocol

### Phase 1: Define — 분석 목적 정의
**Good Questions:**
- 이 분석으로 어떤 의사결정을 하려는가?
- 핵심 지표(KPI)는 무엇인가?
- 비교 대상이 있는가? (기간별, 그룹별, 경쟁사별)
- 데이터 소스는 어디인가? (API, 파일, 수동 입력)
- 실시간 업데이트가 필요한가 vs 스냅샷?

**Quality Gate:** 핵심 질문 정의됨, 데이터 소스 확인됨

### Phase 2: Collect — 데이터 수집
**소스별 패턴:**
| 소스 | 방법 | 주의 |
|------|------|------|
| REST API | fetch + CORS proxy fallback | 2개+ proxy, 수동 입력 폴백 |
| JSON/CSV | 인라인 임베드 (file:// 환경) | 5MB localStorage 제한 |
| 수동 입력 | 폼 UI | 유효성 검증 필수 |
| WebSearch | 멀티 에이전트 병렬 | 출처 명시 |

**Quality Gate:**
- [ ] 데이터 완전성 (누락 항목 체크)
- [ ] 데이터 형식 일관성 (숫자, 날짜, 단위)

### Phase 3: Clean — 정제
- 누락값 처리 (제외 vs 대체 vs 표기)
- 이상치 확인 (범위, 분포)
- 단위 통일 (%, 원, 달러)
- 날짜 형식 통일

### Phase 4: Analyze — 분석
**분석 유형:**
| 목적 | 방법 | 차트 |
|------|------|------|
| 추세 | 시계열 비교 | Line chart |
| 구성 | 비율, 분포 | Pie/Donut, Stacked bar |
| 비교 | 항목 간 차이 | Bar chart, Grouped bar |
| 관계 | 상관, 인과 | Scatter plot |
| 순위 | 크기 비교 | Horizontal bar |

**Chart.js 설정:**
```javascript
Chart.defaults.color = 'oklch(0.65 0.01 260)';
Chart.defaults.borderColor = 'oklch(0.25 0.02 260)';
```

### Phase 5: Insight — 인사이트 도출
**Output Format:**
```markdown
## 데이터 분석 결과

### 핵심 발견 (Top 3)
1. [숫자] — [의미] (🟢 HIGH)
2. [숫자] — [의미] (🟡 MEDIUM)
3. [숫자] — [의미] (Confidence)

### 상세 분석
[차트 + 설명]

### 데이터 제한사항
- 데이터 소스: [출처]
- 기간: [시작~끝]
- 샘플 크기: [N]
- 알려진 편향: [있으면 명시]

### 권고
[데이터 기반 액션 아이템]
```

**Quality Gate:**
- [ ] 모든 숫자에 단위 표기
- [ ] 차트 제목 + 축 레이블 존재
- [ ] Confidence level 명시
- [ ] 데이터 제한사항 고지

## Memory Integration
- 차트 테마: CLAUDE.md UI 규칙 따름 (시스템 테마, oklch)
