# [Project Name] — Presentation Script

**Total Duration**: [Target: 5 minutes]
**Target Audience**: [Technical/Business/General]
**Context**: [Conference/Team Demo/Portfolio Review]
**Date**: March 2026

---

## Pre-Presentation Checklist

- [ ] Test slides in browser (arrow keys, fullscreen)
- [ ] Open speaker notes (Press `S`)
- [ ] Check projector/screen resolution
- [ ] Have backup plan (PDF, offline version)
- [ ] Water bottle nearby
- [ ] Phone on silent
- [ ] Rehearsed at least once

---

## Opening (Before Slide 1) [15 sec]

**Before showing slides**:
- Greet audience
- Wait for attention
- Brief self-intro if needed

**Example**:
> "Good morning everyone! I'm [Name], and I'm excited to share [Project Name] with you today. This should take about 5 minutes, and I'd love to answer questions at the end."

---

## Slide 1: Title [30 sec]

**On Screen**:
- Project name
- Tagline/subtitle
- Your name + date

**Say**:
> "So, [Project Name]. [One-liner description]. [Brief context about why this exists or why you built it]."

**Example**:
> "So, Super Bowl Predictor. It's a single-page app where friends can predict the final score and compete on a live leaderboard. I built this as a fun coding experiment for Super Bowl Sunday."

**Transition**:
> "Let me start with the problem we were trying to solve..."

---

## Slide 2: The Problem [60 sec]

**On Screen**:
- Problem statement
- 3 pain points (revealed with fragments)

**Say**:
> "The problem was simple: [describe problem]. This matters because [impact/cost/frustration].
>
> Specifically, there were three main pain points:
> - First, [pain point 1 - give example]
> - Second, [pain point 2 - give example]
> - And third, [pain point 3 - give example]"

**Example**:
> "The problem was simple: watching the Super Bowl with friends is fun, but tracking everyone's predictions on paper is messy and there's no easy way to see who's winning in real-time.
>
> Specifically:
> - First, manual score checking meant we kept interrupting the game to update standings
> - Second, paper predictions get lost or disputed later
> - And third, there was no automatic way to rank predictions by accuracy"

**Presenter Notes**:
- Pause between each pain point (let fragments appear)
- Use hand gestures to emphasize
- Make eye contact with audience

**Transition**:
> "So we built something to fix this..."

---

## Slide 3: The Solution [90 sec]

**On Screen**:
- 3-4 key features in grid layout

**Say**:
> "Here's what we built: [Project Name] is [describe in one sentence].
>
> The key features are:
> - [Feature 1]: [Explain benefit in 2 sentences]
> - [Feature 2]: [Explain benefit in 2 sentences]
> - [Feature 3]: [Explain benefit in 2 sentences]"

**Example**:
> "Here's what we built: Super Bowl Predictor is a single-page app with live score integration and automatic ranking.
>
> The key features are:
> - Live ESPN API: Real-time scores update automatically, no manual checking needed
> - Smart Scoring: Predictions are ranked by both score proximity and exact match accuracy
> - Persistent Storage: All predictions save locally, so you can close and reopen without losing data"

**Presenter Notes**:
- Focus on benefits, not just features
- Use simple language (avoid jargon)
- Point to specific feature boxes on screen

**Transition**:
> "Let me show you how this works technically..." (if technical audience)
> OR
> "Let me show you the journey of building this..." (if general audience)

---

## Slide 4: Technical Approach [90 sec] (Optional)

**On Screen**:
- Code snippet with highlighted lines

**Say**:
> "From a technical perspective, the interesting part was [describe challenge].
>
> Here's the core [algorithm/function/approach]: [walk through code briefly].
>
> The key decision was [technical decision] because [reasoning]. We considered [alternative approach] but chose this because [trade-off]."

**Example**:
> "From a technical perspective, the interesting part was calculating prediction accuracy. It's not just 'how close is the score' but also 'did they get the winner right?'
>
> Here's the core algorithm: We calculate the distance between predicted and actual scores, then apply a penalty if they got the winner wrong. Lines 5-7 show that penalty calculation.
>
> The key decision was to use localStorage instead of a backend database because this needed to work offline as a single HTML file. We considered Firebase, but that would require internet and complexity we didn't need."

