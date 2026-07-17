---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 14
download: true
info: |
  ## C++ Programming Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-14-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 14: Final Review</p>

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

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A function is made up of a [return value type]{.hl}, a [function name]{.hl}, [parameters]{.hl}, and a [function body]{.hl}.
  - The [function header]{.hl} specifies the return value type, the name, and the parameters.
  - Variables declared in the header are [formal parameters]{.hl}; the values supplied by the caller are [arguments]{.hl}.

- The return value type is the data type of the value the function *returns*.
  - A [value-returning function]{.hl} returns a value; a [`void` function]{.hl} (e.g. `srand`) returns none.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Recap: void Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- A `void` function does not return a value. It needs no `return` statement, but `return;` may be used to end execution and go back to the caller.

<CppRunner stdin="85">

```cpp
#include <iostream>
using namespace std;

// Print the letter grade for a numeric score
void printGrade(double score) {
    if (score >= 90.0)      cout << 'A' << endl;
    else if (score >= 80.0) cout << 'B' << endl;
    else if (score >= 70.0) cout << 'C' << endl;
    else if (score >= 60.0) cout << 'D' << endl;
    else                    cout << 'F' << endl;
    return;   // optional early exit from a void function
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

---
layout: prism
heading: "Recap: Passing Arguments by Value"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- Arguments are normally [passed by value]{.hl}: when a function is called, the value of each argument is copied into a parameter.

- Arguments are bound to the called function's parameters *in order* — this is called [parameter order association]{.hl}.

- Because the function works on copies, changes made to the parameters do **not** affect the original arguments in the caller.

---
layout: prism
heading: "Recap: Passing Arguments by Reference"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- A parameter can be [passed by reference]{.hl}, making the formal parameter an [alias]{.hl} for the argument — changing the parameter also changes the argument.
- A [reference variable]{.hl} acts as an alias for the original variable. Declare it by placing `&` after the type (or before the name): `int& r = count;`.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void increaseByValue(int v)      { v++; }  // works on a copy
void increaseByReference(int& r) { r++; }  // r is an alias for the argument

int main() {
    int count = 5;
    increaseByValue(count);
    cout << "after pass-by-value:     " << count << endl;  // still 5
    increaseByReference(count);
    cout << "after pass-by-reference: " << count << endl;  // now 6
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Local, Global, and Static Local Variables"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- C++ variables are classified as [local]{.hl}, [global]{.hl}, or [static local]{.hl} variables.

- The [scope]{.hl} of a variable is the region of the program in which it can be referenced.

- A variable defined inside a function is a [local variable]{.hl}.

- A variable declared outside all functions, accessible to every function in the file, is a [global variable]{.hl}.
  - Local variables have no default value, but global variables are initialized to `0`.

---
layout: prism
heading: "Recap: Static Local Variables"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- When a function finishes, its local variables disappear from memory — such variables are [automatic variables]{.hl}. A [static local variable]{.hl} (`static`) instead keeps its value across successive calls and lives until the program ends.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int nextCount() {
    static int count = 0;   // retained across calls, not re-initialized
    count++;
    return count;
}

int main() {
    for (int i = 0; i < 5; i++)
        cout << "call " << i << " -> " << nextCount() << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Arrays"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- An [array]{.hl} stores a collection of many data items. In C++ it is a data structure holding a fixed number of elements of the same type in [contiguous]{.hl} memory.

- Array [elements]{.hl} are accessed by an [index]{.hl}. Instead of declaring `num0, num1, ..., num99`, we declare one array `nums` and access `nums[0], nums[1], ..., nums[99]`.

- An array declaration specifies the element type, the name, and the size: `elementType arrayName[SIZE];` where `SIZE` is a constant (`const`).
  - A freshly declared array is filled with arbitrary values.

---
layout: prism
heading: "Recap: Objects and Classes"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [class]{.hl} defines the *properties* and *behavior* of an [object]{.hl}.

- In [object-oriented programming]{.hl}, programs are built from objects. An object is a clearly identifiable entity with its own unique characteristics — its [state]{.hl} and [behavior]{.hl}.

- An object's state (its [properties]{.hl} / [attributes]{.hl}) is represented by [data fields]{.hl}.
  - Example: a *circle* object has a `radius` data field describing its property.

- An object's behavior (its [actions]{.hl}) is defined by functions.

---
layout: prism
heading: "Recap: Classes"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Objects of the same kind are defined by a common class.

- A class is a [template]{.hl} (blueprint) that determines what data fields and functions an object will have; an object is an [instance]{.hl} of the class.
  - Creating an instance is called [instantiation]{.hl}.
  - From a single `Circle` class we can create countless `Circle` objects.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image6.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Recap: Constructing and Using Objects"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- An object's data and functions are accessed with the object name and the [dot operator]{.hl} (`.`).

- In OOP, the [members]{.hl} of an object are its data fields and functions. A newly created object is allocated in memory; after creation, the [member access operator]{.hl} `.` reaches its data and calls its functions.

- A data field being accessed is an [instance variable]{.hl}; a function being called is an [instance function]{.hl}.

```cpp
circle1.radius;      // reference the object's data field
circle1.getArea();   // invoke a function on the object
```

---
layout: prism
heading: "Recap: Object-Oriented Concepts"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Rather than splitting a program merely into data and procedures, OOP divides it into [objects]{.hl} — bundles of a procedure (method / behavior / function) with data (variables) — and focuses on their interactions. In C++ this is naturally expressed with a [class]{.hl}.

- Functions structure *how data is processed* well, but do not structure the *data* itself. OOP mirrors the real world, where every object couples both properties and behavior.

- By hiding internal implementation details ([information hiding]{.hl}), OOP raises cohesion within a module and lowers coupling between modules, improving flexibility and maintainability.

---
layout: prism
heading: "Recap: Instance and Static Members"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [static variable]{.hl} is stored in one shared memory location: when one object changes it, every object of the class is affected.
  - In UML notation, static variables and functions are [underlined]{.hl}.

- Static members use the `static` keyword.

```cpp
static int numberOfObjects;
static int getNumberOfObjects();
```

</div>
<div>

<div style="height: 1.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image7.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Recap: Pointers"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [pointer variable]{.hl} (pointer) is declared to store a *memory address* as its value, whereas an ordinary variable stores a data value (integer, real, character, ...).

- Every byte of memory has a unique address; a variable's address is the address of its first byte. An `int` occupies 4 bytes, so the first byte is the variable's address.

- A pointer must be declared before use: `dataType* pVarName;`, then assigned an address: `pVarName = &varName;`.

---
layout: prism
heading: "Recap: Pointers — & and *"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `&` — the [address-of operator]{.hl}: `&count` is the address of `count`.

- `*` — the [dereference operator]{.hl}: `*pCount` is the value stored at the location the pointer `pCount` points to.

```cpp
int count = 5;
string s("ABC");
int* pCount;
string* pString;
pCount = &count;   // pCount now holds count's address
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image8.png" class="tikz-fig" style="width: 78%;" />

