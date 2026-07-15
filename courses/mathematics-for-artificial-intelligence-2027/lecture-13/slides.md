---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 13
download: true
info: |
  ## Mathematics for Artificial Intelligence Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-13-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 13: Data Flow in Neural Networks</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Matrix Calculus</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span class="text-gray-900 dark:text-gray-100">Data Flow in Neural Networks</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Data Flow in Neural Networks
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- We trace the process by which an input vector or tensor is transformed into a final output as it passes through the network.
  - A neural network is a single function, a tool that maps the data it receives as input to a final output.

- Training a neural network is ultimately the process of reshaping the function's values so that it produces the appropriate output for the given input data.

- To find the optimal function, a backpropagation process that traverses the function's forward pass in reverse is required, and to find a good solution we use gradient descent based on derivative values.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Data Flow in Neural Networks</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Data Flow in the Perceptron</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Data Flow in Convolutional Neural Networks</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Backpropagation and Gradient Descent</span></p>
  </div>

</div>

---
layout: prism
heading: Data Flow in the Perceptron (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- In traditional neural networks and other classical linear machine-learning models, inputs are handled as vectors of numbers.

- Such an input vector is called a [feature vector]{.hl}, and when training a machine-learning model we use a dataset in which each of many feature vectors is assigned a label.
  - If one input datum is one vector, then having several input data is naturally represented as a matrix.

- Models such as the perceptron or the feedforward neural network store the weights between layers as matrices.
  - If layer $i$ has $n$ input nodes and layer $i-1$ has $m$ output nodes, the weight matrix $\mathbf{W}_i$ between the two layers is represented as an $n \times m$ matrix.

---
layout: prism
heading: "DIY: Weight Matrix and Layer Output"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)

# Layer i has n = 3 nodes; layer i-1 produces m = 4 outputs.
n, m = 3, 4
W = rng.standard_normal((n, m))       # weight matrix W_i is n x m
a_prev = rng.standard_normal((m, 1))  # outputs of layer i-1 (m x 1)

z = W @ a_prev                        # -> n x 1, one value per node of layer i
print("W shape        :", W.shape)
print("a_prev shape   :", a_prev.shape)
print("W @ a_prev     :", z.shape, "-> feeds the", n, "nodes of layer i")
```

</PyRunner>

---
layout: prism
heading: Data Flow in the Perceptron (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Multiplying the matrix $\mathbf{W}_i$ by the $m \times 1$ column vector of layer $i-1$'s outputs yields an $n \times 1$ matrix, which is fed into the $n$ nodes of layer $i$.

- The output of each node is computed as follows.
  - A node's output (its activation) applies a nonlinear activation function $\sigma$ to the result of multiplying the current weight matrix $\mathbf{W}_i$ by layer $i-1$'s output vector $\mathbf{a}_{i-1}$ and adding layer $i$'s bias term.

$$
\mathbf{a}_i = \sigma(\mathbf{W}_i \mathbf{a}_{i-1} + \mathbf{b}_i)
$$

- For the nonlinear activation, the ReLU function is generally used between layers, whereas sigmoid-type functions are generally used in the final decision layer.
  - Sigmoid-type functions map the final output to a value between $0$ and $1$.

---
layout: prism
heading: "DIY: Activation Functions"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

def relu(x):    return np.maximum(0.0, x)
def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

W = np.array([[0.2, -0.5], [0.1, 0.4]])
b = np.array([[0.1], [-0.2]])
a_prev = np.array([[1.0], [2.0]])

z = W @ a_prev + b
print("pre-activation z :", z.ravel())
print("ReLU (hidden)    :", relu(z).ravel())
print("sigmoid (output) :", np.round(sigmoid(z).ravel(), 4))
print("output in (0, 1) :", bool(np.all((sigmoid(z) > 0) & (sigmoid(z) < 1))))
```

</PyRunner>

