---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 10
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 10: Linear Algebra (Part 2)</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span class="text-gray-900 dark:text-gray-100">Linear Algebra, Part 2</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">Differentiation</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Matrix Calculus</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Data Flow in Neural Networks</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Recap of Week 9
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Scalars, vectors, and matrices can all be generalized as tensors, corresponding to rank-0, rank-1, and rank-2 tensors, respectively.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W10_tensor.svg" class="tikz-fig" style="width: 100%;" />

</div>
<div>

- A scalar is a value with a single component, a vector is an array of several components at rank 1, and a matrix is an array of vectors at an additional rank.

- For each of these tensors, various operations exist, such as magnitude, inner product, and projection.

</div>
</div>

---
layout: prism
heading: Linear Algebra
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Beyond merely operating on tensors, linear algebra is used to represent space based on the properties that tensors possess, and at the same time to analyze the characteristics of that space.

- It is also used to compute the intrinsic values that each tensor space possesses, and to measure distances within various spaces.
  - In machine learning, there are many algorithms that are trained in a direction that reduces the distance between data distributions.

- Algorithms that reduce the dimension of a space to compute representative values are also carried out using linear algebra.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Square Matrices</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Square Matrices</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Operations on Square Matrices</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Special Square Matrices</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Determinants and Their Operations</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Eigenvalues and Eigenvectors</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Vector Norms, Distances, and PCA</span></p>
  </div>

</div>

---
layout: prism
heading: The Geometric Meaning of Matrices
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- Multiplying a matrix by a column vector yields another column vector.

$$
\begin{bmatrix} 1 & 2 & 3 & 4 \\ 5 & 6 & 7 & 8 \end{bmatrix}
\begin{bmatrix} 11 \\ 12 \\ 13 \\ 14 \end{bmatrix}
= \begin{bmatrix} 130 \\ 330 \end{bmatrix}
$$

- Geometrically, an $\mathbb{R}^{2\times 4}$ matrix [maps]{.hl} a column vector representing a point in the $\mathbb{R}^4$ space to a point in the $\mathbb{R}^2$ space.
  - This mapping is done linearly (no nonlinear operations such as exponentiation are used).
  - That is, a matrix is a means of transforming a point in one space into another space.

- For a [square matrix]{.hl} whose row and column sizes are both $n$, the mapping is from $\mathbb{R}^n$ to $\mathbb{R}^n$.

$$
\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}
\begin{bmatrix} 11 \\ 12 \\ 13 \end{bmatrix}
= \begin{bmatrix} 74 \\ 182 \\ 209 \end{bmatrix}
$$

---
layout: prism
heading: "DIY: Matrix as a Linear Map"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8]])
print("R^4 -> R^2 :", A @ np.array([11, 12, 13, 14]))   # matrix as a linear map

B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("R^3 -> R^3 :", B @ np.array([11, 12, 13]))

