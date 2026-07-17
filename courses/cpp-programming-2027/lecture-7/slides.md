---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 7
download: true
info: |
  ## C++ Programming Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-7-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 07: Midterm Review</p>

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
heading: Midterm Review
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- This week we [recap]{.hl} the core control-flow and type concepts covered so far, and preview the [midterm exam]{.hl}:

  - [Selection]{.hl}: `if-else`, logical operators, `switch`, and conditional (ternary) expressions.

  - [Data]{.hl}: mathematical functions, `char`, `string`, and stream manipulators.

  - [Repetition]{.hl}: `while`, `do-while`, and `for` loops.

- We close with a walkthrough of representative [midterm problems]{.hl} (about 15 problems, 30 points).

---
layout: prism
heading: "Recap: if-else Statements"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [Yes/No decision]{.hl} is expressed in C++ using [`true`/`false`]{.hl} values.
  - A [logical expression]{.hl} evaluates to `true` when its condition is satisfied, `false` otherwise.
  - In C++, `true` and `false` are [reserved words]{.hl}.

```text
if (boolean-expression) {
    statement(s)-for-the-true-case;
} else {
    statement(s)-for-the-false-case;
}
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int score = 72;
    if (score >= 60)
        cout << "Pass" << endl;
    else
        cout << "Fail" << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Logical Operators"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- C++ provides three [logical operators]{.hl} to combine or negate boolean values.

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

| Operator | Name | Description |
|:--------:|:----:|:------------|
| `!` | not | logical negation |
| `&&` | and | logical conjunction |
| `\|\|` | or | logical disjunction |

</div>
<div>

| `p1` | `p2` | `p1 && p2` | `p1 \|\| p2` |
|:----:|:----:|:----------:|:-----------:|
| false | false | false | false |
| false | true  | false | true  |
| true  | false | false | true  |
| true  | true  | true  | true  |

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 24, weight = 140;
    cout << boolalpha;
    cout << (age > 18 && weight == 150) << endl; // false
    cout << (age > 18 || weight == 150) << endl; // true
    cout << !(age > 18) << endl;                 // false
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: switch Statements"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [`switch`]{.hl} statement selects one branch out of many based on a single expression; each `case` usually ends with [`break`]{.hl}, and [`default`]{.hl} handles the rest.

```text
switch (switch-expression) {
    case value1: statement(s)1; break;
    case value2: statement(s)2; break;
    ...
    case valueN: statement(s)N; break;
    default:     statement(s)-for-default;
}
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int day = 3;
    switch (day) {
        case 1: cout << "Mon"; break;
        case 2: cout << "Tue"; break;
        case 3: cout << "Wed"; break;
        default: cout << "Other";
    }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Conditional Expressions"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- The [conditional expression]{.hl} has the syntax `boolean-expression ? expression1 : expression2`.
  - The `?` and `:` form a [ternary operator]{.hl} — it takes [three operands]{.hl}.
  - It is the [only]{.hl} ternary operator in C++.

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

```cpp
if (x > 0)
    y = 1;
else
    y = -1;
```

</div>
<div>

```cpp
y = x > 0 ? 1 : -1;
```

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = -4;
    int y = x > 0 ? 1 : -1;
    cout << "y = " << y << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Mathematical Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- `min`, `max`, and `abs` live in the [`cstdlib`]{.hl} header; the trigonometric, exponent, and rounding functions are in the [`cmath`]{.hl} header.

| Function | Description | Function | Description |
|:---------|:------------|:---------|:------------|
| `sin/cos/tan(x)` | trigonometric (radians) | `pow(a, b)` | $a^b$ |
| `asin/acos/atan(x)` | inverse trigonometric | `sqrt(x)` | $\sqrt{x}$, $x \ge 0$ |
| `exp(x)` | $e^x$ | `ceil(x)` | round up (as `double`) |
| `log(x)` / `log10(x)` | $\ln x$ / $\log_{10} x$ | `floor(x)` | round down (as `double`) |

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    cout << sqrt(16.0) << endl;   // 4
    cout << pow(2.0, 10) << endl; // 1024
    cout << ceil(3.2) << " " << floor(3.8) << endl; // 4 3
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Character"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- Most computers use [ASCII]{.hl} (American Standard Code for Information Interchange), an 8-bit scheme; the size of `char` is [1 byte]{.hl}. A `char` behaves like a small integer: `char ch = 'a'; cout << ++ch;` prints `b`.

