---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 5 (KO)
download: true
info: |
  ## 인공지능수학 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-5/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">5주차: 확률 2부</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">1주차</span> <span style="color:#9aa0a6;">과목 개요</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">2주차</span> <span style="color:#9aa0a6;">수와 연산, 체계</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">3주차</span> <span style="color:#9aa0a6;">함수 해석</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">4주차</span> <span style="color:#9aa0a6;">확률 1부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">5주차</span> <span class="text-gray-900 dark:text-gray-100">확률 2부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">6주차</span> <span style="color:#9aa0a6;">통계</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">7주차</span> <span style="color:#9aa0a6;">중간 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">8주차</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">9주차</span> <span style="color:#9aa0a6;">선형대수 1부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">10주차</span> <span style="color:#9aa0a6;">선형대수 2부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">11주차</span> <span style="color:#9aa0a6;">미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">12주차</span> <span style="color:#9aa0a6;">행렬 미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">13주차</span> <span style="color:#9aa0a6;">신경망의 데이터 흐름</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">14주차</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">15주차</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 4주차 요약 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 지난 시간에는 확률의 기초를 소개하였다.

- 확률은 어떤 일이 일어날 가능성을 $0$과 $1$을 포함한 그 사이의 수치로 표현한 것이다.

- 표본 공간은 주어진 사건의 모든 가능한 결과를 나타낸 이산 집합 또는 관측 구간이다.

- 확률 변수는 표본 공간에서 하나의 값을 특정한 확률로 취하는 변수를 의미한다.

---
layout: prism
heading: 4주차 요약 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 확률의 합의 법칙은 $P(A\cup B)=P(A)+P(B)-P(A\cap B)$이며, 곱의 법칙은 $P(A\cap B)=P(A,B)=P(B|A)\cdot P(A)$이다.
  - $P(B|A)$는 사건 $A$가 일어날 경우 $B$가 일어날 확률을 표현하는 조건부 확률이다.

- 분할 $B_i$에 대한 $A$의 전체 확률은 $P(A)=\sum_i P(A|B_i)\cdot P(B_i)$이다.

- 결합 확률은 둘 이상의 확률 변수들이 특정한 값들을 가질 확률이며, 주변 확률은 한 확률 변수에 대해 다른 모든 확률 변수가 가질 수 있는 모든 값에 관한 합산으로 구한다.

---
layout: prism
heading: 확률 2부
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 이전 시간에는 확률의 기본 개념들을 다루었다면, 이번에는 확률이 실제로 선형 기계학습 알고리즘 및 심층학습 알고리즘에서 쓰이는 주제들을 살펴볼 것이다.

- 특히, 오늘 다룰 베이즈 정리는 확률에 대한 철학적 패러다임의 전환을 일으켰으며, 확률을 생각하고 적용하는 방법을 바꾸었다.

- 오늘 수업에서는 다음과 같은 것들을 다룰 것이다:
  - 확률 분포와 표본 추출(표집)
  - 베이즈 정리

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">확률 분포</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">히스토그램과 확률</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">이산 확률 분포</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">연속 확률 분포</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">중심 극한 정리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">큰 수의 법칙</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">베이즈 정리</span></p>
  </div>

</div>

---
layout: prism
heading: 히스토그램과 확률
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.5fr 1fr;">
<div>


- [확률 분포(probability distribution)]{.hl}는 미리 정의되어 있는 확률에 따라 무작위로 값들을 생성하는 함수이다.
  - 어떤 값들이 나올지는 미리 알 수 없으나, 각 값이 생성될 가능성은 주어진 확률 분포가 정의하는 특정한 패턴을 따른다.

- 예를 들어, 주사위처럼 각 값이 $1/6$의 _균등한_ 확률로 생성되는 확률 분포를 [균등 분포(uniform distribution)]{.hl}라고 한다.

- 오른쪽의, 주사위 두 개를 굴렸을 때 나오는 눈금 합들의 확률을 나타낸 표를 보자.
  - [DIY]{.hl} 이를 각 눈금 합을 $x$-축으로 하여 막대 그래프로 그려보자.
    - 이런 그래프를 [히스토그램(histogram)]{.hl}이라 한다.

