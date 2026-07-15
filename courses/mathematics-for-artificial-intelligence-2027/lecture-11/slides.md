---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 11
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 11: Differentiation</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span class="text-gray-900 dark:text-gray-100">Differentiation</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Matrix Calculus</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Data Flow in Neural Networks</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Differentiation
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- In machine learning, integration is rarely used, whereas differentiation is used very frequently.
  - When training a neural network, the backpropagation algorithm computes derivatives to determine how much each weight should be updated.

- Starting from the concept of the slope of a function, we can derive the notion of the derivative.

- Derivatives can be used to find the minimum and maximum values of a function.

- For functions of two or more variables, we can define partial differentiation based on partial derivatives.
  - Partial derivatives play a central role in the backpropagation algorithm of neural networks.

- We also define the gradient, a kind of differentiation.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Slope and the Derivative</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Slope</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Derivative</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Differentiation Rules</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Minima and Maxima</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Partial Differentiation</span></p>
  </div>

</div>

---
layout: prism
heading: Slope (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- A straight line can be defined by the following linear equation:

$$
y = ax + b
$$

<div class="sub-item">

Here $a$ is the [slope]{.hl} of the line and $b$ is the $y$-[intercept]{.hl}, i.e., the point where the line meets the $y$-axis.

</div>

- Given two points $(x_1, y_1)$ and $(x_0, y_0)$ on the line, the slope is defined as

$$
a = \frac{y_1 - y_0}{x_1 - x_0}
$$

- The slope tells us how much $y$ changes as $x$ changes.
  - In the slope-intercept form, the slope is the [proportionality constant]{.hl} between $x$ and $y$, and the intercept $b$ is a [constant offset]{.hl}.

---
layout: prism
heading: "DIY: Slope of a Line"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
# Slope of the line through two points (x0, y0) and (x1, y1)
def slope(p0, p1):
    return (p1[1] - p0[1]) / (p1[0] - p0[0])

for p0, p1 in [((1.0, 2.0), (4.0, 8.0)), ((0.0, 3.0), (2.0, -1.0))]:
    a = slope(p0, p1)
    b = p0[1] - a * p0[0]                 # intercept from y = a x + b
    print(f"through {p0} and {p1}:  y = {a:.2f} x + {b:.2f}")
```

</PyRunner>

---
layout: prism
heading: Slope (2/3)
---

<div class="flex justify-center" style="margin-top: 1.5rem;">
<div style="width: 72%;">

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W11_tangent.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Slope (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A line passing through two points of a curve is called a [secant line]{.hl}, and a line that merely touches the curve at a single point is called a [tangent line]{.hl}.

- If we imagine the tangent line moving continuously along the curve, then as it approaches a [local maximum point]{.hl} or [local minimum point]{.hl}, the slope of the tangent approaches $0$.

- The points where the tangent slope becomes $0$ are called [stationary points]{.hl}.

- The slope of the tangent is useful in many ways, so we should be able to compute the tangent slope at any point on a curve.

---
layout: prism
heading: Definition of the Derivative (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The slope of the tangent to a curve at a point $x$ is called the [derivative]{.hl} at $x$.
  - The derivative expresses how the curve changes at the point $x$, i.e., how the function value changes when $x$ changes by an infinitesimally small amount.

- On a curve $y = f(x)$, the slope $\Delta y / \Delta x$ of the line through two points $x_0$ and $x_1$ is

$$
\frac{\Delta y}{\Delta x} = \frac{y_1 - y_0}{x_1 - x_0} = \frac{f(x_1) - f(x_0)}{x_1 - x_0}
$$

- Substituting $x_1 = x_0 + h$, the definition of the slope becomes

$$
\frac{\Delta y}{\Delta x} = \frac{f(x_0 + h) - f(x_0)}{h}
$$

---
layout: prism
heading: Definition of the Derivative (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Taking the [limit]{.hl} as $h \to 0$, we obtain the definition of the derivative.

$$
\frac{dy}{dx} = f'(x) \equiv \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

- We can also take the derivative of a derivative.
  - $f'(x)$ is the [first derivative]{.hl}; differentiating it again gives the [second derivative]{.hl}, written $f''(x)$ or $d^2 y / dx^2$.

- The [$n$th derivative]{.hl} can likewise be defined.

---
layout: prism
heading: "DIY: Numerical Derivative"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

f = lambda x: x**3 - 2*x        # test function, f'(x) = 3x^2 - 2
x0 = 1.5

print(f"{'h':>10} | {'secant slope':>14} | {'|error|':>10}")
for h in [1.0, 0.1, 0.01, 1e-4, 1e-6]:
    d = (f(x0 + h) - f(x0)) / h                 # forward difference -> tangent
    print(f"{h:>10} | {d:>14.6f} | {abs(d - (3*x0**2 - 2)):>10.6f}")

# Second derivative via a central difference
h = 1e-3
d2 = (f(x0 + h) - 2*f(x0) + f(x0 - h)) / h**2
print(f"\nf''({x0}) approx {d2:.4f}   (exact 6x = {6*x0})")
```

</PyRunner>

---
layout: prism
heading: The Power Rule
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- We use [differentiation rules]{.hl} to find derivatives; the derivative of a constant $c$ is $0$.

$$
\frac{d}{dx} c = 0
$$

- The power rule applies to differentiating powers of $x$.

$$
\frac{d}{dx} a x^n = n a x^{n-1}
$$

- The derivative operator is linear, so the derivative of terms combined by addition or subtraction is the addition or subtraction of the individual derivatives.

$$
\frac{d}{dx}(f(x) \pm g(x)) = \frac{d}{dx} f(x) \pm \frac{d}{dx} g(x)
$$

---
layout: prism
heading: "DIY: The Power Rule"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2*h)          # central difference

