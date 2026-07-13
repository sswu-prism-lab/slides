---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff' # Sets a custom hex background color
title: AML - Lecture 2
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
---

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.jpeg" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Advanced Machine Learning</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 02: Course Introduction</p>

  <p style="color:#1a1a2e; font-size: 1.5rem; margin-top: 5rem;">Wonjun Ko, Ph.D.</p>

  <div style="color:#1a1a2e; margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p style="color:#1a1a2e; font-size: 1.25rem; margin-top: 2.5rem;">Spring 2027</p>
</div>

---
layout: prism
heading: Course Schedule
---

<div class="absolute left-10 right-10" style="top: 1rem; bottom: 5rem; display: grid; grid-template-columns: 1fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">Course Introduction</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#111;">Preliminaries</span></p>
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
    <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">Introduction</span></p>
    <p style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">Polynomial Curve Fitting</span></p>
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

<div style="height: 4rem;"></div>

- Recognizing patterns from given data is one of the most important problems we have.

<div style="height: 3.5rem;"></div>

- Human beings have been pursuing answers to tackle the pattern recognition problems and successfully finds meaningful patterns for many cases.

<div style="height: 3.5rem;"></div>

- Johannes Keper discovered Kepler’s laws of planetary motion from a massive amount of astronomical data observed by Tycho Brahe, at 16th century.

---
layout: prism
heading: Polynomial Curve Fitting (1/4)
---

<v-clicks>

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

</v-clicks>

---
layout: prism
heading: Polynomial Curve Fitting (2/4)
---

<v-clicks>

- We can select $\mathbf{w}$ which minimizes $E(\mathbf{w})$ to solve the problem.
  - Note that the errror function has a quadratic form, thus we can achieve a unique $\mathbf{w}^\star$ by differentiating the function w.r.t. its coefficients.

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.3.png" class="img-center" style="height: 15rem;" />

</v-clicks>

---
layout: prism
heading: Polynomial Curve Fitting (3/4)
---

<v-clicks>

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

</v-clicks>

---
layout: prism
heading: Polynomial Curve Fitting (4/4)
---

<v-clicks>

- To tacke the overfitting issue, a [regularization]{.hl} trick is widely used.
  - To regularize, we can consider that adding a penalty term to the error function to suppress the magnitude of coefficients.

$$
\tilde{E}(\mathbf{w})=\frac{1}{2}\sum_{n=1}^N \{ y(x_n, \mathbf{w}) - t_n \}^2 + \frac{\lambda}{2}\|\mathbf{w}\|^2
$$

<div class="subsub-item">

$\|\mathbf{w}\|^2 \equiv \mathbf{w}^\top \mathbf{w} = w_0^2 + w_1^2 + \cdots + w_M^2$

</div>

<div class="sub-item">

$\lambda$ controls the relative effect of the regularization terms.

</div>

<div class="sub-item">

This regularization techniques is known as shrinkage method or [ridge regression]{.hl}.

</div>

<div class="subsub-item">

In the viewpoint of the neural network, it is called [weight decay]{.hl}.

</div>

<div class="img-row" style="max-width: 36%; gap: 5rem">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.7a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure1.7b.png" />

</div>

</v-clicks>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 0rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Introduction</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Probability Theory</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">The Basic Laws</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">Probability Density</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">Expectation and Covariance</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">Bayesian Probability</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">Gaussian Distribution</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">Curve Fitting</span></p>
      <p style="margin: 0 0 0 1.5rem; font-size: 1.1rem; color:#111;"><span style="font-size:0.75em; color:#111;">Bayesian Curve Fitting</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Model Selection & Curse of Dimensionality</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Decision Theory</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Information Theory</span></p>
  </div>

</div>

---
layout: prism
heading: Probability Theory (1/3)
---

<v-clicks>

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

</v-clicks>

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
P(Y | X) = P(X | Y)P(Y) / P(X)
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
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline;"}
