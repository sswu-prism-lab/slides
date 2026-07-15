---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 12 (KO)
download: true
info: |
  ## 인공지능수학 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-12/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">12주차: 행렬 미분</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span class="text-gray-900 dark:text-gray-100">행렬 미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">신경망의 데이터 흐름</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 행렬 미분
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 기계학습은 주로 벡터와 행렬을 다루므로, 이러한 다차원, 다랭크의 객체들과 관련된 도함수를 표현하기 위한 표기법과 접근 방식이 필요하다.
  - 벡터의 스칼라 함수인 그래디언트가 그러한 접근 방식 중 하나이다.

- 행렬 미분에는 다양한 종류가 있으며, 행렬 미분이 관여하는 항등식들도 존재한다.

- 행렬 미분과 관련된 특별한 행렬들을 다루게 되며, 이들은 기계학습과 뉴럴 네트워크의 최적화와 관련이 있다.
  - 특히, 뉴럴 네트워크를 학습하는 것은 본질적으로 하나의 최적화 문제이다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">행렬 미분 공식</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">표기법과 레이아웃</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스칼라 인수 벡터 함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">벡터 인수 스칼라 함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">벡터 인수 벡터 함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스칼라 인수 행렬 함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">행렬 인수 스칼라 함수</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">미분 항등식</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">야코비 행렬과 헤세 행렬</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">행렬 미분 예제</span></p>
  </div>

</div>

---
layout: prism
heading: 표기법과 레이아웃
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 그래디언트를 제외하면, 지난 시간에 다룬 미분은 모두 스칼라 함수를 입력으로 받아 스칼라를 돌려주는 함수의 미분이었다.
  - 그래디언트는 벡터를 입력으로 받아 스칼라를 돌려준다.

- 행렬 미분 표기법에는 두 가지 관례, 즉 [분자 중심 표현(numerator layout)]{.hl}과 [분모 중심 표현(denominator layout)]{.hl}이 있다.
  - 학문 분야마다 사용하는 관례가 다르고, 여러 표기법을 섞어 쓰는 경우도 흔하다.
  - 본 수업에서는 분자 중심 표현을 사용한다.

- 일반적으로 한 표기법은 다른 표기법의 전치이다.

---
layout: prism
heading: "스칼라 인수 벡터 함수 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

- 스칼라를 입력으로 받아 벡터를 돌려주는 함수 $\mathbf{f}(x): \mathbb{R} \mapsto \mathbb{R}^m$를 가정하자.
  - 여기서 $m$은 출력 벡터의 차원이다.
  - 이러한 함수를 [벡터값 함수(vector-valued function)]{.hl}라고 부른다.
  - 그 예시 중 하나가 3차원 공간의 [매개변수 곡선(parametric curve)]{.hl}이다:

$$
\mathbf{f}(t) = t\cos(t)\,\hat{\mathbf{x}} + t\sin(t)\,\hat{\mathbf{y}} + t\,\hat{\mathbf{z}}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W12_helix.svg" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "스칼라 인수 벡터 함수 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 행렬 미분 표기법에서는 함수 $\mathbf{f}$를 다음과 같이 함수들로 이루어진 열벡터로 표기한다:

$$
\mathbf{f}(t) = \begin{bmatrix} t\cos(t)\\ t\sin(t)\\ t \end{bmatrix}
$$

- 일반화하면, 성분이 $n$개인 함수 $\mathbf{f}$는 다음과 같이 표기한다.

$$
\mathbf{f}(x) = \begin{bmatrix} f_0(x)\\ f_1(x)\\ \vdots\\ f_{n-1}(x) \end{bmatrix}
$$

---
layout: prism
heading: "스칼라 인수 벡터 함수 (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- $\mathbf{f}(x)$의 도함수를 [접벡터(tangent vector)]{.hl}라 하며, 다음과 같이 정의된다.

$$
\frac{\partial \mathbf{f}}{\partial x} = \begin{bmatrix} \partial f_0/\partial x\\ \partial f_1/\partial x\\ \vdots\\ \partial f_{n-1}/\partial x \end{bmatrix}
$$

- [DIY]{.hl} 아래 함수의 접벡터를 구하라.

$$
\mathbf{f}(x) = \begin{bmatrix} 2x^2 - 3x + 2\\ x^3 - 3 \end{bmatrix}
$$

