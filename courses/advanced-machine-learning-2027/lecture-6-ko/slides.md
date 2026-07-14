---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 6 (KO)
download: true
info: |
  ## 고급 기계학습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-6/
---

<style>
.dark .slidev-page,
.dark .slidev-layout,
.dark .slide-container,
.dark #slide-content,
.dark .slidev-nav-go-container {
  background: #000000 !important;
}
</style>

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.png" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">고급 기계학습</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">6주차: 커널 방법론</p>

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
heading: 강좌 일정
---

<div class="absolute left-10 right-10" style="top: 1rem; bottom: 5rem; display: grid; grid-template-columns: 1fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">강좌 소개</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">예비 지식</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">확률 분포</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">선형 회귀 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">선형 분류 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span class="text-gray-900 dark:text-gray-100">커널 방법론</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간고사 복습</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">그래프 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">혼합 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">근사 추론</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">샘플링 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">연속 잠재 변수</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말고사 복습</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 복습 (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 선형 판별 함수는 입력 벡터에 대해 선형이며 다음과 같이 주어집니다:

$$
y(\mathbf{x})=\mathbf{w}^\top\mathbf{x}+w_0
$$

<div class="sub-item">

$\mathbf{w}$는 [가중치 벡터(weight vector)]{.hl}이고 $w_0$는 [편향(bias)]{.hl}입니다. 이진 클래스 문제에서 일반성을 잃지 않고 $y(\mathbf{x})\geqslant0$이면 $\mathbf{x}$를 $\mathcal{C}_1$에, 그렇지 않으면 $\mathcal{C}_2$에 할당하므로, 결정 경계는 $y(\mathbf{x})=0$입니다.

</div>

<div class="sub-item">

정규방정식을 풀어 최소제곱 해를 얻을 수 있습니다.

</div>

- 피셔(Fisher)는 또 다른 형태의 선형 판별 함수를 위해 다음 기준을 정의했습니다:

$$
J(\mathbf{w})=\frac{\left(m_2-m_1\right)^2}{s_1^2+s_2^2}
$$

---
layout: prism
heading: 복습 (2/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 퍼셉트론 알고리즘은 선형 판별 모델의 또 다른 예입니다:

$$
y(\mathbf{x})=f(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}))
$$

<div class="sub-item">

$f(\cdot)$는 비선형 활성화 함수입니다.

</div>

- 퍼셉트론을 학습하기 위해 보통 확률적 경사하강법을 적용했습니다:

$$
\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}-\eta \nabla E_{P}(\mathbf{w})=\mathbf{w}^{(\tau)}+\eta \boldsymbol{\phi}_n t_n
$$

<div class="sub-item">

$E_P$는 퍼셉트론 기준(perceptron criterion)입니다.

</div>

---
layout: prism
heading: 복습 (3/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 확률적 생성 모델은 사후분포 $p(\mathcal{C}_k|\mathbf{x})$를 추정합니다.

- 관측값이 가우시안 분포로부터 i.i.d.로 샘플링되었다는 가정하에서, 사후분포는 다음과 같이 됩니다:

$$
\begin{gathered}
p(\mathcal{C}_1 | \mathbf{x})=\sigma(\mathbf{w}^{\top} \mathbf{x}+w_0)\\
\mathbf{w}=\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)\\
w_0=-\frac{1}{2} \boldsymbol{\mu}_1^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}_1+\frac{1}{2} \boldsymbol{\mu}_2^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}_2+\ln \frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}
\end{gathered}
$$

<div class="sub-item">

$\sigma(\cdot)$는 로지스틱 시그모이드 함수이며, 이 모델은 [선형 판별 분석(linear discriminant analysis)]{.hl}으로 알려져 있습니다.

</div>

