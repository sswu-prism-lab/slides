---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 3 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-3/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">3주차: 선택문과 조건문</p>

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
heading: 선택문과 조건문
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 프로그램은 종종 상황에 따라 *어떤* 문장을 실행할지 선택해야 합니다. 이번 강의에서는 C++의 [선택문]{.hl}을 공부합니다:

  - [불리언 값]{.hl}과 [관계 연산자]{.hl} — C++이 *참*과 *거짓*을 어떻게 판단하는지.

  - [`if`]{.hl}, [`if-else`]{.hl}, [중첩 `if`]{.hl}, [`switch`]{.hl} 문.

  - [논리 연산자]{.hl}, [조건 표현식]{.hl}, 그리고 연산자의 [우선순위와 결합성]{.hl}.

---
layout: prism
heading: 조건문
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 보통 학생들은 *C++ 프로그래밍* 수업을 듣기 위해 이곳에 옵니다.

- 그런데 어떤 이유로 배우 강하늘이 우리 캠퍼스를 방문한다고 가정해 봅시다.

- 그러면 어떤 학생들은 수업에 *참석하지 않을* 수도 있습니다 — 결과가 [조건에 따라 달라지는]{.hl} 것이죠.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image2.png" class="tikz-fig" style="width: 60%; margin: 0 auto;" />

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image3.png" class="tikz-fig" style="width: 90%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: 판단하기
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 코드를 단순히 순차적으로만 실행하는 것은 지루하고 비효율적입니다.
  - 상황에 따라 *어떤* 문장을 *언제* 실행할지 바꿀 수 있다면 좋을 것입니다.

- 예/아니오 판단으로 많은 것을 할 수 있습니다. 컴퓨터 과학에서는 이를 [참 / 거짓]{.hl}으로 표현합니다.

- 참/거짓은 [논리 데이터]{.hl}와 [논리 연산자]{.hl}로 결정합니다.
  - 논리 데이터가 어떤 조건을 만족하면 *참*으로, 그렇지 않으면 *거짓*으로 봅니다.

- C++에서 [`true`]{.hl}와 [`false`]{.hl}는 예약어입니다.

---
layout: prism
heading: 산술 척도에서의 참과 거짓
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- C++에서 [0]{.hl} 값은 논리값 `false`로 사용할 수 있습니다.

- [0이 아닌]{.hl} 어떤 값(예: `-1`, `18`, `3.5`)도 논리값 `true`로 사용할 수 있습니다.

- 오른쪽의 각 변수를 `bool`로 변환해 보세요.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int   a = 3;     // 참
    int   b = 0;     // 거짓
    float c = 0.0;   // 거짓
    float d = 2.9;   // 참
    bool  e = true;  // 참
    bool  f = false; // 거짓
    bool  g = 1.4;   // 참
    bool  h = 0;     // 거짓

    cout << boolalpha;
    cout << "a=" << (bool)a << "  b=" << (bool)b << "\n";
    cout << "c=" << (bool)c << "  d=" << (bool)d << "\n";
    cout << "e=" << e << "  f=" << f << "\n";
    cout << "g=" << g << "  h=" << h << "\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: 관계 연산자
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 두 값을 비교하여 [참 / 거짓]{.hl}을 판단할 때는 [관계 연산자]{.hl}(관계 연산자)를 사용합니다.

<div style="margin-top: 1rem;"></div>

| 연산자 | 수학 기호 | 이름 | 예시 (`radius`는 5) | 결과 |
|:---:|:---:|:---|:---|:---:|
| `<`  | &lt; | 미만 | `radius < 0`  | false |
| `<=` | ≤ | 이하 | `radius <= 0` | false |
| `>`  | &gt; | 초과 | `radius > 0`  | true |
| `>=` | ≥ | 이상 | `radius >= 0` | true |
| `==` | = | 같음 | `radius == 0` | false |
| `!=` | ≠ | 같지 않음 | `radius != 0` | true |

- 같음을 검사하는 기호는 [`==`]{.hl}이며 `=`가 **아닙니다**. C++에서 `=`는 [대입]{.hl}에 사용됩니다.

---
layout: prism
heading: 불리언 값
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 불리언 값은 참인 경우 [`1`]{.hl}로, 거짓인 경우 [`0`]{.hl}으로 표시됩니다.

