---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff' # Sets a custom hex background color
title: AML - Lecture 2
download: true
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-2-ko/
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
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.jpeg" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Advanced Machine Learning</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 02: Course Introduction</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span class="text-gray-900 dark:text-gray-100">Preliminaries</span></p>
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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Continuous Latent Variables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Introduction</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Introduction</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Polynomial Curve Fitting</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probability Theory</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Model Selection & Curse of Dimensionality</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Decision Theory</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Information Theory</span></p>
  </div>

</div>

---
layout: prism
heading: Introduction
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- Recognizing patterns from given data is one of the most important problems we have.

- Human beings have been pursuing answers to tackle the pattern recognition problems and successfully finds meaningful patterns for many cases.

- Johannes Keper discovered Kepler’s laws of planetary motion from a massive amount of astronomical data observed by Tycho Brahe, at 16th century.


---
layout: prism
heading: Polynomial Curve Fitting (1/4)
---

- Let us consider the following [regression]{.hl} problem.

$$
y(x, \mathbf{w})=w_0 + w_1 x + w_2 x^2 + \cdots + w_M x^M = \sum_{j=0}^{M} w_j x^j
$$

<div class="sub-item">

$M$ represents an [order]{.hl} of the polynomial, and a vector $\mathbf{w}$ denotes the polynomial coefficients, $w_0,...,w_M$.

</div>

<div class="sub-item">

The polynomial function $y(x, \mathbf{w})$ is nonlinear w.r.t. $x$, but linear w.r.t. $\mathbf{w}$.

</div>

<div style="height: 0.7rem;"></div>

- We can determine the coefficients by [fitting]{.hl} the polynomial $y(x, \mathbf{w})$ to given [training data]{.hl}.
  - To do so, we define an [error function]{.hl} to estimate an error between target values $t$ of training dataset and function values $y(x,\mathbf{w})$, and fit the coefficients by minimizing the error.

$$
E(\mathbf{w})=\frac{1}{2}\sum_{n=1}^N \{ y(x_n, \mathbf{w}) - t_n \}^2
$$

<div class="sub-item">

This function always returns a positive value, and could be $0$ if the function value is exactly same with the target.

</div>

---
layout: prism
heading: Polynomial Curve Fitting (2/4)
---

- We can select $\mathbf{w}$ which minimizes $E(\mathbf{w})$ to solve the problem.
  - Note that the errror function has a quadratic form, thus we can achieve a unique $\mathbf{w}^\star$ by differentiating the function w.r.t. its coefficients.

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.3.png" class="img-center" style="height: 15rem;" />

---
layout: prism
heading: Polynomial Curve Fitting (3/4)
---

- There still remain a problem to determine the order $M$, and it is known as [model selection]{.hl} problem.

- Note that each constant ($M = 0$) or linear ($M = 1$) function does not fit well, but a cubic ($M = 3$) function does.
  - For the higher order ($M = 9$), the function is able to exactly fit to the training set and this case we achieve $E(\mathbf{w}^\star) = 0$.
  - But, the curve highly oscciliates and fails to express the trigonometric function, and this phenomenon is known as [overfitting]{.hl}.

<div style="height: 0.1rem;"></div>

<div class="img-row" style="max-width: 90%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.4a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.4b.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.4c.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.4d.png"/>

</div>

---
layout: prism
heading: Polynomial Curve Fitting (4/4)
---

- To tacke the overfitting issue, a [regularization]{.hl} trick is widely used.
  - To regularize, we can consider that adding a penalty term to the error function to suppress the magnitude of coefficients.

$$
\tilde{E}(\mathbf{w})=\frac{1}{2}\sum_{n=1}^N \{ y(x_n, \mathbf{w}) - t_n \}^2 + \frac{\lambda}{2}\|\mathbf{w}\|^2
$$

<div class="subsub-item">

$\|\mathbf{w}\|^2 \equiv \mathbf{w}^\top \mathbf{w} = w_0^2 + w_1^2 + \cdots + w_M^2$

</div>

