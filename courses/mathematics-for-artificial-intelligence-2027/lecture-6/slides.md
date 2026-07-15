---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 6
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 06: Statistics</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span class="text-gray-900 dark:text-gray-100">Statistics</span></p>
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
heading: "Recap: Week 05"
---

- A probability distribution is a function that randomly generates values according to predefined probabilities.
  - When each event is discrete, we use discrete probability distributions, such as the binomial, Bernoulli, and Poisson distributions.
  - Continuous probability distributions follow a particular form but do not assign probability to individual values; examples include the normal, gamma, and beta distributions.

- The central limit theorem states that the probability distribution formed from sample means approaches a normal distribution regardless of the shape of the actual population from which the samples were drawn.

- The law of large numbers states that the more samples drawn from an arbitrary distribution, the closer the sample mean gets to the population mean.

- Bayes' theorem is used widely in machine learning and deep learning, and is given by $P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}$

---
layout: prism
heading: Statistics
---

- If the [dataset]{.hl} is bad, the [model]{.hl} will be bad too.
  - Before building a model, we must properly understand the properties of the data, and it is desirable to use that understanding to build a useful dataset.
  - Understanding the data properly requires basic knowledge of statistics.

- A [statistic]{.hl} is a numerical value computed from a sample that characterizes that sample in some way.
  - One of the most basic statistics is the mean, which summarizes an entire dataset in a single number.

- Today, we will cover the following:
  - Examining the types of data and how to characterize a dataset with summary statistics
  - The definition of quantiles and grasping the contents of data through graphs
  - A discussion of outliers and missing values
  - An introduction to statistical hypothesis testing

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Types of Data</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Summary Statistics</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Quantiles and Box Plots</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Correlation</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Hypothesis Testing</span></p>
  </div>

</div>

---
layout: prism
heading: "Types of Data: Nominal Data"
---

- [Nominal data]{.hl}, also called [categorical data]{.hl}, are data with no order relation between distinct values.
  - The brown, blue, green, etc. in a dataset representing people's eye colors have no particular order relation and can be represented as nominal data.

- To use such color data in a deep neural network, we must first convert it into a form the network can process.

- Since nominal data have no order, one might consider converting, e.g., red to $1$, green to $2$, blue to $3$, but this is not desirable.
  - The network may take these as literal numbers and misinterpret them, as if blue had a three-times relationship to red.

- To resolve this, deep learning usually uses [one-hot encoding]{.hl} to convert each nominal variable into a vector whose components correspond one-to-one with the values the nominal variable can take.
  - [DIY]{.hl} One-hot encode red, green, and blue.

---
layout: prism
heading: "DIY: One-Hot Encoding"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
import numpy as np

# One-hot encode nominal categories: each color -> a unit vector.
colors = ["red", "green", "blue"]
onehot = np.eye(len(colors), dtype=int)

for name, vec in zip(colors, onehot):
    print(f"{name:>6} -> {vec}")

