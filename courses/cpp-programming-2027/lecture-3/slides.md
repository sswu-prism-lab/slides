---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 3
download: true
info: |
  ## C++ Programming Lecture Slides
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">C++ Programming</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 03: Selections and Conditional Statements</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">Wonjun Ko, Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">Fall 2027</p>
</div>

---
layout: prism
heading: Selections and Conditional Statements
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Programs often need to choose *which* statements to run, depending on the circumstances. In this lecture we study C++'s [selection statements]{.hl}:

  - [Boolean values]{.hl} and [relational operators]{.hl} — how C++ decides *true* from *false*.

  - The [`if`]{.hl}, [`if-else`]{.hl}, [nested `if`]{.hl}, and [`switch`]{.hl} statements.

  - [Logical operators]{.hl}, [conditional expressions]{.hl}, and operator [precedence and associativity]{.hl}.

---
layout: prism
heading: Conditional Statement
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Normally, students come here to take the *C++ Programming* course.

- But suppose the actor Ha-neul Kang visits our campus for some reason.

- Then some students might *not* attend the course — the outcome [depends on a condition]{.hl}.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image2.png" class="tikz-fig" style="width: 60%; margin: 0 auto;" />

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image3.png" class="tikz-fig" style="width: 90%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: Making Decisions
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Simple serial execution of code would be boring and inefficient.
  - It would be nice to change *which* statements run and *when*, depending on the circumstances.

- A yes/no decision can drive many things. In computer science, we express this as [true / false]{.hl}.

- We determine true/false from [logical data]{.hl} and [logical operators]{.hl}.
  - If logical data satisfies some condition we consider it *true*; otherwise it is *false*.

- In C++, [`true`]{.hl} and [`false`]{.hl} are reserved words.

---
layout: prism
heading: True and False in the Arithmetic Scale
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- In C++, a value of [zero]{.hl} can be used as the logical value `false`.

- Any [non-zero]{.hl} value (e.g. `-1`, `18`, `3.5`) can be used as the logical value `true`.

- Try converting each variable on the right to a `bool`.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int   a = 3;     // true
    int   b = 0;     // false
    float c = 0.0;   // false
    float d = 2.9;   // true
    bool  e = true;  // true
    bool  f = false; // false
    bool  g = 1.4;   // true
    bool  h = 0;     // false

    cout << boolalpha;
    cout << "a=" << (bool)a << "  b=" << (bool)b << "\n";
    cout << "c=" << (bool)c << "  d=" << (bool)d << "\n";
    cout << "e=" << e << "  f=" << f << "\n";
    cout << "g=" << g << "  h=" << h << "\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: Relational Operators
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- We compare two values to decide [true / false]{.hl} using a [relational operator]{.hl} (관계 연산자).

<div style="margin-top: 1rem;"></div>

| Operator | Math symbol | Name | Example (`radius` is 5) | Result |
|:---:|:---:|:---|:---|:---:|
| `<`  | &lt; | less than | `radius < 0`  | false |
| `<=` | ≤ | less than or equal to | `radius <= 0` | false |
| `>`  | &gt; | greater than | `radius > 0`  | true |
| `>=` | ≥ | greater than or equal to | `radius >= 0` | true |
| `==` | = | equal to | `radius == 0` | false |
| `!=` | ≠ | not equal to | `radius != 0` | true |

- Note that the equality-testing sign is [`==`]{.hl}, **not** `=`. In C++, `=` is used for [assignment]{.hl}.

---
layout: prism
heading: Boolean Values
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A Boolean value is displayed as [`1`]{.hl} for a true statement and [`0`]{.hl} for a false statement.

- Let us assign `1` to `x` and check the results of each comparison.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 1;
    cout << (x > 0)  << endl;  // 1
    cout << (x < 0)  << endl;  // 0
    cout << (x != 0) << endl;  // 1
    cout << (x >= 0) << endl;  // 1
    cout << (x != 1) << endl;  // 0

    cout << (4 < 5) << endl;   // displays 1
    cout << (4 > 5) << endl;   // displays 0
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "if Statements (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- An [`if`]{.hl} statement lets a program specify an *alternative path of execution*.

- A [one-way `if`]{.hl} statement executes an action *if and only if* the condition is `true`.

```cpp
if (boolean-expression)
{
    statement(s);
}
```

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image6.png" class="tikz-fig" style="width: 75%; margin: 0 auto;" />

<div class="sub-item" style="text-align:center; margin-top: 0.6rem;">

Flow of a one-way `if` statement.

</div>

</div>
</div>

