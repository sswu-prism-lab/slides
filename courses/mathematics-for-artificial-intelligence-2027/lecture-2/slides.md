---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 2
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 02: Numbers, Operations, and Systems</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span class="text-gray-900 dark:text-gray-100">Numbers, Operations, and Systems</span></p>
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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Matrix Calculus</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Data Flow in Neural Networks</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Numbers, Operations, and Systems
---



- Beyond the natural numbers and real numbers we are familiar with, we can represent natural phenomena through many other systems such as imaginary numbers, sets, and matrices, and we can operate on them in a variety of ways, just as we do with the four basic arithmetic operations.

- Understanding diverse number systems and ways of operating on them is a foundational concept needed across engineering in general, including artificial intelligence.
  - Representing signals with complex numbers, representing and operating on data with sets, and so on.

- Today, we will cover the following:
  - Various operations that apply to number systems
  - Basic concepts of sets and sequences, and some special sets and sequences
  - The meaning and representation of complex numbers

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Numbers and Operations</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Base-n Notation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Exponents and Logarithms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Summation and Product</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Sets and Sequences</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Complex Numbers</span></p>
  </div>

</div>

---
layout: prism
heading: Base-n Notation
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [Base-$n$ notation]{.hl} is a counting method in which the place value carries over at units of $n$.
  - The system we commonly use is base-$10$, while computers mainly use base-$2$ (binary) and base-$16$ (hexadecimal).

- For any natural number $a$ and $n \geq 2$, we can always uniquely find an ordered tuple of integers $(a_k, a_{k-1}, \ldots, a_1, a_0)$ satisfying

$$
a = a_k n^k + a_{k-1} n^{k-1} + \cdots + a_1 n + a_0,\quad 0 \leq a_0, a_1, \ldots, a_k < n,\ a_k \neq 0.
$$

- We then write $a = \overline{a_k a_{k-1} \cdots a_1 a_0}_{(n)}$ and say $a$ is expressed in base $n$.
  - By convention, the subscript is omitted for base $10$.

- Rational, irrational, and even complex bases can also be used.

---
layout: prism
heading: "DIY: Converting Between Bases"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
# Convert a base-10 integer into an arbitrary base n (2 <= n <= 16),
# and convert it back to verify.
digits = "0123456789ABCDEF"

def to_base(a, n):
    if a == 0:
        return "0"
    out = ""
    while a > 0:
        out = digits[a % n] + out
        a //= n
    return out

def from_base(s, n):
    return sum(digits.index(c) * n**i for i, c in enumerate(reversed(s)))

for a, n in [(2024, 2), (2024, 16), (255, 2), (255, 16)]:
    rep = to_base(a, n)
    print(f"{a:>5} (base 10) = {rep:>12} (base {n:>2})  ->  back: {from_base(rep, n)}")
```

</PyRunner>

---
layout: prism
heading: Exponents
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- Below are various properties that [exponents]{.hl} satisfy.

$$
\begin{gather*}
X^A X^B = X^{A+B}\\
\frac{X^A}{X^B} = X^{A-B}\\
(X^A)^B = X^{AB}\\
X^N + X^N = 2X^N \neq X^{2N}\\
2^N + 2^N = 2^{N+1}
\end{gather*}
$$

---
layout: prism
heading: Logarithms
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- The [logarithm]{.hl} follows the definition below.
  - In computer science, unless otherwise defined, the base of the logarithm is set to $2$.
  - In the natural sciences and engineering, $e$ is used; in economics and everyday life, $10$ is common.

<div class="theorem-box">
<div class="theorem-box-title">Definition of the logarithm</div>
<div class="theorem-box-body">

$X^A = B$ _if and only if_ $\log_X B = A$.

</div>
</div>

- From the definition, several properties of the logarithm follow:

$$
\begin{gather*}
\log_A B = \log_C B / \log_C A,\ \forall A, B, C > 0,\ A \neq 1 \qquad \log AB = \log A + \log B\\
\log A/B = \log A - \log B \qquad \log(A^B) = B \log A \qquad \log X < X,\ \forall X > 0
\end{gather*}
$$

---
layout: prism
heading: "DIY: Logarithm Properties"
---

<div style="height: 0.6rem;"></div>

<PyRunner>

```python
import numpy as np

