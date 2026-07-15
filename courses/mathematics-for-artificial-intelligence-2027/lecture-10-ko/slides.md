---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 10 (KO)
download: true
info: |
  ## 인공지능수학 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-10/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">10주차: 선형대수 2부</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span class="text-gray-900 dark:text-gray-100">선형대수 2부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">행렬 미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">신경망의 데이터 흐름</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 9주차 요약
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 스칼라, 벡터, 행렬 모두 텐서로 일반화할 수 있으며, 각각 랭크-0, 랭크-1, 랭크-2 텐서에 해당한다.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0em;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W10_tensor.svg" class="tikz-fig" style="width: 100%;" />

</div>
<div>

- 스칼라는 하나의 성분만을 가진 수치이고, 벡터는 여러 개의 성분이 랭크 1만큼 있는 배열이며, 행렬은 벡터가 추가적인 랭크만큼 있는 배열이다.

- 각각의 텐서들에 대해, 크기, 내적, 사영 등 다양한 연산이 존재한다.

</div>
</div>

---
layout: prism
heading: 선형대수
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 선형대수는 단순히 텐서들의 연산 이외에도, 그들이 가진 성질을 토대로 공간을 표현하고, 동시에 그 공간의 특성을 분석하기 위해 사용된다.

- 또한, 각각의 텐서 공간이 가지는 고유한 수치를 계산하고, 다양한 공간 내의 거리를 측정하기 위해서도 사용된다.
  - 기계학습에서는 각 데이터 분포 사이의 거리를 줄이기 위한 방향으로 학습되는 알고리즘들이 많이 존재한다.

- 각 공간의 차원을 축소하여 그를 대표하는 수치들을 계산하는 알고리즘 또한 선형대수를 이용하여 계산된다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">정방행렬</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">정방행렬</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">정방행렬의 연산</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">특별한 정방행렬</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">행렬식과 연산</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">고윳값, 고유벡터</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">벡터 노름, 공간의 거리, 주성분 분석</span></p>
  </div>

</div>

---
layout: prism
heading: 행렬의 기하적 의미
---

<style>
.slidev-layout ul > li {
  margin-top: 0em;
}
</style>

- 행렬에 열벡터를 곱하면 또 다른 열벡터가 나온다.

$$
\begin{bmatrix} 1 & 2 & 3 & 4 \\ 5 & 6 & 7 & 8 \end{bmatrix}
\begin{bmatrix} 11 \\ 12 \\ 13 \\ 14 \end{bmatrix}
= \begin{bmatrix} 130 \\ 330 \end{bmatrix}
$$

- 기하적으로, $\mathbb{R}^{2\times 4}$ 행렬은 $\mathbb{R}^4$ 공간의 한 점에 해당하는 열벡터를 $\mathbb{R}^2$ 공간의 한 점으로 [사상(mapping)]{.hl}한 것에 해당한다.
  - 이 사상은 선형으로 이루어졌다(거듭제곱 등 비선형 연산은 사용되지 않았다).
  - 즉, 행렬은 한 공간의 점을 다른 공간으로 변환하는 수단이다.

- 행과 열의 크기가 모두 $n$으로 같은 [정방행렬(square matrix)]{.hl}의 경우는, $\mathbb{R}^n$에서 $\mathbb{R}^n$으로의 사상이 된다.

$$
\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}
\begin{bmatrix} 11 \\ 12 \\ 13 \end{bmatrix}
= \begin{bmatrix} 74 \\ 182 \\ 209 \end{bmatrix}
$$

---
layout: prism
heading: "DIY: 선형 사상으로서의 행렬"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]])
print("R^4 -> R^2 :", A @ np.array([11, 12, 13, 14]))   # matrix as a linear map

B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("R^3 -> R^3 :", B @ np.array([11, 12, 13]))

