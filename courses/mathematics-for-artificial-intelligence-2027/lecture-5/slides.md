---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 5
download: true
info: |
  ## Mathematics for Artificial Intelligence Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-5-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 05: Probability (Part 2)</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span class="text-gray-900 dark:text-gray-100">Probability, Part 2</span></p>
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
heading: Recap of Week 04 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Last time, we introduced the fundamentals of probability.

- Probability expresses the likelihood that something happens as a number between $0$ and $1$ (inclusive).

- The sample space is the discrete set or observation interval that represents all possible outcomes of a given event.

- A random variable is a variable that takes a single value from the sample space with a specific probability.

---
layout: prism
heading: Recap of Week 04 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- The sum rule of probability is $P(A\cup B)=P(A)+P(B)-P(A\cap B)$, and the product rule is $P(A\cap B)=P(A,B)=P(B|A)\cdot P(A)$.
  - $P(B|A)$ is the conditional probability, expressing the probability that $B$ occurs given that $A$ occurs.

- The total probability of $A$ over a partition $B_i$ is $P(A)=\sum_i P(A|B_i)\cdot P(B_i)$.

- The joint probability is the probability that two or more random variables take specific values; the marginal probability is obtained by summing, for one random variable, over all values the other random variables can take.

---
layout: prism
heading: Probability (Part 2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Whereas last time we covered the basic concepts of probability, this time we will look at topics where probability is actually used in linear machine-learning algorithms and deep-learning algorithms.

- In particular, Bayes' theorem, which we cover today, brought about a shift in the philosophical paradigm of probability and changed the way we think about and apply probability.

- Today's lecture will cover the following:
  - Probability distributions and sampling
  - Bayes' theorem

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Probability Distributions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Histograms and Probability</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Discrete Probability Distributions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Continuous Probability Distributions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Central Limit Theorem</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Law of Large Numbers</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Bayes' Theorem</span></p>
  </div>

</div>

---
layout: prism
heading: Histograms and Probability
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.5fr 1fr;">
<div>


- A [probability distribution]{.hl} is a function that randomly generates values according to predefined probabilities.
  - Which values will appear cannot be known in advance, but the likelihood of each value being generated follows a specific pattern defined by the distribution.

- For example, a distribution in which each value is generated with an _equal_ probability of $1/6$, like a die, is called a [uniform distribution]{.hl}.

- Look at the table on the right, showing the probabilities of the sums of pips when rolling two dice.
  - [DIY]{.hl} Draw a bar chart with each pip-sum on the $x$-axis.
    - Such a graph is called a [histogram]{.hl}.

</div>
<div>

<div class="text-center" style="font-size: 0.8rem; margin-top: 0rem;">
  <table style="line-height: 2; border-collapse: collapse; margin: auto;">
    <thead>
      <tr style="padding: 0;">
        <th style="padding: 1px 5px; text-align: center;">Sum</th>
        <th style="padding: 1px 5px; text-align: center;">Probability</th>
      </tr>
    </thead>
    <tbody>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">2</td><td style="padding: 1px 5px; text-align: center;">0.0278</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">3</td><td style="padding: 1px 5px; text-align: center;">0.0556</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">4</td><td style="padding: 1px 5px; text-align: center;">0.0833</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">5</td><td style="padding: 1px 5px; text-align: center;">0.1111</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">6</td><td style="padding: 1px 5px; text-align: center;">0.1389</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">7</td><td style="padding: 1px 5px; text-align: center;">0.1667</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">8</td><td style="padding: 1px 5px; text-align: center;">0.1389</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">9</td><td style="padding: 1px 5px; text-align: center;">0.1111</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">10</td><td style="padding: 1px 5px; text-align: center;">0.0833</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">11</td><td style="padding: 1px 5px; text-align: center;">0.0556</td></tr>
      <tr style="padding: 0;"><td style="padding: 1px 5px; text-align: center;">12</td><td style="padding: 1px 5px; text-align: center;">0.0278</td></tr>
    </tbody>
  </table>
</div>



</div>
</div>

---
layout: prism
heading: "DIY: Histograms and Probability"
---

- From values drawn from a histogram, or any distribution, we can gauge the probability or likelihood that such samples occur.
  - That is, we can [estimate]{.hl} the distribution the samples were drawn from.

<PyRunner>

```python
import numpy as np
# All outcomes of rolling two fair dice, and the distribution of their sums.
faces = np.arange(1, 7)
sums = np.add.outer(faces, faces).ravel()      # 36 equally likely sums
values, counts = np.unique(sums, return_counts=True)
probs = counts / counts.sum()
for v, p in zip(values, probs):
    print(f"sum {v:>2}: P = {p:.4f}  " + "#" * int(round(p * 100)))
print("total probability:", probs.sum())
```

</PyRunner>

---
layout: prism
heading: Discrete Distributions - Binomial (1/2)
---

- A distribution that describes cases where each event is discrete, like rolling a die, is called a [discrete probability distribution]{.hl}.

- The [binomial distribution]{.hl} describes the expected frequency of each event when a specific probability is assigned to each event and the trial is repeated a given number of times.

- The probability that an event with occurrence probability $p$ happens $k$ times in $n$ trials is defined as

$$
P(X=k)=\binom{n}{k}\cdot p^k\cdot (1-p)^{n-k}
$$

- The probability that a single coin lands heads three times in a row over three tosses is

$$
\begin{aligned}
P(HHH) &= \frac{1}{2}\cdot\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{8}\quad\text{(using the product rule)}\\
&=\binom{3}{3}\cdot\left(\frac{1}{2}\right)^3\cdot\left(1-\frac{1}{2}\right)^{3-3}=\frac{1}{8}\quad\text{(using the binomial distribution)}
\end{aligned}
$$

---
layout: prism
heading: Discrete Distributions - Binomial (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The binomial formula gives the probability that, given a per-event probability $p$, exactly $k$ events occur over a given number of trials $n$.

- [DIY]{.hl} For $n=3$ and $p=0.5$, use the binomial distribution to compute the probability of each $k$ for $0\leq k\leq 3$.
  - The sum of all computed probabilities must equal $1.0$.

- The probabilities computed this way define a [probability mass function]{.hl}.
  - A probability mass function tells us the probability associated with every possible outcome.

- The binomial distribution uses $n$ and $p$ as its [hyperparameters]{.hl}.

---
layout: prism
heading: "DIY: Discrete Distributions - Binomial"
---

<PyRunner>

```python
from math import comb
n, p = 3, 0.5

def binom_pmf(k, n, p):
    return comb(n, k) * p**k * (1 - p)**(n - k)

probs = [binom_pmf(k, n, p) for k in range(n + 1)]
for k, pr in enumerate(probs):
    print(f"P(X={k}) = {pr:.4f}")
print("sum of PMF:", sum(probs))
```

</PyRunner>

---
layout: prism
heading: Discrete Distributions - Bernoulli
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The [Bernoulli distribution]{.hl} is a special case of the binomial distribution.

- In the Bernoulli distribution, $n=1$ is fixed (i.e., there is always exactly one trial), and the value drawn is either $0$ or $1$.
  - A single coin toss can be represented by a Bernoulli distribution with $p=0.5$.

- When simulating events whose probabilities are already known, we draw samples from a binomial distribution.

- The Bernoulli distribution is useful for events with a dichotomous outcome.
  - The probability of each event need not be exactly $0.5$.

---
layout: prism
heading: "DIY: Discrete Distributions - Bernoulli"
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(0)
p = 0.5
x = (rng.random(100000) < p).astype(int)   # Bernoulli(p): 1 with prob p, else 0

print("empirical mean :", x.mean(), " (theory p =", p, ")")
print("empirical var  :", x.var(), " (theory p(1-p) =", p * (1 - p), ")")
print("unique values  :", np.unique(x))
```

</PyRunner>

---
layout: prism
heading: Discrete Distributions - Poisson
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- Suppose we do not know the specific probability that an event occurs on any particular trial, but only its average number of occurrences over a fixed interval (e.g., trials over a fixed period of time).

- If the average number of occurrences of an event within a fixed interval is $\lambda$, the probability that the event occurs $k$ times in that interval is defined as

$$
P(k)=\frac{\lambda^k\cdot e^{-\lambda}}{k!}
$$

- A distribution following this equation is called a [Poisson distribution]{.hl}.

---
layout: prism
heading: "DIY: Discrete Distributions - Poisson"
---

- [DIY]{.hl} Suppose a convenience store gets on average $20$ customers per hour. Compute the probability that exactly $22$ customers arrive during the next hour.

<PyRunner>

```python
import numpy as np
from math import exp, factorial

lam = 20                      # average customers per hour

def poisson(k, lam):
    return lam**k * exp(-lam) / factorial(k)

print(f"P(exactly 22) = {poisson(22, lam):.4f}")
print(f"P(exactly 20) = {poisson(20, lam):.4f}")
total = sum(poisson(int(k), lam) for k in np.arange(0, 60))
print("sum over k=0..59:", round(total, 6))
```

</PyRunner>

---
layout: prism
heading: Continuous Probability Distributions
---

- A [continuous probability distribution]{.hl} follows a specific form like a discrete distribution, but it does not assign probability to individual values.
  - The probability that any single specific value is chosen in a continuous distribution is $0$.
    - There are infinitely many values that can be chosen in a continuous distribution.

- For example, the probability that a particular real number is chosen from the interval $[0, 1]$ is $0$, but the probability that the chosen number falls within some subinterval (e.g., $[0.1, 0.2]$) can be expressed using a continuous distribution.
  - Assuming a uniform distribution, that probability would be $0.1$.

- Thus, a continuous distribution is computed via [integration]{.hl}, summing the infinitely small elements within an interval.

- A continuous distribution is associated with a [probability density function]{.hl}, a _closed_-form function that generates the probabilities applied when drawing values from the distribution.

---
layout: prism
heading: Continuous Distributions - Normal
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>


- The [normal distribution]{.hl}, often called the Gaussian distribution or the bell curve, is a curve symmetric about its mean.

- The normal distribution ($\mathcal{N}(\mu, \sigma)$) has two parameters: the mean ($\mu$), the center of the curve, and the standard deviation ($\sigma$), which determines how flat the curve is.

- The probability density function of the normal distribution is

$$
p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\cdot e^{-(x-\mu)^2/\sigma^2}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W05_normal.svg" class="tikz-fig" style="width: 95%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Continuous Distributions - Normal"
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(1)
mu, sigma = 1.0, 0.75
s = rng.normal(mu, sigma, 200000)

print("sample mean/std:", round(s.mean(), 4), round(s.std(), 4))

# Density and its integral (trapezoid rule) over a wide grid
x = np.linspace(mu - 8*sigma, mu + 8*sigma, 4000)
pdf = 1 / np.sqrt(2*np.pi*sigma**2) * np.exp(-(x - mu)**2 / (2*sigma**2))
area = np.sum((pdf[:-1] + pdf[1:]) / 2 * np.diff(x))

print("integral of pdf:", round(area, 6))
```

</PyRunner>

---
layout: prism
heading: Continuous Distributions - Gamma
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.5fr 1fr;">
<div>

- The [gamma distribution]{.hl} ($\Gamma(k, \theta)$) also uses two parameters: the shape ($k$), which determines the curve's form, and the scale ($\theta$), which determines its scaling.

- A larger shape parameter shifts the bulge of the gamma curve toward the center of the distribution, while the scale parameter affects the width of the bulge.

- The probability density function of the gamma distribution is

$$
\begin{gathered}
p(x)=x^{k-1}\cdot\frac{e^{-x/\theta}}{\theta^k\cdot\Gamma(k)}\\
\Gamma(k)=\int_{0}^{\infty}t^{k-1}e^{-t}\,\mathrm{d}t
\end{gathered}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W05_gamma.svg" class="tikz-fig" style="width: 100%; margin-top: 4rem" />

</div>
</div>

---
layout: prism
heading: "DIY: Continuous Distributions - Gamma"
---

<PyRunner>

```python
import numpy as np
from math import gamma

k, theta = 2.0, 2.0

def gamma_pdf(x, k, theta):
    return x**(k - 1) * np.exp(-x / theta) / (theta**k * gamma(k))

x = np.linspace(1e-6, 60, 6000)
pdf = gamma_pdf(x, k, theta)
area = np.sum((pdf[:-1] + pdf[1:]) / 2 * np.diff(x))
mid = (x[:-1] + x[1:]) / 2
mean = np.sum(mid * (pdf[:-1] + pdf[1:]) / 2 * np.diff(x))

print("shape k =", k, " scale theta =", theta)
print("integral of gamma pdf:", round(area, 5))
print("numeric mean:", round(mean, 4), " (theory k*theta =", k * theta, ")")
```

</PyRunner>

---
layout: prism
heading: Continuous Distributions - Beta
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

- The [beta distribution]{.hl} also uses two parameters, $a$ and $b$; the larger $a$ is relative to $b$, the more its bulge shifts to the right.
  - The beta distribution is very flexible, making it useful for simulating a wide range of processes.

- The probability density function of the beta distribution is

$$
\begin{gathered}
p(x)=\frac{x^{a-1}\cdot(1-x)^{b-1}}{B(a, b)}\\
B(a, b)=\int_{0}^{1}t^{a-1}\cdot(1-t)^{b-1}\,\mathrm{d}t
\end{gathered}
$$

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W05_beta.svg" class="tikz-fig" style="width: 95%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Continuous Distributions - Beta"
---

<PyRunner>

```python
import numpy as np
from math import gamma

def beta_fn(a, b):
    return gamma(a) * gamma(b) / gamma(a + b)

def beta_pdf(x, a, b):
    return x**(a - 1) * (1 - x)**(b - 1) / beta_fn(a, b)

a, b = 5.0, 2.0
x = np.linspace(1e-6, 1 - 1e-6, 5000)
pdf = beta_pdf(x, a, b)
area = np.sum((pdf[:-1] + pdf[1:]) / 2 * np.diff(x))
print("a =", a, " b =", b)
print("integral of beta pdf:", round(area, 5))
print("mean = a/(a+b) =", round(a / (a + b), 4))
```

</PyRunner>

---
layout: prism
heading: Central Limit Theorem
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Suppose we repeatedly draw $N$ samples from an arbitrary distribution and compute their mean $m$, many times over.
  - That is, we obtain a collection of means $m_0, m_1, \ldots$
  - Here, $N$ may vary each time, but it must not be too small.

- The [central limit theorem]{.hl} states that the distribution formed from these sample means approaches a normal distribution, regardless of the shape of the underlying distribution the samples were drawn from.
  - For example, if we compute means from many Bernoulli samples and plot the distribution of those means, it follows a normal distribution.

- [DIY]{.hl} A Galton board is a simple toy that lets you observe the central limit theorem.

---
layout: prism
heading: "DIY: Central Limit Theorem"
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(2)
p, N, trials = 0.3, 50, 20000

# Repeatedly draw N Bernoulli(p) samples and record each batch mean.
means = (rng.random((trials, N)) < p).mean(axis=1)
print("mean of sample means :", round(means.mean(), 4), " (~ p =", p, ")")

theory_std = (p * (1 - p) / N) ** 0.5
print("std of sample means  :", round(means.std(), 4), " (~", round(theory_std, 4), ")")

z = (means - means.mean()) / means.std()
print("fraction |z| < 1     :", round(np.mean(np.abs(z) < 1), 4), " (normal ~0.68)")
```

</PyRunner>

---
layout: prism
heading: Law of Large Numbers
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The [law of large numbers]{.hl} states that the larger the size (i.e., the number) of samples drawn from a distribution, the closer the sample mean gets to the population mean.
  - This is different from the central limit theorem.

- The law of large numbers concerns the relationship between the mean of a single sample drawn from a distribution and the population mean, whereas the central limit theorem concerns the distribution of the sample means when many samples are drawn.

- For example, when flipping a coin, the first ten trials might yield eight heads, but as the number of trials grows, the ratio of heads to tails approaches roughly 5:5.

---
layout: prism
heading: "DIY: Law of Large Numbers"
---

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(3)
flips = (rng.random(100000) < 0.5).astype(int)          # fair coin
running = np.cumsum(flips) / np.arange(1, len(flips) + 1)

for n in [10, 100, 1000, 10000, 100000]:
    print(f"after {n:>6} flips: heads proportion = {running[n-1]:.4f}")

print("target = 0.5")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probability Distributions</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Bayes' Theorem</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">A Frequentist View</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">A Bayesian View</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Updating the Prior</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Bayes' Theorem in Machine Learning</span></p>
  </div>

</div>

---
layout: prism
heading: Cancer Diagnosis - A Frequentist View
---

- As a famous example in probability and statistics, let us compute the probability that a woman in her 40s whose mammogram is positive actually has breast cancer.

- The information given to us is as follows:

<div class="sub-item-enum">

1. The probability that a randomly chosen woman in her 40s has breast cancer is 0.8%.
2. The probability that a woman with breast cancer has a positive mammogram is 90%.
3. The probability that a woman without breast cancer has a positive mammogram is 7%.

</div>

- If a woman in her 40s comes to the hospital for an X-ray and the result is positive, what is the probability that she actually has breast cancer?
  - Out of 1,000 women in their 40s, on average 8 have breast cancer, and of those, 7 women ($8\times0.9=7.2$) receive a positive mammogram.
  - Of the 992 women without breast cancer, 69 ($992\times0.07=69.44$) also receive a positive mammogram.
  - In total 76 women ($7+69=76$) have a positive mammogram, yet only 7 of them actually have breast cancer, so the probability of having cancer given a positive mammogram is about 9% ($7/76\approx0.092$).

---
layout: prism
heading: "DIY: Cancer Diagnosis - A Frequentist View"
---

<PyRunner>

```python
# Frequentist counting over 1,000 women in their 40s.
n = 1000
have = n * 0.008              # 8 have breast cancer
no = n - have                 # 992 do not
tp = have * 0.90              # true positives  (7.2)
fp = no * 0.07                # false positives (69.44)
posterior = tp / (tp + fp)

print(f"positive & cancer    : {tp:.2f}")
print(f"positive & no cancer : {fp:.2f}")
print(f"P(cancer | positive) : {posterior:.4f}  (~9%)")
```

</PyRunner>

---
layout: prism
heading: Cancer Diagnosis - A Bayesian View (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Let us revisit the product rule of probability:

$$
\begin{gathered}
P(B, A) = P(B|A)\cdot P(A)\\
P(A, B) = P(A|B)\cdot P(B)
\end{gathered}
$$

- Since it does not matter which event we call $A$ and which we call $B$ in a joint probability, $P(A, B)=P(B, A)$ holds, and therefore

$$
P(B|A)\cdot P(A) = P(A|B)\cdot P(B)
$$

- Dividing both sides by $P(A)$ gives what we call [Bayes' theorem]{.hl}:

$$
P(B|A)=\frac{P(A|B)\cdot P(B)}{P(A)}
$$

<div class="sub-item">

This says the [posterior probability]{.hl} ($P(B|A)$) is the product of the likelihood ($P(A|B)$) and the [prior probability]{.hl} ($P(B)$), normalized by the marginal probability ($P(A)$).

</div>

---
layout: prism
heading: Cancer Diagnosis - A Bayesian View (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.2em;
}
</style>

- The probability of having breast cancer given a positive mammogram corresponds to the posterior probability in Bayes' theorem.
  - Let us denote it $P(bc+ \,|\, +)$ ($bc+$ means a positive breast-cancer diagnosis, and $+$ means a positive mammogram test).

- We also know the probability that the mammogram is positive given that the patient has breast cancer ($P(+ \,|\, bc+)$) and the probability that a randomly chosen woman has breast cancer ($P(bc+)$).

---
layout: prism
heading: "DIY: Cancer Diagnosis - A Bayesian View"
---

- [DIY]{.hl} Compute the marginal probability $P(+)$ that the mammogram is positive, regardless of cancer status.
  - $P(+)=P(+|bc+)\cdot P(bc+) + P(+|bc-)\cdot P(bc-)$

- [DIY]{.hl} Use Bayes' theorem to compute $P(bc+ \,|\, +)$.

<PyRunner>

```python
# Bayes' theorem with the same numbers.
p_bc = 0.008                 # prior P(bc+)
p_pos_given_bc = 0.90        # likelihood P(+ | bc+)
p_pos_given_no = 0.07        # P(+ | bc-)
p_pos = p_pos_given_bc * p_bc + p_pos_given_no * (1 - p_bc)   # marginal P(+)
posterior = p_pos_given_bc * p_bc / p_pos

print("marginal P(+)        :", round(p_pos, 4))
print("posterior P(bc+ | +) :", round(posterior, 4))
```

</PyRunner>

---
layout: prism
heading: Updating the Prior
---

- Suppose a woman in her 40s who was told her mammogram was positive takes another mammogram at a different hospital, and this one is positive as well.
  - In this case, her probability of having breast cancer is no longer 9%, because a new piece of evidence (the first test) now exists, so the [degree of belief]{.hl} that she has cancer grows.

- Bayes' theorem provides the mathematical justification for the process of taking the computed posterior probability and updating it back into the prior to recompute the degree of belief.

- [DIY]{.hl} Based on the earlier mammogram result, compute the new posterior probability.
  - The previously computed $P(bc+ \,|\, +)$ now serves as the new prior probability.

<PyRunner>

```python
# A second independent positive test: yesterday's posterior becomes today's prior.
p_pos_given_bc, p_pos_given_no = 0.90, 0.07
prior = 0.008
for test in range(1, 4):
    p_pos = p_pos_given_bc * prior + p_pos_given_no * (1 - prior)
    prior = p_pos_given_bc * prior / p_pos          # update the belief
    print(f"after positive test #{test}: P(cancer) = {prior:.4f}")
```

</PyRunner>

---
layout: prism
heading: "HW03: Build Your Own Bayes' Theorem Example"
---

- Just like the breast-cancer diagnosis problem we worked through, real life offers many examples where Bayes' theorem applies.

- Create one example of a similar form, use Bayes' theorem to compute a posterior probability, and then additionally carry out the process of updating that posterior back into a prior to compute a new degree of belief.

- You may invent your own scenario, or find an example online and rewrite it in your own words.

- Write up this process (adding figures is welcome) and upload it to the LMS.
  - Please upload it as `HW03_20XXXXXX.pdf`.
  - You may write it by hand (recommended) or use a word processor.
  - No need for a cover page or decoration; just clearly write your name and student ID at the top.
  - Font, text size, and so on are entirely up to you.

---
layout: prism
heading: Bayes' Theorem in Machine Learning (1/2)
---

- Bayes' theorem is widely used in machine learning and deep learning, and one representative example is the naive Bayes classifier.
  - Early spam-email filters were one example that used the naive Bayes classifier very effectively.

- Consider the problem of classifying dogs and cats based on features (e.g., eye shape, ear shape, the sound they make).
  - Given a class label $y$ and a feature vector $\mathbf{x}$, the goal is to find the class with the largest probability for a given feature vector, which Bayes' theorem expresses as

$$
P(y|\mathbf{x})=\frac{P(\mathbf{x}|y)\cdot P(y)}{P(\mathbf{x})}
$$

- To simplify the problem, we ignore the marginal probability $P(\mathbf{x})$.
  - What matters to us is the posterior $P(y|\mathbf{x})$; the denominator (the marginal) is just a tool to normalize the total posterior to $1.0$.
  - That is, the equation becomes $P(y|\mathbf{x})\propto P(\mathbf{x}|y)\cdot P(y)$.

---
layout: prism
heading: Bayes' Theorem in Machine Learning (2/2)
---

- Assuming the distribution of class labels in the given dataset well represents the true population, we can obtain $P(y)$ from the data we have.
  - If the data contain dogs and cats in a 1:1 ratio, we set $P(\text{cat})=0.5$.

- $P(\mathbf{x}|y)$ is the probability of the feature vectors given that they represent class $y$; assuming $y$ is cat for now, and knowing the feature vectors all come from cat data, we momentarily ignore the $y$ part.
  - With $n$ features, for a feature vector $\mathbf{x}=(x_0, x_1, \ldots, x_{n-1})$, $P(\mathbf{x} \,|\, y=\text{cat})$ is the joint probability that all individual features simultaneously take specific values, and the naive Bayes classifier _naively_ assumes all these features are independent.
    - That is, $P(\mathbf{x})=P(x_0, x_1, \ldots, x_{n-1})=P(x_0)\cdot P(x_1)\cdots P(x_{n-1})$.

- The subsequent computation becomes very simple: we count how many times each feature is observed in each class, then use Bayes' rule to infer the final class label.
  - That is, we estimate probabilities using counts such as, among the cat-class feature vectors, how many have sharp eyes, how many have triangular ears, how many make a "meow" sound, and so on.

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
