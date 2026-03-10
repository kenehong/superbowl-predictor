# Setup Guide: PM Spec Writing Skill for GitHub Copilot CLI

This guide walks you through setting up the **PM Spec Writing Skill** — an interactive, 8-phase workflow that helps you write polished product manager specs using GitHub Copilot CLI. The skill guides you through discovery, research, planning, drafting, and polishing — so you never start from a blank page.

**This skill installs globally** — once set up, it's available from any folder, in any project. When it's time to save the finished spec, it asks you where to put it.

> **Already using Claude Code?** A separate setup guide exists for Claude Code in the parent `PMSpecWritingArtifacts` folder. Both can coexist — they use different config directories.

---

## For AI Assistants (Copilot, Claude Code, etc.)

If a user asks you to "set up the PM spec writing skill" or "follow this setup guide", do the following:

### Step A: Read the guide
Read this entire setup guide first to understand the folder structure and file placement.

### Step B: Ask the user these questions (one at a time, before creating any files)

Use the friendly phrasing below — don't just ask for technical values.

1. **Team name** — *"What's your team's name? This shows up in specs as the author team — for example, 'the Windows Experiences team' or 'the Surface Design team'."*
   - Replaces `<YOUR TEAM NAME>` in: **SKILL.md**, **copilot-instructions.md**, and **spec-writing-guide.md**

2. **Terminology preferences** — *"When your team talks about the people who use your product, do you say 'customer', 'user', or something else? And when you refer to people outside your company — partners, enterprises, consumers — what term do you use?"*
   - Update the terminology rules in **copilot-instructions.md** and **spec-writing-guide.md** to match

3. **Default save location** — *"Where do you usually keep your specs and documents? Give me a folder path — for example, `C:\Users\you\Documents\Specs` or `~/Documents/ProductSpecs`. This becomes the default location when a spec is saved, but you can always pick a different spot each time you write one."*
   - Replaces `<DEFAULT SPEC FOLDER>` in **SKILL.md**

4. **Spec template review** — Show the user the 11-section template from `PMSpecTemplate.md`:
   > The default template has these 11 sections:
   > 1. Overview, 2. Problem Statement, 3. Goals & Non-Goals, 4. Target Customers,
   > 5. Current Experience (Baseline), 6. Proposed Solution, 7. User Experience Principles,
   > 8. Experience Flow (High-Level), 9. What Changes vs Today, 10. Success Metrics,
   > 11. Impact Estimate (Directional)

   Then ask: *"Does this template work for the specs you write? Are there any sections you'd want to add — for example, 'Technical Constraints', 'Accessibility', 'Internationalization', or something specific to your product area? Or any sections you'd want to remove?"*
   - If the user wants changes, update **PMSpecTemplate.md** accordingly

5. **Discovery questions review** — Show the user the existing question bank from `discovery-questions.md`. The default questions cover:
   > **Batch 1:** Who is the audience? What's the core problem? Why now?
   > **Batch 2:** What's being built? Timeline and dependencies? Existing docs? What's out of scope?
   > **Optional follow-ups:** Platform coverage, competitive context, success definition, risks, stakeholder alignment

   Then ask: *"These are the questions the skill asks you every time you start a new spec. Are there any questions specific to your product area that should always be asked — for example, 'Which platforms does this affect (Android, iOS, Windows)?', 'Is there a privacy review needed?', or 'Does this require a feature flag?'"*
   - If the user provides additions, add them under the "Add Your Own Domain-Specific Questions Below" section in **discovery-questions.md**

6. **Gold-standard example spec** — *"Do you have a spec your team considers the 'gold standard' — one that represents the quality and depth you want? If so, share the file path. Otherwise, I'll use the sample example spec included in this kit — you can replace it later with your own."*

### Step C: Create the folder structure and copy files
1. Create the global skill folder at `~/.copilot/skills/write-pm-spec/` (and `references/` inside it).
2. Copy each artifact file from this folder to the correct destination (see the table in "Files Included in This Artifacts Folder" below).
3. If the user provided a gold-standard spec, copy it into the skill's `references/` folder and update the filename in SKILL.md (Setup section, item 4).

### Step D: Apply all customizations
Replace placeholders and apply the user's answers across **all** affected files:
- `<YOUR TEAM NAME>` → user's team name in **SKILL.md**, **copilot-instructions.md**, and **spec-writing-guide.md**
- `<DEFAULT SPEC FOLDER>` → user's default save location in **SKILL.md**
- Terminology rules → update in **copilot-instructions.md** and **spec-writing-guide.md**
- Template changes → update in **PMSpecTemplate.md**
- Domain-specific questions → add to **discovery-questions.md**

