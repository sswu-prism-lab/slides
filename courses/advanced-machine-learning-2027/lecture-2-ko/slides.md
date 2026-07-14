---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff' # Sets a custom hex background color
title: AML - Lecture 2 (KO)
download: true
info: |
  ## 고급 기계학습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-2/
---

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.jpeg" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">고급 기계학습</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">2주차: 강좌 소개</p>

  <p style="color:#1a1a2e; font-size: 1.5rem; margin-top: 5rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div style="color:#1a1a2e; margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p style="color:#1a1a2e; font-size: 1.25rem; margin-top: 2.5rem;">2027년 봄학기</p>
</div>

---
layout: prism
heading: 강좌 일정
---

<div class="absolute left-10 right-10" style="top: 1rem; bottom: 5rem; display: grid; grid-template-columns: 1fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">강좌 소개</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#111;">예비 지식</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">확률 분포</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">선형 회귀 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">선형 분류 모델</span></p>
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
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">서론</span></p>
    <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">서론</span></p>
    <p style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">다항식 곡선 피팅</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률론</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">모델 선택 및 차원의 저주</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">결정 이론</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">정보 이론</span></p>
  </div>

</div>

---
layout: prism
heading: 서론
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 주어진 데이터로부터 패턴을 인식하는 것은 우리가 마주한 가장 중요한 문제 중 하나입니다.

- 인류는 패턴 인식 문제를 해결하기 위한 답을 오랫동안 추구해왔으며, 많은 경우에서 의미 있는 패턴을 성공적으로 찾아냈습니다.

- 요하네스 케플러(Johannes Kepler)는 16세기에 티코 브라헤(Tycho Brahe)가 관측한 방대한 천문 데이터로부터 케플러의 행성 운동 법칙을 발견했습니다.


---
layout: prism
heading: 다항식 곡선 피팅 (1/4)
---

- 다음과 같은 [회귀(regression)]{.hl} 문제를 생각해봅시다.

$$
y(x, \mathbf{w})=w_0 + w_1 x + w_2 x^2 + \cdots + w_M x^M = \sum_{j=0}^{M} w_j x^j
$$

<div class="sub-item">

$M$은 다항식의 [차수(order)]{.hl}를 나타내고, 벡터 $\mathbf{w}$는 다항식의 계수 $w_0,...,w_M$을 나타냅니다.

</div>

<div class="sub-item">

다항 함수 $y(x, \mathbf{w})$는 $x$에 대해서는 비선형이지만, $\mathbf{w}$에 대해서는 선형입니다.

</div>

<div style="height: 0.7rem;"></div>

- 주어진 [학습 데이터(training data)]{.hl}에 다항식 $y(x, \mathbf{w})$를 [피팅(fitting)]{.hl}함으로써 계수를 결정할 수 있습니다.
  - 이를 위해, 학습 데이터셋의 목표값 $t$와 함수값 $y(x,\mathbf{w})$ 사이의 오차를 추정하는 [오차 함수(error function)]{.hl}를 정의하고, 이 오차를 최소화하여 계수를 피팅합니다.

$$
E(\mathbf{w})=\frac{1}{2}\sum_{n=1}^N \{ y(x_n, \mathbf{w}) - t_n \}^2
$$

<div class="sub-item">

이 함수는 항상 양의 값을 반환하며, 함수값이 목표값과 정확히 같을 경우 $0$이 될 수 있습니다.

</div>

---
layout: prism
heading: 다항식 곡선 피팅 (2/4)
---

- 문제를 풀기 위해 $E(\mathbf{w})$를 최소화하는 $\mathbf{w}$를 선택할 수 있습니다.
  - 오차 함수가 이차 형태(quadratic form)를 갖기 때문에, 계수에 대해 함수를 미분함으로써 유일한 $\mathbf{w}^\star$를 구할 수 있다는 점에 유의하세요.

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.3.png" class="img-center" style="height: 15rem;" />

---
layout: prism
heading: 다항식 곡선 피팅 (3/4)
---

- 여전히 차수 $M$을 결정하는 문제가 남아있으며, 이는 [모델 선택(model selection)]{.hl} 문제로 알려져 있습니다.