---
layout: prism
heading: "if Statements (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

The boolean-expression must be enclosed in [parentheses]{.hl}.

```cpp
// (a) Wrong
if i > 0
{
    cout << "i is positive" << endl;
}

// (b) Correct
if (i > 0)
{
    cout << "i is positive" << endl;
}
```

</div>
<div>

The braces can be [omitted]{.hl} if they enclose a *single* statement.

```cpp
// (a) with braces
if (i > 0)
{
    cout << "i is positive" << endl;
}

// (b) equivalent, braces omitted
if (i > 0)
    cout << "i is positive" << endl;
```

</div>
</div>

---
layout: prism
heading: "if Statements (3/3)"
---

<div style="height: 0.3rem;"></div>

<CppRunner stdin="10">

```cpp
#include <iostream>   // SimpleIfDemo.cpp
using namespace std;

int main() {
    // Prompt the user to enter an integer
    int number;
    cout << "Enter an integer: ";
    cin >> number;

    if (number % 5 == 0)
        cout << "HiFive" << endl;

    if (number % 2 == 0)
        cout << "HiEven" << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "if-else Statements (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- An [`if-else`]{.hl} statement decides which statements to execute based on whether the condition is `true` or `false`.

- A [two-way `if-else`]{.hl} statement specifies *different* actions for the two cases.

```cpp
if (boolean-expression)
{
    statement(s)-for-the-true-case;
}
else
{
    statement(s)-for-the-false-case;
}
```

</div>
<div>

<div style="height: 4rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image11.png" class="tikz-fig" style="width: 100%; margin: 0 auto;" />

<div class="sub-item" style="text-align:center; margin-top: 0.6rem;">

Flow of a two-way `if-else` statement.

</div>

</div>
</div>

---
layout: prism
heading: "if-else Statements (2/2)"
---

<div style="height: 0.3rem;"></div>

- Let us write a simple program that checks whether a number is [even or odd]{.hl} — obtained by changing the middle of `SimpleIfDemo.cpp`.

<CppRunner stdin="7">

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "Enter an integer: ";
    cin >> number;

    if (number % 2 == 0)
        cout << number << " is even.";
    else
        cout << number << " is odd.";

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Nested if and Multi-Way if-else (1/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- An `if` statement can be placed inside another `if` statement to form a [nested `if`]{.hl} (중첩 if) statement.

- The statement inside an `if` or `if-else` can be *any* legal C++ statement — including another `if` or `if-else`.

</div>
<div>

<div style="height: 2.5rem;"></div>

```cpp
if (i > k)
{
    if (j > k)
        cout << "i and j are greater than k"
             << endl;
}
else
    cout << "i is less than or equal to k"
         << endl;
```

</div>
</div>

---
layout: prism
heading: "Nested if and Multi-Way if-else (2/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

Deeply nested (harder to read):

```cpp
if (score >= 90.0)
    cout << "Grade is A";
else
    if (score >= 80.0)
        cout << "Grade is B";
    else
        if (score >= 70.0)
            cout << "Grade is C";
        else
            if (score >= 60.0)
                cout << "Grade is D";
            else
                cout << "Grade is F";
```

</div>
<div>

[Multi-way]{.hl} form (**preferred**):

```cpp
if (score >= 90.0)
    cout << "Grade is A";
else if (score >= 80.0)
    cout << "Grade is B";
else if (score >= 70.0)
    cout << "Grade is C";
else if (score >= 60.0)
    cout << "Grade is D";
else
    cout << "Grade is F";
```

</div>
</div>

---
layout: prism
heading: "Nested if and Multi-Way if-else (3/4)"
---

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image15.png" class="tikz-fig" style="width: 82%;" />
</div>

<div class="sub-item" style="text-align:center; margin-top: 0.8rem;">

A multi-way `if-else` statement used to assign a letter grade.

</div>

---
layout: prism
heading: "Nested if and Multi-Way if-else (4/4)"
---

<div style="height: 0.2rem;"></div>

- **DIY.** Suppose `x = 3` and `y = 4`; trace the code below. What is the output when `x = 3, y = 2`? When `x = 2, y = 2`?

<CppRunner stdin="3 4">

```cpp
#include <iostream>
using namespace std;