**Presenter Notes**:
- Don't read the code line-by-line
- Highlight the WHY, not just WHAT
- If audience looks confused, simplify
- Skip this slide for non-technical audiences

**Transition**:
> "Now let me share the journey of building this..."

---

## Slide 5: The Journey [90 sec]

**On Screen**:
- Timeline with 3-4 major phases

**Say**:
> "The development journey was interesting. [Describe overall timeline].
>
> - [Phase 1]: [What happened, how long, key achievement]
> - [Phase 2]: [What happened, how long, key achievement]
> - [Phase 3]: [What happened, how long, key learning]"

**Example**:
> "The development journey was interesting. Total time was about 2 hours, but the distribution was surprising.
>
> - First 10-15 minutes: Got the core app functional - form, scoring logic, API integration, leaderboard. That was fast.
> - Next 30 minutes: Design polish and UI improvements. Made it look good.
> - Final 1-2 hours: The real work - simulating actual gameplay, discovering edge cases, refining game rules. For example, we had to prevent tie predictions because the Super Bowl can't end in a tie. We had to hide rankings when the score was 0-0. Lots of little details."

**Presenter Notes**:
- Share surprises or "aha moments"
- Be honest about challenges
- Make it relatable (everyone has dealt with edge cases)

**Transition**:
> "Let me show you what this looks like in action..."

---

## Slide 6: Demo/Screenshot [90 sec]

**On Screen**:
- Screenshot or live demo

**Say**:
> "Here's what it looks like. [Walk through the screenshot/demo].
>
> [Point out key UI elements]: [Describe what user sees]
> [Show key interaction]: [Describe what happens when user clicks/types]
> [Highlight interesting detail]: [Point out something cool or subtle]"

**Example**:
> "Here's what it looks like. The interface is simple - you see the game info at top, a prediction form in the middle, and the leaderboard below.
>
> When you enter a prediction, it saves immediately to localStorage. When the real game score updates via ESPN API, your accuracy is calculated automatically and you see your rank.
>
> Notice the confetti animation when someone's prediction is perfect - little touches like that make it fun."

**Presenter Notes**:
- Use pointer or cursor to guide eyes
- Slow down - give audience time to look
- If live demo, have backup screenshot ready
- Narrate what you're doing if clicking around

**Transition**:
> "So what did we learn from this?"

---

## Slide 7: Impact & Learnings [90 sec]

**On Screen**:
- Stats (commits, iterations, etc.)
- Key quote or learning

**Say**:
> "The impact of this project: [Describe outcome].
>
> By the numbers: [Walk through stats].
>
> But the key learning was: [Big insight from project]. [Quote from project log or personal reflection]. This taught us that [broader lesson applicable beyond this project]."

**Example**:
> "The impact: We used this for the actual Super Bowl with 8 friends. Everyone loved it, and it kept engagement high during the game.
>
> By the numbers: 50+ git commits, 6 major iterations, 2 hours total dev time.
>
> But the key learning was this: 'Building something functional is fast. The real work is relentless iteration.' We spent 15 minutes on the initial build and 2 hours on refinement. That ratio taught us that craft isn't in the first draft - it's in simulating real usage and fixing every edge case."

