---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 6
download: true
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-6-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 06: Kernel Methods</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span class="text-gray-900 dark:text-gray-100">Kernel Methods</span></p>
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
heading: Recap (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- A linear discriminant function is linear to input vectors and given by:

$$
y(\mathbf{x})=\mathbf{w}^\top\mathbf{x}+w_0
$$

<div class="sub-item">

$\mathbf{w}$ is a [weight vector]{.hl} and $w_0$ is a [bias]{.hl}. For a binary-class problem, WLOG we assign $\mathbf{x}$ to $\mathcal{C}_1$ if $y(\mathbf{x})\geqslant0$ and $\mathcal{C}_2$ otherwise, so the decision boundary is $y(\mathbf{x})=0$.

</div>

<div class="sub-item">

We can obtain the least squares solution by solving the normal equation.

</div>

- Fisher defined a criterion for another type of linear discriminant function:

$$
J(\mathbf{w})=\frac{\left(m_2-m_1\right)^2}{s_1^2+s_2^2}
$$

---
layout: prism
heading: Recap (2/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- The perceptron algorithm is another example of linear discriminant models:

$$
y(\mathbf{x})=f(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}))
$$

<div class="sub-item">

$f(\cdot)$ is the nonlinear activation function.

</div>

- We normally applied the stochastic gradient descent to train a perceptron:

$$
\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}-\eta \nabla E_{P}(\mathbf{w})=\mathbf{w}^{(\tau)}+\eta \boldsymbol{\phi}_n t_n
$$

<div class="sub-item">

$E_P$ is the perceptron criterion.

</div>

---
layout: prism
heading: Recap (3/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- The probabilistic generative model estimates the posterior $p(\mathcal{C}_k|\mathbf{x})$.

- Under an assumption that the observations are sampled i.i.d. from a Gaussian distribution, the posterior becomes:

$$
\begin{gathered}
p(\mathcal{C}_1 | \mathbf{x})=\sigma(\mathbf{w}^{\top} \mathbf{x}+w_0)\\
\mathbf{w}=\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)\\
w_0=-\frac{1}{2} \boldsymbol{\mu}_1^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}_1+\frac{1}{2} \boldsymbol{\mu}_2^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}_2+\ln \frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}
\end{gathered}
$$

<div class="sub-item">

$\sigma(\cdot)$ is the logistic sigmoid function and this model is known as [linear discriminant analysis]{.hl}.

</div>

---
layout: prism
heading: Recap (4/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- The probabilistic discriminative model learns the likelihood directly. The logistic regression method is defined as:

$$
p(\mathcal{C}_1|\boldsymbol{\phi})=y(\boldsymbol{\phi})=\sigma(\mathbf{w}^\top\boldsymbol{\phi})
$$

<div class="sub-item">

This model can be trained via the iterative reweighted least squares.

</div>

- We can conduct the [Laplace approximation]{.hl} to approximate a complex probabilistic distribution at its mode.

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Dual Representation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Constructing Kernels</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Gaussian Processes</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Maximum Margin Classifier</span></p>
  </div>

</div>

---
layout: prism
heading: Dual Representation (1/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Many linear parametric models can be reformed to their [dual representation]{.hl}.

- In the dual representation, the model predicts target values using a linear combination of [kernel functions]{.hl} estimated from training datapoints.

- Based on a fixed, nonlinear feature space mapping $\boldsymbol{\phi}(\mathbf{x})$, the kernel function is given by:

$$
k(\mathbf{x},\mathbf{x}')=\boldsymbol{\phi}(\mathbf{x})^\top\boldsymbol{\phi}(\mathbf{x}')
$$

<div class="sub-item">

Note that a kernel function is symmetric, i.e., $k(\mathbf{x},\mathbf{x}')=k(\mathbf{x}',\mathbf{x})$.

</div>

- [Kernel substitution]{.hl}, a.k.a. the [kernel trick]{.hl}, utilizes that a kernel can be defined by the inner product between feature spaces, thereby allowing us to extend some well-known algorithms.

---
layout: prism
heading: Dual Representation (2/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Consider a regularized sum-squared error function for a linear regression model:

$$
J(\mathbf{w})=\frac{1}{2} \sum_{n=1}^N\{\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)-t_n\}^2+\frac{\lambda}{2} \mathbf{w}^{\top} \mathbf{w}
$$

- Differentiate w.r.t. $\mathbf{w}$ and set the result to $0$ to acquire $\mathbf{w}$:

$$
\nabla_\mathbf{w} J(\mathbf{w})=\sum_{n=1}^N\{\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)-t_n\}\boldsymbol{\phi}(\mathbf{x}_n)+\lambda\mathbf{w}=0
$$

$$
\therefore \mathbf{w}=-\frac{1}{\lambda} \sum_{n=1}^N\{\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)-t_n\} \boldsymbol{\phi}(\mathbf{x}_n)=\sum_{n=1}^N a_n \boldsymbol{\phi}(\mathbf{x}_n)=\boldsymbol{\Phi}^{\top} \mathbf{a}
$$

