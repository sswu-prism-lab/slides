---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 12
download: true
info: |
  ## Mathematics for Artificial Intelligence Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-12-ko/
---
<style>
.dark .slidev-page,
.dark .slidev-layout,
.dark .slide-container,
.dark #slide-content,
.dark .slidev-nav-go-container {
  background: #000000 !important;
}
.tikz-fig {
  background: #ffffff;
  border-radius: 8px;
  padding: 0.4rem 0.6rem;
}
</style>

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.png" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Mathematics for Artificial Intelligence</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 12: Matrix Calculus</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">Course Overview</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">Numbers, Operations, and Systems</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">Analysis of Functions</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">Probability, Part 1</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">Probability, Part 2</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">Statistics</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">Midterm Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">Midterm Exam</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">Linear Algebra, Part 1</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">Linear Algebra, Part 2</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">Differentiation</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span class="text-gray-900 dark:text-gray-100">Matrix Calculus</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Data Flow in Neural Networks</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Matrix Calculus
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Machine learning mostly deals with vectors and matrices, so we need a notation and an approach for expressing derivatives of these multi-dimensional, multi-rank objects.
  - The gradient, a scalar function of a vector, is one such approach.

- There are many kinds of matrix derivatives, along with identities that involve matrix calculus.

- We will treat special matrices related to matrix calculus, which are tied to the optimization of machine learning and neural networks.
  - In particular, training a neural network is essentially an optimization problem.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Matrix Calculus Notation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Notation and Layouts</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Scalar &rarr; Vector Functions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Vector &rarr; Scalar Functions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Vector &rarr; Vector Functions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Scalar &rarr; Matrix Functions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Matrix &rarr; Scalar Functions</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Differentiation Identities</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Jacobian and the Hessian</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Matrix Calculus Examples</span></p>
  </div>

</div>

---
layout: prism
heading: Notation and Layouts
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Apart from the gradient, all differentiation we covered last time takes a scalar function as input and returns a scalar.
  - The gradient takes a vector as input and returns a scalar.

- There are two conventions for matrix calculus notation: the [numerator layout]{.hl} and the [denominator layout]{.hl}.
  - Different fields use different conventions, and mixed notations are common.
  - This course uses the numerator layout.

- In general, one notation is the transpose of the other.

---
layout: prism
heading: "Scalar to Vector Functions (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

- Assume a function $\mathbf{f}(x): \mathbb{R} \mapsto \mathbb{R}^m$ that takes a scalar and returns a vector.
  - Here $m$ is the dimension of the output vector.
  - Such a function is called a [vector-valued function]{.hl}.
  - One example is a [parametric curve]{.hl} in 3D space:

