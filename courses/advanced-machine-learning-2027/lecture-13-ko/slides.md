---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 13 (KO)
download: true
info: |
  ## 고급 기계학습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-13/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">13주차: 연속 잠재 변수</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">샘플링 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span class="text-gray-900 dark:text-gray-100">연속 잠재 변수</span></p>
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

- 역변환·거부·중요도 샘플링은 제안 분포로부터 표본을 생성(또는 기댓값을 추정)합니다.

- MCMC(메트로폴리스 / 메트로폴리스–헤이스팅스)는 표본의 마르코프 연쇄를 만들며, 표적 비율에 기반한 확률로 후보를 승인합니다.

- 기브스 샘플링은 각 변수를 완전 조건부 분포에서 갱신하고, 조각 샘플링은 단계 크기를 자동으로 조절합니다.

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">주성분 분석</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률적 주성분 분석</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">커널 주성분 분석</span></p>
</div>
</div>

---
layout: prism
heading: 주성분 분석 (1/3)
---

<div style="display:grid; grid-template-columns: 1.4fr 1.6fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- 데이터는 흔히 저차원 매니폴드 근처에 놓입니다. $64\times64$ 숫자를 $100\times100$ 이미지에 넣으면 [자유도(degrees of freedom)]{.hl}가 3(두 방향 이동 + 회전)이므로 [내재적 차원(intrinsic dimensionality)]{.hl}은 3입니다.

- [주성분 분석(Principal component analysis; PCA)]{.hl}은 가장 단순한 연속 잠재 변수 모델로, 차원 감소·압축·시각화에 쓰입니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.1.png" class="img-center" style="width: 25rem;" />
</div>
</div>

---
layout: prism
heading: 주성분 분석 (2/3)
---

<div style="display:grid; grid-template-columns: 1.6fr 1.4fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- PCA는 두 가지 동등한 정의를 가집니다:

<div class="sub-item-enum">

1. 투영 분산을 최대화하는 [주 부분공간(principal subspace)]{.hl}으로 데이터를 직교 투영한다;
2. 평균 제곱 투영 비용을 최소화하는 선형 투영을 정의한다.

</div>

- 최대 분산 형태: 단위 벡터 $\mathbf{u}_1$에 투영하면 투영 분산은 $\mathbf{u}_1^{\top}\mathbf{S}\mathbf{u}_1$이며 $\mathbf{S}=\frac{1}{N}\sum_n(\mathbf{x}_n-\overline{\mathbf{x}})(\mathbf{x}_n-\overline{\mathbf{x}})^{\top}$입니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.2.png" class="img-center" style="width: 15rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: "참고: 고유값 문제로서의 PCA"
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- $\mathbf{u}_1^{\top}\mathbf{u}_1=1$ 제약 하에서 $\mathbf{u}_1^{\top}\mathbf{S}\mathbf{u}_1$을 최대화하면(라그랑주 승수 사용) 고유값 방정식을 얻습니다:

$$
\mathbf{S}\mathbf{u}_1=\lambda_1\mathbf{u}_1
$$

- 투영 분산이 $\lambda_1$과 같으므로, 제1주성분은 가장 큰 고유값의 고유벡터입니다.

- $J=\sum_{i=M+1}^D\mathbf{u}_i^{\top}\mathbf{S}\mathbf{u}_i$를 최소화하는 최소 오차 형태도 같은 결과를 줍니다: 가장 작은 고유값 방향을 버립니다.