</div>
<div>

<div class="text-center" style="font-size: 0.8rem; margin-top: 0rem;">
  <table style="line-height: 2; border-collapse: collapse; margin: auto;">
    <thead>
      <tr style="padding: 0;">
        <th style="padding: 1px 5px; text-align: center;">합</th>
        <th style="padding: 1px 5px; text-align: center;">확률</th>
      </tr>
    </thead>
    <tbody>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">2</td><td style="padding: 1px 5px; text-align: center;">0.0278</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">3</td><td style="padding: 1px 5px; text-align: center;">0.0556</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">4</td><td style="padding: 1px 5px; text-align: center;">0.0833</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">5</td><td style="padding: 1px 5px; text-align: center;">0.1111</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">6</td><td style="padding: 1px 5px; text-align: center;">0.1389</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">7</td><td style="padding: 1px 5px; text-align: center;">0.1667</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">8</td><td style="padding: 1px 5px; text-align: center;">0.1389</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">9</td><td style="padding: 1px 5px; text-align: center;">0.1111</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">10</td><td style="padding: 1px 5px; text-align: center;">0.0833</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">11</td><td style="padding: 1px 5px; text-align: center;">0.0556</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">12</td><td style="padding: 1px 5px; text-align: center;">0.0278</td></tr>
    </tbody>
  </table>
</div>



</div>
</div>

---
layout: prism
heading: "DIY: 히스토그램과 확률"
---

- 히스토그램 등 임의의 확률 분포로부터 추출된 값들을 토대로, 이러한 표본들이 발생할 확률 또는 가능도를 짐작할 수 있다.
  - 즉, 표본들을 추출한 확률 분포를 [추정(estimate)]{.hl}할 수 있다.

<PyRunner>

```python
import numpy as np
# All outcomes of rolling two fair dice, and the distribution of their sums.
faces = np.arange(1, 7)
sums = np.add.outer(faces, faces).ravel()      # 36 equally likely sums
values, counts = np.unique(sums, return_counts=True)
probs = counts / counts.sum()
for v, p in zip(values, probs):
    print(f"sum {v:>2}: P = {p:.4f}  " + "#" * int(round(p * 100)))
print("total probability:", probs.sum())
```

</PyRunner>

---
layout: prism
heading: 이산 확률 분포 - 이항 분포 (1/2)
---

- 주사위 굴리기처럼 각 사건이 이산적인 경우를 표현하는 확률 분포를 [이산 확률 분포(discrete probability distribution)]{.hl}라고 한다.

- [이항 분포(binomial distribution)]{.hl}는 각 사건에 구체적인 확률이 배정된 상황에서 주어진 횟수만큼 시행을 반복할 때, 각 사건의 기대 빈도를 나타낸다.

- 발생 확률이 $p$인 사건이 $n$번의 시행 중 $k$번 발생할 확률은 다음과 같이 정의된다:

$$
P(X=k)=\binom{n}{k}\cdot p^k\cdot (1-p)^{n-k}
$$

- 동전 하나를 세 번 던졌을 때 앞면이 연달아 세 번 나올 확률은 아래와 같다:

$$
\begin{aligned}
P(HHH) &= \frac{1}{2}\cdot\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{8}\quad\text{(곱의 법칙 이용)}\\
&=\binom{3}{3}\cdot\left(\frac{1}{2}\right)^3\cdot\left(1-\frac{1}{2}\right)^{3-3}=\frac{1}{8}\quad\text{(이항 분포 이용)}
\end{aligned}
$$

---
layout: prism
heading: 이산 확률 분포 - 이항 분포 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 이항 분포 공식은 사건별 확률 $p$가 정의되어 있을 때, 주어진 시행 횟수 $n$에서 정확히 $k$개의 사건이 발생할 확률을 의미한다.

