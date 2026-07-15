---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 3
download: true
info: |
  ## Data Structure Lecture Slides
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Data Structure</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 03: Algorithm Analysis</p>

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

<div class="absolute left-10 right-10" style="top: 0rem; bottom: 0rem; display: grid; grid-template-columns: 1.2fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">Course Introduction</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">Basic Mathematics and C++ Details</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span class="text-gray-900 dark:text-gray-100">Algorithm Analysis</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">Lists, Stacks, and Queues</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">Circular Queues and Priority Queues</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">Trees and Tries</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">Midterm Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">Midterm Exam</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">Heaps</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">Graphs and Weighted Graphs</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">Sets and Maps</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Hash Tables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Algorithm Design Techniques</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: "Recap: The Four Rules of Recursion"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The four basic rules of recursion are:

<div class="sub-item-enum">

1. *Base cases.* Always have some base cases, which can be solved without recursion.
2. *Making progress.* For cases solved recursively, each recursive call must make progress toward a base case.
3. *Design rule.* Assume that all the recursive calls work.
4. *Compound interest rule.* Never duplicate work by solving the same instance of a problem in separate recursive calls.

</div>

---
layout: prism
heading: "Recap: Basic class Syntax"
---

<div style="height: 1rem;"></div>

```cpp
class IntCell {
public:
    /* default parameter, initialization list,
     * and explicit constructor
     */
    explicit IntCell(int initialValue = 0)
        : storedValue{initialValue} {}
    // constant member function
    int read() const { return storedValue; }
    void write(int x) { storedValue = x; }

private:
    int storedValue;
};
```

---
layout: prism
heading: "Recap: Class Templates"
---

<div style="height: 1.5rem;"></div>

```cpp
int main() {
    MemoryCell<int> m1;
    MemoryCell<string> m2{"hello"};

    m1.write(37);
    m2.write(m2.read() + " world");
    cout << m1.read() << endl << m2.read() << endl;

    return 0;
}
```

---
layout: prism
heading: Algorithm Analysis
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- An [algorithm]{.hl} is a clearly specified set of simple instructions to be followed to solve a problem.

- Once an algorithm is given and decided to be correct, an important step is to determine how much in the way of *resources* — such as time or space — the algorithm will require.
  - An algorithm that solves a problem but requires a year is hardly of any use.
  - An algorithm that requires thousands of gigabytes of main memory is not (currently) useful on most machines.

- In this lecture, we discuss some mathematical background and how to estimate the running time of an algorithm:

<div class="sub-item-enum">

1. How to estimate the time required for a program.
2. How to reduce the running time from days or years to fractions of a second.
3. The results of careless use of recursion.

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Mathematical Background</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Relative Growth Rates and Asymptotic Notation</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Model</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Running-Time Calculations</span></p>
  </div>

</div>

---
layout: prism
heading: "Mathematical Background: Asymptotic Notation"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- Estimating the resource use of an algorithm is generally a theoretical issue, so a formal framework is required. We use four definitions to establish a [relative order]{.hl} among functions.

<div class="theorem-box">
<div class="theorem-box-title">Definition. A relative order among functions</div>
<div class="theorem-box-body">

$T(N) = \mathcal{O}(f(N))$ if there exist positive *constants* $c, n_0$ such that $T(N) \leq c\,f(N)$ when $N \geq n_0$.

$T(N) = \Omega(g(N))$ if there exist positive *constants* $c, n_0$ such that $T(N) \geq c\,g(N)$ when $N \geq n_0$.

$T(N) = \Theta(h(N))$ if and only if $T(N) = \mathcal{O}(h(N))$ *and* $T(N) = \Omega(h(N))$.

$T(N) = o(p(N))$ if, for *all* positive constants $c$, there exists $n_0$ such that $T(N) < c\,p(N)$ when $N > n_0$.

</div>
</div>

---
layout: prism
heading: "Big-Oh Notation"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Recall $T(N) = \mathcal{O}(f(N))$ if there exist positive constants $c, n_0$ with $T(N) \leq c\,f(N)$ for $N \geq n_0$.

