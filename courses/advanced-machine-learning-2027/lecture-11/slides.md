---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 11
download: true
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-11-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 11: Approximate Inference</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span class="text-gray-900 dark:text-gray-100">Approximate Inference</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Sampling Methods</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Continuous Latent Variables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Recap
---

<style>
.slidev-layout ul > li { margin-top: 2em; }
</style>

- K-means minimizes the distortion $J=\sum_n\sum_k r_{nk}\|\mathbf{x}_n-\boldsymbol{\mu}_k\|^2$ by alternating assignment and mean updates.

- A mixture of Gaussians is trained by EM: the E step computes responsibilities $\gamma(z_{nk})$; the M step re-estimates $\boldsymbol{\mu}_k$, $\boldsymbol{\Sigma}_k$, $\pi_k$.

- EM maximizes a lower bound $\mathcal{L}(q,\boldsymbol{\theta})$ of the log-likelihood, since $\ln p(\mathbf{X}|\boldsymbol{\theta})=\mathcal{L}(q,\boldsymbol{\theta})+\mathrm{KL}(q\|p)$.

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Variational Inference</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Mixture of Gaussians</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Linear Regression</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Logistic Regression</span></p>
</div>
</div>

---
layout: prism
heading: Variational Inference (1/4)
---

<style>
.slidev-layout ul > li { margin-top: 2em; }
</style>

- Variational methods build on the [calculus of variations]{.hl}: a [functional]{.hl} maps a function to a value (e.g. the entropy $\mathrm{H}[p]=-\int p(x)\ln p(x)\,\mathrm{d}x$).

- For a full Bayesian model with all latents/parameters $\mathbf{Z}$ and observations $\mathbf{X}$, we approximate the posterior $p(\mathbf{Z}|\mathbf{X})$ and the evidence $p(\mathbf{X})$.

- The log marginal decomposes as:

$$
\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q \| p),\qquad
\mathcal{L}(q)=\int q(\mathbf{Z}) \ln \frac{p(\mathbf{X}, \mathbf{Z})}{q(\mathbf{Z})}\, \mathrm{d}\mathbf{Z}
$$

<div class="sub-item">

Maximizing the lower bound $\mathcal{L}(q)$ over $q(\mathbf{Z})$ is equivalent to minimizing the KL divergence.

</div>

---
layout: prism
heading: Variational Inference (2/4)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- The true posterior is intractable, so we restrict $q$ to a tractable family and find the best member. A common choice is the [mean-field]{.hl} factorization:

$$
q(\mathbf{Z})=\prod_{i=1}^{M}q_i(\mathbf{Z}_i)
$$

- Free-form optimization of $\mathcal{L}(q)$ over each factor gives the optimal factor:

$$
\ln q_j^{\star}(\mathbf{Z}_j)=\mathbb{E}_{i \neq j}[\ln p(\mathbf{X}, \mathbf{Z})]+\text{const}
$$

<div class="sub-item">

Each factor depends on expectations of the others, so we update them cyclically.

</div>

---
layout: prism
heading: Variational Inference (3/4)
---

<div style="display:grid; grid-template-columns: 1.5fr 1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- Minimizing $\mathrm{KL}(q\|p)$ is [mode-seeking]{.hl}; minimizing the reverse $\mathrm{KL}(p\|q)$ is [mass-covering]{.hl}.

- For a correlated Gaussian approximated by a factorized $q$, the mean is exact but the variance is [underestimated]{.hl} (the factorized fit shrinks to the smallest conditional variance).

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.9a.png" class="img-center" style="width: 15rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: Variational Inference (4/4)
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
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Inference</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Variational Mixture of Gaussians</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Linear Regression</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Logistic Regression</span></p>
</div>
</div>

---
layout: prism
heading: Variational Mixture of Gaussians (1/2)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 4.5em; }
</style>

- For a Bayesian mixture of Gaussians, place conjugate priors: a Dirichlet on $\boldsymbol{\pi}$ and a Gaussian–Wishart on $(\boldsymbol{\mu},\boldsymbol{\Lambda})$.

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
heading: Variational Mixture of Gaussians (2/2)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- Factorize $q(\mathbf{Z},\boldsymbol{\pi},\boldsymbol{\mu},\boldsymbol{\Lambda})=q(\mathbf{Z})\,q(\boldsymbol{\pi},\boldsymbol{\mu},\boldsymbol{\Lambda})$. The optimal latent factor is:

$$
q^{\star}(\mathbf{Z})=\prod_{n=1}^N \prod_{k=1}^K r_{n k}^{z_{n k}},\qquad r_{nk}=\frac{\rho_{nk}}{\sum_j \rho_{nj}}
$$

<div class="sub-item">

$r_{nk}=\mathbb{E}[z_{nk}]$ plays the role of a responsibility.

