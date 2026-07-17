---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 4 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-4/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">4주차: 수학 함수와 문자</p>

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
heading: "복습: if-else 문"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- *예/아니오* 판단은 여러 가지 일을 이끌어낼 수 있으며, 컴퓨터 과학에서는 이를 [참]{.hl} / [거짓]{.hl}으로 표현합니다.

- 참/거짓은 *논리 데이터*와 *논리 연산자*로부터 결정됩니다.
  - 논리 데이터가 조건을 만족하면 `true`, 그렇지 않으면 `false`입니다.

- C++에서 `true`와 `false`는 [예약어]{.hl}입니다.

</div>
<div>

<div style="height: 3rem;"></div>

```cpp
if (boolean-expression)
{
    statement(s)-for-the-true-case;
}
else
{
    statement(s)-for-the-false-case;
}
```

</div>
</div>

---
layout: prism
heading: "복습: 논리 연산자"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 여러 조건을 결합하기 위해 [논리 연산자]{.hl}(Boolean operators)를 사용합니다.

<div class="grid grid-cols-3 gap-4" style="margin-top: 1.5rem;">
<div>

| 연산자 | 이름 | 의미 |
|----|------|---------|
| `!` | not | 부정 |
| `&&` | and | 논리곱 |
| `\|\|` | or | 논리합 |

</div>
<div>

| `p1` | `p2` | `p1 && p2` |
|------|------|-----------|
| false | false | false |
| false | true | false |
| true | false | false |
| true | true | true |

</div>
<div>

| `p1` | `p2` | `p1 \|\| p2` |
|------|------|-----------|
| false | false | false |
| false | true | true |
| true | false | true |
| true | true | true |

</div>
</div>

- `!` 연산자는 값을 단순히 뒤집습니다: `age > 18`이 `true`일 때 `!(age > 18)`은 `false`입니다.

---
layout: prism
heading: "실습: 윤년 판별"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 어떤 해가 4로 나누어떨어지지만 100으로는 나누어떨어지지 않거나, **또는** 400으로 나누어떨어지면 [윤년]{.hl}입니다.

- 판별식을 단계별로 쌓아올린 뒤, 모두 하나의 불리언 표현식으로 결합할 수 있습니다.

</div>
<div>

```cpp
// 4로 나누어떨어짐
bool isLeapYear = (year % 4 == 0);
// ... 하지만 100으로는 안 됨
isLeapYear = isLeapYear
           && (year % 100 != 0);
// ... 또는 400으로 나누어떨어짐
isLeapYear = isLeapYear
           || (year % 400 == 0);
```

</div>
</div>

<CppRunner stdin="2000">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter a year: ";
    int year;
    cin >> year;

    bool isLeapYear = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    cout << year << (isLeapYear ? " is" : " is not") << " a leap year." << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "switch 문 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [switch]{.hl} 문은 변수나 표현식의 값에 따라 문장을 실행합니다.

- 중첩된 `if` 문을 남용하면 프로그램을 읽기 어려워집니다.

- C++은 *여러 경우*의 코딩을 단순화하기 위해 `switch` 문을 제공합니다.

</div>
<div>

<div style="height: 2rem;"></div>

```cpp
switch (switch-expression)
{
  case value1: statement(s)1;
               break;
  case value2: statement(s)2;
               break;
  ...
  case valueN: statement(s)N;
               break;
  default:     statement(s)-for-default;
}
```

</div>
</div>

---
layout: prism
heading: "switch 문 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.85em;
}
</style>

- `switch` 문은 다음 규칙을 따릅니다:

  - *switch-expression*은 [정수 값]{.hl}을 산출해야 하며 항상 괄호로 둘러싸여야 합니다.

  - `value1, ..., valueN`은 정수 *상수* 표현식입니다 — 변수(예: `1 + x`)를 포함할 수 없고 부동소수점 값일 수 없습니다.

  - `case` 값이 switch-expression과 일치하면 그 지점부터 실행이 시작되어 `break` 또는 `switch`의 끝에 도달할 때까지 계속됩니다.

  - `default` 케이스는 *선택 사항*이며, 지정된 케이스 중 어느 것도 일치하지 않을 때 실행됩니다.

  - `break` 키워드는 *선택 사항*이지만, 이를 만나면 `switch` 문이 즉시 종료됩니다.

