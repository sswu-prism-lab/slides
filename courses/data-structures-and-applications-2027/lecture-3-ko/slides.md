---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 3 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-3/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">자료구조실습</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">3주차: 온라인 저지와 C++ 실습</p>

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
heading: 온라인 저지와 C++ 실습
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 이번 주에는 이론에서 잠시 벗어나 실제 실습 도구를 직접 다뤄봅니다:

  - C++를 온라인에서 작성하고 실행하는 곳: OnlineGDB 같은 [온라인 컴파일러]{.hl}.

  - 연습하는 곳: [온라인 저지]{.hl}와 코딩 테스트 사이트 (백준, 프로그래머스, CodeSignal).

  - 실제 문제를 풀기 위해 필요한 [C++ 기본 요소]{.hl} — `if`, `for`, `vector`, `stack`, `queue`, `string`, `sort` — 를 빠르게 훑어봅니다.

  - 여섯 개의 [코딩 테스트 예제 문제]{.hl}를 각각 샘플 입력으로 구동되는 실행 가능한 C++ 프로그램으로 풀어봅니다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">온라인 도구와 저지</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">온라인 C++ 컴파일러</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">온라인 코딩 테스트 사이트</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">저지 세션 예시</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ 기본 요소</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">코딩 테스트 예제 문제</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">DIY 실습</span></p>
  </div>

</div>

---
layout: prism
heading: 온라인 C++ 컴파일러
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [온라인 컴파일러]{.hl}를 사용하면 별도의 로컬 개발 환경 없이 브라우저에서 바로 C++를 작성, 컴파일, 실행할 수 있습니다.

- [OnlineGDB]{.hl}는 편리한 선택지입니다: C, C++를 비롯한 여러 언어를 지원하며 대화형 디버거도 제공합니다.
  - <code>https://www.onlinegdb.com</code>

- 다른 어떤 온라인 컴파일러를 써도 무방합니다 — 원하는 것을 고르세요.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w03/dsa-w03-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 온라인 코딩 테스트 사이트
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [백준 온라인 저지]{.hl} — `https://www.acmicpc.net`
  - *문제 → 알고리즘 분류* 탭에서 유형별로 문제를 모아 볼 수 있으며, 삼성 SW 역량테스트 대비 문제집이 제공됩니다.

- [프로그래머스]{.hl} — `https://school.programmers.co.kr`
  - *코딩테스트 → 고득점 Kit* 탭에서 알고리즘별로 문제를 모아 볼 수 있으며, 카카오 코딩테스트 대비 문제집이 제공됩니다.

- [CodeSignal]{.hl} — `https://codesignal.com`
  - 영어로 되어 있으며, 외국계 회사 면접을 겨냥한 문제집을 제공합니다.

---
layout: prism
heading: 저지 세션 예시
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 일반적인 저지 페이지는 왼쪽에 [문제 설명]{.hl}, 오른쪽에 [에디터]{.hl}를 보여줍니다.

- `solution` 함수를 완성한 뒤 *Run*을 눌러 샘플에 대해 테스트하고, *Submit*을 눌러 숨겨진 테스트 케이스로 채점받습니다.

- 아래에서는 같은 문제들을 여기서 실시간 `<CppRunner>`로 다시 풀어보며, 샘플 입력을 *stdin*으로 전달합니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w03/dsa-w03-image3.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">온라인 도구와 저지</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">C++ 기본 요소</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>if</code> 문과 <code>for</code> 반복문</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>vector</code>, <code>stack</code>, <code>queue</code></span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>string</code>과 <code>sort</code></span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">코딩 테스트 예제 문제</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">DIY 실습</span></p>
  </div>

</div>

---
layout: prism
heading: "if 문"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [`if` 문]{.hl}은 프로그램이 실행 경로를 선택할 수 있게 해줍니다.

- [단방향 `if`]{.hl}는 조건이 `true`일 때에만 그 동작을 수행합니다:

```cpp
if (boolean-expression) {
    statement(s);
}
```

- 짝수/홀수 판별기를 만들어 봅시다.

</div>
<div>

<CppRunner stdin="7">

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;                 // 정수 하나 입력받기
    if (n % 2 == 0)           // 단방향 if
        cout << n << " is even\n";
    if (n % 2 != 0)
        cout << n << " is odd\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "for 반복문"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [`for` 반복문]{.hl}은 `while` 반복문을 대체할 수 있는 간결한 문법을 제공합니다:

```cpp
for (initial-action;
     loop-condition;
     action-after-each-iteration) {
    statement(s);
}
```

- 홀수 출력기를 만들어 봅시다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    // [1, 20] 범위의 홀수 출력
    for (int i = 1; i <= 20; i++)
        if (i % 2 == 1)
            cout << i << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "vector 클래스"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- C++는 객체의 목록을 저장하기 위한 제네릭 [`vector`]{.hl} 클래스를 제공합니다 (`#include <vector>`).
  - `vector<int> v;` &nbsp; `vector<string> w;`

- `string` 벡터 `["s","u","n","g","s","h","i","n"]`을 만들어 출력하고, 첫 번째 `"s"`를 `"S"`로 바꾼 뒤 다시 출력해 봅시다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> v = {"s","u","n","g","s","h","i","n"};
    for (auto& c : v) cout << c;
    cout << "\n";
    v[0] = "S";                 // 첫 번째 원소 변경
    for (auto& c : v) cout << c;
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "stack 클래스"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 제네릭 [`stack`]{.hl} 클래스 (`#include <stack>`)는 LIFO 컨테이너입니다.
  - `push(x)` 맨 위에 추가 &nbsp; `pop()` 맨 위 제거
  - `top()` 조회 &nbsp; `size()` &nbsp; `empty()`

- `1, 3, 5, 7, 9`를 push한 뒤 세 번 `pop`하면서 `top`을 살펴봅시다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    for (int x : {1, 3, 5, 7, 9}) s.push(x);
    cout << "size = " << s.size() << "\n";
    for (int i = 0; i < 3; i++) {
        cout << "top = " << s.top() << ", pop\n";
        s.pop();
    }
    cout << "top after 3 pops = " << s.top() << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "queue 클래스"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 제네릭 [`queue`]{.hl} 클래스 (`#include <queue>`)는 FIFO 컨테이너입니다.
  - `push(x)` 뒤에 추가 &nbsp; `pop()` 앞을 제거
  - `front()` 조회 &nbsp; `size()` &nbsp; `empty()`

- `"Hi","my","name","is","Gildong."`을 enqueue한 뒤 세 번 `pop`하면서 `front`를 살펴봅시다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
    queue<string> q;
    for (string w : {"Hi","my","name","is","Gildong."})
        q.push(w);
    cout << "size = " << q.size() << "\n";
    for (int i = 0; i < 3; i++) {
        cout << "front = " << q.front() << ", pop\n";
        q.pop();
    }
    cout << "front after 3 pops = " << q.front() << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "string 자료형"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- C++는 [`string`]{.hl} 자료형을 제공합니다 (`#include <string>`).
  - `append` / `insert` 로 내용 추가
  - `at(i)` 또는 `[i]` 로 문자 접근
  - `length` 는 크기를 반환 &nbsp; `substr` 는 잘라냄

- `"C++ Programming"`을 만들고 `" is fun!"`을 덧붙인 뒤, 첫 번째 문자를 읽고, 한 글자씩 출력해 봅시다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string str = "C++ Programming";
    str.append(" is fun!");
    cout << str << "\n";
    cout << "first char: " << str[0] << "\n";
    cout << "length: " << str.length() << "\n";
    for (char c : str) cout << c << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "sort 알고리즘"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 표준 [`sort`]{.hl} 알고리즘 (`#include <algorithm>`)은 범위를 제자리에서 정렬합니다.
  - `sort(v.begin(), v.end())` — *오름차순*
  - `sort(v.rbegin(), v.rend())` — *내림차순*

