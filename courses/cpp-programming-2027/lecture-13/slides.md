---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 13
download: true
info: |
  ## C++ Programming Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-13-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 13: Pointers and Dynamic Memory</p>

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
heading: "Overview: Object-Oriented Concepts"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Rather than splitting a program merely into *data* and *procedures*, [object-oriented programming]{.hl} divides it into fundamental units called [objects]{.hl} and focuses on how those objects interact.
  - An [object]{.hl} bundles together the *methods* (behavior, functions) that perform a single role with the *data* (variables) it acts on. In C++ this is expressed naturally through a [class]{.hl}.

- Functions structure the *processing* of data well, but they do not structure the *data* itself. Object orientation mirrors the real world, where every object relates to both its attributes and its behavior.

- By hiding the internal details of objects from the outside ([information hiding]{.hl}), we raise *cohesion* within a module and lower *coupling* between modules — improving flexibility and maintainability.

---
layout: prism
heading: "Overview: Instance and Static Members"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A [static variable]{.hl} stores its value in one shared memory location: if one object changes it, *every* object of the same class is affected.
  - In UML notation, static variables and functions are shown [underlined]{.hl}.

- Static variables and functions use the `static` keyword.

```cpp
static int numberOfObjects;
static int getNumberOfObjects();
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Pointers (1/5)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [pointer variable]{.hl} (or simply *pointer*) is declared to hold a [memory address]{.hl} as its value, whereas an ordinary variable holds a data value (integer, real number, character, ...).

- Every byte of memory has a unique address, so a variable's address is the address of the *first* byte allocated to it. Since an `int` occupies 4 bytes, its first byte is the variable's address.

- Like any variable, a pointer must be declared before use, following this syntax:

```cpp
dataType* pVarName;
```

- After declaration, we may assign it the address of a variable:

```cpp
pVarName = &varName;
```

---
layout: prism
heading: "Pointers (2/5)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `&` — the [address-of operator]{.hl}.
  - `&count` means *the address of* `count`.

- `*` — the [dereference operator]{.hl}.
  - `*pCount` means *the value stored at* the location that `pCount` points to.

```cpp
int count = 5;
short status = 2;
char letter = 2;
string s("ABC");
int* pCount;
short* pStatus;
char* pLetter;
string* pString;
pCount = &count;
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image3.png" class="tikz-fig" style="width: 78%;" />

</div>
</div>

---
layout: prism
heading: "Lab: TestPointer.cpp"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 5;
    int* pCount = &count;

    cout << "The value of count is " << count << endl;
    cout << "The address of count is " << &count << endl;
    cout << "The address of count is " << pCount << endl;
    cout << "The value of count is " << *pCount << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Pointers (3/5)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A pointer can be initialized at declaration, or later through an assignment statement.

- Referring to a value *through* a pointer is called [indirection]{.hl}.

- A pointer's type must match the type of the variable it points to.

```cpp
*pCount = &count; // wrong
pCount = &count;  // correct

count++;                 // direct reference
cout << count << endl;
(*pCount)++;             // indirect reference
cout << count << endl;   // *pCount is the value pCount points to

int area = 1;
double* pArea = &area;   // wrong: type mismatch
```

---
layout: prism
heading: "Pointers (4/5)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The [assignment operator]{.hl} may be applied to pointers as well.

- `pX = pY` copies the *address*, so `pX` now points where `pY` points.

- `*pX = *pY` copies the *value*, leaving both pointers where they were.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image4.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Pointers (5/5)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

Copying the pointer — `pX = pY`:

```cpp
int x = 5, y = 6;
int* pX = &x;
int* pY = &y;
// x: 5  pX: 0x...45c
// y: 6  pY: 0x...458
pX = pY;
// x: 5  pX: 0x...458
// y: 6  pY: 0x...458
```

</div>
<div>

Copying the value — `*pX = *pY`:

```cpp
int x = 5, y = 6;
int* pX = &x;
int* pY = &y;
// x: 5  pX: 0x...45c
// y: 6  pY: 0x...458
*pX = *pY;
// x: 6  pX: 0x...45c
// y: 6  pY: 0x...458
```