---
layout: prism
heading: "DIY: 접벡터"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# Tangent vector via central finite differences
def tangent(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

# Parametric curve (helix): f(t) = [t cos t, t sin t, t]
helix = lambda t: np.array([t*np.cos(t), t*np.sin(t), t])
t0 = 1.0
exact = np.array([np.cos(t0) - t0*np.sin(t0), np.sin(t0) + t0*np.cos(t0), 1.0])
print("helix tangent (num)  :", np.round(tangent(helix, t0), 5))
print("helix tangent (exact):", np.round(exact, 5))

# DIY: f(x) = [2x^2 - 3x + 2, x^3 - 3]  ->  f'(x) = [4x - 3, 3x^2]
poly = lambda x: np.array([2*x**2 - 3*x + 2, x**3 - 3])
x0 = 2.0
print("poly tangent (num)   :", np.round(tangent(poly, x0), 5))
print("poly tangent (exact) :", [4*x0 - 3, 3*x0**2])
```

</PyRunner>

---
layout: prism
heading: "벡터 인수 스칼라 함수"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 벡터를 입력으로 받아 스칼라를 돌려주는 함수 $f: \mathbb{R}^m \mapsto \mathbb{R}$를 [스칼라장(scalar field)]{.hl}이라고 한다.

- 이 함수의 도함수는 기울기이다. 행렬 미분 표기법에서 $f(\mathbf{x})$의 $\partial f/\partial \mathbf{x}$는 다음과 같이 표기한다.
  - $\mathbf{x} = [x_0\quad x_1\quad \cdots\quad x_{m-1}]^\top$

$$
\frac{\partial f}{\partial \mathbf{x}} = \left[ \frac{\partial f}{\partial x_0}\quad \frac{\partial f}{\partial x_1}\quad \cdots\quad \frac{\partial f}{\partial x_{m-1}} \right]
$$

- 그러나 분자 중심 표현에서 $\partial f/\partial \mathbf{x}$는 행벡터이므로, 좀 더 엄밀하게는 다음과 같다.

$$
\nabla f(\mathbf{x}) = \left[ \frac{\partial f}{\partial \mathbf{x}} \right]^\top
$$

---
layout: prism
heading: "DIY: 스칼라장의 기울기"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# Scalar field  f(x) = x0^2 + 3 x0 x1 + 2 x1^2
f = lambda x: x[0]**2 + 3*x[0]*x[1] + 2*x[1]**2

def grad(f, x, h=1e-6):
    x = np.asarray(x, float)
    g = np.zeros_like(x)
    for i in range(len(x)):
        e = np.zeros_like(x); e[i] = h
        g[i] = (f(x + e) - f(x - e)) / (2 * h)
    return g

x = np.array([1.0, 2.0])
print("numerical gradient :", np.round(grad(f, x), 5))
print("analytic gradient  :", [2*x[0] + 3*x[1], 3*x[0] + 4*x[1]])
```

</PyRunner>

---
layout: prism
heading: "벡터 인수 벡터 함수"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 스칼라 인수 벡터 함수의 도함수는 열벡터, 벡터 인수 스칼라 함수의 도함수는 행벡터이며, 벡터 인수 벡터 함수 $\mathbf{f}: \mathbb{R}^m \mapsto \mathbb{R}^n$의 도함수는 행렬이다.

$$
\frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix}
\frac{\partial f_0}{\partial x_0} & \frac{\partial f_0}{\partial x_1} & \cdots & \frac{\partial f_0}{\partial x_{m-1}}\\
\frac{\partial f_1}{\partial x_0} & \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_{m-1}}\\
\vdots & \vdots & \ddots & \vdots\\
\frac{\partial f_{n-1}}{\partial x_0} & \frac{\partial f_{n-1}}{\partial x_1} & \cdots & \frac{\partial f_{n-1}}{\partial x_{m-1}}
\end{bmatrix}
= \begin{bmatrix}
\nabla f_0(\mathbf{x})^\top\\
\nabla f_1(\mathbf{x})^\top\\
\vdots\\
\nabla f_{n-1}(\mathbf{x})^\top
\end{bmatrix}
$$

---
layout: prism
heading: "DIY: 유한차분을 이용한 야코비"
---

<PyRunner>

```python
import numpy as np

# f: R^2 -> R^2,  f(x) = [4 x0 - 2 x0 x1,  2 x1 + x0 x1 - 2 x1^2]
def f(x):
    return np.array([4*x[0] - 2*x[0]*x[1],
                     2*x[1] + x[0]*x[1] - 2*x[1]**2])

def jacobian(f, x, h=1e-6):
    x = np.asarray(x, float); n = len(x)
    fx = f(x); J = np.zeros((len(fx), n))
    for j in range(n):
        e = np.zeros(n); e[j] = h
        J[:, j] = (f(x + e) - f(x - e)) / (2 * h)
    return J

x = np.array([2.0, 2.0])
print("numerical Jacobian at (2, 2):\n", np.round(jacobian(f, x), 4))
print("analytic  Jacobian at (2, 2):\n",
      np.array([[4 - 2*x[1], -2*x[0]], [x[1], 2 + x[0] - 4*x[1]]], float))
```

</PyRunner>

---
layout: prism
heading: "스칼라 인수 행렬 함수"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 스칼라를 입력으로 받아 행렬을 돌려주는 함수 $\mathbf{F}: \mathbb{R} \mapsto \mathbb{R}^{n \times m}$를 정의할 수 있다:

$$
\mathbf{F} = \begin{bmatrix}
f_{0,0}(x) & f_{0,1}(x) & \cdots & f_{0,m-1}(x)\\
f_{1,0}(x) & f_{1,1}(x) & \cdots & f_{1,m-1}(x)\\
\vdots & \vdots & \ddots & \vdots\\
f_{n-1,0}(x) & f_{n-1,1}(x) & \cdots & f_{n-1,m-1}(x)
\end{bmatrix}
$$

