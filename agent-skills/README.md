# agent-skills

AI agent workspace — skills, agents, and deployment infrastructure for Claude Code, Codex CLI, and GitHub Copilot.

## Structure

```
├── AGENTS.md              # Global agent protocol
├── agents/                # Standalone agent definitions (.md)
├── skills/
│   ├── workflow/          # Methodology & process skills (brainstorm, code, design, etc.)
│   ├── custom/            # One-off, personal skills
│   └── marketplace/       # Production-grade, reusable skills
├── prompts/               # Shared slash commands
├── scripts/               # Deployment & tooling
│   ├── setup.ps1          # Windows setup entry point
│   ├── ai-agent-links.json    # Symlink manifest
│   ├── skills-manifest.json   # External skill registry
│   └── lib/               # Helper scripts
├── .claude/               # Claude Code settings
├── .codex/                # Codex CLI config + agent .toml files
└── docs/                  # Reference documentation
```

## Setup

```powershell
# Full install (deps + symlinks)
.\scripts\setup.ps1 install

# Link AI agent configs only
.\scripts\setup.ps1 link-ai-agents

# Check status
.\scripts\setup.ps1 status

# Update external skills from manifest
.\scripts\setup.ps1 update-skills
```

## Skills

### Workflow (methodology / process)
- **brainstorm** — 발산-수렴 프레임워크, 아이디어 평가, 구조화된 피드백 루프
- **code** — 코드 작성/리뷰 표준. 보안, 패턴, 성능, 유지보수성
- **data** — 데이터 분석/시각화. 수집, 정제, 분석, Chart.js 시각화
- **design** — UI/UX 디자인 프로세스. 3-Agent 분석, 비주얼 계층, 반응형
- **quality** — QA/테스트. 유저 플로우 시뮬레이션, 엣지 케이스, 시나리오 테스트
- **research** — 멀티 에이전트 병렬 리서치. 출처 검증, 반론 포함
- **user-research** — 유저 리서치. 페르소나, 저니 맵, 경쟁사 분석
- **ops** — 배포/운영. Git 워크플로우, 배포 전략, 모니터링

### Custom (personal / one-off)
- **screenshot** — Capture app windows for visual feedback
- **doc-coauthoring** — Document co-authoring workflow
- **system-map** — System architecture visualization
- **claude-code-memory-research** — Memory pattern research
- **winui3-csharp-app** — WinUI 3 app development

### Marketplace (production / reusable)
- **pdf** — Read, create, merge, split PDFs
- **docx** — Word document generation
- **xlsx** — Excel spreadsheet creation with formulas
- **pptx** — PowerPoint presentation building
- **mcp-builder** — MCP server scaffolding
- **skill-creator** — Create & evaluate new skills (includes A/B eval framework)

## Agents

15 specialized agents for different roles:

| Agent | Role | Model |
|-------|------|-------|
| developer | Feature implementation with TDD | opus |
| developer-mini | Simpler tasks, faster model | sonnet |
| architect | System design, no code | opus |
| reviewer | Code review on git diffs | sonnet |
| debugger | Systematic bug diagnosis | opus |
| researcher | Online research & evaluation | opus |
| security-auditor | OWASP, secrets, auth review | sonnet |
| performance-engineer | Profiling & optimization | sonnet |
| technical-writer | READMEs, API docs, ADRs | sonnet |
| ux-designer | Design docs, not code | opus |
| ui-polisher | Screenshot → fix → verify | opus |
| code-flow-analyzer | Dead code, over-engineering | sonnet |
| codebase-investigator | Pattern search, data flow | sonnet |
| codebase-reviewer | Full parallel audit | opus |
| git-workflow | PR management, CI fixes | sonnet |

## Eval Framework

The `skill-creator` skill includes a full evaluation pipeline:
- `run_eval.py` — Test skill triggering
- `comparator.md` — Blind A/B comparison
- `grader.md` — Score comparison results
- `analyzer.md` — Post-hoc analysis
- `eval-viewer/` — HTML report generation