A, B, C = 7.0, 12.0, 2.0

# Change of base: log_A(B) = log_C(B) / log_C(A)
lhs = np.log(B) / np.log(A)          # log_A(B) via natural logs
rhs = (np.log(B) / np.log(C)) / (np.log(A) / np.log(C))
print("change of base :", np.isclose(lhs, rhs))

# Product / power rules (base-2, as in computer science)
print("log2(AB)=log2 A+log2 B :", np.isclose(np.log2(A * B), np.log2(A) + np.log2(B)))
print("log2(A^B)=B log2 A     :", np.isclose(np.log2(A ** B), B * np.log2(A)))
print("log2(1024)             :", np.log2(1024))
```

</PyRunner>

---
layout: prism
heading: Summation
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- The operator $\sum$ is defined as follows:

$$
\sum_{k=i}^{j} a_k = a_i + a_{i+1} + a_{i+2} + \cdots + a_j
$$

- The $\sum$ operator has the following properties:

$$
\sum_{k=1}^{n} (a_k \pm b_k) = \sum_{k=1}^{n} a_k \pm \sum_{k=1}^{n} b_k \qquad
\sum_{k=1}^{n} c\, a_k = c \sum_{k=1}^{n} a_k \qquad
\sum_{k=1}^{n} c = cn
$$

---
layout: prism
heading: Product
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The operator $\prod$ is defined as follows:

$$
\prod_{k=i}^{j} a_k = a_i\, a_{i+1}\, a_{i+2} \cdots a_j
$$

<PyRunner>

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
c = 3

print("sum linearity  :", np.isclose((c * a).sum(), c * a.sum()))
print("prod of c*a    :", np.prod(c * a), "= c^n * prod(a) =", c**len(a) * np.prod(a))
print("prod(a) = 5!   :", np.prod(a))
```

</PyRunner>

- [DIY]{.hl} Explore the various properties of the product operator.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Numbers and Operations</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Sets and Sequences</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Sets</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Special Sets</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Sequences and Series</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Complex Numbers</span></p>
  </div>

</div>

---
layout: prism
heading: Sets, Elements, and Subsets
---


- If an [element]{.hl} $a$ belongs to a [set]{.hl} $A$, we write $a \in A$; otherwise, $a \notin A$.
  - _Collection_, _aggregate_, and _family_ are all synonyms for a set; _object_ is a synonym for an element.

- $\{x : \cdots\}$ denotes the set of all elements $x$ satisfying the condition $\cdots$.

- A set with no elements is called the [empty set]{.hl}, written $\emptyset$.

- If every element of $A$ is also an element of $B$, then $A$ is a [subset]{.hl} of $B$, written $A \subset B$.
  - [DIY]{.hl} Redefine $A \subset B$ using a set-builder (conditional) expression.

---
layout: prism
heading: Power Sets and Index Sets
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The set of all subsets of a set $A$ is called the [power set]{.hl} of $A$, written $\mathcal{P}(A)$.
  - $X \in \mathcal{P}(A) \Rightarrow X \subset A$
  - Every subset of $A$ except $A$ itself is called a [proper subset]{.hl} of $A$.

- Given a set $A$ and a set $M_a$ for every element $a \in A$, the family $\{M_a : a \in A\}$ (also written $\{M_a\}_{a \in A}$) is said to be [indexed]{.hl} by $A$, and $A$ is called the [index set]{.hl}.

$$
\mathcal{L} = \{ L_a : a \in \mathbb{R} \}, \quad\text{where } L_a = \{ x \in \mathbb{R} : x < a \}
$$

<div class="sub-item">

For example, $\mathcal{L}$ above is indexed by the real numbers $\mathbb{R}$, and $\mathcal{A} = \{A_i : i = 1,2,3,4\}$ is indexed by $\{1,2,3,4\}$.

</div>

---
layout: prism
heading: Union and Intersection
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The [union]{.hl} $A \cup B$ is the set of all elements $x$ that belong to at least one of $A$ or $B$.
  - $A \cup B = \{ x : x \in A \text{ or } x \in B \}$

