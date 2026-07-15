---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 4
download: true
info: |
  ## Mathematics for Artificial Intelligence Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-4-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 04: Probability (Part 1)</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span class="text-gray-900 dark:text-gray-100">Probability, Part 1</span></p>
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
heading: Probability (Part 1)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Probability influences many parts of our everyday lives.

- Concepts from probability theory are applied in important ways across many areas of artificial intelligence.
  - The outputs of AI algorithms, the frequencies of real-world data, the initialization of neural networks, and so on.

- Today, we will cover the following:
  - The basic concepts of probability, especially the definition of a random variable
  - The basic probability rules, together with joint and marginal probability
  - One of the two chain rules related to probability

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Basic Concepts</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Sample Space and Events</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Random Variables</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probability Rules</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Joint and Marginal Probability</span></p>
  </div>

</div>

---
layout: prism
heading: Sample Space and Events (1/2)
---

- A [probability]{.hl} $P$ expresses the possibility that something happens as a number between $0$ and $1$ inclusive ($P \in [0, 1]$).
  - $[a, b]$ denotes the interval that includes $a$ and $b$.
  - $(a, b)$ denotes the interval that excludes $a$ and $b$.
  - If something has no chance of happening, its probability is $0$; if it is certain to happen, it is $1$.
  - We sometimes use % units together with a real number between $0$ and $100$.
    - The probability of rain tomorrow is $25\%$.

- The [sample space]{.hl} $\Omega$ is the discrete set or continuous range representing all possible outcomes of a given [event]{.hl}.
  - An event means that some observation has occurred; it is the result of a process such as a coin toss or a die roll.
  - When dealing with probability, we group all possible outcomes of a given event into a single sample space.
  - The sample space represents all possible outcomes, and an individual event corresponds to a subset of the sample space, i.e., a single sample.
    - [DIY]{.hl} Let us define the sample space and the samples for a coin toss and a die roll.

---
layout: prism
heading: Sample Space and Events (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Although we can define the sample space in a discrete way, as with coin tosses or die rolls, it can also be defined over a continuous range when needed.

- The value that expresses how likely an event is to occur is called the [likelihood]{.hl}.

- When tossing a single coin, the likelihood of heads landing up is $0.5$, and the likelihood of tails landing up is $0.5$.
  - The likelihood for a die roll can be computed in a similar way.

- Summing all likelihoods over the sample space always gives $1$.

- [Q]{.hl} In what respect do probability and likelihood differ?

---
layout: prism
heading: "DIY: Sample Spaces and Likelihoods"
---

<div style="height: 0.6rem;"></div>

<PyRunner>

```python
# Sample space of a coin toss and of a die roll
coin = ["H", "T"]
die = list(range(1, 7))
print("coin sample space :", coin)
print("die  sample space :", die)

# Each outcome is equally likely: likelihood = 1 / |Omega|
print("P(heads)   :", 1 / len(coin))
print("P(die = 4) :", 1 / len(die))

# Likelihoods over the whole sample space must sum to 1
print("sum over coin :", sum(1 / len(coin) for _ in coin))
print("sum over die  :", sum(1 / len(die) for _ in die))
```

</PyRunner>

---
layout: prism
heading: Random Variables
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- When we denote the outcome of tossing a single coin by a variable $X$, this $X$ is called a [random variable]{.hl}.

- A random variable is a variable that takes a single value from its sample space with a particular probability.
  - In the coin-toss example the sample space is discrete, so $X$ is a [discrete random variable]{.hl}.
    - Discrete random variables are _conventionally_ written with uppercase letters.
  - A random variable over a continuous sample space is called a [continuous random variable]{.hl}, and is _conventionally_ written with lowercase letters.

- For a coin toss, the probability that $X$ is heads equals the probability that $X$ is tails, both $0.5$, expressed as $P(X=\text{heads})=P(X=\text{tails})=0.5$.

---
layout: prism
heading: "DIY: Random Variables"
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)

# Coin toss as a random variable X (0 = tails, 1 = heads)
tosses = rng.integers(0, 2, size=100_000)
print("empirical P(X = heads):", round(tosses.mean(), 4), " (theory 0.5)")

