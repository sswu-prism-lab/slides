---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 3
download: true
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-3-ko/
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
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.jpeg" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Advanced Machine Learning</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 03: Probabilistic Distributions</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span class="text-gray-900 dark:text-gray-100">Probabilistic Distributions</span></p>
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
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- We can define an error function to model for a regression problem:

$$
E(\mathbf{w})=\frac{1}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})-t_n\}^2
$$

<div class="sub-item">

Note that the error function is quadratic, hence it has a closed-form solution.

</div>

<div class="subsub-item">

Imagine a problem of finding the minimum of $y=4x^2-12x+16$.

</div>

- Note that the log-likelihood function is similar to the aforementioned error function:

$$
\ln p(\boldsymbol{\mathsf{t}}|\boldsymbol{\mathsf{x}}, \mathbf{w}, \beta)=-\frac{\beta}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})-t_n\}^2 + \frac{N}{2}\ln\beta -\frac{N}{2}\ln (2\pi)
$$

---
layout: prism
heading: Recap (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- We further can introduce a penalty term to tackle the overfitting issue, called regularization trick.

$$
\tilde{E}(\mathbf{w})=\frac{1}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w}) - t_n \}^2 + \frac{\lambda}{2}\|\mathbf{w}\|^2
$$

- Note that the maximum a posterior minimizes the following equation, which is similar to the above modified error function:

$$
\frac{\beta}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})-t_n\}^2+\frac{\alpha}{2}\mathbf{w}^\top\mathbf{w}
$$

- For decision-making, we can consider two different strategies, reducing the number of misclassified samples and minimizing an expected loss.

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Discrete Random Variables</span></p>
    <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Beta Distribution</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Multinomial Variables</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Gaussian Distribution</span></p>
  </div>

</div>