**Presenter Notes**:
- Be vulnerable (share what didn't work)
- Make it actionable (what would you do differently?)
- Connect to bigger themes (this applies beyond coding)

**Transition**:
> "If there's one thing to remember from this presentation..."

---

## Slide 8: Key Takeaway [60 sec]

**On Screen**:
- One sentence on colored background

**Say**:
> "If there's one thing to remember: [Read the takeaway sentence].
>
> [Expand on it slightly]: [Why this matters, what it means].
>
> [Optional]: And for us, this means [next steps or future plans]."

**Example**:
> "If there's one thing to remember: Ship fast, iterate relentlessly, capture learnings.
>
> This applies to any project. Don't wait for perfect - get something working, then improve it through real usage. And document what you learn along the way, because those insights are more valuable than the code itself.
>
> For us, this means we're applying this approach to future projects - building a portfolio of small experiments, each teaching us something new."

**Presenter Notes**:
- Pause after the key sentence (let it land)
- Look directly at audience
- Smile - end on positive note

**Transition**:
> "And with that, I'd love to hear your questions."

---

## Slide 9: Q&A [Remaining time]

**On Screen**:
- Large question mark
- Contact info

**Say**:
> "I'd love to answer any questions. Anything about [list 2-3 topics: the project, technical approach, learnings, etc.]?"

**Presenter Notes**:
- Pause and wait (silence is okay)
- Point to someone if they raise hand
- Repeat question for room (if needed)
- Be honest if you don't know ("Great question - I'm not sure, but I'd guess...")
- Keep answers concise (30-60 sec each)

---

## Expected Questions & Answers

### Q: "How long did this take to build?"
**A**: "About 2 hours total. 15 minutes for the core functionality, then 1-2 hours of iteration and refinement. The time breakdown surprised me - I thought it would be the opposite."

### Q: "What technologies did you use?"
**A**: "It's a single HTML file with vanilla JavaScript. No frameworks, no build step. For data, I used the ESPN API for live scores and localStorage for saving predictions. Kept it simple."

### Q: "Would this work for other sports?"
**A**: "Absolutely! The logic is generic - you'd just need to change the API endpoint and maybe tweak the scoring algorithm for sports that can tie. Actually, that could be a fun next project."

### Q: "Can we try it / Where can we see it?"
**A**: "Sure! [Share link or QR code]. It's open source on GitHub if you want to see the code. Just open the HTML file in any browser - no server needed."

### Q: "What was the hardest part?"
**A**: "Honestly, the game rule edge cases. Things like preventing tie predictions, hiding rankings at 0-0, handling unsaved edits. None of that was technically hard, but discovering all those cases through testing took time."

### Q: "Would you do anything differently?"
**A**: "I'd start with the edge case simulation earlier instead of waiting until the end. Maybe write them down as tests first. That would've saved some back-and-forth."

---

## Closing (After Q&A)

**Say**:
> "Thank you all for your time and great questions! If you want to chat more, [mention how to reach you]. Appreciate it!"

**Do**:
- Thank the audience
- Offer to talk individually afterward
- Don't rush off - be available for follow-up chats

---

## Presentation Tips

### Before You Start
- Arrive early to test tech
- Have water nearby
- Take deep breaths
- Smile at a few friendly faces

### During Presentation
- Make eye contact (scan the room)
- Use hand gestures naturally
- Vary your pace (slow down for key points)
- Pause for effect (silence is powerful)
- Show enthusiasm (if you're bored, they're bored)

### If Things Go Wrong
- **Tech failure**: Have backup (PDF, screenshots)
- **Forget what to say**: Check speaker notes (Press S)
- **Question you can't answer**: "Great question - I don't know off the top of my head, but I can follow up"
- **Running out of time**: Skip to key takeaway slide

### Body Language
- Stand up straight (confident posture)
- Move around (don't hide behind podium)
- Use open gestures (avoid crossing arms)
- Face the audience (not the screen)

### Voice
- Speak 20% slower than you think (nerves speed you up)
- Enunciate clearly (especially names/acronyms)
- Vary your tone (monotone = sleep inducer)
- Project from diaphragm (not throat)

---

## Post-Presentation

### Debrief Questions
- What went well?
- What would you change?
- Which slide got best reaction?
- What questions surprised you?
- How was your timing?

### Follow-up Actions
- [ ] Send slides to interested people
- [ ] Share demo link if requested
- [ ] Connect with people who asked questions
- [ ] Update portfolio with presentation
- [ ] Note learnings for next time

---

## Additional Resources

- **Rehearsal**: Practice out loud 2-3 times
- **Timing**: Record yourself to check pace
- **Feedback**: Present to a friend first
- **Backup**: Save offline version (Print to PDF)

**Good luck! You've got this. 🚀**
