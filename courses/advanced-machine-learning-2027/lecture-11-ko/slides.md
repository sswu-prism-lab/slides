---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 11 (KO)
download: true
info: |
  ## 고급 기계학습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-11/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">11주차: 근사 추론</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">커널 방법론</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간고사 복습</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">그래프 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">혼합 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span class="text-gray-900 dark:text-gray-100">근사 추론</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">샘플링 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">연속 잠재 변수</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말고사 복습</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 복습
---

<style>
.slidev-layout ul > li { margin-top: 2em; }
</style>

- K-평균은 할당과 평균 갱신을 번갈아 하며 뒤틀림 $J=\sum_n\sum_k r_{nk}\|\mathbf{x}_n-\boldsymbol{\mu}_k\|^2$를 최소화합니다.

- 가우시안 혼합은 EM으로 학습합니다: E 단계는 책임값 $\gamma(z_{nk})$를 계산하고, M 단계는 $\boldsymbol{\mu}_k$, $\boldsymbol{\Sigma}_k$, $\pi_k$를 재추정합니다.

- $\ln p(\mathbf{X}|\boldsymbol{\theta})=\mathcal{L}(q,\boldsymbol{\theta})+\mathrm{KL}(q\|p)$이므로 EM은 로그 가능도의 하한 $\mathcal{L}(q,\boldsymbol{\theta})$를 최대화합니다.

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">변분 추론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 가우시안 혼합</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 선형 회귀</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 로지스틱 회귀</span></p>
</div>
</div>

---
layout: prism
heading: 변분 추론 (1/4)
---

<style>
.slidev-layout ul > li { margin-top: 2em; }
</style>

- 변분적 방법은 [변분법(calculus of variations)]{.hl}에 기반합니다: [범함수(functional)]{.hl}는 함수를 값으로 사상합니다(예: 엔트로피 $\mathrm{H}[p]=-\int p(x)\ln p(x)\,\mathrm{d}x$).

- 모든 잠재 변수·매개변수 $\mathbf{Z}$와 관측 $\mathbf{X}$를 갖는 완전 베이지안 모델에서, 사후 분포 $p(\mathbf{Z}|\mathbf{X})$와 증거 $p(\mathbf{X})$를 근사합니다.

- 로그 주변 분포는 다음과 같이 분해됩니다:

$$
\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q \| p),\qquad
\mathcal{L}(q)=\int q(\mathbf{Z}) \ln \frac{p(\mathbf{X}, \mathbf{Z})}{q(\mathbf{Z})}\, \mathrm{d}\mathbf{Z}
$$

<div class="sub-item">

하한 $\mathcal{L}(q)$를 $q(\mathbf{Z})$에 대해 최대화하는 것은 KL 발산을 최소화하는 것과 같습니다.

</div>

---
layout: prism
heading: 변분 추론 (2/4)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- 참 사후 분포는 다루기 어려우므로 $q$를 다루기 쉬운 종류로 제한해 최적 원소를 찾습니다. 흔한 선택은 [평균장(mean-field)]{.hl} 인수분해입니다:

$$
q(\mathbf{Z})=\prod_{i=1}^{M}q_i(\mathbf{Z}_i)
$$

- 각 인자에 대해 $\mathcal{L}(q)$를 자유 형태로 최적화하면 최적 인자를 얻습니다:

$$
\ln q_j^{\star}(\mathbf{Z}_j)=\mathbb{E}_{i \neq j}[\ln p(\mathbf{X}, \mathbf{Z})]+\text{const}
$$

<div class="sub-item">

각 인자가 다른 인자들의 기댓값에 의존하므로 순환적으로 갱신합니다.

</div>

---
layout: prism
heading: 변분 추론 (3/4)
---

<div style="display:grid; grid-template-columns: 1.5fr 1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- $\mathrm{KL}(q\|p)$ 최소화는 [최빈값 탐색(mode-seeking)]{.hl}이고, 역방향 $\mathrm{KL}(p\|q)$ 최소화는 [질량 덮기(mass-covering)]{.hl}입니다.

- 상관된 가우시안을 인수분해된 $q$로 근사하면 평균은 정확하지만 분산은 [과소평가(underestimated)]{.hl}됩니다(인수분해 근사는 가장 작은 조건부 분산으로 수축).

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.9a.png" class="img-center" style="width: 15rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: 변분 추론 (4/4)
---

