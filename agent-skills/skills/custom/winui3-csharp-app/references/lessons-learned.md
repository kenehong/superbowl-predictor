# Lessons Learned

Things learned from mistakes. Read before starting complex tasks.

---

## 2025-02-25 — Prioritized reference rules over Figma spec

**What went wrong:** `references/ui-ux.md` said "use NavigationView", so I followed it — but the Figma design used a custom 48px rail. I also added search to the title bar per reference patterns, but Figma had none.

**Why:** References = general best practices, Figma = the project's concrete spec. When they conflict, Figma should win — but I blindly followed the references.

**Lesson:** When a Figma design exists, Figma spec > Reference rules. References apply only to areas not specified in Figma (accessibility, performance, etc.).

**What went wrong:** The Figma API response had exact padding, gap, and dimension values, but I didn't read them and guessed spacing/sizes from experience. I assumed NavigationView was correct, but Figma had a custom rail.

**Why:** First fetch used shallow depth; I skimmed the long response by component names only. Satisfied with "build success" and skipped design-match verification.

**Lesson:**
- Start Figma fetch at `depth=6+`. Extract layout properties (padding, gap, sizing) before coding.
- Decide Figma component → WinUI control mapping first. Similar names can be different controls.
- Build success ≠ design match. Always compare against Figma values after building.
- See `references/figma-to-code.md` for the full workflow.

## 2026-02-26 — Missing DPI awareness check before running WinUI 3 app

**What went wrong:** Built and ran the ChatPrototype app, but UI rendered blurry. The `app.manifest` was missing the `PerMonitorV2` DPI awareness declaration.

**Why:** Focused only on build success without checking manifest settings (DPI, permissions, etc.) before launch.

**Lesson:** Before running/building a WinUI 3 app, always verify `app.manifest` contains:
```xml
<dpiAware>true/pm</dpiAware>
<dpiAwareness>PerMonitorV2</dpiAwareness>
```
Without this, UI renders blurry on high-DPI monitors. Build success ≠ correct runtime config.

## 2026-02-26 — Figma MCP only provides JSON, not visuals

**What went wrong:** Implemented a design using only the JSON tree from Figma MCP `get_figma_data` — ended up adding elements that shouldn't exist (sidebar, avatar), couldn't read icon glyphs, and couldn't judge overall feel.

**Why:** The agent can see images, but Figma MCP does not provide rendered images. It only returns JSON (layout/properties), so the design was implemented without ever "seeing" it.

**Lesson:** Provide **screenshots (PNG) alongside the Figma link** so the agent can reference both visuals and JSON — this is the most accurate approach. Screenshots are essential for detecting elements that should NOT exist, identifying icon shapes, and judging overall layout feel. Reflected in `references/figma-to-code.md`.

## 2026-02-27 — Forgot to auto-update system-map after adding components

**What went wrong:** Added 7 new skills to `agent-skills/` but didn't update `system-map.html` until Kenny reminded me.

**Why:** Treated the copy task as "done" after file operations, forgot the global rule about system map maintenance.

**Lesson:** Whenever creating/moving/deleting tools, agents, skills, or reference files → update `system-map.html` in the same step. Don't wait to be asked.

## 2026-02-27 — Forgot system-map update AGAIN after modifying RIPER

**What went wrong:** Changed RIPER to conditional in `copilot-instructions.md` but didn't update the RIPER card in `system-map.html`. Kenny had to remind me a second time in the same session.

**Why:** Treated the instruction file edit as the only step. System map update still not automatic in my workflow.

**Lesson:** After ANY change to global rules, project instructions, skills, or agent config → system-map.html update is MANDATORY in the same response. No exceptions. Two strikes already.

## 2026-02-28 — WinUI 3 TextBox 세로 가운데 정렬이 속성만으로 안 됨

**뭐가 잘못됐나:** 커스텀 컨테이너 안에 borderless TextBox 텍스트를 세로 가운데 정렬하려고 4번 시도. `VerticalContentAlignment="Center"`, `VerticalAlignment="Center"/"Stretch"`, `TextControlThemePadding`, `TextControlThemeMinHeight` 리소스 오버라이드 — 전부 안 먹힘.

**왜:** WinUI 3 TextBox 내부 ControlTemplate에 Header/Content/Description 용 Row가 있는 Grid 구조. 내부 `ScrollViewer`("ContentElement")와 `PlaceholderTextContentPresenter`가 템플릿에서 `VerticalAlignment="Top"`으로 하드코딩되어 있음. 외부 속성/리소스 오버라이드가 이 내부 요소에 전달 안 됨.

**해결:** `Loaded` 이벤트에서 visual tree를 순회하며 내부 ScrollViewer, TextBlock, ContentPresenter 전부 `VerticalAlignment.Center`로 강제 설정:
```csharp
private void TextBox_Loaded(object sender, RoutedEventArgs e)
{
    CenterAllChildren(sender as DependencyObject);
}
```

