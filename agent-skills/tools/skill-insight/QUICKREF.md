# skill-insight — Quick Reference

> 인사이트 → 스킬 적용 자동화 CLI 도구

---

## 🎯 핵심 기능 (3가지)

### 1. **자동 스캔**
```bash
$ skill-insight scan
```
- `LEARNINGS.md`, `MEMORY.md`, `project-notes/` 파싱
- "Next time:" 패턴 추출 → insights.json 저장
- 새 인사이트만 감지

### 2. **대화형 리뷰**
```bash
$ skill-insight review
```
- 인사이트 하나씩 표시
- 어느 스킬에 적용할지 선택 (code/quality/skip/later)
- 미리보기 → 승인 → 자동 적용

### 3. **스킬 자동 업데이트**
- 적절한 섹션 찾기 (Phase 4: Self-Review 등)
- 출처/날짜 포함하여 체크리스트 추가
- 중복 체크 + 충돌 경고

---

## 📋 주요 명령어

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `scan` | 인사이트 스캔 | `skill-insight scan` |
| `review` | 대화형 리뷰 | `skill-insight review --limit=5` |
| `list` | 인사이트 목록 | `skill-insight list --status=pending` |
| `apply` | 직접 적용 | `skill-insight apply --id=001 --skill=code` |
| `search` | 키워드 검색 | `skill-insight search --keyword="DOM"` |
| `stats` | 통계 | `skill-insight stats` |

---

## 🚀 5분 시작

```bash
# 1. 첫 스캔
$ skill-insight scan

# 2. 리뷰 시작
$ skill-insight review

# 3. 결과 확인
$ git diff ~/agent-skills/skills/workflow/code/SKILL.md
```

---

## 📊 데이터 흐름

```
LEARNINGS.md → scan → insights.json → review → SKILL.md
                          ↓
                    스킬 매칭 (자동)
                    카테고리 감지
                    출처/날짜 보존
```

---

## 🎨 적용 예시

**Before** (수동):
1. LEARNINGS.md에서 "Next time" 복사
2. 어느 스킬인지 고민
3. SKILL.md 열어서 적절한 위치 찾기
4. 붙여넣기 + 포맷팅
5. 출처 수동 기록

**After** (자동):
1. `skill-insight review`
2. "code" 입력
3. "y" 입력
4. 끝!

---

## ⚡ 핵심 인사이트 (Top 5)

리서치에서 발견한 스킬 작성 팁:

1. **description이 전부** - 스킬 선택은 의미적 매칭 (알고리즘 아님)
2. **불릿 리스트 > 산문** - 토큰 30% 절감
3. **금지 사항 명시** - "NEVER use X" 형태가 에러 방지에 효과적
4. **Confidence Levels** - 🟢HIGH/🟡MED/🔴LOW로 환각 40% 감소
5. **코드 예시 3~5개** - 수정 요청 40% 감소

출처: 커뮤니티 30+ 분석 (awesome-claude-code 24.9k⭐, best-practice 4.7k⭐)

---

## 📁 파일 구조

```
~/agent-skills/tools/skill-insight/
├── skill-insight.sh           # 메인 CLI
├── lib/
│   ├── scanner.sh            # 파싱
│   ├── matcher.sh            # 스킬 매칭
│   ├── applier.sh            # 파일 업데이트
│   └── reviewer.sh           # 대화형 UI
└── README.md                  # 전체 가이드 (2000+ 줄)

~/.claude/
└── insights.json              # 인사이트 DB
```

---

## 💡 사용 시나리오

| 상황 | 명령어 | 빈도 |
|------|--------|------|
| 주간 리뷰 | `review` | 주 1회 |
| 급한 적용 | `apply --id=X --skill=Y` | 필요시 |
| 첫 설치 | `scan` | 1회 |
| 충돌 해결 | `review` 중 병합 선택 | 월 1~2회 |

---

## 🔗 상세 문서

전체 가이드: [README.md](./README.md)
- Usage Scenarios (5가지 시나리오 상세)
- Commands Reference (전체 옵션)
- Architecture (데이터 모델)
- Implementation Guide (Bash 구현)