<div class="sub-item">

$\boldsymbol{\Phi}$ is the design matrix whose $n$th row is $\boldsymbol{\phi}(\mathbf{x}_n)^\top$, and $\mathbf{a}=(a_1,\ldots,a_N)^\top$ with $a_n=-\frac{1}{\lambda}\{\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)-t_n\}$.

</div>

---
layout: prism
heading: Dual Representation (3/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Note that we can conduct the least squares method w.r.t. $\mathbf{a}$ instead of $\mathbf{w}$.

- Let us substitute $\mathbf{w}=\boldsymbol{\Phi}^\top\mathbf{a}$, then:

$$
J(\mathbf{a})=\frac{1}{2} \mathbf{a}^{\top} \boldsymbol{\Phi} \boldsymbol{\Phi}^{\top} \boldsymbol{\Phi} \boldsymbol{\Phi}^{\top} \mathbf{a}-\mathbf{a}^{\top} \boldsymbol{\Phi} \boldsymbol{\Phi}^{\top} \boldsymbol{\mathsf{t}}+\frac{1}{2} \boldsymbol{\mathsf{t}}^{\top} \boldsymbol{\mathsf{t}}+\frac{\lambda}{2} \mathbf{a}^{\top} \boldsymbol{\Phi} \boldsymbol{\Phi}^{\top} \mathbf{a}
$$

- Introduce an $N\times N$ [Gram matrix]{.hl} $\mathbf{K}=\boldsymbol{\Phi}\boldsymbol{\Phi}^\top$:

$$
K_{nm}=\boldsymbol{\phi}(\mathbf{x}_n)^\top\boldsymbol{\phi}(\mathbf{x}_m)=k(\mathbf{x}_n,\mathbf{x}_m)
$$

- Then the error function becomes:

$$
J(\mathbf{a})=\frac{1}{2} \mathbf{a}^{\top} \mathbf{K} \mathbf{K} \mathbf{a}-\mathbf{a}^{\top} \mathbf{K} \boldsymbol{\mathsf{t}}+\frac{1}{2} \boldsymbol{\mathsf{t}}^{\top} \boldsymbol{\mathsf{t}}+\frac{\lambda}{2} \mathbf{a}^{\top} \mathbf{K} \mathbf{a}
$$

---
layout: prism
heading: Dual Representation (4/5)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Differentiate $J(\mathbf{a})$ w.r.t. $\mathbf{a}$ and set the result to $0$ to acquire $\mathbf{a}$:

$$
\begin{gathered}
\nabla_\mathbf{a} J(\mathbf{a})=\mathbf{K}\mathbf{K}\mathbf{a}-\mathbf{K}\boldsymbol{\mathsf{t}} +\lambda\mathbf{K}\mathbf{a}=0\\
\mathbf{K}(\mathbf{K}+\lambda\mathbf{I}_N)\mathbf{a}=\mathbf{K}\boldsymbol{\mathsf{t}}\\
(\mathbf{K}+\lambda\mathbf{I}_N)\mathbf{a}=\boldsymbol{\mathsf{t}}\quad\text{(assume $\mathbf{K}$ is full-rank)}\\
\therefore \mathbf{a}=\left(\mathbf{K}+\lambda \mathbf{I}_N\right)^{-1} \boldsymbol{\mathsf{t}}
\end{gathered}
$$

- A kernel-based linear regression predicts a new input $\mathbf{x}$ as follows:

$$
y(\mathbf{x})=\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x})=\mathbf{a}^{\top} \boldsymbol{\Phi} \boldsymbol{\phi}(\mathbf{x})=\mathbf{k}(\mathbf{x})^{\top}(\mathbf{K}+\lambda \mathbf{I}_N)^{-1} \boldsymbol{\mathsf{t}}
$$

