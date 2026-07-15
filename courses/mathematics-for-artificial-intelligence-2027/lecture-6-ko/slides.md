---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 6 (KO)
download: true
info: |
  ## 인공지능수학 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-6/
---
<style>
.dark .slidev-page,
.dark .slidev-layout,
.dark .slide-container,
.dark #slide-content,
.dark .slidev-nav-go-container {
  background: #000000 !important;
}
.tikz-fig {
  background: #ffffff;
  border-radius: 8px;
  padding: 0.4rem 0.6rem;
}
</style>

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.png" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">인공지능수학</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">6주차: 통계</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">2027년 봄학기</p>
</div>

---
layout: prism
heading: 과목 커리큘럼
---

<div class="absolute left-10 right-10" style="top: 1rem; bottom: 5rem; display: grid; grid-template-columns: 1fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">과목 개요</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">수와 연산, 체계</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">함수 해석</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">확률 1부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">확률 2부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span class="text-gray-900 dark:text-gray-100">통계</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">선형대수 1부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">선형대수 2부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">행렬 미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">신경망의 데이터 흐름</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: "복습: 5주차"
---

- 확률 분포는 미리 정의되어 있는 확률에 따라 무작위로 값들을 생성하는 함수이다.
  - 각 사건이 이산적인 경우는 이항 분포, 베르누이 분포, 푸아송 분포 등과 같은 이산 확률 분포를 사용한다.
  - 연속 확률 분포는 특정한 형태를 따르되 개별 값들에 대해 확률을 배정하지는 않으며, 정규 분포, 감마 분포, 베타 분포 등이 있다.

- 중심 극한 정리란, 표본 평균들에서 생성한 확률 분포가 표본을 추출한 실제 모집단의 형태와는 무관하게 정규 분포에 접근한다는 것이다.

- 큰 수의 법칙은, 임의의 분포에서 추출한 표본의 개수가 많을수록 표본 평균이 점점 모평균에 가까워진다는 것이다.

- 베이즈 정리는 기계학습과 심층학습 등에서 광범위하게 사용되며, $P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}$ 와 같이 주어진다.

---
layout: prism
heading: 통계
---

- [데이터셋(dataset)]{.hl}이 나쁘면 [모형(model)]{.hl}도 나쁘게 된다.
  - 모형을 구축하기 전에 데이터의 성질을 제대로 파악해야 하며, 그 이해를 바탕으로 유용한 데이터셋을 구축하는 것이 바람직하다.
  - 데이터의 성질을 제대로 파악하기 위해서는 기본적인 통계에 관한 지식이 필요하다.

- [통계량(statistic)]{.hl}은 어떠한 표본에서 계산한, 그리고 그 표본을 어떠한 방식으로 특징짓는 수치이다.
  - 가장 기본적인 통계량 중 하나가 바로 평균이며, 평균은 한 데이터셋을 단 하나의 수치로 요약한 것이다.

- 오늘 수업에서는 다음과 같은 것들을 다룰 것이다:
  - 데이터의 종류를 살펴보고, 데이터셋을 요약 통계량들로 특징짓는 방법
  - 분위수의 정의 및 그래프를 통한 데이터의 내용 파악
  - 이상치와 결측값에 대한 논의
  - 통계적 가설 검정에 대한 소개

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">자료의 종류</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">요약 통계량</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">사분위수와 상자 그림</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">상관관계</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가설 검정</span></p>
  </div>

</div>

---
layout: prism
heading: "자료의 종류: 명목형 데이터"
---

- [명목형 데이터(nominal data)]{.hl}는 [범주형 데이터(categorical data)]{.hl}라고도 하며, 서로 다른 값들 사이에 순서 관계가 없는 데이터이다.
  - 사람들의 눈 색깔을 나타내는 데이터셋의 갈색, 파란색, 녹색 등에는 특별한 순서 관계가 없으며, 명목형 자료로 나타낼 수 있다.

- 이러한 색상 데이터를 심층 신경망에서 활용하려면, 우선 이런 데이터를 신경망이 처리할 수 있는 형태로 변환해야 한다.

- 명목형 데이터는 순서가 없으므로, 예를 들어 빨간색을 $1$, 녹색을 $2$, 파란색을 $3$ 등으로 변환하는 것을 고려할 수 있지만 이는 바람직하지 않다.
  - 신경망이 이들을 그대로 수치로 인식하여, 마치 파란색이 빨간색의 세 배의 관계가 있는 것처럼 오인할 가능성이 있다.

- 보통 심층학습에서는 이러한 문제를 해소하기 위해 [원핫 부호화(one-hot encoding)]{.hl}를 사용하여 각각의 명목 변수를 하나의 벡터로 변환하며, 이 벡터의 성분들은 명목 변수가 가질 수 있는 값들과 일대일 대응이 된다.
  - [DIY]{.hl} 빨간색, 녹색, 파란색을 각각 원핫 부호화하자.

---
layout: prism
heading: "DIY: 원핫 부호화"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np

# One-hot encode nominal categories: each color -> a unit vector.
colors = ["red", "green", "blue"]
onehot = np.eye(len(colors), dtype=int)

for name, vec in zip(colors, onehot):
    print(f"{name:>6} -> {vec}")

