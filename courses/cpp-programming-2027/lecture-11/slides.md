---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 11
download: true
info: |
  ## C++ Programming Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-11-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 11: Objects and Classes</p>

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
heading: "Recap: Arrays"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- An [array]{.hl} can store a collection of many data items. In C++ an array is a [data structure]{.hl} in which elements of the same type (e.g. `int`) are stored in a fixed-size, contiguous block of memory.

- Each [element]{.hl} of an array is accessed by its [index]{.hl}. Instead of declaring 100 separate variables `num0, num1, ..., num99`, we declare one array `nums` of 100 elements and access them as `nums[0], nums[1], ..., nums[99]`.

- An array declaration specifies the element type, an identifier, and a size: `elementType arrayName[SIZE];`, where `SIZE` is a `const`. Once declared, the array is filled with arbitrary values until initialized.

---
layout: prism
heading: Objects and Classes
---

<style>
.slidev-layout ul > li {
  margin-top: 1.7em;
}
</style>

- A [class]{.hl} defines the *attributes* and *behavior* of an [object]{.hl}.

- In [object-oriented programming]{.hl}, we build programs out of objects. An object represents a clearly distinguishable entity, with its own unique identity, [state]{.hl}, and [behavior]{.hl}.

- The state (or [property / attribute]{.hl}) of an object is represented by its [data fields]{.hl}.
  - Example: a circle object has a `radius` data field describing the circle's characteristics.

- The behavior (or [action]{.hl}) of an object is defined by its functions.

---
layout: prism
heading: "Classes (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Objects of the same type are defined using a common [class]{.hl}.