- The [intersection]{.hl} $A \cap B$ is the set of all elements $x$ that belong to both $A$ and $B$.
  - $A \cap B = \{ x : x \in A \text{ and } x \in B \}$

- If $A \cap B = \emptyset$, the sets $A$ and $B$ are [disjoint]{.hl}.

- For any sets $A$, $B$, $C$, the [distributive laws]{.hl} hold:

<div class="sub-item-enum">

1. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
2. $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$

</div>

---
layout: prism
heading: "DIY: Set Operations and the Distributive Law"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
A = {0, 1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}

print("A ∪ B      :", A | B)
print("A ∩ B      :", A & B)
print("B \\ A      :", B - A)
print("disjoint?  :", A.isdisjoint({7, 8}))

# Distributive law: A ∪ (B ∩ C) == (A ∪ B) ∩ (A ∪ C)
print("distributive:", (A | (B & C)) == ((A | B) & (A | C)))

# Power set of {0,1,2}
from itertools import combinations
S = [0, 1, 2]
power = [set(c) for r in range(len(S) + 1) for c in combinations(S, r)]
print("power set   :", power)
```

</PyRunner>

---
layout: prism
heading: Set Difference and Complement
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The [set difference]{.hl} $B \setminus A$ is the set of all elements of $B$ not contained in $A$.
  - $B \setminus A = \{ x : x \in B \text{ and } x \notin A \}$

- When $A \subset X$, the difference $X \setminus A$ is called the [complement]{.hl} of $A$ with respect to $X$.

<div class="theorem-box">
<div class="theorem-box-title">De Morgan's laws</div>
<div class="theorem-box-body">

If $A$ and $B$ are subsets of a set $X$, then

$$
X \setminus (A \cup B) = (X \setminus A) \cap (X \setminus B) \qquad
X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B)
$$

</div>
</div>

---
layout: prism
heading: Definitions via Indexing
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Let $\{A_i : i \in I\}$ be a family indexed by an index set $I$. The union of this family is defined as

$$
\bigcup_{i \in I} A_i = \{ x : \exists\, i \in I \text{ s.t. } x \in A_i \}.
$$

- Similarly, its intersection is defined as

$$
\bigcap_{i \in I} A_i = \{ x : \forall\, i \in I,\ x \in A_i \}.
$$

- The distributive laws and De Morgan's laws can be rewritten in the same manner:
  - $A \cap \bigcup_{i \in I} B_i = \bigcup_{i \in I} (A \cap B_i)$ and $A \cup \bigcap_{i \in I} B_i = \bigcap_{i \in I} (A \cup B_i)$
  - $X \setminus \left( \bigcup_{i \in I} A_i \right) = \bigcap_{i \in I} (X \setminus A_i)$ and $X \setminus \left( \bigcap_{i \in I} A_i \right) = \bigcup_{i \in I} (X \setminus A_i)$

---
layout: prism
heading: Number System Sets (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- The [natural numbers]{.hl} are the numbers $1, 2, 3, \ldots$.

- Their rigorous definition follows [Peano's axioms]{.hl}: a set $\mathbb{N}$ satisfying the following is called the set of natural numbers.

<div class="sub-item-enum">

1. $\mathbb{N}$ contains a special element called $1$.
2. For each $n \in \mathbb{N}$, its successor $n^+ \in \mathbb{N}$.
3. No element of $\mathbb{N}$ has $1$ as its successor.
4. If two elements of $\mathbb{N}$ have the same successor, they are equal.
5. If $S \subset \mathbb{N}$ with $1 \in S$, and $n^+ \in S$ whenever $n \in S$, then $S = \mathbb{N}$.

</div>

- Since it is inconvenient that the additive identity $0$ is missing, modern mathematics often uses the [whole numbers]{.hl} $\mathbb{N}_0 = \mathbb{N} \cup \{0\}$.

- The [integers]{.hl} are defined as $\mathbb{Z} = \{ x : n + x = 0,\ \forall n \in \mathbb{N}_0 \}$.

---
layout: prism
heading: Number System Sets (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- The [rational numbers]{.hl} are defined as

$$
\mathbb{Q} = \left\{ x : x = \frac{m}{n},\ \forall m, n \in \mathbb{Z},\ n \neq 0 \right\}.
$$

- The [irrational numbers]{.hl} $\mathbb{I}$ are numbers that cannot be expressed as a ratio of two integers, and the [real numbers]{.hl} $\mathbb{R}$ are the rationals and irrationals together.

- With the [imaginary unit]{.hl} $i \equiv \sqrt{-1}$, the [complex numbers]{.hl} are defined as

$$
\mathbb{C} = \{ a + bi : \forall a, b \in \mathbb{R},\ i = \sqrt{-1} \}.
$$

---
layout: prism
heading: Convex Sets
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A set $A$ satisfying the following property is called a [convex set]{.hl}.
  - $tx + (1-t)y \in A,\ \forall x, y \in A,\ t \in [0, 1]$
    - For any two points in $A$, every point on the line segment joining them also lies in $A$.

- The intersection of convex sets is convex, and translating a convex set or taking positive linear combinations preserves convexity.

- Convex sets carry important meaning in machine learning:
  - When the objective and constraints of an optimization problem are convex, the solution is easier to find; finding the decision boundary of a [support vector machine]{.hl} is a convex optimization problem.
  - If the loss function of a [neural network]{.hl} is convex, training proceeds more stably.

---
layout: prism
heading: "DIY: Testing Convexity"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)

# A disk of radius 1 is convex; a ring (annulus) is not.
def in_disk(p):  return p[0]**2 + p[1]**2 <= 1.0
def in_ring(p):  return 0.5 <= p[0]**2 + p[1]**2 <= 1.0

def convex_test(membership, n=20000):
    ok = 0
    for _ in range(n):
        x, y = rng.uniform(-1, 1, 2), rng.uniform(-1, 1, 2)
        if membership(x) and membership(y):
            t = rng.random()
            if membership(t * x + (1 - t) * y):
                ok += 1
            else:
                return False   # found two points whose segment leaves the set
    return True

print("disk is convex :", convex_test(in_disk))
print("ring is convex :", convex_test(in_ring))
```

