# Spec Writing Guide

Reference instructions for writing high-quality PM specs following the PMSpecTemplate.md structure.

---

## Principles

1. **Clarity over completeness** — A shorter spec that everyone understands beats a long one nobody reads. Cut filler.
2. **Audience awareness** — Assume execs read only the Overview. Engineers read the full spec. Write both layers.
3. **Opinionated, not neutral** — The spec should advocate for a direction. Present the recommendation, not a menu of options.
4. **Grounded in evidence** — Every claim should trace back to data, customer feedback, a decision record, or a strategic directive. Cite sources.

---

## Section-by-Section Guidance

### 1. Overview
- **Purpose:** Executive summary. A reader who stops here should understand what, why, and the core idea.
- **Length target:** 3-5 sentences. One paragraph.
- **Common mistakes:** Too long, too vague, buries the recommendation, uses jargon.
- **Quality signals:** Self-contained, specific, states the problem and solution in plain language.

### 2. Problem Statement
- **Purpose:** Make the reader feel the pain. Establish urgency.
- **Length target:** 3 subsections — What is broken, Why it's painful, Why now.
- **Common mistakes:** Describing symptoms without root cause, missing "why now" signals, no customer voice.
- **Quality signals:** Includes customer quotes or feedback themes, cites specific data or strategy reviews, explains competitive pressure.

### 3. Goals & Non-Goals
- **Purpose:** Align on what success looks like and prevent scope creep.
- **Length target:** 4-6 goals, 3-5 non-goals.
- **Common mistakes:** Goals are vague ("improve the experience"), non-goals are missing or token.
- **Quality signals:** Goals are measurable or observable. Non-goals are specific enough that someone could argue they should be in scope — that's the point.

### 4. Target Customers
- **Purpose:** Name who benefits and describe their context.
- **Length target:** 2-3 personas, each with context, key need, and pain point.
- **Common mistakes:** Too many personas, generic descriptions, no connection to the problem.
- **Quality signals:** Each persona maps to a distinct scenario. Platform differences called out if relevant.

### 5. Current Experience (Baseline)
- **Purpose:** Show the "before" so the "after" is clear.
- **Length target:** Step-by-step flow + friction points.
- **Common mistakes:** Describing the ideal flow instead of the actual flow, glossing over pain points.
- **Quality signals:** Numbered steps a customer would actually take. Friction points are specific and verifiable.

### 6. Proposed Solution
- **Purpose:** Describe what changes at a conceptual level. This is the core of the spec.
- **Length target:** 1-2 pages. Tables help.
- **Common mistakes:** Jumping to UI details, mixing in technical implementation, not explaining why this solves the problem.
- **Quality signals:** Clearly states the default behavior change, includes a comparison table, explains the "why" behind the design choice.

### 7. User Experience Principles
- **Purpose:** Provide a decision-making framework for future tradeoffs.
- **Length target:** 3-5 principles, each with a one-sentence explanation.
- **Common mistakes:** Too generic ("be simple"), too many, not actionable.
- **Quality signals:** Each principle could resolve a real debate. They are specific to this feature, not platitudes.

### 8. Experience Flow (High-Level)
- **Purpose:** Walk through the customer journey step by step.
- **Length target:** 6-10 numbered steps per flow. Separate flows for distinct personas if needed.
- **Common mistakes:** Too detailed (pixel-level), too abstract (no concrete steps), missing edge cases for existing customers.
- **Quality signals:** Reads like a story. A designer could start mocking from this. Covers both new and existing customer paths.

### 9. What Changes vs Today
- **Purpose:** A comparison table that makes the impact unmistakable.
- **Length target:** At least 4 rows. More is fine.
- **Common mistakes:** Too few rows, "Today" column is vague, "Proposed" column restates the solution without showing contrast.
- **Quality signals:** Each row highlights a meaningful difference. The table alone tells the story.

### 10. Success Metrics
- **Purpose:** Define how you will know this worked.
- **Length target:** 2-4 primary metrics, 2-4 secondary metrics.
- **Common mistakes:** Only vanity metrics, no distinction between primary and secondary, no directional target.
- **Quality signals:** Primary metrics tie to the core problem (e.g., reducing opt-out rate). Secondary metrics are diagnostic (e.g., profile selection distribution).

### 11. Impact Estimate (Directional)
- **Purpose:** Set expectations without overpromising.
- **Length target:** Table with signal, basis, and expected direction. Optional phasing recommendation.
- **Common mistakes:** Committing to specific numbers, no basis for estimates, missing phasing.
- **Quality signals:** Each estimate references prior data or a benchmark. Phasing is realistic.

---

## Tone & Terminology Rules (from copilot-instructions.md)

Update these to match your team's copilot-instructions.md:

- Write in a concise, executive-friendly tone
- Avoid jargon; explain technical concepts simply
- Use bullet points for key takeaways
- Keep paragraphs short (3-4 sentences max)
- Use "product manager" not "PM"
- Use "customer" not "user" when discussing external stakeholders
- Refer to our team as "<YOUR TEAM NAME>"

---

## Quality Checklist (Phase 8)

Run this checklist before marking the spec as review-ready. Every item should pass.

- [ ] **Overview is self-contained** — A reader who stops after the Overview understands the what, why, and core idea
- [ ] **Overview is under 5 sentences** — No more than one paragraph
- [ ] **Problem Statement includes "why now" signals** — Strategy reviews, leadership direction, competitive pressure, or metrics
- [ ] **Problem Statement includes customer voice** — At least one quote, feedback theme, or data point
- [ ] **Non-Goals list has at least 3 items** — Each specific enough to be debatable
- [ ] **Target Customers section has 2-3 personas** — Each with context, key need, and pain point
- [ ] **Proposed Solution explains "why this solves the problem"** — Not just what, but why
- [ ] **"What Changes vs Today" table has at least 4 rows** — Each row shows a meaningful contrast
- [ ] **Success Metrics distinguish primary from secondary** — Primary metrics tie to the core problem
- [ ] **Impact estimates cite a basis** — Prior experiments, benchmarks, or strategic signals
- [ ] **No jargon throughout** — Technical terms are explained in plain language
- [ ] **Terminology is correct** — Matches the rules in copilot-instructions.md
- [ ] **Paragraphs are 3-4 sentences max** — Concise and scannable
- [ ] **All sources are cited** — Meeting decisions, emails, strategy docs referenced where relevant
