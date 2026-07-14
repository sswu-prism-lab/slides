---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 5
download: true
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-5-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 05: Linear Classification Models</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span class="text-gray-900 dark:text-gray-100">Linear Classification Models</span></p>
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

- We define the log likelihood function of i.i.d. sampled datapoints from Gaussian distribution as follows:

$$
\ln p(\boldsymbol{\mathsf{x}}|\mu,\sigma^2)=\sum_{n=1}^{N}\ln p(x_n)=\sum_{n=1}^{N}\ln\left\{ \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(- \frac{(x_n-\mu)^2}{2\sigma^2} \right)\right\}
$$

<div class="sub-item">

Then, we can estimate the sample mean $\mu_\mathrm{ML}$ and the sample variance $\sigma^2_\mathrm{ML}$ by differentiating the log likelihood function w.r.t. $\mu$ and $\sigma$, respectively.

</div>

- We further estimate the expectation values of the sample mean and the sample variance, and observe that the expectation of mean is NOT biased whereas the expectation of variance is biased.

<div class="sub-item">

It is one of the most important reasons of the overfitting.

</div>

---
layout: prism
heading: Recap (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- A linear regression model with a basis function can be defined as follows:

$$
y(\mathbf{x},\mathbf{w})=\sum_{j=0}^{M-1}w_j\phi_j(\mathbf{x})=\mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})
$$

- Here, we can acquire the maximum likelihood solution for the weight vector $\mathbf{w}$ by solving the normal equation as follows:

$$
\mathbf{w}_{\mathrm{ML}}=(\boldsymbol{\Phi}^{\top} \boldsymbol{\Phi})^{-1} \boldsymbol{\Phi}^{\top} \boldsymbol{\mathsf{t}}
$$

<div class="sub-item">

$\boldsymbol{\Phi}$ denotes the design matrix.

</div>

- For larger dataset, we may introduce the stochastic gradient descent algorithm:

$$
\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}-\eta \nabla E_n
$$