<div class="sub-item">

The $n$th element of $\mathbf{k}(\mathbf{x})$ is $k_n(\mathbf{x})=k(\mathbf{x}_n,\mathbf{x})$.

</div>

---
layout: prism
heading: Dual Representation (5/5)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(0)
X = np.linspace(-3, 3, 40).reshape(-1, 1)                     # 1D inputs
t = np.sin(X).ravel() + 0.1 * rng.standard_normal(40)        # targets: sin(x) + noise
lam = 0.1

def rbf(A, B, s=1.0):                                         # Gaussian kernel
    d2 = np.sum(A**2, 1)[:, None] + np.sum(B**2, 1)[None, :] - 2 * A @ B.T
    return np.exp(-d2 / (2 * s**2))

K = rbf(X, X)                                                 # Gram matrix K_nm = k(x_n, x_m)
a = np.linalg.solve(K + lam * np.eye(len(X)), t)             # a = (K + lam I)^-1 t

Xte = np.linspace(-3, 3, 7).reshape(-1, 1)
ypred = rbf(Xte, X) @ a                                       # y(x) = k(x)^T (K + lam I)^-1 t
print("Dual kernel ridge regression (Gaussian kernel):")
for xi, yi in zip(Xte.ravel(), ypred):
    print(f"  x = {xi:+.2f}   y_pred = {yi:+.3f}   sin(x) = {np.sin(xi):+.3f}")

# Sanity check: with a LINEAR kernel, the dual prediction equals primal ridge regression
Kl = X @ X.T
al = np.linalg.solve(Kl + lam * np.eye(len(X)), t)
y_dual = (Xte @ X.T) @ al
w_primal = np.linalg.solve(X.T @ X + lam * np.eye(1), X.T @ t)
y_primal = Xte @ w_primal
print(f"\nLinear kernel: max|dual - primal| = {np.max(np.abs(y_dual - y_primal)):.2e}  (== 0)")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Dual Representation</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Constructing Kernels</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Gaussian Processes</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Maximum Margin Classifier</span></p>
  </div>

</div>