</div>
</div>

<div style="margin-top: 1rem;"></div>

- Note `int* pX = &x, pY = &y;` declares `pX` as `int*` but `pY` as a plain `int` — the `*` binds to the *name*, not the type.

---
layout: prism
heading: "The typedef Keyword"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `typedef` lets a user define a [synonymous type]{.hl}, simplifying code and helping avoid subtle errors.

```cpp
typedef existingType newType;
```

- It does **not** create a new type — only a *synonym* for an existing one.
  - `int* p1, p2;` gives `p1` as `int*` but `p2` as `int`, while `intPointer p3, p4;` makes *both* `int*`.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    typedef int integer;      // integer is a synonym for int
    integer value = 40;
    cout << "value = " << value << endl;

    typedef int* intPointer;  // intPointer is a synonym for int*
    int a = 1, b = 2;
    intPointer p3 = &a, p4 = &b;  // both are int*
    cout << "*p3 = " << *p3
         << ", *p4 = " << *p4 << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Pointers and const"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [constant pointer]{.hl} must be declared *and* initialized in a single statement; its target cannot be changed afterward.

- A [pointer to constant data]{.hl} may itself be reassigned, but cannot be used to modify what it points to.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    double radius = 5;
    double* const p = &radius;  // constant pointer
    *p = 6;                     // OK: radius becomes 6
    cout << "radius = " << radius << endl;
    // p = &length;             // ERROR: p is constant

    double length = 10;
    const double* p1 = &radius; // pointer to const data
    // *p1 = 7;                 // ERROR: cannot modify via p1
    p1 = &length;               // OK: p1 itself is not const
    cout << "*p1 = " << *p1 << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Arrays and Pointers"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- In C++ an array is fundamentally a [pointer]{.hl}: the array's name is a *constant pointer* to its first element. Thus `list[i]`, `*(list + i)`, `*(p + i)`, and `p[i]` all refer to the same element.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image5.png" class="tikz-fig" style="width: 62%; margin: 0.4rem auto;" />

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int list[6] = {11, 12, 13, 14, 15, 16};
    int* p = list;                     // array name is a pointer to list[0]
    for (int i = 0; i < 6; i++) {
        cout << "list[" << i << "]=" << list[i]
             << "  *(list+" << i << ")=" << *(list + i)
             << "  *(p+" << i << ")=" << *(p + i)
             << "  p[" << i << "]=" << p[i] << endl;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Passing and Returning Pointers in Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A pointer can be passed to a function [by value]{.hl} or [by reference]{.hl}. Consider calling `f(p1, &p2)` where `f` takes two pointers `q1` and `q2`:
  - `q1` is passed *by value* into `p1`, so `*p1` and `*q1` refer to the same content. Changing `*p1` changes `*q1`, but changing `p1` itself does **not** change `q1`.
  - `q2` is passed *by reference* into `p2`, so the two become [aliases]{.hl}: changing either `*p2` or `p2` also changes `*q2` and `q2`.

- Just as a function can take a pointer parameter, it can also *return* a pointer — the return type in the header must be a pointer type.

```cpp
int* returnList(int* list);
```

---
layout: prism
heading: "Lab: TestPointerArgument.cpp"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void swap1(int n1, int n2)      { int t = n1; n1 = n2; n2 = t; }  // by value
void swap2(int& n1, int& n2)    { int t = n1; n1 = n2; n2 = t; }  // by reference
void swap3(int* p1, int* p2)    { int t = *p1; *p1 = *p2; *p2 = t; }  // pointer by value
void swap4(int*& p1, int*& p2)  { int* t = p1; p1 = p2; p2 = t; }     // pointer by reference

int main() {
    int num1 = 1, num2 = 2;
    cout << "start:  num1=" << num1 << " num2=" << num2 << endl;  // 1 2
    swap1(num1, num2);
    cout << "swap1:  num1=" << num1 << " num2=" << num2 << endl;  // 1 2 (no effect)
    swap2(num1, num2);
    cout << "swap2:  num1=" << num1 << " num2=" << num2 << endl;  // 2 1
    swap3(&num1, &num2);
    cout << "swap3:  num1=" << num1 << " num2=" << num2 << endl;  // 1 2

    int* p1 = &num1;
    int* p2 = &num2;
    swap4(p1, p2);
    cout << "swap4:  *p1=" << *p1 << " *p2=" << *p2 << endl;      // *p1=2 *p2=1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Dynamic Persistent Memory Allocation (1/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The `new` operator creates [persistent memory]{.hl} at run time for primitive values, arrays, and objects.

- A function that returns a *reversed copy* of an array, without altering the input, can be written as:

<div class="sub-item-enum">

1. Take the original array `list` as input.
2. Declare a `result` array of the same size.
3. Loop, copying elements in reverse order.
4. Return `result` through a pointer.

</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image6.png" class="tikz-fig" style="width: 100%; margin-top: 3rem;" />

</div>
</div>

---
layout: prism
heading: "Lab: ArrayReverse.cpp"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int* reverse(const int* list, int size) {
    int* result = new int[size];   // dynamic array: persists after the function returns
    for (int i = 0, j = size - 1; i < size; i++, j--) {
        result[j] = list[i];
    }
    return result;
}

int main() {
    int list[] = {1, 2, 3, 4, 5, 6};
    int* p = reverse(list, 6);
    for (int i = 0; i < 6; i++) {
        cout << p[i] << " ";
    }
    cout << endl;
    delete[] p;   // match every new with a delete
    return 0;
}
```

</CppRunner>

<!-- A local `int result[6]` would be discarded when the function returns (a dangling pointer); `new int[6]` fixes this. -->

---
layout: prism
heading: "Dynamic Persistent Memory Allocation (2/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Memory on a function's [call stack]{.hl} does not persist — it is discarded when the function returns. To keep `result` alive afterward, we must allocate it in persistent storage.

- [Dynamic memory allocation]{.hl} with `new` provides that persistent storage; an array created this way is a [dynamic array]{.hl}.
  - An ordinary array must have a *constant* size, but a dynamic array's size is decided at run time, so an integer *variable* may be used.

- Memory allocated with `new` is persistent — it lives until explicitly removed or the program ends. Removal uses the `delete` operator.

```cpp
delete p;
```

---
layout: prism
heading: "Dynamic Persistent Memory Allocation (3/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.9em;
}
</style>

- After the memory a pointer points to is deleted, the pointer's value becomes [undefined]{.hl}.

- If another pointer refers to the same deleted memory, it too becomes undefined; such a pointer is called a [dangling pointer]{.hl}.

- If a pointer is accidentally reassigned *before* its memory is deleted, the old block can no longer be reached or freed — this is a [memory leak]{.hl}.

- Pairing every `new` with a matching `delete` is good programming practice for preventing memory leaks.

---
layout: prism
heading: "Dynamic Persistent Memory Allocation (4/4)"
---

<div class="flex justify-center" style="margin-top: 1rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image7.png" class="tikz-fig" style="width: 72%;" />
</div>

<div style="margin-top: 0.8rem;"></div>

- `(a)` `int* p = new int;` allocates memory for an `int` and assigns its address to `p`; `(b)` `*p = 45;` stores 45 there; `(c)` `p = new int;` reassigns `p` — the old block is now a [leak]{.hl}.

---
layout: prism
heading: "Creating and Accessing Dynamic Objects"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The `new` operator can create a [dynamic object]{.hl}.

- To access a member through a pointer, dereference the pointer and use the dot (`.`) operator.

- The [member selection operator]{.hl} — the arrow (`->`) — is a shorthand for accessing members through a pointer.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string* pString = new string("abcdefg");
    cout << *pString << endl;            // abcdefg
    cout << "first three (.) : "
         << (*pString).substr(0, 3) << endl;
    cout << "first three (->): "
         << pString->substr(0, 3) << endl;
    delete pString;                      // delete the object
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "The this Pointer"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The [`this` pointer]{.hl} points to the calling object itself, and is used to reach a data field that a parameter of the same name would otherwise hide.

- Here the constructor parameter `radius` shadows the field `radius`, so `this->radius` names the field explicitly.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Circle {
public:
    Circle() { radius = 1; }
    Circle(double radius) { this->radius = radius; }
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
    cout << "radius = " << c.getRadius() << endl;
    cout << "area   = " << c.getArea() << endl;
    c.setRadius(-3);
    cout << "radius = " << c.getRadius() << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Destructors"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [destructor]{.hl} is the opposite of a constructor: the constructor runs when an object is *created*, the destructor when it is *destroyed*.
  - If none is defined, every class gets a *default* destructor.

- A destructor has the same name as the class, prefixed with a tilde (`~`).

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Circle {
public:
    Circle() {
        radius = 1;
        cout << "Circle() created\n";
    }
    Circle(double r) {
        radius = r;
        cout << "Circle(" << r << ") created\n";
    }
    ~Circle() {
        cout << "Circle r=" << radius << " destroyed\n";
    }
    double getArea() { return radius * radius * 3.14159; }
private:
    double radius;
};

int main() {
    Circle c1;
    Circle c2(5);
    cout << "area of c2 = " << c2.getArea() << endl;
    return 0;   // destructors run here, in reverse order
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "The Course Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

```cpp
#ifndef COURSE_H
#define COURSE_H
#include <string>
using namespace std;

class Course {
public:
    Course(const string& courseName,
           int capacity);
    ~Course();                  // destructor
    string getCourseName() const;
    void addStudent(const string& name);
    void dropStudent(const string& name);
    string* getStudents() const;
    int getNumberOfStudents() const;
private:
    string courseName;
    string* students;           // dynamic array
    int numberOfStudents;
    int capacity;
};
#endif
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image8.png" class="tikz-fig" style="width: 100%; margin-top: 2rem;" />

</div>
</div>

---
layout: prism
heading: "Lab: Course (merged)"
---

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

class Course {
public:
    Course(const string& courseName, int capacity);
    ~Course();
    string getCourseName() const;
    void addStudent(const string& name);
    void dropStudent(const string& name);
    string* getStudents() const;
    int getNumberOfStudents() const;
private:
    string courseName;
    string* students;
    int numberOfStudents;
    int capacity;
};

Course::Course(const string& courseName, int capacity) {
    numberOfStudents = 0;
    this->courseName = courseName;
    this->capacity = capacity;
    students = new string[capacity];   // size unknown until run time
}
Course::~Course() { delete[] students; }   // free the dynamic array
string Course::getCourseName() const { return courseName; }
void Course::addStudent(const string& name) {
    students[numberOfStudents] = name;
    numberOfStudents++;
}
void Course::dropStudent(const string& name) {
    for (int i = 0; i < numberOfStudents; i++) {
        if (students[i] == name) {
            for (int j = i; j < numberOfStudents - 1; j++)
                students[j] = students[j + 1];  // shift the rest left
            numberOfStudents--;
            break;
        }
    }
}
string* Course::getStudents() const { return students; }
int Course::getNumberOfStudents() const { return numberOfStudents; }

void printCourse(Course& c) {
    cout << c.getCourseName() << " students: " << c.getNumberOfStudents() << endl;
    string* students = c.getStudents();
    for (int i = 0; i < c.getNumberOfStudents(); i++)
        cout << students[i] << " ";
    cout << endl;
}

int main() {
    Course course1("C++ Programming Section 15", 30);
    Course course2("C++ Programming Section 16", 20);
    course1.addStudent("Hyejin");
    course1.addStudent("Yejin");
    course1.addStudent("Sua");
    course1.addStudent("Yuna");
    course2.addStudent("Jeongseon");
    course2.addStudent("Yugyeong");
    course2.addStudent("Inju");
    printCourse(course1);
    printCourse(course2);
    course2.dropStudent("Yugyeong");
    printCourse(course2);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "HW_W13: Implementing dropStudent"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Implement the `dropStudent` function of the `Course` class — **only** this function; do not change its header.

- Use a conditional and a loop, and keep the data fields consistent (shift remaining students, decrease the count).

- Save as `HW_W13_20XXXXXX.cpp` and upload to the LMS.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image9.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

// dropStudent: remove the first student whose name matches, keeping order.
void dropStudent(string* students, int& count, const string& name) {
    for (int i = 0; i < count; i++) {
        if (students[i] == name) {
            for (int j = i; j < count - 1; j++)
                students[j] = students[j + 1];  // shift left
            count--;                            // one fewer student
            break;
        }
    }
}

int main() {
    string s[5] = {"Jeongseon", "Yugyeong", "Inju"};
    int count = 3;
    dropStudent(s, count, "Yugyeong");
    cout << "students: " << count << endl;
    for (int i = 0; i < count; i++) cout << s[i] << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Shallow Copy vs. Deep Copy (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Every class includes a [copy constructor]{.hl} used to copy objects.

- The default copy constructor (or `=`) performs a [shallow copy]{.hl}: when a data field is a pointer, it copies the *address*, not the contents — so both objects share one array.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image10.png" class="tikz-fig" style="width: 100%; margin-top: 0.5rem;" />

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

class Course {
public:
    Course(const string& name, int capacity) {
        numberOfStudents = 0;
        courseName = name;
        this->capacity = capacity;
        students = new string[capacity];
    }
    // no copy constructor -> default (shallow) copy
    void addStudent(const string& n) {
        students[numberOfStudents++] = n;
    }
    string* getStudents() const { return students; }
private:
    string courseName;
    string* students;
    int numberOfStudents;
    int capacity;
};

int main() {
    Course course3("C++", 10);
    Course course4(course3);   // shallow: shared array
    course3.addStudent("Gunaeun");
    course4.addStudent("Seotaeyeong");
    cout << course3.getStudents()[0] << endl;  // Seotaeyeong
    cout << course4.getStudents()[0] << endl;  // Seotaeyeong
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Shallow Copy vs. Deep Copy (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- For a [deep copy]{.hl} — copying only the *contents* a pointer refers to — we define our own copy constructor.

```cpp
class Course {
public:
    Course(const string& courseName, int capacity);
    ~Course();
    Course(const Course&);      // user-defined copy constructor
    string getCourseName() const;
    void addStudent(const string& name);
    void dropStudent(const string& name);
    string* getStudents() const;
    int getNumberOfStudents() const;
private:
    string courseName;
    string* students;
    int numberOfStudents;
    int capacity;
};
```

---
layout: prism
heading: "Shallow Copy vs. Deep Copy (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

class Course {
public:
    Course(const string& name, int capacity) {
        numberOfStudents = 0;
        courseName = name;
        this->capacity = capacity;
        students = new string[capacity];
    }
    Course(const Course& course) {   // deep copy
        courseName = course.courseName;
        numberOfStudents = course.numberOfStudents;
        capacity = course.capacity;
        students = new string[capacity];  // new array
        for (int i = 0; i < numberOfStudents; i++)
            students[i] = course.students[i];
    }
    void addStudent(const string& n) {
        students[numberOfStudents++] = n;
    }
    string* getStudents() const { return students; }
private:
    string courseName;
    string* students;
    int numberOfStudents;
    int capacity;
};

int main() {
    Course course3("C++", 10);
    Course course4(course3);   // deep: independent array
    course3.addStudent("Gunaeun");
    course4.addStudent("Seotaeyeong");
    cout << course3.getStudents()[0] << endl;  // Gunaeun
    cout << course4.getStudents()[0] << endl;  // Seotaeyeong
    return 0;
}
```

</CppRunner>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image11.png" class="tikz-fig" style="width: 100%; margin-top: 4rem;" />

<div style="margin-top: 1rem; text-align: center; color:#9aa0a6;">Each object now owns its own array of students.</div>

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