| Function | Description | Function | Description |
|:---------|:------------|:---------|:------------|
| `isdigit(ch)` | is a digit | `isupper(ch)` | is uppercase |
| `isalpha(ch)` | is a letter | `isspace(ch)` | is whitespace |
| `isalnum(ch)` | is a letter or digit | `tolower(ch)` | to lowercase |
| `islower(ch)` | is lowercase | `toupper(ch)` | to uppercase |

<CppRunner>

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char ch = 'a';
    cout << ++ch << endl;                 // b
    cout << (char)toupper('c') << endl;   // C
    cout << isdigit('7') << endl;         // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: The string Type"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- A [`string`]{.hl} represents a sequence of characters: `string message = "Programming is fun";`.
  - `string` is not a primitive type but an [object type]{.hl}.
  - The relational operators `==`, `!=`, `<`, `<=`, `>`, `>=` compare two strings.

| Function | Description |
|:---------|:------------|
| `length()` | number of characters in the string |
| `size()`   | same as `length()` |
| `at(index)` | the character at the given index |

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string message = "Programming is fun";
    cout << message.length() << endl;   // 18
    cout << message.at(0) << endl;      // P
    cout << ("apple" < string("banana")) << endl; // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Manipulators"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- C++ provides [stream manipulators]{.hl} for controlling how a value is displayed.

| Operator | Description |
|:---------|:------------|
| `setprecision(n)` | sets the precision of a floating-point number |
| `fixed` | displays floating-point numbers in fixed-point notation |
| `showpoint` | shows the decimal point and trailing zeros |
| `setw(width)` | specifies the width of a print field |
| `left` / `right` | left- / right-justifies the output |

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << fixed << setprecision(2) << 3.14159 << endl; // 3.14
    cout << setw(6) << right << 42 << endl;              // "    42"
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: while Loops"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [`while`]{.hl} loop executes its body repeatedly [while the condition is true]{.hl}. One execution of the body is called an [iteration]{.hl}.

```text
while (loop-continuation-condition) {
    // Loop body
    Statement(s);
}
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 0;
    while (count < 3) {
        cout << "Welcome to C++!\n";
        count++;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: do-while Loops"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [`do-while`]{.hl} loop is like a `while` loop, except it [executes the body first]{.hl} and then checks the loop-continuation condition — so the body always runs at least once.

```text
do {
    // Loop body
    Statement(s);
} while (loop-continuation-condition);
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;
    do {
        cout << n << " ";
        n--;
    } while (n > 0);
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: for Loops"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [`for`]{.hl} loop offers a concise syntax that groups the [initial action]{.hl}, [continuation condition]{.hl}, and [action after each iteration]{.hl} in one header.

```text
for (initial-action; loop-continuation-condition; action-after-each-iteration) {
    // Loop body
    Statement(s);
}
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    for (int i = 1; i <= 10; i++)
        sum += i;
    cout << "sum = " << sum << endl; // 55
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Midterm Exam (1/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- The exam is worth [30 points]{.hl}, about [15 problems]{.hl}, written in Korean.

<div class="theorem-box">
<div class="theorem-box-title">O-X Quizzes</div>
<div class="theorem-box-body">

1. The conditional expression `boolean-expression ? a : b` is the only ternary operator in C++.  ( &nbsp;&nbsp; )
2. `return` may be used as a variable name.  ( &nbsp;&nbsp; )

</div>
</div>

<div class="theorem-box">
<div class="theorem-box-title">Predict the output</div>
<div class="theorem-box-body">

```cpp
cout << 'a' + 3 << endl;
cout << static_cast<int>('a' + 7) << endl;
cout << 2 * (3 / 6) + 4 << endl;
int a = 4 < 3 ? 1 : 0;
int b;
if (a) { b = 1; } else { b = 30; }
cout << b << endl;
```

</div>
</div>

---
layout: prism
heading: "Midterm Exam (1/7) — Solution"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [O-X]{.hl}: (1) **O** — the ternary operator is C++'s only three-operand operator.  (2) **X** — `return` is a reserved word, so it cannot be an identifier.

- [Output]{.hl}: `'a'` is `97`, so `'a'+3 = 100`; `'a'+7 = 104`; integer `3/6 = 0`, so `2*0+4 = 4`; `4<3` is false so `a=0`, giving `b=30`.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << 'a' + 3 << endl;                       // 100
    cout << static_cast<int>('a' + 7) << endl;     // 104
    cout << 2 * (3 / 6) + 4 << endl;               // 4
    int a = 4 < 3 ? 1 : 0;                         // a = 0
    int b;
    if (a) { b = 1; } else { b = 30; }
    cout << b << endl;                             // 30
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Midterm Exam (2/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [Using selection and repetition]{.hl}: write a pseudo-algorithm for each task.

<div class="theorem-box">
<div class="theorem-box-title">Pseudo-Algorithm Problems</div>
<div class="theorem-box-body">

1. Read three integers and print them in [ascending order]{.hl}.
2. Read two integers and compute their [least common multiple (LCM)]{.hl}.
3. Read an integer $n$ ($1 \le n \le 15$) and print a [number pyramid]{.hl}, as shown below for `n = 7`.

```text
Enter the number of lines: 7
            1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
  6 5 4 3 2 1 2 3 4 5 6