---
layout: prism
heading: Constructing Kernels (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- To construct a valid kernel function, we can first determine the feature space function $\boldsymbol{\phi}(\cdot)$ then find the kernel based on the definition.

- For instance, for a linear input space, a kernel function is defined as:

$$
k(x, x^{\prime})=\boldsymbol{\phi}(x)^{\top} \boldsymbol{\phi}(x^{\prime})=\sum_{i=1}^M \phi_i(x) \phi_i(x^{\prime})
$$

- One of the most widely-used kernels is the [Gaussian kernel]{.hl}:

$$
k(\mathbf{x}, \mathbf{x}^{\prime})=\exp (-\|\mathbf{x}-\mathbf{x}^{\prime}\|^2 / 2 \sigma^2)
$$

---
layout: prism
heading: Constructing Kernels (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- If we have two valid kernels $k_1(\mathbf{x},\mathbf{x}')$ and $k_2(\mathbf{x},\mathbf{x}')$, the following are also valid kernels:

$$
\begin{aligned}
k(\mathbf{x}, \mathbf{x}^{\prime}) & =c\, k_1(\mathbf{x}, \mathbf{x}^{\prime}) & k(\mathbf{x}, \mathbf{x}^{\prime}) & =f(\mathbf{x}) k_1(\mathbf{x}, \mathbf{x}^{\prime}) f(\mathbf{x}^{\prime}) \\
k(\mathbf{x}, \mathbf{x}^{\prime}) & =q(k_1(\mathbf{x}, \mathbf{x}^{\prime})) & k(\mathbf{x}, \mathbf{x}^{\prime}) & =\exp (k_1(\mathbf{x}, \mathbf{x}^{\prime})) \\
k(\mathbf{x}, \mathbf{x}^{\prime}) & =k_1(\mathbf{x}, \mathbf{x}^{\prime})+k_2(\mathbf{x}, \mathbf{x}^{\prime}) & k(\mathbf{x}, \mathbf{x}^{\prime}) & =k_1(\mathbf{x}, \mathbf{x}^{\prime}) k_2(\mathbf{x}, \mathbf{x}^{\prime}) \\
k(\mathbf{x}, \mathbf{x}^{\prime}) & =k_3(\boldsymbol{\phi}(\mathbf{x}), \boldsymbol{\phi}(\mathbf{x}^{\prime})) & k(\mathbf{x}, \mathbf{x}^{\prime}) & =\mathbf{x}^{\top} \mathbf{A} \mathbf{x}^{\prime} \\
k(\mathbf{x}, \mathbf{x}^{\prime}) & =k_a(\mathbf{x}_a, \mathbf{x}_a^{\prime})+k_b(\mathbf{x}_b, \mathbf{x}_b^{\prime}) & k(\mathbf{x}, \mathbf{x}^{\prime}) & =k_a(\mathbf{x}_a, \mathbf{x}_a^{\prime}) k_b(\mathbf{x}_b, \mathbf{x}_b^{\prime})
\end{aligned}
$$

<div class="sub-item">

Here $c>0$, $f(\cdot)$ is any function, $q(\cdot)$ is a polynomial with non-negative coefficients, and $\mathbf{A}$ is a symmetric positive semidefinite matrix.

</div>

---
layout: prism
heading: Constructing Kernels (3/3)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(1)
X = rng.standard_normal((12, 3))                             # 12 samples in 3D

def gram_linear(X):
    return X @ X.T                                           # k1(x, x') = x^T x'
def gram_rbf(X, s=1.5):
    d2 = np.sum(X**2, 1)[:, None] + np.sum(X**2, 1)[None, :] - 2 * X @ X.T
    return np.exp(-d2 / (2 * s**2))                          # k2(x, x') = exp(-||x-x'||^2/2s^2)

def min_eig(K):
    return np.linalg.eigvalsh((K + K.T) / 2).min()          # smallest eigenvalue

K1, K2 = gram_linear(X), gram_rbf(X)
print("A valid kernel must yield a positive semi-definite Gram matrix (min eig >= 0):")
print(f"  linear   k1                 : min eig = {min_eig(K1):+.4e}")
print(f"  Gaussian k2                 : min eig = {min_eig(K2):+.4e}")
print(f"  sum      k1 + k2            : min eig = {min_eig(K1 + K2):+.4e}")
print(f"  product  k1 * k2 (elem-wise): min eig = {min_eig(K1 * K2):+.4e}")
print(f"  scaled   3 * k2            : min eig = {min_eig(3 * K2):+.4e}")
print("\nAll construction rules preserve PSD => each produces a valid kernel.")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Dual Representation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Constructing Kernels</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Gaussian Processes</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Maximum Margin Classifier</span></p>
  </div>

</div>

---
layout: prism
heading: Gaussian Processes (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- A [Gaussian process]{.hl} is a stochastic process defined by the probability distribution of a function $y(\mathbf{x})$.

<div class="sub-item">

In this distribution, the values $y(\mathbf{x})$ estimated from $\mathbf{x}_1,\ldots,\mathbf{x}_N$ are jointly Gaussian, and the joint distribution of $y_1,\ldots,y_N$ is defined by the mean and the covariance.

</div>

<div class="sub-item">

For instance, assume the model prior $p(\mathbf{w})=\mathcal{N}(\mathbf{w}|\mathbf{0},\alpha^{-1}\mathbf{I})$ for a linear regression model, then:

</div>

$$
\mathbb{E}[\boldsymbol{\mathsf{y}}]=\boldsymbol{\Phi} \mathbb{E}[\mathbf{w}]=\mathbf{0}, \qquad
\operatorname{cov}[\boldsymbol{\mathsf{y}}]=\boldsymbol{\Phi} \mathbb{E}[\mathbf{w} \mathbf{w}^{\top}] \boldsymbol{\Phi}^{\top}=\frac{1}{\alpha} \boldsymbol{\Phi} \boldsymbol{\Phi}^{\top}=\mathbf{K}
$$

<div class="sub-item">

$\boldsymbol{\mathsf{y}}$ is the vector composed of $y_n=y(\mathbf{x}_n)$ and $\mathbf{K}$ is the Gram matrix $K_{nm}=k(\mathbf{x}_n, \mathbf{x}_m)=\frac{1}{\alpha} \boldsymbol{\phi}(\mathbf{x}_n)^{\top} \boldsymbol{\phi}(\mathbf{x}_m)$.

</div>

- Find Gaussian Processes!

---
layout: prism
heading: Gaussian Processes (2/2)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(4)
X = np.linspace(-5, 5, 8).reshape(-1, 1)                     # 8 input locations

def rbf(A, B, s=1.0):
    d2 = np.sum(A**2, 1)[:, None] + np.sum(B**2, 1)[None, :] - 2 * A @ B.T
    return np.exp(-d2 / (2 * s**2))

K = rbf(X, X, s=2.0) + 1e-8 * np.eye(len(X))                 # cov[y] = K (GP prior, mean 0)
L = np.linalg.cholesky(K)

print("Gaussian process prior:  y ~ N(0, K),  K_nm = k(x_n, x_m)")
print("Three sampled functions y(x) evaluated at the 8 input points:")
for s in range(3):
    y = L @ rng.standard_normal(len(X))                     # draw y = L z, z ~ N(0, I)
    print("  sample", s + 1, ":", np.array2string(y, precision=2, floatmode="fixed"))

c_near = K[0, 1] / np.sqrt(K[0, 0] * K[1, 1])               # adjacent inputs
c_far = K[0, -1] / np.sqrt(K[0, 0] * K[-1, -1])            # far-apart inputs
print(f"\ncorr(y at adjacent inputs) = {c_near:.3f}  (strongly correlated)")
print(f"corr(y at far inputs)      = {c_far:.3f}  (nearly independent)")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Dual Representation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Constructing Kernels</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Gaussian Processes</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Maximum Margin Classifier</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Slack Variables</span></p>
  </div>

</div>

---
layout: prism
heading: Maximum Margin Classifier (1/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- Kernel-based learning algorithms need to estimate the kernel function $k(\cdot,\cdot)$ for all data pairs.

<div class="sub-item">

This may require a large amount of computation, or even be intractable.

</div>

- Kernel-based methods whose solution is [sparse]{.hl} depend only on a subset of the training samples.

- One of the most widely-used sparse kernel machines, the [support vector machine; SVM]{.hl}, is utilized for classification, regression, and various other tasks.

<div class="sub-item">

SVM is based on solving a convex optimization, so the local optimum becomes the global optimum. It is deterministic and hence does not output posterior probabilities.

</div>

---
layout: prism
heading: Maximum Margin Classifier (2/6)
---

- Consider the following binary-class classification problem; there would exist many solutions that exactly discriminate the datapoints:

$$
y(\mathbf{x})=\mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})+b
$$

<div class="sub-item">

If there are many solutions, it is best to find a unique one that shows minimal generalization error.

</div>

- SVM introduces the concept of the [margin]{.hl}, and computes a decision boundary that maximizes the minimum distance between the boundary and the samples.

<div class="img-row" style="max-width: 45%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure7.1a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure7.1b.png"/>

</div>

---
layout: prism
heading: Maximum Margin Classifier (3/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- Assuming all datapoints are correctly classified, the distance between a point $\mathbf{x}_n$ and the decision boundary is:

$$
\frac{t_n y\left(\mathbf{x}_n\right)}{\|\mathbf{w}\|}=\frac{t_n(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)+b)}{\|\mathbf{w}\|}
$$

- The margin is the perpendicular distance from the boundary to the nearest point $\mathbf{x}_n$, so SVM is obtained by maximizing the margin:

$$
\underset{\mathbf{w}, b}{\arg \max }\left[\frac{1}{\|\mathbf{w}\|} \min _n\{t_n(\mathbf{w}^{\top} \boldsymbol{\phi}\left(\mathbf{x}_n\right)+b)\}\right]
$$

<div class="sub-item">

This optimization problem is hard to solve directly.

</div>

---
layout: prism
heading: Maximum Margin Classifier (4/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- Multiplying $\mathbf{w}$ and $b$ by any nonzero constant does not change the distances, so we can arbitrarily set, for the points closest to the boundary:

$$
t_n(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)+b)=1
$$

<div class="sub-item">

Then all datapoints satisfy the [canonical representation]{.hl} constraints $t_n(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)+b) \geqslant 1$, $n=1, \ldots, N$.

</div>

- Since at least one point is closest to the boundary, maximizing the margin simplifies to maximizing $\|\mathbf{w}\|^{-1}$, i.e., minimizing $\|\mathbf{w}\|^2$:

$$
\underset{\mathbf{w}, b}{\arg \min } \frac{1}{2}\|\mathbf{w}\|^2
$$

---
layout: prism
heading: Maximum Margin Classifier (5/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- Finally, we build the following Lagrange function:

$$
L(\mathbf{w}, b, \mathbf{a})=\frac{1}{2}\|\mathbf{w}\|^2-\sum_{n=1}^N a_n\{t_n(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}_n)+b)-1\}
$$