### Step E: Verify the setup
List the created files and confirm the folder structure matches what's described in Step 1 below. Read back the key customized values (team name, default save path, any template/question changes) so the user can confirm everything looks right.

---

## What You Get

Once set up, you can ask Copilot to "write a spec" from **any folder** and it will:

1. **Intake your topic** and ask for your initial thinking
2. **Interview you** with structured discovery questions (in two batches)
3. **Search your emails, meetings, and chats** for context (optional — requires WorkIQ)
4. **Read strategy docs and reference files** you point it to
5. **Let you pick a template** (a default 11-section template is included)
6. **Present a section-by-section plan** for your approval before writing
7. **Draft the full spec** following your approved plan, template, and style rules
8. **Ask you where to save** the finished spec — you choose the folder at draft time
9. **Polish and iterate** with you, then run a quality checklist

---

## Prerequisites

- **GitHub Copilot CLI** installed and running — [https://docs.github.com/en/copilot/github-copilot-in-the-cli](https://docs.github.com/en/copilot/github-copilot-in-the-cli)
- (Optional) **WorkIQ MCP server** connected for automatic research from your M365 data

---

## Step-by-Step Setup

### Step 1: Create the folder structure

The skill installs in your **home directory** so it's available globally — you don't need to be in a specific project folder.

**On Windows:**
```
C:\Users\<you>\.copilot\
  skills\
    write-pm-spec\
      SKILL.md                                         <-- Skill definition (Step 2)
      references\
        copilot-instructions.md                        <-- Tone, terminology, structure rules (Step 3)
        spec-writing-guide.md                          <-- Writing guidance + checklist (Step 3)
        discovery-questions.md                         <-- Question bank (Step 3)
        PMSpecTemplate.md                              <-- Spec template (Step 3)
        Example Gold-Standard Spec.md                  <-- Example spec (Step 4)
```

**On macOS / Linux:**
```
~/.copilot/
  skills/
    write-pm-spec/
      SKILL.md
      references/
        copilot-instructions.md
        spec-writing-guide.md
        discovery-questions.md
        PMSpecTemplate.md
        Example Gold-Standard Spec.md
```

> **Why global?** Unlike a project-level setup (`.github/skills/`), a global skill loads automatically in every Copilot session regardless of which folder you're in. The skill asks you where to save the spec when it's time to write — so you can store it wherever makes sense for that particular spec.

### Step 2: Add SKILL.md (skill definition)

Copy **`SKILL.md`** from this artifacts folder into `~/.copilot/skills/write-pm-spec/`.

**Customize it:**
- Update the **team name** in the opening line ("You are a product manager spec writing assistant for [your team]")
- Update the **Org / Team** in Phase 7 to your team name
- If you don't have WorkIQ, leave Phase 3 as-is — the skill gracefully falls back to asking you to paste context manually

### Step 3: Add reference files

Copy all of these files from this artifacts folder into `~/.copilot/skills/write-pm-spec/references/`:

- **`copilot-instructions.md`** — Tone, terminology, and structure rules that Copilot follows when writing
- **`spec-writing-guide.md`** — Section-by-section writing guidance, quality principles, and the quality checklist used in Phase 8
- **`discovery-questions.md`** — The structured question bank used in Phase 2
- **`PMSpecTemplate.md`** — The 11-section spec template

**Customize them:**
- In `copilot-instructions.md`, update the team name, terminology, and tone preferences
- In `spec-writing-guide.md`, update the **Tone & Terminology Rules** section at the bottom to match
- In `discovery-questions.md`, add domain-specific questions relevant to your product area under the "Optional Follow-Ups" section
- In `PMSpecTemplate.md`, add, remove, or rename sections to match your team's spec format

### Step 4: Add a gold-standard example spec

This is the most impactful customization. The skill uses an example spec as a quality benchmark — matching its length, depth, and style when writing your draft.

**What to do:**
- Pick the best spec your team has written — one that represents the quality bar you want
- Save it as a markdown file in `~/.copilot/skills/write-pm-spec/references/`
- Update the filename in `SKILL.md` (Setup section, item 4) to match

A sample gold-standard spec (**`Example Gold-Standard Spec.md`**) is included in this artifacts folder. It demonstrates the 11-section template fully filled out. Replace it with your own when you have one.

### Step 5: (Optional) Connect WorkIQ

WorkIQ is an MCP server that lets GitHub Copilot search your Microsoft 365 emails, meetings, and chats. This powers Phase 3 of the skill — automatic research.

**To set it up:**
- Follow the WorkIQ MCP server setup instructions for GitHub Copilot CLI
- Once connected, the skill will automatically offer to search your M365 data during Phase 3

**Without WorkIQ:**
- The skill still works. In Phase 3, it will ask you to paste context or point to files instead.

---

## How to Use

Once everything is set up:

1. Open GitHub Copilot CLI **from any folder**
2. Ask Copilot to write a spec — for example:
   - `write a spec for adding dark mode to the settings page`
   - `write-pm-spec: Introduce push notification opt-in during onboarding`
   - Or simply say "I want to write a PM spec" and the skill will activate
3. Follow the 8-phase interactive workflow
4. When the draft is ready, Copilot will ask: **"Where would you like me to save this spec?"** — give it a folder path and file name
5. Continue iterating until the spec passes the quality checklist

**Tips for best results:**
- **Bring your thinking.** The more context you share in Phase 1 and 2, the stronger the draft.
- **Point to existing docs.** Strategy decks, prior specs, research reports — Copilot reads them and incorporates insights.
- **Use WorkIQ.** If connected, it finds decisions, feedback, and data you may have forgotten about.
- **Review the plan (Phase 6) carefully.** This is your chance to steer the spec before the full draft is written.
- **Iterate in Phase 8.** Ask for section-by-section revisions. The skill will run a quality checklist at the end.

---

## Files Included in This Artifacts Folder

| File | Purpose | Goes to |
|---|---|---|
| `Setup Guide - PM Spec Writing Skill for GitHub Copilot CLI.md` | This document | Share with your team |
| `SKILL.md` | Skill definition (the 8-phase workflow) | `~/.copilot/skills/write-pm-spec/` |
| `copilot-instructions.md` | Tone, terminology, structure rules | `~/.copilot/skills/write-pm-spec/references/` |
| `spec-writing-guide.md` | Section-by-section writing guidance + quality checklist | `~/.copilot/skills/write-pm-spec/references/` |
| `discovery-questions.md` | Structured discovery question bank | `~/.copilot/skills/write-pm-spec/references/` |
| `PMSpecTemplate.md` | The 11-section spec template | `~/.copilot/skills/write-pm-spec/references/` |
| `Example Gold-Standard Spec.md` | A fully written example spec (quality benchmark) | `~/.copilot/skills/write-pm-spec/references/` |

---

## Customization Checklist

Use this to verify the setup is complete. If an AI assistant set this up for you, everything below should already be done.

- [ ] **Team name** is correct in **SKILL.md**, **copilot-instructions.md**, and **spec-writing-guide.md**
- [ ] **Terminology** (customer vs user, etc.) matches your team's conventions in **copilot-instructions.md** and **spec-writing-guide.md**
- [ ] **Default spec save location** is set in **SKILL.md** (Phase 7)
- [ ] **Spec template** sections match what your team needs in **PMSpecTemplate.md**
- [ ] **Discovery questions** include any domain-specific additions in **discovery-questions.md**
- [ ] **Gold-standard example spec** is either your own or the included sample
- [ ] (Optional) **WorkIQ** or another research MCP server is connected

---

## Troubleshooting

**"The skill doesn't appear or Copilot doesn't recognize write-pm-spec"**
- Make sure `SKILL.md` is in `~/.copilot/skills/write-pm-spec/` (exact path matters)
- On Windows, `~` means `C:\Users\<your username>\`
- Make sure the file starts with the YAML frontmatter block (the `---` delimited section at the top)

**"Copilot can't find the template or reference files"**
- Check that the reference files are in `~/.copilot/skills/write-pm-spec/references/`
- The SKILL.md uses relative paths (`references/...`) so the files must be in that subfolder

**"WorkIQ isn't working"**
- Verify the WorkIQ MCP server is connected in your Copilot CLI configuration
- If it fails to connect, the skill will gracefully fall back to manual context gathering

**"The output tone doesn't match our team's style"**
- Update `references/copilot-instructions.md` with more specific tone guidance
- Replace the gold-standard example spec with one that better represents your desired style

---

## Differences from the Claude Code Setup

If you're familiar with the Claude Code version of this skill, here's what changed:

| Aspect | Claude Code | GitHub Copilot CLI |
|---|---|---|
| **Install location** | Project-level: `.claude/skills/write-pm-spec/` | Global: `~/.copilot/skills/write-pm-spec/` |
| **Instructions file** | `CLAUDE.md` (project root) | `references/copilot-instructions.md` (bundled with skill) |
| **Availability** | Only in the project that has `.claude/` | Every Copilot session, any folder |
| **Spec save location** | Fixed project subfolder | User chooses at draft time |
| **WorkIQ tool name** | `mcp__workiq__ask_work_iq` | `workiq-ask_work_iq` |

The workflow, template, reference files, and example spec are identical. Both setups can coexist.