</PyRunner>

---
layout: prism
heading: Definition of a Sequence
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [sequence]{.hl} is a _function_ whose domain is $\mathbb{N}$ (or the set of naturals up to some $N$); writing the $n$-th term as $x_n$, we denote it $\{x_n\}_{n=1}^{\infty}$ or $\{x_n\}_{n=1}^{N}$.

- An [arithmetic sequence]{.hl} has a constant difference between consecutive terms; with common difference $d$, the general term is $a_n = a + (n-1)d$.

- A [geometric sequence]{.hl} has a constant ratio between consecutive terms; with common ratio $r$, the general term is $a_n = a r^{n-1}$.

- A sequence whose reciprocals form an arithmetic sequence is a [harmonic sequence]{.hl}; its general term is $a_n = \dfrac{a}{1 + a(n-1)d}$.

- The sequence of differences (each term minus the previous) is called the [difference sequence]{.hl}.

---
layout: prism
heading: The Fibonacci Sequence
---

<style>
.slidev-layout ul > li {
  margin-top: 3.4em;
}
</style>

- The [Fibonacci sequence]{.hl}, which describes many phenomena in nature, is defined by the recurrence

$$
F_1 = 1,\quad F_2 = 1,\quad F_{n+2} = F_{n+1} + F_n.
$$

- Its closed-form general term is

$$
F_n = \frac{1}{\sqrt{5}} \left[ \left( \frac{1 + \sqrt{5}}{2} \right)^n - \left( \frac{1 - \sqrt{5}}{2} \right)^n \right].
$$

- [DIY]{.hl} Show that two consecutive terms of the Fibonacci sequence are always coprime.

---
layout: prism
heading: "DIY: Calculate The Fibonacci Sequence"
---

<PyRunner>

