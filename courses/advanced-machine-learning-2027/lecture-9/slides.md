---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 9
download: true
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-9-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 09: Graphical Models</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">Kernel Methods</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">Midterm Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">Midterm Exam</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span class="text-gray-900 dark:text-gray-100">Graphical Models</span></p>
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
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Bayesian Network</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Conditional Independence</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Markov Random Field</span></p>
</div>
</div>

---
layout: prism
heading: Bayesian Network (1/4)
---

<style>
.slidev-layout ul > li { margin-top: 2.8em; }
</style>

- We can exploit [probabilistic graphical models; PGMs]{.hl} which represent probability distributions semantically.

<div class="sub-item">

PGMs visualize a model, reveal its properties such as conditional independence, and express complex computations for training and inference as graph operations.

</div>

- A [graph]{.hl} is composed of [nodes]{.hl} (a.k.a. vertices) and [links]{.hl} (a.k.a. edges or arcs).

- Each node denotes a random variable and a link denotes a probabilistic relationship between the variables.

---
layout: prism
heading: Bayesian Network (2/4)
---

<style>
.slidev-layout ul > li { margin-top: 1.2em; }
</style>

- A [Bayesian network]{.hl}, a.k.a. a [directed graphical model]{.hl}, is a graph whose links have directionality (represented by arrows).

- Consider a joint distribution of three variables factored by the product rule:

$$
p(a,b,c)=p(c|a,b)p(a,b)=p(c|a,b)p(b|a)p(a)
$$

- The right-hand side maps to a simple graph:

<div class="sub-item-enum">

1. Introduce one node for each of $a$, $b$, $c$.
2. Relate each node to its conditional distribution.
3. Add a directed link for each conditional (e.g. $p(c|a,b)$ draws $a\to c$ and $b\to c$; then $c$ is a [child]{.hl} of its [parents]{.hl} $a$, $b$).

</div>

---
layout: prism
heading: Bayesian Network (3/4)
---

<div style="display:grid; grid-template-columns: 1.9fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2em; }
</style>

- A generalized factorization for $K$ variables:

$$
p(x_1,\ldots,x_K)=p(x_K|x_1,\ldots,x_{K-1})\cdots p(x_2|x_1)p(x_1)
$$

<div class="sub-item">

Each node is a conditional distribution with directed links from lower-indexed nodes. If every pair is connected, the graph is [fully connected]{.hl}.

</div>

- A graph may instead have [absent]{.hl} links (the graph on the right is not fully connected).

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.2.png" class="img-center" style="width: 12rem;" />
</div>
</div>

---
layout: prism
heading: Bayesian Network (4/4)
---

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- For a graph with $K$ nodes, we use the general factorization:

$$
p(\mathbf{x})=\prod_{k=1}^{K}p(x_k|\mathrm{pa}_k)
$$

<div class="sub-item">

$\mathrm{pa}_k$ denotes the parent nodes of $x_k$. If each conditional is normalized, the product is always normalized.

</div>

- We restrict ourselves to graphs with no [directed cycle]{.hl}, i.e., a [directed acyclic graph; DAG]{.hl}: following the links from any node never returns to that node.

---
layout: prism
heading: Polynomial Approximation (1/3)
---

<div style="display:grid; grid-template-columns: 1.9fr 1.1fr; gap: 2.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.0em; }
</style>

- A Bayesian polynomial regression model has random variables: the coefficients $\mathbf{w}$ and the targets $\boldsymbol{\mathsf{t}}=(t_1,\ldots,t_N)^\top$.

$$
p(\boldsymbol{\mathsf{t}},\mathbf{w})=p(\mathbf{w})\prod_{n=1}^{N}p(t_n|\mathbf{w})
$$

- Instead of drawing all of $t_1,\ldots,t_N$, we draw one representative node $t_n$ surrounded by a [plate]{.hl} labeled $N$.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.3.png" class="img-center" style="width: 15rem; margin-bottom: 4rem;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.4.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: Polynomial Approximation (2/3)
---