$$
\mathbf{f}(t) = t\cos(t)\,\hat{\mathbf{x}} + t\sin(t)\,\hat{\mathbf{y}} + t\,\hat{\mathbf{z}}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W12_helix.svg" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "Scalar to Vector Functions (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- In matrix calculus notation, we write $\mathbf{f}$ as a column vector of functions:

$$
\mathbf{f}(t) = \begin{bmatrix} t\cos(t)\\ t\sin(t)\\ t \end{bmatrix}
$$

- Generalizing, a function $\mathbf{f}$ with $n$ components is written as

$$
\mathbf{f}(x) = \begin{bmatrix} f_0(x)\\ f_1(x)\\ \vdots\\ f_{n-1}(x) \end{bmatrix}
$$

---
layout: prism
heading: "Scalar to Vector Functions (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The derivative of $\mathbf{f}(x)$ is called the [tangent vector]{.hl}, defined as

$$
\frac{\partial \mathbf{f}}{\partial x} = \begin{bmatrix} \partial f_0/\partial x\\ \partial f_1/\partial x\\ \vdots\\ \partial f_{n-1}/\partial x \end{bmatrix}
$$

- [DIY]{.hl} Find the tangent vector of the function below.

$$
\mathbf{f}(x) = \begin{bmatrix} 2x^2 - 3x + 2\\ x^3 - 3 \end{bmatrix}
$$

---
layout: prism
heading: "DIY: Tangent Vectors"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# Tangent vector via central finite differences
def tangent(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

# Parametric curve (helix): f(t) = [t cos t, t sin t, t]
helix = lambda t: np.array([t*np.cos(t), t*np.sin(t), t])
t0 = 1.0
exact = np.array([np.cos(t0) - t0*np.sin(t0), np.sin(t0) + t0*np.cos(t0), 1.0])
print("helix tangent (num)  :", np.round(tangent(helix, t0), 5))
print("helix tangent (exact):", np.round(exact, 5))

# DIY: f(x) = [2x^2 - 3x + 2, x^3 - 3]  ->  f'(x) = [4x - 3, 3x^2]
poly = lambda x: np.array([2*x**2 - 3*x + 2, x**3 - 3])
x0 = 2.0
print("poly tangent (num)   :", np.round(tangent(poly, x0), 5))
print("poly tangent (exact) :", [4*x0 - 3, 3*x0**2])
```

</PyRunner>

---
layout: prism
heading: "Vector to Scalar Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A function $f: \mathbb{R}^m \mapsto \mathbb{R}$ that takes a vector and returns a scalar is called a [scalar field]{.hl}.

- Its derivative is the gradient. In matrix calculus notation, $\partial f/\partial \mathbf{x}$ for $f(\mathbf{x})$ is written as
  - $\mathbf{x} = [x_0\quad x_1\quad \cdots\quad x_{m-1}]^\top$

$$
\frac{\partial f}{\partial \mathbf{x}} = \left[ \frac{\partial f}{\partial x_0}\quad \frac{\partial f}{\partial x_1}\quad \cdots\quad \frac{\partial f}{\partial x_{m-1}} \right]
$$

- In the numerator layout, however, $\partial f/\partial \mathbf{x}$ is a row vector, so more strictly

$$
\nabla f(\mathbf{x}) = \left[ \frac{\partial f}{\partial \mathbf{x}} \right]^\top
$$

---
layout: prism
heading: "DIY: Gradient of a Scalar Field"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# Scalar field  f(x) = x0^2 + 3 x0 x1 + 2 x1^2
f = lambda x: x[0]**2 + 3*x[0]*x[1] + 2*x[1]**2

def grad(f, x, h=1e-6):
    x = np.asarray(x, float)
    g = np.zeros_like(x)
    for i in range(len(x)):
        e = np.zeros_like(x); e[i] = h
        g[i] = (f(x + e) - f(x - e)) / (2 * h)
    return g

x = np.array([1.0, 2.0])
print("numerical gradient :", np.round(grad(f, x), 5))
print("analytic gradient  :", [2*x[0] + 3*x[1], 3*x[0] + 4*x[1]])
```

</PyRunner>

---
layout: prism
heading: "Vector to Vector Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The derivative of a scalar-argument vector function is a column vector, that of a vector-argument scalar function is a row vector, and that of a vector-argument vector function $\mathbf{f}: \mathbb{R}^m \mapsto \mathbb{R}^n$ is a matrix.

$$
\frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix}
\frac{\partial f_0}{\partial x_0} & \frac{\partial f_0}{\partial x_1} & \cdots & \frac{\partial f_0}{\partial x_{m-1}}\\
\frac{\partial f_1}{\partial x_0} & \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_{m-1}}\\
\vdots & \vdots & \ddots & \vdots\\
\frac{\partial f_{n-1}}{\partial x_0} & \frac{\partial f_{n-1}}{\partial x_1} & \cdots & \frac{\partial f_{n-1}}{\partial x_{m-1}}
\end{bmatrix}
= \begin{bmatrix}
\nabla f_0(\mathbf{x})^\top\\
\nabla f_1(\mathbf{x})^\top\\
\vdots\\
\nabla f_{n-1}(\mathbf{x})^\top
\end{bmatrix}
$$

---
layout: prism
heading: "DIY: Jacobian via Finite Differences"
---

<PyRunner>

```python
import numpy as np

# f: R^2 -> R^2,  f(x) = [4 x0 - 2 x0 x1,  2 x1 + x0 x1 - 2 x1^2]
def f(x):
    return np.array([4*x[0] - 2*x[0]*x[1],
                     2*x[1] + x[0]*x[1] - 2*x[1]**2])

def jacobian(f, x, h=1e-6):
    x = np.asarray(x, float); n = len(x)
    fx = f(x); J = np.zeros((len(fx), n))
    for j in range(n):
        e = np.zeros(n); e[j] = h
        J[:, j] = (f(x + e) - f(x - e)) / (2 * h)
    return J

x = np.array([2.0, 2.0])
print("numerical Jacobian at (2, 2):\n", np.round(jacobian(f, x), 4))
print("analytic  Jacobian at (2, 2):\n",
      np.array([[4 - 2*x[1], -2*x[0]], [x[1], 2 + x[0] - 4*x[1]]], float))
```

</PyRunner>

---
layout: prism
heading: "Scalar to Matrix Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- We can define a function $\mathbf{F}: \mathbb{R} \mapsto \mathbb{R}^{n \times m}$ that takes a scalar and returns a matrix:

$$
\mathbf{F} = \begin{bmatrix}
f_{0,0}(x) & f_{0,1}(x) & \cdots & f_{0,m-1}(x)\\
f_{1,0}(x) & f_{1,1}(x) & \cdots & f_{1,m-1}(x)\\
\vdots & \vdots & \ddots & \vdots\\
f_{n-1,0}(x) & f_{n-1,1}(x) & \cdots & f_{n-1,m-1}(x)
\end{bmatrix}
$$

- Its derivative consists of the derivative of each scalar function; this is called the [tangent matrix]{.hl}.

$$
\frac{\partial \mathbf{F}}{\partial x} = \begin{bmatrix}
\frac{\partial f_{0,0}}{\partial x} & \cdots & \frac{\partial f_{0,m-1}}{\partial x}\\
\vdots & \ddots & \vdots\\
\frac{\partial f_{n-1,0}}{\partial x} & \cdots & \frac{\partial f_{n-1,m-1}}{\partial x}
\end{bmatrix}
$$

---
layout: prism
heading: "Matrix to Scalar Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The derivative of a function $f(\mathbf{X}): \mathbb{R}^{n \times m} \mapsto \mathbb{R}$ that takes a matrix and returns a scalar is called the [gradient matrix]{.hl}, defined as

$$
\frac{\partial f}{\partial \mathbf{X}} = \begin{bmatrix}
\frac{\partial f}{\partial x_{0,0}} & \frac{\partial f}{\partial x_{1,0}} & \cdots & \frac{\partial f}{\partial x_{n-1,0}}\\
\frac{\partial f}{\partial x_{0,1}} & \frac{\partial f}{\partial x_{1,1}} & \cdots & \frac{\partial f}{\partial x_{n-1,1}}\\
\vdots & \vdots & \ddots & \vdots\\
\frac{\partial f}{\partial x_{0,m-1}} & \frac{\partial f}{\partial x_{1,m-1}} & \cdots & \frac{\partial f}{\partial x_{n-1,m-1}}
\end{bmatrix}
$$

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Matrix Calculus Notation</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Differentiation Identities</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Vector &rarr; Scalar Identities</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Scalar &rarr; Vector Identities</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Vector &rarr; Vector Identities</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Matrix &rarr; Scalar Identities</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Jacobian and the Hessian</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Matrix Calculus Examples</span></p>
  </div>

</div>

---
layout: prism
heading: "Vector to Scalar Identities (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- Let $f$ and $g$ be functions that take a vector $\mathbf{x}$ and return a scalar, and let $a$ be a scalar that does not depend on $\mathbf{x}$. Then the following basic rules hold:

$$
\begin{gather*}
\frac{\partial}{\partial \mathbf{x}}(af) = a\frac{\partial f}{\partial \mathbf{x}}\\
\frac{\partial}{\partial \mathbf{x}}(f + g) = \frac{\partial f}{\partial \mathbf{x}} + \frac{\partial g}{\partial \mathbf{x}}\\
\frac{\partial}{\partial \mathbf{x}}(fg) = f\frac{\partial g}{\partial \mathbf{x}} + g\frac{\partial f}{\partial \mathbf{x}}\\
\frac{\partial}{\partial \mathbf{x}}f \circ g = \frac{\partial f}{\partial g}\frac{\partial g}{\partial \mathbf{x}}
\end{gather*}
$$

---
layout: prism
heading: "DIY: Chain Rule for a Scalar Field"
---

- [DIY]{.hl} Given $\mathbf{x} = [x_0, x_1, x_2]^\top$, $g(\mathbf{x}) = x_0 + x_1 x_2$, and $f(g) = g^2$, find the derivative of $f$ with respect to $\mathbf{x}$.

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# g(x) = x0 + x1 x2,  f(g) = g^2  ->  df/dx = 2 g(x) * [1, x2, x1]
g = lambda x: x[0] + x[1]*x[2]
f = lambda x: g(x)**2

def grad(f, x, h=1e-6):
    x = np.asarray(x, float); out = np.zeros_like(x)
    for i in range(len(x)):
        e = np.zeros_like(x); e[i] = h
        out[i] = (f(x + e) - f(x - e)) / (2 * h)
    return out