# scalar/vector/matrix are rank-0/1/2 tensors; reshape moves between ranks
t = np.arange(24)
print("rank-1 shape :", t.shape)
print("rank-3 shape :", t.reshape(2, 3, 4).shape)
```

</PyRunner>

---
layout: prism
heading: 회전행렬
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 비슷한 관점에서, [회전행렬(rotation matrix)]{.hl} 또한 한 공간의 점을 다른 공간의 점으로 사상시키는 것으로 생각할 수 있다.
  - 2차원 공간에서 $\theta$만큼의 회전은 다음과 같이 정의된다.

$$
\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
$$

  - 3차원 공간에서는 다음과 같이 정의된다.

$$
\begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{bmatrix}_x,\
\begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}_y,\
\begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}_z
$$

---
layout: prism
heading: 상관변환
---

- 행렬을 이용하여 [상관변환(affine transformation)]{.hl}을 정의할 수 있으며, 이는 어떤 공간의 한 직선이 사상된 공간에서도 여전히 직선이라는 조건을 만족하는 방식으로 사상하는 변환이다.

- 상관변환은 행렬 변환 $\mathbf{A}$와 이동 $\mathbf{b}$를 이용하여, 벡터 $\mathbf{x}$를 새로운 벡터 $\mathbf{y}$로 사상한다.

$$
\mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b}
$$

- 뉴럴 네트워크의 각 층은 단순히 상관변환에 지나지 않는다.
  - 그러나 일반적으로 뉴럴 네트워크의 각 층 사이에는 비선형 활성화 함수가 존재하므로, 뉴럴 네트워크는 입력을 적절한 관계가 반영된 출력으로 사상하는 방법을 배우게 된다.
  - 만약 비선형 활성화 함수가 없다면, 뉴럴 네트워크의 층이 아무리 많더라도 하나의 층을 가진 뉴럴 네트워크와 다른 점이 없다.

---
layout: prism
heading: "DIY: 행렬로서의 상관변환"
---

- [DIY]{.hl} $\mathbf{W} = \begin{bmatrix} w_{0,0} & w_{0,1} \\ w_{1,0} & w_{1,1} \end{bmatrix}$과 $\mathbf{b} = \begin{bmatrix} b_0 \\ b_1 \end{bmatrix}$에 대해, $\mathbf{x} = \begin{bmatrix} x_0 \\ x_1 \end{bmatrix}$이 $\mathbf{y} = \begin{bmatrix} y_0 \\ y_1 \end{bmatrix}$로 변환된다고 할 경우, 상관변환을 하나의 행렬로 표현하라.

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

W = np.array([[2.0, -1.0], [1.0, 3.0]])
b = np.array([5.0, -2.0])
x = np.array([4.0, 1.0])

# affine y = W x + b  ==  a single augmented matrix times [x; 1]
M = np.block([[W, b.reshape(2, 1)],
              [np.zeros((1, 2)), np.ones((1, 1))]])
xa = np.append(x, 1.0)

print("y = W x + b        :", W @ x + b)
print("y via aug. matrix  :", (M @ xa)[:2])
```

</PyRunner>

---
layout: prism
heading: 전치, 대각합, 거듭제곱
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 정방행렬은 전치 연산을 수행해도 계속해서 정방행렬이다.

- 정방행렬에서는 [대각합(trace)]{.hl} 연산이 정의되며, 임의의 정방행렬 $\mathbf{A}$에 대해 대각합 $\operatorname{tr}(\cdot)$은 다음과 같이 정의된다.

$$
\operatorname{tr}(\mathbf{A}) = \sum_i a_{i,i}
$$

- 또한, 정방행렬은 행과 열의 크기가 같으므로 거듭제곱을 정의할 수 있다.

$$
\mathbf{A}^n = \underbrace{\mathbf{A}\mathbf{A}\cdots\mathbf{A}}_{n}
$$

  - 정방행렬에 한해서 스칼라와 동일한 방식의 지수법칙을 정의할 수 있다.

---
layout: prism
heading: "DIY: 대각합과 행렬 거듭제곱"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
print("trace(A) :", np.trace(A))
print("A^3      :\n", np.linalg.matrix_power(A, 3))

