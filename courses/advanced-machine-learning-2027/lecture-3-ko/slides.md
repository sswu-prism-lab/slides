---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 3 (KO)
download: true
info: |
  ## 고급 기계학습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-3/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">3주차: 확률 분포</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span class="text-gray-900 dark:text-gray-100">확률 분포</span></p>
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
heading: 복습 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 회귀 문제를 모델링하기 위한 오차 함수를 다음과 같이 정의할 수 있습니다:

$$
E(\mathbf{w})=\frac{1}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})-t_n\}^2
$$

<div class="sub-item">

오차 함수가 이차 형태이므로 닫힌 형태(closed-form)의 해를 갖는다는 점에 유의하세요.

</div>

<div class="subsub-item">

$y=4x^2-12x+16$의 최솟값을 구하는 문제를 생각해보세요.

</div>

- 로그가능도 함수가 앞서 언급한 오차 함수와 유사하다는 점에 유의하세요:

$$
\ln p(\boldsymbol{\mathsf{t}}|\boldsymbol{\mathsf{x}}, \mathbf{w}, \beta)=-\frac{\beta}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})-t_n\}^2 + \frac{N}{2}\ln\beta -\frac{N}{2}\ln (2\pi)
$$

---
layout: prism
heading: 복습 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 과적합 문제를 해결하기 위해 정규화 기법이라는 벌점항을 추가로 도입할 수 있습니다.

$$
\tilde{E}(\mathbf{w})=\frac{1}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w}) - t_n \}^2 + \frac{\lambda}{2}\|\mathbf{w}\|^2
$$

- 최대사후확률은 위의 수정된 오차 함수와 유사한 다음 식을 최소화한다는 점에 유의하세요:

$$
\frac{\beta}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})-t_n\}^2+\frac{\alpha}{2}\mathbf{w}^\top\mathbf{w}
$$

- 의사결정을 위해, 오분류된 샘플 수를 줄이는 것과 기대 손실을 최소화하는 것, 두 가지 다른 전략을 고려할 수 있습니다.

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">이산 확률변수</span></p>
    <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">베타 분포</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">다항 변수</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가우시안 분포</span></p>
  </div>

</div>

