---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 6 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-6/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">6주차: 리스트 ADT와 C++ 컨테이너</p>

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
heading: 개요
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 이번 강의에서는 핵심적인 선형 및 계층형 자료구조와 그에 대응하는 C++ 표준 라이브러리 컨테이너를 살펴봅니다:

  - [리스트 ADT]{.hl}와 그 [배열]{.hl} 구현 및 [연결]{.hl} 구현.

  - [스택]{.hl}, [큐]{.hl}, [덱]{.hl} — 제한된 리스트 — 을 `stack`, `queue`, `deque`로.

  - [트리]{.hl}, [힙]{.hl}, [우선순위 큐]{.hl}, 그리고 완전 이진 트리를 배열로 바라보는 관점.

  - [그래프]{.hl}와 그 순회(DFS, BFS), 신장 트리 / 최단 경로 알고리즘.

---
layout: prism
heading: 리스트 ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [리스트]{.hl}는 원소들의 순서 있는 나열 $a_0, a_1, \ldots, a_{N-1}$ 입니다.

- 모든 [추상 자료형]{.hl}(ADT)과 마찬가지로, 리스트는 저장 방식이 아니라 그것이 지원하는 *연산*으로 정의됩니다.

- 어떤 구체적인 구현(배열, 연결 리스트, ...)이든 이 연산들을 제공해야 합니다.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">리스트 ADT 연산</div>
<div class="theorem-box-body">

- `printList` — 리스트를 출력
- `makeEmpty` — 리스트를 비움
- `insert` — 위치 `i`에 `x`를 삽입
- `remove` — `i`번째 원소(또는 `x`)를 삭제
- `find` — 원소 `x`의 인덱스
- `findKth` — 주어진 인덱스의 원소
- `size` — 원소의 개수
- ... 그 밖에 필요한 것(예: `sort`).

</div>
</div>

</div>
</div>

---
layout: prism
heading: 리스트의 배열 구현
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 리스트를 *연속된* 배열에 저장하면 `findKth`가 $O(1)$ 연산이 됩니다.

- 그 대가로 `insert`와 `remove`는 $O(N)$입니다: 배열을 연속적으로 유지하기 위해 원소들을 [이동]{.hl}시켜야 하기 때문입니다.

<div style="margin-top: 1rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 1.05rem; line-height: 2.1;">
  <div><span style="color:#9aa0a6;">start&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> [ 10 &nbsp; 3 &nbsp; 21 &nbsp; 83 &nbsp; 34 ]</div>
  <div><span style="color:#4a6fa5;">insert(1, 77)</span> [ 10 &nbsp; <span style="color:#c2410c; font-weight:bold;">77</span> &nbsp; 3 &nbsp; 21 &nbsp; 83 &nbsp; 34 ]</div>
  <div><span style="color:#4a6fa5;">remove(0)&nbsp;&nbsp;&nbsp;&nbsp;</span> [ 77 &nbsp; 3 &nbsp; 21 &nbsp; 83 &nbsp; 34 ]</div>
</div>

---
layout: prism
heading: "DIY: 배열 기반 리스트"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct List {                      // 작은 배열 기반 리스트 ADT
    vector<int> a;
    void insert(int i, int x) { a.insert(a.begin() + i, x); } // O(N): 오른쪽으로 이동
    void remove(int i)        { a.erase(a.begin() + i); }     // O(N): 왼쪽으로 이동
    int  findKth(int i) const { return a[i]; }                // O(1)
    int  find(int x) const {                                  // x의 인덱스, 없으면 -1
        for (int i = 0; i < (int)a.size(); i++) if (a[i] == x) return i;
        return -1;
    }
    int  size() const { return a.size(); }
    void printList() const { for (int x : a) cout << x << " "; cout << "\n"; }
};