```python
import numpy as np

# Recurrence vs. the closed-form (Binet) formula
phi, psi = (1 + 5**0.5) / 2, (1 - 5**0.5) / 2
F = [0, 1]
for _ in range(18):
    F.append(F[-1] + F[-2])

print(f"{'n':>3} | {'recurrence':>10} | {'closed form':>12}")
for n in range(1, 13):
    binet = (phi**n - psi**n) / 5**0.5
    print(f"{n:>3} | {F[n]:>10} | {binet:>12.4f}")

# Consecutive Fibonacci numbers are coprime
from math import gcd
print("all coprime:", all(gcd(F[n], F[n+1]) == 1 for n in range(1, 18)))
```

</PyRunner>

---
layout: prism
heading: Definition of a Series
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Given the partial sum $S_n = a_1 + a_2 + \cdots + a_n$ of a sequence $\{a_n\}$, the [series]{.hl} is defined as the _limit_

$$
\lim_{n \to \infty} S_n = \lim_{n \to \infty} \sum_{k=1}^{n} a_k.
$$

- If the limit $S$ converges to a real number, the series [converges]{.hl}; otherwise, it [diverges]{.hl}.

- A series is the limit of partial sums, which is a different concept from "adding infinitely many times."
  - This can be understood through the [Riemann series theorem]{.hl}.

$$
\frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots
$$

---
layout: prism
heading: "DIY: The Leibniz Series for π"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# Leibniz: pi/4 = sum_{n=0}^inf (-1)^n / (2n+1)
def leibniz(N):
    n = np.arange(N)
    return 4.0 * np.sum((-1.0)**n / (2*n + 1))

print(f"{'terms':>8} | {'estimate':>12} | {'|error|':>10}")
for N in [10, 100, 1000, 100000]:
    est = leibniz(N)
    print(f"{N:>8} | {est:>12.6f} | {abs(est - np.pi):>10.6f}")

print(f"\ntrue pi = {np.pi:.6f}  (convergence is famously slow!)")
```

</PyRunner>

---
layout: prism
heading: Fourier Series
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Expressing an _arbitrary_ function as a linear combination of [trigonometric]{.hl} and [exponential]{.hl} functions is called [Fourier analysis]{.hl}.

- A function of period $T$ can be expanded as a sum of trigonometric functions, called the [Fourier series]{.hl}:

$$
f(x) = \sum_{n=1}^{\infty} a_n \sin(n \omega x) + \sum_{n=1}^{\infty} b_n \cos(n \omega x) + b_0,\quad \omega = \frac{2\pi}{T}.
$$

- The [Fourier coefficients]{.hl} are defined as

$$
a_n = \frac{2}{T} \int_{x_0}^{x_0+T} f(x) \sin(n \omega x)\, \mathrm{d}x, \quad
b_n = \frac{2}{T} \int_{x_0}^{x_0+T} f(x) \cos(n \omega x)\, \mathrm{d}x.
$$

---
layout: prism
heading: "DIY: Building a Square Wave from Sines"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# A square wave equals the Fourier sum of odd harmonics:
#   f(x) = (4/pi) * sum_{k=1,3,5,...} sin(k x) / k
x = np.linspace(0, 2 * np.pi, 8)     # sample a few points
target = np.sign(np.sin(x))          # ideal square wave

for n_harm in [1, 3, 9, 49]:
    ks = np.arange(1, 2 * n_harm, 2)                 # 1, 3, 5, ...
    approx = (4 / np.pi) * sum(np.sin(k * x) / k for k in ks)
    err = np.mean(np.abs(approx - target))
    print(f"{len(ks):>2} harmonics -> mean |error| = {err:.4f}")
```

</PyRunner>

---
layout: prism
heading: Power Series
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A power series is an infinite series built from powers of a variable, used to represent or approximate functions and sequences.