---
layout: prism
heading: 복습 (4/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 확률적 판별 모델은 가능도를 직접 학습합니다. 로지스틱 회귀 방법은 다음과 같이 정의됩니다:

$$
p(\mathcal{C}_1|\boldsymbol{\phi})=y(\boldsymbol{\phi})=\sigma(\mathbf{w}^\top\boldsymbol{\phi})
$$

<div class="sub-item">

이 모델은 반복 재가중 최소제곱을 통해 학습할 수 있습니다.

</div>

- 복잡한 확률 분포를 그 최빈값에서 근사하기 위해 [라플라스 근사(Laplace approximation)]{.hl}를 수행할 수 있습니다.

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">쌍대 표현</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">커널 구성</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가우시안 과정</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">최대 마진 분류기</span></p>
  </div>

</div>

---
layout: prism
heading: 쌍대 표현 (1/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 많은 선형 매개변수 모델은 그 [쌍대 표현(dual representation)]{.hl}으로 재구성될 수 있습니다.

- 쌍대 표현에서 모델은 학습 데이터포인트로부터 추정한 [커널 함수(kernel functions)]{.hl}의 선형 결합을 이용해 목표값을 예측합니다.

- 고정된 비선형 특징 공간 사상 $\boldsymbol{\phi}(\mathbf{x})$를 기반으로, 커널 함수는 다음과 같이 주어집니다:

$$
k(\mathbf{x},\mathbf{x}')=\boldsymbol{\phi}(\mathbf{x})^\top\boldsymbol{\phi}(\mathbf{x}')
$$

<div class="sub-item">

커널 함수는 대칭임에 유의하세요. 즉, $k(\mathbf{x},\mathbf{x}')=k(\mathbf{x}',\mathbf{x})$입니다.

</div>

- [커널 치환(kernel substitution)]{.hl}, 즉 [커널 트릭(kernel trick)]{.hl}은 커널이 특징 공간 간의 내적으로 정의될 수 있다는 점을 활용하여, 잘 알려진 여러 알고리즘을 확장할 수 있게 해줍니다.

---
layout: prism
heading: 쌍대 표현 (2/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 선형 회귀 모델에 대한 정규화된 제곱합 오차 함수를 고려합니다:

$$
J(\mathbf{w})=\frac{1}{2} \sum_{n=1}^N\{\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)-t_n\}^2+\frac{\lambda}{2} \mathbf{w}^{\top} \mathbf{w}
$$

- $\mathbf{w}$에 대해 미분하고 그 결과를 $0$으로 두어 $\mathbf{w}$를 구합니다:

$$
\nabla_\mathbf{w} J(\mathbf{w})=\sum_{n=1}^N\{\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)-t_n\}\boldsymbol{\phi}(\mathbf{x}_n)+\lambda\mathbf{w}=0
$$

$$
\therefore \mathbf{w}=-\frac{1}{\lambda} \sum_{n=1}^N\{\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)-t_n\} \boldsymbol{\phi}(\mathbf{x}_n)=\sum_{n=1}^N a_n \boldsymbol{\phi}(\mathbf{x}_n)=\boldsymbol{\Phi}^{\top} \mathbf{a}
$$

<div class="sub-item">

$\boldsymbol{\Phi}$는 $n$번째 행이 $\boldsymbol{\phi}(\mathbf{x}_n)^\top$인 설계 행렬이며, $\mathbf{a}=(a_1,\ldots,a_N)^\top$이고 $a_n=-\frac{1}{\lambda}\{\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)-t_n\}$입니다.

</div>