---
layout: prism
heading: "실습: 십이지(띠)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- 연도가 주어졌을 때, `year % 12`로부터 그 해의 동물 띠([Chinese Zodiac]{.hl}, 십이지)를 결정합니다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w04/cpp-w04-image8.png" class="tikz-fig" style="width: 70%;" />

</div>
<div>

<div style="height: 0.5rem;"></div>

| `year % 12` | 띠 | `year % 12` | 띠 |
|:-:|:--|:-:|:--|
| 0 | 원숭이 | 6 | 호랑이 |
| 1 | 닭 | 7 | 토끼 |
| 2 | 개 | 8 | 용 |
| 3 | 돼지 | 9 | 뱀 |
| 4 | 쥐 | 10 | 말 |
| 5 | 소 | 11 | 양 |

</div>
</div>

<CppRunner stdin="1963">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter a year: ";
    int year;
    cin >> year;

    switch (year % 12) {
        case 0:  cout << "monkey"  << endl; break;
        case 1:  cout << "rooster" << endl; break;
        case 2:  cout << "dog"     << endl; break;
        case 3:  cout << "pig"     << endl; break;
        case 4:  cout << "rat"     << endl; break;
        case 5:  cout << "ox"      << endl; break;
        case 6:  cout << "tiger"   << endl; break;
        case 7:  cout << "rabbit"  << endl; break;
        case 8:  cout << "dragon"  << endl; break;
        case 9:  cout << "snake"   << endl; break;
        case 10: cout << "horse"   << endl; break;
        case 11: cout << "sheep"   << endl; break;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "조건 표현식"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [조건 표현식]{.hl}은 조건에 따라 표현식을 평가합니다:

  ```cpp
  boolean-expression ? expr1 : expr2;
  ```

- `?`와 `:`은 함께 [삼항 연산자]{.hl}를 이룹니다 — 세 개의 피연산자를 사용하는, C++의 유일한 삼항 연산자입니다.

</div>
<div>

<div style="height: 1rem;"></div>

```cpp
// if-else 형태
if (x > 0)
    y = 1;
else
    y = -1;

// 동등한 조건 표현식
y = x > 0 ? 1 : -1;
```

</div>
</div>

<CppRunner stdin="-5">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter x: ";
    int x;
    cin >> x;
    int y = x > 0 ? 1 : -1;   // x의 부호
    cout << "y = " << y << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "연산자 우선순위와 결합성 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- 연산자 [우선순위]{.hl}와 [결합성]{.hl}은 연산자가 평가되는 순서를 결정합니다(맨 위가 가장 높음).

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

| 우선순위 | 연산자 |
|:-:|:--|
| 1 | `var++`, `var--` (후위) |
| 2 | `+`, `-` (단항), `++var`, `--var` (전위) |
| 3 | `static_cast<type>(v)`, `(type)` (캐스팅) |
| 4 | `!` (Not) |
| 5 | `*`, `/`, `%` |
| 6 | `+`, `-` (이항) |

</div>
<div>

| 우선순위 | 연산자 |
|:-:|:--|
| 7 | `<`, `<=`, `>`, `>=` (관계) |
| 8 | `==`, `!=` (동등) |
| 9 | `&&` (AND) |
| 10 | `\|\|` (OR) |
| 11 | `=`, `+=`, `-=`, `*=`, `/=`, `%=` (대입) |

</div>
</div>

---
layout: prism
heading: "연산자 우선순위와 결합성 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- *같은* 우선순위의 연산자가 나란히 있을 때는, 그 [결합성]{.hl}이 평가 순서를 결정합니다.

- 대입 연산자를 *제외한* 모든 이항 연산자는 [왼쪽 결합성]{.hl}을 가집니다:

```text
a - b + c - d   is equivalent to   ((a - b) + c) - d
```

- 대입 연산자는 [오른쪽 결합성]{.hl}을 가집니다:

```text
a = b += c = 5   is equivalent to   a = (b += (c = 5))
```

---
layout: prism
heading: "수학 함수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 네 도시의 [GPS 위치]{.hl}가 주어졌을 때, 그 네 도시로 둘러싸인 넓이를 추정해야 한다고 가정해 봅시다.

- 이 문제를 풀려면 프로그램을 어떻게 작성해야 할까요?

- 사각형을 두 개의 삼각형으로 나누어 각 삼각형의 넓이를 추정한 뒤 더합니다.

</div>
<div>

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w04/cpp-w04-image12.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "삼각 함수 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- C++은 흔히 쓰는 수학 작업을 위해 [`<cmath>`]{.hl} 헤더에서 여러 유용한 함수를 제공합니다.

  ```cpp
  #include <cmath>
  ```

<div style="margin-top: 1rem;"></div>

| 함수 | 설명 |
|:--|:--|
| `sin(radians)` | 라디안 단위 각도의 삼각 사인 값을 반환합니다. |
| `cos(radians)` | 라디안 단위 각도의 삼각 코사인 값을 반환합니다. |
| `tan(radians)` | 라디안 단위 각도의 삼각 탄젠트 값을 반환합니다. |
| `asin(a)` | 사인의 역, 즉 라디안 단위 각도를 반환합니다. |
| `acos(a)` | 코사인의 역, 즉 라디안 단위 각도를 반환합니다. |
| `atan(a)` | 탄젠트의 역, 즉 라디안 단위 각도를 반환합니다. |

---
layout: prism
heading: "삼각 함수 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `sin`, `cos`, `tan`의 인자는 [라디안 단위 각도]{.hl}입니다.

- `asin`, `acos`, `atan`의 반환값은 $[-\pi/2, \pi/2]$ 범위의 라디안 단위 각도입니다.

- `PI`는 값이 `3.14159`인 상수라고 가정합니다.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    const double PI = 3.14159;
    cout << sin(0) << endl;              // 0
    cout << sin(270 * PI / 180) << endl; // -1
    cout << sin(PI / 6) << endl;         // 0.5
    cout << cos(0) << endl;              // 1
    cout << asin(0.5) << endl;           // 0.523599
    cout << acos(0.5) << endl;           // 1.0472
    cout << atan(1.0) << endl;           // 0.785398
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "지수 함수 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `<cmath>` 헤더에는 [지수]{.hl}와 관련된 다섯 개의 함수가 있습니다.

<div style="margin-top: 1.5rem;"></div>

| 함수 | 설명 |
|:--|:--|
| `exp(x)` | $e$를 `x` 제곱한 값($e^x$)을 반환합니다. |
| `log(x)` | `x`의 자연로그($\ln x = \log_e x$)를 반환합니다. |
| `log10(x)` | `x`의 상용로그($\log_{10} x$)를 반환합니다. |
| `pow(a, b)` | `a`를 `b` 제곱한 값($a^b$)을 반환합니다. |
| `sqrt(x)` | `x >= 0`에 대해 `x`의 제곱근($\sqrt{x}$)을 반환합니다. |

---
layout: prism
heading: "지수 함수 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- `exp`와 `log`는 서로 역함수이므로, `log(exp(1.0))`은 `1`에 가까운 값을 반환합니다.

- `pow`는 부동소수점 밑과 지수를 받으며, `sqrt`는 음이 아닌 인자를 요구합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    const double E = 2.71828;
    cout << exp(1.0) << endl;   // 2.71828
    cout << log(E) << endl;     // 0.999999
    cout << log10(10.0) << endl;// 1
    cout << pow(2.0, 3) << endl;// 8
    cout << sqrt(4.0) << endl;  // 2
    cout << sqrt(10.5) << endl; // 3.24037
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "반올림 함수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

- `<cmath>` 헤더에는 [반올림]{.hl}을 위한 함수가 들어 있습니다.

| 함수 | 설명 |
|:--|:--|
| `ceil(x)` | `x`를 가장 가까운 정수로 *올림*하여 `double`로 반환합니다. |
| `floor(x)` | `x`를 가장 가까운 정수로 *내림*하여 `double`로 반환합니다. |

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    cout << ceil(2.1)  << endl; // 3
    cout << ceil(-2.1) << endl; // -2
    cout << floor(2.1) << endl; // 2
    cout << floor(-2.1)<< endl; // -3
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "min, max, abs 함수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `min`과 `max`는 두 수(`int`, `long`, `float`, `double`)의 최솟값과 최댓값을 반환합니다.
  - `max(4.4, 5.0)`은 `5.0`을 반환
  - `min(3, 2)`는 `2`를 반환

- `abs`는 수의 [절댓값]{.hl}을 반환합니다.
  - `abs(-2)`는 `2`를 반환
  - `abs(-2.1)`은 `2.1`을 반환

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
using namespace std;

int main() {
    cout << max(4.4, 5.0) << endl; // 5
    cout << min(3, 2)     << endl; // 2
    cout << abs(-2)       << endl; // 2
    cout << abs(-2.1)     << endl; // 2.1
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: 삼각형의 각 구하기 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 삼각형의 세 변이 주어지면, 그 [각]{.hl}을 계산할 수 있습니다.

- 이 공식이 어떻게 유도되는지 **몰라도** 프로그램을 작성할 수 있습니다.

<div style="margin-top: 1rem;"></div>

```text
A = acos((a*a - b*b - c*c) / (-2*b*c))
B = acos((b*b - a*a - c*c) / (-2*a*c))
C = acos((c*c - b*b - a*a) / (-2*a*b))
```

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w04/cpp-w04-image17.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "실습: 삼각형의 각 구하기 (2/2)"
---

<CppRunner stdin="0 0 3 0 0 4">

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    // 사용자에게 세 점을 입력받음
    cout << "Enter three points: ";
    double x1, y1, x2, y2, x3, y3;
    cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    // 세 변을 계산
    double a = sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3));
    double b = sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3));
    double c = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));

    // 라디안 단위로 세 각을 구함
    double A = acos((a * a - b * b - c * c) / (-2 * b * c));
    double B = acos((b * b - a * a - c * c) / (-2 * a * c));
    double C = acos((c * c - b * b - a * a) / (-2 * a * b));

    // 각을 도(degree) 단위로 출력
    const double PI = 3.14159;
    cout << "The three angles are " << A * 180 / PI << " "
         << B * 180 / PI << " " << C * 180 / PI << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "문자 데이터형"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [문자 데이터형]{.hl}은 *하나의* 문자를 나타냅니다. C++에서 이 자료형은 [`char`]{.hl}입니다.

