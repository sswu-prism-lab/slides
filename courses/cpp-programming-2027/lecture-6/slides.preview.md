---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 6
download: true
info: |
  ## C++ Programming Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-2027/lecture-6-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 06: Loops</p>

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
heading: "Recap: The string Type"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- To represent a string of characters, we use the data type called [`string`]{.hl}.
  - `string message = "Programming is fun";`
  - The `string` type is not a primitive type, but an [object type]{.hl}.
  - `message` represents a string object with contents *Programming is fun*.

- We can use the relational operators `==`, `!=`, `<`, `<=`, `>`, `>=` to compare two strings.

<div style="height: 0.8rem;"></div>

| Function | Description |
| --- | --- |
| `length()` | Returns the number of characters in this string. |
| `size()` | Same as `length()`. |
| `at(index)` | Returns the character at the specified index from this string. |

---
layout: prism
heading: "Recap: The string Type — Try It"
---

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string message = "Programming is fun";
    cout << "message  = " << message << "\n";
    cout << "length() = " << message.length() << "\n";
    cout << "at(0)    = " << message.at(0) << "\n";

    string a = "apple", b = "banana";
    cout << boolalpha;
    cout << "(a < b)  = " << (a < b) << "\n";   // lexicographic
    cout << "(a == b) = " << (a == b) << endl;
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
  margin-top: 1.4em;
}
</style>

- C++ provides functions for [formatting how a value is displayed]{.hl}.

<div style="height: 0.5rem;"></div>

| Manipulator | Description |
| --- | --- |
| `setprecision(n)` | Sets the precision of a floating-point number. |
| `fixed` | Displays floating-point numbers in fixed-point notation. |
| `showpoint` | Shows a decimal point with trailing zeros even with no fractional part. |
| `setw(width)` | Specifies the width of a print field. |
| `left` | Justifies the output to the left. |
| `right` | Justifies the output to the right. |

---
layout: prism
heading: "Recap: Manipulators — Try It"
---

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double pi = 3.14159265;
    cout << fixed << setprecision(2) << pi << "\n"; // 3.14
    cout << setprecision(4) << pi << "\n";          // 3.1416

    cout << "|" << setw(8) << right << "abc" << "|\n";
    cout << "|" << setw(8) << left  << "abc" << "|" << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "HW_W05: Random String and My City"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Generate a random string made of [one uppercase letter and five lowercase letters]{.hl}, then compare it with a city name entered by the user in [alphabetical order]{.hl} and print the result.

- Example runs:

```text
Input a city name: Seoul
The randomly generated city name is "Zjqxiu"
The cities in alphabetical order are "Seoul" and "Zjqxiu"

Input a city name: New York
The randomly generated city name is "Aeqpcb"
The cities in alphabetical order are "Aeqpcb" and "New York"
```

- Save your file as `HW_W05_20XXXXXX.cpp` and upload it to the LMS.

---
layout: prism
heading: "Loops (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- Let us imagine that we are driving a car on the highway.