<div style="height: 1.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.7a.png" style="float: right; width: 12rem; margin: 1rem 0rem 0 0rem;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.7b.png" style="float: right; width: 12rem; margin: 1rem 1rem 0 1.5rem;" />

- $\lambda$ controls the relative effect of the regularization terms.

- This regularization techniques is known as shrinkage method or [ridge regression]{.hl}.

<div class="subsub-item">

In the viewpoint of the neural network, it is called [weight decay]{.hl}.

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 0rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Introduction</span></p>
<p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Probability Theory</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Basic Laws</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Probability Density</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Expectation and Covariance</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Bayesian Probability</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Gaussian Distribution</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Curve Fitting</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Bayesian Curve Fitting</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Model Selection & Curse of Dimensionality</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Decision Theory</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Information Theory</span></p>
  </div>

</div>

---
layout: prism
heading: Probability Theory (1/3)
---

<div class="theorem-box">

<div class="theorem-box-title">The basic laws of probability</div>

<div class="theorem-box-body">

Let us denote that $p(X, Y)$ as a [joint probability]{.hl} of $X$ and $Y$, and $p(Y|X)$ as a [conditional probability]{.hl} of $Y$ given $X$, and $p(X)$ as a marginal probability of $X$, then the following laws holds true.

_Sum rule_

$$
p(X) = \sum_Y p(X,Y)
$$

_Product rule_

$$
p(X,Y) = P(Y|X)P(X)
$$

</div>
</div>

---
layout: prism
heading: Probability Theory (2/3)
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

joint = np.array([
    [0.10, 0.05],
    [0.20, 0.15],
    [0.30, 0.20],
])

p_X = joint.sum(axis=1)
print("p(x) estimated by Sum rule:", p_X)

p_Y_given_X = joint / p_X[:, None]
reconstructed = p_Y_given_X * p_X[:, None]
print("Product rule check:", np.allclose(joint, reconstructed))
```

</PyRunner>

---
layout: prism
heading: Probability Theory (3/3)
---

- We can derive [Bayes' theorem]{.hl} from the product rule and the symmetricity $P(X, Y) = P(Y, X)$.

$$
P(Y | X) = \frac{P(X | Y)P(Y)}{P(X)}
$$

<div class="subsub-item">

Here, $P(Y)$ is known as a [prior probability]{.hl} (a probability before observing $X$) and $P(Y | X)$ is known as a [posterior probability]{.hl} (a probability after observing $X$).

</div>

<PyRunner>

```python
import numpy as np

joint = np.array([[0.10, 0.05], [0.20, 0.15], [0.30, 0.20],])

p_X = joint.sum(axis=1)      # p(X)
p_Y = joint.sum(axis=0)      # p(Y)

p_X_given_Y = joint / p_Y[None, :]   # p(X|Y)
p_Y_given_X = joint / p_X[:, None]   # p(Y|X) (direct calculation)

p_Y_given_X_bayes = (p_X_given_Y * p_Y[None, :]) / p_X[:, None] # Bayes' theorem: p(Y|X) = p(X|Y) * p(Y) / p(X)

