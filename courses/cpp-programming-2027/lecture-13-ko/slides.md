---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 13 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-13/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">13주차: 포인터와 동적 메모리</p>

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
heading: "개요: 객체지향 개념"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 프로그램을 단순히 *데이터*와 *처리 방법*으로 나누는 것이 아니라, [객체지향 프로그래밍]{.hl}은 프로그램을 [객체]{.hl}라는 기본 단위로 나눈 뒤 이들이 어떻게 상호작용하는지에 초점을 맞춘다.
  - [객체]{.hl}는 하나의 역할을 수행하는 *메소드*(행동, 함수)와 그것이 다루는 *데이터*(변수)를 하나로 묶은 것이다. C++에서는 이를 [클래스]{.hl}로 자연스럽게 표현한다.

- 함수는 데이터의 *처리 방법*은 잘 구조화하지만, *데이터* 자체는 구조화하지 못한다. 객체지향은 모든 객체가 자신의 속성과 행동 모두에 연관되어 있는 현실 세계를 반영한 방식이다.

- 객체의 내부 세부 구현을 외부로부터 감춤으로써([정보 은닉]{.hl}), 모듈 내부의 *응집력*은 높이고 모듈 간의 *결합도*는 낮추어 유연성과 유지보수성을 향상시킨다.

---
layout: prism
heading: "개요: 인스턴스 멤버와 정적 멤버"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [정적 변수]{.hl}는 공통으로 공유되는 하나의 메모리 위치에 값을 저장한다. 한 객체가 이 값을 변경하면 같은 클래스의 *모든* 객체가 영향을 받는다.
  - UML 표기에서 정적 변수와 함수는 [밑줄]{.hl}로 표현한다.

- 정적 변수와 함수는 `static` 키워드를 사용한다.

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
heading: "포인터 (1/5)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [포인터 변수]{.hl}(또는 간단히 *포인터*)는 그 값으로 [메모리 주소]{.hl}를 저장하기 위해 선언되며, 일반 변수는 데이터 값(정수, 실수, 문자 등)을 저장한다.

- 메모리의 각 바이트에는 고유한 주소가 지정되어 있으므로, 변수의 주소는 그 변수에 할당된 *첫째* 바이트의 주소이다. `int`는 4바이트를 차지하므로, 그 첫째 바이트가 바로 그 변수의 주소가 된다.

- 다른 변수와 마찬가지로 포인터도 사용하기 전에 선언되어야 하며, 다음 구문을 따른다.

```cpp
dataType* pVarName;
```

- 선언 이후에는 변수의 주소를 할당할 수 있다.

```cpp
pVarName = &varName;
```

---
layout: prism
heading: "포인터 (2/5)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `&` — [주소 연산자]{.hl}.
  - `&count`는 `count`의 *주소*를 의미한다.

- `*` — [역참조 연산자]{.hl}.
  - `*pCount`는 `pCount`가 가리키는 위치에 *저장된 값*을 의미한다.

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
heading: "실습: TestPointer.cpp"
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
heading: "포인터 (3/5)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 포인터는 선언과 동시에 초기화하거나, 이후 대입문을 통해 초기화할 수 있다.

- 포인터를 *통해* 값을 참조하는 것을 [간접 참조]{.hl}라고 한다.

- 포인터의 유형은 자신이 가리키는 변수의 유형과 일치해야 한다.

```cpp
*pCount = &count; // 잘못된 표현
pCount = &count;  // 올바른 표현

count++;                 // 직접 참조
cout << count << endl;
(*pCount)++;             // 간접 참조
cout << count << endl;   // *pCount는 pCount가 가리키는 값
```

---
layout: prism
heading: "포인터 (4/5)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 포인터에도 [대입 연산자]{.hl}를 적용할 수 있다.

- `pX = pY`는 *주소*를 복사하므로, 이제 `pX`는 `pY`가 가리키는 곳을 가리킨다.

- `*pX = *pY`는 *값*을 복사하며, 두 포인터가 가리키는 위치는 그대로 유지된다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image4.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "포인터 (5/5)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

포인터 복사 — `pX = pY`:

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

값 복사 — `*pX = *pY`:

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