<PyRunner>

```python
import numpy as np
mu = np.array([0.0, 0.0])
Lam = np.array([[2.0, 1.6], [1.6, 2.0]])       # precision (highly correlated)
Sigma = np.linalg.inv(Lam)
m = np.array([2.0, -1.0])
for it in range(30):                            # mean-field fixed-point updates
    m1 = mu[0] - Lam[0,0]**-1 * Lam[0,1]*(m[1]-mu[1])
    m2 = mu[1] - Lam[1,1]**-1 * Lam[1,0]*(m1-mu[0])
    new = np.array([m1, m2])
    if np.linalg.norm(new-m) < 1e-12: m = new; break
    m = new
print("converged mean q :", np.round(m, 4).tolist(), " (true mean [0, 0])")
print("q variance (axes):", [round(float(1/Lam[0,0]),4), round(float(1/Lam[1,1]),4)])
print("true marginal var:", [round(float(Sigma[0,0]),4), round(float(Sigma[1,1]),4)])
print("-> variational q underestimates the marginal variance")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 추론</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">변분 가우시안 혼합</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 선형 회귀</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 로지스틱 회귀</span></p>
</div>
</div>

---
layout: prism
heading: 변분 가우시안 혼합 (1/2)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 4.5em; }
</style>

- 베이지안 가우시안 혼합에는 켤레 사전 분포를 둡니다: $\boldsymbol{\pi}$에는 디리클레, $(\boldsymbol{\mu},\boldsymbol{\Lambda})$에는 가우시안–위샤트.

$$
p(\boldsymbol{\pi})=\operatorname{Dir}(\boldsymbol{\pi}|\boldsymbol{\alpha}_0)
$$

$$
p(\boldsymbol{\mu},\boldsymbol{\Lambda})=\prod_{k}\mathcal{N}(\boldsymbol{\mu}_k|\mathbf{m}_0,(\beta_0\boldsymbol{\Lambda}_k)^{-1})\,\mathcal{W}(\boldsymbol{\Lambda}_k|\mathbf{W}_0,\nu_0)
$$

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure10.5.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: 변분 가우시안 혼합 (2/2)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- $q(\mathbf{Z},\boldsymbol{\pi},\boldsymbol{\mu},\boldsymbol{\Lambda})=q(\mathbf{Z})\,q(\boldsymbol{\pi},\boldsymbol{\mu},\boldsymbol{\Lambda})$로 인수분해합니다. 최적 잠재 인자는:

$$
q^{\star}(\mathbf{Z})=\prod_{n=1}^N \prod_{k=1}^K r_{n k}^{z_{n k}},\qquad r_{nk}=\frac{\rho_{nk}}{\sum_j \rho_{nj}}
$$

<div class="sub-item">

$r_{nk}=\mathbb{E}[z_{nk}]$가 책임값 역할을 합니다.

</div>

- 책임값 가중 통계량 $N_k$, $\overline{\mathbf{x}}_k$, $\mathbf{S}_k$는 EM의 것과 같은 형태이지만, 이제 점 추정 대신 매개변수에 대한 분포를 갱신합니다.

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 추론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 가우시안 혼합</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">변분 선형 회귀</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 로지스틱 회귀</span></p>
</div>
</div>

---
layout: prism
heading: 변분 선형 회귀 (1/2)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- 가능도와 사전 분포:

$$
p(\boldsymbol{\mathsf{t}}|\mathbf{w})=\prod_{n}\mathcal{N}(t_n|\mathbf{w}^{\top}\boldsymbol{\phi}_n,\beta^{-1}),\quad
p(\mathbf{w}|\alpha)=\mathcal{N}(\mathbf{w}|\mathbf{0},\alpha^{-1}\mathbf{I})
$$

$$
p(\alpha)=\operatorname{Gam}(\alpha|a_0,b_0)
$$

- 결합 분포: $p(\boldsymbol{\mathsf{t}},\mathbf{w},\alpha)=p(\boldsymbol{\mathsf{t}}|\mathbf{w})p(\mathbf{w}|\alpha)p(\alpha)$.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure10.8.png" class="img-center" style="width: 15rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: 변분 선형 회귀 (2/2)
---

<style>
.slidev-layout ul > li { margin-top: 3.3em; }
</style>

- $q(\mathbf{w},\alpha)=q(\mathbf{w})q(\alpha)$로 인수분해합니다. 정밀도 인자는 감마 분포입니다:

$$
q^{\star}(\alpha)=\operatorname{Gam}(\alpha|a_N,b_N),\quad a_N=a_0+\tfrac{M}{2},\quad b_N=b_0+\tfrac{1}{2}\mathbb{E}[\mathbf{w}^{\top}\mathbf{w}]
$$

- 가중치 인자는 가우시안입니다:

$$
q^{\star}(\mathbf{w})=\mathcal{N}(\mathbf{w}|\mathbf{m}_N,\mathbf{S}_N),\quad
\mathbf{m}_N=\beta\mathbf{S}_N\boldsymbol{\Phi}^{\top}\boldsymbol{\mathsf{t}},\quad
\mathbf{S}_N=(\mathbb{E}[\alpha]\mathbf{I}+\beta\boldsymbol{\Phi}^{\top}\boldsymbol{\Phi})^{-1}
$$

<div class="sub-item">

증거 최대화 EM과 같은 형태이지만, $\alpha$의 점 추정이 $\mathbb{E}[\alpha]$로 대체됩니다.

</div>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 추론</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 가우시안 혼합</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">변분 선형 회귀</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">변분 로지스틱 회귀</span></p>
</div>
</div>

---
layout: prism
heading: 변분 로지스틱 회귀 (1/3)
---

<style>
.slidev-layout ul > li { margin-top: 3.3em; }
</style>

- 주변 가능도 $p(\boldsymbol{\mathsf{t}})=\int \prod_n p(t_n|\mathbf{w})\,p(\mathbf{w})\,\mathrm{d}\mathbf{w}$는 다룰 수 없습니다. $a=\mathbf{w}^{\top}\boldsymbol{\phi}$인 $p(t|\mathbf{w})=e^{at}\sigma(-a)$에 변분 시그모이드 하한을 적용합니다:

$$
\sigma(z) \geqslant \sigma(\xi) \exp\{(z-\xi)/2-\lambda(\xi)(z^2-\xi^2)\},\quad \lambda(\xi)=\frac{1}{2\xi}\Big[\sigma(\xi)-\frac{1}{2}\Big]
$$

- 관측마다 변분 매개변수 $\xi_n$을 하나씩 두면 결합 하한이 $\mathbf{w}$에 대한 이차식이 되어 사후 분포의 가우시안 근사를 줍니다.

---
layout: prism
heading: 변분 로지스틱 회귀 (2/2)
---

<style>
.slidev-layout ul > li { margin-top: 3.3em; }
</style>

- 가우시안 사후 근사는:

$$
q(\mathbf{w})=\mathcal{N}(\mathbf{w}|\mathbf{m}_N,\mathbf{S}_N),\quad
\mathbf{S}_N^{-1}=\mathbf{S}_0^{-1}+2\sum_{n}\lambda(\xi_n)\boldsymbol{\phi}_n\boldsymbol{\phi}_n^{\top}
$$

- 변분 매개변수 $\xi_n$은 (예: EM으로) 다음 갱신으로 최적화합니다:

$$
(\xi_n^{\mathrm{new}})^2=\boldsymbol{\phi}_n^{\top}(\mathbf{S}_N+\mathbf{m}_N\mathbf{m}_N^{\top})\boldsymbol{\phi}_n
$$

<div class="sub-item">

예측 분포는 $q(\mathbf{w})$에 대해 주변화해 얻습니다.

</div>

---
layout: prism
heading: 변분 로지스틱 회귀 (3/3)
---

<PyRunner>

```python
import numpy as np
def sig(z): return 1/(1+np.exp(-z))
def lam(xi): return (sig(xi)-0.5)/(2*xi)
def bound(z, xi): return sig(xi)*np.exp((z-xi)/2 - lam(xi)*(z**2-xi**2))
xi = 2.0
print(f"variational sigmoid bound (xi = {xi}; tight at z = +/-xi)")
print(f"  {'z':>4} {'sigma(z)':>9} {'bound':>9} {'gap':>9}")
for z in [-3, -2, -1, 0, 1, 2, 3]:
    print(f"  {z:>4} {sig(z):>9.4f} {bound(z, xi):>9.4f} {sig(z)-bound(z, xi):>9.5f}")
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
