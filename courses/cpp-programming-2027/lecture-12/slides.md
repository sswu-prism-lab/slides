---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 12
download: true
info: |
  ## C++ Programming Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-12-ko/
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
.uml-box {
  background: #ffffff;
  border: 1.5px solid #4a6fa5;
  border-radius: 4px;
  color: #1a1a1a;
  font-family: 'JetBrains Mono', Consolas, monospace;
  font-size: 0.8rem;
}
.uml-title {
  background: #bfe3f2;
  border-bottom: 1.5px solid #4a6fa5;
  text-align: center;
  font-weight: bold;
  padding: 0.25rem;
}
.uml-row {
  padding: 0.35rem 0.6rem;
}
.uml-sep {
  border-top: 1.5px solid #4a6fa5;
}
</style>

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.png" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">C++ Programming</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 12: Classes and Objects (continued)</p>

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
heading: "Summary: Objects and Classes"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- A [class]{.hl} defines the *properties* and *behavior* of an [object]{.hl}.

- In [object-oriented programming]{.hl}, programs are built out of objects.
  - An object represents a clearly *distinguishable* entity.
  - Each object has its own unique characteristics — its [state]{.hl} and its [behavior]{.hl}.

- The *state* (or [property / attribute]{.hl}) of an object is represented by its [data fields]{.hl}.
  - Example: a circle object has a `radius` data field describing its property.

- The *behavior* (or [action]{.hl}) of an object is defined by its [functions]{.hl}.

---
layout: prism
heading: "Summary: Classes"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Objects of the same kind are defined using a common [class]{.hl}.

- A class is a [template]{.hl} (or blueprint) that determines what data fields and functions an object will have; an object is an [instance]{.hl} of the class.
  - Creating an instance is called [instantiation]{.hl}.
  - From a single `Circle` class we can build countless `Circle` objects.

<div class="grid grid-cols-4 gap-3" style="margin-top: 1.5rem;">
<div class="uml-box">
  <div class="uml-title">Class Name: Circle</div>
  <div class="uml-row uml-sep">Data Fields:<br/>&nbsp;&nbsp;radius is ___</div>
  <div class="uml-row uml-sep">Functions:<br/>&nbsp;&nbsp;getArea</div>
</div>
<div class="uml-box" style="align-self: start;">
  <div class="uml-title">Circle Object 1</div>
  <div class="uml-row uml-sep">Data Fields:<br/>&nbsp;&nbsp;radius is <u>1.0</u></div>
</div>
<div class="uml-box" style="align-self: start;">
  <div class="uml-title">Circle Object 2</div>
  <div class="uml-row uml-sep">Data Fields:<br/>&nbsp;&nbsp;radius is <u>25</u></div>
</div>
<div class="uml-box" style="align-self: start;">
  <div class="uml-title">Circle Object 3</div>
  <div class="uml-row uml-sep">Data Fields:<br/>&nbsp;&nbsp;radius is <u>125</u></div>
</div>
</div>

---
layout: prism
heading: "Summary: Accessing Object Members"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- An object's data and functions are accessed through the object name and the [dot operator]{.hl} (`.`).

- From an object-oriented viewpoint, the [members]{.hl} of an object are its data fields and its functions.
  - A newly created object is allocated in memory; afterwards the [object member access operator]{.hl} (the dot operator) is used to read data and call functions.

```cpp
circle1.radius;      // reference a data field of the object
circle1.getArea();   // call a function on the object
```

- An accessed data field is called an [instance variable]{.hl}, and an accessed function is called an [instance function]{.hl}.

---
layout: prism
heading: "Object-Oriented Concepts"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Instead of splitting a program merely into *data* and *procedures*, object-oriented programming divides it into basic units called [objects]{.hl} and focuses on their *interactions*.
  - An object bundles together the *procedures* (methods, actions, functions) and the *data* (variables) that fulfil one role.
    - In C++ this is naturally expressed with a `class`.

- Functions structure how data is *processed*, but do not structure the *data* itself.
  - OOP reflects the real world, where every object is associated with both properties and behavior.

- In an OO program, the internal implementation of objects is hidden from the outside ([information hiding]{.hl}), raising *cohesion* inside a module and lowering *coupling* between modules — improving flexibility and maintainability.

---
layout: prism
heading: "The string Class (1/8)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- The `string` class defines the `string` type in C++ and is far easier to use than the alternative (C-strings).

