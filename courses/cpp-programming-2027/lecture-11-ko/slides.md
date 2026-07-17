---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 11 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-11/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">C++ 프로그래밍</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">11주차: 객체와 클래스</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">2027년 가을학기</p>
</div>

---
layout: prism
heading: "복습: 배열"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [배열]{.hl}은 많은 데이터의 모음을 저장할 수 있습니다. C++에서 배열은 같은 유형(예: `int`)의 요소가 고정된 크기의 연속된 메모리 공간에 저장되는 [자료구조]{.hl}입니다.

- 배열의 각 [요소]{.hl}는 [인덱스]{.hl}를 사용하여 접근합니다. `num0, num1, ..., num99`와 같이 100개의 변수를 따로 선언하는 대신, 100개의 요소를 가지는 하나의 배열 `nums`를 선언하고 `nums[0], nums[1], ..., nums[99]`와 같이 접근합니다.

- 배열의 선언은 요소 유형, 식별자, 크기를 지정합니다: `elementType arrayName[SIZE];`, 여기서 `SIZE`는 `const`입니다. 배열이 선언되면 초기화되기 전까지 임의의 값으로 채워져 있습니다.

---
layout: prism
heading: 객체와 클래스
---

<style>
.slidev-layout ul > li {
  margin-top: 1.7em;
}
</style>

- [클래스]{.hl}는 [객체]{.hl}의 *속성*과 *행동*을 정의합니다.

- [객체지향 프로그래밍]{.hl}에서는 프로그램을 객체로 구성합니다. 객체는 명확히 구별되는 개체를 의미하며, 자신만의 유일한 특성과 [상태]{.hl}, [행동]{.hl}을 가집니다.

- 객체의 상태(또는 [속성 / 특성]{.hl})은 [데이터 필드]{.hl}로 표현됩니다.
  - 예: 원 객체는 원의 특성을 나타내는 `radius` 데이터 필드를 가집니다.

- 객체의 행동(또는 [동작]{.hl})은 함수에 의해 정의됩니다.

---
layout: prism
heading: "클래스 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 같은 유형의 객체는 공통의 [클래스]{.hl}를 사용하여 정의됩니다.

- 클래스는 객체가 어떤 데이터 필드와 함수를 가질지 결정하는 [템플릿]{.hl}(또는 설계도)이며, 객체는 클래스의 [인스턴스]{.hl}입니다.
  - 인스턴스를 생성하는 것을 [실체화]{.hl}라고 합니다.
  - `Circle` 클래스 하나만 있으면, 이로부터 무수히 많은 객체를 생성할 수 있습니다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "클래스 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- C++ 클래스는 변수를 사용하여 [데이터 필드]{.hl}를 정의하고, 함수를 사용하여 행동을 정의합니다.

- 클래스는 [생성자]{.hl}라고 하는 특별한 유형의 함수를 제공합니다.
  - 생성자는 새로운 객체가 생성될 때 호출됩니다. 어떤 동작이든 수행할 수 있지만, 일반적으로 객체의 데이터 필드를 *초기화*하도록 설계됩니다.

- 클래스는 [UML]{.hl}(unified modeling language) 표기법을 사용하여 표현할 수 있습니다.

</div>
<div>

<div style="height: 4rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image3.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Circle 클래스"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

```cpp
#include <iostream>
using namespace std;

class Circle {
public: // 클래스의 객체로부터
        // 접근 가능
    // circle의 반지름
    double radius;
    // circle 객체 생성
    Circle() {
        radius = 1;
    }
    Circle(double newRadius) {
        radius = newRadius;
    }
    // circle의 면적 반환
    double getArea() {
        return radius * radius * 3.14159;
    }
}; // semicolon 확인!
```

</div>
<div>

<div style="height: 3rem;"></div>

<div class="sub-item">

- `radius`는 [데이터 필드]{.hl}입니다.

</div>

<div class="sub-item">

- `Circle()`과 `Circle(double)`은 오버로딩된 [생성자]{.hl}입니다.