# No ordering is implied: every pair is equidistant.
print("distance(red, blue) :", np.linalg.norm(onehot[0] - onehot[2]))
print("distance(red, green):", np.linalg.norm(onehot[0] - onehot[1]))
```

</PyRunner>

---
layout: prism
heading: "자료의 종류: 순서형 데이터"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [순서형 데이터(ordinal data)]{.hl}는 순위 또는 순서는 존재하되, 각 값들의 차이에 어떤 수학적 의미를 가지지는 않는 데이터이다.
  - 설문조사에서 "매우 그렇다"와 "그렇다" 사이에는 분명히 순서의 차이가 있지만, 그들 사이에 어떠한 수리적 관계(예를 들어 "매우 그렇다"가 "그렇다"보다 세 배 강한 동의임)가 존재하지는 않는다.

- 순서형 데이터를 토대로 말할 수 있는 것은, 오직 각 데이터들 사이에 순서가 존재한다는 사실뿐이다.

- 순서형 데이터는 교육 수준 등 [인구통계학적 정보(demographic information)]{.hl}를 나타낼 때에도 주로 쓰인다.
  - 대학교 졸업자는 고등학교 졸업자보다 교육을 _더_ 받았지만, _몇 배_ 더 교육받았는지는 말할 수 없다.

---
layout: prism
heading: "자료의 종류: 구간 데이터"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- [구간 데이터(interval data)]{.hl}는 값들의 차이에 의미가 있는 데이터이다.

- 40°F와 80°F 물이 각각 한 잔씩 있다면, 두 잔의 온도 차가 40°F라고 말할 수 있지만, 두 번째 잔이 첫 번째 잔보다 두 배의 열을 담고 있다고 말할 수는 없다.
  - [화씨(Fahrenheit scale)]{.hl}는 물의 어는점을 32°F, 끓는점을 212°F로 정한 단위계이다.

- 위의 예시를 [섭씨(Celsius scale)]{.hl}로 바꾸면, 첫 잔은 약 4.4°C, 두 번째는 약 26.7°C이다.

- 섭씨나 화씨의 예시와 같이, 구간 자료에서는 차이의 비율이 의미가 없어진다.

---
layout: prism
heading: "자료의 종류: 비율 데이터"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [비율 데이터(ratio data)]{.hl}는 차이가 의미가 있을 뿐만 아니라, 어떠한 [영점(zero point)]{.hl}이 존재하는 데이터이다.
  - 높이는 $0$이라는 영점이 존재하며, 이는 비율 자료로 표현할 수 있다.
  - 나이는 $0$살이라는 영점이 존재하며, 역시 비율 자료로 표현할 수 있다.

- 화씨나 섭씨온도는 구간 데이터이지만, 만약 단위계를 절대온도계로 변환한다면 이는 비율 데이터가 된다.
  - 절대온도계는 0 K라는 영점이 존재하며, 이는 온도가 아예 없음을 의미한다.
  - 이전 예시에서 첫째 잔은 약 277.59 K, 둘째 잔은 약 299.82 K로, 이 경우는 둘째 잔이 첫 번째보다 약 1.08배 뜨겁다고 말할 수 있다.

- 정리하자면, 명목형 데이터는 순서가 없고, 순서형 데이터는 순서는 있되 차이가 의미가 없으며, 구간 데이터는 차이에 의미가 생기지만 엄밀한 영점이 존재하지 않고, 비율 데이터는 진정한 영점이 정의된 구조이다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">자료의 종류</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">요약 통계량</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">평균과 중앙값</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">변동의 측도</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">사분위수와 상자 그림</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">상관관계</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가설 검정</span></p>
  </div>

</div>

---
layout: prism
heading: "평균과 중앙값 - 산술 평균"
---

- 데이터셋을 효과적으로 파악하기 위한 한 방법은 [요약 통계량(summary statistic)]{.hl}을 계산하는 것이다.

- 가장 대표적인 요약 통계량은 [산술 평균(arithmetic mean)]{.hl}으로, 데이터셋이 [스칼라(scalar)]{.hl} 값들의 집합 $\{x_0, x_1, x_2, \ldots, x_{n-1}\}$이라고 할 때, 산술 평균 $\bar{x}$는 원소들을 모두 더한 것을 집합의 크기 $n$으로 나눈 것이다:

$$
\bar{x} = \frac{1}{n} \sum_{i=0}^{n-1} x_i
$$

- 위 식은 [비가중(unweighted)]{.hl} 평균으로, 각 값에 $1/n$의 가중치가 부여된 것이다.

- 데이터셋의 요소들이 고르게 중요한 것이 아니라 더 중요한 것과 덜 중요한 것으로 나뉠 수 있으며, 이 경우 개별적인 가중치를 적용하여 [가중(weighted)]{.hl} 평균을 구할 수 있다:

$$
\bar{x} = \sum_{i=0}^{n-1} w_i x_i, \quad \sum_{i=0}^{n-1} w_i = 1
$$

---
layout: prism
heading: "DIY: 평균과 중앙값 - 산술 평균"
---

<PyRunner>

```python
import numpy as np

x = np.array([81, 80, 85, 87, 83, 90, 79, 88], float)
print("arithmetic mean :", x.mean())

