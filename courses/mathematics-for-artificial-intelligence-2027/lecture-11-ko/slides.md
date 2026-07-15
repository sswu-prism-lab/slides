---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 11 (KO)
download: true
info: |
  ## 인공지능수학 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-11/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">11주차: 미분</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">통계</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">선형대수 1부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">선형대수 2부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span class="text-gray-900 dark:text-gray-100">미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">행렬 미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">신경망의 데이터 흐름</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 미분
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 기계학습에서는 적분은 주로 쓰이지 않는 반면, 미분은 자주 사용된다.
  - 뉴럴 네트워크를 학습시킬 때 역전파 알고리즘을 이용하여 미분값을 구해 가중치들의 갱신 정도를 계산한다.

- 함수의 기울기 개념을 토대로, 그로부터 도함수라는 개념을 도출할 수 있다.

- 도함수는 함수의 최솟값과 최댓값을 찾기 위해서 사용할 수 있다.

- 변수가 둘 이상인 함수에 대해서 편도함수를 토대로 편미분을 정의할 수 있다.
  - 편미분은 뉴럴 네트워크의 역전파 알고리즘에 중요하게 사용된다.

- 미분의 일종인 그래디언트 연산 또한 정의한다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">기울기와 도함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">기울기</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">도함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">미분법</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">함수의 극솟값과 극댓값</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">편미분</span></p>
  </div>

</div>

---
layout: prism
heading: 기울기 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 직선은 다음과 같은 일차방정식으로 정의할 수 있다.

$$
y = ax + b
$$

<div class="sub-item">

이 때 $a$는 직선의 [기울기(slope)]{.hl}, $b$는 $y$[절편(intercept)]{.hl}, 즉 직선이 $y$축과 만나는 지점이다.

</div>

- 직선의 두 점 $(x_1, y_1)$과 $(x_0, y_0)$를 알고 있을 때, 기울기는 다음과 같이 정의된다.

$$
a = \frac{y_1 - y_0}{x_1 - x_0}
$$

- 기울기는 $x$가 변함에 따라 $y$가 얼마나 변하는지를 말해준다.
  - 기울기-절편 형태의 직선 방정식에서 기울기는 $x$와 $y$의 [비례 상수(proportionality constant)]{.hl}이고, 절편 $b$는 [상수 오프셋(constant offset)]{.hl}이다.

---
layout: prism
heading: "DIY: 직선의 기울기"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
# Slope of the line through two points (x0, y0) and (x1, y1)
def slope(p0, p1):
    return (p1[1] - p0[1]) / (p1[0] - p0[0])

for p0, p1 in [((1.0, 2.0), (4.0, 8.0)), ((0.0, 3.0), (2.0, -1.0))]:
    a = slope(p0, p1)
    b = p0[1] - a * p0[0]                 # intercept from y = a x + b
    print(f"through {p0} and {p1}:  y = {a:.2f} x + {b:.2f}")
```

</PyRunner>

---
layout: prism
heading: 기울기 (2/3)
---

<div class="flex justify-center" style="margin-top: 1.5rem;">
<div style="width: 60%;">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W11_tangent.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 기울기 (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 곡선의 두 점을 지나는 직선을 [할선(secant line)]{.hl}이라고 하고, 한 점에서 곡선과 접하기만 하는 직선을 [접선(tangent line)]{.hl}이라고 한다.

- 곡선을 따라서 접선이 계속해서 움직인다고 보면, 곡선의 [극대점(local maximum point)]{.hl} 또는 [극소점(local minimum point)]{.hl}으로 갈 때 접선의 기울기는 $0$에 접근한다.

- 접선의 기울기가 $0$이 되는 점들을 [정류점(stationary points)]{.hl}이라고 한다.

- 접선의 기울기는 여러 방면에서 유용하며, 곡선의 임의의 점에서 접선의 기울기를 계산할 수 있어야 한다.

---
layout: prism
heading: 도함수의 정의 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 곡선의 점 $x$에서 접선의 기울기를 $x$에서의 [도함수(derivative)]{.hl}라고 한다.
  - 도함수는 곡선이 점 $x$에서 어떻게 변하는지, 즉 $x$의 값이 극히 미세하게 변할 때 함수의 값이 어떻게 변하는지를 의미한다.

- 곡선 $y = f(x)$에서 두 점 $x_0$와 $x_1$을 지나는 선의 기울기 $\Delta y / \Delta x$는 다음과 같다.

$$
\frac{\Delta y}{\Delta x} = \frac{y_1 - y_0}{x_1 - x_0} = \frac{f(x_1) - f(x_0)}{x_1 - x_0}
$$

- $x_1 = x_0 + h$로 치환하면 기울기의 정의는 다음과 같다.

$$
\frac{\Delta y}{\Delta x} = \frac{f(x_0 + h) - f(x_0)}{h}
$$

---
layout: prism
heading: 도함수의 정의 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- $h \to 0$으로 두는 [극한(limit)]{.hl}을 이용하여 도함수의 정의를 유도할 수 있다.

$$
\frac{dy}{dx} = f'(x) \equiv \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

- 도함수의 도함수도 구할 수 있다.
  - $f'(x)$는 [일계도함수(first derivative)]{.hl}이며, 이를 다시 미분해서 얻은 도함수는 [이계도함수(second derivative)]{.hl}로 $f''(x)$ 또는 $d^2 y / dx^2$로 표기한다.

- [$n$계도함수($n$th derivative)]{.hl} 역시 정의할 수 있다.

---
layout: prism
heading: "DIY: 수치 도함수"
---

<div style="height: 0rem;"></div>

<PyRunner>

```python
import numpy as np