<div style="display:grid; grid-template-columns: 1.9fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.2em; }
</style>

- We can represent the deterministic parameters explicitly:

$$
p(\boldsymbol{\mathsf{t}}, \mathbf{w} | \boldsymbol{\mathsf{x}}, \alpha, \sigma^2)=p(\mathbf{w} | \alpha) \prod_{n=1}^N p(t_n | \mathbf{w}, x_n, \sigma^2)
$$

<div class="sub-item">

An open circle is a random variable; a small dot is a deterministic variable.

</div>

- Nodes for [observed variables]{.hl} (e.g. the targets) are shaded; unobserved variables such as $\mathbf{w}$ are [latent]{.hl} (hidden) variables.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.5.png" class="img-center" style="width: 15rem;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.6.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: Polynomial Approximation (3/3)
---

<div style="display:grid; grid-template-columns: 1.9fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.2em; }
</style>

- For an unseen input $\widehat{x}$, the joint over all random variables is:

$$
p(\widehat{t}, \boldsymbol{\mathsf{t}}, \mathbf{w} | \widehat{x}, \boldsymbol{\mathsf{x}}, \alpha, \sigma^2)=\Big[\prod_{n=1}^N p(t_n | x_n, \mathbf{w}, \sigma^2)\Big] p(\mathbf{w} | \alpha)\, p(\widehat{t} | \widehat{x}, \mathbf{w}, \sigma^2)
$$

- The predictive distribution follows from the sum rule (marginalizing $\mathbf{w}$):

$$
p(\widehat{t} | \widehat{x}, \boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}}, \alpha, \sigma^2) \propto \int p(\widehat{t}, \boldsymbol{\mathsf{t}}, \mathbf{w} | \widehat{x}, \boldsymbol{\mathsf{x}}, \alpha, \sigma^2)\, \mathrm{d}\mathbf{w}
$$

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.7.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: Discrete Variable (1/4)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- Graphical modeling is useful for showing how members of the exponential family connect; conjugate parent–child pairs have useful properties.

- A discrete variable $\mathbf{x}$ with $K$ states is written as:

$$
p(\mathbf{x} | \boldsymbol{\mu})=\prod_{k=1}^K \mu_k^{x_k}
$$

<div class="sub-item">

With the constraint $\sum_k\mu_k=1$, we need $K-1$ parameters. For $M$ variables, an arbitrary joint needs $K^M-1$ parameters.

</div>

---
layout: prism
heading: Discrete Variable (2/4)
---

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- Chaining the variables reduces the parameter count: a chain of $M$ nodes needs $K-1+(M-1)K(K-1)$ parameters, linear in $M$.

- We can [tie]{.hl} (share) parameters to reduce the count further, or add Dirichlet priors to make a Bayesian model.

<div class="img-row" style="max-width: 88%">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.10.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.11.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.12.png"/>
</div>

---
layout: prism
heading: Discrete Variable (3/4)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.2em; }
</style>

- Instead of a full conditional-probability table (exponential in $M$), a parameterized model keeps the count small.

- Using a logistic sigmoid on a linear combination of the parents:

$$
p(y=1 | x_1, \ldots, x_M)=\sigma\Big(w_0+\sum_{i=1}^M w_i x_i\Big)=\sigma(\mathbf{w}^{\top} \mathbf{x})
$$

<div class="sub-item">

The count grows linearly in $M$ rather than exponentially.

</div>

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.13.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: Discrete Variable (4/4)
---

<PyRunner>