- `int* pX = &x, pY = &y;`에서 `pX`는 `int*`이지만 `pY`는 그냥 `int`임에 주의하자 — `*`는 *유형*이 아니라 *이름*에 결합된다.

---
layout: prism
heading: "typedef 키워드"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `typedef`를 사용하면 사용자가 [동의어 유형]{.hl}을 정의할 수 있어, 코드를 간단하게 하고 미묘한 오류를 피하는 데 도움이 된다.

```cpp
typedef existingType newType;
```

- 이는 새로운 유형을 만드는 것이 **아니라**, 기존 유형에 대한 *동의어*를 만드는 것이다.
  - `int* p1, p2;`는 `p1`을 `int*`, `p2`를 `int`로 만들지만, `intPointer p3, p4;`는 *둘 다* `int*`로 만든다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    typedef int integer;      // integer는 int의 동의어
    integer value = 40;
    cout << "value = " << value << endl;

    typedef int* intPointer;  // intPointer는 int*의 동의어
    int a = 1, b = 2;
    intPointer p3 = &a, p4 = &b;  // 둘 다 int*
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
heading: "포인터와 const"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [상수 포인터]{.hl}는 하나의 문장에서 선언과 초기화를 *동시에* 해야 하며, 이후에는 가리키는 대상을 바꿀 수 없다.

- [상수 데이터를 가리키는 포인터]{.hl}는 그 자신은 다시 대입할 수 있지만, 그것을 통해 가리키는 대상을 수정할 수는 없다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    double radius = 5;
    double* const p = &radius;  // 상수 포인터
    *p = 6;                     // OK: radius가 6이 됨
    cout << "radius = " << radius << endl;
    // p = &length;             // 에러: p는 상수 포인터

    double length = 10;
    const double* p1 = &radius; // 상수 데이터를 가리키는 포인터
    // *p1 = 7;                 // 에러: p1을 통해 수정 불가
    p1 = &length;               // OK: p1 자체는 상수가 아님
    cout << "*p1 = " << *p1 << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "배열과 포인터"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- C++에서 배열은 근본적으로 [포인터]{.hl}이다. 배열의 이름은 첫 번째 요소를 가리키는 *상수 포인터*이다. 따라서 `list[i]`, `*(list + i)`, `*(p + i)`, `p[i]`는 모두 같은 요소를 가리킨다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image5.png" class="tikz-fig" style="width: 62%; margin: 0.4rem auto;" />

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int list[6] = {11, 12, 13, 14, 15, 16};
    int* p = list;                     // 배열 이름은 list[0]을 가리키는 포인터
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
heading: "함수에서 포인터 전달과 반환"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 포인터는 함수에 [값에 의해]{.hl} 또는 [참조에 의해]{.hl} 전달될 수 있다. 두 포인터 `q1`, `q2`를 받는 함수 `f`를 `f(p1, &p2)`로 호출하는 경우를 생각해 보자.
  - `q1`은 *값에 의해* `p1`으로 전달되므로, `*p1`과 `*q1`은 같은 내용을 가리킨다. `*p1`을 변경하면 `*q1`도 변경되지만, `p1` 자체를 변경해도 `q1`은 변경되지 **않는다**.
  - `q2`는 *참조에 의해* `p2`로 전달되므로, 둘은 서로 [별칭]{.hl}이 된다. `*p2`나 `p2` 중 어느 것을 변경해도 `*q2`와 `q2`가 함께 변경된다.

- 함수가 포인터 매개변수를 받을 수 있듯이, 포인터를 *반환*할 수도 있다 — 함수 헤더의 반환 유형을 포인터 유형으로 지정해야 한다.

```cpp
int* returnList(int* list);
```

---
layout: prism
heading: "실습: TestPointerArgument.cpp"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void swap1(int n1, int n2)      { int t = n1; n1 = n2; n2 = t; }  // 값에 의한 전달
void swap2(int& n1, int& n2)    { int t = n1; n1 = n2; n2 = t; }  // 참조에 의한 전달
void swap3(int* p1, int* p2)    { int t = *p1; *p1 = *p2; *p2 = t; }  // 값에 의한 포인터 전달
void swap4(int*& p1, int*& p2)  { int* t = p1; p1 = p2; p2 = t; }     // 참조에 의한 포인터 전달