- [DIY]{.hl} $n=3$이고 $p=0.5$일 때, $0\leq k\leq 3$에서 각 $k$의 확률을 이항 분포를 사용하여 계산해보자.
  - 계산된 모든 확률의 합은 반드시 $1.0$이 되어야 한다.

- 이렇게 계산된 확률들은 하나의 [확률 질량 함수(probability mass function)]{.hl}를 규정한다.
  - 확률 질량 함수는 모든 가능한 결과와 연관된 확률을 말해주는 함수이다.

- 이항 분포는 $n$과 $p$를 [초매개변수(hyperparameters)]{.hl}로 사용한다.

---
layout: prism
heading: "DIY: 이산 확률 분포 - 이항 분포"
---

<PyRunner>

```python
from math import comb
n, p = 3, 0.5

def binom_pmf(k, n, p):
    return comb(n, k) * p**k * (1 - p)**(n - k)

probs = [binom_pmf(k, n, p) for k in range(n + 1)]
for k, pr in enumerate(probs):
    print(f"P(X={k}) = {pr:.4f}")
print("sum of PMF:", sum(probs))
```

</PyRunner>

---
layout: prism
heading: 이산 확률 분포 - 베르누이 분포
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [베르누이 분포(Bernoulli distribution)]{.hl}는 이항 분포의 특수한 경우이다.

- 베르누이 분포에서는 $n=1$로 고정되며(즉, 시행은 항상 정확히 한 번이며), 추출되는 값은 $0$ 또는 $1$이다.
  - 동전 한 번 던지기는 $p=0.5$인 베르누이 분포로 표현될 수 있다.

- 확률을 이미 알고 있는 사건들을 시뮬레이션할 때는 이항 분포에서 표본을 추출한다.

- 베르누이 분포는 이분법적인 결과를 내는 사건들에 유용하다.
  - 각 사건의 확률이 반드시 $0.5$일 필요는 없다.

---
layout: prism
heading: "DIY: 이산 확률 분포 - 베르누이 분포"
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(0)
p = 0.5
x = (rng.random(100000) < p).astype(int)   # Bernoulli(p): 1 with prob p, else 0

print("empirical mean :", x.mean(), " (theory p =", p, ")")
print("empirical var  :", x.var(), " (theory p(1-p) =", p * (1 - p), ")")
print("unique values  :", np.unique(x))
```

</PyRunner>

---
layout: prism
heading: 이산 확률 분포 - 푸아송 분포
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 임의의 특정 시행에서 사건이 발생할 구체적인 확률은 알지 못하고, 일정 구간(예: 일정한 시간 동안의 시행 등)에서의 평균적인 발생 횟수만 알고 있는 경우를 가정하자.

- 일정한 구간 내에서 사건이 발생하는 횟수가 평균적으로 $\lambda$라고 할 때, 그 구간에서 사건이 $k$번 발생할 확률은 다음과 같이 정의된다:

$$
P(k)=\frac{\lambda^k\cdot e^{-\lambda}}{k!}
$$

- 이 식을 따르는 확률 분포를 [푸아송 분포(Poisson distribution)]{.hl}라고 한다.

---
layout: prism
heading: "DIY: 이산 확률 분포 - 푸아송 분포"
---

- [DIY]{.hl} 어떤 편의점에 평균적으로 한 시간 동안 손님이 $20$명 온다고 하자. 다음 한 시간 동안 손님이 정확히 $22$명 도착할 확률을 계산해보자.

<PyRunner>

```python
import numpy as np
from math import exp, factorial

lam = 20                      # average customers per hour

def poisson(k, lam):
    return lam**k * exp(-lam) / factorial(k)

