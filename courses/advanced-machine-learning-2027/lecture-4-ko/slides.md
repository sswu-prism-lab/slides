---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 4 (KO)
download: true
info: |
  ## 고급 기계학습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-4/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">4주차: 선형 회귀 모델</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span class="text-gray-900 dark:text-gray-100">선형 회귀 모델</span></p>
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
heading: 복습 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 이산적이고 이진적인 확률변수에 대해서는 베르누이 분포를 사용할 수 있습니다:

$$
\mathrm{Bern}(x|\mu)=\mu^x(1-\mu)^{1-x}
$$

<div class="sub-item">

여기서 $\mu$는 $x=1$일 확률을 나타냅니다.

</div>

- 베르누이 분포에 대한 켤레 확률분포는 베타 분포이며, 다음과 같이 주어집니다:

$$
\mathrm{Beta}(\mu|a,b)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\mu^{a-1}(1-\mu)^{b-1}
$$

<div class="sub-item">

여기서 $a$와 $b$는 각각 $x=1$과 $x=0$의 유효 관측 횟수를 나타냅니다.

</div>

---
layout: prism
heading: 복습 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 여러 선택지가 있는 경우에는 다음 분포를 사용합니다:

$$
p(\mathbf{x}|\boldsymbol{\mu})=\prod_{k=1}^{K}\mu_k^{x_k}
$$

<div class="sub-item">

여기서 $\mu_k$는 $x_k=1$일 확률입니다.

</div>

- 다항분포에 대한 켤레 확률분포는 디리클레 분포입니다:

$$
\mathrm{Dir}(\boldsymbol{\mu}|\boldsymbol{\alpha})=\frac{\Gamma(\alpha_0)}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_K)}\prod_{k=1}^{K}\mu_k^{\alpha_k-1},\qquad \alpha_0=\sum_{k=1}^{K}\alpha_k
$$

---
layout: prism
heading: 복습 (3/3)
---

- 가우시안 분포는 다음과 같은 형태를 갖는다는 점에 유의하세요:

$$
\mathcal{N}(x|\mu,\sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{-\frac{1}{2\sigma^2}(x-\mu)^2\right\}
$$

- 완전제곱식을 이용하면, 주어진 확률분포가 가우시안인지 아닌지를 판별할 수 있습니다.
  - 또한, 주어진 제약조건 하에서 함수의 최댓값과 최솟값을 추정하기 위한 라그랑주 승수법도 학습했습니다.

<div class="theorem-box">

<div class="theorem-box-title">과제!</div>

<div class="theorem-box-body">

다음 제약조건 하에서 함수 $f(x, y)=xy$의 최댓값과 최솟값을 구하세요:

$$
x^2+4y^2=8
$$

</div>
</div>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">심화: 가우시안 분포와 최대가능도 추정</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">선형 기저 함수 모델</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">편향–분산 트레이드오프</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">베이지안 선형 회귀</span></p>
  </div>

</div>

---
layout: prism
heading: "심화: 가우시안 분포와 MLE (1/7)"
---

- 하나의 데이터셋을 관측하고, 각 데이터포인트가 가우시안 분포로부터 [독립적이며 동일하게 분포된]{.hl} (i.i.d.) 것이라고 가정해봅시다:

$$
p(x_n)\sim\mathcal{N}(x_n|\mu,\sigma^2).
$$

- 이 데이터셋의 가능도 함수는 다음과 같이 주어집니다:

$$
p(\boldsymbol{\mathsf{x}}|\mu,\sigma^2)=\prod_{n=1}^{N}p(x_n)=\prod_{n=1}^{N}\mathcal{N}(x_n|\mu,\sigma^2).
$$

<div class="sub-item">

$\boldsymbol{\mathsf{x}}=(x_1,\ldots,x_N)$이고 $N$은 관측된 데이터포인트의 개수입니다.

</div>

<div class="sub-item">

로그가능도는 다음과 같이 정의됩니다

</div>

$$
\ln p(\boldsymbol{\mathsf{x}}|\mu,\sigma^2)=\sum_{n=1}^{N}\ln p(x_n)=\sum_{n=1}^{N}\ln\left\{ \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(- \frac{(x_n-\mu)^2}{2\sigma^2} \right)\right\}.
$$

---
layout: prism
heading: "심화: 가우시안 분포와 MLE (2/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 로그의 성질을 이용하여 로그가능도 함수 $L(\mu,\sigma^2)$를 다시 유도합니다:

$$
\begin{aligned}
\ln p(\boldsymbol{\mathsf{x}}|\mu,\sigma^2)&=\sum_{n=1}^{N}\ln\left\{ \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(- \frac{(x_n-\mu)^2}{2\sigma^2} \right) \right\}\\
&=\sum_{n=1}^{N}\left[ -\frac{1}{2}\ln(2\pi\sigma^2)-\frac{(x_n-\mu)^2}{2\sigma^2}  \right]\\
\therefore L(\mu,\sigma^2)&=-\frac{N}{2}\ln(2\pi\sigma^2)-\frac{1}{2\sigma^2}\sum_{n=1}^{N}(x_n-\mu)^2.
\end{aligned}
$$

<div class="sub-item">

이제 $\frac{\partial L(\mu,\sigma^2)}{\partial \mu}=0$과 $\frac{\partial L(\mu,\sigma^2)}{\partial \sigma^2}=0$을 풀어 ML 해를 구할 수 있습니다

</div>

---
layout: prism
heading: "심화: 가우시안 분포와 MLE (3/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

$$
\begin{aligned}
\frac{\partial L(\mu,\sigma^2)}{\partial \mu}&=-\frac{1}{2\sigma^2}\cdot 2\sum_{n=1}^{N}(x_n-\mu)(-1)=\frac{1}{\sigma^2}\sum_{n=1}^{N}(x_n-\mu)=0\\
\sum_{n=1}^{N}(x_n-\mu)&=0\quad\Rightarrow\quad\sum_{n=1}^{N}x_n=\sum_{n=1}^{N}\mu=N\mu\\
\therefore \mu_{\mathrm{ML}}&=\frac{1}{N}\sum_{n=1}^{N}x_n
\end{aligned}
$$

- $\mu_\mathrm{ML}$은 표본평균이라고 불린다는 점에 유의하세요.

---
layout: prism
heading: "심화: 가우시안 분포와 MLE (4/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

$$
\begin{aligned}
\frac{\partial L(\mu,\sigma^2)}{\partial \sigma^2}&=-\frac{N}{2}\frac{1}{\sigma^2}+\frac{1}{2(\sigma^2)^2}\sum_{n=1}^{N}(x_n-\mu)^2=-\frac{N}{2\sigma^2}+\frac{1}{2\sigma^4}\sum_{n=1}^{N}(x_n-\mu)^2=0\\
N\sigma^2&=\sum_{n=1}^{N}(x_n-\mu)^2\quad\Rightarrow\quad \sigma^2=\frac{1}{N}\sum_{n=1}^{N}(x_n-\mu)^2\\
\therefore\sigma^2_\mathrm{ML}&=\frac{1}{N}\sum_{n=1}^{N}(x_n-\mu_\mathrm{ML})^2
\end{aligned}
$$

- $\sigma_\mathrm{ML}^2$은 표본분산이라고 불린다는 점에 유의하세요.

---
layout: prism
heading: "심화: 가우시안 분포와 MLE (5/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 4em;
}
</style>

- 표본평균과 표본분산의 기댓값을 구해봅시다.

$$
\mathbb{E}[\mu_{\mathrm{ML}}]=\mathbb{E}\left[\frac{1}{N}\sum_{n=1}^{N}x_n\right]=\frac{1}{N}\sum_{n=1}^{N}\mathbb{E}[x_n]=\frac{1}{N}(N\mu)=\mu
$$

<div class="sub-item">

