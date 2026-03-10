---
name: research
description: 멀티 에이전트 병렬 리서치. 주제 깊이 분석, 출처 검증, 반론 포함. 리서치 요청 시 자동 사용.
argument-hint: "[research topic]"
---

# Research Skill

## Core Rules
- **Verify before execute** — 출처 없는 주장 금지. 모든 정보에 출처 명시
- **Evidence-based only** — 추측/의견이 아닌 데이터와 근거로 판단
- **Counterarguments required** — 한쪽 시각만 제시 금지. 반론 필수 포함

## Confidence Levels
| Level | 기준 | 행동 |
|-------|------|------|
| 🟢 HIGH | 학술지/기관 보고서, 복수 출처 교차 확인됨 | 보고서에 포함, 근거로 활용 |
| 🟡 MEDIUM | 단일 신뢰 출처, 논리적 추론 | 포함하되 "단일 출처" 명시 |
| 🔴 LOW | 블로그/SNS, 미확인, 추정 | 포함하되 "미검증" 경고. 핵심 결론에 사용 금지 |

## Protocol

### Phase 1: Scope — 스코프 정의
**Good Questions:**
- 이 리서치의 핵심 질문은 무엇인가?
- 누가 이 결과를 사용하는가? (의사결정자 vs 학습 목적)
- 어떤 형태의 결론이 필요한가? (비교, 추천, 현황 파악)
- 이미 알고 있는 것은? 모르는 것은?

**Action:** 주제를 3개+ 독립적 서브토픽으로 분할
**Quality Gate:** 서브토픽 간 겹침 없음, 각각 명확한 범위

### Phase 2: Assign — 에이전트 배정
**분할 패턴:**
| 유형 | Agent 1 | Agent 2 | Agent 3 |
|------|---------|---------|---------|
| 질병 | 원인/진행 | 치료법 | 보조요법/영양 |
| 기술 | 현황/원리 | 구현 방법 | 비교/대안 |
| 시장 | 규모/동향 | 경쟁사 | 기회/전략 |
| 인물 | 배경/업적 | 방법론 | 영향/비판 |

**Execution:** `subagent_type: general-purpose` + `run_in_background: true`
**각 에이전트 공통 지시:**
- 한국어 작성
- 반드시 출처(URL) 명시
- 반론 및 논쟁점 포함
- 구체적 통계/수치
- 근거 강도 명시 (강함/중간/예비/일화적)

### Phase 3: Collect — 수집 및 교차 검증
**Quality Gate:**
- [ ] 모든 에이전트 완료
- [ ] 각 결과에 출처 3개 이상
- [ ] 상충 정보 식별 완료

### Phase 4: Synthesize — 통합
- 교차 검증: 에이전트 간 상충 정보 → 어느 출처가 더 신뢰할 수 있는지 판단
- 출처 신뢰도: 학술지 > 정부/기관 > 뉴스 > 블로그/SNS
- 반론 통합: 찬/반 균형 있게 정리

### Phase 5: Report — 보고서 작성
**Output Format:**
```markdown
# [주제] 종합 리서치 보고서
> 작성일: YYYY-MM-DD | 출처: N개

## 핵심 요약 (3-5줄)
## 본문 (섹션별, 출처 각주)
## 논쟁점 및 반론 (찬/반 정리)
## 결론 및 권고
## 참고문헌 ([번호] 제목 - URL)
```

**Quality Gate:**
- [ ] 모든 주장에 출처 있음
- [ ] 반론 섹션 존재
- [ ] LOW confidence 정보가 결론에 사용되지 않음
- [ ] 참고문헌 10개 이상

**HTML Report (Optional):**
After user confirmation, convert to HTML using `~/claude/design-system/research-report-template.html`:
- Structure: Executive Summary → Background → Analysis → Findings → Implications → Conclusion
- Source tiers: 🟢 Tier 1 (Primary), 🔵 Tier 2 (Secondary), ⚫ Tier 3 (Tertiary)
- Confidence badges: HIGH/MEDIUM/LOW
- Save to: `~/claude/_report/[topic]-report/` or `~/claude/_invest/[topic]-report/`

## Memory Integration
- 저장: `claude/<topic>-report/`