int main() {
    List L{{10, 3, 21, 83, 34}};
    cout << "start        : "; L.printList();
    L.insert(1, 77);   cout << "insert(1,77) : "; L.printList();
    L.remove(0);       cout << "remove(0)    : "; L.printList();
    cout << "find(21)     : " << L.find(21) << "\n";
    cout << "findKth(2)   : " << L.findKth(2) << "\n";
    cout << "size         : " << L.size() << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "C++ Array와 vector 클래스"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 내장 [배열]{.hl}은 컴파일 시점에 크기가 고정됩니다; 다차원 배열도 지원됩니다.

- [`vector`]{.hl} 클래스(`<vector>`에 있음)는 *크기 조절이 가능한* 배열입니다: `push_back`, `pop_back`, `size`, 그리고 `[]`를 통한 인덱싱.

- `vector`는 다루기 까다로운 내장 배열을 대체하는 표준적인 방법입니다.

</div>
<div>

```cpp
// array
int    myArr1[6];
myArr1[0] = 1;
double myArr2[4] = {0.1, 0.2, 0.3, 0.4};
int    myArr3[4][3] =
    {{0,1,6}, {2,9,4}, {3,1,7}, {5,2,7}};

// vector, needs #include <vector>
vector<int> v;
v.push_back(10);
v.push_back(20);
v.push_back(30);
v.push_back(40);
cout << v.size() << endl; // 4
v.pop_back();
cout << v.size() << endl; // 3
cout << v[0] << endl;     // 10
```

</div>
</div>

---
layout: prism
heading: "DIY: array vs. vector"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    double myArr2[4] = {0.1, 0.2, 0.3, 0.4};
    int    myArr3[4][3] = {{0,1,6}, {2,9,4}, {3,1,7}, {5,2,7}};
    cout << "myArr2[2]   = " << myArr2[2] << "\n";        // 0.3
    cout << "myArr3[1][2]= " << myArr3[1][2] << "\n";     // 4

    vector<int> v;
    for (int x : {10, 20, 30, 40}) v.push_back(x);
    cout << "size        = " << v.size() << "\n";         // 4
    v.pop_back();
    cout << "size        = " << v.size() << "\n";         // 3
    cout << "v[0]        = " << v[0] << endl;              // 10
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 단순 연결 리스트
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- `insert`와 `remove`의 선형 비용을 피하려면 리스트를 연속적으로 저장하지 *않아야* 합니다.

- [연결 리스트]{.hl}는 메모리상에서 반드시 인접하지는 않은 [노드]{.hl}들의 연속입니다. 각 노드는 원소 하나와 그 다음 노드를 가리키는 [링크]{.hl}(포인터)를 담으며, 마지막 노드의 링크는 `nullptr`입니다.

<div style="margin-top: 0.8rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 1.05rem;">
  <span style="color:#9aa0a6;">head&nbsp;→</span>
  [ 10 |·]→ [ 3 |·]→ [ 21 |·]→ [ 83 |·]→ [ 34 |<span style="color:#c2410c;">/</span>]
</div>

---
layout: prism
heading: "DIY: 단일 연결 리스트 만들기"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int data; Node* next; };

int main() {
    Node* head = nullptr;
    int vals[] = {34, 83, 21, 3, 10};     // 앞에 삽입 -> 순서가 뒤집힘
    for (int x : vals) head = new Node{x, head};

    for (Node* p = head; p != nullptr; p = p->next) // 순회
        cout << p->data << (p->next ? " -> " : "\n");

    // 노드 해제
    while (head) { Node* t = head; head = head->next; delete t; }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 포인터
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [포인터]{.hl}는 다른 변수의 *주소*를 저장하는 변수입니다: `datatype *pointerName`.

- [`&`]{.hl} 연산자는 변수의 주소를 주고, [`*`]{.hl} 연산자는 포인터를 역참조하여 그것이 가리키는 변수를 얻습니다.

- 포인터를 통해 값을 쓰면(`*a = 1`) 가리켜지는 변수 `b`가 바뀝니다.

</div>
<div>

```cpp
int *a;
int  b = 3;

a = &b;                 // a는 b의 주소를 담는다
cout << b << endl;      // 3

*a = 1;                 // 포인터를 통해 값을 쓴다
cout << b << endl;      // 1  (b가 바뀜!)
```

</div>
</div>

---
layout: prism
heading: "DIY: 포인터 실습"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int b = 3;
    int* a = &b;                    // a는 b를 가리킨다
    cout << "b       = " << b  << "\n";   // 3
    cout << "*a      = " << *a << "\n";   // 3
    *a = 1;                          // 포인터를 통해 값을 쓴다
    cout << "after *a = 1, b = " << b << endl; // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 원형 연결 리스트
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [원형 연결 리스트]{.hl}에서는 마지막 노드의 링크가 `nullptr` 대신 *다시 head를 가리킵니다*.

- 순회를 어디서든 시작해 끝없이 돌 수 있어 — 라운드 로빈 스케줄링이나 요세푸스 같은 문제에 유용합니다.

<div style="margin-top: 0.8rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 1.05rem;">
  <span style="color:#9aa0a6;">head&nbsp;→</span>
  [ 10 |·]→ [ 3 |·]→ [ 21 |·]→ [ 83 |·]→ [ 34 |·]<span style="color:#c2410c;">─┐</span><br/>
  <span style="color:#c2410c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──────────────────────────────────────────┘</span>
</div>

---
layout: prism
heading: "DIY: 원형 리스트 순회"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int data; Node* next; };

