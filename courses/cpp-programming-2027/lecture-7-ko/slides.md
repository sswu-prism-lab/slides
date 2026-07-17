---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 7 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-7/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">7주차: 중간 리뷰</p>

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
heading: 중간 리뷰
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 이번 주에는 지금까지 다룬 핵심적인 [제어 흐름]{.hl}과 자료형 개념을 [복습]{.hl}하고, [중간고사]{.hl}를 미리 살펴봅니다:

  - [선택]{.hl}: `if-else`, 논리 연산자, `switch`, 그리고 조건(삼항) 표현식.

  - [자료]{.hl}: 수학 함수, `char`, `string`, 그리고 스트림 조작자.

  - [반복]{.hl}: `while`, `do-while`, `for` 루프.

- 마지막으로 대표적인 [중간고사 문제]{.hl}들(약 15문항, 30점)을 함께 풀어봅니다.

---
layout: prism
heading: "복습: if-else 문"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [예/아니오 결정]{.hl}은 C++에서 [`true`/`false`]{.hl} 값으로 표현됩니다.
  - [논리 표현식]{.hl}은 그 조건이 만족되면 `true`, 그렇지 않으면 `false`로 평가됩니다.
  - C++에서 `true`와 `false`는 [예약어]{.hl}입니다.

```text
if (boolean-expression) {
    statement(s)-for-the-true-case;
} else {
    statement(s)-for-the-false-case;
}
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int score = 72;
    if (score >= 60)
        cout << "Pass" << endl;
    else
        cout << "Fail" << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: 논리 연산자"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- C++은 불리언 값을 결합하거나 부정하기 위한 세 가지 [논리 연산자]{.hl}를 제공합니다.

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

| 연산자 | 이름 | 설명 |
|:--------:|:----:|:------------|
| `!` | not | 논리 부정 |
| `&&` | and | 논리곱 |
| `\|\|` | or | 논리합 |

</div>
<div>

| `p1` | `p2` | `p1 && p2` | `p1 \|\| p2` |
|:----:|:----:|:----------:|:-----------:|
| false | false | false | false |
| false | true  | false | true  |
| true  | false | false | true  |
| true  | true  | true  | true  |

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 24, weight = 140;
    cout << boolalpha;
    cout << (age > 18 && weight == 150) << endl; // false
    cout << (age > 18 || weight == 150) << endl; // true
    cout << !(age > 18) << endl;                 // false
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: switch 문"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [`switch`]{.hl} 문은 하나의 표현식을 기준으로 여러 분기 중 하나를 선택합니다. 각 `case`는 보통 [`break`]{.hl}로 끝나며, [`default`]{.hl}가 나머지 경우를 처리합니다.

```text
switch (switch-expression) {
    case value1: statement(s)1; break;
    case value2: statement(s)2; break;
    ...
    case valueN: statement(s)N; break;
    default:     statement(s)-for-default;
}
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int day = 3;
    switch (day) {
        case 1: cout << "Mon"; break;
        case 2: cout << "Tue"; break;
        case 3: cout << "Wed"; break;
        default: cout << "Other";
    }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: 조건 표현식"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [조건 표현식]{.hl}은 `boolean-expression ? expression1 : expression2` 형태의 문법을 가집니다.
  - `?`와 `:`는 [삼항 연산자]{.hl}를 이룹니다 — [세 개의 피연산자]{.hl}를 취합니다.
  - C++에서 [유일한]{.hl} 삼항 연산자입니다.

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

```cpp
if (x > 0)
    y = 1;
else
    y = -1;
```

</div>
<div>

```cpp
y = x > 0 ? 1 : -1;
```

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = -4;
    int y = x > 0 ? 1 : -1;
    cout << "y = " << y << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: 수학 함수"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- `min`, `max`, `abs`는 [`cstdlib`]{.hl} 헤더에 있으며, 삼각함수·지수·반올림 함수는 [`cmath`]{.hl} 헤더에 있습니다.