x = 2.0
# Power rule: d/dx a x^n = n a x^(n-1)
for a, n in [(3, 4), (1, 5), (2, 3)]:
    num = deriv(lambda t: a*t**n, x)
    print(f"d/dx {a}x^{n} at {x}: num={num:.4f}, rule={n*a*x**(n-1):.4f}")

# Linearity: (f + g)' = f' + g'
f, g = lambda t: t**3, lambda t: 2*t
lhs = deriv(lambda t: f(t) + g(t), x)
print("linearity holds:", np.isclose(lhs, deriv(f, x) + deriv(g, x)))
```

</PyRunner>

---
layout: prism
heading: Product, Quotient, and Chain Rules
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- To differentiate a product of two functions, apply the product rule.

$$
\frac{d}{dx} f(x) g(x) = f'(x) g(x) + f(x) g'(x)
$$

- To differentiate one function divided by another, apply the quotient rule.

$$
\frac{d}{dx}\left(\frac{f(x)}{g(x)}\right) = \frac{f'(x) g(x) - f(x) g'(x)}{g^2(x)}
$$

- To differentiate a composite function, apply the chain rule.
  - Neural networks based on backpropagation rely on this chain rule.

$$
\frac{d}{dx} f(g(x)) = \frac{d}{dx} f \circ g(x) = f'(g(x)) g'(x)
$$

---
layout: prism
heading: "DIY: Product, Quotient, and Chain Rules"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2*h)

x = 1.3
f,  g  = lambda t: t**2 + 1, lambda t: np.sin(t)
fp, gp = lambda t: 2*t,      lambda t: np.cos(t)

print("product :", np.isclose(d(lambda t: f(t)*g(t), x),
                              fp(x)*g(x) + f(x)*gp(x)))
print("quotient:", np.isclose(d(lambda t: f(t)/g(t), x),
                              (fp(x)*g(x) - f(x)*gp(x)) / g(x)**2))
print("chain   :", np.isclose(d(lambda t: f(g(t)), x), fp(g(x))*gp(x)))
```

</PyRunner>

---
layout: prism
heading: Derivatives of Trigonometric Functions
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The derivatives of the trigonometric functions are as follows:
  - cf. $\csc x = 1/\sin x$, $\sec x = 1/\cos x$, $\cot x = 1/\tan x$

$$
\begin{gather*}
\frac{d}{dx}\sin x = \cos x\\
\frac{d}{dx}\cos x = -\sin x\\
\frac{d}{dx}\tan x = \sec^2 x
\end{gather*}
$$

---
layout: prism
heading: "DIY: Trigonometric Derivatives"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2*h)

x = 0.7
print("d/dx sin x  = cos x    :", np.isclose(d(np.sin, x), np.cos(x)))
print("d/dx cos x  = -sin x   :", np.isclose(d(np.cos, x), -np.sin(x)))
print("d/dx tan x  = sec^2 x  :", np.isclose(d(np.tan, x), 1/np.cos(x)**2))
```

</PyRunner>

---
layout: prism
heading: Derivatives of Exponential Functions
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The derivative of the exponential function is itself.

$$
\frac{d}{dx} e^x = e^x
$$

- When the exponent is a function of $x$, the following rule applies.

$$
\frac{d}{dx} e^{g(x)} = g'(x) e^{g(x)}
$$

- Generalizing, we have

$$
\frac{d}{dx} a^{g(x)} = \ln(a) g'(x) a^{g(x)}
$$

---
layout: prism
heading: Derivatives of Logarithmic Functions
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The derivative of the natural logarithm is

$$
\frac{d}{dx} \ln x = \frac{1}{x}
$$

- When the argument is a function of $x$, the following rule applies.

$$
\frac{d}{dx} \ln g(x) = \frac{g'(x)}{g(x)}
$$

- Generalizing, we have

$$
\frac{d}{dx} \log_b g(x) = \frac{g'(x)}{g(x) \ln b}
$$

---
layout: prism
heading: "DIY: Exponential and Logarithmic Derivatives"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

def d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2*h)

x, b = 1.4, 2.0
g = lambda t: t**2                              # inner function g(x) = x^2
print("d/dx e^x   = e^x   :", np.isclose(d(np.exp, x), np.exp(x)))
print("d/dx e^{x^2}       :", np.isclose(d(lambda t: np.exp(g(t)), x),
                                         2*x*np.exp(x**2)))
print("d/dx ln x  = 1/x   :", np.isclose(d(np.log, x), 1/x))
print("d/dx log2(x^2)     :", np.isclose(d(lambda t: np.log(g(t))/np.log(b), x),
                                         2*x/(x**2*np.log(b))))
```