---
layout: prism
heading: Recap (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- Note that machine learning algorithms in the frequentist perspective suffer from the bias–variance tradeoff.

<div class="sub-item">

The bias represents the extent to which the average prediction over all datasets differ from the desired regression function.

</div>

<div class="sub-item">

The variance measures the extent to which the solution for individual datasets vary around their average.

</div>

- For full Bayesian linear regression, we should introduce the prior distribution for the model parameter $p(\mathbf{w})$.

<div class="sub-item">

To set the conjugate prior distribution for the Gaussian likelihood function, we have to set the prior as Gaussian distribution.

</div>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Discriminant Function</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Binary Class</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Multiple Class</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Least Squares for Classification</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Fisher's Linear Discriminant</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Perceptron</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probabilistic Generative Model</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probabilistic Discriminative Model</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Laplace Approximation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bayesian Logistic Regression</span></p>
  </div>

</div>

---
layout: prism
heading: Discriminant Function
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- In a classification problem, input values are assigned to $K$ discrete classes $\mathcal{C}_k$, $k=1,\ldots,K$, one input to one class.

<div class="sub-item">

The input space is divided into multiple [decision regions]{.hl} which is separated by criterions, called [decision boundaries]{.hl} a.k.a. [decision surfaces]{.hl}.

</div>

<div class="sub-item">

If a dataset which can be exactly divided based on linear decision surfaces, then the dataset is called a [linearly separable]{.hl} dataset.

</div>

- Note that we used _real numbers_ for target variables, but now exploit [one hot encoded]{.hl} target vectors.

<div class="sub-item">

An one hot encoded vector $\mathbf{t}$ for $K$ class is constrained by two conditions: $\mathbf{t}\in\{0,1\}^K$ and $\sum_j t_j=1$ where $t_j$ is the $j$th component of $\mathbf{t}$.

</div>

- A [discriminant function]{.hl} is a function that assigns an input vector $\mathbf{x}$ to one of $K$ classes, $\mathcal{C}_k$.

<div class="sub-item">

If the decision boundary is hyperplane, then it is called a [linear discriminant function]{.hl}.

</div>

---
layout: prism
heading: Binary Class (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- A linear discriminant function is linear to input vectors and given by:

$$
y(\mathbf{x})=\mathbf{w}^\top\mathbf{x}+w_0
$$

<div class="sub-item">

$\mathbf{w}$ is a [weight vector]{.hl} and $w_0$ is a [bias]{.hl}.

</div>

<div class="sub-item">

Note that we assume a binary class classification problem, so WLOG we can assign the input to $\mathcal{C}_1$ if $y(\mathbf{x})\geqslant0$ and $\mathcal{C}_2$ otherwise.

</div>

<div class="subsub-item">

Hence, here the decision boundary is $y(\mathbf{x})=0$.

</div>

- For simplicity, we introduce a pseudovariable $x_0=1$ and define $\widetilde{\mathbf{w}}=(w_0,\mathbf{w})$ and $\widetilde{\mathbf{x}}=(x_0,\mathbf{x})$ then obtain:

$$
y(\mathbf{x})=\widetilde{\mathbf{w}}^\top\widetilde{\mathbf{x}}
$$

---
layout: prism
heading: Binary Class (2/2)
---

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.1.png" class="img-center" style="width: 25rem;" />

---
layout: prism
heading: Multiple Class (1/3)
---

- Assume that we have to tackle a multi-class classification problem, i.e., $K>2$.

<div class="sub-item">

Here, we can use $K-1$ numbers of classifiers and each classifier is used for a binary classification, classifying the input value is in $\mathcal{C}_k$ or not.

</div>

<div class="subsub-item">

This option is called [one-versus-the-rest]{.hl} classifier.

</div>

<div class="sub-item">

Another option, called [one-versus-one]{.hl} classifier, use $K(K-1)/2$ numbers of classifiers to classify all possible pairs of classes.

</div>

<div class="img-row" style="max-width: 45%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.2a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.2b.png"/>

</div>

---
layout: prism
heading: Multiple Class (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Consider that there remain some uncertain regions for one-versus-the-rest and/or one-versus-one classifiers.

- We use a unified $K$-class discriminant function which is composed of $K$ numbers of linear functions to avoid the aforementioned issues:

$$
y_k(\mathbf{x})=\mathbf{w}_k^\top\mathbf{x}+w_{k0}
$$

<div class="sub-item">

We assign $\mathbf{x}$ to $\mathcal{C}_k$ if $y_k(\mathbf{x})>y_j(\mathbf{x})$, $\forall j$, $j\neq k$.

</div>

<div class="sub-item">

The decision boundary b/w $\mathcal{C}_k$ and $\mathcal{C}_j$ is defined as $y_k(\mathbf{x})=y_j(\mathbf{x})$, then the $(D-1)$ dimensional hyperplane can be defined as:

</div>

$$
(\mathbf{w}_k -\mathbf{w}_j)^\top\mathbf{x}+(w_{k0}-w_{j0})=0
$$

---
layout: prism
heading: Multiple Class (3/3)
---

- The decision boundaries of the multi-class classification discriminant function are always linked uniquely, and have convex properties.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.3.png" class="img-center" style="width: 25rem;" />

---
layout: prism
heading: Least Squares for Classification (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- Let us rederive a classification model for $K$-class classification:

$$
\mathbf{y}(\mathbf{x})=\widetilde{\mathbf{W}}^\top\widetilde{\mathbf{x}}
$$

<div class="sub-item">

The $k$th column of $\widetilde{\mathbf{W}}$ is a $D+1$ dimensional vector $\widetilde{\mathbf{w}}_k=(w_{k0},\mathbf{w}_k^\top)^\top$.

</div>

- For given training dataset $\{\mathbf{x}_n,\mathbf{t}_n\}$, $n=1,\ldots,N$, we just define matrices $\mathbf{X}$ and $\mathbf{T}$ where their $n$th rows are $\widetilde{\mathbf{x}}_n^\top$ and $\mathbf{t}_n^\top$, respectively, then we can define the least square error function:

$$
E_D(\widetilde{\mathbf{W}})=\frac{1}{2} \operatorname{Tr}\{(\widetilde{\mathbf{X}} \widetilde{\mathbf{W}}-\mathbf{T})^{\top}(\widetilde{\mathbf{X}} \widetilde{\mathbf{W}}-\mathbf{T})\}
$$

---
layout: prism
heading: Least Squares for Classification (2/3)
---

- We differentiate the error function w.r.t. $\widetilde{\mathbf{W}}$ and set $0$, then we find the solution:

$$
\widetilde{\mathbf{W}}=(\widetilde{\mathbf{X}}^{\top} \widetilde{\mathbf{X}})^{-1} \widetilde{\mathbf{X}}^{\top} \mathbf{T}
$$

<div class="subsub-item">

Find the normal equation for the regression problem.

</div>

- We can obtain a closed-form solution when we use the least squares error function, but it is NOT robust to outliers.

<div class="sub-item">

Note that the least squares method is related to the maximum likelihood estimation under Gaussian distribution, hence if the target values are not Gaussian, then it does NOT work well.

</div>

<div class="img-row" style="max-width: 32%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.4a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.4b.png"/>

</div>

---
layout: prism
heading: Linear Squares for Classification (3/3)
---

<PyRunner>

```python
import numpy as np

def one_hot(lab, K=2):
    T = np.zeros((len(lab), K)); T[np.arange(len(lab)), lab] = 1; return T

def fit_W(X, lab):                                   # W = (X^T X)^-1 X^T T
    Xt = np.column_stack([np.ones(len(X)), X]); return np.linalg.inv(Xt.T @ Xt) @ Xt.T @ one_hot(lab)

def boundary_x1(W):                                  # boundary crossing at x2 = 0
    a = W[:, 1] - W[:, 0]; return -a[0] / a[1]

N = 60
X0 = np.random.default_rng(0).normal([-2, 0], 1.0, size=(N, 2))
X1 = np.random.default_rng(0).normal([2, 0], 1.0, size=(N, 2))
X = np.vstack([X0, X1]); lab = np.array([0] * N + [1] * N)

W = fit_W(X, lab)
print(f"Clean boundary crosses x-axis at x1 = {boundary_x1(W):+.3f}  (ideal ~ 0)")

# Far outliers that STILL belong to class 1 (correct side, just far away)
Xout = np.vstack([X1, np.random.default_rng(0).normal([15, 0], 0.5, size=(40, 2))])
Xall = np.vstack([X0, Xout]); lall = np.array([0] * N + [1] * (N + 40))
Wc = fit_W(Xall, lall)
pred_bulk = np.argmax(np.column_stack([np.ones(N), X1]) @ Wc, axis=1)

print(f"With outliers, boundary moves to  x1 = {boundary_x1(Wc):+.3f}")
print(f"Genuine class-1 points misclassified = {int((pred_bulk != 1).sum())}/{N}")
print("\nLeast squares is NOT robust: correct-but-far outliers still drag the boundary.")
```

</PyRunner>

---
layout: prism
heading: Fisher's Linear Discriminant (1/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- A linear classification model can be considered as the viewpoint of dimension reduction.

- Consider a $D$ dimensional input vector $\mathbf{x}$ is projected to one dimension (1D).

$$
y=\mathbf{w}^\top \mathbf{x}
$$

<div class="sub-item">

Normally, the projection into 1D loses a large amount of information.

</div>

<div class="sub-item">

Classes that were well-separated in a $D$ dimensional space may significantly overlap when projected onto the 1D space.

</div>

<div class="subsub-item">

However, by carefully adjusting the components of the weight vector $\mathbf{w}$ of a linear classifier, we can select a projection that maximizes class separability.

</div>

---
layout: prism
heading: Fisher's Linear Discriminant (2/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- For $N_1$ datapoints of class $\mathcal{C}_1$ and $N_2$ datapoints of class $\mathcal{C}_2$, we can estimate their mean vectors $\mathbf{m}_1$ and $\mathbf{m}_2$, respectively:

$$
\mathbf{m}_1=\frac{1}{N_1} \sum_{n \in \mathcal{C}_1} \mathbf{x}_n, \qquad \mathbf{m}_2=\frac{1}{N_2} \sum_{n \in \mathcal{C}_2} \mathbf{x}_n
$$

- We can calculate $\mathbf{w}$ which maximizes the separation between the class means as follows:

$$
\begin{aligned}
m_2-m_1 & =\mathbf{w}^{\top}\left(\mathbf{m}_2-\mathbf{m}_1\right) \\
m_k & =\mathbf{w}^{\top} \mathbf{m}_k
\end{aligned}
$$

<div class="sub-item">

Note that we may just increase the magnitude of $\mathbf{w}$ to increase $m_2-m_1$.

</div>

---
layout: prism
heading: Fisher's Linear Discriminant (3/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- Fisher proposed a method that maximizes the separation between class means when projected onto the vector $\mathbf{w}$ while simultaneously minimizing the variance within each class.

- The intra-class variance of $\mathcal{C}_k$ is computed as:

$$
s_k^2=\sum_{n \in \mathcal{C}_k}\left(y_n-m_k\right)^2
$$

- Finally, Fisher criterion is defined as the ratio of [between class]{.hl} variance to [within class]{.hl} variance:

$$
J(\mathbf{w})=\frac{\left(m_2-m_1\right)^2}{s_1^2+s_2^2}
$$

---
layout: prism
heading: Fisher's Linear Discriminant (4/6)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- The Fisher's criterion can be rederived with $\mathbf{w}$ as follows:

$$
J(\mathbf{w})=\frac{\mathbf{w}^{\top} \mathbf{S}_{\mathrm{B}} \mathbf{w}}{\mathbf{w}^{\top} \mathbf{S}_{\mathrm{W}} \mathbf{w}}
$$

<div class="sub-item">

$\mathbf{S}_\mathrm{B}$ and $\mathbf{S}_\mathrm{W}$ respectively denote the between class and within class covariance matrices.

</div>

$$
\begin{gathered}
\mathbf{S}_{\mathrm{B}}=\left(\mathbf{m}_2-\mathbf{m}_1\right)\left(\mathbf{m}_2-\mathbf{m}_1\right)^{\top}\\
\mathbf{S}_{\mathrm{W}}=\sum_{n \in \mathcal{C}_1}\left(\mathbf{x}_n-\mathbf{m}_1\right)\left(\mathbf{x}_n-\mathbf{m}_1\right)^{\top}+\sum_{n \in \mathcal{C}_2}\left(\mathbf{x}_n-\mathbf{m}_2\right)\left(\mathbf{x}_n-\mathbf{m}_2\right)^{\top}
\end{gathered}
$$

- We differentiate $J(\mathbf{w})$ w.r.t. $\mathbf{w}$ then we obtain:

$$
\mathbf{w} \propto \mathbf{S}_{\mathrm{W}}^{-1}\left(\mathbf{m}_2-\mathbf{m}_1\right)
$$

<div class="sub-item">

This method is known as [Fisher's linear discriminant]{.hl}.

</div>

---
layout: prism
heading: Fisher's Linear Discriminant (5/6)
---

<div class="img-row" style="max-width: 88%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.6a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.6b.png"/>

</div>

---
layout: prism
heading: Fisher's Linear Discriminant (6/6)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(1)
L = np.linalg.cholesky(np.array([[4.0, 0.0], [0.0, 0.25]]))  # anisotropic covariance
C1 = rng.normal(size=(200, 2)) @ L.T + np.array([0.0, 0.0])
C2 = rng.normal(size=(200, 2)) @ L.T + np.array([3.0, 3.0])

m1, m2 = C1.mean(0), C2.mean(0)
SW = (C1 - m1).T @ (C1 - m1) + (C2 - m2).T @ (C2 - m2)        # within-class scatter
w_fisher = np.linalg.inv(SW) @ (m2 - m1)                      # Fisher's solution
w_naive = m2 - m1                                            # naive mean difference

def fisher_J(w):
    w = w / np.linalg.norm(w); y1, y2 = C1 @ w, C2 @ w
    return (y2.mean() - y1.mean()) ** 2 / (y1.var() * len(y1) + y2.var() * len(y2))

print(f"Fisher criterion J, Fisher's w = S_W^-1 (m2-m1) : {fisher_J(w_fisher):.3f}")
print(f"Fisher criterion J, naive    w = m2 - m1        : {fisher_J(w_naive):.3f}")
print("\nFisher's direction maximizes between/within separation:",
      fisher_J(w_fisher) > fisher_J(w_naive))
```

</PyRunner>

---
layout: prism
heading: Perceptron (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [Perceptron]{.hl} algorithm is another example of linear discriminant models, exploits a fixed nonlinear transformation to represent an input vector $\mathbf{x}$ to a feature vector $\boldsymbol{\phi}(\mathbf{x})$:

$$
y(\mathbf{x})=f(\mathbf{w}^{\top} \boldsymbol{\phi}(\mathbf{x}))
$$

- Here, the [nonlinear activation function]{.hl} $f(\cdot)$ normally has the form:

$$
f(a)= \begin{cases}+1 & a \geqslant 0 \\ -1 & a<0\end{cases}
$$

<div class="sub-item">

Note that we use $t\in\{0,1\}$ for probabilistic models, but here $\{-1,1\}$.

</div>

---
layout: prism
heading: Perceptron (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- For perceptron, [perceptron criterion]{.hl} is a widely used error function:

$$
E_P(\mathbf{w})=-\sum_{n \in \mathcal{M}} \mathbf{w}^{\top} \boldsymbol{\phi}_n t_n
$$

<div class="sub-item">

$\boldsymbol{\phi}_n=\boldsymbol{\phi}(\mathbf{x}_n)$ and $\mathcal{M}$ means a set of misclassified patterns.

</div>

- We apply the stochastic gradient descent to the error function, and obtain:

$$
\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}-\eta \nabla E_{\mathrm{P}}(\mathbf{w})=\mathbf{w}^{(\tau)}+\eta \boldsymbol{\phi}_n t_n
$$

---
layout: prism
heading: Perceptron (3/3)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(2)
A = rng.normal([-2, -2], 1.0, size=(40, 2))
B = rng.normal([2, 2], 1.0, size=(40, 2))
X = np.vstack([A, B]); t = np.array([-1] * 40 + [1] * 40)    # perceptron targets in {-1, +1}
Phi = np.column_stack([np.ones(len(X)), X])                  # augmented features [1, x]

w = np.zeros(3); eta = 1.0
for epoch in range(1, 101):
    mis = (Phi @ w) * t <= 0
    if not mis.any():
        break
    for i in np.where(mis)[0]:
        w = w + eta * Phi[i] * t[i]                          # w <- w + eta * phi_n * t_n

pred = np.sign(Phi @ w)
print(f"Converged in {epoch} epochs")
print(f"Misclassified at the end = {int((pred != t).sum())}")
print(f"Training accuracy = {np.mean(pred == t):.3f}")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Discriminant Function</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Probabilistic Generative Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Continuous Inputs</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Maximum Likelihood Solution</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probabilistic Discriminative Model</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Laplace Approximation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bayesian Logistic Regression</span></p>
  </div>

</div>

---
layout: prism
heading: Probabilistic Generative Model (1/2)
---
<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>
- The probabilistic approach for classification simply assumes data distribution and induces a model of linear decision boundary.

- More specifically, it models the class-wise conditional distribution $p(\mathbf{x}|\mathcal{C}_k)$ and the prior distribution of each class $p(\mathcal{C}_k)$, conducts Bayesian theorem, and finally obtain the posterior distribution $p(\mathcal{C}_k|\mathbf{x})$.

- For a binary case, we can estimate the posterior of $\mathcal{C}_1$ as follows:

$$
\begin{gathered}
p(\mathcal{C}_1 | \mathbf{x})  =\frac{p(\mathbf{x} | \mathcal{C}_1) p(\mathcal{C}_1)}{p(\mathbf{x} | \mathcal{C}_1) p(\mathcal{C}_1)+p(\mathbf{x} | \mathcal{C}_2) p(\mathcal{C}_2)}=\frac{1}{1+\exp (-a)}=\sigma(a),\quad a=\ln \frac{p(\mathbf{x} | \mathcal{C}_1) p(\mathcal{C}_1)}{p(\mathbf{x} | \mathcal{C}_2) p(\mathcal{C}_2)}\\
\sigma(a)=\frac{1}{1+\exp (-a)}
\end{gathered}
$$

<div class="sub-item">

$\sigma(\cdot)$ is a [logistic sigmoid]{.hl} function.

</div>

---
layout: prism
heading: Probabilistic Generative Model (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- A logistic sigmoid function satisfies:

$$
\sigma(-a)=1-\sigma(a)
$$

- The inverse function of a logistic sigmoid is called [logit]{.hl} function and defined as follows:

$$
a=\ln\left(\frac{\sigma}{1-\sigma}\right)
$$

- For $K>2$ classes, we used a generalized version of the logistic sigmoid, called [normalized exponential function]{.hl} a.k.a. [softmax function]{.hl}.

$$
\begin{aligned}
p(\mathcal{C}_k | \mathbf{x})&=\frac{p(\mathbf{x} | \mathcal{C}_k) p(\mathcal{C}_k)}{\sum_j p(\mathbf{x} | \mathcal{C}_j) p\left(\mathcal{C}_j\right)}=\frac{\exp (a_k)}{\sum_j \exp (a_j)}\\
a_k&=\ln (p(\mathbf{x} | \mathcal{C}_k) p(\mathcal{C}_k))
\end{aligned}
$$

---
layout: prism
heading: Continuous Inputs
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Let us assume that the conditional density is Gaussian and all classes share the same covariance matrix, then we have:

$$
p\left(\mathbf{x} | \mathcal{C}_k\right)=\frac{1}{(2 \pi)^{D / 2}} \frac{1}{|\boldsymbol{\Sigma}|^{1 / 2}} \exp \left\{-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_k)^{\top} \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_k)\right\}
$$

- For a binary-class case, we finally acquire:

$$
\begin{gathered}
p(\mathcal{C}_1 | \mathbf{x})=\sigma(\mathbf{w}^{\top} \mathbf{x}+w_0)\\
\mathbf{w}=\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)\\
w_0=-\frac{1}{2} \boldsymbol{\mu}_1^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}_1+\frac{1}{2} \boldsymbol{\mu}_2^{\top} \boldsymbol{\Sigma}^{-1} \boldsymbol{\mu}_2+\ln \frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}
\end{gathered}
$$

<div class="sub-item">

Note that the input variable of the logistic sigmoid is linear to $\mathbf{x}$, since the quadratic term in the exponent is vanished due to our assumption that the covariance is shared.

</div>

---
layout: prism
heading: "NOTE: Binary Classification for Continuous Inputs"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- Let us revisit the posterior for a binary-class case:

$$
p(\mathcal{C}_k|\mathbf{x})=\frac{p(\mathbf{x}|\mathcal{C}_k)p(\mathcal{C}_k)}{p(\mathcal{C}_1)p(\mathbf{x}|\mathcal{C}_1)+p(\mathcal{C}_2)p(\mathbf{x}|\mathcal{C}_2)},\quad k=1,2
$$

- Now, take the logarithm of the numerator of the posterior, then we can define:

$$
g_k(\mathbf{x})=\ln p(\mathbf{x}|\mathcal{C}_k)+\ln p(\mathcal{C}_k)
$$

<div class="sub-item">

then,

</div>

$$
g_1(\mathbf{x})-g_2(\mathbf{x})=\ln\frac{p(\mathbf{x}|\mathcal{C}_1)p(\mathcal{C}_1)}{p(\mathbf{x}|\mathcal{C}_2)p(\mathcal{C}_2)}=\ln\frac{p(\mathbf{x}|\mathcal{C}_1)}{p(\mathbf{x}|\mathcal{C}_2)}+\ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}
$$

---
layout: prism
heading: "NOTE: Binary Classification for Continuous Inputs"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- We include the Gaussian conditional density above, then can obtain:

$$
g_1(\mathbf{x})-g_2(\mathbf{x})=\ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}+\ln\frac{ \frac{1}{(2\pi)^{D/2}|\boldsymbol{\Sigma}|^{1/2}}\exp(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_1)^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_1)) }{\frac{1}{(2\pi)^{D/2}|\boldsymbol{\Sigma}|^{1/2}} \exp(-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_2))}
$$

- We just ignore constant terms:

$$
g_1(\mathbf{x})-g_2(\mathbf{x})=\ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)} - \frac{1}{2}[(\mathbf{x}-\boldsymbol{\mu}_1)^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_1)-(\mathbf{x}-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_2)]
$$

- Now let us focus on the inside of the square brackets.

---
layout: prism
heading: "NOTE: Binary Classification for Continuous Inputs"
---

$$
\begin{aligned}
[(\mathbf{x}-\boldsymbol{\mu}_1)^\top&\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_1)-(\mathbf{x}-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu}_2)]\\
=&({\color{#4a6fa5}\mathbf{x}^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}}-2\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}+\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_1)\\
&-({\color{#4a6fa5}\mathbf{x}^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}}-2\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}+\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_2)\\
=&-2(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}+(\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_1-\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_2)
\end{aligned}
$$

- We finally achieve:

$$
\begin{aligned}
g_1(\mathbf{x})-g_2(\mathbf{x})&=-\frac{1}{2}[-2(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}+(\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_1-\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_2)] + \ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}\\
&=(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}^{-1}\mathbf{x} -\frac{1}{2}\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_1+\frac{1}{2}\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_2+\ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}\\
&=\mathbf{w}^\top\mathbf{x} +w_0
\end{aligned}
$$

<div class="sub-item">

This method is known as [linear discriminant analysis]{.hl}.

</div>

---
layout: prism
heading: "NOTE: Binary Classification for Continuous Inputs"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Note that:

$$
\begin{aligned}
&g_1(\mathbf{x})-g_2(\mathbf{x})=\ln\frac{p(\mathbf{x}|\mathcal{C}_1)p(\mathcal{C}_1)}{p(\mathbf{x}|\mathcal{C}_2)p(\mathcal{C}_2)}=\ln\frac{p(\mathcal{C}_1|\mathbf{x})}{p(\mathcal{C}_2|\mathbf{x})}=\mathbf{w}^\top\mathbf{x} +w_0\\
\Rightarrow&\ \ln\frac{p(\mathcal{C}_1|\mathbf{x})}{p(\mathcal{C}_2|\mathbf{x})}=\mathbf{w}^\top\mathbf{x}+w_0\\
\Rightarrow&\ \ln\frac{p(\mathcal{C}_1|\mathbf{x})}{1-p(\mathcal{C}_1|\mathbf{x})}=\mathbf{w}^\top\mathbf{x}+w_0\qquad \text{Compare this with the definition of logit.}\\
\therefore&\ p(\mathcal{C}_1|\mathbf{x})=\frac{1}{1+\exp(-[\mathbf{w}^\top\mathbf{x}+w_0])}=\sigma(\mathbf{w}^\top\mathbf{x}+w_0)
\end{aligned}
$$

---
layout: prism
heading: Maximum Likelihood Solution
---

- Assume that for a binary-class case, given dataset $\{\mathbf{x}_n,t_n\}$, and the prior $p(\mathcal{C}_1)=\pi$ then we obtain

$$
\begin{gathered}
p(\mathbf{x}_n, \mathcal{C}_1)=p(\mathcal{C}_1) p(\mathbf{x}_n | \mathcal{C}_1)=\pi \mathcal{N}(\mathbf{x}_n | \boldsymbol{\mu}_1, \boldsymbol{\Sigma})\\
p(\mathbf{x}_n, \mathcal{C}_2)=p(\mathcal{C}_2) p(\mathbf{x}_n | \mathcal{C}_2)=(1-\pi) \mathcal{N}(\mathbf{x}_n | \boldsymbol{\mu}_2, \boldsymbol{\Sigma})
\end{gathered}
$$

- The likelihood function is given by

$$
p\left(\boldsymbol{\mathsf{t}}, \mathbf{X} | \pi, \boldsymbol{\mu}_1, \boldsymbol{\mu}_2, \boldsymbol{\Sigma}\right)=\prod_{n=1}^N\left[\pi \mathcal{N}\left(\mathbf{x}_n | \boldsymbol{\mu}_1, \boldsymbol{\Sigma}\right)\right]^{t_n}\left[(1-\pi) \mathcal{N}\left(\mathbf{x}_n | \boldsymbol{\mu}_2, \boldsymbol{\Sigma}\right)\right]^{1-t_n}
$$

<div class="sub-item">

$\boldsymbol{\mathsf{t}}=(t_1,\ldots,t_N)^\top$.

</div>

- By differentiating the log likelihood, we obtain:

$$
\pi=\frac{1}{N} \sum_{n=1}^N t_n=\frac{N_1}{N}=\frac{N_1}{N_1+N_2}\quad\Rightarrow\quad\boldsymbol{\mu}_1=\frac{1}{N_1} \sum_{n=1}^N t_n \mathbf{x}_n
$$

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Discriminant Function</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probabilistic Generative Model</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Probabilistic Discriminative Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Fixed Basis Function</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Logistic Regression</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Iterative Reweighted Least Squares</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Laplace Approximation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bayesian Logistic Regression</span></p>
  </div>

</div>

---
layout: prism
heading: Probabilistic Discriminative Model
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Instead of discriminant function or probabilistic generative model, we can just explicitly define a generalized form of linear classification model and acquire its parameters.

<div class="sub-item">

There is an efficient algorithm, called [iterative reweighted least squares; IRLS]{.hl}, widely-used to compute the solution.

</div>

- Generative models exploit class conditional density and prior distribution to explore the parameters by Bayes' theorem.

- Unlike generative models, [discriminative models]{.hl} directly maximize the likelihood function defined by the conditional distribution $p(\mathcal{C}_k|\mathbf{x})$.

<div class="sub-item">

Mostly, discriminative models require less hyperparameters and is often well-generalized for some case when the assumption for the class conditional density fails in approximating real one.

</div>

---
layout: prism
heading: Fixed Basis Function
---

- Appropriately selected basis function $\boldsymbol{\phi}(\cdot)$ can increase the posterior modeling performance.

<div class="img-row" style="max-width: 70%">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.12a.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure4.12b.png"/>

</div>

---
layout: prism
heading: Logistic Regression (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2.5em;
}
</style>

- For a binary-class classification, we can write the posterior for class $\mathcal{C}_1$ as the logistic regression function of a linear function of a feature vector:

$$
p(\mathcal{C}_1 | \boldsymbol{\phi})=y(\boldsymbol{\phi})=\sigma(\mathbf{w}^{\top} \boldsymbol{\phi})
$$

<div class="sub-item">

Recall the earlier posterior derivation $p(\mathcal{C}_1|\mathbf{x})=\sigma(\mathbf{w}^\top\mathbf{x}+w_0)$.

</div>

<div class="sub-item">

This model is known as [logistic regression]{.hl}.

</div>

- The logistic regression model only requires $M$ numbers of parameters for $M$ dimensional feature space $\boldsymbol{\phi}$.

---
layout: prism
heading: Logistic Regression (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- We define the likelihood function as follows:

$$
p(\boldsymbol{\mathsf{t}} | \mathbf{w})=\prod_{n=1}^N y_n^{t_n}\left(1-y_n\right)^{1-t_n}
$$

<div class="sub-item">

$\boldsymbol{\mathsf{t}}=(t_1,\ldots,t_N)^\top$ and $y_n=p(\mathcal{C}_1|\boldsymbol{\phi}_n)$.

</div>

- We use the negative log likelihood as the error function, called [cross entropy]{.hl}:

$$
E(\mathbf{w})=-\ln p( \boldsymbol{\mathsf{t}} | \mathbf{w})=-\sum_{n=1}^N\left\{t_n \ln y_n+\left(1-t_n\right) \ln \left(1-y_n\right)\right\}
$$

<div class="sub-item">

$y_n=\sigma(a_n)$ and $a_n=\mathbf{w}^\top\boldsymbol{\phi}_n$.

</div>

<div class="subsub-item">

The gradient is computed as: $\nabla E(\mathbf{w})=\sum_{n=1}^N\left(y_n-t_n\right) \boldsymbol{\phi}_n$.

</div>

---
layout: prism
heading: Iterative Reweighted Least Squares (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- Since the logistic regression has nonlinearity, thus its solution may not be a closed-form.

- To solve this kinds of problems, we use an IRLS algorithm, called [Newton–Raphson]{.hl} method:

$$
\mathbf{w}^{(\mathrm {new})}=\mathbf{w}^{(\mathrm {old})}-\mathbf{H}^{-1} \nabla E(\mathbf{w})
$$

<div class="sub-item">

$\mathbf{H}$ is Hessian matrix and each element is second derivative of $E(\mathbf{w})$ w.r.t. each component of $\mathbf{w}$.

</div>

- The Hessian of the cross entropy of the logistic regression can be computed as:

$$
\begin{aligned}
\nabla E(\mathbf{w})&=\sum_{n=1}^N(y_n-t_n) \boldsymbol{\phi}_n=\boldsymbol{\Phi}^{\top}(\boldsymbol{\mathsf{y}}-\boldsymbol{\mathsf{t}})\\
\mathbf{H}&=\nabla \nabla E(\mathbf{w})=\sum_{n=1}^N y_n(1-y_n) \boldsymbol{\phi}_n \boldsymbol{\phi}_n^{\top}=\boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\Phi}
\end{aligned}
$$

<div class="sub-item">

$\mathbf{R}$ is an $N\times N$ diagonal matrix and $R_{nn}=y_n(1-y_n)$.

</div>

---
layout: prism
heading: Iterative Reweighted Least Squares (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 3em;
}
</style>

- The Newton–Raphson update for the logistic regression is:

$$
\begin{aligned}
\mathbf{w}^{(\mathrm{new})} & =\mathbf{w}^{(\mathrm{old})}-(\boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\Phi})^{-1} \boldsymbol{\Phi}^{\top}(\boldsymbol{\mathsf{y}}-\boldsymbol{\mathsf{t}})\\
& =(\boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\Phi})^{-1}(\boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\Phi} \mathbf{w}^{\mathrm {(old})}-\boldsymbol{\Phi}^{\top}(\boldsymbol{\mathsf{y}}-\boldsymbol{\mathsf{t}}))\\
& =(\boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\Phi})^{-1} \boldsymbol{\Phi}^{\top} \mathbf{R} \boldsymbol{\mathsf{z}}
\end{aligned}
$$

<div class="sub-item">

$\boldsymbol{\mathsf{z}}$ is an $N$ dimensional vector and defined as:

</div>

$$
\boldsymbol{\mathsf{z}} = \boldsymbol{\Phi} \mathbf{w}^{\mathrm{(old)}} - \mathbf{R}^{-1}(\boldsymbol{\mathsf{y}}-\boldsymbol{\mathsf{t}})
$$

---
layout: prism
heading: Iterative Reweighted Least Squares (3/3)
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(3)
G0 = rng.normal([-1, 0], 1.3, size=(100, 2))                 # overlapping (non-separable) classes
G1 = rng.normal([1.5, 0.5], 1.3, size=(100, 2))
X = np.vstack([G0, G1]); t = np.array([0.0] * 100 + [1.0] * 100)
Phi = np.column_stack([np.ones(len(X)), X])

sigmoid = lambda a: 1.0 / (1.0 + np.exp(-a))
def nll(w):
    y = np.clip(sigmoid(Phi @ w), 1e-12, 1 - 1e-12)
    return -np.sum(t * np.log(y) + (1 - t) * np.log(1 - y))

w = np.zeros(3)
print(f"{'iter':>4} | {'neg-log-likelihood':>18} | {'||gradient||':>12}")
for it in range(6):
    y = sigmoid(Phi @ w)
    R = np.diag(y * (1 - y))
    grad = Phi.T @ (y - t)
    z = Phi @ w - np.linalg.solve(R + 1e-8 * np.eye(len(R)), y - t)  # z = Phi w - R^-1 (y - t)
    w = np.linalg.solve(Phi.T @ R @ Phi, Phi.T @ R @ z)            # w = (Phi^T R Phi)^-1 Phi^T R z
    print(f"{it:>4} | {nll(w):>18.4f} | {np.linalg.norm(grad):>12.3e}")

print(f"\nNewton-Raphson drives the gradient to ~0; accuracy = "
      f"{np.mean((sigmoid(Phi @ w) >= 0.5) == (t == 1)):.3f}")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Discriminant Function</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probabilistic Generative Model</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probabilistic Discriminative Model</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Laplace Approximation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bayesian Logistic Regression</span></p>
  </div>

</div>

---
layout: prism
heading: Laplace Approximation
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [Laplace approximation]{.hl} is used for a Gaussian approximation for an arbitrary probability density of continuous variables.

- For a continuous random variable $z\sim p(z)$, Laplace approximation finds a Gaussian approximation $q(z)$ centered at a mode of $p(z)$.

<div class="sub-item-enum">

1. We first find the mode $z_0$, i.e., find the MAP.
2. We derive the 2nd order Taylor's expansion of the log probability density.
3. We take the exponent and achieve a Gaussian-formed function.
4. By completing the square, we can acquire the mean and the variance of $q(z)$.

</div>

---
layout: prism
heading: "NOTE: Laplace Approximation"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.5em;
}
</style>

- Let us conduct Laplace approximation to $p(z)\sim\exp(-z^2-z^4)$.

<div class="sub-item-enum">

1. $\dfrac{\mathrm{d}p(z)}{\mathrm{d}z}\big|_{z=z_0}=(-2z-4z^3)\exp(-z^2-z^4)\big|_{z=z_0}=0\Rightarrow z_0=0$

<div class="subsub-item">

Here, the mode is $z_0=0$.

</div>

2. $\ln p(z)\simeq \ln p(z_0)-\dfrac{1}{2}\left(-\dfrac{\mathrm{d}^2}{\mathrm{d}z^2}\ln p(z)\big|_{z=z_0}\right)(z-z_0)^2=0-\dfrac{1}{2}(-(-2-12z^2)|_{z=z_0})(z-0)^2$
3. $\ln q(z)=-z^2$
4. $\therefore q(z)=\exp(-(z-0)^2)\sim\mathcal{N}(z|0,\tfrac{1}{2})$

</div>

---
layout: prism
heading: "NOTE: Laplace Approximation"
---

<PyRunner>

```python
import numpy as np

f = lambda z: np.exp(-z**2 - z**4)                           # unnormalized density
lnp = lambda z: -z**2 - z**4
zz = np.linspace(-3, 3, 600001)

z0 = zz[np.argmax(f(zz))]                                    # 1) mode by grid search
h = 1e-4
A = -(lnp(z0 + h) - 2 * lnp(z0) + lnp(z0 - h)) / h**2        # 2) curvature A = -d^2/dz^2 ln p
q = lambda z: np.exp(-z**2) / np.sqrt(np.pi)                 # Laplace q = N(0, 1/2)
lnq_curv = -(np.log(q(z0 + h)) - 2 * np.log(q(z0)) + np.log(q(z0 - h))) / h**2

print(f"Mode z0 (grid argmax)           = {z0:.4f}   (slide: 0)")
print(f"Curvature A = -d^2/dz^2 ln p|z0 = {A:.4f}   (analytic 2 + 12*z0^2 = {2 + 12 * z0**2:.1f})")
print(f"Laplace variance = 1/A          = {1 / A:.4f}   (slide: 1/2)")
print(f"\nLaplace matches the curvature at the mode: "
      f"ln q curvature {lnq_curv:.3f} == A {A:.3f}")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Discriminant Function</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probabilistic Generative Model</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probabilistic Discriminative Model</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Laplace Approximation</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Bayesian Logistic Regression</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Posterior Estimation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Predictive Distribution</span></p>
  </div>

</div>

---
layout: prism
heading: Posterior Estimation (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- For Bayesian logistic regression, we have to estimate the posterior by normalizing the production of the prior and the likelihood function.

<div class="sub-item">

Here, each datapoint has the logistic sigmoid function, thus the likelihood function becomes complex.

</div>

- We can conduct Laplace approximation for the Bayesian logistic regression problem.

- We define the following Gaussian prior:

$$
p(\mathbf{w})=\mathcal{N}(\mathbf{w}|\mathbf{m}_0,\mathbf{S}_0)
$$

<div class="sub-item">

then the posterior becomes

</div>

$$
p(\mathbf{w}|\boldsymbol{\mathsf{t}})\propto p(\mathbf{w})p(\boldsymbol{\mathsf{t}}|\mathbf{w})
$$

---
layout: prism
heading: Posterior Estimation (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- We take the logarithm and introduce the prior and the likelihood function then acquire:

$$
\begin{aligned}
\ln p(\mathbf{w} | \boldsymbol{\mathsf{t}})= & -\frac{1}{2}\left(\mathbf{w}-\mathbf{m}_0\right)^{\top} \mathbf{S}_0^{-1}\left(\mathbf{w}-\mathbf{m}_0\right)\\
& +\sum_{n=1}^N\left\{t_n \ln y_n+\left(1-t_n\right) \ln \left(1-y_n\right)\right\}+\text {const }
\end{aligned}
$$

<div class="sub-item">

$y_n=\sigma(\mathbf{w}^\top\boldsymbol{\phi}_n)$.

</div>

- Finally, by performing Laplace approximation, we can obtain the Gaussian approximation of the posterior as follows:

$$
q(\mathbf{w})=\mathcal{N}\left(\mathbf{w} | \mathbf{w}_{\mathrm{MAP}}, \mathbf{S}_N\right)
$$

---
layout: prism
heading: Predictive Distribution
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- For a new feature vector $\boldsymbol{\phi}(\mathbf{x})$, we can approximate the posterior using $q(\mathbf{w})$:

$$
\begin{aligned}
p(\mathcal{C}_1 | \boldsymbol{\phi}, \boldsymbol{\mathsf{t}})&=\int p(\mathcal{C}_1 | \boldsymbol{\phi}, \mathbf{w}) p(\mathbf{w} | \boldsymbol{\mathsf{t}}) \mathrm{~d} \mathbf{w} \simeq \int \sigma(\mathbf{w}^{\top} \boldsymbol{\phi}) q(\mathbf{w}) \mathrm{~d} \mathbf{w}\\
&\simeq\int \sigma(a) \mathcal{N}(a | \mu_a, \sigma_a^2) \mathrm{~d} a
\end{aligned}
$$

<div class="sub-item">

$a=\mathbf{w}^\top\boldsymbol{\phi}$ and

</div>

$$
\begin{aligned}
\mu_a&=\mathbb{E}[a]=\int p(a) a \mathrm{~d} a=\int q(\mathbf{w}) \mathbf{w}^{\top} \boldsymbol{\phi} \mathrm{~d} \mathbf{w}=\mathbf{w}_{\mathrm{MAP}}^{\top} \boldsymbol{\phi}\\
\sigma_a^2&=\operatorname{var}[a]=\int p(a)\{a^2-\mathbb{E}[a]^2\} \mathrm{~d} a=\boldsymbol{\phi}^{\top} \mathbf{S}_N \boldsymbol{\phi}
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