print(f"P(exactly 22) = {poisson(22, lam):.4f}")
print(f"P(exactly 20) = {poisson(20, lam):.4f}")
total = sum(poisson(int(k), lam) for k in np.arange(0, 60))
print("sum over k=0..59:", round(total, 6))
```

</PyRunner>

---
layout: prism
heading: 연속 확률 분포
---

- [연속 확률 분포(continuous probability distribution)]{.hl}는 이산 확률 분포처럼 특정한 형태를 따르되, 개별 값들에 확률을 배정하지는 않는다.
  - 연속 확률 분포에서 특정한 하나의 값이 선택될 확률은 $0$이다.
    - 연속 확률 분포에서 선택할 수 있는 값은 무수히 많기 때문이다.

- 예를 들어, 실수 구간 $[0, 1]$에서 특정한 하나의 실수가 선택될 확률은 $0$이지만, 선택된 숫자가 임의의 부분 구간(예: $[0.1, 0.2]$) 안에 들어 있을 확률은 연속 확률 분포를 이용하여 표현할 수 있다.
  - 균등 분포를 가정한다면, 그러한 확률은 $0.1$일 것이다.

- 즉, 연속 확률 분포는 어떤 구간 안에 있는 무수히 작은 요소들을 더하는 [적분(integration)]{.hl}을 이용하여 계산된다.

- 연속 확률 분포에는 [확률 밀도 함수(probability density function)]{.hl}가 연관되며, 이는 해당 분포에서 값들을 추출할 때 적용되는 확률들을 생성하는 _닫힌_ 형식의 함수이다.

---
layout: prism
heading: 연속 확률 분포 - 정규 분포
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>


- [정규 분포(normal distribution)]{.hl}는 흔히 가우스 분포 또는 종 곡선이라고도 불리며, 평균을 중심으로 대칭인 곡선이다.

- 정규 분포($\mathcal{N}(\mu, \sigma)$)는 두 개의 매개변수를 가지며, 곡선의 중심점이 위치하는 평균($\mu$)과 곡선이 얼마나 평평한지를 결정하는 표준편차($\sigma$)를 가진다.

- 정규 분포의 확률 밀도 함수는 아래와 같다:

$$
p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\cdot e^{-(x-\mu)^2/\sigma^2}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W05_normal.svg" class="tikz-fig" style="width: 95%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 연속 확률 분포 - 정규 분포"
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(1)
mu, sigma = 1.0, 0.75
s = rng.normal(mu, sigma, 200000)

print("sample mean/std:", round(s.mean(), 4), round(s.std(), 4))

# Density and its integral (trapezoid rule) over a wide grid
x = np.linspace(mu - 8*sigma, mu + 8*sigma, 4000)
pdf = 1 / np.sqrt(2*np.pi*sigma**2) * np.exp(-(x - mu)**2 / (2*sigma**2))
area = np.sum((pdf[:-1] + pdf[1:]) / 2 * np.diff(x))

print("integral of pdf:", round(area, 6))
```

</PyRunner>

---
layout: prism
heading: 연속 확률 분포 - 감마 분포
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.5fr 1fr;">
<div>

- [감마 분포(gamma distribution)]{.hl}($\Gamma(k, \theta)$)도 두 개의 매개변수를 사용하며, 곡선의 모양을 결정하는 형태($k$)와 축척을 결정하는 규모($\theta$)를 가진다.

- 형태 매개변수가 클수록 감마 곡선의 볼록한 부분이 분포의 중심으로 이동하며, 규모 매개변수는 볼록한 부분의 너비에 영향을 미친다.

- 감마 분포의 확률 밀도 함수는 아래와 같다:

$$
\begin{gathered}
p(x)=x^{k-1}\cdot\frac{e^{-x/\theta}}{\theta^k\cdot\Gamma(k)}\\
\Gamma(k)=\int_{0}^{\infty}t^{k-1}e^{-t}\,\mathrm{d}t
\end{gathered}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W05_gamma.svg" class="tikz-fig" style="width: 100%; margin-top: 4rem" />

</div>
</div>

---
layout: prism
heading: "DIY: 연속 확률 분포 - 감마 분포"
---

<PyRunner>