---
layout: prism
heading: 이산 확률변수 (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [확률변수(random variable)]{.hl} (r.v.) $x\in\{0,1\}$를 생각해봅시다. 이때 $x=1$일 확률은 확률변수 $\mu$로 나타낼 수 있습니다:

$$
p(x=1|\mu)=\mu
$$

<div class="sub-item">

$0\leqslant \mu\leqslant 1$이고 $p(x=0|\mu)=1-\mu$라는 점에 유의하세요.

</div>

- 이 이산적이고 이진적인 확률변수 $x$에 대해, 확률분포를 [베르누이 분포(Bernoulli distribution)]{.hl}라고 불리는 형태로 다시 쓸 수 있습니다:

$$
\mathrm{Bern}(x|\mu)=\mu^x(1-\mu)^{1-x}
$$

<div class="sub-item">

베르누이 분포는 정규화되어 있으며 다음과 같은 기댓값과 분산을 갖습니다:

</div>

$$
\begin{aligned}
\mathbb{E}[x]&=\mu\\
\operatorname{var}[x]&=\mu(1-\mu)
\end{aligned}
$$

---
layout: prism
heading: 이산 확률변수 (2/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 확률변수 $x$의 관측 데이터셋 $\mathcal{D}=\{x_1,\ldots,x_N\}$이 주어지고, 이 데이터포인트들이 $p(x|\mu)$로부터 독립적으로 샘플링되었다고 가정하면, 가능도 함수를 다음과 같이 정형화할 수 있습니다:

$$
p(\mathcal{D}|\mu)=\prod_{n=1}^{N}p(x_n|\mu)=\prod_{n=1}^{N}\mu^{x_n}(1-\mu)^{1-x_n}
$$

<div class="sub-item">

이에 대응하는 로그가능도 함수는 다음과 같습니다:

</div>

$$
\ln p(\mathcal{D}|\mu)=\sum_{n=1}^{N}\ln p(x_n|\mu)=\sum_{n=1}^{N}\{x_n\ln\mu + (1-x_n)\ln(1-\mu)\}
$$

<div class="subsub-item">

이 로그가능도는 $N$개의 관측값 $x_n$과, 그 관측값들의 합 $\sum_n x_n$에만 관련되어 있다는 점에 유의하세요.

</div>

<div class="subsub-item">

이 합은 [충분통계량(sufficient statistic)]{.hl}의 한 예시입니다.

</div>

---
layout: prism
heading: 이산 확률변수 (3/4)
---

- 로그가능도 $\ln p(\mathcal{D}|\mu)$를 $\mu$에 대해 미분하고 $0$으로 놓으면, 최대가능도(ML) 추론을 추정할 수 있습니다.

$$
\mu_\mathrm{ML}=\frac{1}{N}\sum_{n=1}^{N}x_n
$$

<div class="sub-item">

$\mu_\mathrm{ML}$은 [표본평균(sample mean)]{.hl}이라고 불립니다.

</div>

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(0)

true_mu = 0.65
sample_sizes = [5, 20, 100, 1000, 10000]

print(f"true mu = {true_mu}\n")
print(f"{'N':>7} | {'mu_ML (sample mean)':>20} | {'|error|':>10}")
for N in sample_sizes:
    samples = (rng.random(N) < true_mu).astype(int)
    mu_ml = samples.mean()
    print(f"{N:>7} | {mu_ml:>20.4f} | {abs(mu_ml - true_mu):>10.4f}")
```

</PyRunner>

---
layout: prism
heading: 이산 확률변수 (4/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- $N$개의 데이터포인트에 대해, $x=1$인 개수를 $m$이라 하면, 이 개수의 분포를 [이항분포(binomial distribution)]{.hl}라 하며 다음과 같이 정의됩니다:

$$
\mathrm{Bin}(m|N,\mu)=\binom{N}{m}\mu^m(1-\mu)^{N-m}
$$

<div class="sub-item">

여기서, $\binom{N}{m}\equiv\frac{N!}{(N-m)!m!}$입니다.

</div>

<div class="sub-item">

이항분포의 기댓값과 분산은 다음과 같이 정의됩니다:

</div>

$$
\begin{aligned}
\mathbb{E}[m]&\equiv\sum_{m=0}^{N}m\operatorname{Bin}(m|N, \mu)=N \mu\\
\mathrm{var}[m]&\equiv\sum_{m=0}^{N}(m-\mathbb{E}[m])^2\operatorname{Bin}(m|N,\mu)=N\mu(1-\mu)
\end{aligned}
$$

---
layout: prism
heading: 베타 분포 (1/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 베르누이 분포에 베이지안 접근법을 적용하고자 하며, 이를 위해 매개변수 $\mu$에 대한 사전분포 $p(\mu)$를 도입한다고 합시다.

- 베르누이의 가능도가 $\mu^x(1-\mu)^{1-x}$ 형태의 인자를 갖는다는 점에 유의하세요.

<div class="sub-item">

만약 $\mu$와 $(1-\mu)$의 거듭제곱에 비례하는 사전분포를 선택한다면, 사전확률과 가능도 함수의 곱에 비례하는 사후분포 역시 사전분포와 같은 함수 형태를 갖게 됩니다.

</div>

<div class="subsub-item">

이러한 성질을 [켤레성(conjugacy)]{.hl}이라고 합니다.

</div>

- 예를 들어, 동전 던지기 예제를 생각해봅시다.

<div class="sub-item">

관측된 데이터에 기반한 가능도 함수가 베르누이라는 점에 유의하세요.

</div>

<div class="sub-item">

이 경우, 사전분포로 베타분포를 사용하면 사후분포 역시 다시 베타분포가 됩니다.

</div>

---
layout: prism
heading: 베타 분포 (2/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [베타 분포(Beta distribution)]{.hl}는 다음과 같은 형태를 갖습니다:

$$
\mathrm{Beta}(\mu|a, b)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\mu^{a-1}(1-\mu)^{b-1}
$$

<div class="sub-item">

감마 함수 $\Gamma(\cdot)$는 다음과 같이 정의됩니다:

</div>

$$
\Gamma(x)\equiv\int_{0}^{\infty}u^{x-1}e^{-u}\,\mathrm{d}u
$$

<div class="sub-item">

베타 분포는 다음과 같은 형태의 기댓값과 분산을 갖습니다:

</div>

$$
\begin{aligned}
\mathbb{E}[\mu]&=\frac{a}{a+b}\\
\mathrm{var}[\mu]&=\frac{ab}{(a+b)^2(a+b+1)}
\end{aligned}
$$

<div class="subsub-item">

여기서 $a$와 $b$는 하이퍼파라미터입니다.

</div>

---
layout: prism
heading: 베타 분포 (3/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 하이퍼파라미터 $a$와 $b$는 각각 $x=1$과 $x=0$의 [유효 관측 횟수(effective number of observations)]{.hl}로 볼 수 있습니다.

<div class="sub-item">

베이지안 관점에서, 이러한 [순차적(sequential)]{.hl} 접근법은 매우 자연스럽습니다.

</div>

- 사전분포를 $\mathrm{Beta}(\mu|a,b)$, 가능도를 $\mathrm{Bern}(x|\mu)$로 설정하고 앞면 $H$번, 뒷면 $T$번을 관측하면, 사후분포는 $\mathrm{Beta}(\mu|a+H,b+T)$가 됩니다.

---
layout: prism
heading: 베타 분포 (4/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 여기서, 관측이 많아질수록 그래프는 더 뾰족해집니다.

- 베이지안 학습의 일반적인 성질은, 더 많은 데이터가 관측될수록 사후분포의 불확실성이 꾸준히 감소한다는 것입니다.

<div class="img-row" style="max-width: 100%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.2a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.2b.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.2c.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.2d.png"/>

</div>

---
layout: prism
heading: 베타 분포 (5/5)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(42)

true_mu = 0.7   # true probability of heads
a, b = 2, 2     # Beta(a, b) prior
n_tosses = 20

heads = 0
tails = 0
print(f"{'Toss':>4} | {'Result':>6} | {'Posterior Beta(a,b)':>20} | {'Posterior mean':>14}")
for i in range(1, n_tosses + 1):
    result = rng.random() < true_mu
    if result:
        heads += 1
    else:
        tails += 1
    post_a, post_b = a + heads, b + tails
    post_mean = post_a / (post_a + post_b)
    print(f"{i:>4} | {'H' if result else 'T':>6} | Beta({post_a}, {post_b}){'':>7} | {post_mean:>14.4f}")

print(f"\ntrue mu = {true_mu}, final posterior mean = {post_mean:.4f}")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">이산 확률변수</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">다항 변수</span></p>
    <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">디리클레 분포</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가우시안 분포</span></p>
  </div>

</div>

---
layout: prism
heading: 다항 변수 (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.2em;
}
</style>

- $K$차원 이산 변수가 필요할 수 있습니다.

<div class="sub-item">

기계학습에서는 종종 [원-핫 인코딩(one hot encoding)]{.hl}을 사용하여, 각 변수 $\mathbf{x}\in\{0, 1\}^K$이고 $\sum_{k=1}^K x_k=1$이 되도록 합니다.

</div>

- $x_k=1$일 확률이 $\mu_k$라고 하면, $\mathbf{x}$의 분포는 다음과 같이 주어집니다

$$
p(\mathbf{x}|\boldsymbol{\mu})=\prod_{k=1}^{K}\mu_k^{x_k}
$$

<div class="sub-item">

이 분포는 다음 두 가지 성질을 갖습니다:

</div>

$$
\begin{aligned}
\sum_x p(\mathbf{x}|\boldsymbol{\mu})&=\sum_{k=1}^{K}\mu_k=1\\
\mathbb{E}[\mathbf{x}|\boldsymbol{\mu}]&=\sum_xp(\mathbf{x}|\boldsymbol{\mu})\mathbf{x}=\boldsymbol{\mu}
\end{aligned}
$$

---
layout: prism
heading: 다항 변수 (2/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- $N$개의 독립적인 관측값 $\mathbf{x}_1,\ldots,\mathbf{x}_N$을 포함하는 데이터셋에 대해, 가능도는 다음과 같은 형태를 갖습니다:

$$
p(\mathcal{D}|\boldsymbol{\mu})=\prod_{n=1}^{N}\prod_{k=1}^{K}\mu_k^{x_{nk}}=\prod_{k=1}^{K}\mu_k^{\sum_n x_{nk}}=\prod_{k=1}^{K}\mu_k^{m_k}
$$

<div class="sub-item">

$m_k$는 $x_k=1$인 관측의 개수이며, 충분통계량입니다.

</div>

- 최대가능도, 즉 $\ln p(\mathcal{D}|\boldsymbol{\mu})$를 구하고자 합니다.

<div class="sub-item">

$\sum_k\mu_k=1$이라는 제약조건이 있다는 점에 유의하세요.

</div>

---
layout: prism
heading: "NOTE: 라그랑주 승수"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 함수 $f(x)=x^2$와 제약조건 $(x-2)^2=1$이 있다고 합시다.

<div class="sub-item">

제약조건을 $x$에 대한 함수로 설정하여 $g(x)=1-(x-2)^2$로 둡니다.

</div>

- 라그랑주 함수 $f(x)+\lambda g(x)$를 설정합니다:

$$
\mathcal{L}(x,\lambda)=f(x)+\lambda g(x) = x^2 + \lambda(1-(x-2)^2)
$$

- $x$와 $\lambda$에 대해 편미분하여 정류점(stationary point)을 구합니다:

$$
\begin{aligned}
\frac{\partial\mathcal{L}}{\partial x}&=2x+\lambda(-2(x-2))=2x-2\lambda(x-2)=0\\
\frac{\partial\mathcal{L}}{\partial \lambda}&=1-(x-2)^2=0
\end{aligned}
$$

---
layout: prism
heading: "NOTE: 라그랑주 승수"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 이제 다음과 같은 연립방정식을 얻습니다:

$$
\begin{cases}
2x-2\lambda(x-2)=0\\
1-(x-2)^2=0
\end{cases}
$$

- 그 해는 다음과 같습니다:

$$
\begin{aligned}
&(x, \lambda)=(1,-1)\\
&(x,\lambda)=(3,3)
\end{aligned}
$$

<div class="sub-item">

최종적으로, 최솟점 $f(x=1)=1^2=1$과 최댓점 $f(x=3)=3^2=9$를 얻습니다.

</div>

- _이 문제를 기하학적 관점에서 생각해보세요._

---
layout: prism
heading: 다항 변수 (3/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 여기서 최댓값을 구하고자 하는 함수는 로그가능도입니다:

$$
\ln p(\mathcal{D}|\boldsymbol{\mu})=\ln\prod_{k=1}^{K}\mu_k^{m_k}=\sum_{k=1}^{K}m_k\ln \mu_k.
$$

- 이제 [라그랑주 승수(Lagrange multiplier)]{.hl} $\lambda$를 사용합니다:

$$
\sum_{k=1}^{K}m_k \ln \mu_k + \lambda\left(\sum_{k=1}^{K}\mu_k-1\right).
$$

<div class="sub-item">

위 식을 $\mu_k$에 대해 미분하고 $0$으로 놓으면 $\mu_k=-m_k/\lambda$를 얻습니다.

</div>

- 제약조건 $\sum_k\mu_k=1$ 하에서 $\lambda=-N$임을 알 수 있고, 최종적으로 ML 해를 얻습니다.

$$
\mu_k^\mathrm{ML}=\frac{m_k}{N}
$$

---
layout: prism
heading: 다항 변수 (4/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- $\boldsymbol{\mu}$와 관측 개수 $N$에 의해 결정되는 $m_1,\ldots,m_k$의 결합확률분포는 다음과 같이 정의되며, [다항분포(multinomial distribution)]{.hl}라고 불립니다

$$
\operatorname{Mult}(m_1,m_2,\ldots,m_k|\boldsymbol{\mu}, N)=\binom{N}{m_1m_2\cdots m_k}\prod_{k=1}^{K}\mu_k^{m_k},\ \sum_{k=1}^{K}m_k=N.
$$

<div class="sub-item">

여기서 $\binom{N}{m_1m_2\cdots m_K}\equiv\frac{N!}{m_1!m_2!\cdots m_K!}$입니다.

</div>

---
layout: prism
heading: 디리클레 분포
---

- 다항분포에 대한 켤레분포로 [디리클레 분포(Dirichlet distribution)]{.hl}가 있습니다

$$
\mathrm{Dir}(\boldsymbol{\mu}|\boldsymbol{\alpha})=\frac{\Gamma(\alpha_0)}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_K)}\prod_{k=1}^{K}\mu_k^{\alpha_k-1}, \quad \alpha_0=\sum_{k=1}^{K}\alpha_k.
$$

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.4.png" class="img-center" style="width: 14rem;" />

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">이산 확률변수</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">다항 변수</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">가우시안 분포</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">조건부 가우시안 분포</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">주변 가우시안 분포</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">가우시안 확률변수에 대한 베이즈 정리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">가우시안 확률변수에 대한 최대가능도</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">가우시안 혼합</span></p>
  </div>

</div>

---
layout: prism
heading: 가우시안 분포 (1/2)
---

- 단일 확률변수 $x$에 대해, 가우시안 분포는 다음과 같이 주어집니다

$$
\mathcal{N}(x|\mu,\sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{-\frac{1}{2\sigma^2}(x-\mu)^2\right\}.
$$

- $D$차원 벡터 $\mathbf{x}$에 대해, 가우시안 분포는 다음과 같이 됩니다

$$
\mathcal{N}(\mathbf{x}|\boldsymbol{\mu}, \boldsymbol{\Sigma})=\frac{1}{(2\pi)^{D/2}}\frac{1}{|\boldsymbol{\Sigma}|^{1/2}}\exp\left\{-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right\}.
$$

- [중심극한정리(central limit theorem)]{.hl}에 따르면, 특정 조건 하에서 여러 확률변수의 합을 나타내는 확률변수는 합산되는 변수의 개수가 늘어날수록 점차 가우시안 분포에 가까워집니다.

<div class="img-row" style="max-width: 43%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.6a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.6b.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.6c.png"/>

</div>

---
layout: prism
heading: 가우시안 분포 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 가우시안 분포는 확률밀도를 모델링하는 데 사용되지만, 고차원 데이터나 역행렬을 다룰 경우 계산 비용이 클 수 있습니다.

<div class="sub-item">

[대각행렬(diagonal matrix)]{.hl} 형태의 공분산 행렬을 사용하면 계산이 다루기 쉬워집니다.

</div>

- 가우시안 분포는 본질적으로 [단봉형(unimodal)]{.hl}이므로, [다봉형(multimodal)]{.hl} 데이터 분포를 표현할 수 없습니다.

<div class="sub-item">

기계학습에서는 이 문제를 해결하기 위해 많은 방법들이 [잠재변수(latent variable)]{.hl}를 도입합니다.

</div>

---
layout: prism
heading: 조건부 가우시안 분포 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 두 변수 집합이 각각 가우시안 분포를 가지면, 한 집합이 다른 집합에 대해 조건화된 분포 또한 가우시안 분포를 갖습니다.

<div class="sub-item">

각 변수 집합의 주변분포 역시 가우시안 형태를 갖습니다.

</div>

- $D$차원 벡터 $\mathbf{x}$가 $\mathcal{N}(\mathbf{x}|\boldsymbol{\mu},\boldsymbol{\Sigma})$를 따르고, $\mathbf{x}$가 두 개의 분리된 벡터 $\mathbf{x}_a$와 $\mathbf{x}_b$로 나뉜다고 합시다.

<div class="sub-item">

일반성을 잃지 않고, $\mathbf{x}_a$는 $\mathbf{x}$의 처음 $M$개 원소를, $\mathbf{x}_b$는 나머지를 갖는다고 합시다.

</div>

$$
\begin{aligned}
\mathbf{x}&=\binom{\mathbf{x}_a}{\mathbf{x}_b}\\
\boldsymbol{\mu}&=\binom{\boldsymbol{\mu}_a}{\boldsymbol{\mu}_b}\\
\boldsymbol{\Sigma}&=\begin{pmatrix}
\boldsymbol{\Sigma}_{aa} & \boldsymbol{\Sigma}_{ab}\\
\boldsymbol{\Sigma}_{ba} & \boldsymbol{\Sigma}_{bb}
\end{pmatrix}
\end{aligned}
$$

---
layout: prism
heading: 조건부 가우시안 분포 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.3em;
}
</style>

- 다음을 계산할 수 있습니다:

$$
\begin{aligned}
-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})=&-\frac{1}{2}(\mathbf{x}_a-\boldsymbol{\mu}_a)^\top\boldsymbol{\Lambda}_{aa}(\mathbf{x}_a-\boldsymbol{\mu}_a)-\frac{1}{2}(\mathbf{x}_a-\boldsymbol{\mu}_a)^\top\boldsymbol{\Lambda}_{ab}(\mathbf{x}_b-\boldsymbol{\mu}_b)\\
&-\frac{1}{2}(\mathbf{x}_b-\boldsymbol{\mu}_b)^\top\boldsymbol{\Lambda}_{ba}(\mathbf{x}_a-\boldsymbol{\mu}_a)-\frac{1}{2}(\mathbf{x}_b-\boldsymbol{\mu}_b)^\top\boldsymbol{\Lambda}_{bb}(\mathbf{x}_b-\boldsymbol{\mu}_b)
\end{aligned}
$$

여기서 $\Lambda$는 공분산 행렬의 역행렬이며, [정밀도 행렬(precision matrix)]{.hl}이라고 불립니다.

$$
\boldsymbol{\Lambda}\equiv\boldsymbol{\Sigma}^{-1}=\begin{pmatrix}
\boldsymbol{\Lambda}_{aa}& \boldsymbol{\Lambda}_{ab}\\
\boldsymbol{\Lambda}_{ba} & \boldsymbol{\Lambda}_{bb}
\end{pmatrix}
$$

- [완전제곱식(completing the square)]{.hl}을 이용하면, 조건부 분포 $p(\mathbf{x}_a|\mathbf{x}_b)$가 다음과 같은 매개변수를 갖는 가우시안 분포임을 알 수 있습니다:

$$
\begin{aligned}
\boldsymbol{\mu}_{a|b}&=\boldsymbol{\mu}_a+\boldsymbol{\Sigma}_{a|b}\{\boldsymbol{\Lambda}_{aa}\boldsymbol{\mu}_a-\boldsymbol{\Lambda}_{ab}(\mathbf{x}_b-\boldsymbol{\mu}_b)\}\\
\boldsymbol{\Sigma}_{a|b}&=\boldsymbol{\Lambda}_{aa}^{-1}
\end{aligned}
$$

---
layout: prism
heading: 조건부 가우시안 분포 (3/3)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(1)
D, M = 3, 1  # x_a is the first M elements

mu = rng.normal(size=D)
A_rand = rng.normal(size=(D, D))
Sigma = A_rand @ A_rand.T + D * np.eye(D)  # positive-definite covariance

mu_a, mu_b = mu[:M], mu[M:]
Sigma_aa, Sigma_ab = Sigma[:M, :M], Sigma[:M, M:]
Sigma_ba, Sigma_bb = Sigma[M:, :M], Sigma[M:, M:]

# Conditional mean/covariance using the slide's formula
mu_a_given_b = mu_a + Sigma_ab @ np.linalg.inv(Sigma_bb) @ (mu_b + 0.5 - mu_b)
Sigma_a_given_b = Sigma_aa - Sigma_ab @ np.linalg.inv(Sigma_bb) @ Sigma_ba

# Compare with the Lambda_aa^{-1} formula (also from the slide)
Lambda = np.linalg.inv(Sigma)
Sigma_a_given_b_v2 = np.linalg.inv(Lambda[:M, :M])

print("Conditional covariance via Sigma_ab, Sigma_bb^-1:", np.round(np.diag(Sigma_a_given_b), 4))
print("Conditional covariance via Lambda_aa^-1:         ", np.round(np.diag(Sigma_a_given_b_v2), 4))
print("\nDo both formulas agree?", np.allclose(Sigma_a_given_b, Sigma_a_given_b_v2))
```

</PyRunner>

---
layout: prism
heading: "NOTE: 완전제곱식 만들기"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 가우시안 분포가 다음과 같은 형태를 갖는다는 점에 유의하세요:

$$
\mathcal{N}(x|\mu,\sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{-\frac{1}{2\sigma^2}(x-\mu)^2\right\}\propto\exp\{(x-\mu)^2/\sigma^2\}
$$

- 이제, 다음과 같은 형태의 확률분포를 생각해봅시다:

$$
p(x)\propto\exp\left(-\frac{x^2-6x+10}{2}\right)
$$

<div class="sub-item">

여기서 질문은, 위 분포가 가우시안인가 하는 것입니다.

</div>

---
layout: prism
heading: "NOTE: 완전제곱식 만들기"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 완전제곱식을 이용하면, 주어진 확률분포를 다음과 같이 다시 쓸 수 있습니다:

$$
p(x)\propto\exp\left(-\frac{x^2-6x+10}{2}\right)\propto\exp\left(-\frac{(x-3)^2+1}{2}\right)
$$

<div class="sub-item">

여기서 분자의 상수 $+1$은 정규화에만 영향을 미칠 뿐, 확률분포의 형태에는 영향을 주지 않습니다.

</div>

<div class="sub-item">

따라서, 주어진 확률분포가 가우시안임을 결론지을 수 있습니다:

</div>

$$
p(x)\sim\mathcal{N}(3, 1)
$$

---
layout: prism
heading: 주변 가우시안 분포
---

- 결합확률분포 $p(\mathbf{x}_a,\mathbf{x}_b)$가 가우시안이면, 그 조건부 확률분포 $p(\mathbf{x}_a|\mathbf{x}_b)$ 역시 가우시안임을 살펴보았습니다.

- 마찬가지로, 주변분포 $p(\mathbf{x}_a)$나 $p(\mathbf{x}_b)$ 역시 가우시안이며, 예를 들면

$$
p(\mathbf{x}_a)=\mathcal{N}(\mathbf{x}_a|\boldsymbol{\mu}_a,\boldsymbol{\Sigma}_{aa})
$$

<div class="img-row" style="max-width: 46%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.9a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.9b.png"/>

</div>

---
layout: prism
heading: "가우시안 확률변수에 대한 베이즈 정리 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 선형 가우시안 모델이 있다고 가정하면, 주변분포 $p(\mathbf{x})$와 조건부분포 $p(\mathbf{y}|\mathbf{x})$의 일반적인 형태를 다음과 같이 정의할 수 있습니다:

$$
\begin{aligned}
p(\mathbf{x})&=\mathcal{N}(\mathbf{x}|\boldsymbol{\mu},\boldsymbol{\Lambda}^{-1})\\
p(\mathbf{y}|\mathbf{x})&=\mathcal{N}(\mathbf{y}|\mathbf{A}\mathbf{x}+\mathbf{b}, \mathbf{L}^{-1})
\end{aligned}
$$

<div class="sub-item">

여기서 $\boldsymbol{\mu}$, $\mathbf{A}$, $\mathbf{b}$는 평균을 제어하는 하이퍼파라미터이고, $\boldsymbol{\Lambda}$와 $\mathbf{L}$은 정밀도 행렬입니다.

</div>

---
layout: prism
heading: "가우시안 확률변수에 대한 베이즈 정리 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- 결합분포를 고려하기 위해 $\mathbf{z}=\binom{\mathbf{x}}{\mathbf{y}}$로 정의하고, 로그를 취해봅시다.

$$
\begin{aligned}
\ln p(\mathbf{z})= & \ln p(\mathbf{x})+\ln p(\mathbf{y} | \mathbf{x}) \\
= & -\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top \boldsymbol{\Lambda}(\mathbf{x}-\boldsymbol{\mu})\\& -\frac{1}{2}(\mathbf{y}-\mathbf{A} \mathbf{x}-\mathbf{b})^\top \mathbf{L}(\mathbf{y}-\mathbf{A} \mathbf{x}-\mathbf{b})+\text{const}
\end{aligned}
$$

<div class="sub-item">

이것이 $\mathbf{z}$에 대해 이차식이라는 점에 유의하세요. 이는 $p(\mathbf{z})$가 가우시안임을 의미합니다.

</div>

- 따라서 위 식을 완전제곱식으로 만들어 $\mathbb{E}[\mathbf{z}]$와 $\mathrm{cov}[\mathbf{z}]$를 계산할 수 있습니다.

---
layout: prism
heading: "가우시안 확률변수에 대한 베이즈 정리 (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 최종적으로, 다음과 같은 기댓값과 공분산을 얻을 수 있습니다.

$$
\begin{aligned}
\mathbb{E}[\mathbf{y}] & =\mathbf{A} \boldsymbol{\mu}+\mathbf{b} \\
\mathrm{cov}[\mathbf{y}] & =\mathbf{L}^{-1}+\mathbf{A} \boldsymbol{\Lambda}^{-1} \mathbf{A}^{\top}\\
\mathbb{E}[\mathbf{x} | \mathbf{y}] & =(\boldsymbol{\Lambda}+\mathbf{A}^{\top} \mathbf{L} \mathbf{A})^{-1}\{\mathbf{A}^{\top} \mathbf{L}(\mathbf{y}-\mathbf{b})+\boldsymbol{\Lambda} \boldsymbol{\mu}\} \\
\mathrm{cov}[\mathbf{x} | \mathbf{y}] & =(\boldsymbol{\Lambda}+\mathbf{A}^{\top} \mathbf{L} \mathbf{A})^{-1}
\end{aligned}
$$

---
layout: prism
heading: "가우시안 확률변수에 대한 최대가능도 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 데이터셋 $\mathbf{X}=(\mathbf{x}_1,\ldots,\mathbf{x}_N)^\top$이 주어지고 관측값 $\{\mathbf{x}_n\}$이 다변량 가우시안 분포로부터 독립적으로 샘플링되었다면, 최대가능도 방법을 이용해 원래 분포의 매개변수를 추정할 수 있습니다.

- 로그가능도 함수는 다음과 같습니다:

$$
\begin{aligned}
\ln p(\mathbf{X} | \boldsymbol{\mu}, \boldsymbol{\Sigma})=&-\frac{N D}{2} \ln (2 \pi)-\frac{N}{2} \ln |\boldsymbol{\Sigma}|-\frac{1}{2} \sum_{n=1}^N\left(\mathbf{x}_n-\boldsymbol{\mu}\right)^{\top} \boldsymbol{\Sigma}^{-1}\left(\mathbf{x}_n-\boldsymbol{\mu}\right)
\end{aligned}
$$

<div class="sub-item">

가능도 함수는 다음 항들에만 의존하며, 이는 가우시안 분포의 충분통계량입니다:

</div>

$$
\sum_{n=1}^{N}\mathbf{x}_n,\qquad \sum_{n=1}^{N}\mathbf{x}_n\mathbf{x}_n^\top
$$

---
layout: prism
heading: "가우시안 확률변수에 대한 최대가능도 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- 미분을 수행하면 다음과 같은 해를 얻을 수 있습니다:

$$
\begin{aligned}
\boldsymbol{\mu}_{\mathrm{ML}}&=\frac{1}{N} \sum_{n=1}^N \mathbf{x}_n\\
\boldsymbol{\Sigma}_{\mathrm{ML}}&=\frac{1}{N} \sum_{n=1}^N\left(\mathbf{x}_n-\boldsymbol{\mu}_{\mathrm{ML}}\right)\left(\mathbf{x}_n-\boldsymbol{\mu}_{\mathrm{ML}}\right)^{\top}
\end{aligned}
$$

---
layout: prism
heading: 가우시안 혼합 (1/2)
---

- 가우시안 분포들을 선형적으로 중첩시켜 다봉형 데이터 분포를 모델링할 수 있습니다.

<div class="sub-item">

이러한 관점에서, 충분한 개수의 가우시안 분포를 사용하고 선형결합의 평균, 공분산, 계수를 조절할 수 있다면, _거의 모든_ 연속분포를 임의의 적합도로 추론할 수 있습니다.

</div>

<div class="img-row" style="max-width: 60%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.21a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.21b.png"/>

</div>

---
layout: prism
heading: 가우시안 혼합 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- $K$개의 가우시안 확률밀도의 중첩은 다음과 같이 정의될 수 있습니다

$$
p(\mathbf{x})=\sum_{k=1}^K \pi_k \mathcal{N}\left(\mathbf{x} | \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k\right)
$$

<div class="sub-item">

이를 [가우시안 혼합(mixture of Gaussians)]{.hl}이라고 합니다.

</div>

<div class="sub-item">

각 가우시안 분포 $\mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)$는 혼합의 [성분(component)]{.hl}이라고 불립니다.

</div>

<div class="sub-item">

매개변수 $\pi_k$는 [혼합 계수(mixing coefficients)]{.hl}이며 다음 제약조건을 만족합니다.

</div>

$$
\sum_{k=1}^K \pi_k=1,\qquad 0\leqslant \pi_k \leqslant 1
$$

<div class="subsub-item">

$\pi_k=p(k)$는 $k$번째 성분이 선택될 사전확률이며, 밀도 $\mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)=p(\mathbf{x}|k)$는 $k$가 주어졌을 때 $\mathbf{x}$의 확률입니다.

</div>

<div class="subsub-item">

사후확률 $p(k|\mathbf{x})$는 흔히 [책임값(responsibilities)]{.hl}이라고 불립니다.

</div>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}