- A class is a [template]{.hl} (or blueprint) that determines what data fields and functions the objects will have; an object is an [instance]{.hl} of the class.
  - Creating an instance is called [instantiation]{.hl}.
  - With a single `Circle` class, we can create countless objects from it.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Classes (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A C++ class uses variables to define its [data fields]{.hl} and functions to define its behavior.

- A class provides a special kind of function called a [constructor]{.hl}.
  - A constructor is called when a new object is created. It can perform any action, but is generally designed to *initialize* the object's data fields.

- A class can be described using [UML]{.hl} (unified modeling language) notation.

</div>
<div>

<div style="height: 4rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image3.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "The Circle Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

```cpp
#include <iostream>
using namespace std;

class Circle {
public: // accessible from
        // objects of the class
    // radius of the circle
    double radius;
    // construct a circle object
    Circle() {
        radius = 1;
    }
    Circle(double newRadius) {
        radius = newRadius;
    }
    // return the area of the circle
    double getArea() {
        return radius * radius * 3.14159;
    }
}; // note the semicolon!
```

</div>
<div>

<div style="height: 3rem;"></div>

<div class="sub-item">

- `radius` is a [data field]{.hl}.

</div>

<div class="sub-item">

- `Circle()` and `Circle(double)` are overloaded [constructors]{.hl}.

</div>

<div class="sub-item">

- `getArea()` is a [function]{.hl} (behavior).

</div>

<div class="sub-item">

- Do not forget the trailing `;` after the closing brace of the class.

</div>

</div>
</div>

---
layout: prism
heading: "Lab: TestCircle.cpp"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Circle {
public:
    double radius;                          // data field
    Circle() { radius = 1; }                // no-argument constructor
    Circle(double newRadius) { radius = newRadius; }
    double getArea() { return radius * radius * 3.14159; }
};

int main() {
    Circle circle1;      // constructed with no argument
    Circle circle2(25);
    Circle circle3(125);
    cout << "The area of the circle of radius "
         << circle1.radius << " is " << circle1.getArea() << endl;
    cout << "The area of the circle of radius "
         << circle2.radius << " is " << circle2.getArea() << endl;
    cout << "The area of the circle of radius "
         << circle3.radius << " is " << circle3.getArea() << endl;
    circle1.radius = 100; // change the radius of the circle
    cout << "The area of the circle of radius "
         << circle1.radius << " is " << circle1.getArea() << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Constructors
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [constructor]{.hl} is a special function called to create an object:
  - it has the *same name* as the class;
  - it has *no return type* (not even `void`);
  - it is called when the object is created, initializing it.

- Constructors can be [overloaded]{.hl} like ordinary functions.

- Constructors initialize data fields — class members cannot be initialized at declaration. A class defined without a constructor gets one implicitly. A constructor may use an [initialization list]{.hl}.

</div>
<div>

<div style="height: 4rem;"></div>

```cpp
// assign inside the body
Circle() {
    radius = 1;
}
```

<div style="height: 1rem;"></div>

```cpp
// equivalent initialization list
Circle() : radius(1) {}
```

</div>
</div>

---
layout: prism
heading: "Constructing and Using Objects (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- An object's data and functions are accessed with the object name and the [dot operator]{.hl} (`.`).

- In OOP, the [members]{.hl} of an object are its data fields and functions. A newly created object is allocated in memory; after construction, the [object member access operator]{.hl} (the dot) accesses its data and calls its functions.

- An accessed data field is an [instance variable]{.hl}, and an invoked function is an [instance function]{.hl}.

```cpp
circle1.radius;    // refer to a data field of the object
circle1.getArea(); // call a function on the object
```

---
layout: prism
heading: "★ Coding Style"
---

<div class="grid grid-cols-3 gap-3" style="margin-top: 1.5rem;">
<div>

K&R style (Java / C++):

```cpp
if (...) {
    // body;
}
```

</div>
<div>

GNU style:

```cpp
if (...)
  {
    // body;
  }
```

</div>
<div>

BSD / VS default:

```cpp
if (...)
{
    // body;
}
```

</div>
</div>

<div style="margin-top: 1.5rem;"></div>

- Naming conventions used in C++:

<div class="sub-item">

- `camelCase` — variables and functions &nbsp;·&nbsp; `PascalCase` — user-defined class names
- `snake_case` and `SCREAMING_SNAKE_CASE` — alternative styles (e.g. constants)

</div>

---
layout: prism
heading: "Constructing and Using Objects (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- A class is itself a *data type*. In C++, assignment can copy the contents of one object into another.

- Once an object name is declared, it cannot be reassigned to name a different object. Only data is physically stored per object — functions are shared by all objects, so objects stay small.

- For one-time use, an unnamed [anonymous object]{.hl} can be created. Even with a no-argument constructor, parentheses are required.

</div>
<div>

```cpp
/* copy circle1's radius into
   circle2; afterwards they are
   still distinct objects, only
   the radius matches */
circle2 = circle1;
```

<div style="height: 0.8rem;"></div>

```cpp
cout << "Area is "
     << Circle(2.3).getArea() << endl;
```

<div style="height: 0.8rem;"></div>

```cpp
Circle myCircle; // named, no-arg object
Circle();        // anonymous object
```

</div>
</div>

---
layout: prism
heading: "Separating Declaration and Implementation (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.7em;
}
</style>

- In C++, separating a class [definition]{.hl} from its [implementation]{.hl} makes the class easier to maintain.

- The class *definition* describes the contract: it lists all data fields together with the constructor and function prototypes.

- The class *implementation* fulfills that contract: it provides the bodies of the constructors and functions.

- The two are stored in separate files with the same name but different extensions: the definition in a `.h` file and the implementation in a `.cpp` file.

---
layout: prism
heading: "Separating Declaration and Implementation (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

`Circle.h` — definition:

```cpp
class Circle {
public:
    // radius of the circle
    double radius;
    // default constructor
    Circle();
    // constructor with radius
    Circle(double);
    // return the area
    double getArea();
};
```

</div>
<div>

`Circle.cpp` — implementation:

```cpp
#include "Circle.h"

Circle::Circle() {
    radius = 1;
}
Circle::Circle(double newRadius) {
    radius = newRadius;
}
double Circle::getArea() {
    return radius * radius * 3.14159;
}
```

</div>
</div>

---
layout: prism
heading: "Separating Declaration and Implementation (3/3)"
---

For the lab, the `Circle.h`, `Circle.cpp`, and the test `main` are merged into one compilable file.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// ---- Circle.h : class definition ----
class Circle {
public:
    double radius;
    Circle();
    Circle(double);
    double getArea();
};

// ---- Circle.cpp : class implementation ----
Circle::Circle() { radius = 1; }
Circle::Circle(double newRadius) { radius = newRadius; }
double Circle::getArea() { return radius * radius * 3.14159; }

// ---- main ----
int main() {
    Circle circle1;
    Circle circle2(5.0);
    cout << "The area of the circle of radius "
         << circle1.radius << " is " << circle1.getArea() << endl;
    cout << "The area of the circle of radius "
         << circle2.radius << " is " << circle2.getArea() << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Preventing Multiple Inclusion
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- To keep a header file from being included more than once, use an [inclusion guard]{.hl}.

- Calling the same header twice or more causes a *multiple inclusion* error.

- The `#ifndef`, `#define`, and `#endif` directives prevent multiple inclusion.
  - Example: if `TestHead.cpp` includes both `Circle.h` and `Head.h`, and `Head.h` also includes `Circle.h`, then `Circle.h` is included twice — an error without a guard.

</div>
<div>

<div style="height: 3.5rem;"></div>

```cpp
#ifndef ClassName_H
#define ClassName_H

// class declaration

#endif
```

</div>
</div>

---
layout: prism
heading: "Inline Functions in Classes (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- For better performance, short functions can be defined as [inline functions]{.hl}.

- When a function is implemented *inside* the class definition, it automatically becomes an inline function — this is an [inline definition]{.hl}.

- Even if a function is only declared inside the class (prototype only), using the `inline` keyword at its later definition makes it an inline function.

- Making *short* functions inline (rather than long ones) is what improves performance.

---
layout: prism
heading: "Inline Functions in Classes (2/2)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class A {
public:
    A() { value = 10; }
    // defined inside the class -> automatically an inline function
    double f1() { return value + 1; }
    double f2();        // ordinary member function
    double f3();        // note the inline keyword on the definition below
private:
    double value;
};

double A::f2() { return value + 2; }
inline double A::f3() { return value + 3; } // f3 is an inline function

int main() {
    A a;
    cout << "f1() = " << a.f1() << endl; // inline definition
    cout << "f2() = " << a.f2() << endl; // ordinary function
    cout << "f3() = " << a.f3() << endl; // inline via keyword
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Data Field Encapsulation (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Making data fields private protects the data and makes the class easier to maintain.

- In the earlier `Circle` class, the `radius` data field can be modified directly: `circle1.radius = 100;`

- Allowing direct modification of an attribute is *not* good programming practice:
  - data can be changed arbitrarily;
  - the class becomes harder to maintain and more bug-prone;
  - modifying `Circle` may force every program that uses it to change at once.

---
layout: prism
heading: "Data Field Encapsulation (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- To prevent direct modification, we declare data fields [private]{.hl} with the `private` keyword — this is [data field encapsulation]{.hl}.

- To reach a private data field, use a [get]{.hl} function to read it and a [set]{.hl} function to change it.

</div>
<div>

<div style="height: 2.5rem;"></div>

```cpp
class Circle {
public:
    Circle();
    Circle(double);
    double getArea();

private:
    double radius; // make radius private
};
```

</div>
</div>

---
layout: prism
heading: "Data Field Encapsulation (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Informally, a get function (which reads the variable) is an [accessor]{.hl}, and a set function (which modifies it) is a [mutator]{.hl}.

- A get function uses the form:

<div class="sub-item">

`returnType getPropertyName()` &nbsp;or&nbsp; `bool isPropertyName()`

</div>

- A set function uses the form:

<div class="sub-item">

`void setPropertyName(dataType propertyValue)`

</div>

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image5.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Lab: CircleWithPrivateDataField"
---

The header, implementation, and test `main` are merged into one runnable file.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// ---- CircleWithPrivateDataFields.h ----
class Circle {
public:
    Circle();
    Circle(double);
    double getRadius();     // accessor
    void setRadius(double); // mutator
    double getArea();
private:
    double radius;          // private data field
};

// ---- CircleWithPrivateDataFields.cpp ----
Circle::Circle() { radius = 1; }
Circle::Circle(double newRadius) { radius = newRadius; }
double Circle::getRadius() { return radius; }
void Circle::setRadius(double newRadius) { radius = (newRadius >= 0) ? newRadius : 0; }
double Circle::getArea() { return radius * radius * 3.14159; }

// ---- TestCircleWithPrivateDataFields.cpp ----
int main() {
    Circle circle1;
    Circle circle2(5.0);
    cout << "The area of the circle of radius "
         << circle1.getRadius() << " is " << circle1.getArea() << endl;
    cout << "The area of the circle of radius "
         << circle2.getRadius() << " is " << circle2.getArea() << endl;
    circle2.setRadius(100); // circle2.radius = 100; would be a compile error!
    cout << "The area of the circle of radius "
         << circle2.getRadius() << " is " << circle2.getArea() << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Variable Scope (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The scope of instance and static variables is the *entire class*, regardless of where they are declared.

- Data fields are variables accessible to every constructor and function within the class, and members can be written in any order.

- The three classes on the right are all equivalent, but C++ programmers usually write it like the first one.

</div>
<div>

```cpp
class Circle {
public:
    Circle();
    Circle(double);
    double getRadius();
    void setRadius();
    double getArea();
private:
    double radius;
};
```

</div>
</div>

---
layout: prism
heading: "Lab: HideDataField.cpp"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Foo {
public:
    int x, y; // data fields
    Foo() {
        x = 10;
        y = 10;
    }
    void p() {
        int x = 20; // local variable hides the data field x
        cout << "x is " << x << endl; // prints the local x (20)
        cout << "y is " << y << endl; // prints the data field y (10)
    }
};

int main() {
    Foo foo;
    foo.p();
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Variable Scope (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- A data-field variable can be declared only once, but a name used for a variable inside one function may be reused for a variable in another function.

- A [local variable]{.hl} is declared inside a function and used locally within it.

- If a local variable has the same name as a data field, the [local variable takes precedence]{.hl} and the same-named data field is hidden.
  - To avoid this confusion, it is good practice not to declare a variable with the same name as a data field inside the class, except when it is used as a function parameter.

---
layout: prism
heading: "Class Abstraction and Encapsulation (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [Class abstraction]{.hl} separates a class's implementation from its use.

- The class author can supply documentation telling users how to use the class.

- Together with descriptions of how functions and data fields behave, the set of externally accessible functions and data fields is provided as the [class contract]{.hl}.

</div>
<div>

<div style="height: 4rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image7.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Class Abstraction and Encapsulation (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Hiding the implementation details from the user is called [class encapsulation]{.hl}.
  - We can create a `Circle` object and compute its area without knowing *how* the area is calculated.

- A computer system is made of many parts — CPU, motherboard, fan, and so on.

- For those parts to work together, we only need to know how each part is used and how they interact — not how each part works internally.

- Each part can be thought of as an object of a class for that part.

---
layout: prism
heading: "Class Abstraction and Encapsulation (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Given a UML diagram, we can write a test program based on the contract without knowing how the class is implemented internally.

- That is, implementing a class and using a class are two separate tasks.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image8.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Lab: TestLoanClass.cpp"
---

The `Loan` class implements the contract from the UML diagram; `main` reads input and reports the payments.

<CppRunner stdin="2.5 5 1000">

```cpp
#include <iostream>
#include <cmath>
using namespace std;

class Loan {
public:
    Loan() : annualInterestRate(2.5), numberOfYears(1), loanAmount(1000) {}
    Loan(double rate, int years, double amount)
        : annualInterestRate(rate), numberOfYears(years), loanAmount(amount) {}
    double getAnnualInterestRate() { return annualInterestRate; }
    int getNumberOfYears() { return numberOfYears; }
    double getLoanAmount() { return loanAmount; }
    void setAnnualInterestRate(double rate) { annualInterestRate = rate; }
    void setNumberOfYears(int years) { numberOfYears = years; }
    void setLoanAmount(double amount) { loanAmount = amount; }
    double getMonthlyPayment() {
        double monthlyInterestRate = annualInterestRate / 1200;
        return loanAmount * monthlyInterestRate /
               (1 - 1 / pow(1 + monthlyInterestRate, numberOfYears * 12));
    }
    double getTotalPayment() { return getMonthlyPayment() * numberOfYears * 12; }
private:
    double annualInterestRate; // default 2.5
    int numberOfYears;         // default 1
    double loanAmount;         // default 1000
};

int main() {
    cout << "Enter yearly interest rate: ";
    double annualInterestRate;
    cin >> annualInterestRate;
    cout << "Enter number of years: ";
    int numberOfYears;
    cin >> numberOfYears;
    cout << "Enter loan amount: ";
    double loanAmount;
    cin >> loanAmount;
    Loan loan(annualInterestRate, numberOfYears, loanAmount);
    cout << "The monthly payment is " << loan.getMonthlyPayment() << endl;
    cout << "The total payment is " << loan.getTotalPayment() << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY_W11: Build a TV Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Using the UML diagram, build a `TV` class.
  - `channel` (1 to 120), `volumeLevel` (1 to 7), and `on` (whether the TV is on).
  - Constructor plus `turnOn`, `turnOff`, `setChannel`, `setVolume`, `channelUp`, `channelDown`, `volumeUp`, `volumeDown`.

- Guard each operation so it only takes effect when the TV is on and stays within range.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image9.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY_W11: TV Class — A Solution"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class TV {
public:
    int channel;     // current channel (1 to 120)
    int volumeLevel; // current volume level (1 to 7)
    bool on;         // whether this TV is on/off

    TV() { channel = 1; volumeLevel = 1; on = false; } // default TV object
    void turnOn()  { on = true; }
    void turnOff() { on = false; }
    void setChannel(int newChannel) {
        if (on && newChannel >= 1 && newChannel <= 120) channel = newChannel;
    }
    void setVolume(int newVolumeLevel) {
        if (on && newVolumeLevel >= 1 && newVolumeLevel <= 7) volumeLevel = newVolumeLevel;
    }
    void channelUp()   { if (on && channel < 120) channel++; }
    void channelDown() { if (on && channel > 1) channel--; }
    void volumeUp()    { if (on && volumeLevel < 7) volumeLevel++; }
    void volumeDown()  { if (on && volumeLevel > 1) volumeLevel--; }
};

int main() {
    TV tv;
    tv.turnOn();
    tv.setChannel(30);
    tv.setVolume(3);
    tv.channelUp();
    tv.volumeDown();
    cout << "Channel: " << tv.channel
         << ", Volume: " << tv.volumeLevel << endl;
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