# det(A^n) == det(A)^n
n = 3
print("det(A^3) :", round(np.linalg.det(np.linalg.matrix_power(A, n)), 4))
print("det(A)^3 :", round(np.linalg.det(A) ** n, 4))
```

</PyRunner>

---
layout: prism
heading: 특별한 정방행렬(1/2)
---

- 정방행렬 중 [영행렬(zero matrix)]{.hl}과 [일행렬(ones matrix)]{.hl}은 각각 모든 원소가 $0$, $1$인 정방행렬을 의미한다.
  - 크기가 $n$일 경우, 관습적으로 $\mathbf{0}_n$, $\mathbf{1}_n$으로 표기한다.

- [단위행렬(identity matrix)]{.hl}은 항등행렬(행렬 곱셈의 항등원이므로)이라고도 하며, 대각 성분들이 $1$이고 나머지는 모두 $0$인 정방행렬이다.
  - 크기가 $n$일 경우, 관습적으로 $\mathbf{I}_n$ 또는 $\mathbb{1}_n$으로 표기한다.

$$
\mathbf{I}_n = \begin{bmatrix}
1 & 0 & 0 & \cdots & 0 \\
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & 1
\end{bmatrix}
$$

- 주대각에만 $0$이 아닌 성분들이 있는 행렬을 [대각행렬(diagonal matrix)]{.hl}이라 한다.

---
layout: prism
heading: "DIY: 단위행렬과 대각행렬"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

print("identity I_3 :\n", np.eye(3, dtype=int))
print("zeros  0_2   :\n", np.zeros((2, 2), dtype=int))
print("ones   1_2   :\n", np.ones((2, 2), dtype=int))

D = np.diag([2, 5, 7])
print("diagonal     :\n", D)
print("I is identity of matmul :", np.array_equal(np.eye(3, dtype=int) @ D, D))
```

</PyRunner>

