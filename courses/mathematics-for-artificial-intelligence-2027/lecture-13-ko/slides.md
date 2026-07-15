---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 13 (KO)
download: true
info: |
  ## 인공지능수학 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-13/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">13주차: 신경망의 데이터 흐름</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">행렬 미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span class="text-gray-900 dark:text-gray-100">신경망의 데이터 흐름</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 신경망의 데이터 흐름
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 신경망에 입력된 벡터 또는 텐서가 신경망을 통과하며 최종 출력으로 변환되는 과정을 추적한다.
  - 신경망은 하나의 함수이며, 입력으로 받은 데이터를 최종 출력으로 사상시키는 도구이다.

- 신경망을 학습시키는 과정은 결국 입력 데이터에 대해 알맞은 출력을 내도록 함숫값을 변형시켜주는 과정이다.

- 최적의 함수를 찾기 위해서는 함수의 순전파 과정을 반대로 거슬러 올라가는 역전파 과정이 필요하며, 좋은 해를 찾기 위해 미분값에 기반한 경사하강법을 사용한다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">신경망의 데이터 흐름</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">퍼셉트론의 데이터 흐름</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">합성곱 신경망의 데이터 흐름</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">역전파와 경사하강법</span></p>
  </div>

</div>

---
layout: prism
heading: 퍼셉트론의 데이터 흐름 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 전통적인 신경망이나 기타 고전적인 선형 기계학습 모형에서 입력값은 수치들의 벡터로 다룬다.

- 이러한 입력 벡터를 [특징 벡터(feature vector)]{.hl}라고 부르며, 기계학습 모델을 학습할 때는 다수의 특징 벡터 각각에 레이블을 부여한 데이터셋을 사용한다.
  - 입력 데이터 하나가 벡터 하나라고 본다면, 입력 데이터가 여러 개 있는 경우는 행렬로 표현하는 것이 자연스럽다.

- 퍼셉트론이나 순방향 신경망과 같은 모델들은 층과 층 사이의 가중치들을 행렬로 저장한다.
  - 층 $i$의 입력 노드가 $n$개이고 층 $i-1$의 출력 노드가 $m$개라고 하면, 두 층 사이의 가중치 행렬 $\mathbf{W}_i$는 $n \times m$ 행렬로 표현한다.

---
layout: prism
heading: "DIY: 가중치 행렬과 층 출력"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)

# Layer i has n = 3 nodes; layer i-1 produces m = 4 outputs.
n, m = 3, 4
W = rng.standard_normal((n, m))       # weight matrix W_i is n x m
a_prev = rng.standard_normal((m, 1))  # outputs of layer i-1 (m x 1)

z = W @ a_prev                        # -> n x 1, one value per node of layer i
print("W shape        :", W.shape)
print("a_prev shape   :", a_prev.shape)
print("W @ a_prev     :", z.shape, "-> feeds the", n, "nodes of layer i")
```

</PyRunner>

---
layout: prism
heading: 퍼셉트론의 데이터 흐름 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 행렬 $\mathbf{W}_i$에 층 $i-1$의 출력들로 이루어진 $m \times 1$ 열벡터를 곱하면 $n \times 1$ 행렬이 나오며, 이것이 층 $i$의 $n$개의 노드들로 입력된다.

- 각 노드의 출력은 아래와 같이 계산된다.
  - 한 노드의 출력(활성화 값)은 현재 가중치 행렬 $\mathbf{W}_i$에 층 $i-1$의 출력 벡터 $\mathbf{a}_{i-1}$을 곱하고 층 $i$의 바이어스 항을 더한 결과에 비선형 활성화 함수 $\sigma$를 적용한 결과이다.

$$
\mathbf{a}_i = \sigma(\mathbf{W}_i \mathbf{a}_{i-1} + \mathbf{b}_i)
$$

- 비선형 활성화 함수로는 층과 층 사이에는 일반적으로 ReLU 함수를, 최종 의사결정 층에서는 일반적으로 시그모이드 계열 함수를 사용하는 경향이 있다.
  - 시그모이드 계열 함수들은 최종 출력을 $0$에서 $1$ 사이의 값으로 사상시킨다.

---
layout: prism
heading: "DIY: 활성화 함수"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

def relu(x):    return np.maximum(0.0, x)
def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

W = np.array([[0.2, -0.5], [0.1, 0.4]])
b = np.array([[0.1], [-0.2]])
a_prev = np.array([[1.0], [2.0]])

z = W @ a_prev + b
print("pre-activation z :", z.ravel())
print("ReLU (hidden)    :", relu(z).ravel())
print("sigmoid (output) :", np.round(sigmoid(z).ravel(), 4))
print("output in (0, 1) :", bool(np.all((sigmoid(z) > 0) & (sigmoid(z) < 1))))
```

