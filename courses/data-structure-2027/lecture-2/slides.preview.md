---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 2
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 02: Basic Mathematics and C++ Details</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span class="text-gray-900 dark:text-gray-100">Basic Mathematics and C++ Details</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">Algorithm Analysis</span></p>
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
heading: Basic Mathematics and C++ Details
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- In this lecture, we briefly review the discrete mathematics and programming concepts used throughout the course:

  - Summarize the basic mathematical background needed for the rest of the course.

  - Briefly review [recursion]{.hl}.

  - Summarize some important features of [C++]{.hl} that are used throughout this course.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Mathematics Review</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Exponents and Logarithms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Series</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Modular Arithmetic</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Proofs</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Recursion</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ Classes</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ Details</span></p>
  </div>

</div>

---
layout: prism
heading: Exponents
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- Below are some basic formulas involving [exponents]{.hl} that we should be able to *memorize* or *derive*.

$$
\begin{gather*}
X^A X^B = X^{A+B} \qquad \frac{X^A}{X^B} = X^{A-B} \qquad (X^A)^B = X^{AB}\\[0.4em]
X^N + X^N = 2X^N \neq X^{2N} \qquad 2^N + 2^N = 2^{N+1}
\end{gather*}
$$

- The last two are especially easy to get wrong, so keep them in mind.

---
layout: prism
heading: Logarithms
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- In computer science, all logarithms are to the [base 2]{.hl} unless specified otherwise.

<div class="theorem-box">
<div class="theorem-box-title">Definition of the logarithm</div>
<div class="theorem-box-body">

$X^A = B$ _if and only if_ $\log_X B = A$.

</div>
</div>

- Several convenient equalities follow from this definition:

<div class="sub-item-enum">

1. $\log_A B = \log_C B / \log_C A,\ \forall A, B, C > 0,\ A \neq 1$
2. $\log AB = \log A + \log B \quad(\forall A, B > 0) \qquad \log A/B = \log A - \log B \qquad \log(A^B) = B\log A$
3. $\log X < X\ (\forall X > 0) \qquad \log 1 = 0,\quad \log 2 = 1,\quad \log 1024 = 10$

</div>

---
layout: prism
heading: Geometric Series
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The easiest formulas to remember are

$$
\sum_{i=0}^{N} 2^i = 2^{N+1} - 1 \qquad\text{and its companion}\qquad \sum_{i=0}^{N} A^i = \frac{A^{N+1} - 1}{A - 1}.
$$

- In the latter, if $0 < A < 1$, then

$$
\sum_{i=0}^{N} A^i \leq \frac{1}{1 - A},
$$

and as $N \to \infty$ the sum approaches $1/(1-A)$. These are the [geometric series]{.hl} formulas.

---
layout: prism
heading: Deriving the Geometric Sum
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- We can derive $\sum_{i=0}^{\infty} A^i$ for $0 < A < 1$ as follows (let $S$ be the sum):

$$
S = 1 + A + A^2 + A^3 + \cdots \qquad AS = A + A^2 + A^3 + A^4 + \cdots
$$

- Subtracting (valid only for a *convergent* series) cancels virtually all terms on the right:

$$
S - AS = 1 \;\Rightarrow\; S = \frac{1}{1 - A}.
$$

- The same technique gives $\sum_{i=0}^{\infty} (1/2)^i = 2$, a sum that occurs frequently.

---
layout: prism
heading: Arithmetic and Power Series
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Another common series is the [arithmetic series]{.hl}:

$$
\sum_{i=1}^{N} i = \frac{N(N+1)}{2} \approx \frac{N^2}{2}.
$$

- The next two are less common but still useful:

$$
\sum_{i=1}^{N} i^2 = \frac{N(N+1)(2N+1)}{6} \approx \frac{N^3}{3} \qquad
\sum_{i=1}^{N} i^k \approx \frac{N^{k+1}}{|k+1|},\ \forall k \neq -1.
$$

---
layout: prism
heading: Harmonic Numbers
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The following appears far more in computer science than elsewhere:

$$
H_N = \sum_{i=1}^{N} \frac{1}{i} \approx \log_e N,
$$

where the $H_N$ are the [harmonic numbers]{.hl} and the sum is a [harmonic sum]{.hl}.