| Function     | Description                                              |
| ------------ | -------------------------------------------------------- |
| `length()`   | Returns the number of characters in this string.         |
| `size()`     | Same as `length()`.                                      |
| `at(index)`  | Returns the character at the specified index.            |

- We *could* implement functions such as `length`, `size`, and `at` by hand ourselves.

- But in a [large programming project]{.hl} mixing many data types (`int`, `float`, `bool`), non-string variables would then gain [needless access to these functions]{.hl} — an inefficient way to program.

---
layout: prism
heading: "The string Class (2/8)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Defining string objects through the `string` class keeps the string-only behavior (functions) separate from other data, enabling efficient programming.

```cpp
// Using a string literal: creates a string object,
// then copies it into s (a two-step process).
string s1 = "Welcome to C++";

// A better way is to use the string constructor directly.
string s2("Welcome to C++");

// An empty string (using the no-argument constructor).
string s3;

// Build a string from a C-string.
char s4[] = "Welcome to C++";
string s5(s4);
```

---
layout: prism
heading: "The string Class (3/8)"
---

- The functions of the `string` class may be [overloaded]{.hl}, avoiding needless namespace expansion. Below: the `append` overloads.

| `append` overload                       | Description                                                        |
| --------------------------------------- | ----------------------------------------------------------------- |
| `append(s)`                             | Appends string `s` to this string object.                         |
| `append(s, index, n)`                   | Appends `n` characters from `s` starting at position `index`.     |
| `append(s, n)`                          | Appends the first `n` characters of `s` to this string.           |
| `append(n, ch)`                         | Appends `n` copies of character `ch` to this string.              |

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1("Welcome");
    s1.append(" to C++");
    cout << s1 << endl;  // Welcome to C++

    string s2("Welcome");
    s2.append(" to C and C++", 0, 5);
    cout << s2 << endl;  // Welcome to C

    string s3("Welcome");
    s3.append(" to C and C++", 5);
    cout << s3 << endl;  // Welcome to C

    string s4("Welcome");
    s4.append(4, 'G');
    cout << s4 << endl;  // WelcomeGGGG
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "The string Class (4/8)"
---

| `assign` overload            | Description                                                     |
| ---------------------------- | -------------------------------------------------------------- |
| `assign(s)`                  | Assigns a character array or string `s` to this string.        |
| `assign(s, index, n)`        | Assigns `n` characters of `s` starting at position `index`.    |
| `assign(s, n)`               | Assigns the first `n` characters of `s` to this string.        |
| `assign(n, ch)`              | Assigns `n` copies of character `ch` to this string.           |

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s5("Welcome");
    s5.assign("Dallas");
    cout << s5 << endl;  // Dallas

    string s6("Welcome");
    s6.assign("Dallas, Texas", 0, 5);
    cout << s6 << endl;  // Dalla

    string s7("Welcome");
    s7.assign("Dallas, Texas", 5);
    cout << s7 << endl;  // Dalla

    string s8("Welcome");
    s8.assign(4, 'G');
    cout << s8 << endl;  // GGGG
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "The string Class (5/8)"
---

| Function            | Description                                                     |
| ------------------- | -------------------------------------------------------------- |
| `at(index)`         | Returns the character at position `index`.                     |
| `clear()`           | Removes all characters in this string.                         |
| `erase(index, n)`   | Removes `n` characters starting at position `index`.           |
| `empty()`           | Returns `true` if this string is empty.                        |

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s9("Welcome");
    cout << s9.at(3) << " " << s9[3] << endl;  // c c
    cout << s9.erase(2, 3) << endl;            // s9 becomes Weme
    s9.clear();                                // s9 becomes empty
    cout << s9.empty() << endl;                // s9 is empty (true, 1)
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "The string Class (6/8)"
---

| Function                     | Description                                                          |
| ---------------------------- | ------------------------------------------------------------------- |
| `compare(s)`                 | Returns a value `> 0`, `0`, or `< 0` if this string is greater than, equal to, or less than `s`. |
| `compare(index, n, s)`       | Compares this string with the substring `s(index, ..., index+n-1)`. |
| `substr(index, n)`           | Returns a substring of `n` characters starting at `index`.          |
| `substr(index)`              | Returns the substring of this string starting at `index`.           |

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s10("Welcome");
    string s11("Welcomg");
    cout << s10.compare(s11) << endl;       // -2
    cout << s11.compare(s10) << endl;       // 2
    cout << s10.compare("Welcome") << endl; // 0

    cout << s10.substr(0, 1) << endl;       // W
    cout << s10.substr(3) << endl;          // come
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "The string Class (7/8)"
---