# scalar/vector/matrix are rank-0/1/2 tensors; reshape moves between ranks
t = np.arange(24)
print("rank-1 shape :", t.shape)
print("rank-3 shape :", t.reshape(2, 3, 4).shape)
```

</PyRunner>

---
layout: prism
heading: Rotation Matrices
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- From a similar viewpoint, a [rotation matrix]{.hl} can also be thought of as mapping a point in one space to a point in another.
  - A rotation by $\theta$ in two-dimensional space is defined as follows.

$$
\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}
$$

  - In three-dimensional space, the rotations are defined as follows.

$$
\begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{bmatrix}_x,\
\begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}_y,\
\begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}_z
$$

---
layout: prism
heading: Affine Transformations
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Using a matrix, we can define an [affine transformation]{.hl}, a mapping under the condition that a line in one space still remains a line in the mapped space.

- An affine transformation maps a vector $\mathbf{x}$ to a new vector $\mathbf{y}$ using a matrix transform $\mathbf{A}$ and a translation $\mathbf{b}$.

$$
\mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b}
$$

  - [DIY]{.hl} For $\mathbf{W} = \begin{bmatrix} w_{0,0} & w_{0,1} \\ w_{1,0} & w_{1,1} \end{bmatrix}$ and $\mathbf{b} = \begin{bmatrix} b_0 \\ b_1 \end{bmatrix}$, express the affine transformation of $\mathbf{x} = \begin{bmatrix} x_0 \\ x_1 \end{bmatrix}$ into $\mathbf{y} = \begin{bmatrix} y_0 \\ y_1 \end{bmatrix}$ as a single matrix.

- Each layer of a neural network is nothing more than an affine transformation.
  - However, because a nonlinear activation function generally exists between the layers, a neural network learns how to map inputs to outputs that reflect the appropriate relationships.
  - Without a nonlinear activation function, no matter how many layers a network has, it would be no different from a single-layer network.

---
layout: prism
heading: "DIY: Affine Transformation as a Matrix"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

W = np.array([[2.0, -1.0], [1.0, 3.0]])
b = np.array([5.0, -2.0])
x = np.array([4.0, 1.0])

# affine y = W x + b  ==  a single augmented matrix times [x; 1]
M = np.block([[W, b.reshape(2, 1)],
              [np.zeros((1, 2)), np.ones((1, 1))]])
xa = np.append(x, 1.0)

print("y = W x + b        :", W @ x + b)
print("y via aug. matrix  :", (M @ xa)[:2])
```

</PyRunner>

---
layout: prism
heading: Transpose, Trace, and Powers
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- A square matrix remains a square matrix even after the transpose operation.

- On square matrices, the [trace]{.hl} operation is defined; for any square matrix $\mathbf{A}$, the trace $\operatorname{tr}(\cdot)$ is defined as follows.

$$
\operatorname{tr}(\mathbf{A}) = \sum_i a_{i,i}
$$

- Also, since a square matrix has equal row and column sizes, powers can be defined.

$$
\mathbf{A}^n = \underbrace{\mathbf{A}\mathbf{A}\cdots\mathbf{A}}_{n}
$$

  - Only for square matrices can exponent rules be defined in the same way as for scalars.

---
layout: prism
heading: "DIY: Trace and Matrix Powers"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
print("trace(A) :", np.trace(A))
print("A^3      :\n", np.linalg.matrix_power(A, 3))

# det(A^n) == det(A)^n
n = 3
print("det(A^3) :", round(np.linalg.det(np.linalg.matrix_power(A, n)), 4))
print("det(A)^3 :", round(np.linalg.det(A) ** n, 4))
```

</PyRunner>

---
layout: prism
heading: Special Square Matrices (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- Among square matrices, the [zero matrix]{.hl} and the [ones matrix]{.hl} are the square matrices whose entries are all $0$ and all $1$, respectively.
  - For size $n$, they are conventionally written $\mathbf{0}_n$ and $\mathbf{1}_n$.

- The [identity matrix]{.hl} (also called the unit matrix, since it is the identity of matrix multiplication) is a square matrix with $1$s on the diagonal and $0$s elsewhere.
  - For size $n$, it is conventionally written $\mathbf{I}_n$ or $\mathbb{1}_n$.

$$
\mathbf{I}_n = \begin{bmatrix}
1 & 0 & 0 & \cdots & 0 \\
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & 1
\end{bmatrix}
$$

- A matrix with nonzero entries only on the main diagonal is called a [diagonal matrix]{.hl}.

---
layout: prism
heading: "DIY: Identity and Diagonal Matrices"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

print("identity I_3 :\n", np.eye(3, dtype=int))
print("zeros  0_2   :\n", np.zeros((2, 2), dtype=int))
print("ones   1_2   :\n", np.ones((2, 2), dtype=int))

D = np.diag([2, 5, 7])
print("diagonal     :\n", D)
print("I is identity of matmul :", np.array_equal(np.eye(3, dtype=int) @ D, D))
```

</PyRunner>