# No ordering is implied: every pair is equidistant.
print("distance(red, blue) :", np.linalg.norm(onehot[0] - onehot[2]))
print("distance(red, green):", np.linalg.norm(onehot[0] - onehot[1]))
```

</PyRunner>

---
layout: prism
heading: "Types of Data: Ordinal Data"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [Ordinal data]{.hl} have a rank or order, but the differences between values carry no mathematical meaning.
  - In a survey, there is clearly an order difference between "strongly agree" and "agree", but no numerical relationship exists between them (e.g., "strongly agree" is not three times stronger agreement than "agree").

- All we can say based on ordinal data is that an order exists between the data points.

- Ordinal data are also often used to represent [demographic information]{.hl}, such as education level.
  - A university graduate has received _more_ education than a high-school graduate, but we cannot say _how many times_ more.

---
layout: prism
heading: "Types of Data: Interval Data"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- [Interval data]{.hl} are data where the differences between values are meaningful.

- If we have one cup of water at 40°F and one at 80°F, we can say the temperature difference between them is 40°F, but we cannot say the second cup holds twice as much heat as the first.
  - The [Fahrenheit scale]{.hl} sets the freezing point of water at 32°F and the boiling point at 212°F.

- Converting the example above to the [Celsius scale]{.hl}, the first cup is about 4.4°C and the second about 26.7°C.

- As with the Celsius and Fahrenheit examples, ratios of differences become meaningless for interval data.

---
layout: prism
heading: "Types of Data: Ratio Data"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [Ratio data]{.hl} are data where not only are the differences meaningful, but a [zero point]{.hl} exists.
  - Height has a zero point at $0$, and can be represented as ratio data.
  - Age has a zero point at $0$ years, and can also be represented as ratio data.

- Fahrenheit and Celsius temperatures are interval data, but converting the scale to absolute temperature makes them ratio data.
  - The absolute temperature scale has a zero point at 0 K, meaning a complete absence of temperature.
  - In the earlier example, the first cup is about 277.59 K and the second about 299.82 K, so we can say the second cup is about 1.08 times hotter than the first.

- In summary: nominal data have no order; ordinal data have order but meaningless differences; interval data have meaningful differences but no strict zero point; and ratio data have a true zero point defined.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Types of Data</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Summary Statistics</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Mean and Median</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Measures of Variation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Quantiles and Box Plots</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Correlation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Hypothesis Testing</span></p>
  </div>

</div>

---
layout: prism
heading: "Mean and Median - Arithmetic Mean"
---

- One way to effectively understand a dataset is to compute [summary statistics]{.hl}.

- The most representative summary statistic is the [arithmetic mean]{.hl}. When a dataset is a set of [scalar]{.hl} values $\{x_0, x_1, x_2, \ldots, x_{n-1}\}$, the arithmetic mean $\bar{x}$ is the sum of the elements divided by the size $n$:

$$
\bar{x} = \frac{1}{n} \sum_{i=0}^{n-1} x_i
$$

- The equation above is the [unweighted]{.hl} mean, where each value is given a weight of $1/n$.

- When the elements of a dataset are not equally important but split into more and less important ones, we can apply individual weights to compute a [weighted]{.hl} mean:

$$
\bar{x} = \sum_{i=0}^{n-1} w_i x_i, \quad \sum_{i=0}^{n-1} w_i = 1
$$

---
layout: prism
heading: "DIY: Mean and Median - Arithmetic Mean"
---

<PyRunner>

```python
import numpy as np

x = np.array([81, 80, 85, 87, 83, 90, 79, 88], float)
print("arithmetic mean :", x.mean())

# A weighted mean: weights must sum to 1.
w = np.linspace(1, 2, len(x))
w = w / w.sum()
print("weights sum to  :", round(w.sum(), 6))
print("weighted mean   :", round(float((w * x).sum()), 4))
```

</PyRunner>

---
layout: prism
heading: "Mean and Median - Geometric Mean"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- The [geometric mean]{.hl} of two positive numbers $a$ and $b$ is defined as:

$$
\bar{x}_g = \sqrt{ab}
$$

- Generalizing, the geometric mean of $n$ positive numbers is defined as:

$$
\bar{x}_g = \sqrt[n]{\prod_{i=0}^{n-1} x_i} = \sqrt[n]{x_0 x_1 x_2 \cdots x_{n-1}}
$$

- The geometric mean is also used in image processing as a filter to reduce image [noise]{.hl}.

---
layout: prism
heading: "Mean and Median - Harmonic Mean (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- The [harmonic mean]{.hl} of two numbers $a$ and $b$ is the reciprocal of the arithmetic mean of their reciprocals:

$$
\bar{x}_h = \left( \frac{1}{2} \left( \frac{1}{a} + \frac{1}{b} \right) \right)^{-1}
$$

- Generalizing:

$$
\bar{x}_h = \left( \frac{1}{n} \sum_{i=0}^{n-1} \frac{1}{x_i} \right)^{-1}
$$

- The [F1 score]{.hl} used in deep learning is the harmonic mean of [recall]{.hl} and [precision]{.hl}:

$$
\mathrm{F}1 = \left( \frac{1}{2} \left( \frac{1}{\mathrm{recall}} + \frac{1}{\mathrm{precision}} \right) \right)^{-1}
$$

---
layout: prism
heading: "DIY: Mean and Median - Harmonic Mean"
---


<PyRunner>

```python
import numpy as np