# Die roll: expectation and variance estimated by sampling
rolls = rng.integers(1, 7, size=200_000)
print("sample mean :", round(rolls.mean(), 4), " (theory 3.5)")
print("sample var  :", round(rolls.var(), 4), " (theory", round(35/12, 4), ")")
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Basic Concepts</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Probability Rules</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Probability of a Single Event</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Sum Rule</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Product Rule</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Birthday Paradox</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Conditional Probability</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Total Probability</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Joint and Marginal Probability</span></p>
  </div>

</div>

---
layout: prism
heading: Probability of a Single Event
---

- Since summing all probabilities over a sample space gives $1$, the probability of any single event in the sample space is always less than or equal to $1$.

- Formally, for any event $A$ in the sample space,

$$
0 \leq P(A) \leq 1.
$$

- Over all events of the sample space,

$$
\sum_i P(A_i) = 1.
$$

- The probability $P(\bar{A})$ that event $A$ does not occur is called the probability of the [complementary event]{.hl}, defined as $P(\bar{A}) = 1 - P(A)$.

---
layout: prism
heading: "DIY: Probability of a Signle Event"
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)

# Rolling a die: event A = "roll a 6", complement = "not a 6"
rolls = rng.integers(1, 7, size=300_000)
pA = float(np.mean(rolls == 6))
pnotA = float(np.mean(rolls != 6))

print("P(A)          :", round(pA, 4), " (theory", round(1/6, 4), ")")
print("P(not A)      :", round(pnotA, 4))
print("P(A)+P(notA)  :", round(pA + pnotA, 4), " (must be 1)")
```

</PyRunner>

---
layout: prism
heading: The Sum Rule (1/2)
---

- When two events $A$ and $B$ cannot occur at the same time—i.e., if one occurs, the other cannot occur simultaneously—the two events are said to be [mutually exclusive]{.hl}.
  - Heads and tails of a coin cannot appear at once, so they are mutually exclusive.

- If the occurrence probabilities of two events are completely unrelated—i.e., the probability of one is unaffected by whether the other occurs, and vice versa—the two events are said to be [independent]{.hl}.

- The [sum rule]{.hl} of probability concerns the probability that two or more mutually exclusive events occur.
  - When rolling a die, the two events "a 4" and "a 5" are mutually exclusive and each has probability $1/6$, so the probability of a 4 or a 5 is the sum of the two probabilities.

- For mutually exclusive events, the sum rule of probability is defined as

$$
P(A \text{ or } B) = P(A \cup B) = P(A) + P(B).
$$

<div class="sub-item">

$\cup$ denotes "or" (logical OR) and "union".

</div>

---
layout: prism
heading: The Sum Rule (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- The equation above is the sum rule that holds only for mutually exclusive events.

- For events that are not mutually exclusive—that is, in the general case—the following sum rule applies:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B).
$$

- [DIY]{.hl} A bag contains 20 coins, of which 12 are Korean coins and 8 are Japanese coins; among the Korean coins 6 are silver, and among the Japanese coins 3 are silver. If we pick one coin at random from the bag, what is the probability that it is silver or a Korean coin?

---
layout: prism
heading: "DIY: The Sum Rule with a Bag of Coins"
---

<div style="height: 0.6rem;"></div>

<PyRunner>

```python
total = 20
korean, japanese = 12, 8
korean_silver, japanese_silver = 6, 3
silver = korean_silver + japanese_silver

P_silver = silver / total
P_korean = korean / total
P_silver_and_korean = korean_silver / total   # silver AND Korean