- `x`에 `1`을 대입하고 각 비교의 결과를 확인해 봅시다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 1;
    cout << (x > 0)  << endl;  // 1
    cout << (x < 0)  << endl;  // 0
    cout << (x != 0) << endl;  // 1
    cout << (x >= 0) << endl;  // 1
    cout << (x != 1) << endl;  // 0

    cout << (4 < 5) << endl;   // 1 출력
    cout << (4 > 5) << endl;   // 0 출력
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "if 문 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [`if`]{.hl} 문은 프로그램이 *대안적인 실행 경로*를 지정할 수 있게 합니다.

- [단방향 `if`]{.hl} 문은 조건이 `true`일 *때에만* 동작을 실행합니다.

```cpp
if (boolean-expression)
{
    statement(s);
}
```

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image6.png" class="tikz-fig" style="width: 75%; margin: 0 auto;" />

<div class="sub-item" style="text-align:center; margin-top: 0.6rem;">

단방향 `if` 문의 흐름.

</div>

</div>
</div>

---
layout: prism
heading: "if 문 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

boolean-expression은 반드시 [괄호]{.hl}로 감싸야 합니다.

```cpp
// (a) 잘못됨
if i > 0
{
    cout << "i is positive" << endl;
}

// (b) 올바름
if (i > 0)
{
    cout << "i is positive" << endl;
}
```

</div>
<div>

중괄호는 *단일* 문장을 감쌀 경우 [생략]{.hl}할 수 있습니다.

```cpp
// (a) 중괄호 사용
if (i > 0)
{
    cout << "i is positive" << endl;
}

// (b) 동일함, 중괄호 생략
if (i > 0)
    cout << "i is positive" << endl;
```

</div>
</div>

---
layout: prism
heading: "if 문 (3/3)"
---

<div style="height: 0.3rem;"></div>

<CppRunner stdin="10">

```cpp
#include <iostream>   // SimpleIfDemo.cpp
using namespace std;

int main() {
    // 사용자에게 정수를 입력하도록 안내
    int number;
    cout << "Enter an integer: ";
    cin >> number;

    if (number % 5 == 0)
        cout << "HiFive" << endl;

    if (number % 2 == 0)
        cout << "HiEven" << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "if-else 문 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [`if-else`]{.hl} 문은 조건이 `true`인지 `false`인지에 따라 어떤 문장을 실행할지 결정합니다.

- [양방향 `if-else`]{.hl} 문은 두 경우에 대해 *서로 다른* 동작을 지정합니다.

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
<div>

<div style="height: 4rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image11.png" class="tikz-fig" style="width: 100%; margin: 0 auto;" />

<div class="sub-item" style="text-align:center; margin-top: 0.6rem;">

양방향 `if-else` 문의 흐름.

</div>

</div>
</div>

---
layout: prism
heading: "if-else 문 (2/2)"
---

<div style="height: 0.3rem;"></div>

- 어떤 수가 [짝수인지 홀수인지]{.hl}를 검사하는 간단한 프로그램을 작성해 봅시다 — `SimpleIfDemo.cpp`의 중간 부분만 바꾸면 됩니다.

<CppRunner stdin="7">

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;
    cout << "Enter an integer: ";
    cin >> number;

    if (number % 2 == 0)
        cout << number << " is even.";
    else
        cout << number << " is odd.";

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "중첩 if와 다중 분기 if-else (1/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- `if` 문은 다른 `if` 문 안에 넣어 [중첩 `if`]{.hl}(중첩 if) 문을 만들 수 있습니다.

- `if`나 `if-else` 안의 문장은 또 다른 `if`나 `if-else`를 포함해 *어떤* 합법적인 C++ 문장이든 될 수 있습니다.

</div>
<div>

<div style="height: 2.5rem;"></div>

```cpp
if (i > k)
{
    if (j > k)
        cout << "i and j are greater than k"
             << endl;
}
else
    cout << "i is less than or equal to k"
         << endl;
```

</div>
</div>

---
layout: prism
heading: "중첩 if와 다중 분기 if-else (2/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

깊게 중첩된 형태 (읽기 어려움):

```cpp
if (score >= 90.0)
    cout << "Grade is A";
