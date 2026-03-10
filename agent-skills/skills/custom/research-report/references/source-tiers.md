# Source Evaluation Guide

리서치 시 출처 신뢰도를 평가하고 Tier를 분류하는 가이드입니다.

## Tier Definitions

### 🟢 Tier 1 - Primary Sources (최고 신뢰도)

**정의**: 원본 데이터, 직접 연구, 1차 출처

**포함 대상**:
- **학술 논문**: Peer-reviewed journals (Nature, Science, JAMA 등)
- **정부 데이터**: 통계청, FDA, CDC, NHTSA, OSPI 등 공식 기관
- **연구 기관**: NBER, Pew Research, Brookings Institution
- **기업 공시**: 10-K, 10-Q, 실적 발표 (IR 자료)
- **1차 데이터**: Bloomberg Terminal, Reuters, 공식 통계
- **전문가 인터뷰**: 해당 분야 박사/교수, 현업 전문가 직접 인터뷰

**신뢰도**: 90-100%

**예시**:
- "According to CDC data (2024)..."
- "Published in The Lancet (peer-reviewed)..."
- "Tesla Q4 2024 Earnings Report..."
- "US Bureau of Labor Statistics employment data..."

---

### 🔵 Tier 2 - Secondary Sources (높은 신뢰도)

**정의**: 1차 출처를 분석/종합한 2차 자료

**포함 대상**:
- **분석 리포트**: McKinsey, BCG, Gartner, Forrester
- **전문 언론**: Wall Street Journal, Financial Times, The Economist, Bloomberg News
- **산업 협회**: IEEE, ACM, AMA 보고서
- **기업 백서**: 기술 기업의 공식 기술 문서, 백서
- **전문가 블로그**: 해당 분야 인정받는 전문가의 심층 분석
- **책**: 전문가가 쓴 학술/전문서적

**신뢰도**: 70-90%

**주의사항**:
- 출처가 어떤 1차 자료를 참조했는지 확인
- 저자의 자격/소속 확인
- 이해 충돌 가능성 체크 (스폰서 확인)

**예시**:
- "According to McKinsey's 2024 AI Report..."
- "Analysis by Goldman Sachs Research..."
- "As reported in The Economist (citing World Bank data)..."

---

### ⚫ Tier 3 - Tertiary Sources (보통 신뢰도)

**정의**: 2차 출처를 재가공하거나 의견 중심의 자료

**포함 대상**:
- **일반 뉴스**: CNN, NBC, 일반 신문사 기사
- **기업 블로그**: 마케팅 목적의 회사 블로그
- **Wikipedia**: 잘 관리된 항목 (출처 확인 필수)
- **전문가 의견**: SNS, 인터뷰 단편, 팟캐스트
- **리뷰/사용기**: 제품 리뷰, 사용자 경험담
- **집합 데이터**: Reddit, Quora, 포럼 의견 종합

**신뢰도**: 40-70%

**주의사항**:
- **반드시 교차 검증** (다른 출처로 확인)
- 1차/2차 출처로 뒷받침되는지 확인
- 핵심 결론의 근거로 사용 금지 (보조 자료로만)
- 편향 가능성 높음

**예시**:
- "According to TechCrunch article..."
- "Company blog post suggests..."
- "User reviews on Reddit indicate..."

---

## Confidence Levels

| Confidence | 기준 | 출처 구성 | 사용 |
|-----------|------|----------|------|
| 🟢 **HIGH** | 복수 Tier 1 출처 일치 | Tier 1: 3개+<br>Tier 2: 보조 | 핵심 결론, 권고사항 근거 |
| 🟡 **MEDIUM** | 단일 Tier 1 또는 복수 Tier 2 | Tier 1: 1개<br>Tier 2: 2개+ | 포함하되 "단일 출처" 명시 |
| 🔴 **LOW** | Tier 3만 또는 추론 | Tier 3만<br>또는 논리적 추론 | "미검증" 경고 표시, 결론에 미사용 |

---

## 평가 체크리스트

### ✅ 출처 신뢰도 평가

**1. 저자/기관 확인**
- [ ] 저자가 해당 분야 전문가인가?
- [ ] 기관이 해당 주제에 권위가 있는가?
- [ ] 소속/자격이 명시되어 있는가?

**2. 출판 형태**
- [ ] Peer-reviewed 논문인가?
- [ ] 공식 기관 발표인가?
- [ ] 독립적 편집 과정을 거쳤는가?

**3. 데이터 투명성**
- [ ] 원본 데이터/방법론이 공개되어 있는가?
- [ ] 샘플 크기/기간이 적절한가?
- [ ] 통계적 유의성이 확인되었는가?

**4. 이해 충돌**
- [ ] 스폰서/후원자가 있는가?
- [ ] 저자가 금전적 이해관계가 있는가?
- [ ] 중립성이 의심되는가?