- `[0,8,2,3,9,1,5]`를 `v1, v2, v3`에 복사한 뒤 `v2`는 오름차순, `v3`는 내림차순으로 정렬하고, 셋 모두 출력해 봅시다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v1 = {0, 8, 2, 3, 9, 1, 5};
    vector<int> v2 = v1, v3 = v1;
    sort(v2.begin(), v2.end());    // 오름차순
    sort(v3.rbegin(), v3.rend());  // 내림차순
    for (auto* v : {&v1, &v2, &v3}) {
        for (int x : *v) cout << x << ' ';
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">온라인 도구와 저지</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ 기본 요소</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">코딩 테스트 예제 문제</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">같은 숫자는 싫어 &nbsp;·&nbsp; 올바른 괄호 &nbsp;·&nbsp; 주식가격 <span style="color:#9aa0a6;">(stack)</span></span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">기능개발 &nbsp;·&nbsp; 프로세스 &nbsp;·&nbsp; 다리를 지나는 트럭 <span style="color:#9aa0a6;">(queue)</span></span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">DIY 실습</span></p>
  </div>

</div>

---
layout: prism
heading: "같은 숫자는 싫어 — 문제"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 숫자(`0`–`9`)로 이루어진 배열 `arr`이 주어집니다. [연속으로 중복되는 값]{.hl}을 제거하고 각 연속 구간의 첫 번째 값만 남겨, 남은 수를 *순서대로* 반환하세요.

- 어떤 C++ 요소가 필요할까요? — `if`, `for`, `vector`, 그리고 [`stack`]{.hl} ADT (`push`, `top`).

<div class="theorem-box">
<div class="theorem-box-title">접근</div>
<div class="theorem-box-body">

`arr`을 원소 하나씩 스택에 넣으면서, `top()`으로 가장 최근 원소를 확인하고 그와 같은 원소는 건너뜁니다. 남긴 원소들이 답이 됩니다.

</div>
</div>

| `arr` | `answer` |
|-------|----------|
| `[1, 1, 3, 3, 0, 1, 1]` | `[1, 3, 0, 1]` |
| `[4, 4, 4, 3, 3]` | `[4, 3]` |

---
layout: prism
heading: "같은 숫자는 싫어 — 풀이"
---

<CppRunner stdin="7
1 1 3 3 0 1 1">

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    stack<int> s;
    s.push(arr[0]);                 // 첫 원소는 항상 유지
    answer.push_back(arr[0]);
    for (int i = 1; i < (int)arr.size(); i++)
        if (s.top() != arr[i]) {    // 새로운 값이 등장
            s.push(arr[i]);
            answer.push_back(arr[i]);
        }
    return answer;
}

int main() {
    int n; cin >> n;                // 원소 개수
    vector<int> arr(n);
    for (auto& x : arr) cin >> x;
    for (int x : solution(arr)) cout << x << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "기능개발 — 문제"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 각 기능에는 진행도와 하루 작업 속도가 있으며, 진행도가 `100`에 도달하면 기능이 배포됩니다. 어떤 기능은 목록에서 앞선 모든 기능과 *함께 또는 그 이후에만* 배포될 수 있습니다.

- `progresses`와 `speeds`가 주어질 때, 각 배포일에 몇 개의 기능이 배포되는지 반환하세요. `if`, `for`, `while`, `vector`, 그리고 [`queue`]{.hl} ADT를 사용합니다.

<div class="theorem-box">
<div class="theorem-box-title">접근</div>
<div class="theorem-box-body">

각 기능을 아직 필요한 일수로 변환하여 순서대로 큐에 넣습니다. 큐를 앞에서부터 훑으면서, 현재 맨 앞 기능보다 늦지 않게 끝나는 뒤쪽 기능은 같은 날 배포되고, 더 오래 걸리는 기능은 새로운 배포일을 시작합니다.

</div>
</div>

| `progresses` | `speeds` | `return` |
|--------------|----------|----------|
| `[93, 30, 55]` | `[1, 30, 5]` | `[2, 1]` |
| `[95, 90, 99, 99, 80, 99]` | `[1, 1, 1, 1, 1, 1]` | `[1, 3, 2]` |

---
layout: prism
heading: "기능개발 — 풀이"
---

<CppRunner stdin="3
93 30 55
1 30 5">

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    for (int i = 0; i < (int)progresses.size(); i++) {
        int days = 100 - progresses[i];
        // 올림 나눗셈: 나머지가 있으면 하루 더 추가
        days = days / speeds[i] + (days % speeds[i] != 0);
        q.push(days);
    }
    int day = q.front(), cnt = 1; q.pop();
    while (!q.empty()) {
        int cur = q.front(); q.pop();
        if (day >= cur) cnt++;                 // 같은 날 배포
        else { answer.push_back(cnt); cnt = 1; day = cur; }
    }
    answer.push_back(cnt);
    return answer;
}