else
    if (score >= 80.0)
        cout << "Grade is B";
    else
        if (score >= 70.0)
            cout << "Grade is C";
        else
            if (score >= 60.0)
                cout << "Grade is D";
            else
                cout << "Grade is F";
```

</div>
<div>

[다중 분기]{.hl} 형태 (**권장**):

```cpp
if (score >= 90.0)
    cout << "Grade is A";
else if (score >= 80.0)
    cout << "Grade is B";
else if (score >= 70.0)
    cout << "Grade is C";
else if (score >= 60.0)
    cout << "Grade is D";
else
    cout << "Grade is F";
```

</div>
</div>

---
layout: prism
heading: "중첩 if와 다중 분기 if-else (3/4)"
---

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image15.png" class="tikz-fig" style="width: 82%;" />
</div>

<div class="sub-item" style="text-align:center; margin-top: 0.8rem;">

문자 등급을 부여하는 데 사용된 다중 분기 `if-else` 문.

</div>

---
layout: prism
heading: "중첩 if와 다중 분기 if-else (4/4)"
---

<div style="height: 0.2rem;"></div>

- **직접 해보기.** `x = 3`, `y = 4`일 때 아래 코드를 추적해 보세요. `x = 3, y = 2`일 때 출력은 무엇인가요? `x = 2, y = 2`일 때는요?

<CppRunner stdin="3 4">

```cpp
#include <iostream>
using namespace std;