```python
K = 3
print("Parameters vs. #variables M (K = 3 states):")
print(f"{'M':>3} | {'fully connected':>16} | {'chain':>8} | {'independent':>12}")
for M in [1, 2, 4, 6, 8]:
    full = K**M - 1                       # arbitrary joint
    chain = K-1 + (M-1)*K*(K-1)           # chain of nodes
    indep = M*(K-1)                       # fully factorized
    print(f"{M:>3} | {full:>16} | {chain:>8} | {indep:>12}")
print("\nOnly the fully connected graph explodes exponentially in M.")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bayesian Network</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Conditional Independence</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Markov Random Field</span></p>
</div>
</div>

---
layout: prism
heading: Conditional Independence
---

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- For three variables $a$, $b$, $c$, if $a$ is independent of $b$ given $c$:

$$
p(a|b,c)=p(a|c)
$$

- Equivalently, the joint over $a$, $b$ given $c$ factorizes:

$$
p(a,b|c)=p(a|b,c)p(b|c)=p(a|c)p(b|c)
$$

<div class="sub-item">

We denote this compactly as $a \perp\!\!\!\perp b \mid c$.

</div>

---
layout: prism
heading: Examples (1/3) — Tail-to-Tail
---

<div style="display:grid; grid-template-columns: 1.6fr 1.4fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- Node $c$ is a [tail-to-tail]{.hl} node: $p(a,b,c)=p(a|c)p(b|c)p(c)$.

- If $c$ is unobserved, marginalizing gives $p(a,b)=\sum_c p(a|c)p(b|c)p(c)$, which does not factorize, so $a\not\perp\!\!\!\perp b\mid\emptyset$.

- If $c$ is observed, $p(a,b|c)=p(a|c)p(b|c)$, so it [blocks]{.hl} the path and $a\perp\!\!\!\perp b\mid c$.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.15.png" class="img-center" style="width: 15rem;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.16.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: Examples (2/3) — Head-to-Tail
---

<div style="display:grid; grid-template-columns: 1.6fr 1.4fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- Node $c$ is a [head-to-tail]{.hl} node: $p(a,b,c)=p(a)p(c|a)p(b|c)$.

- If $c$ is unobserved, $p(a,b)=p(a)\sum_c p(c|a)p(b|c)=p(a)p(b|a)$, so $a\not\perp\!\!\!\perp b\mid\emptyset$.

- If $c$ is observed, $p(a,b|c)=\dfrac{p(a)p(c|a)p(b|c)}{p(c)}=p(a|c)p(b|c)$, so $a\perp\!\!\!\perp b\mid c$.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.17.png" class="img-center" style="width: 15rem; margin-bottom: 6rem" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.18.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: Examples (3/3) — Head-to-Head
---

<div style="display:grid; grid-template-columns: 1.6fr 1.4fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- Node $c$ is a [head-to-head]{.hl} node: $p(a,b,c)=p(a)p(b)p(c|a,b)$.

- If $c$ is unobserved, $p(a,b)=p(a)p(b)$, so $a\perp\!\!\!\perp b\mid\emptyset$.

- If $c$ (or a descendant) is observed, $p(a,b|c)\neq p(a|c)p(b|c)$ in general, so $a\not\perp\!\!\!\perp b\mid c$ ([explaining away]{.hl}).

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.19.png" class="img-center" style="width: 12rem; margin-bottom: 4rem" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.20.png" class="img-center" style="width: 12rem;" />
</div>
</div>

---
layout: prism
heading: D-Separation
---

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- For disjoint node sets $A$, $B$, $C$ in a DAG, to test $A\perp\!\!\!\perp B\mid C$ we consider every path from $A$ to $B$.

- A path is [blocked]{.hl} if it contains a node such that either:

<div class="sub-item-enum">

1. the arrows meet head-to-tail or tail-to-tail at the node and it is in $C$, or
2. the arrows meet head-to-head at the node and neither it nor any descendant is in $C$.

</div>

- If all paths are blocked, $A$ is d-separated from $B$ given $C$, hence $A\perp\!\!\!\perp B\mid C$.

---
layout: prism
heading: Conditional Independence Again
---

<PyRunner>

```python
import numpy as np
# head-to-head: a, b independent causes; c a common effect (explaining away)
pa = np.array([0.5, 0.5]); pb = np.array([0.5, 0.5])
pc1 = np.array([[0.1, 0.8], [0.8, 0.95]])           # p(c=1 | a, b)
joint = np.zeros((2, 2, 2))
for a in range(2):
    for b in range(2):
        joint[a, b, 1] = pa[a]*pb[b]*pc1[a, b]
        joint[a, b, 0] = pa[a]*pb[b]*(1-pc1[a, b])