---
layout: prism
heading: 주성분 분석 (3/3)
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)
A = np.array([[2.0, 0.0], [1.3, 0.7]])
X = (rng.standard_normal((1000, 2)) @ A.T) + [1.0, -2.0]
Xc = X - X.mean(0); S = Xc.T @ Xc / len(X)              # covariance
w, V = np.linalg.eigh(S); idx = np.argsort(w)[::-1]; w = w[idx]; V = V[:, idx]
u1 = V[:, 0]                                            # first principal component
print("eigenvalues:", np.round(w, 4).tolist())
print("u1 =", np.round(u1, 3).tolist())
print(f"projected variance u1^T S u1 = {u1@S@u1:.4f}  (= lambda1 = {w[0]:.4f})")
print(f"variance explained = {w[0]/w.sum():.3f}")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">주성분 분석</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">확률적 주성분 분석</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">커널 주성분 분석</span></p>
</div>
</div>

---
layout: prism
heading: 확률적 주성분 분석 (1/2)
---

<div style="display:grid; grid-template-columns: 1.6fr 1.4fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- [확률적 주성분 분석(Probabilistic PCA)]{.hl}은 PCA를 선형–가우시안 잠재 변수 모델의 최대 가능도 해로 표현합니다:

$$
p(\mathbf{z})=\mathcal{N}(\mathbf{z}|\mathbf{0},\mathbf{I}),\quad
p(\mathbf{x}|\mathbf{z})=\mathcal{N}(\mathbf{x}|\mathbf{W}\mathbf{z}+\boldsymbol{\mu},\sigma^2\mathbf{I})
$$

- 즉 $\mathbf{x}=\mathbf{W}\mathbf{z}+\boldsymbol{\mu}+\boldsymbol{\epsilon}$ — 잠재 공간에서 데이터 공간으로의 사상입니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.9.png" class="img-center" style="width: 25rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: 확률적 주성분 분석 (2/2)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- 주변 분포와 사후 분포:

$$
p(\mathbf{x})=\mathcal{N}(\mathbf{x}|\boldsymbol{\mu},\mathbf{C}),\quad \mathbf{C}=\mathbf{W}\mathbf{W}^{\top}+\sigma^2\mathbf{I}
$$

$$
p(\mathbf{z}|\mathbf{x})=\mathcal{N}(\mathbf{z}|\mathbf{M}^{-1}\mathbf{W}^{\top}(\mathbf{x}-\boldsymbol{\mu}),\sigma^2\mathbf{M}^{-1})
$$

- 최대 가능도 해는 닫힌 형태입니다: $\mathbf{W}_{\mathrm{ML}}=\mathbf{U}_M(\mathbf{L}_M-\sigma^2\mathbf{I})^{1/2}\mathbf{R}$, $\sigma_{\mathrm{ML}}^2=\frac{1}{D-M}\sum_{i=M+1}^D\lambda_i$(버린 분산의 평균).

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.10.png" class="img-center" style="width: 15rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: PCA를 위한 EM (1/2)
---

<div style="display:grid; grid-template-columns: 1.4fr 1.6fr; gap: 1rem; align-items:center;">
<div>

- EM은 공분산 고유분해를 만들지 않고 풉니다. E 단계:

$$
\mathbb{E}[\mathbf{z}_n]=\mathbf{M}^{-1}\mathbf{W}^{\top}(\mathbf{x}_n-\overline{\mathbf{x}})
$$

- M 단계:

$$
\mathbf{W}_{\mathrm{new}}=\Big[\sum_n(\mathbf{x}_n-\overline{\mathbf{x}})\mathbb{E}[\mathbf{z}_n]^{\top}\Big]\Big[\sum_n\mathbb{E}[\mathbf{z}_n\mathbf{z}_n^{\top}]\Big]^{-1}
$$

<div class="sub-item">

고차원에서 효율적이며 누락된 데이터도 다룰 수 있습니다.

</div>

</div>
<div>
<div class="img-row" style="max-width: 100%">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.12a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.12b.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.12c.png"/>
</div>
<div class="img-row" style="max-width: 100%">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.12d.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.12e.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.12f.png"/>
</div>
</div>
</div>