---
layout: prism
heading: 특별한 정방행렬(2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 정방행렬에서는 [삼각행렬(triangular matrix)]{.hl}을 정의할 수 있으며, 주대각 위쪽에만 $0$이 아닌 성분들이 있는 행렬을 상삼각행렬, 주대각 아래쪽에만 $0$이 아닌 성분들이 있는 행렬을 하삼각행렬이라 한다.
  - [DIY]{.hl} $\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$의 상삼각행렬과 하삼각행렬을 구하자.

- 삼각행렬은 선형대수의 다양한 연산에서 사용된다.

---
layout: prism
heading: "DIY: 삼각행렬"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("upper triangular :\n", np.triu(A))
print("lower triangular :\n", np.tril(A))

# the determinant of a triangular matrix is the product of its diagonal
U = np.triu(A)
print("det(U) :", round(np.linalg.det(U), 4), "= prod(diag) =", np.prod(np.diag(U)))
```

</PyRunner>

---
layout: prism
heading: 행렬식(1/2)
---

- 정방행렬의 [행렬식(determinant)]{.hl}은 정방행렬을 하나의 스칼라로 사상하는 함수이다.

- 임의의 정방행렬 $\mathbf{A}$에 대해, 행렬식 $\operatorname{det}(\mathbf{A}) \in \mathbb{R}$은 다음과 같은 성질을 가진다.
  - 원소가 하나인($1 \times 1$) 정방행렬의 행렬식은 자기 자신과 같다.
  - $\mathbf{A}$에 모든 성분이 $0$인 행이나 열이 존재하면 $\operatorname{det}(\mathbf{A}) = 0$이다.
  - $\mathbf{A}$에 동일한 두 행이 존재하면 $\operatorname{det}(\mathbf{A}) = 0$이다.
  - $\mathbf{A}$가 삼각행렬이면 $\operatorname{det}(\mathbf{A}) = \prod_{i=0}^{n-1} a_{i,i}$이다.
  - $\mathbf{A}$가 대각행렬이면 $\operatorname{det}(\mathbf{A}) = \prod_{i=0}^{n-1} a_{i,i}$이다.
  - 단위행렬의 행렬식은 항상 $1$이다.
  - $\operatorname{det}(\mathbf{A}\mathbf{B}) = \operatorname{det}(\mathbf{A})\operatorname{det}(\mathbf{B})$
  - $\operatorname{det}(\mathbf{A}) = \operatorname{det}(\mathbf{A}^\top)$
  - $\operatorname{det}(\mathbf{A}^n) = \operatorname{det}(\mathbf{A})^n$

- 정방행렬의 행렬식을 구하는 방법은 여러 가지가 있지만, 점화식을 이용한 방식이 주로 사용된다.

---
layout: prism
heading: 행렬식(2/2)
---

- 점화식을 정의하기 위해 아래 정의들을 사용한다.
  - 임의의 행렬 $\mathbf{A}$에 대해, 그 [소행렬(minor matrix)]{.hl} $\mathbf{A}_{ij}$를 $\mathbf{A}$에서 $i$번째 행과 $j$번째 열을 제거한 행렬로 정의한다.

$$
\mathbf{A} = \begin{bmatrix} 9 & 8 & 7 \\ 6 & 5 & 4 \\ 3 & 2 & 1 \end{bmatrix} \Rightarrow
\mathbf{A}_{11} = \begin{bmatrix} 9 & 7 \\ 3 & 1 \end{bmatrix}
$$

  - 임의의 소행렬 $\mathbf{A}_{ij}$의 [여인수(cofactor)]{.hl} $C_{ij}$는 다음과 같이 정의된다.

$$
C_{ij} = (-1)^{i+j+2}\operatorname{det}(\mathbf{A}_{ij})
$$

- 위 정의를 이용하여, 여인수 전개를 이용한 행렬식의 정의는 다음과 같다.

$$
\operatorname{det}(\mathbf{A}) = \sum_{j=0}^{n-1} a_{0,j} C_{0j}
$$

---
layout: prism
heading: "DIY: 여인수 전개에 의한 행렬식"
---

- [DIY]{.hl} $\mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$의 행렬식을 구하자.

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0], [3.0, 2.0, 1.0]])

def det(M):                       # cofactor expansion along the first row
    n = len(M)
    if n == 1:
        return M[0, 0]
    total = 0.0
    for j in range(n):
        minor = np.delete(np.delete(M, 0, axis=0), j, axis=1)
        total += (-1) ** j * M[0, j] * det(minor)
    return total

print("cofactor expansion :", det(A))
print("numpy det          :", round(np.linalg.det(A), 6))
print("det([[a,b],[c,d]]) = ad - bc :", det(np.array([[3.0, 1.0], [2.0, 4.0]])))
```

</PyRunner>

---
layout: prism
heading: 역행렬(1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 행렬식의 주요 용도 중 하나는 행렬의 [역행렬(inverse matrix)]{.hl}이 존재하는지 판정하는 것이다.

- 단위행렬이 스칼라 곱셈의 항등원과 비슷한 것처럼, 역행렬은 스칼라 곱셈의 역원처럼 행동한다.

- 역행렬이 존재하는 임의의 행렬 $\mathbf{A}$에 대해, 그 역행렬 $\mathbf{A}^{-1}$은 다음을 만족한다.

$$
\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}
$$

- $\mathbf{A}^{-1}$이 존재하면 다음이 성립한다.

$$
\operatorname{det}(\mathbf{A}^{-1}) = \frac{1}{\operatorname{det}(\mathbf{A})}
$$

---
layout: prism
heading: "DIY: 역행렬과 특이행렬"
---

- [DIY]{.hl} 역행렬이 존재하지 않는 임의의 행렬을 하나 만들어보라.

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[4.0, 7.0], [2.0, 6.0]])
Ainv = np.linalg.inv(A)
print("A^-1               :\n", Ainv)
print("A A^-1 = I         :", np.allclose(A @ Ainv, np.eye(2)))
print("det(A^-1)=1/det(A) :", np.isclose(np.linalg.det(Ainv), 1 / np.linalg.det(A)))

# solving A x = b relies on the inverse implicitly
print("solve A x = b      :", np.linalg.solve(A, np.array([1.0, 2.0])))