x = np.array([1.0, 2.0, 3.0])
print("numerical df/dx :", np.round(grad(f, x), 4))
print("chain-rule df/dx:", np.round(2*g(x) * np.array([1.0, x[2], x[1]]), 4))
```

</PyRunner>

---
layout: prism
heading: "Vector to Scalar Identities (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Letting $\mathbf{a}$ be a constant vector independent of $\mathbf{x}$, the following rule holds:

$$
\frac{\partial}{\partial \mathbf{x}}(\mathbf{a} \cdot \mathbf{x}) = \frac{\partial}{\partial \mathbf{x}}(\mathbf{a}^\top \mathbf{x}) = \mathbf{a}^\top
$$

- For vector-valued functions $\mathbf{f}$ and $\mathbf{g}$, the following identities hold:

$$
\begin{gather*}
\frac{\partial}{\partial \mathbf{x}}(\mathbf{a} \cdot \mathbf{f}) = \frac{\partial}{\partial \mathbf{x}}(\mathbf{a}^\top \mathbf{f}) = \mathbf{a}^\top \frac{\partial \mathbf{f}}{\partial \mathbf{x}}\\
\frac{\partial}{\partial \mathbf{x}}(\mathbf{f} \cdot \mathbf{g}) = \frac{\partial}{\partial \mathbf{x}}(\mathbf{f}^\top \mathbf{g}) = \mathbf{f}^\top \frac{\partial \mathbf{g}}{\partial \mathbf{x}} + \mathbf{g}^\top \frac{\partial \mathbf{f}}{\partial \mathbf{x}}
\end{gather*}
$$

---
layout: prism
heading: "Scalar to Vector Identities"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The following rules hold for scalar-argument vector functions:

$$
\begin{gather*}
\frac{\partial}{\partial x}(a\mathbf{f}) = a\frac{\partial \mathbf{f}}{\partial x} \qquad
\frac{\partial}{\partial x}(\mathbf{A}\mathbf{f}) = \mathbf{A}\frac{\partial \mathbf{f}}{\partial x} \qquad
\frac{\partial}{\partial x}(\mathbf{f} + \mathbf{g}) = \frac{\partial \mathbf{f}}{\partial x} + \frac{\partial \mathbf{g}}{\partial x}\\
\frac{\partial}{\partial x}\mathbf{f} \circ \mathbf{g} = \frac{\partial \mathbf{f}}{\partial \mathbf{g}}\frac{\partial \mathbf{g}}{\partial x} \qquad
\frac{\partial}{\partial x}(\mathbf{f} \cdot \mathbf{g}) = \mathbf{f}^\top \frac{\partial \mathbf{g}}{\partial x} + \mathbf{g}^\top \frac{\partial \mathbf{f}}{\partial x}
\end{gather*}
$$

- The composition of $f(\mathbf{g})$ and $\mathbf{g}(x)$ is

$$
\frac{\partial}{\partial x}f \circ \mathbf{g} = \frac{\partial f}{\partial \mathbf{g}} \cdot \frac{\partial \mathbf{g}}{\partial x} = \frac{\partial f}{\partial \mathbf{g}}\frac{\partial \mathbf{g}}{\partial x}
$$

---
layout: prism
heading: "Vector to Vector Identities"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.6em;
}
</style>

- The derivative of a [loss function]{.hl} used in the backpropagation of machine learning is exactly the derivative of a vector-argument vector function, and the following rules hold:

$$
\begin{gather*}
\frac{\partial}{\partial \mathbf{x}}(a\mathbf{f}) = a\frac{\partial \mathbf{f}}{\partial \mathbf{x}} \qquad
\frac{\partial}{\partial \mathbf{x}}(\mathbf{A}\mathbf{f}) = \mathbf{A}\frac{\partial \mathbf{f}}{\partial \mathbf{x}}\\
\frac{\partial}{\partial \mathbf{x}}(\mathbf{f} + \mathbf{g}) = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} + \frac{\partial \mathbf{g}}{\partial \mathbf{x}} \qquad
\frac{\partial}{\partial \mathbf{x}}\mathbf{f} \circ \mathbf{g} = \frac{\partial \mathbf{f}}{\partial \mathbf{g}}\frac{\partial \mathbf{g}}{\partial \mathbf{x}}
\end{gather*}
$$

---
layout: prism
heading: "Matrix to Scalar Identities"
---

<style>
.slidev-layout ul > li {
  margin-top: 3.6em;
}
</style>

- The derivative of a function that takes a matrix and returns a scalar satisfies the following rules:

$$
\begin{gather*}
\frac{\partial}{\partial \mathbf{X}}(f + g) = \frac{\partial f}{\partial \mathbf{X}} + \frac{\partial g}{\partial \mathbf{X}} \qquad
\frac{\partial}{\partial \mathbf{X}}(fg) = f\frac{\partial g}{\partial \mathbf{X}} + g\frac{\partial f}{\partial \mathbf{X}}\\
\frac{\partial}{\partial \mathbf{X}}f \circ g = \frac{\partial f}{\partial g}\frac{\partial g}{\partial \mathbf{X}}
\end{gather*}
$$

---
layout: prism
heading: "DIY: Gradient Matrix"
---

- [DIY]{.hl} Given $\mathbf{X} = \begin{bmatrix} x_0 & x_1\\ x_2 & x_3 \end{bmatrix}$, $f(g) = \frac{1}{2}g^2$, and $g(\mathbf{X}) = x_0 x_3 + x_1 x_2$, find $\partial f/\partial \mathbf{X}$.

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# X = [[x0, x1], [x2, x3]],  g = x0 x3 + x1 x2,  f = 1/2 g^2
def g(X): return X[0, 0]*X[1, 1] + X[0, 1]*X[1, 0]
def f(X): return 0.5 * g(X)**2

def grad_mat(f, X, h=1e-6):
    G = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            E = np.zeros_like(X); E[i, j] = h
            G[i, j] = (f(X + E) - f(X - E)) / (2 * h)
    return G

X = np.array([[1., 2.], [3., 4.]])
gv = g(X)
print("numerical df/dX:\n", np.round(grad_mat(f, X), 4))
print("analytic  df/dX:\n",
      np.array([[gv*X[1, 1], gv*X[1, 0]], [gv*X[0, 1], gv*X[0, 0]]]))
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Matrix Calculus Notation</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Differentiation Identities</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">The Jacobian and the Hessian</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Jacobian Matrix</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Hessian Matrix</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Matrix Calculus Examples</span></p>
  </div>

</div>

---
layout: prism
heading: The Jacobian Matrix
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The [Jacobian matrix]{.hl} is defined as

$$
\mathbf{J}_\mathbf{x} = \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \begin{bmatrix}
\frac{\partial f_0}{\partial x_0} & \cdots & \frac{\partial f_0}{\partial x_{m-1}}\\
\vdots & \ddots & \vdots\\
\frac{\partial f_{n-1}}{\partial x_0} & \cdots & \frac{\partial f_{n-1}}{\partial x_{m-1}}
\end{bmatrix} = \begin{bmatrix}
\nabla f_0(\mathbf{x})^\top\\
\vdots\\
\nabla f_{n-1}(\mathbf{x})^\top
\end{bmatrix}
$$

- The Jacobian can be regarded as a stack of gradients.
  - It is a generalization of the first derivative.
  - It provides information about how a vector-valued function behaves near a point $\mathbf{x}$.

- The Jacobian is used to solve systems of differential equations and to find solutions of vector-valued functions.

---
layout: prism
heading: "The Jacobian - Systems of ODEs (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- A [differential equation]{.hl} is an equation in which function values and their derivatives appear together.

- Suppose two functions $x(t)$ and $y(t)$, where the change of $x(t)$ depends not only on $x$ but also on $y$, and $y(t)$ is coupled in the same way, giving the following system:

$$
\frac{dx}{dt} = 4x - 2xy \qquad \frac{dy}{dt} = 2y + xy - 2y^2
$$

- This system is expressed by a single vector-valued function:

$$
\mathbf{f}(\mathbf{x}) = \begin{bmatrix} f_0\\ f_1 \end{bmatrix} = \begin{bmatrix} 4x_0 - 2x_0 x_1\\ 2x_1 + x_0 x_1 - 2x_1^2 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} x_0\\ x_1 \end{bmatrix}
$$

---
layout: prism
heading: "The Jacobian - Systems of ODEs (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- The critical points of $\mathbf{f}$ are the points where $\mathbf{f} = \mathbf{0}$; omitting the derivation, they are

$$
\mathbf{c}_0 = \begin{bmatrix} 0\\ 0 \end{bmatrix}, \quad \mathbf{c}_1 = \begin{bmatrix} 0\\ 1 \end{bmatrix}, \quad \mathbf{c}_2 = \begin{bmatrix} 2\\ 2 \end{bmatrix}
$$

- The Jacobian of $\mathbf{f}(\mathbf{x})$ is

$$
\mathbf{J} = \begin{bmatrix}
\partial f_0/\partial x_0 & \partial f_0/\partial x_1\\
\partial f_1/\partial x_0 & \partial f_1/\partial x_1
\end{bmatrix} = \begin{bmatrix}
4 - 2x_1 & -2x_0\\
x_1 & 2 + x_0 - 4x_1
\end{bmatrix}
$$

- Evaluating the Jacobian at each critical point:

$$
\mathbf{J}|_{\mathbf{x} = \mathbf{c}_0} = \begin{bmatrix} 4 & 0\\ 0 & 2 \end{bmatrix}, \quad
\mathbf{J}|_{\mathbf{x} = \mathbf{c}_1} = \begin{bmatrix} 2 & 0\\ 1 & -2 \end{bmatrix}, \quad
\mathbf{J}|_{\mathbf{x} = \mathbf{c}_2} = \begin{bmatrix} 0 & -4\\ 2 & -4 \end{bmatrix}
$$

---
layout: prism
heading: "The Jacobian - Systems of ODEs (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- Computing the eigenvalues of each Jacobian lets us [characterize]{.hl} each critical point.

- If both eigenvalues are real with the same sign, the point is a [node]{.hl}.
  - If they are negative the node is stable; otherwise it is unstable.
    - A stable node is like a pit&mdash;anything nearby falls into it&mdash;while an unstable node is like a peak.

- If both eigenvalues are real with opposite signs, the point is a [saddle point]{.hl}: it is unstable, with one direction rolling in and another rolling out.
  - Most loss-function minima found in neural network training are likely actually saddle points.

- If the eigenvalues are complex, the point is a [spiral]{.hl}; it is stable if the real parts are negative, otherwise unstable.
  - The two eigenvalues are complex conjugates, so their real parts always share the same sign.

---
layout: prism
heading: "DIY: Eigenvalues at Critical Points"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# J(x) = [[4 - 2x1, -2x0], [x1, 2 + x0 - 4x1]] at the critical points
def J(x):
    x0, x1 = x
    return np.array([[4 - 2*x1, -2*x0], [x1, 2 + x0 - 4*x1]], float)

crits = {"c0": [0, 0], "c1": [0, 1], "c2": [2, 2]}
for name, c in crits.items():
    ev = np.linalg.eigvals(J(c))
    if np.all(np.isreal(ev)):
        kind = "saddle" if ev[0].real * ev[1].real < 0 else "node"
    else:
        kind = "spiral"
    print(f"{name} at {c}: eigenvalues = {np.round(ev, 3)}  ->  {kind}")
```