| 함수 | 설명 | 함수 | 설명 |
|:---------|:------------|:---------|:------------|
| `sin/cos/tan(x)` | 삼각함수 (라디안) | `pow(a, b)` | $a^b$ |
| `asin/acos/atan(x)` | 역삼각함수 | `sqrt(x)` | $\sqrt{x}$, $x \ge 0$ |
| `exp(x)` | $e^x$ | `ceil(x)` | 올림 (`double` 형) |
| `log(x)` / `log10(x)` | $\ln x$ / $\log_{10} x$ | `floor(x)` | 내림 (`double` 형) |

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    cout << sqrt(16.0) << endl;   // 4
    cout << pow(2.0, 10) << endl; // 1024
    cout << ceil(3.2) << " " << floor(3.8) << endl; // 4 3
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: 문자"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 대부분의 컴퓨터는 8비트 방식인 [ASCII]{.hl}(American Standard Code for Information Interchange)를 사용하며, `char`의 크기는 [1바이트]{.hl}입니다. `char`는 작은 정수처럼 동작합니다: `char ch = 'a'; cout << ++ch;`는 `b`를 출력합니다.

| 함수 | 설명 | 함수 | 설명 |
|:---------|:------------|:---------|:------------|
| `isdigit(ch)` | 숫자인가 | `isupper(ch)` | 대문자인가 |
| `isalpha(ch)` | 문자인가 | `isspace(ch)` | 공백 문자인가 |
| `isalnum(ch)` | 문자 또는 숫자인가 | `tolower(ch)` | 소문자로 변환 |
| `islower(ch)` | 소문자인가 | `toupper(ch)` | 대문자로 변환 |

<CppRunner>

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char ch = 'a';
    cout << ++ch << endl;                 // b
    cout << (char)toupper('c') << endl;   // C
    cout << isdigit('7') << endl;         // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: string 타입"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [`string`]{.hl}은 문자들의 시퀀스를 나타냅니다: `string message = "Programming is fun";`.
  - `string`은 원시 타입이 아니라 [객체 타입]{.hl}입니다.
  - 관계 연산자 `==`, `!=`, `<`, `<=`, `>`, `>=`로 두 문자열을 비교합니다.

| 함수 | 설명 |
|:---------|:------------|
| `length()` | 문자열의 문자 개수 |
| `size()`   | `length()`와 동일 |
| `at(index)` | 주어진 인덱스의 문자 |

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string message = "Programming is fun";
    cout << message.length() << endl;   // 18
    cout << message.at(0) << endl;      // P
    cout << ("apple" < string("banana")) << endl; // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: 조작자"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- C++은 값이 표시되는 방식을 제어하기 위한 [스트림 조작자]{.hl}를 제공합니다.

| 연산자 | 설명 |
|:---------|:------------|
| `setprecision(n)` | 부동소수점 수의 정밀도를 설정 |
| `fixed` | 부동소수점 수를 고정소수점 표기로 표시 |
| `showpoint` | 소수점과 뒤따르는 0을 표시 |
| `setw(width)` | 출력 필드의 너비를 지정 |
| `left` / `right` | 출력을 왼쪽 / 오른쪽 정렬 |

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << fixed << setprecision(2) << 3.14159 << endl; // 3.14
    cout << setw(6) << right << 42 << endl;              // "    42"
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: while 루프"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [`while`]{.hl} 루프는 [조건이 참인 동안]{.hl} 본문을 반복 실행합니다. 본문의 한 번 실행을 [반복(iteration)]{.hl}이라고 부릅니다.

```text
while (loop-continuation-condition) {
    // Loop body
    Statement(s);
}
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 0;
    while (count < 3) {
        cout << "Welcome to C++!\n";
        count++;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: do-while 루프"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [`do-while`]{.hl} 루프는 `while` 루프와 비슷하지만, [본문을 먼저 실행]{.hl}한 뒤 루프 계속 조건을 검사합니다 — 따라서 본문은 항상 최소 한 번은 실행됩니다.

```text
do {
    // Loop body
    Statement(s);
} while (loop-continuation-condition);
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;
    do {
        cout << n << " ";
        n--;
    } while (n > 0);
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: for 루프"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [`for`]{.hl} 루프는 [초기 동작]{.hl}, [계속 조건]{.hl}, 그리고 [매 반복 이후의 동작]{.hl}을 하나의 헤더에 모아 간결한 문법을 제공합니다.