# print("Results of P(Y|X):", p_Y_given_X, p_Y_given_X_bayes)
print("Bayes' theorem check: ", np.allclose(p_Y_given_X, p_Y_given_X_bayes))
```

</PyRunner>

---
layout: prism
heading: Probability Density
---


- In a continuous space, if there exist a real variable $x \in (x, x + \delta x)$ and its probability is $p(x) \delta x$, $\delta x \rightarrow 0$, then $p(x)$ is called as a [probability density]{.hl} of $x$.
  - For a probability density, the followings holds true.

$$
p(x \in (a, b)) = \int_a^b p(x)\, \mathrm{d}x\\
p(x) \geq 0,\quad \int_{-\infty}^{\infty} p(x)\, \mathrm{d}x = 1
$$

<div style="height: 1.5rem;"></div>

- A [cumulative distribution function]{.hl} represents that a probability of $x$ is in the range of $(-\infty, z)$.

$$
P(z) = \int_{-\infty}^z p(x)\, \mathrm{d}x
$$

<div class="sub-item">

If $x$ is a discrete variable, then $p(x)$ is often called [probability mass function]{.hl}.

</div>

---
layout: prism
heading: Expectation and Covariance (1/2)
---

- Under a probabiilty density $p(x)$, an average of a function $f(x)$, $\mathbb{E}[f]$ is called [expectation]{.hl}.
  - For a discrete distribution, its expectation is defined as:

$$
\mathbb{E}[f] = \sum_x p(x)f(x)
$$

<div class="sub-item">

For a continuous distribution, the expectation is:

</div>

$$
\mathbb{E}[f] = \int p(x)f(x)\, \mathrm{d}x
$$

- Given $N$ datapoints, we can approximate the expectation as follows:

$$
\mathbb{E}[f] \approx \frac{1}{N}\sum_{n=1}^N f(x_n)
$$

- A [conditioned expectation]{.hl} can be estimated similarly.

---
layout: prism
heading: Expectation and Covariance (2/2)
---

- A [variance]{.hl} of $f(x)$ is defined as follows:

$$
\begin{aligned}
\operatorname{var}[f]&=\mathbb{E}[ (f(x)-\mathbb{E}[f(x)])^2 ]\\ 
&=\mathbb{E}[f(x)^2]-\mathbb{E}[f(x)]^2
\end{aligned}
$$

- For two variables $x$ and $y$, their \wj{covariance} is defined as follows:

$$
\begin{aligned}
\operatorname{cov}[x, y]&=\mathbb{E}_{x,y}[\{x-\mathbb{E}[x]\}\{y-\mathbb{E}[y]\}]\\
&=\mathbb{E}_{x,y}[xy]-\mathbb{E}[x]\mathbb{E}[y]
\end{aligned}
$$

<div class="sub-item">

A covariance is a measure indicating how much the values of $x$ and $y$ vary together.

</div>

<div class="sub-item">

For a continuous distribution, the expectation is:
If the variables are vectors, then their covariance becomes a matrix.
</div>

$$
\begin{aligned}
\operatorname{cov}[\mathbf{x}, \mathbf{y}]&=\mathbb{E}_{\mathbf{x}, \mathbf{y}}[ \{\mathbf{x}-\mathbb{E}[\mathbf{x}]\}\{\mathbf{y}^\top-\mathbb{E}[\mathbf{y}^\top]\} ]\\
&=\mathbb{E}_{\mathbf{x}, \mathbf{y}}[\mathbf{x}\mathbf{y}^\top]-\mathbb{E}[\mathbf{x}]\mathbb{E}[\mathbf{y}^\top]
\end{aligned}
$$

---
layout: prism
heading: Bayesian Probability (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- Interpreting probability as _"the frequency of occurrence of a repeatable random event"_ is known as the [frequentist]{.hl} or [classical]{.hl} perspective.

<div class="sub-item">

In the frequentist perspective, we cannot define a probability of never observed cases.

</div>

- More widely, we can quantify uncertainty using probabilities and evidence with the [Bayesian]{.hl} perspective.

- For the polynomial curve fitting example, we can use a prior probability $p(\mathbf{w})$ to represent our hypothesis of $\mathbf{w}$ and a conditioned probability with observed data $\mathcal{D}$ as $p(\mathcal{D}|\mathbf{w})$, then achieve the Bayes' theorem.

$$
p(\mathbf{w}|\mathcal{D})=\frac{p(\mathcal{D}|\mathbf{w})p(\mathbf{w})}{p(\mathcal{D})}
$$

---
layout: prism
heading: Bayesian Probability (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- In the Bayesian perspective, we use a posterior probability $p(\mathbf{w}|\mathcal{D})$ for representing the uncertainty of $\mathbf{w}$ after observing $\mathcal{D}$.

- $p(\mathcal{D}|\mathbf{w})$ in the Bayes' theorem is a function w.r.t. $\mathbf{w}$, and called a [likelihood function]{.hl}.

<div class="sub-item">

A likelihood expresses _how likely_ it is that the observed data could have occurred under each different parameter.

</div>

- In the frequentist standpoint, [maximum likelihood]{.hl} is one of the most widely used inference measures.

<div class="sub-item">

In machine learning literature, a negative log-likelihood is often used as an error function.

</div>

<div class="sub-item">

A negative log-likelihood function is monotonically decreasing, thus it is equivalent with minimizing errors to find maximizing likelihoods.

</div>

---
layout: prism
heading: Gaussian Distribution
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [Normal distribution]{.hl}, also known as [Gaussian distribution]{.hl}, is defined with a real variable $x$ as follows:

$$
\mathcal{N}(x|\mu, \sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{ -\frac{1}{2\sigma^2}(x-\mu)^2 \right\}
$$

<div class="sub-item">

Two hyperparameters, [mean]{.hl} $\mu$ and [variance]{.hl} $\sigma^2$ controls the distribution.

</div>

<div class="sub-item">

A squarred-root of the variance is called [standard deviation]{.hl}.

</div>

<div class="sub-item">

An inverse value of the variance $\beta=1/\sigma^2$ is called [precision]{.hl}.

</div>

- For a continuous variable and $D$-dimensional vector $\mathbf{x}$, Gaussian distribution is defined as follows:

$$
\mathcal{N}(\mathbf{x}|\boldsymbol{\mu}, \boldsymbol{\Sigma}^2)=\frac{1}{(2\pi)^{D/2}}\frac{1}{|\boldsymbol{\Sigma}|^{1/2}}\exp\left\{ -\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}) \right\}
$$

<div class="sub-item">

$D$-dimensional vector $\boldsymbol{\mu}$ is a mean and $D\times D$ matrix $\boldsymbol{\Sigma}$ is a covaraince, and $|\boldsymbol{\Sigma}|$ is a determinant.

</div>

---
layout: prism
heading: Curve Fitting (1/4)
---

- The goal for curve fitting is inferring a target $t$ of a newly-given input variable $x$, with $N$ observed values $\boldsymbol{\mathsf{x}}=(x_1,\ldots,x_N)^\top$ and their targets $\boldsymbol{\mathsf{t}}=(t_1,\ldots,t_N)^\top$.

- With a probability distribution, we can represent uncertainty about the target values.
  - Let us hypothesize that the target value for $x$ is Gaussian distributed with the mean $y(x,\mathbf{w})$, then we can derive the following conditioned distribution.

$$
p(t|x,\mathbf{w},\beta)=\mathcal{N}(t|y(x,\mathbf{w}), \beta^{-1})
$$

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.16.png" class="img-center" style="width: 16rem;" />

---
layout: prism
heading: Curve Fitting (2/4)
---

- We can estimate $\mathbf{w}$ and $\beta$ using the maximum likelihood with the training set $\{\boldsymbol{\mathsf{x}},\boldsymbol{\mathsf{t}}\}$.

- The likelihood function is derived as follows:

$$
p(\boldsymbol{\mathsf{t}}|\boldsymbol{\mathsf{x}},\mathbf{w},\beta)=\prod_{n=1}^{N}\mathcal{N}(t_n|y(x_n,\mathbf{w}), \beta^{-1})
$$

- We substitute Gaussian distribution and take logarithm to obtain the log-likelihood function.

$$
\ln p(\boldsymbol{\mathsf{t}}|\boldsymbol{\mathsf{x}},\mathbf{w},\beta) = -\frac{\beta}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})- t_n\}^2+\frac{N}{2}\ln\beta-\frac{N}{2}\ln(2\pi)
$$

<div class="sub-item">

We can reject the final two terms for estimating a maximum likelihood solution $\mathbf{w}_\mathrm{ML}$.

</div>

<div class="sub-item">

We can substitute $\beta/2$ to $1/2$ since $\beta$ is irrelevant.

</div>

<div class="sub-item">

We can minimize the negative log-likelihood instead of maximizing the vanilla log-likelihood.

</div>

---
layout: prism
heading: Curve Fitting (3/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- For the inference, since we are considering a probabilistic model, $t$ is represented as a [predictive distribution]{.hl}, not a point estimation.

$$
p(t|x,\mathbf{w}_\text{ML},\beta_\text{ML})=\mathcal{N}(t|y(x,\mathbf{w}_\text{ML}),\beta_\text{ML}^{-1})
$$

- Here, we can introduce a prior of $\mathbf{w}$.

<div class="sub-item">

We use the following Gaussian distribution for the simplicity.

</div>

$$
p(\mathbf{w}|\alpha)=\mathcal{N}(\mathbf{w}|\mathbf{0},\alpha^{-1}\mathbf{I})=\left(\frac{\alpha}{2\pi}\right)^{(M+1)/2}\exp\left\{-\frac{\alpha}{2}\mathbf{w}^\top\mathbf{w}\right\}
$$

<div class="subsub-item">

$\alpha$ is the precision, and known as [hyperparameter]{.hl}, and $\mathbf{I}$ is an identity matrix.

</div>

---
layout: prism
heading: Curve Fitting (4/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

- Based on the Bayes' theorem, the posteior of $\mathbf{w}$ is derived as follows:

$$
p(\mathbf{w}|\mathbf{x}, \mathbf{t},\alpha,\beta)\propto p(\mathbf{t}|\mathbf{x},\mathbf{w},\beta)p(\mathbf{w}|\alpha)
$$

<div class="sub-item">

Here, we can determine $\mathbf{w}$ by maximizing the posterior, and this technique is known as [maximum a posterior]{.hl}.

</div>

<div class="sub-item">

Note that maximizng a posterior is equivalent with minimizing the following equation.

</div>

$$
\frac{\beta}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})-t_n\}^2+\frac{\alpha}{2}\mathbf{w}^\top\mathbf{w}
$$

- Thus, maximum a posterior is same with the minimizing a regularized error function.

---
layout: prism
heading: Bayesian Curve Fitting (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

- We used a prior $p(\mathbf{w}|\alpha)$ for maximum a posterior, but we still point-estimate $\mathbf{w}$, hence we do not use a full Bayesian method.

<div class="sub-item">

In machine learning and pattern recognition, Bayesian methods are used for _marginalizing_ $\mathbf{w}$ by conducting integrations to all possible $\mathbf{w}$.

</div>

- To acquire the predictive distribution $p(t|x,\boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}})$, we can successively apply the sum rule and the product rule of probability.

$$
p(t|x, \boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}})=\int p(t|x, \mathbf{w})p(\mathbf{w}|\boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}})\,\mathrm{d}\mathbf{w}
$$

---
layout: prism
heading: Bayesian Curve Fitting (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

- After the integration, the predictive distribution can be derived as Gaussian:

$$
p(t|x, \boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}})=\mathcal{N}(t|m(x),s^2(x))
$$

<div class="sub-item">

Here the mean and variance are as follows:

</div>

$$
\begin{aligned}
m(x)&=\beta \boldsymbol{\phi}(x)^\top\mathbf{S}\sum_{n=1}^{N}\boldsymbol{\phi}(x_n)t_n\\
s^2(x)&=\beta^{-1}+\boldsymbol{\phi}(x)^\top\mathbf{S}\boldsymbol{\phi}(x)\\
\mathbf{S}^{-1}&=\alpha\mathbf{I}+\beta\sum_{n=1}^{N}\boldsymbol{\phi}(x_n)\boldsymbol{\phi}(x_n)^\top
\end{aligned}
$$

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 0rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Introduction</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probability Theory</span></p>
<p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Model Selection & Curse of Dimensionality</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Model Selection</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Curse of Dimensionality</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Decision Theory</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Information Theory</span></p>
  </div>

</div>

---
layout: prism
heading: Model Selection
---

- As illustrated by the example of overfitting, good performance on the training set does not necessarily guarantee good predictive performance.

- To tackle the issue, we divide [validation dataset]{.hl} to select optimal model and parameters.

<div class="sub-item">

In this case, we also separately define [testing dataset]{.hl} to validate the final performance of the selected model.

</div>

- For the validation, [$S$-fold cross-validation]{.hl} is widely used.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.18.png" class="img-center" style="width: 14rem;" />

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

---
layout: prism
heading: Curse of Dimensionality
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- In many applications, we have to consider high-dimensional and multiple variables, not a single $x$.

- Imagine that if we have $D$ input variables, then the third coefficients of the polynomial curve for fitting problem can be derived as follows:

$$
y(\mathbf{x}, \mathbf{w})=w_0+\sum_{i=1}^{D}w_ix_i + \sum_{i=1}^{D}\sum_{j=1}^{D}w_{ij}x_i x_j + \sum_{i=1}^{D}\sum_{j=1}^{D}\sum_{k=1}^{D}w_{ijk}x_i x_j x_k
$$

<div class="sub-item">

Note that the number of coefficients increases with $\mathcal{O}(D^3)$.

</div>

- The aforementioned problem is known as the [curse of dimensionality]{.hl}.

<div class="sub-item">

Many pattern recognition and machine learning algorithms are developed to tackle this issue.

</div>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 0rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Introduction</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probability Theory</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Model Selection & Curse of Dimensionality</span></p>
<p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Decision Theory</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Decision Theory</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Minimizing Misclassified Rate</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Reject Option</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Inference and Decision</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Information Theory</span></p>  </div>

</div>

---
layout: prism
heading: Decision Theory
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- Imagine that we have to make a _decision_, but there exists uncertainty represented with probabilities.

- In this case, we use [decision theory]{.hl} to make an optimal decision.

- We can use the Bayes' theorem to discover each conditioned probability of class for a given data.

$$
p(\mathcal{C}_k|\mathbf{x})=\frac{p(\mathbf{x}|\mathcal{C}_k)p(\mathcal{C}_k)}{p(\mathbf{x})}
$$

---
layout: prism
heading: Minimizing Misclassified Rate (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Consider that our main goal is simply reducing a number of misclassified samples, then we have to make a rule that maps each $\mathbf{x}$ to possible classes.

<div class="sub-item">

This rule divides the input space into areas $\mathcal{R}_k$, called [decision regions]{.hl}.

</div>

<div class="subsub-item">

The number of decision regions is same with the number of classes, and datapoints in $\mathcal{R}_k$ are belong to $\mathcal{C}_k$.

</div>

<div class="subsub-item">

A boundary between decision regions is called [decision boundary]{.hl} or decision surface.

</div>

- For a binary-class classification problem, a probability which makes a _mistake_ $p(m)$ can be estimated as follows:

$$
\begin{aligned}
p(m)&=p(\mathbf{x}\in\mathcal{R}_1, \mathcal{C}_2)+p(\mathbf{x}\in\mathcal{R}_2,\mathcal{C}_1)\\
&=\int_{\mathcal{R}_1}p(\mathbf{x},\mathcal{C}_2)\,\mathrm{d}\mathbf{x}+\int_{\mathcal{R}_2}p(\mathbf{x}, \mathcal{C}_1)\,\mathrm{d}\mathbf{x}
\end{aligned}
$$

---
layout: prism
heading: Minimizing Misclassified Rate (2/2)
---

- To minimize $p(m)$, $\mathbf{x}$ should be assigned to the class whose integrand has the smaller value.

<div class="sub-item">

For instance, $\mathbf{x}$ should be assigned to $\mathcal{C}_1$ if $p(\mathbf{x},\mathcal{C}_1)>p(\mathbf{x},\mathcal{C}_2)$.

</div>

- More formally, each $\mathbf{x}$ should be assigned the class which maximizes the posterior $p(\mathcal{C}_k|\mathbf{x})$.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.24.png" class="img-center" style="width: 22rem;" />

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

---
layout: prism
heading: Minimizing Expected Loss
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Minimizing the expected loss could be more complex than that minimizing misclassified samples.

- We can introduce a [cost function]{.hl}, also known as [loss function]{.hl} to tackle the issue.

- Let us define that the loss $L_{kj}$ is a penalty for class $k$-sample is misclassified to class $j$.

- In this case, our final goal is to minimize the average value of losses:

$$
\mathbb{E}[L]=\sum_k\sum_j\int_{\mathcal{R}_j}L_{kj}p(\mathbf{x},\mathcal{C}_k)\,\mathrm{d}\mathbf{x}
$$

<div class="sub-item">

Hence, we have to appropriately select $\mathcal{R}_j$ to minimize the expected loss.

</div>

---
layout: prism
heading: Reject Option
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- In certain regions of the input space, the joint probabilities $p(x,\mathcal{C}_k)$ may have similar values, making it less exact which class these regions belong to.

- Depending on the situation, it may be appropriate to refrain from making decisions in regions where classification is uncertain, in order to minimize the error rate.

<div class="sub-item">

This approach is known as [reject option]{.hl}.

</div>

- We can set a threshold value $\theta$, and if a maximum value of posterior $p(\mathcal{C}_k|\mathbf{x})$ is less than or equal to $\theta$, then the system can reject the decision making.

---
layout: prism
heading: Inference and Decision
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- A classification problem can be divided into two phases:

<div class="sub-item-enum">

1. [Inference stage]{.hl} trains a model using training dataset.
2. [Decision stage]{.hl} allocates optimal classes based on the learned posteriors.

</div>

- Moreover, we can learn a function that returns a decision for an input value, and the function is called [discriminant function]{.hl}.

- There are three approaches to solve the decision problem:

<div class="sub-item-enum">

1. [Generative model]{.hl} _models_ distributions of the input and output values.
2. [Discriminative model]{.hl} directly _models_ the posterior.
3. Without probabilities, we could discover a discriminant function that maps training samples to respective class.

</div>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 0rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Introduction</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probability Theory</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Model Selection & Curse of Dimensionality</span></p>
<p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Decision Theory</span></p>
<p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Information Theory</span></p>
  <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Information Theory</span></p>  </div>

</div>

---
layout: prism
heading: Information Theory (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- The amount of information of a discrete random variable $x$ related to how surprising it is.

<div class="sub-item">

Note that we feel more surprised when informed about events that are less likely to occur than those that are more probable.

</div>

- The measurement of the amount of information is dependent to the probability distribution $p(x)$, and a function which represents the amount of information can be defined as follows:

$$
h(x)=-\log _2 p(x)
$$

<div class="sub-item">

When two independent events occur together, the amount of information obtained is the sum of the information gained from each event separately, and the probability of both events occurring simultaneously is the product of their individual probabilities.

</div>

<div class="subsub-item">

Here, we can infer that the amount of information is the log of probability distribution.

</div>

---
layout: prism
heading: Information Theory (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- [Entropy]{.hl} of $x$, an average value for the information transportation, is defined as follows:

$$
\mathrm{H}[x]=-\sum_x p(x) \log _2 p(x)
$$

<div class="sub-item">

We can use $\ln$ instead of $\log_2$, then the unit is changed to _nat_ from _bit_.

</div>

- Suppose that we have $N$ objects and they are in some bucket, then the number of cases, called [multiplicity]{.hl}, is defined as follows:

$$
W=\frac{N!}{\prod_i n_{i}!}
$$

<div class="sub-item">

Entropy can be derived from the log of multiplicity, as follows:

</div>

$$
\mathrm{H}=\frac{1}{N} \ln W=\frac{1}{N} \ln N!-\frac{1}{N} \sum_i \ln n_{i}!
$$

---
layout: prism
heading: Information Theory (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- Let us apply $N\rightarrow\infty$ to the entropy, and use the following [Stirling's approximation]{.hl}:

$$
\ln N!\simeq N \ln N-N
$$

- Finally, we could obtain the following definition:

$$
\mathrm{H}=-\lim _{N \rightarrow \infty} \sum_i\left(\frac{n_i}{N}\right) \ln \left(\frac{n_i}{N}\right)=-\sum_i p_i \ln p_i
$$

<div class="sub-item">

In literature of physics, the order of objects in a bucket is known as [microstate]{.hl}, the ratio of the numbers of objects in each bucket is known as [macrostate]{.hl}.

</div>

<div class="sub-item">

The multiplicity $W$ is also known as [weights]{.hl} of the macrostate.

</div>

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
