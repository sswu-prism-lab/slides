---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 4 (KO)
download: true
info: |
  ## 인공지능수학 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-4/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">4주차: 확률 1부</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span class="text-gray-900 dark:text-gray-100">확률 1부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">확률 2부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">통계</span></p>
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
heading: 확률 1부
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 확률은 실생활의 다양한 부분에 많은 영향을 끼치고 있다.

- 확률론의 개념들은 인공지능의 다양한 분야에서 중요하게 적용된다.
  - 인공지능 알고리즘의 출력, 현실 세계 데이터의 빈도, 신경망의 초기화 등.

- 오늘 수업에서는 다음과 같은 것들을 다룰 것이다:
  - 확률의 기본 개념들, 특히 확률 변수의 정의
  - 기본적인 확률 법칙들 및 결합 확률과 주변 확률
  - 확률과 관련한 2가지 연쇄 법칙 중 하나

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">기본 개념들</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">표본 공간과 사건</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">확률 변수</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률 법칙들</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">결합 확률과 주변 확률</span></p>
  </div>

</div>

---
layout: prism
heading: 표본 공간과 사건 (1/2)
---

- [확률(probability)]{.hl} $P$는 어떤 일이 일어날 가능성을 $0$과 $1$을 포함하여 그 사이의 수치로 표현한 것($P \in [0, 1]$)이다.
  - $[a, b]$는 $a$와 $b$를 포함하는 구간을 의미한다.
  - $(a, b)$는 $a$와 $b$를 포함하지 않는 구간을 의미한다.
  - 어떤 일이 일어날 가능성이 전혀 없다면 그 확률은 $0$, 반드시 일어날 것이 확실하다면 $1$이다.
  - $0$과 $100$ 사이의 실수와 함께 % 단위를 사용하기도 한다.
    - 내일 비가 올 확률은 $25\%$이다.

- [표본 공간(sample space)]{.hl} $\Omega$는 주어진 한 [사건(event)]{.hl}의 모든 가능한 결과를 나타내는 이산 집합 또는 연속 구간이다.
  - 사건은 어떤 관측이 일어났음을 의미하며, 동전 던지기, 주사위 굴리기 같은 과정의 결과이다.
  - 확률을 다룰 때는 주어진 사건의 모든 가능한 결과를 하나의 표본 공간으로 묶어서 취급한다.
  - 표본 공간은 모든 가능한 결과를 대표하며, 개별 사건은 표본 공간의 한 부분집합, 즉 하나의 표본에 해당한다.
    - [DIY]{.hl} 동전 던지기, 주사위 굴리기의 표본 공간과 표본을 정의해보자.

---
layout: prism
heading: 표본 공간과 사건 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 동전 던지기나 주사위 굴리기처럼 이산적인 방식으로 표본 공간을 정의할 수도 있지만, 필요하다면 연속적인 구간에서도 정의될 수 있다.

- 어떤 사건이 일어날 가능성이 어느 정도인지를 나타내는 값을 [가능도(likelihood)]{.hl}라고 한다.

- 동전 하나를 던졌을 때 앞면이 위로 나올 가능도는 $0.5$이며, 뒷면이 위로 나올 가능도는 $0.5$이다.
  - 주사위 굴리기도 비슷한 방식으로 가능도를 계산할 수 있다.

- 표본 공간에서 모든 가능도를 더하면 반드시 $1$이 된다.

- [Q]{.hl} 확률과 가능도는 어떠한 점에서 다른가?

---
layout: prism
heading: "DIY: 표본 공간과 가능도"
---

<div style="height: 0.6rem;"></div>

<PyRunner>

```python
# Sample space of a coin toss and of a die roll
coin = ["H", "T"]
die = list(range(1, 7))
print("coin sample space :", coin)
print("die  sample space :", die)

# Each outcome is equally likely: likelihood = 1 / |Omega|
print("P(heads)   :", 1 / len(coin))
print("P(die = 4) :", 1 / len(die))

# Likelihoods over the whole sample space must sum to 1
print("sum over coin :", sum(1 / len(coin) for _ in coin))
print("sum over die  :", sum(1 / len(die) for _ in die))
```

</PyRunner>