**교훈:** WinUI 3 TextBox 레이아웃을 속성으로 안 되면 바로 visual tree 조작(`Loaded`)으로 가라. 속성/리소스 오버라이드에 시간 낭비하지 말 것 — 내부 템플릿이 세로 정렬 관련은 대부분 무시함.

## 2026-02-28 — WinUI 3 Canvas 클리핑 & Lottie unpackaged 호환 삽질

**뭐가 잘못됐나:** Confetti overlay를 Canvas로 구현 → 파티클이 프로필 사이즈만큼만 보임. Lottie 시도 → `ms-appx:///` URI 안 됨 → 결국 Composition API로 회귀. 6번의 빌드-실행-디버그 루프.

**왜:**
1. **Canvas는 자식 크기에 맞춰 0x0** — Grid처럼 부모에 Stretch 안 됨. Canvas.SetLeft/SetTop으로 위치 잡으면 Canvas 자체 크기 밖 파티클은 클리핑됨.
2. **Lottie + unpackaged app**: `ms-appx:///` URI가 `WindowsPackageType=None` 앱에서 LottieVisualSource에서 작동 안 함. `StorageFile.GetFileFromPathAsync`로만 로드 가능.
3. **CommunityToolkit.WinUI.Lottie 8.2**는 `WinRT.Runtime 2.2` 필요 → SDK 1.6과 호환 안 됨, CsWinRT 패키지 직접 추가 필요.

**해결:** Canvas 완전 제거. Grid에 파티클 추가 + Composition `Offset` 절대 좌표로 위치 제어. 클리핑 문제 없음.

**교훈:**
- WinUI 3에서 절대 위치 파티클 → Canvas 쓰지 말고 Grid + Composition Offset 사용
- Unpackaged 앱에서 Lottie → `ms-appx` 대신 `StorageFile.SetSourceAsync` 필수
- Lottie NuGet 추가 시 WinRT.Runtime 버전 호환 먼저 체크
- 빌드 전 `ChatPrototype` 프로세스 실행 중인지 먼저 확인 → 파일 락 방지

## 2026-03-03 — 또 같은 실수: Figma 레퍼런스 안 읽고 구현

**뭐가 잘못됐나:** NotificationsSetup 앱 Figma→WinUI 변환에서 (1) lessons-learned.md 안 읽음, (2) figma-to-code.md 안 읽음, (3) depth 파라미터 없이 기본값으로 fetch → 데이터 수천 줄 대충 훑음, (4) NavigationView 기본 패턴 사용 → Figma는 상단 탭 + 좁은 사이드바, (5) 스크린샷 스킬 존재도 몰랐음.

**왜:** 레퍼런스 파일을 "이전 세션에서 읽었으니 됐겠지" 하고 스킵. 매 세션 시작 시 다시 안 읽음.

**교훈:**
- WinUI 3 + Figma 작업 시작 전 **반드시** `lessons-learned.md` → `figma-to-code.md` 순서로 읽기
- Figma fetch는 항상 `depth=2`로 구조 파악 → 필요 노드만 `depth=6+`로 재fetch
- 스크린샷 스킬로 빌드 후 반드시 시각 검증
- "이전에 읽었다"는 핑계 금지 — 매번 읽어라

## 2026-02-28 — Confetti 이펙트 제품 적용 리서치 메모

**현재 상태:** ChatPrototype에서 송신 메시지에 "축하/congrat/🎉/🥳/🎊" 포함 시 confetti 발사. Composition API + Grid + Offset 방식.

**수신 메시지에도 적용 가능:** 텍스트 감지 로직(`ShouldFireConfetti`)을 수신 메시지 추가 시점에도 호출하면 됨. 코드 한 줄 수준.

**실제 제품 (Shell.MMX) 적용 시 고려사항:**
- **접근법 A (클라이언트 텍스트 감지):** 서버 변경 없이 바로 가능. 다만 언어별 키워드 관리, 오탐("축하 안 합니다") 주의.
- **접근법 B (iMessage 방식 메타데이터):** 메시지에 effect 태그 포함. 오탐 없지만 프로토콜/서버 지원 필요.
- **접근법 C (AI/NLP):** 감성 분석. 무겁고 프라이버시 이슈.

**디자인 결정 필요 사항:** 트리거 주체(송신/수신/양쪽), 발사 타이밍(즉시/스크롤 시), 반복 여부(최초 1회?), 옵트아웃 설정, 접근성(prefers-reduced-motion).

## 2026-03-03 — Empty API response cached as valid data

**What went wrong:** WorkIQ Tamagotchi app couldn't show today's meetings. First fetch returned empty `events: []` (likely slow MCP startup), but `saveMeetings()` cached it with today's timestamp. All subsequent requests saw `isStale() = false` and returned the empty cache.

**Why:** No guard against caching empty results. The code treated "0 meetings" as a valid fetch — same as a day with genuinely no meetings.

**Fix:** Added check in `getMeetings` IPC handler — if `events.length === 0`, don't save to cache, so next request retries the fetch.

**Lesson:** Never cache empty/error API responses as valid data. Always validate response content before writing to cache. This applies to any fetch-then-cache pattern (meetings, briefings, Teams data).