이 기댓값은 편향되지 않았다는 점에 유의하세요.

</div>

---
layout: prism
heading: "심화: 가우시안 분포와 MLE (6/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

$$
\begin{aligned}
\mathbb{E}[\sigma^2_\mathrm{ML}]&=\mathbb{E}\left[ \frac{1}{N}\sum_{n=1}^{N}(x_n-\mu_\mathrm{ML})^2 \right]=\mathbb{E}\left[ \frac{1}{N}\sum_{n=1}^{N}(x_n-\mu+\mu- \mu_\mathrm{ML})^2 \right]\\
&=\mathbb{E}\left[\frac{1}{N}\sum_{n=1}^{N}(x_n-\mu)^2\right]-\mathbb{E}[(\mu_{\mathrm{ML}}-\mu)^2]\\
&=\sigma^2-\mathrm{Var}[\mu_{\mathrm{ML}}]=\sigma^2-\mathrm{Var}\left[\frac{1}{N}\sum_{n=1}^{N}x_n\right]=\sigma^2 -\frac{1}{N^2}\sum_{n=1}^{N}\mathrm{Var}[x_n]\\
&=\frac{N-1}{N}\sigma^2
\end{aligned}
$$

- 이 기댓값은 편향되어 있다는 점에 유의하세요.

---
layout: prism
heading: "심화: 가우시안 분포와 MLE (7/7)"
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(0)

true_mu, true_sigma2 = 5.0, 2.0
N = 10
n_trials = 100000

sample_means = np.empty(n_trials)
sample_vars_ml = np.empty(n_trials)

for i in range(n_trials):
    x = rng.normal(true_mu, np.sqrt(true_sigma2), size=N)
    mu_ml = x.mean()
    sample_means[i] = mu_ml
    sample_vars_ml[i] = np.mean((x - mu_ml) ** 2)

print(f"true sigma^2 = {true_sigma2}")
print(f"(N-1)/N * true sigma^2 = {(N - 1) / N * true_sigma2:.4f}  (predicted by the slide's formula)")
print()
print(f"E[mu_ML] over {n_trials} trials = {sample_means.mean():.4f}  (should be close to true mu = {true_mu})")
print(f"E[sigma^2_ML] over {n_trials} trials = {sample_vars_ml.mean():.4f}  (biased, should match (N-1)/N * sigma^2)")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">심화: 가우시안 분포와 최대가능도 추정</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">선형 기저 함수 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">최대가능도와 최소제곱</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">순차 학습</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">정규화된 최소제곱</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">편향–분산 트레이드오프</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">베이지안 선형 회귀</span></p>
  </div>

</div>

---
layout: prism
heading: 선형 기저 함수 모델 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- $\mathbf{x}=(x_1,\ldots,x_D)$에 대해, 입력 변수들의 선형결합을 기반으로 [선형 회귀]{.hl} 모델을 정의할 수 있습니다:

$$
y(\mathbf{x},\mathbf{w})=w_0+w_1x_1+\cdots+x_Dw_D
$$

<div class="sub-item">

$\mathbf{w}=(w_0,\ldots,w_D)^\top$.

</div>

- 여기서, 고정된 비선형 함수들의 선형결합을 정의할 수 있습니다

$$
y(\mathbf{x},\mathbf{w})=w_0+\sum_{j=1}^{M-1}w_j\phi_j(\mathbf{x})
$$

<div class="sub-item">

$\phi_j(\mathbf{x})$는 [기저 함수(basis function)]{.hl}입니다.

</div>

<div class="sub-item">

$w_0$는 고정된 오프셋을 나타내며, 때때로 [편향(bias)]{.hl} 매개변수라고 불립니다.

</div>

<div class="subsub-item">