---
layout: prism
heading: PCA를 위한 EM (2/2)
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)
D, M, N = 5, 2, 2000
Wtrue = rng.standard_normal((D, M)); Z = rng.standard_normal((N, M))
X = Z @ Wtrue.T + 0.3*rng.standard_normal((N, D)) + rng.standard_normal(D)
Xc = X - X.mean(0); S = Xc.T @ Xc / N
lam, U = np.linalg.eigh(S); idx = np.argsort(lam)[::-1]; lam = lam[idx]; U = U[:, idx]
sig2 = lam[M:].mean()                                   # sigma^2_ML = mean discarded eigenvalues
WML = U[:, :M] @ np.diag(np.sqrt(np.maximum(lam[:M]-sig2, 0)))
C = WML @ WML.T + sig2*np.eye(D)                        # reconstructed covariance
print(f"sigma^2_ML = {sig2:.4f}  (mean discarded eigenvalue)")
print(f"max|C - S| = {np.abs(C-S).max():.4f}  (marginal covariance recovered)")
print("top-M eigenvalues:", np.round(lam[:M], 3).tolist())
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">주성분 분석</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">확률적 주성분 분석</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">커널 주성분 분석</span></p>
</div>
</div>

---
layout: prism
heading: 커널 주성분 분석 (1/3)
---

<div style="display:grid; grid-template-columns: 1.5fr 1.5fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- [커널 주성분 분석(Kernel PCA)]{.hl}은 커널 트릭으로 PCA를 비선형으로 일반화합니다. 주성분은 특징 공간 공분산 $\mathbf{C}=\frac{1}{N}\sum_n\boldsymbol{\phi}(\mathbf{x}_n)\boldsymbol{\phi}(\mathbf{x}_n)^{\top}$의 고유벡터입니다.

- $\mathbf{v}_i=\sum_n a_{in}\boldsymbol{\phi}(\mathbf{x}_n)$를 대입하면 그램 행렬의 고유값 문제로 환원됩니다.

</div>
<div>
<div class="img-row" style="max-width: 100%">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.16a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.16b.png"/>
</div>
</div>
</div>

---
layout: prism
heading: 커널 주성분 분석 (2/3)
---

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- 고유값 문제와 투영은 전부 커널만으로 표현됩니다:

$$
\mathbf{K}\mathbf{a}_i=\lambda_i N\mathbf{a}_i,\qquad
y_i(\mathbf{x})=\sum_{n=1}^N a_{in}\,k(\mathbf{x},\mathbf{x}_n)
$$

- 특징 공간에서 선형인 투영이 데이터 공간에서는 비선형이므로, 커널 PCA는 선형 PCA가 못 잡는 구조를 포착합니다.

---
layout: prism
heading: 커널 주성분 분석 (3/3)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(3)

def ring(r, n):
    t = rng.uniform(0, 2*np.pi, n); rr = r + 0.08*rng.standard_normal(n)
    return np.c_[rr*np.cos(t), rr*np.sin(t)]
X = np.vstack([ring(1.0, 150), ring(3.0, 150)]); y = np.r_[np.zeros(150), np.ones(150)]
N = len(X); one = np.ones((N, N))/N
d2 = ((X[:, None, :]-X[None, :, :])**2).sum(2)
K = np.exp(-d2/(2*1.5**2))                              # Gaussian kernel (sigma = 1.5)
Kc = K - one@K - K@one + one@K@one                      # centered kernel matrix
lam, al = np.linalg.eigh(Kc); idx = np.argsort(lam)[::-1]; al = al[:, idx]
proj = Kc @ al[:, 0]                                    # first kernel principal component
m0, m1 = proj[y==0].mean(), proj[y==1].mean(); thr = (m0+m1)/2
acc = max(np.mean((proj>thr)==(y==1)), np.mean((proj<thr)==(y==1)))

print(f"1st kernel PC -- inner ring mean = {m0:+.3f}, outer ring mean = {m1:+.3f}")
print(f"separation accuracy from 1st component = {acc:.1%} (impossible for linear PCA)")
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
