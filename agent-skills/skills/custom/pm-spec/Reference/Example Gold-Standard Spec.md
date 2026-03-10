# PM Spec: Notifications Onboarding — Quiet by Default

**Author:** Sourab Nagpal
**Org / Team:** the CXE team
**Status:** Draft
**Last Updated:** February 2026

---

## 1. Overview

Cross-device notifications are one of the most valued capabilities of Phone Link, yet notification noise is consistently the top customer detractor. Today, when a customer enables phone notifications, every app immediately starts delivering feed + banner notifications — and there is no way to set preferences upfront. The customer's only option is to manually disable apps one by one after the fact.

This spec introduces two changes: a **quiet-by-default notification model** where phone notifications arrive as feed only in Action Center (no banner) unless the customer opts in per-app, and a **notifications onboarding flow** during Phone Link setup that lets customers choose between two profiles — Quiet by Default (feed only) or All Notifications (feed + banner). Both profiles give customers per-app control using Phone Link's three options: Feed, Feed + Banner, or Disabled. Together, these changes reduce noise, build trust, and give customers control from the very first moment.

---

## 2. Problem Statement

### What is broken today

- **No notification onboarding exists.** When a customer grants notification permissions (~98% do during LTW onboarding), all phone app notifications begin arriving as feed + banner immediately. There is no step where the customer sets preferences.
- **Defaults are fully noisy.** The current model is opt-out: every app delivers feed + banner by default, and customers must manually go into settings to silence what they don't want. This is the opposite of what Apple and Google offer.
- **Controls are fragmented.** Per-app notification settings exist in both Phone Link and Windows Settings, creating confusion about where to manage them.

### Why this is painful for customers

> "This product has become nagware."
> "Too many notifications that I can't turn off."

Notification noise is the single most cited pain point in customer feedback. Customers who feel overwhelmed are more likely to disable notifications entirely or uninstall Phone Link — both of which directly hurt retention and engagement.

### Why now

- The Jan 15, 2026 Notifications Strategy review confirmed **noise reduction as the top priority**, aligned with K2 themes.
- "Quiet by default" was endorsed as a **strategic experience principle** at both the CXE team level and the Windows Experiences Town Hall (Feb 12, 2026).
- Prior experiments (silencing connectivity notification sounds, Nov 2024) showed **measurable improvements in DAU and a significant drop in negative feedback**, validating this direction.
- Competitive pressure: Apple's iPhone-on-Mac experience uses Focus/DND sync and per-app controls. Google's Phone Hub offers quick silencing. Both are ahead of our current opt-out-everything model.

---

## 3. Goals & Non-Goals

### Goals

- **Reduce notification noise** by changing the default from noisy to quiet.
- **Introduce a notifications onboarding step** that gives customers control from the start.
- **Improve retention and engagement** by reducing the #1 reason customers disable notifications or leave Phone Link.
- **Align with the broader Notifications Strategy** and K2 priorities.
- **Cover all platforms:** Samsung Android, non-OEM Android, and iOS.

### Non-Goals

- **Action Center redesign** — this spec works within current Action Center capabilities. Richer notification UI is a separate, uncommitted workstream.
- **AI-driven summarization or smart bundling** — intelligent noise reduction is a future strategy pillar, not in scope here.
- **Full notification deduplication across devices** — suppressing duplicates when the same app is on both PC and phone is tracked separately.
- **Fixing sync quality issues** — broken sync, disappearing notifications, and clear-all bugs are craft/quality work tracked independently.

---

## 4. Target Customers

### Persona 1: New Phone Link Customer (First-Time Setup)

- **Context:** Just linked their phone to PC for the first time. Excited about cross-device features but unfamiliar with what notifications will look like.
- **Key need:** A smooth setup that doesn't overwhelm them in the first few minutes.
- **Pain point:** Today, the moment setup completes, a flood of notifications arrives with no context or control.

### Persona 2: Existing Customer Who Hasn't Configured Notifications

- **Context:** Has been using Phone Link for weeks or months. May have silenced some apps manually but never went through a structured setup.
- **Key need:** A simple way to reset or configure notification preferences without digging through settings.
- **Pain point:** Notifications feel noisy but the path to fix it is unclear and fragmented.

### Persona 3: Power Customer

- **Context:** Wants granular control. Knows exactly which apps should show banners, which should be feed only, and which should be disabled.
- **Key need:** Quick access to per-app controls after choosing a starting profile.
- **Pain point:** Today, per-app controls exist but are split across Phone Link and Windows Settings.

### Platform Coverage