</div>

- The responsibility-weighted statistics $N_k$, $\overline{\mathbf{x}}_k$, $\mathbf{S}_k$ mirror those of EM, but now update distributions over parameters rather than point estimates.

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Inference</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Mixture of Gaussians</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Variational Linear Regression</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Logistic Regression</span></p>
</div>
</div>

---
layout: prism
heading: Variational Linear Regression (1/2)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- Likelihood and priors:

$$
p(\boldsymbol{\mathsf{t}}|\mathbf{w})=\prod_{n}\mathcal{N}(t_n|\mathbf{w}^{\top}\boldsymbol{\phi}_n,\beta^{-1}),\quad
p(\mathbf{w}|\alpha)=\mathcal{N}(\mathbf{w}|\mathbf{0},\alpha^{-1}\mathbf{I})
$$

$$
p(\alpha)=\operatorname{Gam}(\alpha|a_0,b_0)
$$

- Joint: $p(\boldsymbol{\mathsf{t}},\mathbf{w},\alpha)=p(\boldsymbol{\mathsf{t}}|\mathbf{w})p(\mathbf{w}|\alpha)p(\alpha)$.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure10.8.png" class="img-center" style="width: 15rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: Variational Linear Regression (2/2)
---

<style>
.slidev-layout ul > li { margin-top: 3.3em; }
</style>

- Factorize $q(\mathbf{w},\alpha)=q(\mathbf{w})q(\alpha)$. The precision factor is a Gamma:

$$
q^{\star}(\alpha)=\operatorname{Gam}(\alpha|a_N,b_N),\quad a_N=a_0+\tfrac{M}{2},\quad b_N=b_0+\tfrac{1}{2}\mathbb{E}[\mathbf{w}^{\top}\mathbf{w}]
$$

- The weight factor is a Gaussian:

$$
q^{\star}(\mathbf{w})=\mathcal{N}(\mathbf{w}|\mathbf{m}_N,\mathbf{S}_N),\quad
\mathbf{m}_N=\beta\mathbf{S}_N\boldsymbol{\Phi}^{\top}\boldsymbol{\mathsf{t}},\quad
\mathbf{S}_N=(\mathbb{E}[\alpha]\mathbf{I}+\beta\boldsymbol{\Phi}^{\top}\boldsymbol{\Phi})^{-1}
$$

<div class="sub-item">

Same form as evidence-maximization EM, but the point estimate of $\alpha$ is replaced by $\mathbb{E}[\alpha]$.

</div>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Inference</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Mixture of Gaussians</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Variational Linear Regression</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Variational Logistic Regression</span></p>
</div>
</div>

---
layout: prism
heading: Variational Logistic Regression (1/3)
---

<style>
.slidev-layout ul > li { margin-top: 3.3em; }
</style>

- The marginal likelihood $p(\boldsymbol{\mathsf{t}})=\int \prod_n p(t_n|\mathbf{w})\,p(\mathbf{w})\,\mathrm{d}\mathbf{w}$ is intractable. Using $p(t|\mathbf{w})=e^{at}\sigma(-a)$ with $a=\mathbf{w}^{\top}\boldsymbol{\phi}$, apply the variational sigmoid bound:

$$
\sigma(z) \geqslant \sigma(\xi) \exp\{(z-\xi)/2-\lambda(\xi)(z^2-\xi^2)\},\quad \lambda(\xi)=\frac{1}{2\xi}\Big[\sigma(\xi)-\frac{1}{2}\Big]
$$

- With one variational parameter $\xi_n$ per observation, the joint bound is quadratic in $\mathbf{w}$, giving a Gaussian approximation of the posterior.

---
layout: prism
heading: Variational Logistic Regression (2/2)
---

<style>
.slidev-layout ul > li { margin-top: 3.3em; }
</style>

- The Gaussian posterior approximation is:

$$
q(\mathbf{w})=\mathcal{N}(\mathbf{w}|\mathbf{m}_N,\mathbf{S}_N),\quad
\mathbf{S}_N^{-1}=\mathbf{S}_0^{-1}+2\sum_{n}\lambda(\xi_n)\boldsymbol{\phi}_n\boldsymbol{\phi}_n^{\top}
$$

- The variational parameters $\xi_n$ are optimized (e.g. via EM) with the update:

$$
(\xi_n^{\mathrm{new}})^2=\boldsymbol{\phi}_n^{\top}(\mathbf{S}_N+\mathbf{m}_N\mathbf{m}_N^{\top})\boldsymbol{\phi}_n
$$

<div class="sub-item">

The predictive distribution is obtained by marginalizing over $q(\mathbf{w})$.

</div>

---
layout: prism
heading: Variational Logistic Regression (3/3)
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

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
