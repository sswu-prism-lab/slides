---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 6 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-6/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">6주차: 반복문</p>

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
heading: "복습: string 타입"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 문자들의 문자열을 표현하기 위해 [`string`]{.hl}이라는 자료형을 사용합니다.
  - `string message = "Programming is fun";`
  - `string` 타입은 원시 타입이 아니라 [객체 타입]{.hl}입니다.
  - `message`는 내용이 *Programming is fun*인 문자열 객체를 나타냅니다.

- 두 문자열을 비교하기 위해 관계 연산자 `==`, `!=`, `<`, `<=`, `>`, `>=`를 사용할 수 있습니다.

<div style="height: 0.8rem;"></div>

| 함수 | 설명 |
| --- | --- |
| `length()` | 이 문자열의 문자 개수를 반환합니다. |
| `size()` | `length()`와 동일합니다. |
| `at(index)` | 이 문자열에서 지정한 인덱스의 문자를 반환합니다. |

---
layout: prism
heading: "복습: string 타입 — 직접 해보기"
---

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string message = "Programming is fun";
    cout << "message  = " << message << "\n";
    cout << "length() = " << message.length() << "\n";
    cout << "at(0)    = " << message.at(0) << "\n";

    string a = "apple", b = "banana";
    cout << boolalpha;
    cout << "(a < b)  = " << (a < b) << "\n";   // 사전식 비교
    cout << "(a == b) = " << (a == b) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: 조작자(Manipulator)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- C++는 [값이 표시되는 형식을 지정하는]{.hl} 함수들을 제공합니다.

<div style="height: 0.5rem;"></div>

| 조작자 | 설명 |
| --- | --- |
| `setprecision(n)` | 부동소수점 수의 정밀도를 설정합니다. |
| `fixed` | 부동소수점 수를 고정소수점 표기법으로 표시합니다. |
| `showpoint` | 소수 부분이 없어도 소수점과 뒤따르는 0을 표시합니다. |
| `setw(width)` | 출력 필드의 너비를 지정합니다. |
| `left` | 출력을 왼쪽으로 정렬합니다. |
| `right` | 출력을 오른쪽으로 정렬합니다. |

---
layout: prism
heading: "복습: 조작자(Manipulator) — 직접 해보기"
---

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double pi = 3.14159265;
    cout << fixed << setprecision(2) << pi << "\n"; // 3.14
    cout << setprecision(4) << pi << "\n";          // 3.1416

    cout << "|" << setw(8) << right << "abc" << "|\n";
    cout << "|" << setw(8) << left  << "abc" << "|" << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "HW_W05: 무작위 문자열과 내가 사는 도시"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [1개의 대문자와 5개의 소문자]{.hl}로 이루어진 무작위 문자열을 생성한 뒤, 사용자가 입력한 도시 이름과 [알파벳 순서]{.hl}로 비교하여 결과를 출력하세요.

- 작동 예시:

```text
Input a city name: Seoul
The randomly generated city name is "Zjqxiu"
The cities in alphabetical order are "Seoul" and "Zjqxiu"

Input a city name: New York
The randomly generated city name is "Aeqpcb"
The cities in alphabetical order are "Aeqpcb" and "New York"
```

- 파일을 `HW_W05_20XXXXXX.cpp`로 저장한 뒤 LMS에 업로드하세요.

---
layout: prism
heading: "반복문 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 고속도로에서 자동차를 운전하고 있다고 상상해 봅시다.

- 내비게이션 알림이나 긴급 상황이 없다면, 우리는 [계속해서]{.hl} 앞으로 운전해 나갈 것입니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w06/cpp-w06-image5.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "반복문 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 반복문은 프로그램에게 [문장을 반복적으로 실행]{.hl}하도록 지시하는 데 사용할 수 있습니다.

- 어떤 문자열(예: `"Welcome to C++!"`)을 100번 표시해야 한다면, `cout` 문을 100개 작성하는 것은 지루한 일입니다.

- C++는 연산 또는 일련의 연산이 연속해서 몇 번 수행되는지를 제어하는 [반복문(loop)]{.hl}이라는 강력한 구조를 제공합니다.

- C++는 [`while`]{.hl}, [`do-while`]{.hl}, [`for`]{.hl} 반복문을 제공합니다.

