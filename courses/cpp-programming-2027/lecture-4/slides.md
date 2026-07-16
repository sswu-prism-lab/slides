---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 4
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 04: Math Functions and Characters</p>

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
heading: "Recap: if-else Statements"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A *Yes/No* decision can drive many things; in computer science we phrase it as [true]{.hl} / [false]{.hl}.

- We determine true/false from *logical data* and *logical operators*.
  - If the logical data satisfies a condition, it is `true`; otherwise it is `false`.

- In C++, `true` and `false` are [reserved words]{.hl}.

</div>
<div>

<div style="height: 3rem;"></div>

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
</div>

---
layout: prism
heading: "Recap: Logical Operators"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- We use [logical operators]{.hl} (논리 연산자, a.k.a. Boolean operators) to combine several conditions.

<div class="grid grid-cols-3 gap-4" style="margin-top: 1.5rem;">
<div>

| Op | Name | Meaning |
|----|------|---------|
| `!` | not | negation |
| `&&` | and | conjunction |
| `\|\|` | or | disjunction |

</div>
<div>

| `p1` | `p2` | `p1 && p2` |
|------|------|-----------|
| false | false | false |
| false | true | false |
| true | false | false |
| true | true | true |

</div>
<div>

| `p1` | `p2` | `p1 \|\| p2` |
|------|------|-----------|
| false | false | false |
| false | true | true |
| true | false | true |
| true | true | true |

</div>
</div>

- The `!` operator simply flips a value: `!(age > 18)` is `false` when `age > 18` is `true`.

---
layout: prism
heading: "Practice: Determining Leap Year"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A year is a [leap year]{.hl} (윤년) if it is divisible by 4 but not by 100, **or** if it is divisible by 400.

- We can build the test up step by step, then combine everything into one Boolean expression.

</div>
<div>

```cpp
// divisible by 4
bool isLeapYear = (year % 4 == 0);
// ... but not by 100
isLeapYear = isLeapYear
           && (year % 100 != 0);
// ... or divisible by 400
isLeapYear = isLeapYear
           || (year % 400 == 0);
```

</div>
</div>

<CppRunner stdin="2000">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter a year: ";
    int year;
    cin >> year;

    bool isLeapYear = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    cout << year << (isLeapYear ? " is" : " is not") << " a leap year." << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "switch Statements (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [switch]{.hl} statement executes statements based on the value of a variable or an expression.

- Overusing nested `if` statements makes a program difficult to read.

- C++ provides a `switch` statement to simplify coding for *multiple cases*.

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
  margin-top: 0.85em;
}
</style>

- The `switch` statement observes the following rules:

  - The *switch-expression* must yield an [integral value]{.hl} and always be enclosed in parentheses.

  - `value1, ..., valueN` are integral *constant* expressions — they cannot contain variables (such as `1 + x`) and cannot be floating-point values.

  - When a `case` value matches the switch-expression, execution starts there and continues until a `break` or the end of the `switch` is reached.

  - The `default` case is *optional*; it runs when none of the specified cases matches.

  - The keyword `break` is *optional*, but it immediately ends the `switch` statement.

---
layout: prism
heading: "Practice: Chinese Zodiac"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- Given a year, determine its animal sign ([Chinese Zodiac]{.hl}, 띠) from `year % 12`.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp-2027/w04/cpp-w04-image8.png" class="tikz-fig" style="width: 70%;" />

</div>
<div>

<div style="height: 0.5rem;"></div>

| `year % 12` | Sign | `year % 12` | Sign |
|:-:|:--|:-:|:--|
| 0 | monkey | 6 | tiger |
| 1 | rooster | 7 | rabbit |
| 2 | dog | 8 | dragon |
| 3 | pig | 9 | snake |
| 4 | rat | 10 | horse |
| 5 | ox | 11 | sheep |

</div>
</div>