</PyRunner>

---
layout: prism
heading: 합성곱 신경망의 데이터 흐름 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 합성곱 신경망(CNN)은 합성곱 층을 사용하여 데이터에 존재하는 공간적 관계들을 포착하고 활용한다.

- 일반적으로 합성곱 신경망은 2차원 배열로 표현된 이미지 데이터를 분석하기 위해 사용된다.
  - 회색조 이미지는 하나의 행렬로 표현되며, 원색(컬러) 이미지는 행렬 3개(빛의 3원색)가 쌓인 텐서의 형태로 표현된다.

- 일반적으로 이미지 텐서는 $\mathbb{R}^{H \times W \times C}$ 형태로 표현되며, $H$, $W$, $C$는 각각 이미지의 높이, 너비, 채널 갯수를 의미한다.
  - 즉, 일반적인 회색조 이미지는 $C = 1$, 원색 이미지는 $C = 3$이다.

---
layout: prism
heading: "DIY: 이미지 텐서의 형태"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# grayscale image: C = 1 ; color image: C = 3
H, W = 4, 5
gray = np.zeros((H, W, 1))
color = np.zeros((H, W, 3))

print("grayscale H x W x C :", gray.shape, "-> C =", gray.shape[2])
print("color     H x W x C :", color.shape, "-> C =", color.shape[2])
print("stored values (gray):", gray.size)
print("stored values (color):", color.size)
```

</PyRunner>

---
layout: prism
heading: 합성곱 신경망의 데이터 흐름 (2/3)
---

- 합성곱 연산은 한 함수를 다른 함수 위에서 밀어 이동시키는 방식으로 진행되며, 함수 $f$와 $g$의 합성곱 $\star$은 다음과 같이 정의된다.

$$
(f \star g)(t) \equiv \int_{-\infty}^{\infty} f(\tau)\, g(t - \tau)\, \mathrm{d}\tau
$$

- 기계학습에서 다루는 합성곱 연산은 이산 정의역에서 이루어지며, 실제로 적분을 수행하는 경우는 드물다.

- 입력 $f$ 위를 미끄러지며 이동하는 값들의 집합인 $g$를 [커널(kernel)]{.hl}이라고 부른다.

- 합성곱 연산을 수행하면 출력 크기가 줄어들게 된다.
  - 합성곱 연산 이후 출력의 크기를 입력과 동일하게 유지하고자 할 때 흔히 [영 패딩(zero padding)]{.hl} 방식을 사용한다.
  - [DIY]{.hl} 입력 $[2, 6, 15, 31, 56, 27, 15, 0, -11]$에 대해 커널 $[-1, 0, 1]$과의 합성곱을 영 패딩을 사용한 경우와 사용하지 않은 경우 각각 계산하라.

---
layout: prism
heading: "DIY: 1차원 합성곱과 영 패딩"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

x = np.array([2, 6, 15, 31, 56, 27, 15, 0, -11])
k = np.array([-1, 0, 1])

# 'valid': no padding -> length len(x) - len(k) + 1
valid = np.array([x[i:i+3] @ k for i in range(len(x) - 2)])

# 'same': zero-pad one element on each side -> same length as the input
xp = np.concatenate(([0], x, [0]))
same = np.array([xp[i:i+3] @ k for i in range(len(xp) - 2)])

print("input          :", x)
print("valid (no pad) :", valid)
print("same  (0-pad)  :", same)
print("lengths        :", len(valid), "vs", len(same), "(input length", len(x), ")")
```