편의를 위해, 가상의 기저 함수 $\phi_0(\mathbf{x})=1$을 도입하면, $y(\mathbf{x},\mathbf{w})=\sum_{j=0}^{M-1}w_j\phi_j(\mathbf{x})=\mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})$를 유도할 수 있습니다. 여기서 $\boldsymbol{\phi}=(\phi_0,\ldots,\phi_{M-1})^\top$이고 $\mathbf{w}$는 $(w_0,\ldots,w_{M-1})^\top$이 됩니다.

</div>

---
layout: prism
heading: 선형 기저 함수 모델 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 기저 함수에는 여러 종류가 있습니다.

- 다음은 가우시안 기저 함수입니다

$$
\phi_j({x})=\exp \left\{-\frac{\left(x-\mu_j\right)^2}{2 s^2}\right\}
$$

- 다음은 [시그모이드(sigmoid)]{.hl} 기저 함수입니다

$$
\phi_j(x)=\sigma\left(\frac{x-\mu_j}{s}\right)
$$

<div class="sub-item">

여기서 $\sigma(a)$는 [로지스틱 시그모이드(logistic sigmoid)]{.hl} 함수입니다

</div>

$$
\sigma(a)=\frac{1}{1+\exp (-a)}
$$

---
layout: prism
heading: 최대가능도와 최소제곱 (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 목표 변수 $t$가 평균 $y(\mathbf{x},\mathbf{w})$와 정밀도 $\beta$를 갖는 가우시안 분포로 표현될 수 있다고 가정합니다

$$
\begin{aligned}
t&=y(\mathbf{x}, \mathbf{w})+\epsilon\\
p(t|\mathbf{x},\mathbf{w},\beta)&=\mathcal{N}(t|y(\mathbf{x},\mathbf{w}),\beta^{-1})
\end{aligned}
$$

- 제곱합 오차 함수를 사용하는 경우, 최적의 예측은 조건부 기댓값으로 주어집니다:

$$
\mathbb{E}[t | \mathbf{x}]=\int t\, p(t | \mathbf{x}) \,\mathrm{d} t=y(\mathbf{x}, \mathbf{w})
$$

---
layout: prism
heading: 최대가능도와 최소제곱 (2/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 데이터셋 $\mathbf{X}=\{\mathbf{x}_1,\ldots,\mathbf{x}_N\}$과 그에 대응하는 목표 변수 $\boldsymbol{\mathsf{t}}=\{t_1,\ldots,t_N\}$이 주어지면, 가능도 함수를 다음과 같이 쓸 수 있습니다:

$$
p(\boldsymbol{\mathsf{t}} | \mathbf{X}, \mathbf{w}, \beta)=\prod_{n=1}^N \mathcal{N}(t_n | \mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n), \beta^{-1})
$$

<div class="sub-item">

여기서부터는 회귀 문제가 입력 변수의 분포를 모델링할 필요가 없으므로, 가능도 함수를 $p(\boldsymbol{\mathsf{t}}|\mathbf{w},\beta)$로 표기합니다.

</div>

- 로그가능도 함수는 다음과 같이 나타낼 수 있습니다:

$$
\ln p(\boldsymbol{\mathsf{t}} | \mathbf{w}, \beta)  =\sum_{n=1}^N \ln \mathcal{N}(t_n | \mathbf{w}^{\top} \phi(\mathbf{x}_n), \beta^{-1}) =\frac{N}{2} \ln \beta-\frac{N}{2} \ln (2 \pi)-\beta E_D(\mathbf{w})
$$

<div class="sub-item">

제곱합 오차 함수는 다음과 같이 정의됩니다: $E_D(\mathbf{w})=\frac{1}{2} \sum_{n=1}^N\{t_n-\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)\}^2$.

</div>

---
layout: prism
heading: 최대가능도와 최소제곱 (3/4)
---

- 최대가능도를 추정하기 위해, 로그가능도 함수를 $\mathbf{w}$에 대해 미분하고 $0$으로 놓습니다:

