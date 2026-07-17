---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 5 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-5/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">5주차: 문자열, 서식, 파일 입출력</p>

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
heading: "복습: switch 문"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [`switch`]{.hl} 문은 하나의 식 값에 따라 여러 case 중 하나를 선택합니다. 각 `case`는 `break`로 끝나며, `default`는 그 밖의 모든 값을 처리합니다.

<div style="height: 1rem;"></div>

```cpp
switch (switch-expression) {
    case value1: statement(s)1;
                 break;
    case value2: statement(s)2;
                 break;
    // ...
    case valueN: statement(s)N;
                 break;
    default:     statement(s)-for-default;
}
```

---
layout: prism
heading: "복습: 조건 표현식"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [삼항 연산자]{.hl} `? :`는 조건 표현식을 만듭니다: `boolean-expression ? expression1 : expression2`.

- 피연산자를 *세 개* 사용하며, C++에서 유일한 삼항 연산자입니다.

- 오른쪽의 두 코드 조각은 서로 동등합니다.

</div>
<div>

<div style="height: 2rem;"></div>

```cpp
if (x > 0)
    y = 1;
else
    y = -1;

// equivalent conditional expression
y = x > 0 ? 1 : -1;
```

</div>
</div>

---
layout: prism
heading: "복습: 수학 함수"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- `min`, `max`, `abs`는 [`cstdlib`]{.hl} 헤더에 정의되어 있고, 삼각함수·지수·반올림 함수는 [`cmath`]{.hl} 헤더에 있습니다.

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

| `cmath` 함수 | 설명 |
|---|---|
| `sin/cos/tan(r)` | 라디안 각도의 삼각함수 |
| `asin/acos/atan(a)` | 역삼각함수, 결과는 라디안 |
| `exp(x)` | $e^x$ |
| `log(x)` / `log10(x)` | 자연로그 / 상용로그(밑 10) |
| `pow(a, b)` | $a^b$ |
| `sqrt(x)` | 제곱근, $x \geq 0$ |

</div>
<div>

| 반올림 | 설명 |
|---|---|
| `ceil(x)` | 가장 가까운 정수로 *올림* (`double` 반환) |
| `floor(x)` | 가장 가까운 정수로 *내림* (`double` 반환) |

</div>
</div>

---
layout: prism
heading: "복습: 문자"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 대부분의 컴퓨터는 문자, 숫자, 문장 부호, 제어 문자를 위한 8비트 인코딩인 [ASCII]{.hl}를 사용합니다. `char`는 1바이트입니다.

```cpp
char ch = 'a';
cout << ++ch; // 'b'
```

</div>
<div>

| 함수 | 문자가 …이면 `true` 반환 |
|---|---|
| `isdigit(ch)` | 숫자 |
| `isalpha(ch)` | 알파벳 |
| `isalnum(ch)` | 알파벳 또는 숫자 |
| `islower(ch)` | 소문자 |
| `isupper(ch)` | 대문자 |
| `isspace(ch)` | 공백 문자 |
| `tolower(ch)` | 소문자 형태를 *반환* |
| `toupper(ch)` | 대문자 형태를 *반환* |

</div>
</div>

---
layout: prism
heading: "DIY_W04: 20진수 한 자리 변환기"
---

- 한 자리 20진수를 입력받아 10진수로 변환하세요. 소문자가 입력되면 대문자로 자동 변환되었음을 경고하세요. (숫자 `0`–`9`는 `0`–`9`로, 알파벳 `A`–`J`는 `10`–`19`로 대응됩니다.)