---
layout: prism
heading: 쌍대 표현 (3/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- $\mathbf{w}$ 대신 $\mathbf{a}$에 대해 최소제곱 방법을 수행할 수 있음에 유의하세요.

- $\mathbf{w}=\boldsymbol{\Phi}^\top\mathbf{a}$를 대입하면 다음과 같습니다:

$$
J(\mathbf{a})=\frac{1}{2} \mathbf{a}^{\top} \boldsymbol{\Phi} \boldsymbol{\Phi}^{\top} \boldsymbol{\Phi} \boldsymbol{\Phi}^{\top} \mathbf{a}-\mathbf{a}^{\top} \boldsymbol{\Phi} \boldsymbol{\Phi}^{\top} \boldsymbol{\mathsf{t}}+\frac{1}{2} \boldsymbol{\mathsf{t}}^{\top} \boldsymbol{\mathsf{t}}+\frac{\lambda}{2} \mathbf{a}^{\top} \boldsymbol{\Phi} \boldsymbol{\Phi}^{\top} \mathbf{a}
$$

- $N\times N$ 크기의 [그람 행렬(Gram matrix)]{.hl} $\mathbf{K}=\boldsymbol{\Phi}\boldsymbol{\Phi}^\top$를 도입합니다:

$$
K_{nm}=\boldsymbol{\phi}(\mathbf{x}_n)^\top\boldsymbol{\phi}(\mathbf{x}_m)=k(\mathbf{x}_n,\mathbf{x}_m)
$$

- 그러면 오차 함수는 다음과 같이 됩니다:

$$
J(\mathbf{a})=\frac{1}{2} \mathbf{a}^{\top} \mathbf{K} \mathbf{K} \mathbf{a}-\mathbf{a}^{\top} \mathbf{K} \boldsymbol{\mathsf{t}}+\frac{1}{2} \boldsymbol{\mathsf{t}}^{\top} \boldsymbol{\mathsf{t}}+\frac{\lambda}{2} \mathbf{a}^{\top} \mathbf{K} \mathbf{a}
$$

---
layout: prism
heading: 쌍대 표현 (4/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- $J(\mathbf{a})$를 $\mathbf{a}$에 대해 미분하고 그 결과를 $0$으로 두어 $\mathbf{a}$를 구합니다:

$$
\begin{gathered}
\nabla_\mathbf{a} J(\mathbf{a})=\mathbf{K}\mathbf{K}\mathbf{a}-\mathbf{K}\boldsymbol{\mathsf{t}} +\lambda\mathbf{K}\mathbf{a}=0\\
\mathbf{K}(\mathbf{K}+\lambda\mathbf{I}_N)\mathbf{a}=\mathbf{K}\boldsymbol{\mathsf{t}}\\
(\mathbf{K}+\lambda\mathbf{I}_N)\mathbf{a}=\boldsymbol{\mathsf{t}}\quad\text{($\mathbf{K}$가 full-rank라고 가정)}\\
\therefore \mathbf{a}=\left(\mathbf{K}+\lambda \mathbf{I}_N\right)^{-1} \boldsymbol{\mathsf{t}}
\end{gathered}
$$

- 커널 기반 선형 회귀는 새로운 입력 $\mathbf{x}$를 다음과 같이 예측합니다:

$$
y(\mathbf{x})=\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x})=\mathbf{a}^{\top} \boldsymbol{\Phi} \boldsymbol{\phi}(\mathbf{x})=\mathbf{k}(\mathbf{x})^{\top}(\mathbf{K}+\lambda \mathbf{I}_N)^{-1} \boldsymbol{\mathsf{t}}
$$

<div class="sub-item">

$\mathbf{k}(\mathbf{x})$의 $n$번째 원소는 $k_n(\mathbf{x})=k(\mathbf{x}_n,\mathbf{x})$입니다.

</div>

---
layout: prism
heading: 쌍대 표현 (5/5)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(0)
X = np.linspace(-3, 3, 40).reshape(-1, 1)                     # 1D inputs
t = np.sin(X).ravel() + 0.1 * rng.standard_normal(40)        # targets: sin(x) + noise
lam = 0.1

def rbf(A, B, s=1.0):                                         # Gaussian kernel
    d2 = np.sum(A**2, 1)[:, None] + np.sum(B**2, 1)[None, :] - 2 * A @ B.T
    return np.exp(-d2 / (2 * s**2))

K = rbf(X, X)                                                 # Gram matrix K_nm = k(x_n, x_m)
a = np.linalg.solve(K + lam * np.eye(len(X)), t)             # a = (K + lam I)^-1 t