$$
\begin{aligned}
\nabla \ln p(\boldsymbol{\mathsf{t}} | \mathbf{w}, \beta)&=\beta \sum_{n=1}^N\{t_n-\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)\} \boldsymbol{\phi}(\mathbf{x}_n)^{\top}\\
0&=\sum_{n=1}^N t_n \phi(\mathbf{x}_n)^{\top}-\mathbf{w}^{\top}\left\{\sum_{n=1}^N \phi(\mathbf{x}_n) \boldsymbol{\phi}(\mathbf{x}_n)^{\top}\right\}\quad\Rightarrow\quad \mathbf{w}_{\mathrm{ML}}=(\boldsymbol{\Phi}^{\top} \boldsymbol{\Phi})^{-1} \boldsymbol{\Phi}^{\top} \boldsymbol{\mathsf{t}}
\end{aligned}
$$

- 위 식은 최소제곱 문제에 대한 [정규방정식(normal equation)]{.hl}으로 알려져 있으며, $\boldsymbol{\Phi}$는 $N\times M$ 행렬로 [설계 행렬(design matrix)]{.hl}이라고 불립니다

$$
\boldsymbol{\Phi}=\left(\begin{array}{cccc}
\phi_0(\mathbf{x}_1) & \phi_1(\mathbf{x}_1) & \cdots & \phi_{M-1}(\mathbf{x}_1) \\
\phi_0(\mathbf{x}_2) & \phi_1(\mathbf{x}_2) & \cdots & \phi_{M-1}(\mathbf{x}_2) \\
\vdots & \vdots & \ddots & \vdots \\
\phi_0(\mathbf{x}_N) & \phi_1(\mathbf{x}_N) & \cdots & \phi_{M-1}(\mathbf{x}_N)
\end{array}\right)
$$

---
layout: prism
heading: "NOTE: 정규방정식"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 간단히 하기 위해, 선형 기저 함수 $\phi(x)=x$를 사용한다고 가정합시다.

- 이제, 주어진 데이터셋 $\mathbf{x}$와 $\boldsymbol{\mathsf{t}}$에 대해, 최소제곱 문제를 풀어 최적의 회귀 모델을 찾아야 합니다:

$$
\mathbf{x}=
\begin{pmatrix}
1\\
2\\
3
\end{pmatrix}\qquad
\boldsymbol{\mathsf{t}}=\begin{pmatrix}
2\\
3\\
5
\end{pmatrix}
$$

- 오프셋을 포함하여, 설계 행렬을 구성합니다

$$
\boldsymbol{\Phi}=\begin{pmatrix}
\phi_0(x_1) & \phi_1(x_1)\\
\phi_0(x_2) & \phi_1(x_2)\\
\phi_0(x_3) & \phi_1(x_3)
\end{pmatrix}
=
\begin{pmatrix}
1&1\\
1&2\\
1&3
\end{pmatrix}
$$

---
layout: prism
heading: "NOTE: 정규방정식"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- 이제, 다음 방정식을 풀어야 합니다:

$$
\boldsymbol{\Phi}\mathbf{w}=\boldsymbol{\mathsf{t}}
$$

- 다음 식들을 유도할 수 있습니다