x = np.array([1, 3, 9, 27], float)
print("arithmetic mean :", x.mean())
print("geometric mean  :", np.exp(np.log(x).mean()))   # = (prod x)^(1/n)
print("harmonic mean   :", 1.0 / np.mean(1.0 / x))

# F1 = harmonic mean of precision and recall
precision, recall = 0.8, 0.6
print("F1 score        :", 2.0 / (1/precision + 1/recall))
```

</PyRunner>

---
layout: prism
heading: "Mean and Median - Harmonic Mean (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- Recall and precision are defined as:

$$
\begin{aligned}
\mathrm{recall} &= \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}} \\
\mathrm{precision} &= \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FP}}
\end{aligned}
$$

- $\mathrm{TP}$ is the number of [true positives]{.hl}, $\mathrm{FN}$ the number of [false negatives]{.hl}, and $\mathrm{FP}$ the number of [false positives]{.hl}.

- Because the F1 score ignores the [true negative]{.hl} count, it often fails to evaluate a model properly and tends to give relatively optimistic results.

---
layout: prism
heading: "Mean and Median - Median"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The [median]{.hl} of a dataset is the value in the middle of all the data.
  - When the dataset's values are sorted by magnitude, half lie above the median and half below.

- The sorted dataset $\{37, 44, 55, 63, 65, 69, 71, 73, 74, 87\}$ has an even number of elements, so there is no single middle value; in this case, we use the arithmetic mean of the two middle values as the median.
  - That is, the median is $67$.

- With the median, the order of elements matters, whereas with the mean, the actual sum of the data values is reflected.

---
layout: prism
heading: "DIY: Mean and Median - Median"
---

<PyRunner>

```python
import numpy as np

data = np.array([37, 44, 55, 63, 65, 69, 71, 73, 74, 87], float)
print("median (numpy)  :", np.median(data))

