---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 9
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 09: Linear Algebra (Part 1)</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span class="text-gray-900 dark:text-gray-100">Linear Algebra, Part 1</span></p>
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
heading: Linear Algebra
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Linear algebra in the narrow sense concerns first-order (linear) equations, but the broader [linear algebra]{.hl} we aim to cover in this course encompasses multi-dimensional objects such as vectors and matrices, together with operations on such objects.

- The linear algebra generally applied in machine learning is a collection of operations on multi-dimensional mathematical objects; deep learning algorithms treat data as objects such as vectors and matrices.

- Scalars, vectors, matrices, and tensors are in fact all tensors of different orders, and can be expressed in a generalized way using tensor operations.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W09_00.png" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Linear Algebra Objects</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Scalars and Vectors</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Matrices and Tensors</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Tensor Arithmetic Operations</span></p>
  </div>

</div>

---
layout: prism
heading: Scalars and Vectors (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- A [scalar]{.hl} is the most basic numerical value we use, having only a single component.
  - Values such as $7$, $-3$, and $\pi$ are scalars.
  - By convention, it is written in the form $x$.

- A [vector]{.hl} is a one-dimensional array made up of several components.
  - A vector whose components are arranged vertically is called a row vector, and one whose components are arranged horizontally is called a column vector.
  - By convention, unless otherwise specified, a vector means a column vector, written in the form $\mathbf{x}$.
  - The $i$-th component of a vector is conventionally written $x_i$.

$$
\mathbf{x}=\begin{bmatrix} x_0 \\ x_1 \\ x_2 \end{bmatrix}
\qquad\qquad
\mathbf{x}^\top = \begin{bmatrix} x_0 & x_1 & x_2 \end{bmatrix}
$$

- The operation of swapping rows and columns ($\top$) is called the [transpose]{.hl}.

<PyRunner>

```python
import numpy as np

x = np.array([1.0, 2.0, 3.0])                # column vector by convention
print("vector x        :", x)
print("components      : x0=%.0f, x1=%.0f, x2=%.0f" % (x[0], x[1], x[2]))
print("transpose x^T   :", x.reshape(1, -1))
print("shape x, x^T    :", x.reshape(-1, 1).shape, x.reshape(1, -1).shape)
```

</PyRunner>

---
layout: prism
heading: Scalars and Vectors (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- From a geometric viewpoint, each component of a vector can be interpreted as a coordinate component in coordinate space, i.e., the distance traveled along each coordinate axis.

- In machine learning, the components of a vector are used to represent [features]{.hl}.
  - A feature in machine learning refers to a property of the data (e.g., ear shape, face shape) used in the process by which a model makes some decision (e.g., dog vs. cat classification).
  - Such a vector is also called a [feature vector]{.hl}.
  - Machine learning tends to ignore the geometric properties of feature vectors, but there also exist algorithms that use these geometric properties to obtain good results.
    - e.g., geometric deep learning, topological deep learning

- The set of all possible features is defined as the [feature space]{.hl}, and the dataset we use must reflect the feature space well.

---
layout: prism
heading: Matrices and Tensors
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- A [matrix]{.hl} is a two-dimensional array of numbers.
  - A column vector can be viewed as a matrix with a single column, and a row vector as a matrix with a single row.
  - By convention, it is written in the form $\mathbf{X}$.
  - The element at row $i$, column $j$ of a matrix $\mathbf{X}$ is conventionally written $x_{i,j}$.
    - In this course, we assume that each index starts from $0$.

$$
\mathbf{X}=\begin{bmatrix}
x_{0,0} & x_{0,1} & x_{0,2} & x_{0,3} \\
x_{1,0} & x_{1,1} & x_{1,2} & x_{1,3} \\
x_{2,0} & x_{2,1} & x_{2,2} & x_{2,3} \\
x_{3,0} & x_{3,1} & x_{3,2} & x_{3,3}
\end{bmatrix}
$$

- A scalar has no dimension, a vector has one dimension, and a matrix has two dimensions. A mathematical object with three or more dimensions is called a [tensor]{.hl}.
  - We use the [rank]{.hl} to express the dimension of a tensor: a scalar is a rank-0 tensor, a vector a rank-1 tensor, and a matrix a rank-2 tensor.

<PyRunner>

```python
import numpy as np

scalar = np.array(7.0)
vector = np.array([1.0, 2.0, 3.0])
matrix = np.arange(12).reshape(3, 4)
tensor = np.arange(24).reshape(2, 3, 4)

for name, t in [("scalar", scalar), ("vector", vector),
                ("matrix", matrix), ("tensor", tensor)]:
    print(f"{name:>7}: rank(ndim)={t.ndim}, shape={t.shape}")
print("x_{2,3} of matrix:", matrix[2, 3])
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Linear Algebra Objects</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Tensor Arithmetic Operations</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Vector Operations</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Matrix Operations</span></p>
  </div>

</div>

---
layout: prism
heading: Magnitude of a Vector
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- From a geometric viewpoint, a vector has a direction and a length.

- The length of a vector is called its [magnitude]{.hl}. The magnitude of a vector with $n$ components $x_0, x_1, \ldots, x_{n-1}$ is defined as follows.
  - Geometrically, it is connected to the Pythagorean theorem.

$$
\|\mathbf{x}\| = \sqrt{x_0^2 + x_1^2 + \cdots + x_{n-1}^2}
$$

- Dividing the components of a vector by its magnitude yields a vector with the same direction as the original but with magnitude $1$; this is called a [unit vector]{.hl} and is defined as

$$
\hat{\mathbf{x}} = \frac{\mathbf{x}}{\|\mathbf{x}\|}
$$

<PyRunner>

```python
import numpy as np

x = np.array([3.0, 4.0, 12.0])
mag = np.sqrt(np.sum(x**2))
print("magnitude ||x|| :", mag)
print("numpy norm      :", np.linalg.norm(x))

xhat = x / mag
print("unit vector     :", xhat)
print("||unit vector|| :", np.linalg.norm(xhat))
```

</PyRunner>

---
layout: prism
heading: Inner Product
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The [inner product (dot product)]{.hl} of two arbitrary vectors $\mathbf{x}$ and $\mathbf{y}$ with $n$ components is defined as follows, where $\theta$ is the angle between the two vectors.

$$
\begin{aligned}
\mathbf{x}\cdot\mathbf{y} = \langle \mathbf{x}, \mathbf{y}\rangle
&= \mathbf{x}^\top \mathbf{y} \\
&= \sum_{k=0}^{n-1} x_k y_k \\
&= \|\mathbf{x}\|\,\|\mathbf{y}\|\cos\theta
\end{aligned}
$$

- The inner product is commutative and distributive, but not associative.
  - $\mathbf{x}\cdot\mathbf{y} = \mathbf{y}\cdot\mathbf{x}$
  - $\mathbf{x}\cdot(\mathbf{y}+\mathbf{z}) = \mathbf{x}\cdot\mathbf{y} + \mathbf{x}\cdot\mathbf{z}$

- The inner product of two vectors whose angle is $\pi/2$ is $0$; in this case the two vectors are said to be [orthogonal]{.hl}.

<PyRunner>

```python
import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([4.0, -5.0, 6.0])

dot = np.dot(x, y)
print("x . y           :", dot, "=", x @ y)
cos_t = dot / (np.linalg.norm(x) * np.linalg.norm(y))
print("cos(theta)      :", round(cos_t, 4))

u, v = np.array([1.0, 0.0]), np.array([0.0, 1.0])
print("u . v           :", np.dot(u, v))
print("orthogonal?     :", np.isclose(np.dot(u, v), 0.0))
```

</PyRunner>

---
layout: prism
heading: Projection
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The [projection]{.hl} of a vector is an operation that computes how far one vector extends in the direction of another vector.

- The projection of $\mathbf{x}$ onto $\mathbf{y}$ is defined as

$$
\operatorname{proj}_{\mathbf{y}} \mathbf{x} = \frac{\mathbf{x}\cdot\mathbf{y}}{\|\mathbf{y}\|^2}\,\mathbf{y}
$$

- The projection of mutually orthogonal vectors is always $0$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W09_proj.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

<PyRunner>

```python
import numpy as np

x = np.array([4.0, 1.0])
y = np.array([3.0, 4.0])
proj = (np.dot(x, y) / np.dot(y, y)) * y
print("proj_y x        :", proj)

z = np.array([-4.0, 3.0])          # z is orthogonal to y
print("x.y , z.y       :", np.dot(x, y), np.dot(z, y))
print("proj_y z        :", (np.dot(z, y) / np.dot(y, y)) * y)
```

</PyRunner>

---
layout: prism
heading: Outer Product
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The inner product of two vectors is a scalar value, but the [outer product]{.hl} of two vectors is a matrix.

- Unlike the inner product, the outer product is defined even when the two vectors have different lengths. The outer product of a vector $\mathbf{x}$ with $m$ components and a vector $\mathbf{y}$ with $n$ components is defined as

$$
\mathbf{x}\times\mathbf{y} = \begin{bmatrix}
x_0 y_0 & x_0 y_1 & x_0 y_2 & \cdots & x_0 y_{n-1} \\
x_1 y_0 & x_1 y_1 & x_1 y_2 & \cdots & x_1 y_{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
x_{m-1} y_0 & x_{m-1} y_1 & x_{m-1} y_2 & \cdots & x_{m-1} y_{n-1}
\end{bmatrix}
$$

- From a similar viewpoint, we can define the [Cartesian product]{.hl} of two sets: $A\times B = \{(a, b) \mid \forall a\in A,\ \forall b\in B\}$.

<PyRunner>

```python
import numpy as np
from itertools import product

x = np.array([1, 2, 3])            # length m = 3
y = np.array([4, 5])               # length n = 2
print("outer product (3x2):")
print(np.outer(x, y))

A, B = {1, 2}, {"a", "b"}
print("Cartesian A x B :", sorted(product(A, B)))
```

</PyRunner>

---
layout: prism
heading: Hadamard Product
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- For two matrices $\mathbf{X}$ and $\mathbf{Y}$ of the same dimensions, we can define the [Hadamard product]{.hl}.

$$
\begin{aligned}
\mathbf{X}\odot\mathbf{Y} &= \begin{bmatrix}
x_{0,0} & x_{0,1} & x_{0,2} \\
x_{1,0} & x_{1,1} & x_{1,2} \\
x_{2,0} & x_{2,1} & x_{2,2}
\end{bmatrix}
\odot
\begin{bmatrix}
y_{0,0} & y_{0,1} & y_{0,2} \\
y_{1,0} & y_{1,1} & y_{1,2} \\
y_{2,0} & y_{2,1} & y_{2,2}
\end{bmatrix} \\[4pt]
&= \begin{bmatrix}
x_{0,0}y_{0,0} & x_{0,1}y_{0,1} & x_{0,2}y_{0,2} \\
x_{1,0}y_{1,0} & x_{1,1}y_{1,1} & x_{1,2}y_{1,2} \\
x_{2,0}y_{2,0} & x_{2,1}y_{2,1} & x_{2,2}y_{2,2}
\end{bmatrix}
\end{aligned}
$$

- More rigorously, if the result of the Hadamard product is a matrix $\mathbf{Z}$, it can be defined as $z_{ij} = x_{ij}\,y_{ij}$.

<PyRunner>

```python
import numpy as np

X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])