---
layout: prism
heading: Special Square Matrices (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- On square matrices we can define [triangular matrices]{.hl}: a matrix with nonzero entries only above the main diagonal is an upper triangular matrix, and one with nonzero entries only below the main diagonal is a lower triangular matrix.
  - [DIY]{.hl} Find the upper and lower triangular matrices of $\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$.

- Triangular matrices are used in a variety of linear algebra operations.

---
layout: prism
heading: "DIY: Triangular Matrices"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("upper triangular :\n", np.triu(A))
print("lower triangular :\n", np.tril(A))

# the determinant of a triangular matrix is the product of its diagonal
U = np.triu(A)
print("det(U) :", round(np.linalg.det(U), 4), "= prod(diag) =", np.prod(np.diag(U)))
```

</PyRunner>

---
layout: prism
heading: Determinants (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- The [determinant]{.hl} of a square matrix is a function that maps the square matrix to a single scalar.

- For any square matrix $\mathbf{A}$, the determinant $\operatorname{det}(\mathbf{A}) \in \mathbb{R}$ has the following properties.
  - The determinant of a $1 \times 1$ matrix equals itself.
  - If $\mathbf{A}$ has a row or column of all zeros, then $\operatorname{det}(\mathbf{A}) = 0$.
  - If $\mathbf{A}$ has two identical rows, then $\operatorname{det}(\mathbf{A}) = 0$.
  - If $\mathbf{A}$ is triangular, then $\operatorname{det}(\mathbf{A}) = \prod_{i=0}^{n-1} a_{i,i}$.
  - If $\mathbf{A}$ is diagonal, then $\operatorname{det}(\mathbf{A}) = \prod_{i=0}^{n-1} a_{i,i}$.
  - The determinant of the identity matrix is always $1$.
  - $\operatorname{det}(\mathbf{A}\mathbf{B}) = \operatorname{det}(\mathbf{A})\operatorname{det}(\mathbf{B})$
  - $\operatorname{det}(\mathbf{A}) = \operatorname{det}(\mathbf{A}^\top)$
  - $\operatorname{det}(\mathbf{A}^n) = \operatorname{det}(\mathbf{A})^n$

- There are several ways to compute a determinant, but a recursive-formula-based method is the one most commonly used.

---
layout: prism
heading: Determinants (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- To define the recurrence, we use the following definitions.
  - For any matrix $\mathbf{A}$, its [minor matrix]{.hl} $\mathbf{A}_{ij}$ is defined as the matrix obtained by removing the $i$-th row and $j$-th column from $\mathbf{A}$.

$$
\mathbf{A} = \begin{bmatrix} 9 & 8 & 7 \\ 6 & 5 & 4 \\ 3 & 2 & 1 \end{bmatrix} \Rightarrow
\mathbf{A}_{11} = \begin{bmatrix} 9 & 7 \\ 3 & 1 \end{bmatrix}
$$

  - The [cofactor]{.hl} $C_{ij}$ of a minor $\mathbf{A}_{ij}$ is defined as follows.

$$
C_{ij} = (-1)^{i+j+2}\operatorname{det}(\mathbf{A}_{ij})
$$

- Using these definitions, the determinant via cofactor expansion is defined as follows.

$$
\operatorname{det}(\mathbf{A}) = \sum_{j=0}^{n-1} a_{0,j} C_{0j}
$$

  - [DIY]{.hl} Find the determinant of $\mathbf{A} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$.

---
layout: prism
heading: "DIY: Determinant by Cofactor Expansion"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0], [3.0, 2.0, 1.0]])

def det(M):                       # cofactor expansion along the first row
    n = len(M)
    if n == 1:
        return M[0, 0]
    total = 0.0
    for j in range(n):
        minor = np.delete(np.delete(M, 0, axis=0), j, axis=1)
        total += (-1) ** j * M[0, j] * det(minor)
    return total

print("cofactor expansion :", det(A))
print("numpy det          :", round(np.linalg.det(A), 6))
print("det([[a,b],[c,d]]) = ad - bc :", det(np.array([[3.0, 1.0], [2.0, 4.0]])))
```

</PyRunner>

---
layout: prism
heading: Inverse Matrices (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- One main use of the determinant is to determine whether the [inverse matrix]{.hl} of a matrix exists.

- Just as the identity matrix is like the identity of scalar multiplication, the inverse behaves like the inverse of scalar multiplication.

- For any matrix $\mathbf{A}$ whose inverse exists, the inverse $\mathbf{A}^{-1}$ satisfies the following.

$$
\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}
$$

- If $\mathbf{A}^{-1}$ exists, the following holds.

$$
\operatorname{det}(\mathbf{A}^{-1}) = \frac{1}{\operatorname{det}(\mathbf{A})}
$$

  - [DIY]{.hl} Construct a matrix that has no inverse.

---
layout: prism
heading: "DIY: Inverse and Singular Matrices"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[4.0, 7.0], [2.0, 6.0]])
Ainv = np.linalg.inv(A)
print("A^-1               :\n", Ainv)
print("A A^-1 = I         :", np.allclose(A @ Ainv, np.eye(2)))
print("det(A^-1)=1/det(A) :", np.isclose(np.linalg.det(Ainv), 1 / np.linalg.det(A)))

