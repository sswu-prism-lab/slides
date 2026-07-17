---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 12 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-12/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">C++ 프로그래밍</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">12주차: 클래스와 객체 (계속)</p>

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
heading: "요약: 객체와 클래스"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [클래스]{.hl}(class)는 [객체]{.hl}(object)의 *속성*과 *행동*을 정의합니다.

- [객체지향 프로그래밍]{.hl}(object-oriented programming)에서는 프로그램을 객체들로 구성합니다.
  - 객체는 명확히 *구별되는* 개체를 의미합니다.
  - 각 객체는 자신만의 유일한 특성, 즉 [상태]{.hl}(state)와 [행동]{.hl}(behavior)을 가집니다.

- 객체의 *상태*(또는 [속성 / 특성]{.hl})은 [데이터 필드]{.hl}(data field)로 표현됩니다.
  - 예: 원 객체는 자신의 속성을 나타내는 `radius` 데이터 필드를 가집니다.

- 객체의 *행동*(또는 [동작]{.hl})은 [함수]{.hl}에 의해 정의됩니다.

---
layout: prism
heading: "요약: 클래스"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 같은 유형의 객체들은 공통 [클래스]{.hl}를 사용하여 정의됩니다.

- 클래스는 객체가 어떤 데이터 필드와 함수를 가질지를 결정하는 [템플릿]{.hl}(template, 설계도)이며, 객체는 그 클래스의 [인스턴스]{.hl}(instance)입니다.
  - 인스턴스를 생성하는 것을 [실체화]{.hl}(instantiation)라고 합니다.
  - 하나의 `Circle` 클래스로부터 무수히 많은 `Circle` 객체를 만들 수 있습니다.

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
heading: "요약: 객체 멤버 접근"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 객체의 데이터와 함수는 객체 이름과 [점 연산자]{.hl}(`.`)를 사용하여 접근합니다.

- 객체지향 관점에서, 객체의 [멤버]{.hl}(member)란 데이터 필드와 함수를 의미합니다.
  - 새롭게 생성된 객체는 메모리에 할당되며, 그 후 [객체 멤버 접근 연산자]{.hl}(점 연산자)를 사용하여 데이터를 읽고 함수를 호출합니다.

```cpp
circle1.radius;      // 객체의 데이터 필드를 참조함
circle1.getArea();   // 객체에 대한 함수를 호출함
```

- 접근되는 데이터 필드를 [인스턴스 변수]{.hl}라 하고, 접근되는 함수를 [인스턴스 함수]{.hl}라고 합니다.

---
layout: prism
heading: "객체지향 개념"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 프로그램을 단순히 *데이터*와 *처리 방법*으로 나누는 대신, 객체지향 프로그래밍은 프로그램을 [객체]{.hl}(object)라는 기본 단위로 나눈 뒤 이들의 *상호작용*을 중점적으로 다룹니다.
  - 객체는 하나의 역할을 수행하는 *처리 방법*(메소드, 행동, 함수)과 *데이터*(변수)를 하나로 묶습니다.
    - C++에서는 이를 `class`로 자연스럽게 표현할 수 있습니다.

- 함수는 데이터의 *처리 방법*을 구조화하지만, *데이터* 자체는 구조화하지 못합니다.
  - 객체지향 프로그래밍은 모든 객체가 속성과 행동 모두에 연관되어 있는 현실 세계를 반영합니다.

- 객체지향 프로그램에서는 객체의 내부 구현을 외부로부터 감추어([정보 은닉]{.hl}), 모듈 내부의 *응집력*은 높이고 모듈 간의 *결합도*는 낮추어 유연성과 유지보수성을 향상시킵니다.

---
layout: prism
heading: "string 클래스 (1/8)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- `string` 클래스는 C++에서 `string` 형을 정의하며, 다른 방식(C-문자열)보다 훨씬 사용이 용이합니다.

| 함수         | 설명                                                     |
| ------------ | -------------------------------------------------------- |
| `length()`   | 이 문자열의 문자 개수를 반환합니다.                       |
| `size()`     | `length()`와 동일합니다.                                 |
| `at(index)`  | 지정된 인덱스의 문자를 반환합니다.                        |

- `length`, `size`, `at` 같은 함수들은 우리가 직접 함수 형태로 구현해서 사용할 수도 있을 것입니다.

- 그러나 다양한 데이터 유형(`int`, `float`, `bool`)을 함께 사용하는 [대규모 프로그래밍 프로젝트]{.hl}에서는, string이 아닌 변수들도 [불필요하게 이 함수들에 접근]{.hl}할 수 있게 되어 비효율적인 프로그래밍 방식이 됩니다.