print("Hadamard X (.) Y (elementwise):")
print(X * Y)
print("matrix product X Y (for contrast):")
print(X @ Y)
```

</PyRunner>

---
layout: prism
heading: Matrix Multiplication
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- To compute the matrix product $\mathbf{XY}$ of matrices $\mathbf{X}$ and $\mathbf{Y}$, the number of columns of the left matrix must match the number of rows of the right matrix.

- Matrix multiplication takes the row vectors of $\mathbf{X}$ in order and computes their inner products with the column vectors of $\mathbf{Y}$. Letting the result of $\mathbf{XY}$ be $\mathbf{Z}$, it is defined as

$$
z_{i,j} = \sum_{k=0}^{m-1} x_{i,k}\, y_{k,j}
$$

- Matrix multiplication is associative and distributive, but not commutative.
  - $(\mathbf{XY})\mathbf{Z} = \mathbf{X}(\mathbf{YZ})$
  - $\mathbf{X}(\mathbf{Y}+\mathbf{Z}) = \mathbf{XY} + \mathbf{XZ}$
  - $\mathbf{XY} \neq \mathbf{YX}$

<PyRunner>

```python
import numpy as np

X = np.array([[1, 2, 3], [4, 5, 6]])       # 2x3
Y = np.array([[1, 0], [0, 1], [1, 1]])     # 3x2
print("X Y (2x2):")
print(X @ Y)