# a singular matrix has no inverse (det = 0, rank < n)
S = np.array([[1.0, 2.0], [2.0, 4.0]])
print("det(S), rank(S)    :", round(np.linalg.det(S), 4), np.linalg.matrix_rank(S))
```

</PyRunner>

---
layout: prism
heading: 역행렬(2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 역행렬이 존재할 경우 아래 성질도 성립한다.

$$
(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}
$$

- 대각행렬의 역행렬은 대각 성분들의 역수들로 이루어진 행렬이다.

$$
\mathbf{A} = \begin{bmatrix} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c \end{bmatrix}
\Leftrightarrow
\mathbf{A}^{-1} = \begin{bmatrix} a^{-1} & 0 & 0 \\ 0 & b^{-1} & 0 \\ 0 & 0 & c^{-1} \end{bmatrix},\ \forall a, b, c \neq 0
$$

- 역행렬이 없는 행렬을 [특이행렬(singular matrix)]{.hl} 또는 퇴화행렬이라 한다.
  - 즉, 특이행렬의 행렬식은 $0$이다.
  - 특이행렬이 아닌 행렬은 비특이 또는 비퇴화 행렬이라 한다.

---
layout: prism
heading: 대칭행렬과 직교행렬
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 다음 조건을 만족하는 정방행렬을 [대칭행렬(symmetric matrix)]{.hl}이라 한다.

$$
\mathbf{A}^\top = \mathbf{A}
$$

  - 대칭행렬들의 곱셈에는 교환법칙이 성립한다.

$$
\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A} \Leftrightarrow \mathbf{A} = \mathbf{A}^\top,\ \mathbf{B} = \mathbf{B}^\top
$$

- 다음 조건을 만족하는 정방행렬을 [직교행렬(orthogonal matrix)]{.hl}이라 한다.

$$
\mathbf{A}\mathbf{A}^\top = \mathbf{A}^\top\mathbf{A} = \mathbf{I}
$$

  - 직교행렬 $\mathbf{A}$에 대해 $\mathbf{A}^{-1} = \mathbf{A}^\top$이 성립하며, 따라서 $\operatorname{det}(\mathbf{A}) = \pm 1$이다.

---
layout: prism
heading: "DIY: 직교행렬"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

theta = np.pi / 4
Q = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])   # a rotation is orthogonal

print("Q Q^T = I   :", np.allclose(Q @ Q.T, np.eye(2)))
print("Q^-1 = Q^T  :", np.allclose(np.linalg.inv(Q), Q.T))
print("det(Q) = ±1 :", round(np.linalg.det(Q), 4))
```

</PyRunner>

---
layout: prism
heading: 정부호성
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 임의의 열벡터 $\mathbf{x}$에 대해, 아래 조건을 만족하는 대칭행렬 $\mathbf{A}$를 [양의 정부호(positive definite)]{.hl}라고 한다.

$$
\mathbf{x}^\top\mathbf{A}\mathbf{x} > 0,\ \forall \mathbf{x} \neq 0
$$

  - 이와 비슷하게, 아래 조건을 충족하면 양의 준정부호라고 한다.

$$
\mathbf{x}^\top\mathbf{A}\mathbf{x} \geq 0
$$

- 임의의 열벡터 $\mathbf{x}$에 대해, 아래 조건을 만족하는 대칭행렬 $\mathbf{A}$를 [음의 정부호(negative definite)]{.hl}라고 한다.

$$
\mathbf{x}^\top\mathbf{A}\mathbf{x} < 0,\ \forall \mathbf{x} \neq 0
$$

  - 이와 비슷하게, 아래 조건을 충족하면 음의 준정부호라고 한다.

$$
\mathbf{x}^\top\mathbf{A}\mathbf{x} \leq 0
$$

---
layout: prism
heading: 유니터리 행렬
---

<style>
.slidev-layout ul > li {
  margin-top: 3.6em;
}
</style>

- 복소수 성분을 가진 행렬도 정의할 수 있다. 복소수 행렬 $\mathbf{U}$가 아래의 조건을 만족할 경우, $\mathbf{U}$를 [유니터리 행렬(unitary matrix)]{.hl}이라 하고 $\mathbf{U}^*$를 $\mathbf{U}$의 [켤레전치(conjugate transpose)]{.hl} 또는 에르미트 수반행렬이라고 한다.

$$
\mathbf{U}^*\mathbf{U} = \mathbf{U}\mathbf{U}^* = \mathbf{I}
$$

  - 에르미트 수반행렬을 $\mathbf{U}^\dagger$로 표현하기도 하며, 어떤 유니터리 행렬이 자신의 에르미트 수반행렬과 동일할 경우 그런 행렬을 에르미트 행렬이라 한다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">정방행렬</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">고윳값, 고유벡터</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">고윳값과 고유벡터</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">벡터 노름, 공간의 거리, 주성분 분석</span></p>
  </div>

</div>