# A weighted mean: weights must sum to 1.
w = np.linspace(1, 2, len(x))
w = w / w.sum()
print("weights sum to  :", round(w.sum(), 6))
print("weighted mean   :", round(float((w * x).sum()), 4))
```

</PyRunner>

---
layout: prism
heading: "평균과 중앙값 - 기하 평균"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 두 양수 $a$와 $b$의 [기하 평균(geometric mean)]{.hl}은 다음과 같이 정의된다:

$$
\bar{x}_g = \sqrt{ab}
$$

- 이를 일반화하여, 양수 $n$개의 기하 평균은 아래와 같이 정의된다:

$$
\bar{x}_g = \sqrt[n]{\prod_{i=0}^{n-1} x_i} = \sqrt[n]{x_0 x_1 x_2 \cdots x_{n-1}}
$$

- 기하 평균은 이미지 처리 분야에서 이미지의 [잡음(noise)]{.hl}을 줄이는 필터로도 사용된다.

---
layout: prism
heading: "평균과 중앙값 - 조화 평균 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- 두 수 $a$와 $b$의 [조화 평균(harmonic mean)]{.hl}은 그 역수들의 산술 평균의 역수이다:

$$
\bar{x}_h = \left( \frac{1}{2} \left( \frac{1}{a} + \frac{1}{b} \right) \right)^{-1}
$$

- 이를 일반화하면 아래와 같다:

$$
\bar{x}_h = \left( \frac{1}{n} \sum_{i=0}^{n-1} \frac{1}{x_i} \right)^{-1}
$$

- 심층학습에서 쓰이는 [F1 점수(F1 score)]{.hl}는 [재현율(recall)]{.hl}과 [정밀도(precision)]{.hl}의 조화 평균이다:

$$
\mathrm{F}1 = \left( \frac{1}{2} \left( \frac{1}{\mathrm{recall}} + \frac{1}{\mathrm{precision}} \right) \right)^{-1}
$$

---
layout: prism
heading: "DIY: 평균과 중앙값 - 조화 평균"
---


<PyRunner>

```python
import numpy as np

x = np.array([1, 3, 9, 27], float)
print("arithmetic mean :", x.mean())
print("geometric mean  :", np.exp(np.log(x).mean()))   # = (prod x)^(1/n)
print("harmonic mean   :", 1.0 / np.mean(1.0 / x))

# F1 = harmonic mean of precision and recall
precision, recall = 0.8, 0.6
print("F1 score        :", 2.0 / (1/precision + 1/recall))
```

</PyRunner>

---
layout: prism
heading: "평균과 중앙값 - 조화 평균 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 재현율과 정밀도의 정의는 다음과 같다:

$$
\begin{aligned}
\mathrm{recall} &= \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}} \\
\mathrm{precision} &= \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FP}}
\end{aligned}
$$

- $\mathrm{TP}$는 [참 양성(true positive)]{.hl}, $\mathrm{FN}$은 [거짓 음성(false negative)]{.hl}, $\mathrm{FP}$는 [거짓 양성(false positive)]{.hl}의 수이다.

- F1 점수는 [참 음성(true negative)]{.hl} 수치를 무시하기 때문에, 모형을 제대로 평가하지 못하여 비교적 더 낙관적인 결과를 낼 때가 많다.

---
layout: prism
heading: "평균과 중앙값 - 중앙값"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 데이터셋의 [중앙값(median)]{.hl}은 전체 데이터들 중 중앙에 있는 값이다.
  - 데이터셋의 값들을 수치 크기 순으로 정렬했을 때, 절반은 중앙값 위에, 나머지 절반은 중앙값 아래에 존재한다.

- 정렬된 데이터셋 $\{37, 44, 55, 63, 65, 69, 71, 73, 74, 87\}$은 원소가 짝수 개이므로 가운데 값이 하나로 정해지지 않는데, 이 경우는 가운데 두 값의 산술 평균을 중앙값으로 사용한다.
  - 즉 중앙값은 $67$이다.

- 중앙값에서는 요소들의 순서가 중요하고, 평균에서는 데이터 값들의 합이 실제로 반영된다.

---
layout: prism
heading: "DIY: 평균과 중앙값 - 중앙값"
---

<PyRunner>

```python
import numpy as np

data = np.array([37, 44, 55, 63, 65, 69, 71, 73, 74, 87], float)
print("median (numpy)  :", np.median(data))