- 문자 리터럴은 **작은**따옴표로 둘러쌉니다:

  ```cpp
  char letter = 'A';
  char numChar = '4';
  ```

- *문자열* 리터럴은 반드시 **큰**따옴표(`" "`)로 둘러싸야 하며, *문자* 리터럴은 작은따옴표(`' '`)를 사용합니다.
  - `"A"`는 문자열이고, `'A'`는 문자입니다.

---
layout: prism
heading: "ASCII 코드"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 컴퓨터는 내부적으로 이진수로 동작하므로, 문자는 0과 1의 나열로 저장됩니다.

- 대부분의 컴퓨터는 문자, 숫자, 문장 부호, 제어 문자를 위한 8비트 인코딩인 [ASCII]{.hl}(American Standard Code for Information Interchange)를 사용합니다.
  - 대부분의 시스템에서 `char`는 1바이트입니다.

| 문자 | ASCII 코드 |
|:--|:--|
| `'0'` ~ `'9'` | 48 ~ 57 |
| `'A'` ~ `'Z'` | 65 ~ 90 |
| `'a'` ~ `'z'` | 97 ~ 122 |

</div>
<div>

<div style="height: 1rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    char ch = 'a';
    cout << "ch      = " << ch << endl;   // a
    cout << "ASCII   = " << (int)ch << endl; // 97
    cout << "++ch    = " << ++ch << endl; // b
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "이스케이프 시퀀스"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