</div>

<div class="sub-item">

- `getArea()`는 [함수]{.hl}(행동)입니다.

</div>

<div class="sub-item">

- 클래스의 닫는 중괄호 뒤에 오는 `;`를 잊지 마세요.

</div>

</div>
</div>

---
layout: prism
heading: "실습: TestCircle.cpp"
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
heading: 생성자
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [생성자]{.hl}는 객체를 생성하기 위해 호출되는 특별한 함수입니다:
  - 클래스와 *같은 이름*을 가집니다;
  - *반환 유형이 없습니다*(`void`도 없음);
  - 객체가 생성될 때 호출되어 객체를 초기화합니다.

- 생성자는 일반 함수와 마찬가지로 [오버로딩]{.hl}할 수 있습니다.

- 생성자는 데이터 필드를 초기화합니다 — 클래스 멤버는 선언 시에 초기화될 수 없습니다. 생성자 없이 정의된 클래스에는 암시적으로 생성자가 부여됩니다. 생성자는 [초기화 목록]{.hl}을 사용할 수도 있습니다.

</div>
<div>

<div style="height: 4rem;"></div>

```cpp
// 본문 안에서 대입
Circle() {
    radius = 1;
}
```

<div style="height: 1rem;"></div>

```cpp
// 동일한 초기화 목록
Circle() : radius(1) {}
```

</div>
</div>

---
layout: prism
heading: "객체 구성과 사용 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 객체의 데이터와 함수는 객체 이름과 [점 연산자]{.hl}(`.`)를 사용하여 접근합니다.

- 객체지향 프로그래밍에서 객체의 [멤버]{.hl}란 데이터 필드와 함수를 의미합니다. 새롭게 생성된 객체는 메모리에 할당되며, 생성된 후에는 [객체 멤버 접근 연산자]{.hl}(점 연산자)를 사용하여 데이터에 접근하고 함수를 호출합니다.

- 접근된 데이터 필드를 [인스턴스 변수]{.hl}라 하고, 호출된 함수를 [인스턴스 함수]{.hl}라고 합니다.

```cpp
circle1.radius;    // refer to a data field of the object
circle1.getArea(); // call a function on the object
```

---
layout: prism
heading: "★ 코딩 스타일"
---

<div class="grid grid-cols-3 gap-3" style="margin-top: 1.5rem;">
<div>

K&R 스타일 (Java / C++):

```cpp
if (...) {
    // body;
}
```

</div>
<div>

GNU 스타일:

```cpp
if (...)
  {
    // body;
  }
```

</div>
<div>

BSD / VS 기본:

```cpp
if (...)
{
    // body;
}
```

</div>
</div>

<div style="margin-top: 1.5rem;"></div>

- C++에서 사용하는 명명 규칙:

<div class="sub-item">

- `camelCase` — 변수와 함수 &nbsp;·&nbsp; `PascalCase` — 사용자 정의 클래스 이름
- `snake_case`와 `SCREAMING_SNAKE_CASE` — 대체 스타일(예: 상수)

</div>

---
layout: prism
heading: "객체 구성과 사용 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 클래스 자체가 하나의 *데이터 유형*입니다. C++에서는 대입 연산으로 한 객체의 내용을 다른 객체에 복사할 수 있습니다.

- 객체 이름이 한번 선언되면, 다른 객체를 가리키도록 다시 할당될 수 없습니다. 객체마다 물리적으로 저장되는 것은 데이터뿐이며, 함수는 모든 객체가 공유하므로 객체의 크기는 작게 유지됩니다.

- 일회성 사용을 위해 이름 없는 [익명 객체]{.hl}를 생성할 수 있습니다. 인수 없는 생성자를 사용하더라도 소괄호는 반드시 붙여야 합니다.

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
heading: "클래스 정의와 구현의 분리 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.7em;
}
</style>

- C++에서는 클래스 [정의]{.hl}와 [구현]{.hl}을 분리하면 클래스의 유지보수가 쉬워집니다.