---
layout: prism
heading: "string 클래스 (2/8)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `string` 클래스를 통해 문자열 객체를 정의하면, 문자열만을 위한 행동(함수)들을 다른 데이터와 분리하여 효율적인 프로그래밍이 가능합니다.

```cpp
// 문자열 리터럴 사용: 문자열 객체를 생성한 뒤
// s에 복사하는 두 단계를 거침.
string s1 = "Welcome to C++";

// 더 좋은 방법은 문자열 생성자를 직접 사용하는 것.
string s2("Welcome to C++");

// (인수 없는 생성자를 사용한) 빈 문자열.
string s3;

// C-문자열로부터 문자열을 생성.
char s4[] = "Welcome to C++";
string s5(s4);
```

---
layout: prism
heading: "string 클래스 (3/8)"
---

- `string` 클래스의 함수들은 [오버로딩]{.hl}될 수 있어 불필요한 네임스페이스 확장을 방지합니다. 아래는 `append` 오버로딩입니다.

| `append` 오버로딩                       | 설명                                                              |
| --------------------------------------- | ----------------------------------------------------------------- |
| `append(s)`                             | 이 문자열 객체에 문자열 `s`를 덧붙입니다.                         |
| `append(s, index, n)`                   | `s`의 `index` 위치부터 `n`개의 문자를 덧붙입니다.                 |
| `append(s, n)`                          | `s`의 처음 `n`개의 문자를 이 문자열에 덧붙입니다.                 |
| `append(n, ch)`                         | 문자 `ch`를 `n`개 복사하여 이 문자열에 덧붙입니다.               |

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
heading: "string 클래스 (4/8)"
---

| `assign` 오버로딩            | 설명                                                           |
| ---------------------------- | -------------------------------------------------------------- |
| `assign(s)`                  | 문자 배열 또는 문자열 `s`를 이 문자열에 대입합니다.            |
| `assign(s, index, n)`        | `s`의 `index` 위치부터 `n`개의 문자를 대입합니다.             |
| `assign(s, n)`               | `s`의 처음 `n`개의 문자를 대입합니다.                          |
| `assign(n, ch)`              | 문자 `ch`를 `n`개 복사하여 대입합니다.                        |

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
heading: "string 클래스 (5/8)"
---

| 함수                | 설명                                                           |
| ------------------- | -------------------------------------------------------------- |
| `at(index)`         | `index` 위치의 문자를 반환합니다.                             |
| `clear()`           | 이 문자열의 모든 문자를 제거합니다.                           |
| `erase(index, n)`   | `index` 위치부터 `n`개의 문자를 제거합니다.                   |
| `empty()`           | 이 문자열이 비어 있으면 `true`를 반환합니다.                  |

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
heading: "string 클래스 (6/8)"
---

| 함수                         | 설명                                                                |
| ---------------------------- | ------------------------------------------------------------------- |
| `compare(s)`                 | 이 문자열이 `s`보다 크면 `> 0`, 같으면 `0`, 작으면 `< 0`을 반환합니다. |
| `compare(index, n, s)`       | 이 문자열을 부분 문자열 `s(index, ..., index+n-1)`와 비교합니다. |
| `substr(index, n)`           | `index`부터 시작하는 `n`개 문자의 부분 문자열을 반환합니다.         |
| `substr(index)`              | 이 문자열의 `index`부터 시작하는 부분 문자열을 반환합니다.          |

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
heading: "string 클래스 (7/8)"
---

| 함수                         | 설명                                                                |
| ---------------------------- | ------------------------------------------------------------------- |
| `find(ch)` / `find(ch, index)` | 처음 일치하는 문자 `ch`의 위치 (`index` 위치/이후).             |
| `find(s)` / `find(s, index)` | 처음 일치하는 부분 문자열 `s`의 위치 (`index` 위치/이후).           |
| `insert(index, s)`           | `index` 위치에 문자열 `s`를 삽입합니다.                            |
| `insert(index, n, ch)`       | `index` 위치에 문자 `ch`를 `n`번 삽입합니다.                       |
| `replace(index, n, s)`       | `index`부터 `n`개의 문자를 문자열 `s`로 교체합니다.                |

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
heading: "string 클래스 (8/8)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

