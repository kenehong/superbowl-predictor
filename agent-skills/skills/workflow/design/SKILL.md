---
name: design
description: UI/UX 디자인 프로세스. 3-Agent 분석, 비주얼 계층, 반응형. UI 빌드 시 자동 사용.
argument-hint: "[project or component name]"
---

# Design Skill

## Core Rules
- **유저 중심** — 예쁜 것보다 쓰기 쉬운 것. 기능이 디자인을 이끈다
- **Verify before apply** — 디자인 결정에 근거 필요 (유저 선호, 경쟁사 패턴, 접근성 기준)
- **센터 레이아웃 필수** — max-width + margin:0 auto + 좌우 패딩. 왼쪽 치우침 금지
- **Figma spec 우선** — Figma 데이터에 값이 있으면 그대로 사용, 추측 금지 (→ figma-to-code.md)

## Confidence Levels
| Level | 기준 | 행동 |
|-------|------|------|
| 🟢 HIGH | 유저 피드백 기반 선호, 검증된 디자인 패턴 | 바로 적용 |
| 🟡 MEDIUM | 경쟁사에서 본 패턴, 일반적 UX 원칙 | 적용하되 근거 명시 |
| 🔴 LOW | 개인 취향, 트렌드 따라하기 | 유저에게 선택지 제시, 임의 적용 금지 |

## Protocol

### Phase 1: Understand — 유저 니즈 파악
**Good Questions:**
- 이 화면의 핵심 액션은 무엇인가? (1가지)
- 유저가 이 화면에서 가장 먼저 봐야 할 것은?
- 유저가 이미 알고 있는 정보 vs 새로 보여줘야 할 정보?
- 모바일에서 어떻게 달라져야 하는가?
- Figma 디자인 파일이 있는가? → figma-to-code.md 참조

**Quality Gate:** 핵심 액션 1개, 정보 우선순위 정의됨

### Phase 2: Structure — 정보 구조
- 정보 계층: 요약 → 상세 순
- 그룹핑: 관련 정보끼리 시각적으로 묶기
- 플로우: 유저의 시선 흐름 (위→아래, 왼→오른)
- WinUI 3: NavigationView, TitleBar, 백드롭 패턴 → ui-ux.md 참조

### Phase 3: 3-Agent 병렬 분석
| Agent | Focus | 핵심 질문 |
|-------|-------|----------|
| **UX** | 인터랙션, 입력 최소화 | 클릭 몇 번으로 결과 도달? 자동 채움 가능한 값? |
| **Design** | 시각 계층, 간격, 정렬 | 계층이 명확한가? 반응형 깨지는 곳? |
| **Brand** | 컬러, 톤, 무드 | 카테고리에 맞는 Primary 컬러? 대시보드 vs 앱 톤? |

### Phase 4: Visual Design
**기본 원칙:**
- 시스템 테마 (prefers-color-scheme) 기본 — OS 설정 따름
- shadcn/ui 스타일 참고: 클린한 border, 적절한 radius, 미니멀 색상
- 팔레트: oklch 기반
- 폰트: Inter + JetBrains Mono
- 레이아웃: 센터 배치 + 프로젝트 타입별 max-width
- 카테고리별 Primary: 금융=Blue, 교육=Green, 미디어=Red, 의학=Purple 등

**Spacing (빽빽한 레이아웃 금지):**
- 섹션 간: `gap: 1.25rem`+
- 카드/블록 내부: `padding: 0.75rem`+
- 스택 요소 간: `gap: 0.5rem`+
- 인라인 요소 간: `gap: 0.25rem`+
- 헤더/타이틀 아래: `margin-bottom: 0.5rem`+

**Figma 구현 시:**
- figma-to-code.md의 Step 1~4 따르기
- Deep Fetch (depth 6+) → Extract → Build with exact values → Verify
- Figma spec > Reference rules > 개인 경험

### Phase 5: Review — 피드백 반영
**Quality Gate:**
- [ ] 센터 레이아웃 적용됨
- [ ] 모바일 반응형 (sm/md/lg 브레이크포인트)
- [ ] 정보 계층 명확 (요약→상세)
- [ ] Spacing 충분 — 섹션 간 2rem+, 카드 내부 1.5rem+, 스택 요소 1rem+
- [ ] 에러/빈 상태 UI 존재
- [ ] 유저 선호 패턴 위반 없음
- [ ] Figma 구현 시: 값 비교 완료 (spacing, size, alignment, color)

## Output Format
```
디자인 결정 요약:
- 레이아웃: [타입] + [max-width]
- 팔레트: [카테고리] → [Primary 컬러]
- 핵심 컴포넌트: [목록]
- 반응형: [브레이크포인트별 변화]
```

## Design Engineering — 5대 원칙

### 1. 레이아웃 시프트 금지
- 숫자: `font-variant-numeric: tabular-nums` (고정 폭)
- 이미지/카드: 고정 높이 또는 aspect-ratio 지정
- 로딩 상태: skeleton과 실제 컨텐츠 크기 일치

### 2. 터치 우선, 호버 보강
- 최소 탭 대상: `44px × 44px`
- 호버 효과: `@media (hover: hover)` 안에서만
- 스와이프/제스처보다 명시적 버튼 우선

### 3. 키보드 네비게이션
- Tab 순서 논리적 유지
- 모달/드롭다운: 포커스 트랩 + ESC로 닫기
- 커스텀 컨트롤에 `tabindex`, `role` 속성

### 4. 접근성 기본값
- `prefers-reduced-motion: reduce` 시 애니메이션 제거
- 인터랙티브 요소에 `aria-label` (아이콘 버튼 필수)
- 컬러만으로 정보 전달 금지 (아이콘/텍스트 병행)
- WinUI 3: `AutomationProperties.Name`, F6 네비게이션 → ui-ux.md 참조

### 5. 속도 > 화려함
- Product UI: 빠르고 목적성 있게. 불필요한 애니메이션 금지
- 트랜지션: `150ms ease-out` (기본), `200ms` (복잡한 전환)
- 대량 리스트: 가상화 (virtualization) 고려

## Animation Quick Ref
| 용도 | Duration | Easing |
|------|----------|--------|
| 호버/포커스 | 100-150ms | ease-out |
| 진입 | 150-250ms | ease-out |
| 퇴출 | 100-200ms | ease-in |
| 페이지 전환 | 200-350ms | ease-in-out |

## Memory Integration
- UI 규칙은 CLAUDE.md 참조 (shadcn 스타일, 시스템 테마, Spacing)
