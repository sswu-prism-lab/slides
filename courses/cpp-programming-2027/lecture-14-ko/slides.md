---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 14 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-14/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">14주차: 기말 리뷰</p>

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
heading: "개요: 함수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 함수는 [반환값 유형]{.hl}, [함수 이름]{.hl}, [매개변수]{.hl}, [함수 몸체]{.hl}로 구성됨.
  - [함수 헤더]{.hl}에서 반환값 유형, 함수 이름, 매개변수를 지정함.
  - 함수 헤더에 선언된 변수를 [형식 매개변수]{.hl}라 하며, 호출자가 넘겨주는 값을 [인수]{.hl}라고 함.

- 반환값 유형은 함수가 *반환*하는 값의 데이터 유형을 의미함.
  - [값 반환 함수]{.hl}는 값을 반환하고, [`void` 함수]{.hl}(예: `srand`)는 값을 반환하지 않음.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "개요: void 함수"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- `void` 함수는 값을 반환하지 않음. `return`문이 필요하지 않지만, 함수의 실행을 끝내고 호출자로 되돌아가기 위해 `return;`을 사용할 수 있음.

<CppRunner stdin="85">

```cpp
#include <iostream>
using namespace std;

// 숫자 점수에 해당하는 등급을 출력
void printGrade(double score) {
    if (score >= 90.0)      cout << 'A' << endl;
    else if (score >= 80.0) cout << 'B' << endl;
    else if (score >= 70.0) cout << 'C' << endl;
    else if (score >= 60.0) cout << 'D' << endl;
    else                    cout << 'F' << endl;
    return;   // void 함수의 선택적인 조기 종료
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
heading: "개요: 값에 의한 인수 전달"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- 인수는 보통 [값에 의해 전달]{.hl}됨: 함수가 호출될 때 각 인수의 값이 매개변수로 복사됨.

- 인수는 호출된 함수의 매개변수에 *순차적으로* 결합되며, 이를 [매개변수 순차 결합]{.hl}이라고 함.

- 함수는 복사본을 다루므로, 매개변수에 가한 변경은 호출자의 원래 인수에 **영향을 주지 않음**.

---
layout: prism
heading: "개요: 참조에 의한 인수 전달"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 매개변수는 [참조에 의해 전달]{.hl}될 수 있으며, 이때 형식 매개변수는 인수의 [별칭]{.hl}이 되어 매개변수를 바꾸면 인수도 함께 바뀜.
- [참조 변수]{.hl}는 원 변수에 대한 별칭으로 동작함. 데이터 유형 뒤(또는 변수 이름 앞)에 `&`를 붙여 선언함: `int& r = count;`.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void increaseByValue(int v)      { v++; }  // 복사본에 대해 동작
void increaseByReference(int& r) { r++; }  // r은 인수의 별칭

int main() {
    int count = 5;
    increaseByValue(count);
    cout << "after pass-by-value:     " << count << endl;  // 여전히 5
    increaseByReference(count);
    cout << "after pass-by-reference: " << count << endl;  // 이제 6
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "개요: 지역, 전역, 정적 지역 변수"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- C++의 변수는 [지역]{.hl}, [전역]{.hl}, [정적 지역]{.hl} 변수로 나뉨.

- 변수의 [범위]{.hl}는 그 변수가 참조될 수 있는 프로그램의 영역을 의미함.

- 함수 안에서 정의된 변수를 [지역 변수]{.hl}라고 함.

- 모든 함수 외부에서 선언되어 파일 내 모든 함수에서 접근 가능한 변수를 [전역 변수]{.hl}라고 함.
  - 지역 변수는 기본 값이 없지만, 전역 변수는 `0`으로 초기화됨.

---
layout: prism
heading: "개요: 정적 지역 변수"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- 함수 실행이 끝나면 지역 변수는 메모리에서 사라지며, 이러한 변수를 [자동 변수]{.hl}라고 함. 반면 [정적 지역 변수]{.hl}(`static`)는 연속되는 호출에서도 값을 유지하며 프로그램이 끝날 때까지 존재함.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int nextCount() {
    static int count = 0;   // 호출 간에 유지되고 다시 초기화되지 않음
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
heading: "개요: 배열"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [배열]{.hl}은 많은 데이터의 모음을 저장함. C++에서 배열은 같은 유형의 요소를 고정된 개수만큼 [연속된]{.hl} 메모리에 저장하는 자료구조임.

- 배열의 [요소]{.hl}는 [인덱스]{.hl}로 접근함. `num0, num1, ..., num99`처럼 선언하는 대신, 하나의 배열 `nums`를 선언하고 `nums[0], nums[1], ..., nums[99]`로 접근함.

- 배열 선언은 요소 유형, 이름, 크기를 지정함: `elementType arrayName[SIZE];` 여기서 `SIZE`는 상수(`const`)임.
  - 갓 선언된 배열은 임의의 값으로 채워져 있음.

---
layout: prism
heading: "개요: 객체와 클래스"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [클래스]{.hl}는 [객체]{.hl}의 *속성*과 *행동*을 정의함.

- [객체지향 프로그래밍]{.hl}에서는 프로그램을 객체로 구성함. 객체는 명확히 구별되는 개체로, 자신만의 유일한 특성인 [상태]{.hl}와 [행동]{.hl}을 가짐.

- 객체의 상태(그 [속성]{.hl} / [특성]{.hl})은 [데이터 필드]{.hl}로 표현됨.
  - 예: *원* 객체는 그 속성을 나타내는 `radius` 데이터 필드를 가짐.

- 객체의 행동(그 [동작]{.hl})은 함수로 정의됨.

---
layout: prism
heading: "개요: 클래스"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 같은 유형의 객체는 공통 클래스로 정의됨.

- 클래스는 객체가 어떤 데이터 필드와 함수를 가질지 결정하는 [템플릿]{.hl}(설계도)이며, 객체는 클래스의 [인스턴스]{.hl}임.
  - 인스턴스를 생성하는 것을 [실체화]{.hl}라고 함.
  - `Circle` 클래스 하나만 있으면 무수히 많은 `Circle` 객체를 생성할 수 있음.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image6.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "개요: 객체 구성과 사용"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 객체의 데이터와 함수는 객체 이름과 [점 연산자]{.hl}(`.`)로 접근함.

- 객체지향에서 객체의 [멤버]{.hl}란 데이터 필드와 함수를 의미함. 새로 생성된 객체는 메모리에 할당되며, 생성 후 [멤버 접근 연산자]{.hl} `.`로 데이터에 접근하고 함수를 호출함.

- 접근되는 데이터 필드를 [인스턴스 변수]{.hl}라 하고, 호출되는 함수를 [인스턴스 함수]{.hl}라 함.

```cpp
circle1.radius;      // 객체의 데이터 필드를 참조
circle1.getArea();   // 객체에 대한 함수를 호출
```

---
layout: prism
heading: "개요: 객체지향 개념"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 프로그램을 단순히 데이터와 처리 방법으로 나누는 대신, OOP는 프로그램을 [객체]{.hl}—처리 방법(메소드 / 행동 / 함수)과 데이터(변수)의 묶음—로 나누고 그 상호작용에 집중함. C++에서는 이를 [클래스]{.hl}로 자연스럽게 표현함.

- 함수는 *데이터를 처리하는 방법*은 잘 구조화하지만, *데이터* 자체는 구조화하지 못함. OOP는 모든 객체가 속성과 행동을 함께 지니는 현실 세계를 반영함.

- 내부 구현 세부를 감춤으로써([정보 은닉]{.hl}), OOP는 모듈 내부의 응집력을 높이고 모듈 간 결합도를 낮추어 유연성과 유지보수성을 향상시킴.

---
layout: prism
heading: "개요: 인스턴스 멤버와 정적 멤버"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [정적 변수]{.hl}는 공유되는 하나의 메모리 위치에 저장됨: 한 객체가 값을 바꾸면 그 클래스의 모든 객체가 영향을 받음.
  - UML 표기에서 정적 변수와 함수는 [밑줄]{.hl}로 표현함.

- 정적 멤버는 `static` 키워드를 사용함.

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
heading: "개요: 포인터"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [포인터 변수]{.hl}(포인터)는 값으로 *메모리 주소*를 저장하기 위해 선언됨. 반면 일반 변수는 데이터 값(정수, 실수, 문자 등)을 저장함.

- 메모리의 각 바이트는 고유 주소를 가지며, 변수의 주소는 그 첫째 바이트의 주소임. `int`는 4바이트를 차지하므로 첫째 바이트가 그 변수의 주소가 됨.

- 포인터는 사용 전에 선언해야 함: `dataType* pVarName;`, 그 뒤 주소를 할당함: `pVarName = &varName;`.

---
layout: prism
heading: "개요: 포인터 — & 와 *"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `&` — [주소 연산자]{.hl}: `&count`는 `count`의 주소임.

- `*` — [역참조 연산자]{.hl}: `*pCount`는 포인터 `pCount`가 가리키는 위치에 저장된 값임.

```cpp
int count = 5;
string s("ABC");
int* pCount;
string* pString;
pCount = &count;   // pCount는 이제 count의 주소를 담음
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image8.png" class="tikz-fig" style="width: 78%;" />

