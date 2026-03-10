---
name: ops
description: 배포/운영. Git 워크플로우, 배포 전략, 모니터링. 배포 및 인프라 작업 시 사용.
disable-model-invocation: true
argument-hint: "[deploy/setup/status]"
---

# Ops Skill

## Core Rules
- **Verify before deploy** — 로컬 테스트 통과 없이 배포 금지
- **비가역 작업 확인** — force push, 삭제, 환경 변수 변경 전 반드시 유저 확인
- **롤백 계획** — 배포 전 롤백 방법 확인

## Confidence Levels
| Level | 기준 | 행동 |
|-------|------|------|
| 🟢 HIGH | 로컬 테스트 통과, 이전 배포 성공 이력, 변경 범위 명확 | 배포 진행 |
| 🟡 MEDIUM | 코드 리뷰 통과했으나 미테스트, 새 환경 | 유저 확인 후 진행 |
| 🔴 LOW | 미테스트, 의존성 변경, 인프라 변경 | 배포 중단. 테스트 먼저 |

## Protocol

### Phase 1: Assess — 환경 확인
**Good Questions:**
- 어디에 배포하는가? (GitHub Pages, Vercel, static hosting)
- 현재 브랜치 상태는? (clean, uncommitted changes?)
- 환경 변수나 시크릿이 필요한가?
- 이 프로젝트가 Git repo인가? (`MEMORY.md` 확인)
- 마지막 성공 배포는 언제?

**Action:** `git status`, `git log`, 환경 확인
**Quality Gate:** Working directory clean, 브랜치 확인됨

### Phase 2: Build — 빌드 검증
**프로젝트 타입별:**
| 타입 | 빌드 | 검증 |
|------|------|------|
| Single-file HTML | 없음 | 브라우저 열기 + /quality 실행 |
| Node.js | `npm run build` | 에러 없음 + 번들 크기 확인 |
| Static site | 빌드 명령 | 출력 폴더 확인 |

**Quality Gate:**
- [ ] 빌드 에러 0
- [ ] 콘솔 warning 확인

### Phase 3: Deploy — 배포
**Git 워크플로우:**
```
feature branch → PR → review → merge to main → deploy
```
- 커밋 메시지: 목적 중심 ("what" + "why")
- PR: 제목 70자 이내, 요약 + 테스트 계획 포함
- force push 금지 (main/master)
- `--no-verify` 금지

**배포 전략:**
| 플랫폼 | 명령 | 확인 |
|--------|------|------|
| GitHub Pages | `git push` → Settings > Pages | URL 접속 확인 |
| 수동 호스팅 | 파일 업로드 | URL 접속 확인 |

### Phase 4: Verify — 헬스체크
- 배포 URL 접속 확인
- 핵심 기능 1가지 동작 확인
- 콘솔 에러 없음
- 모바일 접속 확인

### Phase 5: Document — 문서화
**Output Format:**
```markdown
## 배포 결과
- 프로젝트: [이름]
- 배포 일시: [날짜]
- URL: [배포 URL]
- 브랜치: [브랜치명]
- 커밋: [hash + 메시지]
- 상태: SUCCESS/FAIL
- 참고: [특이사항]
```

**Action:** `dev-log.md` 업데이트

## Memory Integration
- 참조: `MEMORY.md` (Git repos 목록)
- Git repos: car-calculator, stock-widget, stock-analyzer