# solving A x = b relies on the inverse implicitly
print("solve A x = b      :", np.linalg.solve(A, np.array([1.0, 2.0])))

# a singular matrix has no inverse (det = 0, rank < n)
S = np.array([[1.0, 2.0], [2.0, 4.0]])
print("det(S), rank(S)    :", round(np.linalg.det(S), 4), np.linalg.matrix_rank(S))
```

</PyRunner>

---
layout: prism
heading: Inverse Matrices (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- When the inverse exists, the following property also holds.

$$
(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}
$$

- The inverse of a diagonal matrix is the matrix of reciprocals of its diagonal entries.

$$
\mathbf{A} = \begin{bmatrix} a & 0 & 0 \\ 0 & b & 0 \\ 0 & 0 & c \end{bmatrix}
\Leftrightarrow
\mathbf{A}^{-1} = \begin{bmatrix} a^{-1} & 0 & 0 \\ 0 & b^{-1} & 0 \\ 0 & 0 & c^{-1} \end{bmatrix},\ \forall a, b, c \neq 0
$$

- A matrix with no inverse is called a [singular matrix]{.hl} or a degenerate matrix.
  - That is, the determinant of a singular matrix is $0$.
  - A matrix that is not singular is called a nonsingular or nondegenerate matrix.

---
layout: prism
heading: Symmetric and Orthogonal Matrices
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A square matrix satisfying the following condition is called a [symmetric matrix]{.hl}.

$$
\mathbf{A}^\top = \mathbf{A}
$$

  - Multiplication of symmetric matrices is commutative.

$$
\mathbf{A}\mathbf{B} = \mathbf{B}\mathbf{A} \Leftrightarrow \mathbf{A} = \mathbf{A}^\top,\ \mathbf{B} = \mathbf{B}^\top
$$

- A square matrix satisfying the following condition is called an [orthogonal matrix]{.hl}.

$$
\mathbf{A}\mathbf{A}^\top = \mathbf{A}^\top\mathbf{A} = \mathbf{I}
$$

  - For an orthogonal matrix $\mathbf{A}$, $\mathbf{A}^{-1} = \mathbf{A}^\top$ holds, and therefore $\operatorname{det}(\mathbf{A}) = \pm 1$.

---
layout: prism
heading: "DIY: Orthogonal Matrices"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

theta = np.pi / 4
Q = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])   # a rotation is orthogonal

print("Q Q^T = I   :", np.allclose(Q @ Q.T, np.eye(2)))
print("Q^-1 = Q^T  :", np.allclose(np.linalg.inv(Q), Q.T))
print("det(Q) = ±1 :", round(np.linalg.det(Q), 4))
```

</PyRunner>

---
layout: prism
heading: Definiteness
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- For any column vector $\mathbf{x}$, a symmetric matrix $\mathbf{A}$ satisfying the following condition is called [positive definite]{.hl}.

$$
\mathbf{x}^\top\mathbf{A}\mathbf{x} > 0,\ \forall \mathbf{x} \neq 0
$$

  - Similarly, if it satisfies the following condition, it is positive semidefinite.