s = np.sort(data)
n = len(s)
if n % 2:
    med = s[n // 2]
else:
    med = (s[n // 2 - 1] + s[n // 2]) / 2   # mean of the two middle values
print("median (manual) :", med, "(mean of 65 and 69)")
```

</PyRunner>

---
layout: prism
heading: "변동의 측도 (1/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 어떤 데이터셋에는 $\{-100, -10, -1, 0, 1, 10, 100\}$, 또 다른 데이터셋에는 $\{0, 0, 0, 0, 0, 0, 0\}$이 들어 있다고 하면, 이 둘의 평균과 중앙값은 모두 $0$으로 같지만 그 값들의 [변동(variation)]{.hl}은 다르다.

- 데이터셋의 변동을 측정하는 한 방법은 [범위(range)]{.hl}, 즉 가장 큰 값과 가장 작은 값의 차이를 구하는 것이다.
  - 그러나 범위는 데이터 전체가 아니라 양극단의 두 값만 반영하므로 대표성을 잘 띠지 못한다.

- 범위보다는 각 값과 평균의 차이에 기반한 [평균 편차(mean deviation)]{.hl} $\mathrm{MD}$가 변동을 좀 더 잘 표현하며, 이를 구하는 공식은 아래와 같다:

$$
\mathrm{MD} = \frac{1}{n} \sum_{i=0}^{n-1} |x_i - \bar{x}|
$$

---
layout: prism
heading: "변동의 측도 (2/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 평균 편차는 [절댓값(absolute value)]{.hl}을 다루기가 까다로우므로, 각 값과 평균의 차이의 제곱들의 평균인 [편향 표본 분산(biased sample variance)]{.hl}이 대신 쓰인다:

$$
s_n^2 = \frac{1}{n} \sum_{i=0}^{n-1} (x_i - \bar{x})^2
$$

- 아래와 같은 살짝 다른 방식을 [비편향 표본 분산(unbiased sample variance)]{.hl}이라고 한다:

$$
s^2 = \frac{1}{n-1} \sum_{i=0}^{n-1} (x_i - \bar{x})^2
$$

  - $n$ 대신 $n-1$을 사용한 것을 [베셀 보정(Bessel's correction)]{.hl}이라고 하며, 표본 분산의 _편향성_ 을 낮추기 위해 고안되었다.

---
layout: prism
heading: "DIY: 변동의 측도"
---

<PyRunner>

```python
import numpy as np

x = np.array([-100, -10, -1, 0, 1, 10, 100], float)
n = len(x)
biased = x.var()            # divides by n
unbiased = x.var(ddof=1)    # Bessel's correction: divides by n-1

print("mean            :", x.mean())
print("biased  s_n^2   :", round(biased, 4))
print("unbiased s^2    :", round(unbiased, 4))
print("std deviation   :", round(np.sqrt(unbiased), 4))
print("standard error  :", round(np.sqrt(unbiased) / np.sqrt(n), 4))
```

</PyRunner>

---
layout: prism
heading: "변동의 측도 (3/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 실제로는 [모집단(population)]{.hl}의 실제 평균 $\mu$와 분산 $\sigma^2$를 알 수 없으므로, 우리는 [표본(sample)]{.hl}의 평균 $m$과 분산 $s_n^2$(또는 $s^2$)을 통해 이를 추정한다.

- $\sigma^2$를 추정하는 데 $s_n^2$보다 $s^2$가 더 적합한 선택이라는 주장이 현재 널리 받아들여지고 있다.
  - 다만, 데이터셋이 충분히 크다면 베셀 보정을 가하든 하지 않든 큰 차이가 없다.
    - 표본 데이터의 크기가 크면 클수록, 모집단을 편향적으로 추정하지 않을 가능성이 크다.
  - 대규모 데이터를 다루는 심층학습 등에서는 분산을 어떤 것으로 사용하든 큰 차이가 없다.

- 분산의 제곱근을 [표준편차(standard deviation)]{.hl}라고 하며, 변동을 표현하기 위해 역시 주로 채택되는 통계치이다.
  - 주로 모집단의 표준편차를 $\sigma$, 표본의 표준편차를 $s$로 표기한다.

---
layout: prism
heading: "변동의 측도 (4/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- 표본 평균들의 집합의 표준편차를 [평균 표준오차(standard error of the mean)]{.hl} 또는 표준오차라고 하며, $\mathrm{SE}$로 표기하고 아래와 같이 정의된다:

$$
\mathrm{SE} = \frac{s}{\sqrt{n}}
$$

- 표준편차는 평균을 중심으로 값들이 얼마나 흩어져 있는지를 파악할 때, 표준오차는 표본 평균이 모집단 평균을 얼마나 잘 추정한 것인지를 파악할 때 유용하다.

- 심층학습에서는 훈련에 사용할 데이터셋의 특징을 파악할 때 표준편차를 활용할 수 있다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">자료의 종류</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">요약 통계량</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">사분위수와 상자 그림</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">상관관계</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가설 검정</span></p>
  </div>

</div>

---
layout: prism
heading: 분위수
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [분위수(quantile)]{.hl}란 데이터 집합을 고정된 크기의 여러 그룹으로 나누는 값을 의미한다.
  - 중앙값은 데이터셋을 같은 크기의 두 그룹으로 나누기 때문에 [이분위수(2-quantile)]{.hl}이다.
    - 중앙값은 [50 백분위수(50th percentile)]{.hl}라고도 부르는데, 데이터 집합의 50%의 값들보다 큰 값임을 의미한다.
    - 95 백분위수는 데이터의 95%보다 큰 값을 의미한다.

- 데이터셋은 [사분위(quartile)]{.hl}로 나누기도 한다.
  - 1사분위(Q1)에는 25%의 값들이, 2사분위(Q2)까지는 50%, 3사분위(Q3)까지는 75%가 속하며, 4사분위(Q4)는 데이터 전체를 포함한다.

- 사분위수를 보이기 위해 잘 사용되는 도구는 [상자 그림(box plot)]{.hl}이다.

---
layout: prism
heading: 상자 그림
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 상자 그림에는 Q1과 Q3가 표기되며, 두 값의 차이를 [사분범위(interquartile range; IQR)]{.hl}라고 부른다.

- 상자 가운데에는 중앙값(Q2)이 표기된다.

- 상자에서 뻗어 나온 선들을 [수염(whisker)]{.hl}이라고 하며, 수염 바깥에 있는 값들을 [잠재적 이상치(possible outlier)]{.hl}라고 한다.

<div class="flex justify-center" style="margin-top: 0.6rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W06_boxplot_diagram.svg" class="tikz-fig" style="width: 78%;" />
</div>

---
layout: prism
heading: "DIY: 사분위수와 IQR"
---

<div style="height: 0.6rem;"></div>

<PyRunner>

```python
import numpy as np

# A sample of exam scores.
data = np.array([81, 80, 85, 87, 83, 87, 87, 90, 79, 83,
                 88, 75, 87, 92, 78, 80, 94, 100, 77, 91], float)

q1, q2, q3 = np.percentile(data, [25, 50, 75])
iqr = q3 - q1
lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr

print(f"Q1 = {q1},  median (Q2) = {q2},  Q3 = {q3}")
print(f"IQR = Q3 - Q1 = {iqr}")
print(f"whisker fences: [{lo}, {hi}]")
print("possible outliers:", data[(data < lo) | (data > hi)])
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">자료의 종류</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">요약 통계량</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">사분위수와 상자 그림</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">상관관계</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">피어슨 상관계수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스피어먼 상관계수</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가설 검정</span></p>
  </div>

</div>

---
layout: prism
heading: 상관관계
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 데이터셋의 특징들 사이에 어떤 관계가 존재할 때가 종종 있다.
  - 한 특징이 증가하면 다른 특징이 (꼭 정비례하지 않더라도) 증가하거나 감소할 수 있으며, 이러한 종류의 연관 관계를 [상관관계(correlation)]{.hl}라 한다.

- 일반적으로 기계학습에서 높은 상관관계는 새로운 정보를 제공하지 않는다는 뜻이므로, 학습 모델에 혼란을 가중시킨다.
  - 기계학습의 [특징 선택(feature selection)]{.hl}은 이런 문제를 해소하기 위해 수행된다.

- 상관관계는 다양한 방식으로 계산될 수 있지만, 어떤 종류든 데이터셋의 두 특징이 얼마나 강하게 연관되는지를 하나의 수치로 표현한다.

---
layout: prism
heading: 피어슨 상관계수
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- [피어슨 상관계수(Pearson correlation coefficient)]{.hl}는 두 특징 사이의 [선형(linear)]{.hl} 상관관계의 강도를 뜻하는 $[-1, 1]$ 구간의 수치로, 흔히 $r$로 표기된다.
  - 선형은 두 특징의 상관관계를 하나의 직선으로 서술할 수 있음을 의미한다.
  - 한 특징이 일정한 양만큼 증가했을 때 다른 특징도 딱 그만큼 증가했다면 피어슨 상관계수는 $+1$, 반대로 감소했다면 $-1$이다.
  - 두 특징 사이의 상관계수가 $0$이라면 두 특징은 잠재적으로 독립이다.

- 데이터셋의 두 특징 벡터 $\mathbf{v}$, $\mathbf{w}$에 대해, 피어슨 상관계수는 아래와 같이 정의된다:

$$
r = \frac{E(\mathbf{v}\mathbf{w}) - E(\mathbf{v})E(\mathbf{w})}{\sqrt{E(\mathbf{v}^2) - E(\mathbf{v})^2}\,\sqrt{E(\mathbf{w}^2) - E(\mathbf{w})^2}}
$$

  - $E(\cdot)$는 [기댓값(expectation value)]{.hl}을 의미한다.

---
layout: prism
heading: "DIY: 피어슨 상관계수"
---

<PyRunner>

```python
import numpy as np

v = np.array([1, 2, 3, 4, 5, 6], float)
w = np.array([2.1, 3.9, 6.2, 7.8, 10.1, 12.2], float)

def pearson(a, b):
    E = np.mean
    num = E(a * b) - E(a) * E(b)
    den = np.sqrt(E(a * a) - E(a) ** 2) * np.sqrt(E(b * b) - E(b) ** 2)
    return num / den

print("Pearson r (formula) :", round(pearson(v, w), 6))
print("check vs corrcoef   :", round(np.corrcoef(v, w)[0, 1], 6))
```

</PyRunner>

---
layout: prism
heading: 스피어먼 상관계수
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- 널리 쓰이는 또 다른 상관계수로 [스피어먼 상관계수(Spearman correlation coefficient)]{.hl}가 있다.
  - 피어슨 상관계수처럼 $[-1, 1]$ 구간의 수치이며, $\rho$로 표기한다.
  - 스피어먼 상관계수는 특징 값 자체가 아닌, 특징 값들의 [순위(rank)]{.hl}에 기초한다.

- 피어슨 상관은 선형 관계를 찾지만, 스피어먼 상관은 입력들 사이의 단조적 연관 관계를 찾는다.
  - 비선형 관계에 대해 피어슨 상관은 그런 관계를 암시할 뿐이지만, 스피어먼 상관은 비선형 관계를 반영한다.

- 각각 $n$개의 값을 가진 두 벡터 $\mathbf{v}$, $\mathbf{w}$에 대해, 스피어먼 상관은 아래와 같이 정의된다:

$$
\rho = 1 - \left( \frac{6}{n(n^2 - 1)} \right) \sum_{i=0}^{n-1} d_i^2, \quad d = \operatorname{rank}(\mathbf{v}) - \operatorname{rank}(\mathbf{w})
$$

---
layout: prism
heading: "DIY: 스피어먼 상관계수"
---

<PyRunner>

```python
import numpy as np

v = np.array([10, 20, 30, 40, 50], float)
w = np.array([1, 4, 9, 16, 25], float)   # monotonic but nonlinear in v

def rankdata(a):                          # 1-based ranks (no ties here)
    return np.argsort(np.argsort(a)).astype(float) + 1

def pearson(a, b):
    a = a - a.mean(); b = b - b.mean()
    return (a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum())

rv, rw = rankdata(v), rankdata(w)
n = len(v)
d = rv - rw
print("Pearson on values  :", round(pearson(v, w), 4))
print("Spearman (rank r)  :", round(pearson(rv, rw), 4))
print("Spearman (formula) :", round(1 - 6 * np.sum(d ** 2) / (n * (n ** 2 - 1)), 4))
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">자료의 종류</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">요약 통계량</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">사분위수와 상자 그림</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">상관관계</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">가설 검정</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">가설</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">t-검정</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">맨-휘트니 U-검정</span></p>
  </div>

</div>

---
layout: prism
heading: "가설 검정 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 인공지능수학 수업을 수강하는 학생 100명을 50명씩 두 그룹으로 묶은 후, 그룹 1에는 강의뿐만 아니라 실습과제를 수행하게 하고, 그룹 2는 강의만 듣게 한 후 같은 시험을 치르게 하여 점수 분포를 확인하였다.

- 두 그룹의 점수에 유의미한 차이가 있는지 파악하기 위해서는 [가설 검정(hypothesis testing)]{.hl}을 수행해야 한다.
  - 가설 검정은 현대 과학의 필수 요소이다.

<table style="margin: 0.8rem auto 0 auto; font-size: 0.8rem; border-collapse: collapse;">
<thead>
<tr>
<th style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; text-align: center;">그룹</th>
<th style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; text-align: left;">시험 점수</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; text-align: center;">그룹 1</td>
<td style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; font-family: monospace;">81 80 85 87 83 87 87 90 79 83 88 75 87 92 78 80 83 91 82 88 89 92 97 82 79 82 82 85 89 91 83 85 77 81 90 87 82 84 86 79 84 85 90 84 90 85 85 78 94 100</td>
</tr>
<tr>
<td style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; text-align: center;">그룹 2</td>
<td style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; font-family: monospace;">92 82 78 74 86 69 83 67 85 82 81 91 79 82 82 88 80 63 85 86 77 94 85 75 77 89 86 71 82 82 80 88 72 91 90 92 95 87 71 83 94 90 78 60 76 88 91 83 85 73</td>
</tr>
</tbody>
</table>

---
layout: prism
heading: "가설 검정 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 가설 검정은 다양한 방식으로 발전했으며, 연구자가 마주칠 수 있는 여러 상황에 따라 다양한 방법이 발전되어 왔다.

- 본 수업에서는 t-검정과 맨-휘트니 U 검정에 대해서만 다룬다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W06_boxplot.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "가설 (1/2)"
---

- 두 데이터셋이 같은 모분포에서 추출된 것인지 알고자 할 때, 기본적으로 확인해볼 수 있는 일은 요약 통계량을 확인하는 것이다.
  - 인공지능수학 시험 점수 분포를 보면, 두 그룹의 중앙값이 다르고 상자가 중앙값을 기준으로 상당히 대칭적이므로, 두 그룹의 평균이 다를 가능성이 크다.
  - 두 그룹의 평균을 중심으로 가설 검정을 적용하자.

- 가설 검정에서는 두 종류의 가설을 사용한다.

<div class="sub-item-enum">

1. [귀무가설(null hypothesis)]{.hl} $H_0$: 영가설이라고도 하며, 우리가 의심하는 바가 틀렸을 것이라고 가정하는 가설이다.
   - 두 그룹이 사실은 같은 모집단에서 나왔을 것, 즉 같은 평균값을 가지고 있을 것이라고 가정한다.
2. [대안가설(alternative hypothesis)]{.hl} $H_a$: 우리가 보이고자 하는 가설이다.
   - 두 그룹이 서로 다른 모집단으로부터 나왔음을 의미한다.
   - 귀무가설이 기각된다면, 암묵적으로 대안가설이 승인됨을 의미한다.

</div>

- 가설 검정은 귀무가설이 참인지 아닌지를 말해주는 것이 아니라, 단순히 귀무가설을 기각할지 승인할지 판단하는 데 사용할 증거를 제시한다.

---
layout: prism
heading: "가설 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- 이 가설 검정으로 판단할 것은 두 그룹이 같은 모집단에서 비롯됐는지 여부이므로, 모든 검정은 [양꼬리(two-tailed)]{.hl}([양면(two-sided)]{.hl}이라고도 함) 검정에 해당한다.
  - 두 집단이 서로 다른지만 알고자 할 때는 양꼬리 검정을, 어떤 집단이 다른 집단보다 큰지/작은지를 알고자 할 때는 [한꼬리(one-tailed)]{.hl}([단면(one-sided)]{.hl}) 검정을 사용한다.

- 가설 검정을 위해 가정들을 정리해보자:

<div class="sub-item-enum">

1. 독립적인 두 그룹을 비교하고자 한다.
2. 두 그룹의 표준편차가 같은지에 대해서는 아무런 가정도 하지 않는다.
3. 귀무가설은 두 그룹의 모집단 평균이 같다는 뜻이다($H_0: \mu_1 = \mu_2$).
   - 모집단 평균을 알지 못하므로, 표본 평균과 표본 표준편차를 이용하여 귀무가설을 승인할지 판정하는 데 필요한 증거를 얻는다.
4. 데이터는 [독립 동일 분포(independent and identically distributed; i.i.d.)]{.hl}라고 가정한다.
   - 상당히 무작위한 과정으로 생성한 표본들은 독립 동일 분포를 가정할 수 있다.

</div>

---
layout: prism
heading: "t-검정 (1/2)"
---

- [$t$-검정($t$-test)]{.hl}은 $t$로 표기하는 검정 통계량에 의존하여, 이 통계량을 미리 만들어진 [$t$-분포($t$-distribution)]{.hl}와 비교해서 $p$값을 구한다.
  - $p$값은 $H_0$에 관한 결론을 내리는 데 사용하는 확률이다.

- $t$-검정은 [모수적(parametric)]{.hl} 검정의 일종으로, 검정할 데이터와 그 분포에 관해 특정한 가정들을 둔다.
  - $t$-검정은 데이터가 독립 동일 분포이며, 그 분포가 정규분포라고 가정한다.
    - 많은 현실의 현상들이 실제로 정규분포를 따르므로, 실제 측정치들로 이루어진 데이터는 정규분포를 따를 가능성이 높다.

- $t$-검정도 여러 종류가 있고, 데이터셋의 크기나 분산에 따라 적합한 것을 선택해야 한다.
  - [웰치 $t$-검정(Welch's $t$-test)]{.hl}는 두 표본의 분산이 같다고 가정하지 않으며, 두 표본이 각각 $n_1$, $n_2$개의 데이터를 가지고 있다고 할 때 아래와 같이 $t$-점수를 계산한다:

$$
t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{(s_1^2 / n_1) + (s_2^2 / n_2)}}
$$

---
layout: prism
heading: "t-검정 (2/2)"
---

- 계산된 $t$-점수를 이용하여 $t$-분포 곡선의 특정 구간에서 곡선 아래의 면적을 계산함으로써 $p$값을 구할 수 있다.
  - 양꼬리 검정에서는 양의 $t$-점수에서 양의 무한대까지의 꼬리와 음의 $t$-점수에서 음의 무한대까지의 꼬리의 총면적이 $p$값이 된다.

- $p$값은 만약 귀무가설이 참이라면 두 평균이 다를 확률을 의미한다.
  - 이 확률값이 우리가 미리 정의한 어떤 특정 수치보다 작으면, 두 그룹의 평균이 다르다는 증거, 즉 두 그룹이 다른 모집단에서 비롯했다는 증거로 간주하여 귀무가설을 기각한다.

- 이처럼 귀무가설을 기각했을 때, 흔히 [통계적으로 유의미한(statistically significant)]{.hl} 차이가 있다는 표현을 사용하며, 주로 사용되는 $p$값 기준은 $0.05$이다.
  - 엄밀한 통계를 요구하는 연구에서는 더 작은 $p$값을 사용하거나, 같은 실험을 여러 번 반복한 결과 $p$값이 일관되게 $0.05$ 미만을 유지한다면 귀무가설의 기각을 고려한다.

---
layout: prism
heading: "신뢰구간 (1/2)"
---

- 통계에서 $p$값과 함께 자주 등장하는 것이 [신뢰구간(confidence interval)]{.hl}이다.

- 신뢰구간은 우리가 비교하는 두 데이터 사이의 반복된 표본들의 평균 차이들이 일정한 비율(신뢰수준)로 속하게 되는 참 모평균 차이들의 구간을 의미한다.
  - 흔히 쓰이는 것은 $95\%$ 신뢰구간이다.
  - 현재 예제에서 가설 검정은 표본 평균들의 차이가 $0$인지 아닌지를 봄으로써 평균들이 같은지를 확인하기 위한 것이므로, 신뢰구간에 $0$이 속한다는 것은 귀무가설을 기각하지 말아야 하는 증거가 된다.

- 웰치 $t$-검정에서 자유도 $df$는 다음과 같이 계산한다:

$$
df = \frac{\left( \dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2} \right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1 - 1} + \dfrac{(s_2^2/n_2)^2}{n_2 - 1}}
$$

---
layout: prism
heading: "신뢰구간 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 주어진 자유도 $df$에 대해, 신뢰구간 $CI_\alpha$는 신뢰수준 $\alpha$와 [임계값(critical value)]{.hl} $t_{1-\alpha/2,\,df}$을 바탕으로 아래와 같이 정의된다:

$$
CI_\alpha = (\bar{x}_1 - \bar{x}_2) \pm t_{1-\alpha/2,\,df} \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
$$

- $95\%$ 신뢰구간의 의미는, 모집단 분포에서 표본들을 추출해서 두 데이터셋을 만들고 각 표본 평균들의 차이를 측정하는 과정을 100번 반복하여 각각 신뢰구간을 계산했을 때, 100개 중 95개의 신뢰구간에 참 모집단 평균 차이가 속함을 의미한다.

- 신뢰구간의 너비는 어떠한 [효과(effect)]{.hl}가 얼마나 큰지를 나타낸다.
  - 신뢰구간이 좁다는 것은 참 효과를 포함하는 범위가 좁다는 뜻이다.

---
layout: prism
heading: 효과 크기
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 통계적으로 유의미한 $p$값을 얻었어도, 그 차이가 현실 세계에서 반드시 의미 있는 것은 아니다.

- 실질적인 의미를 더 잘 표현하는 것은 [효과 크기(effect size)]{.hl}로, 이를 측정하기 위해서는 주로 [코헨-$d$(Cohen's $d$)]{.hl} 값을 사용하며, 웰치 $t$-검정에서는 다음과 같이 구한다:

$$
d = \frac{\bar{x}_2 - \bar{x}_1}{\sqrt{\frac{1}{2}(s_1^2 + s_2^2)}}
$$

- 효과 크기를 어떻게 해석하는지는 상황마다 다를 수 있으며, 일반적으로 해석 결과와 함께 수치를 보고한다.

- [DIY]{.hl} 앞서 제시된 두 그룹의 가설 검정 결과 $p = 0.01825$, $CI = [0.56105, 5.95895]$, $d = 0.48047$를 토대로 해석해보라.

---
layout: prism
heading: "DIY: 두 그룹에 대한 웰치 t-검정"
---

<div style="height: 0.3rem;"></div>

<PyRunner>

```python
import numpy as np
from math import gamma

g1 = np.array([81,80,85,87,83,87,87,90,79,83,88,75,87,92,78,80,83,91,82,88,
               89,92,97,82,79,82,82,85,89,91,83,85,77,81,90,87,82,84,86,79,
               84,85,90,84,90,85,85,78,94,100], float)
g2 = np.array([92,82,78,74,86,69,83,67,85,82,81,91,79,82,82,88,80,63,85,86,
               77,94,85,75,77,89,86,71,82,82,80,88,72,91,90,92,95,87,71,83,
               94,90,78,60,76,88,91,83,85,73], float)
n1, n2 = len(g1), len(g2)
m1, m2 = g1.mean(), g2.mean()
v1, v2 = g1.var(ddof=1), g2.var(ddof=1)          # unbiased variances
t = (m1 - m2) / np.sqrt(v1/n1 + v2/n2)
df = (v1/n1 + v2/n2)**2 / ((v1/n1)**2/(n1-1) + (v2/n2)**2/(n2-1))

def t_pdf(x, dof):                                # Student-t density
    c = gamma((dof+1)/2) / (np.sqrt(dof*np.pi) * gamma(dof/2))
    return c * (1 + x*x/dof)**(-(dof+1)/2)

xs = np.linspace(abs(t), 200, 400000)             # two-tailed p by integration
f = t_pdf(xs, df)
p = 2 * np.sum((f[:-1] + f[1:]) / 2 * np.diff(xs))
d = (m1 - m2) / np.sqrt(0.5*(v1 + v2))            # Cohen's d (magnitude)
print(f"means: {m1:.3f} vs {m2:.3f}   t = {t:.4f}   df = {df:.2f}")
print(f"two-tailed p = {p:.5f}   Cohen's d = {abs(d):.5f}")
```

</PyRunner>

---
layout: prism
heading: "맨-휘트니 U-검정 (1/2)"
---

- $t$-검정은 원본 데이터가 정규분포를 따른다고 가정하는데, 이 가정을 만족하지 않을 때는 [비모수적(nonparametric)]{.hl} 검정을 사용해야 한다.
  - 비모수적 검정은 데이터의 분포에 대해 아무런 가정도 하지 않는다.

- [윌콕슨 순위합 검정(Wilcoxon rank-sum test)]{.hl}이라고도 부르는 [맨-휘트니 $U$-검정(Mann-Whitney $U$-test)]{.hl}은 두 데이터셋이 같은 모분포에서 비롯된 것인지 판정할 때 사용하는 비모수적 검정이다.
  - 맨-휘트니 $U$-검정은 데이터 값들 자체가 아닌 데이터 값들의 순위를 사용한다.
  - 이 검정의 귀무가설은 "그룹 1에서 무작위로 선택한 값이 그룹 2에서 무작위로 선택한 값보다 클 확률은 $0.5$이다"로, 두 그룹이 같은 모분포에서 비롯됐다면 무작위로 추출한 어느 그룹의 값이 다른 그룹의 값보다 더 큰 경향을 보일 이유가 없음을 의미한다.
    - $t$-검정의 귀무가설은 "두 그룹의 평균들의 차이가 $0$이다"로, 맨-휘트니 $U$-검정과 다르다.

- $t$-검정이든 맨-휘트니 $U$-검정이든, 두 데이터셋이 실제로 다른 모분포에서 비롯됐다면 두 귀무가설 모두 거짓이 된다.

---
layout: prism
heading: "맨-휘트니 U-검정 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 맨-휘트니 $U$-검정의 검정 통계량은 $U$로, 데이터셋들의 값을 모두 합친 후 크기순으로 정렬하여 순위를 매겨 계산한다.

- $n_1$개의 샘플이 있는 그룹 1의 순위합 $R_1$과 $n_2$개의 샘플이 있는 그룹 2의 순위합 $R_2$를 구한 후, $U$ 값을 아래와 같이 계산한다:

$$
U = n_1 n_2 + \min\left( \frac{n_1(n_1 - 1)}{2} - R_1,\ \frac{n_2(n_2 - 1)}{2} - R_2 \right)
$$

- 맨-휘트니 $U$-검정에서도 $p$값을 구하는 것이 가능하다.
  - 표본 크기가 커질수록 통계적으로 유의미한 $p$값을 산출할 가능성이 높다.

---
layout: prism
heading: "DIY: 맨-휘트니 U-검정"
---

<PyRunner>

```python
import numpy as np
from math import erf, sqrt

g1 = np.array([81,80,85,87,83,87,87,90,79,83,88,75,87,92,78,80,83,91,82,88,
               89,92,97,82,79,82,82,85,89,91,83,85,77,81,90,87,82,84,86,79,
               84,85,90,84,90,85,85,78,94,100], float)
g2 = np.array([92,82,78,74,86,69,83,67,85,82,81,91,79,82,82,88,80,63,85,86,
               77,94,85,75,77,89,86,71,82,82,80,88,72,91,90,92,95,87,71,83,
               94,90,78,60,76,88,91,83,85,73], float)

def avg_ranks(a):                     # average ranks with ties
    order = np.argsort(a, kind="mergesort"); sa = a[order]; r = np.empty(len(a)); i = 0
    while i < len(a):
        j = i
        while j < len(a) and sa[j] == sa[i]: j += 1
        r[order[i:j]] = (i + j - 1) / 2 + 1; i = j
    return r

n1, n2 = len(g1), len(g2)
ranks = avg_ranks(np.concatenate([g1, g2]))
R1, R2 = ranks[:n1].sum(), ranks[n1:].sum()
U = min(R1 - n1*(n1+1)/2, R2 - n2*(n2+1)/2)      # standard Mann-Whitney U
z = (U - n1*n2/2) / sqrt(n1*n2*(n1+n2+1)/12)     # normal approximation
p = 2 * (1 - 0.5*(1 + erf(abs(z)/sqrt(2))))
print(f"R1 = {R1},  R2 = {R2},  U = {U}")
print(f"z = {z:.4f},  two-tailed p = {p:.5f}")
```

</PyRunner>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