```python
import numpy as np
from math import gamma

k, theta = 2.0, 2.0

def gamma_pdf(x, k, theta):
    return x**(k - 1) * np.exp(-x / theta) / (theta**k * gamma(k))

x = np.linspace(1e-6, 60, 6000)
pdf = gamma_pdf(x, k, theta)
area = np.sum((pdf[:-1] + pdf[1:]) / 2 * np.diff(x))
mid = (x[:-1] + x[1:]) / 2
mean = np.sum(mid * (pdf[:-1] + pdf[1:]) / 2 * np.diff(x))

print("shape k =", k, " scale theta =", theta)
print("integral of gamma pdf:", round(area, 5))
print("numeric mean:", round(mean, 4), " (theory k*theta =", k * theta, ")")
```

</PyRunner>

---
layout: prism
heading: 연속 확률 분포 - 베타 분포
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

- [베타 분포(beta distribution)]{.hl}도 두 개의 매개변수 $a$와 $b$를 사용하며, $b$에 비해 $a$가 클수록 볼록한 부분이 오른쪽으로 치우친다.
  - 베타 분포는 매우 유연해서 다양한 과정을 시뮬레이션하는 데 유용하다.

- 베타 분포의 확률 밀도 함수는 아래와 같다:

$$
\begin{gathered}
p(x)=\frac{x^{a-1}\cdot(1-x)^{b-1}}{B(a, b)}\\
B(a, b)=\int_{0}^{1}t^{a-1}\cdot(1-t)^{b-1}\,\mathrm{d}t
\end{gathered}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W05_beta.svg" class="tikz-fig" style="width: 95%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 연속 확률 분포 - 베타 분포"
---

<PyRunner>

```python
import numpy as np
from math import gamma

def beta_fn(a, b):
    return gamma(a) * gamma(b) / gamma(a + b)

def beta_pdf(x, a, b):
    return x**(a - 1) * (1 - x)**(b - 1) / beta_fn(a, b)

a, b = 5.0, 2.0
x = np.linspace(1e-6, 1 - 1e-6, 5000)
pdf = beta_pdf(x, a, b)
area = np.sum((pdf[:-1] + pdf[1:]) / 2 * np.diff(x))
print("a =", a, " b =", b)
print("integral of beta pdf:", round(area, 5))
print("mean = a/(a+b) =", round(a / (a + b), 4))
```

</PyRunner>

---
layout: prism
heading: 중심 극한 정리
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 임의의 분포에서 $N$개의 표본을 추출하여 그 평균 $m$을 구하는 과정을 여러 번 반복하는 상황을 가정하자.
  - 즉, 평균값들의 모음 $m_0, m_1, \ldots$을 얻게 된다.
  - 이때 $N$은 매번 달라져도 되지만, 너무 작아서는 안 된다.

- [중심 극한 정리(central limit theorem)]{.hl}란, 이러한 표본 평균들로 형성된 분포가 표본을 추출한 실제 분포의 형태와는 무관하게 점점 정규 분포에 접근한다는 것이다.
  - 예를 들어, 베르누이 분포로부터 얻은 여러 표본들로 평균을 계산하고 그 평균들의 분포를 그리면, 이것이 정규 분포를 따른다.

- [DIY]{.hl} 갈톤 보드(Galton board)는 중심 극한 정리를 관찰할 수 있는 간단한 장난감이다.

---
layout: prism
heading: "DIY: 중심 극한 정리"
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(2)
p, N, trials = 0.3, 50, 20000

# Repeatedly draw N Bernoulli(p) samples and record each batch mean.
means = (rng.random((trials, N)) < p).mean(axis=1)
print("mean of sample means :", round(means.mean(), 4), " (~ p =", p, ")")

theory_std = (p * (1 - p) / N) ** 0.5
print("std of sample means  :", round(means.std(), 4), " (~", round(theory_std, 4), ")")