Xte = np.linspace(-3, 3, 7).reshape(-1, 1)
ypred = rbf(Xte, X) @ a                                       # y(x) = k(x)^T (K + lam I)^-1 t
print("Dual kernel ridge regression (Gaussian kernel):")
for xi, yi in zip(Xte.ravel(), ypred):
    print(f"  x = {xi:+.2f}   y_pred = {yi:+.3f}   sin(x) = {np.sin(xi):+.3f}")

# Sanity check: with a LINEAR kernel, the dual prediction equals primal ridge regression
Kl = X @ X.T
al = np.linalg.solve(Kl + lam * np.eye(len(X)), t)
y_dual = (Xte @ X.T) @ al
w_primal = np.linalg.solve(X.T @ X + lam * np.eye(1), X.T @ t)
y_primal = Xte @ w_primal
print(f"\nLinear kernel: max|dual - primal| = {np.max(np.abs(y_dual - y_primal)):.2e}  (== 0)")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">쌍대 표현</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">커널 구성</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가우시안 과정</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">최대 마진 분류기</span></p>
  </div>

</div>

---
layout: prism
heading: 커널 구성 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 유효한 커널 함수를 구성하려면, 먼저 특징 공간 함수 $\boldsymbol{\phi}(\cdot)$를 정한 뒤 정의에 따라 커널을 찾을 수 있습니다.

- 예를 들어, 선형 입력 공간에 대한 커널 함수는 다음과 같이 정의됩니다:

$$
k(x, x^{\prime})=\boldsymbol{\phi}(x)^{\top} \boldsymbol{\phi}(x^{\prime})=\sum_{i=1}^M \phi_i(x) \phi_i(x^{\prime})
$$

- 가장 널리 사용되는 커널 중 하나는 [가우시안 커널(Gaussian kernel)]{.hl}입니다:

$$
k(\mathbf{x}, \mathbf{x}^{\prime})=\exp (-\|\mathbf{x}-\mathbf{x}^{\prime}\|^2 / 2 \sigma^2)
$$

---
layout: prism
heading: 커널 구성 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 두 개의 유효한 커널 $k_1(\mathbf{x},\mathbf{x}')$과 $k_2(\mathbf{x},\mathbf{x}')$이 있을 때, 다음도 유효한 커널입니다:

$$
\begin{aligned}
k(\mathbf{x}, \mathbf{x}^{\prime}) & =c\, k_1(\mathbf{x}, \mathbf{x}^{\prime}) & k(\mathbf{x}, \mathbf{x}^{\prime}) & =f(\mathbf{x}) k_1(\mathbf{x}, \mathbf{x}^{\prime}) f(\mathbf{x}^{\prime}) \\
k(\mathbf{x}, \mathbf{x}^{\prime}) & =q(k_1(\mathbf{x}, \mathbf{x}^{\prime})) & k(\mathbf{x}, \mathbf{x}^{\prime}) & =\exp (k_1(\mathbf{x}, \mathbf{x}^{\prime})) \\
k(\mathbf{x}, \mathbf{x}^{\prime}) & =k_1(\mathbf{x}, \mathbf{x}^{\prime})+k_2(\mathbf{x}, \mathbf{x}^{\prime}) & k(\mathbf{x}, \mathbf{x}^{\prime}) & =k_1(\mathbf{x}, \mathbf{x}^{\prime}) k_2(\mathbf{x}, \mathbf{x}^{\prime}) \\
k(\mathbf{x}, \mathbf{x}^{\prime}) & =k_3(\boldsymbol{\phi}(\mathbf{x}), \boldsymbol{\phi}(\mathbf{x}^{\prime})) & k(\mathbf{x}, \mathbf{x}^{\prime}) & =\mathbf{x}^{\top} \mathbf{A} \mathbf{x}^{\prime} \\
k(\mathbf{x}, \mathbf{x}^{\prime}) & =k_a(\mathbf{x}_a, \mathbf{x}_a^{\prime})+k_b(\mathbf{x}_b, \mathbf{x}_b^{\prime}) & k(\mathbf{x}, \mathbf{x}^{\prime}) & =k_a(\mathbf{x}_a, \mathbf{x}_a^{\prime}) k_b(\mathbf{x}_b, \mathbf{x}_b^{\prime})
\end{aligned}
$$