</PyRunner>

---
layout: prism
heading: Minima and Maxima of a Function
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Stationary points let us judge whether a point on a curve is a minimum or a maximum.
  - Among all [local minima]{.hl}, the smallest is the [global minimum]{.hl}; among all [local maxima]{.hl}, the largest is the [global maximum]{.hl}.

- Minima and maxima together are called [extrema]{.hl}.

- However, even if the derivative is $0$ at a stationary point, if it is not smaller (or larger) than all nearby points, it is not a minimum (or maximum).

- A stationary point that is not an extremum is called an [inflection point]{.hl}, or, for functions of several variables, a [saddle point]{.hl}.

---
layout: prism
heading: "DIY: Stationary Points"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

f  = lambda x: x**3 - 3*x                        # f'(x) = 3x^2 - 3 = 0 -> x = +/-1
d  = lambda g, x, h=1e-5: (g(x+h) - g(x-h)) / (2*h)
d2 = lambda g, x, h=1e-3: (g(x+h) - 2*g(x) + g(x-h)) / h**2

xs = np.linspace(-2, 2, 4001)
sign = np.sign([d(f, x) for x in xs])            # sign of the first derivative
for i in np.where(np.diff(sign) != 0)[0]:        # where f' changes sign
    x = xs[i]
    kind = "minimum" if d2(f, x) > 0 else "maximum"
    print(f"stationary near x={x:+.3f}: {kind} (f={f(x):+.3f})")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Slope and the Derivative</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Partial Differentiation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Partial Derivatives</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Mixed Partial Derivatives</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Multivariable Chain Rule</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Computing the Gradient</span></p>
  </div>

</div>

---
layout: prism
heading: Definition of the Partial Derivative
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- For functions of two or more variables, e.g., $f(x, y)$ or $f(x_0, x_1, x_2, \cdots, x_n)$, we use [partial differentiation]{.hl} (the partial derivative).

- A partial derivative is the derivative with respect to one particular variable: we fix the other variables as constants and differentiate with respect to only that variable.

- Partial derivatives use the $\partial$ symbol; for example, the partial derivatives of $f(x, y, z) = x^2 + y^2 + z^2 + 3xyz$ are

$$
\begin{gather*}
\frac{\partial}{\partial x} f(x, y, z) = 2x + 3yz\\
\frac{\partial}{\partial y} f(x, y, z) = 2y + 3xz\\
\frac{\partial}{\partial z} f(x, y, z) = 2z + 3xy
\end{gather*}
$$

---
layout: prism
heading: "DIY: Partial Derivatives"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
f = lambda x, y, z: x**2 + y**2 + z**2 + 3*x*y*z
h = 1e-6
x, y, z = 1.0, 2.0, 3.0

fx = (f(x+h, y, z) - f(x-h, y, z)) / (2*h)
fy = (f(x, y+h, z) - f(x, y-h, z)) / (2*h)
fz = (f(x, y, z+h) - f(x, y, z-h)) / (2*h)