z = (means - means.mean()) / means.std()
print("fraction |z| < 1     :", round(np.mean(np.abs(z) < 1), 4), " (normal ~0.68)")
```

</PyRunner>

---
layout: prism
heading: 큰 수의 법칙
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [큰 수의 법칙(law of large numbers)]{.hl}이란, 임의의 분포에서 추출한 표본의 크기(즉, 개수)가 클수록 표본 평균이 점점 모평균에 가까워진다는 것이다.
  - 이는 중심 극한 정리와 다르다.

- 큰 수의 법칙은 분포에서 추출한 표본 하나의 평균과 모평균의 관계를 의미하는 반면, 중심 극한 정리는 분포에서 다수의 표본을 추출했을 때 그 표본 평균들의 분포가 어떠한지를 의미한다.

- 예를 들어, 동전 던지기를 할 때 처음 열 번의 시행에서는 앞면이 여덟 번 나올 수도 있지만, 시행이 늘어날수록 앞면과 뒷면의 비율이 대략 5:5에 가까워진다.

---
layout: prism
heading: "DIY: 큰 수의 법칙"
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(3)
flips = (rng.random(100000) < 0.5).astype(int)          # fair coin
running = np.cumsum(flips) / np.arange(1, len(flips) + 1)

for n in [10, 100, 1000, 10000, 100000]:
    print(f"after {n:>6} flips: heads proportion = {running[n-1]:.4f}")

print("target = 0.5")
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률 분포</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">베이즈 정리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">빈도주의적 관점</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">베이지안 관점</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">사전 확률의 갱신</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">기계학습의 베이즈 정리</span></p>
  </div>

</div>

---
layout: prism
heading: 암 진단 예제 - 빈도주의적 관점
---

- 확률과 통계의 유명한 예제로, 유방조영상 진단 결과가 양성인 40대 여성이 실제로 유방암을 가지고 있을 확률을 계산해보자.

- 우리에게 주어진 정보는 다음과 같다:

<div class="sub-item-enum">

1. 무작위로 선택한 40대 여성이 유방암을 보유할 확률은 0.8%이다.
2. 유방암이 있는 여성의 유방조영상 진단이 양성일 확률은 90%이다.
3. 유방암이 없는 여성의 유방조영상 진단이 양성일 확률은 7%이다.

</div>

- 한 40대 여성이 병원에 와서 X선을 찍었을 때 결과가 양성이면, 실제로 유방암을 가지고 있을 확률은 얼마인가?
  - 40대 여성 1,000명 중 평균 8명이 유방암 보유자이며, 그 중 7명($8\times0.9=7.2$)이 양성 유방조영상 진단을 받는다.
  - 유방암이 없는 992명의 여성 중 69명($992\times0.07=69.44$)도 양성 유방조영상 진단을 받는다.
  - 유방조영상 진단이 양성인 여성은 총 76명($7+69=76$)인데, 그 중 7명만 실제 유방암 보유자이므로, 유방조영상 진단이 양성일 때 실제로 유방암이 있을 확률은 약 9%($7/76\approx0.092$)이다.

---
layout: prism
heading: "DIY: 암 진단 예제 - 빈도주의적 관점"
---

<PyRunner>

```python
# Frequentist counting over 1,000 women in their 40s.
n = 1000
have = n * 0.008              # 8 have breast cancer
no = n - have                 # 992 do not
tp = have * 0.90              # true positives  (7.2)
fp = no * 0.07                # false positives (69.44)
posterior = tp / (tp + fp)