<CppRunner stdin="A">

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    // 20진수 한 자리를 입력받는다.
    cout << "한 자리 20진수를 입력하세요: ";
    char inputNum;
    cin >> inputNum;

    /* 입력한 자릿수는 숫자이거나
       a ~ j 또는 A ~ J 사이의 알파벳이어야 한다. */
    if (isdigit(inputNum)
        || (toupper(inputNum) >= 65 && toupper(inputNum) < 75)) {
        if (isdigit(inputNum)) {
            cout << "입력한 20진수 " << inputNum << "은/는 10진수 "
                 << inputNum << "입니다.";
        }
        else if (islower(inputNum)) {
            cout << "입력한 알파벳 " << inputNum << "은/는 "
                 << static_cast<char>(toupper(inputNum))
                 << "으로 자동으로 변환되었습니다." << endl;
            cout << static_cast<char>(toupper(inputNum))
                 << "은/는 10진수 " << static_cast<int>(toupper(inputNum)) - 55
                 << "입니다.";
        }
        else {
            cout << "입력한 20진수 " << inputNum
                 << "은/는 10진수 " << static_cast<int>(inputNum) - 55 << "입니다.";
        }
    }
    else {
        cout << "입력 20진수에 오류가 있습니다.";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "string 타입 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [문자열(string)]{.hl}은 문자들의 *열(sequence)*인 반면, `char`는 한 개의 문자만 나타냅니다.

- 문자열을 표현하기 위해 [`string`]{.hl} 데이터 타입을 사용합니다.

```cpp
string message = "Programming is fun";
```

- `string`은 원시 타입이 아니라 [객체 타입]{.hl}입니다. `message`는 내용이 `Programming is fun`인 문자열 객체입니다.

- `string`은 `<string>` 헤더에 미리 정의된 클래스입니다 — `#include <string>`.

---
layout: prism
heading: "string 타입 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- `string` 클래스의 함수들은 특정 문자열 인스턴스로부터 호출됩니다 — 이를 [인스턴스 함수]{.hl}라고 합니다.

```cpp
string message = "Sungshin";
// check the length of the string
// find the third character of the string
```

</div>
<div>

<div style="height: 1.5rem;"></div>

| 함수 | 설명 |
|---|---|
| `length()` | 문자열의 문자 개수 |
| `size()` | `length()`와 동일 |
| `at(index)` | 지정한 인덱스의 문자 |

</div>
</div>

---
layout: prism
heading: "문자열 인덱스와 첨자 연산자"
---

- `s.at(index)`는 문자열 `s`에서 문자를 가져오며, `index`는 `0`부터 `s.length() - 1` 사이입니다. 편의를 위해 C++은 [첨자 연산자]{.hl} `stringName[index]`도 제공합니다.

<div style="display:flex; justify-content:center; margin: 1.2rem 0;">
<table style="border-collapse: collapse; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 0.9rem;">
<tr>
  <td style="border:none; padding:2px 6px;">Indices</td>
  <td style="border:1px solid #888; padding:2px 8px;">0</td><td style="border:1px solid #888; padding:2px 8px;">1</td><td style="border:1px solid #888; padding:2px 8px;">2</td><td style="border:1px solid #888; padding:2px 8px;">3</td><td style="border:1px solid #888; padding:2px 8px;">4</td><td style="border:1px solid #888; padding:2px 8px;">5</td><td style="border:1px solid #888; padding:2px 8px;">6</td><td style="border:1px solid #888; padding:2px 8px;">7</td><td style="border:1px solid #888; padding:2px 8px;">8</td><td style="border:1px solid #888; padding:2px 8px;">9</td><td style="border:1px solid #888; padding:2px 8px;">10</td><td style="border:1px solid #888; padding:2px 8px;">11</td><td style="border:1px solid #888; padding:2px 8px;">12</td><td style="border:1px solid #888; padding:2px 8px;">13</td>
</tr>
<tr>
  <td style="border:none; padding:2px 6px;">message</td>
  <td style="border:1px solid #888; padding:2px 8px;">W</td><td style="border:1px solid #888; padding:2px 8px;">e</td><td style="border:1px solid #888; padding:2px 8px;">l</td><td style="border:1px solid #888; padding:2px 8px;">c</td><td style="border:1px solid #888; padding:2px 8px;">o</td><td style="border:1px solid #888; padding:2px 8px;">m</td><td style="border:1px solid #888; padding:2px 8px;">e</td><td style="border:1px solid #888; padding:2px 8px;">&nbsp;</td><td style="border:1px solid #888; padding:2px 8px;">t</td><td style="border:1px solid #888; padding:2px 8px;">o</td><td style="border:1px solid #888; padding:2px 8px;">&nbsp;</td><td style="border:1px solid #888; padding:2px 8px;">C</td><td style="border:1px solid #888; padding:2px 8px;">+</td><td style="border:1px solid #888; padding:2px 8px;">+</td>
</tr>
</table>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string message = "Welcome to C++";
    cout << "length = " << message.length() << endl; // 14
    cout << "at(0)  = " << message.at(0) << endl;     // W
    cout << "at(13) = " << message.at(13) << endl;    // +

    string s = message;
    s[0] = 'P';                      // subscript operator (write)
    cout << "s[0]   = " << s[0] << endl; // P
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "문자열 연결"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- C++은 두 문자열을 [연결(concatenating)]{.hl}하는 `+`를 제공하며, 확장 대입 연산자 `+=`도 연결합니다.

- 두 문자열 리터럴을 연결하는 것은 *허용되지 않습니다*:

```cpp
string cities = "London" + "Paris"; // error
```

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1 = "Welcome ", s2 = "to C++";
    string s3 = s1 + s2;          // + operator
    cout << s3 << endl;

    string message = "Welcome to C++";
    message += " and programming is fun"; // += operator
    cout << message << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "문자열 비교"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 관계 연산자 `==`, `!=`, `<`, `<=`, `>`, `>=`로 두 문자열을 비교합니다.

- 비교는 대응하는 문자끼리 [왼쪽에서 오른쪽으로 하나씩]{.hl} 진행됩니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1 = "ABC";
    string s2 = "ABE";
    cout << (s1 == s2) << endl; // 0 (false)
    cout << (s1 != s2) << endl; // 1 (true)
    cout << (s1 >  s2) << endl; // 0 (false)
    cout << (s1 >= s2) << endl; // 0 (false)
    cout << (s1 <  s2) << endl; // 1 (true)
    cout << (s1 <= s2) << endl; // 1 (true)
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "문자열 읽기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 문자열은 `cin`으로 키보드에서 읽을 수 있지만, `cin >> s`는 첫 *공백*에서 멈추므로 `New York`을 하나의 문자열로 읽을 수 없습니다.

```cpp
string city;
cin >> city; // reads only up to the first space
```

- C++은 한 줄 전체를 읽기 위해 `<string>` 헤더에 [`getline`]{.hl}을 제공합니다:

```cpp
getline(cin, s, delimitCharacter)
```

- [구분 문자(delimiter)]{.hl}는 읽히지만 문자열에 저장되지는 *않습니다*. 세 번째 인자 `delimitCharacter`의 기본값은 `'\n'`이므로 `getline(cin, city);`는 한 줄 전체를 읽습니다.

---
layout: prism
heading: "실습: 두 도시 정렬"
---

두 도시 이름(각각 공백을 포함할 수 있음)을 `getline`으로 읽은 뒤, 알파벳 순서로 출력하세요.

<CppRunner stdin="Seoul
Busan">

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string city1, city2;
    cout << "Enter the first city: ";
    getline(cin, city1);
    cout << "Enter the second city: ";
    getline(cin, city2);

    cout << "The cities in alphabetical order are ";
    if (city1 < city2)
        cout << city1 << " " << city2 << endl;
    else
        cout << city2 << " " << city1 << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "실습: 로또 프로그램 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 로또 프로그램은 무작위 두 자리 수를 생성하고, 사용자에게 두 자리 수를 입력받아 당첨 여부를 판정합니다.

- 상금 [규칙]{.hl}:
  - 로또 번호와 순서까지 정확히 일치 → **$10,000**
  - 모든 자릿수가 일치(순서 무관) → **$3,000**
  - 한 자릿수가 일치 → **$1,000**

```cpp
#include <iostream>
#include <string>   // for using strings
#include <ctime>    // for time function
#include <cstdlib>  // for rand and srand functions
using namespace std;
```

---
layout: prism
heading: "실습: 로또 프로그램 (2/2)"
---

<div style="height: 0.2rem;"></div>

<CppRunner stdin="36">

```cpp
#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
using namespace std;

int main() {
    string lottery;
    srand(1); // fixed seed for a reproducible run (was srand(time(0)))
    int digit = rand() % 10;                    // Generate first digit
    lottery += static_cast<char>(digit + '0');
    digit = rand() % 10;                        // Generate second digit
    lottery += static_cast<char>(digit + '0');

    // Prompt the user to enter a guess
    cout << "Enter your lottery pick (two digits): ";
    string guess;
    cin >> guess;

    cout << "The lottery number is " << lottery << endl;

    // Check the guess
    if (guess == lottery)
        cout << "Exact match: you win $10,000" << endl;
    else if (guess[1] == lottery[0] && guess[0] == lottery[1])
        cout << "Match all digits: you win $3,000" << endl;
    else if (guess[0] == lottery[0] || guess[0] == lottery[1]
             || guess[1] == lottery[0] || guess[1] == lottery[1])
        cout << "Match one digit: you win $1,000" << endl;
    else
        cout << "Sorry, no match" << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "콘솔 출력 서식"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- [스트림 조정자(stream manipulators)]{.hl}를 사용하면 콘솔에 서식이 적용된 출력을 표시할 수 있습니다.

- C++은 값을 어떻게 표시할지 서식화하는 함수들을 제공하며, 이들이 스트림 조정자이고 [`iomanip`]{.hl} 헤더 파일에 포함되어 있습니다.

```cpp
#include <iomanip>
```

---
layout: prism
heading: "setprecision(n) 조정자"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [`setprecision(n)`]{.hl}은 부동소수점 수에 표시되는 전체 자릿수를 지정합니다.

- 정밀도가 다시 바뀔 때까지 그 설정이 유지됩니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double number = 12.34567;
    cout << setprecision(3) << number << " "
         << setprecision(4) << number << " "
         << setprecision(5) << number << " "
         << setprecision(6) << number << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "fixed 조정자"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 큰 부동소수점 수는 기본적으로 *과학적 표기법*으로 표시됩니다 (예: `2.32123e+08`).

- [`fixed`]{.hl} 조정자는 소수점 이하 6자리의 비과학적 표기법을 강제하며, `setprecision`과 함께 쓰면 그 자릿수를 바꿀 수 있습니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << 232123434.357 << endl;         // 2.32123e+08
    cout << fixed << 232123434.357 << endl; // 232123434.357000

    double monthlyPayment = 345.4567;
    double totalPayment = 78676.887234;
    cout << setprecision(2)
         << monthlyPayment << endl
         << totalPayment << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "showpoint 조정자"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [`showpoint`]{.hl} 조정자는 `setprecision`과 함께 소수점 이하 자릿수를 고정하여 표시하며, 뒤따르는 0도 유지합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << setprecision(6);
    cout << 1.23 << endl;              // 1.23
    cout << showpoint << 1.23 << endl; // 1.23000
    cout << showpoint << 123.0 << endl;// 123.000
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "setw(width) 조정자"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 기본적으로 `cout`은 필요한 만큼의 자리만 사용합니다. [`setw(width)`]{.hl}은 다음 출력에 한해 *최소* 열 개수를 지정합니다.

- 항목이 `width`보다 많은 공간을 필요로 하면 너비가 자동으로 늘어납니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << setw(8) << "C++"  << setw(6) << 101 << endl;
    cout << setw(8) << "Java" << setw(6) << 101 << endl;
    cout << setw(8) << "HTML" << setw(6) << 101 << endl;
    // width too small -> automatically increased
    cout << setw(8) << "Programming" << "#" << setw(2) << 101 << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "left와 right 조정자"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `setw`은 기본적으로 [오른쪽]{.hl} 정렬을 사용합니다.

- [`left`]{.hl} 조정자는 출력을 왼쪽 정렬하고, [`right`]{.hl} 조정자는 오른쪽 정렬합니다. (아래의 `|`는 필드 경계를 나타냅니다.)

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << right;
    cout << "|" << setw(8) << 1.23   << "|" << endl;
    cout << "|" << setw(8) << 351.34 << "|" << endl;

    cout << left;
    cout << "|" << setw(8) << 1.23   << "|" << endl;
    cout << "|" << setw(8) << 351.34 << "|" << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "파일에 쓰기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 파일에 데이터를 쓰려면 [`<fstream>`]{.hl} 헤더를 포함하고 [`ofstream`]{.hl} 타입의 변수를 선언합니다.

```cpp
#include <fstream>
ofstream output;
```

- `open`을 호출해 파일을 지정합니다 — 이는 현재 디렉터리에 파일을 생성하며, 이미 존재하는 경우 그 내용이 지워지고 새 파일이 만들어집니다.

```cpp
output.open("numbers.txt");
```

- 작업이 끝나면 `close`를 호출합니다:

```cpp
output.close();
```

---
layout: prism
heading: "실습: 간단한 파일 출력"
---

이 프로그램은 세 개의 수를 `numbers.txt`에 쓴 뒤 다시 읽어 들여 샌드박스에서 결과를 확인할 수 있게 합니다.

<CppRunner>

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream output;
    output.open("numbers.txt");             // Create a file
    output << 95 << " " << 56 << " " << 34; // Write numbers
    output.close();                         // close file
    cout << "Done" << endl;

    // Read it back so the output is visible in the sandbox
    ifstream input("numbers.txt");
    int a, b, c;
    input >> a >> b >> c;
    input.close();
    cout << "File contents: " << a << " " << b << " " << c << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "파일에서 읽기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 파일에서 데이터를 읽으려면 [`ifstream`]{.hl} 타입의 변수를 선언하고 파일을 엽니다:

```cpp
ifstream input;
input.open("numbers.txt");
```

- 파일 입력 객체 생성과 파일 열기를 한 문장으로 처리할 수도 있습니다:

```cpp
ifstream input("numbers.txt");
```

---
layout: prism
heading: "실습: 간단한 파일 입력"
---

예제를 자체 완결형으로 만들기 위해 먼저 `numbers.txt`를 생성한 뒤, 세 점수를 다시 읽어 들여 합산합니다.

<CppRunner>

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // First create numbers.txt so there is something to read
    ofstream output("numbers.txt");
    output << 95 << " " << 56 << " " << 34;
    output.close();

    ifstream input;
    input.open("numbers.txt");   // Open a file
    int score1, score2, score3;
    input >> score1;             // Read data
    input >> score2;
    input >> score3;

    cout << "Total score is " << score1 + score2 + score3 << endl;
    input.close();               // Close file
    cout << "Done" << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "HW_W05: 무작위 도시 이름"
---

무작위 6글자 "도시"(대문자 1개 + 소문자 5개)를 생성한 뒤, 사용자가 입력한 도시 이름과 함께 알파벳 순서로 출력하세요. `HW_W05_20XXXXXX.cpp`로 저장하여 LMS에 업로드하세요.

<CppRunner stdin="Seoul">

```cpp
#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int main() {
    srand(1); // fixed seed for a reproducible run

    // 1 uppercase letter + 5 lowercase letters
    string generated;
    generated += static_cast<char>('A' + rand() % 26);
    for (int i = 0; i < 5; i++)
        generated += static_cast<char>('a' + rand() % 26);

    cout << "Input a city name: ";
    string city;
    getline(cin, city);

    cout << "The randomly generated city name is \"" << generated << "\"" << endl;
    cout << "The cities in alphabetical order are ";
    if (city < generated)
        cout << "\"" << city << "\" and \"" << generated << "\"" << endl;
    else
        cout << "\"" << generated << "\" and \"" << city << "\"" << endl;

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
