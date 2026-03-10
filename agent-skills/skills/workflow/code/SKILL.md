---
name: code
description: 코드 작성/리뷰 표준. 보안, 패턴, 성능, 유지보수성. 코드 작성 및 리뷰 시 자동 사용.
argument-hint: "[file path or feature name]"
---

# Code Skill

## Core Rules
- **검증된 패턴 우선** — 아래 체크리스트의 검증된 패턴 적용. 새 패턴은 검증 후 적용
- **보안 최우선** — XSS, injection, CORS 문제 사전 차단. innerHTML에 유저 데이터 직접 삽입 금지
- **Verify before commit** — 변경 후 전체 리뷰. 스코프, 핸들러 충돌, DOM 포커스 확인

## Confidence Levels
| Level | 기준 | 행동 |
|-------|------|------|
| 🟢 HIGH | 테스트 통과, 기존 코드에서 검증됨 | 바로 적용 |
| 🟡 MEDIUM | 공식 문서 기반, 단일 프로젝트에서 사용 | 적용하되 주석으로 출처 |
| 🔴 LOW | Stack Overflow 답변, 미테스트, 추측 | 적용 금지. 먼저 검증 |

## Protocol

### Phase 1: Analyze — 요구사항 분석
**Good Questions:**
- 이 기능의 입력과 출력은 무엇인가?
- 기존 코드에 비슷한 패턴이 있는가? (grep 확인)
- 이 변경이 영향을 주는 다른 함수/컴포넌트는?
- file:// 환경 제약이 있는가? (fetch 차단 등)
- 에러 상황에서 어떻게 동작해야 하는가?

**Quality Gate:** 입/출력 정의됨, 영향 범위 파악됨

### Phase 2: Pattern — 패턴 선택
**검증된 패턴 체크리스트:**
- [ ] localStorage → `loadState()/saveState()` + try/catch + 5000자 제한
- [ ] Claude API → `anthropic-dangerous-direct-browser-access` 헤더
- [ ] 외부 fetch → CORS proxy 2개+ fallback
- [ ] 유저 입력 표시 → `escapeHtml()` XSS 방지
- [ ] innerHTML 교체 → DOM focus 복원 패턴
- [ ] 이벤트 → 이벤트 위임 (data-* attribute)
- [ ] 숫자 → `fI()`, `fC()`, `pN()` 포맷 유틸

### Phase 3: Implement — 구현
- 간결 실용적. 불필요한 추상화 금지
- 에러 상태 처리 포함 (빈 입력, 네트워크 실패, 파싱 에러)
- 변수 네이밍: 의미 명확, 축약은 관행적인 것만 (e.g., `el`, `btn`, `idx`)

### Phase 4: Self-Review — 셀프 리뷰
**Security Checklist:**
- [ ] innerHTML에 escapeHtml 적용됨
- [ ] API 키가 코드에 하드코딩되지 않음
- [ ] URL 파라미터 sanitize됨
- [ ] localStorage에 민감 정보 평문 저장 안 됨

**Quality Checklist:**
- [ ] 변경된 함수의 모든 호출처 확인 (grep)
- [ ] DOM 교체 시 focus/selection 복원
- [ ] 이벤트 핸들러 중복 등록 없음
- [ ] 모바일에서 터치 이벤트 정상 동작

### Phase 5: Refactor — 정리
- 중복 코드 → 유틸 함수 추출 (3회 이상 반복 시에만)
- 매직 넘버 → 상수로 추출
- 불필요한 주석 제거 (코드가 자명한 경우)

## Output Format
```
변경 요약:
- 수정 파일: [경로:라인]
- 패턴 사용: [적용된 패턴]
- 보안 체크: [통과/이슈]
- 영향 범위: [관련 함수/컴포넌트]
```

## Memory Integration
- 기존 프로젝트: `project-notes/` 먼저 확인