print("df/dx:", round(fx, 4), " exact 2x+3yz =", 2*x + 3*y*z)
print("df/dy:", round(fy, 4), " exact 2y+3xz =", 2*y + 3*x*z)
print("df/dz:", round(fz, 4), " exact 2z+3xy =", 2*z + 3*x*y)
```

</PyRunner>

---
layout: prism
heading: Mixed Partial Derivatives
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Just as we can take the derivative of a derivative, we can take the partial derivative of a partial derivative.

- Mixed partial derivatives can differentiate with respect to different variables; for example, a mixed partial of $f(x, y, z) = x^2 + y^2 + z^2 + 3xyz$ is

$$
\frac{\partial}{\partial x}\frac{\partial}{\partial y} f(x, y, z) = \frac{\partial^2}{\partial x\, \partial y} f(x, y, z) = 3z
$$

---
layout: prism
heading: "DIY: Mixed Partial Derivatives"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

f = lambda x, y, z: x**2 + y**2 + z**2 + 3*x*y*z
h = 1e-4
x, y, z = 1.0, 2.0, 3.0

dy = lambda x, y, z: (f(x, y+h, z) - f(x, y-h, z)) / (2*h)
dx = lambda x, y, z: (f(x+h, y, z) - f(x-h, y, z)) / (2*h)

fxy = (dy(x+h, y, z) - dy(x-h, y, z)) / (2*h)     # d/dx of (df/dy)
fyx = (dx(x, y+h, z) - dx(x, y-h, z)) / (2*h)     # d/dy of (df/dx)

print("d2f/dxdy:", round(fxy, 3), " (exact 3z =", 3*z, ")")
print("symmetric (fxy == fyx):", np.isclose(fxy, fyx, atol=1e-3))
```

</PyRunner>

---
layout: prism
heading: The Multivariable Chain Rule
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- When $x$ and $y$ of $f(x, y)$ are themselves functions $x(r, s)$ and $y(r, s)$ of other variables, finding the partial derivatives of $f$ with respect to $r$ and $s$ requires applying the chain rule to each of $x$ and $y$.

$$
\begin{gather*}
\frac{\partial f}{\partial r} = \left(\frac{\partial f}{\partial x}\right)\left(\frac{\partial x}{\partial r}\right) + \left(\frac{\partial f}{\partial y}\right)\left(\frac{\partial y}{\partial r}\right)\\
\frac{\partial f}{\partial s} = \left(\frac{\partial f}{\partial x}\right)\left(\frac{\partial x}{\partial s}\right) + \left(\frac{\partial f}{\partial y}\right)\left(\frac{\partial y}{\partial s}\right)
\end{gather*}
$$

---
layout: prism
heading: "DIY: The Multivariable Chain Rule"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

f = lambda x, y: x**2 + x*y
x = lambda r, s: r*s
y = lambda r, s: r + s
h = 1e-6
r0, s0 = 1.5, 2.0

F = lambda r, s: f(x(r, s), y(r, s))
direct = (F(r0+h, s0) - F(r0-h, s0)) / (2*h)      # df/dr directly

xv, yv = x(r0, s0), y(r0, s0)
fx = (f(xv+h, yv) - f(xv-h, yv)) / (2*h)
fy = (f(xv, yv+h) - f(xv, yv-h)) / (2*h)
xr = (x(r0+h, s0) - x(r0-h, s0)) / (2*h)
yr = (y(r0+h, s0) - y(r0-h, s0)) / (2*h)
chain = fx*xr + fy*yr                             # df/dr via chain rule
print("df/dr direct:", round(direct, 4), " chain rule:", round(chain, 4))
print("match:", np.isclose(direct, chain))
```

</PyRunner>

---
layout: prism
heading: Computing the Gradient
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- If we interpret a multivariable function $f(x, y, z)$ as positions on coordinate axes, then $f$ returns a single scalar value at an arbitrary point $(x, y, z)$ in 3D space.
  - Setting $\mathbf{x} = (x, y, z)$, the function $f(\mathbf{x})$ maps one vector to one scalar.
  - A function that takes a vector and returns a scalar is called a [scalar field]{.hl}.

- The [gradient]{.hl} is the derivative of a function that takes a vector; mathematically it extends partial differentiation to $n$ dimensions.

- The gradient uses the $\nabla$ operator, called gradient, del, or nabla.

$$
\nabla f(\mathbf{x}) = \nabla f(x_0, x_1, \ldots, x_n) \equiv \begin{bmatrix}
\frac{\partial f}{\partial x_0}\\
\frac{\partial f}{\partial x_1}\\
\vdots\\
\frac{\partial f}{\partial x_n}
\end{bmatrix}
$$

---
layout: prism
heading: "DIY: The Gradient"
---

<div style="height: 2rem;"></div>

<PyRunner>

```python
import numpy as np

f = lambda v: v[0]**2 + v[1]**2 + v[2]**2 + 3*v[0]*v[1]*v[2]

def gradient(f, v, h=1e-6):
    v = np.asarray(v, float)
    g = np.zeros_like(v)
    for i in range(len(v)):
        e = np.zeros_like(v); e[i] = h
        g[i] = (f(v + e) - f(v - e)) / (2*h)
    return g

x = np.array([1.0, 2.0, 3.0])
grad  = gradient(f, x)
exact = np.array([2*x[0] + 3*x[1]*x[2], 2*x[1] + 3*x[0]*x[2], 2*x[2] + 3*x[0]*x[1]])
print("nabla f :", np.round(grad, 4))
print("exact   :", exact)
print("match   :", np.allclose(grad, exact))
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