| Platform | Notification type | Click behavior |
|---|---|---|
| Samsung Android (preinstalled LTW) | Clickable + inline actions | Opens app via mirroring/deep link |
| Non-OEM Android (Pixel, Motorola, etc.) | Info-only | Opens Bing search (poor UX) |
| iOS (via Bluetooth) | Info-only | No click action |

The onboarding flow and quiet defaults apply **across all platforms**. Per-app inline actions and click behavior remain platform-dependent.

---

## 5. Current Experience (Baseline)

### Customer Flow Today

1. Customer sets up Phone Link and grants notification permission on their phone.
2. All phone app notifications immediately start arriving on PC as feed + banner for every app.
3. Notifications appear in Action Center, as banners, in Phone Link, and as missed activities in Start Menu.
4. To reduce noise, customer must: open Settings or Phone Link > find per-app toggles > disable one by one.
5. Many customers never do this and either tolerate the noise, disable all notifications, or stop using Phone Link.

### Key Friction Points

- **No preference step during onboarding.** The jump from "permission granted" to "everything is on" is jarring.
- **Default is maximum noise.** Every app delivers feed + banner from moment one.
- **Controls are fragmented.** Per-app settings live in both Phone Link and Windows Settings > Notifications. Customers don't know which surface to use.
- **Phone notifications are not clearly distinguished.** In Action Center, notifications show the Phone Link icon rather than the phone app icon, making it hard to identify the source at a glance.

---

## 6. Proposed Solution

### Default Behavior Change

Change the default notification behavior for all phone notifications:

- **Today:** All phone app notifications arrive as feed + banner (opt-out model). Every app that has notifications enabled on the phone immediately sends banners on PC.
- **Proposed:** All phone app notifications default to **feed only** — they appear in Action Center but do not produce a banner. Customers choose which apps deserve a banner.

### Notifications Onboarding Flow

Introduce a new step during (or immediately after) Phone Link setup where customers choose one of two starting profiles. Both profiles apply to all apps that have notifications turned ON on the phone.

| Profile | Default behavior | Per-app control | Recommended for |
|---|---|---|---|
| **Quiet by Default** (recommended) | **Feed only** for all apps. Notifications appear silently in Action Center — no banner. | Customer can enable apps one by one and choose from three options: **Feed**, **Feed + Banner**, or **Disabled**. | Most customers — reduces noise, builds trust, gives control |
| **All Notifications** | **Feed + Banner** for all apps. Notifications appear in Action Center and produce a banner on screen. | Customer can change any app to **Feed**, **Feed + Banner**, or **Disabled**. | Customers who want full visibility of all phone activity on PC |

#### How the per-app controls work (both profiles)

For each phone app, the customer can set one of three states:

| Setting | Behavior |
|---|---|
| **Feed** | Notification appears in Action Center only. No banner, no sound. |
| **Feed + Banner** | Notification appears in Action Center and produces a visible banner on screen. |
| **Disabled** | Notification is not forwarded to PC at all. |

- The onboarding screen shows the profile choice first. After selecting a profile, the customer can optionally review and adjust individual apps immediately, or skip and adjust later in Settings.
- The "Quiet by Default" profile is pre-selected as the recommended option.

### For Existing Customers

- Surface a **"Set up your notifications"** prompt (in Phone Link or as a toast) for existing customers who have not gone through this flow.
- The prompt links to the same profile selection experience.
- This is a one-time prompt, dismissible, and does not change any current settings without explicit customer action.

---

## 7. User Experience Principles

1. **Quiet by default** — Earn trust by being respectful of attention. Noise is opt-in, not opt-out.
2. **Explicit customer choice** — Never change behavior without asking. The onboarding flow gives customers agency from the start.
3. **Progressive disclosure** — Start with a simple profile choice. Offer per-app granularity for those who want it, but don't require it.
4. **Respect customer context** — Phone notifications on PC should complement the workflow, not interrupt it.
5. **One home, one control** — Action Center is the canonical place for notifications. Windows Settings is the canonical place for controls. Avoid fragmenting further.

---

## 8. Experience Flow (High-Level)

### Flow A: New Customer (First-Time Setup)

1. Customer completes Phone Link pairing and grants notification permission on their phone.
2. **New step:** A "Set up your notifications" screen appears, explaining that phone notifications are now connected.
3. Customer sees two profile options: **Quiet by Default** (recommended, pre-selected) and **All Notifications**.
4. Customer selects a profile.
5. Optionally, customer reviews the list of phone apps and adjusts individual apps (Feed / Feed + Banner / Disabled). This step can be skipped.
6. System applies the selected defaults immediately.
7. Customer sees a confirmation: "You can change this anytime in Settings > Notifications."
8. Notifications begin arriving according to the selected profile and any per-app overrides.