A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [1, 0]])
print("AB == BA ?      :", np.array_equal(A @ B, B @ A))
print("A applied to v  :", A @ np.array([1, 1]))   # matrix as a mapping
```

</PyRunner>

---
layout: prism
heading: Kronecker Product
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Whereas in matrix multiplication the components of the two matrices are mixed and multiplied, the [Kronecker product]{.hl} is obtained by multiplying the entire second matrix by each component of the first matrix.

- For an arbitrary $m\times n$ matrix $\mathbf{X}$, the Kronecker product is defined as

$$
\mathbf{X}\otimes\mathbf{Y} = \begin{bmatrix}
x_{0,0}\mathbf{Y} & x_{0,1}\mathbf{Y} & \cdots & x_{0,n-1}\mathbf{Y} \\
x_{1,0}\mathbf{Y} & x_{1,1}\mathbf{Y} & \cdots & x_{1,n-1}\mathbf{Y} \\
\vdots & \vdots & \ddots & \vdots \\
x_{m-1,0}\mathbf{Y} & x_{m-1,1}\mathbf{Y} & \cdots & x_{m-1,n-1}\mathbf{Y}
\end{bmatrix}
$$

<PyRunner>

```python
import numpy as np

X = np.array([[1, 2], [3, 4]])
Y = np.array([[0, 1], [1, 0]])
K = np.kron(X, Y)
print("Kronecker X (x) Y  ->  shape", K.shape)
print(K)
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
