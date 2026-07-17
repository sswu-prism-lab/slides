---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 10
download: true
info: |
  ## C++ Programming Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-10-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 10: Arrays</p>

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
heading: "Recap: Functions"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A function consists of a [return value type]{.hl}, a [function name]{.hl}, [parameters]{.hl}, and a [function body]{.hl}.
  - The [function header]{.hl} specifies the return value type, the function name, and the parameters.
  - Variables declared in the header are [formal parameters]{.hl}; the values supplied by the caller are [arguments]{.hl}.

- The [return value type]{.hl} is the data type of the value the function returns.
  - A [value-returning function]{.hl} returns a value.
  - A [void function]{.hl} returns nothing (e.g. `srand`).

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w10/cpp-w10-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Recap: void Functions"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [void function]{.hl} does not return a value.

- A `void` function does not require a `return` statement, but a bare `return;` can be used to end the function's execution and go back to the caller.

- `printGrade` prints a letter grade for a numeric score without returning anything.

</div>
<div>

<CppRunner stdin="85">

```cpp
#include <iostream>
using namespace std;

// Print grade for the score
void printGrade(double score) {
    if (score >= 90.0)      cout << 'A' << endl;
    else if (score >= 80.0) cout << 'B' << endl;
    else if (score >= 70.0) cout << 'C' << endl;
    else if (score >= 60.0) cout << 'D' << endl;
    else                    cout << 'F' << endl;
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
heading: "Recap: Passing Arguments by Value"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- Arguments are passed to parameters [by value]{.hl} when a function is called; the function then does its work with those parameter values.

- When the arguments are passed to the called function, each is assigned to the corresponding parameter *in order*.
  - This is called [parameter order association]{.hl}.

- Because a copy is passed, changes to a parameter inside the function do **not** affect the caller's argument.

---
layout: prism
heading: "Recap: Passing Arguments by Reference"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Parameters can be passed [by reference]{.hl}, making the formal parameter an [alias]{.hl} of the argument.

- If a by-reference parameter is changed inside the function, the argument value changes with it.

- A [reference variable]{.hl} acts as an alias for the original variable. Declare it by placing `&` after the type (or before the name).

</div>
<div>

<div style="height: 5rem;"></div>

```cpp
int count = 1;
int& r = count;   // or: int &r = count;

r = 10;           // count is now 10
```

</div>
</div>

---
layout: prism
heading: "Recap: Local, Global, and Static Local Variables"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- C++ variables are classified as [local]{.hl}, [global]{.hl}, or [static local]{.hl}. The [scope]{.hl} of a variable is the region of the program in which it can be referenced.
  - A variable defined inside a function is a [local variable]{.hl}; it has no default value.
  - A variable declared outside all functions, accessible to every function in the file, is a [global variable]{.hl}; it defaults to `0`.

- When a function finishes, its local variables disappear from memory — these are [automatic variables]{.hl}.

- To keep a local variable's value between successive calls, C++ provides [static local variables]{.hl}, which persist until the program ends. Declare them with the `static` keyword.

```cpp
static int x = 1;   // retains its value across calls
```

---
layout: prism
heading: "DIY_W09: Stepwise Refinement"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- [Stepwise refinement]{.hl} is an implementation methodology that breaks a large problem into smaller, more manageable subproblems.

- Each subproblem can be implemented using a function.

- In real, large-scale projects, stepwise refinement is a great help.

- Think about *in what ways* it actually helps.

---
layout: prism
heading: "Arrays (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- An [array]{.hl} can store a large collection of data. In C++, an array is a [data structure]{.hl} that stores a fixed number of elements of the *same* type (e.g. `int`) in contiguous memory.
  - Each [element]{.hl} of the array is accessed using an [index]{.hl}.

- Instead of declaring 100 variables `num0, num1, …, num99`, it is far easier to declare a single array `nums` with 100 elements and access them as `nums[0], nums[1], …, nums[99]`.

- Declaring an array specifies the element type, an identifier, and a size:

```cpp
elementType arrayName[SIZE];   // SIZE must be a const
```

<div class="sub-item">

When declared without initialization, the elements hold arbitrary values.

</div>

---
layout: prism
heading: "Arrays (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- To assign a value to an element of an initialized array, use:

```cpp
arrayName[index] = value;
```

- The declaration and values can also be written together in a shorthand form.

</div>
<div>

```cpp
double myList[3];
myList[0] = 0.1;
myList[1] = 2.9;
myList[2] = -1.4;
```

<div style="height: 1.5rem;"></div>

```cpp
// shorthand
elementType arrayName[SIZE]
    = {value0, ..., valuek};