- 클래스 *정의*는 규약을 기술합니다: 모든 데이터 필드와 함께 생성자 및 함수의 원형을 목록으로 나열합니다.

- 클래스 *구현*은 그 규약을 실현합니다: 생성자와 함수의 본문을 제공합니다.

- 두 파일은 이름은 같지만 확장자가 다른 별도의 파일로 저장됩니다: 정의는 `.h` 파일에, 구현은 `.cpp` 파일에 저장됩니다.

---
layout: prism
heading: "클래스 정의와 구현의 분리 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

`Circle.h` — 정의:

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

`Circle.cpp` — 구현:

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
heading: "클래스 정의와 구현의 분리 (3/3)"
---

실습을 위해 `Circle.h`, `Circle.cpp`, 그리고 테스트용 `main`을 하나의 컴파일 가능한 파일로 합쳤습니다.

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
heading: 다중 포함 방지
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 헤더 파일이 두 번 이상 포함되는 것을 방지하기 위해 [포함 감시]{.hl}를 사용합니다.

- 같은 헤더를 2회 이상 호출하면 *다중 포함* 오류가 발생합니다.

- `#ifndef`, `#define`, `#endif` 지시자를 사용하면 다중 포함을 방지할 수 있습니다.
  - 예: `TestHead.cpp`가 `Circle.h`와 `Head.h`를 모두 포함하고, `Head.h`도 `Circle.h`를 포함한다면, `Circle.h`가 두 번 포함되어 — 감시가 없으면 오류가 발생합니다.

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
heading: "클래스에서의 인라인 함수 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 성능 개선을 위해, 짧은 함수는 [인라인 함수]{.hl}로 정의할 수 있습니다.

- 함수가 클래스 정의 *내부*에서 구현되면 자동으로 인라인 함수가 되며 — 이를 [인라인 정의]{.hl}라고 합니다.

- 함수가 클래스 내부에서 선언만 되었더라도(원형만), 추후 정의 시 `inline` 키워드를 사용하면 인라인 함수가 됩니다.

- 성능 개선에 유리한 것은 긴 함수가 아니라 *짧은* 함수를 인라인으로 만드는 것입니다.

---
layout: prism
heading: "클래스에서의 인라인 함수 (2/2)"
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
heading: "데이터 필드 캡슐화 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 데이터 필드를 전용(private)으로 만들면 데이터를 보호하고 클래스의 유지보수를 쉽게 할 수 있습니다.

- 앞의 `Circle` 클래스에서 `radius` 데이터 필드는 직접 수정이 가능합니다: `circle1.radius = 100;`

- 속성을 직접 수정할 수 있게 하는 것은 좋은 프로그래밍 방식이 *아닙니다*:
  - 데이터가 임의로 수정될 수 있습니다;
  - 클래스의 유지보수가 어려워지고 버그 발생 확률이 높아집니다;
  - `Circle`을 수정하면 이를 사용하는 모든 프로그램을 한꺼번에 변경해야 할 수 있습니다.

---
layout: prism
heading: "데이터 필드 캡슐화 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 직접 수정을 방지하기 위해, `private` 키워드로 데이터 필드를 [전용]{.hl}으로 선언하며 — 이를 [데이터 필드 캡슐화]{.hl}라고 합니다.

- 전용 데이터 필드에 접근하려면, 읽기에는 [get]{.hl} 함수를, 변경에는 [set]{.hl} 함수를 사용합니다.

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
heading: "데이터 필드 캡슐화 (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 일상적으로, 변수를 읽는 get 함수는 [접근자]{.hl}, 변수를 수정하는 set 함수는 [변경자]{.hl}라고 합니다.

- get 함수는 다음 형식을 사용합니다:

<div class="sub-item">

`returnType getPropertyName()` &nbsp;또는&nbsp; `bool isPropertyName()`

</div>

- set 함수는 다음 형식을 사용합니다:

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
heading: "실습: CircleWithPrivateDataField"
---

