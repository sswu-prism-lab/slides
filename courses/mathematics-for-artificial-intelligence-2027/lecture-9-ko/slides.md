---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 9 (KO)
download: true
info: |
  ## 인공지능수학 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-9/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">9주차: 선형대수 1부</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span class="text-gray-900 dark:text-gray-100">선형대수 1부</span></p>
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
heading: 선형대수
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.8fr 1fr;">
<div>

- 협의의 선형대수는 일차방정식에 관한 것이지만, 본 수업에서 다루고자 하는 광의의 [선형대수(linear algebra)]{.hl}는 벡터나 행렬과 같은 다차원 객체들과 그러한 객체들에 대한 연산을 포괄한다.

- 일반적으로 기계학습에 적용되는 선형대수는 다차원 수학 객체들의 연산의 집합이며, 딥러닝 알고리즘은 데이터를 벡터나 행렬 같은 객체들로 취급한다.

- 스칼라, 벡터, 행렬, 텐서는 사실상 모두 차수가 다른 텐서이며, 텐서 연산을 이용하여 일반화된 방식으로 표현할 수 있다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W09_00.png" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">선형대수 객체</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스칼라, 벡터</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">행렬, 텐서</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">텐서 산술 연산</span></p>
  </div>

</div>

---
layout: prism
heading: 스칼라, 벡터 (1/2)
---

- [스칼라(scalar)]{.hl}는 우리가 가장 기본적으로 사용하는, 하나의 성분만을 가진 수치이다.
  - $7$, $-3$, $\pi$와 같은 수치가 스칼라이다.
  - 관습적으로 $x$와 같은 형태로 표현한다.

- [벡터(vector)]{.hl}는 여러 개의 성분으로 이루어진 1차원 배열을 의미한다.
  - 각 성분이 수직으로 배치된 형태의 벡터를 행벡터라고 하며, 수평으로 배치된 형태의 벡터를 열벡터라고 한다.
  - 관습적으로 따로 명시하지 않는 한 벡터는 열벡터를 의미하며, $\mathbf{x}$와 같은 형태로 표현한다.
  - 벡터의 $i$번째 성분은 관습적으로 $x_i$로 표현한다.

$$
\mathbf{x}=\begin{bmatrix} x_0 \\ x_1 \\ x_2 \end{bmatrix}
\qquad\qquad
\mathbf{x}^\top = \begin{bmatrix} x_0 & x_1 & x_2 \end{bmatrix}
$$

- 각 행과 열을 바꾸는 연산($\top$)을 [전치(transpose)]{.hl}라고 한다.

---
layout: prism
heading: "DIY: 벡터와 전치"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np