**5. 최신성**
- [ ] 데이터가 최근 것인가? (기술: 1-2년 이내, 기타: 3-5년 이내)
- [ ] 현재 상황에 적용 가능한가?

---

## 교차 검증 방법

### 1. 삼각 검증 (Triangulation)
- **최소 3개 독립 출처**에서 같은 사실 확인
- 출처 간 의존성 체크 (A가 B를 인용했는지)
- 다른 관점/방법론으로 같은 결론 도출되는지

### 2. 상충 정보 처리
```
상충 발견 시:
1. 각 출처의 Tier 확인
2. Tier 1 > Tier 2 > Tier 3 우선순위
3. 같은 Tier면 최신 자료 우선
4. 여전히 불명확하면 "논쟁 중" 명시
```

### 3. 반론 찾기
- **의도적으로** 반대 의견 검색
  - "X criticism"
  - "X limitations"
  - "X debunked"
- 양쪽 입장 모두 Tier 1/2 출처로 확인

---

## 신뢰할 수 있는 출처 예시 (by 분야)

### 의료/건강
- **Tier 1**: CDC, WHO, NIH, FDA, JAMA, The Lancet, New England Journal of Medicine
- **Tier 2**: Mayo Clinic, Cleveland Clinic, WebMD (의사 검증 콘텐츠)
- **피할 것**: 개인 건강 블로그, 광고성 콘텐츠

### 금융/투자
- **Tier 1**: SEC filings (10-K, 10-Q), Fed 데이터, Bloomberg Terminal, 실적 발표
- **Tier 2**: Goldman Sachs Research, Morgan Stanley, Morningstar
- **피할 것**: 투자 권유 블로그, 익명 포럼

### 기술/AI
- **Tier 1**: arXiv (preprint), ACL/NeurIPS 논문, 기업 공식 논문 (Google AI, OpenAI)
- **Tier 2**: Gartner, IEEE Spectrum, A16Z 분석
- **피할 것**: 과장 광고, "AI will..." 예측성 기사

### 교육 (WA State)
- **Tier 1**: OSPI (WA 교육청), Common Core Standards, NGSS
- **Tier 2**: Edmonds School District 공식 자료, 교사 협회
- **피할 것**: 개인 교사 블로그 (검증 안 됨)

### 경제/시장
- **Tier 1**: BLS (노동 통계), World Bank, IMF, FRED (Fed 데이터)
- **Tier 2**: McKinsey, Economist Intelligence Unit, Brookings
- **피할 것**: 단순 뉴스 헤드라인, 예측성 기사

---

## Red Flags (경고 신호)

### ⚠️ 출처 신뢰도 낮음 표시

- **익명 저자** - "전문가에 따르면" (누구?)
- **출처 없는 통계** - "연구에 따르면" (어떤 연구?)
- **과장된 주장** - "혁명적", "완전히 바꿀", "절대적"
- **단일 출처** - 다른 곳에서 확인 안 됨
- **오래된 데이터** - 5년+ 지난 통계 (분야에 따라)
- **광고성** - "최고의", "추천하는" (스폰서 의심)
- **편향된 언어** - 중립적이지 않은 표현

---

## 리서치 보고서 작성 시

### 출처 표기 형식

**Tier 1**:
```
[1] Smith, J. (2024). "Paper Title." Journal Name, 45(3), 123-145.
    DOI: 10.1234/example
    [Tier 1: Peer-reviewed]
```

**Tier 2**:
```
[2] McKinsey & Company (2024). "Industry Report Title."
    https://mckinsey.com/report
    [Tier 2: Industry analysis]
```

**Tier 3**:
```
[3] TechCrunch (2024). "News Article."
    https://techcrunch.com/article
    [Tier 3: News media - requires verification]
```

### 본문 인용

- **HIGH confidence**: "Research conclusively shows [1,2,3]..."
- **MEDIUM confidence**: "Evidence suggests [1]..." (단일 출처 명시)
- **LOW confidence**: "Preliminary data indicates [3]... (unverified)"

---

## 퀵 결정 플로우차트

```
출처 발견
  ↓
Peer-reviewed 논문? → YES → Tier 1
  ↓ NO
정부/공식 기관 데이터? → YES → Tier 1
  ↓ NO
전문 분석 기관? → YES → Tier 2
  ↓ NO
신뢰할 수 있는 언론? → YES → Tier 2
  ↓ NO
일반 뉴스/블로그? → YES → Tier 3
  ↓ NO
익명/출처 불명? → 사용 금지
```

---

## 참고

- 모든 주장에는 출처 필요
- Tier 3만으로 핵심 결론 내리지 말 것
- 반론 없는 리포트는 불완전
- 의심스러우면 → 교차 검증 → 여전히 의심스러우면 → 제외