헤더, 구현, 테스트용 `main`을 하나의 실행 가능한 파일로 합쳤습니다.

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
heading: "변수의 범위 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 인스턴스 변수와 정적 변수의 범위는 선언된 위치와 상관없이 *클래스 전체*입니다.

- 데이터 필드는 클래스 내의 모든 생성자와 함수가 접근할 수 있는 변수이며, 멤버는 어떤 순서로든 작성할 수 있습니다.

- 오른쪽의 세 클래스는 모두 동일하지만, C++ 프로그래머는 보통 첫 번째처럼 작성합니다.

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
heading: "실습: HideDataField.cpp"
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
heading: "변수의 범위 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 데이터 필드 변수는 단 한 번만 선언할 수 있지만, 어느 한 함수 안에서 사용한 변수 이름은 다른 함수의 변수 이름으로 다시 사용할 수 있습니다.

- [지역 변수]{.hl}는 함수 안에서 선언되어 그 안에서 지역적으로 사용됩니다.

- 지역 변수가 데이터 필드와 같은 이름을 가지면, [지역 변수가 우선권을 가지며]{.hl} 같은 이름의 데이터 필드는 숨겨집니다.
  - 이러한 혼동을 피하기 위해, 함수의 매개변수로 사용하는 경우를 제외하면 클래스 안에서 데이터 필드와 같은 이름의 변수는 선언하지 않는 것이 좋은 습관입니다.

---
layout: prism
heading: "클래스 추상화와 캡슐화 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [클래스 추상화]{.hl}는 클래스의 구현과 사용을 분리하는 것입니다.

- 클래스 작성자는 사용자에게 클래스를 어떻게 사용하는지 알려주는 설명문을 제공할 수 있습니다.

- 함수와 데이터 필드가 어떻게 동작하는지에 대한 서술과 함께, 외부에서 접근 가능한 함수 및 데이터 필드의 모음이 [클래스 규약]{.hl}으로 제공됩니다.

</div>
<div>

<div style="height: 4rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image7.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "클래스 추상화와 캡슐화 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 구현 세부 사항을 사용자에게 감추는 것을 [클래스 캡슐화]{.hl}라고 합니다.
  - 면적이 *어떻게* 계산되는지 몰라도 `Circle` 객체를 생성하고 면적을 계산할 수 있습니다.

- 컴퓨터 시스템은 CPU, motherboard, fan 등 여러 부품으로 이루어져 있습니다.

- 이 부품들이 함께 동작하려면, 각 부품이 어떻게 사용되고 어떻게 상호작용하는지만 알면 되고 — 각 부품이 내부적으로 어떻게 동작하는지는 알 필요가 없습니다.

- 각 부품은 그 부품에 대한 클래스의 객체로 생각할 수 있습니다.

---
layout: prism
heading: "클래스 추상화와 캡슐화 (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- UML 다이어그램이 주어지면, 클래스가 내부적으로 어떻게 구현되었는지 몰라도 규약을 토대로 테스트 프로그램을 작성할 수 있습니다.

- 즉, 클래스를 구현하는 일과 클래스를 사용하는 일은 서로 분리된 작업입니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image8.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "실습: TestLoanClass.cpp"
---

`Loan` 클래스는 UML 다이어그램의 규약을 구현하며, `main`은 입력을 읽어 상환액을 출력합니다.

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
heading: "DIY_W11: TV 클래스 만들기"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- UML 다이어그램을 토대로 `TV` 클래스를 만들어 보세요.
  - `channel`(1 ~ 120), `volumeLevel`(1 ~ 7), 그리고 `on`(TV가 켜져 있는지 여부).
  - 생성자와 함께 `turnOn`, `turnOff`, `setChannel`, `setVolume`, `channelUp`, `channelDown`, `volumeUp`, `volumeDown`.

- 각 동작은 TV가 켜져 있고 범위 안에 있을 때에만 적용되도록 방어 처리하세요.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w11/cpp-w11-image9.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY_W11: TV 클래스 — 예시 해답"
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

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