- 상수 함수($M = 0$)나 선형 함수($M = 1$)는 잘 피팅되지 않지만, 3차 함수($M = 3$)는 잘 피팅된다는 점에 유의하세요.
  - 더 높은 차수($M = 9$)에서는 함수가 학습 집합에 정확히 맞춰질 수 있으며, 이 경우 $E(\mathbf{w}^\star) = 0$을 얻게 됩니다.
  - 하지만 곡선이 심하게 진동하여 삼각함수를 제대로 표현하지 못하며, 이러한 현상을 [과적합(overfitting)]{.hl}이라고 합니다.

<div style="height: 0.1rem;"></div>

<div class="img-row" style="max-width: 90%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.4a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.4b.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.4c.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.4d.png"/>

</div>

---
layout: prism
heading: 다항식 곡선 피팅 (4/4)
---

- 과적합 문제를 해결하기 위해 [정규화(regularization)]{.hl} 기법이 널리 사용됩니다.
  - 정규화를 위해, 계수의 크기를 억제하도록 오차 함수에 벌점항(penalty term)을 추가하는 것을 고려할 수 있습니다.

$$
\tilde{E}(\mathbf{w})=\frac{1}{2}\sum_{n=1}^N \{ y(x_n, \mathbf{w}) - t_n \}^2 + \frac{\lambda}{2}\|\mathbf{w}\|^2
$$

<div class="subsub-item">

$\|\mathbf{w}\|^2 \equiv \mathbf{w}^\top \mathbf{w} = w_0^2 + w_1^2 + \cdots + w_M^2$

</div>

<div style="height: 1.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.7a.png" style="float: right; width: 12rem; margin: 1rem 0rem 0 0rem;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.7b.png" style="float: right; width: 12rem; margin: 1rem 1rem 0 1.5rem;" />

- $\lambda$는 정규화 항의 상대적인 영향을 조절합니다.

- 이 정규화 기법은 축소법(shrinkage method) 또는 [릿지 회귀(ridge regression)]{.hl}로 알려져 있습니다.

<div class="subsub-item">

신경망의 관점에서는 이를 [가중치 감쇠(weight decay)]{.hl}라고 합니다.

</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 0rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">서론</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">확률론</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">기본 법칙</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">확률 밀도</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">기댓값과 공분산</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">베이지안 확률</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">가우시안 분포</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">곡선 피팅</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">베이지안 곡선 피팅</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">모델 선택 및 차원의 저주</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">결정 이론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">정보 이론</span></p>
  </div>

</div>

---
layout: prism
heading: 확률론 (1/3)
---

<div class="theorem-box">

<div class="theorem-box-title">확률의 기본 법칙</div>

<div class="theorem-box-body">

$p(X, Y)$를 $X$와 $Y$의 [결합확률(joint probability)]{.hl}, $p(Y|X)$를 $X$가 주어졌을 때 $Y$의 [조건부확률(conditional probability)]{.hl}, $p(X)$를 $X$의 주변확률(marginal probability)이라고 하면, 다음 법칙들이 성립합니다.

_합의 법칙 (Sum rule)_

$$
p(X) = \sum_Y p(X,Y)
$$

_곱의 법칙 (Product rule)_

$$
p(X,Y) = P(Y|X)P(X)
$$

</div>
</div>

---
layout: prism
heading: 확률론 (2/3)
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

joint = np.array([
    [0.10, 0.05],
    [0.20, 0.15],
    [0.30, 0.20],
])

p_X = joint.sum(axis=1)
print("p(x) estimated by Sum rule:", p_X)

p_Y_given_X = joint / p_X[:, None]
reconstructed = p_Y_given_X * p_X[:, None]
print("Product rule check:", np.allclose(joint, reconstructed))
```

</PyRunner>

---
layout: prism
heading: 확률론 (3/3)
---

- 곱의 법칙과 대칭성 $P(X, Y) = P(Y, X)$로부터 [베이즈 정리(Bayes' theorem)]{.hl}를 유도할 수 있습니다.

$$
P(Y | X) = \frac{P(X | Y)P(Y)}{P(X)}
$$

<div class="subsub-item">

여기서 $P(Y)$는 $X$를 관측하기 전의 확률인 [사전확률(prior probability)]{.hl}, $P(Y | X)$는 $X$를 관측한 후의 확률인 [사후확률(posterior probability)]{.hl}로 알려져 있습니다.

</div>

<PyRunner>

```python
import numpy as np

joint = np.array([[0.10, 0.05], [0.20, 0.15], [0.30, 0.20],])

p_X = joint.sum(axis=1)      # p(X)
p_Y = joint.sum(axis=0)      # p(Y)

