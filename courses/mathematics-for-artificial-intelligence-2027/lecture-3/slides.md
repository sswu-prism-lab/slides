---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 3
download: true
info: |
  ## Mathematics for Artificial Intelligence Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 03: Analysis of Functions</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span class="text-gray-900 dark:text-gray-100">Analysis of Functions</span></p>
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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Matrix Calculus</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Data Flow in Neural Networks</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Analysis of Functions
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- In mathematics, we need to define rules or relationships that correspond between individual objects.

- A function is a relationship in mathematics that maps elements of one set to elements of another set.

- In mathematics, as well as in science and engineering, functions are used to express relationships between variables and to represent such phenomena through concise models.

- From the perspective of data analysis as well, functions allow us to identify patterns in data.

- In today's lecture, we will cover the following:
  - The definition of functions and their properties from a set-theoretic viewpoint
  - Various types of functions and their graphs
  - Translations of functions on the coordinate plane

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Functions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Definition of a Function</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Properties of Functions</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Functions and Graphs</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Transformations of Functions</span></p>
  </div>

</div>

---
layout: prism
heading: Functions (1/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- A [function]{.hl} $f$ mapping a set $X$ to a set $Y$ is a rule that maps each $x \in X$ to a unique $y = f(x) \in Y$, written $f : X \mapsto Y$.
  - In $y = f(x)$, $y$ is the [image]{.hl} of $x$, and $x$ is the [preimage]{.hl} of $y$.
  - The set $X$ is the [domain]{.hl} of $f$, and $Y$ is the [codomain]{.hl} or [range]{.hl} of $f$.

- From a more rigorous viewpoint, a function is a relation, i.e., a set of [ordered pair]{.hl}s.
  - The left element of each ordered pair is the preimage, and the right element is the image.
  - That is, from a set-theoretic viewpoint, a function is seen not as a formula but as a correspondence of values, a [mapping]{.hl}.

- [DIY]{.hl} Express the function $f : \mathbb{R} \mapsto \mathbb{R},\ f(x) = x^2$ according to the set-theoretic definition.

---
layout: prism
heading: Functions (2/4)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>


- The rigorous definition of a function with domain $X$ and codomain $Y$ is:

$$
f = \{ (x, y) \mid x \in X \wedge y \in Y \} \text{ s.t. } \forall (x, y) \in f\ \forall (x, y') \in f;\ y = y'
$$

<div class="sub-item">

That is, each $x \in X$ has exactly one $y \in Y$.

</div>


- For a function $f : X \mapsto Y$, if $f(x_i) \neq f(x_j)$ holds for all $x_i, x_j \in X$ with $i \neq j$, then $f$ is called [one-to-one]{.hl} or [injective]{.hl}.
  - This means that two distinct points of the domain cannot have the same image.

- If $f(X) = Y$, then $f$ is called a function [onto]{.hl} $Y$ from $X$, or [surjective]{.hl}.

- If $f$ is both injective and surjective, it is called a [one-to-one correspondence]{.hl} or [bijective]{.hl}.
  - There exists an [inverse function]{.hl} $f^{-1} : Y \mapsto X$ that maps each $y \in Y$ uniquely to its [inverse image]{.hl} $x = f^{-1}(y)$.

---
layout: prism
heading: Functions (3/4)
---

- For a set $X$, the [identity function]{.hl} $i_X : X \mapsto X$ is defined as

$$
i_X(x) = x, \quad x \in X.
$$

- For functions $f : X \mapsto Y$ and $g : Y \mapsto Z$, the [composite function]{.hl} $g \circ f : X \mapsto Z$ is defined as

$$
g \circ f(x) = g(f(x)), \quad x \in X.
$$

- [DIY]{.hl} Given the real-valued functions $f(x) = \sqrt{x - 1}$ and $g(x) = 3x$, find the domain of $f \circ g(x)$.

<PyRunner>

```python
import numpy as np

# f(x)=sqrt(x-1), g(x)=3x  =>  (f o g)(x) = f(3x) = sqrt(3x - 1)
# domain requires 3x - 1 >= 0  =>  x >= 1/3
for x in [-0.5, 0.0, 1/3, 0.5, 1.0, 2.0]:
    inside = 3*x - 1
    if inside >= 0:
        print(f"x={x:6.3f} -> (f o g)(x) = sqrt({inside:6.3f}) = {np.sqrt(inside):.4f}")
    else:
        print(f"x={x:6.3f} -> undefined  (3x-1={inside:6.3f} < 0)")

print("domain of f o g : x >= 1/3 =", round(1/3, 4))
```

</PyRunner>

---
layout: prism
heading: Functions (4/4)
---

- When a function is described using different formulas on different parts of its domain, this is called a [piecewise definition]{.hl}.

- The [absolute value]{.hl} function, using a piecewise definition, is given by

$$
|x| = \begin{cases} x & \text{if } x \geq 0 \\ -x & \text{otherwise} \end{cases}
$$

- [DIY]{.hl} Define the [sign function]{.hl} $\operatorname{sgn} x$, which outputs $+1$ if the input $x$ is positive, $0$ if it is $0$, and $-1$ if it is negative, using a piecewise definition.

<PyRunner>

```python
import numpy as np
def sgn(x):
    if x > 0:  return 1
    if x < 0:  return -1
    return 0
for x in [-3.2, -1, 0, 0.5, 7]:
    print(f"sgn({x:>4}) = {sgn(x):>2}")
print("matches numpy sign:", all(sgn(x) == np.sign(x) for x in [-3.2, -1, 0, 0.5, 7]))
```

</PyRunner>

---
layout: prism
heading: Properties of Functions (1/2)
---

- For a set $X$, a [relation]{.hl} $R$ on $X$ is a subset of $X \times X$; if $(x, y) \in R$, then $x$ is said to be [related]{.hl} to $y$ by $R$, written $xRy$.

<div class="theorem-box">
<div class="theorem-box-title">Equivalence relation</div>
<div class="theorem-box-body">

An [equivalence relation]{.hl} on a set $X$ is a relation satisfying the following three properties.

<div class="sub-item-enum">

1. [Reflexive]{.hl} property: $xRx,\ \forall x \in X$
2. [Symmetric]{.hl} property: $xRy \Rightarrow yRx$
3. [Transitive]{.hl} property: $xRy,\ yRz \Rightarrow xRz$

</div>
</div>
</div>

- When a relation $\approx$ is an equivalence relation on $X$, the [equivalence class]{.hl} $[x]$ is the set of all elements of $X$ related to $x \in X$ by $\approx$, defined as $[x] = \{ y \in X : y \approx x \}.$

---
layout: prism
heading: Properties of Functions (2/2)
---

- The property that a function is defined without any break at a point is called [continuity]{.hl}; if $\lim_{x \to a} f(x) = f(a)$, then $f(x)$ is said to be continuous at $x = a$.

- The property that the _derivative_ of a function exists is called [differentiability]{.hl}.
  - If a function is differentiable, then it is continuous.

- The property that a function is always increasing or always decreasing throughout its domain is called [monotonicity]{.hl}.
  - Monotonically increasing function: $x_1 < x_2 \Rightarrow f(x_1) \leq f(x_2)$
  - Monotonically decreasing function: $x_1 < x_2 \Rightarrow f(x_1) \geq f(x_2)$

- The property that a function's values repeat at regular intervals is called [periodicity]{.hl}.

- The property that a function is symmetric about a certain axis or point is called [symmetry]{.hl}.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Functions</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Functions and Graphs</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Real-Valued Functions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Complex-Valued Functions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Multivariate Functions</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Transformations of Functions</span></p>
  </div>

</div>

---
layout: prism
heading: Real-Valued Functions (1/5)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

- A function whose domain is a subset of the real numbers and whose codomain is the real numbers is called a [real-valued function]{.hl}.

- If $f$ is a function with domain $D$, then the graph of $f$ is $\{ (x, f(x)) \mid x \in D \}$.
  - For a real-valued function, since the domain and codomain are real, its graph can be represented as a subset of $\mathbb{R} \times \mathbb{R}$, i.e., of the plane.

- For example, the graph of $f(x) = x + 2$ is the set of points $(x, y)$ with $y = x + 2$; the point where $x = 0$ is the $y$-intercept and the point where $y = 0$ is the $x$-intercept.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_line.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Real-Valued Functions (2/5)
---

<div class="grid grid-cols-2 gap-1" style="margin-top: 0rem; grid-template-columns: 1.5fr 1fr">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.3em;
}
</style>

- The [linear function]{.hl} $f(x) = ax + b$, a kind of real-valued function, satisfies the following properties:
  - The slope is $a$.
  - It is a one-to-one correspondence and a monotonic function.
  - The $x$-intercept is $-\frac{b}{a}$ and the $y$-intercept is $b$.
  - The derivative $f'(x) = a$ is a constant function.

- A function built from _polynomials_ is called a [polynomial function]{.hl}.

- The [Legendre function]{.hl}, which plays an important role in mathematics and physics, is defined as

$$
P_n(x) = \frac{1}{2^n n!} \frac{\mathrm{d}^n}{\mathrm{d}x^n}(x^2 - 1)^n.
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_legendre.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Real-Valued Functions"
---

<PyRunner>

```python
import numpy as np

x = np.linspace(-1, 1, 5)
P = [np.ones_like(x), x.copy()]            # P0 = 1, P1 = x
for n in range(1, 3):                      # Bonnet's recurrence
    P.append(((2*n + 1) * x * P[n] - n * P[n-1]) / (n + 1))

closed = [np.ones_like(x), x, 0.5*(3*x**2 - 1), 0.5*(5*x**3 - 3*x)]
for n in range(4):
    print(f"P{n}(x) =", np.round(P[n], 3), " matches closed form:", np.allclose(P[n], closed[n]))
```

</PyRunner>

---
layout: prism
heading: Real-Valued Functions (3/5)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem; grid-template-columns: 1.5fr 1fr">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A function whose codomain is not continuous is called a [discrete function]{.hl}; an example is the [step function]{.hl}.

- [DIY]{.hl} Express the step function $u(x)$ shown in the graph as a formula.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_step.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

<PyRunner>

```python
import numpy as np

# Heaviside step: u(x) = 0 for x < 0, and 1 for x >= 0
def u(x):
    return np.where(x >= 0, 1.0, 0.0)

xs = np.linspace(-3, 3, 7)
print("x    :", xs)
print("u(x) :", u(xs))
print("jump at 0: u(-0.001)=%d, u(0)=%d, u(0.001)=%d" % (u(-0.001), u(0.0), u(0.001)))
```

</PyRunner>

---
layout: prism
heading: Real-Valued Functions (4/5)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The [Dirac-delta function]{.hl} is one of the functions used to approximate various waveforms; below is one such example:

$$
\delta_n(x) = \begin{cases} \dfrac{n}{2} & \text{if } |x| \leq \dfrac{1}{n} \\ 0 & \text{otherwise} \end{cases}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_dirac.svg" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Real-Valued Functions"
---

<PyRunner>

```python
import numpy as np

# delta_n(x) = n/2 for |x| <= 1/n, else 0.  Its integral over R should be 1 for every n.
def integral(n, N=200000):
    x = np.linspace(-1, 1, N)
    y = np.where(np.abs(x) <= 1/n, n/2, 0.0)
    dx = x[1] - x[0]
    return float(np.sum(y) * dx)          # Riemann sum

for n in [5, 10, 50, 200]:
    print(f"n={n:4d}  peak height = {n/2:7.1f}   integral over R = {integral(n):.4f}")
```

</PyRunner>

---
layout: prism
heading: Real-Valued Functions (5/5)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A function that fails to satisfy properties generally expected of functions is specifically called a [pathological function]{.hl}.

- One pathological function, [Thomae's function]{.hl}, is defined as

$$
f(x) = \begin{cases} 1 & x = 0 \\ \dfrac{1}{q} & x = \dfrac{p}{q},\ \gcd(p, q) = 1,\ q > 0 \\ 0 & x \notin \mathbb{Q} \end{cases}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_thomae.svg" class="tikz-fig" style="width: 80%;" />

</div>
</div>

- [DIY]{.hl} Look up the definition of [Dirichlet's function]{.hl} $\mathbf{1}_{\mathbb{Q}}(x)$ below and try to plot its graph: $\ \mathbf{1}_{\mathbb{Q}}(x) = 1$ if $x \in \mathbb{Q}$, and $0$ if $x \notin \mathbb{Q}$.

---
layout: prism
heading: "DIY: Real-Valued Functions"
---

<PyRunner>

```python
from math import gcd

# Thomae's function on a rational p/q in lowest terms: f(p/q) = 1/q
def thomae(p, q):
    g = gcd(p, q)
    p, q = p // g, q // g
    return 0.0 if q == 0 else 1.0 / q

for (p, q) in [(1, 2), (2, 4), (1, 3), (2, 3), (1, 7), (3, 9), (0, 1)]:
    print(f"f({p}/{q}) = {thomae(p, q):.4f}")

print("f(1/2) == f(2/4):", thomae(1, 2) == thomae(2, 4), "(same reduced fraction)")
```

</PyRunner>

---
layout: prism
heading: Complex-Valued Functions (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.1em;
}
</style>


- A [complex-valued function]{.hl} is a function whose domain and codomain are extended to the set of complex numbers.

- If a complex-valued function $f(z)$ is complex-differentiable in some region, then the function is said to possess [analyticity]{.hl} in that region, which is a stricter condition than the differentiability of a real-valued function.

- An analytic complex-valued function is also called a [holomorphic function]{.hl}.

---
layout: prism
heading: Complex-Valued Functions (2/2)
---

<div class="theorem-box">
<div class="theorem-box-title">Cauchy-Riemann equations</div>
<div class="theorem-box-body">

When a function $f(z) = u(z) + iv(z)$ is defined on an open set of the complex plane $\mathbb{C}$, the necessary and sufficient condition for it to be analytic is

$$
\begin{cases} \dfrac{\partial u}{\partial x} = \dfrac{\partial v}{\partial y} \\[4pt] \dfrac{\partial u}{\partial y} = -\dfrac{\partial v}{\partial x} \end{cases}
$$

</div>
</div>

---
layout: prism
heading: "DIY: Complex-Valued Functions"
---

<PyRunner>

```python
import numpy as np

# f(z) = z^2 = (x^2 - y^2) + i(2xy)  =>  u = x^2 - y^2,  v = 2xy
u = lambda x, y: x**2 - y**2
v = lambda x, y: 2*x*y
h = 1e-6
def d(f, x, y, axis):
    if axis == 'x': return (f(x+h, y) - f(x-h, y)) / (2*h)
    return (f(x, y+h) - f(x, y-h)) / (2*h)

for (x, y) in [(1.0, 2.0), (-0.5, 0.3)]:
    ux, vy = d(u, x, y, 'x'), d(v, x, y, 'y')
    uy, vx = d(u, x, y, 'y'), d(v, x, y, 'x')
    print(f"z=({x}, {y}):  u_x=v_y? {np.isclose(ux, vy)}    u_y=-v_x? {np.isclose(uy, -vx)}")
```

</PyRunner>

---
layout: prism
heading: Multivariate Functions
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem; grid-template-columns: 1.6fr 1fr;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.3em;
}
</style>

- A [multivariate function]{.hl} is a function whose value is determined by two or more independent variables.

- For a multivariate function, we can define [partial differentiation]{.hl}.

- The graph on the right visualizes the function $z = x^2 - y^2$.
  - [DIY]{.hl} Find $\partial z / \partial x$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_mesh.svg" class="tikz-fig" style="width: 70%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Multivariate Functions"
---

<PyRunner>

```python
import numpy as np

z = lambda x, y: x**2 - y**2
h = 1e-6
for (x, y) in [(1.0, 1.0), (2.0, -3.0), (0.5, 4.0)]:
    dzdx = (z(x+h, y) - z(x-h, y)) / (2*h)     # partial derivative wrt x
    print(f"(x,y)=({x}, {y}):  numeric dz/dx = {dzdx:.4f},  analytic 2x = {2*x:.4f}")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Functions</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Functions and Graphs</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Transformations of Functions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Translation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Reflection</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Scaling</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Rotation</span></p>
  </div>

</div>

---
layout: prism
heading: Translation (1/2)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- A [translation]{.hl} of a function is generally divided into two kinds.

- Shifting a function $f(x)$ by $h$ along the $x$-axis is called a [horizontal shift]{.hl}, computed as

$$
y = f(x - h).
$$

  - If $h > 0$, the graph shifts to the right by $h$.
  - If $h < 0$, the graph shifts to the left by $|h|$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_translate.svg" class="tikz-fig" style="width: 100%; margin-top: 6rem" />

</div>
</div>

---
layout: prism
heading: Translation (2/2)
---

- Shifting a function $f(x)$ by $k$ along the $y$-axis is called a [vertical shift]{.hl}, computed as

$$
y = f(x) + k.
$$

  - If $k > 0$, the graph shifts up by $k$.
  - If $k < 0$, the graph shifts down by $|k|$.

- [DIY]{.hl} Draw the result of translating $f(x) = 3x + 2$ by $-7$.

<PyRunner>

```python
import numpy as np

f = lambda x: 3*x + 2
xs = np.array([-1.0, 0.0, 1.0, 2.0])
print("x             :", xs)
print("f(x) = 3x+2   :", f(xs))
print("vertical  -7  :", f(xs) - 7)          # y = f(x) - 7 = 3x - 5
print("horizontal -7 :", f(xs - (-7)))       # y = f(x-h), h=-7  =>  f(x+7) = 3x + 23
```

</PyRunner>

---
layout: prism
heading: Reflection
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.6fr 1fr;">
<div>

- Moving a function so that it is symmetric with respect to an axis is called a [reflection]{.hl}; for symmetry about the $x$-axis it becomes $y = -f(x)$, and for symmetry about the $y$-axis it becomes $y = f(-x)$.

<PyRunner>

```python
import numpy as np

f = lambda x: x**2
xs = np.linspace(-2, 2, 5)
print("x               :", xs)
print("f(x) = x^2      :", f(xs))
# reflection across the x-axis
print("x-axis  y=-f(x) :", -f(xs))
# reflection across the y-axis (even -> unchanged)
print("y-axis  y=f(-x) :", f(-xs))
```

</PyRunner>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_reflect.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Scaling (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- A function can be enlarged ([scaling]{.hl}) or shrunk ([dilation]{.hl}).

- For vertical scaling, we multiply the function by a constant $a$ to enlarge or shrink the graph along the $y$-axis:

$$
y = a f(x)
$$

  - If $|a| > 1$, the graph is enlarged by a factor of $a$ along the $y$-axis.
  - If $0 < |a| < 1$, the graph is shrunk by a factor of $a$ along the $y$-axis.
  - If $a < 0$, it is simultaneously reflected about the $x$-axis.

---
layout: prism
heading: Scaling (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- For horizontal scaling, we multiply the input by a constant $b$ to enlarge or shrink the graph along the $x$-axis:

$$
y = f(bx)
$$

  - If $|b| > 1$, the graph is shrunk by a factor of $1/b$ along the $x$-axis.
  - If $0 < |b| < 1$, the graph is enlarged by a factor of $1/b$ along the $x$-axis.
  - If $b < 0$, it is simultaneously reflected about the $y$-axis.

---
layout: prism
heading: Rotation
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.6fr 1fr;">
<div>

- In general, to rotate $(x, y)$ by an angle $\theta$ and obtain $(x', y')$, we apply the following coordinate transformation:

$$
\begin{gathered} x' = x\cos\theta - y\sin\theta \\ y' = x\sin\theta + y\cos\theta \end{gathered}
$$

<PyRunner>

```python
import numpy as np

theta = np.pi / 4 # rotate by 45 degrees
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
pts = np.array([[1, 0], [0, 1], [1, 1]], float).T # columns are points
rot = R @ pts
for i in range(pts.shape[1]):
    x, y = pts[:, i]
    xr, yr = rot[:, i]
    print(f"({x:.0f}, {y:.0f}) -> ({xr:7.4f}, {yr:7.4f})")

print("length preserved:", 
      np.allclose(np.linalg.norm(pts, axis=0), 
                  np.linalg.norm(rot, axis=0)))
```

</PyRunner>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W03_rotate.svg" class="tikz-fig" style="width: 100%; margin-top: 3rem" />

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