- If there are no navigation alerts or emergency situations, we will [continue]{.hl} to drive forward.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w06/cpp-w06-image5.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Loops (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A loop can be used to tell a program to [execute statements repeatedly]{.hl}.

- If we should display a string (e.g., `"Welcome to C++!"`) 100 times, writing 100 `cout` statements would be tedious.

- C++ provides a powerful construct called a [loop]{.hl} that controls how many times an operation or a sequence of operations is performed in succession.

- C++ provides [`while`]{.hl}, [`do-while`]{.hl}, and [`for`]{.hl} loops.

<div style="height: 0.8rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 0;
    while (count < 3) {          // repeat instead of copy-pasting
        cout << "Welcome to C++!\n";
        count++;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "The while Loop (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A `while` loop executes statements repeatedly [while the condition is true]{.hl}.

- The syntax for the `while` loop is:

```cpp
while (loop-continuation-condition) {
    // Loop body
    Statement(s);
}
```

- The one-time execution of a loop body is an [iteration]{.hl} (or repetition) of the loop.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w06/cpp-w06-image4.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "The while Loop (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The `loop-continuation-condition` must always appear inside the [parentheses]{.hl}.

- A common programming error involves [infinite loops]{.hl}.
  - If a program takes an unusually long time to run and does not stop, it may have an infinite loop.
  - To stop the program by force, press `ctrl (cmd) + c`.

- Programmers often make the mistake of executing a loop one more or one less time.

```cpp
int count = 0;
while (count <= 100)   // runs 101 times, not 100!
{
    cout << "Welcome to C++!\n";
    count++;
}
```

---
layout: prism
heading: "Practice: Guess Number"
---

<CppRunner stdin="50 25 42 39">

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>   // Needed for the time function
using namespace std;

int main() {
    // Normally: srand(time(0)); int number = rand() % 101;
    // Fixed here so the run is reproducible.
    int number = 39;

    cout << "Guess a magic number between 0 and 100\n";

    int guess = -1;
    while (guess != number) {
        cout << "\nEnter your guess: ";
        cin >> guess;

        if (guess == number)
            cout << "Yes, the number is " << number << endl;
        else if (guess > number)
            cout << "Your guess is too high" << endl;
        else
            cout << "Your guess is too low" << endl;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Loop Design Strategies"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- For writing a correct loop, we consider three steps:

<div class="sub-item-enum">

1. Identify the statements that need to be [repeated]{.hl}.
2. Wrap these statements in a loop.
3. Code the `loop-continuation-condition` and add appropriate statements for controlling the loop.

</div>

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

```cpp
while (true) {
    Statements;
}
```

</div>
<div>

```cpp
while (loop-continuation-condition) {
    Statements;
    Additional statements for
        controlling the loop;
}
```

</div>
</div>

---
layout: prism
heading: "Controlling a Loop with User Confirmation"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- If we want the user to decide whether to continue, we can offer a [user confirmation]{.hl}.

<CppRunner stdin="10 Y 20 Y 30 N">

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0, data;
    char continueLoop = 'Y';
    while (continueLoop == 'Y') {
        // Execute the loop body once
        cout << "Enter an integer: ";
        cin >> data;
        sum += data;

        // Prompt the user for confirmation
        cout << "Enter Y to continue and N to quit: ";
        cin >> continueLoop;
    }
    cout << "Sum = " << sum << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Controlling a Loop with a Sentinel Value"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- We can designate a [special value]{.hl} when reading and processing a set of values for controlling a loop.

- This special input value, known as a [sentinel value]{.hl}, signifies the end of the input.

- A loop that uses a sentinel value to control its execution is a [sentinel-controlled loop]{.hl}.

</div>
<div>

<CppRunner stdin="2 3 4 0">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter an integer "
         << "(the input ends if it is 0): ";
    int data;
    cin >> data;

    // Keep reading until the input is 0
    int sum = 0;
    while (data != 0) {
        sum += data;
        cout << "Enter an integer "
             << "(the input ends if it is 0): ";
        cin >> data;
    }

    cout << "The sum is " << sum << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "The do-while Loop"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A `do-while` loop is the same as a `while` loop except that [it executes the loop body first]{.hl} and then checks the loop-continuation-condition.

```cpp
do {
    // Loop body
    Statement(s);
} while (loop-continuation-condition);
```

- The loop body is executed first, then the `loop-continuation-condition` is evaluated.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w06/cpp-w06-image19.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Practice: Test Do-While"
---

<CppRunner stdin="2 3 4 0">

```cpp
#include <iostream>
using namespace std;

int main() {
    // Keep reading data until the input is 0
    int sum = 0;
    int data = 0;

    do {
        sum += data;

        // Read the next data
        cout << "Enter an integer (the input ends if it is 0): ";
        cin >> data;
    } while (data != 0);

    cout << "The sum is " << sum << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "The for Loop (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A `for` loop has a [concise syntax]{.hl} for writing loops.

```cpp
i = initialValue;   // init control var
while (i < endValue) {
    // Loop body
    i++;            // adjust control var
}
```

- The syntax of a `for` loop is:

```cpp
for (initial-action;
     loop-continuation-condition;
     action-after-each-iteration) {
    // Loop body
    Statement(s);
}
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w06/cpp-w06-image24.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "The for Loop (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- The `for` loop starts with the keyword `for`, followed by a pair of parentheses enclosing `initial-action`, `loop-continuation-condition`, and `action-after-each-iteration`, [separated by semicolons]{.hl}.

- A [control variable]{.hl} controls how many times the loop body is executed and when the loop terminates.
  - The `initial-action` initializes the control variable.
  - The `action-after-each-iteration` usually increments or decrements it.
  - The `loop-continuation-condition` tests whether it has reached a termination value.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 3; i++)
        cout << "Welcome to C++! (i = " << i << ")\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Various Loops"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- We can use a `for` loop, a `while` loop, or a `do-while` loop, whichever is convenient.

- The `while` and `for` loops are [pretest loops]{.hl} because the continuation condition is checked *before* the loop body.

- The `do-while` loop is a [posttest loop]{.hl} because the condition is checked *after* the loop body.

</div>
<div>

```cpp
for (initial-action;
     loop-continuation-condition;
     action-after-each-iteration) {
    // Loop body;
}
```

<div style="text-align:center; margin: 0.4rem 0;">— Equivalent to —</div>

```cpp
initial-action;
while (loop-continuation-condition) {
    // Loop body;
    action-after-each-iteration;
}
```

</div>
</div>

---
layout: prism
heading: "Nested Loops"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A loop can be [nested]{.hl} inside another loop.

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << "         Multiplication Table\n";
    cout << "-----------------------------------\n";

    // Display the number title
    cout << "  | ";
    for (int j = 1; j <= 9; j++)
        cout << setw(3) << j;
    cout << "\n";

    // Display table body
    for (int i = 1; i <= 9; i++) {
        cout << i << " | ";
        for (int j = 1; j <= 9; j++)
            cout << setw(3) << i * j;
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Minimizing Numeric Errors"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- Using [floating-point]{.hl} numbers in the loop-continuation-condition [may cause numeric errors]{.hl}. The sum below is `49.5`, not `50` — `1.0` is skipped because `i` never lands exactly on it.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    // Add 0.01, 0.02, ..., 0.99, 1.0 to sum
    double sum = 0;
    for (double i = 0.01; i <= 1.0; i = i + 0.01)
        sum += i;
    cout << "The sum is " << sum << endl;   // 49.5 (numeric error)
    return 0;
}
```

</CppRunner>

<div class="sub-item">

Prefer an integer control variable: `for (int count = 0; count < 100; count++) { sum += currentValue; currentValue += 0.01; }`.

</div>

---
layout: prism
heading: "Practice: Greatest Common Divisor"
---

<CppRunner stdin="125 2525">

```cpp
#include <iostream>
using namespace std;

int main() {
    // Prompt the user to enter two integers
    cout << "Enter first integer: ";
    int n1;
    cin >> n1;

    cout << "Enter second integer: ";
    int n2;
    cin >> n2;

    int gcd = 1;
    int k = 2;
    while (k <= n1 && k <= n2) {
        if (n1 % k == 0 && n2 % k == 0)
            gcd = k;
        k++;
    }

    cout << "The greatest common divisor for " << n1 << " and "
         << n2 << " is " << gcd << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Practice: Monte-Carlo Simulation (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- [Monte-Carlo simulation]{.hl} uses random numbers and probability to solve problems, with wide applications in mathematics, physics, chemistry, etc.

- It avoids intricate mathematical calculations and leverages computers with high computational capabilities to approximate solutions.

- [Occam's razor]{.hl} is a principle in scientific theories that suggests *not to complicate assumptions unnecessarily*.

---
layout: prism
heading: "Practice: Monte-Carlo Simulation (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- To estimate [$\pi$]{.hl} using the Monte-Carlo method, we assume the radius of the circle is `1`.

- The circle area is $\pi$ and the square area is `4`.

- If we randomly generate a point in the square, the probability that it falls in the circle is `circleArea / squareArea` $= \pi / 4$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w06/cpp-w06-image34.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Practice: Monte-Carlo Simulation (3/3)"
---

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    const int NUMBER_OF_TRIALS = 1000000;
    int numberOfHits = 0;
    srand(1);   // fixed seed so the estimate is reproducible

    for (int i = 0; i < NUMBER_OF_TRIALS; i++) {
        double x = rand() * 2.0 / RAND_MAX - 1;
        double y = rand() * 2.0 / RAND_MAX - 1;
        if (x * x + y * y <= 1)
            numberOfHits++;
    }

    double pi = 4.0 * numberOfHits / NUMBER_OF_TRIALS;
    cout << "PI is " << pi << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Practice: Decimal to Hexadecimal"
---

<CppRunner stdin="1234">

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // Prompt the user to enter a decimal integer
    cout << "Enter a decimal number: ";
    int decimal;
    cin >> decimal;

    // Convert decimal to hex
    string hex = "";
    while (decimal != 0) {
        int hexValue = decimal % 16;

        // Convert a decimal value to a hex digit
        char hexChar = (hexValue <= 9 && hexValue >= 0) ?
            static_cast<char>(hexValue + '0') :
            static_cast<char>(hexValue - 10 + 'A');

        hex = hexChar + hex;
        decimal = decimal / 16;
    }

    cout << "The hex number is " << hex << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Keywords break and continue (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- The [`break`]{.hl} and [`continue`]{.hl} keywords provide additional controls in a loop.

- We can use `break` in a loop to [immediately terminate the loop]{.hl}.

- We can use `continue` in a loop to [end the current iteration]{.hl}.

- In short: `continue` breaks out of an *iteration*, while `break` breaks out of the *loop*.

---
layout: prism
heading: "Keywords break and continue (2/3)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    int number = 0;

    while (number < 20) {
        number++;
        sum += number;
        if (sum >= 100)
            break;   // jump out of the loop
    }

    cout << "The number is " << number << endl;
    cout << "The sum is " << sum << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Keywords break and continue (3/3)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    int number = 0;

    while (number < 20) {
        number++;
        if (number == 10 || number == 11)
            continue;   // skip the rest of this iteration
        sum += number;
    }

    cout << "The sum is " << sum << endl;
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