```text
for (initial-action; loop-continuation-condition; action-after-each-iteration) {
    // Loop body
    Statement(s);
}
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    for (int i = 1; i <= 10; i++)
        sum += i;
    cout << "sum = " << sum << endl; // 55
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "중간고사 (1/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 시험은 [30점]{.hl}, 약 [15문항]{.hl}으로 구성되며 한국어로 출제됩니다.

<div class="theorem-box">
<div class="theorem-box-title">O-X 퀴즈</div>
<div class="theorem-box-body">

1. 조건 표현식 `boolean-expression ? a : b`는 C++에서 유일한 삼항 연산자이다.  ( &nbsp;&nbsp; )
2. `return`은 변수명으로 사용할 수 있다.  ( &nbsp;&nbsp; )

</div>
</div>

<div class="theorem-box">
<div class="theorem-box-title">출력 결과 예측</div>
<div class="theorem-box-body">

```cpp
cout << 'a' + 3 << endl;
cout << static_cast<int>('a' + 7) << endl;
cout << 2 * (3 / 6) + 4 << endl;
int a = 4 < 3 ? 1 : 0;
int b;
if (a) { b = 1; } else { b = 30; }
cout << b << endl;
```

</div>
</div>

---
layout: prism
heading: "중간고사 (1/7) — 풀이"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [O-X]{.hl}: (1) **O** — 삼항 연산자는 C++에서 유일하게 세 개의 피연산자를 취하는 연산자이다.  (2) **X** — `return`은 예약어이므로 식별자로 사용할 수 없다.

- [출력]{.hl}: `'a'`는 `97`이므로 `'a'+3 = 100`; `'a'+7 = 104`; 정수 나눗셈 `3/6 = 0`이므로 `2*0+4 = 4`; `4<3`은 거짓이라 `a=0`, 따라서 `b=30`.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << 'a' + 3 << endl;                       // 100
    cout << static_cast<int>('a' + 7) << endl;     // 104
    cout << 2 * (3 / 6) + 4 << endl;               // 4
    int a = 4 < 3 ? 1 : 0;                         // a = 0
    int b;
    if (a) { b = 1; } else { b = 30; }
    cout << b << endl;                             // 30
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "중간고사 (2/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [선택문과 반복문의 활용]{.hl}: 각 작업에 대해 의사 알고리즘(pseudo-algorithm)을 작성하시오.

<div class="theorem-box">
<div class="theorem-box-title">의사 알고리즘 문제</div>
<div class="theorem-box-body">

1. 세 정수를 입력받아 [오름차순]{.hl}으로 출력하시오.
2. 두 정수를 입력받아 [최소공배수(LCM)]{.hl}를 구하시오.
3. 정수 $n$ ($1 \le n \le 15$)을 입력받아, `n = 7`일 때 아래와 같이 [숫자 피라미드]{.hl}를 출력하시오.

```text
Enter the number of lines: 7
            1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
  6 5 4 3 2 1 2 3 4 5 6
