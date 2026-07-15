---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 10
download: true
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-10-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 10: Mixture Models</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span class="text-gray-900 dark:text-gray-100">Mixture Models</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">Approximate Inference</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Sampling Methods</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Continuous Latent Variables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Recap (1/2)
---

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- A directed graphical model factorizes the joint as:

$$
p(\mathbf{x})=\prod_{k=1}^{K}p(x_k|\mathrm{pa}_k)
$$

<div class="sub-item">

$\mathrm{pa}_k$ are the parents of $x_k$; the graph must be a directed acyclic graph.

</div>

- We reduce the parameter count by removing links, tying parameters, or using parameterized conditionals (e.g. a logistic sigmoid of the parents).

---
layout: prism
heading: Recap (2/2)
---

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- Conditional independence $a\perp\!\!\!\perp b\mid c$ can be read off the graph via [d-separation]{.hl}.

- Tail-to-tail and head-to-tail nodes [block]{.hl} a path when observed; head-to-head nodes block a path when unobserved and open it when observed (or a descendant is observed).

- An undirected graph (Markov random field) removes the parent–child asymmetry: $A\perp\!\!\!\perp B\mid C$ holds when every path from $A$ to $B$ passes through $C$.

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">K-Means Clustering</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Mixture of Gaussians</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">EM Algorithm</span></p>
</div>
</div>

---
layout: prism
heading: K-Means Clustering (1/4)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- Cluster $N$ observations $\{\mathbf{x}_1,\ldots,\mathbf{x}_N\}$ into $K$ clusters; introduce a [prototype]{.hl} $\boldsymbol{\mu}_k$ (the cluster center).

- With a one-hot assignment $r_{nk}\in\{0,1\}$, minimize the [distortion measure]{.hl}:

$$
J=\sum_{n=1}^N \sum_{k=1}^K r_{n k}\left\|\mathbf{x}_n-\boldsymbol{\mu}_k\right\|^2
$$

- Alternate two phases: fix $\boldsymbol{\mu}_k$ and optimize $r_{nk}$; then fix $r_{nk}$ and optimize $\boldsymbol{\mu}_k$ (the E and M steps of the [EM algorithm]{.hl}).

---
layout: prism
heading: K-Means Clustering (2/4)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- Assignment step (E): each point goes to the nearest prototype,

$$
r_{nk}=\begin{cases}1 & k=\arg\min_j\|\mathbf{x}_n-\boldsymbol{\mu}_j\|^2\\ 0 & \text{otherwise}\end{cases}
$$

- Update step (M): differentiating $J$ w.r.t. $\boldsymbol{\mu}_k$ gives the cluster mean,

$$
\boldsymbol{\mu}_k=\frac{\sum_n r_{nk}\mathbf{x}_n}{\sum_n r_{nk}}
$$

<div class="sub-item">

Replacing the squared distance by a general $\mathcal{V}(\cdot,\cdot)$ gives the [K-medoids]{.hl} algorithm.

</div>

---
layout: prism
heading: K-Means Clustering (3/4)
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
heading: K-Means Clustering (4/4)
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
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">K-Means Clustering</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Mixture of Gaussians</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">EM Algorithm</span></p>
</div>
</div>

---
layout: prism
heading: Mixture of Gaussians (1/3)
---

<style>
.slidev-layout ul > li { margin-top: 1.5em; }
</style>

- A mixture of Gaussians is a linear superposition of Gaussians:

$$
p(\mathbf{x})=\sum_{k=1}^K \pi_k \mathcal{N}\left(\mathbf{x} | \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k\right)
$$

- Introduce a one-hot latent variable $\mathbf{z}$ with $p(z_k=1)=\pi_k$, so $p(\mathbf{z})=\prod_k\pi_k^{z_k}$ and $p(\mathbf{x}|\mathbf{z})=\prod_k\mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)^{z_k}$.

- Marginalizing $\mathbf{z}$ recovers the mixture:

$$
p(\mathbf{x})=\sum_{\mathbf{z}} p(\mathbf{z}) p(\mathbf{x} | \mathbf{z})=\sum_{k=1}^K \pi_k \mathcal{N}\left(\mathbf{x} | \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k\right)
$$

---
layout: prism
heading: Mixture of Gaussians (2/3)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- Given $\mathbf{x}$, the posterior of $\mathbf{z}$ is the [responsibility]{.hl} of component $k$:

$$
\gamma(z_k)=p(z_k=1|\mathbf{x})=\frac{\pi_k \mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)}{\sum_{j} \pi_j \mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_j,\boldsymbol{\Sigma}_j)}
$$

<div class="sub-item">

$\gamma(z_k)$ measures how much component $k$ explains the observation $\mathbf{x}$.