<CppRunner stdin="1963">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter a year: ";
    int year;
    cin >> year;

    switch (year % 12) {
        case 0:  cout << "monkey"  << endl; break;
        case 1:  cout << "rooster" << endl; break;
        case 2:  cout << "dog"     << endl; break;
        case 3:  cout << "pig"     << endl; break;
        case 4:  cout << "rat"     << endl; break;
        case 5:  cout << "ox"      << endl; break;
        case 6:  cout << "tiger"   << endl; break;
        case 7:  cout << "rabbit"  << endl; break;
        case 8:  cout << "dragon"  << endl; break;
        case 9:  cout << "snake"   << endl; break;
        case 10: cout << "horse"   << endl; break;
        case 11: cout << "sheep"   << endl; break;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Conditional Expressions"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [conditional expression]{.hl} evaluates an expression based on a condition:

  ```cpp
  boolean-expression ? expr1 : expr2;
  ```

- The `?` and `:` together form a [ternary operator]{.hl} — the only ternary operator in C++, using three operands.

</div>
<div>

<div style="height: 1rem;"></div>

```cpp
// if-else form
if (x > 0)
    y = 1;
else
    y = -1;

// equivalent conditional expression
y = x > 0 ? 1 : -1;
```

</div>
</div>

<CppRunner stdin="-5">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter x: ";
    int x;
    cin >> x;
    int y = x > 0 ? 1 : -1;   // sign of x
    cout << "y = " << y << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Operator Precedence and Associativity (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- Operator [precedence]{.hl} and [associativity]{.hl} determine the order in which operators are evaluated (highest at the top).

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

| Precedence | Operator |
|:-:|:--|
| 1 | `var++`, `var--` (Postfix) |
| 2 | `+`, `-` (Unary), `++var`, `--var` (Prefix) |
| 3 | `static_cast<type>(v)`, `(type)` (Casting) |
| 4 | `!` (Not) |
| 5 | `*`, `/`, `%` |
| 6 | `+`, `-` (Binary) |

</div>
<div>

| Precedence | Operator |
|:-:|:--|
| 7 | `<`, `<=`, `>`, `>=` (Relational) |
| 8 | `==`, `!=` (Equality) |
| 9 | `&&` (AND) |
| 10 | `\|\|` (OR) |
| 11 | `=`, `+=`, `-=`, `*=`, `/=`, `%=` (Assignment) |

</div>
</div>

---
layout: prism
heading: "Operator Precedence and Associativity (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- When operators with the *same* precedence sit next to each other, their [associativity]{.hl} decides the order of evaluation.

- All binary operators *except* assignment are [left associative]{.hl} (왼쪽 결합성):

```text
a - b + c - d   is equivalent to   ((a - b) + c) - d
```

- Assignment operators are [right associative]{.hl} (오른쪽 결합성):

```text
a = b += c = 5   is equivalent to   a = (b += (c = 5))
```

---
layout: prism
heading: "Mathematical Functions"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Suppose you must estimate the area enclosed by four cities, given their [GPS locations]{.hl}.

- How would you write a program to solve this?

- We split the quadrilateral into two triangles, estimate each triangle's area, and add them.

</div>
<div>

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp-2027/w04/cpp-w04-image12.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Trigonometric Functions (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- C++ provides many useful functions in the [`<cmath>`]{.hl} header for common mathematical work.

  ```cpp
  #include <cmath>
  ```

<div style="margin-top: 1rem;"></div>

| Function | Description |
|:--|:--|
| `sin(radians)` | Returns the trigonometric sine of an angle in radians. |
| `cos(radians)` | Returns the trigonometric cosine of an angle in radians. |
| `tan(radians)` | Returns the trigonometric tangent of an angle in radians. |
| `asin(a)` | Returns the angle in radians for the inverse of sine. |
| `acos(a)` | Returns the angle in radians for the inverse of cosine. |
| `atan(a)` | Returns the angle in radians for the inverse of tangent. |

---
layout: prism
heading: "Trigonometric Functions (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The parameter for `sin`, `cos`, `tan` is an [angle in radians]{.hl}.

- The return value of `asin`, `acos`, `atan` is an angle in radians in the range $[-\pi/2, \pi/2]$.

- Assume `PI` is a constant with value `3.14159`.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    const double PI = 3.14159;
    cout << sin(0) << endl;              // 0
    cout << sin(270 * PI / 180) << endl; // -1
    cout << sin(PI / 6) << endl;         // 0.5
    cout << cos(0) << endl;              // 1
    cout << asin(0.5) << endl;           // 0.523599
    cout << acos(0.5) << endl;           // 1.0472
    cout << atan(1.0) << endl;           // 0.785398
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Exponent Functions (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- There are five functions related to [exponents]{.hl} in the `<cmath>` header.

<div style="margin-top: 1.5rem;"></div>

| Function | Description |
|:--|:--|
| `exp(x)` | Returns $e$ raised to the power of `x` ($e^x$). |
| `log(x)` | Returns the natural logarithm of `x` ($\ln x = \log_e x$). |
| `log10(x)` | Returns the base-10 logarithm of `x` ($\log_{10} x$). |
| `pow(a, b)` | Returns `a` raised to the power of `b` ($a^b$). |
| `sqrt(x)` | Returns the square root of `x` ($\sqrt{x}$) for `x >= 0`. |

---
layout: prism
heading: "Exponent Functions (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- `exp` and `log` are inverses of each other, so `log(exp(1.0))` returns close to `1`.

- `pow` accepts a floating-point base and exponent, while `sqrt` requires a non-negative argument.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    const double E = 2.71828;
    cout << exp(1.0) << endl;   // 2.71828
    cout << log(E) << endl;     // 0.999999
    cout << log10(10.0) << endl;// 1
    cout << pow(2.0, 3) << endl;// 8
    cout << sqrt(4.0) << endl;  // 2
    cout << sqrt(10.5) << endl; // 3.24037
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Rounding Functions"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

- The `<cmath>` header contains functions for [rounding]{.hl}.

| Function | Description |
|:--|:--|
| `ceil(x)` | `x` is rounded *up* to its nearest integer, returned as a `double`. |
| `floor(x)` | `x` is rounded *down* to its nearest integer, returned as a `double`. |

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    cout << ceil(2.1)  << endl; // 3
    cout << ceil(-2.1) << endl; // -2
    cout << floor(2.1) << endl; // 2
    cout << floor(-2.1)<< endl; // -3
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "The min, max, and abs Functions"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `min` and `max` return the minimum and maximum of two numbers (`int`, `long`, `float`, or `double`).
  - `max(4.4, 5.0)` returns `5.0`
  - `min(3, 2)` returns `2`

- `abs` returns the [absolute value]{.hl} of a number.
  - `abs(-2)` returns `2`
  - `abs(-2.1)` returns `2.1`

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
using namespace std;

int main() {
    cout << max(4.4, 5.0) << endl; // 5
    cout << min(3, 2)     << endl; // 2
    cout << abs(-2)       << endl; // 2
    cout << abs(-2.1)     << endl; // 2.1
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Practice: Computing Angles of a Triangle (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Given the three sides of a triangle, we can compute its [angles]{.hl}.

- We do **not** need to know how the formula is derived to write the program.

<div style="margin-top: 1rem;"></div>

```text
A = acos((a*a - b*b - c*c) / (-2*b*c))
B = acos((b*b - a*a - c*c) / (-2*a*c))
C = acos((c*c - b*b - a*a) / (-2*a*b))
```

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp-2027/w04/cpp-w04-image17.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Practice: Computing Angles of a Triangle (2/2)"
---

<CppRunner stdin="0 0 3 0 0 4">

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // Prompt the user to enter three points
    cout << "Enter three points: ";
    double x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    // Compute three sides
    double a = sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3));
    double b = sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3));
    double c = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));

    // Obtain three angles in radians
    double A = acos((a * a - b * b - c * c) / (-2 * b * c));
    double B = acos((b * b - a * a - c * c) / (-2 * a * c));
    double C = acos((c * c - b * b - a * a) / (-2 * a * b));

    // Display the angles in degrees
    const double PI = 3.14159;
    cout << "The three angles are " << A * 180 / PI << " "
         << B * 180 / PI << " " << C * 180 / PI << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Character Data Type"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [character data type]{.hl} represents a *single* character. In C++ this type is [`char`]{.hl}.