---
layout: prism
heading: 확률 변수
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 동전 하나 던지기의 결과를 $X$라는 변수로 표기하기로 할 때, 이 $X$를 [확률 변수(random variable)]{.hl}라고 한다.

- 확률 변수는 해당 표본 공간에서 하나의 값을 특정한 확률로 취하는 변수를 의미한다.
  - 동전 던지기 예시는 표본 공간이 이산적이므로, $X$는 [이산 확률 변수(discrete random variable)]{.hl}이다.
    - 이산 확률 변수는 _관습적으로_ 대문자로 표기한다.
  - 연속 표본 공간의 확률 변수는 [연속 확률 변수(continuous random variable)]{.hl}라 하며, _관습적으로_ 소문자로 표기한다.

- 동전 던지기의 경우 $X$가 앞면일 확률은 $X$가 뒷면일 확률과 동일한 $0.5$이며, $P(X=\text{앞면})=P(X=\text{뒷면})=0.5$로 표현된다.

---
layout: prism
heading: "DIY: 확률 변수"
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)

# Coin toss as a random variable X (0 = tails, 1 = heads)
tosses = rng.integers(0, 2, size=100_000)
print("empirical P(X = heads):", round(tosses.mean(), 4), " (theory 0.5)")

# Die roll: expectation and variance estimated by sampling
rolls = rng.integers(1, 7, size=200_000)
print("sample mean :", round(rolls.mean(), 4), " (theory 3.5)")
print("sample var  :", round(rolls.var(), 4), " (theory", round(35/12, 4), ")")
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">기본 개념들</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">확률 법칙들</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">단일 사건의 확률</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">합의 법칙</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">곱의 법칙</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">생일 역설</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">조건부 확률</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">전체 확률</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">결합 확률과 주변 확률</span></p>
  </div>

</div>

---
layout: prism
heading: 단일 사건의 확률
---

- 한 표본 공간의 모든 확률을 합하면 $1$이 되므로, 표본 공간 안의 임의의 한 사건의 확률은 반드시 $1$보다 작거나 같다.

- 수식적으로는, 표본 공간의 임의의 사건 $A$에 대해,

$$
0 \leq P(A) \leq 1.
$$

- 표본 공간의 모든 사건들에 대해,

$$
\sum_i P(A_i) = 1.
$$

- 사건 $A$가 발생하지 않을 확률 $P(\bar{A})$를 [여사건(complementary event)]{.hl}의 확률이라고 하며, $P(\bar{A}) = 1 - P(A)$로 정의한다.

---
layout: prism
heading: "DIY: 단일 사건의 확률"
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)

# Rolling a die: event A = "roll a 6", complement = "not a 6"
rolls = rng.integers(1, 7, size=300_000)
pA = float(np.mean(rolls == 6))
pnotA = float(np.mean(rolls != 6))

print("P(A)          :", round(pA, 4), " (theory", round(1/6, 4), ")")
print("P(not A)      :", round(pnotA, 4))
print("P(A)+P(notA)  :", round(pA + pnotA, 4), " (must be 1)")
```

</PyRunner>

---
layout: prism
heading: 합의 법칙 (1/2)
---

- 두 사건 $A$와 $B$가 동시에 일어날 수 없을 때—즉 사건 하나가 발생하면 다른 하나가 동시에 발생할 수 없을 때—이 두 사건을 [상호 배반적(mutually exclusive)]{.hl}이라 한다.
  - 동전 앞면과 뒷면은 동시에 나올 수 없으므로, 이 둘은 상호 배반적이다.

- 만일 두 사건의 발생 확률이 서로 완전히 무관하다면—즉 어떤 사건 하나의 확률이 다른 사건의 발생 여부에 영향을 받지 않으며 그 역도 성립한다면—이 두 사건을 서로 [독립적(independent)]{.hl}이라고 한다.

- 확률의 [합의 법칙(sum rule)]{.hl}은 둘 이상의 상호 배반 사건들이 발생할 확률에 관한 것이다.
  - 주사위를 굴렸을 때 "4" 사건과 "5" 사건은 상호 배반적이며 각각 확률이 $1/6$이므로, 4 또는 5가 나올 확률은 두 확률의 합이다.

- 상호 배반 사건들에 대해, 확률의 합의 법칙은 다음과 같이 정의된다:

$$
P(A \text{ 또는 } B) = P(A \cup B) = P(A) + P(B).
$$

<div class="sub-item">

$\cup$은 "또는"(논리합, OR)과 "합집합"을 의미한다.

</div>

---
layout: prism
heading: 합의 법칙 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 위 식은 상호 배반인 사건들에 대해서만 성립하는 합의 법칙이다.

- 상호 배반이 아닌 사건들에 대해서는—즉 일반적인 경우에는—아래와 같은 합의 법칙이 적용된다:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B).
$$

- [DIY]{.hl} 어떤 주머니 안에 동전 20개가 들어 있는데, 그 중 12개는 우리나라 동전, 8개는 일본 동전이고, 우리나라 동전 중 6개는 은화, 일본 동전 중 3개가 은화이다. 주머니에서 동전 하나를 임의로 선택했을 때, 그것이 은화이거나 우리나라 동전일 확률은 얼마인가?

---
layout: prism
heading: "DIY: 동전 주머니와 합의 법칙"
---

<div style="height: 0.6rem;"></div>

<PyRunner>

```python
total = 20
korean, japanese = 12, 8
korean_silver, japanese_silver = 6, 3
silver = korean_silver + japanese_silver