# Inclusion-exclusion: P(silver OR Korean)
P_union = P_silver + P_korean - P_silver_and_korean
print("P(silver)            :", P_silver)
print("P(Korean)            :", P_korean)
print("P(silver and Korean) :", P_silver_and_korean)
print("P(silver or Korean)  :", P_union)
```

</PyRunner>

---
layout: prism
heading: The Product Rule
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- Whereas the sum rule gives the probability that event $A$ _or_ $B$ occurs, the [product rule]{.hl} gives the probability that event $A$ _and_ $B$ occur:

$$
P(A \text{ and } B) = P(A \cap B) = P(A) \cdot P(B).
$$

<div class="sub-item">

$\cap$ denotes "and" (logical AND) and "intersection".

</div>

- The fact that mutually exclusive events have zero probability of occurring together cannot be derived from the product-rule equation.
  - The product-rule equation applies to mutually independent events.

- For example, if 80% of the world's population has brown eyes and 50% are women, the probability that a randomly chosen person is a brown-eyed woman can be found by applying the product rule.

- The product rule is not limited to two events; to compute the probability that several independent events occur together, we simply multiply all their individual probabilities.

---
layout: prism
heading: "DIY: The Product Rule"
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(2)

p_brown, p_woman = 0.8, 0.5
print("P(brown-eyed woman) = 0.8 * 0.5 =", p_brown * p_woman)

# Verify independence by simulation
n = 500_000
brown = rng.random(n) < p_brown
woman = rng.random(n) < p_woman
print("simulated P(brown & woman):", round(float(np.mean(brown & woman)), 4))
```

</PyRunner>

---
layout: prism
heading: The Birthday Paradox
---

- The problem of finding the minimum number of people that must be in a room for the probability that at least two share a birthday to exceed 50% is called the [birthday paradox]{.hl}.

- (Assuming a year always has 365 days) the probability that two randomly chosen people share a birthday is $1/365 \approx 0.00274$, and the probability that they do not is $1 - 1/365 = 364/365 \approx 0.9973$.

- The probability that a randomly chosen pair does not share a birthday is, by the product rule, $(364/365)^2 \approx 0.9945$.

- Similarly, after comparing birthdays $n$ times, the probability that none share a birthday is $(364/365)^n$; for this probability to drop below $0.5$, we need $n = 253$.

- Since we must find the number of ways to choose $2$ from $m$ people to reach $253$ [combinations]{.hl}, the smallest $m$ with $\binom{m}{2} = \frac{m!}{2!(m-2)!}$ at least $253$ is $23$.

---
layout: prism
heading: "DIY: The Birthday Paradox"
---

<PyRunner>

```python
import numpy as np

# P(no shared birthday) after n pairwise comparisons: (364/365)^n
n = np.arange(0, 400)
p_none = (364/365) ** n
print("smallest n with (364/365)^n < 0.5 :", int(np.argmax(p_none < 0.5)))

# Exact: probability that m people all have distinct birthdays
def p_distinct(m):
    p = 1.0
    for k in range(m):
        p *= (365 - k) / 365
    return p

for m in [10, 22, 23, 40, 50]:
    print(f"m={m:>3}: P(at least one shared) = {1 - p_distinct(m):.4f}")
```

</PyRunner>

---
layout: prism
heading: Conditional Probability
---

- If a bag contains 8 red marbles and 2 blue marbles, and we draw one marble that turns out to be red, then set it aside and draw again, what is the probability of drawing red again?

- If the fact that event $A$ has occurred changes the probability of event $B$, we write this second probability as $P(B|A)$ and call it the [conditional probability]{.hl}, meaning the probability conditioned on the occurrence of event $A$.

- Unlike the product-rule equation, when two events are [dependent]{.hl}—i.e., not independent—the product rule is defined as

$$
P(A, B) = P(B|A) \cdot P(A).
$$

<div class="sub-item">

$P(A, B)$ denotes the probability of $A$ and $B$.

</div>

- Note that $P(B|A) \neq P(A|B)$.

---
layout: prism
heading: "DIY: Conditional Probability"
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(3)

# Bag: 8 red, 2 blue. Draw one (red), remove it, draw again.
# Exact conditional probability P(2nd red | 1st red) = 7/9
print("exact P(red | red) :", round(7/9, 4))

trials, first_red, second_red = 200_000, 0, 0
for _ in range(trials):
    bag = ["R"] * 8 + ["B"] * 2
    a = bag.pop(rng.integers(len(bag)))
    if a == "R":
        first_red += 1
        if bag.pop(rng.integers(len(bag))) == "R":
            second_red += 1