$$
\mathbf{x}^\top\mathbf{A}\mathbf{x} \geq 0
$$

- For any column vector $\mathbf{x}$, a symmetric matrix $\mathbf{A}$ satisfying the following condition is called [negative definite]{.hl}.

$$
\mathbf{x}^\top\mathbf{A}\mathbf{x} < 0,\ \forall \mathbf{x} \neq 0
$$

  - Similarly, if it satisfies the following condition, it is negative semidefinite.

$$
\mathbf{x}^\top\mathbf{A}\mathbf{x} \leq 0
$$

---
layout: prism
heading: Unitary Matrices
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- We can also define matrices with complex entries. If a complex matrix $\mathbf{U}$ satisfies the following condition, then $\mathbf{U}$ is a [unitary matrix]{.hl} and $\mathbf{U}^*$ is the [conjugate transpose]{.hl} of $\mathbf{U}$, also called the Hermitian adjoint.

$$
\mathbf{U}^*\mathbf{U} = \mathbf{U}\mathbf{U}^* = \mathbf{I}
$$

  - The Hermitian adjoint is sometimes written $\mathbf{U}^\dagger$, and when a unitary matrix equals its own Hermitian adjoint, such a matrix is called a Hermitian matrix.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Square Matrices</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Eigenvalues and Eigenvectors</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Eigenvalues and Eigenvectors</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Vector Norms, Distances, and PCA</span></p>
  </div>

</div>