int main() {
    int x, y;
    cin >> x >> y;

    if (x > 2)
    {
        if (y > 2)
        {
            int z = x + y;
            cout << "z is " << z << endl;
        }
    }
    else
        cout << "x is " << x << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Common Errors and Pitfalls (1/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Common errors: forgetting necessary [braces]{.hl}, misplacing [semicolons]{.hl}, mistaking [`==` for `=`]{.hl}, and [dangling `else`]{.hl} (else 결합) clauses.

- Common pitfalls: [duplicated statements]{.hl} in `if-else`, and testing [equality of `double`]{.hl} values.

</div>
<div>

Forgetting necessary braces:

```cpp
// (a) Wrong — only the first line is guarded
if (radius >= 0)
    area = radius * radius * PI;
    cout << "The area is " << area;

// (b) Correct
if (radius >= 0)
{
    area = radius * radius * PI;
    cout << "The area is " << area;
}
```

</div>
</div>

---
layout: prism
heading: "Common Errors and Pitfalls (2/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

Wrong semicolon at the `if` line:

```cpp
// Logic error: empty body, {} runs always
if (radius >= 0);
{
    area = radius * radius * PI;
    cout << "The area is " << area;
}
```

</div>
<div>

Mistakenly using `=` for `==`:

```cpp
// (=) assigns 3 to count, always true!
if (count = 3)
    cout << "count is zero" << endl;
else
    cout << "count is not zero" << endl;

// Correct:  if (count == 3)
```

</div>
</div>

---
layout: prism
heading: "Common Errors and Pitfalls (3/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

Redundant testing of Boolean values:

```cpp
// (a) redundant
if (even == true)
    cout << "It is even.";

// (b) better
if (even)
    cout << "It is even.";
```

- The `else` binds to the [nearest]{.hl} unmatched `if` — *not* the indentation.

</div>
<div>

Dangling `else`:

```cpp
int i = 1, j = 2, k = 3;

// else actually matches the SECOND if
if (i > j)
    if (i > k)
        cout << "A";
    else
        cout << "B";

// force else to match the FIRST if:
if (i > j)
{
    if (i > k)
        cout << "A";
}
else
    cout << "B";
```

</div>
</div>

---
layout: prism
heading: "Common Errors and Pitfalls (4/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Floating-point numbers have [limited precision]{.hl}; calculations can introduce round-off errors, so an equality test of two `double` values is [not reliable]{.hl}.

- Instead, test whether the difference is smaller than a small [threshold]{.hl}. `fabs` / `abs` in `<cmath>` returns an absolute value.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x = 1.0 - 0.1 - 0.1 - 0.1 - 0.1 - 0.1;

    // Unreliable direct equality
    if (x == 0.5) cout << "x is 0.5\n";
    else          cout << "x is not 0.5\n";

    // Reliable threshold comparison
    const double EPSILON = 1E-14;
    if (fabs(x - 0.5) < EPSILON)
        cout << "x is approximately 0.5\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Common Errors and Pitfalls (5/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

Simplifying Boolean assignment:

```cpp
// (a) verbose
if (number % 2 == 0)
    even = true;
else
    even = false;

// (b) better
bool even = number % 2 == 0;
```

</div>
<div>

Avoiding duplicate code — [DRY]{.hl} ("don't repeat yourself"):

```cpp
// (a) duplicated cout
if (inState) {
    tuition = 5000;
    cout << "The tuition is " << tuition << endl;
} else {
    tuition = 15000;
    cout << "The tuition is " << tuition << endl;
}

// (b) print once
if (inState) tuition = 5000;
else         tuition = 15000;
cout << "The tuition is " << tuition << endl;
```

</div>
</div>

---
layout: prism
heading: "Common Errors and Pitfalls (6/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- In C++, a numeric value can be used as a Boolean, which may cause [logic errors]{.hl}.

- If `amount` is `40`, the code below prints *"Amount is more than 50"*, because `!amount` evaluates to `0` and `0 <= 50` is `true`.

- The not (`!`) operator negates `true`↔`false`.

</div>
<div>

```cpp
// Wrong: !amount is applied first
if (!amount <= 50)
    cout << "Amount is more than 50";
```

<div style="height: 1.5rem;"></div>

```cpp
// Correct: negate the whole comparison
if (!(amount <= 50))
    cout << "Amount is more than 50";
```

</div>
</div>

---
layout: prism
heading: "Practice: Computing Body Mass Index"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

- Write a [BMI]{.hl} program: compute in meters and kilograms, but read the input in [pounds and inches]{.hl}.

<div style="margin-top: 0.8rem;"></div>

| BMI | Interpretation |
|:---|:---|
| BMI &lt; 18.5 | Underweight |
| 18.5 ≤ BMI &lt; 25.0 | Normal |
| 25.0 ≤ BMI &lt; 30.0 | Overweight |
| 30.0 ≤ BMI | Obese |

</div>
<div>

<CppRunner stdin="146 70">

```cpp
#include <iostream>   // ComputeAndInterpretBMI.cpp
using namespace std;

int main() {
    double weight, height;
    cout << "Enter weight in pounds: ";
    cin >> weight;
    cout << "Enter height in inches: ";
    cin >> height;

    const double KILOGRAMS_PER_POUND = 0.45359237;
    const double METERS_PER_INCH = 0.0254;

    double kg = weight * KILOGRAMS_PER_POUND;
    double m  = height * METERS_PER_INCH;
    double bmi = kg / (m * m);

    cout << "BMI is " << bmi << endl;
    if (bmi < 18.5)      cout << "Underweight" << endl;
    else if (bmi < 25)   cout << "Normal" << endl;
    else if (bmi < 30)   cout << "Overweight" << endl;
    else                 cout << "Obese" << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Practice: Generating Random Numbers"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- A subtraction quiz for elementary students. Use `rand()` from `<cstdlib>` for numbers `0`–`9`.

- `rand()` alone repeats the same sequence; change the [seed]{.hl} with `srand`.
  - `srand(time(0))` uses the current time — seconds since 1970-01-01.

- Generate two single-digit integers, keep the answer non-negative, ask, then check.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>  // SubtractionQuiz.cpp
#include <ctime>     // for time()
#include <cstdlib>   // for rand() and srand()
using namespace std;

int main() {
    // In practice: srand(time(0));
    // Fixed seed here so the demo is reproducible.
    srand(1);
    int number1 = rand() % 10;
    int number2 = rand() % 10;

    if (number1 < number2) {   // avoid a negative answer
        int t = number1; number1 = number2; number2 = t;
    }

    cout << "What is " << number1 << " - " << number2 << "? ";
    int answer = number1 - number2;   // the student's input
    cout << answer << endl;

    if (number1 - number2 == answer)
        cout << "You are correct!" << endl;
    else
        cout << "Your answer is wrong." << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Logical Operators (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- Use [logical operators]{.hl} (논리 연산자, a.k.a. Boolean operators) to combine several conditions.

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

| Operator | Name | Description |
|:---:|:---|:---|
| `!`  | not | logical negation |
| `&&` | and | logical conjunction |
| `\|\|` | or | logical disjunction |

<div style="margin-top: 1rem;"></div>

| `p` | `!p` |
|:---:|:---:|
| true  | false |
| false | true  |

</div>
<div>

| `p1` | `p2` | `p1 && p2` | `p1 \|\| p2` |
|:---:|:---:|:---:|:---:|
| false | false | false | false |
| false | true  | false | true  |
| true  | false | false | true  |
| true  | true  | true  | true  |

</div>
</div>

---
layout: prism
heading: "Logical Operators (2/3)"
---

<div style="height: 0.2rem;"></div>

<CppRunner stdin="18">

```cpp
#include <iostream>   // TestBooleanOperators.cpp
using namespace std;

int main() {
    int number;
    cout << "Enter an integer: ";
    cin >> number;

    if (number % 2 == 0 && number % 3 == 0)
        cout << number << " is divisible by 2 and 3." << endl;

    if (number % 2 == 0 || number % 3 == 0)
        cout << number << " is divisible by 2 or 3." << endl;

    if ((number % 2 == 0 || number % 3 == 0) &&
        !(number % 2 == 0 && number % 3 == 0))
        cout << number << " is divisible by 2 or 3, but not both." << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Logical Operators (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- In mathematics `1 <= numDays <= 31` is correct, but in C++ it is [not]{.hl}.
  - C++ evaluates `1 <= numDays` to a `bool`, then compares that `bool` with `31` — a logic error.

- By [de Morgan's law]{.hl}, we can simplify Boolean expressions:

<div class="sub-item-enum">

1. `!(cond1 && cond2)` is the same as `!cond1 || !cond2`
2. `!(cond1 || cond2)` is the same as `!cond1 && !cond2`

</div>

---
layout: prism
heading: "Practice: Determining Leap Year"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A year is a [leap year]{.hl} (윤년) if it is divisible by `4` but *not* by `100`, **or** if it is divisible by `400`.

- We can combine the three tests into one Boolean expression:

```cpp
bool isLeapYear = (year % 4 == 0);
isLeapYear = isLeapYear && (year % 100 != 0);
isLeapYear = isLeapYear || (year % 400 == 0);
```

</div>
<div>

<CppRunner stdin="2020">

```cpp
#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "Enter a year: ";
    cin >> year;

    bool isLeapYear =
        (year % 4 == 0 && year % 100 != 0)
        || (year % 400 == 0);

    if (isLeapYear)
        cout << year << " is a leap year." << endl;
    else
        cout << year << " is not a leap year." << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "switch Statements (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A [`switch`]{.hl} statement executes statements based on the value of a variable or an expression.

- Overusing nested `if` statements makes a program hard to read.

- C++ provides `switch` to simplify coding for [multiple cases]{.hl}.

</div>
<div>

<div style="height: 2rem;"></div>

```cpp
switch (switch-expression)
{
    case value1: statement(s)1;
                 break;
    case value2: statement(s)2;
                 break;
    ...
    case valueN: statement(s)N;
                 break;
    default:     statement(s)-for-default;
}
```

</div>
</div>

---
layout: prism
heading: "switch Statements (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The `switch`-expression must yield an [integral value]{.hl} and be enclosed in parentheses.

- The `value1, …, valueN` are [integral constant expressions]{.hl} — no variables (e.g. `1 + x`) and no floating-point values.

- When a `case` value matches, execution starts there and continues until a [`break`]{.hl} or the end of the `switch`.

- The optional [`default`]{.hl} case runs when no `case` matches.

- The keyword `break` is optional, but it immediately ends the `switch` (otherwise execution *falls through*).

---
layout: prism
heading: "Practice: Chinese Zodiac"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

- Given a year, determine its [Chinese Zodiac]{.hl} (띠) using `year % 12`.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image41.png" class="tikz-fig" style="width: 78%; margin: 0.5rem auto;" />

</div>
<div>

<CppRunner stdin="1963">

```cpp
#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "Enter a year: ";
    cin >> year;

    switch (year % 12) {
        case 0:  cout << "monkey";  break;
        case 1:  cout << "rooster"; break;
        case 2:  cout << "dog";     break;
        case 3:  cout << "pig";     break;
        case 4:  cout << "rat";     break;
        case 5:  cout << "ox";      break;
        case 6:  cout << "tiger";   break;
        case 7:  cout << "rabbit";  break;
        case 8:  cout << "dragon";  break;
        case 9:  cout << "snake";   break;
        case 10: cout << "horse";   break;
        case 11: cout << "sheep";   break;
    }
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: Conditional Expressions
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [conditional expression]{.hl} evaluates an expression based on a condition:

```cpp
boolean-expression ? expression1 : expression2;
```

- The `?` and `:` form the [ternary operator]{.hl} — the only ternary operator in C++.

- The two forms below are equivalent:

```cpp
if (x > 0)
    y = 1;
else
    y = -1;

y = x > 0 ? 1 : -1;
```

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int x = -2; x <= 2; x++) {
        int y = x > 0 ? 1 : -1;
        cout << "x = " << x
             << " -> y = " << y << endl;
    }

    int a = 5, b = 8;
    int max = (a > b) ? a : b;   // pick the larger
    cout << "max(" << a << ", " << b
         << ") = " << max << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Operator Precedence and Associativity (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- Operator [precedence]{.hl} and [associativity]{.hl} determine the order in which operators are evaluated (highest at the top).

<div class="grid grid-cols-2 gap-6" style="margin-top: 0.8rem;">
<div>

| Precedence | Operator |
|:---:|:---|
| highest | `var++`, `var--` (postfix) |
| | `+`, `-` (unary), `++var`, `--var` (prefix) |
| | `static_cast<type>(v)`, `(type)` (casting) |
| | `!` (not) |
| | `*`, `/`, `%` (multiplicative) |
| | `+`, `-` (binary additive) |

</div>
<div>

| Precedence | Operator |
|:---:|:---|
| | `<`, `<=`, `>`, `>=` (relational) |
| | `==`, `!=` (equality) |
| | `&&` (and) |
| | `\|\|` (or) |
| lowest | `=`, `+=`, `-=`, `*=`, `/=`, `%=` (assignment) |

</div>
</div>

---
layout: prism
heading: "Operator Precedence and Associativity (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- If operators with the same precedence are next to each other, their [associativity]{.hl} decides the order of evaluation.

- All binary operators except assignment are [left associative]{.hl} (왼쪽 결합성):

```cpp
a - b + c - d   // is equivalent to   ((a - b) + c) - d
```

- Assignment operators are [right associative]{.hl} (오른쪽 결합성):

```cpp
a = b += c = 5   // is equivalent to   a = (b += (c = 5))
```

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