P_silver = silver / total
P_korean = korean / total
P_silver_and_korean = korean_silver / total   # silver AND Korean

# Inclusion-exclusion: P(silver OR Korean)
P_union = P_silver + P_korean - P_silver_and_korean
print("P(silver)            :", P_silver)
print("P(Korean)            :", P_korean)
print("P(silver and Korean) :", P_silver_and_korean)
print("P(silver or Korean)  :", P_union)
```

</PyRunner>

---
layout: prism
heading: 곱의 법칙
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- 합의 법칙이 사건 $A$ _또는_ $B$가 발생할 확률을 의미한다면, [곱의 법칙(product rule)]{.hl}은 사건 $A$ _그리고_ $B$가 발생할 확률을 의미한다:

$$
P(A \text{ 그리고 } B) = P(A \cap B) = P(A) \cdot P(B).
$$

<div class="sub-item">

$\cap$은 "그리고"(논리곱, AND)와 "교집합"을 의미한다.

</div>

- 상호 배반인 사건이 동시에 일어날 확률이 $0$인 것은 곱의 법칙 식으로 유도할 수 없다.
  - 곱의 법칙 식은 서로 독립인 사건들에 대해 적용된다.

- 예를 들어, 전 세계 인구의 80%가 갈색 눈을 가지고 있고 50%가 여성이라고 할 때, 무작위로 선택한 사람이 갈색 눈을 가진 여성일 확률은 곱의 법칙을 적용하여 알 수 있다.

- 곱의 법칙은 두 사건에만 한정되지 않으며, 독립인 여러 사건이 동시에 일어날 확률을 계산하려면 각 사건의 확률을 전부 곱하면 된다.

---
layout: prism
heading: "DIY: 곱의 법칙"
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(2)

p_brown, p_woman = 0.8, 0.5
print("P(brown-eyed woman) = 0.8 * 0.5 =", p_brown * p_woman)

# Verify independence by simulation
n = 500_000
brown = rng.random(n) < p_brown
woman = rng.random(n) < p_woman
print("simulated P(brown & woman):", round(float(np.mean(brown & woman)), 4))
```

</PyRunner>

---
layout: prism
heading: 생일 역설
---

- 한 방에 있는 사람 중 생일이 같은 사람이 적어도 두 명일 확률이 50%를 넘으려면 방에 최소 몇 명이 있어야 하는지를 푸는 문제를 [생일 역설(birthday paradox)]{.hl}이라고 한다.

- (한 해가 반드시 365일이라고 가정하면) 임의로 선택한 두 사람의 생일이 같을 확률은 $1/365 \approx 0.00274$, 그렇지 않을 확률은 $1 - 1/365 = 364/365 \approx 0.9973$이다.

- 무작위로 선택한 두 쌍이 모두 생일이 같지 않을 확률은 곱의 법칙에 따라 $(364/365)^2 \approx 0.9945$이다.

- 비슷한 방식으로, $n$번 생일을 비교했을 때 전부 생일이 같지 않을 확률은 $(364/365)^n$이 되며, 이 확률이 $0.5$보다 낮아지려면 $n = 253$이 된다.