f = lambda x: x**3 - 2*x        # test function, f'(x) = 3x^2 - 2
x0 = 1.5

print(f"{'h':>10} | {'secant slope':>14} | {'|error|':>10}")
for h in [1.0, 0.1, 0.01, 1e-4, 1e-6]:
    d = (f(x0 + h) - f(x0)) / h                 # forward difference -> tangent
    print(f"{h:>10} | {d:>14.6f} | {abs(d - (3*x0**2 - 2)):>10.6f}")

# Second derivative via a central difference
h = 1e-3
d2 = (f(x0 + h) - 2*f(x0) + f(x0 - h)) / h**2
print(f"\nf''({x0}) approx {d2:.4f}   (exact 6x = {6*x0})")
```

</PyRunner>

---
layout: prism
heading: 거듭제곱 법칙
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 도함수를 구하는 데 [미분법(differentiation rules)]{.hl}을 사용할 수 있으며, 상수 $c$의 도함수는 $0$이다.

$$
\frac{d}{dx} c = 0
$$

- $x$의 거듭제곱의 미분에는 거듭제곱 법칙이 적용된다.

$$
\frac{d}{dx} a x^n = n a x^{n-1}
$$

- 미분 연산자는 선형 연산자로, 항들이 덧셈 또는 뺄셈으로 결합된 표현식의 미분은 개별 도함수들의 덧셈 또는 뺄셈이 된다.

$$
\frac{d}{dx}(f(x) \pm g(x)) = \frac{d}{dx} f(x) \pm \frac{d}{dx} g(x)
$$

---
layout: prism
heading: "DIY: 거듭제곱 법칙"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2*h)          # central difference

x = 2.0
# Power rule: d/dx a x^n = n a x^(n-1)
for a, n in [(3, 4), (1, 5), (2, 3)]:
    num = deriv(lambda t: a*t**n, x)
    print(f"d/dx {a}x^{n} at {x}: num={num:.4f}, rule={n*a*x**(n-1):.4f}")

# Linearity: (f + g)' = f' + g'
f, g = lambda t: t**3, lambda t: 2*t
lhs = deriv(lambda t: f(t) + g(t), x)
print("linearity holds:", np.isclose(lhs, deriv(f, x) + deriv(g, x)))
```

</PyRunner>

---
layout: prism
heading: 곱 법칙, 몫 법칙, 연쇄법칙
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 두 함수를 곱한 형태를 미분할 때는 곱 법칙을 적용한다.

$$
\frac{d}{dx} f(x) g(x) = f'(x) g(x) + f(x) g'(x)
$$

- 한 함수를 다른 함수로 나눈 형태를 미분할 때는 몫 법칙을 적용한다.

$$
\frac{d}{dx}\left(\frac{f(x)}{g(x)}\right) = \frac{f'(x) g(x) - f(x) g'(x)}{g^2(x)}
$$

- 합성함수의 미분에는 연쇄법칙을 적용한다.
  - 역전파 알고리즘에 기초한 뉴럴 네트워크는 이 연쇄법칙에 의존한다.