</div>
</div>

---
layout: prism
heading: "Recap: Arrays and Pointers"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- In C++ an array is fundamentally a pointer: the array's name is a *constant pointer* to its first element, so `list[i]`, `*(list + i)`, `p[i]`, and `*(p + i)` all name the same element.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int list[6] = {11, 12, 13, 14, 15, 16};
    int* p = list;   // the array name is a pointer to the first element

    for (int i = 0; i < 6; i++) {
        cout << "index " << i
             << "  list[i]=" << list[i]
             << "  *(list+i)=" << *(list + i)
             << "  p[i]=" << p[i]
             << "  *(p+i)=" << *(p + i) << endl;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Dynamic Object Creation and Access"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- The `new` operator creates a dynamic object. To reach a member through a pointer, dereference it and use `.`, or use the shorthand [arrow operator]{.hl} `->`. `delete` explicitly destroys the object.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string* pString = new string("abcdefg");
    cout << *pString << endl;                             // abcdefg
    cout << "First three (via *.): "
         << (*pString).substr(0, 3) << endl;             // dot operator
    cout << "First three (via ->): "
         << pString->substr(0, 3) << endl;               // arrow operator

    delete pString;   // explicitly delete the object
    // Reading *pString after delete is undefined behavior — omitted.
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: The this Pointer"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- The [`this` pointer]{.hl} refers to the calling object itself, and is used to reference a hidden data field (when a parameter shares the field's name).

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Circle {
public:
    Circle() { radius = 1; }
    Circle(double radius) { this->radius = radius; }      // this-> disambiguates
    double getRadius() { return radius; }
    void setRadius(double radius) {
        this->radius = (radius >= 0) ? radius : 0;
    }
    double getArea() { return radius * radius * 3.14159; }
private:
    double radius;
};

int main() {
    Circle c(5);
    cout << "radius = " << c.getRadius() << ", area = " << c.getArea() << endl;
    c.setRadius(-3);   // negative rejected -> 0
    cout << "after setRadius(-3): radius = " << c.getRadius() << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Destructor"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- A [destructor]{.hl} is the opposite of a constructor: the constructor runs when an object is created, the destructor when it is destroyed. Every class has a default destructor unless one is defined. It shares the constructor's name preceded by a tilde (`~`).

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Circle {
public:
    Circle(double r) { radius = r; cout << "Circle(" << radius << ") created\n"; }
    ~Circle()        { cout << "Circle(" << radius << ") destroyed\n"; }
    double getArea() { return radius * radius * 3.14159; }
private:
    double radius;
};

int main() {
    Circle c(2.0);
    cout << "Area = " << c.getArea() << endl;
    {
        Circle temp(1.0);        // created here
        cout << "Inner area = " << temp.getArea() << endl;
    }                            // temp destroyed at end of the inner scope
    cout << "After inner scope\n";
    return 0;                    // c destroyed here
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Shallow Copy and Deep Copy"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

- Every class has a *copy constructor* used to copy an object. Using the default copy constructor or the assignment operator (`=`) performs a [shallow copy]{.hl}: when a data field is a pointer, only the pointer's *address* is copied, not the content it points to.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image11.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

- A [deep copy]{.hl} copies the *content* the pointer refers to; we define our own copy constructor to achieve it, giving each object its own independent data.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image10.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Recap: Deep Copy in Action"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- A user-defined copy constructor allocates a *new* array, so the copy is independent — changing `c2` leaves `c1` untouched.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

class Course {
public:
    Course(int cap) : capacity(cap), numStudents(0) { students = new string[cap]; }
    // Deep copy constructor: allocate our own array and copy the contents
    Course(const Course& other)
        : capacity(other.capacity), numStudents(other.numStudents) {
        students = new string[other.capacity];
        for (int i = 0; i < numStudents; i++) students[i] = other.students[i];
    }
    ~Course() { delete[] students; }
    void add(const string& s) { students[numStudents++] = s; }
    void setFirst(const string& s) { if (numStudents) students[0] = s; }
    string first() const { return numStudents ? students[0] : "(none)"; }
private:
    string* students; int capacity; int numStudents;
};

int main() {
    Course c1(10);
    c1.add("Alice");
    Course c2 = c1;          // deep copy -> independent array
    c2.setFirst("Zoe");      // modify only c2's data
    cout << "c1 first student: " << c1.first() << endl;   // Alice
    cout << "c2 first student: " << c2.first() << endl;   // Zoe
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Final Exam"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [40 points]{.hl} total, [15–20 questions]{.hl}, written in Korean.

- Question formats include:
  - Simple true/false (O-X) quizzes.
  - Predicting the output of C++ code (including conditionals and loops).

- Conceptual descriptions (functions, classes, object-orientation, pointers, ...).

- Writing a [pseudo-algorithm]{.hl} (hand-writing the code is fine if you prefer).

- Fixing errors in given code.

- Solving a goal-oriented problem (cf. midterm: Monte-Carlo simulation).

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