7 6 5 4 3 2 1 2 3 4 5 6 7
```

</div>
</div>

---
layout: prism
heading: "중간고사 (2/7) — 세 정수 정렬"
---

<CppRunner stdin="7 3 5">

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    // 두 값씩 교환하여 오름차순 정렬
    if (a > b) { int t = a; a = b; b = t; }
    if (a > c) { int t = a; a = c; c = t; }
    if (b > c) { int t = b; b = c; c = t; }

    cout << a << " " << b << " " << c << endl; // 3 5 7
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "중간고사 (2/7) — 최소공배수"
---

<CppRunner stdin="4 6">

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    // 최대공약수를 구하는 유클리드 호제법
    int x = a, y = b;
    while (y != 0) {
        int r = x % y;
        x = y;
        y = r;
    }
    int gcd = x;
    int lcm = a / gcd * b;

    cout << "LCM = " << lcm << endl; // 12
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "중간고사 (2/7) — 숫자 피라미드"
---

<CppRunner stdin="7">

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int row = 1; row <= n; row++) {
        for (int col = 1; col <= n - row; col++)
            cout << "   ";                 // 앞쪽 공백
        for (int num = row; num >= 1; num--)
            cout << setw(3) << num;        // 내림차순 부분
        for (int num = 2; num <= row; num++)
            cout << setw(3) << num;        // 오름차순 부분
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "중간고사 (3/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [`break`와 `continue`의 활용]{.hl}: 아래 코드를 추적하시오. `continue`일 때 무엇이 출력되는가? `continue`를 `break`로 바꾸면 어떻게 되는가?

<div class="theorem-box">
<div class="theorem-box-title">루프 추적하기</div>
<div class="theorem-box-body">

```cpp
int main() {
    int sum = 0, num = 0;
    while (num < 20) {
        num++;
        if (num % 2 == 0 && num % 3 == 0) {
            continue; // break;
        }
        sum += num;
    }
    cout << sum << endl;
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: "중간고사 (3/7) — 풀이"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 조건 `num % 2 == 0 && num % 3 == 0`은 `num`이 [6]{.hl}의 배수일 때(`6, 12, 18`)만 참이 됩니다.
  - [`continue`]{.hl}인 경우: 이 세 값이 건너뛰어지므로 `sum = (1+...+20) - (6+12+18) = 210 - 36 = ` **174**.
  - [`break`]{.hl}인 경우: 6의 첫 배수(`num = 6`)에서 루프가 멈추므로 `sum = 1+2+3+4+5 = ` **15**.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int sumC = 0, sumB = 0, num;

    num = 0;
    while (num < 20) {          // continue 버전
        num++;
        if (num % 2 == 0 && num % 3 == 0) continue;
        sumC += num;
    }

    num = 0;
    while (num < 20) {          // break 버전
        num++;
        if (num % 2 == 0 && num % 3 == 0) break;
        sumB += num;
    }

    cout << "continue -> " << sumC << endl; // 174
    cout << "break    -> " << sumB << endl; // 15
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "중간고사 (4/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [자료형과 형 변환]{.hl}: `int`, `double`, `bool`, `char`, `string`. 아래 오류를 찾아 수정하시오.

<div class="theorem-box">
<div class="theorem-box-title">(a) 컴파일 오류</div>
<div class="theorem-box-body">

```cpp
string message = 'Welcome to C++!'
```

</div>
</div>

<div class="theorem-box">
<div class="theorem-box-title">(b) 컴파일은 되지만 논리적으로 잘못됨 — 0.01, 0.02, ..., 0.99, 1의 합</div>
<div class="theorem-box-body">

```cpp
double sum = 0;
for (double i = 0.01; i <= 1.0; i = i + 0.01)
    sum += i;
cout << "The sum is " << sum << endl;
```

</div>
</div>

---
layout: prism
heading: "중간고사 (4/7) — 풀이"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [(a)]{.hl} `string` 리터럴에는 [큰따옴표]{.hl}가 필요하며, 문장 끝에는 세미콜론이 필요합니다: `string message = "Welcome to C++!";`.

- [(b)]{.hl} `0.01`은 정확히 표현할 수 없으므로, 누적된 `i`가 `1.0`을 넘어서 마지막 항이 누락될 수 있고 반올림 오차도 커집니다. 대신 [정수 카운터]{.hl}로 반복하세요.

<CppRunner>

```cpp
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
    string message = "Welcome to C++!"; // (a) 수정
    cout << message << endl;

    double sum = 0;                      // (b) 수정: 정수 카운터
    for (int i = 1; i <= 100; i++)
        sum += i / 100.0;
    cout << fixed << setprecision(2)
         << "The sum is " << sum << endl; // 50.50
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "중간고사 (5/7)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [연산자와 평가 순서]{.hl}: 모든 출력 줄을 예측하시오.

<div class="theorem-box">
<div class="theorem-box-title">출력 결과 예측</div>
<div class="theorem-box-body">

```cpp
int a = 10;
cout << a++ << endl;
cout << ++a << endl;
cout << a-- << endl;
cout << --a << endl;
a *= 2;
cout << a << endl;
int b = 20;
bool c;
c = a == b;
cout << c << endl;
b -= 5;
c = !(a < b);
cout << c << endl;
```

</div>
</div>

---
layout: prism
heading: "중간고사 (5/7) — 풀이"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [후위]{.hl} 증가 vs [전위]{.hl} 증가: `a++`는 출력 후 증가하고, `++a`는 증가 후 출력합니다. `a`를 추적하면: `10 → 11 → 12 → 11 → 10`, 이후 `a *= 2 → 20`.
  - `a == b`는 `20 == 20 → 1`이고, `b -= 5`(`b = 15`) 이후 `!(20 < 15) → !false → 1`.
- [출력]{.hl}: `10`, `12`, `12`, `10`, `20`, `1`, `1`.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10;
    cout << a++ << endl;  // 10
    cout << ++a << endl;  // 12
    cout << a-- << endl;  // 12
    cout << --a << endl;  // 10
    a *= 2;
    cout << a << endl;    // 20
    int b = 20;
    bool c;
    c = a == b;
    cout << c << endl;    // 1
    b -= 5;
    c = !(a < b);
    cout << c << endl;    // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "중간고사 (6/7)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [수학 함수 문제]{.hl} (빈칸 채우기). [정오각형]{.hl}의 중심에서 꼭짓점까지의 길이 $r$을 입력받아 넓이를 계산하는 프로그램을 작성하시오.

$$
\text{Area} = \frac{5 \times s^2}{4 \times \tan\!\left(\dfrac{\pi}{5}\right)}, \quad s = 2r\sin\frac{\pi}{5}
$$

- 소수점 둘째 자리까지 반올림합니다. 예시: `r = 5.5`이면 넓이는 `71.92`.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w07/cpp-w07-image25.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "중간고사 (6/7) — 풀이"
---

<CppRunner stdin="5.5">

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    const double PI = 3.14159265358979323846;
    double r;
    cin >> r;                       // 중심 -> 꼭짓점 길이

    double s = 2 * r * sin(PI / 5); // 변의 길이
    double area = (5 * s * s) / (4 * tan(PI / 5));

    cout << fixed << setprecision(2);
    cout << "The area of the pentagon is " << area << endl; // 71.92
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "중간고사 (7/7)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [몬테카를로 알고리즘]{.hl} (의사 알고리즘 작성 / 빈칸 채우기).

- 정사각형이 네 개의 영역으로 나뉘어 있습니다. 정사각형 안으로 다트를 [1,000,000]{.hl}번 던졌을 때, [홀수 번호 영역]{.hl}(1 또는 3)에 떨어질 확률은 얼마인가요?

- 이 과정을 시뮬레이션하고 결과를 표시하시오.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w07/cpp-w07-image27.png" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "중간고사 (7/7) — 풀이"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.6em;
}
</style>

- 정사각형 안의 한 점을 표본으로 뽑아 그 영역을 분류하고, 홀수 영역에 떨어진 횟수를 셉니다. 예상되는 답은 약 [0.625]{.hl}입니다.

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
#include <iomanip>
using namespace std;

int main() {
    srand(42);
    const int N = 1000000;
    int odd = 0;
    for (int i = 0; i < N; i++) {
        double x = (double)rand() / RAND_MAX * 2.0; // [0, 2]
        double y = (double)rand() / RAND_MAX * 2.0;
        if (x < 1.0)               odd++;       // 영역 1 (왼쪽 절반)
        else if (y >= 1.0 && x + y < 3.0) odd++; // 영역 3 (안쪽 삼각형)
        // 영역 2 (바깥 삼각형)와 영역 4 (오른쪽 아래)는 짝수
    }
    cout << fixed << setprecision(4);
    cout << "Probability (odd region) = " << (double)odd / N << endl;
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
