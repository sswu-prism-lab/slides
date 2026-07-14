---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 5 (KO)
download: true
info: |
  ## 고급 기계학습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-5/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">5주차: 선형 분류 모델</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span class="text-gray-900 dark:text-gray-100">선형 분류 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">커널 방법론</span></p>
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
heading: 복습 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 가우시안 분포로부터 i.i.d.로 샘플링된 데이터포인트의 로그가능도 함수를 다음과 같이 정의합니다:

$$
\ln p(\boldsymbol{\mathsf{x}}|\mu,\sigma^2)=\sum_{n=1}^{N}\ln p(x_n)=\sum_{n=1}^{N}\ln\left\{ \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(- \frac{(x_n-\mu)^2}{2\sigma^2} \right)\right\}
$$

<div class="sub-item">

그러면 로그가능도 함수를 각각 $\mu$와 $\sigma$에 대해 미분하여 표본평균 $\mu_\mathrm{ML}$과 표본분산 $\sigma^2_\mathrm{ML}$을 추정할 수 있습니다.

</div>

- 나아가 표본평균과 표본분산의 기댓값을 추정하면, 평균의 기댓값은 편향되지 않는 반면 분산의 기댓값은 편향된다는 것을 관찰할 수 있습니다.

<div class="sub-item">

이는 과적합의 가장 중요한 원인 중 하나입니다.

</div>

---
layout: prism
heading: 복습 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 기저 함수를 사용한 선형 회귀 모델은 다음과 같이 정의할 수 있습니다:

$$
y(\mathbf{x},\mathbf{w})=\sum_{j=0}^{M-1}w_j\phi_j(\mathbf{x})=\mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})
$$

- 여기서, 정규방정식을 풀어 가중치 벡터 $\mathbf{w}$에 대한 최대가능도 해를 다음과 같이 얻을 수 있습니다:

$$
\mathbf{w}_{\mathrm{ML}}=(\boldsymbol{\Phi}^{\top} \boldsymbol{\Phi})^{-1} \boldsymbol{\Phi}^{\top} \boldsymbol{\mathsf{t}}
$$

<div class="sub-item">

$\boldsymbol{\Phi}$는 설계 행렬을 나타냅니다.

</div>

- 더 큰 데이터셋에 대해서는 확률적 경사 하강법 알고리즘을 도입할 수 있습니다:

$$
\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}-\eta \nabla E_n
$$

