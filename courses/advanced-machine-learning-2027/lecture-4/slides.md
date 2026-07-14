---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 4
download: true
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-4-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 04: Linear Regression Models</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span class="text-gray-900 dark:text-gray-100">Linear Regression Models</span></p>
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
heading: Recap (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- For a discrete and binary r.v. we can use Bernoulli distribution:

$$
\mathrm{Bern}(x|\mu)=\mu^x(1-\mu)^{1-x}
$$

<div class="sub-item">

Here $\mu$ denotes the probability that $x=1$.

</div>

- The conjugate probabilistic distribution for Bernoulli distribution is Beta distribution which is given by:

$$
\mathrm{Beta}(\mu|a,b)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\mu^{a-1}(1-\mu)^{b-1}
$$

<div class="sub-item">

Here $a$ and $b$ respectively denote the effective numbers of observations for $x=1$ and $x=0$.

</div>

---
layout: prism
heading: Recap (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- For multiple choices, we use the following distribution:

$$
p(\mathbf{x}|\boldsymbol{\mu})=\prod_{k=1}^{K}\mu_k^{x_k}
$$

<div class="sub-item">

Here $\mu_k$ is the probability that $x_k=1$.

</div>

- The conjugate probabilistic distribution for multinomial distribution is Dirichlet distribution:

$$
\mathrm{Dir}(\boldsymbol{\mu}|\boldsymbol{\alpha})=\frac{\Gamma(\alpha_0)}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_K)}\prod_{k=1}^{K}\mu_k^{\alpha_k-1},\qquad \alpha_0=\sum_{k=1}^{K}\alpha_k
$$

---
layout: prism
heading: Recap (3/3)
---

- Note that a Gaussian distribution has the form:

$$
\mathcal{N}(x|\mu,\sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{-\frac{1}{2\sigma^2}(x-\mu)^2\right\}
$$

- By completing the square, we can find whether a given probabilistic distribution is Gaussian or not.
  - We also studied Lagrange multiplier to estimate the maximum and minimum values of a given function with given constraints.

<div class="theorem-box">

<div class="theorem-box-title">Homework!</div>

<div class="theorem-box-body">

Find the maximum and minimum values of a function $f(x, y)=xy$ under the given constraint:

$$
x^2+4y^2=8
$$

</div>
</div>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Advance: Gaussian Distribution and Maximum Likelihood Estimation</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Linear Basis Function Model</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bias–Variance Tradeoff</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bayesian Linear Regression</span></p>
  </div>

</div>

---
layout: prism
heading: "Advance: Gaussian Distribution and MLE (1/7)"
---

- Let us assume that we observe a dataset and each datapoint is [independently and identically distributed]{.hl} (i.i.d.) from Gaussian distribution:

$$
p(x_n)\sim\mathcal{N}(x_n|\mu,\sigma^2).
$$

- The likelihood function of the dataset is given by:

$$
p(\boldsymbol{\mathsf{x}}|\mu,\sigma^2)=\prod_{n=1}^{N}p(x_n)=\prod_{n=1}^{N}\mathcal{N}(x_n|\mu,\sigma^2).
$$

<div class="sub-item">

$\boldsymbol{\mathsf{x}}=(x_1,\ldots,x_N)$ and $N$ is the number of observed datapoints.

</div>

<div class="sub-item">

The log likelihood is defined as

</div>

$$
\ln p(\boldsymbol{\mathsf{x}}|\mu,\sigma^2)=\sum_{n=1}^{N}\ln p(x_n)=\sum_{n=1}^{N}\ln\left\{ \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(- \frac{(x_n-\mu)^2}{2\sigma^2} \right)\right\}.
$$

---
layout: prism
heading: "Advance: Gaussian Distribution and MLE (2/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- We re-derive the log likelihood function $L(\mu,\sigma^2)$ using the properties of logarithm:

$$
\begin{aligned}
\ln p(\boldsymbol{\mathsf{x}}|\mu,\sigma^2)&=\sum_{n=1}^{N}\ln\left\{ \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(- \frac{(x_n-\mu)^2}{2\sigma^2} \right) \right\}\\
&=\sum_{n=1}^{N}\left[ -\frac{1}{2}\ln(2\pi\sigma^2)-\frac{(x_n-\mu)^2}{2\sigma^2}  \right]\\
\therefore L(\mu,\sigma^2)&=-\frac{N}{2}\ln(2\pi\sigma^2)-\frac{1}{2\sigma^2}\sum_{n=1}^{N}(x_n-\mu)^2.
\end{aligned}
$$

<div class="sub-item">

Now we can find the ML solutions by solving $\frac{\partial L(\mu,\sigma^2)}{\partial \mu}=0$ and $\frac{\partial L(\mu,\sigma^2)}{\partial \sigma^2}=0$

</div>

---
layout: prism
heading: "Advance: Gaussian Distribution and MLE (3/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

$$
\begin{aligned}
\frac{\partial L(\mu,\sigma^2)}{\partial \mu}&=-\frac{1}{2\sigma^2}\cdot 2\sum_{n=1}^{N}(x_n-\mu)(-1)=\frac{1}{\sigma^2}\sum_{n=1}^{N}(x_n-\mu)=0\\
\sum_{n=1}^{N}(x_n-\mu)&=0\quad\Rightarrow\quad\sum_{n=1}^{N}x_n=\sum_{n=1}^{N}\mu=N\mu\\
\therefore \mu_{\mathrm{ML}}&=\frac{1}{N}\sum_{n=1}^{N}x_n
\end{aligned}
$$

- Note that $\mu_\mathrm{ML}$ is called the sample mean.

---
layout: prism
heading: "Advance: Gaussian Distribution and MLE (4/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

$$
\begin{aligned}
\frac{\partial L(\mu,\sigma^2)}{\partial \sigma^2}&=-\frac{N}{2}\frac{1}{\sigma^2}+\frac{1}{2(\sigma^2)^2}\sum_{n=1}^{N}(x_n-\mu)^2=-\frac{N}{2\sigma^2}+\frac{1}{2\sigma^4}\sum_{n=1}^{N}(x_n-\mu)^2=0\\
N\sigma^2&=\sum_{n=1}^{N}(x_n-\mu)^2\quad\Rightarrow\quad \sigma^2=\frac{1}{N}\sum_{n=1}^{N}(x_n-\mu)^2\\
\therefore\sigma^2_\mathrm{ML}&=\frac{1}{N}\sum_{n=1}^{N}(x_n-\mu_\mathrm{ML})^2
\end{aligned}
$$

- Note that $\sigma_\mathrm{ML}^2$ is called the sample variance.

---
layout: prism
heading: "Advance: Gaussian Distribution and MLE (5/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 4em;
}
</style>

- Let us find the expectation values of the sample mean and the sample variance.

$$
\mathbb{E}[\mu_{\mathrm{ML}}]=\mathbb{E}\left[\frac{1}{N}\sum_{n=1}^{N}x_n\right]=\frac{1}{N}\sum_{n=1}^{N}\mathbb{E}[x_n]=\frac{1}{N}(N\mu)=\mu
$$

<div class="sub-item">

Note that the expectation value is NOT biased.

</div>

---
layout: prism
heading: "Advance: Gaussian Distribution and MLE (6/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

$$
\begin{aligned}
\mathbb{E}[\sigma^2_\mathrm{ML}]&=\mathbb{E}\left[ \frac{1}{N}\sum_{n=1}^{N}(x_n-\mu_\mathrm{ML})^2 \right]=\mathbb{E}\left[ \frac{1}{N}\sum_{n=1}^{N}(x_n-\mu+\mu- \mu_\mathrm{ML})^2 \right]\\
&=\mathbb{E}\left[\frac{1}{N}\sum_{n=1}^{N}(x_n-\mu)^2\right]-\mathbb{E}[(\mu_{\mathrm{ML}}-\mu)^2]\\
&=\sigma^2-\mathrm{Var}[\mu_{\mathrm{ML}}]=\sigma^2-\mathrm{Var}\left[\frac{1}{N}\sum_{n=1}^{N}x_n\right]=\sigma^2 -\frac{1}{N^2}\sum_{n=1}^{N}\mathrm{Var}[x_n]\\
&=\frac{N-1}{N}\sigma^2
\end{aligned}
$$

