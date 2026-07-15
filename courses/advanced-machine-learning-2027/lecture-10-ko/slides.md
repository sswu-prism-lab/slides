---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 10 (KO)
download: true
info: |
  ## 고급 기계학습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-10/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">10주차: 혼합 모델</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span class="text-gray-900 dark:text-gray-100">혼합 모델</span></p>
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
.slidev-layout ul > li { margin-top: 3em; }
</style>

- 방향성 그래프 모델은 결합 분포를 다음과 같이 인수분해합니다:

$$
p(\mathbf{x})=\prod_{k=1}^{K}p(x_k|\mathrm{pa}_k)
$$

<div class="sub-item">

$\mathrm{pa}_k$는 $x_k$의 부모이며, 그래프는 방향성 비순환 그래프여야 합니다.

</div>

- 링크를 제거하거나, 매개변수를 매듭으로 묶거나, 매개변수화된 조건부 분포(예: 부모들의 로지스틱 시그모이드)를 써서 매개변수 수를 줄입니다.

---
layout: prism
heading: 복습 (2/2)
---

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- 조건부 독립 $a\perp\!\!\!\perp b\mid c$는 [d 분리(d-separation)]{.hl}로 그래프에서 읽어낼 수 있습니다.

- 꼬리 대 꼬리·머리 대 꼬리 노드는 관측되면 경로를 [막고(block)]{.hl}, 머리 대 머리 노드는 관측되지 않으면 막고 관측되면(또는 자손이 관측되면) 엽니다.

- 비방향성 그래프(마르코프 무작위장)는 부모–자식 비대칭을 없앱니다: $A$에서 $B$로 가는 모든 경로가 $C$를 지나면 $A\perp\!\!\!\perp B\mid C$입니다.

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">K-평균 군집화</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가우시안 혼합</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">EM 알고리즘</span></p>
</div>
</div>

---
layout: prism
heading: K-평균 군집화 (1/4)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- $N$개 관측값 $\{\mathbf{x}_1,\ldots,\mathbf{x}_N\}$을 $K$개 군집으로 나눕니다. 각 군집 중심인 [원형(prototype)]{.hl} $\boldsymbol{\mu}_k$를 도입합니다.

- 원 핫 할당 $r_{nk}\in\{0,1\}$로 [뒤틀림 척도(distortion measure)]{.hl}를 최소화합니다:

$$
J=\sum_{n=1}^N \sum_{k=1}^K r_{n k}\left\|\mathbf{x}_n-\boldsymbol{\mu}_k\right\|^2
$$

- 두 단계를 번갈아 합니다: $\boldsymbol{\mu}_k$를 고정하고 $r_{nk}$를 최적화한 뒤, $r_{nk}$를 고정하고 $\boldsymbol{\mu}_k$를 최적화합니다([EM 알고리즘(EM algorithm)]{.hl}의 E·M 단계).

---
layout: prism
heading: K-평균 군집화 (2/4)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- 할당 단계(E): 각 점을 가장 가까운 원형에 배정합니다,

$$
r_{nk}=\begin{cases}1 & k=\arg\min_j\|\mathbf{x}_n-\boldsymbol{\mu}_j\|^2\\ 0 & \text{otherwise}\end{cases}
$$

- 갱신 단계(M): $J$를 $\boldsymbol{\mu}_k$로 미분하면 군집 평균이 됩니다,

$$
\boldsymbol{\mu}_k=\frac{\sum_n r_{nk}\mathbf{x}_n}{\sum_n r_{nk}}
$$

<div class="sub-item">

제곱 거리를 일반 거리 $\mathcal{V}(\cdot,\cdot)$로 바꾸면 [K-메도이드(K-medoids)]{.hl} 알고리즘이 됩니다.

</div>

---
layout: prism
heading: K-평균 군집화 (3/4)
---

<div class="img-row" style="max-width: 82%">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.1a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.1b.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.1c.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.1d.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.1e.png"/>
</div>

<div class="img-row" style="max-width: 82%">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.1f.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.1g.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.1h.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.1i.png"/>
</div>

---
layout: prism
heading: K-평균 군집화 (4/4)
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)
X = np.vstack([rng.normal([0,0], 0.6, (80,2)),
               rng.normal([3,3], 0.6, (80,2)),
               rng.normal([0,3], 0.6, (80,2))])
K = 3; mu = X[rng.choice(len(X), K, replace=False)].copy(); prev = None
for it in range(12):
    d = ((X[:,None,:]-mu[None,:,:])**2).sum(2); r = d.argmin(1)   # E: assign
    J = d[np.arange(len(X)), r].sum()
    for k in range(K):
        if (r==k).any(): mu[k] = X[r==k].mean(0)                  # M: update
    print(f"iter {it+1}: distortion J = {J:.2f}")
    if prev is not None and abs(J-prev) < 1e-9: break
    prev = J
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">K-평균 군집화</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">가우시안 혼합</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">EM 알고리즘</span></p>
</div>
</div>

---
layout: prism
heading: 가우시안 혼합 (1/3)
---

<style>
.slidev-layout ul > li { margin-top: 1.5em; }
</style>