- A character literal is enclosed in **single** quotation marks:

  ```cpp
  char letter = 'A';
  char numChar = '4';
  ```

- A *string* literal must be enclosed in **double** quotation marks (`" "`); a *character* literal uses single quotation marks (`' '`).
  - `"A"` is a string, and `'A'` is a character.

---
layout: prism
heading: "ASCII Code"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- Computers work with binary internally, so a character is stored as a sequence of 0s and 1s.

- Most computers use [ASCII]{.hl} (American Standard Code for Information Interchange), an 8-bit encoding for letters, digits, punctuation, and control characters.
  - On most systems, `char` is 1 byte.

| Characters | ASCII Code |
|:--|:--|
| `'0'` to `'9'` | 48 to 57 |
| `'A'` to `'Z'` | 65 to 90 |
| `'a'` to `'z'` | 97 to 122 |

</div>
<div>

<div style="height: 1rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    char ch = 'a';
    cout << "ch      = " << ch << endl;   // a
    cout << "ASCII   = " << (int)ch << endl; // 97
    cout << "++ch    = " << ++ch << endl; // b
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Escape Sequences"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

- C++ uses a special notation, an [escape sequence]{.hl}, to represent special characters: a backslash `\` followed by a character or digits.

| Escape | Name | ASCII |
|:--|:--|:--|
| `\b` | Backspace | 8 |
| `\t` | Tab | 9 |
| `\n` | Linefeed | 10 |
| `\f` | Formfeed | 12 |
| `\r` | Carriage Return | 13 |
| `\\` | Backslash | 92 |
| `\"` | Double Quote | 34 |

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Tab:" << '\t' << "ending" << endl;
    cout << "Newline:" << '\n' << "ending" << endl;
    cout << "Backslash: " << '\\' << "ending" << endl;
    cout << "Quote: " << '\"' << "ending" << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Casting between char and Numeric Types (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- A `char` can be cast into any numeric type, and vice versa.

- When an integer is cast into a `char`, only its lower 8 bits are used:

  ```cpp
  char c = 0XFF41; // 'A', because the lower 8 bits (0x41 = 65) are assigned
  ```

- When a floating-point value is cast into a `char`, it is first cast into an `int`:

  ```cpp
  char c = 65.25;  // 'A', because 65 is assigned
  ```

- When a `char` is cast into a numeric type, the character's [ASCII code]{.hl} is used:

  ```cpp
  int i = 'A';     // i is 65, the ASCII code of 'A'
  ```

---
layout: prism
heading: "Casting between char and Numeric Types (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The `char` type is treated as if it were an integer of byte size, so all numeric operators apply to `char` operands.

- A `char` operand is automatically cast into a number when the other operand is a number.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    // ASCII of '2' is 50, '3' is 51
    int i = '2' + '3';   // 101
    cout << "i = " << i << endl;

    // ASCII of 'a' is 97
    int j = 2 + 'a';     // 99
    cout << "j = " << j << endl;
    cout << static_cast<char>(j) << endl; // 'c'
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Practice: To Uppercase"
---

- Read a lowercase letter and convert it to uppercase using the [ASCII offset]{.hl} `'A' + (letter - 'a')`.

<CppRunner stdin="b">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter a lowercase letter: ";
    char lowercaseLetter;
    cin >> lowercaseLetter;

    char uppercaseLetter =
        static_cast<char>('A' + (lowercaseLetter - 'a'));

    cout << "The corresponding uppercase letter is "
         << uppercaseLetter << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Comparing and Testing Characters"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- Two characters can be compared with relational operators, just like numbers — this compares their [ASCII codes]{.hl}.
  - `'a' < 'b'` is `true` (97 < 98)
  - `'a' < 'A'` is `false` (97 > 65)
  - `'1' < '8'` is `true` (49 < 56)

- Let us make a simple *letter checker*.

</div>
<div>

<CppRunner stdin="H">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter a character: ";
    char ch;
    cin >> ch;

    if (ch >= 'A' && ch <= 'Z')
        cout << ch << " is uppercase" << endl;
    else if (ch >= 'a' && ch <= 'z')
        cout << ch << " is lowercase" << endl;
    else
        cout << ch << " is not a letter" << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Practice: Display Random Character"
---

- Read a starting and an ending character, then display a random character in that range with `rand()`.

<CppRunner stdin="a z">

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    cout << "Enter a starting character: ";
    char startChar;
    cin >> startChar;

    cout << "Enter an ending character: ";
    char endChar;
    cin >> endChar;

    // Get a random character
    char randomChar = static_cast<char>(startChar + rand() %
                (endChar - startChar + 1));

    cout << "The random character between " << startChar << " and "
         << endChar << " is " << randomChar << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Character Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- C++ provides functions for *testing* and *converting* characters in the [`<cctype>`]{.hl} header. Testing functions return `true` or `false`.

  ```cpp
  #include <cctype>
  ```

<div class="grid grid-cols-2 gap-6" style="margin-top: 0.8rem;">
<div>

| Function | Description |
|:--|:--|
| `isdigit(ch)` | true if `ch` is a digit |
| `isalpha(ch)` | true if `ch` is a letter |
| `isalnum(ch)` | true if `ch` is a letter or digit |
| `islower(ch)` | true if `ch` is lowercase |

</div>
<div>

| Function | Description |
|:--|:--|
| `isupper(ch)` | true if `ch` is uppercase |
| `isspace(ch)` | true if `ch` is whitespace |
| `tolower(ch)` | returns the lowercase of `ch` |
| `toupper(ch)` | returns the uppercase of `ch` |

</div>
</div>

---
layout: prism
heading: "Practice: Hex Digit to Decimal Digit"
---

<CppRunner stdin="B">

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    cout << "Enter a hex digit: ";
    char hexDigit;
    cin >> hexDigit;

    hexDigit = toupper(hexDigit);
    if (hexDigit <= 'F' && hexDigit >= 'A') {
        int value = 10 + hexDigit - 'A';
        cout << "The decimal value for hex digit "
             << hexDigit << " is " << value << endl;
    }
    else if (isdigit(hexDigit)) {
        cout << "The decimal value for hex digit "
             << hexDigit << " is " << hexDigit << endl;
    }
    else {
        cout << hexDigit << " is an invalid input" << endl;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY_W04: Base-20 Digit to Decimal"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- Read a **single-digit base-20 number** and convert it to decimal (`0`-`9`, `A`-`J` → `0`-`19`).

- If a *lowercase* letter is entered, warn that it was automatically converted to uppercase.

</div>
<div>

<div style="height: 0.5rem;"></div>

Sample runs:

```text
Input:  A
Output: base-20 'A' is 10 in decimal.

Input:  g
Output: 'g' was auto-converted to 'G'.
        'G' is 16 in decimal.
```

</div>
</div>

<CppRunner stdin="g">

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    cout << "Enter a base-20 digit: ";
    char digit;
    cin >> digit;

    if (islower(digit)) {
        char upper = toupper(digit);
        cout << "'" << digit << "' was auto-converted to '" << upper << "'." << endl;
        digit = upper;
    }

    if (isdigit(digit))
        cout << "base-20 '" << digit << "' is " << (digit - '0') << " in decimal." << endl;
    else if (digit >= 'A' && digit <= 'J')
        cout << "'" << digit << "' is " << (10 + digit - 'A') << " in decimal." << endl;
    else
        cout << "'" << digit << "' is an invalid base-20 digit." << endl;
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