- C++은 특수 문자를 나타내기 위해 [이스케이프 시퀀스]{.hl}라는 특별한 표기법을 사용합니다: 역슬래시 `\` 뒤에 문자나 숫자가 옵니다.

| 이스케이프 | 이름 | ASCII |
|:--|:--|:--|
| `\b` | Backspace | 8 |
| `\t` | Tab | 9 |
| `\n` | Linefeed | 10 |
| `\f` | Formfeed | 12 |
| `\r` | Carriage Return | 13 |
| `\\` | Backslash | 92 |
| `\"` | Double Quote | 34 |

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Tab:" << '\t' << "ending" << endl;
    cout << "Newline:" << '\n' << "ending" << endl;
    cout << "Backslash: " << '\\' << "ending" << endl;
    cout << "Quote: " << '\"' << "ending" << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "char와 수치형 간의 캐스팅 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- `char`는 어떤 수치형으로든 캐스팅할 수 있으며, 그 반대도 가능합니다.

- 정수가 `char`로 캐스팅될 때는 하위 8비트만 사용됩니다:

  ```cpp
  char c = 0XFF41; // 'A', 하위 8비트(0x41 = 65)가 대입되기 때문
  ```

- 부동소수점 값이 `char`로 캐스팅될 때는 먼저 `int`로 캐스팅됩니다:

  ```cpp
  char c = 65.25;  // 'A', 65가 대입되기 때문
  ```