print("simulated          :", round(second_red / first_red, 4))
```

</PyRunner>

---
layout: prism
heading: Total Probability
---

- Suppose the sample space is divided into several disjoint regions $B_i$ ($B_1, B_2, \ldots$).
  - Disjoint means the regions share no common elements, i.e., the regions do not overlap.
  - Summing all such $B_i$ recovers the entire sample space.

- Each such region (subset) is called a [partition]{.hl} of the set, and the probability of an event over all partitions can be computed as

$$
P(A) = \sum_i P(A|B_i) \cdot P(B_i).
$$

- Here $P(B_i)$ is the probability of partition $B_i$, the fraction of the whole sample space it occupies, and $P(A|B_i)$ is the probability that $A$ occurs within the given partition $B_i$.
  - This equation is called the [total probability]{.hl} of $A$ over the partitions $B_i$.

---
layout: prism
heading: "DIY: Total Probability"
---

- [DIY]{.hl} Three groups have populations of 2,000, 1,000, and 3,000 respectively, and the proportions with black eyes are 12%, 3%, and 21% in that order. If one person is picked at random, what is the probability that they have black eyes?

<PyRunner>

```python
sizes = [2000, 1000, 3000]
rates = [0.12, 0.03, 0.21]
total = sum(sizes)

# Law of total probability: P(black) = sum P(black | group) P(group)
P_black = sum(r * (s / total) for r, s in zip(rates, sizes))
for i, (s, r) in enumerate(zip(sizes, rates), 1):
    print(f"group {i}: P(group)={s/total:.3f}, P(black | group)={r}")
print("P(black eyes) :", round(P_black, 4))
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Basic Concepts</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Probability Rules</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Joint and Marginal Probability</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Joint and Marginal Probability</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Joint Probability Table</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Chain Rule for Probability</span></p>
  </div>

</div>

---
layout: prism
heading: Joint and Marginal Probability
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The [joint probability]{.hl} of two random variables, $P(X=x, Y=y)$, is the probability that $X$ equals $x$ and at the same time $Y$ equals $y$.
  - Joint probability is the probability that several conditions are true at the same time.
  - Joint probability is the probability that two or more random variables take specific values.

- The [marginal probability]{.hl} is the probability that one or more conditions are true, computed regardless of (without caring about) whether the other conditions are true or false.
  - Marginal probability is computed over only a subset of all the random variables.
  - The marginal probability of one random variable is obtained by summing over all possible values of every other random variable.

- We can use a probability table to compute joint and marginal probabilities.