- 가우시안 혼합은 가우시안들의 선형 중첩입니다:

$$
p(\mathbf{x})=\sum_{k=1}^K \pi_k \mathcal{N}\left(\mathbf{x} | \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k\right)
$$

- 원 핫 잠재 변수 $\mathbf{z}$를 $p(z_k=1)=\pi_k$로 도입하면 $p(\mathbf{z})=\prod_k\pi_k^{z_k}$이고 $p(\mathbf{x}|\mathbf{z})=\prod_k\mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)^{z_k}$입니다.

- $\mathbf{z}$를 주변화하면 혼합이 복원됩니다:

$$
p(\mathbf{x})=\sum_{\mathbf{z}} p(\mathbf{z}) p(\mathbf{x} | \mathbf{z})=\sum_{k=1}^K \pi_k \mathcal{N}\left(\mathbf{x} | \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k\right)
$$

---
layout: prism
heading: 가우시안 혼합 (2/3)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- $\mathbf{x}$가 주어지면 $\mathbf{z}$의 사후 분포가 성분 $k$의 [책임값(responsibility)]{.hl}입니다:

$$
\gamma(z_k)=p(z_k=1|\mathbf{x})=\frac{\pi_k \mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)}{\sum_{j} \pi_j \mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_j,\boldsymbol{\Sigma}_j)}
$$

<div class="sub-item">

$\gamma(z_k)$는 성분 $k$가 관측 $\mathbf{x}$를 얼마나 설명하는지를 나타냅니다.

</div>

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.5a.png" class="img-center" style="width: 10rem;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.5b.png" class="img-center" style="width: 10rem;" />
</div>
</div>

---
layout: prism
heading: 가우시안 혼합 (3/3)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- 혼합의 로그 가능도는:

$$
\ln p(\mathbf{X} | \boldsymbol{\pi}, \boldsymbol{\mu}, \boldsymbol{\Sigma})=\sum_{n=1}^N \ln \Big\{\sum_{k=1}^K \pi_k \mathcal{N}(\mathbf{x}_n | \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)\Big\}
$$

- 직접 최대 가능도는 [특이점(singularity)]{.hl} 문제를 겪습니다: 한 성분이 한 점으로 붕괴하면($\sigma_j\to0$) 로그 가능도가 발산합니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.6.png" class="img-center" style="width: 14rem;" />
</div>
</div>

---
layout: prism
heading: 가우시안 혼합을 위한 EM (1/3)
---

<style>
.slidev-layout ul > li { margin-top: 2.2em; }
</style>

- 로그 가능도의 미분을 0으로 두면 갱신식을 얻습니다($N_k=\sum_n\gamma(z_{nk})$):

$$
\boldsymbol{\mu}_k=\frac{1}{N_k}\sum_{n} \gamma(z_{nk})\mathbf{x}_n,\qquad
\boldsymbol{\Sigma}_k=\frac{1}{N_k}\sum_{n}\gamma(z_{nk})(\mathbf{x}_n-\boldsymbol{\mu}_k)(\mathbf{x}_n-\boldsymbol{\mu}_k)^{\top}
$$

- $\sum_k\pi_k=1$에 대한 라그랑주 승수를 쓰면:

$$
\pi_k=\frac{N_k}{N}
$$

<div class="sub-item">

$\gamma(z_{nk})$가 매개변수에 의존하므로 닫힌 형태가 아니어서 반복합니다.

</div>

---
layout: prism
heading: 가우시안 혼합을 위한 EM (2/3)
---

<div style="display:grid; grid-template-columns: 1.4fr 1.6fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2em; }
</style>
- E 단계: 현재 매개변수로 책임값을 계산합니다.

- M 단계: $\boldsymbol{\mu}_k$, $\boldsymbol{\Sigma}_k$, $\pi_k$를 재추정합니다.

- 보통 K-평균으로 먼저 초기화한 뒤 EM을 돌립니다. 로그 가능도는 여러 지역 최댓값을 가질 수 있습니다.

</div>
<div>
<div class="img-row" style="max-width: 100%">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.8a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.8b.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.8c.png"/>
</div>
<div class="img-row" style="max-width: 100%">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.8d.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.8e.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.8f.png"/>
</div>
</div>
</div>

---
layout: prism
heading: 가우시안 혼합 — (3/3)
---

<PyRunner>