- `char`가 수치형으로 캐스팅될 때는 그 문자의 [ASCII 코드]{.hl}가 사용됩니다:

  ```cpp
  int i = 'A';     // i는 65, 'A'의 ASCII 코드
  ```

---
layout: prism
heading: "char와 수치형 간의 캐스팅 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `char` 자료형은 바이트 크기의 정수처럼 취급되므로, 모든 수치 연산자를 `char` 피연산자에 적용할 수 있습니다.

- `char` 피연산자는 다른 피연산자가 숫자일 때 자동으로 숫자로 캐스팅됩니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    // '2'의 ASCII는 50, '3'은 51
    int i = '2' + '3';   // 101
    cout << "i = " << i << endl;

    // 'a'의 ASCII는 97
    int j = 2 + 'a';     // 99
    cout << "j = " << j << endl;
    cout << static_cast<char>(j) << endl; // 'c'
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: 대문자로 변환"
---

- 소문자 하나를 입력받아 [ASCII 오프셋]{.hl} `'A' + (letter - 'a')`을 이용해 대문자로 변환합니다.

<CppRunner stdin="b">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter a lowercase letter: ";
    char lowercaseLetter;
    cin >> lowercaseLetter;

    char uppercaseLetter =
        static_cast<char>('A' + (lowercaseLetter - 'a'));

    cout << "The corresponding uppercase letter is "
         << uppercaseLetter << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "문자 비교와 검사"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 두 문자는 숫자처럼 관계 연산자로 비교할 수 있으며 — 이는 그들의 [ASCII 코드]{.hl}를 비교하는 것입니다.
  - `'a' < 'b'`는 `true` (97 < 98)
  - `'a' < 'A'`는 `false` (97 > 65)
  - `'1' < '8'`는 `true` (49 < 56)

- 간단한 *문자 판별기*를 만들어 봅시다.

</div>
<div>