- 이 함수의 미분은 각 스칼라 함수의 도함수로 구성되며, 이를 [접행렬(tangent matrix)]{.hl}이라 한다.

$$
\frac{\partial \mathbf{F}}{\partial x} = \begin{bmatrix}
\frac{\partial f_{0,0}}{\partial x} & \cdots & \frac{\partial f_{0,m-1}}{\partial x}\\
\vdots & \ddots & \vdots\\
\frac{\partial f_{n-1,0}}{\partial x} & \cdots & \frac{\partial f_{n-1,m-1}}{\partial x}
\end{bmatrix}
$$

---
layout: prism
heading: "행렬 인수 스칼라 함수"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 행렬을 입력으로 받아 스칼라를 돌려주는 함수 $f(\mathbf{X}): \mathbb{R}^{n \times m} \mapsto \mathbb{R}$의 도함수를 [기울기 행렬(gradient matrix)]{.hl}이라 하며, 다음과 같이 정의된다.

$$
\frac{\partial f}{\partial \mathbf{X}} = \begin{bmatrix}
\frac{\partial f}{\partial x_{0,0}} & \frac{\partial f}{\partial x_{1,0}} & \cdots & \frac{\partial f}{\partial x_{n-1,0}}\\
\frac{\partial f}{\partial x_{0,1}} & \frac{\partial f}{\partial x_{1,1}} & \cdots & \frac{\partial f}{\partial x_{n-1,1}}\\
\vdots & \vdots & \ddots & \vdots\\
\frac{\partial f}{\partial x_{0,m-1}} & \frac{\partial f}{\partial x_{1,m-1}} & \cdots & \frac{\partial f}{\partial x_{n-1,m-1}}
\end{bmatrix}
$$

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">행렬 미분 공식</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">미분 항등식</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">벡터 인수 스칼라 함수 관련 항등식</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스칼라 인수 벡터 함수 관련 항등식</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">벡터 인수 벡터 함수 관련 항등식</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">행렬 인수 스칼라 함수 관련 항등식</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">야코비 행렬과 헤세 행렬</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">행렬 미분 예제</span></p>
  </div>

</div>

---
layout: prism
heading: "벡터 인수 스칼라 함수 관련 항등식 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 함수 $f$와 $g$를 벡터 $\mathbf{x}$를 받아 스칼라를 돌려주는 함수, $a$를 $\mathbf{x}$에 의존하지 않는 스칼라라고 하면, 다음과 같은 기본 법칙들이 성립한다:

$$
\begin{gather*}
\frac{\partial}{\partial \mathbf{x}}(af) = a\frac{\partial f}{\partial \mathbf{x}}\\
\frac{\partial}{\partial \mathbf{x}}(f + g) = \frac{\partial f}{\partial \mathbf{x}} + \frac{\partial g}{\partial \mathbf{x}}\\
\frac{\partial}{\partial \mathbf{x}}(fg) = f\frac{\partial g}{\partial \mathbf{x}} + g\frac{\partial f}{\partial \mathbf{x}}\\
\frac{\partial}{\partial \mathbf{x}}f \circ g = \frac{\partial f}{\partial g}\frac{\partial g}{\partial \mathbf{x}}
\end{gather*}
$$

---
layout: prism
heading: "DIY: 스칼라장의 연쇄법칙"
---

- [DIY]{.hl} $\mathbf{x} = [x_0, x_1, x_2]^\top$, $g(\mathbf{x}) = x_0 + x_1 x_2$, $f(g) = g^2$가 주어졌을 때, $f$의 $\mathbf{x}$에 대한 도함수를 구하라.

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# g(x) = x0 + x1 x2,  f(g) = g^2  ->  df/dx = 2 g(x) * [1, x2, x1]
g = lambda x: x[0] + x[1]*x[2]
f = lambda x: g(x)**2

def grad(f, x, h=1e-6):
    x = np.asarray(x, float); out = np.zeros_like(x)
    for i in range(len(x)):
        e = np.zeros_like(x); e[i] = h
        out[i] = (f(x + e) - f(x - e)) / (2 * h)
    return out