print(f"positive & cancer    : {tp:.2f}")
print(f"positive & no cancer : {fp:.2f}")
print(f"P(cancer | positive) : {posterior:.4f}  (~9%)")
```

</PyRunner>

---
layout: prism
heading: 암 진단 예제 - 베이지안 관점 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 확률의 곱의 법칙을 다시 살펴보자:

$$
\begin{gathered}
P(B, A) = P(B|A)\cdot P(A)\\
P(A, B) = P(A|B)\cdot P(B)
\end{gathered}
$$

- 결합 확률에서 어떤 사건을 $A$라 부르고 어떤 사건을 $B$라 부르는지는 상관없으므로 $P(A, B)=P(B, A)$가 성립하며, 따라서 아래 식이 성립한다:

$$
P(B|A)\cdot P(A) = P(A|B)\cdot P(B)
$$

- 위 식의 양변을 $P(A)$로 나눈 것을 [베이즈 정리(Bayes' theorem)]{.hl}라고 한다:

$$
P(B|A)=\frac{P(A|B)\cdot P(B)}{P(A)}
$$

<div class="sub-item">

이는 [사후 확률(posterior probability)]{.hl}($P(B|A)$)이 가능도($P(A|B)$)와 [사전 확률(prior probability)]{.hl}($P(B)$)의 곱을 주변 확률($P(A)$)로 정규화한 결과임을 의미한다.

</div>

---
layout: prism
heading: 암 진단 예제 - 베이지안 관점 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.2em;
}
</style>

- 유방조영상 결과가 양성일 때의 유방암 보유 확률은 베이즈 정리의 사후 확률에 해당한다.
  - 이를 $P(bc+ \,|\, +)$로 표기하자($bc+$는 유방암 진단이 양성임을, $+$는 유방조영상 검사가 양성임을 의미한다).

- 또한, 환자가 유방암을 보유했다고 할 때 유방조영상 검사가 양성일 확률($P(+ \,|\, bc+)$)과 무작위로 선택한 여성의 유방암 보유 확률($P(bc+)$)은 알고 있다.

---
layout: prism
heading: "DIY: 암 진단 예제 - 베이지안 관점"
---

- [DIY]{.hl} 유방암 여부와는 무관하게 유방조영상 검사가 양성일 주변 확률 $P(+)$를 구해보자.
  - $P(+)=P(+|bc+)\cdot P(bc+) + P(+|bc-)\cdot P(bc-)$

- [DIY]{.hl} 베이즈 정리를 이용하여 $P(bc+ \,|\, +)$를 구해보자.

<PyRunner>

```python
# Bayes' theorem with the same numbers.
p_bc = 0.008                 # prior P(bc+)
p_pos_given_bc = 0.90        # likelihood P(+ | bc+)
p_pos_given_no = 0.07        # P(+ | bc-)
p_pos = p_pos_given_bc * p_bc + p_pos_given_no * (1 - p_bc)   # marginal P(+)
posterior = p_pos_given_bc * p_bc / p_pos

print("marginal P(+)        :", round(p_pos, 4))
print("posterior P(bc+ | +) :", round(posterior, 4))
```

</PyRunner>

---
layout: prism
heading: 사전 확률의 갱신
---

- 유방조영상 검사가 양성이라는 소식을 들은 한 40대 여성이 다른 병원에서 다시 한번 유방조영상 검사를 받았는데, 이번에도 양성인 경우를 가정해보자.
  - 이 경우 이 여성의 유방암 보유 확률은 더 이상 9%가 아닌데, 또 다른 증거(1차 검사)가 생긴 상태이므로 유방암이 있다는 [믿음의 정도(degree of belief)]{.hl}가 더 커지기 때문이다.

- 베이즈 정리는 이렇게 계산된 사후 확률을 다시 사전 확률로 갱신하여 믿음의 정도를 다시 계산하는 과정의 수학적 정당성을 제공한다.

- [DIY]{.hl} 이전의 유방조영상 검사 결과에 기초하여 새로운 사후 확률을 계산해보자.
  - 앞서 계산된 $P(bc+ \,|\, +)$가 이번에는 새로운 사전 확률로 사용된다.

<PyRunner>

```python
# A second independent positive test: yesterday's posterior becomes today's prior.
p_pos_given_bc, p_pos_given_no = 0.90, 0.07
prior = 0.008
for test in range(1, 4):
    p_pos = p_pos_given_bc * prior + p_pos_given_no * (1 - prior)
    prior = p_pos_given_bc * prior / p_pos          # update the belief
    print(f"after positive test #{test}: P(cancer) = {prior:.4f}")