int main() {
    int vals[] = {10, 3, 21, 83, 34};
    Node* head = new Node{vals[0], nullptr};
    Node* tail = head;
    for (int i = 1; i < 5; i++) { tail->next = new Node{vals[i], nullptr}; tail = tail->next; }
    tail->next = head;                       // 원을 닫는다

    Node* p = head;                          // 두 바퀴 돈다
    for (int step = 0; step < 10; step++) { cout << p->data << " "; p = p->next; }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 이중 연결 리스트
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 단일 연결 리스트나 원형 연결 리스트의 노드들은 한 방향으로만 연결되어 있습니다: 임의의 노드가 주어졌을 때 *뒤로* 돌아갈 수 없습니다.

- [이중 연결 리스트]{.hl}에서는 각 노드가 앞 노드와 뒤 노드 모두에 연결되어 있어 양방향으로 순회할 수 있습니다. 또한 원형으로 만들 수도 있습니다.

<div style="margin-top: 0.8rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 1.05rem;">
  <span style="color:#9aa0a6;">head&nbsp;⇄</span>
  [ 10 ]⇄ [ 3 ]⇄ [ 21 ]⇄ [ 83 ]⇄ [ 34 ]
</div>

---
layout: prism
heading: "DIY: 이중 연결 리스트 (std::list)"
---

<CppRunner>

```cpp
#include <iostream>
#include <list>
using namespace std;

int main() {
    list<int> L = {10, 3, 21, 83, 34};   // std::list는 이중 연결이다

    cout << "forward : ";
    for (auto it = L.begin(); it != L.end(); ++it) cout << *it << " ";
    cout << "\nreverse : ";
    for (auto it = L.rbegin(); it != L.rend(); ++it) cout << *it << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 스택 ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [스택]{.hl}은 삽입과 삭제가 오직 한쪽 끝, 즉 [top]{.hl}에서만 일어나도록 제한된 리스트입니다.

- 스택은 [LIFO]{.hl}(last in, first out) 리스트입니다 — 오직 top 원소에만 접근할 수 있습니다.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">스택 ADT 연산</div>
<div class="theorem-box-body">

- `push` — top에 원소를 추가
- `top` — top 원소를 읽음
- `pop` — top 원소를 삭제
- ... 그 밖의 것(예: `popAll`).

</div>
</div>

<div style="margin-top: 1rem; font-family: 'JetBrains Mono', Consolas, monospace; text-align:center;">
  top → [ 10 ]<br/>[ 77 ]<br/>[ &nbsp;3 ]<br/>[ 21 ]<br/>[ 83 ]<br/>[ 34 ]
</div>

</div>
</div>

---
layout: prism
heading: "C++ stack 클래스"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [`stack`]{.hl} 클래스(`<stack>`에 있음)는 `push`, `top`, `pop`, `size`, `empty`를 제공합니다.

- 대표적인 응용: [괄호 검사]{.hl}, [후위 표기식 계산]{.hl}, 그리고 [깊이 우선 탐색]{.hl} 알고리즘.

```cpp
stack<int> s;              // needs #include <stack>
s.push(3); s.push(2); s.push(1);
cout << s.top() << " " << s.size() << endl;  // 1 3
s.pop();
cout << s.top() << " " << s.empty() << endl; // 2 0 (false)
```

---
layout: prism
heading: "DIY: 스택 — 괄호 검사기"
---

<CppRunner>

```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool balanced(const string& s) {
    stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') st.push(c);
        else if (c == ')' || c == ']' || c == '}') {
            if (st.empty()) return false;
            char o = st.top(); st.pop();
            if ((c==')'&&o!='(') || (c==']'&&o!='[') || (c=='}'&&o!='{')) return false;
        }
    }
    return st.empty();
}