$$
\frac{d}{dx} f(g(x)) = \frac{d}{dx} f \circ g(x) = f'(g(x)) g'(x)
$$

---
layout: prism
heading: "DIY: 곱 법칙, 몫 법칙, 연쇄법칙"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2*h)

x = 1.3
f,  g  = lambda t: t**2 + 1, lambda t: np.sin(t)
fp, gp = lambda t: 2*t,      lambda t: np.cos(t)

print("product :", np.isclose(d(lambda t: f(t)*g(t), x),
                              fp(x)*g(x) + f(x)*gp(x)))
print("quotient:", np.isclose(d(lambda t: f(t)/g(t), x),
                              (fp(x)*g(x) - f(x)*gp(x)) / g(x)**2))
print("chain   :", np.isclose(d(lambda t: f(g(t)), x), fp(g(x))*gp(x)))
```

</PyRunner>

---
layout: prism
heading: 삼각함수의 미분
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 삼각함수의 미분은 다음과 같다.
  - cf. $\csc x = 1/\sin x$, $\sec x = 1/\cos x$, $\cot x = 1/\tan x$

$$
\begin{gather*}
\frac{d}{dx}\sin x = \cos x\\
\frac{d}{dx}\cos x = -\sin x\\
\frac{d}{dx}\tan x = \sec^2 x
\end{gather*}
$$

---
layout: prism
heading: "DIY: 삼각함수의 미분"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2*h)

x = 0.7
print("d/dx sin x  = cos x    :", np.isclose(d(np.sin, x), np.cos(x)))
print("d/dx cos x  = -sin x   :", np.isclose(d(np.cos, x), -np.sin(x)))
print("d/dx tan x  = sec^2 x  :", np.isclose(d(np.tan, x), 1/np.cos(x)**2))
```

</PyRunner>

---
layout: prism
heading: 지수함수의 미분
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 지수함수의 도함수는 자기 자신이다.

$$
\frac{d}{dx} e^x = e^x
$$

- 지수가 $x$의 함수일 때는 다음 법칙이 적용된다.

$$
\frac{d}{dx} e^{g(x)} = g'(x) e^{g(x)}
$$

- 일반화하면 다음과 같다.

$$
\frac{d}{dx} a^{g(x)} = \ln(a) g'(x) a^{g(x)}
$$

---
layout: prism
heading: 로그함수의 미분
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 자연로그의 도함수는 다음과 같다.

$$
\frac{d}{dx} \ln x = \frac{1}{x}
$$

- 인수가 $x$의 함수일 때는 다음 법칙이 적용된다.