<div class="sub-item">

여기서 $c>0$, $f(\cdot)$는 임의의 함수, $q(\cdot)$는 음이 아닌 계수를 갖는 다항식, $\mathbf{A}$는 대칭 양의 준정부호 행렬입니다.

</div>

---
layout: prism
heading: 커널 구성 (3/3)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(1)
X = rng.standard_normal((12, 3))                             # 12 samples in 3D

def gram_linear(X):
    return X @ X.T                                           # k1(x, x') = x^T x'
def gram_rbf(X, s=1.5):
    d2 = np.sum(X**2, 1)[:, None] + np.sum(X**2, 1)[None, :] - 2 * X @ X.T
    return np.exp(-d2 / (2 * s**2))                          # k2(x, x') = exp(-||x-x'||^2/2s^2)

def min_eig(K):
    return np.linalg.eigvalsh((K + K.T) / 2).min()          # smallest eigenvalue

K1, K2 = gram_linear(X), gram_rbf(X)
print("A valid kernel must yield a positive semi-definite Gram matrix (min eig >= 0):")
print(f"  linear   k1                 : min eig = {min_eig(K1):+.4e}")
print(f"  Gaussian k2                 : min eig = {min_eig(K2):+.4e}")
print(f"  sum      k1 + k2            : min eig = {min_eig(K1 + K2):+.4e}")
print(f"  product  k1 * k2 (elem-wise): min eig = {min_eig(K1 * K2):+.4e}")
print(f"  scaled   3 * k2            : min eig = {min_eig(3 * K2):+.4e}")
print("\nAll construction rules preserve PSD => each produces a valid kernel.")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">쌍대 표현</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">커널 구성</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">가우시안 과정</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">최대 마진 분류기</span></p>
  </div>

</div>

---
layout: prism
heading: 가우시안 과정 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- [가우시안 과정(Gaussian process)]{.hl}은 함수 $y(\mathbf{x})$의 확률 분포로 정의되는 확률 과정입니다.

<div class="sub-item">

이 분포에서 $\mathbf{x}_1,\ldots,\mathbf{x}_N$으로부터 추정된 값 $y(\mathbf{x})$는 결합적으로 가우시안이며, $y_1,\ldots,y_N$의 결합 분포는 평균과 공분산으로 정의됩니다.

</div>

<div class="sub-item">

예를 들어, 선형 회귀 모델에 대해 모델 사전분포 $p(\mathbf{w})=\mathcal{N}(\mathbf{w}|\mathbf{0},\alpha^{-1}\mathbf{I})$를 가정하면 다음을 얻습니다:

</div>

$$
\mathbb{E}[\boldsymbol{\mathsf{y}}]=\boldsymbol{\Phi} \mathbb{E}[\mathbf{w}]=\mathbf{0}, \qquad
\operatorname{cov}[\boldsymbol{\mathsf{y}}]=\boldsymbol{\Phi} \mathbb{E}[\mathbf{w} \mathbf{w}^{\top}] \boldsymbol{\Phi}^{\top}=\frac{1}{\alpha} \boldsymbol{\Phi} \boldsymbol{\Phi}^{\top}=\mathbf{K}
$$

<div class="sub-item">

$\boldsymbol{\mathsf{y}}$는 $y_n=y(\mathbf{x}_n)$으로 구성된 벡터이고, $\mathbf{K}$는 그람 행렬 $K_{nm}=k(\mathbf{x}_n, \mathbf{x}_m)=\frac{1}{\alpha} \boldsymbol{\phi}(\mathbf{x}_n)^{\top} \boldsymbol{\phi}(\mathbf{x}_m)$입니다.