---
layout: prism
heading: 고윳값, 고유벡터(1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 정방행렬은 한 공간의 벡터를 그와 같은 공간에 있는 다른 벡터로 사상한다.
  - $\mathbf{v}'$과 $\mathbf{v}$가 $n$차원 공간의 벡터이고, $\mathbf{A}$가 $n \times n$ 행렬이며 $\mathbf{v}' = \mathbf{A}\mathbf{v}$인 경우를 생각하자.

- 영벡터가 아닌 $\mathbf{v}$와 임의의 스칼라 $\lambda$에 대해 다음과 같은 방정식을 생각해볼 수 있다.

$$
\mathbf{A}\mathbf{v} = \lambda\mathbf{v}
$$

  - 즉, $\mathbf{v}$를 $\mathbf{A}$로 사상했을 때 $\mathbf{v}$에 스칼라 값을 곱한 벡터가 나오는 상황이며, 이 때 $\mathbf{v}$를 $\mathbf{A}$의 [고유벡터(eigenvector)]{.hl}, $\lambda$를 그 [고윳값(eigenvalue)]{.hl}이라고 한다.
  - 기하학적인 관점에서 $\mathbf{A}$는 방향 변화 없이 확대나 축소만 고유벡터에 적용한다.
  - [DIY]{.hl} 임의의 행렬에 항상 고유벡터가 있는지 확인하라.

---
layout: prism
heading: 고윳값, 고유벡터(2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 고유벡터가 존재한다고 할 때, 행렬의 고윳값을 구하는 방정식은 다음과 같다.

$$
\mathbf{A}\mathbf{v} - \lambda\mathbf{v} = \mathbf{A}\mathbf{v} - \lambda\mathbf{I}\mathbf{v} = (\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}
$$

  - 즉, $\mathbf{v}$가 영벡터가 아니려면 $\mathbf{A} - \lambda\mathbf{I}$의 행렬식이 $0$이 되어야 한다.

- 이러한 방정식 $\operatorname{det}(\mathbf{A} - \lambda\mathbf{I}) = 0$을 [특성 방정식(characteristic equation)]{.hl}이라 한다.
  - $n \times n$ 행렬의 특성 다항식은 $n$차 다항식이다.

---
layout: prism
heading: "DIY: 고윳값"
---

- [DIY]{.hl} $\begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}$의 고윳값들을 계산하자.

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[0.0, 1.0], [-2.0, -3.0]])
vals, vecs = np.linalg.eig(A)
print("eigenvalues :", np.round(vals, 4))

for lam, v in zip(vals, vecs.T):
    print(f"lambda = {lam:.1f}:  A v = {np.round(A @ v, 4)},  lambda v = {np.round(lam * v, 4)}")
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">정방행렬</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">고윳값, 고유벡터</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">벡터 노름, 공간의 거리, 주성분 분석</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">노름</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">거리 함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">공분산 행렬</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">마할라노비스 거리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">쿨백-라이블러 발산</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">주성분 분석</span></p>
  </div>

</div>

---
layout: prism
heading: 노름과 거리 함수
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 수리적으로 [노름(norm)]{.hl}과 거리는 구별되는 개념이지만, 기계학습에서는 혼용되는 경향이 있다.

- [벡터 노름(vector norm)]{.hl}은 벡터를 $0$ 이상의 어떤 실수로 사상하는 함수이며, 대체로 벡터의 "거리"를 노름이라고 부를 때가 많다.
  - 두 벡터 사이의 거리를 따질 때에는 벡터의 입력 순서와 무관하게 항상 거리가 같아야 하지만, 이런 조건을 충족하지 않는 함수 중에서도 거리로 사용되는 것들이 있다.

- 벡터 노름은 벡터들의 거리를 측정하기 위한 간단한 방법으로 많이 사용되며, 다양한 종류의 거리 함수를 정의할 때에도 사용된다.

---
layout: prism
heading: "$L$-노름과 거리 함수(1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- $n$차원 벡터 $\mathbf{x}$의 $L_p$-노름은 다음과 같이 정의되며, 이 때 $p$는 실수이다.

$$
\|\mathbf{x}\|_p \equiv \left( \sum_i |x_i|^p \right)^{\frac{1}{p}}
$$

- 벡터의 크기는 $L_2$-노름이다.

$$
\|\mathbf{x}\|_2 = \sqrt{x_0^2 + x_1^2 + x_2^2 + \cdots + x_{n-1}^2} = \sqrt{\mathbf{x}^\top \mathbf{x}}
$$