- Although $1{,}000N$ is larger than $N^2$ for small $N$, $N^2$ grows at a *faster rate* and will eventually be the larger function — so we compare their [relative rates of growth]{.hl}. The turning point here is $N = 1{,}000$.

- The definition says that beyond some point $n_0$, $c \cdot f(N)$ is always at least as large as $T(N)$; ignoring constant factors, $f(N)$ is at least as big as $T(N)$.
  - Here $T(N) = 1{,}000N$, $f(N) = N^2$, $n_0 = 1{,}000$, and $c = 1$.

- Thus $1{,}000N = \mathcal{O}(N^2)$ (*order $N$-squared* or *big-oh $N$-squared*). This is the [Big-Oh notation]{.hl}.

---
layout: prism
heading: "Comparing Growth Rates"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- Using the traditional inequality operators to compare growth rates:
  - $T(N) = \mathcal{O}(f(N))$ says the growth rate of $T(N)$ is *less than or equal to* ($\leq$) that of $f(N)$.
  - $T(N) = \Omega(g(N))$ (*omega*) says the growth rate of $T(N)$ is *greater than or equal to* ($\geq$) that of $g(N)$.
  - $T(N) = \Theta(h(N))$ (*theta*) says the growth rate of $T(N)$ *equals* ($=$) that of $h(N)$.
  - $T(N) = o(p(N))$ (*little-oh*) says the growth rate of $T(N)$ is *strictly less than* ($<$) that of $p(N)$.

- Little-oh differs from $\mathcal{O}(\cdot)$: big-oh *allows* the possibility that the growth rates are the same, whereas little-oh does not.

---
layout: prism
heading: "Upper and Lower Bounds"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- To prove $T(N) = \mathcal{O}(f(N))$, we usually do not apply the definitions formally but instead use a *repertoire* of known results. A proof should be a simple calculation and rarely involves calculus.

- When $T(N) = \mathcal{O}(f(N))$, we guarantee $T(N)$ grows no faster than $f(N)$; thus $f(N)$ is an [upper bound]{.hl} on $T(N)$. Since this implies $f(N) = \Omega(T(N))$, $T(N)$ is a [lower bound]{.hl} on $f(N)$.
  - $N^3$ grows faster than $N^2$, hence $N^2 = \mathcal{O}(N^3)$ or $N^3 = \Omega(N^2)$.
  - $f(N) = N^2$ and $g(N) = 2N^2$ grow at the same rate, so both $f(N) = \mathcal{O}(g(N))$ and $f(N) = \Omega(g(N))$ hold.

- If $g(N) = 2N^2$, then $g(N) = \mathcal{O}(N^4)$, $\mathcal{O}(N^3)$, and $\mathcal{O}(N^2)$ are all technically correct, but $\mathcal{O}(N^2)$ is best.
  - Writing $g(N) = \Theta(N^2)$ says the result is as *tight* as possible.

---
layout: prism
heading: "Rules for Big-Oh"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- Some useful rules:

<div class="sub-item-enum">

1. If $T_1(N) = \mathcal{O}(f(N))$ and $T_2(N) = \mathcal{O}(g(N))$, then $T_1(N) + T_2(N) = \mathcal{O}(\max(f(N), g(N)))$ and $T_1(N)\cdot T_2(N) = \mathcal{O}(f(N)\cdot g(N))$.
2. If $T(N)$ is a polynomial of degree $k$, then $T(N) = \Theta(N^k)$.
3. $\log^k N = \mathcal{O}(N)$ for any constant $k$.

</div>

- Several points are in order:

<div class="sub-item-enum">

1. It is very bad style to include constants or low-order terms inside a $\mathcal{O}(\cdot)$: write $T(N) = \mathcal{O}(N^2)$, not $\mathcal{O}(2N^2)$ or $\mathcal{O}(N^2 + N)$.
2. We can always determine relative growth rates by computing $\lim_{N\to\infty} f(N)/g(N)$, using *L'Hôpital's rule* if necessary: if $\lim f(N) = \lim g(N) = \infty$, then $\lim f(N)/g(N) = \lim f'(N)/g'(N)$.

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Mathematical Background</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Model of Computation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">What to Analyze</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Running-Time Calculations</span></p>
  </div>