```

</PyRunner>

---
layout: prism
heading: "HW03: 베이즈 정리 예시 만들어보기"
---

- 우리가 다루어본 유방암 진단 문제처럼, 실생활에는 베이즈 정리가 적용 가능한 다양한 예제들이 존재한다.

- 이와 비슷한 형태의 예제를 하나 만들어서 베이즈 정리를 이용하여 사후 확률을 계산하고, 추가적으로 그 사후 확률을 다시 사전 확률로 갱신하여 새로운 믿음의 정도를 계산하는 과정을 수행해보자.

- 직접 시나리오를 만들어도 좋고, 인터넷에서 예제를 찾아본 후 자신만의 언어로 바꾸어도 좋다.

- 이러한 과정을 서술(그림을 추가해도 좋다)하여 LMS에 업로드하자.
  - `HW03_20XXXXXX.pdf`로 업로드해 주세요.
  - 직접 손으로 작성해도 좋고(권장합니다), 워드 프로세서를 이용해도 좋다.
  - 표지 등으로 꾸밀 필요는 없고, 맨 위에 성함과 학번만 명확히 적어주세요.
  - 폰트, 글씨 크기 등은 모두 자유이다.

---
layout: prism
heading: 기계학습의 베이즈 정리 (1/2)
---

- 베이즈 정리는 기계학습과 심층학습에서 광범위하게 쓰이며, 대표적인 예시 중 하나가 단순 베이즈 분류기(naive Bayes classifier)이다.
  - 초기 스팸 이메일 필터가 단순 베이즈 분류기를 대단히 효과적으로 이용한 예시 중 하나이다.

- 특징들(예: 눈의 모양, 귀의 모양, 울음소리 등)을 토대로 강아지와 고양이를 분류하는 문제를 생각해보자.
  - 분류명 $y$와 특징 벡터 $\mathbf{x}$가 주어졌다고 할 때, 주어진 특징 벡터에 대해 확률이 가장 큰 분류를 찾는 것이 목적이며, 이를 베이즈 정리로 표현하면 아래와 같다:

$$
P(y|\mathbf{x})=\frac{P(\mathbf{x}|y)\cdot P(y)}{P(\mathbf{x})}
$$

- 문제를 단순화하기 위해 주변 확률 $P(\mathbf{x})$는 무시한다.
  - 우리에게 중요한 것은 사후 확률 $P(y|\mathbf{x})$이며, 분모인 주변 확률은 전체 사후 확률의 총합을 $1.0$으로 맞춰주기 위한(정규화하기 위한) 도구일 뿐이다.
  - 즉, 식은 $P(y|\mathbf{x})\propto P(\mathbf{x}|y)\cdot P(y)$가 된다.

---
layout: prism
heading: 기계학습의 베이즈 정리 (2/2)
---

- 주어진 데이터 집합의 분류명 분포가 실제 모집단을 잘 대표한다는 가정하에, 가지고 있는 데이터를 이용하여 $P(y)$를 구할 수 있다.
  - 데이터에 강아지와 고양이가 1:1 비율로 있다면, $P(\text{고양이})=0.5$로 설정한다.

- $P(\mathbf{x}|y)$는 특징 벡터들이 분류 $y$를 대표한다고 할 때의 특징 벡터들의 확률이며, 우선 $y$가 고양이일 때를 가정하고 특징 벡터들이 전부 고양이 데이터로부터 온 것임을 알고 있으므로 잠시 $y$ 부분은 무시한다.
  - 특징이 $n$개일 때 특징 벡터 $\mathbf{x}=(x_0, x_1, \ldots, x_{n-1})$에 대해 $P(\mathbf{x} \,|\, y=\text{고양이})$는 모든 개별 특징이 동시에 특정한 값을 가질 결합 확률에 해당하며, 단순 베이즈 분류기는 _단순하게_ 이 모든 특징들이 전부 독립적이라고 가정한다.
    - 즉, $P(\mathbf{x})=P(x_0, x_1, \ldots, x_{n-1})=P(x_0)\cdot P(x_1)\cdots P(x_{n-1})$이 된다.

- 이후의 계산은 매우 간단해지는데, 각 분류에서 각 특징이 몇 번이나 관찰되는지 센 다음 베이즈 법칙을 이용하여 최종 분류명을 추론한다.
  - 즉, 고양이 분류의 특징 벡터 중 눈 모양이 날카로운 데이터 수, 귀 모양이 삼각형인 데이터 수, 울음소리가 "야옹"인 데이터 수 등을 이용하여 확률을 추정한다.

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