</PyRunner>

---
layout: prism
heading: "The Jacobian - Newton's Method (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The critical values above can be solved simply and algebraically, but real-world problems are not guaranteed to be this simple.

- A classic method for finding the roots of a function is [Newton's method]{.hl}, which starts from the first derivative and an initial guess and iteratively refines the root.
  - For a one-dimensional function, Newton's method improves the solution as follows:

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

  - Iterating from the initial guess until $x_n$ barely changes (i.e., until it converges), that $x_n$ is the approximate root we sought.

- [DIY]{.hl} With $f(x) = x^2$ and an initial value of $1$, find the root using Newton's method.

---
layout: prism
heading: "The Jacobian - Newton's Method (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- To extend Newton's method to vector-argument vector functions, we use the inverse of the Jacobian.

- The more general Newton iteration is defined as

$$
\mathbf{x}_{n+1} = \mathbf{x}_n - \mathbf{J}^{-1}|_{\mathbf{x} = \mathbf{x}_n}\mathbf{f}(\mathbf{x}_n)
$$

- To find all critical points via Newton's method, we must choose and vary the initial guess appropriately.

---
layout: prism
heading: "DIY: Newton's Method"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

# Newton's method:  x_{n+1} = x_n - f(x_n) / f'(x_n)
f  = lambda x: x**2
df = lambda x: 2*x

x = 1.0
for n in range(6):
    print(f"n = {n}: x = {x:.6f},  f(x) = {f(x):.3e}")
    x = x - f(x) / df(x)

print("Newton's method converges toward the root x = 0")
```

</PyRunner>

---
layout: prism
heading: "The Hessian Matrix (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- If the Jacobian generalizes the first derivative of a single-variable function, the [Hessian matrix]{.hl} $\mathbf{H}_f$ generalizes the second derivative.
  - The Hessian is limited to scalar fields.

- For $\mathbf{x} = [x_0, x_1, \cdots, x_{n-1}]^\top$, the Hessian of $f(\mathbf{x})$ is defined as

$$
\mathbf{H}_f = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_0^2} & \frac{\partial^2 f}{\partial x_0 \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_0 \partial x_{n-1}}\\
\frac{\partial^2 f}{\partial x_1 \partial x_0} & \frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_{n-1}}\\
\vdots & \vdots & \ddots & \vdots\\
\frac{\partial^2 f}{\partial x_{n-1} \partial x_0} & \frac{\partial^2 f}{\partial x_{n-1} \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_{n-1}^2}
\end{bmatrix}
$$

- [DIY]{.hl} Find the Hessian of $f(\mathbf{x}) = 2x_0^2 + x_0 x_2 + 3x_1 x_2 - x_1^2$.

---
layout: prism
heading: "The Hessian Matrix (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- The Hessian is the Jacobian of the gradient of a scalar field:

$$
\mathbf{H}_f = \mathbf{J}(\nabla f)
$$

- Using the second derivative, we can tell whether a critical point of a function is a minimum ($f'' > 0$) or a maximum ($f'' < 0$).

- From the eigenvalues of the Hessian: if all eigenvalues are positive the critical point is a minimum, if all are negative it is a maximum, and if the signs are mixed it is a saddle point.

---
layout: prism
heading: "DIY: Numerical Hessian"
---

<PyRunner>

```python
import numpy as np

# f(x) = 2 x0^2 + x0 x2 + 3 x1 x2 - x1^2
f = lambda x: 2*x[0]**2 + x[0]*x[2] + 3*x[1]*x[2] - x[1]**2

def hessian(f, x, h=1e-4):
    x = np.asarray(x, float); n = len(x)
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            ei = np.zeros(n); ei[i] = h
            ej = np.zeros(n); ej[j] = h
            H[i, j] = (f(x+ei+ej) - f(x+ei-ej) - f(x-ei+ej) + f(x-ei-ej)) / (4*h*h)
    return H

x = np.array([1.0, -1.0, 2.0])
print("numerical Hessian:\n", np.round(hessian(f, x), 3))
print("analytic Hessian :\n", np.array([[4, 0, 1], [0, -2, 3], [1, 3, 0]], float))
```

</PyRunner>

---
layout: prism
heading: "The Hessian - Optimization (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- Training a neural network is, to a first-order approximation, an optimization problem whose goal is to find the [weights]{.hl} and [biases]{.hl} that minimize the loss function.

- An algorithm that relies entirely on the gradient (the first derivative) is called a [first-order optimization method]{.hl}.
  - It exploits the fact that moving opposite to the gradient decreases the function value, using a constant $\eta$ (the [step size]{.hl}):

$$
x_n = x_{n-1} - \eta f'(x_{n-1})
$$

- Since the Hessian is a second derivative, beyond the gradient it also carries information about how the gradient changes (the [curvature]{.hl}).

- An algorithm that optimizes using the Hessian is called a [second-order optimization method]{.hl}.

---
layout: prism
heading: "The Hessian - Optimization (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- To apply an optimization method on a scalar field, we must consider the gradient rather than a plain derivative.
  - The general term of [gradient descent]{.hl}, which descends along the gradient, is

$$
\mathbf{x}_1 = \mathbf{x}_0 - \eta \nabla f(\mathbf{x}_0)
$$

- Optimization can also be performed using the second derivative; for a scalar field, we optimize as follows:

$$
\mathbf{x}_{n+1} = \mathbf{x}_n - \mathbf{H}_f^{-1}|_{\mathbf{x}_n}\nabla f(\mathbf{x}_n)
$$

- Newton's method tends to converge faster than gradient descent, which uses only the first derivative, but in practice neural networks are trained with gradient descent, not Newton's method.
  - The Hessian has restricted applicability and, being complex to compute, has very high [time complexity]{.hl}.

---
layout: prism
heading: "DIY: Gradient Descent vs. Newton's Step"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# Convex scalar field  f(x) = x0^2 + 3 x1^2
grad = lambda x: np.array([2*x[0], 6*x[1]])
H = np.array([[2., 0.], [0., 6.]])

x_gd = np.array([3.0, 3.0]); eta = 0.1
for _ in range(20):
    x_gd = x_gd - eta * grad(x_gd)

x_nt = np.array([3.0, 3.0])
x_nt = x_nt - np.linalg.solve(H, grad(x_nt))   # a single Newton step

print("gradient descent (20 steps):", np.round(x_gd, 4))
print("Newton (single step)       :", np.round(x_nt, 4))
print("true minimizer             : [0. 0.]")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Matrix Calculus Notation</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Differentiation Identities</span></p>
    <p style="margin: 0.9rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Jacobian and the Hessian</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Matrix Calculus Examples</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Element-wise Operations</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Activation Functions</span></p>
  </div>

</div>

---
layout: prism
heading: "Element-wise Operations (1/2)"
---

- Consider the addition of two vectors.

$$
\mathbf{f} = \mathbf{a} + \mathbf{b} = \begin{bmatrix} f_0\\ f_1\\ \vdots\\ f_{n-1} \end{bmatrix} = \begin{bmatrix} a_0 + b_0\\ a_1 + b_1\\ \vdots\\ a_{n-1} + b_{n-1} \end{bmatrix}
$$

- The Jacobian $\partial \mathbf{f}/\partial \mathbf{a}$ of this vector is

$$
\frac{\partial \mathbf{f}}{\partial \mathbf{a}} = \begin{bmatrix}
\frac{\partial f_0}{\partial a_0} & 0 & \cdots & 0\\
0 & \frac{\partial f_1}{\partial a_1} & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & \frac{\partial f_{n-1}}{\partial a_{n-1}}
\end{bmatrix} = \mathbf{I}
$$

- Likewise $\partial \mathbf{f}/\partial \mathbf{b} = \mathbf{I}$; for subtraction, $\partial \mathbf{f}/\partial \mathbf{a} = \mathbf{I}$ and $\partial \mathbf{f}/\partial \mathbf{b} = -\mathbf{I}$.

---
layout: prism
heading: "Element-wise Operations (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The Jacobians of the element-wise product of $\mathbf{a}$ and $\mathbf{b}$ are as follows:

$$
\begin{aligned}
\frac{\partial \mathbf{f}}{\partial \mathbf{a}} &= \begin{bmatrix}
\frac{\partial(a_0 b_0)}{\partial a_0} & 0 & \cdots & 0\\
0 & \frac{\partial(a_1 b_1)}{\partial a_1} & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & \frac{\partial(a_{n-1} b_{n-1})}{\partial a_{n-1}}
\end{bmatrix} = \begin{bmatrix}
b_0 & 0 & \cdots & 0\\
0 & b_1 & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & b_{n-1}
\end{bmatrix}\\
\frac{\partial \mathbf{f}}{\partial \mathbf{b}} &= \begin{bmatrix}
a_0 & 0 & \cdots & 0\\
0 & a_1 & \cdots & 0\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & a_{n-1}
\end{bmatrix}
\end{aligned}
$$

---
layout: prism
heading: "DIY: Element-wise Jacobians"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# Element-wise product  f = a * b  ->  df/da = diag(b),  df/db = diag(a)
a = np.array([2.0, -1.0, 3.0])
b = np.array([5.0, 4.0, -2.0])
f = lambda a, b: a * b

def jac_a(a, b, h=1e-6):
    n = len(a); J = np.zeros((n, n))
    for j in range(n):
        e = np.zeros(n); e[j] = h
        J[:, j] = (f(a + e, b) - f(a - e, b)) / (2 * h)
    return J

print("df/da (numerical):\n", np.round(jac_a(a, b), 3))
print("diag(b)          :", b)
print("is diagonal      :", np.allclose(jac_a(a, b), np.diag(b)))
```

</PyRunner>

---
layout: prism
heading: Activation Functions
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- In a [layer]{.hl} of a neural network, the previous layer's output $\mathbf{x}$ is multiplied element-wise by a weight vector $\mathbf{w}$ and summed (i.e., an inner product), and then a scalar $b$ is added.

- A [nonlinear activation function]{.hl} then introduces nonlinearity.
  - Without a nonlinear activation, no number of stacked layers is meaningful.

- One commonly used nonlinear activation, the ReLU function, is defined as

$$
\operatorname{ReLU}(z) = \max(0, z) = \begin{cases} 0 & z \leq 0\\ z & z > 0 \end{cases}
$$

- Thus a single layer of a neural network is

$$
y = \operatorname{ReLU}(\mathbf{w} \cdot \mathbf{x} + b)
$$

---
layout: prism
heading: "DIY: ReLU Layer Gradient"
---

- [DIY]{.hl} Find $\partial y/\partial \mathbf{w}$ and $\partial y/\partial b$.

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# y = ReLU(w . x + b)  ->  dy/dw = x if z > 0 else 0,  dy/db = 1 if z > 0 else 0
w = np.array([0.5, -1.0, 2.0])
x = np.array([1.0, 2.0, 1.0])
b = 0.5
relu = lambda z: max(0.0, z)
y = lambda w, b: relu(w @ x + b)

def grad_w(w, b, h=1e-6):
    g = np.zeros_like(w)
    for i in range(len(w)):
        e = np.zeros_like(w); e[i] = h
        g[i] = (y(w + e, b) - y(w - e, b)) / (2 * h)
    return g

z = w @ x + b
print("z = w . x + b =", z)
print("dy/dw (num)   :", np.round(grad_w(w, b), 4), " exact:", x if z > 0 else np.zeros_like(x))
print("dy/db (num)   :", round((y(w, b + 1e-6) - y(w, b - 1e-6)) / 2e-6, 4),
      " exact:", 1.0 if z > 0 else 0.0)
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