</div>

---
layout: prism
heading: "Model of Computation"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- To analyze algorithms in a formal framework, we need a [model of computation]{.hl}. Our model is basically a normal computer in which instructions are executed *sequentially*.

- It has the standard repertoire of simple instructions — addition, multiplication, comparison, assignment — but, unlike real computers, it takes exactly *one time unit* to do anything.

- To be reasonable, we assume the model has fixed-size (e.g. 32-bit) integers, no fancy operations such as matrix inversion or sorting (which clearly cannot be done in one time unit), and *infinite memory*.

- This model clearly has weaknesses:
  - In the real world, not all operations take exactly the same time.
  - Assuming infinite memory ignores that memory access can cost more when slower memory is used for larger requirements.

---
layout: prism
heading: "What to Analyze"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The most important resource to analyze is generally the [running time]{.hl}.
  - Factors such as the compiler and computer used affect it, but they are beyond our theoretical model.
  - The other main factors are the *algorithm* used and the *input* to the algorithm; the *size* of the input is typically the main consideration.

- We define $T_\text{avg}(N)$ and $T_\text{worst}(N)$ as the average and worst-case running time on input of size $N$, so that $T_\text{avg}(N) \leq T_\text{worst}(N)$.

- Best-case performance is rarely of interest — it does not represent typical behavior.
  - *Average-case* performance often reflects typical behavior.
  - *Worst-case* performance is a *guarantee* on any possible input.

---
layout: prism
heading: "What to Analyze — Worst Case"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- Our analysis bounds are really bounds for *algorithms* rather than *programs*.
  - Programs are an implementation of the algorithm in a particular language.
  - Almost always the details of the programming language do not affect a $\mathcal{O}(\cdot)$ answer.

- The quantity required is the [worst-case time]{.hl}, unless otherwise specified. There are two reasons:
  - It provides a bound for *all* input, including particularly bad input, which an average-case analysis does not.
  - Average-case bounds are usually much harder to compute, because the very definition of "average" can affect the result (*what is average input for a given problem?*).

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Mathematical Background</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Model</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Running-Time Calculations</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">A Simple Example</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">General Rules</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Maximum Subsequence Sum Problem</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Logarithms in the Running-Time</span></p>
  </div>

</div>

---
layout: prism
heading: "Running-Time Calculations"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- There are usually several algorithmic ideas, and we would like to eliminate the bad ones early — so an analysis is usually required.

- The ability to do an analysis usually provides insight into *designing* efficient algorithms, and generally pinpoints the *bottlenecks*, which are worth coding carefully.

- To simplify the analysis, we adopt the convention that there are no particular units of time, throwing away leading constants and low-order terms — essentially computing a [Big-Oh running time]{.hl}.

- Since Big-Oh is an *upper bound*, we must never underestimate the running time.
  - The answer guarantees the program terminates within a certain time.
  - The program may stop earlier, but never later.

---
layout: prism
heading: "A Simple Example"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- A fragment to calculate $\sum_{i=1}^{N} i^3$.

- The declarations count for no time; the assignment (Line 3) and return (Line 6) count for one unit each.

- Line 5 counts four units per execution (two multiplications, one addition, one assignment), executed $N$ times: $4N$ units.

- Line 4 hides the cost of `i = 1`, `i <= n`, and `i++`: $1 + (N{+}1) + N$.

- Total is $6N + 4$, thus this function is $\mathcal{O}(N)$.

</div>
<div>

<div style="height: 3rem;"></div>