s = np.sort(data)
n = len(s)
if n % 2:
    med = s[n // 2]
else:
    med = (s[n // 2 - 1] + s[n // 2]) / 2   # mean of the two middle values
print("median (manual) :", med, "(mean of 65 and 69)")
```

</PyRunner>

---
layout: prism
heading: "Measures of Variation (1/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Suppose one dataset contains $\{-100, -10, -1, 0, 1, 10, 100\}$ and another contains $\{0, 0, 0, 0, 0, 0, 0\}$. Their mean and median are both $0$, but their [variation]{.hl} differs.

- One way to measure the variation of a dataset is the [range]{.hl}, i.e., the difference between the largest and smallest values.
  - However, the range reflects only the two extreme values rather than all the data, so it is not very representative.

- Better than the range is the [mean deviation]{.hl} $\mathrm{MD}$, based on the differences between each value and the mean, computed as:

$$
\mathrm{MD} = \frac{1}{n} \sum_{i=0}^{n-1} |x_i - \bar{x}|
$$

---
layout: prism
heading: "Measures of Variation (2/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- Since the mean deviation is awkward to handle because of the [absolute value]{.hl}, the [biased sample variance]{.hl}, the mean of the squared differences between each value and the mean, is used instead:

$$
s_n^2 = \frac{1}{n} \sum_{i=0}^{n-1} (x_i - \bar{x})^2
$$

- A slightly different form below is called the [unbiased sample variance]{.hl}:

$$
s^2 = \frac{1}{n-1} \sum_{i=0}^{n-1} (x_i - \bar{x})^2
$$

  - Using $n-1$ instead of $n$ is called [Bessel's correction]{.hl}, devised to reduce the _bias_ of the sample variance.

---
layout: prism
heading: "DIY: Measures of Variation"
---

<PyRunner>

```python
import numpy as np

x = np.array([-100, -10, -1, 0, 1, 10, 100], float)
n = len(x)
biased = x.var()            # divides by n
unbiased = x.var(ddof=1)    # Bessel's correction: divides by n-1

print("mean            :", x.mean())
print("biased  s_n^2   :", round(biased, 4))
print("unbiased s^2    :", round(unbiased, 4))
print("std deviation   :", round(np.sqrt(unbiased), 4))
print("standard error  :", round(np.sqrt(unbiased) / np.sqrt(n), 4))
```

</PyRunner>

---
layout: prism
heading: "Measures of Variation (3/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- In practice, since we cannot know the true mean $\mu$ and variance $\sigma^2$ of the [population]{.hl}, we estimate them using the mean $m$ and variance $s_n^2$ (or $s^2$) of a [sample]{.hl}.

- The claim that $s^2$ is a more suitable choice than $s_n^2$ for estimating $\sigma^2$ is now widely accepted.
  - However, if the dataset is large enough, applying Bessel's correction or not makes little difference.
    - The larger the sample data, the more likely it is not to estimate the population in a biased way.
  - In deep learning and other large-scale data settings, it makes little difference which variance is used.

- The square root of the variance is called the [standard deviation]{.hl}, another commonly adopted statistic for expressing variation.
  - The population standard deviation is usually denoted $\sigma$ and the sample standard deviation $s$.

---
layout: prism
heading: "Measures of Variation (4/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- The standard deviation of the set of sample means is called the [standard error of the mean]{.hl} (or standard error), denoted $\mathrm{SE}$ and defined as:

$$
\mathrm{SE} = \frac{s}{\sqrt{n}}
$$

- The standard deviation is useful for understanding how spread out the values are around the mean, while the standard error is useful for understanding how well a sample mean estimates the population mean.

- In deep learning, the standard deviation can be used to understand the characteristics of the dataset used for training.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Types of Data</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Summary Statistics</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Quantiles and Box Plots</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Correlation</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Hypothesis Testing</span></p>
  </div>

</div>

---
layout: prism
heading: Quantiles
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [quantile]{.hl} is a value that divides a dataset into several groups of fixed size.
  - The median is a [2-quantile]{.hl} because it divides the dataset into two groups of equal size.
    - The median is also called the [50th percentile]{.hl}, meaning it is greater than 50% of the values in the dataset.
    - The 95th percentile means a value greater than 95% of the data.

- Datasets are also commonly divided into [quartiles]{.hl}.
  - The first quartile (Q1) contains 25% of the values, up to the second quartile (Q2) 50%, up to the third quartile (Q3) 75%, and the fourth quartile (Q4) includes all the data.

- A commonly used tool for showing quartiles is the [box plot]{.hl}.

---
layout: prism
heading: Box Plot
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- A box plot marks Q1 and Q3, and the difference between the two is called the [interquartile range (IQR)]{.hl}.

- The median (Q2) is marked in the middle of the box.

- The lines extending from the box are called [whiskers]{.hl}, and the values outside the whiskers are called [possible outliers]{.hl}.

<div class="flex justify-center" style="margin-top: 0.6rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W06_boxplot_diagram.svg" class="tikz-fig" style="width: 78%;" />
</div>

---
layout: prism
heading: "DIY: Quartiles and IQR"
---

<div style="height: 0.6rem;"></div>

<PyRunner>

```python
import numpy as np

# A sample of exam scores.
data = np.array([81, 80, 85, 87, 83, 87, 87, 90, 79, 83,
                 88, 75, 87, 92, 78, 80, 94, 100, 77, 91], float)

q1, q2, q3 = np.percentile(data, [25, 50, 75])
iqr = q3 - q1
lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr

print(f"Q1 = {q1},  median (Q2) = {q2},  Q3 = {q3}")
print(f"IQR = Q3 - Q1 = {iqr}")
print(f"whisker fences: [{lo}, {hi}]")
print("possible outliers:", data[(data < lo) | (data > hi)])
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Types of Data</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Summary Statistics</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Quantiles and Box Plots</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Correlation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Pearson Correlation Coefficient</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Spearman Correlation Coefficient</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Hypothesis Testing</span></p>
  </div>

</div>

---
layout: prism
heading: Correlation
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- There are often relationships between the features of a dataset.
  - When one feature increases, another may increase or decrease (not necessarily in exact proportion); this kind of association is called [correlation]{.hl}.

- Generally, in machine learning, high correlation means that no new information is provided, which adds confusion to the learning model.
  - [Feature selection]{.hl} in machine learning is performed to resolve this problem.

- Correlation can be computed in various ways, but every kind expresses how strongly two features of a dataset are associated as a single number.

---
layout: prism
heading: Pearson Correlation Coefficient
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- The [Pearson correlation coefficient]{.hl} is a value in $[-1, 1]$ representing the strength of the [linear]{.hl} correlation between two features, commonly denoted $r$.
  - Linear means the correlation between the two features can be described by a single straight line.
  - If one feature increases by a fixed amount and the other increases by exactly the same amount, the Pearson coefficient is $+1$; if it decreases, $-1$.
  - If the coefficient between two features is $0$, the two features are potentially independent.

- For two feature vectors $\mathbf{v}$, $\mathbf{w}$ of a dataset, the Pearson coefficient is defined as:

$$
r = \frac{E(\mathbf{v}\mathbf{w}) - E(\mathbf{v})E(\mathbf{w})}{\sqrt{E(\mathbf{v}^2) - E(\mathbf{v})^2}\,\sqrt{E(\mathbf{w}^2) - E(\mathbf{w})^2}}
$$

  - $E(\cdot)$ denotes the [expectation value]{.hl}.

---
layout: prism
heading: "DIY: Pearson Correlation Coefficient"
---

<PyRunner>

```python
import numpy as np

v = np.array([1, 2, 3, 4, 5, 6], float)
w = np.array([2.1, 3.9, 6.2, 7.8, 10.1, 12.2], float)

def pearson(a, b):
    E = np.mean
    num = E(a * b) - E(a) * E(b)
    den = np.sqrt(E(a * a) - E(a) ** 2) * np.sqrt(E(b * b) - E(b) ** 2)
    return num / den

print("Pearson r (formula) :", round(pearson(v, w), 6))
print("check vs corrcoef   :", round(np.corrcoef(v, w)[0, 1], 6))
```

</PyRunner>

---
layout: prism
heading: Spearman Correlation Coefficient
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- Another widely used correlation coefficient is the [Spearman correlation coefficient]{.hl}.
  - Like the Pearson coefficient, it is a value in $[-1, 1]$, denoted $\rho$.
  - The Spearman coefficient is based not on the feature values themselves but on their [ranks]{.hl}.

- The Pearson correlation finds linear relationships, while the Spearman correlation finds monotonic associations between inputs.
  - For a nonlinear relationship, the Pearson correlation only hints at it, whereas the Spearman correlation reflects the nonlinear relationship.

- For two vectors $\mathbf{v}$, $\mathbf{w}$ each with $n$ values, the Spearman correlation is defined as:

$$
\rho = 1 - \left( \frac{6}{n(n^2 - 1)} \right) \sum_{i=0}^{n-1} d_i^2, \quad d = \operatorname{rank}(\mathbf{v}) - \operatorname{rank}(\mathbf{w})
$$

---
layout: prism
heading: "DIY: Spearman Correlation Coefficient"
---

<PyRunner>

```python
import numpy as np

v = np.array([10, 20, 30, 40, 50], float)
w = np.array([1, 4, 9, 16, 25], float)   # monotonic but nonlinear in v

def rankdata(a):                          # 1-based ranks (no ties here)
    return np.argsort(np.argsort(a)).astype(float) + 1

def pearson(a, b):
    a = a - a.mean(); b = b - b.mean()
    return (a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum())

rv, rw = rankdata(v), rankdata(w)
n = len(v)
d = rv - rw
print("Pearson on values  :", round(pearson(v, w), 4))
print("Spearman (rank r)  :", round(pearson(rv, rw), 4))
print("Spearman (formula) :", round(1 - 6 * np.sum(d ** 2) / (n * (n ** 2 - 1)), 4))
```

</PyRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Types of Data</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Summary Statistics</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Quantiles and Box Plots</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Correlation</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Hypothesis Testing</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Hypotheses</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">t-test</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Mann-Whitney U-test</span></p>
  </div>

</div>

---
layout: prism
heading: "Hypothesis Testing (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 100 students taking the Mathematics for AI course were split into two groups of 50. Group 1 attended lectures and completed hands-on assignments, while Group 2 only attended lectures; they then took the same exam, and we examined the score distributions.

- To determine whether there is a meaningful difference between the two groups' scores, we must perform [hypothesis testing]{.hl}.
  - Hypothesis testing is an essential element of modern science.

<table style="margin: 0.8rem auto 0 auto; font-size: 0.8rem; border-collapse: collapse;">
<thead>
<tr>
<th style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; text-align: center;">Group</th>
<th style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; text-align: left;">Exam scores</th>
</tr>
</thead>
<tbody>
<tr>
<td style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; text-align: center;">Group 1</td>
<td style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; font-family: monospace;">81 80 85 87 83 87 87 90 79 83 88 75 87 92 78 80 83 91 82 88 89 92 97 82 79 82 82 85 89 91 83 85 77 81 90 87 82 84 86 79 84 85 90 84 90 85 85 78 94 100</td>
</tr>
<tr>
<td style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; text-align: center;">Group 2</td>
<td style="border: 1px solid #9aa0a6; padding: 0.3rem 0.6rem; font-family: monospace;">92 82 78 74 86 69 83 67 85 82 81 91 79 82 82 88 80 63 85 86 77 94 85 75 77 89 86 71 82 82 80 88 72 91 90 92 95 87 71 83 94 90 78 60 76 88 91 83 85 73</td>
</tr>
</tbody>
</table>

---
layout: prism
heading: "Hypothesis Testing (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Hypothesis testing has developed in various ways, with many methods evolving for the different situations a researcher may encounter.

- In this course, we cover only the t-test and the Mann-Whitney U test.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W06_boxplot.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Hypotheses (1/2)"
---

- When we want to know whether two datasets were sampled from the same population distribution, a basic first step is to check the summary statistics.
  - Looking at the AI-math exam score distributions, the two groups' medians differ and the boxes are fairly symmetric about the median, so the two groups' means are likely to differ.
  - Let us apply hypothesis testing centered on the two groups' means.

- Hypothesis testing uses two kinds of hypotheses.

<div class="sub-item-enum">

1. [Null hypothesis]{.hl} $H_0$: also called the void hypothesis, it assumes that what we suspect is false.
   - It assumes the two groups actually came from the same population, i.e., have the same mean.
2. [Alternative hypothesis]{.hl} $H_a$: the hypothesis we want to demonstrate.
   - It means the two groups came from different populations.
   - If the null hypothesis is rejected, the alternative is implicitly accepted.

</div>

- Hypothesis testing does not tell us whether the null hypothesis is true or false; it simply provides evidence to decide whether to reject or accept the null hypothesis.

---
layout: prism
heading: "Hypotheses (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- Since this hypothesis test judges whether the two groups came from the same population, every test here is a [two-tailed]{.hl} (also [two-sided]{.hl}) test.
  - Use a two-tailed test when we only want to know whether the two groups differ; use a [one-tailed]{.hl} ([one-sided]{.hl}) test when we want to know whether one group is larger or smaller than the other.

- To prepare for hypothesis testing, let us organize the assumptions:

<div class="sub-item-enum">

1. We want to compare two independent groups.
2. We make no assumption about whether the two groups have equal standard deviations.
3. The null hypothesis is that the two groups' population means are equal ($H_0: \mu_1 = \mu_2$).
   - Since we do not know the population means, we use the sample means and sample standard deviations to obtain the evidence needed to decide whether to accept the null hypothesis.
4. We assume the data are [independent and identically distributed (i.i.d.)]{.hl}.
   - Samples generated by a sufficiently random process can be assumed i.i.d.

</div>

---
layout: prism
heading: "t-test (1/2)"
---

- The [$t$-test]{.hl} relies on a test statistic denoted $t$, which it compares against a precomputed [$t$-distribution]{.hl} to obtain a $p$-value.
  - The $p$-value is the probability used to draw a conclusion about $H_0$.

- The $t$-test is a type of [parametric]{.hl} test, making specific assumptions about the data and its distribution.
  - The $t$-test assumes the data are i.i.d. and that the distribution is normal.
    - Many real-world phenomena actually follow a normal distribution, so data made of real measurements are likely to be normal.

- There are several kinds of $t$-test, and the appropriate one must be chosen based on the dataset's size or variance.
  - [Welch's $t$-test]{.hl} does not assume the two samples' variances are equal; when the two samples have $n_1$ and $n_2$ data points, the $t$-score is computed as:

$$
t = \bar{x}_1 - \bar{x}_2 / \sqrt{(s_1^2 / n_1) + (s_2^2 / n_2)}
$$

---
layout: prism
heading: "t-test (2/2)"
---

- Using the computed $t$-score, we can find the $p$-value by computing the area under the $t$-distribution curve over a particular interval.
  - In a two-tailed test, the $p$-value is the total area of the tail from the positive $t$-score to positive infinity and from the negative $t$-score to negative infinity.

- The $p$-value is the probability that the two means differ if the null hypothesis were true.
  - If this probability is smaller than some predefined value, we treat it as evidence that the two groups' means differ, i.e., that the two groups came from different populations, and we reject the null hypothesis.

- When we reject the null hypothesis this way, we often say there is a [statistically significant]{.hl} difference; the commonly used $p$-value threshold is $0.05$.
  - Research requiring rigorous statistics uses a smaller $p$-value, or considers rejecting the null hypothesis if repeating the same experiment many times keeps the $p$-value consistently below $0.05$.

---
layout: prism
heading: "Confidence Interval (1/2)"
---

- Alongside the $p$-value, the [confidence interval]{.hl} frequently appears in statistics.

- The confidence interval is the range of true population mean differences within which the mean differences of repeated samples between the two datasets fall at a certain rate (the confidence level).
  - A commonly used one is the $95\%$ confidence interval.
  - In the current example, since the hypothesis test checks whether the means are equal by seeing whether the difference of sample means is $0$, a confidence interval containing $0$ is evidence that we should not reject the null hypothesis.

- In Welch's $t$-test, the degrees of freedom $df$ are computed as:

$$
df = \frac{\left( \dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2} \right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1 - 1} + \dfrac{(s_2^2/n_2)^2}{n_2 - 1}}
$$

---
layout: prism
heading: "Confidence Interval (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- For given degrees of freedom $df$, the confidence interval $CI_\alpha$ is defined based on the confidence level $\alpha$ and the [critical value]{.hl} $t_{1-\alpha/2,\,df}$ as:

$$
CI_\alpha = (\bar{x}_1 - \bar{x}_2) \pm t_{1-\alpha/2,\,df} \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
$$

- A $95\%$ confidence interval means that if we drew samples from the population to form two datasets, measured the difference of their sample means, and repeated this 100 times computing a confidence interval each time, the true population mean difference would fall within 95 of the 100 confidence intervals.

- The width of the confidence interval indicates how large an [effect]{.hl} is.
  - A narrow confidence interval means the range containing the true effect is narrow.

---
layout: prism
heading: Effect Size
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Even with a statistically significant $p$-value, the difference is not necessarily meaningful in the real world.

- What better expresses practical significance is the [effect size]{.hl}; to measure it, [Cohen's $d$]{.hl} is commonly used, computed in Welch's $t$-test as:

$$
d = \frac{\bar{x}_2 - \bar{x}_1}{\sqrt{\frac{1}{2}(s_1^2 + s_2^2)}}
$$

- How to interpret the effect size can vary by situation, and the number is usually reported together with its interpretation.

- [DIY]{.hl} Based on the hypothesis test results for the two groups, $p = 0.01825$, $CI = [0.56105, 5.95895]$, and $d = 0.48047$, provide an interpretation.

---
layout: prism
heading: "DIY: Welch's t-test on the Two Groups"
---

<div style="height: 0.3rem;"></div>

<PyRunner>

```python
import numpy as np
from math import gamma

g1 = np.array([81,80,85,87,83,87,87,90,79,83,88,75,87,92,78,80,83,91,82,88,
               89,92,97,82,79,82,82,85,89,91,83,85,77,81,90,87,82,84,86,79,
               84,85,90,84,90,85,85,78,94,100], float)
g2 = np.array([92,82,78,74,86,69,83,67,85,82,81,91,79,82,82,88,80,63,85,86,
               77,94,85,75,77,89,86,71,82,82,80,88,72,91,90,92,95,87,71,83,
               94,90,78,60,76,88,91,83,85,73], float)
n1, n2 = len(g1), len(g2)
m1, m2 = g1.mean(), g2.mean()
v1, v2 = g1.var(ddof=1), g2.var(ddof=1)          # unbiased variances
t = (m1 - m2) / np.sqrt(v1/n1 + v2/n2)
df = (v1/n1 + v2/n2)**2 / ((v1/n1)**2/(n1-1) + (v2/n2)**2/(n2-1))

def t_pdf(x, dof):                                # Student-t density
    c = gamma((dof+1)/2) / (np.sqrt(dof*np.pi) * gamma(dof/2))
    return c * (1 + x*x/dof)**(-(dof+1)/2)

xs = np.linspace(abs(t), 200, 400000)             # two-tailed p by integration
f = t_pdf(xs, df)
p = 2 * np.sum((f[:-1] + f[1:]) / 2 * np.diff(xs))
d = (m1 - m2) / np.sqrt(0.5*(v1 + v2))            # Cohen's d (magnitude)
print(f"means: {m1:.3f} vs {m2:.3f}   t = {t:.4f}   df = {df:.2f}")
print(f"two-tailed p = {p:.5f}   Cohen's d = {abs(d):.5f}")
```

</PyRunner>

---
layout: prism
heading: "Mann-Whitney U-test (1/2)"
---

- The $t$-test assumes the original data follow a normal distribution; when this assumption is not met, we must use a [nonparametric]{.hl} test.
  - A nonparametric test makes no assumption about the distribution of the data.

- The [Mann-Whitney $U$-test]{.hl}, also called the [Wilcoxon rank-sum test]{.hl}, is a nonparametric test used to judge whether two datasets came from the same population distribution.
  - The Mann-Whitney $U$-test uses the ranks of the data values rather than the values themselves.
  - Its null hypothesis is "the probability that a value randomly chosen from Group 1 is greater than a value randomly chosen from Group 2 is $0.5$", meaning that if the two groups came from the same population distribution, there is no reason for a randomly drawn value of one group to tend to be larger than that of the other.
    - The null hypothesis of the $t$-test is "the difference of the two groups' means is $0$", which differs from that of the Mann-Whitney $U$-test.

- Whether we use the $t$-test or the Mann-Whitney $U$-test, if the two datasets truly came from different population distributions, both null hypotheses are false.

---
layout: prism
heading: "Mann-Whitney U-test (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The test statistic of the Mann-Whitney $U$-test is $U$, computed by combining all values of the datasets, sorting them by magnitude, and assigning ranks.

- After computing the rank sum $R_1$ of Group 1 (with $n_1$ samples) and the rank sum $R_2$ of Group 2 (with $n_2$ samples), the $U$ value is computed as:

$$
U = n_1 n_2 + \min\left( \frac{n_1(n_1 - 1)}{2} - R_1,\ \frac{n_2(n_2 - 1)}{2} - R_2 \right)
$$

- It is also possible to obtain a $p$-value for the Mann-Whitney $U$-test.
  - The larger the sample size, the more likely it is to produce a statistically significant $p$-value.

---
layout: prism
heading: "DIY: Mann-Whitney U-test"
---

<PyRunner>

```python
import numpy as np
from math import erf, sqrt

g1 = np.array([81,80,85,87,83,87,87,90,79,83,88,75,87,92,78,80,83,91,82,88,
               89,92,97,82,79,82,82,85,89,91,83,85,77,81,90,87,82,84,86,79,
               84,85,90,84,90,85,85,78,94,100], float)
g2 = np.array([92,82,78,74,86,69,83,67,85,82,81,91,79,82,82,88,80,63,85,86,
               77,94,85,75,77,89,86,71,82,82,80,88,72,91,90,92,95,87,71,83,
               94,90,78,60,76,88,91,83,85,73], float)

def avg_ranks(a):                     # average ranks with ties
    order = np.argsort(a, kind="mergesort"); sa = a[order]; r = np.empty(len(a)); i = 0
    while i < len(a):
        j = i
        while j < len(a) and sa[j] == sa[i]: j += 1
        r[order[i:j]] = (i + j - 1) / 2 + 1; i = j
    return r

n1, n2 = len(g1), len(g2)
ranks = avg_ranks(np.concatenate([g1, g2]))
R1, R2 = ranks[:n1].sum(), ranks[n1:].sum()
U = min(R1 - n1*(n1+1)/2, R2 - n2*(n2+1)/2)      # standard Mann-Whitney U
z = (U - n1*n2/2) / sqrt(n1*n2*(n1+n2+1)/12)     # normal approximation
p = 2 * (1 - 0.5*(1 + erf(abs(z)/sqrt(2))))
print(f"R1 = {R1},  R2 = {R2},  U = {U}")
print(f"z = {z:.4f},  two-tailed p = {p:.5f}")
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