int main() {
    int x, y;
    cin >> x >> y;

    if (x > 2)
    {
        if (y > 2)
        {
            int z = x + y;
            cout << "z is " << z << endl;
        }
    }
    else
        cout << "x is " << x << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "흔한 오류와 함정 (1/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 흔한 오류: 필요한 [중괄호]{.hl} 빠뜨리기, [세미콜론]{.hl} 잘못 놓기, [`==`를 `=`로]{.hl} 착각하기, [매달린 `else`]{.hl}(else 결합) 절.

- 흔한 함정: `if-else`에서 [중복된 문장]{.hl}, 그리고 [`double`의 동등성 검사]{.hl}.

</div>
<div>

필요한 중괄호 빠뜨리기:

```cpp
// (a) 잘못됨 — 첫 줄만 보호됨
if (radius >= 0)
    area = radius * radius * PI;
    cout << "The area is " << area;

// (b) 올바름
if (radius >= 0)
{
    area = radius * radius * PI;
    cout << "The area is " << area;
}
```

</div>
</div>

---
layout: prism
heading: "흔한 오류와 함정 (2/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

`if` 줄에 잘못된 세미콜론:

```cpp
// 논리 오류: 본문이 비어 있고, {}는 항상 실행됨
if (radius >= 0);
{
    area = radius * radius * PI;
    cout << "The area is " << area;
}
```

</div>
<div>

`==` 대신 `=`를 실수로 사용:

```cpp
// (=) count에 3을 대입하므로 항상 참!
if (count = 3)
    cout << "count is zero" << endl;
else
    cout << "count is not zero" << endl;

// 올바름:  if (count == 3)
```

</div>
</div>

---
layout: prism
heading: "흔한 오류와 함정 (3/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

불리언 값을 중복 검사하기:

```cpp
// (a) 불필요함
if (even == true)
    cout << "It is even.";

// (b) 더 나음
if (even)
    cout << "It is even.";
```

- `else`는 들여쓰기가 아니라 짝이 없는 [가장 가까운]{.hl} `if`에 결합됩니다.

</div>
<div>

매달린 `else`:

```cpp
int i = 1, j = 2, k = 3;

// else는 실제로 두 번째 if에 결합됨
if (i > j)
    if (i > k)
        cout << "A";
    else
        cout << "B";

// else를 첫 번째 if에 강제로 결합:
if (i > j)
{
    if (i > k)
        cout << "A";
}
else
    cout << "B";
```

</div>
</div>

---
layout: prism
heading: "흔한 오류와 함정 (4/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 부동소수점 수는 [정밀도가 제한적]{.hl}이며, 계산 과정에서 반올림 오차가 생길 수 있으므로 두 `double` 값의 동등성 검사는 [신뢰할 수 없습니다]{.hl}.

- 대신 두 수의 차이가 작은 [임계값]{.hl}보다 작은지 검사하세요. `<cmath>`의 `fabs` / `abs`는 절댓값을 반환합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x = 1.0 - 0.1 - 0.1 - 0.1 - 0.1 - 0.1;

    // 직접 동등성 비교는 신뢰할 수 없음
    if (x == 0.5) cout << "x is 0.5\n";
    else          cout << "x is not 0.5\n";

    // 신뢰할 수 있는 임계값 비교
    const double EPSILON = 1E-14;
    if (fabs(x - 0.5) < EPSILON)
        cout << "x is approximately 0.5\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "흔한 오류와 함정 (5/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

불리언 대입 단순화하기:

```cpp
// (a) 장황함
if (number % 2 == 0)
    even = true;
else
    even = false;

// (b) 더 나음
bool even = number % 2 == 0;
```

</div>
<div>

중복 코드 피하기 — [DRY]{.hl} ("don't repeat yourself"):

```cpp
// (a) cout 중복
if (inState) {
    tuition = 5000;
    cout << "The tuition is " << tuition << endl;
} else {
    tuition = 15000;
    cout << "The tuition is " << tuition << endl;
}

// (b) 한 번만 출력
if (inState) tuition = 5000;
else         tuition = 15000;
cout << "The tuition is " << tuition << endl;
```

</div>
</div>

---
layout: prism
heading: "흔한 오류와 함정 (6/6)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- C++에서는 수치 값을 불리언으로 사용할 수 있는데, 이는 [논리 오류]{.hl}를 유발할 수 있습니다.

- `amount`가 `40`이면 아래 코드는 *"Amount is more than 50"*을 출력합니다. `!amount`가 `0`으로 평가되고 `0 <= 50`이 `true`이기 때문입니다.

- 부정(`!`) 연산자는 `true`↔`false`를 반전시킵니다.

</div>
<div>

```cpp
// 잘못됨: !amount가 먼저 적용됨
if (!amount <= 50)
    cout << "Amount is more than 50";
```

<div style="height: 1.5rem;"></div>

```cpp
// 올바름: 비교 전체를 부정
if (!(amount <= 50))
    cout << "Amount is more than 50";
```

</div>
</div>

---
layout: prism
heading: "실습: 체질량지수 계산"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

- [BMI]{.hl} 프로그램을 작성해 봅시다: 미터와 킬로그램 단위로 계산하되, 입력은 [파운드와 인치]{.hl}로 받습니다.

<div style="margin-top: 0.8rem;"></div>

| BMI | 해석 |
|:---|:---|
| BMI &lt; 18.5 | 저체중 |
| 18.5 ≤ BMI &lt; 25.0 | 정상 |
| 25.0 ≤ BMI &lt; 30.0 | 과체중 |
| 30.0 ≤ BMI | 비만 |

</div>
<div>

<CppRunner stdin="146 70">

```cpp
#include <iostream>   // ComputeAndInterpretBMI.cpp
using namespace std;

int main() {
    double weight, height;
    cout << "Enter weight in pounds: ";
    cin >> weight;
    cout << "Enter height in inches: ";
    cin >> height;

    const double KILOGRAMS_PER_POUND = 0.45359237;
    const double METERS_PER_INCH = 0.0254;

    double kg = weight * KILOGRAMS_PER_POUND;
    double m  = height * METERS_PER_INCH;
    double bmi = kg / (m * m);

    cout << "BMI is " << bmi << endl;
    if (bmi < 18.5)      cout << "Underweight" << endl;
    else if (bmi < 25)   cout << "Normal" << endl;
    else if (bmi < 30)   cout << "Overweight" << endl;
    else                 cout << "Obese" << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: 난수 생성하기"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 초등학생을 위한 뺄셈 퀴즈입니다. `0`–`9` 사이의 수를 얻기 위해 `<cstdlib>`의 `rand()`를 사용합니다.

- `rand()`만 쓰면 매번 같은 수열이 반복되므로 `srand`로 [시드]{.hl}를 바꿉니다.
  - `srand(time(0))`는 현재 시각 — 1970-01-01 이후의 초 — 를 사용합니다.

- 한 자리 정수 두 개를 생성하고, 답이 음수가 되지 않게 한 뒤 질문하고 검사합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>  // SubtractionQuiz.cpp
#include <ctime>     // time()을 위해
#include <cstdlib>   // rand()와 srand()를 위해
using namespace std;

int main() {
    // 실제로는: srand(time(0));
    // 데모의 재현성을 위해 시드를 고정함.
    srand(1);
    int number1 = rand() % 10;
    int number2 = rand() % 10;

    if (number1 < number2) {   // 답이 음수가 되지 않도록
        int t = number1; number1 = number2; number2 = t;
    }

    cout << "What is " << number1 << " - " << number2 << "? ";
    int answer = number1 - number2;   // 학생의 입력
    cout << answer << endl;

    if (number1 - number2 == answer)
        cout << "You are correct!" << endl;
    else
        cout << "Your answer is wrong." << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "논리 연산자 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 여러 조건을 결합하려면 [논리 연산자]{.hl}(논리 연산자, 불리언 연산자라고도 함)를 사용합니다.

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

| 연산자 | 이름 | 설명 |
|:---:|:---|:---|
| `!`  | not | 논리 부정 |
| `&&` | and | 논리곱 |
| `\|\|` | or | 논리합 |

<div style="margin-top: 1rem;"></div>

| `p` | `!p` |
|:---:|:---:|
| true  | false |
| false | true  |

</div>
<div>

| `p1` | `p2` | `p1 && p2` | `p1 \|\| p2` |
|:---:|:---:|:---:|:---:|
| false | false | false | false |
| false | true  | false | true  |
| true  | false | false | true  |
| true  | true  | true  | true  |

</div>
</div>

---
layout: prism
heading: "논리 연산자 (2/3)"
---

<div style="height: 0.2rem;"></div>

<CppRunner stdin="18">

```cpp
#include <iostream>   // TestBooleanOperators.cpp
using namespace std;

int main() {
    int number;
    cout << "Enter an integer: ";
    cin >> number;

    if (number % 2 == 0 && number % 3 == 0)
        cout << number << " is divisible by 2 and 3." << endl;

    if (number % 2 == 0 || number % 3 == 0)
        cout << number << " is divisible by 2 or 3." << endl;

    if ((number % 2 == 0 || number % 3 == 0) &&
        !(number % 2 == 0 && number % 3 == 0))
        cout << number << " is divisible by 2 or 3, but not both." << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "논리 연산자 (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 수학에서 `1 <= numDays <= 31`은 올바르지만, C++에서는 [그렇지 않습니다]{.hl}.
  - C++은 `1 <= numDays`를 먼저 `bool`로 평가한 뒤 그 `bool`을 `31`과 비교합니다 — 논리 오류입니다.

- [드모르간의 법칙]{.hl}으로 불리언 표현식을 단순화할 수 있습니다:

<div class="sub-item-enum">

1. `!(cond1 && cond2)`는 `!cond1 || !cond2`와 같습니다
2. `!(cond1 || cond2)`는 `!cond1 && !cond2`와 같습니다

</div>

---
layout: prism
heading: "실습: 윤년 판별"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 어떤 해가 `4`로 나누어떨어지지만 `100`으로는 나누어떨어지지 *않거나*, **또는** `400`으로 나누어떨어지면 [윤년]{.hl}(윤년)입니다.

- 세 가지 검사를 하나의 불리언 표현식으로 결합할 수 있습니다:

```cpp
bool isLeapYear = (year % 4 == 0);
isLeapYear = isLeapYear && (year % 100 != 0);
isLeapYear = isLeapYear || (year % 400 == 0);
```

</div>
<div>

<CppRunner stdin="2020">

```cpp
#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "Enter a year: ";
    cin >> year;

    bool isLeapYear =
        (year % 4 == 0 && year % 100 != 0)
        || (year % 400 == 0);

    if (isLeapYear)
        cout << year << " is a leap year." << endl;
    else
        cout << year << " is not a leap year." << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "switch 문 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [`switch`]{.hl} 문은 변수나 표현식의 값에 따라 문장을 실행합니다.

- 중첩 `if` 문을 남용하면 프로그램을 읽기 어려워집니다.

- C++은 [여러 경우]{.hl}에 대한 코딩을 단순화하기 위해 `switch`를 제공합니다.

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
  margin-top: 1.1em;
}
</style>

- `switch`-표현식은 [정수형 값]{.hl}을 산출해야 하며 괄호로 감싸야 합니다.

- `value1, …, valueN`은 [정수 상수 표현식]{.hl}입니다 — 변수(예: `1 + x`)나 부동소수점 값은 안 됩니다.

- 어떤 `case` 값이 일치하면 거기서부터 실행이 시작되어 [`break`]{.hl}나 `switch`의 끝까지 계속됩니다.

- 선택적인 [`default`]{.hl} case는 어떤 `case`도 일치하지 않을 때 실행됩니다.

- `break` 키워드는 선택 사항이지만, 즉시 `switch`를 끝냅니다(그렇지 않으면 실행이 *fall through*됩니다).

---
layout: prism
heading: "실습: 십이지 띠"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

- 주어진 연도에 대해 `year % 12`를 사용하여 [십이지 띠]{.hl}(띠)를 판별합니다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w03/cpp-w03-image41.png" class="tikz-fig" style="width: 78%; margin: 0.5rem auto;" />

</div>
<div>

<CppRunner stdin="1963">

```cpp
#include <iostream>
using namespace std;

int main() {
    int year;
    cout << "Enter a year: ";
    cin >> year;

    switch (year % 12) {
        case 0:  cout << "monkey";  break;
        case 1:  cout << "rooster"; break;
        case 2:  cout << "dog";     break;
        case 3:  cout << "pig";     break;
        case 4:  cout << "rat";     break;
        case 5:  cout << "ox";      break;
        case 6:  cout << "tiger";   break;
        case 7:  cout << "rabbit";  break;
        case 8:  cout << "dragon";  break;
        case 9:  cout << "snake";   break;
        case 10: cout << "horse";   break;
        case 11: cout << "sheep";   break;
    }
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: 조건 표현식
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [조건 표현식]{.hl}은 조건에 따라 표현식을 평가합니다:

```cpp
boolean-expression ? expression1 : expression2;
```

- `?`와 `:`는 [삼항 연산자]{.hl}를 이룹니다 — C++의 유일한 삼항 연산자입니다.

- 아래 두 형태는 동등합니다:

```cpp
if (x > 0)
    y = 1;
else
    y = -1;

y = x > 0 ? 1 : -1;
```

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int x = -2; x <= 2; x++) {
        int y = x > 0 ? 1 : -1;
        cout << "x = " << x
             << " -> y = " << y << endl;
    }

    int a = 5, b = 8;
    int max = (a > b) ? a : b;   // 더 큰 값 선택
    cout << "max(" << a << ", " << b
         << ") = " << max << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "연산자 우선순위와 결합성 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 연산자 [우선순위]{.hl}와 [결합성]{.hl}은 연산자가 평가되는 순서를 결정합니다(맨 위가 가장 높음).

<div class="grid grid-cols-2 gap-6" style="margin-top: 0.8rem;">
<div>

| 우선순위 | 연산자 |
|:---:|:---|
| 가장 높음 | `var++`, `var--` (후위) |
| | `+`, `-` (단항), `++var`, `--var` (전위) |
| | `static_cast<type>(v)`, `(type)` (캐스팅) |
| | `!` (not) |
| | `*`, `/`, `%` (곱셈류) |
| | `+`, `-` (이항 덧셈류) |

</div>
<div>

| 우선순위 | 연산자 |
|:---:|:---|
| | `<`, `<=`, `>`, `>=` (관계) |
| | `==`, `!=` (동등) |
| | `&&` (and) |
| | `\|\|` (or) |
| 가장 낮음 | `=`, `+=`, `-=`, `*=`, `/=`, `%=` (대입) |

</div>
</div>

---
layout: prism
heading: "연산자 우선순위와 결합성 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 우선순위가 같은 연산자가 서로 인접해 있으면, 그들의 [결합성]{.hl}이 평가 순서를 결정합니다.

- 대입을 제외한 모든 이항 연산자는 [왼쪽 결합]{.hl}(왼쪽 결합성)입니다:

```cpp
a - b + c - d   // is equivalent to   ((a - b) + c) - d
```

- 대입 연산자는 [오른쪽 결합]{.hl}(오른쪽 결합성)입니다:

```cpp
a = b += c = 5   // is equivalent to   a = (b += (c = 5))
```

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