- The error in the approximation tends to [Euler's constant]{.hl} $\gamma \approx 0.57721566$.

- Two more general algebraic manipulations:

$$
\sum_{i=1}^{N} f(N) = N f(N) \qquad \sum_{i=n_0}^{N} f(i) = \sum_{i=1}^{N} f(i) - \sum_{i=1}^{n_0 - 1} f(i).
$$

---
layout: prism
heading: Modular Arithmetic
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- We say $A$ is [congruent]{.hl} to $B$ modulo $N$, written $A \equiv B \ (\operatorname{mod}\ N)$, if $N$ divides $A - B$.
  - Equivalently, $A$ and $B$ leave the same *remainder* when divided by $N$, e.g. $81 \equiv 61 \equiv 1\ (\operatorname{mod}\ 10)$.

- As with equality, if $A \equiv B\ (\operatorname{mod}\ N)$, then $A + C \equiv B + C$ and $AD \equiv BD \ (\operatorname{mod}\ N)$.

- When $N$ is [prime]{.hl}, three important theorems hold:

<div class="sub-item-enum">

1. $ab \equiv 0\ (\operatorname{mod}\ N)$ *if and only if* $a \equiv 0$ or $b \equiv 0\ (\operatorname{mod}\ N)$.
2. $ax \equiv 1\ (\operatorname{mod}\ N)$ has a unique solution for all $0 < a < N$; the solution is the [multiplicative inverse]{.hl}.
3. $x^2 \equiv a\ (\operatorname{mod}\ N)$ has either two solutions for all $0 < a < N$, or none.

</div>

---
layout: prism
heading: Proof by Counterexample
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The two most common ways of proving statements in data-structure analysis are proof by [induction]{.hl} and proof by [contradiction]{.hl}.

- The best way to prove a theorem *false* is by [exhibiting a counterexample]{.hl}.

<div class="theorem-box">
<div class="theorem-box-title">Theorem. The statement $F_k \leq k^2$ is false.</div>
<div class="theorem-box-body">

The easiest way to prove this is to compute $F_{13} = 233 > 13^2 = 169$.

</div>
</div>

---
layout: prism
heading: Proof by Induction
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- A [proof by induction]{.hl} has two standard parts:
  - a *base case* — establish that the theorem holds for some small value(s); usually trivial.
  - an *inductive hypothesis* — assume the theorem holds up to some limit $k$, then show it for $k+1$.

<div class="theorem-box">
<div class="theorem-box-title">Theorem. The Fibonacci numbers satisfy $F_i < (5/3)^i$.</div>
<div class="theorem-box-body">

$F_1 = 1 < 5/3$ and $F_2 = 1 < 25/9$. Then

$$
F_{k+1} = F_k + F_{k-1} < (5/3)^k + (5/3)^{k-1} < (24/25)(5/3)^{k+1} < (5/3)^{k+1}.
$$

</div>
</div>

---
layout: prism
heading: Proof by Contradiction
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [proof by contradiction]{.hl} assumes the theorem is false and shows this implies that some known property is false — hence the assumption was wrong.

<div class="theorem-box">
<div class="theorem-box-title">Theorem. There is an infinite number of primes.</div>
<div class="theorem-box-body">

Assume the theorem is false, so there is a largest prime $P_k$. Let $P_1, P_2, \ldots, P_k$ be all primes in order, and consider $N = P_1 P_2 \cdots P_k + 1$. Then $N > P_k$, so by assumption $N$ is not prime. But none of $P_1, \ldots, P_k$ divides $N$ exactly (there is always a remainder of $1$) — a contradiction, since every number is either prime or a product of primes. Hence the theorem is true.

</div>
</div>

---
layout: prism
heading: A Brief Introduction to Recursion
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Most familiar functions have a simple formula, but some are defined less conventionally.
  - On the nonnegative integers, define $f$ by $f(0) = 0$ and $f(x) = 2 f(x-1) + x^2$.

- A function defined in terms of itself is [recursive]{.hl}. C++ (like many modern languages) allows recursive functions.

</div>
<div>

```cpp
int f(int x) {
    if (x == 0)   // base case
        return 0;
    else          // recursive call
        return 2 * f(x - 1) + x * x;
}
```

</div>
</div>

---
layout: prism
heading: Recursion — Common Pitfalls
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The computer automatically does the bookkeeping for pending recursive calls and their variables.
  - Calls continue until a base case is reached — evaluating `f(-1)` calls `f(-2)`, `f(-3)`, … and never terminates.

- A subtler error: the code below gives no clue what `bad(1)` actually is.

</div>
<div>

```cpp
int bad(int n) {
    if (n == 0)   // looks like a base case
        return 0;
    else          // cannot estimate bad(1)
        return bad(n / 3 + 1) + n - 1;
}
```

</div>
</div>

---
layout: prism
heading: Recursion — Printing a Number
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- These lead to the first two fundamental rules of recursion:
  - Always have a *base case* solvable without recursion.
  - Every recursive call must make *progress* toward a base case.

- Suppose we can only output a single digit via `printDigit`. Recursion gives a clean solution.

</div>
<div>

```cpp
void printOut(int n) { // print nonnegative n
    if (n >= 10)
        printOut(n / 10);
    printDigit(n % 10);
}
```

</div>
</div>

---
layout: prism
heading: Recursion and Induction
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- We can prove the number-printing program correct using induction.

<div class="theorem-box">
<div class="theorem-box-title">Theorem. The recursive number-printing algorithm is correct for $n \geq 0$.</div>
<div class="theorem-box-body">

If $n$ has one digit, the program is trivially correct — it just calls `printDigit`. Assume `printOut` works for all numbers of $k$ or fewer digits. A $(k+1)$-digit number is its first $k$ digits followed by its last digit. The first $k$ digits form exactly $\lfloor n/10 \rfloor$, printed correctly by the inductive hypothesis, and the last digit is $n \bmod 10$. Thus every number is printed correctly.

</div>
</div>

- When designing a recursive program, all smaller instances on the path to a base case may be *assumed* correct.

---
layout: prism
heading: The Four Rules of Recursion
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The recursive program only needs to combine solutions of smaller problems — this is the *third* rule: assume all recursive calls work.

- The main cost of recursion is hidden bookkeeping; do not use it as a substitute for a simple `for` loop.

- The four basic rules of recursion:

<div class="sub-item-enum">

1. *Base cases.* Always have base cases solvable without recursion.
2. *Making progress.* Recursive calls must progress toward a base case.
3. *Design rule.* Assume that all recursive calls work.
4. *Compound interest rule.* Never duplicate work by solving the same instance in separate recursive calls.

</div>

---
layout: prism
heading: "DIY: Tracing Recursion"
---

<div style="height: 0.3rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// f(0) = 0,  f(x) = 2 f(x-1) + x^2
int f(int x) {
    if (x == 0) return 0;         // base case
    return 2 * f(x - 1) + x * x;  // recursive call
}

void printDigit(int d) { cout << d; }   // the only output routine we have

void printOut(int n) {                  // print a nonnegative integer
    if (n >= 10) printOut(n / 10);
    printDigit(n % 10);
}

int main() {
    for (int x = 0; x <= 5; x++)
        cout << "f(" << x << ") = " << f(x) << "\n";
    cout << "printOut(31415) -> ";
    printOut(31415);
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Mathematics Review</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">C++ Classes</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Basic <code>class</code> Syntax</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Extra Constructor Syntax and Accessors</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>vector</code> and <code>string</code></span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ Details</span></p>
  </div>

</div>

---
layout: prism
heading: "Basic class Syntax"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- All of our data structures will be [objects]{.hl} that store data and provide functions manipulating that collection. In C++ this is done with a [class]{.hl}.

- A class consists of its [members]{.hl}, which are either data or functions.
  - The functions are [member functions]{.hl} (often called [methods]{.hl}).
  - Each instance of a class is an [object]{.hl}, containing the data components specified in the class (unless declared `static`).

- We will implement an `IntCell` class: it holds a single data member `storedValue`, with four methods — `read`, `write`, and two constructors.

---
layout: prism
heading: "Basic class Syntax — IntCell"
---

```cpp
class IntCell {                 // Simulating an integer memory cell
public:
    IntCell() {                 // Constructor
        storedValue = 0;
    }
    IntCell(int initialValue) { // Constructor with parameter
        storedValue = initialValue;
    }
    int read() {                // return the stored value
        return storedValue;
    }
    void write(int x) {         // change the stored value to x
        storedValue = x;
    }

private:
    int storedValue;
};
```

---
layout: prism
heading: "Basic class Syntax — Visibility"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The labels `public` and `private` determine the visibility of class members.
  - A `public` member may be accessed by any method in any class.
  - A `private` member may only be accessed by methods in its own class.

- Typically, data members are `private` while general-use methods are `public`, restricting access to internal details — this is [information hiding]{.hl}.

- The two [constructors]{.hl} describe how an instance of the class is *constructed*.

---
layout: prism
heading: Extra Constructor Syntax and Accessors
---

<div style="height: 0.4rem;"></div>

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
heading: "Constructors: Defaults, Lists, explicit"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The [default parameter]{.hl} `0` means `0` is used when no argument is provided — effectively two constructors from one.

- The [initialization list]{.hl} `: storedValue{initialValue}` initializes data members directly.

- The constructor is [explicit]{.hl}: we make all one-parameter constructors `explicit` to avoid behind-the-scenes type conversions.

- A method that examines but does not change the object's state is an [accessor]{.hl}; one that changes it is a [mutator]{.hl}. Here `read` is an accessor, so it is a [constant member function]{.hl} (`const`).

---
layout: prism
heading: "vector and string"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The C++ standard library defines two useful classes: [`vector`]{.hl} and [`string`]{.hl}.

- `vector` is intended to replace the troublesome built-in C++ array.

```cpp
// int squares[] = {1, 4, 9, 16, 25, 36, 49, 64, 81};
vector<int> squares = {1, 4, 9, 16, 25, 36, 49, 64, 81};
```

- `string` supports all relational and equality operators (`str1 == str2` is `true` when the values match) and a `length` method returning the string length.

---
layout: prism
heading: "vector and string — Iteration"
---

<div class="grid grid-cols-3 gap-3" style="margin-top: 0.6rem;">
<div>

Indexing with `[]`:

```cpp
int sum = 0;
for (int i = 0;
     i < squares.size();
     i++)
    sum += squares[i];
```

</div>
<div>

Range `for`:

```cpp
int sum = 0;
for (int x : squares)
    sum += x;
```

</div>
<div>

With `auto`:

```cpp
int sum = 0;
for (auto x : squares)
    sum += x;
```

</div>
</div>

<div style="margin-top: 1rem;"></div>

- The [range `for`]{.hl} syntax iterates directly over elements, and [`auto`]{.hl} lets the compiler infer the appropriate type automatically.

---
layout: prism
heading: "DIY: IntCell and vector"
---

<div style="height: 0.3rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class IntCell {
public:
    explicit IntCell(int initialValue = 0) : storedValue{initialValue} {}
    int read() const { return storedValue; }
    void write(int x) { storedValue = x; }
private:
    int storedValue;
};

int main() {
    IntCell c;                       // default value 0
    c.write(5);
    cout << "IntCell after write(5): " << c.read() << "\n";

    vector<int> squares = {1, 4, 9, 16, 25, 36, 49, 64, 81};
    int sum = 0;
    for (auto x : squares) sum += x; // range-based for + auto
    cout << "sum of squares = " << sum << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Mathematics Review</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ Classes</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">C++ Details</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Pointers</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Lvalues, Rvalues, and References</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Big-Five</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Templates</span></p>
  </div>

</div>

---
layout: prism
heading: Pointers
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [pointer variable]{.hl} stores the *address* where another object resides — the fundamental mechanism behind many data structures.

- The code dynamically allocates an `IntCell`.

- The [address-of operator]{.hl} `&` returns the memory location where an object resides.

</div>
<div>

```cpp
int main() {
    IntCell* m;  // m is a pointer

    m = new IntCell{0};  // dynamic allocation
    m->write(5);
    cout << "Cell contents: "
         << m->read() << endl;

    delete m;  // free the memory
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: Lvalues, Rvalues, and References
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- An [lvalue]{.hl} identifies a non-temporary object.

- An [rvalue]{.hl} identifies a temporary object, or a value (such as a literal) not associated with any object.

</div>
<div>

```cpp
vector<string> arr(3);
const int x = 2;
int y;
int z = x + y;
string str = "foo";
vector<string>* ptr = &arr;
```

</div>
</div>

- `arr`, `str`, `arr[x]`, `&x`, `y`, `z`, `ptr`, `*ptr`, `(*ptr)[x]` are all [lvalues]{.hl}.
- `2`, `"foo"`, `x + y`, `str.substr(0, 1)` are all [rvalues]{.hl}.

---
layout: prism
heading: Lvalue References
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- An [lvalue reference]{.hl} is declared with `&` after a type; it becomes a synonym — another name — for the object it references.

- An lvalue reference cannot bind to a temporary (an rvalue), so the last three lines are compile errors.

</div>
<div>

```cpp
string str = "hell";
string& rstr = str;  // another name for str
rstr += "o";         // changes str to "hello"
bool cond = (&str == &rstr);  // true

string& bad1 = "hello";          // error
string& bad2 = str + "";         // error
string& sub  = str.substr(0, 4); // error
```

</div>
</div>

---
layout: prism
heading: Rvalue References
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- An [rvalue reference]{.hl} is declared with `&&` after a type.

- It has the same characteristics as an lvalue reference, except that — unlike an lvalue reference — it can also bind to an rvalue (a temporary).

- Hence all three declarations are now legal.

</div>
<div>

```cpp
string str = "hell";

string&& bad1 = "hello";          // legal
string&& bad2 = str + "";         // legal
string&& sub  = str.substr(0, 4); // legal
```

</div>
</div>

---
layout: prism
heading: The Big-Five
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- C++ classes come with *five* special functions, already written by default: the [destructor]{.hl}, [copy constructor]{.hl}, [move constructor]{.hl}, [copy assignment operator]{.hl}, and [move assignment operator]{.hl}.

- The [destructor]{.hl} is called whenever an object goes out of scope or is subjected to a `delete`.

- Two special constructors build a new object initialized to the same state as another object of the same type:
  - the [copy constructor]{.hl} if the source is an lvalue, and the [move constructor]{.hl} if it is an rvalue (a temporary about to be destroyed anyway).

---
layout: prism
heading: The Big-Five — Assignment
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The assignment operator is called when `=` is applied to two already-constructed objects.

- `lhs = rhs` copies the state of `rhs` into `lhs`:
  - via the [copy assignment operator]{.hl} if `rhs` is an lvalue,
  - via the [move assignment operator]{.hl} if `rhs` is an rvalue.

</div>
<div>

```cpp
// signatures for IntCell
~IntCell();                    // destructor
IntCell(const IntCell& rhs);   // copy ctor
IntCell(IntCell&& rhs);        // move ctor
IntCell& operator=
    (const IntCell& rhs);      // copy assign
IntCell& operator=
    (IntCell&& rhs);           // move assign
```

</div>
</div>

---
layout: prism
heading: Function Templates
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- For a *type-independent* algorithm, we prefer to write the code once rather than recode it per type.
  - Such [generic algorithms]{.hl} are written in C++ using [templates]{.hl}.

- A [function template]{.hl} is not an actual function but a *pattern* for one.

</div>
<div>

```cpp
template <typename Comparable>
const Comparable& findMax(
        const vector<Comparable>& a) {
    int maxIndex = 0;
    for (int i = 1; i < a.size(); i++)
        if (a[maxIndex] < a[i])
            maxIndex = i;
    return a[maxIndex];
}
```

</div>
</div>

---
layout: prism
heading: Function Templates — Instantiation
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Function templates are expanded automatically as needed; each expansion generates code, known as [code bloat]{.hl}.

- `findMax(v4)` fails because `operator<` is not defined for `IntCell`.

</div>
<div>

```cpp
int main() {
    vector<int> v1(37);
    vector<double> v2(40);
    vector<string> v3(80);
    vector<IntCell> v4(75);
    // Assume the vectors are filled.
    cout << findMax(v1) << endl; // int
    cout << findMax(v2) << endl; // double
    cout << findMax(v3) << endl; // string
    cout << findMax(v4) << endl; // error!
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: Class Templates
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A [class template]{.hl} works much like a function template.

- `MemoryCell` is like `IntCell` but works for any type `Object` that has a zero-parameter constructor, a copy constructor, and a copy assignment operator.

</div>
<div>

```cpp
template <typename Object>
class MemoryCell {
public:
    explicit MemoryCell(
        const Object& initialValue = Object{})
        : storedValue{initialValue} {}
    const Object& read() const {
        return storedValue;
    }
    void write(const Object& x) {
        storedValue = x;
    }
private:
    Object storedValue;
};
```

</div>
</div>

---
layout: prism
heading: Class Templates — Usage
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `Object` is passed by constant reference, and the default parameter is *not* `0` (which might be an invalid `Object`).
  - Instead, the default is an `Object` built with its zero-parameter constructor, `Object{}`.

</div>
<div>

```cpp
int main() {
    MemoryCell<int> m1;
    MemoryCell<string> m2{"hello"};

    m1.write(37);
    m2.write(m2.read() + " world");
    cout << m1.read() << endl
         << m2.read() << endl;

    return 0;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: Function and Class Templates"
---

<div style="height: 0.3rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

template <typename Comparable>
const Comparable& findMax(const vector<Comparable>& a) {
    int maxIndex = 0;
    for (int i = 1; i < (int)a.size(); i++)
        if (a[maxIndex] < a[i]) maxIndex = i;
    return a[maxIndex];
}

template <typename Object>
class MemoryCell {
public:
    explicit MemoryCell(const Object& initialValue = Object{}) : storedValue{initialValue} {}
    const Object& read() const { return storedValue; }
    void write(const Object& x) { storedValue = x; }
private:
    Object storedValue;
};

int main() {
    vector<int> vi = {3, 1, 4, 1, 5, 9, 2, 6};
    vector<string> vs = {"apple", "pear", "kiwi", "fig"};
    cout << "findMax(int)    = " << findMax(vi) << "\n";
    cout << "findMax(string) = " << findMax(vs) << "\n";

    MemoryCell<string> m{"hello"};
    m.write(m.read() + " world");
    cout << "MemoryCell      = " << m.read() << endl;
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