</div>

- 가우시안 과정을 직접 찾아보세요!

---
layout: prism
heading: 가우시안 과정 (2/2)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(4)
X = np.linspace(-5, 5, 8).reshape(-1, 1)                     # 8 input locations

def rbf(A, B, s=1.0):
    d2 = np.sum(A**2, 1)[:, None] + np.sum(B**2, 1)[None, :] - 2 * A @ B.T
    return np.exp(-d2 / (2 * s**2))

K = rbf(X, X, s=2.0) + 1e-8 * np.eye(len(X))                 # cov[y] = K (GP prior, mean 0)
L = np.linalg.cholesky(K)

print("Gaussian process prior:  y ~ N(0, K),  K_nm = k(x_n, x_m)")
print("Three sampled functions y(x) evaluated at the 8 input points:")
for s in range(3):
    y = L @ rng.standard_normal(len(X))                     # draw y = L z, z ~ N(0, I)
    print("  sample", s + 1, ":", np.array2string(y, precision=2, floatmode="fixed"))

c_near = K[0, 1] / np.sqrt(K[0, 0] * K[1, 1])               # adjacent inputs
c_far = K[0, -1] / np.sqrt(K[0, 0] * K[-1, -1])            # far-apart inputs
print(f"\ncorr(y at adjacent inputs) = {c_near:.3f}  (strongly correlated)")
print(f"corr(y at far inputs)      = {c_far:.3f}  (nearly independent)")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">쌍대 표현</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">커널 구성</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가우시안 과정</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">최대 마진 분류기</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">여유 변수</span></p>
  </div>

</div>

---
layout: prism
heading: 최대 마진 분류기 (1/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 커널 기반 학습 알고리즘은 모든 데이터 쌍에 대해 커널 함수 $k(\cdot,\cdot)$를 추정해야 합니다.

<div class="sub-item">

이는 많은 계산량을 요구하거나, 심지어 다루기 어려울(intractable) 수 있습니다.

</div>

- 해가 [희소(sparse)]{.hl}한 커널 기반 방법은 학습 샘플의 부분집합에만 의존합니다.

- 가장 널리 사용되는 희소 커널 기계 중 하나인 [서포트 벡터 머신(support vector machine; SVM)]{.hl}은 분류, 회귀 및 다양한 다른 과제에 활용됩니다.

<div class="sub-item">

SVM은 볼록 최적화를 푸는 것에 기반하므로, 지역 최적해가 전역 최적해가 됩니다. 또한 결정적(deterministic)이어서 사후 확률을 출력하지 않습니다.

</div>

---
layout: prism
heading: 최대 마진 분류기 (2/6)
---

- 다음과 같은 이진 클래스 분류 문제를 고려하면, 데이터포인트를 정확히 구분하는 해가 여러 개 존재할 수 있습니다:

$$
y(\mathbf{x})=\mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})+b
$$

<div class="sub-item">

해가 여러 개 있다면, 최소의 일반화 오차를 보이는 유일한 해를 찾는 것이 가장 좋습니다.

</div>

- SVM은 [마진(margin)]{.hl}이라는 개념을 도입하여, 결정 경계와 샘플 사이의 최소 거리를 최대화하는 결정 경계를 계산합니다.

<div class="img-row" style="max-width: 45%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure7.1a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure7.1b.png"/>

</div>

---
layout: prism
heading: 최대 마진 분류기 (3/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 모든 데이터포인트가 올바르게 분류되었다고 가정하면, 점 $\mathbf{x}_n$과 결정 경계 사이의 거리는 다음과 같습니다:

$$
\frac{t_n y\left(\mathbf{x}_n\right)}{\|\mathbf{w}\|}=\frac{t_n(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)+b)}{\|\mathbf{w}\|}
$$

- 마진은 결정 경계로부터 가장 가까운 점 $\mathbf{x}_n$까지의 수직 거리이므로, SVM은 마진을 최대화하여 얻어집니다:

$$
\underset{\mathbf{w}, b}{\arg \max }\left[\frac{1}{\|\mathbf{w}\|} \min _n\{t_n(\mathbf{w}^{\top} \boldsymbol{\phi}\left(\mathbf{x}_n\right)+b)\}\right]
$$

<div class="sub-item">

이 최적화 문제는 직접 풀기 어렵습니다.

</div>

---
layout: prism
heading: 최대 마진 분류기 (4/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- $\mathbf{w}$와 $b$에 0이 아닌 임의의 상수를 곱해도 거리는 변하지 않으므로, 경계에 가장 가까운 점들에 대해 다음과 같이 임의로 설정할 수 있습니다:

$$
t_n(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)+b)=1
$$

<div class="sub-item">

그러면 모든 데이터포인트는 [정규 표현(canonical representation)]{.hl} 제약 $t_n(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)+b) \geqslant 1$, $n=1, \ldots, N$을 만족합니다.

</div>

- 경계에 가장 가까운 점이 적어도 하나 존재하므로, 마진을 최대화하는 것은 $\|\mathbf{w}\|^{-1}$을 최대화하는 것, 즉 $\|\mathbf{w}\|^2$을 최소화하는 것으로 단순화됩니다:

$$
\underset{\mathbf{w}, b}{\arg \min } \frac{1}{2}\|\mathbf{w}\|^2
$$

---
layout: prism
heading: 최대 마진 분류기 (5/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 마지막으로, 다음과 같은 라그랑주 함수를 구성합니다:

$$
L(\mathbf{w}, b, \mathbf{a})=\frac{1}{2}\|\mathbf{w}\|^2-\sum_{n=1}^N a_n\{t_n(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)+b)-1\}
$$

- 이 함수를 미분하면 다음을 얻습니다:

$$
\mathbf{w} =\sum_{n=1}^N a_n t_n \boldsymbol{\phi}\left(\mathbf{x}_n\right), \qquad 0 =\sum_{n=1}^N a_n t_n
$$

- 이 라그랑주 함수의 쌍대 표현을 계산할 수 있음에 유의하세요.

---
layout: prism
heading: 최대 마진 분류기 (6/6)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(2)
X = np.vstack([rng.normal([-2, -2], 0.6, (25, 2)),          # linearly separable data
               rng.normal([ 2,  2], 0.6, (25, 2))])
t = np.array([-1.0] * 25 + [1.0] * 25)
N = len(X)

Q = (X @ X.T) * np.outer(t, t)                              # dual: maximize 1^T a - 1/2 a^T Q a
a = np.zeros(N); eta = 1e-3
for _ in range(20000):
    a = a + eta * (1 - Q @ a)                              # gradient ascent step
    a -= t * (t @ a) / (t @ t)                             # project onto sum_n a_n t_n = 0
    a = np.maximum(a, 0.0)                                 # enforce a_n >= 0