| Function                     | Description                                                          |
| ---------------------------- | ------------------------------------------------------------------- |
| `find(ch)` / `find(ch, index)` | Position of the first matching character `ch` (at/from `index`).  |
| `find(s)` / `find(s, index)` | Position of the first matching substring `s` (at/from `index`).     |
| `insert(index, s)`           | Inserts string `s` at position `index`.                             |
| `insert(index, n, ch)`       | Inserts character `ch` `n` times at position `index`.               |
| `replace(index, n, s)`       | Replaces `n` characters starting at `index` with string `s`.        |

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s12("Welcome to HTML");
    cout << s12.find("co") << endl;     // 3
    cout << s12.find("co", 6) << endl;  // no match -> npos (a huge value)
    cout << s12.find('o') << endl;      // 4
    cout << s12.find('o', 6) << endl;   // 9

    s12.insert(11, "C++ and ");
    cout << s12 << endl;  // Welcome to C++ and HTML
    s12.insert(1, 3, 'B');
    cout << s12 << endl;  // WBBBelcome to C++ and HTML
    s12.replace(1, 3, "***");
    cout << s12 << endl;  // W***elcome to C++ and HTML
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "The string Class (8/8)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

| Operator            | Description                                                              |
| ------------------- | ----------------------------------------------------------------------- |
| `[]`                | Accesses characters using the array subscript operator.                 |
| `=`                 | Copies the contents of one string to another.                           |
| `+`                 | Concatenates two strings into a new string.                             |
| `+=`                | Appends the contents of one string to another.                          |
| `<<`                | Inserts a string into a stream.                                         |
| `>>`                | Extracts characters from a stream into a string (delimited by whitespace). |
| `==` `!=` `<` `<=` `>` `>=` | The six relational operators for comparing strings.             |

- Strings can be combined using the assignment / concatenation operators.

- The comparison operators let us compare strings directly.

---
layout: prism
heading: "Lab: ExtractWords.cpp"
---

<div style="height: 0.3rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string text("Programming is fun");  // create a string object
    stringstream ss(text);              // create a stringstream object

    cout << "The words in the test are " << endl;
    string word;                        // create a string object
    while (!ss.eof()) {                 // ss.eof() is true when the stream ends
        ss >> word;                     // extract data from the stream
        cout << word << endl;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Lab: ReplaceString.cpp (1/2)"
---

<div style="height: 1rem;"></div>

```cpp
#include <iostream>
#include <string>
using namespace std;

// A function that replaces oldSubStr with newSubStr inside s.
bool replaceString(string& s, const string& oldSubStr, const string& newSubStr);

int main() {
    // Read s, oldSubStr, and newSubStr.
    cout << "Enter string s, oldSubstr, and newSubstr: ";
    string s, oldSubStr, newSubStr;
    cin >> s >> oldSubStr >> newSubStr;

    bool isReplaced = replaceString(s, oldSubStr, newSubStr);

    if (isReplaced)
        cout << "The replaced string is " << s << endl;
    else
        cout << "No matches" << endl;

    return 0;
}
```

---
layout: prism
heading: "Lab: ReplaceString.cpp (2/2)"
---

<CppRunner stdin="abcabcabc abc X">

```cpp
#include <iostream>
#include <string>
using namespace std;

bool replaceString(string& s, const string& oldSubStr, const string& newSubStr);

int main() {
    cout << "Enter string s, oldSubstr, and newSubstr: ";
    string s, oldSubStr, newSubStr;
    cin >> s >> oldSubStr >> newSubStr;

    bool isReplaced = replaceString(s, oldSubStr, newSubStr);
    if (isReplaced)
        cout << "The replaced string is " << s << endl;
    else
        cout << "No matches" << endl;
    return 0;
}

// Function implementation
bool replaceString(
        string& s, const string& oldSubStr, const string& newSubStr) {
    bool isReplaced = false;
    int currentPosition = 0;
    while (currentPosition < (int)s.length()) {
        int position = s.find(oldSubStr, currentPosition);
        if (position == (int)string::npos)  // no more matches
            return isReplaced;
        else {
            s.replace(position, oldSubStr.length(), newSubStr);
            currentPosition = position + newSubStr.length();
            isReplaced = true;
        }
    }
    return isReplaced;
}
```

</CppRunner>

---
layout: prism
heading: "Passing Objects to Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.0em;
}
</style>

