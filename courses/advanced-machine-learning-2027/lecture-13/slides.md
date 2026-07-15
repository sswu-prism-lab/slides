---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 13
download: true
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-13-ko/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Advanced Machine Learning</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 13: Continuous Latent Variables</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">Wonjun Ko, Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">Spring 2027</p>
</div>

---
layout: prism
heading: Course Schedule
---

<div class="absolute left-10 right-10" style="top: 1rem; bottom: 5rem; display: grid; grid-template-columns: 1fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">Course Introduction</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">Preliminaries</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">Probabilistic Distributions</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">Linear Regression Models</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">Linear Classification Models</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">Kernel Methods</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">Midterm Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">Midterm Exam</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">Graphical Models</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">Mixture Models</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">Approximate Inference</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Sampling Methods</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span class="text-gray-900 dark:text-gray-100">Continuous Latent Variables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Recap
---

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- Inverse transform, rejection, and importance sampling generate samples (or estimate expectations) from a proposal distribution.

- MCMC (Metropolis / Metropolis–Hastings) draws a Markov chain of samples, accepting candidates with a probability based on the target ratio.

- Gibbs sampling updates each variable from its full conditional; slice sampling adapts the step size automatically.

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Principal Component Analysis</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probabilistic PCA</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Kernel PCA</span></p>
</div>
</div>

---
layout: prism
heading: Principal Component Analysis (1/3)
---

<div style="display:grid; grid-template-columns: 1.4fr 1.6fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- Data often lie near a low-dimensional manifold. Inserting a $64\times64$ digit into a $100\times100$ image has three [degrees of freedom]{.hl} (two shifts + rotation), so the [intrinsic dimensionality]{.hl} is 3.

- [Principal component analysis; PCA]{.hl} is the simplest continuous latent variable model, used for dimension reduction, compression, and visualization.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.1.png" class="img-center" style="width: 25rem;" />
</div>
</div>

---
layout: prism
heading: Principal Component Analysis (2/3)
---

<div style="display:grid; grid-template-columns: 1.6fr 1.4fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- PCA has two equivalent definitions:

<div class="sub-item-enum">

1. orthogonally project data onto a [principal subspace]{.hl} that maximizes the projected variance;
2. define a linear projection that minimizes the mean squared projection cost.

</div>

- Maximal-variance form: project onto a unit vector $\mathbf{u}_1$; the projected variance is $\mathbf{u}_1^{\top}\mathbf{S}\mathbf{u}_1$ with $\mathbf{S}=\frac{1}{N}\sum_n(\mathbf{x}_n-\overline{\mathbf{x}})(\mathbf{x}_n-\overline{\mathbf{x}})^{\top}$.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.2.png" class="img-center" style="width: 15rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: "NOTE: PCA as an Eigenproblem"
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- Maximizing $\mathbf{u}_1^{\top}\mathbf{S}\mathbf{u}_1$ subject to $\mathbf{u}_1^{\top}\mathbf{u}_1=1$ (via a Lagrange multiplier) gives the eigenvalue equation:

$$
\mathbf{S}\mathbf{u}_1=\lambda_1\mathbf{u}_1
$$

- The projected variance equals $\lambda_1$, so the first principal component is the eigenvector with the largest eigenvalue.

- The minimal-error form, minimizing $J=\sum_{i=M+1}^D\mathbf{u}_i^{\top}\mathbf{S}\mathbf{u}_i$, gives the same result: discard the smallest-eigenvalue directions.

---
layout: prism
heading: Principal Component Analysis (3/3)
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
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Principal Component Analysis</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Probabilistic PCA</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Kernel PCA</span></p>
</div>
</div>

---
layout: prism
heading: Probabilistic PCA (1/2)
---

<div style="display:grid; grid-template-columns: 1.6fr 1.4fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- [Probabilistic PCA]{.hl} expresses PCA as the ML solution of a linear-Gaussian latent variable model:

$$
p(\mathbf{z})=\mathcal{N}(\mathbf{z}|\mathbf{0},\mathbf{I}),\quad
p(\mathbf{x}|\mathbf{z})=\mathcal{N}(\mathbf{x}|\mathbf{W}\mathbf{z}+\boldsymbol{\mu},\sigma^2\mathbf{I})
$$

- i.e. $\mathbf{x}=\mathbf{W}\mathbf{z}+\boldsymbol{\mu}+\boldsymbol{\epsilon}$ — a mapping from latent to data space.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.9.png" class="img-center" style="width: 25rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: Probabilistic PCA (2/2)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- Marginal and posterior distributions:

$$
p(\mathbf{x})=\mathcal{N}(\mathbf{x}|\boldsymbol{\mu},\mathbf{C}),\quad \mathbf{C}=\mathbf{W}\mathbf{W}^{\top}+\sigma^2\mathbf{I}
$$

$$
p(\mathbf{z}|\mathbf{x})=\mathcal{N}(\mathbf{z}|\mathbf{M}^{-1}\mathbf{W}^{\top}(\mathbf{x}-\boldsymbol{\mu}),\sigma^2\mathbf{M}^{-1})
$$

- The ML solution is closed-form: $\mathbf{W}_{\mathrm{ML}}=\mathbf{U}_M(\mathbf{L}_M-\sigma^2\mathbf{I})^{1/2}\mathbf{R}$, and $\sigma_{\mathrm{ML}}^2=\frac{1}{D-M}\sum_{i=M+1}^D\lambda_i$ (average discarded variance).

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure12.10.png" class="img-center" style="width: 15rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: EM for PCA (1/2)
---

<div style="display:grid; grid-template-columns: 1.4fr 1.6fr; gap: 1rem; align-items:center;">
<div>

- EM avoids forming the covariance eigendecomposition. E step:

$$
\mathbb{E}[\mathbf{z}_n]=\mathbf{M}^{-1}\mathbf{W}^{\top}(\mathbf{x}_n-\overline{\mathbf{x}})
$$

- M step:

$$
\mathbf{W}_{\mathrm{new}}=\Big[\sum_n(\mathbf{x}_n-\overline{\mathbf{x}})\mathbb{E}[\mathbf{z}_n]^{\top}\Big]\Big[\sum_n\mathbb{E}[\mathbf{z}_n\mathbf{z}_n^{\top}]\Big]^{-1}
$$

<div class="sub-item">

Efficient in high dimensions and handles missing data.

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
heading: EM for PCA (2/2)
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
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Principal Component Analysis</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probabilistic PCA</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Kernel PCA</span></p>
</div>
</div>

---
layout: prism
heading: Kernel PCA (1/3)
---

<div style="display:grid; grid-template-columns: 1.5fr 1.5fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- [Kernel PCA]{.hl} generalizes PCA nonlinearly via the kernel trick. Principal components are eigenvectors of the feature-space covariance $\mathbf{C}=\frac{1}{N}\sum_n\boldsymbol{\phi}(\mathbf{x}_n)\boldsymbol{\phi}(\mathbf{x}_n)^{\top}$.

- Substituting $\mathbf{v}_i=\sum_n a_{in}\boldsymbol{\phi}(\mathbf{x}_n)$ reduces it to an eigenproblem of the Gram matrix.

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
heading: Kernel PCA (2/3)
---

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- The eigenproblem and the projection are expressed entirely with the kernel:

$$
\mathbf{K}\mathbf{a}_i=\lambda_i N\mathbf{a}_i,\qquad
y_i(\mathbf{x})=\sum_{n=1}^N a_{in}\,k(\mathbf{x},\mathbf{x}_n)
$$

- A projection that is linear in the feature space is nonlinear in the data space, so kernel PCA captures structure that linear PCA cannot.

---
layout: prism
heading: Kernel PCA (3/3)
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

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