```cpp
int sum(int n) {
    int partialSum;
    partialSum = 0;
    for (int i = 1; i <= n; i++)
        partialSum += i * i * i;
    return partialSum;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: Estimating Running Time"
---

<div style="height: 0.3rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

long long ops = 0;                       // basic-operation counter

long long sum(int n) {
    long long partialSum = 0;   ops += 1;         // one assignment
    for (int i = 1; i <= n; i++) {                // hidden loop costs below
        partialSum += (long long)i * i * i;
        ops += 4;                                 // 2 mults, 1 add, 1 assign
    }
    ops += 1 + (n + 1) + n;                       // init + tests + increments
    ops += 1;                                     // return
    return partialSum;
}

int main() {
    for (int n : {10, 100, 1000}) {
        ops = 0;
        long long s = sum(n);
        cout << "N=" << n << "  sum=" << s
             << "  ops=" << ops << "  (6N+4=" << 6 * n + 4 << ")\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "General Rules — Loops"
---

<div style="height: 0.5rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Rule 1 — FOR loops</div>
<div class="theorem-box-body">

The running time of a `for` loop is at most the running time of the statements inside the loop (including tests) times the number of iterations.

</div>
</div>

<div class="theorem-box">
<div class="theorem-box-title">Rule 2 — Nested loops</div>
<div class="theorem-box-body">

The total running time of a statement inside a group of nested loops is the running time of the statement multiplied by the product of the sizes of all the loops.

</div>
</div>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

The following fragment is $\mathcal{O}(N^2)$:

</div>
<div>

```cpp
for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
        k++;
```

</div>
</div>

---
layout: prism
heading: "General Rules — Consecutive Statements"
---

<div style="height: 1rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Rule 3 — Consecutive statements</div>
<div class="theorem-box-body">

Consecutive statements just add, which means that the *maximum* is the one that counts.

</div>
</div>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

The fragment has $\mathcal{O}(N)$ work followed by $\mathcal{O}(N^2)$ work, so it is $\mathcal{O}(N^2)$ overall.

</div>
<div>

```cpp
for (i = 0; i < n; i++)
    a[i] = 0;
for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
        a[i] += a[j] + i + j;
```

</div>
</div>

---
layout: prism
heading: "General Rules — If/Else and Recursion"
---

<div class="theorem-box">
<div class="theorem-box-title">Rule 4 — IF/ELSE</div>
<div class="theorem-box-body">

The running time of an `if/else` statement is never more than the running time of the test plus the *larger* of the running times of each branch.

</div>
</div>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- For recursive functions, there are several options.
  - If the recursion is really just a thinly veiled `for` loop, the analysis is trivial.

- The function on the right is just a simple loop and is $\mathcal{O}(N)$.

</div>
<div>

<div style="height: 2rem;"></div>

```cpp
long factorial(int n) {
    if (n <= 1)
        return 1;
    else
        return n * factorial(n - 1);
}
```

</div>
</div>

---
layout: prism
heading: "General Rules — Careless Recursion"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- When recursion is properly used, it is difficult to convert into a simple loop.

- The running time of this program grows *exponentially*.

- It is slow because of a huge amount of *redundant work*, violating the fourth rule of recursion (the [compound interest rule]{.hl}).

</div>
<div>

<div style="height: 3rem;"></div>

```cpp
long fib(int n) {
    if (n <= 1)
        return 1;
    else
        return fib(n - 1) + fib(n - 2);
}
```

</div>
</div>

---
layout: prism
heading: "The Maximum Subsequence Sum Problem"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Given (possibly negative) integers $A_1, A_2, \ldots, A_N$, find the maximum value of a subsequence sum $\sum_{k=i}^{j} A_k$.
  - For convenience, the maximum subsequence sum is $0$ if all integers are negative.
  - *Example:* for input $-2, 11, -4, 13, -5, -2$, the answer is $20$ (from $A_2$ through $A_4$).

- This problem is interesting mainly because there are so many algorithms to solve it, and their performance varies *drastically*.

- We will discuss [four algorithms]{.hl} to solve this problem.

---
layout: prism
heading: "Maximum Subsequence Sum — Solution 1"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

```cpp
int maxSubSum1(const vector<int> &a) {
    int maxSum = 0;
    for (int i = 0; i < a.size(); i++)
        for (int j = i; j < a.size(); j++) {
            int thisSum = 0;
            for (int k = i; k <= j; k++)
                thisSum += a[k];
            if (thisSum > maxSum)
                maxSum = thisSum;
        }
    return maxSum;
}
```

</div>
<div>

<div style="height: 3rem;"></div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- This algorithm is $\mathcal{O}(N^3)$.

- The running time is entirely due to the *third* nested `for` loop.

</div>
</div>

---
layout: prism
heading: "Maximum Subsequence Sum — Solution 2"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

```cpp
int maxSubSum2(const vector<int> &a) {
    int maxSum = 0;
    for (int i = 0; i < a.size(); i++) {
        int thisSum = 0;
        for (int j = i; j < a.size(); j++) {
            thisSum += a[j];
            if (thisSum > maxSum)
                maxSum = thisSum;
        }
    }
    return maxSum;
}
```

</div>
<div>

<div style="height: 3rem;"></div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- By reusing the running `thisSum`, we drop the innermost loop.

- This algorithm is clearly $\mathcal{O}(N^2)$, with an even simpler analysis than before.

</div>
</div>

---
layout: prism
heading: "Maximum Subsequence Sum — Solution 3 (1/2)"
---

<div style="height: 0.3rem;"></div>

- We can use a [divide-and-conquer]{.hl} strategy: split the array in half, and the best sum is on the left, on the right, or *spanning* the center.

```cpp
int maxSumRec(const vector<int> &a, int left, int right) {
    if (left == right)          // base case
        if (a[left] > 0) return a[left];
        else             return 0;
    int center = (left + right) / 2;
    int maxLeftSum  = maxSumRec(a, left, center);
    int maxRightSum = maxSumRec(a, center + 1, right);

    int maxLeftBorderSum = 0, leftBorderSum = 0;
    for (int i = center; i >= left; i--) {
        leftBorderSum += a[i];
        if (leftBorderSum > maxLeftBorderSum) maxLeftBorderSum = leftBorderSum;
    }
    /* CONTINUE */
```

---
layout: prism
heading: "Maximum Subsequence Sum — Solution 3 (2/2)"
---

<div style="height: 0.3rem;"></div>

```cpp
    /* CONTINUE */
    int maxRightBorderSum = 0, rightBorderSum = 0;
    for (int j = center + 1; j <= right; j++) {
        rightBorderSum += a[j];
        if (rightBorderSum > maxRightBorderSum) maxRightBorderSum = rightBorderSum;
    }
    return max(maxLeftSum, maxRightSum,
               maxLeftBorderSum + maxRightBorderSum);
}