$$
\begin{aligned}
\boldsymbol{\Phi}^{\top}\boldsymbol{\Phi}\mathbf{w}&=\boldsymbol{\Phi}^{\top}\boldsymbol{\mathsf{t}}\\
\mathbf{w}&=(\boldsymbol{\Phi}^{\top}\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^{\top}\boldsymbol{\mathsf{t}}\\
\therefore \mathbf{w}&=
\left(
\begin{pmatrix}
1 & 1 & 1\\
1 & 2 & 3
\end{pmatrix}
\begin{pmatrix}
1&1\\
1&2\\
1&3
\end{pmatrix}
\right)^{-1}
\begin{pmatrix}
1 & 1 & 1\\
1 & 2 & 3
\end{pmatrix}
\begin{pmatrix}
2\\
3\\
5
\end{pmatrix}
\simeq
\begin{pmatrix}
0.333\\
1.5
\end{pmatrix}
\end{aligned}
$$

- 최종적으로 선형 회귀 모델을 얻습니다:

$$
t=0.333+1.5x
$$

---
layout: prism
heading: "NOTE: 정규방정식"
---

<PyRunner>

```python
import numpy as np

x = np.array([1, 2, 3])
t = np.array([2, 3, 5])

Phi = np.column_stack([np.ones_like(x), x])  # design matrix: [phi_0(x), phi_1(x)] = [1, x]

w_ml = np.linalg.inv(Phi.T @ Phi) @ Phi.T @ t

print("Design matrix Phi:\n", Phi)
print("\nw_ML =", np.round(w_ml, 4))
print(f"\nFitted model: t = {w_ml[0]:.3f} + {w_ml[1]:.3f} * x")
print("\nMatches the slide's answer (0.333, 1.5)?", np.allclose(w_ml, [0.333, 1.5], atol=1e-3))
```

</PyRunner>

---
layout: prism
heading: 최대가능도와 최소제곱 (4/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 최소제곱 해는 $(\mathbf{x},\boldsymbol{\mathsf{t}})$의 오차를 최소화하는 벡터라는 점에 유의하세요.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure3.2.png" class="img-center" style="width: 26rem;" />

---
layout: prism
heading: 순차 학습 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 설계 행렬은 전체 학습 데이터셋을 한 번에 사용하며, 이를 [배치 학습(batch learning)]{.hl}이라고 합니다.

<div class="sub-item">

만약 대규모 데이터셋을 다룬다면, 이 방법은 계산이 불가능해질 수 있음을 생각해보세요.

</div>

- 대규모 데이터셋에 대해서는 [순차(sequential)]{.hl} 알고리즘을 사용합니다

<div class="sub-item">

딥러닝 문헌에서는 [미니배치 학습(mini-batch learning)]{.hl}이라는 용어를 사용했습니다.

</div>

<div class="sub-item">

순차 알고리즘에서는 각 모델 업데이트마다 일부 데이터포인트만 고려됩니다.

</div>

- [확률적 경사 하강법(stochastic gradient descent)]{.hl} 알고리즘은 매개변수 벡터를 다음과 같이 업데이트합니다

$$
\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}-\eta \nabla E_n
$$

<div class="sub-item">

여기서 $\tau$와 $\eta$는 각각 반복 횟수와 학습률을 나타냅니다.

</div>

<div class="sub-item">

처음에 $\mathbf{w}$는 임의의 초기 벡터 $\mathbf{w}^{(0)}$로 초기화됩니다.

</div>

- 위의 제곱합 오차 함수를 확률적 경사 하강법에 사용하면, 이를 흔히 [최소평균제곱(least mean squares, LMS)]{.hl} 알고리즘이라고 부릅니다.

---
layout: prism
heading: 순차 학습 (2/2)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(1)

# A slightly larger toy dataset than the Normal Equation example
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
t = np.array([2.0, 3.0, 5.0, 6.0, 8.0])
Phi = np.column_stack([np.ones_like(x), x])

# Closed-form (batch) solution
w_batch = np.linalg.inv(Phi.T @ Phi) @ Phi.T @ t

# Stochastic gradient descent (one datapoint at a time)
w_sgd = np.zeros(2)
eta = 0.01
n_epochs = 2000

for epoch in range(n_epochs):
    idx = rng.permutation(len(x))
    for i in idx:
        phi_n = Phi[i]
        error_n = t[i] - w_sgd @ phi_n
        w_sgd = w_sgd + eta * error_n * phi_n  # w <- w + eta * error_n * phi(x_n)

print("w from Normal Equation (batch):", np.round(w_batch, 4))
print("w from SGD after", n_epochs, "epochs:  ", np.round(w_sgd, 4))
print("\nDo they converge to the same solution?", np.allclose(w_batch, w_sgd, atol=5e-2))
```

</PyRunner>

---
layout: prism
heading: 정규화된 최소제곱
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 정규화를 위해 벌점항을 추가할 수 있으며, 그러면 일반화된 형태를 다음과 같이 쓸 수 있습니다

$$
\frac{1}{2} \sum_{n=1}^N\{t_n-\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)\}^2+\frac{\lambda}{2} \sum_{j=1}^M|w_j|^q
$$

<div class="sub-item">

$q=2$인 경우 모델은 릿지 회귀가 되고, $q=1$인 경우 모델은 라쏘 회귀가 됩니다.

</div>

<div class="subsub-item">

충분히 큰 $\lambda$에 대해서는 일부 매개변수 $w_j$가 $0$이 될 수 있으며, 이 경우 모델을 [희소(sparse)]{.hl} 모델이라고 합니다.

</div>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">심화: 가우시안 분포와 최대가능도 추정</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">선형 기저 함수 모델</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">편향–분산 트레이드오프</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">베이지안 선형 회귀</span></p>
  </div>

</div>

---
layout: prism
heading: "편향–분산 트레이드오프 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 조건부 분포 $p(t|\mathbf{x})$가 주어지면, 최적 예측 $h(\mathbf{x})$는 다음과 같이 추정할 수 있습니다:

$$
h(\mathbf{x})=\mathbb{E}[t|\mathbf{x}]=\int t\, p(t|\mathbf{x})\,\mathrm{d}t
$$

- 이제 기대 제곱 오차는 다음과 같이 추정할 수 있습니다:

$$
\mathbb{E}[L]=\int\{y(\mathbf{x})-h(\mathbf{x})\}^2 p(\mathbf{x}) \,\mathrm{d} \mathbf{x}+\iint\{h(\mathbf{x})-t\}^2 p(\mathbf{x}, t) \,\mathrm{d} \mathbf{x} \,\mathrm{d} t
$$

<div class="sub-item">

여기서 $y(\mathbf{x})$와 무관한 두 번째 항은 데이터의 내재적 잡음에서 비롯됩니다.

</div>

<div class="sub-item">

첫 번째 항은 우리가 선택한 함수 $y(\mathbf{x})$에 의해 결정되므로, 우리의 목표는 첫 번째 항의 크기를 최소화하는 $y(\mathbf{x})$를 찾는 것입니다.

</div>

---
layout: prism
heading: "편향–분산 트레이드오프 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 빈도주의 관점에서, 우리는 데이터셋 $\mathcal{D}$를 사용하여 $\mathbf{w}$를 점추정합니다.

<div class="sub-item">

이 경우, $\mathbb{E}[L]$의 첫 번째 항의 피적분 함수는 다음 식과 같습니다:

</div>

$$
\{y(\mathbf{x};\mathcal{D}) -h(\mathbf{x})\}^2
$$

<div class="subsub-item">

이 값은 $\mathcal{D}$에 의존합니다.

</div>

$$
\begin{aligned}
\{y(\mathbf{x} ; \mathcal{D})-\mathbb{E}_{\mathcal{D}}[&y(\mathbf{x} ; \mathcal{D})]+\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]-h(\mathbf{x}) \}^2 \\
=&\left\{y(\mathbf{x} ; \mathcal{D})-\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]\right\}^2+\left\{\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]-h(\mathbf{x})\right\}^2 \\
&+2\left\{y(\mathbf{x} ; \mathcal{D})-\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]\right\}\left\{\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]-h(\mathbf{x})\right\}
\end{aligned}
$$

<div class="sub-item">

이제 이 식을 $\mathcal{D}$에 대해 기댓값을 취하면, 마지막 항이 사라져 다음을 얻습니다,

</div>

$$
\begin{aligned}
\mathbb{E}_{\mathcal{D}}\left[\{y(\mathbf{x} ; \mathcal{D})-h(\mathbf{x})\}^2\right] =\underbrace{\left\{\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]-h(\mathbf{x})\right\}^2}_{(\text{bias})^2}+\underbrace{\mathbb{E}_{\mathcal{D}}\left[\left\{y(\mathbf{x} ; \mathcal{D})-\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]\right\}^2\right]}_{\text{variance}}
\end{aligned}
$$

---
layout: prism
heading: "편향–분산 트레이드오프 (3/3)"
---

- 첫 번째 [편향(bias)]{.hl} 항은 모든 데이터셋에 대한 평균 예측이 원하는 회귀 함수와 얼마나 차이 나는지를 나타냅니다.

- 두 번째 [분산(variance)]{.hl}은 개별 데이터셋에 대한 해들이 그 평균 주위에서 얼마나 변동하는지를 측정하며, 따라서 함수 $y(\mathbf{x};\mathcal{D})$가 특정 데이터셋 선택에 얼마나 민감한지를 측정합니다.

- 기대 손실은 제곱 편향, 분산, 그리고 잡음으로 분해될 수 있으며, [편향–분산 트레이드오프(bias–variance tradeoff)]{.hl}를 갖습니다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure3.6.png" class="img-center" style="width: 12rem;" />

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">심화: 가우시안 분포와 최대가능도 추정</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">선형 기저 함수 모델</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">편향–분산 트레이드오프</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">베이지안 선형 회귀</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">매개변수 분포</span></p>
  </div>

</div>

---
layout: prism
heading: 매개변수 분포
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- 완전한 베이지안 선형 회귀를 위해, 모델 매개변수에 대한 사전분포 $p(\mathbf{w})$를 도입합니다.

- 정밀도 $\beta$가 알려진 상수라고 가정하면, 가능도 함수 $p(\boldsymbol{\mathsf{t}}|\mathbf{w})$는 $\mathbf{w}$에 대한 이차 함수의 지수 함수 형태를 갖습니다.

<div class="sub-item">

켤레 사전분포를 다음과 같이 설정할 수 있습니다

</div>

$$
p(\mathbf{w})=\mathcal{N}\left(\mathbf{w} | \mathbf{m}_0, \mathbf{S}_0\right).
$$

<div class="sub-item">

$\mathbf{m}_0$과 $\mathbf{S}_0$은 평균과 공분산입니다.

</div>

<div class="sub-item">

사후분포 역시 가우시안이라는 점에 유의하세요.

</div>

- 완전제곱식을 이용하면, 계수를 추정하고 사후분포를 찾을 수 있습니다.

$$
\begin{aligned}
p(\mathbf{w} | \boldsymbol{\mathsf{t}})&=\mathcal{N}(\mathbf{w} | \mathbf{m}_N, \mathbf{S}_N)\\
\mathbf{m}_N & =\mathbf{S}_N(\mathbf{S}_0^{-1} \mathbf{m}_0+\beta \boldsymbol{\Phi}^{\top} \boldsymbol{\mathsf{t}}) \\
\mathbf{S}_N^{-1} & =\mathbf{S}_0^{-1}+\beta \boldsymbol{\Phi}^{\top} \boldsymbol{\Phi}
\end{aligned}
$$

---
layout: prism
heading: 예측 분포
---

<style>
.slidev-layout ul > li {
  margin-top: 4em;
}
</style>

- 주어진 새로운 입력 $\mathbf{x}$에 대해 새로운 목표 값 $t$를 예측하기 위해, 다음 [예측 분포(predictive distribution)]{.hl}를 고려합니다.

$$
\begin{aligned}
p(t | \boldsymbol{\mathsf{t}}, \alpha, \beta)&=\int p(t | \mathbf{w}, \beta)\, p(\mathbf{w} | \boldsymbol{\mathsf{t}}, \alpha, \beta) \,\mathrm{d} \mathbf{w}\\
&=\mathcal{N}(t | \mathbf{m}_N^{\top} \boldsymbol{\phi}(\mathbf{x}), \sigma_N^2(\mathbf{x}))\\
\sigma_N^2(\mathbf{x})&=\frac{1}{\beta}+\phi(\mathbf{x})^{\top} \mathbf{S}_N \phi(\mathbf{x})
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