x = np.array([1.0, 2.0, 3.0])
print("numerical df/dx :", np.round(grad(f, x), 4))
print("chain-rule df/dx:", np.round(2*g(x) * np.array([1.0, x[2], x[1]]), 4))
```

</PyRunner>

---
layout: prism
heading: "벡터 인수 스칼라 함수 관련 항등식 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- $\mathbf{a}$를 $\mathbf{x}$에 의존하지 않는 상수 벡터라고 하면, 다음 법칙이 성립한다:

$$
\frac{\partial}{\partial \mathbf{x}}(\mathbf{a} \cdot \mathbf{x}) = \frac{\partial}{\partial \mathbf{x}}(\mathbf{a}^\top \mathbf{x}) = \mathbf{a}^\top
$$

- 벡터값 함수 $\mathbf{f}$와 $\mathbf{g}$에 대해, 다음 항등식들이 성립한다:

$$
\begin{gather*}
\frac{\partial}{\partial \mathbf{x}}(\mathbf{a} \cdot \mathbf{f}) = \frac{\partial}{\partial \mathbf{x}}(\mathbf{a}^\top \mathbf{f}) = \mathbf{a}^\top \frac{\partial \mathbf{f}}{\partial \mathbf{x}}\\
\frac{\partial}{\partial \mathbf{x}}(\mathbf{f} \cdot \mathbf{g}) = \frac{\partial}{\partial \mathbf{x}}(\mathbf{f}^\top \mathbf{g}) = \mathbf{f}^\top \frac{\partial \mathbf{g}}{\partial \mathbf{x}} + \mathbf{g}^\top \frac{\partial \mathbf{f}}{\partial \mathbf{x}}
\end{gather*}
$$

---
layout: prism
heading: "스칼라 인수 벡터 함수 관련 항등식"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 스칼라 인수 벡터 함수에는 다음과 같은 법칙이 성립한다:

$$
\begin{gather*}
\frac{\partial}{\partial x}(a\mathbf{f}) = a\frac{\partial \mathbf{f}}{\partial x} \qquad
\frac{\partial}{\partial x}(\mathbf{A}\mathbf{f}) = \mathbf{A}\frac{\partial \mathbf{f}}{\partial x} \qquad
\frac{\partial}{\partial x}(\mathbf{f} + \mathbf{g}) = \frac{\partial \mathbf{f}}{\partial x} + \frac{\partial \mathbf{g}}{\partial x}\\
\frac{\partial}{\partial x}\mathbf{f} \circ \mathbf{g} = \frac{\partial \mathbf{f}}{\partial \mathbf{g}}\frac{\partial \mathbf{g}}{\partial x} \qquad
\frac{\partial}{\partial x}(\mathbf{f} \cdot \mathbf{g}) = \mathbf{f}^\top \frac{\partial \mathbf{g}}{\partial x} + \mathbf{g}^\top \frac{\partial \mathbf{f}}{\partial x}
\end{gather*}
$$

- $f(\mathbf{g})$와 $\mathbf{g}(x)$의 합성은 다음과 같다.

$$
\frac{\partial}{\partial x}f \circ \mathbf{g} = \frac{\partial f}{\partial \mathbf{g}} \cdot \frac{\partial \mathbf{g}}{\partial x} = \frac{\partial f}{\partial \mathbf{g}}\frac{\partial \mathbf{g}}{\partial x}
$$

---
layout: prism
heading: "벡터 인수 벡터 함수 관련 항등식"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.6em;
}
</style>

- 기계학습의 역전파 과정에서 쓰이는 [손실함수(loss function)]{.hl}의 도함수가 바로 벡터 인수 벡터 함수의 도함수이며, 다음과 같은 법칙이 성립한다:

$$
\begin{gather*}
\frac{\partial}{\partial \mathbf{x}}(a\mathbf{f}) = a\frac{\partial \mathbf{f}}{\partial \mathbf{x}} \qquad
\frac{\partial}{\partial \mathbf{x}}(\mathbf{A}\mathbf{f}) = \mathbf{A}\frac{\partial \mathbf{f}}{\partial \mathbf{x}}\\
\frac{\partial}{\partial \mathbf{x}}(\mathbf{f} + \mathbf{g}) = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} + \frac{\partial \mathbf{g}}{\partial \mathbf{x}} \qquad
\frac{\partial}{\partial \mathbf{x}}\mathbf{f} \circ \mathbf{g} = \frac{\partial \mathbf{f}}{\partial \mathbf{g}}\frac{\partial \mathbf{g}}{\partial \mathbf{x}}
\end{gather*}
$$

---
layout: prism
heading: "행렬 인수 스칼라 함수 관련 항등식"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.6em;
}
</style>

- 행렬을 받아 스칼라를 돌려주는 함수의 도함수는 다음과 같은 법칙들을 만족한다:

$$
\begin{gather*}
\frac{\partial}{\partial \mathbf{X}}(f + g) = \frac{\partial f}{\partial \mathbf{X}} + \frac{\partial g}{\partial \mathbf{X}} \qquad
\frac{\partial}{\partial \mathbf{X}}(fg) = f\frac{\partial g}{\partial \mathbf{X}} + g\frac{\partial f}{\partial \mathbf{X}}\\
\frac{\partial}{\partial \mathbf{X}}f \circ g = \frac{\partial f}{\partial g}\frac{\partial g}{\partial \mathbf{X}}
\end{gather*}
$$

---
layout: prism
heading: "DIY: 기울기 행렬"
---

- [DIY]{.hl} $\mathbf{X} = \begin{bmatrix} x_0 & x_1\\ x_2 & x_3 \end{bmatrix}$, $f(g) = \frac{1}{2}g^2$, $g(\mathbf{X}) = x_0 x_3 + x_1 x_2$일 때, $\partial f/\partial \mathbf{X}$를 구하라.

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# X = [[x0, x1], [x2, x3]],  g = x0 x3 + x1 x2,  f = 1/2 g^2
def g(X): return X[0, 0]*X[1, 1] + X[0, 1]*X[1, 0]
def f(X): return 0.5 * g(X)**2

def grad_mat(f, X, h=1e-6):
    G = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            E = np.zeros_like(X); E[i, j] = h
            G[i, j] = (f(X + E) - f(X - E)) / (2 * h)
    return G

X = np.array([[1., 2.], [3., 4.]])
gv = g(X)
print("numerical df/dX:\n", np.round(grad_mat(f, X), 4))
print("analytic  df/dX:\n",
      np.array([[gv*X[1, 1], gv*X[1, 0]], [gv*X[0, 1], gv*X[0, 0]]]))
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">행렬 미분 공식</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">미분 항등식</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">야코비 행렬과 헤세 행렬</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">야코비 행렬</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">헤세 행렬</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">행렬 미분 예제</span></p>
  </div>

</div>

---
layout: prism
heading: 야코비 행렬
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [야코비 행렬(Jacobian matrix)]{.hl}은 다음과 같이 정의된다.

$$
\mathbf{J}_\mathbf{x} = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix}
\frac{\partial f_0}{\partial x_0} & \cdots & \frac{\partial f_0}{\partial x_{m-1}}\\
\vdots & \ddots & \vdots\\
\frac{\partial f_{n-1}}{\partial x_0} & \cdots & \frac{\partial f_{n-1}}{\partial x_{m-1}}
\end{bmatrix} = \begin{bmatrix}
\nabla f_0(\mathbf{x})^\top\\
\vdots\\
\nabla f_{n-1}(\mathbf{x})^\top
\end{bmatrix}
$$

- 야코비 행렬은 기울기들을 쌓은 것으로 볼 수 있다.
  - 이는 일계도함수의 일반화이다.
  - 벡터값 함수가 어떤 점 $\mathbf{x}$ 부근에서 어떻게 움직이는지에 관한 정보를 제공한다.

- 야코비 행렬은 연립 미분방정식을 풀거나 벡터값 함수의 해를 구하는 데 사용된다.

---
layout: prism
heading: "야코비 행렬 - 연립 미분방정식 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- [미분방정식(differential equation)]{.hl}은 함숫값과 그 도함수가 함께 등장하는 방정식이다.

- 두 함수 $x(t)$와 $y(t)$가 있고, $x(t)$의 변화가 $x$뿐 아니라 $y$에도 의존하며 $y(t)$ 역시 같은 방식으로 결합되어, 다음과 같은 연립방정식이 주어진다고 하자:

$$
\frac{dx}{dt} = 4x - 2xy \qquad \frac{dy}{dt} = 2y + xy - 2y^2
$$

- 이 연립방정식은 다음과 같은 하나의 벡터값 함수로 표현된다:

$$
\mathbf{f}(\mathbf{x}) = \begin{bmatrix} f_0\\ f_1 \end{bmatrix} = \begin{bmatrix} 4x_0 - 2x_0 x_1\\ 2x_1 + x_0 x_1 - 2x_1^2 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} x_0\\ x_1 \end{bmatrix}
$$

---
layout: prism
heading: "야코비 행렬 - 연립 미분방정식 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- $\mathbf{f}$의 임계점은 $\mathbf{f} = \mathbf{0}$인 점들이며, 유도 과정은 생략하면 다음과 같다.

$$
\mathbf{c}_0 = \begin{bmatrix} 0\\ 0 \end{bmatrix}, \quad \mathbf{c}_1 = \begin{bmatrix} 0\\ 1 \end{bmatrix}, \quad \mathbf{c}_2 = \begin{bmatrix} 2\\ 2 \end{bmatrix}
$$

- $\mathbf{f}(\mathbf{x})$의 야코비 행렬은 다음과 같다.

$$
\mathbf{J} = \begin{bmatrix}
\partial f_0/\partial x_0 & \partial f_0/\partial x_1\\
\partial f_1/\partial x_0 & \partial f_1/\partial x_1
\end{bmatrix} = \begin{bmatrix}
4 - 2x_1 & -2x_0\\
x_1 & 2 + x_0 - 4x_1
\end{bmatrix}
$$

- 각 임계점에서 야코비 행렬을 구하면:

$$
\mathbf{J}|_{\mathbf{x} = \mathbf{c}_0} = \begin{bmatrix} 4 & 0\\ 0 & 2 \end{bmatrix}, \quad
\mathbf{J}|_{\mathbf{x} = \mathbf{c}_1} = \begin{bmatrix} 2 & 0\\ 1 & -2 \end{bmatrix}, \quad
\mathbf{J}|_{\mathbf{x} = \mathbf{c}_2} = \begin{bmatrix} 0 & -4\\ 2 & -4 \end{bmatrix}
$$

---
layout: prism
heading: "야코비 행렬 - 연립 미분방정식 (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 각 야코비 행렬의 고윳값을 계산하면 각 임계점을 [특징지을(characterize)]{.hl} 수 있다.

- 두 고윳값이 모두 실수이고 부호가 같으면, 그 임계점은 [마디점(node)]{.hl}이다.
  - 고윳값이 음수이면 그 마디점은 안정적이고, 그렇지 않으면 불안정하다.
    - 안정적인 마디점은 구덩이와 같아 근처의 것이 안으로 떨어지고, 불안정한 마디점은 봉우리와 같다.

- 두 고윳값이 모두 실수이고 부호가 반대이면, 그 임계점은 [안장점(saddle point)]{.hl}이며 불안정하다. 한 방향으로는 굴러 들어오고 다른 방향으로는 굴러 나간다.
  - 뉴럴 네트워크 학습에서 찾는 손실함수의 극소점 대부분은 실제로는 안장점일 가능성이 크다.

- 고윳값이 복소수이면 그 임계점은 [나선형(spiral)]{.hl}이며, 실수부가 음수이면 안정적이고 그렇지 않으면 불안정하다.
  - 두 고윳값은 서로 켤레복소수이므로 실수부의 부호는 항상 같다.

---
layout: prism
heading: "DIY: 임계점에서의 고윳값"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# J(x) = [[4 - 2x1, -2x0], [x1, 2 + x0 - 4x1]] at the critical points
def J(x):
    x0, x1 = x
    return np.array([[4 - 2*x1, -2*x0], [x1, 2 + x0 - 4*x1]], float)

crits = {"c0": [0, 0], "c1": [0, 1], "c2": [2, 2]}
for name, c in crits.items():
    ev = np.linalg.eigvals(J(c))
    if np.all(np.isreal(ev)):
        kind = "saddle" if ev[0].real * ev[1].real < 0 else "node"
    else:
        kind = "spiral"
    print(f"{name} at {c}: eigenvalues = {np.round(ev, 3)}  ->  {kind}")
```

