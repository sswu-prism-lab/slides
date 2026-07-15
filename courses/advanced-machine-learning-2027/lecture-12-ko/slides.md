---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 12 (KO)
download: true
info: |
  ## 고급 기계학습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-12/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">12주차: 샘플링 기법</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">근사 추론</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span class="text-gray-900 dark:text-gray-100">샘플링 기법</span></p>
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
.slidev-layout ul > li { margin-top: 3em; }
</style>

- 변분 추론은 로그 증거를 $\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p)$로 분해하고 하한 $\mathcal{L}(q)$를 최대화합니다.

- $q$를 다루기 쉬운 종류, 흔히 평균장 인수분해 $q(\mathbf{Z})=\prod_i q_i(\mathbf{Z}_i)$로 제한합니다.

- $\mathrm{KL}(q\|p)$는 최빈값 탐색, $\mathrm{KL}(p\|q)$는 질량 덮기이며, 더 다루기 쉬운 기본 KL을 주로 씁니다.

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">샘플링 알고리즘</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">마르코프 연쇄 몬테카를로</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">기타 샘플링</span></p>
</div>
</div>

---
layout: prism
heading: 샘플링 알고리즘
---

<style>
.slidev-layout ul > li { margin-top: 3.8em; }
</style>

- $p(\mathbf{z})$ 하에서 $f(\mathbf{z})$의 기댓값을, 표본 $\mathbf{z}^{(l)}$에 대한 유한 합으로 추정합니다:

$$
\widehat{f}=\frac{1}{L} \sum_{l=1}^L f(\mathbf{z}^{(l)}),\qquad
\operatorname{var}[\widehat{f}]=\frac{1}{L} \mathbb{E}[(f-\mathbb{E}[f])^2]
$$

- 보통 독립 표본 수십 개면 충분하지만, 상관된 표본은 더 많이 필요합니다.

---
layout: prism
heading: 표준 분포
---

<div style="display:grid; grid-template-columns: 1.5fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- 균등 난수 $z\in(0,1)$을 $y=f(z)$로 변환하면 $p(y)=p(z)|\mathrm{d}z/\mathrm{d}y|$입니다.

- 누적 분포 $h(y)=\int_{-\infty}^y p(\widehat{y})\,\mathrm{d}\widehat{y}$의 역함수 $f=h^{-1}$을 쓰면 원하는 $p(y)$를 얻습니다 — [역변환(inverse transform)]{.hl} 표집.

<div class="sub-item">

지수 분포 $p(y)=\lambda e^{-\lambda y}$는 $y=-\lambda^{-1}\ln(1-z)$로 생성합니다.

</div>

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure11.2.png" class="img-center" style="width: 15rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: 거부 샘플링
---

<div style="display:grid; grid-template-columns: 1.4fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- $Z_p$를 모르는 $p(z)=\widetilde{p}(z)/Z_p$를 표집하려면, [제안 분포(proposal distribution)]{.hl} $q(z)$와 $kq(z)\geqslant\widetilde{p}(z)$인 상수 $k$를 씁니다.

- $z_0\sim q$, $u_0\sim \mathcal{U}[0,kq(z_0)]$을 뽑고 $u_0>\widetilde{p}(z_0)$이면 거부합니다. 승인된 표본은 $p(z)$를 따릅니다.

- 승인 확률: $p(a)=\dfrac{1}{k}\int\widetilde{p}(z)\,\mathrm{d}z$.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure11.4.png" class="img-center" style="width: 20rem;" />
</div>
</div>

---
layout: prism
heading: 중요도 샘플링
---

<div style="display:grid; grid-template-columns: 1.4fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- [중요도 샘플링(importance sampling)]{.hl}은 제안 분포 $q$와 [중요도 가중치(importance weights)]{.hl} $r_l=p(\mathbf{z}^{(l)})/q(\mathbf{z}^{(l)})$로 기댓값을 직접 근사합니다:

$$
\mathbb{E}[f]=\int f(\mathbf{z}) \frac{p(\mathbf{z})}{q(\mathbf{z})} q(\mathbf{z})\, \mathrm{d}\mathbf{z} \simeq \frac{1}{L} \sum_{l=1}^L \frac{p(\mathbf{z}^{(l)})}{q(\mathbf{z}^{(l)})} f(\mathbf{z}^{(l)})
$$

- 가중치는 잘못된 분포에서 표집해 생긴 편향을 보정합니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure11.8.png" class="img-center" style="width: 20rem;" />
</div>
</div>

---
layout: prism
heading: 샘플링 알고리즘 다시 보기
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)
def ptil(z):                                            # unnormalized bimodal target
    return 0.6*np.exp(-(z+1)**2/(2*0.5**2)) + 0.4*np.exp(-(z-1.5)**2/(2*0.4**2))
sq = 1.5
def q(z): return np.exp(-z**2/(2*sq**2))/np.sqrt(2*np.pi*sq**2)
zg = np.linspace(-5, 5, 2001); dz = zg[1]-zg[0]
k = np.max(ptil(zg)/q(zg))*1.02                         # kq(z) >= p~(z)
L = 200000; z0 = rng.normal(0, sq, L); u = rng.uniform(0, k*q(z0), L)
acc = u <= ptil(z0); zs = z0[acc]
Zp = np.sum(ptil(zg))*dz
print(f"k = {k:.3f}, acceptance = {acc.mean():.3f} (theory (1/k)*int p~ = {Zp/k:.3f})")
print(f"accepted-sample mean = {zs.mean():.3f} (true mean = {np.sum(zg*ptil(zg))*dz/Zp:.3f})")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">샘플링 알고리즘</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">마르코프 연쇄 몬테카를로</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">기타 샘플링</span></p>
</div>
</div>