---
layout: prism
heading: 복습 (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 빈도주의 관점의 기계학습 알고리즘은 편향–분산 트레이드오프를 겪는다는 점에 유의하세요.

<div class="sub-item">

편향은 모든 데이터셋에 대한 평균 예측이 원하는 회귀 함수와 얼마나 차이 나는지를 나타냅니다.

</div>

<div class="sub-item">

분산은 개별 데이터셋에 대한 해가 그 평균 주위에서 얼마나 변동하는지를 측정합니다.

</div>

- 완전한 베이지안 선형 회귀를 위해서는 모델 매개변수에 대한 사전분포 $p(\mathbf{w})$를 도입해야 합니다.

<div class="sub-item">

가우시안 가능도 함수에 대한 켤레 사전분포를 설정하려면, 사전분포를 가우시안 분포로 설정해야 합니다.

</div>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">판별 함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">이진 클래스</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">다중 클래스</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">분류를 위한 최소제곱</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">피셔 선형 판별</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">퍼셉트론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률적 생성 모델</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률적 판별 모델</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">라플라스 근사</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">베이지안 로지스틱 회귀</span></p>
  </div>

</div>

---
layout: prism
heading: 판별 함수
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 분류 문제에서는 입력 값이 $K$개의 이산 클래스 $\mathcal{C}_k$, $k=1,\ldots,K$에 하나의 입력이 하나의 클래스로 할당됩니다.

<div class="sub-item">

입력 공간은 여러 개의 [결정 영역(decision regions)]{.hl}으로 나뉘며, 이는 [결정 경계(decision boundaries)]{.hl}, 즉 [결정 표면(decision surfaces)]{.hl}이라 불리는 기준에 의해 구분됩니다.

</div>

<div class="sub-item">

선형 결정 표면으로 정확히 나눌 수 있는 데이터셋을 [선형 분리 가능(linearly separable)]{.hl} 데이터셋이라고 합니다.

</div>

- 이전에는 목표 변수로 _실수_ 를 사용했지만, 이제는 [원-핫 인코딩된(one hot encoded)]{.hl} 목표 벡터를 활용한다는 점에 유의하세요.

<div class="sub-item">

$K$개 클래스에 대한 원-핫 인코딩 벡터 $\mathbf{t}$는 두 가지 조건으로 제약됩니다: $\mathbf{t}\in\{0,1\}^K$이고 $\sum_j t_j=1$이며, 여기서 $t_j$는 $\mathbf{t}$의 $j$번째 성분입니다.

</div>

- [판별 함수(discriminant function)]{.hl}는 입력 벡터 $\mathbf{x}$를 $K$개 클래스 $\mathcal{C}_k$ 중 하나로 할당하는 함수입니다.

<div class="sub-item">

결정 경계가 초평면인 경우, 이를 [선형 판별 함수(linear discriminant function)]{.hl}라고 합니다.

</div>

---
layout: prism
heading: 이진 클래스 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 선형 판별 함수는 입력 벡터에 대해 선형이며 다음과 같이 주어집니다:

$$
y(\mathbf{x})=\mathbf{w}^\top\mathbf{x}+w_0
$$

<div class="sub-item">

$\mathbf{w}$는 [가중치 벡터(weight vector)]{.hl}이고 $w_0$는 [편향(bias)]{.hl}입니다.

</div>

<div class="sub-item">

이진 클래스 분류 문제를 가정하므로, 일반성을 잃지 않고 $y(\mathbf{x})\geqslant0$이면 입력을 $\mathcal{C}_1$에, 그렇지 않으면 $\mathcal{C}_2$에 할당할 수 있습니다.

</div>

<div class="subsub-item">

따라서 여기서 결정 경계는 $y(\mathbf{x})=0$입니다.

</div>

- 간단히 하기 위해, 가상 변수 $x_0=1$을 도입하고 $\widetilde{\mathbf{w}}=(w_0,\mathbf{w})$와 $\widetilde{\mathbf{x}}=(x_0,\mathbf{x})$를 정의하면 다음을 얻습니다:

$$
y(\mathbf{x})=\widetilde{\mathbf{w}}^\top\widetilde{\mathbf{x}}
$$

---
layout: prism
heading: 이진 클래스 (2/2)
---

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.1.png" class="img-center" style="width: 25rem;" />

---
layout: prism
heading: 다중 클래스 (1/3)
---

- 다중 클래스 분류 문제, 즉 $K>2$를 다뤄야 한다고 가정합시다.

<div class="sub-item">

여기서, $K-1$개의 분류기를 사용할 수 있으며, 각 분류기는 입력 값이 $\mathcal{C}_k$에 속하는지 아닌지를 분류하는 이진 분류에 사용됩니다.

</div>

<div class="subsub-item">

이 방식을 [일대다(one-versus-the-rest)]{.hl} 분류기라고 합니다.

</div>

<div class="sub-item">

또 다른 방식인 [일대일(one-versus-one)]{.hl} 분류기는 가능한 모든 클래스 쌍을 분류하기 위해 $K(K-1)/2$개의 분류기를 사용합니다.

</div>

<div class="img-row" style="max-width: 45%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.2a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.2b.png"/>

</div>

---
layout: prism
heading: 다중 클래스 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 일대다 및/또는 일대일 분류기에는 일부 불확실한 영역이 남는다는 점을 생각해보세요.

- 앞서 언급한 문제를 피하기 위해, $K$개의 선형 함수로 구성된 통합된 $K$-클래스 판별 함수를 사용합니다:

$$
y_k(\mathbf{x})=\mathbf{w}_k^\top\mathbf{x}+w_{k0}
$$

<div class="sub-item">

모든 $j\neq k$에 대해 $y_k(\mathbf{x})>y_j(\mathbf{x})$이면 $\mathbf{x}$를 $\mathcal{C}_k$에 할당합니다.

</div>

<div class="sub-item">

$\mathcal{C}_k$와 $\mathcal{C}_j$ 사이의 결정 경계는 $y_k(\mathbf{x})=y_j(\mathbf{x})$로 정의되며, $(D-1)$차원 초평면은 다음과 같이 정의할 수 있습니다:

</div>

$$
(\mathbf{w}_k -\mathbf{w}_j)^\top\mathbf{x}+(w_{k0}-w_{j0})=0
$$

---
layout: prism
heading: 다중 클래스 (3/3)
---

- 다중 클래스 분류 판별 함수의 결정 경계는 항상 유일하게 연결되며, 볼록(convex) 성질을 갖습니다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.3.png" class="img-center" style="width: 25rem;" />

---
layout: prism
heading: 분류를 위한 최소제곱 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- $K$-클래스 분류를 위한 분류 모델을 다시 유도해봅시다:

$$
\mathbf{y}(\mathbf{x})=\widetilde{\mathbf{W}}^\top\widetilde{\mathbf{x}}
$$

<div class="sub-item">

$\widetilde{\mathbf{W}}$의 $k$번째 열은 $D+1$차원 벡터 $\widetilde{\mathbf{w}}_k=(w_{k0},\mathbf{w}_k^\top)^\top$입니다.

</div>

- 주어진 학습 데이터셋 $\{\mathbf{x}_n,\mathbf{t}_n\}$, $n=1,\ldots,N$에 대해, $n$번째 행이 각각 $\widetilde{\mathbf{x}}_n^\top$과 $\mathbf{t}_n^\top$인 행렬 $\mathbf{X}$와 $\mathbf{T}$를 정의하면, 최소제곱 오차 함수를 다음과 같이 정의할 수 있습니다:

$$
E_D(\widetilde{\mathbf{W}})=\frac{1}{2} \operatorname{Tr}\{(\widetilde{\mathbf{X}} \widetilde{\mathbf{W}}-\mathbf{T})^{\top}(\widetilde{\mathbf{X}} \widetilde{\mathbf{W}}-\mathbf{T})\}
$$

---
layout: prism
heading: 분류를 위한 최소제곱 (2/3)
---

- 오차 함수를 $\widetilde{\mathbf{W}}$에 대해 미분하고 $0$으로 놓으면, 해를 구할 수 있습니다:

$$
\widetilde{\mathbf{W}}=(\widetilde{\mathbf{X}}^{\top} \widetilde{\mathbf{X}})^{-1} \widetilde{\mathbf{X}}^{\top} \mathbf{T}
$$

<div class="subsub-item">

회귀 문제에 대한 정규방정식을 구해보세요.

</div>

- 최소제곱 오차 함수를 사용하면 닫힌 형태의 해를 얻을 수 있지만, 이상치에 강건하지 않습니다.

<div class="sub-item">

최소제곱법은 가우시안 분포 하에서의 최대가능도 추정과 관련되어 있으므로, 목표 값이 가우시안이 아니면 잘 작동하지 않는다는 점에 유의하세요.

</div>

<div class="img-row" style="max-width: 32%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.4a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.4b.png"/>

</div>

---
layout: prism
heading: 분류를 위한 최소제곱 (3/3)
---

<PyRunner>

```python
import numpy as np

def one_hot(lab, K=2):
    T = np.zeros((len(lab), K)); T[np.arange(len(lab)), lab] = 1; return T

def fit_W(X, lab):                                   # W = (X^T X)^-1 X^T T
    Xt = np.column_stack([np.ones(len(X)), X]); return np.linalg.inv(Xt.T @ Xt) @ Xt.T @ one_hot(lab)

def boundary_x1(W):                                  # boundary crossing at x2 = 0
    a = W[:, 1] - W[:, 0]; return -a[0] / a[1]

N = 60
X0 = np.random.default_rng(0).normal([-2, 0], 1.0, size=(N, 2))
X1 = np.random.default_rng(0).normal([2, 0], 1.0, size=(N, 2))
X = np.vstack([X0, X1]); lab = np.array([0] * N + [1] * N)

W = fit_W(X, lab)
print(f"Clean boundary crosses x-axis at x1 = {boundary_x1(W):+.3f}  (ideal ~ 0)")

# Far outliers that STILL belong to class 1 (correct side, just far away)
Xout = np.vstack([X1, np.random.default_rng(0).normal([15, 0], 0.5, size=(40, 2))])
Xall = np.vstack([X0, Xout]); lall = np.array([0] * N + [1] * (N + 40))
Wc = fit_W(Xall, lall)
pred_bulk = np.argmax(np.column_stack([np.ones(N), X1]) @ Wc, axis=1)

print(f"With outliers, boundary moves to  x1 = {boundary_x1(Wc):+.3f}")
print(f"Genuine class-1 points misclassified = {int((pred_bulk != 1).sum())}/{N}")
print("\nLeast squares is NOT robust: correct-but-far outliers still drag the boundary.")
```

</PyRunner>

---
layout: prism
heading: 피셔 선형 판별 (1/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 선형 분류 모델은 차원 축소의 관점에서 볼 수 있습니다.

- $D$차원 입력 벡터 $\mathbf{x}$가 1차원(1D)으로 투영된다고 생각해봅시다.

$$
y=\mathbf{w}^\top \mathbf{x}
$$

<div class="sub-item">

일반적으로, 1D로의 투영은 많은 양의 정보를 잃습니다.

</div>

<div class="sub-item">

$D$차원 공간에서 잘 분리되어 있던 클래스들이 1D 공간으로 투영되면 크게 겹칠 수 있습니다.

</div>

<div class="subsub-item">

그러나 선형 분류기의 가중치 벡터 $\mathbf{w}$의 성분을 신중하게 조정하면, 클래스 분리도를 최대화하는 투영을 선택할 수 있습니다.

</div>

---
layout: prism
heading: 피셔 선형 판별 (2/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 클래스 $\mathcal{C}_1$의 $N_1$개 데이터포인트와 클래스 $\mathcal{C}_2$의 $N_2$개 데이터포인트에 대해, 각각의 평균 벡터 $\mathbf{m}_1$과 $\mathbf{m}_2$를 추정할 수 있습니다:

$$
\mathbf{m}_1=\frac{1}{N_1} \sum_{n \in \mathcal{C}_1} \mathbf{x}_n, \qquad \mathbf{m}_2=\frac{1}{N_2} \sum_{n \in \mathcal{C}_2} \mathbf{x}_n
$$

- 클래스 평균 간의 분리를 최대화하는 $\mathbf{w}$를 다음과 같이 계산할 수 있습니다:

$$
\begin{aligned}
m_2-m_1 & =\mathbf{w}^{\top}\left(\mathbf{m}_2-\mathbf{m}_1\right) \\
m_k & =\mathbf{w}^{\top} \mathbf{m}_k
\end{aligned}
$$

<div class="sub-item">

단순히 $\mathbf{w}$의 크기를 키우는 것만으로도 $m_2-m_1$을 증가시킬 수 있다는 점에 유의하세요.

</div>

---
layout: prism
heading: 피셔 선형 판별 (3/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 피셔는 벡터 $\mathbf{w}$로 투영했을 때 클래스 평균 간의 분리를 최대화하는 동시에 각 클래스 내의 분산을 최소화하는 방법을 제안했습니다.

- $\mathcal{C}_k$의 클래스 내 분산은 다음과 같이 계산됩니다:

$$
s_k^2=\sum_{n \in \mathcal{C}_k}\left(y_n-m_k\right)^2
$$

- 최종적으로, 피셔 기준은 [클래스 간(between class)]{.hl} 분산 대 [클래스 내(within class)]{.hl} 분산의 비율로 정의됩니다:

$$
J(\mathbf{w})=\frac{\left(m_2-m_1\right)^2}{s_1^2+s_2^2}
$$

---
layout: prism
heading: 피셔 선형 판별 (4/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 피셔 기준은 $\mathbf{w}$로 다음과 같이 다시 유도할 수 있습니다:

$$
J(\mathbf{w})=\frac{\mathbf{w}^{\top} \mathbf{S}_{\mathrm{B}} \mathbf{w}}{\mathbf{w}^{\top} \mathbf{S}_{\mathrm{W}} \mathbf{w}}
$$

<div class="sub-item">

$\mathbf{S}_\mathrm{B}$와 $\mathbf{S}_\mathrm{W}$는 각각 클래스 간 및 클래스 내 공분산 행렬을 나타냅니다.

</div>

$$
\begin{gathered}
\mathbf{S}_{\mathrm{B}}=\left(\mathbf{m}_2-\mathbf{m}_1\right)\left(\mathbf{m}_2-\mathbf{m}_1\right)^{\top}\\
\mathbf{S}_{\mathrm{W}}=\sum_{n \in \mathcal{C}_1}\left(\mathbf{x}_n-\mathbf{m}_1\right)\left(\mathbf{x}_n-\mathbf{m}_1\right)^{\top}+\sum_{n \in \mathcal{C}_2}\left(\mathbf{x}_n-\mathbf{m}_2\right)\left(\mathbf{x}_n-\mathbf{m}_2\right)^{\top}
\end{gathered}
$$

- $J(\mathbf{w})$를 $\mathbf{w}$에 대해 미분하면 다음을 얻습니다:

$$
\mathbf{w} \propto \mathbf{S}_{\mathrm{W}}^{-1}\left(\mathbf{m}_2-\mathbf{m}_1\right)
$$

<div class="sub-item">

이 방법은 [피셔 선형 판별(Fisher's linear discriminant)]{.hl}로 알려져 있습니다.

</div>

---
layout: prism
heading: 피셔 선형 판별 (5/6)
---

<div class="img-row" style="max-width: 88%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.6a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.6b.png"/>

</div>

---
layout: prism
heading: 피셔 선형 판별 (6/6)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(1)
L = np.linalg.cholesky(np.array([[4.0, 0.0], [0.0, 0.25]]))  # anisotropic covariance
C1 = rng.normal(size=(200, 2)) @ L.T + np.array([0.0, 0.0])
C2 = rng.normal(size=(200, 2)) @ L.T + np.array([3.0, 3.0])

m1, m2 = C1.mean(0), C2.mean(0)
SW = (C1 - m1).T @ (C1 - m1) + (C2 - m2).T @ (C2 - m2)        # within-class scatter
w_fisher = np.linalg.inv(SW) @ (m2 - m1)                      # Fisher's solution
w_naive = m2 - m1                                            # naive mean difference

def fisher_J(w):
    w = w / np.linalg.norm(w); y1, y2 = C1 @ w, C2 @ w
    return (y2.mean() - y1.mean()) ** 2 / (y1.var() * len(y1) + y2.var() * len(y2))

print(f"Fisher criterion J, Fisher's w = S_W^-1 (m2-m1) : {fisher_J(w_fisher):.3f}")
print(f"Fisher criterion J, naive    w = m2 - m1        : {fisher_J(w_naive):.3f}")
print("\nFisher's direction maximizes between/within separation:",
      fisher_J(w_fisher) > fisher_J(w_naive))
```

</PyRunner>

---
layout: prism
heading: 퍼셉트론 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [퍼셉트론(Perceptron)]{.hl} 알고리즘은 선형 판별 모델의 또 다른 예로, 고정된 비선형 변환을 활용하여 입력 벡터 $\mathbf{x}$를 특징 벡터 $\boldsymbol{\phi}(\mathbf{x})$로 표현합니다:

$$
y(\mathbf{x})=f(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}))
$$

- 여기서 [비선형 활성화 함수(nonlinear activation function)]{.hl} $f(\cdot)$는 일반적으로 다음 형태를 갖습니다:

$$
f(a)= \begin{cases}+1 & a \geqslant 0 \\ -1 & a<0\end{cases}
$$

<div class="sub-item">

확률 모델에서는 $t\in\{0,1\}$을 사용하지만, 여기서는 $\{-1,1\}$을 사용한다는 점에 유의하세요.

</div>

---
layout: prism
heading: 퍼셉트론 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 퍼셉트론에서는 [퍼셉트론 기준(perceptron criterion)]{.hl}이 널리 사용되는 오차 함수입니다:

$$
E_P(\mathbf{w})=-\sum_{n \in \mathcal{M}} \mathbf{w}^{\top} \boldsymbol{\phi}_n t_n
$$

<div class="sub-item">

$\boldsymbol{\phi}_n=\boldsymbol{\phi}(\mathbf{x}_n)$이고 $\mathcal{M}$은 오분류된 패턴의 집합을 의미합니다.

</div>

- 오차 함수에 확률적 경사 하강법을 적용하면 다음을 얻습니다:

$$
\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}-\eta \nabla E_{\mathrm{P}}(\mathbf{w})=\mathbf{w}^{(\tau)}+\eta \boldsymbol{\phi}_n t_n
$$

---
layout: prism
heading: 퍼셉트론 (3/3)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(2)
A = rng.normal([-2, -2], 1.0, size=(40, 2))
B = rng.normal([2, 2], 1.0, size=(40, 2))
X = np.vstack([A, B]); t = np.array([-1] * 40 + [1] * 40)    # perceptron targets in {-1, +1}
Phi = np.column_stack([np.ones(len(X)), X])                  # augmented features [1, x]

w = np.zeros(3); eta = 1.0
for epoch in range(1, 101):
    mis = (Phi @ w) * t <= 0
    if not mis.any():
        break
    for i in np.where(mis)[0]:
        w = w + eta * Phi[i] * t[i]                          # w <- w + eta * phi_n * t_n

pred = np.sign(Phi @ w)
print(f"Converged in {epoch} epochs")
print(f"Misclassified at the end = {int((pred != t).sum())}")
print(f"Training accuracy = {np.mean(pred == t):.3f}")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">판별 함수</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">확률적 생성 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">연속 입력</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">최대가능도 해</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률적 판별 모델</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">라플라스 근사</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">베이지안 로지스틱 회귀</span></p>
  </div>

</div>

---
layout: prism
heading: 확률적 생성 모델 (1/2)
---
<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>
- 분류에 대한 확률적 접근법은 단순히 데이터 분포를 가정하고 선형 결정 경계 모델을 유도합니다.

- 더 구체적으로는, 클래스별 조건부 분포 $p(\mathbf{x}|\mathcal{C}_k)$와 각 클래스의 사전분포 $p(\mathcal{C}_k)$를 모델링하고, 베이즈 정리를 수행하여 최종적으로 사후분포 $p(\mathcal{C}_k|\mathbf{x})$를 얻습니다.

- 이진 경우에 대해, $\mathcal{C}_1$의 사후분포를 다음과 같이 추정할 수 있습니다:

$$
\begin{gathered}
p(\mathcal{C}_1 | \mathbf{x})  =\frac{p(\mathbf{x} | \mathcal{C}_1) p(\mathcal{C}_1)}{p(\mathbf{x} | \mathcal{C}_1) p(\mathcal{C}_1)+p(\mathbf{x} | \mathcal{C}_2) p(\mathcal{C}_2)}=\frac{1}{1+\exp (-a)}=\sigma(a),\quad a=\ln \frac{p(\mathbf{x} | \mathcal{C}_1) p(\mathcal{C}_1)}{p(\mathbf{x} | \mathcal{C}_2) p(\mathcal{C}_2)}\\
\sigma(a)=\frac{1}{1+\exp (-a)}
\end{gathered}
$$

<div class="sub-item">

$\sigma(\cdot)$는 [로지스틱 시그모이드(logistic sigmoid)]{.hl} 함수입니다.

</div>

---
layout: prism
heading: 확률적 생성 모델 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 로지스틱 시그모이드 함수는 다음을 만족합니다:

$$
\sigma(-a)=1-\sigma(a)
$$

- 로지스틱 시그모이드의 역함수는 [로짓(logit)]{.hl} 함수라고 하며 다음과 같이 정의됩니다:

$$
a=\ln\left(\frac{\sigma}{1-\sigma}\right)
$$

- $K>2$ 클래스에 대해서는 로지스틱 시그모이드의 일반화된 버전인 [정규화 지수 함수(normalized exponential function)]{.hl}, 즉 [소프트맥스 함수(softmax function)]{.hl}를 사용했습니다.

$$
\begin{aligned}
p(\mathcal{C}_k | \mathbf{x})&=\frac{p(\mathbf{x} | \mathcal{C}_k) p(\mathcal{C}_k)}{\sum_j p(\mathbf{x} | \mathcal{C}_j) p\left(\mathcal{C}_j\right)}=\frac{\exp (a_k)}{\sum_j \exp (a_j)}\\
a_k&=\ln (p(\mathbf{x} | \mathcal{C}_k) p(\mathcal{C}_k))
\end{aligned}
$$

---
layout: prism
heading: 연속 입력
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 조건부 밀도가 가우시안이고 모든 클래스가 동일한 공분산 행렬을 공유한다고 가정하면, 다음을 얻습니다:

$$
p\left(\mathbf{x} | \mathcal{C}_k\right)=\frac{1}{(2 \pi)^{D / 2}} \frac{1}{|\boldsymbol{\Sigma}|^{1 / 2}} \exp \left\{-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_k)^{\top} \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_k)\right\}
$$

- 이진 클래스 경우에 대해, 최종적으로 다음을 얻습니다:

$$
\begin{gathered}
p(\mathcal{C}_1 | \mathbf{x})=\sigma(\mathbf{w}^{\top} \mathbf{x}+w_0)\\
\mathbf{w}=\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)\\
w_0=-\frac{1}{2} \boldsymbol{\mu}_1^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}_1+\frac{1}{2} \boldsymbol{\mu}_2^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}_2+\ln \frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}
\end{gathered}
$$

<div class="sub-item">

공분산이 공유된다는 가정 때문에 지수의 이차항이 사라지므로, 로지스틱 시그모이드의 입력 변수가 $\mathbf{x}$에 대해 선형이라는 점에 유의하세요.

</div>

---
layout: prism
heading: "NOTE: 연속 입력에 대한 이진 분류"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 이진 클래스 경우의 사후분포를 다시 살펴봅시다:

$$
p(\mathcal{C}_k|\mathbf{x})=\frac{p(\mathbf{x}|\mathcal{C}_k)p(\mathcal{C}_k)}{p(\mathcal{C}_1)p(\mathbf{x}|\mathcal{C}_1)+p(\mathcal{C}_2)p(\mathbf{x}|\mathcal{C}_2)},\quad k=1,2
$$

- 이제, 사후분포 분자에 로그를 취하면 다음을 정의할 수 있습니다:

$$
g_k(\mathbf{x})=\ln p(\mathbf{x}|\mathcal{C}_k)+\ln p(\mathcal{C}_k)
$$

<div class="sub-item">

그러면,

</div>

$$
g_1(\mathbf{x})-g_2(\mathbf{x})=\ln\frac{p(\mathbf{x}|\mathcal{C}_1)p(\mathcal{C}_1)}{p(\mathbf{x}|\mathcal{C}_2)p(\mathcal{C}_2)}=\ln\frac{p(\mathbf{x}|\mathcal{C}_1)}{p(\mathbf{x}|\mathcal{C}_2)}+\ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}
$$

---
layout: prism
heading: "NOTE: 연속 입력에 대한 이진 분류"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 위의 가우시안 조건부 밀도를 대입하면 다음을 얻을 수 있습니다:

$$
g_1(\mathbf{x})-g_2(\mathbf{x})=\ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}+\ln\frac{ \frac{1}{(2\pi)^{D/2}|\boldsymbol{\Sigma}|^{1/2}}\exp(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_1)^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_1)) }{\frac{1}{(2\pi)^{D/2}|\boldsymbol{\Sigma}|^{1/2}} \exp(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_2))}
$$

- 상수항을 무시하면:

$$
g_1(\mathbf{x})-g_2(\mathbf{x})=\ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)} - \frac{1}{2}[(\mathbf{x}-\boldsymbol{\mu}_1)^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_1)-(\mathbf{x}-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_2)]
$$

- 이제 대괄호 안쪽에 집중해봅시다.

---
layout: prism
heading: "NOTE: 연속 입력에 대한 이진 분류"
---

$$
\begin{aligned}
[(\mathbf{x}-\boldsymbol{\mu}_1)^\top&\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_1)-(\mathbf{x}-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_2)]\\
=&({\color{#4a6fa5}\mathbf{x}^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}}-2\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}+\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_1)\\
&-({\color{#4a6fa5}\mathbf{x}^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}}-2\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}+\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_2)\\
=&-2(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}+(\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_1-\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_2)
\end{aligned}
$$

- 최종적으로 다음을 얻습니다:

$$
\begin{aligned}
g_1(\mathbf{x})-g_2(\mathbf{x})&=-\frac{1}{2}[-2(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}+(\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_1-\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_2)] + \ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}\\
&=(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}\mathbf{x} -\frac{1}{2}\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_1+\frac{1}{2}\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_2+\ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}\\
&=\mathbf{w}^\top\mathbf{x} +w_0
\end{aligned}
$$

<div class="sub-item">

이 방법은 [선형 판별 분석(linear discriminant analysis)]{.hl}으로 알려져 있습니다.

</div>

---
layout: prism
heading: "NOTE: 연속 입력에 대한 이진 분류"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 다음에 유의하세요:

$$
\begin{aligned}
&g_1(\mathbf{x})-g_2(\mathbf{x})=\ln\frac{p(\mathbf{x}|\mathcal{C}_1)p(\mathcal{C}_1)}{p(\mathbf{x}|\mathcal{C}_2)p(\mathcal{C}_2)}=\ln\frac{p(\mathcal{C}_1|\mathbf{x})}{p(\mathcal{C}_2|\mathbf{x})}=\mathbf{w}^\top\mathbf{x} +w_0\\
\Rightarrow&\ \ln\frac{p(\mathcal{C}_1|\mathbf{x})}{p(\mathcal{C}_2|\mathbf{x})}=\mathbf{w}^\top\mathbf{x}+w_0\\
\Rightarrow&\ \ln\frac{p(\mathcal{C}_1|\mathbf{x})}{1-p(\mathcal{C}_1|\mathbf{x})}=\mathbf{w}^\top\mathbf{x}+w_0\qquad \text{로짓의 정의와 비교해보세요.}\\
\therefore&\ p(\mathcal{C}_1|\mathbf{x})=\frac{1}{1+\exp(-[\mathbf{w}^\top\mathbf{x}+w_0])}=\sigma(\mathbf{w}^\top\mathbf{x}+w_0)
\end{aligned}
$$

---
layout: prism
heading: 최대가능도 해
---

- 이진 클래스 경우에 대해, 데이터셋 $\{\mathbf{x}_n,t_n\}$과 사전확률 $p(\mathcal{C}_1)=\pi$가 주어졌다고 가정하면 다음을 얻습니다

$$
\begin{gathered}
p(\mathbf{x}_n, \mathcal{C}_1)=p(\mathcal{C}_1) p(\mathbf{x}_n | \mathcal{C}_1)=\pi \mathcal{N}(\mathbf{x}_n | \boldsymbol{\mu}_1, \boldsymbol{\Sigma})\\
p(\mathbf{x}_n, \mathcal{C}_2)=p(\mathcal{C}_2) p(\mathbf{x}_n | \mathcal{C}_2)=(1-\pi) \mathcal{N}(\mathbf{x}_n | \boldsymbol{\mu}_2, \boldsymbol{\Sigma})
\end{gathered}
$$

- 가능도 함수는 다음과 같이 주어집니다

$$
p\left(\boldsymbol{\mathsf{t}}, \mathbf{X} | \pi, \boldsymbol{\mu}_1, \boldsymbol{\mu}_2, \boldsymbol{\Sigma}\right)=\prod_{n=1}^N\left[\pi \mathcal{N}\left(\mathbf{x}_n | \boldsymbol{\mu}_1, \boldsymbol{\Sigma}\right)\right]^{t_n}\left[(1-\pi) \mathcal{N}\left(\mathbf{x}_n | \boldsymbol{\mu}_2, \boldsymbol{\Sigma}\right)\right]^{1-t_n}
$$

<div class="sub-item">

$\boldsymbol{\mathsf{t}}=(t_1,\ldots,t_N)^\top$.

</div>

- 로그가능도를 미분하면 다음을 얻습니다:

$$
\pi=\frac{1}{N} \sum_{n=1}^N t_n=\frac{N_1}{N}=\frac{N_1}{N_1+N_2}\quad\Rightarrow\quad\boldsymbol{\mu}_1=\frac{1}{N_1} \sum_{n=1}^N t_n \mathbf{x}_n
$$

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">판별 함수</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률적 생성 모델</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">확률적 판별 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">고정 기저 함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">로지스틱 회귀</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">반복 재가중 최소제곱</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">라플라스 근사</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">베이지안 로지스틱 회귀</span></p>
  </div>

</div>

---
layout: prism
heading: 확률적 판별 모델
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 판별 함수나 확률적 생성 모델 대신, 선형 분류 모델의 일반화된 형태를 명시적으로 정의하고 그 매개변수를 획득할 수 있습니다.

<div class="sub-item">

해를 계산하는 데 널리 사용되는 효율적인 알고리즘으로 [반복 재가중 최소제곱(iterative reweighted least squares; IRLS)]{.hl}이 있습니다.

</div>

- 생성 모델은 클래스 조건부 밀도와 사전분포를 활용하여 베이즈 정리로 매개변수를 탐색합니다.

- 생성 모델과 달리, [판별 모델(discriminative models)]{.hl}은 조건부 분포 $p(\mathcal{C}_k|\mathbf{x})$로 정의된 가능도 함수를 직접 최대화합니다.

<div class="sub-item">

대체로 판별 모델은 더 적은 하이퍼파라미터를 필요로 하며, 클래스 조건부 밀도에 대한 가정이 실제 분포를 근사하는 데 실패하는 경우에도 종종 잘 일반화됩니다.

</div>

---
layout: prism
heading: 고정 기저 함수
---

- 적절히 선택된 기저 함수 $\boldsymbol{\phi}(\cdot)$는 사후분포 모델링 성능을 높일 수 있습니다.

<div class="img-row" style="max-width: 70%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.12a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.12b.png"/>

</div>

---
layout: prism
heading: 로지스틱 회귀 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 이진 클래스 분류에서, 클래스 $\mathcal{C}_1$의 사후분포를 특징 벡터의 선형 함수에 대한 로지스틱 회귀 함수로 쓸 수 있습니다:

$$
p(\mathcal{C}_1 | \boldsymbol{\phi})=y(\boldsymbol{\phi})=\sigma(\mathbf{w}^{\top} \boldsymbol{\phi})
$$

<div class="sub-item">

앞서 유도한 사후분포 $p(\mathcal{C}_1|\mathbf{x})=\sigma(\mathbf{w}^\top\mathbf{x}+w_0)$를 상기하세요.

</div>

<div class="sub-item">

이 모델은 [로지스틱 회귀(logistic regression)]{.hl}로 알려져 있습니다.

</div>

- 로지스틱 회귀 모델은 $M$차원 특징 공간 $\boldsymbol{\phi}$에 대해 $M$개의 매개변수만 필요로 합니다.

---
layout: prism
heading: 로지스틱 회귀 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 가능도 함수를 다음과 같이 정의합니다:

$$
p(\boldsymbol{\mathsf{t}} | \mathbf{w})=\prod_{n=1}^N y_n^{t_n}\left(1-y_n\right)^{1-t_n}
$$

<div class="sub-item">

$\boldsymbol{\mathsf{t}}=(t_1,\ldots,t_N)^\top$이고 $y_n=p(\mathcal{C}_1|\boldsymbol{\phi}_n)$입니다.

</div>

- 오차 함수로 음의 로그가능도를 사용하며, 이를 [교차 엔트로피(cross entropy)]{.hl}라고 합니다:

$$
E(\mathbf{w})=-\ln p( \boldsymbol{\mathsf{t}} | \mathbf{w})=-\sum_{n=1}^N\left\{t_n \ln y_n+\left(1-t_n\right) \ln \left(1-y_n\right)\right\}
$$

<div class="sub-item">

$y_n=\sigma(a_n)$이고 $a_n=\mathbf{w}^\top\boldsymbol{\phi}_n$입니다.

</div>

<div class="subsub-item">

기울기는 다음과 같이 계산됩니다: $\nabla E(\mathbf{w})=\sum_{n=1}^N\left(y_n-t_n\right) \boldsymbol{\phi}_n$.

</div>

---
layout: prism
heading: 반복 재가중 최소제곱 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 로지스틱 회귀는 비선형성을 가지므로, 그 해가 닫힌 형태가 아닐 수 있습니다.

- 이러한 종류의 문제를 풀기 위해, [뉴턴–랩슨(Newton–Raphson)]{.hl} 방법이라 불리는 IRLS 알고리즘을 사용합니다:

$$
\mathbf{w}^{(\mathrm {new})}=\mathbf{w}^{(\mathrm {old})}-\mathbf{H}^{-1} \nabla E(\mathbf{w})
$$

<div class="sub-item">

$\mathbf{H}$는 헤세 행렬이며, 각 원소는 $\mathbf{w}$의 각 성분에 대한 $E(\mathbf{w})$의 이계도함수입니다.

</div>

- 로지스틱 회귀 교차 엔트로피의 헤세 행렬은 다음과 같이 계산할 수 있습니다:

$$
\begin{aligned}
\nabla E(\mathbf{w})&=\sum_{n=1}^N(y_n-t_n) \boldsymbol{\phi}_n=\boldsymbol{\Phi}^{\top}(\boldsymbol{\mathsf{y}}-\boldsymbol{\mathsf{t}})\\
\mathbf{H}&=\nabla \nabla E(\mathbf{w})=\sum_{n=1}^N y_n(1-y_n) \boldsymbol{\phi}_n \boldsymbol{\phi}_n^{\top}=\boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\Phi}
\end{aligned}
$$

<div class="sub-item">

$\mathbf{R}$은 $N\times N$ 대각 행렬이고 $R_{nn}=y_n(1-y_n)$입니다.

</div>

---
layout: prism
heading: 반복 재가중 최소제곱 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

- 로지스틱 회귀에 대한 뉴턴–랩슨 갱신은 다음과 같습니다:

$$
\begin{aligned}
\mathbf{w}^{(\mathrm{new})} & =\mathbf{w}^{(\mathrm{old})}-(\boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\Phi})^{-1} \boldsymbol{\Phi}^{\top}(\boldsymbol{\mathsf{y}}-\boldsymbol{\mathsf{t}})\\
& =(\boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\Phi})^{-1}(\boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\Phi} \mathbf{w}^{\mathrm {(old})}-\boldsymbol{\Phi}^{\top}(\boldsymbol{\mathsf{y}}-\boldsymbol{\mathsf{t}}))\\
& =(\boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\Phi})^{-1} \boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\mathsf{z}}
\end{aligned}
$$

<div class="sub-item">

$\boldsymbol{\mathsf{z}}$는 $N$차원 벡터이며 다음과 같이 정의됩니다:

</div>

$$
\boldsymbol{\mathsf{z}} = \boldsymbol{\Phi} \mathbf{w}^{\mathrm{(old)}} - \mathbf{R}^{-1}(\boldsymbol{\mathsf{y}}-\boldsymbol{\mathsf{t}})
$$

---
layout: prism
heading: 반복 재가중 최소제곱 (3/3)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(3)
G0 = rng.normal([-1, 0], 1.3, size=(100, 2))                 # overlapping (non-separable) classes
G1 = rng.normal([1.5, 0.5], 1.3, size=(100, 2))
X = np.vstack([G0, G1]); t = np.array([0.0] * 100 + [1.0] * 100)
Phi = np.column_stack([np.ones(len(X)), X])

sigmoid = lambda a: 1.0 / (1.0 + np.exp(-a))
def nll(w):
    y = np.clip(sigmoid(Phi @ w), 1e-12, 1 - 1e-12)
    return -np.sum(t * np.log(y) + (1 - t) * np.log(1 - y))

w = np.zeros(3)
print(f"{'iter':>4} | {'neg-log-likelihood':>18} | {'||gradient||':>12}")
for it in range(6):
    y = sigmoid(Phi @ w)
    R = np.diag(y * (1 - y))
    grad = Phi.T @ (y - t)
    z = Phi @ w - np.linalg.solve(R + 1e-8 * np.eye(len(R)), y - t)  # z = Phi w - R^-1 (y - t)
    w = np.linalg.solve(Phi.T @ R @ Phi, Phi.T @ R @ z)            # w = (Phi^T R Phi)^-1 Phi^T R z
    print(f"{it:>4} | {nll(w):>18.4f} | {np.linalg.norm(grad):>12.3e}")

print(f"\nNewton-Raphson drives the gradient to ~0; accuracy = "
      f"{np.mean((sigmoid(Phi @ w) >= 0.5) == (t == 1)):.3f}")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">판별 함수</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률적 생성 모델</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률적 판별 모델</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">라플라스 근사</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">베이지안 로지스틱 회귀</span></p>
  </div>

</div>

---
layout: prism
heading: 라플라스 근사
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [라플라스 근사(Laplace approximation)]{.hl}는 연속 변수의 임의의 확률밀도에 대한 가우시안 근사를 위해 사용됩니다.

- 연속 확률변수 $z\sim p(z)$에 대해, 라플라스 근사는 $p(z)$의 최빈값을 중심으로 하는 가우시안 근사 $q(z)$를 찾습니다.

<div class="sub-item-enum">

1. 먼저 최빈값 $z_0$를 찾습니다, 즉 최대사후확률(MAP)을 찾습니다.
2. 로그 확률밀도의 2차 테일러 전개를 유도합니다.
3. 지수를 취하여 가우시안 형태의 함수를 얻습니다.
4. 완전제곱식을 통해 $q(z)$의 평균과 분산을 얻을 수 있습니다.

</div>

---
layout: prism
heading: "NOTE: 라플라스 근사"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- $p(z)\sim\exp(-z^2-z^4)$에 대해 라플라스 근사를 수행해봅시다.

<div class="sub-item-enum">

1. $\dfrac{\mathrm{d}p(z)}{\mathrm{d}z}\big|_{z=z_0}=(-2z-4z^3)\exp(-z^2-z^4)\big|_{z=z_0}=0\Rightarrow z_0=0$

<div class="subsub-item">

여기서 최빈값은 $z_0=0$입니다.

</div>

2. $\ln p(z)\simeq \ln p(z_0)-\dfrac{1}{2}\left(-\dfrac{\mathrm{d}^2}{\mathrm{d}z^2}\ln p(z)\big|_{z=z_0}\right)(z-z_0)^2=0-\dfrac{1}{2}(-(-2-12z^2)|_{z=z_0})(z-0)^2$
3. $\ln q(z)=-z^2$
4. $\therefore q(z)=\exp(-(z-0)^2)\sim\mathcal{N}(z|0,\tfrac{1}{2})$

</div>

---
layout: prism
heading: "NOTE: 라플라스 근사"
---

<PyRunner>

```python
import numpy as np

f = lambda z: np.exp(-z**2 - z**4)                           # unnormalized density
lnp = lambda z: -z**2 - z**4
zz = np.linspace(-3, 3, 600001)

z0 = zz[np.argmax(f(zz))]                                    # 1) mode by grid search
h = 1e-4
A = -(lnp(z0 + h) - 2 * lnp(z0) + lnp(z0 - h)) / h**2        # 2) curvature A = -d^2/dz^2 ln p
q = lambda z: np.exp(-z**2) / np.sqrt(np.pi)                 # Laplace q = N(0, 1/2)
lnq_curv = -(np.log(q(z0 + h)) - 2 * np.log(q(z0)) + np.log(q(z0 - h))) / h**2

print(f"Mode z0 (grid argmax)           = {z0:.4f}   (slide: 0)")
print(f"Curvature A = -d^2/dz^2 ln p|z0 = {A:.4f}   (analytic 2 + 12*z0^2 = {2 + 12 * z0**2:.1f})")
print(f"Laplace variance = 1/A          = {1 / A:.4f}   (slide: 1/2)")
print(f"\nLaplace matches the curvature at the mode: "
      f"ln q curvature {lnq_curv:.3f} == A {A:.3f}")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">판별 함수</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률적 생성 모델</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률적 판별 모델</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">라플라스 근사</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">베이지안 로지스틱 회귀</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">사후분포 추정</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">예측 분포</span></p>
  </div>

</div>

---
layout: prism
heading: 사후분포 추정 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 베이지안 로지스틱 회귀에서는 사전분포와 가능도 함수의 곱을 정규화하여 사후분포를 추정해야 합니다.

<div class="sub-item">

여기서 각 데이터포인트는 로지스틱 시그모이드 함수를 가지므로, 가능도 함수가 복잡해집니다.

</div>

- 베이지안 로지스틱 회귀 문제에 대해 라플라스 근사를 수행할 수 있습니다.

- 다음과 같은 가우시안 사전분포를 정의합니다:

$$
p(\mathbf{w})=\mathcal{N}(\mathbf{w}|\mathbf{m}_0,\mathbf{S}_0)
$$

<div class="sub-item">

그러면 사후분포는 다음과 같이 됩니다

</div>

$$
p(\mathbf{w}|\boldsymbol{\mathsf{t}})\propto p(\mathbf{w})p(\boldsymbol{\mathsf{t}}|\mathbf{w})
$$

---
layout: prism
heading: 사후분포 추정 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 로그를 취하고 사전분포와 가능도 함수를 대입하면 다음을 얻습니다:

$$
\begin{aligned}
\ln p(\mathbf{w} | \boldsymbol{\mathsf{t}})= & -\frac{1}{2}\left(\mathbf{w}-\mathbf{m}_0\right)^{\top} \mathbf{S}_0^{-1}\left(\mathbf{w}-\mathbf{m}_0\right)\\
& +\sum_{n=1}^N\left\{t_n \ln y_n+\left(1-t_n\right) \ln \left(1-y_n\right)\right\}+\text {const }
\end{aligned}
$$

<div class="sub-item">

$y_n=\sigma(\mathbf{w}^\top\boldsymbol{\phi}_n)$.

</div>

- 최종적으로, 라플라스 근사를 수행하면 사후분포의 가우시안 근사를 다음과 같이 얻을 수 있습니다:

$$
q(\mathbf{w})=\mathcal{N}\left(\mathbf{w} | \mathbf{w}_{\mathrm{MAP}}, \mathbf{S}_N\right)
$$

---
layout: prism
heading: 예측 분포
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 새로운 특징 벡터 $\boldsymbol{\phi}(\mathbf{x})$에 대해, $q(\mathbf{w})$를 사용하여 사후분포를 근사할 수 있습니다:

$$
\begin{aligned}
p(\mathcal{C}_1 | \boldsymbol{\phi}, \boldsymbol{\mathsf{t}})&=\int p(\mathcal{C}_1 | \boldsymbol{\phi}, \mathbf{w}) p(\mathbf{w} | \boldsymbol{\mathsf{t}}) \mathrm{~d} \mathbf{w} \simeq \int \sigma(\mathbf{w}^{\top} \boldsymbol{\phi}) q(\mathbf{w}) \mathrm{~d} \mathbf{w}\\
&\simeq\int \sigma(a) \mathcal{N}(a | \mu_a, \sigma_a^2) \mathrm{~d} a
\end{aligned}
$$

<div class="sub-item">

$a=\mathbf{w}^\top\boldsymbol{\phi}$이고

</div>

$$
\begin{aligned}
\mu_a&=\mathbb{E}[a]=\int p(a) a \mathrm{~d} a=\int q(\mathbf{w}) \mathbf{w}^{\top} \boldsymbol{\phi} \mathrm{~d} \mathbf{w}=\mathbf{w}_{\mathrm{MAP}}^{\top} \boldsymbol{\phi}\\
\sigma_a^2&=\operatorname{var}[a]=\int p(a)\{a^2-\mathbb{E}[a]^2\} \mathrm{~d} a=\boldsymbol{\phi}^{\top} \mathbf{S}_N \boldsymbol{\phi}
\end{aligned}
$$

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}