int main() {
    for (string t : {"(a[b]{c})", "([)]", "(()"})
        cout << t << " -> " << (balanced(t) ? "balanced" : "not balanced") << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 큐 ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [큐]{.hl}는 삽입이 [rear]{.hl}(뒤)에서, 삭제가 [front]{.hl}(앞)에서 일어나는 리스트입니다.

- 큐는 [FIFO]{.hl}(first in, first out) 리스트입니다 — 뒤에서 삽입하고 앞에서 삭제합니다.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">큐 ADT 연산</div>
<div class="theorem-box-body">

- `push` — rear에 원소를 추가
- `front` — front 원소를 읽음
- `pop` — front 원소를 삭제
- ... 그 밖의 것(예: `popAll`).

</div>
</div>

<div style="margin-top: 1rem; font-family: 'JetBrains Mono', Consolas, monospace; text-align:center;">
  front → [ 34 | 83 | 21 | 3 | 77 | 10 ] ← rear
</div>

</div>
</div>

---
layout: prism
heading: "C++ queue 클래스"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [`queue`]{.hl} 클래스(`<queue>`에 있음)는 `push`, `front`, `pop`, `size`, `empty`를 제공합니다.

- 대표적인 응용은 [요세푸스 문제]{.hl}로, 큐를 회전시켜 손쉽게 시뮬레이션할 수 있습니다.

```cpp
queue<int> q;              // needs #include <queue>
q.push(3); q.push(2); q.push(1);
cout << q.front() << " " << q.size() << endl;  // 3 3
q.pop();
cout << q.front() << " " << q.empty() << endl; // 2 0 (false)
```

---
layout: prism
heading: "DIY: 큐 — 요세푸스 문제"
---

<CppRunner>

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n = 7, k = 3;             // 원형으로 선 n명, 매 k번째 사람 제거
    queue<int> q;
    for (int i = 1; i <= n; i++) q.push(i);

    cout << "elimination order: ";
    while (!q.empty()) {
        for (int i = 1; i < k; i++) { q.push(q.front()); q.pop(); } // k-1명 건너뜀
        cout << q.front() << " ";                                    // k번째 제거
        q.pop();
    }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 덱 (Double Ended Queue)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [덱]{.hl}(double-ended queue)은 큐를 확장하여 삽입과 삭제가 앞과 뒤 *양쪽* 끝에서 모두 일어날 수 있게 한 것입니다.

- 덱은 [원형 큐]{.hl} 위에 구현할 수 있습니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w06/dsa-w06-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "C++ deque 클래스"
---

<CppRunner>

```cpp
#include <iostream>
#include <deque>
using namespace std;

deque<int> dq;             // needs #include <deque>
void print_dq() { for (size_t i = 0; i < dq.size(); i++) cout << dq.at(i) << " "; cout << "\n"; }

int main() {
    dq.push_back(1); dq.push_back(2); dq.push_back(3);
    print_dq();                              // 1 2 3
    dq.insert(dq.begin() + 1, 4);
    print_dq();                              // 1 4 2 3
    dq.pop_front(); dq.pop_back();
    print_dq();                              // 4 2
    dq.push_front(5); dq.push_back(6);
    print_dq();                              // 5 4 2 6
    dq.clear();
    print_dq();                              // (empty)
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 트리, 이진 트리, 힙
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [트리]{.hl}는 노드들의 계층 구조이며, [이진 트리]{.hl}는 각 노드가 최대 두 개의 자식을 갖게 한 것입니다.

- [정 이진 트리]{.hl}(full binary tree)는 모든 노드가 자식을 $0$개 또는 $2$개 갖는 트리이고, [완전 이진 트리]{.hl}(complete binary tree)는 레벨별로 왼쪽부터 오른쪽으로 채워진 트리입니다.

- [힙]{.hl}은 [힙 순서 성질]{.hl}을 만족하는 완전 이진 트리입니다: [최대 힙]{.hl}에서는 모든 부모가 자식보다 $\geq$이며(따라서 최댓값이 루트에 위치).

---
layout: prism
heading: 완전 이진 트리 구현
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [리스트]{.hl}(배열)는 포인터 없이도 완전 이진 트리를 깔끔하게 표현합니다.

- [1-기반 인덱스]{.hl}를 사용하면(우리는 `A[0]`을 건너뜀), 인덱스 `i`의 원소에 대해:

<div class="sub-item-enum">

1. 왼쪽 자식은 `2i`에 &nbsp;(0-기반에서는 `2i+1`)
2. 오른쪽 자식은 `2i+1`에 &nbsp;(0-기반에서는 `2i+2`)
3. 부모는 `i/2`에 &nbsp;(0-기반에서는 `(i-1)/2`)

</div>

</div>
<div>

<div style="font-family: 'JetBrains Mono', Consolas, monospace; font-size: 0.95rem; text-align:center; margin-top: 1rem;">
  A[1]<br/>
  &nbsp;&nbsp;2<br/>
  &nbsp;&nbsp;╱ ╲<br/>
  &nbsp;7 &nbsp;&nbsp;5<br/>
  ╱╲ &nbsp;&nbsp;╱╲<br/>
  2 6 &nbsp;9 4<br/>
</div>

<div style="margin-top: 1rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 0.95rem; text-align:center;">
  index&nbsp;&nbsp;1 2 3 4 5 6 7 …<br/>
  A&nbsp;&nbsp;&nbsp;&nbsp;[ 2 7 5 2 6 9 4 … ]
</div>

</div>
</div>

---
layout: prism
heading: "DIY: 완전 이진 트리의 배열 관점"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    // 1-기반: A[0]은 사용하지 않음; 트리의 레벨 순서 값
    int A[] = {0, 2, 7, 5, 2, 6, 9, 4, 10, 5, 11, 3, 0};
    int n = 12;

    for (int i = 1; i <= 3; i++) {
        cout << "A[" << i << "]=" << A[i]
             << "  left=A[" << 2*i << "]=" << A[2*i]
             << "  right=A[" << 2*i+1 << "]=" << A[2*i+1] << "\n";
    }
    cout << "parent of A[8]=" << A[8] << " is A[" << 8/2 << "]=" << A[8/2] << "\n";

    cout << "level-order: ";
    for (int i = 1; i <= n; i++) cout << A[i] << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 우선순위 큐 ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [우선순위 큐]{.hl}는 항상 우선순위가 가장 높은 원소(여기서는 [최댓값]{.hl})를 먼저 꺼낼 수 있게 합니다.

- 이는 [이진 힙]{.hl}으로 구현되어, 삽입과 최댓값 삭제가 $O(\log N)$입니다.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">우선순위 큐 ADT 연산</div>
<div class="theorem-box-body">

- `insert` — 원소를 삽입
- `deleteMax` — 최댓값을 삭제
- `max` — 최댓값을 읽음
- `isEmpty` — 비었는지 검사
- `clear` — 큐를 비움

</div>
</div>

</div>
</div>

---
layout: prism
heading: "DIY: 이진 최대 힙"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> h = {0};                 // 1-기반 힙; h[0]은 미사용

void insert(int x) {                 // 위로 올리기 (percolate up)
    h.push_back(x);
    int i = h.size() - 1;
    while (i > 1 && h[i/2] < h[i]) { swap(h[i/2], h[i]); i /= 2; }
}
int deleteMax() {                    // 아래로 내리기 (percolate down)
    int top = h[1]; h[1] = h.back(); h.pop_back();
    int i = 1, n = h.size() - 1;
    while (2*i <= n) {
        int c = 2*i; if (c < n && h[c+1] > h[c]) c++;
        if (h[i] >= h[c]) break;
        swap(h[i], h[c]); i = c;
    }
    return top;
}

int main() {
    for (int x : {3, 9, 2, 7, 1, 8, 5}) insert(x);
    cout << "extract max in order: ";
    while (h.size() > 1) cout << deleteMax() << " ";
    cout << endl;                    // 9 8 7 5 3 2 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "C++ priority_queue 클래스"
---

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    priority_queue<int> pq1;                 // 최대 힙 (기본값)
    pq1.push(1); pq1.push(9); pq1.push(3);
    cout << pq1.top() << "\n";               // 9

    priority_queue<pair<int,int>> pq2;       // .first 다음 .second 순으로 정렬
    pq2.push({1,2}); pq2.push({1,3}); pq2.push({3,2});
    cout << pq2.top().first << " " << pq2.top().second << "\n"; // 3 2

    priority_queue<int, vector<int>, greater<int>> pq3; // 최소 힙
    pq3.push(1); pq3.push(9); pq3.push(3);
    cout << pq3.top() << endl;               // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 그래프
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [그래프]{.hl}는 데이터를 [정점]{.hl}(노드)과 그것을 잇는 [간선]{.hl}으로 표현합니다.

- 그래프는 도시 간 경로, 웹사이트 간 하이퍼링크, 사람 사이의 관계, 뇌세포 간 연결 등 매우 다양한 것을 모델링합니다.

- [방향]{.hl}, [무방향]{.hl}, [가중치]{.hl} 그래프가 있습니다.

<div style="margin-top: 0.6rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 1.05rem;">
  G = { A, B, C, (A, B), (A, C), (B, C) }
</div>

---
layout: prism
heading: 그래프 구현
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 그래프는 [인접 행렬]{.hl}로 저장할 수 있습니다: 노드 $i$가 노드 $j$와 연결되어 있으면 $(i, j)$ 성분이 $1$, 아니면 $0$입니다.

- 무방향 그래프에서는 행렬이 [대칭]{.hl}입니다.

</div>
<div>

<div style="font-family: 'JetBrains Mono', Consolas, monospace; font-size: 0.95rem; text-align:center; margin-top: 0.5rem; line-height: 1.6;">
  &nbsp;&nbsp;&nbsp;0 1 2 3 4 5<br/>
  0&nbsp;[0 1 1 1 0 1]<br/>
  1&nbsp;[1 0 1 0 0 0]<br/>
  2&nbsp;[1 1 0 0 1 0]<br/>
  3&nbsp;[1 0 0 0 0 1]<br/>
  4&nbsp;[0 0 1 0 0 1]<br/>
  5&nbsp;[1 0 0 1 1 0]
</div>

</div>
</div>

---
layout: prism
heading: "DIY: 인접 행렬 만들기"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n = 6;
    vector<vector<int>> A(n, vector<int>(n, 0));
    int edges[][2] = {{0,1},{0,2},{0,3},{0,5},{1,2},{2,4},{3,5},{4,5}};
    for (auto& e : edges) { A[e[0]][e[1]] = 1; A[e[1]][e[0]] = 1; } // 무방향

    cout << "  0 1 2 3 4 5\n";
    for (int i = 0; i < n; i++) {
        cout << i << " ";
        for (int j = 0; j < n; j++) cout << A[i][j] << " ";
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 최소 신장 트리
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- $n$개의 노드로 이루어진 무방향 그래프에서 모든 노드를 서로 연결하는 데 필요한 최소 간선 수는 $n - 1$입니다; 이렇게 연결되어 있으면서 사이클이 없는 부분 그래프를 [신장 트리]{.hl}라고 합니다.

- [최소 신장 트리]{.hl}(MST)는 간선 가중치의 합이 가장 작은 신장 트리입니다.

  - 최적의 전기 회로 구성, 최적의 네트워크 구축, 최적의 케이블 배선 등에 사용할 수 있습니다.

- MST를 구하는 두 가지 고전적인 탐욕 알고리즘: [크루스칼]{.hl}(간선을 정렬하여 union-find로 합침)과 [프림]{.hl}(한 정점에서 트리를 키워 나감).

---
layout: prism
heading: "DIY: 크루스칼 알고리즘"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
using namespace std;

int par[6];
int findSet(int x) { return par[x] == x ? x : par[x] = findSet(par[x]); }

int main() {
    // 6-노드 가중 그래프의 {u, v, w}
    vector<array<int,3>> e = {{0,1,6},{0,2,1},{0,3,5},{0,5,4},
                              {1,2,2},{2,4,3},{3,5,7},{4,5,8}};
    sort(e.begin(), e.end(), [](auto&a, auto&b){ return a[2] < b[2]; });
    for (int i = 0; i < 6; i++) par[i] = i;

    int total = 0;
    cout << "MST edges: ";
    for (auto& ed : e) {
        if (findSet(ed[0]) != findSet(ed[1])) {          // 사이클 없음
            par[findSet(ed[0])] = findSet(ed[1]);
            cout << ed[0] << "-" << ed[1] << "(" << ed[2] << ") ";
            total += ed[2];
        }
    }
    cout << "\ntotal weight = " << total << endl;        // 15
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY: 프림 알고리즘"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int n = 6;
    vector<vector<pair<int,int>>> adj(n);                // (이웃, 가중치)
    int E[][3] = {{0,1,6},{0,2,1},{0,3,5},{0,5,4},{1,2,2},{2,4,3},{3,5,7},{4,5,8}};
    for (auto& e : E) { adj[e[0]].push_back({e[1],e[2]}); adj[e[1]].push_back({e[0],e[2]}); }

    vector<int> done(n, 0);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq; // (가중치, 노드)
    pq.push({0, 0});
    int total = 0;
    while (!pq.empty()) {
        auto [w, u] = pq.top(); pq.pop();
        if (done[u]) continue;
        done[u] = 1; total += w;
        for (auto [v, wt] : adj[u]) if (!done[v]) pq.push({wt, v});
    }
    cout << "MST total weight = " << total << endl;      // 15
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY: 다익스트라 알고리즘"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int INF = 1e9;

int main() {
    int n = 6;
    vector<vector<pair<int,int>>> adj(n);
    int E[][3] = {{0,1,6},{0,2,1},{0,3,5},{0,5,4},{1,2,2},{2,4,3},{3,5,7},{4,5,8}};
    for (auto& e : E) { adj[e[0]].push_back({e[1],e[2]}); adj[e[1]].push_back({e[0],e[2]}); }

    vector<int> dist(n, INF); dist[0] = 0;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, 0});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u])
            if (dist[u] + w < dist[v]) { dist[v] = dist[u] + w; pq.push({dist[v], v}); }
    }
    cout << "shortest distances from 0: ";
    for (int i = 0; i < n; i++) cout << dist[i] << " ";
    cout << endl;                                        // 0 3 1 5 4 4
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY: 플로이드-워셜 알고리즘"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;
const int INF = 1e9;

int main() {
    int n = 6;
    vector<vector<int>> d(n, vector<int>(n, INF));
    for (int i = 0; i < n; i++) d[i][i] = 0;
    int E[][3] = {{0,1,6},{0,2,1},{0,3,5},{0,5,4},{1,2,2},{2,4,3},{3,5,7},{4,5,8}};
    for (auto& e : E) { d[e[0]][e[1]] = e[2]; d[e[1]][e[0]] = e[2]; }

    for (int k = 0; k < n; k++)                          // 모든 쌍 최단 경로
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (d[i][k] + d[k][j] < d[i][j]) d[i][j] = d[i][k] + d[k][j];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << d[i][j] << " ";
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 깊이 우선 탐색
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [깊이 우선 탐색]{.hl}(DFS)은 각 분기를 따라 가능한 한 깊이 탐색한 뒤 되돌아옵니다.

- DFS는 [스택]{.hl}(또는 재귀)을 사용하며 그래프 전체에 대해 $O(N)$으로 동작합니다.

</div>
<div>

```text
DFS(graph, v, visited):
    visited[v] = True          // v를 방문 표시
    for i in graph[v]:         // 재귀적으로 방문
        if not visited[i]:
            DFS(graph, i, visited)
```

</div>
</div>

---
layout: prism
heading: "DIY: 재귀 DFS"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> g(9);   // 1..8; 방문 순서대로의 인접 리스트
vector<int> vis(9, 0);

void dfs(int v) {
    vis[v] = 1; cout << v << " ";
    for (int u : g[v]) if (!vis[u]) dfs(u);
}

int main() {
    g[1]={2,3}; g[2]={1,7,8}; g[7]={2,6}; g[6]={7,8};
    g[8]={2,6,3}; g[3]={1,8,4}; g[4]={3,5}; g[5]={4};
    cout << "DFS order: ";
    dfs(1);                 // 1 2 7 6 8 3 4 5
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 재귀 프로그래밍
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 어떤 계산은 반복문으로 표현하기는 어색하지만 그 *자기 자신*으로 표현하면 자연스럽습니다 — 이것이 [재귀]{.hl}입니다.

- 무한 반복을 피하려면 재귀에는 두 가지 요소가 필요합니다:

<div class="sub-item-enum">

1. [기저 사례]{.hl} — 재귀 *없이* 풀리는 사례가 적어도 하나 있어야 하며, 이것이 재귀를 멈춥니다.
2. [재귀 사례]{.hl} — 기저 사례를 향해 나아가는 일반적인 사례.

</div>

---
layout: prism
heading: 재귀 예제
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w06/dsa-w06-image10.png" class="tikz-fig" style="width: 100%;" />

<div style="text-align:center; font-size: 0.8rem; color:#9aa0a6;">팩토리얼: 호출이 풀려나가는 과정</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w06/dsa-w06-image11.png" class="tikz-fig" style="width: 100%;" />

<div style="text-align:center; font-size: 0.8rem; color:#9aa0a6;">피보나치: 호출 트리</div>

</div>
</div>

---
layout: prism
heading: "DIY: 팩토리얼과 피보나치"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int factorial(int n) {
    if (n == 0) return 1;                 // 기저 사례
    return n * factorial(n - 1);          // 재귀 사례
}
int fib(int n) {
    if (n == 0) return 0;                 // 기저 사례
    if (n == 1) return 1;
    return fib(n - 1) + fib(n - 2);       // 재귀 사례
}

int main() {
    cout << "factorial(4) = " << factorial(4) << "\n";  // 24
    cout << "fib(0..9)    = ";
    for (int i = 0; i < 10; i++) cout << fib(i) << " ";  // 0 1 1 2 3 5 8 13 21 34
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 너비 우선 탐색
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [너비 우선 탐색]{.hl}(BFS)은 더 깊이 내려가기 전에 현재 깊이의 모든 이웃을 먼저 탐색합니다.

- BFS는 [큐]{.hl}를 사용하며 $O(N)$으로 동작합니다; 실제로는 보통 DFS보다 약간 더 빠릅니다.

</div>
<div>

```text
BFS(graph, v, visited):
    q.push(v); visited[v] = True
    while not q.empty():
        v = q.pop()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.push(i)
```

</div>
</div>

---
layout: prism
heading: "DIY: 큐 기반 BFS"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    vector<vector<int>> g(9);   // 1..8; 방문 순서대로의 인접 리스트
    g[1]={2,3}; g[2]={1,8}; g[3]={1,7}; g[8]={2,4,5};
    g[7]={3,6}; g[4]={8}; g[5]={8}; g[6]={7};

    vector<int> vis(9, 0);
    queue<int> q; q.push(1); vis[1] = 1;
    cout << "BFS order: ";
    while (!q.empty()) {
        int v = q.front(); q.pop();
        cout << v << " ";
        for (int u : g[v]) if (!vis[u]) { vis[u] = 1; q.push(u); }
    }
    cout << endl;               // 1 2 3 8 7 4 5 6
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