int main() {
    int num1 = 1, num2 = 2;
    cout << "start:  num1=" << num1 << " num2=" << num2 << endl;  // 1 2
    swap1(num1, num2);
    cout << "swap1:  num1=" << num1 << " num2=" << num2 << endl;  // 1 2 (변화 없음)
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
heading: "동적 영구 메모리 할당 (1/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `new` 연산자는 원시 값, 배열, 객체에 대해 실행 시점에 [영구 메모리]{.hl}를 생성한다.

- 입력 배열을 변경하지 않고 그 *역순 복사본*을 반환하는 함수는 다음과 같이 작성할 수 있다.

<div class="sub-item-enum">

1. 원래 배열 `list`를 입력으로 받는다.
2. 같은 크기의 `result` 배열을 선언한다.
3. 반복하며 요소를 역순으로 복사한다.
4. 포인터를 통해 `result`를 반환한다.

</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image6.png" class="tikz-fig" style="width: 100%; margin-top: 3rem;" />

</div>
</div>

---
layout: prism
heading: "실습: ArrayReverse.cpp"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int* reverse(const int* list, int size) {
    int* result = new int[size];   // 동적 배열: 함수가 반환된 후에도 유지됨
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
    delete[] p;   // 모든 new는 delete와 짝을 맞춘다
    return 0;
}
```

</CppRunner>

<!-- A local `int result[6]` would be discarded when the function returns (a dangling pointer); `new int[6]` fixes this. -->

---
layout: prism
heading: "동적 영구 메모리 할당 (2/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 함수의 [호출 스택]{.hl}에 있는 메모리는 계속 유지되지 않고 함수가 반환될 때 폐기된다. 함수가 반환된 후에도 `result`를 살아 있게 하려면 영구 저장소에 할당해야 한다.

- `new`를 사용한 [동적 메모리 할당]{.hl}이 그러한 영구 저장소를 제공하며, 이렇게 생성된 배열을 [동적 배열]{.hl}이라 한다.
  - 일반 배열은 크기가 반드시 *상수*여야 하지만, 동적 배열의 크기는 실행 시점에 결정되므로 정수 *변수*를 사용할 수 있다.

- `new`로 할당된 메모리는 영구적이어서, 명시적으로 제거하거나 프로그램이 종료될 때까지 존재한다. 제거는 `delete` 연산자를 사용한다.

```cpp
delete p;
```

---
layout: prism
heading: "동적 영구 메모리 할당 (3/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.9em;
}
</style>

- 포인터가 가리키던 메모리가 삭제된 후에는, 그 포인터의 값이 [정의되지 않은]{.hl} 상태가 된다.

- 다른 포인터가 동일한 삭제된 메모리를 가리키고 있으면 그것 역시 정의되지 않은 상태가 되며, 이러한 포인터를 [허상 포인터]{.hl}라고 한다.

- 포인터가 가리키는 메모리를 삭제하기 *전에* 실수로 재할당하면, 이전 블록에는 더 이상 접근하거나 해제할 수 없게 되는데, 이를 [메모리 누설]{.hl}이라 한다.

- 모든 `new`를 대응하는 `delete`와 짝을 맞추는 것은 메모리 누설을 방지하는 좋은 프로그래밍 습관이다.

---
layout: prism
heading: "동적 영구 메모리 할당 (4/4)"
---

<div class="flex justify-center" style="margin-top: 1rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w13/cpp-w13-image7.png" class="tikz-fig" style="width: 72%;" />
</div>

<div style="margin-top: 0.8rem;"></div>

- `(a)` `int* p = new int;`는 `int`용 메모리를 할당하고 그 주소를 `p`에 대입한다. `(b)` `*p = 45;`는 그곳에 45를 저장한다. `(c)` `p = new int;`는 `p`를 재할당하여, 이전 블록은 이제 [누설]{.hl}이 된다.

---
layout: prism
heading: "동적 객체 생성과 접근"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `new` 연산자는 [동적 객체]{.hl}를 생성할 수 있다.

- 포인터를 통해 멤버에 접근하려면 포인터를 역참조한 뒤 점(`.`) 연산자를 사용한다.

- [멤버 선택 연산자]{.hl} — 화살표(`->`) — 는 포인터를 통해 멤버에 접근하는 축약 표현이다.

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
    delete pString;                      // 객체 삭제
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "this 포인터"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [`this` 포인터]{.hl}는 호출 객체 자신을 가리키며, 같은 이름의 매개변수에 의해 가려진 데이터 필드에 접근할 때 사용한다.

- 여기서 생성자 매개변수 `radius`가 필드 `radius`를 가리므로, `this->radius`로 필드를 명시적으로 지칭한다.

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
heading: "소멸자"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [소멸자]{.hl}는 생성자의 반대이다. 생성자는 객체가 *생성될* 때 실행되고, 소멸자는 객체가 *삭제될* 때 실행된다.
  - 명시적으로 정의하지 않으면, 모든 클래스는 *기본* 소멸자를 갖는다.

- 소멸자는 클래스와 같은 이름을 가지며, 앞에 틸드(`~`)를 붙인다.

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
    return 0;   // 소멸자는 여기서 역순으로 실행됨
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Course 클래스"
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
    ~Course();                  // 소멸자
    string getCourseName() const;
    void addStudent(const string& name);
    void dropStudent(const string& name);
    string* getStudents() const;
    int getNumberOfStudents() const;
private:
    string courseName;
    string* students;           // 동적 배열
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
heading: "실습: Course (통합)"
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
    students = new string[capacity];   // 실행 시점까지 크기를 모름
}
Course::~Course() { delete[] students; }   // 동적 배열 해제
string Course::getCourseName() const { return courseName; }
void Course::addStudent(const string& name) {
    students[numberOfStudents] = name;
    numberOfStudents++;
}
void Course::dropStudent(const string& name) {
    for (int i = 0; i < numberOfStudents; i++) {
        if (students[i] == name) {
            for (int j = i; j < numberOfStudents - 1; j++)
                students[j] = students[j + 1];  // 나머지를 왼쪽으로 이동
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
heading: "HW_W13: dropStudent 함수 구현"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- `Course` 클래스의 `dropStudent` 함수를 구현하세요 — 이 함수 **하나만** 구현하고, 함수 헤더는 변경하지 마세요.

- 조건문과 반복문을 사용하고, 데이터 필드가 일관되게 유지되도록 하세요(남은 학생을 이동하고 인원수를 줄임).

- `HW_W13_20XXXXXX.cpp`로 저장한 뒤 LMS에 업로드하세요.

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

// dropStudent: 이름이 처음 일치하는 학생을 순서를 유지하며 제거한다.
void dropStudent(string* students, int& count, const string& name) {
    for (int i = 0; i < count; i++) {
        if (students[i] == name) {
            for (int j = i; j < count - 1; j++)
                students[j] = students[j + 1];  // 왼쪽으로 이동
            count--;                            // 학생 한 명 감소
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
heading: "얕은 복사와 깊은 복사 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 모든 클래스에는 객체를 복사하는 데 사용되는 [복사 생성자]{.hl}가 포함되어 있다.

- 기본 복사 생성자(또는 `=`)는 [얕은 복사]{.hl}를 수행한다. 데이터 필드가 포인터일 때, 내용이 아니라 *주소*를 복사하므로 두 객체가 하나의 배열을 공유하게 된다.

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
    // 복사 생성자 없음 -> 기본(얕은) 복사
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
    Course course4(course3);   // 얕은 복사: 배열 공유
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
heading: "얕은 복사와 깊은 복사 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [깊은 복사]{.hl} — 포인터가 가리키는 *내용*만 복사 — 를 하려면, 직접 복사 생성자를 정의한다.

```cpp
class Course {
public:
    Course(const string& courseName, int capacity);
    ~Course();
    Course(const Course&);      // 사용자 정의 복사 생성자
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
heading: "얕은 복사와 깊은 복사 (3/3)"
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
    Course(const Course& course) {   // 깊은 복사
        courseName = course.courseName;
        numberOfStudents = course.numberOfStudents;
        capacity = course.capacity;
        students = new string[capacity];  // 새로운 배열
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
    Course course4(course3);   // 깊은 복사: 독립된 배열
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

<div style="margin-top: 1rem; text-align: center; color:#9aa0a6;">이제 각 객체가 자신만의 학생 배열을 소유한다.</div>

</div>
</div>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
