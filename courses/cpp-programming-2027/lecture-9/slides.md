---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 9
download: true
info: |
  ## C++ Programming Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-9-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 09: Functions</p>

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
heading: "Functions (1/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [function]{.hl} is used to define, organize, and simplify reusable code.

- In C++, code that plays a similar role can be defined as a function and *called* repeatedly, minimizing repetitive work.
  - Familiar examples include `max`, `min`, `ceil`, and `floor`.

- Instead of writing the same summation loop three times, we can factor it into a single `sum(i1, i2)` function and call it with different arguments.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// Return the sum of all integers from i1 to i2
int sum(int i1, int i2) {
    int sum = 0;
    for (int i = i1; i <= i2; i++)
        sum += i;
    return sum;
}

int main() {
    cout << "Sum from 1 to 10 is " << sum(1, 10) << endl;
    cout << "Sum from 20 to 37 is " << sum(20, 37) << endl;
    cout << "Sum from 35 to 49 is " << sum(35, 49) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Functions (2/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A function consists of a [return value type]{.hl}, a [function name]{.hl}, [parameters]{.hl}, and a [function body]{.hl}.
  - The [function header]{.hl} specifies the return value type, name, and parameters.
  - A variable declared in the header is a [formal parameter]{.hl}; the value supplied by the caller is an [argument]{.hl}.

- The return value type is the data type of the value the function [returns]{.hl}.
  - A function that returns a value is a [value-returning function]{.hl}.
  - A function that returns nothing is a [`void` function]{.hl} (e.g. `srand`).

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w09/cpp-w09-image4.png" class="tikz-fig" style="width: 100%; margin-top: 2rem;" />

</div>
</div>

---
layout: prism
heading: "Functions (3/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A function is [called]{.hl} (invoked) by executing its code.

- When a function returns a value, the function call is treated as a single value:
  - `int larger = max(3, 4);` stores the return value of `max(3, 4)` in `larger`.
  - `cout << max(3, 4);` prints the return value directly.
  - If the caller does not need the return value, it may simply ignore it.

- When a function is called, [control]{.hl} passes to the called function. Once a `return` statement runs or the closing brace `}` is reached, control returns to the caller.

---
layout: prism
heading: "Practice: Test Max"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A function must be [defined before it is called]{.hl}. Since `max` is called by `main`, it is declared *ahead* of `main`.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// Return the max between two numbers
int max(int num1, int num2) {
    int result;
    if (num1 > num2)
        result = num1;
    else
        result = num2;
    return result;
}

int main() {
    int i = 5;
    int j = 2;
    int k = max(i, j);   // pass the values i and j
    cout << "The maximum between " << i
         << " and " << j << " is " << k << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Functions (4/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Each time a function is called, the system creates an [activation record]{.hl} that stores the function's arguments and variables, and pushes it onto the [call stack]{.hl} in memory.
  - The call stack is also known as the *execution stack*, *runtime stack*, or *machine stack*.

- The call stack is a [last-in, first-out]{.hl} (LIFO) structure: the most recently added data is the first to be removed.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w09/cpp-w09-image7.png" class="tikz-fig" style="width: 100%; margin-top: 2rem;" />

</div>
</div>

---
layout: prism
heading: "void Functions"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [`void` function]{.hl} does not return a value.

- A `void` function does not require a `return` statement, but one may be used to *end execution* early and return to the caller:
  - `return;`

- Sample input: `85.5` &rarr; the grade is `B`.

</div>
<div>

<CppRunner stdin="85.5">

```cpp
#include <iostream>
using namespace std;

// Print grade for the score
void printGrade(double score) {
    if (score >= 90.0)
        cout << 'A' << endl;
    else if (score >= 80.0)
        cout << 'B' << endl;
    else if (score >= 70.0)
        cout << 'C' << endl;
    else if (score >= 60.0)
        cout << 'D' << endl;
    else
        cout << 'F' << endl;
}

int main() {
    cout << "Enter a score: ";
    double score;
    cin >> score;
    cout << "The grade is ";
    printGrade(score);
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Passing Arguments by Value"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Arguments are [passed by value]{.hl}: when a function is called, the argument values are copied into the parameters.

- Arguments are bound to the called function's parameters *in order* — this is [parameter order association]{.hl}.
  - To print `ch` exactly `n` times we call `nPrint('a', 3)`.
  - The original `nPrintln` had two bugs, fixed below: (1) it re-declared `int n = 1;`, shadowing the parameter, and (2) it was called as `nPrintln(5, "...")` with the arguments in the *wrong order*.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

void nPrint(char ch, int n) {          // print ch n times
    for (int i = 0; i < n; i++)
        cout << ch;
}

void nPrintln(string message, int n) { // print message n times
    for (int i = 0; i < n; i++)        // do NOT redeclare n here
        cout << message << endl;
}

int main() {
    nPrint('a', 3);
    cout << endl;
    nPrintln("Welcome to C++!", 5);    // correct argument order
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Modularizing Code"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- [Modularizing]{.hl} (or [encapsulating]{.hl}) code keeps it reusable and makes maintenance and debugging easier.

- Functions reduce duplicated code and enable code reuse; they are also used to modularize code and improve a program's overall structure.

- Modularizing code with functions gives us:
  - A clear separation between the `main` logic and additional computation, making the code easier to understand.
  - A narrower [debugging]{.hl} scope — errors in an extra computation are confined to that function.
  - Reusable functions that can be shared across other programs.

---
layout: prism
heading: "Practice: Prime Number Function"
---

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

// Check whether number is prime
bool isPrime(int number) {
    for (int divisor = 2; divisor <= number / 2; divisor++)
        if (number % divisor == 0)
            return false;   // number is not a prime
    return true;            // number is prime
}

void printPrimeNumbers(int numberOfPrimes) {
    const int NUMBER_OF_PRIMES_PER_LINE = 10; // display 10 per line
    int count = 0;   // count of prime numbers found
    int number = 2;  // a number to be tested for primeness

    while (count < numberOfPrimes) {
        if (isPrime(number)) {
            count++;
            if (count % NUMBER_OF_PRIMES_PER_LINE == 0)
                cout << setw(4) << number << endl;
            else
                cout << setw(4) << number;
        }
        number++;
    }
}

int main() {
    cout << "The first 50 prime numbers are \n";
    printPrimeNumbers(50);
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Function Overloading"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- [Overloading functions]{.hl} lets us define functions with the *same name* but *different parameters*.

- To build a function that does the same job (e.g. returning the maximum) regardless of its arguments' data types, we use function overloading.

- The C++ compiler decides which function to run based on the function's [parameter list]{.hl}.

- When two or more functions match a call and the compiler cannot choose one, it is an [ambiguous invocation]{.hl}, which produces a compile error.

---
layout: prism
heading: "Practice: Test Function Overloading"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// Return the max between two int values
int max(int num1, int num2) {
    if (num1 > num2) return num1;
    else return num2;
}

// Find the max between two double values
double max(double num1, double num2) {
    if (num1 > num2) return num1;
    else return num2;
}

// Return the max among three double values
double max(double num1, double num2, double num3) {
    return max(max(num1, num2), num3);
}

int main() {
    cout << "The maximum between 3 and 4 is " << max(3, 4) << endl;
    cout << "The maximum between 3.0 and 5.4 is "
         << max(3.0, 5.4) << endl;
    cout << "The maximum between 3.0, 5.4, and 10.14 is "
         << max(3.0, 5.4, 10.14) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Function Prototypes"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [function prototype]{.hl} declares a function *before* its body is written.

- Because a function's header must be declared before it is called, defining just the header (without the body) is called defining a function prototype.
  - The full implementation can then appear *after* `main`.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// Function prototype
int max(int num1, int num2);

int main() {
    cout << "The maximum between 3 and 4 is "
         << max(3, 4) << endl;
    return 0;
}

// Return the max between two int values
int max(int num1, int num2) {
    if (num1 > num2)
        return num1;
    else
        return num2;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Default Arguments"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- C++ lets us declare a function with [default argument]{.hl} values; calling it without an argument passes the default.
  - Default arguments must come *last* in the parameter list.
  - When an argument is omitted, all arguments after it must be omitted too.

```cpp
void f1(int x, int y = 0, int z);     // wrong
void f2(int x = 0, int y = 0, int z); // wrong
void f3(int x, int y = 0, int z = 0); // ok
void f4(int x = 0, int y = 0, int z = 0); // ok
f3(1, , 20);  // wrong
f4(, , 2);    // wrong
f3(1);        // y, z take defaults
f4(1, 2);     // z takes the default
```

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// width and height default to 1
int volume(int length, int width = 1, int height = 1) {
    return length * width * height;
}

int main() {
    cout << "volume(3)       = " << volume(3) << endl;
    cout << "volume(3, 4)    = " << volume(3, 4) << endl;
    cout << "volume(3, 4, 5) = " << volume(3, 4, 5) << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Inline Functions"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- To improve the performance of short functions, C++ offers [inline functions]{.hl}, declared by adding the `inline` keyword.

- A function call incurs [execution overhead]{.hl} (pushing arguments and CPU registers onto the stack, transferring control between functions, etc.).

- Rather than calling the function, the compiler [copies]{.hl} the inline function's code directly to each call site.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

inline void f(int month, int year) {
    cout << "month is " << month << endl;
    cout << "year is " << year << endl;
}

int main() {
    int month = 10, year = 2008;
    f(month, year); // invoke inline function
    f(9, 2010);     // invoke inline function
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Local, Global, and Static Local Variables (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- In C++, variables are divided into [local variables]{.hl}, [global variables]{.hl}, and [static local variables]{.hl}.

- The [scope]{.hl} of a variable is the region of the program in which the variable can be referenced.

- A variable defined *inside* a function is a [local variable]{.hl}.

- A variable declared *outside* all functions, accessible to every function in the file, is a [global variable]{.hl}.
  - Local variables have no default value, but global variables default to `0`.

---
layout: prism
heading: "Practice: Variable Scope Demo"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void t1(); // function prototype
void t2(); // function prototype

int main() {
    t1();
    t2();
    return 0;
}

int y; // global variable, default to 0

void t1() {
    int x = 1;
    cout << "x is " << x << endl;
    cout << "y is " << y << endl;
    x++;
    y++;
}

void t2() {
    int x = 1;
    cout << "x is " << x << endl;
    cout << "y is " << y << endl;
}
```

</CppRunner>

</div>
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

<div style="height: 3rem;"></div>

- Each `t1`/`t2` gets its own local `x`, always starting at `1`.

- The global `y` persists across calls, so `t1` increments it from `0` to `1` before `t2` reads it.

</div>
</div>

---
layout: prism
heading: "Local, Global, and Static Local Variables (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A variable declared in a `for` header's initialization is scoped to the *entire loop*.

- Within one function, [non-nesting]{.hl} blocks may declare local variables of the same name.
  - Reusing the same name in *nested* blocks is allowed but is not good practice.

- The driver reuses `i` across two separate (non-nesting) `for` loops.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void function1() {
    int x = 1;
    int y = 1;
    for (int i = 1; i < 10; i++) { // i in block 1
        x += i;
    }
    for (int i = 1; i < 10; i++) { // i in block 2
        y += i;
    }
    cout << "x is " << x << endl;
    cout << "y is " << y << endl;
}

int main() {
    function1();
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Local, Global, and Static Local Variables (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- When a function finishes, all its local variables disappear from memory; these are called [automatic variables]{.hl}.

- Sometimes we want a local variable to *retain* its value across successive calls.

- C++ solves this with [static local variables]{.hl}.
  - A static local variable stays in memory until the program ends, keeping its value between calls.
  - Declare one with the `static` keyword: `static int x = 1;`

---
layout: prism
heading: "Practice: Static Variable Demo"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void t1(); // function prototype

int main() {
    t1();
    t1();
    return 0;
}

void t1() {
    static int x = 1; // retained across calls
    int y = 1;        // reset on every call
    x++;
    y++;
    cout << "x is " << x << endl;
    cout << "y is " << y << endl;
}
```

</CppRunner>

</div>
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

<div style="height: 3rem;"></div>

- The static `x` keeps its value: it goes `1 → 2` on the first call, then `2 → 3` on the second.

- The automatic `y` is re-initialized to `1` every call, so it always prints `2`.

</div>
</div>

---
layout: prism
heading: "Passing Arguments by Reference (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A parameter can be [passed by reference]{.hl}, making the formal parameter an [alias]{.hl} of the argument.

- When a parameter is passed by reference, changing the parameter inside the function also changes the argument.

- Here `increment` takes its parameter *by value*, so the caller's `x` is unaffected.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void increment(int n) {
    n++;
    cout << "\tn inside the function is " << n << endl;
}

int main() {
    int x = 1;
    cout << "Before the call, x is " << x << endl;
    increment(x);
    cout << "after the call, x is " << x << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Practice: Swap by Value"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// Attempt to swap two variables does not work!
void swap(int n1, int n2) {
    cout << "\tInside the swap function" << endl;
    cout << "\tBefore swapping n1 is " << n1
         << " n2 is " << n2 << endl;
    // Swap n1 with n2
    int temp = n1;
    n1 = n2;
    n2 = temp;
    cout << "\tAfter swapping n1 is " << n1
         << " n2 is " << n2 << endl;
}

int main() {
    int num1 = 1;
    int num2 = 2;
    cout << "Before invoking the swap function, num1 is "
         << num1 << " and num2 is " << num2 << endl;
    swap(num1, num2);
    cout << "After invoking the swap function, num1 is " << num1
         << " and num2 is " << num2 << endl;
    return 0;
}
```

</CppRunner>

</div>
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

<div style="height: 3rem;"></div>

- Because `n1` and `n2` are [copies]{.hl}, swapping them affects only the function's own variables.

- After the call, `num1` and `num2` in `main` are [unchanged]{.hl}.

</div>
</div>

---
layout: prism
heading: "Passing Arguments by Reference (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- When a parameter is passed by value, it receives its *own* memory, separate from the caller's argument; that memory disappears when the function returns.

- A [reference variable]{.hl} is a special C++ variable type that acts as an [alias]{.hl} of the original variable, enabling pass by reference.
  - Declare one by placing `&` after the type (or before the name): `int& r = count; // or int &r = count;`

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w09/cpp-w09-image34.png" class="tikz-fig" style="width: 100%; margin-top: 2rem;" />

</div>
</div>

---
layout: prism
heading: "Practice: Test Reference Variable"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 1;
    int& r = count;   // r is an alias for count
    cout << "count is " << count << endl;
    cout << "r is " << r << endl;

    r++;              // changes count too
    cout << "count is " << count << endl;
    cout << "r is " << r << endl;

    count = 10;       // changes r too
    cout << "count is " << count << endl;
    cout << "r is " << r << endl;
    return 0;
}
```

</CppRunner>

</div>
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

<div style="height: 3rem;"></div>

- `r` and `count` name the *same* memory location.

- Incrementing `r` changes `count`, and assigning to `count` changes `r` — they always move together.

</div>
</div>

---
layout: prism
heading: "Practice: Swap by Reference"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// Swap two variables
void swap(int& n1, int& n2) {
    cout << "\tInside the swap function" << endl;
    cout << "\tBefore swapping n1 is " << n1
         << " n2 is " << n2 << endl;
    // Swap n1 with n2
    int temp = n1;
    n1 = n2;
    n2 = temp;
    cout << "\tAfter swapping n1 is " << n1
         << " n2 is " << n2 << endl;
}

int main() {
    int num1 = 1;
    int num2 = 2;
    cout << "Before invoking the swap function, num1 is "
         << num1 << " and num2 is " << num2 << endl;
    swap(num1, num2); // pass by reference
    cout << "After invoking the swap function, num1 is " << num1
         << " and num2 is " << num2 << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Passing Arguments by Reference (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- When passed by reference, the reference parameter acts as an [alias]{.hl} of the argument, so operations such as swapping work as intended.

- When passing arguments by reference, the formal parameter and the argument must have the [same data type]{.hl}.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w09/cpp-w09-image39.png" class="tikz-fig" style="width: 100%; margin-top: 2rem;" />

</div>
</div>

---
layout: prism
heading: "Constant Reference Parameters"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- To prevent a value from being changed inside a function, we can specify a [constant reference parameter]{.hl}.

- Adding `const` before a parameter tells the compiler that the parameter's value must *not* change.
  - This gives the efficiency of pass-by-reference (no copy) with the safety of pass-by-value.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// Return the max between two numbers
int max(const int& num1, const int& num2) {
    int result;
    if (num1 > num2)
        result = num1;
    else
        result = num2;
    return result;
}

int main() {
    cout << "max(3, 4)  = " << max(3, 4) << endl;
    cout << "max(9, -1) = " << max(9, -1) << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Function Abstraction and Stepwise Refinement (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [Function abstraction]{.hl} is obtained by selecting the functions used to build a program.

- A [client]{.hl} program uses a function without needing to know how it is implemented.
  - The implementation is encapsulated and hidden — this is [information hiding]{.hl}.
  - We use `rand` to generate random numbers without knowing its internals.

- We can apply function abstraction to program development: to break a large program into smaller subproblems, we use the [divide-and-conquer]{.hl} strategy known as [stepwise refinement]{.hl}.

---
layout: prism
heading: "Function Abstraction and Stepwise Refinement (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A `printCalendar` program decomposes into smaller functions, each solving one subproblem.

- Leaf functions such as `isLeapYear` and `getNumberOfDaysInMonth` are simple, testable building blocks.
  - This driver tests them *bottom-up* before assembling the full program.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w09/cpp-w09-image41.png" class="tikz-fig" style="width: 100%;" />

<CppRunner>

```cpp
#include <iostream>
using namespace std;

bool isLeapYear(int year) {
    return (year % 4 == 0 && year % 100 != 0)
        || (year % 400 == 0);
}

int getNumberOfDaysInMonth(int year, int month) {
    if (month == 1 || month == 3 || month == 5 || month == 7 ||
        month == 8 || month == 10 || month == 12) return 31;
    if (month == 4 || month == 6 || month == 9 || month == 11) return 30;
    if (month == 2) return isLeapYear(year) ? 29 : 28;
    return 0;
}

int main() {
    cout << "2027 leap? " << (isLeapYear(2027) ? "yes" : "no") << "\n";
    cout << "2024 leap? " << (isLeapYear(2024) ? "yes" : "no") << "\n";
    cout << "Days in Feb 2024: " << getNumberOfDaysInMonth(2024, 2) << "\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Function Abstraction and Stepwise Refinement (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Programs can be implemented [top-down]{.hl} or [bottom-up]{.hl}.

- The top-down approach implements functions from the top down.
  - To use a not-yet-implemented function, we substitute a [stub]{.hl} — a simple but incomplete version of the function.

- The bottom-up approach implements functions from the bottom up.
  - As each function is written, we build a test program called a [driver]{.hl} to check it.

- Both approaches implement functions [incrementally]{.hl}, confining errors to individual functions. Top-down and bottom-up can be combined.

---
layout: prism
heading: "DIY_W09"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [Stepwise refinement]{.hl} means splitting a large problem into small, manageable subproblems, each implemented as a function.

- On real, large-scale projects, stepwise refinement is a huge help — think about *in what ways* it helps.

- The full `printCalendar` below is assembled from the building blocks. Try entering different years and months.
  - Sample input: `2027 9`

</div>
<div>

<CppRunner stdin="2027 9">

```cpp
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

bool isLeapYear(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

int getNumberOfDaysInMonth(int year, int month) {
    if (month == 1 || month == 3 || month == 5 || month == 7 ||
        month == 8 || month == 10 || month == 12) return 31;
    if (month == 4 || month == 6 || month == 9 || month == 11) return 30;
    if (month == 2) return isLeapYear(year) ? 29 : 28;
    return 0;
}

int getTotalNumberOfDays(int year, int month) {
    int total = 0;
    for (int y = 1800; y < year; y++)
        total += isLeapYear(y) ? 366 : 365;
    for (int m = 1; m < month; m++)
        total += getNumberOfDaysInMonth(year, m);
    return total;
}

// Jan 1, 1800 was a Wednesday (Sun = 0)
int getStartDay(int year, int month) {
    return (3 + getTotalNumberOfDays(year, month)) % 7;
}

void printMonthBody(int year, int month) {
    int startDay = getStartDay(year, month);
    int days = getNumberOfDaysInMonth(year, month);
    for (int i = 0; i < startDay; i++) cout << "    ";
    for (int i = 1; i <= days; i++) {
        cout << setw(4) << i;
        if ((i + startDay) % 7 == 0) cout << "\n";
    }
    cout << "\n";
}

int main() {
    string names[] = {"", "January", "February", "March", "April",
        "May", "June", "July", "August", "September",
        "October", "November", "December"};
    int year, month;
    cin >> year >> month;
    cout << "      " << names[month] << " " << year << "\n";
    cout << "-----------------------------\n";
    cout << " Sun Mon Tue Wed Thu Fri Sat\n";
    printMonthBody(year, month);
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