- An object can be passed to a function [by value]{.hl} or [by reference]{.hl}, but passing [by reference is more efficient]{.hl}.

- When passing *by value*, the function creates a new object and works on a *copy* of the object that was passed.

- When passing [by reference]{.hl}, the function works directly on the passed object itself — the parameter is an *alias* for it.

- Pass-by-value needs extra time and memory, so [pass-by-reference is more efficient]{.hl}.

---
layout: prism
heading: "Lab: PassObject.cpp"
---

<div style="height: 0.3rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// (merged from CircleWithPrivateDataFields.h)
class Circle {
public:
    Circle(double newRadius = 1.0) { radius = newRadius; }
    double getArea() const { return radius * radius * 3.14159; }
    double getRadius() const { return radius; }
private:
    double radius;
};

void printCirclePassByValue(Circle c) {
    cout << "The area of the circle of " << c.getRadius()
         << " is " << c.getArea() << endl;
}

void printCirclePassByReference(Circle& c) {
    cout << "The area of the circle of " << c.getRadius()
         << " is " << c.getArea() << endl;
}

int main() {
    Circle myCircle(5.0);
    printCirclePassByValue(myCircle);
    printCirclePassByReference(myCircle);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Arrays of Objects"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Just like arrays of primitive values or strings, we can create an [array of objects]{.hl}.

- The array may be declared with the no-argument constructor, or [declared and initialized]{.hl} at once using a constructor with arguments.

- Each element of an object array is accessed with `arrayName[i]`, exactly like an ordinary array.

```cpp
Circle circleArray[10]; // declare an array of 10 Circle objects
// The no-arg constructor sets radius to 1, so each getRadius() returns 1.

// An array can also be declared and initialized with an argument constructor.
Circle circleArray[3] = {Circle(3), Circle(5), Circle(7)};
cout << circleArray[0].getRadius() << endl; // 3
```

---
layout: prism
heading: "Instance and Static Members (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A data field used inside a class is called an [instance data field]{.hl} (or [instance variable]{.hl}).

- Instance variables are *not* shared among objects.

```cpp
Circle circle1;
Circle circle2(5); // the radius of circle1 and circle2 are independent
```

- To let *all* instances of a class share data, we use a [static variable]{.hl}.
  - A static variable is also called a [class variable]{.hl}.

---
layout: prism
heading: "Instance and Static Members (2/2)"
---

- A static variable stores its value in a *shared* memory location; when one object changes it, all objects of the same class are affected.
  - In UML notation, static variables and functions are *underlined*.

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<div class="uml-box">
  <div class="uml-title">Circle</div>
  <div class="uml-row uml-sep">-radius: double<br/><u>-numberOfObjects: int</u></div>
  <div class="uml-row uml-sep"><u>+getNumberOfObjects(): int</u><br/>+getRadius(): double<br/>+setArea(radius: double): void<br/>+getArea(): double</div>
</div>

<div style="font-size: 0.72rem; color: #6b7280; margin-top: 0.6rem; font-family: monospace;">
+ : public &nbsp; − : private &nbsp; <u>underline</u> : static
</div>

</div>
<div>

<div class="uml-box" style="margin-bottom: 1rem;">
  <div class="uml-title">circle1: Circle</div>
  <div class="uml-row uml-sep">radius = 1<br/><u>numberOfObjects = 2</u></div>
</div>
<div class="uml-box">
  <div class="uml-title">circle2: Circle</div>
  <div class="uml-row uml-sep">radius = 5<br/><u>numberOfObjects = 2</u></div>
</div>

<div style="font-size: 0.75rem; color: #6b7280; margin-top: 0.6rem;">
Both objects share the single <code>numberOfObjects</code> in memory (value 2), while each keeps its own <code>radius</code>.
</div>

</div>
</div>

- Static variables and functions use the `static` keyword: `static int numberOfObjects;` &nbsp;/&nbsp; `static int getNumberOfObjects();`

---
layout: prism
heading: "Lab: CircleWithStaticDataFields.h"
---

<div style="height: 1rem;"></div>

```cpp
#ifndef CIRCLE_H
#define CIRCLE_H

class Circle {
public:
    Circle();
    Circle(double);
    double getArea();
    double getRadius();
    void setRadius(double);
    static int getNumberOfObjects();  // static function

private:
    double radius;
    static int numberOfObjects;       // static variable
};

#endif
```

---
layout: prism
heading: "Lab: CircleWithStaticDataFields.cpp"
---

```cpp
#include "CircleWithStaticDataFields.h"

int Circle::numberOfObjects = 0;  // initialize the static variable

Circle::Circle() {                // construct a circle object
    radius = 1;
    numberOfObjects++;
}
Circle::Circle(double newRadius) { // constructor with an argument
    radius = newRadius;
    numberOfObjects++;
}
double Circle::getArea() {        // return the area of the circle
    return radius * radius * 3.14159;
}
double Circle::getRadius() {      // return the radius of the circle
    return radius;
}
void Circle::setRadius(double newRadius) {  // set a new radius
    radius = (newRadius >= 0) ? newRadius : 0;
}
int Circle::getNumberOfObjects() {  // return the number of circle objects
    return numberOfObjects;
}
```

---
layout: prism
heading: "Lab: TestCircleWithStaticDataFields.cpp"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// merged: CircleWithStaticDataFields.h + .cpp
class Circle {
public:
    Circle();
    Circle(double);
    double getArea();
    double getRadius();
    void setRadius(double);
    static int getNumberOfObjects();
private:
    double radius;
    static int numberOfObjects;
};

int Circle::numberOfObjects = 0;
Circle::Circle() { radius = 1; numberOfObjects++; }
Circle::Circle(double newRadius) { radius = newRadius; numberOfObjects++; }
double Circle::getArea() { return radius * radius * 3.14159; }
double Circle::getRadius() { return radius; }
void Circle::setRadius(double newRadius) { radius = (newRadius >= 0) ? newRadius : 0; }
int Circle::getNumberOfObjects() { return numberOfObjects; }

void printCircle(Circle& c) {
    cout << "The area of the circle of radius " << c.getRadius() << " is "
         << c.getArea() << endl;
    cout << "The numbers of circle objects created: "
         << Circle::getNumberOfObjects() << endl;
}

int main() {
    cout << "The number of circle objects created: "
         << Circle::getNumberOfObjects() << endl;  // accessible without any object

    Circle circleArray[2] = {Circle(), Circle(5.0)};  // create 2 objects

    printCircle(circleArray[0]);
    printCircle(circleArray[1]);

    circleArray[0].setRadius(3.3);  // does NOT create a new object
    printCircle(circleArray[0]);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Constant Member Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- In C++ we can mark a function as a [constant member function]{.hl}, telling the compiler that the function will *not* change any data field of the object.

- To signal that a function will not modify the object's data fields, we declare it a constant member function (a *constant function* for short) using the [`const`]{.hl} keyword.

- Only [instance member functions]{.hl} may be defined as constant functions; like constant parameters, constant functions support [defensive programming]{.hl}.
  - Static functions cannot be constant — only instance functions can.

---
layout: prism
heading: "Object Composition (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- An object can *contain* another object; this relationship is called [composition]{.hl}.
  - Example: a `Circle` class could include a `string` data field.

- Composition is a special case of the [aggregation]{.hl} relationship.
  - Aggregation models a [has-a]{.hl} relationship — an *ownership* relationship between two objects.
  - The [owner object]{.hl} is the *aggregating* object, and its class is the *aggregating* class.
  - The owned ([subject]{.hl}) object is the *aggregated* object, and its class is the *aggregated* class.

- An object may be owned by several aggregating objects; if it is owned *exclusively* by one aggregating object, that relationship is [composition]{.hl}.

---
layout: prism
heading: "Object Composition (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- A `Student` [has a]{.hl} `Name`.
  - A student has only one name, so `Student`–`Name` is a [composition]{.hl}.

- A `Student` [has an]{.hl} `Address`.
  - An address can be *shared* by several students (e.g. roommates), so `Student`–`Address` is an [aggregation]{.hl}.
    - The range `m..n` means the number of objects must lie between `m` and `n` (here, at most 3 students share one address).
    - `*` means an unlimited number of objects is possible.

<div class="flex items-center justify-center gap-2" style="margin-top: 1rem; font-family: monospace; font-size: 0.85rem;">
  <span class="uml-box uml-title" style="padding: 0.3rem 0.8rem;">Name</span>
  <span>&#9670;&mdash; 1 &mdash;</span>
  <span class="uml-box uml-title" style="padding: 0.3rem 0.8rem;">Student</span>
  <span>&#9671;&mdash; 1..3 &mdash;</span>
  <span class="uml-box uml-title" style="padding: 0.3rem 0.8rem;">Address</span>
</div>

<div style="text-align:center; font-size: 0.75rem; color:#6b7280; margin-top:0.4rem;">&#9670; = Composition &nbsp;&nbsp; &#9671; = Aggregation &nbsp;&nbsp; (<code>Student</code> holds <code>Name name;</code> and <code>Address address;</code>)</div>

---
layout: prism
heading: "Object Composition (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Aggregation can also occur between objects of the [same class]{.hl}.

- A `Person` class may contain a `supervisor` that is itself a `Person`.

- An array of a class can likewise be composed.

</div>
<div>

```cpp
class Person {
private:
    Person supervisor;
    ...
};
```

<div style="height: 1rem;"></div>

```cpp
class Person {
    ...
private:
    Person supervisors[10];
};
```

</div>
</div>

---
layout: prism
heading: "Class Design Guidelines"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [Cohesion]{.hl}
  - A class should be designed around a *single* entity.

- [Consistency]{.hl}
  - Follow standard programming style and naming conventions; use meaningful names.

- [Encapsulation]{.hl}
  - Hide data from direct access by clients.

- [Clarity]{.hl}
  - Follow clear rules that are easy to explain and understand.

- [Completeness]{.hl}
  - Design for a wide range of users and situations.

---
layout: prism
heading: "OOP Principles (SOLID)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [Single Responsibility Principle (SRP)]{.hl}
  - An object should have only one responsibility.

- [Open-Closed Principle (OCP)]{.hl}
  - An object should be open for extension but closed for modification.

- [Liskov Substitution Principle (LSP)]{.hl}
  - A subclass should always be substitutable for its parent class.

- [Interface Segregation Principle (ISP)]{.hl}
  - A client should not depend on methods it does not use.

- [Dependency Inversion Principle (DIP)]{.hl}
  - High-level, abstract, stable classes should not depend on low-level, concrete, unstable ones.

---
layout: prism
heading: "DIY_W12"
---

- Based on the UML diagram below, *define*, *implement*, and *test* `StackOfIntegers`.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<div class="uml-box">
  <div class="uml-title">StackOfIntegers</div>
  <div class="uml-row uml-sep">-elements[100]: int<br/>-size: int</div>
  <div class="uml-row uml-sep">+StackOfIntegers()<br/>+isEmpty(): bool const<br/>+peek(): int const<br/>+push(value: int): void<br/>+pop(): int<br/>+getSize(): int const</div>
</div>

</div>
<div style="font-size: 0.8rem; color:#374151;">

- `elements[100]` — array storing the integers.
- `size` — number of integers in the stack.
- `StackOfIntegers()` — constructs an empty stack.
- `isEmpty()` — `true` if the stack is empty.
- `peek()` — top integer, without removing it.
- `push(value)` — stores an integer on top.
- `pop()` — removes and returns the top integer.
- `getSize()` — number of elements.

</div>
</div>

<div style="height: 0.6rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class StackOfIntegers {
public:
    StackOfIntegers();
    bool isEmpty() const;
    int peek() const;
    void push(int value);
    int pop();
    int getSize() const;
private:
    int elements[100];
    int size;
};

StackOfIntegers::StackOfIntegers() : size{0} {}
bool StackOfIntegers::isEmpty() const { return size == 0; }
int StackOfIntegers::peek() const { return elements[size - 1]; }
void StackOfIntegers::push(int value) { elements[size++] = value; }
int StackOfIntegers::pop() { return elements[--size]; }
int StackOfIntegers::getSize() const { return size; }

int main() {
    StackOfIntegers stack;
    cout << "Is the stack empty? " << (stack.isEmpty() ? "yes" : "no") << endl;
    for (int i = 1; i <= 5; i++) stack.push(i * 10);
    cout << "Size after pushing 5 values: " << stack.getSize() << endl;
    cout << "Top element (peek): " << stack.peek() << endl;
    cout << "Popping all: ";
    while (!stack.isEmpty()) cout << stack.pop() << " ";
    cout << endl;
    cout << "Is the stack empty now? " << (stack.isEmpty() ? "yes" : "no") << endl;
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