- 이때 $m$명 중 $2$명을 선택하는 [조합(combinations)]{.hl}이 $253$이 되어야 하므로, $\binom{m}{2} = \frac{m!}{2!(m-2)!}$이 적어도 $253$이 되는 가장 작은 $m$은 $23$이다.

---
layout: prism
heading: "DIY: 생일 역설"
---

<PyRunner>

```python
import numpy as np

# P(no shared birthday) after n pairwise comparisons: (364/365)^n
n = np.arange(0, 400)
p_none = (364/365) ** n
print("smallest n with (364/365)^n < 0.5 :", int(np.argmax(p_none < 0.5)))

# Exact: probability that m people all have distinct birthdays
def p_distinct(m):
    p = 1.0
    for k in range(m):
        p *= (365 - k) / 365
    return p

for m in [10, 22, 23, 40, 50]:
    print(f"m={m:>3}: P(at least one shared) = {1 - p_distinct(m):.4f}")
```

</PyRunner>

---
layout: prism
heading: 조건부 확률
---

- 주머니 안에 빨간 구슬 8개와 파란 구슬 2개가 들어 있을 때, 구슬 하나를 꺼냈는데 빨간 구슬이고 이를 빼둔 후 다시 구슬을 뽑을 때 또다시 빨간색이 나올 확률은 얼마인가?

- 사건 $A$가 발생했다는 사실로 인해 사건 $B$의 확률이 변한다면, 이때 둘째 사건의 확률을 $P(B|A)$로 표기하고, 사건 $A$의 발생을 조건으로 한 확률이라는 뜻에서 [조건부 확률(conditional probability)]{.hl}이라고 한다.

- 곱의 법칙 식과 다르게, 두 사건이 서로 [종속(dependent)]{.hl}인 경우—즉 독립적이지 않은 경우—곱의 법칙은 다음과 같이 정의된다:

$$
P(A, B) = P(B|A) \cdot P(A).
$$

<div class="sub-item">

$P(A, B)$는 $A$ 그리고 $B$일 확률을 의미한다.

</div>

- $P(B|A) \neq P(A|B)$임에 유의하라.

---
layout: prism
heading: "DIY: 조건부 확률"
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(3)

# Bag: 8 red, 2 blue. Draw one (red), remove it, draw again.
# Exact conditional probability P(2nd red | 1st red) = 7/9
print("exact P(red | red) :", round(7/9, 4))

trials, first_red, second_red = 200_000, 0, 0
for _ in range(trials):
    bag = ["R"] * 8 + ["B"] * 2
    a = bag.pop(rng.integers(len(bag)))
    if a == "R":
        first_red += 1
        if bag.pop(rng.integers(len(bag))) == "R":
            second_red += 1
print("simulated          :", round(second_red / first_red, 4))
```

</PyRunner>

---
layout: prism
heading: 전체 확률
---

- 표본 공간을 다수의 서로소 영역 $B_i$들($B_1, B_2, \ldots$)로 나누었다고 가정하자.
  - 서로소는 영역들에 공통 요소가 없다는, 즉 영역들이 겹치지 않는다는 것을 의미한다.
  - 이러한 $B_i$를 모두 합하면 표본 공간 전체가 된다.

- 이렇게 나뉜 각 영역(부분집합)을 집합의 [분할(partition)]{.hl}이라고 하며, 모든 분할에 관한 한 사건의 확률을 다음과 같이 계산할 수 있다:

$$
P(A) = \sum_i P(A|B_i) \cdot P(B_i).
$$

- 여기서 $P(B_i)$는 분할 $B_i$의 확률로 전체 표본 공간 중 $B_i$가 차지하는 비율이며, $P(A|B_i)$는 주어진 분할 $B_i$에서 $A$가 발생할 확률이다.
  - 이 식을 분할 $B_i$들에 관한 $A$의 [전체 확률(total probability)]{.hl}이라고 한다.

---
layout: prism
heading: "DIY: 전체 확률"
---

- [DIY]{.hl} 세 그룹에 인구가 각각 2,000명, 1,000명, 3,000명이 있고, 눈이 검정인 사람들의 비율이 순서대로 12%, 3%, 21%라고 할 때, 한 사람을 무작위로 골랐을 경우 눈이 검정일 확률은 얼마인가?

<PyRunner>

```python
sizes = [2000, 1000, 3000]
rates = [0.12, 0.03, 0.21]
total = sum(sizes)