---
layout: prism
heading: Discrete Random Variables (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Consider a [random variable]{.hl} (r.v.) $x\in\{0,1\}$, then the probability of $x=1$ can be represented as a r.v. $\mu$:

$$
p(x=1|\mu)=\mu
$$

<div class="sub-item">

Note that $0\leqslant \mu\leqslant 1$ and $p(x=0|\mu)=1-\mu$.

</div>

- For this discrete, and binary r.v. $x$ we can rewrite the probability distribution of $x$, called [Bernoulli distribution]{.hl}:

$$
\mathrm{Bern}(x|\mu)=\mu^x(1-\mu)^{1-x}
$$

<div class="sub-item">

Bernoulli distribution is normalized and has the following expectation and variance:

</div>

$$
\begin{aligned}
\mathbb{E}[x]&=\mu\\
\operatorname{var}[x]&=\mu(1-\mu)
\end{aligned}
$$

---
layout: prism
heading: Discrete Random Variables (2/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Given an observed dataset $\mathcal{D}=\{x_1,\ldots,x_N\}$ of r.v. $x$, under an assumption that those datapoints are sampled from $p(x|\mu)$ independently, then we can formalize the likelihood function as follows:

$$
p(\mathcal{D}|\mu)=\prod_{n=1}^{N}p(x_n|\mu)=\prod_{n=1}^{N}\mu^{x_n}(1-\mu)^{1-x_n}
$$

<div class="sub-item">

The corresponding log-likelihood function is:

</div>

$$
\ln p(\mathcal{D}|\mu)=\sum_{n=1}^{N}\ln p(x_n|\mu)=\sum_{n=1}^{N}\{x_n\ln\mu + (1-x_n)\ln(1-\mu)\}
$$

<div class="subsub-item">

Note that this log-likelihood is related to $N$ observations $x_n$, only with the summation of observations $\sum_n x_n$.

</div>

<div class="subsub-item">

The summation is an example of [sufficient statistic]{.hl}.

</div>

---
layout: prism
heading: Discrete Random Variables (3/4)
---

- Let us differentiate the log-likelihood $\ln p(\mathcal{D}|\mu)$ w.r.t. $\mu$ and set $0$, then we can estimate maximum likelihood (ML) inference.

$$
\mu_\mathrm{ML}=\frac{1}{N}\sum_{n=1}^{N}x_n
$$

<div class="sub-item">

$\mu_\mathrm{ML}$ is called as [sample mean]{.hl}.

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
heading: Discrete Random Variables (4/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- For $N$ datapoints, we can consider that the distribution of the number of $x=1$, which is denoted by $m$, then the distribution is called [binomial distribution]{.hl} and defined as follows:

$$
\mathrm{Bin}(m|N,\mu)=\binom{N}{m}\mu^m(1-\mu)^{N-m}
$$

<div class="sub-item">

Here, $\binom{N}{m}\equiv\frac{N!}{(N-m)!m!}$.

</div>

<div class="sub-item">

Its expectation and variance are defined as follows:

</div>

$$
\begin{aligned}
\mathbb{E}[m]&\equiv\sum_{m=0}^{N}m\operatorname{Bin}(m|N, \mu)=N \mu\\
\mathrm{var}[m]&\equiv\sum_{m=0}^{N}(m-\mathbb{E}[m])^2\operatorname{Bin}(m|N,\mu)=N\mu(1-\mu)
\end{aligned}
$$

---
layout: prism
heading: Beta Distribution (1/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Suppose that we want to take Bayesian approach for Bernoulli distribution, hence introduce prior distribution for the parameter $\mu$, $p(\mu)$.

- Note that the likelihood of Bernoulli has factors of $\mu^x(1-\mu)^{1-x}$.

<div class="sub-item">

If we choose a priori which is proportional to powers of $\mu$ and $(1-\mu)$, then the posterior distribution—which is proportional to the product of the prior probability and the likelihood function—will also have the same functional form as the prior distribution.

</div>

<div class="subsub-item">

This property is known as [conjugacy]{.hl}.

</div>

- For instance, let us imagine that a coin toss example.

<div class="sub-item">

Note that the likelihood function based on the observed data is Bernoulli.

</div>

<div class="sub-item">

In this case, if we use Beta for the prior, then the posterior becomes Beta again.

</div>

---
layout: prism
heading: Beta Distribution (2/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [Beta distribution]{.hl} has the form of:

$$
\mathrm{Beta}(\mu|a, b)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\mu^{a-1}(1-\mu)^{b-1}
$$

<div class="sub-item">

The gamma function $\Gamma(\cdot)$ is defined as follows:

</div>

$$
\Gamma(x)\equiv\int_{0}^{\infty}u^{x-1}e^{-u}\,\mathrm{d}u
$$

<div class="sub-item">

Beta distribution has expectation and variance of the form:

</div>

$$
\begin{aligned}
\mathbb{E}[\mu]&=\frac{a}{a+b}\\
\mathrm{var}[\mu]&=\frac{ab}{(a+b)^2(a+b+1)}
\end{aligned}
$$

<div class="subsub-item">

Here $a$ and $b$ are hyperparameters.

</div>

---
layout: prism
heading: Beta Distribution (3/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- The hyperparameters $a$ and $b$ can be considered as [effective number of observations]{.hl} of $x=1$ and $x=0$, respectively.

<div class="sub-item">

In the Bayesian perspective, this [sequential]{.hl} approach is quite natural.

</div>

- If we set the prior as $\mathrm{Beta}(\mu|a,b)$ and the likelihood as $\mathrm{Bern}(x|\mu)$ and observe $H$ numbers of heads and $T$ numbers of tails, then, the posterior becomes $\mathrm{Beta}(\mu|a+H,b+T)$.

---
layout: prism
heading: Beta Distribution (4/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- Here, the plot becomes sharper for more observations.

- A general property of Bayesian learning is that as more data is observed, the uncertainty of the posterior distribution steadily decreases.

<div class="img-row" style="max-width: 100%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.2a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.2b.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.2c.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.2d.png"/>

</div>

---
layout: prism
heading: Beta Distribution (5/5)
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
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Discrete Random Variables</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Multinomial Variables</span></p>
    <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Dirichlet Distribution</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Gaussian Distribution</span></p>
  </div>

</div>

---
layout: prism
heading: Multinomial Variables (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- We may need $K$-dimensional discrete variables.

<div class="sub-item">

In machine learning, we often use [one hot encoding]{.hl} s.t. each variable $\mathbf{x}\in\{0, 1\}^K$ and $\sum_{k=1}^K x_k=1$.

</div>

- Suppose that the probability of $x_k=1$ is $\mu_k$, then the distribution of $\mathbf{x}$ is given by

$$
p(\mathbf{x}|\boldsymbol{\mu})=\prod_{k=1}^{K}\mu_k^{x_k}
$$

<div class="sub-item">

This distribution has two following properties:

</div>

$$
\begin{aligned}
\sum_x p(\mathbf{x}|\boldsymbol{\mu})&=\sum_{k=1}^{K}\mu_k=1\\
\mathbb{E}[\mathbf{x}|\boldsymbol{\mu}]&=\sum_xp(\mathbf{x}|\boldsymbol{\mu})\mathbf{x}=\boldsymbol{\mu}
\end{aligned}
$$

---
layout: prism
heading: Multinomial Variables (2/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- For a dataset contains $N$ independent observations $\mathbf{x}_1,\ldots,\mathbf{x}_N$, then the likelihood has the form:

$$
p(\mathcal{D}|\boldsymbol{\mu})=\prod_{n=1}^{N}\prod_{k=1}^{K}\mu_k^{x_{nk}}=\prod_{k=1}^{K}\mu_k^{\sum_n x_{nk}}=\prod_{k=1}^{K}\mu_k^{m_k}
$$

<div class="sub-item">

$m_k$ is the number of observations that $x_k=1$, and is sufficient statistics.

</div>

- We want to find the ML, $\ln p(\mathcal{D}|\boldsymbol{\mu})$.

<div class="sub-item">

Note that there is a constraint, $\sum_k\mu_k=1$.

</div>

---
layout: prism
heading: "NOTE: Lagrange Multiplier"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Consider we have a function $f(x)=x^2$ and a constraint $(x-2)^2=1$.

<div class="sub-item">

We set the constraint as a function of $x$, hence $g(x)=1-(x-2)^2$.

</div>

- We set the Lagrangian function $f(x)+\lambda g(x)$:

$$
\mathcal{L}(x,\lambda)=f(x)+\lambda g(x) = x^2 + \lambda(1-(x-2)^2)
$$

- We take partial derivatives w.r.t. $x$ and $\lambda$ to find stationary points:

$$
\begin{aligned}
\frac{\partial\mathcal{L}}{\partial x}&=2x+\lambda(-2(x-2))=2x-2\lambda(x-2)=0\\
\frac{\partial\mathcal{L}}{\partial \lambda}&=1-(x-2)^2=0
\end{aligned}
$$

---
layout: prism
heading: "NOTE: Lagrange Multiplier"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Now, we have simultaneous equations:

$$
\begin{cases}
2x-2\lambda(x-2)=0\\
1-(x-2)^2=0
\end{cases}
$$

- The solutions are:

$$
\begin{aligned}
&(x, \lambda)=(1,-1)\\
&(x,\lambda)=(3,3)
\end{aligned}
$$

<div class="sub-item">

Finally, we achieve the minimum point $f(x=1)=1^2=1$ and the maximum point $f(x=3)=3^2=9$.

</div>

- _Consider this problem in the geometric viewpoint._

---
layout: prism
heading: Multinomial Variables (3/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Here, the function we want to find the maximum is log-likelihood:

$$
\ln p(\mathcal{D}|\boldsymbol{\mu})=\ln\prod_{k=1}^{K}\mu_k^{m_k}=\sum_{k=1}^{K}m_k\ln \mu_k.
$$

- We now use a [Lagrange multiplier]{.hl} $\lambda$:

$$
\sum_{k=1}^{K}m_k \ln \mu_k + \lambda\left(\sum_{k=1}^{K}\mu_k-1\right).
$$

<div class="sub-item">

We differentiate the above equation w.r.t. $\mu_k$ and set $0$, then acquire $\mu_k=-m_k/\lambda$.

</div>

- Under the constraint $\sum_k\mu_k=1$, we know $\lambda=-N$, the finally get the ML solution.

$$
\mu_k^\mathrm{ML}=\frac{m_k}{N}
$$

---
layout: prism
heading: Multinomial Variables (4/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- A joint probabilistic distribution of $m_1,\ldots,m_k$ decided by $\boldsymbol{\mu}$ and the number of observations $N$ is defined as follows, and called [multinomial distribution]{.hl}

$$
\operatorname{Mult}(m_1,m_2,\ldots,m_k|\boldsymbol{\mu}, N)=\binom{N}{m_1m_2\cdots m_k}\prod_{k=1}^{K}\mu_k^{m_k},\ \sum_{k=1}^{K}m_k=N.
$$

<div class="sub-item">

Here $\binom{N}{m_1m_2\cdots m_K}\equiv\frac{N!}{m_1!m_2!\cdots m_K!}$.

</div>

---
layout: prism
heading: Dirichlet Distribution
---

- There is a conjugate distribution for the multinomial distribution is [Dirichlet distribution]{.hl}

$$
\mathrm{Dir}(\boldsymbol{\mu}|\boldsymbol{\alpha})=\frac{\Gamma(\alpha_0)}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_K)}\prod_{k=1}^{K}\mu_k^{\alpha_k-1}, \quad \alpha_0=\sum_{k=1}^{K}\alpha_k.
$$

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.4.png" class="img-center" style="width: 14rem;" />

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Discrete Random Variables</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Multinomial Variables</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Gaussian Distribution</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Conditional Gaussian Distribution</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Marginal Gaussian Distribution</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Bayes' Theorem for Gaussian Random Variables</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Maximum Likelihood for Gaussian Random Variables</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Mixture of Gaussians</span></p>
  </div>

</div>

---
layout: prism
heading: Gaussian Distribution (1/2)
---

- For a single r.v. $x$, Gaussian distribution is given by

$$
\mathcal{N}(x|\mu,\sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{-\frac{1}{2\sigma^2}(x-\mu)^2\right\}.
$$

- For a $D$-dimensional vector $\mathbf{x}$, Gaussian distribution becomes

$$
\mathcal{N}(\mathbf{x}|\boldsymbol{\mu}, \boldsymbol{\Sigma})=\frac{1}{(2\pi)^{D/2}}\frac{1}{|\boldsymbol{\Sigma}|^{1/2}}\exp\left\{-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right\}.
$$

- Based on [central limit theorem]{.hl}, under certain conditions, an r.v. representing the sum of multiple r.v.s gradually approaches a Gaussian distribution as the number of summed variables increases.

<div class="img-row" style="max-width: 43%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.6a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.6b.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.6c.png"/>

</div>

---
layout: prism
heading: Gaussian Distribution (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- Gaussian distributions are used for modeling the probability density, but the calculation may be expensive if we treat high dimensional data or inverse matrix.

<div class="sub-item">

If we use a covariance matrix which has the form of [diagonal matrix]{.hl}, then the computation becomes tractable.

</div>

- Gaussian distribution is inherently [unimodal]{.hl}, so it cannot represent [multimodal]{.hl} data distribution.

<div class="sub-item">

In machine learning, many approaches introduce [latent variable]{.hl} to tackle this issue.

</div>

---
layout: prism
heading: Conditional Gaussian Distribution (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- If two variable sets have Gaussian distributions respectively, then a conditional distribution of a set given another set also has Gaussian distribution.

<div class="sub-item">

Marginal distributions of each variable set also has Gaussian form.

</div>

- Suppose that a $D$-dimensional vector $\mathbf{x}$ is $\mathcal{N}(\mathbf{x}|\boldsymbol{\mu},\boldsymbol{\Sigma})$ and $\mathbf{x}$ is divided into two separated vectors $\mathbf{x}_a$ and $\mathbf{x}_b$.

<div class="sub-item">

WLOG, $\mathbf{x}_a$ has the first $M$ elements of $\mathbf{x}$ and $\mathbf{x}_b$ has the others.

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
heading: Conditional Gaussian Distribution (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.3em;
}
</style>

- We can calculate the follows:

$$
\begin{aligned}
-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})=&-\frac{1}{2}(\mathbf{x}_a-\boldsymbol{\mu}_a)^\top\boldsymbol{\Lambda}_{aa}(\mathbf{x}_a-\boldsymbol{\mu}_a)-\frac{1}{2}(\mathbf{x}_a-\boldsymbol{\mu}_a)^\top\boldsymbol{\Lambda}_{ab}(\mathbf{x}_b-\boldsymbol{\mu}_b)\\
&-\frac{1}{2}(\mathbf{x}_b-\boldsymbol{\mu}_b)^\top\boldsymbol{\Lambda}_{ba}(\mathbf{x}_a-\boldsymbol{\mu}_a)-\frac{1}{2}(\mathbf{x}_b-\boldsymbol{\mu}_b)^\top\boldsymbol{\Lambda}_{bb}(\mathbf{x}_b-\boldsymbol{\mu}_b)
\end{aligned}
$$

where $\Lambda$ is the inverse matrix of the covariance matrix, and called [precision matrix]{.hl}.

$$
\boldsymbol{\Lambda}\equiv\boldsymbol{\Sigma}^{-1}=\begin{pmatrix}
\boldsymbol{\Lambda}_{aa}& \boldsymbol{\Lambda}_{ab}\\
\boldsymbol{\Lambda}_{ba} & \boldsymbol{\Lambda}_{bb}
\end{pmatrix}
$$

- By [completing the square]{.hl}, we can conclude that the conditional distribution $p(\mathbf{x}_a|\mathbf{x}_b)$ is Gaussian with following parameters:

$$
\begin{aligned}
\boldsymbol{\mu}_{a|b}&=\boldsymbol{\mu}_a+\boldsymbol{\Sigma}_{a|b}\{\boldsymbol{\Lambda}_{aa}\boldsymbol{\mu}_a-\boldsymbol{\Lambda}_{ab}(\mathbf{x}_b-\boldsymbol{\mu}_b)\}\\
\boldsymbol{\Sigma}_{a|b}&=\boldsymbol{\Lambda}_{aa}^{-1}
\end{aligned}
$$

---
layout: prism
heading: Conditional Gaussian Distribution (3/3)
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
heading: "NOTE: Completing the Square"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- Note that a Gaussian distribution has the form:

$$
\mathcal{N}(x|\mu,\sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{-\frac{1}{2\sigma^2}(x-\mu)^2\right\}\propto\exp\{(x-\mu)^2/\sigma^2\}
$$

- Now, consider that a probabilistic distribution has the form:

$$
p(x)\propto\exp\left(-\frac{x^2-6x+10}{2}\right)
$$

<div class="sub-item">

Here is the question; is the above distribution Gaussian?

</div>

---
layout: prism
heading: "NOTE: Completing the Square"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- By completing the square, we can rewrite the given probabilistic distribution:

$$
p(x)\propto\exp\left(-\frac{x^2-6x+10}{2}\right)\propto\exp\left(-\frac{(x-3)^2+1}{2}\right)
$$

<div class="sub-item">

Here the constant $+1$ in the numerator only affects the normalization, but not the form of probabilistic distribution.

</div>

<div class="sub-item">

Therefore, we could conclude that the given probability distribution is Gaussian:

</div>

$$
p(x)\sim\mathcal{N}(3, 1)
$$

---
layout: prism
heading: Marginal Gaussian Distribution
---

- We have seen that if a joint probability distribution $p(\mathbf{x}_a,\mathbf{x}_b)$ is Gaussian, then its conditional probability distribution $p(\mathbf{x}_a|\mathbf{x}_b)$ is Gaussian.

- Similarly, the marginal distributions $p(\mathbf{x}_a)$ or $p(\mathbf{x}_b)$ are also Gaussian, for example

$$
p(\mathbf{x}_a)=\mathcal{N}(\mathbf{x}_a|\boldsymbol{\mu}_a,\boldsymbol{\Sigma}_{aa})
$$

<div class="img-row" style="max-width: 46%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.9a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.9b.png"/>

</div>

---
layout: prism
heading: "Bayes' Theorem for Gaussian R.V. (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- Assume that we have a linear Gaussian model, then we can define general forms of marginal distribution $p(\mathbf{x})$ and conditional distribution $p(\mathbf{y}|\mathbf{x})$:

$$
\begin{aligned}
p(\mathbf{x})&=\mathcal{N}(\mathbf{x}|\boldsymbol{\mu},\boldsymbol{\Lambda}^{-1})\\
p(\mathbf{y}|\mathbf{x})&=\mathcal{N}(\mathbf{y}|\mathbf{A}\mathbf{x}+\mathbf{b}, \mathbf{L}^{-1})
\end{aligned}
$$

<div class="sub-item">

Here $\boldsymbol{\mu}$, $\mathbf{A}$, and $\mathbf{b}$ are hyperparameters to control the mean and $\boldsymbol{\Lambda}$ and $\mathbf{L}$ are precision matrices.

</div>

---
layout: prism
heading: "Bayes' Theorem for Gaussian R.V. (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- To consider the joint distribution, we define $\mathbf{z}=\binom{\mathbf{x}}{\mathbf{y}}$, and consider the logarithm.

$$
\begin{aligned}
\ln p(\mathbf{z})= & \ln p(\mathbf{x})+\ln p(\mathbf{y} | \mathbf{x}) \\
= & -\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top \boldsymbol{\Lambda}(\mathbf{x}-\boldsymbol{\mu})\\& -\frac{1}{2}(\mathbf{y}-\mathbf{A} \mathbf{x}-\mathbf{b})^\top \mathbf{L}(\mathbf{y}-\mathbf{A} \mathbf{x}-\mathbf{b})+\text{const}
\end{aligned}
$$

<div class="sub-item">

Note that this is quadratic w.r.t. $\mathbf{z}$, which means $p(\mathbf{z})$ is Gaussian.

</div>

- Hence, we can calculate $\mathbb{E}[\mathbf{z}]$ and $\mathrm{cov}[\mathbf{z}]$ by completing the square of the above equation.

---
layout: prism
heading: "Bayes' Theorem for Gaussian R.V. (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- Finally, we could achieve the following expectations and covariances.

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
heading: "Maximum Likelihood for Gaussian R.V. (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Given dataset $\mathbf{X}=(\mathbf{x}_1,\ldots,\mathbf{x}_N)^\top$ and observations $\{\mathbf{x}_n\}$ are independently sampled from a multivariate Gaussian distribution, we can estimate the parameters of original distribution using maximum likelihood method.

- The log-likelihood function is:

$$
\begin{aligned}
\ln p(\mathbf{X} | \boldsymbol{\mu}, \boldsymbol{\Sigma})=&-\frac{N D}{2} \ln (2 \pi)-\frac{N}{2} \ln |\boldsymbol{\Sigma}|-\frac{1}{2} \sum_{n=1}^N\left(\mathbf{x}_n-\boldsymbol{\mu}\right)^{\top} \boldsymbol{\Sigma}^{-1}\left(\mathbf{x}_n-\boldsymbol{\mu}\right)
\end{aligned}
$$

<div class="sub-item">

The likelihood function is only dependent w.r.t. the following terms, which are sufficient statistics of Gaussian distribution:

</div>

$$
\sum_{n=1}^{N}\mathbf{x}_n,\qquad \sum_{n=1}^{N}\mathbf{x}_n\mathbf{x}_n^\top
$$

---
layout: prism
heading: "Maximum Likelihood for Gaussian R.V. (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- By performing differentiation, we can achieve the solutions as follows:

$$
\begin{aligned}
\boldsymbol{\mu}_{\mathrm{ML}}&=\frac{1}{N} \sum_{n=1}^N \mathbf{x}_n\\
\boldsymbol{\Sigma}_{\mathrm{ML}}&=\frac{1}{N} \sum_{n=1}^N\left(\mathbf{x}_n-\boldsymbol{\mu}_{\mathrm{ML}}\right)\left(\mathbf{x}_n-\boldsymbol{\mu}_{\mathrm{ML}}\right)^{\top}
\end{aligned}
$$

---
layout: prism
heading: Mixture of Gaussians (1/2)
---

- We can linearly overlap Gaussian distributions, thereby modeling multimodal data distribution.

<div class="sub-item">

In this viewpoint, we can infer _almost all_ continuous distributions with arbitrary fitness if we can use sufficient numbers of Gaussian distributions and control means, covariances, and coefficients of the linear combination.

</div>

<div class="img-row" style="max-width: 60%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.21a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure2.21b.png"/>

</div>

---
layout: prism
heading: Mixture of Gaussians (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- An overlap of $K$ Gaussian probability densities can be defined as

$$
p(\mathbf{x})=\sum_{k=1}^K \pi_k \mathcal{N}\left(\mathbf{x} | \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k\right)
$$

<div class="sub-item">

This is known as [mixture of Gaussians]{.hl}.

</div>

<div class="sub-item">

Each Gaussian distribution $\mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)$ is called a [component]{.hl} of the mixture.

</div>

<div class="sub-item">

The parameters $\pi_k$ are [mixing coefficients]{.hl} and satisfy the following constraints.

</div>

$$
\sum_{k=1}^K \pi_k=1,\qquad 0\leqslant \pi_k \leqslant 1
$$

<div class="subsub-item">

$\pi_k=p(k)$ is the prior probability that the $k$th component is selected, and the density $\mathcal{N}(\mathbf{x}|\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)=p(\mathbf{x}|k)$ is a probability of $\mathbf{x}$ given $k$.

</div>

<div class="subsub-item">

The posteriors $p(k|\mathbf{x})$ are often called [responsibilities]{.hl}.

</div>

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