double myList[3] = {0.1, 2.9, -1.4};
```

</div>
</div>

---
layout: prism
heading: "Arrays (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Declaration and initialization must happen in a *single* statement.

- When both are done at once, the array size may be [omitted]{.hl}.

- Only *part* of an array may be initialized; the remaining elements are set to `0`.

</div>
<div>

```cpp
double myList[3];
myList = {0.1, 2.9, -1.4}; // syntax error

// size may be omitted
double myList[] = {0.1, 2.9, -1.4};

// partial initialization
double myList[3] = {0.1};
// elements 2 and 3 hold 0
```

</div>
</div>

---
layout: prism
heading: "Array Processing (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Array elements are frequently processed with a `for` loop.

- Common operations:
  - initialize an array from input,
  - initialize with random values (`rand() % 100`),
  - print the elements.

</div>
<div>

<CppRunner stdin="1 2 3 4 5 6 7 8 9 10">

```cpp
#include <iostream>
using namespace std;

int main() {
    const int ARRAY_SIZE = 10;
    double myList[ARRAY_SIZE];

    // Initialize array from input
    cout << "Enter " << ARRAY_SIZE << " values: ";
    for (int i = 0; i < ARRAY_SIZE; i++)
        cin >> myList[i];

    // Print the array elements
    for (int i = 0; i < ARRAY_SIZE; i++)
        cout << myList[i] << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Array Processing (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- More common array operations:
  - copy an array element-by-element,
  - sum all elements,
  - find the maximum,
  - find the *smallest* index of the maximum element.

- What if we wanted the *largest* index of the maximum instead?

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int ARRAY_SIZE = 6;
    double myList[ARRAY_SIZE] = {2, 9, 5, 4, 8, 9};
    double list[ARRAY_SIZE];

    for (int i = 0; i < ARRAY_SIZE; i++)   // copy
        list[i] = myList[i];

    double total = 0;                      // sum
    for (int i = 0; i < ARRAY_SIZE; i++)
        total += myList[i];

    double max = myList[0];                // max + index
    int indexOfMax = 0;
    for (int i = 1; i < ARRAY_SIZE; i++)
        if (myList[i] > max) {
            max = myList[i];
            indexOfMax = i;
        }

    cout << "Sum = " << total << endl;
    cout << "Max = " << max << endl;
    cout << "Smallest index of max = " << indexOfMax << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Array Processing (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [Shuffling]{.hl}: for `i` from the last index down to `1`, pick a random `j` in `[0, i]` and swap `myList[i]` with `myList[j]`.

- [Shifting]{.hl}: shift every element one position to the left, and move the first element into the vacated last position.

```cpp
// shuffle (sketch)
for (int i = ARRAY_SIZE - 1; i > 0; i--) {
    int j = rand() % (i + 1);
    swap(myList[i], myList[j]);
}
```

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int ARRAY_SIZE = 6;
    double myList[ARRAY_SIZE] = {1, 2, 3, 4, 5, 6};

    // Shift elements left; wrap first element to the last
    double temp = myList[0];        // retain the first element
    for (int i = 1; i < ARRAY_SIZE; i++)
        myList[i - 1] = myList[i];
    myList[ARRAY_SIZE - 1] = temp;  // fill in the last position

    cout << "After left shift: ";
    for (int i = 0; i < ARRAY_SIZE; i++)
        cout << myList[i] << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Lab: Passing Arrays to Functions (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- When an array argument is passed to a function, the [starting address]{.hl} of the array is passed to the function's array parameter.

- The size is passed separately, since the parameter carries no length information.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void printArray(int list[], int arraySize); // prototype

int main() {
    int numbers[5] = {1, 4, 3, 6, 8};
    printArray(numbers, 5);   // invoke the function
    cout << endl;
    return 0;
}

void printArray(int list[], int arraySize) {
    for (int i = 0; i < arraySize; i++)
        cout << list[i] << " ";
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Lab: Passing Arrays to Functions (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A scalar argument (`x`) is passed [by value]{.hl}: modifying the parameter inside `m` does **not** change `x`.

- An array argument (`y`) shares its storage with the parameter, so `numbers[0] = 5555` **does** change `y[0]`.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void m(int, int[]);

int main() {
    int x = 1;      // a single int value
    int y[10];      // an array of int values
    y[0] = 1;       // initialize y[0]

    m(x, y);        // invoke m with x and y

    cout << "x is " << x << endl;
    cout << "y[0] is " << y[0] << endl;
    return 0;
}

void m(int number, int numbers[]) {
    number = 1001;      // new value to number
    numbers[0] = 5555;  // new value to numbers[0]
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Lab: Protecting Array Arguments with const"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- To prevent a function from changing the values of an array parameter, declare it as a [`const`]{.hl} array parameter.

- Any attempt to modify a `const` array parameter is caught by the compiler:
  - uncommenting `list[0] = 100;` produces a *compile error*.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void p(const int list[], int arraySize) {
    // list[0] = 100;  // Compile error: list is const!
    cout << "Read-only first element: "
         << list[0] << endl;
}

int main() {
    int numbers[5] = {1, 4, 3, 6, 8};
    p(numbers, 5);
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Lab: Returning an Array from a Function"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// newList is the reversal of list
void reverse(const int list[], int newList[], int size) {
    for (int i = 0, j = size - 1; i < size; i++, j--)
        newList[j] = list[i];
}

void printArray(const int list[], int size) {
    for (int i = 0; i < size; i++)
        cout << list[i] << " ";
}

int main() {
    const int SIZE = 6;
    int list[] = {1, 2, 3, 4, 5, 6};
    int newList[SIZE];

    reverse(list, newList, SIZE);

    cout << "The original array: ";
    printArray(list, SIZE);
    cout << endl;

    cout << "The reversed array: ";
    printArray(newList, SIZE);
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Array Search — Linear Search"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [Searching]{.hl} is the task of finding a particular element in an array.

- In [linear search]{.hl}, the [key]{.hl} is compared with array elements one-by-one from start to end. It returns the index when a match is found, or `-1` otherwise.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int linearSearch(const int list[], int key, int arraySize) {
    for (int i = 0; i < arraySize; i++)
        if (key == list[i])
            return i;
    return -1;
}

int main() {
    int list[] = {1, 4, 3, 6, 8, 2, 9};
    cout << "index of 6: " << linearSearch(list, 6, 7) << endl;
    cout << "index of 5: " << linearSearch(list, 5, 7) << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Array Search — Binary Search (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [Binary search]{.hl} works only on a [sorted]{.hl} array. It compares the key with the middle element and narrows the search:
  - if the key is *less* than the middle, search the front half;
  - if the key *equals* the middle, the value is found and the search ends;
  - if the key is *greater*, search the back half.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w10/cpp-w10-image23.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Array Search — Binary Search (2/2)"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int binarySearch(const int list[], int key, int listSize) {
    int low = 0;
    int high = listSize - 1;

    while (high >= low) {
        int mid = (low + high) / 2;
        if (key < list[mid])
            high = mid - 1;
        else if (key == list[mid])
            return mid;
        else
            low = mid + 1;
    }

    return -low - 1;   // not found: insertion point encoded
}

int main() {
    int list[] = {2, 4, 7, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79};
    cout << "index of 11: " << binarySearch(list, 11, 13) << endl;
    cout << "search  12 : " << binarySearch(list, 12, 13) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Array Sort — Selection Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [Selection sort]{.hl} finds the smallest number in the array, swaps it with the first element, then repeats on the remainder (excluding the first element), and so on.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w10/cpp-w10-image26.png" class="tikz-fig" style="width: 100%;" />

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void selectionSort(double list[], int listSize) {
    for (int i = 0; i < listSize - 1; i++) {
        // Find the minimum in list[i..listSize-1]
        double currentMin = list[i];
        int currentMinIndex = i;

        for (int j = i + 1; j < listSize; j++)
            if (currentMin > list[j]) {
                currentMin = list[j];
                currentMinIndex = j;
            }

        // Swap if necessary
        if (currentMinIndex != i) {
            list[currentMinIndex] = list[i];
            list[i] = currentMin;
        }
    }
}

int main() {
    double list[] = {2, 9, 5, 4, 8, 1, 6};
    selectionSort(list, 7);
    for (int i = 0; i < 7; i++) cout << list[i] << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Two-Dimensional Arrays"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Table or matrix data can be represented with a [two-dimensional array]{.hl}.

- A 2D array is declared with the syntax:

```cpp
elementType arrayName[ROW_SIZE][COLUMN_SIZE];
```

```cpp
int m[4][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {10, 11, 12}
};
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w10/cpp-w10-image27.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "2D Array Processing (1/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Processing a 2D array typically uses a [nested `for`]{.hl} loop.

- Initialize each element with a random value (`rand() % 100`) using an outer loop over rows and an inner loop over columns.

- A fixed seed (`srand(1)`) keeps the output reproducible.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    srand(1);
    const int ROW_SIZE = 3, COLUMN_SIZE = 4;
    int matrix[ROW_SIZE][COLUMN_SIZE];

    // Initialize with random values
    for (int row = 0; row < ROW_SIZE; row++)
        for (int column = 0; column < COLUMN_SIZE; column++)
            matrix[row][column] = rand() % 100;

    for (int row = 0; row < ROW_SIZE; row++) {
        for (int column = 0; column < COLUMN_SIZE; column++)
            cout << matrix[row][column] << " ";
        cout << endl;
    }
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "2D Array Processing (2/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Print the array, row by row.

- Sum *all* elements with a nested loop.

- Sum *each column* by iterating columns on the outside and rows on the inside.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int ROW_SIZE = 3, COLUMN_SIZE = 4;
    int matrix[ROW_SIZE][COLUMN_SIZE] = {
        {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}
    };

    int total = 0;
    for (int row = 0; row < ROW_SIZE; row++) {
        for (int column = 0; column < COLUMN_SIZE; column++) {
            cout << matrix[row][column] << " ";
            total += matrix[row][column];
        }
        cout << endl;
    }
    cout << "Total sum is " << total << endl;

    for (int column = 0; column < COLUMN_SIZE; column++) {
        int colTotal = 0;
        for (int row = 0; row < ROW_SIZE; row++)
            colTotal += matrix[row][column];
        cout << "Sum for column " << column << " is " << colTotal << endl;
    }
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "2D Array Processing (3/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Find the [row with the largest sum]{.hl}.

- Seed `maxRow` with the sum of row `0`, then compare each subsequent row's total against it, tracking the index of the best row.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int ROW_SIZE = 3, COLUMN_SIZE = 4;
    int matrix[ROW_SIZE][COLUMN_SIZE] = {
        {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}
    };

    int maxRow = 0, indexOfMaxRow = 0;
    for (int column = 0; column < COLUMN_SIZE; column++)
        maxRow += matrix[0][column];   // sum of first row

    for (int row = 1; row < ROW_SIZE; row++) {
        int totalOfThisRow = 0;
        for (int column = 0; column < COLUMN_SIZE; column++)
            totalOfThisRow += matrix[row][column];
        if (totalOfThisRow > maxRow) {
            maxRow = totalOfThisRow;
            indexOfMaxRow = row;
        }
    }

    cout << "Row " << indexOfMaxRow
         << " has the maximum sum of " << maxRow << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "2D Array Processing (4/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [Shuffle]{.hl} a 2D array: for every cell `(i, j)`, pick a random cell `(i1, j1)` and swap the two.

- With a fixed seed (`srand(1)`), the shuffled result is deterministic and reproducible.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    srand(1);
    const int ROW_SIZE = 3, COLUMN_SIZE = 4;
    double matrix[ROW_SIZE][COLUMN_SIZE] = {
        {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}
    };

    for (int i = 0; i < ROW_SIZE; i++)
        for (int j = 0; j < COLUMN_SIZE; j++) {
            int i1 = rand() % ROW_SIZE;
            int j1 = rand() % COLUMN_SIZE;
            double temp = matrix[i][j];   // swap (i,j) and (i1,j1)
            matrix[i][j] = matrix[i1][j1];
            matrix[i1][j1] = temp;
        }

    for (int i = 0; i < ROW_SIZE; i++) {
        for (int j = 0; j < COLUMN_SIZE; j++)
            cout << matrix[i][j] << " ";
        cout << endl;
    }
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Lab: Passing a 2D Array to a Function"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- When passing a 2D array to a function, the [column size]{.hl} must be specified in the parameter's type declaration.

- The row size may be left blank (`a[][COLUMN_SIZE]`) and passed as a separate argument.

</div>
<div>

<CppRunner stdin="1 2 3 4 5 6 7 8 9 10 11 12">

```cpp
#include <iostream>
using namespace std;

const int COLUMN_SIZE = 4;

int sum(const int a[][COLUMN_SIZE], int rowSize) {
    int total = 0;
    for (int row = 0; row < rowSize; row++)
        for (int column = 0; column < COLUMN_SIZE; column++)
            total += a[row][column];
    return total;
}

int main() {
    const int ROW_SIZE = 3;
    int m[ROW_SIZE][COLUMN_SIZE];
    cout << "Enter " << ROW_SIZE << " rows and "
         << COLUMN_SIZE << " columns: " << endl;
    for (int i = 0; i < ROW_SIZE; i++)
        for (int j = 0; j < COLUMN_SIZE; j++)
            cin >> m[i][j];
    cout << "Sum of all elements is " << sum(m, ROW_SIZE) << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Lab: Grading Exam Answers"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int NUMBER_OF_STUDENTS = 8;
    const int NUMBER_OF_QUESTIONS = 10;

    // Students' answers to the questions
    char answers[NUMBER_OF_STUDENTS][NUMBER_OF_QUESTIONS] = {
        {'A','B','A','C','C','D','E','E','A','D'},
        {'D','B','A','B','C','A','E','E','A','D'},
        {'E','D','D','A','C','B','E','E','A','D'},
        {'C','B','A','E','D','C','E','E','A','D'},
        {'A','B','D','C','C','D','E','E','A','D'},
        {'B','B','E','C','C','D','E','E','A','D'},
        {'B','B','A','C','C','D','E','E','A','D'},
        {'E','B','E','C','C','D','E','E','A','D'}
    };

    // Key to the questions
    char keys[] = {'D','B','D','C','C','D','A','E','A','D'};

    // Grade all answers
    for (int i = 0; i < NUMBER_OF_STUDENTS; i++) {
        int correctCount = 0;
        for (int j = 0; j < NUMBER_OF_QUESTIONS; j++)
            if (answers[i][j] == keys[j])
                correctCount++;
        cout << "Student " << i << "'s correct count is "
             << correctCount << endl;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Multidimensional Arrays"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- C++ allows arrays of [arbitrary dimension]{.hl}.

- By generalizing the 2D declaration, we can declare and initialize arrays of three or more dimensions.

- `scores[6][5][2]` might hold, for 6 students, 5 exams each with 2 parts (multiple-choice and essay).

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    double scores[6][5][2] = {
        {{7.5,20.5},{9.0,22.5},{15,33.5},{13,21.5},{15,2.5}},
        {{4.5,21.5},{9.0,22.5},{15,34.5},{12,20.5},{14,9.5}},
        {{6.5,30.5},{9.4,10.5},{11,33.5},{11,23.5},{10,2.5}},
        {{6.5,23.5},{9.4,32.5},{13,34.5},{11,20.5},{16,7.5}},
        {{8.5,26.5},{9.4,52.5},{13,36.5},{13,24.5},{16,2.5}},
        {{9.5,20.5},{9.4,42.5},{13,31.5},{12,20.5},{16,6.5}}
    };

    cout << "scores[0][0][0] = " << scores[0][0][0] << endl;
    cout << "scores[5][4][1] = " << scores[5][4][1] << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "HW_W10: Bubble Sort then Binary Search"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [Bubble sort]{.hl} is similar to selection sort, but the way it finds the maximum/minimum differs slightly.

- Sort a 1D array using bubble sort, then find a key with binary search.
  - You only need to implement `binarySearch` (no `main` required).

- Save as `HW_W10_20XXXXXX.cpp` and upload to the LMS.

```text
bubbleSort(A[], n):
    for last <- n-1 downto 1:
        for i <- 0 to last-1:
            if (A[i] > A[i+1]):
                swap(A[i], A[i+1])
```

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void bubbleSort(int A[], int n) {
    for (int last = n - 1; last >= 1; last--)
        for (int i = 0; i <= last - 1; i++)
            if (A[i] > A[i + 1]) {
                int t = A[i]; A[i] = A[i + 1]; A[i + 1] = t;
            }
}

int binarySearch(const int list[], int key, int listSize) {
    int low = 0, high = listSize - 1;
    while (high >= low) {
        int mid = (low + high) / 2;
        if (key < list[mid])      high = mid - 1;
        else if (key == list[mid]) return mid;
        else                       low = mid + 1;
    }
    return -low - 1;
}

int main() {
    int A[] = {5, 2, 9, 1, 7, 3};
    bubbleSort(A, 6);
    for (int i = 0; i < 6; i++) cout << A[i] << " ";
    cout << endl;
    cout << "index of 7: " << binarySearch(A, 7, 6) << endl;
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