---
layout: prism
heading: Data Flow in Convolutional Neural Networks (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Convolutional neural networks (CNNs) use convolutional layers to capture and exploit the spatial relationships present in data.

- CNNs are generally used to analyze image data represented as two-dimensional arrays.
  - A grayscale image is represented as a single matrix, while a color image is represented as a tensor of three stacked matrices (the three primary colors of light).

- An image tensor is generally represented in the form $\mathbb{R}^{H \times W \times C}$, where $H$, $W$, and $C$ denote the height, width, and number of channels of the image, respectively.
  - That is, a typical grayscale image has $C = 1$ and a color image has $C = 3$.

---
layout: prism
heading: "DIY: Image Tensor Shapes"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# grayscale image: C = 1 ; color image: C = 3
H, W = 4, 5
gray = np.zeros((H, W, 1))
color = np.zeros((H, W, 3))

print("grayscale H x W x C :", gray.shape, "-> C =", gray.shape[2])
print("color     H x W x C :", color.shape, "-> C =", color.shape[2])
print("stored values (gray):", gray.size)
print("stored values (color):", color.size)
```

</PyRunner>

---
layout: prism
heading: Data Flow in Convolutional Neural Networks (2/3)
---

- The convolution operation proceeds by sliding one function over another; the convolution $\star$ of functions $f$ and $g$ is defined as

$$
(f \star g)(t) \equiv \int_{-\infty}^{\infty} f(\tau)\, g(t - \tau)\, \mathrm{d}\tau
$$

- The convolution used in machine learning operates on a discrete domain, and integration is rarely actually performed.

- The set of values $g$ that slides over the input $f$ is called the [kernel]{.hl}.

- Performing a convolution reduces the output size.
  - To keep the output the same size as the input after a convolution, [zero padding]{.hl} is commonly used.
  - [DIY]{.hl} For the input $[2, 6, 15, 31, 56, 27, 15, 0, -11]$, compute the convolution with the kernel $[-1, 0, 1]$ both with and without zero padding.

---
layout: prism
heading: "DIY: 1D Convolution and Zero Padding"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

x = np.array([2, 6, 15, 31, 56, 27, 15, 0, -11])
k = np.array([-1, 0, 1])

# 'valid': no padding -> length len(x) - len(k) + 1
valid = np.array([x[i:i+3] @ k for i in range(len(x) - 2)])

# 'same': zero-pad one element on each side -> same length as the input
xp = np.concatenate(([0], x, [0]))
same = np.array([xp[i:i+3] @ k for i in range(len(xp) - 2)])

print("input          :", x)
print("valid (no pad) :", valid)
print("same  (0-pad)  :", same)
print("lengths        :", len(valid), "vs", len(same), "(input length", len(x), ")")
```

</PyRunner>

---
layout: prism
heading: Data Flow in Convolutional Neural Networks (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- The step size by which the convolution kernel moves is called the [stride]{.hl}, and two-dimensional convolution works in much the same way as the one-dimensional case.

- After a convolution, a [pooling]{.hl} operation is used to reduce the height and width dimensions of the tensor while preserving its channel dimension.
  - Pooling inevitably causes information loss, so it must be used appropriately and in suitable situations.

- Max pooling and average pooling are the most common, determining the output by taking the maximum or the average value within a predefined window.
  - A stride can also be defined for the pooling operation.

- At the end of a CNN, the tensor is [flattened]{.hl} into a vector, which is finally fed into a perceptron to make the decision.

---
layout: prism
heading: "DIY: Max and Average Pooling"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

img = np.array([[1, 3, 2, 4],
                [5, 6, 1, 2],
                [7, 8, 3, 0],
                [1, 2, 4, 9]], float)

# 2 x 2 pooling with stride 2
def pool(a, op):
    out = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            out[i, j] = op(a[2*i:2*i+2, 2*j:2*j+2])
    return out

print("max pooling:\n", pool(img, np.max))
print("avg pooling:\n", pool(img, np.mean))
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Data Flow in Neural Networks</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Backpropagation and Gradient Descent</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Backpropagation Computation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Basic Gradient Descent</span></p>
  </div>

</div>

---
layout: prism
heading: Backpropagation
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The [backpropagation]{.hl} algorithm is the de facto standard for training deep learning models.
  - Without backpropagation, training a neural network becomes very slow or, in the worst case, impossible.

- Neural network training is essentially an optimization problem that relies on a loss function.
  - The loss function expresses how well the network performs on the given input (the training data).
  - The loss function takes the network's weight and bias values as input and outputs a value related to performance.

- When training a network with backpropagation, we use gradient values to find the maximum of the performance the loss function encodes, that is, the minimum of the loss function.

---
layout: prism
heading: Backpropagation Computation (1/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- Consider a simple network that takes two values and outputs a single value.
  - It has a hidden layer with two nodes and an output layer with one node.

- The weights and biases are all scalars, and the hidden layer uses the sigmoid function below.

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

- No activation function is applied at the output node, and the squared-error loss below is used.

$$
L = \frac{1}{2}(y - a_2)^2
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W13_nn.svg" class="tikz-fig" style="width: 95%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Sigmoid and Its Derivative"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

def sigmoid(x):  return 1.0 / (1.0 + np.exp(-x))
def dsigmoid(x): return sigmoid(x) * (1.0 - sigmoid(x))

xs = np.array([-2.0, -0.5, 0.0, 0.5, 2.0])
h = 1e-6                                   # verify sigma'(x) = sigma(x)(1 - sigma(x))
fd = (sigmoid(xs + h) - sigmoid(xs - h)) / (2 * h)
print("sigmoid   :", np.round(sigmoid(xs), 4))
print("analytic' :", np.round(dsigmoid(xs), 6))
print("finite  ' :", np.round(fd, 6))
print("match     :", bool(np.allclose(dsigmoid(xs), fd)))
```

</PyRunner>

---
layout: prism
heading: Backpropagation Computation (2/3)
---

- The forward pass of this network is described as follows.

$$
\begin{aligned}
z_0 &= w_0 x_0 + w_2 x_1 + b_0\\
a_0 &= \sigma(z_0)\\
z_1 &= w_1 x_0 + w_3 x_1 + b_1\\
a_1 &= \sigma(z_1)\\
a_2 &= w_4 a_0 + w_5 a_1 + b_2
\end{aligned}
$$

- The loss can be written in terms of the weights and biases.
  - The parameters, the weights and biases combined, are bundled into a vector written $\boldsymbol{\theta}$.

$$
\begin{aligned}
L &= L(w_0, w_1, w_2, w_3, w_4, w_5, b_0, b_1, b_2; x_0, x_1, y)\\
  &= L(\boldsymbol{\theta}; \mathbf{x}, y)
\end{aligned}
$$

- To carry out backpropagation, we must compute the gradient $\nabla L(\boldsymbol{\theta}; \mathbf{x}, y)$ of this loss function.

---
layout: prism
heading: "DIY: Forward Pass"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

w = np.array([0.10, 0.20, 0.30, 0.40, 0.50, 0.60])   # w0..w5
b = np.array([0.10, -0.20, 0.05])                    # b0, b1, b2
x0, x1, y = 1.0, 2.0, 1.0

z0 = w[0]*x0 + w[2]*x1 + b[0]; a0 = sigmoid(z0)
z1 = w[1]*x0 + w[3]*x1 + b[1]; a1 = sigmoid(z1)
a2 = w[4]*a0 + w[5]*a1 + b[2]          # no activation at the output
L = 0.5 * (y - a2)**2                  # squared-error loss

print(f"a0 = {a0:.4f}, a1 = {a1:.4f}")
print(f"prediction a2 = {a2:.4f}, target y = {y}")
print(f"loss L = {L:.6f}")
```

</PyRunner>

---
layout: prism
heading: Backpropagation Computation (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- To compute the gradient, we first find the derivative of the sigmoid function.
  - [DIY]{.hl} Carry out the differentiation yourself.

$$
\frac{\mathrm{d}}{\mathrm{d}x}\sigma(x) = \sigma(x)\bigl(1 - \sigma(x)\bigr)
$$

- Based on this, we can compute $\dfrac{\partial L}{\partial w_i},\ i = 0, 1, \ldots, 5$ and $\dfrac{\partial L}{\partial b_j},\ j = 0, 1, 2$.
  - [DIY]{.hl} Carry out the partial differentiation yourself.

---
layout: prism
heading: "DIY: Backpropagation"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

def loss(p, x0=1.0, x1=2.0, y=1.0):
    w, b = p[:6], p[6:]
    a0 = sigmoid(w[0]*x0 + w[2]*x1 + b[0])
    a1 = sigmoid(w[1]*x0 + w[3]*x1 + b[1])
    a2 = w[4]*a0 + w[5]*a1 + b[2]
    return 0.5 * (y - a2)**2

p = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.1, -0.2, 0.05])
x0, x1, y = 1.0, 2.0, 1.0
w, b = p[:6], p[6:]
a0 = sigmoid(w[0]*x0 + w[2]*x1 + b[0]); a1 = sigmoid(w[1]*x0 + w[3]*x1 + b[1])
a2 = w[4]*a0 + w[5]*a1 + b[2]; d = -(y - a2)          # dL/da2 via the chain rule
g = np.array([d*w[4]*a0*(1-a0)*x0, d*w[5]*a1*(1-a1)*x0, d*w[4]*a0*(1-a0)*x1,
              d*w[5]*a1*(1-a1)*x1, d*a0, d*a1,
              d*w[4]*a0*(1-a0), d*w[5]*a1*(1-a1), d])
fd = np.array([(loss(p + e) - loss(p - e)) / 2e-6 for e in np.eye(9) * 1e-6])
print("max |analytic - finite diff| :", np.max(np.abs(g - fd)))
print("gradients match              :", bool(np.allclose(g, fd)))
```

</PyRunner>

---
layout: prism
heading: Basic Gradient Descent
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The basic gradient descent update rule, without mini-batches, is as follows.

$$
\begin{gather*}
\mathbf{W} \leftarrow \mathbf{W} - \eta\, \Delta \mathbf{W}\\
\mathbf{b} \leftarrow \mathbf{b} - \eta\, \Delta \mathbf{b}
\end{gather*}
$$

- Here $\Delta \mathbf{W}$ and $\Delta \mathbf{b}$ are the errors based on the partial derivatives of the weights and biases, and $\eta$ is the learning rate, which determines how far a single update moves toward the minimum.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W13_00.png" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Gradient Descent Steps"
---

<PyRunner>

```python
import numpy as np

def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

def loss_and_grad(p, x0=1.0, x1=2.0, y=1.0):
    w, b = p[:6], p[6:]
    a0 = sigmoid(w[0]*x0 + w[2]*x1 + b[0]); a1 = sigmoid(w[1]*x0 + w[3]*x1 + b[1])
    a2 = w[4]*a0 + w[5]*a1 + b[2]; d = -(y - a2)
    g = np.array([d*w[4]*a0*(1-a0)*x0, d*w[5]*a1*(1-a1)*x0, d*w[4]*a0*(1-a0)*x1,
                  d*w[5]*a1*(1-a1)*x1, d*a0, d*a1,
                  d*w[4]*a0*(1-a0), d*w[5]*a1*(1-a1), d])
    return 0.5 * (y - a2)**2, g

p = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.1, -0.2, 0.05])
eta = 0.5
for step in range(6):
    L, g = loss_and_grad(p)
    print(f"step {step}: loss = {L:.6f}")
    p = p - eta * g          # descend along the negative gradient
```

</PyRunner>

---
layout: prism
heading: "DIY: Learning-Rate Effects"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

def sigmoid(x): return 1.0 / (1.0 + np.exp(-x))

def run(eta, steps=20):
    p = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.1, -0.2, 0.05])
    x0, x1, y = 1.0, 2.0, 1.0
    for _ in range(steps):
        w, b = p[:6], p[6:]
        a0 = sigmoid(w[0]*x0 + w[2]*x1 + b[0]); a1 = sigmoid(w[1]*x0 + w[3]*x1 + b[1])
        a2 = w[4]*a0 + w[5]*a1 + b[2]; d = -(y - a2)
        g = np.array([d*w[4]*a0*(1-a0)*x0, d*w[5]*a1*(1-a1)*x0, d*w[4]*a0*(1-a0)*x1,
                      d*w[5]*a1*(1-a1)*x1, d*a0, d*a1,
                      d*w[4]*a0*(1-a0), d*w[5]*a1*(1-a1), d])
        p = p - eta * g
    return 0.5 * (y - a2)**2

for eta in [0.01, 0.5, 3.0]:
    print(f"eta = {eta:>4}: final loss after 20 steps = {run(eta):.6f}")
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