---
layout: prism
heading: 마르코프 연쇄 몬테카를로 (1/2)
---

<style>
.slidev-layout ul > li { margin-top: 3.8em; }
</style>

- 거부·중요도 샘플링은 고차원에서 어렵습니다. [마르코프 연쇄 몬테카를로(Markov chain Monte Carlo; MCMC)]{.hl}는 현재 상태에 의존하는 제안 분포 $q(\mathbf{z}|\mathbf{z}^{(\tau)})$에서 표집하므로 표본이 마르코프 연쇄를 이룹니다.

- [메트로폴리스 알고리즘(Metropolis algorithm)]{.hl}은 대칭 제안 분포를 가정하고 다음 확률로 후보를 승인합니다:

$$
A(\mathbf{z}^{\star}, \mathbf{z}^{(\tau)})=\min\Big(1, \frac{\widetilde{p}(\mathbf{z}^{\star})}{\widetilde{p}(\mathbf{z}^{(\tau)})}\Big)
$$

<div class="sub-item">

$u\sim\mathcal{U}(0,1)$을 뽑아 $A>u$이면 승인하고, 아니면 현재 상태를 유지합니다.

</div>

---
layout: prism
heading: 마르코프 연쇄 몬테카를로 (2/2)
---

<style>
.slidev-layout ul > li { margin-top: 1em; }
</style>

- [메트로폴리스–헤이스팅스 알고리즘(Metropolis–Hastings algorithm)]{.hl}은 비대칭 제안 분포로 일반화하며 제안 비율을 보정합니다:

$$
A_k(\mathbf{z}^{\star}, \mathbf{z}^{(\tau)})=\min\Big(1, \frac{\widetilde{p}(\mathbf{z}^{\star}) q_k(\mathbf{z}^{(\tau)} | \mathbf{z}^{\star})}{\widetilde{p}(\mathbf{z}^{(\tau)}) q_k(\mathbf{z}^{\star} | \mathbf{z}^{(\tau)})}\Big)
$$

<div class="sub-item">

$k$는 고려하는 전이 집합 내에서 각 전이를 가리키는 라벨입니다.

</div>

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(3)
def ptil(z): return 0.5*np.exp(-(z+2)**2/(2*0.5**2)) + 0.5*np.exp(-(z-2)**2/(2*0.5**2))
L = 100000; step = 1.5; z = 0.0; samples = np.empty(L); nacc = 0
for t in range(L):
    zstar = z + rng.normal(0, step)                     # symmetric random-walk proposal
    if rng.uniform() < min(1, ptil(zstar)/ptil(z)):     # Metropolis acceptance
        z = zstar; nacc += 1
    samples[t] = z
s = samples[2000:]                                      # discard burn-in
print(f"acceptance rate = {nacc/L:.3f}")
print(f"sample mean = {s.mean():+.3f} (true 0), sample var = {s.var():.3f} (true {0.25+4:.2f})")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">샘플링 알고리즘</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">마르코프 연쇄 몬테카를로</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">기타 샘플링</span></p>
</div>
</div>

---
layout: prism
heading: 기브스 샘플링
---

- [기브스 샘플링(Gibbs sampling)]{.hl}은 메트로폴리스–헤이스팅스의 특수한 경우로, 간단하고 널리 쓰입니다.

- $p(\mathbf{z})=p(z_1,\ldots,z_M)$에 대해 각 변수를 나머지가 주어졌을 때의 조건부 분포에서 차례로 갱신합니다:

$$
z_j^{(\tau+1)} \sim p(z_j | z_1^{(\tau+1)}, \ldots, z_{j-1}^{(\tau+1)}, z_{j+1}^{(\tau)}, \ldots, z_M^{(\tau)})
$$

<div class="sub-item">

모든 제안이 승인되므로(승인 확률 $1$) 거부가 없습니다.

</div>

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(4)
rho = 0.8; L = 100000; z1 = z2 = 0.0; S = np.empty((L, 2))
for t in range(L):
    z1 = rng.normal(rho*z2, np.sqrt(1-rho**2))          # z1 | z2 ~ N(rho z2, 1-rho^2)
    z2 = rng.normal(rho*z1, np.sqrt(1-rho**2))          # z2 | z1 ~ N(rho z1, 1-rho^2)
    S[t] = [z1, z2]
S = S[1000:]                                            # discard burn-in
c = np.cov(S.T)
print("sample mean  :", np.round(S.mean(0), 3).tolist(), "(true [0, 0])")
print(f"sample cov   : [[{c[0,0]:.3f}, {c[0,1]:.3f}], [{c[1,0]:.3f}, {c[1,1]:.3f}]]  (off-diag ~ {rho})")
```

</PyRunner>

---
layout: prism
heading: 조각 샘플링
---

<div style="display:grid; grid-template-columns: 1.3fr 1.2fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- 메트로폴리스는 단계 크기에 민감합니다. [조각 샘플링(slice sampling)]{.hl}은 보조 변수 $u$로 단계 크기를 자동 조절합니다:

$$
\widehat{p}(z, u)=\begin{cases}1/Z_p & 0\leqslant u\leqslant\widetilde{p}(z)\\ 0 & \text{otherwise}\end{cases}
$$

- $u$를 주변화하면 $p(z)$가 복원됩니다. $u\in[0,\widetilde{p}(z)]$을 뽑고, 조각 $\{z:\widetilde{p}(z)>u\}$에서 $z$를 균등 표집하는 것을 번갈아 합니다.

</div>
<div>
<div class="img-row" style="max-width: 100%">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure11.13a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure11.13b.png"/>
</div>
</div>
</div>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
