---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 3 (KO)
download: true
info: |
  ## 인공지능수학 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-3/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">3주차: 함수 해석</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span class="text-gray-900 dark:text-gray-100">함수 해석</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">확률 1부</span></p>
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
heading: 함수 해석
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 수학에서는 각각의 개체들 사이에 대응되는 규칙이나 관계를 정의할 필요가 있다.

- 함수는 수학에서 어떤 집합의 원소를 다른 집합의 원소에 대응시키는 관계를 의미한다.

- 수학을 비롯하여 과학과 공학 등에서도 변수들 사이의 관계를 나타내고, 그러한 현상을 간결한 모델을 통해 표현할 때 함수를 사용한다.

- 데이터 분석의 관점에서도 함수를 통해 데이터의 패턴을 파악할 수 있다.

- 오늘 수업에서는 다음과 같은 것들을 다룰 것이다:
  - 함수의 정의와 집합론적 관점에서의 성질
  - 다양한 함수의 종류와 그래프
  - 좌표평면 상 함수의 이동

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">함수의 정의</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">함수의 성질</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">함수와 그래프</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">함수의 이동</span></p>
  </div>

</div>

---
layout: prism
heading: 함수 (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 집합 $X$에서 집합 $Y$로 대응하는 [함수(function)]{.hl} $f$는 각 $x \in X$를 유일한 $y = f(x) \in Y$로 대응시키는 규칙으로, $f : X \mapsto Y$로 표기한다.
  - $y = f(x)$에서 $y$는 $x$의 [상(image)]{.hl}, $x$는 $y$의 [원상(preimage)]{.hl}이라 한다.
  - 집합 $X$는 함수 $f$의 [정의역(domain)]{.hl}, $Y$는 $f$의 [공역(codomain)]{.hl} 또는 [치역(range)]{.hl}이라 한다.

- 좀 더 엄밀한 관점에서 함수는 관계, 즉 [순서쌍(ordered pair)]{.hl}의 집합이다.
  - 각 순서쌍의 왼편이 원상, 오른편이 상이 된다.
  - 즉, 집합론적 관점에서 함수는 어떠한 식이 아닌 값의 대응, [사상(mapping)]{.hl}으로 바라본 것이다.

- [DIY]{.hl} 함수 $f : \mathbb{R} \mapsto \mathbb{R},\ f(x) = x^2$를 집합론에서의 정의에 따라 표현하라.

---
layout: prism
heading: 함수 (2/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>


- 정의역이 $X$, 공역이 $Y$인 함수의 엄밀한 정의는 다음과 같다:

$$
f = \{ (x, y) \mid x \in X \wedge y \in Y \} \text{ s.t. } \forall (x, y) \in f\ \forall (x, y') \in f;\ y = y'
$$

<div class="sub-item">

즉, 각 $x \in X$는 정확히 하나의 $y \in Y$만을 가진다.

</div>


- 함수 $f : X \mapsto Y$에서 $i \neq j$인 모든 $x_i, x_j \in X$에 대해 $f(x_i) \neq f(x_j)$가 성립하면, $f$를 [일대일(one-to-one)]{.hl} 또는 [단사(injective)]{.hl}라고 한다.
  - 정의역의 서로 다른 두 점이 같은 상을 가질 수 없음을 의미한다.

- $f(X) = Y$일 경우 $f$를 $X$에서 $Y$ [위로(onto)]{.hl}의 함수 또는 [전사(surjective)]{.hl}라고 한다.

- $f$가 단사이며 전사일 경우 이를 [일대일 대응(one-to-one correspondence)]{.hl} 또는 [전단사(bijective)]{.hl}라고 한다.
  - 각 $y \in Y$를 그 [역상(inverse image)]{.hl} $x = f^{-1}(y)$로 유일하게 대응시키는 [역함수(inverse function)]{.hl} $f^{-1} : Y \mapsto X$가 존재한다.

---
layout: prism
heading: 함수 (3/4)
---

- 집합 $X$에 대해 [항등함수(identity function)]{.hl} $i_X : X \mapsto X$는 다음과 같이 정의된다.

$$
i_X(x) = x, \quad x \in X.
$$

- 함수 $f : X \mapsto Y$와 $g : Y \mapsto Z$에 대하여 [합성함수(composite function)]{.hl} $g \circ f : X \mapsto Z$는 다음과 같이 정의된다.

$$
g \circ f(x) = g(f(x)), \quad x \in X.
$$

- [DIY]{.hl} 실수 영역에서 정의되는 함수 $f(x) = \sqrt{x - 1}$과 $g(x) = 3x$가 주어졌을 때, $f \circ g(x)$의 정의역을 구하라.

<PyRunner>

```python
import numpy as np

# f(x)=sqrt(x-1), g(x)=3x  =>  (f o g)(x) = f(3x) = sqrt(3x - 1)
# domain requires 3x - 1 >= 0  =>  x >= 1/3
for x in [-0.5, 0.0, 1/3, 0.5, 1.0, 2.0]:
    inside = 3*x - 1
    if inside >= 0:
        print(f"x={x:6.3f} -> (f o g)(x) = sqrt({inside:6.3f}) = {np.sqrt(inside):.4f}")
    else:
        print(f"x={x:6.3f} -> undefined  (3x-1={inside:6.3f} < 0)")

print("domain of f o g : x >= 1/3 =", round(1/3, 4))
```

</PyRunner>

---
layout: prism
heading: 함수 (4/4)
---

- 정의역의 서로 다른 부분에서 서로 다른 식을 사용하여 함수를 묘사하는 경우가 있는데, 이를 [조각적 정의(piecewise definition)]{.hl}라 한다.

- 조각적 정의를 이용한 [절댓값(absolute value)]{.hl} 함수의 정의는 아래와 같다.

$$
|x| = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{otherwise} \end{cases}
$$

- [DIY]{.hl} 입력값 $x$가 양수이면 $+1$, $0$이면 $0$, 음수이면 $-1$을 출력하는 [부호함수(sign function)]{.hl} $\operatorname{sgn} x$를 조각적 정의를 이용하여 표기하시오.

<PyRunner>

```python
import numpy as np
def sgn(x):
    if x > 0:  return 1
    if x < 0:  return -1
    return 0
for x in [-3.2, -1, 0, 0.5, 7]:
    print(f"sgn({x:>4}) = {sgn(x):>2}")
print("matches numpy sign:", all(sgn(x) == np.sign(x) for x in [-3.2, -1, 0, 0.5, 7]))
```

</PyRunner>

---
layout: prism
heading: 함수의 성질 (1/2)
---

- 집합 $X$에 대하여 $X$에 대한 [관계(relation)]{.hl} $R$은 $X \times X$의 부분집합이며, $(x, y) \in R$이면 $x$는 $R$에 의해 $y$와 [관계가 있다(related)]{.hl}고 하고 $xRy$로 표기한다.

<div class="theorem-box">
<div class="theorem-box-title">동치 관계</div>
<div class="theorem-box-body">

집합 $X$의 [동치 관계(equivalence relation)]{.hl}는 아래 세 가지 성질을 만족하는 관계이다.

<div class="sub-item-enum">

1. [반사적(reflexive)]{.hl} 성질: $xRx,\ \forall x \in X$
2. [대칭적(symmetric)]{.hl} 성질: $xRy \Rightarrow yRx$
3. [전이적(transitive)]{.hl} 성질: $xRy,\ yRz \Rightarrow xRz$

</div>
</div>
</div>

- 관계 $\approx$가 $X$에 대한 동치 관계일 때, [동치류(equivalence class)]{.hl} $[x]$는 $x \in X$에 대해 $\approx$ 관계가 있는 $X$의 모든 원소를 모은 집합으로, $[x] = \{ y \in X : y \approx x \}$로 정의된다.

---
layout: prism
heading: 함수의 성질 (2/2)
---

- 함수가 어떤 점에서 끊김 없이 정의되는 성질을 [연속성(continuity)]{.hl}이라 하며, $\lim_{x \to a} f(x) = f(a)$이면 $f(x)$는 $x = a$에서 연속이라고 한다.

- 어떤 함수의 _도함수_ 가 존재하는 성질을 [미분 가능성(differentiability)]{.hl}이라 한다.
  - 미분 가능하면 연속이다.

- 함수가 정의역 내에서 항상 증가하거나 항상 감소하는 성질을 [단조성(monotonicity)]{.hl}이라 한다.
  - 단조 증가 함수: $x_1 < x_2 \Rightarrow f(x_1) \leq f(x_2)$
  - 단조 감소 함수: $x_1 < x_2 \Rightarrow f(x_1) \geq f(x_2)$

- 일정한 간격마다 함수 값이 반복되는 성질을 [주기성(periodicity)]{.hl}이라 한다.

- 함수가 특정 축이나 점에 대해 대칭적인 성질을 [대칭성(symmetry)]{.hl}이라 한다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">함수</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">함수와 그래프</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">실함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">복소함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">다변수함수</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">함수의 이동</span></p>
  </div>

</div>

---
layout: prism
heading: 실함수 (1/5)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

- 실수집합의 부분집합을 정의역으로 하고 실수집합을 공역으로 하는 함수를 [실함수(real-valued function)]{.hl}라 한다.

- $f$가 정의역이 $D$인 함수라면, $f$의 그래프는 $\{ (x, f(x)) \mid x \in D \}$이다.
  - 실함수의 경우 정의역과 공역이 실수이므로, 그 그래프는 $\mathbb{R} \times \mathbb{R}$, 즉 평면의 부분집합으로 나타낼 수 있다.

- 예를 들어 함수 $f(x) = x + 2$의 그래프는 $y = x + 2$인 점 $(x, y)$의 집합이며, $x = 0$인 점을 $y$절편, $y = 0$인 점을 $x$절편이라 한다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_line.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 실함수 (2/5)
---

<div class="grid grid-cols-2 gap-1" style="margin-top: 0rem; grid-template-columns: 1.5fr 1fr">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.3em;
}
</style>

- 실함수의 일종인 [일차함수(linear function)]{.hl} $f(x) = ax + b$는 다음 성질들을 만족한다:
  - 기울기는 $a$이다.
  - 일대일 대응이며 단조함수이다.
  - $x$절편은 $-\frac{b}{a}$이며 $y$절편은 $b$이다.
  - 도함수 $f'(x) = a$로 상수함수이다.

- _다항식_ 으로 이루어진 함수를 [다항함수(polynomial function)]{.hl}이라 한다.

- 수학 및 물리학에서 중요한 역할을 하는 [르장드르 함수(Legendre function)]{.hl}는 다음과 같이 정의된다.

$$
P_n(x) = \frac{1}{2^n n!} \frac{\mathrm{d}^n}{\mathrm{d}x^n}(x^2 - 1)^n.
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_legendre.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 실함수"
---

<PyRunner>

```python
import numpy as np

x = np.linspace(-1, 1, 5)
P = [np.ones_like(x), x.copy()]            # P0 = 1, P1 = x
for n in range(1, 3):                      # Bonnet's recurrence
    P.append(((2*n + 1) * x * P[n] - n * P[n-1]) / (n + 1))

closed = [np.ones_like(x), x, 0.5*(3*x**2 - 1), 0.5*(5*x**3 - 3*x)]
for n in range(4):
    print(f"P{n}(x) =", np.round(P[n], 3), " matches closed form:", np.allclose(P[n], closed[n]))
```

</PyRunner>

---
layout: prism
heading: 실함수 (3/5)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem; grid-template-columns: 1.5fr 1fr">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 공역의 집합이 연속이 아닌 함수를 [이산함수(discrete function)]{.hl}라고 하며, 그 예시로는 [계단함수(step function)]{.hl}가 있다.

- [DIY]{.hl} 아래 그래프의 계단 함수 $u(x)$를 수식으로 표현하라.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_step.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

<PyRunner>

```python
import numpy as np

# Heaviside step: u(x) = 0 for x < 0, and 1 for x >= 0
def u(x):
    return np.where(x >= 0, 1.0, 0.0)

xs = np.linspace(-3, 3, 7)
print("x    :", xs)
print("u(x) :", u(xs))
print("jump at 0: u(-0.001)=%d, u(0)=%d, u(0.001)=%d" % (u(-0.001), u(0.0), u(0.001)))
```

</PyRunner>

---
layout: prism
heading: 실함수 (4/5)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [디랙-델타 함수(Dirac-delta function)]{.hl}는 여러 파형을 근사하기 위해 사용되는 함수 중 하나이며, 아래는 그 예시 중 하나이다:

$$
\delta_n(x) = \begin{cases} \dfrac{n}{2} & \text{if } |x| \leq \dfrac{1}{n} \\ 0 & \text{otherwise} \end{cases}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_dirac.svg" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 실함수"
---

<PyRunner>

```python
import numpy as np

# delta_n(x) = n/2 for |x| <= 1/n, else 0.  Its integral over R should be 1 for every n.
def integral(n, N=200000):
    x = np.linspace(-1, 1, N)
    y = np.where(np.abs(x) <= 1/n, n/2, 0.0)
    dx = x[1] - x[0]
    return float(np.sum(y) * dx)          # Riemann sum

for n in [5, 10, 50, 200]:
    print(f"n={n:4d}  peak height = {n/2:7.1f}   integral over R = {integral(n):.4f}")
```

</PyRunner>

---
layout: prism
heading: 실함수 (5/5)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 함수로서 일반적으로 만족시킬 것으로 여겨지는 성질들을 만족시키지 않는 함수를 특별히 [병리적 함수(pathological function)]{.hl}이라고 한다.

- 병리적 함수의 하나인 [토메 함수(Thomae's function)]{.hl}는 아래와 같이 정의된다.

$$
f(x) = \begin{cases} 1 & x = 0 \\ \dfrac{1}{q} & x = \dfrac{p}{q},\ \gcd(p, q) = 1,\ q > 0 \\ 0 & x \notin \mathbb{Q} \end{cases}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_thomae.svg" class="tikz-fig" style="width: 80%;" />

</div>
</div>

- [DIY]{.hl} 아래 [디리클레 함수(Dirichlet's function)]{.hl} $\mathbf{1}_{\mathbb{Q}}(x)$의 정의를 확인하고 그래프를 그려보라: $\ \mathbf{1}_{\mathbb{Q}}(x) = 1$ if $x \in \mathbb{Q}$, and $0$ if $x \notin \mathbb{Q}$.

---
layout: prism
heading: "DIY: 실함수"
---

<PyRunner>

```python
from math import gcd

# Thomae's function on a rational p/q in lowest terms: f(p/q) = 1/q
def thomae(p, q):
    g = gcd(p, q)
    p, q = p // g, q // g
    return 0.0 if q == 0 else 1.0 / q

for (p, q) in [(1, 2), (2, 4), (1, 3), (2, 3), (1, 7), (3, 9), (0, 1)]:
    print(f"f({p}/{q}) = {thomae(p, q):.4f}")

print("f(1/2) == f(2/4):", thomae(1, 2) == thomae(2, 4), "(same reduced fraction)")
```

</PyRunner>

---
layout: prism
heading: 복소함수 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.1em;
}
</style>


- [복소함수(complex-valued function)]{.hl}는 정의역과 공역이 복소수 집합으로 확장된 함수를 의미한다.

- 복소함수 $f(z)$가 어떤 영역에서 복소 미분 가능하면, 그 함수는 해당 영역에서 [해석성(analyticity)]{.hl}을 갖는다고 하며, 이는 실함수의 미분 가능성보다 더 엄격한 조건이다.

- 해석적인 복소함수를 [홀로모픽 함수(holomorphic function)]{.hl}이라고도 한다.

---
layout: prism
heading: 복소함수 (2/2)
---

<div class="theorem-box">
<div class="theorem-box-title">코시-리만 방정식</div>
<div class="theorem-box-body">

함수 $f(z) = u(z) + iv(z)$가 복소평면 $\mathbb{C}$의 열린 집합에서 정의될 때, 이 함수가 해석적일 [필요충분조건(Cauchy-Riemann equations)]{.hl}은 다음과 같다.

$$
\begin{cases} \dfrac{\partial u}{\partial x} = \dfrac{\partial v}{\partial y} \\[4pt] \dfrac{\partial u}{\partial y} = -\dfrac{\partial v}{\partial x} \end{cases}
$$

</div>
</div>

---
layout: prism
heading: "DIY: 복소함수"
---

<PyRunner>

```python
import numpy as np

# f(z) = z^2 = (x^2 - y^2) + i(2xy)  =>  u = x^2 - y^2,  v = 2xy
u = lambda x, y: x**2 - y**2
v = lambda x, y: 2*x*y
h = 1e-6
def d(f, x, y, axis):
    if axis == 'x': return (f(x+h, y) - f(x-h, y)) / (2*h)
    return (f(x, y+h) - f(x, y-h)) / (2*h)

for (x, y) in [(1.0, 2.0), (-0.5, 0.3)]:
    ux, vy = d(u, x, y, 'x'), d(v, x, y, 'y')
    uy, vx = d(u, x, y, 'y'), d(v, x, y, 'x')
    print(f"z=({x}, {y}):  u_x=v_y? {np.isclose(ux, vy)}    u_y=-v_x? {np.isclose(uy, -vx)}")
```

</PyRunner>

---
layout: prism
heading: 다변수함수
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem; grid-template-columns: 1.6fr 1fr;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.3em;
}
</style>

- [다변수함수(multivariate function)]{.hl}란 두 개 이상의 독립변수에 따라 그 값이 정해지는 함수를 의미한다.

- 다변수함수에서는 [편미분(partial differentiation)]{.hl}을 정의할 수 있다.

- 오른쪽 그래프는 함수 $z = x^2 - y^2$를 시각화한 것이다.
  - [DIY]{.hl} $\partial z / \partial x$를 구하라.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_mesh.svg" class="tikz-fig" style="width: 70%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 다변수함수"
---

<PyRunner>

```python
import numpy as np

z = lambda x, y: x**2 - y**2
h = 1e-6
for (x, y) in [(1.0, 1.0), (2.0, -3.0), (0.5, 4.0)]:
    dzdx = (z(x+h, y) - z(x-h, y)) / (2*h)     # partial derivative wrt x
    print(f"(x,y)=({x}, {y}):  numeric dz/dx = {dzdx:.4f},  analytic 2x = {2*x:.4f}")
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">함수</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">함수와 그래프</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">함수의 이동</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">평행 이동</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">대칭 이동</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">확대 및 축소</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">회전</span></p>
  </div>

</div>

---
layout: prism
heading: 평행 이동 (1/2)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 함수의 [평행 이동(translation)]{.hl}은 일반적으로 두 가지 방법으로 나뉜다.

- 함수 $f(x)$를 $x$축 방향으로 $h$만큼 이동시키는 것을 [수평 이동(horizontal shift)]{.hl}이라 하며 다음과 같이 계산한다:

$$
y = f(x - h).
$$

  - $h > 0$인 경우 그래프는 오른쪽으로 $h$만큼 이동한다.
  - $h < 0$인 경우 그래프는 왼쪽으로 $|h|$만큼 이동한다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_translate.svg" class="tikz-fig" style="width: 100%; margin-top: 6rem" />

</div>
</div>

---
layout: prism
heading: 평행 이동 (2/2)
---

- 함수 $f(x)$를 $y$축 방향으로 $k$만큼 이동시키는 것을 [수직 이동(vertical shift)]{.hl}이라 하며 다음과 같이 계산한다:

$$
y = f(x) + k.
$$

  - $k > 0$인 경우 그래프는 위로 $k$만큼 이동한다.
  - $k < 0$인 경우 그래프는 아래로 $|k|$만큼 이동한다.

- [DIY]{.hl} $f(x) = 3x + 2$를 $-7$만큼 평행 이동시킨 결과를 그리라.

<PyRunner>

```python
import numpy as np

f = lambda x: 3*x + 2
xs = np.array([-1.0, 0.0, 1.0, 2.0])
print("x             :", xs)
print("f(x) = 3x+2   :", f(xs))
print("vertical  -7  :", f(xs) - 7)          # y = f(x) - 7 = 3x - 5
print("horizontal -7 :", f(xs - (-7)))       # y = f(x-h), h=-7  =>  f(x+7) = 3x + 23
```

</PyRunner>

---
layout: prism
heading: 대칭 이동
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.6fr 1fr;">
<div>

- 함수를 축에 대해 대칭되도록 이동시키는 것을 [대칭 이동(reflection)]{.hl}이라 하며, $x$축 대칭의 경우 $y = -f(x)$, $y$축 대칭의 경우 $y = f(-x)$가 된다.

<PyRunner>

```python
import numpy as np

f = lambda x: x**2
xs = np.linspace(-2, 2, 5)
print("x               :", xs)
print("f(x) = x^2      :", f(xs))
# reflection across the x-axis
print("x-axis  y=-f(x) :", -f(xs))
# reflection across the y-axis (even -> unchanged)
print("y-axis  y=f(-x) :", f(-xs))
```

</PyRunner>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_reflect.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 확대 및 축소 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 함수를 [확대(scaling)]{.hl}하거나 [축소(dilation)]{.hl}할 수 있다.

- 수직 방향 확대/축소의 경우, 함수에 상수 $a$를 곱하여 $y$축 방향으로 그래프를 확대 또는 축소한다:

$$
y = a f(x)
$$

  - $|a| > 1$인 경우 그래프는 $y$축 방향으로 $a$배 확대된다.
  - $0 < |a| < 1$인 경우 그래프는 $y$축 방향으로 $a$배 축소된다.
  - $a < 0$인 경우에는 동시에 $x$축에 대해 대칭 이동된다.

---
layout: prism
heading: 확대 및 축소 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 수평 방향 확대/축소의 경우, 입력값에 상수 $b$를 곱하여 $x$축 방향으로 그래프를 확대 또는 축소한다:

$$
y = f(bx)
$$

  - $|b| > 1$인 경우 그래프는 $x$축 방향으로 $1/b$배 축소된다.
  - $0 < |b| < 1$인 경우 그래프는 $x$축 방향으로 $1/b$배 확대된다.
  - $b < 0$인 경우에는 동시에 $y$축에 대해 대칭 이동된다.

---
layout: prism
heading: 회전
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.6fr 1fr;">
<div>

- 일반적으로 $(x, y)$를 각도 $\theta$만큼 [회전(rotation)]{.hl}시켜 $(x', y')$을 얻기 위해서는 아래와 같은 좌표 변환을 적용한다:

$$
\begin{gathered} x' = x\cos\theta - y\sin\theta \\ y' = x\sin\theta + y\cos\theta \end{gathered}
$$

<PyRunner>

```python
import numpy as np

theta = np.pi / 4 # rotate by 45 degrees
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
pts = np.array([[1, 0], [0, 1], [1, 1]], float).T # columns are points
rot = R @ pts
for i in range(pts.shape[1]):
    x, y = pts[:, i]
    xr, yr = rot[:, i]
    print(f"({x:.0f}, {y:.0f}) -> ({xr:7.4f}, {yr:7.4f})")

print("length preserved:", 
      np.allclose(np.linalg.norm(pts, axis=0), 
                  np.linalg.norm(rot, axis=0)))
```

</PyRunner>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_rotate.svg" class="tikz-fig" style="width: 100%; margin-top: 3rem" />

</div>
</div>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
