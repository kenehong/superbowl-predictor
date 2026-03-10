# Agent Protocols

- We are working together. I am your colleague, not just "the user" or "the human".
- Maintain a pragmatic outlook as we work, we both win when problems are solved.
- Be real. Use whatever language is appropriate to express yourself.
- Push back, question, and disagree with me so long as you have evidence to do so. In technical discussions, take an extra moment to research what I am asking if it does not appear to be logically sound.
- It is okay to admit you are wrong, we will both make mistakes and learn from them.

## Environment

- Work with parallel subagents where it makes sense.
- Default workspace: `/Users/kennyhong/claude` (Mac).
- Editor: `code <path>`.
- Commits: Conventional Commits (`feat|fix|refactor|build|ci|chore|docs|style|perf|test`).
- PRs: `gh pr view` / `gh pr diff`; no browser URLs.
- Deletes go to trash.
- Bugs: add regression test when appropriate.
- Keep files <= ~500 LOC; split/refactor as needed.
- Prefer end-to-end verification; if blocked, state what is missing.
- New deps: quick health check (recent releases/commits, adoption).
- Before coding: check `docs/` if present, follow links until domain is clear.

## Resource Discovery

Before starting complex tasks, consider:
- Check `~/agent-skills/skills/` for specialized workflows (e.g., kids, research)
- Check `~/agent-skills/agents/` for task delegation options
- Read `@LEARNINGS.md` for past patterns and common mistakes

When you discover non-obvious lessons, append to `~/agent-skills/LEARNINGS.md`.

## Learnings

Global learnings and patterns discovered across all projects:

@LEARNINGS.md

**Project-specific learnings:**
- Track learnings in a `LEARNINGS.md` file at the project root as you work. Read this file before you start.
- Record things like: discovered project conventions, non-obvious gotchas, debugging insights, architectural decisions, and useful commands.
- Keep entries concise - one bullet per learning.
- Before adding a new entry, check for duplicates or outdated entries and update them instead.
- Do not log routine or obvious information - only things that would save time in a future session.

## Git

- When asked to "commit staged changes", commit exactly what is staged - do not stage or unstage files yourself.
- If the staging looks wrong, warn but still follow the instruction.
- Only run `git add -A` or `git add .` if nothing is staged.
- Stage specific files by name when you need to stage.

## App Design Defaults

When building apps in `claude/_tool/`, `claude/_game/`, or standalone HTML apps:

**Design System**:
- Color palette: Neutral grays + primary blue (#0d6efd)
- Auto dark mode via `prefers-color-scheme`
- Typography: System font stack (-apple-system, Pretendard, Segoe UI)
- Spacing: 4px base grid (0.25rem, 0.5rem, 0.75rem, 1rem, 1.5rem, 2rem)
- Border radius: 8px (0.5rem)
- Shadows: Subtle (0 1px 3px rgba(0,0,0,0.1))

**Layout**:
- Max width: 900px centered
- Mobile-first responsive
- Touch targets: 44px minimum
- Padding: 1rem~2rem

**Components**:
- Buttons: 44px+ height, rounded, clear hover/active states
- Inputs: Border + focus ring, label above field
- Cards: Subtle shadow, 1rem padding, rounded

Use CSS variables for consistency. Keep it minimal - only add styling that serves function.

**Reference**:
- Component library: `~/claude/design-system/index.html`
- Research report template: `~/claude/design-system/research-report-template.html`
- Research report skill: `~/agent-skills/skills/custom/research-report/` (source tiers, templates)

## External libs/frameworks

- Prefer existing, well-maintained libraries over custom code when they reduce complexity.
- If multiple good options exist, propose 2-3 with pros/cons and a recommendation.
- Prefer latest library versions unless compatibility concerns.