</PyRunner>

---
layout: prism
heading: "야코비 행렬 - 뉴턴 방법 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 앞서 나온 임계값은 간단히 대수적으로 풀 수 있지만, 실제 문제가 이렇게 간단하리라는 보장은 없다.

- 함수의 근을 구하는 고전적인 방법으로 [뉴턴 방법(Newton's method)]{.hl}이 있으며, 이는 일계도함수와 초기 추측값에서 출발하여 반복적으로 근을 개선한다.
  - 일차원 함수의 경우, 뉴턴 방법은 다음과 같이 해를 개선한다:

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

  - 초기 추측값부터 시작해 $x_n$이 거의 변하지 않을 때까지(즉, 수렴할 때까지) 반복하면, 그때의 $x_n$이 우리가 찾던 근의 근사값이다.

- [DIY]{.hl} $f(x) = x^2$에서 초기값을 $1$로 두고 뉴턴 방법으로 근을 찾아보라.

---
layout: prism
heading: "야코비 행렬 - 뉴턴 방법 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 뉴턴 방법을 벡터 인수 벡터 함수로 확장하려면 야코비 행렬의 역행렬을 사용한다.

- 보다 일반적인 뉴턴 반복식은 다음과 같이 정의된다.

$$
\mathbf{x}_{n+1} = \mathbf{x}_n - \mathbf{J}^{-1}|_{\mathbf{x} = \mathbf{x}_n}\mathbf{f}(\mathbf{x}_n)
$$

- 뉴턴 방법으로 모든 임계점을 찾으려면 초기 추측값을 적절히 바꾸어 가며 선택해야 한다.

---
layout: prism
heading: "DIY: 뉴턴 방법"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

# Newton's method:  x_{n+1} = x_n - f(x_n) / f'(x_n)
f  = lambda x: x**2
df = lambda x: 2*x

x = 1.0
for n in range(6):
    print(f"n = {n}: x = {x:.6f},  f(x) = {f(x):.3e}")
    x = x - f(x) / df(x)

print("Newton's method converges toward the root x = 0")
```

</PyRunner>

---
layout: prism
heading: "헤세 행렬 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 야코비 행렬이 단변수 함수의 일계도함수를 일반화한 것이라면, [헤세 행렬(Hessian matrix)]{.hl} $\mathbf{H}_f$는 이계도함수를 일반화한 것이다.
  - 헤세 행렬은 스칼라장에만 한정된다.

- $\mathbf{x} = [x_0, x_1, \cdots, x_{n-1}]^\top$에 대해, $f(\mathbf{x})$의 헤세 행렬은 다음과 같이 정의된다.

$$
\mathbf{H}_f = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_0^2} & \frac{\partial^2 f}{\partial x_0 \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_0 \partial x_{n-1}}\\
\frac{\partial^2 f}{\partial x_1 \partial x_0} & \frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_{n-1}}\\
\vdots & \vdots & \ddots & \vdots\\
\frac{\partial^2 f}{\partial x_{n-1} \partial x_0} & \frac{\partial^2 f}{\partial x_{n-1} \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_{n-1}^2}
\end{bmatrix}
$$

- [DIY]{.hl} $f(\mathbf{x}) = 2x_0^2 + x_0 x_2 + 3x_1 x_2 - x_1^2$의 헤세 행렬을 구하라.

---
layout: prism
heading: "헤세 행렬 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 헤세 행렬은 스칼라장의 기울기의 야코비 행렬이다:

$$
\mathbf{H}_f = \mathbf{J}(\nabla f)
$$

- 이계도함수를 이용하면 함수의 임계점이 극소점인지($f'' > 0$) 극대점인지($f'' < 0$) 알 수 있다.

- 헤세 행렬의 고윳값이 모두 양수이면 임계점은 극소점, 모두 음수이면 극대점이며, 부호가 섞여 있으면 안장점이다.

---
layout: prism
heading: "DIY: 수치 헤세 행렬"
---

<PyRunner>

```python
import numpy as np

# f(x) = 2 x0^2 + x0 x2 + 3 x1 x2 - x1^2
f = lambda x: 2*x[0]**2 + x[0]*x[2] + 3*x[1]*x[2] - x[1]**2

def hessian(f, x, h=1e-4):
    x = np.asarray(x, float); n = len(x)
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            ei = np.zeros(n); ei[i] = h
            ej = np.zeros(n); ej[j] = h
            H[i, j] = (f(x+ei+ej) - f(x+ei-ej) - f(x-ei+ej) + f(x-ei-ej)) / (4*h*h)
    return H

x = np.array([1.0, -1.0, 2.0])
print("numerical Hessian:\n", np.round(hessian(f, x), 3))
print("analytic Hessian :\n", np.array([[4, 0, 1], [0, -2, 3], [1, 3, 0]], float))
```

</PyRunner>

---
layout: prism
heading: "헤세 행렬 - 최적화 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 뉴럴 네트워크를 학습한다는 것은, 1차 근사에서 보면, 손실함수를 최소화하는 [가중치(weights)]{.hl}와 [바이어스(biases)]{.hl}를 찾는 최적화 문제이다.

- 전적으로 기울기(일계도함수)에만 의존하는 알고리즘을 [일차 최적화 방법(first-order optimization method)]{.hl}이라고 한다.
  - 이는 기울기의 반대 방향으로 이동하면 함숫값이 작아진다는 점을 활용하여, 상수 $\eta$([단계 크기(step size)]{.hl})를 사용한다:

$$
x_n = x_{n-1} - \eta f'(x_{n-1})
$$

- 헤세 행렬은 이계도함수이므로, 기울기 외에 기울기가 어떻게 변하는지에 관한 정보([곡률(curvature)]{.hl})도 담고 있다.

- 헤세 행렬을 이용해 최적화하는 알고리즘을 [이차 최적화 방법(second-order optimization method)]{.hl}이라고 한다.

---
layout: prism
heading: "헤세 행렬 - 최적화 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 스칼라장에서 최적화 방법을 적용하려면 단순한 도함수가 아닌 기울기를 고려해야 한다.
  - 기울기를 따라 내려가는 [경사하강법(gradient descent)]{.hl}의 일반항은 다음과 같다.

$$
\mathbf{x}_1 = \mathbf{x}_0 - \eta \nabla f(\mathbf{x}_0)
$$

- 이계도함수를 이용해서도 최적화를 수행할 수 있으며, 스칼라장의 경우 다음과 같이 최적화한다.

$$
\mathbf{x}_{n+1} = \mathbf{x}_n - \mathbf{H}_f^{-1}|_{\mathbf{x}_n}\nabla f(\mathbf{x}_n)
$$

- 뉴턴 방법은 일계도함수만 사용하는 경사하강법보다 빠르게 수렴하는 경향이 있지만, 실제로 뉴럴 네트워크는 뉴턴 방법이 아닌 경사하강법으로 학습한다.
  - 헤세 행렬은 적용 대상에 제약이 있고 계산이 복잡하여 [시간복잡도(time complexity)]{.hl}가 매우 크다.

---
layout: prism
heading: "DIY: 경사하강법 vs. 뉴턴 스텝"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# Convex scalar field  f(x) = x0^2 + 3 x1^2
grad = lambda x: np.array([2*x[0], 6*x[1]])
H = np.array([[2., 0.], [0., 6.]])

x_gd = np.array([3.0, 3.0]); eta = 0.1
for _ in range(20):
    x_gd = x_gd - eta * grad(x_gd)

x_nt = np.array([3.0, 3.0])
x_nt = x_nt - np.linalg.solve(H, grad(x_nt))   # a single Newton step

print("gradient descent (20 steps):", np.round(x_gd, 4))
print("Newton (single step)       :", np.round(x_nt, 4))
print("true minimizer             : [0. 0.]")
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">행렬 미분 공식</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">미분 항등식</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">야코비 행렬과 헤세 행렬</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">행렬 미분 예제</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">성분별 연산의 도함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">활성화 함수의 도함수</span></p>
  </div>

</div>

---
layout: prism
heading: "성분별 연산의 도함수 (1/2)"
---

- 두 벡터의 덧셈을 고려하자.

$$
\mathbf{f} = \mathbf{a} + \mathbf{b} = \begin{bmatrix} f_0\\ f_1\\ \vdots\\ f_{n-1} \end{bmatrix} = \begin{bmatrix} a_0 + b_0\\ a_1 + b_1\\ \vdots\\ a_{n-1} + b_{n-1} \end{bmatrix}
$$

- 이 벡터의 야코비 행렬 $\partial \mathbf{f}/\partial \mathbf{a}$는 다음과 같다.

$$
\frac{\partial \mathbf{f}}{\partial \mathbf{a}} = \begin{bmatrix}
\frac{\partial f_0}{\partial a_0} & 0 & \cdots & 0\\
0 & \frac{\partial f_1}{\partial a_1} & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & \frac{\partial f_{n-1}}{\partial a_{n-1}}
\end{bmatrix} = \mathbf{I}
$$

- 마찬가지로 $\partial \mathbf{f}/\partial \mathbf{b} = \mathbf{I}$이며, 뺄셈의 경우 $\partial \mathbf{f}/\partial \mathbf{a} = \mathbf{I}$, $\partial \mathbf{f}/\partial \mathbf{b} = -\mathbf{I}$이다.

---
layout: prism
heading: "성분별 연산의 도함수 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- $\mathbf{a}$와 $\mathbf{b}$의 성분별 곱셈의 야코비 행렬들은 다음과 같다.

$$
\begin{aligned}
\frac{\partial \mathbf{f}}{\partial \mathbf{a}} &= \begin{bmatrix}
\frac{\partial(a_0 b_0)}{\partial a_0} & 0 & \cdots & 0\\
0 & \frac{\partial(a_1 b_1)}{\partial a_1} & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & \frac{\partial(a_{n-1} b_{n-1})}{\partial a_{n-1}}
\end{bmatrix} = \begin{bmatrix}
b_0 & 0 & \cdots & 0\\
0 & b_1 & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & b_{n-1}
\end{bmatrix}\\
\frac{\partial \mathbf{f}}{\partial \mathbf{b}} &= \begin{bmatrix}
a_0 & 0 & \cdots & 0\\
0 & a_1 & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & a_{n-1}
\end{bmatrix}
\end{aligned}
$$

---
layout: prism
heading: "DIY: 성분별 야코비"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# Element-wise product  f = a * b  ->  df/da = diag(b),  df/db = diag(a)
a = np.array([2.0, -1.0, 3.0])
b = np.array([5.0, 4.0, -2.0])
f = lambda a, b: a * b

def jac_a(a, b, h=1e-6):
    n = len(a); J = np.zeros((n, n))
    for j in range(n):
        e = np.zeros(n); e[j] = h
        J[:, j] = (f(a + e, b) - f(a - e, b)) / (2 * h)
    return J

print("df/da (numerical):\n", np.round(jac_a(a, b), 3))
print("diag(b)          :", b)
print("is diagonal      :", np.allclose(jac_a(a, b), np.diag(b)))
```

</PyRunner>

---
layout: prism
heading: 활성화 함수의 도함수
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 뉴럴 네트워크의 한 [층(layer)]{.hl}에서는 이전 층의 출력 $\mathbf{x}$에 가중치 벡터 $\mathbf{w}$를 성분별로 곱해 합한 뒤(즉, 내적한 뒤), 스칼라 $b$를 더한다.

- 그런 다음 [비선형 활성화 함수(nonlinear activation function)]{.hl}로 비선형성을 부여한다.
  - 비선형 활성화 함수가 없으면 층을 아무리 쌓아도 무의미하다.

- 주로 사용되는 비선형 활성화 함수 중 하나인 ReLU 함수는 다음과 같이 정의된다.

$$
\operatorname{ReLU}(z) = \max(0, z) = \begin{cases} 0 & z \leq 0\\ z & z > 0 \end{cases}
$$

- 따라서 뉴럴 네트워크의 한 층은 다음과 같다.

$$
y = \operatorname{ReLU}(\mathbf{w} \cdot \mathbf{x} + b)
$$

---
layout: prism
heading: "DIY: ReLU 층의 기울기"
---

- [DIY]{.hl} $\partial y/\partial \mathbf{w}$와 $\partial y/\partial b$를 구하라.

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# y = ReLU(w . x + b)  ->  dy/dw = x if z > 0 else 0,  dy/db = 1 if z > 0 else 0
w = np.array([0.5, -1.0, 2.0])
x = np.array([1.0, 2.0, 1.0])
b = 0.5
relu = lambda z: max(0.0, z)
y = lambda w, b: relu(w @ x + b)

def grad_w(w, b, h=1e-6):
    g = np.zeros_like(w)
    for i in range(len(w)):
        e = np.zeros_like(w); e[i] = h
        g[i] = (y(w + e, b) - y(w - e, b)) / (2 * h)
    return g

z = w @ x + b
print("z = w . x + b =", z)
print("dy/dw (num)   :", np.round(grad_w(w, b), 4), " exact:", x if z > 0 else np.zeros_like(x))
print("dy/db (num)   :", round((y(w, b + 1e-6) - y(w, b - 1e-6)) / 2e-6, 4),
      " exact:", 1.0 if z > 0 else 0.0)
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