$$
\frac{d}{dx} \ln g(x) = \frac{g'(x)}{g(x)}
$$

- 일반화하면 다음과 같다.

$$
\frac{d}{dx} \log_b g(x) = \frac{g'(x)}{g(x) \ln b}
$$

---
layout: prism
heading: "DIY: 지수함수와 로그함수의 미분"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2*h)

x, b = 1.4, 2.0
g = lambda t: t**2                              # inner function g(x) = x^2
print("d/dx e^x   = e^x   :", np.isclose(d(np.exp, x), np.exp(x)))
print("d/dx e^{x^2}       :", np.isclose(d(lambda t: np.exp(g(t)), x),
                                         2*x*np.exp(x**2)))
print("d/dx ln x  = 1/x   :", np.isclose(d(np.log, x), 1/x))
print("d/dx log2(x^2)     :", np.isclose(d(lambda t: np.log(g(t))/np.log(b), x),
                                         2*x/(x**2*np.log(b))))
```

</PyRunner>

---
layout: prism
heading: 함수의 극솟값과 극댓값
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 정류점을 통해 곡선 위의 임의의 점이 극솟값인지 극댓값인지를 판단할 수 있다.
  - 모든 [국소 극솟값(local minima)]{.hl} 중 가장 작은 값을 [전역 극솟값(global minimum)]{.hl}, 모든 [국소 극댓값(local maxima)]{.hl} 중 가장 큰 값을 [전역 극댓값(global maximum)]{.hl}이라 한다.

- 극솟값과 극댓값을 통틀어 [극값(extrema)]{.hl}이라고 한다.

- 그러나 단순히 도함수가 $0$인 정류점이라고 해도, 부근의 모든 점보다 작거나 크지 않다면 극소점이나 극대점이 아니다.

- 극점이 아닌 정류점을 [변곡점(inflection point)]{.hl}이라고 하며, 변수가 여러 개인 함수에서는 [안장점(saddle point)]{.hl}이라 한다.

---
layout: prism
heading: "DIY: 정류점"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

f  = lambda x: x**3 - 3*x                        # f'(x) = 3x^2 - 3 = 0 -> x = +/-1
d  = lambda g, x, h=1e-5: (g(x+h) - g(x-h)) / (2*h)
d2 = lambda g, x, h=1e-3: (g(x+h) - 2*g(x) + g(x-h)) / h**2

xs = np.linspace(-2, 2, 4001)
sign = np.sign([d(f, x) for x in xs])            # sign of the first derivative
for i in np.where(np.diff(sign) != 0)[0]:        # where f' changes sign
    x = xs[i]
    kind = "minimum" if d2(f, x) > 0 else "maximum"
    print(f"stationary near x={x:+.3f}: {kind} (f={f(x):+.3f})")
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">기울기와 도함수</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">편미분</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">편미분</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">혼합 편미분</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">편미분 연쇄법칙</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">그래디언트 계산</span></p>
  </div>

</div>

---
layout: prism
heading: 편미분의 정의
---

- 변수가 둘 이상인, 예를 들어 $f(x, y)$나 $f(x_0, x_1, x_2, \cdots, x_n)$과 같은 함수에는 [편미분(partial differentiation)]{.hl}(또는 편도함수) 기법을 사용한다.

- 편미분은 여러 변수 중 특정한 변수 하나에 대한 미분으로, 다른 변수들은 상수로 고정해 두고 한 변수에 대해서만 함수를 미분한 것이다.

- 편미분은 $\partial$ 기호를 사용하며, 예를 들어 함수 $f(x, y, z) = x^2 + y^2 + z^2 + 3xyz$의 편미분은 다음과 같다.

$$
\begin{gather*}
\frac{\partial}{\partial x} f(x, y, z) = 2x + 3yz\\
\frac{\partial}{\partial y} f(x, y, z) = 2y + 3xz\\
\frac{\partial}{\partial z} f(x, y, z) = 2z + 3xy
\end{gather*}
$$

---
layout: prism
heading: "DIY: 편미분"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
f = lambda x, y, z: x**2 + y**2 + z**2 + 3*x*y*z
h = 1e-6
x, y, z = 1.0, 2.0, 3.0

fx = (f(x+h, y, z) - f(x-h, y, z)) / (2*h)
fy = (f(x, y+h, z) - f(x, y-h, z)) / (2*h)
fz = (f(x, y, z+h) - f(x, y, z-h)) / (2*h)

print("df/dx:", round(fx, 4), " exact 2x+3yz =", 2*x + 3*y*z)
print("df/dy:", round(fy, 4), " exact 2y+3xz =", 2*y + 3*x*z)
print("df/dz:", round(fz, 4), " exact 2z+3xy =", 2*z + 3*x*y)
```

</PyRunner>

---
layout: prism
heading: 혼합 편미분
---

<style>
.slidev-layout ul > li {
  margin-top: 3.8em;
}
</style>

- 도함수의 도함수를 취할 수 있는 것과 마찬가지로, 편도함수의 편도함수를 취하는 것도 가능하다.

- 혼합 편미분은 대상 변수를 다르게 둘 수 있으며, 예를 들어 함수 $f(x, y, z) = x^2 + y^2 + z^2 + 3xyz$의 혼합 편미분의 예시는 다음과 같다.

$$
\frac{\partial}{\partial x}\frac{\partial}{\partial y} f(x, y, z) = \frac{\partial^2}{\partial x\, \partial y} f(x, y, z) = 3z
$$

---
layout: prism
heading: "DIY: 혼합 편미분"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

f = lambda x, y, z: x**2 + y**2 + z**2 + 3*x*y*z
h = 1e-4
x, y, z = 1.0, 2.0, 3.0

dy = lambda x, y, z: (f(x, y+h, z) - f(x, y-h, z)) / (2*h)
dx = lambda x, y, z: (f(x+h, y, z) - f(x-h, y, z)) / (2*h)

fxy = (dy(x+h, y, z) - dy(x-h, y, z)) / (2*h)     # d/dx of (df/dy)
fyx = (dx(x, y+h, z) - dx(x, y-h, z)) / (2*h)     # d/dy of (df/dx)

print("d2f/dxdy:", round(fxy, 3), " (exact 3z =", 3*z, ")")
print("symmetric (fxy == fyx):", np.isclose(fxy, fyx, atol=1e-3))
```

</PyRunner>

---
layout: prism
heading: 편미분 연쇄법칙
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- $f(x, y)$의 $x$와 $y$가 각각 또 다른 변수에 대한 함수 $x(r, s)$와 $y(r, s)$일 때, $f$의 $r$과 $s$에 대한 편도함수를 구하려면 $x$와 $y$ 각각에 연쇄법칙을 적용해야 한다.

$$
\begin{gather*}
\frac{\partial f}{\partial r} = \left(\frac{\partial f}{\partial x}\right)\left(\frac{\partial x}{\partial r}\right) + \left(\frac{\partial f}{\partial y}\right)\left(\frac{\partial y}{\partial r}\right)\\
\frac{\partial f}{\partial s} = \left(\frac{\partial f}{\partial x}\right)\left(\frac{\partial x}{\partial s}\right) + \left(\frac{\partial f}{\partial y}\right)\left(\frac{\partial y}{\partial s}\right)
\end{gather*}
$$

---
layout: prism
heading: "DIY: 편미분 연쇄법칙"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

f = lambda x, y: x**2 + x*y
x = lambda r, s: r*s
y = lambda r, s: r + s
h = 1e-6
r0, s0 = 1.5, 2.0

F = lambda r, s: f(x(r, s), y(r, s))
direct = (F(r0+h, s0) - F(r0-h, s0)) / (2*h)      # df/dr directly

xv, yv = x(r0, s0), y(r0, s0)
fx = (f(xv+h, yv) - f(xv-h, yv)) / (2*h)
fy = (f(xv, yv+h) - f(xv, yv-h)) / (2*h)
xr = (x(r0+h, s0) - x(r0-h, s0)) / (2*h)
yr = (y(r0+h, s0) - y(r0-h, s0)) / (2*h)
chain = fx*xr + fy*yr                             # df/dr via chain rule
print("df/dr direct:", round(direct, 4), " chain rule:", round(chain, 4))
print("match:", np.isclose(direct, chain))
```

</PyRunner>

---
layout: prism
heading: 그래디언트 계산
---

- 다변수 함수 $f(x, y, z)$를 좌표축에서의 각 위치로 해석한다면, $f$는 3차원 공간의 임의의 점 $(x, y, z)$에서 하나의 스칼라 값을 돌려주는 함수로 생각할 수 있다.
  - 이를 벡터 $\mathbf{x} = (x, y, z)$로 둔다면 $f(\mathbf{x})$는 하나의 벡터를 하나의 스칼라로 사상하는 함수가 된다.
  - 벡터를 받고 스칼라를 돌려주는 함수를 [스칼라장(scalar field)]{.hl}이라고 한다.

- [그래디언트(gradient)]{.hl}는 벡터를 받는 함수의 도함수이며, 수학에서는 편미분을 $n$차원으로 확장한 것에 해당한다.

- 그래디언트는 $\nabla$ 연산자를 사용하며, 그래디언트, 델, 나블라 등으로 부른다.

$$
\nabla f(\mathbf{x}) = \nabla f(x_0, x_1, \ldots, x_n) \equiv \begin{bmatrix}
\frac{\partial f}{\partial x_0}\\
\frac{\partial f}{\partial x_1}\\
\vdots\\
\frac{\partial f}{\partial x_n}
\end{bmatrix}
$$

---
layout: prism
heading: "DIY: 그래디언트"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

f = lambda v: v[0]**2 + v[1]**2 + v[2]**2 + 3*v[0]*v[1]*v[2]

def gradient(f, v, h=1e-6):
    v = np.asarray(v, float)
    g = np.zeros_like(v)
    for i in range(len(v)):
        e = np.zeros_like(v); e[i] = h
        g[i] = (f(v + e) - f(v - e)) / (2*h)
    return g

x = np.array([1.0, 2.0, 3.0])
grad  = gradient(f, x)
exact = np.array([2*x[0] + 3*x[1]*x[2], 2*x[1] + 3*x[0]*x[2], 2*x[2] + 3*x[0]*x[1]])
print("nabla f :", np.round(grad, 4))
print("exact   :", exact)
print("match   :", np.allclose(grad, exact))
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