- Differentiating the function, we acquire:

$$
\mathbf{w} =\sum_{n=1}^N a_n t_n \boldsymbol{\phi}\left(\mathbf{x}_n\right), \qquad 0 =\sum_{n=1}^N a_n t_n
$$

- Note that we can compute the dual representation of the Lagrange function.

---
layout: prism
heading: Maximum Margin Classifier (6/6)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(2)
X = np.vstack([rng.normal([-2, -2], 0.6, (25, 2)),          # linearly separable data
               rng.normal([ 2,  2], 0.6, (25, 2))])
t = np.array([-1.0] * 25 + [1.0] * 25)
N = len(X)

Q = (X @ X.T) * np.outer(t, t)                              # dual: maximize 1^T a - 1/2 a^T Q a
a = np.zeros(N); eta = 1e-3
for _ in range(20000):
    a = a + eta * (1 - Q @ a)                              # gradient ascent step
    a -= t * (t @ a) / (t @ t)                             # project onto sum_n a_n t_n = 0
    a = np.maximum(a, 0.0)                                 # enforce a_n >= 0

w = (a * t) @ X                                            # w = sum_n a_n t_n x_n
sv = a > 1e-4                                              # support vectors have a_n > 0
b = np.mean(t[sv] - X[sv] @ w)
pred = np.sign(X @ w + b)
print(f"Support vectors            : {int(sv.sum())} of {N}")
print(f"Margin  1/||w||            : {1 / np.linalg.norm(w):.3f}")
print(f"Training accuracy          : {np.mean(pred == t):.3f}")
print(f"min_n t_n (w^T x_n + b)    : {np.min(t * (X @ w + b)):.3f}   (~1 at the margin)")
```

</PyRunner>

---
layout: prism
heading: Slack Variables (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

- Practically, overlap may exist between class-conditional distributions.

- When class distributions overlap, training a model to perfectly separate the training data may lead to poor generalization; we therefore allow some training points to be misclassified.

- We allow datapoints on the incorrect side of the margin boundary, but impose penalties that grow with the distance from the boundary, using a [slack variable]{.hl} $\xi_n\geqslant 0$.

<div class="sub-item">

One slack variable is used per datapoint: if a datapoint is inside the correct margin boundary, $\xi_n=0$, otherwise $\xi_n=|t_n-y(\mathbf{x}_n)|$. The constraint then becomes $t_n\, y(\mathbf{x}_n) \geqslant 1-\xi_n$, $n=1, \ldots, N$.

</div>

---
layout: prism
heading: Slack Variables (2/4)
---

- If $\xi_n=0$, the datapoint is correctly classified; if $0<\xi_n\leqslant 1$, it is correctly classified but inside the margin; and if $\xi_n>1$, it is misclassified.

<div class="sub-item">

Allowing $\xi_n>1$ is called a [soft margin]{.hl} constraint, otherwise a [hard margin]{.hl} constraint.

</div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure7.3.png" class="img-center" style="width: 19rem;" />

---
layout: prism
heading: Slack Variables (3/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The final goal is to minimize the following:

$$
C \sum_{n=1}^N \xi_n+\frac{1}{2}\|\mathbf{w}\|^2
$$

<div class="sub-item">

The parameter $C>0$ controls the tradeoff between the slack variables and the margin.

</div>

- We obtain the Lagrange function:

$$
\begin{aligned}
L(\mathbf{w}, b, \boldsymbol{\xi}, \mathbf{a}, \boldsymbol{\mu})=&\frac{1}{2}\|\mathbf{w}\|^2+C \sum_{n=1}^N \xi_n\\
&-\sum_{n=1}^N a_n\left\{t_n y\left(\mathbf{x}_n\right)-1+\xi_n\right\}-\sum_{n=1}^N \mu_n \xi_n
\end{aligned}
$$

---
layout: prism
heading: Slack Variables (4/4)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(3)
X = np.vstack([rng.normal([-1.0, 0.0], 1.1, (40, 2)),       # overlapping (non-separable)
               rng.normal([ 1.0, 0.0], 1.1, (40, 2))])
t = np.array([-1.0] * 40 + [1.0] * 40)
N = len(X)
Q = (X @ X.T) * np.outer(t, t)                              # linear kernel

def solve_soft(C, iters=20000, eta=1e-3):
    a = np.zeros(N)
    for _ in range(iters):
        a = a + eta * (1 - Q @ a)
        a -= t * (t @ a) / (t @ t)                          # sum_n a_n t_n = 0
        a = np.clip(a, 0.0, C)                              # box constraint 0 <= a_n <= C
    w = (a * t) @ X
    on = (a > 1e-4) & (a < C - 1e-4)                        # points exactly on the margin
    b = np.mean(t[on] - X[on] @ w) if on.any() else 0.0
    return 1 / np.linalg.norm(w), np.mean(np.sign(X @ w + b) == t), int((a > 1e-4).sum())

print("Soft-margin SVM: C trades off margin width against slack (misclassification).")
print(f"{'C':>7} | {'margin 1/||w||':>14} | {'train acc':>9} | {'#support vec':>12}")
for C in [0.01, 0.1, 1.0, 10.0]:
    m, acc, nsv = solve_soft(C)
    print(f"{C:>7.2f} | {m:>14.3f} | {acc:>9.3f} | {nsv:>12d}")
print("\nSmall C -> wider margin, more support vectors; large C -> narrower margin, harder fit.")
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