x = np.array([1.0, 2.0, 3.0])                # column vector by convention
print("vector x        :", x)
print("components      : x0=%.0f, x1=%.0f, x2=%.0f" % (x[0], x[1], x[2]))
print("transpose x^T   :", x.reshape(1, -1))
print("shape x, x^T    :", x.reshape(-1, 1).shape, x.reshape(1, -1).shape)
```

</PyRunner>

---
layout: prism
heading: 스칼라, 벡터 (2/2)
---

- 기하적인 관점에서는 벡터의 각 성분을 좌표공간의 좌표성분, 즉 각 좌표축을 따라 나아간 거리로 해석할 수 있다.

- 기계학습에서는 벡터의 성분들이 각 [특징(feature)]{.hl}을 나타내는 데 사용된다.
  - 기계학습의 특징은 모델이 어떤 의사결정(예: 강아지/고양이 판단)을 내리는 과정에서 사용되는, 데이터가 가진 성질(예: 귀 모양, 얼굴 모양 등)을 의미한다.
  - 이러한 벡터를 [특징 벡터(feature vector)]{.hl}라고도 한다.
  - 보통 기계학습의 특징 벡터에서 기하와 관련된 성질을 무시하는 경향이 있지만, 이러한 기하적 성질을 함께 사용하여 좋은 결과를 도출하는 알고리즘도 존재한다.
    - 예: 기하적 딥러닝(geometric deep learning), 위상적 딥러닝(topological deep learning)

- 가능한 특징들이 모여 있는 집합을 [특징 공간(feature space)]{.hl}이라고 정의하며, 우리가 사용하는 데이터셋은 특징 공간을 잘 반영해야만 한다.

---
layout: prism
heading: 행렬, 텐서
---

- [행렬(matrix)]{.hl}은 수치들의 2차원 배열이다.
  - 열벡터는 열이 하나인 행렬로, 행벡터는 행이 하나인 행렬로 해석할 수 있다.
  - 관습적으로 $\mathbf{X}$와 같은 형태로 표현한다.
  - 행렬 $\mathbf{X}$의 $i$번째 행, $j$번째 열의 원소는 관습적으로 $x_{i,j}$와 같이 표현한다.
    - 본 수업에서는 각 첨자가 $0$부터 시작한다고 가정한다.

$$
\mathbf{X}=\begin{bmatrix}
x_{0,0} & x_{0,1} & x_{0,2} & x_{0,3} \\
x_{1,0} & x_{1,1} & x_{1,2} & x_{1,3} \\
x_{2,0} & x_{2,1} & x_{2,2} & x_{2,3} \\
x_{3,0} & x_{3,1} & x_{3,2} & x_{3,3}
\end{bmatrix}
$$

- 스칼라에는 차원이 없고, 벡터에는 차원이 하나 있으며, 행렬에는 차원이 두 개 있다. 차원이 셋 이상인 수학적 객체를 [텐서(tensor)]{.hl}라고 한다.
  - 텐서의 차원을 표현하기 위해 [랭크(rank)]{.hl}를 사용한다: 스칼라는 랭크 0-텐서, 벡터는 랭크 1-텐서, 행렬은 랭크 2-텐서이다.

---
layout: prism
heading: "DIY: 텐서 랭크와 형태"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np

scalar = np.array(7.0)
vector = np.array([1.0, 2.0, 3.0])
matrix = np.arange(12).reshape(3, 4)
tensor = np.arange(24).reshape(2, 3, 4)

for name, t in [("scalar", scalar), ("vector", vector),
                ("matrix", matrix), ("tensor", tensor)]:
    print(f"{name:>7}: rank(ndim)={t.ndim}, shape={t.shape}")
print("x_{2,3} of matrix:", matrix[2, 3])
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">선형대수 객체</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">텐서 산술 연산</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">벡터 연산</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">행렬 연산</span></p>
  </div>

</div>

---
layout: prism
heading: 벡터의 크기
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 기하적인 관점에서 벡터는 방향과 길이를 가진다.

- 벡터의 길이를 [크기(magnitude)]{.hl}라고 한다. $n$개의 성분 $x_0, x_1, \ldots, x_{n-1}$를 가진 벡터의 크기는 다음과 같이 정의된다.
  - 기하적인 관점에서 피타고라스의 정리와 연관되어 있다.

$$
\|\mathbf{x}\| = \sqrt{x_0^2 + x_1^2 + \cdots + x_{n-1}^2}
$$

- 벡터의 성분들을 벡터의 크기로 나누면 원래 벡터와 방향은 같지만 크기가 $1$인 벡터가 나오며, 이를 [단위 벡터(unit vector)]{.hl}라 하고 다음과 같이 정의된다.

$$
\hat{\mathbf{x}} = \frac{\mathbf{x}}{\|\mathbf{x}\|}
$$

---
layout: prism
heading: "DIY: 크기와 단위 벡터"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np

x = np.array([3.0, 4.0, 12.0])
mag = np.sqrt(np.sum(x**2))
print("magnitude ||x|| :", mag)
print("numpy norm      :", np.linalg.norm(x))

xhat = x / mag
print("unit vector     :", xhat)
print("||unit vector|| :", np.linalg.norm(xhat))
```

</PyRunner>

---
layout: prism
heading: 내적
---

- $n$개의 성분을 가진 임의의 두 벡터 $\mathbf{x}$와 $\mathbf{y}$의 [내적(inner product, dot product)]{.hl}은 다음과 같이 정의되며, $\theta$는 두 벡터 사이의 각도를 의미한다.

$$
\begin{aligned}
\mathbf{x}\cdot\mathbf{y} = \langle \mathbf{x}, \mathbf{y}\rangle
&= \mathbf{x}^\top \mathbf{y} \\
&= \sum_{k=0}^{n-1} x_k y_k \\
&= \|\mathbf{x}\|\,\|\mathbf{y}\|\cos\theta
\end{aligned}
$$