- Note that the expectation is biased.

---
layout: prism
heading: "Advance: Gaussian Distribution and MLE (7/7)"
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(0)

true_mu, true_sigma2 = 5.0, 2.0
N = 10
n_trials = 100000

sample_means = np.empty(n_trials)
sample_vars_ml = np.empty(n_trials)

for i in range(n_trials):
    x = rng.normal(true_mu, np.sqrt(true_sigma2), size=N)
    mu_ml = x.mean()
    sample_means[i] = mu_ml
    sample_vars_ml[i] = np.mean((x - mu_ml) ** 2)

print(f"true sigma^2 = {true_sigma2}")
print(f"(N-1)/N * true sigma^2 = {(N - 1) / N * true_sigma2:.4f}  (predicted by the slide's formula)")
print()
print(f"E[mu_ML] over {n_trials} trials = {sample_means.mean():.4f}  (should be close to true mu = {true_mu})")
print(f"E[sigma^2_ML] over {n_trials} trials = {sample_vars_ml.mean():.4f}  (biased, should match (N-1)/N * sigma^2)")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Advance: Gaussian Distribution and Maximum Likelihood Estimation</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Linear Basis Function Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Maximum Likelihood and Least Squares</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Sequential Learning</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Regularized Least Squares</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bias–Variance Tradeoff</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bayesian Linear Regression</span></p>
  </div>

</div>

---
layout: prism
heading: Linear Basis Function Model (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- For $\mathbf{x}=(x_1,\ldots,x_D)$, we can define a [linear regression]{.hl} model based on a linear combination of the input variables:

$$
y(\mathbf{x},\mathbf{w})=w_0+w_1x_1+\cdots+x_Dw_D
$$

<div class="sub-item">

$\mathbf{w}=(w_0,\ldots,w_D)^\top$.

</div>

- Here, we can define a linear combination of fixed nonlinear functions

$$
y(\mathbf{x},\mathbf{w})=w_0+\sum_{j=1}^{M-1}w_j\phi_j(\mathbf{x})
$$

<div class="sub-item">

$\phi_j(\mathbf{x})$ is a [basis function]{.hl}.

</div>

<div class="sub-item">

$w_0$ represents a fixed offset, and sometimes called [bias]{.hl} parameter.

</div>

<div class="subsub-item">

For the convenience, we introduce a pseudo-basis function $\phi_0(\mathbf{x})=1$, then we derive $y(\mathbf{x},\mathbf{w})=\sum_{j=0}^{M-1}w_j\phi_j(\mathbf{x})=\mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})$, where $\boldsymbol{\phi}=(\phi_0,\ldots,\phi_{M-1})^\top$ and $\mathbf{w}$ becomes $(w_0,\ldots,w_{M-1})^\top$.

</div>