- For variables $x_1, x_2, \ldots, x_n$, the [power series]{.hl} at $(x_1', x_2', \ldots, x_n')$ is

$$
\sum_{(k_1, \ldots, k_n) \in \mathbb{N}^n} a_{k_1, \ldots, k_n} \prod_{i=1}^{n} (x_i - x_i')^{k_i}.
$$

- [DIY]{.hl} For an arithmetic sequence $\{a_n\}$ and a geometric sequence $\{b_n\}$, consider the term-wise product $c_n = a_n b_n$ and compute the "arithmetico-geometric" series $S_n = \sum_{k=1}^{n} c_k$.

---
layout: prism
heading: Taylor Series (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- The [Taylor series]{.hl} (or Taylor expansion) represents an arbitrary function $f(x)$ as an infinite sum of polynomials around a point $a$.

- It approximates the function value using all derivatives at that point:

$$
f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots
$$

- The special case $a = 0$ is called the [Maclaurin series]{.hl}:

$$
f(x) \approx f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots
$$

---
layout: prism
heading: Taylor Series (2/2)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The higher the expansion order (the more terms), the closer the approximation matches the target function.
  - [DIY]{.hl} Expand the Maclaurin series of $\sin x$.

- Taylor and Maclaurin series greatly simplify function evaluation, so they are widely used across engineering, e.g., signal processing.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W02_taylor.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Calcuate Taylor Series"
---

<PyRunner>

```python
import numpy as np
from math import factorial

# Maclaurin series of sin(x): sum (-1)^k x^(2k+1)/(2k+1)!
def sin_taylor(x, order):
    return sum((-1)**k * x**(2*k+1) / factorial(2*k+1) for k in range((order+1)//2 + 1))

x = 1.0
for order in [1, 3, 5, 7]:
    print(f"order {order}: {sin_taylor(x, order):.6f}   (true sin 1 = {np.sin(x):.6f})")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Numbers and Operations</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Sets and Sequences</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Complex Numbers</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Definition and Conjugate</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Operations</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Matrix Representation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Polar Form</span></p>
  </div>

</div>

---
layout: prism
heading: Complex Numbers
---

<style>
.slidev-layout ul > li {
  margin-top: 2.6em;
}
</style>

- In science and engineering, we often need to treat expressions made of several composite units as a single number. Such a number, written not as a single value like $1$, $2$, $3$ but as $a + bi$, is a [complex number]{.hl}.

- Complex numbers were devised precisely to express solutions in spaces where representing them with a single ordinary number is impossible.

- For all $a, b \in \mathbb{R}$, a complex number is written $a + bi$ with $i \equiv \sqrt{-1}$; we call $\mathfrak{R}(a+bi) = a$ the [real part]{.hl} and $\mathfrak{I}(a+bi) = b$ the [imaginary part]{.hl}.

---
layout: prism
heading: The Complex Conjugate
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- For $z = a + bi \in \mathbb{C}$, the [complex conjugate]{.hl} $\bar{z}$ is defined as

$$
\bar{z} \equiv \mathfrak{R}(z) - i\,\mathfrak{I}(z) = a - bi.
$$

- The [absolute value]{.hl} (modulus) $|z|$ is defined as

$$
|z| = \sqrt{z \bar{z}} = \sqrt{\mathfrak{R}(z)^2 + \mathfrak{I}(z)^2} = \sqrt{a^2 + b^2}.
$$

- [DIY]{.hl} Plot $z = -1 + i$ and $\bar{z}$ on the complex plane, and interpret $|z|$ geometrically.
- [DIY]{.hl} Solve $z^2 + 2z + 5 = 0$ and check whether the roots are complex conjugates of each other.

---
layout: prism
heading: Operations on Complex Numbers
---

- For two complex numbers $a + bi$ and $c + di$, addition is defined as

$$
(a + bi) + (c + di) = (a + c) + (b + d)i.
$$

- Multiplication is defined as

$$
(a + bi)(c + di) = (ac - bd) + (ad + bc)i.
$$

<div class="sub-item">

Both addition and multiplication of complex numbers satisfy associativity and commutativity, and identities and inverses always exist.

</div>

- [DIY]{.hl} Compute the inverse of a complex number and check whether division can be defined.

<PyRunner>

```python
z1 = complex(2, 3)   # 2 + 3i
z2 = complex(1, -1)  # 1 - i

print("z1 + z2 :", z1 + z2)
print("z1 * z2 :", z1 * z2, " = (ac-bd)+(ad+bc)i =", complex(2*1 - 3*(-1), 2*(-1) + 3*1))
print("conj z1 :", z1.conjugate(), " |z1| =", abs(z1))
print("1 / z1  :", 1 / z1, " -> z1 * (1/z1) =", z1 * (1 / z1))
```

</PyRunner>

---
layout: prism
heading: Matrix Representation (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.4em;
}
</style>

- Complex numbers can also be represented well using the [matrix representation]{.hl} of [linear algebra]{.hl}:

$$
z = a + bi = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}.
$$

- For $z_1 = a + bi$ and $z_2 = c + di$, their sum and product become

$$
z_1 + z_2 = \begin{pmatrix} a+c & -(b+d) \\ b+d & a+c \end{pmatrix}, \quad
z_1 z_2 = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}\begin{pmatrix} c & -d \\ d & c \end{pmatrix} = \begin{pmatrix} ac-bd & -(ad+bc) \\ ad+bc & ac-bd \end{pmatrix}.
$$

---
layout: prism
heading: Matrix Representation (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Representing the imaginary unit $i$ as a matrix gives $i = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, and raising it to successive powers yields

$$
i^n = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}^n =
\begin{cases}
\ \ 1 & \text{if } n \equiv 0 \\
\ \ i & \text{if } n \equiv 1 \\
-1 & \text{if } n \equiv 2 \\
-i & \text{if } n \equiv 3
\end{cases} \pmod 4
$$

<div class="sub-item">

This exactly reproduces the familiar cycle $i^0 = 1,\ i^1 = i,\ i^2 = -1,\ i^3 = -i,\ i^4 = 1, \ldots$

</div>

---
layout: prism
heading: Matrix Representation (3/3)
---

<div class="grid grid-cols-2 gap-1" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Operating in the same way on the [rotation matrix]{.hl} shows the deep link between $i$ and rotation by $\pi/2$:

$$
\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
$$

- Generalizing, we find

$$
i^n = \begin{pmatrix} \cos\frac{n\pi}{2} & -\sin\frac{n\pi}{2} \\ \sin\frac{n\pi}{2} & \cos\frac{n\pi}{2} \end{pmatrix}.
$$

</div>
<div>

<PyRunner>

```python
import numpy as np

def cx(a, b):        # complex a+bi as a matrix
    return np.array([[a, -b], [b, a]], float)

z1, z2 = cx(2, 3), cx(1, -1)
# matrix product == complex product?
prod = z1 @ z2
print("matrix product :\n", prod)
print("(ac-bd, ad+bc) :", (2*1-3*-1, 2*-1+3*1))

# i^n via matrix power equals rotation by n*pi/2
i = cx(0, 1)
for n in range(1, 5):
    R = np.linalg.matrix_power(i, n)
    th = n * np.pi / 2
    rot = np.array([
      [np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]
    ])
    print(f"i^{n}: matches rotation?" 
         "{np.allclose(R, rot)}")
```

</PyRunner>

</div>
</div>

---
layout: prism
heading: Polar Form
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The figure visualizes a complex number on the complex plane; this representation is called the [polar form]{.hl}.

- For $z = a + bi$ with argument $\theta$, the polar form is

$$
z = |z|(\cos\theta + i\sin\theta).
$$

- [DIY]{.hl} Given $a$ and $b$, compute the argument $\theta$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W02_polar.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

- In the same way, we obtain [Euler's formula]{.hl}: $\ e^{ix} \equiv \cos x + i\sin x$.
  - [DIY]{.hl} Substitute $x = \pi$ to obtain [Euler's identity]{.hl} $e^{i\pi} + 1 = 0$.

---
layout: prism
heading: "DIY: Estimate Euler's Identity"
---

<PyRunner>

```python
import numpy as np

for z in [complex(2, 1.5), complex(-1, 1)]:
    r, theta = abs(z), np.angle(z)
    print(f"z = {z}:  r = {r:.4f}, theta = {theta:.4f} rad")
    print("   polar reconstruct :", r * (np.cos(theta) + 1j*np.sin(theta)))

print("\nEuler's identity  e^(i*pi) + 1 =", np.exp(1j*np.pi) + 1)
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