- 이외에도, $L_1$-노름과 $L_\infty$-노름을 정의할 수 있다.

$$
\|\mathbf{x}\|_1 = \sum_i |x_i| \qquad\qquad \|\mathbf{x}\|_\infty = \max_i |x_i|
$$

---
layout: prism
heading: "$L$-노름과 거리 함수(2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- $\mathbf{x}$를 두 벡터의 차이 $\mathbf{x} - \mathbf{y}$로 대체하면, 노름을 두 벡터의 거리로 간주할 수 있다.

$$
L_p(\mathbf{x}, \mathbf{y}) = \left( \sum_i |x_i - y_i|^p \right)^{\frac{1}{p}}
$$

- $L_2$-거리를 유클리드 거리, $L_1$-거리를 맨해튼 거리, $L_\infty$-거리를 체비셰프 거리라고 한다.
  - $\mathbf{x} = (1, -2)$과 $\mathbf{y} = (3, 1)$의 유클리드, 맨해튼, 체비셰프 거리를 구하자.

- $L_1$-노름과 $L_2$-노름은 딥 뉴럴 네트워크의 정칙화로 많이 사용된다.

---
layout: prism
heading: 공분산 행렬
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 우리가 가지고 있는 데이터셋의 특징 벡터들의 특징 값들이 서로 어느 정도나 다른지 확인하고 싶은 경우에는 특징들의 [공분산(covariance)]{.hl}을 계산한다.
  - 특징 값들의 표준편차를 구할 수도 있겠으나, 표준편차는 개별 특징의 값들이 평균을 기준으로 어느 정도나 분산되어 있는지를 알려주는 값이며, 특징이 여러 개일 때는 공분산을 사용하여야 한다.

- 행렬 $\mathbf{X}$의 행은 각각의 데이터 샘플, 열은 서로 다른 특징을 나타낸다고 할 때, $\mathbf{X}$의 공분산 행렬 $\mathbf{\Sigma}$의 성분들은 다음과 같이 정의된다.

$$
\Sigma_{i,j} = \frac{1}{n-1} \sum_{k=0}^{n-1} (x_{k,i} - \bar{\mathbf{x}}_i)(x_{k,j} - \bar{\mathbf{x}}_j)
$$

- 공분산 행렬은 값들이 얼마나 퍼져 있는지를 반영한다.

---
layout: prism
heading: "DIY: 공분산 행렬"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

# rows = samples, columns = features
X = np.array([[2.0, 1.0], [4.0, 3.0], [6.0, 4.0], [8.0, 8.0]])
Xc = X - X.mean(axis=0)
n = len(X)
Sigma = (Xc.T @ Xc) / (n - 1)