p_X_given_Y = joint / p_Y[None, :]   # p(X|Y)
p_Y_given_X = joint / p_X[:, None]   # p(Y|X) (direct calculation)

p_Y_given_X_bayes = (p_X_given_Y * p_Y[None, :]) / p_X[:, None] # Bayes' theorem: p(Y|X) = p(X|Y) * p(Y) / p(X)

# print("Results of P(Y|X):", p_Y_given_X, p_Y_given_X_bayes)
print("Bayes' theorem check: ", np.allclose(p_Y_given_X, p_Y_given_X_bayes))
```

</PyRunner>

---
layout: prism
heading: 확률 밀도
---


- 연속 공간에서, 실수 변수 $x \in (x, x + \delta x)$가 존재하고 $\delta x \rightarrow 0$일 때 그 확률이 $p(x) \delta x$로 주어진다면, $p(x)$를 $x$의 [확률밀도(probability density)]{.hl}라고 합니다.
  - 확률밀도에 대해서는 다음이 성립합니다.

$$
p(x \in (a, b)) = \int_a^b p(x)\, \mathrm{d}x\\
p(x) \geq 0,\quad \int_{-\infty}^{\infty} p(x)\, \mathrm{d}x = 1
$$

<div style="height: 1.5rem;"></div>

- [누적분포함수(cumulative distribution function)]{.hl}는 $x$가 $(-\infty, z)$ 범위에 있을 확률을 나타냅니다.

$$
P(z) = \int_{-\infty}^z p(x)\, \mathrm{d}x
$$

<div class="sub-item">

$x$가 이산 변수인 경우, $p(x)$는 흔히 [확률질량함수(probability mass function)]{.hl}라고 불립니다.

</div>

---
layout: prism
heading: 기댓값과 공분산 (1/2)
---

- 확률밀도 $p(x)$ 하에서, 함수 $f(x)$의 평균 $\mathbb{E}[f]$를 [기댓값(expectation)]{.hl}이라고 합니다.
  - 이산 분포의 경우, 기댓값은 다음과 같이 정의됩니다:

$$
\mathbb{E}[f] = \sum_x p(x)f(x)
$$

<div class="sub-item">

연속 분포의 경우, 기댓값은 다음과 같습니다:

</div>

$$
\mathbb{E}[f] = \int p(x)f(x)\, \mathrm{d}x
$$

- $N$개의 데이터 포인트가 주어졌을 때, 기댓값을 다음과 같이 근사할 수 있습니다:

$$
\mathbb{E}[f] \approx \frac{1}{N}\sum_{n=1}^N f(x_n)
$$

- [조건부 기댓값(conditioned expectation)]{.hl}도 유사한 방식으로 추정할 수 있습니다.

---
layout: prism
heading: 기댓값과 공분산 (2/2)
---

- $f(x)$의 [분산(variance)]{.hl}은 다음과 같이 정의됩니다:

$$
\begin{aligned}
\operatorname{var}[f]&=\mathbb{E}[ (f(x)-\mathbb{E}[f(x)])^2 ]\\ 
&=\mathbb{E}[f(x)^2]-\mathbb{E}[f(x)]^2
\end{aligned}
$$

- 두 변수 $x$와 $y$에 대해, 이들의 [공분산(covariance)]{.hl}은 다음과 같이 정의됩니다:

$$
\begin{aligned}
\operatorname{cov}[x, y]&=\mathbb{E}_{x,y}[\{x-\mathbb{E}[x]\}\{y-\mathbb{E}[y]\}]\\
&=\mathbb{E}_{x,y}[xy]-\mathbb{E}[x]\mathbb{E}[y]
\end{aligned}
$$

<div class="sub-item">

공분산은 $x$와 $y$의 값이 얼마나 함께 변하는지를 나타내는 척도입니다.

</div>

<div class="sub-item">

변수가 벡터라면, 공분산은 행렬이 됩니다.

</div>

$$
\begin{aligned}
\operatorname{cov}[\mathbf{x}, \mathbf{y}]&=\mathbb{E}_{\mathbf{x}, \mathbf{y}}[ \{\mathbf{x}-\mathbb{E}[\mathbf{x}]\}\{\mathbf{y}^\top-\mathbb{E}[\mathbf{y}^\top]\} ]\\
&=\mathbb{E}_{\mathbf{x}, \mathbf{y}}[\mathbf{x}\mathbf{y}^\top]-\mathbb{E}[\mathbf{x}]\mathbb{E}[\mathbf{y}^\top]
\end{aligned}
$$

---
layout: prism
heading: 베이지안 확률 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 확률을 _"반복 가능한 무작위 사건이 발생하는 빈도"_로 해석하는 관점을 [빈도주의(frequentist)]{.hl} 또는 [고전적(classical)]{.hl} 관점이라고 합니다.

<div class="sub-item">

빈도주의 관점에서는 한 번도 관측되지 않은 경우에 대한 확률을 정의할 수 없습니다.

</div>

- 더 넓게는, [베이지안(Bayesian)]{.hl} 관점을 이용해 확률과 증거로 불확실성을 정량화할 수 있습니다.

- 다항식 곡선 피팅 예제에서, $\mathbf{w}$에 대한 우리의 가설을 나타내는 사전확률 $p(\mathbf{w})$와 관측 데이터 $\mathcal{D}$에 대한 조건부확률 $p(\mathcal{D}|\mathbf{w})$를 이용하여 베이즈 정리를 얻을 수 있습니다.

$$
p(\mathbf{w}|\mathcal{D})=\frac{p(\mathcal{D}|\mathbf{w})p(\mathbf{w})}{p(\mathcal{D})}
$$

---
layout: prism
heading: 베이지안 확률 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 베이지안 관점에서는 $\mathcal{D}$를 관측한 후의 $\mathbf{w}$에 대한 불확실성을 나타내기 위해 사후확률 $p(\mathbf{w}|\mathcal{D})$를 사용합니다.

- 베이즈 정리에서 $p(\mathcal{D}|\mathbf{w})$는 $\mathbf{w}$에 대한 함수이며, [가능도 함수(likelihood function)]{.hl}라고 불립니다.

<div class="sub-item">

가능도(likelihood)는 서로 다른 각 매개변수 하에서 관측된 데이터가 발생했을 _가능성이 얼마나 되는지_를 나타냅니다.

</div>

- 빈도주의 관점에서, [최대가능도(maximum likelihood)]{.hl}는 가장 널리 사용되는 추론 척도 중 하나입니다.

<div class="sub-item">

기계학습 문헌에서는 음의 로그가능도(negative log-likelihood)가 오차 함수로 자주 사용됩니다.

</div>

<div class="sub-item">

음의 로그가능도 함수는 단조 감소하므로, 가능도를 최대화하는 것은 오차를 최소화하는 것과 동일합니다.

</div>

---
layout: prism
heading: 가우시안 분포
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [정규분포(normal distribution)]{.hl}는 [가우시안 분포(Gaussian distribution)]{.hl}라고도 하며, 실수 변수 $x$에 대해 다음과 같이 정의됩니다:

$$
\mathcal{N}(x|\mu, \sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{ -\frac{1}{2\sigma^2}(x-\mu)^2 \right\}
$$

<div class="sub-item">

두 개의 하이퍼파라미터인 [평균(mean)]{.hl} $\mu$와 [분산(variance)]{.hl} $\sigma^2$가 분포를 제어합니다.

</div>

<div class="sub-item">

분산의 제곱근을 [표준편차(standard deviation)]{.hl}라고 합니다.

</div>

<div class="sub-item">

분산의 역수 $\beta=1/\sigma^2$를 [정밀도(precision)]{.hl}라고 합니다.

</div>

- 연속 변수 및 $D$차원 벡터 $\mathbf{x}$에 대해, 가우시안 분포는 다음과 같이 정의됩니다:

$$
\mathcal{N}(\mathbf{x}|\boldsymbol{\mu}, \boldsymbol{\Sigma}^2)=\frac{1}{(2\pi)^{D/2}}\frac{1}{|\boldsymbol{\Sigma}|^{1/2}}\exp\left\{ -\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}) \right\}
$$

<div class="sub-item">

$D$차원 벡터 $\boldsymbol{\mu}$는 평균이고, $D\times D$ 행렬 $\boldsymbol{\Sigma}$는 공분산이며, $|\boldsymbol{\Sigma}|$는 행렬식(determinant)입니다.

</div>

---
layout: prism
heading: 곡선 피팅 (1/4)
---

- 곡선 피팅의 목표는 $N$개의 관측값 $\boldsymbol{\mathsf{x}}=(x_1,\ldots,x_N)^\top$과 그에 대응하는 목표값 $\boldsymbol{\mathsf{t}}=(t_1,\ldots,t_N)^\top$이 주어졌을 때, 새롭게 주어진 입력 변수 $x$의 목표값 $t$를 추론하는 것입니다.

- 확률분포를 이용하면 목표값에 대한 불확실성을 나타낼 수 있습니다.
  - $x$에 대한 목표값이 평균 $y(x,\mathbf{w})$를 갖는 가우시안 분포를 따른다고 가정하면, 다음과 같은 조건부 분포를 유도할 수 있습니다.

$$
p(t|x,\mathbf{w},\beta)=\mathcal{N}(t|y(x,\mathbf{w}), \beta^{-1})
$$

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.16.png" class="img-center" style="width: 16rem;" />

---
layout: prism
heading: 곡선 피팅 (2/4)
---

- 학습 집합 $\{\boldsymbol{\mathsf{x}},\boldsymbol{\mathsf{t}}\}$을 이용한 최대가능도를 통해 $\mathbf{w}$와 $\beta$를 추정할 수 있습니다.

- 가능도 함수는 다음과 같이 유도됩니다:

$$
p(\boldsymbol{\mathsf{t}}|\boldsymbol{\mathsf{x}},\mathbf{w},\beta)=\prod_{n=1}^{N}\mathcal{N}(t_n|y(x_n,\mathbf{w}), \beta^{-1})
$$

- 가우시안 분포를 대입하고 로그를 취하여 로그가능도 함수를 얻습니다.

$$
\ln p(\boldsymbol{\mathsf{t}}|\boldsymbol{\mathsf{x}},\mathbf{w},\beta) = -\frac{\beta}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})- t_n\}^2+\frac{N}{2}\ln\beta-\frac{N}{2}\ln(2\pi)
$$

<div class="sub-item">

최대가능도 해 $\mathbf{w}_\mathrm{ML}$를 추정할 때는 마지막 두 항을 제외할 수 있습니다.

</div>

<div class="sub-item">

$\beta$는 무관하므로 $\beta/2$를 $1/2$로 대체할 수 있습니다.

</div>

<div class="sub-item">

원래의 로그가능도를 최대화하는 대신 음의 로그가능도를 최소화할 수 있습니다.

</div>

---
layout: prism
heading: 곡선 피팅 (3/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 추론을 위해, 확률적 모델을 고려하고 있으므로 $t$는 점 추정(point estimation)이 아니라 [예측 분포(predictive distribution)]{.hl}로 표현됩니다.

$$
p(t|x,\mathbf{w}_\text{ML},\beta_\text{ML})=\mathcal{N}(t|y(x,\mathbf{w}_\text{ML}),\beta_\text{ML}^{-1})
$$

- 여기서 $\mathbf{w}$의 사전확률을 도입할 수 있습니다.

<div class="sub-item">

단순화를 위해 다음과 같은 가우시안 분포를 사용합니다.

</div>

$$
p(\mathbf{w}|\alpha)=\mathcal{N}(\mathbf{w}|\mathbf{0},\alpha^{-1}\mathbf{I})=\left(\frac{\alpha}{2\pi}\right)^{(M+1)/2}\exp\left\{-\frac{\alpha}{2}\mathbf{w}^\top\mathbf{w}\right\}
$$

<div class="subsub-item">

$\alpha$는 정밀도이며 [하이퍼파라미터(hyperparameter)]{.hl}로 알려져 있고, $\mathbf{I}$는 단위행렬(identity matrix)입니다.

</div>

---
layout: prism
heading: 곡선 피팅 (4/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

- 베이즈 정리에 기반하여, $\mathbf{w}$의 사후확률은 다음과 같이 유도됩니다:

$$
p(\mathbf{w}|\mathbf{x}, \mathbf{t},\alpha,\beta)\propto p(\mathbf{t}|\mathbf{x},\mathbf{w},\beta)p(\mathbf{w}|\alpha)
$$

<div class="sub-item">

여기서 사후확률을 최대화함으로써 $\mathbf{w}$를 결정할 수 있으며, 이 기법을 [최대사후확률(maximum a posterior)]{.hl}이라고 합니다.

</div>

<div class="sub-item">

사후확률을 최대화하는 것은 다음 식을 최소화하는 것과 동일하다는 점에 유의하세요.

</div>

$$
\frac{\beta}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})-t_n\}^2+\frac{\alpha}{2}\mathbf{w}^\top\mathbf{w}
$$

- 따라서 최대사후확률은 정규화된 오차 함수를 최소화하는 것과 동일합니다.

---
layout: prism
heading: 베이지안 곡선 피팅 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

- 최대사후확률을 위해 사전확률 $p(\mathbf{w}|\alpha)$를 사용했지만, 여전히 $\mathbf{w}$를 점 추정하므로 완전한 베이지안 방법을 사용하는 것은 아닙니다.

<div class="sub-item">

기계학습 및 패턴 인식에서 베이지안 방법은 가능한 모든 $\mathbf{w}$에 대해 적분을 수행하여 $\mathbf{w}$를 _주변화(marginalize)_하는 데 사용됩니다.

</div>

- 예측 분포 $p(t|x,\boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}})$를 구하기 위해, 확률의 합의 법칙과 곱의 법칙을 순차적으로 적용할 수 있습니다.

$$
p(t|x, \boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}})=\int p(t|x, \mathbf{w})p(\mathbf{w}|\boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}})\,\mathrm{d}\mathbf{w}
$$

---
layout: prism
heading: 베이지안 곡선 피팅 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

- 적분 이후, 예측 분포는 가우시안 분포로 유도될 수 있습니다:

$$
p(t|x, \boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}})=\mathcal{N}(t|m(x),s^2(x))
$$

<div class="sub-item">

여기서 평균과 분산은 다음과 같습니다:

</div>

$$
\begin{aligned}
m(x)&=\beta \boldsymbol{\phi}(x)^\top\mathbf{S}\sum_{n=1}^{N}\boldsymbol{\phi}(x_n)t_n\\
s^2(x)&=\beta^{-1}+\boldsymbol{\phi}(x)^\top\mathbf{S}\boldsymbol{\phi}(x)\\
\mathbf{S}^{-1}&=\alpha\mathbf{I}+\beta\sum_{n=1}^{N}\boldsymbol{\phi}(x_n)\boldsymbol{\phi}(x_n)^\top
\end{aligned}
$$

---
layout: prism
heading: 목차
---
<div style="margin-top: 0rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">서론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률론</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">모델 선택 및 차원의 저주</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">모델 선택</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">차원의 저주</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">결정 이론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">정보 이론</span></p>
  </div>

</div>

---
layout: prism
heading: 모델 선택
---

- 과적합의 예시에서 볼 수 있듯이, 학습 집합에서의 좋은 성능이 반드시 좋은 예측 성능을 보장하지는 않습니다.

- 이 문제를 해결하기 위해, 최적의 모델과 매개변수를 선택하기 위한 [검증 데이터셋(validation dataset)]{.hl}을 나눕니다.

<div class="sub-item">

이 경우, 선택된 모델의 최종 성능을 검증하기 위해 [테스트 데이터셋(testing dataset)]{.hl}도 별도로 정의합니다.

</div>

- 검증을 위해 [$S$-겹 교차검증($S$-fold cross-validation)]{.hl}이 널리 사용됩니다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.18.png" class="img-center" style="width: 14rem;" />

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

---
layout: prism
heading: 차원의 저주
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 많은 응용에서 우리는 단일 변수 $x$가 아니라 고차원의 여러 변수를 고려해야 합니다.

- $D$개의 입력 변수가 있다고 가정하면, 곡선 피팅 문제를 위한 다항식의 3차 계수는 다음과 같이 유도될 수 있습니다:

$$
y(\mathbf{x}, \mathbf{w})=w_0+\sum_{i=1}^{D}w_ix_i + \sum_{i=1}^{D}\sum_{j=1}^{D}w_{ij}x_i x_j + \sum_{i=1}^{D}\sum_{j=1}^{D}\sum_{k=1}^{D}w_{ijk}x_i x_j x_k
$$

<div class="sub-item">

계수의 개수가 $\mathcal{O}(D^3)$로 증가한다는 점에 유의하세요.

</div>

- 앞서 언급한 문제를 [차원의 저주(curse of dimensionality)]{.hl}라고 합니다.

<div class="sub-item">

이 문제를 해결하기 위해 많은 패턴 인식 및 기계학습 알고리즘이 개발되었습니다.

</div>

---
layout: prism
heading: 목차
---

<div style="margin-top: 0rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">서론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">모델 선택 및 차원의 저주</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">결정 이론</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">결정 이론</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">오분류율 최소화</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">거부 옵션</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">추론과 결정</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">정보 이론</span></p>
  </div>

</div>

---
layout: prism
heading: 결정 이론
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 확률로 표현되는 불확실성이 존재하는 상황에서 _결정(decision)_을 내려야 한다고 가정해봅시다.

- 이 경우, 최적의 결정을 내리기 위해 [결정 이론(decision theory)]{.hl}을 사용합니다.

- 주어진 데이터에 대한 각 클래스의 조건부확률을 구하기 위해 베이즈 정리를 사용할 수 있습니다.

$$
p(\mathcal{C}_k|\mathbf{x})=\frac{p(\mathbf{x}|\mathcal{C}_k)p(\mathcal{C}_k)}{p(\mathbf{x})}
$$

---
layout: prism
heading: 오분류율 최소화 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 우리의 주된 목표가 단순히 오분류된 샘플의 수를 줄이는 것이라고 하면, 각 $\mathbf{x}$를 가능한 클래스로 대응시키는 규칙을 만들어야 합니다.

<div class="sub-item">

이 규칙은 입력 공간을 [결정 영역(decision regions)]{.hl}이라고 불리는 영역 $\mathcal{R}_k$로 나눕니다.

</div>

<div class="subsub-item">

결정 영역의 개수는 클래스의 개수와 같으며, $\mathcal{R}_k$ 안의 데이터 포인트는 $\mathcal{C}_k$에 속합니다.

</div>

<div class="subsub-item">

결정 영역 사이의 경계를 [결정 경계(decision boundary)]{.hl} 또는 결정 표면(decision surface)이라고 합니다.

</div>

- 이진 분류 문제에서, _실수(mistake)_를 범할 확률 $p(m)$은 다음과 같이 추정할 수 있습니다:

$$
\begin{aligned}
p(m)&=p(\mathbf{x}\in\mathcal{R}_1, \mathcal{C}_2)+p(\mathbf{x}\in\mathcal{R}_2,\mathcal{C}_1)\\
&=\int_{\mathcal{R}_1}p(\mathbf{x},\mathcal{C}_2)\,\mathrm{d}\mathbf{x}+\int_{\mathcal{R}_2}p(\mathbf{x}, \mathcal{C}_1)\,\mathrm{d}\mathbf{x}
\end{aligned}
$$

---
layout: prism
heading: 오분류율 최소화 (2/2)
---

- $p(m)$을 최소화하려면, $\mathbf{x}$는 피적분함수 값이 더 작은 클래스에 할당되어야 합니다.

<div class="sub-item">

예를 들어, $p(\mathbf{x},\mathcal{C}_1)>p(\mathbf{x},\mathcal{C}_2)$이면 $\mathbf{x}$는 $\mathcal{C}_1$에 할당되어야 합니다.

</div>

- 더 형식적으로 말하면, 각 $\mathbf{x}$는 사후확률 $p(\mathcal{C}_k|\mathbf{x})$를 최대화하는 클래스에 할당되어야 합니다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.24.png" class="img-center" style="width: 22rem;" />

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

---
layout: prism
heading: 기대 손실 최소화
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 기대 손실을 최소화하는 것은 오분류된 샘플을 최소화하는 것보다 더 복잡할 수 있습니다.

- 이 문제를 해결하기 위해 [비용 함수(cost function)]{.hl}, 즉 [손실 함수(loss function)]{.hl}를 도입할 수 있습니다.

- 손실 $L_{kj}$를 클래스 $k$의 샘플이 클래스 $j$로 오분류되었을 때의 벌점(penalty)으로 정의합시다.

- 이 경우, 우리의 최종 목표는 손실의 평균값을 최소화하는 것입니다:

$$
\mathbb{E}[L]=\sum_k\sum_j\int_{\mathcal{R}_j}L_{kj}p(\mathbf{x},\mathcal{C}_k)\,\mathrm{d}\mathbf{x}
$$

<div class="sub-item">

따라서 기대 손실을 최소화하기 위해 $\mathcal{R}_j$를 적절히 선택해야 합니다.

</div>

---
layout: prism
heading: 거부 옵션
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 입력 공간의 특정 영역에서는 결합확률 $p(x,\mathcal{C}_k)$가 비슷한 값을 가질 수 있어, 이 영역이 어느 클래스에 속하는지 명확하지 않을 수 있습니다.

- 상황에 따라, 오류율을 최소화하기 위해 분류가 불확실한 영역에서는 결정을 내리지 않는 것이 적절할 수 있습니다.

<div class="sub-item">

이러한 접근법을 [거부 옵션(reject option)]{.hl}이라고 합니다.

</div>

- 임계값 $\theta$를 설정할 수 있으며, 사후확률 $p(\mathcal{C}_k|\mathbf{x})$의 최댓값이 $\theta$ 이하이면 시스템은 결정을 거부할 수 있습니다.

---
layout: prism
heading: 추론과 결정
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 분류 문제는 두 단계로 나눌 수 있습니다:

<div class="sub-item-enum">

1. [추론 단계(inference stage)]{.hl}는 학습 데이터셋을 이용해 모델을 학습합니다.
2. [결정 단계(decision stage)]{.hl}는 학습된 사후확률을 바탕으로 최적의 클래스를 할당합니다.

</div>

- 또한, 입력값에 대한 결정을 반환하는 함수를 학습할 수 있으며, 이 함수를 [판별 함수(discriminant function)]{.hl}라고 합니다.

- 결정 문제를 해결하는 세 가지 접근법이 있습니다:

<div class="sub-item-enum">

1. [생성 모델(generative model)]{.hl}은 입력값과 출력값의 분포를 _모델링_합니다.
2. [판별 모델(discriminative model)]{.hl}은 사후확률을 직접 _모델링_합니다.
3. 확률을 사용하지 않고도, 학습 샘플을 각 클래스에 대응시키는 판별 함수를 찾을 수 있습니다.

</div>

---
layout: prism
heading: 목차
---

<div style="margin-top: 0rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">서론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">모델 선택 및 차원의 저주</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">결정 이론</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">정보 이론</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">정보 이론</span></p>
  </div>

</div>

---
layout: prism
heading: 정보 이론 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 이산 확률변수 $x$의 정보량은 그것이 얼마나 놀라운지와 관련이 있습니다.

<div class="sub-item">

발생 가능성이 낮은 사건에 대해 알게 될 때, 더 확률이 높은 사건보다 더 놀라움을 느낀다는 점에 유의하세요.

</div>

- 정보량의 측정은 확률분포 $p(x)$에 의존하며, 정보량을 나타내는 함수는 다음과 같이 정의될 수 있습니다:

$$
h(x)=-\log _2 p(x)
$$

<div class="sub-item">

두 개의 독립 사건이 함께 발생할 때, 얻어지는 정보량은 각 사건에서 개별적으로 얻는 정보량의 합이며, 두 사건이 동시에 발생할 확률은 각각의 확률의 곱입니다.

</div>

<div class="subsub-item">

여기서 정보량이 확률분포의 로그(log)임을 유추할 수 있습니다.

</div>

---
layout: prism
heading: 정보 이론 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 정보 전달량의 평균값인 $x$의 [엔트로피(entropy)]{.hl}는 다음과 같이 정의됩니다:

$$
\mathrm{H}[x]=-\sum_x p(x) \log _2 p(x)
$$

<div class="sub-item">

$\log_2$ 대신 $\ln$을 사용할 수 있으며, 이 경우 단위는 _비트(bit)_에서 _내트(nat)_로 바뀝니다.

</div>

- $N$개의 물체가 있고 이들이 여러 버킷(bucket)에 나뉘어 있다고 가정하면, [다중도(multiplicity)]{.hl}라고 불리는 경우의 수는 다음과 같이 정의됩니다:

$$
W=\frac{N!}{\prod_i n_{i}!}
$$

<div class="sub-item">

엔트로피는 다중도의 로그로부터 다음과 같이 유도될 수 있습니다:

</div>

$$
\mathrm{H}=\frac{1}{N} \ln W=\frac{1}{N} \ln N!-\frac{1}{N} \sum_i \ln n_{i}!
$$

---
layout: prism
heading: 정보 이론 (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 엔트로피에 $N\rightarrow\infty$를 적용하고, 다음과 같은 [스털링 근사(Stirling's approximation)]{.hl}를 사용합시다:

$$
\ln N!\simeq N \ln N-N
$$

- 최종적으로 다음과 같은 정의를 얻을 수 있습니다:

$$
\mathrm{H}=-\lim _{N \rightarrow \infty} \sum_i\left(\frac{n_i}{N}\right) \ln \left(\frac{n_i}{N}\right)=-\sum_i p_i \ln p_i
$$

<div class="sub-item">

물리학 문헌에서, 버킷 안의 물체들의 배열 순서를 [미시상태(microstate)]{.hl}라고 하고, 각 버킷에 있는 물체 수의 비율을 [거시상태(macrostate)]{.hl}라고 합니다.

</div>

<div class="sub-item">

다중도 $W$는 거시상태의 [가중치(weights)]{.hl}라고도 알려져 있습니다.

</div>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}