---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 9 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-9/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">9주차: 함수</p>

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
heading: "함수 (1/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [함수]{.hl}는 재사용이 가능한 코드를 정의하고 조직화하며 간략화하기 위해 사용됩니다.

- C++에서는 유사한 역할을 하는 코드를 함수로 정의하고 반복해서 *호출*하여 반복적인 작업을 최소화할 수 있습니다.
  - `max`, `min`, `ceil`, `floor` 등이 익숙한 예시입니다.

- 같은 합산 루프를 세 번 작성하는 대신, 하나의 `sum(i1, i2)` 함수로 묶어 서로 다른 인수로 호출할 수 있습니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// i1부터 i2까지 모든 정수의 합을 반환
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
heading: "함수 (2/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 함수는 [반환값 유형]{.hl}, [함수 이름]{.hl}, [매개변수]{.hl}, [함수 몸체]{.hl}로 구성됩니다.
  - [함수 헤더]{.hl}에서 반환값 유형, 함수 이름, 매개변수를 지정합니다.
  - 헤더에 선언된 변수는 [형식 매개변수]{.hl}이고, 호출자가 제공하는 값은 [인수]{.hl}입니다.

- 반환값 유형은 함수가 [반환]{.hl}하는 값의 데이터 유형입니다.
  - 값을 반환하는 함수는 [값 반환 함수]{.hl}입니다.
  - 아무것도 반환하지 않는 함수는 [`void` 함수]{.hl}입니다(예: `srand`).

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w09/cpp-w09-image4.png" class="tikz-fig" style="width: 100%; margin-top: 2rem;" />

</div>
</div>

---
layout: prism
heading: "함수 (3/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 함수는 그 코드를 실행함으로써 [호출]{.hl}(invoke)됩니다.

- 함수에 반환값이 있는 경우, 함수 호출은 하나의 값으로 취급됩니다:
  - `int larger = max(3, 4);` 는 `max(3, 4)`의 반환값을 `larger`에 저장합니다.
  - `cout << max(3, 4);` 는 반환값을 곧바로 출력합니다.
  - 호출하는 쪽에서 반환값이 필요 없다면, 그냥 무시해도 됩니다.

- 함수를 호출하면 [제어]{.hl}가 호출된 함수로 넘어갑니다. `return` 문이 실행되거나 끝 괄호 `}`에 도달하면 제어가 호출자에게 돌아갑니다.

---
layout: prism
heading: "실습: Test Max"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 함수는 [호출되기 전에 정의되어야]{.hl} 합니다. `max`는 `main`에 의해 호출되므로 `main` *앞에서* 선언됩니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// 두 수 중 최댓값을 반환
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
    int k = max(i, j);   // i와 j의 값을 전달
    cout << "The maximum between " << i
         << " and " << j << " is " << k << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "함수 (4/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 함수가 호출될 때마다 시스템은 함수의 인수와 변수를 저장하는 [활성 레코드]{.hl}를 생성하여, 메모리 안의 [호출 스택]{.hl}에 쌓습니다.
  - 호출 스택은 *실행 스택*, *실행시간 스택*, *기계 스택*이라고도 합니다.

- 호출 스택은 [후입선출]{.hl}(LIFO) 구조로, 가장 나중에 들어온 데이터가 가장 먼저 나갑니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w09/cpp-w09-image7.png" class="tikz-fig" style="width: 100%; margin-top: 2rem;" />

</div>
</div>

---
layout: prism
heading: "void 함수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [`void` 함수]{.hl}는 값을 반환하지 않습니다.

- `void` 함수에는 `return` 문이 필요하지 않지만, 실행을 일찍 *끝내고* 호출자로 되돌아가기 위해 사용할 수 있습니다:
  - `return;`

- 예시 입력: `85.5` &rarr; 학점은 `B`입니다.

</div>
<div>

<CppRunner stdin="85.5">