w = (a * t) @ X                                            # w = sum_n a_n t_n x_n
sv = a > 1e-4                                              # support vectors have a_n > 0
b = np.mean(t[sv] - X[sv] @ w)
pred = np.sign(X @ w + b)
print(f"Support vectors            : {int(sv.sum())} of {N}")
print(f"Margin  1/||w||            : {1 / np.linalg.norm(w):.3f}")
print(f"Training accuracy          : {np.mean(pred == t):.3f}")
print(f"min_n t_n (w^T x_n + b)    : {np.min(t * (X @ w + b)):.3f}   (~1 at the margin)")
```

</PyRunner>

---
layout: prism
heading: 여유 변수 (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

- 실제로는 클래스 조건부 분포 사이에 겹침이 존재할 수 있습니다.

- 클래스 분포가 겹칠 때, 학습 데이터를 완벽하게 분리하도록 모델을 학습하면 일반화 성능이 저하될 수 있습니다. 따라서 일부 학습 점이 오분류되도록 허용합니다.

- 데이터포인트가 마진 경계의 잘못된 쪽에 존재하도록 허용하되, 경계로부터의 거리가 커질수록 증가하는 페널티를 [여유 변수(slack variable)]{.hl} $\xi_n\geqslant 0$을 사용하여 부과합니다.

<div class="sub-item">

각 데이터포인트마다 하나의 여유 변수가 사용됩니다. 데이터포인트가 올바른 마진 경계 안쪽에 있으면 $\xi_n=0$, 그렇지 않으면 $\xi_n=|t_n-y(\mathbf{x}_n)|$입니다. 그러면 제약은 $t_n\, y(\mathbf{x}_n) \geqslant 1-\xi_n$, $n=1, \ldots, N$이 됩니다.

</div>

---
layout: prism
heading: 여유 변수 (2/4)
---

- $\xi_n=0$이면 데이터포인트는 올바르게 분류되고, $0<\xi_n\leqslant 1$이면 올바르게 분류되지만 마진 안쪽에 있으며, $\xi_n>1$이면 오분류됩니다.

<div class="sub-item">

$\xi_n>1$을 허용하는 것을 [소프트 마진(soft margin)]{.hl} 제약, 그렇지 않은 경우를 [하드 마진(hard margin)]{.hl} 제약이라고 합니다.

</div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure7.3.png" class="img-center" style="width: 19rem;" />

---
layout: prism
heading: 여유 변수 (3/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 최종 목표는 다음을 최소화하는 것입니다:

$$
C \sum_{n=1}^N \xi_n+\frac{1}{2}\|\mathbf{w}\|^2
$$

<div class="sub-item">

매개변수 $C>0$는 여유 변수와 마진 사이의 절충을 조절합니다.

</div>

- 라그랑주 함수를 얻습니다:

$$
\begin{aligned}
L(\mathbf{w}, b, \boldsymbol{\xi}, \mathbf{a}, \boldsymbol{\mu})=&\frac{1}{2}\|\mathbf{w}\|^2+C \sum_{n=1}^N \xi_n\\
&-\sum_{n=1}^N a_n\left\{t_n y\left(\mathbf{x}_n\right)-1+\xi_n\right\}-\sum_{n=1}^N \mu_n \xi_n
\end{aligned}
$$

---
layout: prism
heading: 여유 변수 (4/4)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(3)
X = np.vstack([rng.normal([-1.0, 0.0], 1.1, (40, 2)),       # overlapping (non-separable)
               rng.normal([ 1.0, 0.0], 1.1, (40, 2))])
t = np.array([-1.0] * 40 + [1.0] * 40)
N = len(X)
Q = (X @ X.T) * np.outer(t, t)                              # linear kernel

def solve_soft(C, iters=20000, eta=1e-3):
    a = np.zeros(N)
    for _ in range(iters):
        a = a + eta * (1 - Q @ a)
        a -= t * (t @ a) / (t @ t)                          # sum_n a_n t_n = 0
        a = np.clip(a, 0.0, C)                              # box constraint 0 <= a_n <= C
    w = (a * t) @ X
    on = (a > 1e-4) & (a < C - 1e-4)                        # points exactly on the margin
    b = np.mean(t[on] - X[on] @ w) if on.any() else 0.0
    return 1 / np.linalg.norm(w), np.mean(np.sign(X @ w + b) == t), int((a > 1e-4).sum())

print("Soft-margin SVM: C trades off margin width against slack (misclassification).")
print(f"{'C':>7} | {'margin 1/||w||':>14} | {'train acc':>9} | {'#support vec':>12}")
for C in [0.01, 0.1, 1.0, 10.0]:
    m, acc, nsv = solve_soft(C)
    print(f"{C:>7.2f} | {m:>14.3f} | {acc:>9.3f} | {nsv:>12d}")
print("\nSmall C -> wider margin, more support vectors; large C -> narrower margin, harder fit.")
```

</PyRunner>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