int maxSubSum3(const vector<int> &a) {   // driver function
    return maxSumRec(a, 0, a.size() - 1);
}
```

<div style="height: 0.5rem;"></div>

- This algorithm is $\mathcal{O}(N \log N)$.

---
layout: prism
heading: "Maximum Subsequence Sum — Solution 4"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

```cpp
int maxSubSum4(const vector<int> &a) {
    int maxSum = 0, thisSum = 0;
    for (int j = 0; j < a.size(); j++) {
        thisSum += a[j];
        if (thisSum > maxSum)
            maxSum = thisSum;
        else if (thisSum < 0)
            thisSum = 0;
    }
    return maxSum;
}
```

</div>
<div>

<div style="height: 2.5rem;"></div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A more clever, single-pass method with $\mathcal{O}(N)$ performance.

- Whenever the running `thisSum` becomes negative, it cannot help a future subsequence, so we *reset* it to $0$.

</div>
</div>

---
layout: prism
heading: "DIY: Maximum Subsequence Sum"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxSubSum1(const vector<int> &a) {                 // O(N^3)
    int maxSum = 0;
    for (int i = 0; i < (int)a.size(); i++)
        for (int j = i; j < (int)a.size(); j++) {
            int thisSum = 0;
            for (int k = i; k <= j; k++) thisSum += a[k];
            if (thisSum > maxSum) maxSum = thisSum;
        }
    return maxSum;
}
int maxSubSum2(const vector<int> &a) {                 // O(N^2)
    int maxSum = 0;
    for (int i = 0; i < (int)a.size(); i++) {
        int thisSum = 0;
        for (int j = i; j < (int)a.size(); j++) {
            thisSum += a[j];
            if (thisSum > maxSum) maxSum = thisSum;
        }
    }
    return maxSum;
}
int maxSumRec(const vector<int> &a, int left, int right) {   // O(N log N)
    if (left == right) return a[left] > 0 ? a[left] : 0;
    int center = (left + right) / 2;
    int mL = maxSumRec(a, left, center);
    int mR = maxSumRec(a, center + 1, right);
    int mLB = 0, s = 0;
    for (int i = center; i >= left; i--) { s += a[i]; mLB = max(mLB, s); }
    int mRB = 0; s = 0;
    for (int j = center + 1; j <= right; j++) { s += a[j]; mRB = max(mRB, s); }
    return max({mL, mR, mLB + mRB});
}
int maxSubSum3(const vector<int> &a) { return maxSumRec(a, 0, a.size() - 1); }
int maxSubSum4(const vector<int> &a) {                 // O(N)
    int maxSum = 0, thisSum = 0;
    for (int j = 0; j < (int)a.size(); j++) {
        thisSum += a[j];
        if (thisSum > maxSum) maxSum = thisSum;
        else if (thisSum < 0) thisSum = 0;
    }
    return maxSum;
}

int main() {
    vector<int> a = {-2, 11, -4, 13, -5, -2};
    cout << "Input: -2 11 -4 13 -5 -2\n";
    cout << "Solution 1  O(N^3)      = " << maxSubSum1(a) << "\n";
    cout << "Solution 2  O(N^2)      = " << maxSubSum2(a) << "\n";
    cout << "Solution 3  O(N log N)  = " << maxSubSum3(a) << "\n";
    cout << "Solution 4  O(N)        = " << maxSubSum4(a) << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Logarithms in the Running-Time"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The most confusing aspect of analyzing algorithms probably centers around the [logarithm]{.hl}.

- We have already seen that some divide-and-conquer algorithms run in $\mathcal{O}(N \log N)$ time.

- Besides them, the most frequent appearance of logarithms centers on a general rule:
  - An algorithm is $\mathcal{O}(\log N)$ if it takes constant $\mathcal{O}(1)$ time to cut the problem size by a *fraction* (usually $1/2$).

- Only special kinds of problems can be $\mathcal{O}(\log N)$.
  - If the input is a list of $N$ numbers, an algorithm must take $\Omega(N)$ merely to *read* the input.
  - So for $\mathcal{O}(\log N)$ algorithms on such problems, we usually presume the input is *preread*.

---
layout: prism
heading: "Binary Search"
---

<div style="height: 0.5rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Binary Search</div>
<div class="theorem-box-body">

Given an integer $X$ and integers $A_0, A_1, \ldots, A_{N-1}$, which are *presorted* and already in memory, find $i$ such that $A_i = X$, or return $i = -1$ if $X$ is not in the input.

</div>
</div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The obvious solution scans the list left to right in linear time, but does not exploit that the list is sorted, and is thus not likely to be best.

- A better strategy checks whether $X$ is the *middle* element.
  - If so, the answer is at hand.
  - If $X$ is smaller than the middle element, apply the same strategy to the left subarray; if larger, look to the right half.

---
layout: prism
heading: "Binary Search — Implementation"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

```cpp
template <typename Comparable>
int binarySearch(const vector<Comparable> &a,
                 const Comparable &x) {
    int low = 0, high = a.size() - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (a[mid] < x)
            low = mid + 1;
        else if (a[mid] > x)
            high = mid - 1;
        else
            return mid;   // found
    }
    return NOT_FOUND;     // NOT_FOUND is -1
}
```

</div>
<div>

<div style="height: 3rem;"></div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Each iteration halves the search range, so binary search runs in $\mathcal{O}(\log N)$ time.

- All the work is $\mathcal{O}(1)$ per iteration, and there are at most $\lceil \log N \rceil$ iterations.

</div>
</div>

---
layout: prism
heading: "DIY: Binary Search"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int NOT_FOUND = -1;

template <typename Comparable>
int binarySearch(const vector<Comparable> &a, const Comparable &x) {
    int low = 0, high = (int)a.size() - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (a[mid] < x)      low = mid + 1;
        else if (a[mid] > x) high = mid - 1;
        else                 return mid;   // found
    }
    return NOT_FOUND;
}

int main() {
    vector<int> a = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};  // presorted
    for (int x : {23, 91, 2, 17}) {
        int idx = binarySearch(a, x);
        cout << "search " << x << " -> index " << idx;
        if (idx == NOT_FOUND) cout << "  (not found)";
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