</div>

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.5a.png" class="img-center" style="width: 10rem;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.5b.png" class="img-center" style="width: 10rem;" />
</div>
</div>

---
layout: prism
heading: Mixture of Gaussians (3/3)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- The log-likelihood of the mixture is:

$$
\ln p(\mathbf{X} | \boldsymbol{\pi}, \boldsymbol{\mu}, \boldsymbol{\Sigma})=\sum_{n=1}^N \ln \Big\{\sum_{k=1}^K \pi_k \mathcal{N}(\mathbf{x}_n | \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)\Big\}
$$

- Direct MLE suffers from a [singularity]{.hl}: if a component collapses onto a single point ($\sigma_j\to0$), the log-likelihood diverges.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.6.png" class="img-center" style="width: 14rem;" />
</div>
</div>

---
layout: prism
heading: EM for Mixture of Gaussians (1/3)
---

<style>
.slidev-layout ul > li { margin-top: 2.2em; }
</style>

- Setting derivatives of the log-likelihood to zero gives the update equations ($N_k=\sum_n\gamma(z_{nk})$):

$$
\boldsymbol{\mu}_k=\frac{1}{N_k}\sum_{n} \gamma(z_{nk})\mathbf{x}_n,\qquad
\boldsymbol{\Sigma}_k=\frac{1}{N_k}\sum_{n}\gamma(z_{nk})(\mathbf{x}_n-\boldsymbol{\mu}_k)(\mathbf{x}_n-\boldsymbol{\mu}_k)^{\top}
$$

- With a Lagrange multiplier for $\sum_k\pi_k=1$:

$$
\pi_k=\frac{N_k}{N}
$$

<div class="sub-item">

These are not closed-form, since $\gamma(z_{nk})$ depends on the parameters — so we iterate.

</div>

---
layout: prism
heading: EM for Mixture of Gaussians (2/3)
---

<div style="display:grid; grid-template-columns: 1.4fr 1.6fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2em; }
</style>
- E step: compute responsibilities from current parameters.

- M step: re-estimate $\boldsymbol{\mu}_k$, $\boldsymbol{\Sigma}_k$, $\pi_k$.

- We usually run K-means first for initialization, then EM; the log-likelihood may have several local maxima.

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
heading: Mixture of Gaussians — (3/3)
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
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">K-Means Clustering</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Mixture of Gaussians</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">EM Algorithm</span></p>
</div>
</div>

---
layout: prism
heading: General EM Algorithm (1/3)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- EM finds the maximum-likelihood solution of models with latent variables, maximizing $p(\mathbf{X}|\boldsymbol{\theta})=\sum_{\mathbf{Z}} p(\mathbf{X},\mathbf{Z}|\boldsymbol{\theta})$.

- Introducing a distribution $q(\mathbf{Z})$ decomposes the log-likelihood:

$$
\ln p(\mathbf{X} | \boldsymbol{\theta})=\mathcal{L}(q, \boldsymbol{\theta})+\mathrm{KL}(q \| p)
$$

$$
\mathcal{L}(q, \boldsymbol{\theta})=\sum_{\mathbf{Z}} q(\mathbf{Z}) \ln \frac{p(\mathbf{X}, \mathbf{Z} | \boldsymbol{\theta})}{q(\mathbf{Z})},\qquad
\mathrm{KL}(q \| p)=-\sum_{\mathbf{Z}} q(\mathbf{Z}) \ln \frac{p(\mathbf{Z} | \mathbf{X}, \boldsymbol{\theta})}{q(\mathbf{Z})}
$$

<div class="sub-item">

Since $\mathrm{KL}\geqslant 0$, $\mathcal{L}(q,\boldsymbol{\theta})$ is a lower bound of the log-likelihood.

</div>

---
layout: prism
heading: General EM Algorithm (2/3)
---

<div style="display:grid; grid-template-columns: 1.5fr 1fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- E step: with $\boldsymbol{\theta}^{\mathrm{old}}$ fixed, maximize $\mathcal{L}$ over $q$. This sets $q(\mathbf{Z})=p(\mathbf{Z}|\mathbf{X},\boldsymbol{\theta}^{\mathrm{old}})$, so $\mathrm{KL}=0$ and the bound touches the log-likelihood.

- M step: with $q$ fixed, maximize $\mathcal{L}$ over $\boldsymbol{\theta}$. The bound (and the log-likelihood) increases; $q$ now differs from the new posterior so $\mathrm{KL}>0$.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.11.png" class="img-center" style="width: 12rem; margin-bottom: 4rem" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure9.13.png" class="img-center" style="width: 12rem;" />
</div>
</div>

---
layout: prism
heading: General EM Algorithm (3/3)
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

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