def corr_ab(P):
    P = P/P.sum(); Ea = P.sum(1)[1]; Eb = P.sum(0)[1]; Eab = P[1, 1]
    return (Eab - Ea*Eb)/np.sqrt(Ea*(1-Ea)*Eb*(1-Eb))
print("unconditional corr(a,b)   =", f"{corr_ab(joint.sum(2)):+.3f}  (~0, independent)")
print("corr(a,b | c=1)           =", f"{corr_ab(joint[:,:,1]):+.3f}  (explaining away)")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bayesian Network</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Conditional Independence</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Markov Random Field</span></p>
</div>
</div>

---
layout: prism
heading: Markov Random Field
---

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- A [Markov network]{.hl}, a.k.a. [undirected graphical model]{.hl} or [Markov random field]{.hl}, has nodes and links.

- Its links have no directionality, so we do not use arrows.

- Conditional independence is simpler here: $A\perp\!\!\!\perp B\mid C$ holds whenever every path from $A$ to $B$ passes through at least one node in $C$.

---
layout: prism
heading: Conditional Independence Property
---

<div style="display:grid; grid-template-columns: 1.5fr 1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- In a directed graph, d-separation tests whether paths are blocked; head-to-head nodes make blocking subtle.

- Removing directionality erases the parent–child asymmetry, giving an undirected model.

- To check $A\perp\!\!\!\perp B\mid C$, examine every path between $A$ and $B$: if all pass through $C$, the property holds.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.27.png" class="img-center" style="width: 18rem;" />
</div>
</div>

---
layout: prism
heading: Inference in Graphical Model (1/2)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- In graphical models, we [infer]{.hl} the posterior of one or more nodes given some observed nodes, expressed as [message passing]{.hl}.

- For a joint $p(x,y)=p(x)p(y|x)$ where $y$ is observed, the marginal $p(x)$ is the prior for the hidden variable $x$, and we infer its posterior via Bayes' theorem.

- On an undirected chain, the marginal $p(x_n)=\dfrac{1}{Z}\mu_\alpha(x_n)\mu_\beta(x_n)$ is a product of a forward and a backward message, computed recursively in $O(N)$.

---
layout: prism
heading: Inference in Graphical Model (2/2)
---

<PyRunner>

```python
import numpy as np, itertools
rng = np.random.default_rng(1)
N, K = 5, 3
psi = [rng.uniform(0.2, 1.8, (K, K)) for _ in range(N-1)]      # chain potentials
# brute force: enumerate the full joint
marg = np.zeros((N, K)); Z = 0.0
for x in itertools.product(range(K), repeat=N):
    p = 1.0
    for i in range(N-1): p *= psi[i][x[i], x[i+1]]
    Z += p
    for i in range(N): marg[i, x[i]] += p
marg /= Z
# forward / backward message passing at node 2
node = 2
mu_a = np.ones(K)
for i in range(node): mu_a = mu_a @ psi[i]
mu_b = np.ones(K)
for i in range(N-1, node, -1): mu_b = psi[i-1] @ mu_b
p_msg = mu_a*mu_b; p_msg /= p_msg.sum()
print("marginal p(x2) brute force :", np.round(marg[node], 4).tolist())
print("marginal p(x2) messages    :", np.round(p_msg, 4).tolist())
print("max error                  :", f"{np.abs(marg[node]-p_msg).max():.1e}")
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