| 연산자              | 설명                                                                    |
| ------------------- | ----------------------------------------------------------------------- |
| `[]`                | 배열 첨자 연산자를 사용하여 문자에 접근합니다.                          |
| `=`                 | 한 문자열의 내용을 다른 문자열로 복사합니다.                            |
| `+`                 | 두 문자열을 이어 새로운 문자열을 만듭니다.                              |
| `+=`                | 한 문자열의 내용을 다른 문자열에 덧붙입니다.                            |
| `<<`                | 문자열을 스트림에 삽입합니다.                                           |
| `>>`                | 스트림에서 문자를 추출하여 문자열에 넣습니다(공백으로 구분).             |
| `==` `!=` `<` `<=` `>` `>=` | 문자열 비교를 위한 여섯 개의 관계 연산자.                        |

- 문자열은 대입 / 연결 연산자를 사용하여 결합할 수 있습니다.

- 비교 연산자를 통해 문자열을 직접 비교할 수 있습니다.

---
layout: prism
heading: "실습: ExtractWords.cpp"
---

<div style="height: 0.3rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string text("Programming is fun");  // string 객체 생성
    stringstream ss(text);              // stringstream 객체 생성

    cout << "The words in the test are " << endl;
    string word;                        // string 객체 생성
    while (!ss.eof()) {                 // ss.eof()는 스트림이 끝날 때 true
        ss >> word;                     // 스트림으로부터 데이터 획득
        cout << word << endl;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "실습: ReplaceString.cpp (1/2)"
---

<div style="height: 1rem;"></div>

```cpp
#include <iostream>
#include <string>
using namespace std;

// s 내의 oldSubStr을 newSubStr으로 교체하는 함수.
bool replaceString(string& s, const string& oldSubStr, const string& newSubStr);

int main() {
    // s, oldSubStr, newSubStr 입력.
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
heading: "실습: ReplaceString.cpp (2/2)"
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

// 함수 구현
bool replaceString(
        string& s, const string& oldSubStr, const string& newSubStr) {
    bool isReplaced = false;
    int currentPosition = 0;
    while (currentPosition < (int)s.length()) {
        int position = s.find(oldSubStr, currentPosition);
        if (position == (int)string::npos)  // 더 이상 일치하는 내용이 없음
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
heading: "함수에 객체 전달"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.0em;
}
</style>

- 객체는 함수로 [값에 의한 전달]{.hl} 또는 [참조에 의한 전달]{.hl} 모두 가능하지만, [참조에 의한 전달이 더 효율적]{.hl}입니다.

- *값에 의한 전달* 시, 함수는 새로운 객체를 생성하고 전달된 객체의 *복사본*을 대상으로 작업합니다.

- [참조에 의한 전달]{.hl} 시, 함수는 전달된 객체 자체를 대상으로 직접 작업합니다 — 매개변수가 그 객체의 *별칭*이 됩니다.

- 값에 의한 전달은 추가적인 시간과 메모리가 필요하므로, [참조에 의한 전달이 더 효율적]{.hl}입니다.

---
layout: prism
heading: "실습: PassObject.cpp"
---

<div style="height: 0.3rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// (CircleWithPrivateDataFields.h에서 병합)
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
heading: "객체의 배열"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 원시 값 배열이나 문자열 배열처럼, [객체의 배열]{.hl}도 생성할 수 있습니다.

- 배열은 인수 없는 생성자로 선언할 수도 있고, 인수를 갖는 생성자를 사용하여 [선언과 동시에 초기화]{.hl}할 수도 있습니다.

- 객체 배열의 각 요소는 일반 배열과 똑같이 `arrayName[i]`를 사용하여 접근합니다.

```cpp
Circle circleArray[10]; // 10개의 Circle 객체 배열 선언
// 인수 없는 생성자가 radius를 1로 설정하므로, 각 getRadius()는 1을 반환.

// 인수를 갖는 생성자를 사용하여 배열을 선언 및 초기화할 수도 있음.
Circle circleArray[3] = {Circle(3), Circle(5), Circle(7)};
cout << circleArray[0].getRadius() << endl; // 3
```

---
layout: prism
heading: "인스턴스 멤버와 정적 멤버 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 클래스 내에서 사용되는 데이터 필드를 [인스턴스 데이터 필드]{.hl}(또는 [인스턴스 변수]{.hl})라고 합니다.

- 인스턴스 변수는 객체들 사이에서 공유되지 *않습니다*.

```cpp
Circle circle1;
Circle circle2(5); // circle1과 circle2의 radius는 독립적임
```

- 클래스의 *모든* 인스턴스가 데이터를 공유하도록 하려면 [정적 변수]{.hl}(static variable)를 사용합니다.
  - 정적 변수는 [클래스 변수]{.hl}(class variable)라고도 합니다.

---
layout: prism
heading: "인스턴스 멤버와 정적 멤버 (2/2)"
---

- 정적 변수는 그 값을 *공통* 메모리 위치에 저장하며, 한 객체가 이를 변경하면 같은 클래스의 모든 객체가 영향을 받습니다.
  - UML 표기에서 정적 변수와 함수는 *밑줄*로 표현합니다.

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
두 객체는 메모리 상의 단 하나의 <code>numberOfObjects</code>(값 2)를 공유하며, 각자 자신의 <code>radius</code>를 유지합니다.
</div>

</div>
</div>

- 정적 변수와 함수는 `static` 키워드를 사용합니다: `static int numberOfObjects;` &nbsp;/&nbsp; `static int getNumberOfObjects();`

---
layout: prism
heading: "실습: CircleWithStaticDataFields.h"
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
    static int getNumberOfObjects();  // 정적 함수

private:
    double radius;
    static int numberOfObjects;       // 정적 변수
};

#endif
```

---
layout: prism
heading: "실습: CircleWithStaticDataFields.cpp"
---

```cpp
#include "CircleWithStaticDataFields.h"

int Circle::numberOfObjects = 0;  // 정적 변수 초기화

Circle::Circle() {                // circle 객체 생성
    radius = 1;
    numberOfObjects++;
}
Circle::Circle(double newRadius) { // 인수 있는 생성자
    radius = newRadius;
    numberOfObjects++;
}
double Circle::getArea() {        // 원의 면적 반환
    return radius * radius * 3.14159;
}
double Circle::getRadius() {      // 원의 반지름 반환
    return radius;
}
void Circle::setRadius(double newRadius) {  // 새 반지름 설정
    radius = (newRadius >= 0) ? newRadius : 0;
}
int Circle::getNumberOfObjects() {  // 원 객체 수 반환
    return numberOfObjects;
}
```

---
layout: prism
heading: "실습: TestCircleWithStaticDataFields.cpp"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// 병합: CircleWithStaticDataFields.h + .cpp
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
         << Circle::getNumberOfObjects() << endl;  // 객체 없이 접근 가능

    Circle circleArray[2] = {Circle(), Circle(5.0)};  // 객체 2개 생성

    printCircle(circleArray[0]);
    printCircle(circleArray[1]);

    circleArray[0].setRadius(3.3);  // 새 객체가 생성되는 것은 아님
    printCircle(circleArray[0]);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "상수 멤버 함수"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- C++에서는 함수가 객체의 어떤 데이터 필드도 *변경하지 않음*을 컴파일러에게 알리는 [상수 멤버 함수]{.hl}로 지정할 수 있습니다.

- 함수가 객체의 데이터 필드를 수정하지 않음을 나타내기 위해, [`const`]{.hl} 키워드를 사용하여 상수 멤버 함수(줄여서 *상수 함수*)로 선언합니다.

- [인스턴스 멤버 함수]{.hl}만이 상수 함수로 정의될 수 있으며, 상수 매개변수처럼 상수 함수 또한 [방어적 프로그래밍]{.hl}을 지원합니다.
  - 정적 함수는 상수가 될 수 없으며, 인스턴스 함수만 가능합니다.

---
layout: prism
heading: "객체 합성 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 객체는 다른 객체를 *포함*할 수 있으며, 이 관계를 [합성]{.hl}(composition)이라고 합니다.
  - 예: `Circle` 클래스가 `string` 데이터 필드를 포함할 수 있습니다.

- 합성은 [집합]{.hl}(aggregation) 관계의 특별한 경우입니다.
  - 집합은 [has-a]{.hl} 관계를 모델링하며, 두 객체 사이의 *소유* 관계를 나타냅니다.
  - [소유하는 객체]{.hl}(owner object)는 *aggregating* 객체이고, 그 클래스는 *aggregating* 클래스입니다.
  - 소유되는 ([종속]{.hl}) 객체는 *aggregated* 객체이고, 그 클래스는 *aggregated* 클래스입니다.

- 하나의 객체는 여러 aggregating 객체에 의해 소유될 수 있으며, 만약 *하나의* aggregating 객체에 의해 독점적으로 소유되면 그 관계가 [합성]{.hl}입니다.

---
layout: prism
heading: "객체 합성 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- `Student`는 `Name`을 [가집니다(has a)]{.hl}.
  - 학생은 하나의 이름만 가지므로 `Student`–`Name`은 [합성]{.hl}입니다.

- `Student`는 `Address`를 [가집니다(has an)]{.hl}.
  - 주소는 여러 학생이 *공유*할 수 있으므로(예: 룸메이트), `Student`–`Address`는 [집합]{.hl}입니다.
    - 범위 `m..n`은 객체의 수가 `m`과 `n` 사이여야 함을 의미합니다(여기서는 최대 3명의 학생이 하나의 주소를 공유).
    - `*`는 무한한 수의 객체가 가능함을 의미합니다.

<div class="flex items-center justify-center gap-2" style="margin-top: 1rem; font-family: monospace; font-size: 0.85rem;">
  <span class="uml-box uml-title" style="padding: 0.3rem 0.8rem;">Name</span>
  <span>&#9670;&mdash; 1 &mdash;</span>
  <span class="uml-box uml-title" style="padding: 0.3rem 0.8rem;">Student</span>
  <span>&#9671;&mdash; 1..3 &mdash;</span>
  <span class="uml-box uml-title" style="padding: 0.3rem 0.8rem;">Address</span>
</div>

<div style="text-align:center; font-size: 0.75rem; color:#6b7280; margin-top:0.4rem;">&#9670; = 합성 &nbsp;&nbsp; &#9671; = 집합 &nbsp;&nbsp; (<code>Student</code>는 <code>Name name;</code>과 <code>Address address;</code>를 가짐)</div>

---
layout: prism
heading: "객체 합성 (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 집합은 [같은 클래스]{.hl}의 객체 사이에서도 나타날 수 있습니다.

- `Person` 클래스는 그 자신이 `Person`인 `supervisor`를 포함할 수 있습니다.

- 클래스의 배열도 마찬가지로 합성될 수 있습니다.

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
heading: "클래스 설계 지침"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [결합성(Cohesion)]{.hl}
  - 클래스는 *단일* 요소를 중심으로 설계되어야 합니다.

- [일관성(Consistency)]{.hl}
  - 표준 프로그래밍 형식 및 이름 명명 규칙을 따르고, 의미 있는 이름을 사용해야 합니다.

- [캡슐화(Encapsulation)]{.hl}
  - 클라이언트의 직접 접근으로부터 데이터를 숨겨야 합니다.

- [명확성(Clarity)]{.hl}
  - 설명하고 이해하기 쉬운 명확한 규칙을 따라야 합니다.

- [완성도(Completeness)]{.hl}
  - 폭넓은 사용자와 상황을 위해 설계해야 합니다.

---
layout: prism
heading: "객체지향 프로그래밍 원칙 (SOLID)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [단일 책임 원칙 (SRP)]{.hl}
  - 객체는 오직 하나의 책임만 가져야 합니다.

- [개방-폐쇄 원칙 (OCP)]{.hl}
  - 객체는 확장에 대해서는 개방적이고, 수정에 대해서는 폐쇄적이어야 합니다.

- [리스코프 치환 원칙 (LSP)]{.hl}
  - 자식 클래스는 언제나 부모 클래스를 대체할 수 있어야 합니다.

- [인터페이스 분리 원칙 (ISP)]{.hl}
  - 클라이언트는 사용하지 않는 메소드에 의존해서는 안 됩니다.

- [의존성 역전 원칙 (DIP)]{.hl}
  - 추상성이 높고 안정적인 고수준 클래스는 구체적이고 불안정한 저수준 클래스에 의존해서는 안 됩니다.

---
layout: prism
heading: "DIY_W12"
---

- 아래 UML 다이어그램을 토대로 `StackOfIntegers`를 *정의*하고, *구현*하고, *테스트*해보세요.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<div class="uml-box">
  <div class="uml-title">StackOfIntegers</div>
  <div class="uml-row uml-sep">-elements[100]: int<br/>-size: int</div>
  <div class="uml-row uml-sep">+StackOfIntegers()<br/>+isEmpty(): bool const<br/>+peek(): int const<br/>+push(value: int): void<br/>+pop(): int<br/>+getSize(): int const</div>
</div>

</div>
<div style="font-size: 0.8rem; color:#374151;">

- `elements[100]` — 정수를 저장하는 배열.
- `size` — 스택에 담긴 정수의 개수.
- `StackOfIntegers()` — 빈 스택을 생성.
- `isEmpty()` — 스택이 비어 있으면 `true`.
- `peek()` — 제거하지 않고 최상단 정수를 반환.
- `push(value)` — 정수를 최상단에 저장.
- `pop()` — 최상단 정수를 제거하고 반환.
- `getSize()` — 요소의 개수.

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

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