<div style="height: 0.8rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int count = 0;
    while (count < 3) {          // 복사-붙여넣기 대신 반복
        cout << "Welcome to C++!\n";
        count++;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "while 반복문 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `while` 반복문은 [조건이 참인 동안]{.hl} 문장을 반복적으로 실행합니다.

- `while` 반복문의 구문은 다음과 같습니다:

```cpp
while (loop-continuation-condition) {
    // Loop body
    Statement(s);
}
```

- 반복문 본문을 한 번 실행하는 것을 반복문의 [반복(iteration)]{.hl}(또는 루프 반복)이라고 합니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w06/cpp-w06-image4.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "while 반복문 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `loop-continuation-condition`은 항상 [괄호]{.hl} 안에 나타나야 합니다.

- 흔한 프로그래밍 오류 중 하나는 [무한 루프]{.hl}입니다.
  - 프로그램이 비정상적으로 오래 실행되며 멈추지 않는다면, 무한 루프가 있을 수 있습니다.
  - 프로그램을 강제로 멈추려면 `ctrl (cmd) + c`를 누릅니다.

- 프로그래머는 반복문을 한 번 더 또는 한 번 덜 실행하는 실수를 자주 합니다.

```cpp
int count = 0;
while (count <= 100)   // 100번이 아니라 101번 실행됩니다!
{
    cout << "Welcome to C++!\n";
    count++;
}
```

---
layout: prism
heading: "실습: 숫자 맞히기"
---

<CppRunner stdin="50 25 42 39">

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>   // time 함수에 필요
using namespace std;

int main() {
    // 보통은: srand(time(0)); int number = rand() % 101;
    // 실행 재현을 위해 여기서는 고정.
    int number = 39;

    cout << "Guess a magic number between 0 and 100\n";

    int guess = -1;
    while (guess != number) {
        cout << "\nEnter your guess: ";
        cin >> guess;

        if (guess == number)
            cout << "Yes, the number is " << number << endl;
        else if (guess > number)
            cout << "Your guess is too high" << endl;
        else
            cout << "Your guess is too low" << endl;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "반복문 설계 전략"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 올바른 반복문을 작성하기 위해 세 단계를 고려합니다:

<div class="sub-item-enum">

1. [반복]{.hl}되어야 하는 문장들을 식별합니다.
2. 이 문장들을 반복문으로 감쌉니다.
3. `loop-continuation-condition`을 작성하고, 반복문을 제어하기 위한 적절한 문장을 추가합니다.

</div>

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

```cpp
while (true) {
    Statements;
}
```

</div>
<div>

```cpp
while (loop-continuation-condition) {
    Statements;
    Additional statements for
        controlling the loop;
}
```

</div>
</div>

---
layout: prism
heading: "사용자 확인으로 반복문 제어하기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 계속할지 여부를 사용자가 결정하게 하려면, [사용자 확인]{.hl}을 제공할 수 있습니다.

<CppRunner stdin="10 Y 20 Y 30 N">

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0, data;
    char continueLoop = 'Y';
    while (continueLoop == 'Y') {
        // 반복문 본문을 한 번 실행
        cout << "Enter an integer: ";
        cin >> data;
        sum += data;

        // 사용자에게 확인 요청
        cout << "Enter Y to continue and N to quit: ";
        cin >> continueLoop;
    }
    cout << "Sum = " << sum << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "감시 값(Sentinel Value)으로 반복문 제어하기"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 일련의 값을 읽어 처리하며 반복문을 제어할 때 [특수한 값]{.hl}을 지정할 수 있습니다.

- 이 특수한 입력 값을 [감시 값(sentinel value)]{.hl}이라고 하며, 입력의 끝을 나타냅니다.

- 감시 값을 사용해 실행을 제어하는 반복문을 [감시 값 제어 반복문(sentinel-controlled loop)]{.hl}이라고 합니다.

</div>
<div>

<CppRunner stdin="2 3 4 0">

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Enter an integer "
         << "(the input ends if it is 0): ";
    int data;
    cin >> data;

    // 입력이 0이 될 때까지 계속 읽기
    int sum = 0;
    while (data != 0) {
        sum += data;
        cout << "Enter an integer "
             << "(the input ends if it is 0): ";
        cin >> data;
    }

    cout << "The sum is " << sum << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "do-while 반복문"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `do-while` 반복문은 [반복문 본문을 먼저 실행]{.hl}한 뒤 loop-continuation-condition을 확인한다는 점을 제외하면 `while` 반복문과 동일합니다.

```cpp
do {
    // Loop body
    Statement(s);
} while (loop-continuation-condition);
```

- 반복문 본문이 먼저 실행된 다음 `loop-continuation-condition`이 평가됩니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w06/cpp-w06-image19.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "실습: do-while 테스트"
---

<CppRunner stdin="2 3 4 0">

```cpp
#include <iostream>
using namespace std;

int main() {
    // 입력이 0이 될 때까지 데이터를 계속 읽기
    int sum = 0;
    int data = 0;

    do {
        sum += data;

        // 다음 데이터 읽기
        cout << "Enter an integer (the input ends if it is 0): ";
        cin >> data;
    } while (data != 0);

    cout << "The sum is " << sum << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "for 반복문 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `for` 반복문은 반복문을 작성하기 위한 [간결한 구문]{.hl}을 가집니다.

```cpp
i = initialValue;   // init control var
while (i < endValue) {
    // Loop body
    i++;            // adjust control var
}
```

- `for` 반복문의 구문은 다음과 같습니다:

```cpp
for (initial-action;
     loop-continuation-condition;
     action-after-each-iteration) {
    // Loop body
    Statement(s);
}
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w06/cpp-w06-image24.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "for 반복문 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- `for` 반복문은 키워드 `for`로 시작하고, 그 뒤에 `initial-action`, `loop-continuation-condition`, `action-after-each-iteration`을 [세미콜론으로 구분하여]{.hl} 담은 한 쌍의 괄호가 옵니다.

- [제어 변수]{.hl}는 반복문 본문이 몇 번 실행되고 언제 종료되는지를 제어합니다.
  - `initial-action`은 제어 변수를 초기화합니다.
  - `action-after-each-iteration`은 보통 제어 변수를 증가 또는 감소시킵니다.
  - `loop-continuation-condition`은 제어 변수가 종료 값에 도달했는지 검사합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 3; i++)
        cout << "Welcome to C++! (i = " << i << ")\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "다양한 반복문"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 편리한 것에 따라 `for` 반복문, `while` 반복문, `do-while` 반복문 중 어느 것이든 사용할 수 있습니다.

- `while` 및 `for` 반복문은 계속 조건을 반복문 본문 *이전에* 검사하므로 [사전 검사 반복문(pretest loop)]{.hl}입니다.

- `do-while` 반복문은 조건을 반복문 본문 *이후에* 검사하므로 [사후 검사 반복문(posttest loop)]{.hl}입니다.

</div>
<div>

```cpp
for (initial-action;
     loop-continuation-condition;
     action-after-each-iteration) {
    // Loop body;
}
```

<div style="text-align:center; margin: 0.4rem 0;">— 다음과 동등함 —</div>

```cpp
initial-action;
while (loop-continuation-condition) {
    // Loop body;
    action-after-each-iteration;
}
```

</div>
</div>

---
layout: prism
heading: "중첩 반복문"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 반복문은 다른 반복문 안에 [중첩(nested)]{.hl}될 수 있습니다.

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << "         Multiplication Table\n";
    cout << "-----------------------------------\n";

    // 숫자 제목 표시
    cout << "  | ";
    for (int j = 1; j <= 9; j++)
        cout << setw(3) << j;
    cout << "\n";

    // 표 본문 표시
    for (int i = 1; i <= 9; i++) {
        cout << i << " | ";
        for (int j = 1; j <= 9; j++)
            cout << setw(3) << i * j;
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "수치 오류 최소화하기"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- loop-continuation-condition에 [부동소수점]{.hl} 수를 사용하면 [수치 오류가 발생할 수 있습니다]{.hl}. 아래의 합은 `50`이 아니라 `49.5`입니다 — `i`가 정확히 그 값에 도달하지 못하기 때문에 `1.0`이 건너뛰어집니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    // 0.01, 0.02, ..., 0.99, 1.0 을 sum에 더하기
    double sum = 0;
    for (double i = 0.01; i <= 1.0; i = i + 0.01)
        sum += i;
    cout << "The sum is " << sum << endl;   // 49.5 (수치 오류)
    return 0;
}
```

</CppRunner>

<div class="sub-item">

정수 제어 변수를 사용하는 것을 선호하세요: `for (int count = 0; count < 100; count++) { sum += currentValue; currentValue += 0.01; }`.

</div>

---
layout: prism
heading: "실습: 최대공약수"
---

<CppRunner stdin="125 2525">

```cpp
#include <iostream>
using namespace std;

int main() {
    // 사용자에게 두 정수 입력 요청
    cout << "Enter first integer: ";
    int n1;
    cin >> n1;

    cout << "Enter second integer: ";
    int n2;
    cin >> n2;

    int gcd = 1;
    int k = 2;
    while (k <= n1 && k <= n2) {
        if (n1 % k == 0 && n2 % k == 0)
            gcd = k;
        k++;
    }

    cout << "The greatest common divisor for " << n1 << " and "
         << n2 << " is " << gcd << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "실습: 몬테카를로 시뮬레이션 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- [몬테카를로 시뮬레이션]{.hl}은 무작위 수와 확률을 사용해 문제를 해결하며, 수학, 물리학, 화학 등에서 폭넓게 응용됩니다.

- 이 방법은 복잡한 수학적 계산을 피하고, 높은 계산 능력을 가진 컴퓨터를 활용하여 해를 근사합니다.

- [오컴의 면도날]{.hl}은 과학 이론에서 *불필요하게 가정을 복잡하게 하지 말라*는 것을 제안하는 원리입니다.

---
layout: prism
heading: "실습: 몬테카를로 시뮬레이션 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 몬테카를로 방법으로 [$\pi$]{.hl}를 추정하기 위해, 원의 반지름을 `1`이라고 가정합니다.

- 원의 넓이는 $\pi$이고 정사각형의 넓이는 `4`입니다.

- 정사각형 안에 점을 무작위로 생성하면, 그 점이 원 안에 들어갈 확률은 `circleArea / squareArea` $= \pi / 4$입니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w06/cpp-w06-image34.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "실습: 몬테카를로 시뮬레이션 (3/3)"
---

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    const int NUMBER_OF_TRIALS = 1000000;
    int numberOfHits = 0;
    srand(1);   // 추정 재현을 위한 고정 시드

    for (int i = 0; i < NUMBER_OF_TRIALS; i++) {
        double x = rand() * 2.0 / RAND_MAX - 1;
        double y = rand() * 2.0 / RAND_MAX - 1;
        if (x * x + y * y <= 1)
            numberOfHits++;
    }

    double pi = 4.0 * numberOfHits / NUMBER_OF_TRIALS;
    cout << "PI is " << pi << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "실습: 10진수를 16진수로"
---

<CppRunner stdin="1234">

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // 사용자에게 10진 정수 입력 요청
    cout << "Enter a decimal number: ";
    int decimal;
    cin >> decimal;

    // 10진수를 16진수로 변환
    string hex = "";
    while (decimal != 0) {
        int hexValue = decimal % 16;

        // 10진 값을 16진 자릿수로 변환
        char hexChar = (hexValue <= 9 && hexValue >= 0) ?
            static_cast<char>(hexValue + '0') :
            static_cast<char>(hexValue - 10 + 'A');

        hex = hexChar + hex;
        decimal = decimal / 16;
    }

    cout << "The hex number is " << hex << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "키워드 break와 continue (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- [`break`]{.hl}와 [`continue`]{.hl} 키워드는 반복문에서 추가적인 제어를 제공합니다.

- 반복문에서 `break`를 사용하면 [반복문을 즉시 종료]{.hl}할 수 있습니다.

- 반복문에서 `continue`를 사용하면 [현재 반복(iteration)을 끝낼]{.hl} 수 있습니다.

- 요약하면: `continue`는 *반복(iteration)*을 빠져나가고, `break`는 *반복문(loop)*을 빠져나갑니다.

---
layout: prism
heading: "키워드 break와 continue (2/3)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    int number = 0;

    while (number < 20) {
        number++;
        sum += number;
        if (sum >= 100)
            break;   // 반복문 밖으로 빠져나감
    }

    cout << "The number is " << number << endl;
    cout << "The sum is " << sum << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "키워드 break와 continue (3/3)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    int number = 0;

    while (number < 20) {
        number++;
        if (number == 10 || number == 11)
            continue;   // 이번 반복의 나머지를 건너뜀
        sum += number;
    }

    cout << "The sum is " << sum << endl;
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