# Law of total probability: P(black) = sum P(black | group) P(group)
P_black = sum(r * (s / total) for r, s in zip(rates, sizes))
for i, (s, r) in enumerate(zip(sizes, rates), 1):
    print(f"group {i}: P(group)={s/total:.3f}, P(black | group)={r}")
print("P(black eyes) :", round(P_black, 4))
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">기본 개념들</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률 법칙들</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">결합 확률과 주변 확률</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">결합 확률과 주변 확률</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">결합 확률표</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">확률의 연쇄법칙</span></p>
  </div>

</div>

---
layout: prism
heading: 결합 확률과 주변 확률
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 두 확률 변수의 [결합 확률(joint probability)]{.hl} $P(X=x, Y=y)$는 $X$의 값이 $x$임과 동시에 $Y$의 값이 $y$일 확률이다.
  - 결합 확률은 여러 조건이 동시에 참일 확률이다.
  - 결합 확률은 둘 이상의 확률 변수가 특정한 값들을 가질 확률이다.

- [주변 확률(marginal probability)]{.hl}은 하나 이상의 조건이 참일 확률을 그 밖의 조건들의 참·거짓 여부와 무관하게(신경 쓰지 않고) 계산한 것이다.
  - 주변 확률은 전체 확률 변수의 한 부분집합에 대해서만 계산한다.
  - 한 확률 변수의 주변 확률은 다른 모든 확률 변수가 가질 수 있는 모든 값에 관해 합산하여 구한다.

- 확률표를 이용하여 결합 확률과 주변 확률을 계산할 수 있다.

---
layout: prism
heading: 결합 확률표 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 남성은 12명 중 1명이 색맹이고, 여성은 200명 중 1명이 색맹이다.

- 1,000명을 조사하여 성별에 따른 색맹 여부를 아래 표와 같이 배열했다고 가정하자.

|        | 색맹 | 비색맹 | 합계 |
| ------ | ---- | ------ | ----- |
| 남성   | 42   | 456    | 498   |
| 여성   | 3    | 499    | 502   |
| 합계   | 45   | 955    | 1,000 |

---
layout: prism
heading: 결합 확률표 (2/3)
---

- 위 표를 [분할표(contingency table)]{.hl}라 하며, 각 칸을 1,000으로 나누면 [결합 확률표(joint probability table)]{.hl}가 된다.

|        | 색맹    | 비색맹  | 합계    |
| ------ | ------- | ------- | ------- |
| 남성   | $0.042$ | $0.456$ | $0.498$ |
| 여성   | $0.003$ | $0.499$ | $0.502$ |
| 합계   | $0.045$ | $0.955$ | $1.000$ |