print("covariance matrix :\n", Sigma)
print("matches np.cov    :", np.allclose(Sigma, np.cov(X, rowvar=False)))
```

</PyRunner>

---
layout: prism
heading: 마할라노비스 거리
---

- 공분산을 이용하여 [마할라노비스 거리(Mahalanobis distance)]{.hl} $D_M$을 정의할 수 있다.

$$
D_M = \sqrt{(\mathbf{x} - \mathbf{y})^\top \mathbf{\Sigma}^{-1} (\mathbf{x} - \mathbf{y})}
$$

- 계산 자체는 복잡하지만, 그 의미는 확률 분포상의 거리로서, 어떤 값이 평균으로부터 몇 분산만큼 떨어져 있는지를 나타낸다.
  - 수하루라는 카페에 수요일 오전에는 평균적으로 $300$명의 손님이 방문하고, 그 표준편차는 $30$명(분산은 $900$)이라고 하자.
    - 즉, 특별한 일이 없다면 수요일 오전 손님 수는 $270$명에서 $330$명 사이이다.
  - 그런데 오늘 $360$명의 손님이 방문했다면, 특히 손님이 많았던 날로 볼 수 있다.
  - 마할라노비스 거리는 이러한 일이 얼마나 일어나기 힘든 값인지를 수치화한 것이다.
    - 이 경우, 평균과의 차이를 표준편차로 나눠준 값($60/30 = 2$)이 마할라노비스 거리가 된다.

- 마할라노비스 거리는 다양한 기계학습 알고리즘에서 데이터의 특성을 분석하기 위해 사용되는 도구이다.

---
layout: prism
heading: 쿨백-라이블러 발산
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [쿨백-라이블러 발산(Kullback-Leibler divergence)]{.hl}(KL 발산)은 두 확률 분포 사이의 거리를 나타내는 측도로, 상대적 엔트로피로 나타내기도 한다.

- 두 이산 확률 분포 $P$와 $Q$의 KL 발산은 다음과 같이 정의된다.

$$
D_{\mathrm{KL}}(P \,\|\, Q) = \sum_x P(x) \log\left( \frac{P(x)}{Q(x)} \right)
$$

  - 이진(base-$2$) 로그를 사용하면 단위는 비트가 되고, 자연로그($\ln$)를 사용하면 단위는 내트가 된다.
  - KL 발산은 대칭적이지 않지만, 그렇다고 해서 거리 함수로 사용하지 못할 이유는 없다.

---
layout: prism
heading: "DIY: 쿨백-라이블러 발산"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

P = np.array([0.5, 0.3, 0.2])
Q = np.array([0.4, 0.4, 0.2])

kl_pq = np.sum(P * np.log2(P / Q))   # in bits
kl_qp = np.sum(Q * np.log2(Q / P))

print("D_KL(P||Q) :", round(kl_pq, 4), "bits")
print("D_KL(Q||P) :", round(kl_qp, 4), "bits")
print("asymmetric :", not np.isclose(kl_pq, kl_qp))
print("D_KL(P||P) :", round(np.sum(P * np.log2(P / P)), 4))
```

</PyRunner>

---
layout: prism
heading: 주성분 분석(1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 어떤 데이터셋을 나타내는 행렬 $\mathbf{X}$에 대해, 각 데이터 샘플이 $n$차원 공간의 한 점이라면(즉, 특징 벡터의 차원이 $n$이라면) 각 관측 데이터들은 $n$차원 공간에서 점들의 집합을 이루게 된다.

- [주성분 분석(principal component analysis; PCA)]{.hl}은 데이터가 주로 어느 방향으로 흩어져 있는지를 파악하기 위한 알고리즘이다.
  - 데이터들이 가장 길게 흩어진 방향, 즉 분산이 가장 큰 축을 가리켜 주성분이라 한다.

- 주성분 분석은 주성분을 먼저 구한 후, 나머지 성분들을 흩어진 정도가 감소하는 순으로 구하며, 각각 구해진 성분들은 다른 성분들과 직교한다.

- 주성분 분석은 주로 데이터의 차원 축소를 위해 사용된다.

---
layout: prism
heading: 주성분 분석(2/2)
---

<div style="height: 0.5rem;"></div>

- 주성분 분석 알고리즘은 다음과 같다.

<div class="sub-item-enum">

1. 데이터셋의 평균이 $0$이 되도록 중심화한다.
2. 데이터셋의 공분산 행렬을 구한다.
3. 공분산 행렬의 고윳값들과 고유벡터들을 구한다.
4. 고윳값들을 절댓값 내림차순으로 정렬한다.
5. 약한(작은) 고윳값 및 고유벡터를 폐기한다(이 단계는 선택 사항이다).
6. 나머지 고유벡터들로 변환 행렬을 만든다.
7. 변환 행렬을 기존 데이터셋에 적용하여 새로운 데이터셋을 구한다.

</div>

---
layout: prism
heading: "DIY: 주성분 분석"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

# small 2-D dataset (rows = samples)
X = np.array([[2.0, 0.0], [3.0, 1.0], [4.0, 3.0], [5.0, 4.0], [6.0, 6.0]])

Xc = X - X.mean(axis=0)                 # 1) center
Sigma = np.cov(Xc, rowvar=False)        # 2) covariance
vals, vecs = np.linalg.eig(Sigma)       # 3) eigen-decomposition
order = np.argsort(np.abs(vals))[::-1]  # 4) sort by |eigenvalue|
vals, vecs = vals[order], vecs[:, order]

print("eigenvalues (variance per axis):", np.round(vals, 4))
pc1 = vecs[:, 0]
print("principal component :", np.round(pc1, 4))
print("projection onto PC1 :", np.round(Xc @ pc1, 4))
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