---
layout: prism
heading: Linear Basis Function Model (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- There are many kinds of basis functions.

- The following is the Gaussian basis function

$$
\phi_j({x})=\exp \left\{-\frac{\left(x-\mu_j\right)^2}{2 s^2}\right\}
$$

- The following is [sigmoid]{.hl} basis function

$$
\phi_j(x)=\sigma\left(\frac{x-\mu_j}{s}\right)
$$

<div class="sub-item">

Here $\sigma(a)$ is the [logistic sigmoid]{.hl} function

</div>

$$
\sigma(a)=\frac{1}{1+\exp (-a)}
$$

---
layout: prism
heading: Maximum Likelihood and Least Squares (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- Assume that the target variable $t$ can be represented as a Gaussian distribution which has the mean of $y(\mathbf{x},\mathbf{w})$ and the precision of $\beta$

$$
\begin{aligned}
t&=y(\mathbf{x}, \mathbf{w})+\epsilon\\
p(t|\mathbf{x},\mathbf{w},\beta)&=\mathcal{N}(t|y(\mathbf{x},\mathbf{w}),\beta^{-1})
\end{aligned}
$$

- If we use the sum-squared error function, the optimal prediction is given by the conditional expectation:

$$
\mathbb{E}[t | \mathbf{x}]=\int t\, p(t | \mathbf{x}) \,\mathrm{d} t=y(\mathbf{x}, \mathbf{w})
$$

---
layout: prism
heading: Maximum Likelihood and Least Squares (2/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Given dataset $\mathbf{X}=\{\mathbf{x}_1,\ldots,\mathbf{x}_N\}$ and corresponding target variables $\boldsymbol{\mathsf{t}}=\{t_1,\ldots,t_N\}$, we can write the likelihood function as follows:

$$
p(\boldsymbol{\mathsf{t}} | \mathbf{X}, \mathbf{w}, \beta)=\prod_{n=1}^N \mathcal{N}(t_n | \mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n), \beta^{-1})
$$

<div class="sub-item">

From here, we use $p(\boldsymbol{\mathsf{t}}|\mathbf{w},\beta)$ to represent the likelihood function since the regression problem does not need to model the distribution of the input variables.

</div>

- The log likelihood function can be denoted as:

$$
\ln p(\boldsymbol{\mathsf{t}} | \mathbf{w}, \beta)  =\sum_{n=1}^N \ln \mathcal{N}(t_n | \mathbf{w}^{\top} \phi(\mathbf{x}_n), \beta^{-1}) =\frac{N}{2} \ln \beta-\frac{N}{2} \ln (2 \pi)-\beta E_D(\mathbf{w})
$$

<div class="sub-item">

The sum-squared error function is defined as: $E_D(\mathbf{w})=\frac{1}{2} \sum_{n=1}^N\{t_n-\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)\}^2$.

</div>

---
layout: prism
heading: Maximum Likelihood and Least Squares (3/4)
---

- To estimate the maximum likelihood, we differentiate the log likelihood function w.r.t. $\mathbf{w}$ and set $0$:

$$
\begin{aligned}
\nabla \ln p(\boldsymbol{\mathsf{t}} | \mathbf{w}, \beta)&=\beta \sum_{n=1}^N\{t_n-\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)\} \boldsymbol{\phi}(\mathbf{x}_n)^{\top}\\
0&=\sum_{n=1}^N t_n \phi(\mathbf{x}_n)^{\top}-\mathbf{w}^{\top}\left\{\sum_{n=1}^N \phi(\mathbf{x}_n) \boldsymbol{\phi}(\mathbf{x}_n)^{\top}\right\}\quad\Rightarrow\quad \mathbf{w}_{\mathrm{ML}}=(\boldsymbol{\Phi}^{\top} \boldsymbol{\Phi})^{-1} \boldsymbol{\Phi}^{\top} \boldsymbol{\mathsf{t}}
\end{aligned}
$$

- The above equation is known as [normal equation]{.hl} for the least square problem, and $\boldsymbol{\Phi}$ is an $N\times M$ matrix and called [design matrix]{.hl}

$$
\boldsymbol{\Phi}=\left(\begin{array}{cccc}
\phi_0(\mathbf{x}_1) & \phi_1(\mathbf{x}_1) & \cdots & \phi_{M-1}(\mathbf{x}_1) \\
\phi_0(\mathbf{x}_2) & \phi_1(\mathbf{x}_2) & \cdots & \phi_{M-1}(\mathbf{x}_2) \\
\vdots & \vdots & \ddots & \vdots \\
\phi_0(\mathbf{x}_N) & \phi_1(\mathbf{x}_N) & \cdots & \phi_{M-1}(\mathbf{x}_N)
\end{array}\right)
$$

---
layout: prism
heading: "NOTE: Normal Equation"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- For simplicity, assume that we use a linear basis function $\phi(x)=x$.

- Now, for given dataset $\mathbf{x}$ and $\boldsymbol{\mathsf{t}}$, we have to find an optimal regression model by solving the least squares problem:

$$
\mathbf{x}=
\begin{pmatrix}
1\\
2\\
3
\end{pmatrix}\qquad
\boldsymbol{\mathsf{t}}=\begin{pmatrix}
2\\
3\\
5
\end{pmatrix}
$$

- With the offset, we build the design matrix

$$
\boldsymbol{\Phi}=\begin{pmatrix}
\phi_0(x_1) & \phi_1(x_1)\\
\phi_0(x_2) & \phi_1(x_2)\\
\phi_0(x_3) & \phi_1(x_3)
\end{pmatrix}
=
\begin{pmatrix}
1&1\\
1&2\\
1&3
\end{pmatrix}
$$

---
layout: prism
heading: "NOTE: Normal Equation"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- Now, we have to solve the following equation:

$$
\boldsymbol{\Phi}\mathbf{w}=\boldsymbol{\mathsf{t}}
$$

- We can derive the following equations

$$
\begin{aligned}
\boldsymbol{\Phi}^{\top}\boldsymbol{\Phi}\mathbf{w}&=\boldsymbol{\Phi}^{\top}\boldsymbol{\mathsf{t}}\\
\mathbf{w}&=(\boldsymbol{\Phi}^{\top}\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^{\top}\boldsymbol{\mathsf{t}}\\
\therefore \mathbf{w}&=
\left(
\begin{pmatrix}
1 & 1 & 1\\
1 & 2 & 3
\end{pmatrix}
\begin{pmatrix}
1&1\\
1&2\\
1&3
\end{pmatrix}
\right)^{-1}
\begin{pmatrix}
1 & 1 & 1\\
1 & 2 & 3
\end{pmatrix}
\begin{pmatrix}
2\\
3\\
5
\end{pmatrix}
\simeq
\begin{pmatrix}
0.333\\
1.5
\end{pmatrix}
\end{aligned}
$$

- Finally we get our linear regression model:

$$
t=0.333+1.5x
$$

---
layout: prism
heading: "NOTE: Normal Equation"
---

<PyRunner>

```python
import numpy as np

x = np.array([1, 2, 3])
t = np.array([2, 3, 5])

Phi = np.column_stack([np.ones_like(x), x])  # design matrix: [phi_0(x), phi_1(x)] = [1, x]

w_ml = np.linalg.inv(Phi.T @ Phi) @ Phi.T @ t

print("Design matrix Phi:\n", Phi)
print("\nw_ML =", np.round(w_ml, 4))
print(f"\nFitted model: t = {w_ml[0]:.3f} + {w_ml[1]:.3f} * x")
print("\nMatches the slide's answer (0.333, 1.5)?", np.allclose(w_ml, [0.333, 1.5], atol=1e-3))
```

</PyRunner>

---
layout: prism
heading: Maximum Likelihood and Least Squares (4/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- Note that the least square solution is a vector which minimizes errors of $(\mathbf{x},\boldsymbol{\mathsf{t}})$.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure3.2.png" class="img-center" style="width: 26rem;" />

---
layout: prism
heading: Sequential Learning (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The design matrix use whole training dataset at once, and it is known as [batch learning]{.hl}.

<div class="sub-item">

Consider if we have a large dataset, then it cannot be computed.

</div>

- For the large dataset, we use the [sequential]{.hl} algorithm

<div class="sub-item">

In the literature of deep learning, we used the term, [mini-batch learning]{.hl}.

</div>

<div class="sub-item">

In the sequential algorithm, only partial datapoints are considered for each model update.

</div>

- The [stochastic gradient descent]{.hl} algorithm update the parameter vector as follows

$$
\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}-\eta \nabla E_n
$$

<div class="sub-item">

Here $\tau$ and $\eta$ respectively denote the number of iterations and the learning rate.

</div>

<div class="sub-item">

At beginning, $\mathbf{w}$ is initiated by a temporal vector $\mathbf{w}^{(0)}$.

</div>

- If we use the sum-squared error function above for the stochastic gradient descent, it is often called [least mean squares (LMS)]{.hl} algorithm.

---
layout: prism
heading: Sequential Learning (2/2)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(1)

# A slightly larger toy dataset than the Normal Equation example
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
t = np.array([2.0, 3.0, 5.0, 6.0, 8.0])
Phi = np.column_stack([np.ones_like(x), x])

# Closed-form (batch) solution
w_batch = np.linalg.inv(Phi.T @ Phi) @ Phi.T @ t

# Stochastic gradient descent (one datapoint at a time)
w_sgd = np.zeros(2)
eta = 0.01
n_epochs = 2000

for epoch in range(n_epochs):
    idx = rng.permutation(len(x))
    for i in idx:
        phi_n = Phi[i]
        error_n = t[i] - w_sgd @ phi_n
        w_sgd = w_sgd + eta * error_n * phi_n  # w <- w + eta * error_n * phi(x_n)

print("w from Normal Equation (batch):", np.round(w_batch, 4))
print("w from SGD after", n_epochs, "epochs:  ", np.round(w_sgd, 4))
print("\nDo they converge to the same solution?", np.allclose(w_batch, w_sgd, atol=5e-2))
```

</PyRunner>

---
layout: prism
heading: Regularized Least Squares
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- We can add a penalty term to regularize, then the generalized form can be written as

$$
\frac{1}{2} \sum_{n=1}^N\{t_n-\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)\}^2+\frac{\lambda}{2} \sum_{j=1}^M|w_j|^q
$$

<div class="sub-item">

For $q=2$, the model becomes a ridge regression, and for $q=1$, the model becomes a lasso regression.

</div>

<div class="subsub-item">

For sufficiently large $\lambda$, some parameters $w_j$ may become $0$, and the model is called [sparse]{.hl} model in this case.

</div>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Advance: Gaussian Distribution and Maximum Likelihood Estimation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Linear Basis Function Model</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Bias–Variance Tradeoff</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bayesian Linear Regression</span></p>
  </div>

</div>

---
layout: prism
heading: "Bias–Variance Tradeoff (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- Given conditional distribution $p(t|\mathbf{x})$, then the optimal prediction $h(\mathbf{x})$ can be estimated as:

$$
h(\mathbf{x})=\mathbb{E}[t|\mathbf{x}]=\int t\, p(t|\mathbf{x})\,\mathrm{d}t
$$

- Now the expected squared error can be estimated as:

$$
\mathbb{E}[L]=\int\{y(\mathbf{x})-h(\mathbf{x})\}^2 p(\mathbf{x}) \,\mathrm{d} \mathbf{x}+\iint\{h(\mathbf{x})-t\}^2 p(\mathbf{x}, t) \,\mathrm{d} \mathbf{x} \,\mathrm{d} t
$$

<div class="sub-item">

Here the second term independent with $y(\mathbf{x})$ is caused from the intrinsic noise of data.

</div>

<div class="sub-item">

The first term is determined by our selection of the function $y(\mathbf{x})$, hence our goal is to find $y(\mathbf{x})$ which minimizes the magnitude of the first term.

</div>

---
layout: prism
heading: "Bias–Variance Tradeoff (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- In the viewpoint of the frequentist, we point-estimate $\mathbf{w}$ using the dataset $\mathcal{D}$.

<div class="sub-item">

In this case, the integrand in the first term of $\mathbb{E}[L]$ is equal to the following equation:

</div>

$$
\{y(\mathbf{x};\mathcal{D}) -h(\mathbf{x})\}^2
$$

<div class="subsub-item">

This value is dependent on $\mathcal{D}$.

</div>

$$
\begin{aligned}
\{y(\mathbf{x} ; \mathcal{D})-\mathbb{E}_{\mathcal{D}}[&y(\mathbf{x} ; \mathcal{D})]+\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]-h(\mathbf{x}) \}^2 \\
=&\left\{y(\mathbf{x} ; \mathcal{D})-\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]\right\}^2+\left\{\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]-h(\mathbf{x})\right\}^2 \\
&+2\left\{y(\mathbf{x} ; \mathcal{D})-\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]\right\}\left\{\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]-h(\mathbf{x})\right\}
\end{aligned}
$$

<div class="sub-item">

We now take the expectation of this expression w.r.t. $\mathcal{D}$ and note that the final term will vanish, giving,

</div>

$$
\begin{aligned}
\mathbb{E}_{\mathcal{D}}\left[\{y(\mathbf{x} ; \mathcal{D})-h(\mathbf{x})\}^2\right] =\underbrace{\left\{\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]-h(\mathbf{x})\right\}^2}_{(\text{bias})^2}+\underbrace{\mathbb{E}_{\mathcal{D}}\left[\left\{y(\mathbf{x} ; \mathcal{D})-\mathbb{E}_{\mathcal{D}}[y(\mathbf{x} ; \mathcal{D})]\right\}^2\right]}_{\text{variance}}
\end{aligned}
$$

---
layout: prism
heading: "Bias–Variance Tradeoff (3/3)"
---

- The first [bias]{.hl} term represents the extent to which the average prediction over all datasets differ from the desired regression function.

- The second [variance]{.hl} measures the extent to which the solutions for individual datasets vary around their average, and hence this measures the extent to which the function $y(\mathbf{x};\mathcal{D})$ is sensitive to the particular choice of dataset.

- The expected loss can be decomposed as the squared bias, the variance, and the noise, and has the [bias–variance tradeoff]{.hl}.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure3.6.png" class="img-center" style="width: 12rem;" />

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Advance: Gaussian Distribution and Maximum Likelihood Estimation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Linear Basis Function Model</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bias–Variance Tradeoff</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Bayesian Linear Regression</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Parameter Distribution</span></p>
  </div>

</div>

---
layout: prism
heading: Parameter Distribution
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- For full Bayesian linear regression, we introduce the prior distribution for the model parameter, $p(\mathbf{w})$.

- Assume that our precision $\beta$ is a known constant, and the likelihood function $p(\boldsymbol{\mathsf{t}}|\mathbf{w})$ is an exponential function of a quadratic function of $\mathbf{w}$.

<div class="sub-item">

We can set the conjugate prior distribution as follows

</div>

$$
p(\mathbf{w})=\mathcal{N}\left(\mathbf{w} | \mathbf{m}_0, \mathbf{S}_0\right).
$$

<div class="sub-item">

$\mathbf{m}_0$ and $\mathbf{S}_0$ are the mean and the covariance.

</div>

<div class="sub-item">

Note that the posterior distribution is also Gaussian.

</div>

- By completing the square, we can estimate coefficients and find the posterior distribution.

$$
\begin{aligned}
p(\mathbf{w} | \boldsymbol{\mathsf{t}})&=\mathcal{N}(\mathbf{w} | \mathbf{m}_N, \mathbf{S}_N)\\
\mathbf{m}_N & =\mathbf{S}_N(\mathbf{S}_0^{-1} \mathbf{m}_0+\beta \boldsymbol{\Phi}^{\top} \boldsymbol{\mathsf{t}}) \\
\mathbf{S}_N^{-1} & =\mathbf{S}_0^{-1}+\beta \boldsymbol{\Phi}^{\top} \boldsymbol{\Phi}
\end{aligned}
$$

---
layout: prism
heading: Predictive Distribution
---

<style>
.slidev-layout ul > li {
  margin-top: 4em;
}
</style>

- To predict a new target value $t$ for given new input $\mathbf{x}$, we consider the following [predictive distribution]{.hl}.

$$
\begin{aligned}
p(t | \boldsymbol{\mathsf{t}}, \alpha, \beta)&=\int p(t | \mathbf{w}, \beta)\, p(\mathbf{w} | \boldsymbol{\mathsf{t}}, \alpha, \beta) \,\mathrm{d} \mathbf{w}\\
&=\mathcal{N}(t | \mathbf{m}_N^{\top} \boldsymbol{\phi}(\mathbf{x}), \sigma_N^2(\mathbf{x}))\\
\sigma_N^2(\mathbf{x})&=\frac{1}{\beta}+\phi(\mathbf{x})^{\top} \mathbf{S}_N \phi(\mathbf{x})
\end{aligned}
$$

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}