- 내적은 교환법칙과 분배법칙이 성립하지만, 결합법칙은 성립하지 않는다.
  - $\mathbf{x}\cdot\mathbf{y} = \mathbf{y}\cdot\mathbf{x}$
  - $\mathbf{x}\cdot(\mathbf{y}+\mathbf{z}) = \mathbf{x}\cdot\mathbf{y} + \mathbf{x}\cdot\mathbf{z}$

- 각도가 $\pi/2$인 두 벡터의 내적은 $0$이며, 이 경우 두 벡터가 [직교(orthogonal)]{.hl}한다고 한다.

---
layout: prism
heading: "DIY: 내적과 직교"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([4.0, -5.0, 6.0])

dot = np.dot(x, y)
print("x . y           :", dot, "=", x @ y)
cos_t = dot / (np.linalg.norm(x) * np.linalg.norm(y))
print("cos(theta)      :", round(cos_t, 4))

u, v = np.array([1.0, 0.0]), np.array([0.0, 1.0])
print("u . v           :", np.dot(u, v))
print("orthogonal?     :", np.isclose(np.dot(u, v), 0.0))
```

</PyRunner>

---
layout: prism
heading: 사영
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem; grid-template-columns: 1.5fr 1fr;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 벡터의 [사영(projection)]{.hl}은 한 벡터가 다른 벡터의 방향으로 얼마나 나아가는지를 계산하는 연산이다.

- $\mathbf{y}$에 대한 $\mathbf{x}$의 사영은 다음과 같이 정의된다.

$$
\operatorname{proj}_{\mathbf{y}} \mathbf{x} = \frac{\mathbf{x}\cdot\mathbf{y}}{\|\mathbf{y}\|^2}\,\mathbf{y}
$$

- 서로 직교인 벡터들의 사영은 항상 $0$이다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W09_proj.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 벡터 사영"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np

x = np.array([4.0, 1.0])
y = np.array([3.0, 4.0])
proj = (np.dot(x, y) / np.dot(y, y)) * y
print("proj_y x        :", proj)

z = np.array([-4.0, 3.0])          # z is orthogonal to y
print("x.y , z.y       :", np.dot(x, y), np.dot(z, y))
print("proj_y z        :", (np.dot(z, y) / np.dot(y, y)) * y)
```

</PyRunner>

---
layout: prism
heading: 외적
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 두 벡터의 내적은 스칼라 값이지만, 두 벡터의 [외적(outer product)]{.hl}은 행렬이 된다.

- 내적과는 달리 외적은 두 벡터의 길이가 달라도 정의된다. 성분이 $m$개인 벡터 $\mathbf{x}$와 $n$개인 벡터 $\mathbf{y}$의 외적은 다음과 같이 정의된다.