### Flow B: Existing Customer (Finish Setup Prompt)

1. Customer opens Phone Link (or receives a one-time toast prompt).
2. Prompt: "You're getting phone notifications — want to set your preferences?"
3. Customer taps the prompt > same profile selection screen as Flow A.
4. System applies the selected defaults. **Existing per-app overrides the customer already set are preserved** — the profile only sets defaults for apps the customer hasn't manually configured.
5. Confirmation with link to Settings.

### Post-Profile Behavior

- **Quiet by Default:** All phone app notifications appear in Action Center only (feed). No banners. Customer enables banners per-app by switching individual apps to Feed + Banner.
- **All Notifications:** All phone app notifications appear in Action Center and produce a banner (feed + banner). Customer can quiet individual apps by switching them to Feed, or turn them off with Disabled.

---

## 9. What Changes vs Today

| Area | Today | Proposed |
|---|---|---|
| **Defaults** | All apps: feed + banner (opt-out) | Quiet by Default profile: feed only (opt-in for banners per-app) |
| **Per-app control** | Toggle on/off only, fragmented across surfaces | Three clear options per app: Feed, Feed + Banner, Disabled |
| **Customer effort to reduce noise** | High — must find and disable apps one by one | Low — choose a profile during setup; fine-tune per-app later if desired |
| **Onboarding** | No notification preference step | Two-profile selection during Phone Link setup |
| **Control surface** | Fragmented: Phone Link + Windows Settings | Primary: Windows Settings > Notifications (deep link from Phone Link) |
| **Existing customer path** | No prompt to configure | One-time "Set up your notifications" prompt |
| **Perceived value** | "Noisy and annoying" | "Respectful and useful" |

### Platform-Specific Differences

| Behavior | Samsung Android | Non-OEM Android | iOS |
|---|---|---|---|
| Profile selection available | Yes | Yes | Yes |
| Inline actions (reply, dismiss) | Yes | No | No |
| Click-to-open app | Yes (mirroring/deep link) | No (Bing search fallback) | No |
| Silent-at-creation-time approach | Yes | Yes | N/A (BT notifications) |

The quiet-by-default model and onboarding flow are **consistent across all platforms**. The differences in inline actions and click behavior are pre-existing and not changed by this spec.

---

## 10. Success Metrics

### Primary Metrics

- **Notification opt-out rate (reduce):** Fewer customers turning off all phone notifications after setup. Target: measurable reduction in full opt-out within 7 days of setup.
- **DAU retention:** Increase in 7-day and 28-day retention for customers who go through the onboarding flow vs. control.
- **Negative feedback reduction:** Decrease in feedback volume related to notification noise, spam, and "nagware."

### Secondary Metrics

- **Onboarding completion rate:** Percentage of customers who see the profile selection and make a choice (vs. skip/dismiss).
- **Profile selection distribution:** Which profiles customers choose (validates whether "Quiet" is the right default recommendation).
- **Post-onboarding settings change rate:** How often customers adjust per-app settings after choosing a profile (indicates whether profiles are well-calibrated).
- **Customer sentiment:** Improvement in notification-related NPS or satisfaction scores.

---

## 11. Impact Estimate (Directional)

These are directional estimates, not commitments, based on prior experiment results and competitive benchmarks.

| Signal | Basis | Expected direction |
|---|---|---|
| **DAU engagement** | Silencing connectivity notification sounds (Nov 2024 experiment) increased DAU days and reduced negative feedback | Expect similar or stronger lift from quieting all notifications by default |
| **Notification opt-out rate** | Today, a meaningful share of customers disable notifications within the first week due to noise | Expect significant reduction with quiet defaults + onboarding |
| **Retention** | Noise is cited as a top churn driver in feedback | Expect measurable improvement in 28-day retention for onboarded customers |
| **Customer satisfaction** | Apple and Google both default to quieter, more controlled experiences and score higher in cross-device notification satisfaction | Expect improvement in sentiment once parity is achieved |

### Phasing Recommendation

| Phase | Scope | Timing |
|---|---|---|
| **Phase 1** | Quiet by default for new customers + onboarding flow (profile selection) | Target: next available cycle |
| **Phase 2** | "Finish setup" prompt for existing customers | Follow-on, after Phase 1 learnings |
| **Phase 3** | Smart defaults refinement (auto-suggest Feed + Banner for high-value apps like messaging and calls based on usage data) | Informed by Phase 1 per-app configuration data |