---
layout: prism
heading: 결합 확률표 (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 결합 확률표를 토대로 결합 확률을 직접 읽어낼 수 있다.
  - $P(X=\text{남성}, Y=\text{색맹}) = 0.042$
  - $P(X=\text{여성}, Y=\text{비색맹}) = 0.499$

- 비슷한 방식으로 주변 확률을 계산할 수 있다.
  - $P(Y=\text{색맹}) = P(X=\text{남성}, Y=\text{색맹}) + P(X=\text{여성}, Y=\text{색맹})$

---
layout: prism
heading: "DIY: 결합 확률표"
---

- [DIY]{.hl} 아래 결합 확률표를 토대로 전체 중 과제를 제출한 주변 확률, 출석이 좋은 조건에서 과제를 제출했을 확률, 과제를 제출했으면서 성적이 $A$일 확률, 과제를 제출하지 않았으면서 성적이 $A$일 확률을 계산해보자.

| 과제   | 출석  | A       | B       | C       |
| ------ | ----- | ------- | ------- | ------- |
| 제출   | 좋음  | $0.334$ | $0.103$ | $0.087$ |
| 제출   | 나쁨  | $0.081$ | $0.103$ | $0.018$ |
| 미제출 | 좋음  | $0.051$ | $0.053$ | $0.081$ |
| 미제출 | 나쁨  | $0.003$ | $0.007$ | $0.079$ |

---
layout: prism
heading: "DIY: 결합 확률표"
---

<PyRunner>

```python
import numpy as np

# Joint probability table: rows = [man, woman], cols = [color blind, not]
J = np.array([[0.042, 0.456],
              [0.003, 0.499]])
print("P(man, color blind) :", J[0, 0])
print("P(woman, not blind) :", J[1, 1])

# Marginals: sum over the other variable
print("P(color blind)      :", round(J[:, 0].sum(), 3))
print("P(man)              :", round(J[0, :].sum(), 3))
print("total (must be 1)   :", round(J.sum(), 3))
```

</PyRunner>

---
layout: prism
heading: 확률의 연쇄법칙 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 확률 변수가 두 개이고 조건부 확률과 무조건부 확률이 모두 주어졌을 때, 결합 확률은 조건부 확률에 대한 곱의 법칙으로 구할 수 있다.

- 이를 일반화한 법칙을 [확률의 연쇄법칙(chain rule for probability)]{.hl}이라 하며, 조건부 확률 식의 확장으로 생각할 수 있다.

- 확률 변수 $n$개의 결합 확률을 위한 연쇄법칙의 일반형은 다음과 같이 정의된다:

$$
P(X_n, X_{n-1}, \ldots, X_1) = \prod_{i=1}^{n} P\left( X_i \,\Big|\, \bigcap_{j=1}^{i-1} X_j \right) = \prod_{i=1}^{n} P(X_i \mid X_1, X_2, \ldots, X_{i-1}).
$$

- 예를 들어, $P(X, Y, Z)$는 다음과 같이 분해할 수 있다:

$$
P(X, Y, Z) = P(X \mid Y, Z) \cdot P(Y, Z) = P(X \mid Y, Z) \cdot P(Y \mid Z) \cdot P(Z).
$$

<div class="sub-item">

여기서 연쇄법칙은 _연쇄적_으로 사슬(chain)을 엮듯이 적용된다.

</div>

---
layout: prism
heading: "DIY: 확률의 연쇄법칙"
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(4)

# Random joint distribution over X, Y, Z (2 values each)
P = rng.random((2, 2, 2))
P /= P.sum()

# Chain rule: P(x,y,z) = P(x | y,z) P(y | z) P(z)
Pz = P.sum(axis=(0, 1))          # P(Z)
Pyz = P.sum(axis=0)              # P(Y, Z)
Py_given_z = Pyz / Pz            # P(Y | Z)
Px_given_yz = P / Pyz            # P(X | Y, Z)
recon = Px_given_yz * Py_given_z * Pz
print("chain rule reconstructs joint:", np.allclose(recon, P))
```

</PyRunner>

---
layout: prism
heading: 확률의 연쇄법칙 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 비슷하게, 확률 변수 네 개의 결합 분해도 전개할 수 있다:

$$
\begin{aligned}
P(A, B, C, D) &= P(A \mid B, C, D) \cdot P(B, C, D) \\
&= P(A \mid B, C, D) \cdot P(B \mid C, D) \cdot P(C, D) \\
&= P(A \mid B, C, D) \cdot P(B \mid C, D) \cdot P(C \mid D) \cdot P(D).
\end{aligned}
$$

- 현재 수강생 60명 중 지난 여름방학 때 경리단길에 다녀온 학생이 총 7명이었다고 가정하자.

---
layout: prism
heading: "DIY: 확률의 연쇄법칙"
---

- [DIY]{.hl} 전체 수강생에서 무작위로 세 명을 뽑았을 때, 셋 중 아무도 경리단길에 다녀온 적이 없을 확률은 얼마인가?

<PyRunner>

```python
import numpy as np
from math import comb
rng = np.random.default_rng(5)

n, visited = 60, 7
# Exact: none of the 3 chosen has visited = C(53,3) / C(60,3)
exact = comb(n - visited, 3) / comb(n, 3)
print("exact P(none visited) :", round(exact, 4))

# Simulation (sampling three students without replacement)
pop = np.array([1] * visited + [0] * (n - visited))
trials = 200_000
hits = sum(rng.choice(pop, 3, replace=False).sum() == 0 for _ in range(trials))
print("simulated             :", round(hits / trials, 4))
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