$$
\mathbf{x}\times\mathbf{y} = \begin{bmatrix}
x_0 y_0 & x_0 y_1 & x_0 y_2 & \cdots & x_0 y_{n-1} \\
x_1 y_0 & x_1 y_1 & x_1 y_2 & \cdots & x_1 y_{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
x_{m-1} y_0 & x_{m-1} y_1 & x_{m-1} y_2 & \cdots & x_{m-1} y_{n-1}
\end{bmatrix}
$$

- 비슷한 관점에서 두 집합의 [데카르트 곱(Cartesian product)]{.hl}을 정의할 수 있다: $A\times B = \{(a, b) \mid \forall a\in A,\ \forall b\in B\}$.

---
layout: prism
heading: "DIY: 외적과 데카르트 곱"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np
from itertools import product

x = np.array([1, 2, 3])            # length m = 3
y = np.array([4, 5])               # length n = 2
print("outer product (3x2):")
print(np.outer(x, y))

A, B = {1, 2}, {"a", "b"}
print("Cartesian A x B :", sorted(product(A, B)))
```

</PyRunner>

---
layout: prism
heading: 아다마르 곱
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 서로 차원이 같은 두 행렬 $\mathbf{X}$, $\mathbf{Y}$에 대해 [아다마르 곱(Hadamard product)]{.hl}을 정의할 수 있다.

$$
\begin{aligned}
\mathbf{X}\odot\mathbf{Y} &= \begin{bmatrix}
x_{0,0} & x_{0,1} & x_{0,2} \\
x_{1,0} & x_{1,1} & x_{1,2} \\
x_{2,0} & x_{2,1} & x_{2,2}
\end{bmatrix}
\odot
\begin{bmatrix}
y_{0,0} & y_{0,1} & y_{0,2} \\
y_{1,0} & y_{1,1} & y_{1,2} \\
y_{2,0} & y_{2,1} & y_{2,2}
\end{bmatrix} \\[4pt]
&= \begin{bmatrix}
x_{0,0}y_{0,0} & x_{0,1}y_{0,1} & x_{0,2}y_{0,2} \\
x_{1,0}y_{1,0} & x_{1,1}y_{1,1} & x_{1,2}y_{1,2} \\
x_{2,0}y_{2,0} & x_{2,1}y_{2,1} & x_{2,2}y_{2,2}
\end{bmatrix}
\end{aligned}
$$

- 좀 더 엄밀하게, 아다마르 곱의 결과 행렬을 $\mathbf{Z}$라고 하면 $z_{ij} = x_{ij}\,y_{ij}$와 같이 정의할 수 있다.

---
layout: prism
heading: "DIY: 아다마르 곱"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np

X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

print("Hadamard X (.) Y (elementwise):")
print(X * Y)
print("matrix product X Y (for contrast):")
print(X @ Y)
```

</PyRunner>

---
layout: prism
heading: 행렬곱
---

- 행렬 $\mathbf{X}$와 $\mathbf{Y}$의 행렬곱 $\mathbf{XY}$를 계산하기 위해서는 왼쪽 행렬의 열 수가 오른쪽 행렬의 행 수와 일치해야 한다.

- 행렬곱은 $\mathbf{X}$의 행벡터들을 순서대로 $\mathbf{Y}$의 열벡터들과 내적한 것이다. 행렬곱 $\mathbf{XY}$의 결과를 $\mathbf{Z}$라고 할 때, 다음과 같이 정의된다.

$$
z_{i,j} = \sum_{k=0}^{m-1} x_{i,k}\, y_{k,j}
$$

- 행렬곱은 결합법칙과 분배법칙은 만족하지만, 교환법칙은 성립하지 않는다.
  - $(\mathbf{XY})\mathbf{Z} = \mathbf{X}(\mathbf{YZ})$
  - $\mathbf{X}(\mathbf{Y}+\mathbf{Z}) = \mathbf{XY} + \mathbf{XZ}$
  - $\mathbf{XY} \neq \mathbf{YX}$

---
layout: prism
heading: "DIY: 선형 사상으로서의 행렬"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np

X = np.array([[1, 2, 3], [4, 5, 6]])       # 2x3
Y = np.array([[1, 0], [0, 1], [1, 1]])     # 3x2
print("X Y (2x2):")
print(X @ Y)

A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [1, 0]])
print("AB == BA ?      :", np.array_equal(A @ B, B @ A))
print("A applied to v  :", A @ np.array([1, 1]))   # matrix as a mapping
```

</PyRunner>

---
layout: prism
heading: 크로네커 곱
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 행렬곱에서는 두 행렬의 성분들이 섞여서 곱해지는 반면, [크로네커 곱(Kronecker product)]{.hl}은 한 행렬의 각 성분에 다른 행렬 전체를 곱하여 얻어진다.

- 임의의 $m\times n$ 행렬 $\mathbf{X}$에 대해 크로네커 곱은 다음과 같이 정의된다.

$$
\mathbf{X}\otimes\mathbf{Y} = \begin{bmatrix}
x_{0,0}\mathbf{Y} & x_{0,1}\mathbf{Y} & \cdots & x_{0,n-1}\mathbf{Y} \\
x_{1,0}\mathbf{Y} & x_{1,1}\mathbf{Y} & \cdots & x_{1,n-1}\mathbf{Y} \\
\vdots & \vdots & \ddots & \vdots \\
x_{m-1,0}\mathbf{Y} & x_{m-1,1}\mathbf{Y} & \cdots & x_{m-1,n-1}\mathbf{Y}
\end{bmatrix}
$$

---
layout: prism
heading: "DIY: 크로네커 곱"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np

X = np.array([[1, 2], [3, 4]])
Y = np.array([[0, 1], [1, 0]])
K = np.kron(X, Y)
print("Kronecker X (x) Y  ->  shape", K.shape)
print(K)
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