```python
import numpy as np
def gauss(X, mu, S):
    D = X.shape[1]; d = X-mu; Si = np.linalg.inv(S)
    return np.exp(-0.5*np.einsum('ni,ij,nj->n', d, Si, d))/np.sqrt((2*np.pi)**D*np.linalg.det(S))
rng = np.random.default_rng(1)
X = np.vstack([rng.multivariate_normal([0,0], [[0.5,0],[0,0.5]], 120),
               rng.multivariate_normal([3,3], [[0.6,0.3],[0.3,0.6]], 120)])
K = 2; N = len(X)
mu = X[rng.choice(N, K, replace=False)].copy(); S = [np.eye(2) for _ in range(K)]; pi = np.ones(K)/K
prev = -np.inf
for it in range(40):
    R = np.stack([pi[k]*gauss(X, mu[k], S[k]) for k in range(K)], 1)    # E step
    ll = np.log(R.sum(1)).sum(); R = R/R.sum(1, keepdims=True); Nk = R.sum(0)
    for k in range(K):                                                  # M step
        mu[k] = (R[:,k,None]*X).sum(0)/Nk[k]
        d = X-mu[k]; S[k] = (R[:,k,None,None]*np.einsum('ni,nj->nij', d, d)).sum(0)/Nk[k]
    pi = Nk/N
    if it < 3 or it % 6 == 0: print(f"iter {it+1:2d}: log-likelihood = {ll:.2f}")
    if ll-prev < 1e-6: print(f"converged (iter {it+1})"); break
    prev = ll
print("estimated pi:", np.round(pi,3).tolist(), " means:", np.round(mu,2).tolist())
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">K-평균 군집화</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">가우시안 혼합</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">EM 알고리즘</span></p>
</div>
</div>

---
layout: prism
heading: 일반적인 EM 알고리즘 (1/3)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- EM은 잠재 변수를 가진 모델의 최대 가능도 해를 찾아 $p(\mathbf{X}|\boldsymbol{\theta})=\sum_{\mathbf{Z}} p(\mathbf{X},\mathbf{Z}|\boldsymbol{\theta})$를 최대화합니다.

- 분포 $q(\mathbf{Z})$를 도입하면 로그 가능도가 분해됩니다:

$$
\ln p(\mathbf{X} | \boldsymbol{\theta})=\mathcal{L}(q, \boldsymbol{\theta})+\mathrm{KL}(q \| p)
$$

$$
\mathcal{L}(q, \boldsymbol{\theta})=\sum_{\mathbf{Z}} q(\mathbf{Z}) \ln \frac{p(\mathbf{X}, \mathbf{Z} | \boldsymbol{\theta})}{q(\mathbf{Z})},\qquad
\mathrm{KL}(q \| p)=-\sum_{\mathbf{Z}} q(\mathbf{Z}) \ln \frac{p(\mathbf{Z} | \mathbf{X}, \boldsymbol{\theta})}{q(\mathbf{Z})}
$$

<div class="sub-item">

$\mathrm{KL}\geqslant 0$이므로 $\mathcal{L}(q,\boldsymbol{\theta})$는 로그 가능도의 하한입니다.

</div>

---
layout: prism
heading: 일반적인 EM 알고리즘 (2/3)
---

<div style="display:grid; grid-template-columns: 1.5fr 1fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- E 단계: $\boldsymbol{\theta}^{\mathrm{old}}$를 고정하고 $\mathcal{L}$을 $q$에 대해 최대화합니다. $q(\mathbf{Z})=p(\mathbf{Z}|\mathbf{X},\boldsymbol{\theta}^{\mathrm{old}})$가 되어 $\mathrm{KL}=0$이고 하한이 로그 가능도에 닿습니다.

- M 단계: $q$를 고정하고 $\mathcal{L}$을 $\boldsymbol{\theta}$에 대해 최대화합니다. 하한(과 로그 가능도)이 증가하며, $q$가 새 사후 분포와 달라져 $\mathrm{KL}>0$이 됩니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.11.png" class="img-center" style="width: 12rem; margin-bottom: 4rem" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.13.png" class="img-center" style="width: 12rem;" />
</div>
</div>

---
layout: prism
heading: 일반적인 EM 알고리즘 (3/3)
---

<PyRunner>

```python
import numpy as np
def gauss(X, mu, S):
    D = X.shape[1]; d = X-mu; Si = np.linalg.inv(S)
    return np.exp(-0.5*np.einsum('ni,ij,nj->n', d, Si, d))/np.sqrt((2*np.pi)**D*np.linalg.det(S))
rng = np.random.default_rng(3)
X = np.vstack([rng.multivariate_normal([0,0], np.eye(2)*0.4, 50),
               rng.multivariate_normal([2.5,2.5], np.eye(2)*0.4, 50)])
K = 2; mu = np.array([[0.5,0.0],[2.0,2.0]]); S = [np.eye(2)*0.5]*2; pi = np.array([0.5,0.5])
px = np.stack([pi[k]*gauss(X, mu[k], S[k]) for k in range(K)], 1)
lnpX = np.log(px.sum(1)).sum(); post = px/px.sum(1, keepdims=True)      # posterior
def elbo(q):
    L = KL = 0.0
    for k in range(K):
        m = q[:,k] > 1e-12
        L  += np.sum(q[m,k]*(np.log(px[m,k]) - np.log(q[m,k])))
        KL += np.sum(q[m,k]*(np.log(q[m,k]) - np.log(post[m,k])))
    return L, KL
Lb, KLb = elbo(np.full_like(post, 0.5))      # arbitrary q
Lg, KLg = elbo(post)                          # q = posterior
print(f"ln p(X)          = {lnpX:.3f}")
print(f"arbitrary q : L={Lb:.3f}, KL={KLb:.3f}, L+KL={Lb+KLb:.3f}")
print(f"q=posterior : L={Lg:.3f}, KL={KLg:.3f}, L+KL={Lg+KLg:.3f}  (KL~0)")
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