7 6 5 4 3 2 1 2 3 4 5 6 7
```

</div>
</div>

---
layout: prism
heading: "Midterm Exam (2/7) — Sort Three Integers"
---

<CppRunner stdin="7 3 5">

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    // Sort ascending with pairwise swaps
    if (a > b) { int t = a; a = b; b = t; }
    if (a > c) { int t = a; a = c; c = t; }
    if (b > c) { int t = b; b = c; c = t; }

    cout << a << " " << b << " " << c << endl; // 3 5 7
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Midterm Exam (2/7) — Least Common Multiple"
---

<CppRunner stdin="4 6">

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    // Euclidean algorithm for the greatest common divisor
    int x = a, y = b;
    while (y != 0) {
        int r = x % y;
        x = y;
        y = r;
    }
    int gcd = x;
    int lcm = a / gcd * b;

    cout << "LCM = " << lcm << endl; // 12
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Midterm Exam (2/7) — Number Pyramid"
---

<CppRunner stdin="7">

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int row = 1; row <= n; row++) {
        for (int col = 1; col <= n - row; col++)
            cout << "   ";                 // leading spaces
        for (int num = row; num >= 1; num--)
            cout << setw(3) << num;        // descending part
        for (int num = 2; num <= row; num++)
            cout << setw(3) << num;        // ascending part
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Midterm Exam (3/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [Using `break` and `continue`]{.hl}: trace the code below. What is printed with `continue`? What if `continue` is replaced by `break`?

<div class="theorem-box">
<div class="theorem-box-title">Trace the loop</div>
<div class="theorem-box-body">

```cpp
int main() {
    int sum = 0, num = 0;
    while (num < 20) {
        num++;
        if (num % 2 == 0 && num % 3 == 0) {
            continue; // break;
        }
        sum += num;
    }
    cout << sum << endl;
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: "Midterm Exam (3/7) — Solution"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- The condition `num % 2 == 0 && num % 3 == 0` is true exactly when `num` is a multiple of [6]{.hl} (`6, 12, 18`).
  - With [`continue`]{.hl}: those three are skipped, so `sum = (1+...+20) - (6+12+18) = 210 - 36 = ` **174**.
  - With [`break`]{.hl}: the loop stops at the first multiple of 6 (`num = 6`), so `sum = 1+2+3+4+5 = ` **15**.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int sumC = 0, sumB = 0, num;

    num = 0;
    while (num < 20) {          // continue version
        num++;
        if (num % 2 == 0 && num % 3 == 0) continue;
        sumC += num;
    }

    num = 0;
    while (num < 20) {          // break version
        num++;
        if (num % 2 == 0 && num % 3 == 0) break;
        sumB += num;
    }

    cout << "continue -> " << sumC << endl; // 174
    cout << "break    -> " << sumB << endl; // 15
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Midterm Exam (4/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [Data types and type conversion]{.hl}: `int`, `double`, `bool`, `char`, `string`. Find and fix the errors below.

<div class="theorem-box">
<div class="theorem-box-title">(a) Compile error</div>
<div class="theorem-box-body">

```cpp
string message = 'Welcome to C++!'
```

</div>
</div>

<div class="theorem-box">
<div class="theorem-box-title">(b) Compiles, but logically wrong — sum of 0.01, 0.02, ..., 0.99, 1</div>
<div class="theorem-box-body">

```cpp
double sum = 0;
for (double i = 0.01; i <= 1.0; i = i + 0.01)
    sum += i;
cout << "The sum is " << sum << endl;
```

</div>
</div>

---
layout: prism
heading: "Midterm Exam (4/7) — Solution"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [(a)]{.hl} A `string` literal needs [double quotes]{.hl}, and the statement needs a semicolon: `string message = "Welcome to C++!";`.

- [(b)]{.hl} `0.01` is not exactly representable, so the accumulated `i` may overshoot `1.0` and the last term is dropped, plus rounding error grows. Loop over an [integer counter]{.hl} instead.

<CppRunner>

```cpp
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
    string message = "Welcome to C++!"; // (a) fixed
    cout << message << endl;

    double sum = 0;                      // (b) fixed: integer counter
    for (int i = 1; i <= 100; i++)
        sum += i / 100.0;
    cout << fixed << setprecision(2)
         << "The sum is " << sum << endl; // 50.50
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Midterm Exam (5/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [Operators and evaluation order]{.hl}: predict every line of output.

<div class="theorem-box">
<div class="theorem-box-title">Predict the output</div>
<div class="theorem-box-body">

```cpp
int a = 10;
cout << a++ << endl;
cout << ++a << endl;
cout << a-- << endl;
cout << --a << endl;
a *= 2;
cout << a << endl;
int b = 20;
bool c;
c = a == b;
cout << c << endl;
b -= 5;
c = !(a < b);
cout << c << endl;
```

</div>
</div>

---
layout: prism
heading: "Midterm Exam (5/7) — Solution"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [Post-]{.hl} vs [pre-increment]{.hl}: `a++` prints then increments; `++a` increments then prints. Tracing `a`: `10 → 11 → 12 → 11 → 10`, then `a *= 2 → 20`.
  - `a == b` is `20 == 20 → 1`; after `b -= 5` (`b = 15`), `!(20 < 15) → !false → 1`.
- [Output]{.hl}: `10`, `12`, `12`, `10`, `20`, `1`, `1`.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10;
    cout << a++ << endl;  // 10
    cout << ++a << endl;  // 12
    cout << a-- << endl;  // 12
    cout << --a << endl;  // 10
    a *= 2;
    cout << a << endl;    // 20
    int b = 20;
    bool c;
    c = a == b;
    cout << c << endl;    // 1
    b -= 5;
    c = !(a < b);
    cout << c << endl;    // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Midterm Exam (6/7)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [Math-function problem]{.hl} (fill in the blanks). Write a program that reads the length $r$ from the center of a [pentagon]{.hl} to a vertex and computes its area.

$$
\text{Area} = \frac{5 \times s^2}{4 \times \tan\!\left(\dfrac{\pi}{5}\right)}, \quad s = 2r\sin\frac{\pi}{5}
$$

- Round to two decimals. Sample: `r = 5.5` gives area `71.92`.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w07/cpp-w07-image25.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Midterm Exam (6/7) — Solution"
---

<CppRunner stdin="5.5">

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    const double PI = 3.14159265358979323846;
    double r;
    cin >> r;                       // length center -> vertex

    double s = 2 * r * sin(PI / 5); // side length
    double area = (5 * s * s) / (4 * tan(PI / 5));

    cout << fixed << setprecision(2);
    cout << "The area of the pentagon is " << area << endl; // 71.92
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Midterm Exam (7/7)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [Monte-Carlo algorithm]{.hl} (write the pseudo-algorithm / fill in the blanks).

- A square is divided into four regions. If you throw a dart into the square [1,000,000]{.hl} times, what is the probability that it lands in an [odd-numbered region]{.hl} (1 or 3)?

- Simulate the process and display the result.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w07/cpp-w07-image27.png" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "Midterm Exam (7/7) — Solution"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- Sample a point in the square, classify its region, and count hits in the odd regions. The expected answer is about [0.625]{.hl}.

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
#include <iomanip>
using namespace std;

int main() {
    srand(42);
    const int N = 1000000;
    int odd = 0;
    for (int i = 0; i < N; i++) {
        double x = (double)rand() / RAND_MAX * 2.0; // [0, 2]
        double y = (double)rand() / RAND_MAX * 2.0;
        if (x < 1.0)               odd++;       // region 1 (left half)
        else if (y >= 1.0 && x + y < 3.0) odd++; // region 3 (inner triangle)
        // region 2 (outer triangle) and region 4 (bottom-right) are even
    }
    cout << fixed << setprecision(4);
    cout << "Probability (odd region) = " << (double)odd / N << endl;
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