```cpp
#include <iostream>
using namespace std;

// 점수에 대한 학점을 출력
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
heading: "값에 의한 인수 전달"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 인수는 [값에 의해 전달]{.hl}됩니다: 함수를 호출하면 인수의 값이 매개변수로 복사됩니다.

- 인수는 호출된 함수의 매개변수에 *순서대로* 결합됩니다 — 이를 [매개변수 순차 결합]{.hl}이라고 합니다.
  - `ch`를 정확히 `n`번 출력하려면 `nPrint('a', 3)`으로 호출합니다.
  - 원래의 `nPrintln`에는 두 가지 오류가 있었으며 아래에서 수정했습니다: (1) `int n = 1;`을 다시 선언하여 매개변수를 가렸고(shadowing), (2) 인수 순서를 *잘못* 넣어 `nPrintln(5, "...")`으로 호출했습니다.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

void nPrint(char ch, int n) {          // ch를 n번 출력
    for (int i = 0; i < n; i++)
        cout << ch;
}

void nPrintln(string message, int n) { // message를 n번 출력
    for (int i = 0; i < n; i++)        // 여기서 n을 다시 선언하지 말 것
        cout << message << endl;
}

int main() {
    nPrint('a', 3);
    cout << endl;
    nPrintln("Welcome to C++!", 5);    // 올바른 인수 순서
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "코드 모듈화"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 코드를 [모듈화]{.hl}(또는 [캡슐화]{.hl})하면 코드를 재사용할 수 있게 유지하고 유지보수와 디버깅을 쉽게 만듭니다.

- 함수는 중복 코드를 줄이고 코드 재사용을 가능하게 하며, 코드를 모듈화하여 프로그램의 전체 구조를 개선하는 데에도 사용됩니다.

- 함수로 코드를 모듈화하면 다음을 얻습니다:
  - `main` 로직과 추가적인 연산이 명확히 분리되어 코드를 이해하기 쉬워집니다.
  - [디버깅]{.hl} 범위가 좁아집니다 — 추가 연산의 오류는 해당 함수 안에 국한됩니다.
  - 다른 프로그램에서도 공유할 수 있는 재사용 가능한 함수가 됩니다.

---
layout: prism
heading: "실습: Prime Number Function"
---

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

// number가 소수인지 검사
bool isPrime(int number) {
    for (int divisor = 2; divisor <= number / 2; divisor++)
        if (number % divisor == 0)
            return false;   // number는 소수가 아님
    return true;            // number는 소수임
}

void printPrimeNumbers(int numberOfPrimes) {
    const int NUMBER_OF_PRIMES_PER_LINE = 10; // 한 줄에 10개씩 출력
    int count = 0;   // 찾은 소수의 개수
    int number = 2;  // 소수인지 검사할 수

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
heading: "함수 오버로딩"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- [함수 오버로딩]{.hl}은 *이름은 같되* *매개변수는 다른* 함수를 정의할 수 있게 해줍니다.

- 인수의 데이터 유형에 관계없이 같은 역할을 하는 함수(예: 최댓값 반환)를 만들려면 함수 오버로딩을 사용합니다.

- C++ 컴파일러는 함수의 [매개변수 목록]{.hl}에 따라 어떤 함수를 실행할지 결정합니다.

- 호출에 두 개 이상의 함수가 일치하여 컴파일러가 하나를 고르지 못하는 경우를 [모호한 호출]{.hl}이라고 하며, 컴파일 오류를 발생시킵니다.

---
layout: prism
heading: "실습: Test Function Overloading"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// 두 int 값 중 최댓값을 반환
int max(int num1, int num2) {
    if (num1 > num2) return num1;
    else return num2;
}

// 두 double 값 중 최댓값을 반환
double max(double num1, double num2) {
    if (num1 > num2) return num1;
    else return num2;
}

// 세 double 값 중 최댓값을 반환
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
heading: "함수 원형"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [함수 원형]{.hl}은 함수의 몸체를 작성하기 *전에* 함수를 선언하는 것입니다.

- 함수의 헤더는 호출되기 전에 반드시 선언되어야 하므로, 몸체 없이 헤더만 정의하는 것을 함수 원형을 정의한다고 합니다.
  - 전체 구현은 그 뒤 `main` *다음에* 나올 수 있습니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// 함수 원형
int max(int num1, int num2);

int main() {
    cout << "The maximum between 3 and 4 is "
         << max(3, 4) << endl;
    return 0;
}

// 두 int 값 중 최댓값을 반환
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
heading: "기본 인수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- C++에서는 [기본 인수]{.hl} 값을 가진 함수를 선언할 수 있으며, 인수 없이 호출하면 기본 값이 전달됩니다.
  - 기본 인수는 매개변수 목록의 *맨 뒤*에 와야 합니다.
  - 어떤 인수를 생략하면, 그 뒤의 모든 인수도 함께 생략해야 합니다.

```cpp
void f1(int x, int y = 0, int z);     // 잘못된 경우
void f2(int x = 0, int y = 0, int z); // 잘못된 경우
void f3(int x, int y = 0, int z = 0); // 알맞은 경우
void f4(int x = 0, int y = 0, int z = 0); // 알맞은 경우
f3(1, , 20);  // 잘못된 경우
f4(, , 2);    // 잘못된 경우
f3(1);        // y, z는 기본 값을 사용
f4(1, 2);     // z는 기본 값을 사용
```

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// width와 height는 기본 값 1
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
heading: "인라인 함수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 짧은 함수의 성능을 높이기 위해 C++은 [인라인 함수]{.hl}를 제공하며, `inline` 키워드를 붙여 선언합니다.

- 함수 호출에는 [실행 오버헤드]{.hl}가 발생합니다(인수와 CPU 레지스터를 스택에 푸시하고, 함수 간에 제어를 전달하는 등).

- 인라인 함수는 함수를 호출하는 대신, 컴파일러가 호출 지점마다 함수 코드를 직접 [복사]{.hl}합니다.

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
    f(month, year); // 인라인 함수 호출
    f(9, 2010);     // 인라인 함수 호출
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "지역, 전역, 정적 지역 변수 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- C++에서 변수는 [지역 변수]{.hl}, [전역 변수]{.hl}, [정적 지역 변수]{.hl}로 나뉩니다.

- 변수의 [범위]{.hl}(scope)는 그 변수가 참조될 수 있는 프로그램의 영역입니다.

- 함수 *안에서* 정의된 변수는 [지역 변수]{.hl}입니다.

- 모든 함수 *바깥에서* 선언되어 파일 내 모든 함수가 접근할 수 있는 변수는 [전역 변수]{.hl}입니다.
  - 지역 변수는 기본 값이 없지만, 전역 변수는 `0`으로 초기화됩니다.

---
layout: prism
heading: "실습: Variable Scope Demo"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void t1(); // 함수 원형
void t2(); // 함수 원형

int main() {
    t1();
    t2();
    return 0;
}

int y; // 전역 변수, 기본 값 0

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

- `t1`/`t2`는 각각 자신만의 지역 `x`를 가지며, 항상 `1`에서 시작합니다.

- 전역 `y`는 호출 사이에서 유지되므로, `t1`이 `0`에서 `1`로 증가시킨 뒤 `t2`가 그 값을 읽습니다.

</div>
</div>

---
layout: prism
heading: "지역, 전역, 정적 지역 변수 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `for` 헤더의 초기화에서 선언된 변수의 범위는 *루프 전체*로 설정됩니다.

- 한 함수 안에서 [중첩되지 않은]{.hl} 블록들은 같은 이름의 지역 변수를 선언할 수 있습니다.
  - *중첩된* 블록에서 같은 이름을 재사용하는 것도 허용되지만 좋은 습관은 아닙니다.

- 아래 드라이버는 서로 분리된(중첩되지 않은) 두 `for` 루프에서 `i`를 재사용합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void function1() {
    int x = 1;
    int y = 1;
    for (int i = 1; i < 10; i++) { // 블록 1의 i
        x += i;
    }
    for (int i = 1; i < 10; i++) { // 블록 2의 i
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
heading: "지역, 전역, 정적 지역 변수 (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 함수가 끝나면 모든 지역 변수는 메모리에서 사라집니다. 이러한 변수를 [자동 변수]{.hl}라고 합니다.

- 때로는 연속되는 호출 사이에서 지역 변수가 그 값을 *유지*하기를 원할 때가 있습니다.

- C++은 이 문제를 [정적 지역 변수]{.hl}로 해결합니다.
  - 정적 지역 변수는 프로그램이 끝날 때까지 메모리에 남아, 호출 사이에서 값을 유지합니다.
  - `static` 키워드로 선언합니다: `static int x = 1;`

---
layout: prism
heading: "실습: Static Variable Demo"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void t1(); // 함수 원형

int main() {
    t1();
    t1();
    return 0;
}

void t1() {
    static int x = 1; // 호출 사이에서 유지됨
    int y = 1;        // 매 호출마다 초기화됨
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

- 정적 `x`는 값을 유지합니다: 첫 호출에서 `1 → 2`, 두 번째 호출에서 `2 → 3`이 됩니다.

- 자동 변수 `y`는 매 호출마다 `1`로 다시 초기화되므로 항상 `2`를 출력합니다.

</div>
</div>

---
layout: prism
heading: "참조에 의한 인수 전달 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 매개변수는 [참조에 의해 전달]{.hl}될 수 있으며, 이때 형식 매개변수는 인수의 [별칭]{.hl}이 됩니다.

- 매개변수가 참조에 의해 전달되면, 함수 안에서 매개변수를 변경할 때 인수도 함께 변경됩니다.

- 여기서 `increment`는 매개변수를 *값에 의해* 받으므로 호출자의 `x`는 영향을 받지 않습니다.

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
heading: "실습: Swap by Value"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// 두 변수를 교환하려는 시도 — 동작하지 않음!
void swap(int n1, int n2) {
    cout << "\tInside the swap function" << endl;
    cout << "\tBefore swapping n1 is " << n1
         << " n2 is " << n2 << endl;
    // n1과 n2를 교환
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

- `n1`과 `n2`는 [복사본]{.hl}이므로, 이들을 교환해도 함수 자신의 변수에만 영향을 줍니다.

- 호출 후에도 `main`의 `num1`과 `num2`는 [변하지 않습니다]{.hl}.

</div>
</div>

---
layout: prism
heading: "참조에 의한 인수 전달 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 매개변수가 값에 의해 전달되면 호출자의 인수와는 별개로 *자신만의* 메모리를 받으며, 그 메모리는 함수가 반환될 때 사라집니다.

- [참조 변수]{.hl}는 원래 변수의 [별칭]{.hl}으로 동작하는 C++의 특수한 변수 유형으로, 참조에 의한 전달을 가능하게 합니다.
  - 타입 뒤(또는 이름 앞)에 `&`를 붙여 선언합니다: `int& r = count; // 또는 int &r = count;`

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w09/cpp-w09-image34.png" class="tikz-fig" style="width: 100%; margin-top: 2rem;" />