---
layout: prism
heading: Eigenvalues and Eigenvectors (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A square matrix maps a vector in one space to another vector in the same space.
  - Consider the case where $\mathbf{v}'$ and $\mathbf{v}$ are vectors in $n$-dimensional space, $\mathbf{A}$ is an $n \times n$ matrix, and $\mathbf{v}' = \mathbf{A}\mathbf{v}$.

- For a nonzero $\mathbf{v}$ and any scalar $\lambda$, we can consider the following equation.

$$
\mathbf{A}\mathbf{v} = \lambda\mathbf{v}
$$

  - That is, mapping $\mathbf{v}$ by $\mathbf{A}$ produces a scalar multiple of $\mathbf{v}$; here $\mathbf{v}$ is an [eigenvector]{.hl} of $\mathbf{A}$ and $\lambda$ is its [eigenvalue]{.hl}.
  - Geometrically, $\mathbf{A}$ only scales the eigenvector up or down without changing its direction.
  - [DIY]{.hl} Check whether every matrix always has an eigenvector.

---
layout: prism
heading: Eigenvalues and Eigenvectors (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Assuming an eigenvector exists, the equation for finding the eigenvalues of a matrix is as follows.

$$
\mathbf{A}\mathbf{v} - \lambda\mathbf{v} = \mathbf{A}\mathbf{v} - \lambda\mathbf{I}\mathbf{v} = (\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{0}
$$

  - That is, for $\mathbf{v}$ to be nonzero, the determinant of $\mathbf{A} - \lambda\mathbf{I}$ must be $0$.

- This equation $\operatorname{det}(\mathbf{A} - \lambda\mathbf{I}) = 0$ is called the [characteristic equation]{.hl}.
  - The characteristic polynomial of an $n \times n$ matrix is a polynomial of degree $n$.
  - [DIY]{.hl} Compute the eigenvalues of $\begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}$.

---
layout: prism
heading: "DIY: Eigenvalues"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

A = np.array([[0.0, 1.0], [-2.0, -3.0]])
vals, vecs = np.linalg.eig(A)
print("eigenvalues :", np.round(vals, 4))

for lam, v in zip(vals, vecs.T):
    print(f"lambda = {lam:.1f}:  A v = {np.round(A @ v, 4)},  lambda v = {np.round(lam * v, 4)}")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Square Matrices</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Eigenvalues and Eigenvectors</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Vector Norms, Distances, and PCA</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Norms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Distance Functions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Covariance Matrices</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Mahalanobis Distance</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Kullback-Leibler Divergence</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Principal Component Analysis</span></p>
  </div>

</div>

---
layout: prism
heading: Norms and Distance Functions
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Mathematically, a [norm]{.hl} and a distance are distinct concepts, but they tend to be used interchangeably in machine learning.

- A [vector norm]{.hl} is a function that maps a vector to a nonnegative real number, and the "distance" of a vector is often called its norm.
  - When measuring the distance between two vectors, the distance should be the same regardless of the input order, but some functions that do not satisfy this condition are still used as distances.

- Vector norms are widely used as a simple way to measure distances between vectors, and they are also used to define various kinds of distance functions.

---
layout: prism
heading: "$L$-Norms and Distance Functions (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- The $L_p$-norm of an $n$-dimensional vector $\mathbf{x}$ is defined as follows, where $p$ is a real number.

$$
\|\mathbf{x}\|_p \equiv \left( \sum_i |x_i|^p \right)^{\frac{1}{p}}
$$

- The magnitude of a vector is the $L_2$-norm.

$$
\|\mathbf{x}\|_2 = \sqrt{x_0^2 + x_1^2 + x_2^2 + \cdots + x_{n-1}^2} = \sqrt{\mathbf{x}^\top \mathbf{x}}
$$

- In addition, we can define the $L_1$-norm and the $L_\infty$-norm.

$$
\|\mathbf{x}\|_1 = \sum_i |x_i| \qquad\qquad \|\mathbf{x}\|_\infty = \max_i |x_i|
$$

---
layout: prism
heading: "$L$-Norms and Distance Functions (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Replacing $\mathbf{x}$ with the difference $\mathbf{x} - \mathbf{y}$, a norm can be regarded as the distance between two vectors.

$$
L_p(\mathbf{x}, \mathbf{y}) = \left( \sum_i |x_i - y_i|^p \right)^{\frac{1}{p}}
$$

- The $L_2$-distance is called the Euclidean distance, the $L_1$-distance the Manhattan distance, and the $L_\infty$-distance the Chebyshev distance.
  - Compute the Euclidean, Manhattan, and Chebyshev distances between $\mathbf{x} = (1, -2)$ and $\mathbf{y} = (3, 1)$.

- The $L_1$-norm and $L_2$-norm are widely used as regularizers for deep neural networks.

---
layout: prism
heading: Covariance Matrices
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- To check how much the feature values of the feature vectors in our dataset differ from one another, we compute the [covariance]{.hl} of the features.
  - We could compute the standard deviation of the feature values, but the standard deviation tells us how spread individual feature values are around the mean; when there are several features, covariance must be used.

- Let the rows of a matrix $\mathbf{X}$ represent data samples and the columns represent different features. Then the entries of the covariance matrix $\mathbf{\Sigma}$ of $\mathbf{X}$ are defined as follows.

$$
\Sigma_{i,j} = \frac{1}{n-1} \sum_{k=0}^{n-1} (x_{k,i} - \bar{\mathbf{x}}_i)(x_{k,j} - \bar{\mathbf{x}}_j)
$$

- The covariance matrix reflects how spread out the values are.

---
layout: prism
heading: "DIY: Covariance Matrix"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

# rows = samples, columns = features
X = np.array([[2.0, 1.0], [4.0, 3.0], [6.0, 4.0], [8.0, 8.0]])
Xc = X - X.mean(axis=0)
n = len(X)
Sigma = (Xc.T @ Xc) / (n - 1)

print("covariance matrix :\n", Sigma)
print("matches np.cov    :", np.allclose(Sigma, np.cov(X, rowvar=False)))
```

</PyRunner>

---
layout: prism
heading: Mahalanobis Distance
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Using covariance, we can define the [Mahalanobis distance]{.hl} $D_M$.

$$
D_M = \sqrt{(\mathbf{x} - \mathbf{y})^\top \mathbf{\Sigma}^{-1} (\mathbf{x} - \mathbf{y})}
$$

- The computation itself is complex, but its meaning is a distance on a probability distribution, expressing how many variances away from the mean a value lies.
  - Suppose a cafe called Suharu receives on average $300$ customers on Wednesday mornings, with a standard deviation of $30$ (variance $900$).
    - So, barring anything unusual, the Wednesday-morning customer count is between $270$ and $330$.
  - If $360$ customers visited today, we can regard it as an unusually busy day.
  - The Mahalanobis distance quantifies how unlikely such an event is.
    - In this case, the difference from the mean divided by the standard deviation ($60/30 = 2$) is the Mahalanobis distance.

- The Mahalanobis distance is a tool used in various machine learning algorithms to analyze the characteristics of data.

---
layout: prism
heading: Kullback-Leibler Divergence
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The [Kullback-Leibler divergence]{.hl} (KL divergence) is a measure of the distance between two probability distributions, sometimes also expressed as the relative entropy.

- The KL divergence of two discrete distributions $P$ and $Q$ is defined as follows.

$$
D_{\mathrm{KL}}(P \,\|\, Q) = \sum_x P(x) \log\left( \frac{P(x)}{Q(x)} \right)
$$

  - Using the binary (base-$2$) logarithm gives units of bits, while using the natural logarithm ($\ln$) gives units of nats.
  - The KL divergence is not symmetric, but that does not mean it cannot be used as a distance function.

---
layout: prism
heading: "DIY: Kullback-Leibler Divergence"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

P = np.array([0.5, 0.3, 0.2])
Q = np.array([0.4, 0.4, 0.2])

kl_pq = np.sum(P * np.log2(P / Q))   # in bits
kl_qp = np.sum(Q * np.log2(Q / P))

print("D_KL(P||Q) :", round(kl_pq, 4), "bits")
print("D_KL(Q||P) :", round(kl_qp, 4), "bits")
print("asymmetric :", not np.isclose(kl_pq, kl_qp))
print("D_KL(P||P) :", round(np.sum(P * np.log2(P / P)), 4))
```

</PyRunner>

---
layout: prism
heading: Principal Component Analysis (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- For a matrix $\mathbf{X}$ representing a dataset, if each data sample is a point in $n$-dimensional space (i.e., the feature vector has dimension $n$), the observations form a set of points in $n$-dimensional space.

- [Principal component analysis (PCA)]{.hl} is an algorithm for identifying the main direction in which data is scattered.
  - The direction along which the data is most spread out, i.e., the axis of greatest variance, is called the principal component.

- PCA first finds the principal component, then finds the remaining components in decreasing order of spread; each component obtained is orthogonal to the others.

- PCA is mainly used for the dimensionality reduction of data.

---
layout: prism
heading: Principal Component Analysis (2/2)
---

<div style="height: 0.5rem;"></div>

- The PCA algorithm is as follows.

<div class="sub-item-enum">

1. Center the dataset so that its mean is $0$.
2. Compute the covariance matrix of the dataset.
3. Compute the eigenvalues and eigenvectors of the covariance matrix.
4. Sort the eigenvalues in descending order of absolute value.
5. Discard the weak (small) eigenvalues and eigenvectors (this step is optional).
6. Build a transformation matrix from the remaining eigenvectors.
7. Apply the transformation matrix to the original dataset to obtain a new dataset.

</div>

---
layout: prism
heading: "DIY: PCA"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
import numpy as np

# small 2-D dataset (rows = samples)
X = np.array([[2.0, 0.0], [3.0, 1.0], [4.0, 3.0], [5.0, 4.0], [6.0, 6.0]])

Xc = X - X.mean(axis=0)                 # 1) center
Sigma = np.cov(Xc, rowvar=False)        # 2) covariance
vals, vecs = np.linalg.eig(Sigma)       # 3) eigen-decomposition
order = np.argsort(np.abs(vals))[::-1]  # 4) sort by |eigenvalue|
vals, vecs = vals[order], vecs[:, order]

print("eigenvalues (variance per axis):", np.round(vals, 4))
pc1 = vecs[:, 0]
print("principal component :", np.round(pc1, 4))
print("projection onto PC1 :", np.round(Xc @ pc1, 4))
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
