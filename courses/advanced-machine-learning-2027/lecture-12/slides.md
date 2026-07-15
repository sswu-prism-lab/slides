---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 12
download: true
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-12-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 12: Sampling Methods</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span class="text-gray-900 dark:text-gray-100">Sampling Methods</span></p>
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
.slidev-layout ul > li { margin-top: 3em; }
</style>

- Variational inference decomposes the log evidence as $\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p)$ and maximizes the lower bound $\mathcal{L}(q)$.

- We restrict $q$ to a tractable family, commonly the mean-field factorization $q(\mathbf{Z})=\prod_i q_i(\mathbf{Z}_i)$.

- $\mathrm{KL}(q\|p)$ is mode-seeking while $\mathrm{KL}(p\|q)$ is mass-covering; the vanilla KL is preferred as it is more tractable.

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Sampling Algorithms</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Markov Chain Monte Carlo</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Other Samplings</span></p>
</div>
</div>

---
layout: prism
heading: Sampling Algorithms
---

<style>
.slidev-layout ul > li { margin-top: 3.8em; }
</style>

- We use sampling to estimate the expectation of $f(\mathbf{z})$ under $p(\mathbf{z})$, using a finite sum over samples $\mathbf{z}^{(l)}$:

$$
\widehat{f}=\frac{1}{L} \sum_{l=1}^L f(\mathbf{z}^{(l)}),\qquad
\operatorname{var}[\widehat{f}]=\frac{1}{L} \mathbb{E}[(f-\mathbb{E}[f])^2]
$$

- A few dozen independent samples usually suffice; correlated samples need more.

---
layout: prism
heading: Standard Distribution
---

<div style="display:grid; grid-template-columns: 1.5fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- Given uniform random numbers $z\in(0,1)$, transforming by $y=f(z)$ gives $p(y)=p(z)|\mathrm{d}z/\mathrm{d}y|$.

- Choosing $f=h^{-1}$ where $h(y)=\int_{-\infty}^y p(\widehat{y})\,\mathrm{d}\widehat{y}$ (the CDF) yields the desired $p(y)$ — [inverse transform]{.hl} sampling.

<div class="sub-item">

For the exponential distribution $p(y)=\lambda e^{-\lambda y}$, use $y=-\lambda^{-1}\ln(1-z)$.

</div>

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure11.2.png" class="img-center" style="width: 15rem; margin-top: 4rem" />
</div>
</div>

---
layout: prism
heading: Rejection Sampling
---

<div style="display:grid; grid-template-columns: 1.4fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- To sample $p(z)=\widetilde{p}(z)/Z_p$ with unknown $Z_p$, use a [proposal distribution]{.hl} $q(z)$ and a constant $k$ with $kq(z)\geqslant\widetilde{p}(z)$.

- Draw $z_0\sim q$ and $u_0\sim \mathcal{U}[0,kq(z_0)]$; reject if $u_0>\widetilde{p}(z_0)$. Accepted samples follow $p(z)$.

- Acceptance probability: $p(a)=\dfrac{1}{k}\int\widetilde{p}(z)\,\mathrm{d}z$.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure11.4.png" class="img-center" style="width: 20rem;" />
</div>
</div>

---
layout: prism
heading: Importance Sampling
---

<div style="display:grid; grid-template-columns: 1.4fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- [Importance sampling]{.hl} approximates expectations directly, using a proposal $q$ and [importance weights]{.hl} $r_l=p(\mathbf{z}^{(l)})/q(\mathbf{z}^{(l)})$:

$$
\mathbb{E}[f]=\int f(\mathbf{z}) \frac{p(\mathbf{z})}{q(\mathbf{z})} q(\mathbf{z})\, \mathrm{d}\mathbf{z} \simeq \frac{1}{L} \sum_{l=1}^L \frac{p(\mathbf{z}^{(l)})}{q(\mathbf{z}^{(l)})} f(\mathbf{z}^{(l)})
$$

- The weights correct the bias from sampling under the wrong distribution.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure11.8.png" class="img-center" style="width: 20rem;" />
</div>
</div>

---
layout: prism
heading: Sampling Algorithms Again
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
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Sampling Algorithms</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Markov Chain Monte Carlo</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Other Samplings</span></p>
</div>
</div>

---
layout: prism
heading: Markov Chain Monte Carlo (1/2)
---

<style>
.slidev-layout ul > li { margin-top: 3.8em; }
</style>

- Rejection and importance sampling struggle in high dimensions. [Markov chain Monte Carlo; MCMC]{.hl} samples from a state-dependent proposal $q(\mathbf{z}|\mathbf{z}^{(\tau)})$, so the samples form a Markov chain.

- The [Metropolis algorithm]{.hl} assumes a symmetric proposal and accepts a candidate with probability:

$$
A(\mathbf{z}^{\star}, \mathbf{z}^{(\tau)})=\min\Big(1, \frac{\widetilde{p}(\mathbf{z}^{\star})}{\widetilde{p}(\mathbf{z}^{(\tau)})}\Big)
$$

<div class="sub-item">

Draw $u\sim\mathcal{U}(0,1)$ and accept if $A>u$; otherwise keep the current state.

</div>

---
layout: prism
heading: Markov Chain Monte Carlo (2/2)
---

<style>
.slidev-layout ul > li { margin-top: 1em; }
</style>

- The [Metropolis–Hastings algorithm]{.hl} generalizes to asymmetric proposals, correcting for the proposal ratio:

$$
A_k(\mathbf{z}^{\star}, \mathbf{z}^{(\tau)})=\min\Big(1, \frac{\widetilde{p}(\mathbf{z}^{\star}) q_k(\mathbf{z}^{(\tau)} | \mathbf{z}^{\star})}{\widetilde{p}(\mathbf{z}^{(\tau)}) q_k(\mathbf{z}^{\star} | \mathbf{z}^{(\tau)})}\Big)
$$

<div class="sub-item">

$k$ labels the transition within the set of considered transitions.

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
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Sampling Algorithms</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Markov Chain Monte Carlo</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Other Samplings</span></p>
</div>
</div>

---
layout: prism
heading: Gibbs Sampling
---

- [Gibbs sampling]{.hl} is a special case of Metropolis–Hastings that is simple and widely used.

- For $p(\mathbf{z})=p(z_1,\ldots,z_M)$, update each variable in turn from its conditional given the rest:

$$
z_j^{(\tau+1)} \sim p(z_j | z_1^{(\tau+1)}, \ldots, z_{j-1}^{(\tau+1)}, z_{j+1}^{(\tau)}, \ldots, z_M^{(\tau)})
$$

<div class="sub-item">

Every proposal is accepted (acceptance probability $1$), so there is no rejection.

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
heading: Slice Sampling
---

<div style="display:grid; grid-template-columns: 1.3fr 1.2fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- Metropolis is sensitive to the step size; [slice sampling]{.hl} adapts it automatically using an auxiliary variable $u$:

$$
\widehat{p}(z, u)=\begin{cases}1/Z_p & 0\leqslant u\leqslant\widetilde{p}(z)\\ 0 & \text{otherwise}\end{cases}
$$

- Marginalizing $u$ recovers $p(z)$. Alternately sample $u\in[0,\widetilde{p}(z)]$, then $z$ uniformly on the slice $\{z:\widetilde{p}(z)>u\}$.

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

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