</PyRunner>

---
layout: prism
heading: 합성곱 신경망의 데이터 흐름 (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 합성곱 커널이 움직이는 크기를 [보폭(stride)]{.hl}이라 하며, 2차원 합성곱 연산도 1차원과 비슷한 방식으로 이루어진다.

- 합성곱 연산 뒤에는, 텐서의 채널 차원은 유지하면서 높이와 너비 차원을 줄이기 위해 [풀링(pooling)]{.hl} 연산이 사용된다.
  - 풀링은 필연적으로 정보 손실을 일으키므로, 적절하게 알맞은 상황에 사용해야 한다.

- 최대 풀링과 평균 풀링이 가장 흔히 사용되며, 미리 정의된 구간(윈도우) 안에서 각각 최댓값 또는 평균값을 취하여 출력을 결정한다.
  - 풀링 연산에서도 보폭을 정의할 수 있다.

- 합성곱 신경망의 마지막 부분에서는, 텐서를 [평탄화(flattening)]{.hl}하여 벡터로 만든 후, 최종적으로 퍼셉트론에 입력하여 의사결정을 내린다.

---
layout: prism
heading: "DIY: 최대 풀링과 평균 풀링"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

img = np.array([[1, 3, 2, 4],
                [5, 6, 1, 2],
                [7, 8, 3, 0],
                [1, 2, 4, 9]], float)

# 2 x 2 pooling with stride 2
def pool(a, op):
    out = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            out[i, j] = op(a[2*i:2*i+2, 2*j:2*j+2])
    return out

print("max pooling:\n", pool(img, np.max))
print("avg pooling:\n", pool(img, np.mean))
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">신경망의 데이터 흐름</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">역전파와 경사하강법</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">역전파 계산</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">기본 경사하강법</span></p>
  </div>

</div>

---
layout: prism
heading: 역전파
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [역전파(backpropagation)]{.hl} 알고리즘은 딥러닝 모델 학습을 위한 사실상 표준(de facto standard)이다.
  - 역전파가 없으면 신경망 훈련이 매우 느려지거나, 최악의 경우 불가능해진다.

- 신경망 학습은 본질적으로 손실 함수에 의존하는 하나의 최적화 문제이다.
  - 손실 함수는 주어진 입력(학습 데이터)에 대해 신경망이 얼마나 잘 동작하는지를 나타낸다.
  - 손실 함수는 신경망의 가중치 및 바이어스 값들을 입력으로 받아 성능과 관련한 값을 출력한다.

- 역전파로 신경망을 학습할 때는 그래디언트 값을 토대로 손실 함수가 나타내는 성능의 최댓값, 즉 손실 함수의 최솟값을 찾는다.

---
layout: prism
heading: 역전파 계산 (1/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- 값 두 개를 받아 하나의 값을 출력하는 간단한 신경망을 생각해보자.
  - 노드 두 개짜리 은닉층과 노드 하나짜리 출력층으로 이루어져 있다.

- 가중치와 바이어스 값은 모두 스칼라이며, 은닉층은 아래와 같은 시그모이드 함수를 사용한다.

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

- 출력 노드에는 활성화 함수를 적용하지 않으며, 손실 함수로는 아래와 같은 제곱오차 함수를 사용한다.

$$
L = \frac{1}{2}(y - a_2)^2
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W13_nn.svg" class="tikz-fig" style="width: 95%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 시그모이드와 그 도함수"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

def sigmoid(x):  return 1.0 / (1.0 + np.exp(-x))
def dsigmoid(x): return sigmoid(x) * (1.0 - sigmoid(x))

xs = np.array([-2.0, -0.5, 0.0, 0.5, 2.0])
h = 1e-6                                   # verify sigma'(x) = sigma(x)(1 - sigma(x))
fd = (sigmoid(xs + h) - sigmoid(xs - h)) / (2 * h)
print("sigmoid   :", np.round(sigmoid(xs), 4))
print("analytic' :", np.round(dsigmoid(xs), 6))
print("finite  ' :", np.round(fd, 6))
print("match     :", bool(np.allclose(dsigmoid(xs), fd)))
```

</PyRunner>

---
layout: prism
heading: 역전파 계산 (2/3)
---

- 이 신경망의 순전파는 아래와 같이 서술된다.

$$
\begin{aligned}
z_0 &= w_0 x_0 + w_2 x_1 + b_0\\
a_0 &= \sigma(z_0)\\
z_1 &= w_1 x_0 + w_3 x_1 + b_1\\
a_1 &= \sigma(z_1)\\
a_2 &= w_4 a_0 + w_5 a_1 + b_2
\end{aligned}
$$

- 손실은 가중치들과 바이어스 값들을 이용하여 다음과 같이 표기할 수 있다.
  - 가중치들과 바이어스 값을 합친 매개변수를 벡터로 묶어 $\boldsymbol{\theta}$로 표기한다.

$$
\begin{aligned}
L &= L(w_0, w_1, w_2, w_3, w_4, w_5, b_0, b_1, b_2; x_0, x_1, y)\\
  &= L(\boldsymbol{\theta}; \mathbf{x}, y)
\end{aligned}
$$

- 역전파를 수행하려면 이 손실 함수의 그래디언트 $\nabla L(\boldsymbol{\theta}; \mathbf{x}, y)$를 구해야 한다.

---
layout: prism
heading: "DIY: 순전파"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

w = np.array([0.10, 0.20, 0.30, 0.40, 0.50, 0.60])   # w0..w5
b = np.array([0.10, -0.20, 0.05])                    # b0, b1, b2
x0, x1, y = 1.0, 2.0, 1.0

z0 = w[0]*x0 + w[2]*x1 + b[0]; a0 = sigmoid(z0)
z1 = w[1]*x0 + w[3]*x1 + b[1]; a1 = sigmoid(z1)
a2 = w[4]*a0 + w[5]*a1 + b[2]          # no activation at the output
L = 0.5 * (y - a2)**2                  # squared-error loss

print(f"a0 = {a0:.4f}, a1 = {a1:.4f}")
print(f"prediction a2 = {a2:.4f}, target y = {y}")
print(f"loss L = {L:.6f}")
```

</PyRunner>

---
layout: prism
heading: 역전파 계산 (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 그래디언트를 구하기 위해 먼저 시그모이드 함수의 도함수를 구한다.
  - [DIY]{.hl} 미분을 직접 수행하자.

$$
\frac{\mathrm{d}}{\mathrm{d}x}\sigma(x) = \sigma(x)\bigl(1 - \sigma(x)\bigr)
$$

- 이를 토대로 $\dfrac{\partial L}{\partial w_i},\ i = 0, 1, \ldots, 5$와 $\dfrac{\partial L}{\partial b_j},\ j = 0, 1, 2$를 구할 수 있다.
  - [DIY]{.hl} 편미분을 직접 수행하자.

---
layout: prism
heading: "DIY: 역전파"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

def loss(p, x0=1.0, x1=2.0, y=1.0):
    w, b = p[:6], p[6:]
    a0 = sigmoid(w[0]*x0 + w[2]*x1 + b[0])
    a1 = sigmoid(w[1]*x0 + w[3]*x1 + b[1])
    a2 = w[4]*a0 + w[5]*a1 + b[2]
    return 0.5 * (y - a2)**2

p = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.1, -0.2, 0.05])
x0, x1, y = 1.0, 2.0, 1.0
w, b = p[:6], p[6:]
a0 = sigmoid(w[0]*x0 + w[2]*x1 + b[0]); a1 = sigmoid(w[1]*x0 + w[3]*x1 + b[1])
a2 = w[4]*a0 + w[5]*a1 + b[2]; d = -(y - a2)          # dL/da2 via the chain rule
g = np.array([d*w[4]*a0*(1-a0)*x0, d*w[5]*a1*(1-a1)*x0, d*w[4]*a0*(1-a0)*x1,
              d*w[5]*a1*(1-a1)*x1, d*a0, d*a1,
              d*w[4]*a0*(1-a0), d*w[5]*a1*(1-a1), d])
fd = np.array([(loss(p + e) - loss(p - e)) / 2e-6 for e in np.eye(9) * 1e-6])
print("max |analytic - finite diff| :", np.max(np.abs(g - fd)))
print("gradients match              :", bool(np.allclose(g, fd)))
```

</PyRunner>

---
layout: prism
heading: 기본 경사하강법
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 미니배치를 고려하지 않은 기본적인 경사하강법 갱신 규칙은 다음과 같다.

$$
\begin{gather*}
\mathbf{W} \leftarrow \mathbf{W} - \eta\, \Delta \mathbf{W}\\
\mathbf{b} \leftarrow \mathbf{b} - \eta\, \Delta \mathbf{b}
\end{gather*}
$$

- 여기서 $\Delta \mathbf{W}$와 $\Delta \mathbf{b}$는 각각 가중치와 바이어스 값들의 편미분에 기초한 오차이며, $\eta$는 학습률(learning rate)로 한 번의 갱신에서 극소점 쪽으로 얼마나 이동할지를 결정한다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W13_00.png" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 경사하강 단계"
---

<PyRunner>

```python
import numpy as np

def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

def loss_and_grad(p, x0=1.0, x1=2.0, y=1.0):
    w, b = p[:6], p[6:]
    a0 = sigmoid(w[0]*x0 + w[2]*x1 + b[0]); a1 = sigmoid(w[1]*x0 + w[3]*x1 + b[1])
    a2 = w[4]*a0 + w[5]*a1 + b[2]; d = -(y - a2)
    g = np.array([d*w[4]*a0*(1-a0)*x0, d*w[5]*a1*(1-a1)*x0, d*w[4]*a0*(1-a0)*x1,
                  d*w[5]*a1*(1-a1)*x1, d*a0, d*a1,
                  d*w[4]*a0*(1-a0), d*w[5]*a1*(1-a1), d])
    return 0.5 * (y - a2)**2, g

p = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.1, -0.2, 0.05])
eta = 0.5
for step in range(6):
    L, g = loss_and_grad(p)
    print(f"step {step}: loss = {L:.6f}")
    p = p - eta * g          # descend along the negative gradient
```

</PyRunner>

---
layout: prism
heading: "DIY: 학습률의 효과"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

def run(eta, steps=20):
    p = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.1, -0.2, 0.05])
    x0, x1, y = 1.0, 2.0, 1.0
    for _ in range(steps):
        w, b = p[:6], p[6:]
        a0 = sigmoid(w[0]*x0 + w[2]*x1 + b[0]); a1 = sigmoid(w[1]*x0 + w[3]*x1 + b[1])
        a2 = w[4]*a0 + w[5]*a1 + b[2]; d = -(y - a2)
        g = np.array([d*w[4]*a0*(1-a0)*x0, d*w[5]*a1*(1-a1)*x0, d*w[4]*a0*(1-a0)*x1,
                      d*w[5]*a1*(1-a1)*x1, d*a0, d*a1,
                      d*w[4]*a0*(1-a0), d*w[5]*a1*(1-a1), d])
        p = p - eta * g
    return 0.5 * (y - a2)**2

for eta in [0.01, 0.5, 3.0]:
    print(f"eta = {eta:>4}: final loss after 20 steps = {run(eta):.6f}")
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