</div>
</div>

---
layout: prism
heading: "실습: Test Reference Variable"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 1;
    int& r = count;   // r은 count의 별칭
    cout << "count is " << count << endl;
    cout << "r is " << r << endl;

    r++;              // count도 함께 변경됨
    cout << "count is " << count << endl;
    cout << "r is " << r << endl;

    count = 10;       // r도 함께 변경됨
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

- `r`과 `count`는 *같은* 메모리 위치를 가리킵니다.

- `r`을 증가시키면 `count`가 변하고, `count`에 대입하면 `r`이 변합니다 — 둘은 항상 함께 움직입니다.

</div>
</div>

---
layout: prism
heading: "실습: Swap by Reference"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// 두 변수를 교환
void swap(int& n1, int& n2) {
    cout << "\tInside the swap function" << endl;
    cout << "\tBefore swapping n1 is " << n1
         << " n2 is " << n2 << endl;
    // n1과 n2를 교환
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
    swap(num1, num2); // 참조에 의한 전달
    cout << "After invoking the swap function, num1 is " << num1
         << " and num2 is " << num2 << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "참조에 의한 인수 전달 (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 참조에 의해 전달되면 참조 매개변수가 인수의 [별칭]{.hl}으로 동작하므로, 교환 같은 연산이 의도대로 이루어집니다.

- 참조에 의해 인수를 전달할 때, 형식 매개변수와 인수는 [같은 데이터 유형]{.hl}이어야 합니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w09/cpp-w09-image39.png" class="tikz-fig" style="width: 100%; margin-top: 2rem;" />

</div>
</div>

---
layout: prism
heading: "상수 참조 매개변수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 함수 안에서 값이 변경되는 것을 막기 위해 [상수 참조 매개변수]{.hl}를 지정할 수 있습니다.

- 매개변수 앞에 `const`를 붙이면, 그 값을 변경해서는 *안 된다는 것*을 컴파일러에 알립니다.
  - 이렇게 하면 참조에 의한 전달의 효율(복사 없음)과 값에 의한 전달의 안전성을 함께 얻습니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// 두 수 중 최댓값을 반환
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
heading: "함수 추상화와 단계적 상세화 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [함수 추상화]{.hl}는 프로그램을 구성하는 데 사용할 함수를 선별하는 과정에서 얻어집니다.

- [클라이언트]{.hl} 프로그램은 함수가 어떻게 구현되었는지 알 필요 없이 그 함수를 사용합니다.
  - 구현 내용은 캡슐화되어 감춰집니다 — 이를 [정보 은닉]{.hl}이라고 합니다.
  - 우리는 `rand`의 내부를 모른 채 난수를 생성하는 데 사용합니다.

- 함수 추상화를 프로그램 개발에 적용할 수 있습니다: 큰 프로그램을 작은 부분 문제로 분해하기 위해 [단계적 상세화]{.hl}로 알려진 [분할 정복]{.hl} 전략을 사용합니다.

---
layout: prism
heading: "함수 추상화와 단계적 상세화 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `printCalendar` 프로그램은 각각 하나의 부분 문제를 푸는 작은 함수들로 분해됩니다.

- `isLeapYear`나 `getNumberOfDaysInMonth` 같은 말단(leaf) 함수는 간단하고 테스트하기 좋은 구성 요소입니다.
  - 이 드라이버는 전체 프로그램을 조립하기 전에 이들을 *상향식*으로 테스트합니다.

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
heading: "함수 추상화와 단계적 상세화 (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 프로그램은 [하향식]{.hl} 또는 [상향식]{.hl}으로 구현할 수 있습니다.

- 하향식 방법은 위에서 아래로 내려가며 함수를 구현합니다.
  - 아직 구현되지 않은 함수를 사용하려면, 간단하지만 불완전한 버전인 [스텁]{.hl}으로 대체합니다.

- 상향식 방법은 아래에서 위로 올라가며 함수를 구현합니다.
  - 각 함수를 작성하면서 그것을 점검하는 테스트 프로그램인 [드라이버]{.hl}를 만듭니다.

- 두 방법 모두 함수를 [점진적으로]{.hl} 구현하여 오류를 개별 함수에 국한시킵니다. 하향식과 상향식은 함께 사용할 수 있습니다.

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

- [단계적 상세화]{.hl}는 큰 문제를 다루기 쉬운 작은 부분 문제로 나누어, 각각을 함수로 구현하는 것을 의미합니다.

- 실제 대규모 프로젝트에서는 단계적 상세화가 큰 도움이 됩니다 — 과연 *어떤 측면에서* 도움이 될지 생각해보세요.

- 아래의 완성된 `printCalendar`는 구성 요소들을 조립한 것입니다. 여러 연도와 월을 입력해보세요.
  - 예시 입력: `2027 9`

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

// 1800년 1월 1일은 수요일 (Sun = 0)
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

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