---
layout: prism
heading: The Joint Probability Table (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- Among men, 1 in 12 is color blind; among women, 1 in 200 is color blind.

- Suppose we survey 1,000 people and arrange color blindness by sex as in the table below.

|         | Color blind | Not color blind | Total |
| ------- | ----------- | --------------- | ----- |
| Men     | 42          | 456             | 498   |
| Women   | 3           | 499             | 502   |
| Total   | 45          | 955             | 1,000 |

---
layout: prism
heading: The Joint Probability Table (2/3)
---

- The table above is called a [contingency table]{.hl}; dividing each cell by 1,000 gives the [joint probability table]{.hl}.

|         | Color blind | Not color blind | Total |
| ------- | ----------- | --------------- | ----- |
| Men     | $0.042$     | $0.456$         | $0.498$ |
| Women   | $0.003$     | $0.499$         | $0.502$ |
| Total   | $0.045$     | $0.955$         | $1.000$ |

---
layout: prism
heading: The Joint Probability Table (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- From the joint probability table, we can read off joint probabilities directly.
  - $P(X=\text{man}, Y=\text{color blind}) = 0.042$
  - $P(X=\text{woman}, Y=\text{not color blind}) = 0.499$

- In a similar way, we can compute marginal probabilities.
  - $P(Y=\text{color blind}) = P(X=\text{man}, Y=\text{color blind}) + P(X=\text{woman}, Y=\text{color blind})$

---
layout: prism
heading: "DIY: The Joint Probability Table"
---

- [DIY]{.hl} Using the joint probability table below, compute the marginal probability of submitting the assignment, the probability of submitting given good attendance, the probability of submitting and getting an $A$, and the probability of not submitting and getting an $A$.

| Assignment    | Attendance | A       | B       | C       |
| ------------- | ---------- | ------- | ------- | ------- |
| Submitted     | Good       | $0.334$ | $0.103$ | $0.087$ |
| Submitted     | Poor       | $0.081$ | $0.103$ | $0.018$ |
| Not submitted | Good       | $0.051$ | $0.053$ | $0.081$ |
| Not submitted | Poor       | $0.003$ | $0.007$ | $0.079$ |

---
layout: prism
heading: "DIY: The Joint Probability Table"
---

<PyRunner>

```python
import numpy as np

# Joint probability table: rows = [man, woman], cols = [color blind, not]
J = np.array([[0.042, 0.456],
              [0.003, 0.499]])
print("P(man, color blind) :", J[0, 0])
print("P(woman, not blind) :", J[1, 1])

# Marginals: sum over the other variable
print("P(color blind)      :", round(J[:, 0].sum(), 3))
print("P(man)              :", round(J[0, :].sum(), 3))
print("total (must be 1)   :", round(J.sum(), 3))
```

</PyRunner>

---
layout: prism
heading: The Chain Rule for Probability (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- When there are two random variables and both the conditional and the unconditional probabilities are given, the joint probability can be found via the product rule for conditional probability.

- The generalization of this is called the [chain rule for probability]{.hl}, and can be viewed as an extension of the conditional-probability equation.

- The general form of the chain rule for the joint probability of $n$ random variables is defined as

$$
P(X_n, X_{n-1}, \ldots, X_1) = \prod_{i=1}^{n} P\left( X_i \,\Big|\, \bigcap_{j=1}^{i-1} X_j \right) = \prod_{i=1}^{n} P(X_i \mid X_1, X_2, \ldots, X_{i-1}).
$$

- For example, $P(X, Y, Z)$ can be decomposed as

$$
P(X, Y, Z) = P(X \mid Y, Z) \cdot P(Y, Z) = P(X \mid Y, Z) \cdot P(Y \mid Z) \cdot P(Z).
$$

<div class="sub-item">

Here the chain rule is applied _chain-wise_, linking terms like a chain.

</div>

---
layout: prism
heading: "DIY: The Chain Rule for Probability"
---

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(4)

# Random joint distribution over X, Y, Z (2 values each)
P = rng.random((2, 2, 2))
P /= P.sum()

# Chain rule: P(x,y,z) = P(x | y,z) P(y | z) P(z)
Pz = P.sum(axis=(0, 1))          # P(Z)
Pyz = P.sum(axis=0)              # P(Y, Z)
Py_given_z = Pyz / Pz            # P(Y | Z)
Px_given_yz = P / Pyz            # P(X | Y, Z)
recon = Px_given_yz * Py_given_z * Pz
print("chain rule reconstructs joint:", np.allclose(recon, P))
```

</PyRunner>

---
layout: prism
heading: The Chain Rule for Probability (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Similarly, the joint decomposition for four random variables can be expanded:

$$
\begin{aligned}
P(A, B, C, D) &= P(A \mid B, C, D) \cdot P(B, C, D) \\
&= P(A \mid B, C, D) \cdot P(B \mid C, D) \cdot P(C, D) \\
&= P(A \mid B, C, D) \cdot P(B \mid C, D) \cdot P(C \mid D) \cdot P(D).
\end{aligned}
$$

- Suppose that, among the 60 current students, a total of 7 visited Gyeongnidan-gil during last summer break.

---
layout: prism
heading: "DIY: The Chain Rule for Probability"
---

- [DIY]{.hl} If we pick three students at random from all those enrolled, what is the probability that none of the three has been to Gyeongnidan-gil?

<PyRunner>

```python
import numpy as np
from math import comb
rng = np.random.default_rng(5)

n, visited = 60, 7
# Exact: none of the 3 chosen has visited = C(53,3) / C(60,3)
exact = comb(n - visited, 3) / comb(n, 3)
print("exact P(none visited) :", round(exact, 4))

# Simulation (sampling three students without replacement)
pop = np.array([1] * visited + [0] * (n - visited))
trials = 200_000
hits = sum(rng.choice(pop, 3, replace=False).sum() == 0 for _ in range(trials))
print("simulated             :", round(hits / trials, 4))
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