int main() {
    int n; cin >> n;
    vector<int> progresses(n), speeds(n);
    for (auto& x : progresses) cin >> x;
    for (auto& x : speeds) cin >> x;
    for (int x : solution(progresses, speeds)) cout << x << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "올바른 괄호 — 문제"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `(`와 `)`로 이루어진 문자열 `s`는 모든 `(`가 뒤에서 짝이 되는 `)`로 닫힐 때 [올바른 괄호]{.hl}입니다. 올바르면 `true`, 아니면 `false`를 반환하세요.

- 어떤 C++ 요소가 필요할까요? — `if`, `for`, `string`, 그리고 [`stack`]{.hl} ADT (`push`, `pop`, `empty`).

<div class="theorem-box">
<div class="theorem-box-title">접근</div>
<div class="theorem-box-body">

왼쪽에서 오른쪽으로 훑습니다. `(`이면 push합니다. `)`이면 스택이 비어 있지 않아야 하며 — 짝이 되는 `(`를 pop합니다. 그렇지 않으면 문자열이 올바르지 않습니다. 끝나고 나면 스택이 비어 있어야 합니다.

</div>
</div>

| `s` | `answer` |
|-----|----------|
| `"()()"` &nbsp; `"(())()"` | `true` |
| `")()("` &nbsp; `"(()("` | `false` |

---
layout: prism
heading: "올바른 괄호 — 풀이"
---

<CppRunner stdin="4
()()
(())()
)()(
(()(">

```cpp
#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool solution(string s) {
    stack<char> st;
    for (char& c : s) {
        if (c == '(') st.push(c);       // 여는 괄호
        else {                          // 닫는 괄호
            if (st.empty()) return false;
            st.pop();
        }
    }
    return st.empty();                  // 짝 없는 괄호가 남지 않음
}

int main() {
    int t; cin >> t;                    // 테스트 문자열 개수
    while (t--) {
        string s; cin >> s;
        cout << s << " -> " << (solution(s) ? "true" : "false") << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "프로세스 — 문제"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 프린터 큐는 FIFO 순서로 프로세스를 실행하지만, 대기 중인 프로세스 가운데 *더 높은* 우선순위가 없을 때에만 실행하고, 그렇지 않으면 맨 뒤로 보냅니다. `priorities`와 `location`이 주어질 때, 그 인덱스에 있는 프로세스의 [실행 순서]{.hl}를 반환하세요.

- `if`, `while`, [`queue`]{.hl} ADT, 그리고 `sort`를 사용합니다.

<div class="theorem-box">
<div class="theorem-box-title">접근</div>
<div class="theorem-box-body">

각 프로세스를 `(원래 인덱스, 우선순위)`로 큐에 넣습니다. 우선순위를 내림차순으로 정렬해 기준으로 삼습니다. 맨 앞을 반복해서 확인하며, 더 높은 우선순위가 아직 대기 중이면 다시 큐에 넣고, 그렇지 않으면 실행(개수 셈)하고 그것이 우리가 찾는 인덱스이면 그 개수를 보고합니다.

</div>
</div>

| `priorities` | `location` | `return` |
|--------------|:---:|:---:|
| `[2, 1, 3, 2]` | `2` | `1` |
| `[1, 1, 9, 1, 1, 1]` | `0` | `5` |

---
layout: prism
heading: "프로세스 — 풀이"
---

<CppRunner stdin="6
1 1 9 1 1 1
0">

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int solution(vector<int> priorities, int location) {
    queue<pair<int,int>> q;                   // (인덱스, 우선순위)
    for (int i = 0; i < (int)priorities.size(); i++)
        q.push({i, priorities[i]});
    sort(priorities.rbegin(), priorities.rend());  // 내림차순 기준

    int answer = 0, idx = 0;
    while (!q.empty()) {
        auto cur = q.front(); q.pop();
        if (cur.second < priorities[idx]) {   // 더 높은 우선순위가 대기 중
            q.push(cur);
        } else {                              // 실행
            answer++;
            idx++;
            if (cur.first == location) return answer;
        }
    }
    return answer;
}

int main() {
    int n; cin >> n;
    vector<int> priorities(n);
    for (auto& x : priorities) cin >> x;
    int location; cin >> location;
    cout << solution(priorities, location) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "다리를 지나는 트럭 — 문제"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 트럭들이 순서대로 1차선 다리를 건넙니다. 다리는 트럭 `bridge_length`대를 수용하며 총 무게는 최대 `weight`까지입니다. 매 시간 단위마다 모든 트럭이 한 칸씩 전진합니다. 모든 트럭이 건너는 데 걸리는 [총 시간]{.hl}을 반환하세요.

- `if`, `while`, 그리고 [`queue`]{.hl} ADT를 사용합니다 — 여기서는 *다리 자체*를 큐로 모델링합니다.

<div class="theorem-box">
<div class="theorem-box-title">접근</div>
<div class="theorem-box-body">

다리 칸을 나타내는 길이 `bridge_length`의 큐를 유지합니다 (`0`은 빈 칸을 의미). 매 단계: 시간을 증가시키고, 반대편 끝에서 빠져나가는 트럭을 내보내며, 들어오는 트럭이 무게 제한 안에 들어가면 push하고 그렇지 않으면 `0`을 push합니다.

</div>
</div>

| `bridge_length` | `weight` | `truck_weights` | `return` |
|:---:|:---:|:---|:---:|
| `2` | `10` | `[7, 4, 5, 6]` | `8` |
| `100` | `100` | `[10]` | `101` |

---
layout: prism
heading: "다리를 지나는 트럭 — 풀이"
---

<CppRunner stdin="2 10
4
7 4 5 6">

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0, idx = 0, sum = 0;
    queue<int> bridge;                              // 현재 다리 위의 트럭
    while (true) {
        if (idx == (int)truck_weights.size()) {     // 모든 트럭이 진입 완료
            answer += bridge_length;                // 마지막 트럭이 건넘
            break;
        }
        answer++;                                   // 시간 한 단위
        if ((int)bridge.size() == bridge_length) {  // 반대편 끝에서 트럭이 빠져나감
            sum -= bridge.front(); bridge.pop();
        }
        int tmp = truck_weights[idx];
        if (sum + tmp <= weight) {                  // 여유 용량 충분
            sum += tmp; bridge.push(tmp); idx++;
        } else {
            bridge.push(0);                         // 빈 칸, 대기만
        }
    }
    return answer;
}

int main() {
    int bridge_length, weight, n;
    cin >> bridge_length >> weight >> n;
    vector<int> truck_weights(n);
    for (auto& x : truck_weights) cin >> x;
    cout << solution(bridge_length, weight, truck_weights) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "주식가격 — 문제"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 초 단위 `prices`가 주어질 때, 각 초마다 가격이 [떨어지지 않은]{.hl} 시간이 몇 초인지 (즉, 처음으로 더 낮은 가격이 나오는 순간까지, 또는 끝까지) 보고하세요.

- 어떤 C++ 요소가 필요할까요? — `if`, `for`, `while`, 그리고 [`stack`]{.hl} ADT.

<div class="theorem-box">
<div class="theorem-box-title">접근</div>
<div class="theorem-box-body">

답이 아직 정해지지 않은 *인덱스*들을 스택에 유지합니다. 시각 `i`의 가격이 스택에 있는 인덱스 `j`의 가격보다 낮아지면, `j`의 하락이 지금 발생한 것이므로 그 답은 `i - j`가 되고 pop합니다. 스택에 남은 인덱스들은 끝까지 떨어지지 않은 것이므로 답은 끝까지의 시간이 됩니다.

</div>
</div>

| `prices` | `return` |
|----------|----------|
| `[1, 2, 3, 2, 3]` | `[4, 3, 1, 1, 0]` |

---
layout: prism
heading: "주식가격 — 풀이"
---

<CppRunner stdin="5
1 2 3 2 3">

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> solution(vector<int> prices) {
    int n = prices.size();
    vector<int> answer(n);
    stack<int> s;                       // 답이 아직 정해지지 않은 인덱스
    for (int i = 0; i < n; i++) {
        while (!s.empty() && prices[s.top()] > prices[i]) {
            answer[s.top()] = i - s.top();   // 가격이 지금 떨어짐
            s.pop();
        }
        s.push(i);
    }
    while (!s.empty()) {                // 끝까지 안 떨어짐: 끝까지 계산
        answer[s.top()] = n - 1 - s.top();
        s.pop();
    }
    return answer;
}

int main() {
    int n; cin >> n;
    vector<int> prices(n);
    for (auto& x : prices) cin >> x;
    for (int x : solution(prices)) cout << x << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "과제 — HW_W03"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 백준, 프로그래머스, 혹은 문제집 등 원하는 코딩 테스트 연습 수단을 자유롭게 이용하세요. 수업 시간에 다룬 프로그래머스 6개 문제는 *제외*합니다.

- 리스트, 스택, 또는 큐가 쓰인 [문제 3개]{.hl}를 찾아 풀어보세요. 다른 자료구조나 알고리즘을 추가로 사용하는 것은 전혀 문제되지 않습니다.

- 각 문제에 대해 [문제]{.hl}, [풀이 코드]{.hl}, [테스트 결과]{.hl}를 캡처하여 한글 또는 워드 문서에 붙여넣으세요.
  - 공개된 해답을 보지 않고 스스로 풀어보길 바랍니다.
  - 시간이 부족하더라도 통과하지 못한 자신의 정직한 풀이를 제출하면 만점으로 인정합니다.

- `HW_03_20XXXXXX.pdf`로 저장 후 LMS에 업로드하세요.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">온라인 도구와 저지</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ 기본 요소</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">코딩 테스트 예제 문제</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">DIY 실습</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">원형 연결 리스트 &nbsp;·&nbsp; 이중 연결 리스트 노드 삭제</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">왕실의 나이트 &nbsp;·&nbsp; 후위 표기식 계산</span></p>
  </div>

</div>

---
layout: prism
heading: "DIY: 연결 리스트가 원형인가?"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int data; Node* next; Node(int d) : data(d), next(nullptr) {} };

// 플로이드의 순환 탐지: slow는 1칸, fast는 2칸씩 이동.
bool isCircular(Node* head) {
    if (!head) return false;
    Node* slow = head;
    Node* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;   // 포인터가 만나면 => 순환
    }
    return false;
}

int main() {
    Node* a = new Node(1); Node* b = new Node(2); Node* c = new Node(3);
    Node* d = new Node(4); Node* e = new Node(5);
    a->next = b; b->next = c; c->next = d; d->next = e;
    cout << "linear list: " << (isCircular(a) ? "circular" : "not circular") << "\n";
    e->next = c;                          // 꼬리를 노드 3에 다시 연결
    cout << "after cycle: " << (isCircular(a) ? "circular" : "not circular") << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY: 노드 삭제 (이중 연결 리스트)"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int data; Node* prev; Node* next; Node(int d) : data(d), prev(nullptr), next(nullptr) {} };

struct DoublyList {
    Node* head = nullptr;
    void push_back(int v) {
        Node* n = new Node(v);
        if (!head) { head = n; return; }
        Node* t = head; while (t->next) t = t->next;
        t->next = n; n->prev = t;
    }
    void remove(int val) {
        for (Node* temp = head; temp; temp = temp->next) {
            if (temp->data != val) continue;
            if (!temp->prev) { head = temp->next; if (head) head->prev = nullptr; }       // 머리
            else if (!temp->next) { temp->prev->next = nullptr; }                          // 꼬리
            else { temp->prev->next = temp->next; temp->next->prev = temp->prev; }         // 중간
            delete temp; return;
        }
    }
    void print() { for (Node* t = head; t; t = t->next) cout << t->data << ' '; cout << "\n"; }
};

int main() {
    DoublyList L;
    for (int x : {10, 20, 30, 40, 50}) L.push_back(x);
    cout << "initial:   "; L.print();
    L.remove(30); cout << "remove 30: "; L.print();
    L.remove(10); cout << "remove 10: "; L.print();
    L.remove(50); cout << "remove 50: "; L.print();
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY: 왕실의 나이트"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `8 × 8` 판 위에서 나이트는 [L자 모양]{.hl}으로 움직이며 판을 벗어날 수 없습니다.

- `A1`이나 `D4` 같은 칸이 주어질 때, 나이트가 이동할 수 있는 경우의 수를 출력하세요.
  - `A1` &rarr; `2` &nbsp;&nbsp; `D4` &rarr; `8`

- 여덟 개의 후보 이동을 모두 확인하고 판 안에 남는 경우를 셉니다.

</div>
<div>

<CppRunner stdin="A1
D4">

```cpp
#include <iostream>
#include <string>
using namespace std;

int knightMoves(const string& pos) {
    int col = pos[0] - 'A';       // 0..7
    int row = pos[1] - '1';       // 0..7
    int dc[] = {1, 1,-1,-1, 2, 2,-2,-2};
    int dr[] = {2,-2, 2,-2, 1,-1, 1,-1};
    int count = 0;
    for (int k = 0; k < 8; k++) {
        int nc = col + dc[k], nr = row + dr[k];
        if (nc >= 0 && nc < 8 && nr >= 0 && nr < 8)
            count++;
    }
    return count;
}

int main() {
    string in;
    while (cin >> in)
        cout << in << " -> " << knightMoves(in) << "\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "DIY: 후위 표기식 계산"
---

<div style="height: 0.2rem;"></div>

<CppRunner stdin="23+4*
95-2*">

```cpp
#include <iostream>
#include <string>
#include <stack>
#include <cctype>
using namespace std;

bool isOperator(char c) { return c == '+' || c == '-' || c == '*' || c == '/'; }

int performOperation(char op, int a, int b) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return a / b;
        default:  return 0;
    }
}

int evaluatePostfix(const string& expr) {
    stack<int> s;
    for (char c : expr) {
        if (isdigit(c)) s.push(c - '0');           // 피연산자
        else if (isOperator(c)) {                  // 위쪽 두 개에 적용
            int op2 = s.top(); s.pop();
            int op1 = s.top(); s.pop();
            s.push(performOperation(c, op1, op2));
        }
    }
    return s.top();
}

int main() {
    string expr;
    while (cin >> expr)                            // 예: 23+4* 는 (2+3)*4 를 의미
        cout << expr << " = " << evaluatePostfix(expr) << "\n";
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
