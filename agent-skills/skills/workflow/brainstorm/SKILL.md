---
name: brainstorm
description: 브레인스토밍/피드백. 발산-수렴 프레임워크, 아이디어 평가, 구조화된 피드백 루프.
argument-hint: "[topic or problem statement]"
---

# Brainstorm Skill

## Core Rules
- **발산과 수렴을 분리** — 아이디어 생성 중 비판 금지. 평가는 별도 Phase
- **양이 먼저** — 좋은 아이디어는 많은 아이디어에서 나온다. 최소 10개 생성
- **Verify before commit** — 선택된 아이디어는 실현 가능성 검증 후 확정

## Confidence Levels
| Level | 기준 | 행동 |
|-------|------|------|
| 🟢 HIGH | 기존에 검증된 패턴, 유사 사례 성공 이력 | 바로 실행 가능 |
| 🟡 MEDIUM | 논리적으로 타당하나 미검증 | 프로토타입/POC 먼저 |
| 🔴 LOW | 참신하지만 리스크 큼, 사례 없음 | 탐색 가치 있으나 실행 전 검증 필수 |

## Protocol

### Phase 1: Frame — 문제 정의
**Good Questions:**
- 해결하려는 핵심 문제는 무엇인가? (1문장)
- 이 문제가 왜 중요한가? 누구에게?
- 현재 해결 방법은? 왜 부족한가?
- 제약 조건은? (시간, 기술, 예산, 범위)
- 성공 기준은? ("이것이 되면 성공")

**Quality Gate:** 문제 1문장 정의, 제약 조건 명시, 성공 기준 합의

### Phase 2: Diverge — 아이디어 발산
**기법:**
| 기법 | 방법 | 적합한 상황 |
|------|------|-----------|
| **브레인덤프** | 제한 없이 쏟아내기 (최소 10개) | 초기 탐색 |
| **역전 사고** | "이걸 최악으로 만들려면?" → 반전 | 막혔을 때 |
| **유사 매핑** | 다른 분야에서 비슷한 문제 해결 사례 | 차별화 필요 |
| **제약 제거** | "시간/돈/기술 제한 없다면?" | 범위 확장 |
| **SCAMPER** | 대체/결합/적용/수정/다른용도/제거/역전 | 기존 것 개선 |

**규칙:** 이 Phase에서 비판/평가 금지. 양 우선.

### Phase 3: Cluster — 구조화
- 유사 아이디어 그룹핑
- 테마/카테고리 이름 부여
- 중복 합치기, 파생 아이디어 추가

### Phase 4: Converge — 평가/선택
**Impact vs Effort 매트릭스:**
```
          Low Effort    High Effort
High    | ★ Quick Win  | Big Bet     |
Impact  |              |             |
Low     | Fill-in      | Avoid       |
Impact  |              |             |
```

**평가 기준:**
- 핵심 문제 해결에 직결? (Impact)
- 제약 조건 내 실현 가능? (Feasibility)
- 유저 가치 체감 가능? (Value)
- 기존 시스템과 통합 용이? (Compatibility)

**Quality Gate:**
- [ ] 최소 10개 아이디어 생성됨
- [ ] Impact/Effort 평가됨
- [ ] Quick Win 2~3개 식별됨
- [ ] Big Bet 1개 식별됨

### Phase 5: Action — 액션 아이템
**Output Format:**
```markdown
## 브레인스토밍 결과

### 문제 정의
[1문장]

### 아이디어 목록 (N개)
| # | 아이디어 | Impact | Effort | 분류 |
|---|---------|--------|--------|------|
| 1 | [설명]  | H/M/L  | H/M/L  | Quick Win / Big Bet / Fill-in |

### 선정 아이디어 (Top 3)
1. **[이름]** — [이유] (Confidence: 🟢/🟡/🔴)
   - 다음 단계: [구체적 액션]

### 탐색 대기 (미검증)
- [아이디어]: [검증 필요 사항]
```

## Memory Integration
- 완료 후: 선정된 아이디어 → `/design` 또는 `/user-research`로 핸드오프