<CppRunner stdin="H">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter a character: ";
    char ch;
    cin >> ch;

    if (ch >= 'A' && ch <= 'Z')
        cout << ch << " is uppercase" << endl;
    else if (ch >= 'a' && ch <= 'z')
        cout << ch << " is lowercase" << endl;
    else
        cout << ch << " is not a letter" << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: 랜덤 문자 출력"
---

- 시작 문자와 끝 문자를 입력받은 뒤, `rand()`로 그 범위 안의 랜덤 문자를 출력합니다.

<CppRunner stdin="a z">

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    cout << "Enter a starting character: ";
    char startChar;
    cin >> startChar;

    cout << "Enter an ending character: ";
    char endChar;
    cin >> endChar;

    // 랜덤 문자 얻기
    char randomChar = static_cast<char>(startChar + rand() %
                (endChar - startChar + 1));

    cout << "The random character between " << startChar << " and "
         << endChar << " is " << randomChar << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "문자 함수"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- C++은 [`<cctype>`]{.hl} 헤더에서 문자를 *검사*하고 *변환*하는 함수를 제공합니다. 검사 함수는 `true` 또는 `false`를 반환합니다.

  ```cpp
  #include <cctype>
  ```

<div class="grid grid-cols-2 gap-6" style="margin-top: 0.8rem;">
<div>

| 함수 | 설명 |
|:--|:--|
| `isdigit(ch)` | `ch`가 숫자면 true |
| `isalpha(ch)` | `ch`가 문자면 true |
| `isalnum(ch)` | `ch`가 문자 또는 숫자면 true |
| `islower(ch)` | `ch`가 소문자면 true |

</div>
<div>

| 함수 | 설명 |
|:--|:--|
| `isupper(ch)` | `ch`가 대문자면 true |
| `isspace(ch)` | `ch`가 공백 문자면 true |
| `tolower(ch)` | `ch`의 소문자를 반환 |
| `toupper(ch)` | `ch`의 대문자를 반환 |

</div>
</div>

---
layout: prism
heading: "실습: 16진 숫자를 10진 숫자로"
---

<CppRunner stdin="B">

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    cout << "Enter a hex digit: ";
    char hexDigit;
    cin >> hexDigit;

    hexDigit = toupper(hexDigit);
    if (hexDigit <= 'F' && hexDigit >= 'A') {
        int value = 10 + hexDigit - 'A';
        cout << "The decimal value for hex digit "
             << hexDigit << " is " << value << endl;
    }
    else if (isdigit(hexDigit)) {
        cout << "The decimal value for hex digit "
             << hexDigit << " is " << hexDigit << endl;
    }
    else {
        cout << hexDigit << " is an invalid input" << endl;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY_W04: 20진 숫자를 10진수로"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- **한 자리 20진수**를 입력받아 10진수로 변환합니다(`0`-`9`, `A`-`J` → `0`-`19`).

- 만약 *소문자*가 입력되면, 대문자로 자동 변환되었음을 알리는 경고를 출력합니다.

</div>
<div>

<div style="height: 0.5rem;"></div>

실행 예시:

```text
Input:  A
Output: base-20 'A' is 10 in decimal.

Input:  g
Output: 'g' was auto-converted to 'G'.
        'G' is 16 in decimal.
```

</div>
</div>

<CppRunner stdin="g">

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    cout << "Enter a base-20 digit: ";
    char digit;
    cin >> digit;

    if (islower(digit)) {
        char upper = toupper(digit);
        cout << "'" << digit << "' was auto-converted to '" << upper << "'." << endl;
        digit = upper;
    }

    if (isdigit(digit))
        cout << "base-20 '" << digit << "' is " << (digit - '0') << " in decimal." << endl;
    else if (digit >= 'A' && digit <= 'J')
        cout << "'" << digit << "' is " << (10 + digit - 'A') << " in decimal." << endl;
    else
        cout << "'" << digit << "' is an invalid base-20 digit." << endl;
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