</div>
</div>

---
layout: prism
heading: "개요: 배열과 포인터"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- C++에서 배열은 근본적으로 포인터임: 배열의 이름은 첫 번째 요소를 가리키는 *상수 포인터*이므로, `list[i]`, `*(list + i)`, `p[i]`, `*(p + i)`는 모두 같은 요소를 가리킴.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int list[6] = {11, 12, 13, 14, 15, 16};
    int* p = list;   // 배열 이름은 첫 요소를 가리키는 포인터

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
heading: "개요: 동적 객체 생성과 접근"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- `new` 연산자는 동적 객체를 생성함. 포인터를 통해 멤버에 접근하려면 역참조 후 `.`을 쓰거나, 축약형 [화살표 연산자]{.hl} `->`를 사용함. `delete`는 객체를 명시적으로 삭제함.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string* pString = new string("abcdefg");
    cout << *pString << endl;                             // abcdefg
    cout << "First three (via *.): "
         << (*pString).substr(0, 3) << endl;             // 점 연산자
    cout << "First three (via ->): "
         << pString->substr(0, 3) << endl;               // 화살표 연산자

    delete pString;   // 객체를 명시적으로 삭제
    // delete 이후 *pString을 읽는 것은 미정의 동작 — 생략함.
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "개요: this 포인터"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- [`this` 포인터]{.hl}는 호출 객체 자신을 가리키며, (매개변수가 데이터 필드와 같은 이름을 가질 때) 숨겨진 데이터 필드를 참조하는 데 사용함.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Circle {
public:
    Circle() { radius = 1; }
    Circle(double radius) { this->radius = radius; }      // this->로 모호성 해소
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
    c.setRadius(-3);   // 음수는 거부됨 -> 0
    cout << "after setRadius(-3): radius = " << c.getRadius() << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "개요: 소멸자"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- [소멸자]{.hl}는 생성자의 반대임: 생성자는 객체가 생성될 때, 소멸자는 객체가 삭제될 때 호출됨. 소멸자를 직접 정의하지 않으면 모든 클래스에 기본 소멸자가 포함됨. 이름은 생성자와 같되 앞에 틸드(`~`)를 붙임.

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
        Circle temp(1.0);        // 여기서 생성됨
        cout << "Inner area = " << temp.getArea() << endl;
    }                            // 내부 스코프가 끝나면서 temp 소멸
    cout << "After inner scope\n";
    return 0;                    // 여기서 c 소멸
}
```

</CppRunner>

---
layout: prism
heading: "개요: 얕은 복사와 깊은 복사"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

- 모든 클래스에는 객체를 복사하는 데 쓰이는 *복사 생성자*가 있음. 기본 복사 생성자나 대입 연산자(`=`)를 사용하면 [얕은 복사]{.hl}가 수행됨: 데이터 필드가 포인터일 때, 가리키는 내용이 아니라 포인터의 *주소*만 복사됨.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image11.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

- [깊은 복사]{.hl}는 포인터가 가리키는 *내용*을 복사함. 이를 위해 복사 생성자를 직접 정의하여 각 객체가 자신만의 독립적인 데이터를 갖게 함.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w14/cpp-w14-image10.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "개요: 깊은 복사 실습"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- 사용자 정의 복사 생성자는 *새* 배열을 할당하므로 복사본이 독립적임 — `c2`를 바꿔도 `c1`은 그대로임.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

class Course {
public:
    Course(int cap) : capacity(cap), numStudents(0) { students = new string[cap]; }
    // 깊은 복사 생성자: 자신의 배열을 할당하고 내용을 복사
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
    Course c2 = c1;          // 깊은 복사 -> 독립적인 배열
    c2.setFirst("Zoe");      // c2의 데이터만 수정
    cout << "c1 first student: " << c1.first() << endl;   // Alice
    cout << "c2 first student: " << c2.first() << endl;   // Zoe
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "기말고사"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 총 [40점]{.hl}, [15~20문제]{.hl}, 한국어로 출제.

- 문제 유형:
  - 단순 O-X 퀴즈.
  - C++ 코드의 출력 예측(조건문과 반복문 포함).

- 개념 서술(함수, 클래스, 객체지향, 포인터 등).

- [의사 알고리즘]{.hl} 작성(손코딩이 더 편하면 손코딩도 OK).

- 주어진 코드의 오류 고치기.

- 목적 지향적 문제 풀기(참고: 중간고사 몬테카를로 시뮬레이션).

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
