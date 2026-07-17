---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 2 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-2/
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
.node-box {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 2.6rem;
  height: 2.4rem;
  border: 2px solid #5c60a8;
  border-radius: 6px;
  font-family: 'JetBrains Mono', Consolas, monospace;
  font-size: 1.05rem;
}
.node-arrow {
  color: #4a6fa5;
  font-size: 1.3rem;
  margin: 0 0.15rem;
}
.cell {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 2.6rem;
  height: 2.4rem;
  border: 1px solid #9aa0a6;
  font-family: 'JetBrains Mono', Consolas, monospace;
  font-size: 1rem;
}
.cell-hl { background: #dbeafe; }
</style>

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.png" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3rem; font-weight: bold; margin: 0rem;">자료구조실습</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">2주차: 추상 데이터 타입과 리스트 ADT</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 4rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">2027년 가을학기</p>
</div>

---
layout: prism
heading: 추상 데이터 타입과 리스트 ADT
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 이번 강의에서는 첫 번째 자료구조인 [리스트]{.hl}를 *추상 데이터 타입*이라는 개념과 함께 소개합니다:

  - [추상 데이터 타입(ADT)]{.hl}이 무엇이며 왜 중요한지 정의합니다.

  - [리스트 ADT]{.hl}와 그 연산들을 명세합니다.

  - 리스트의 [배열]{.hl} 구현과 [연결 리스트]{.hl} 구현을 비교합니다.

  - 회전, 최대 부분 배열, 회문, 요세푸스 같은 고전적인 리스트 문제로 연습합니다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">추상 데이터 타입</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">ADT의 개념</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">리스트 ADT</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">리스트 구현</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">배열 구현</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">단일, 원형, 이중 연결 리스트</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">리스트로 연습하기</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">회전, 최대 부분 배열, 회문, 요세푸스</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">스택 ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스택과 그 구현</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">더 시원한 날, 뒤집기, 괄호 짝맞춤, 후위 표기</span></p>
  </div>

</div>

---
layout: prism
heading: 추상 데이터 타입
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [추상 데이터 타입(ADT)]{.hl}은 객체들의 집합과 그 객체들에 대한 *연산*들의 집합을 함께 묶은 것입니다.

- 많은 프로그래밍 언어(예: C++, Python)는 *구현 세부 사항을 적절히 숨기면서* ADT를 구현할 수 있도록 지원합니다.
  - 구현을 바꿔야 한다면, ADT 연산을 수행하는 루틴만 바꾸는 것으로 손쉽게 처리할 수 있어야 합니다.
  - 이상적으로는 그 변경이 프로그램의 나머지 부분에는 완전히 *투명*해야 합니다.

- 각 ADT가 어떤 연산을 반드시 지원해야 하는지 정해주는 규칙은 없습니다 — 이는 [설계상의 결정]{.hl}입니다.

---
layout: prism
heading: 리스트 ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [리스트]{.hl}는 원소들이 순서대로 나열된 수열 $a_0, a_1, \ldots, a_{N-1}$입니다.

- 리스트 ADT는 이 수열과 그 위에서 수행하고자 하는 연산들을 하나로 묶습니다.

- 필요하다면 다른 연산(예: `sort`)을 추가할 수도 있습니다.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">리스트 ADT 연산</div>
<div class="theorem-box-body">

- `printList` — 리스트를 출력
- `makeEmpty` — 리스트를 비움
- `insert` — `i`번째 위치에 `x`를 삽입
- `remove` — `i`번째 원소(또는 `x`)를 제거
- `find` — 원소 `x`의 인덱스를 찾음
- `findKth` — 특정 인덱스의 원소를 반환
- `size` — 원소의 개수를 반환

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

- 리스트 ADT는 [배열]{.hl}을 사용하여 간단히 구현할 수 있습니다.
  - `printList`는 *선형* 시간, `findKth`는 *상수* 시간에 동작합니다.
  - `insert`와 `remove`는 변경이 일어나는 위치에 따라 비용이 커질 수 있습니다 — $\mathcal{O}(1) \sim \mathcal{O}(N)$.

<div class="flex justify-center items-center gap-8" style="margin-top: 1.6rem;">
  <div class="text-center">
    <div class="flex justify-center"><span class="cell">10</span><span class="cell">3</span><span class="cell">21</span><span class="cell">83</span><span class="cell">34</span><span class="cell"></span></div>
    <div style="margin: 0.4rem 0; color:#4a6fa5; font-family: monospace;">↓ insert(1, 77)</div>
    <div class="flex justify-center"><span class="cell">10</span><span class="cell cell-hl">77</span><span class="cell cell-hl">3</span><span class="cell cell-hl">21</span><span class="cell cell-hl">83</span><span class="cell cell-hl">34</span></div>
  </div>
  <div class="text-center">
    <div class="flex justify-center"><span class="cell">10</span><span class="cell">77</span><span class="cell">3</span><span class="cell">21</span><span class="cell">83</span><span class="cell">34</span></div>
    <div style="margin: 0.4rem 0; color:#4a6fa5; font-family: monospace;">↓ remove(0)</div>
    <div class="flex justify-center"><span class="cell cell-hl">77</span><span class="cell cell-hl">3</span><span class="cell cell-hl">21</span><span class="cell cell-hl">83</span><span class="cell cell-hl">34</span><span class="cell"></span></div>
  </div>
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

class ArrayList {          // 배열로 뒷받침되는 리스트 ADT
    vector<int> a;
public:
    void insert(int i, int x) { a.insert(a.begin() + i, x); } // 오른쪽으로 밀기
    void remove(int i)        { a.erase(a.begin() + i); }     // 왼쪽으로 당기기
    int  findKth(int i) const { return a[i]; }                // O(1)
    int  size() const         { return (int)a.size(); }
    void printList() const {
        for (int x : a) cout << x << ' ';
        cout << '\n';
    }
};

int main() {
    ArrayList L;
    for (int x : {10, 3, 21, 83, 34}) L.insert(L.size(), x);
    cout << "start:        "; L.printList();
    L.insert(1, 77);  cout << "insert(1,77): "; L.printList();
    L.remove(0);      cout << "remove(0):    "; L.printList();
    cout << "findKth(2) = " << L.findKth(2) << ", size = " << L.size() << '\n';
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 단일 연결 리스트 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- `insert`와 `remove`의 선형 비용을 피하기 위해, 리스트를 [연속된 공간에 저장하지 않도록]{.hl} 합니다.

- [연결 리스트]{.hl}는 일련의 *노드*들로 이루어지며, 이 노드들이 메모리상에서 반드시 인접해 있지는 않습니다.
  - 각 노드는 원소와 함께, 그 다음 원소를 담은 노드를 가리키는 `next` 링크를 가집니다.
  - 마지막 노드의 `next` 링크는 `nullptr`을 가리킵니다.

<div class="flex justify-center items-center" style="margin-top: 1.4rem;">
  <span class="node-box">head</span><span class="node-arrow">→</span>
  <span class="node-box">10</span><span class="node-arrow">→</span>
  <span class="node-box">3</span><span class="node-arrow">→</span>
  <span class="node-box">21</span><span class="node-arrow">→</span>
  <span class="node-box">83</span><span class="node-arrow">→</span>
  <span class="node-box">34</span><span class="node-arrow">→</span>
  <span style="font-family: monospace; color:#9aa0a6;">nullptr</span>
</div>

---
layout: prism
heading: 단일 연결 리스트 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `printList`와 `find`는 배열 구현에서와 마찬가지로 명백히 *선형 시간*입니다.

- `findKth` 연산은 더 이상 배열만큼 효율적이지 않습니다.
  - `findKth(i)`는 $\mathcal{O}(i)$ 시간이 걸리며, 리스트를 따라 순차적으로 내려가는 방식으로 동작합니다.
  - 실제로는 `findKth` 호출이 `i` 순서대로 이루어지는 경우가 많기 때문에, 이 한계는 다소 비관적인 추정입니다.

<div class="flex justify-center items-center" style="margin-top: 1.4rem;">
  <span class="node-box">head</span><span class="node-arrow">→</span>
  <span class="node-box">10</span><span class="node-arrow">→</span>
  <span class="node-box">3</span><span class="node-arrow">→</span>
  <span class="node-box">21</span><span class="node-arrow">→</span>
  <span class="node-box">83</span><span class="node-arrow">→</span>
  <span class="node-box">34</span><span class="node-arrow">→</span>
  <span style="font-family: monospace; color:#9aa0a6;">nullptr</span>
</div>

---
layout: prism
heading: 단일 연결 리스트 (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- `remove` 메소드는 *하나의* `next` 포인터 변경만으로 실행할 수 있습니다.

- `insert` 메소드는 `new`로 새 노드를 얻은 뒤, *두 번의* `next` 포인터 조작을 수행합니다.

- 원칙적으로, 변경이 일어날 *위치*를 알고 있다면 항목을 삽입하거나 제거할 때 [많은 항목을 옮길 필요가 없습니다]{.hl}.

<div class="flex justify-center items-center" style="margin-top: 1.2rem;">
  <span class="node-box">head</span><span class="node-arrow">→</span>
  <span class="node-box">10</span><span class="node-arrow">→</span>
  <span class="node-box" style="border-color:#c2410c;">77</span><span class="node-arrow">→</span>
  <span class="node-box">3</span><span class="node-arrow">→</span>
  <span class="node-box">21</span><span class="node-arrow">→</span>
  <span class="node-box">83</span><span class="node-arrow">→</span>
  <span class="node-box">34</span>
  <span style="margin-left: 1rem; font-family: monospace; color:#c2410c;">insert(1, 77)</span>
</div>

---
layout: prism
heading: "DIY: 단일 연결 리스트"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int d) : data(d), next(nullptr) {}
};

struct SList {
    Node* head = nullptr;
    void pushBack(int x) {                 // 맨 끝에 추가
        Node* n = new Node(x);
        if (!head) { head = n; return; }
        Node* t = head;
        while (t->next) t = t->next;
        t->next = n;
    }
    void insertAfter(int val, int x) {     // 'val' 노드 바로 뒤에 x를 삽입
        for (Node* t = head; t; t = t->next)
            if (t->data == val) {
                Node* n = new Node(x);
                n->next = t->next;         // 조작 1
                t->next = n;               // 조작 2
                return;
            }
    }
    void removeVal(int x) {                // next 포인터 하나 변경
        if (!head) return;
        if (head->data == x) { Node* d = head; head = head->next; delete d; return; }
        for (Node* t = head; t->next; t = t->next)
            if (t->next->data == x) { Node* d = t->next; t->next = d->next; delete d; return; }
    }
    void print() const {
        for (Node* t = head; t; t = t->next) cout << t->data << " -> ";
        cout << "nullptr\n";
    }
};

int main() {
    SList L;
    for (int x : {10, 3, 21, 83, 34}) L.pushBack(x);
    cout << "start:        "; L.print();
    L.insertAfter(10, 77); cout << "insert 77:    "; L.print();
    L.removeVal(21);       cout << "remove 21:    "; L.print();
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
  margin-top: 1.1em;
}
</style>

- 일반적인 연결 리스트에서는 첫 번째 노드와 마지막 노드에 접근하는 난이도가 [현저히 다릅니다]{.hl}.
  - 첫 번째 노드에는 즉시 도달할 수 있지만, 마지막 노드에 도달하려면 모든 링크를 따라가야 합니다.
  - $N$개의 원소를 가진 리스트에서 앞쪽 `insert`/`remove`는 $\mathcal{O}(1)$이지만, 뒤쪽은 $\mathcal{O}(N)$입니다.

- [원형 연결 리스트]{.hl}에서는 마지막 노드의 `next` 포인터가 다시 첫 번째 노드를 가리켜 이 비대칭성을 없앱니다(종종 `tail` 포인터도 함께 둡니다).

<div class="flex justify-center items-center" style="margin-top: 1.2rem;">
  <span class="node-box">head</span><span class="node-arrow">→</span>
  <span class="node-box">10</span><span class="node-arrow">→</span>
  <span class="node-box">3</span><span class="node-arrow">→</span>
  <span class="node-box">21</span><span class="node-arrow">→</span>
  <span class="node-box">83</span><span class="node-arrow">→</span>
  <span class="node-box">34</span>
  <span class="node-arrow">⟳</span>
  <span style="font-family: monospace; color:#4a6fa5;">back to head</span>
</div>

---
layout: prism
heading: 이중 연결 리스트
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 단일 연결 리스트나 원형 연결 리스트의 노드들은 [단방향]{.hl}으로 연결됩니다.
  - 임의의 노드가 주어졌을 때, 이전 노드를 저장해 두지 않았다면 되돌아갈 수 없습니다.

- [이중 연결 리스트]{.hl}에서는 각 노드가 *양방향*으로 연결됩니다 — `next`와 `prev`를 통해 양쪽 이웃 노드와 이어집니다.

- 나아가 이중 연결 리스트 자체도 *원형*이 될 수 있습니다.

<div class="flex justify-center items-center" style="margin-top: 1.2rem;">
  <span class="node-box">head</span><span class="node-arrow">⇄</span>
  <span class="node-box">10</span><span class="node-arrow">⇄</span>
  <span class="node-box">3</span><span class="node-arrow">⇄</span>
  <span class="node-box">21</span><span class="node-arrow">⇄</span>
  <span class="node-box">83</span><span class="node-arrow">⇄</span>
  <span class="node-box">34</span>
</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">추상 데이터 타입</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">리스트 구현</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">리스트로 연습하기</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">배열 회전하기</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">최대 부분 배열 (완전 탐색과 카데인)</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">이중 연결 리스트를 이용한 회문 판별</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">요세푸스 문제</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">곱하기 혹은 더하기</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">스택 ADT</span></p>
  </div>

</div>

---
layout: prism
heading: 배열 회전하기
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 주어진 배열에서 각 원소를 주어진 횟수 $k$만큼 뒤로 밀어내고, 밀려난 원소들을 앞쪽으로 감아 붙입니다.
  - 입력: `[1, -2, 3, 5, -4, 2, 5]`, `k = 3`
  - 출력: `[-4, 2, 5, 1, -2, 3, 5]`

- [완전 탐색]{.hl} 방식은 한 칸씩 회전하는 것을 $k$번 반복합니다 — 비용이 $k$에 따라 커집니다.

- 더 효율적으로는 [마지막 $k$개의 원소를 잘라내어 앞쪽에 붙이면]{.hl} 됩니다. 세 번의 배열 *뒤집기*를 이용하는 깔끔한 요령으로 $\mathcal{O}(N)$ 시간에 이를 달성할 수 있습니다.

---
layout: prism
heading: "DIY: 배열 회전하기"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> rotateBruteForce(const vector<int>& nums, int k) {
    vector<int> r = nums;
    int n = nums.size();
    k %= n;
    for (int i = 0; i < k; ++i) {          // 한 칸씩 오른쪽으로, k번 반복
        int last = r[n - 1];
        for (int j = n - 1; j > 0; --j) r[j] = r[j - 1];
        r[0] = last;
    }
    return r;
}

vector<int> rotateEfficient(vector<int> r, int k) {
    int n = r.size();
    k %= n;
    auto rev = [&](int s, int e) { while (s < e) swap(r[s++], r[e--]); };
    rev(0, n - 1); rev(0, k - 1); rev(k, n - 1);   // 전체 뒤집기 후, 두 부분 뒤집기
    return r;
}

int main() {
    vector<int> sample = {1, -2, 3, 5, -4, 2, 5};
    for (int x : rotateBruteForce(sample, 3)) cout << x << ' ';
    cout << "  (brute force)\n";
    for (int x : rotateEfficient(sample, 3)) cout << x << ' ';
    cout << "  (three reversals)\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 최대 부분 배열
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 모든 *연속된* 부분 배열 중에서 합이 가장 큰 것을 찾고, 그 시작/끝 인덱스를 보고합니다.
  - 입력: `[1, -2, 3, 5, -4, 2, 5]`
  - 출력: 시작 `2`, 끝 `6` (부분 배열 `[3, 5, -4, 2, 5]`, 합 $= 11$)

- [완전 탐색]{.hl} 방법은 모든 부분 배열 $A[i..j]$의 합을 구해 그중 최댓값을 유지합니다.

- 구현하기는 쉽지만 $\mathcal{O}(N^2)$에 동작하여 — 코딩 테스트에서 시간 제한에 걸릴 정도입니다.

---
layout: prism
heading: "최대 부분 배열: 카데인 알고리즘"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [동적 계획법]{.hl}을 사용하면 복잡도를 $\mathcal{O}(N)$으로 낮출 수 있습니다.

- 각 위치에서, *그 위치에서 끝나는* 최적의 부분 배열은 이전 최적을 *이어가거나* 현재 원소에서 *다시 시작*합니다.

<div class="flex justify-center" style="margin-top: 1.4rem;">
  <table style="border-collapse: collapse; font-family: monospace; text-align: center;">
    <tr>
      <td style="padding: 0.3rem 0.6rem; color:#4a6fa5;">원소</td>
      <td class="cell">1</td><td class="cell">-2</td><td class="cell">3</td><td class="cell">5</td><td class="cell">-4</td><td class="cell">2</td><td class="cell">5</td>
    </tr>
    <tr>
      <td style="padding: 0.3rem 0.6rem; color:#4a6fa5;">최적 합</td>
      <td class="cell">1</td><td class="cell">-1</td><td class="cell">3</td><td class="cell">8</td><td class="cell">4</td><td class="cell">6</td><td class="cell cell-hl">11</td>
    </tr>
  </table>
</div>

---
layout: prism
heading: "DIY: 최대 부분 배열"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

pair<int,int> maxSubarrayBruteForce(const vector<int>& a) {
    int best = INT_MIN, bs = 0, be = 0;
    for (int i = 0; i < (int)a.size(); ++i) {
        int cur = 0;
        for (int j = i; j < (int)a.size(); ++j) {
            cur += a[j];
            if (cur > best) { best = cur; bs = i; be = j; }
        }
    }
    return {bs, be};
}

pair<int,int> maxSubarrayKadane(const vector<int>& a) {
    int cur = a[0], best = a[0], bs = 0, be = 0, tmp = 0;
    for (int i = 1; i < (int)a.size(); ++i) {
        if (a[i] > cur + a[i]) { cur = a[i]; tmp = i; }   // 다시 시작
        else                     cur += a[i];             // 이어가기
        if (cur > best) { best = cur; bs = tmp; be = i; }
    }
    return {bs, be};
}

int main() {
    vector<int> s = {1, -2, 3, 5, -4, 2, 5};
    auto b = maxSubarrayBruteForce(s);
    auto k = maxSubarrayKadane(s);
    cout << "Brute force: start = " << b.first  << ", end = " << b.second << "\n";
    cout << "Kadane:      start = " << k.first  << ", end = " << k.second << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 회문
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [회문]{.hl}은 앞으로 읽으나 뒤로 읽으나 똑같은 단어나 문구를 말합니다.
  - `noon`, `eye`, `kayak`, `level`, `racecar`, ...

- 주어진 문자열을 [이중 연결 리스트]{.hl}에 넣은 뒤, *양 끝*에서부터 안쪽으로 이동하며 문자를 비교합니다.
  - 각 노드가 이전 노드와 연결되어 있으므로, 꼬리에서 머리 쪽으로 거슬러 가며 확인하기가 편리합니다.

---
layout: prism
heading: "DIY: 이중 연결 리스트를 이용한 회문 판별"
---

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

struct Node {
    char data;
    Node *next, *prev;
    Node(char c) : data(c), next(nullptr), prev(nullptr) {}
};

class DoublyLinkedList {
    Node *head = nullptr, *tail = nullptr;
public:
    void append(char c) {
        Node* n = new Node(c);
        if (!head) head = tail = n;
        else { tail->next = n; n->prev = tail; tail = n; }
    }
    bool isPalindrome() const {
        Node *s = head, *e = tail;
        while (s && e && s != e && e->next != s) {   // 양 끝에서 안쪽으로 이동
            if (s->data != e->data) return false;
            s = s->next; e = e->prev;
        }
        return true;
    }
};

bool check(const string& w) {
    DoublyLinkedList d;
    for (char c : w) d.append(c);
    return d.isPalindrome();
}

int main() {
    for (string w : {"level", "racecar", "hello"})
        cout << w << " -> " << (check(w) ? "palindrome" : "not a palindrome") << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 요세푸스 문제
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- $N$명의 사람이 원을 이루어 서 있습니다. 반복해서 수를 세어 $M$번째 사람을 제거하고, 마지막으로 살아남은 사람의 인덱스를 반환합니다.
  - 입력: $N = 10$, $M = 3$
  - 출력: `4`번 사람

- [원형 연결 리스트]{.hl}로 원을 모델링합니다: $N$개의 인덱스를 넣은 뒤, $M$ 단위로 돌면서 도달하는 사람을 삭제하여 하나의 노드만 남을 때까지 반복합니다.

---
layout: prism
heading: "DIY: 원형 연결 리스트를 이용한 요세푸스"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int d) : data(d), next(nullptr) {}
};

class CircularLinkedList {
    Node* head = nullptr;
public:
    void append(int data) {
        Node* n = new Node(data);
        if (!head) { head = n; n->next = head; }
        else {
            Node* t = head;
            while (t->next != head) t = t->next;
            t->next = n; n->next = head;
        }
    }
    int josephus(int m) {
        Node *ptr = head, *prev = nullptr;
        while (ptr->next != ptr) {          // 노드가 하나 남을 때까지
            int count = 1;
            while (count != m) { prev = ptr; ptr = ptr->next; ++count; }
            prev->next = ptr->next;         // m번째 노드를 링크에서 제거
            delete ptr;
            ptr = prev->next;
        }
        return ptr->data;
    }
};

int main() {
    const int n = 10, m = 3;
    CircularLinkedList list;
    for (int i = 1; i <= n; ++i) list.append(i);
    cout << "The survivor is at position: " << list.josephus(m) << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 곱하기 혹은 더하기
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 숫자(`0`–`9`)로 이루어진 문자열이 주어질 때, 인접한 각 숫자 쌍 사이에 `+` 또는 `×`를 넣어 결과를 최대로 만듭니다. 모든 연산은 *왼쪽에서 오른쪽으로* 적용됩니다.
  - 입력: `02984` &nbsp;→&nbsp; 출력: `576`
  - 입력: `567` &nbsp;→&nbsp; 출력: `210`

- [탐욕 규칙]{.hl}: 곱하기가 더하기보다 수를 더 빠르게 키웁니다. *단*, `0`이나 `1`이 관여할 때는 예외로, 이 경우에는 더합니다.

---
layout: prism
heading: "DIY: 곱하기 혹은 더하기"
---

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

long long multiplyOrAdd(const string& s) {
    long long result = s[0] - '0';
    for (size_t i = 1; i < s.size(); ++i) {
        int d = s[i] - '0';
        if (result <= 1 || d <= 1) result += d;   // 0 또는 1이 관여하면 더하기
        else                       result *= d;   // 그 외에는 곱하기
    }
    return result;
}

int main() {
    for (string s : {"02984", "567"})
        cout << s << " -> " << multiplyOrAdd(s) << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "W02_DIY01: 연결 리스트가 원형인가?"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 주어진 연결 리스트가 *원형*인지 판별하는 함수를 작성하세요.

- [플로이드의 토끼와 거북이]{.hl}를 사용합니다: 한 포인터는 한 칸씩, 다른 포인터는 두 칸씩 전진시킵니다.
  - 두 포인터가 언젠가 만나면, 리스트에 순환이 있는 것입니다.
  - 빠른 포인터가 `nullptr`에 도달하면, 순환이 없는 일반 리스트입니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int data; Node* next; Node(int d):data(d),next(nullptr){} };

bool isCircular(Node* head) {
    Node *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

int main() {
    Node* a = new Node(1);
    a->next = new Node(2);
    a->next->next = new Node(3);
    cout << "plain: " << boolalpha << isCircular(a) << "\n";
    a->next->next->next = a;        // 고리를 닫음
    cout << "loop:  " << isCircular(a) << "\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "W02_DIY02: 이중 연결 리스트에서 노드 제거"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node *next, *prev;
    Node(int d) : data(d), next(nullptr), prev(nullptr) {}
};

struct DList {
    Node *head = nullptr, *tail = nullptr;
    void append(int x) {
        Node* n = new Node(x);
        if (!head) head = tail = n;
        else { tail->next = n; n->prev = tail; tail = n; }
    }
    void remove(int x) {                       // 최대 네 개의 링크를 손봄
        for (Node* t = head; t; t = t->next)
            if (t->data == x) {
                if (t->prev) t->prev->next = t->next; else head = t->next;
                if (t->next) t->next->prev = t->prev; else tail = t->prev;
                delete t;
                return;
            }
    }
    void print() const {
        for (Node* t = head; t; t = t->next) cout << t->data << ' ';
        cout << '\n';
    }
};

int main() {
    DList d;
    for (int x : {10, 3, 21, 83, 34}) d.append(x);
    cout << "before:      "; d.print();
    d.remove(21);  cout << "remove(21):  "; d.print();
    d.remove(10);  cout << "remove(10):  "; d.print();
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">추상 데이터 타입</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">리스트 구현</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">리스트로 연습하기</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">스택 ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스택과 그 구현</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">더 시원한 날과 문자열 뒤집기</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">괄호 짝맞춤</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">중위에서 후위로 변환과 후위 표기 계산</span></p>
  </div>

</div>

---
layout: prism
heading: 스택 ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [스택]{.hl}은 삽입과 삭제를 *오직 한 위치*, 즉 리스트의 끝인 [top]{.hl}에서만 수행할 수 있도록 제한한 리스트입니다.
  - 스택은 [LIFO]{.hl}(last in, first out, 후입선출) 리스트로 알려져 있습니다.
  - 오직 top 원소에만 접근할 수 있습니다.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">스택 ADT 연산</div>
<div class="theorem-box-body">

- `push` — top에 원소를 추가
- `top` — top 원소를 확인
- `pop` — top 원소를 제거
- 그 밖에 필요한 연산(예: `popAll`)

</div>
</div>

<div class="flex justify-center items-center gap-3" style="margin-top: 1rem;">
  <div class="flex flex-col">
    <div class="cell cell-hl" style="width: 3.4rem;">34</div>
    <div class="cell" style="width: 3.4rem;">83</div>
    <div class="cell" style="width: 3.4rem;">21</div>
    <div class="cell" style="width: 3.4rem;">3</div>
    <div class="cell" style="width: 3.4rem;">77</div>
    <div class="cell" style="width: 3.4rem;">10</div>
  </div>
  <div style="font-size: 0.8rem; color:#4a6fa5;">← <code>top</code><br/>(이것만<br/>접근 가능)</div>
</div>

</div>
</div>

---
layout: prism
heading: 스택의 구현
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 스택은 리스트이므로 [어떤 리스트 구현이든]{.hl} 사용할 수 있습니다.

- `push`와 `pop`은 단순한 상수 시간이 아니라 *매우 빠른* 상수 시간에 수행됩니다.
  - 일부 기계에서는 자동 증가/자동 감소 주소 지정을 이용해 단일 명령어로 컴파일되며, 대부분의 현대 기계는 스택 연산을 명령어 집합에 내장하고 있습니다.
  - 스택은 배열 다음으로 컴퓨터 과학에서 가장 기본적인 자료구조입니다.

- [배열 구현]{.hl}은 최종 길이를 미리 알 수 없을 수 있어 충분한 공간을 확보해 두어야 하며, 이는 효율을 떨어뜨릴 수 있습니다.
  - [연결 리스트 구현]{.hl}은 필요한 만큼 정확히 늘어나는 유연한 대안입니다.

---
layout: prism
heading: "DIY: 스택의 기본 연산"
---

<CppRunner>

```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    for (int x : {10, 77, 3, 21, 83, 34}) {   // 순서대로 push
        s.push(x);
        cout << "push(" << x << ")  top = " << s.top() << ", size = " << s.size() << "\n";
    }
    cout << "--- popping (LIFO order) ---\n";
    while (!s.empty()) {
        cout << "pop " << s.top() << "\n";     // 마지막에 넣은 것이 먼저 나옴
        s.pop();
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 더 시원한 날
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 일주일간의 기온이 주어질 때, 각 날짜마다 *다음으로* 더 시원한 날의 기온을 출력합니다. 이후에 더 시원한 날이 없으면 `-1`을 출력합니다.
  - 입력: `[4, 5, 2, 10, 8, 6, 12]`
  - 출력: `[2, 2, -1, 8, 6, -1, -1]`

- [인덱스 스택]{.hl}으로 해결합니다: 현재 기온이 스택 top에 있는 날짜보다 더 시원하면, 그 날짜는 답을 찾은 것이므로 pop하여 결과를 기록합니다.
  - 각 인덱스는 최대 한 번 push되고 한 번 pop되므로 $\mathcal{O}(N)$ 스캔이 됩니다.

---
layout: prism
heading: "DIY: 더 시원한 날"
---

<CppRunner>

```cpp
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

vector<int> nextCoolerDay(const vector<int>& t) {
    vector<int> result(t.size(), -1);   // 기본값: 앞으로 더 시원한 날 없음
    stack<int> s;                       // 아직 답을 기다리는 날들의 인덱스
    for (int i = 0; i < (int)t.size(); ++i) {
        while (!s.empty() && t[s.top()] > t[i]) {   // 오늘이 더 시원함
            result[s.top()] = t[i];
            s.pop();
        }
        s.push(i);
    }
    return result;
}

int main() {
    vector<int> temps = {4, 5, 2, 10, 8, 6, 12};
    for (int x : nextCoolerDay(temps)) cout << x << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 문자열 뒤집기
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 주어진 문자열을 거꾸로 뒤집어 출력합니다.
  - 입력: `Sungshin` &nbsp;→&nbsp; 출력: `nihsgnuS`

- 모든 문자를 [스택]{.hl}에 push한 뒤 다시 pop합니다: LIFO 순서가 자연스럽게 문자들을 역순으로 내놓으며, 이를 이어 붙여 새로운 문자열을 만듭니다.

---
layout: prism
heading: "DIY: 문자열 뒤집기"
---

<CppRunner>

```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

string reverseString(const string& input) {
    stack<char> s;
    for (char ch : input) s.push(ch);   // 각 문자를 push
    string reversed;
    while (!s.empty()) {                 // LIFO 순서로 pop
        reversed += s.top();
        s.pop();
    }
    return reversed;
}

int main() {
    string input = "Sungshin";
    cout << "Original: " << input << "\n";
    cout << "Reversed: " << reverseString(input) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 괄호 짝맞춤
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 여러 종류의 괄호 — `()`, `{}`, `[]` — 는 열린 뒤 올바른 순서로 닫혀야 합니다.
  - 모든 괄호가 제대로 짝지어지면 `true`, 그렇지 않으면 `false`를 출력합니다.
  - `{[()]}` → `true` &nbsp;&nbsp; `{([)}]` → `false` &nbsp;&nbsp; `(hello){}[bye]` → `true`

- 여는 괄호를 스택에 [push]{.hl}하고, 닫는 괄호를 만나면 [top]{.hl}을 확인하여 짝이 맞는 여는 괄호일 때만 `pop`합니다. 스택이 비어 있는 상태로 끝날 때 정확히 균형이 맞는 식입니다.

---
layout: prism
heading: "DIY: 괄호 짝맞춤"
---

<CppRunner>

```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool arePairs(char opening, char closing) {
    return (opening == '(' && closing == ')') ||
           (opening == '{' && closing == '}') ||
           (opening == '[' && closing == ']');
}

bool areParenthesesBalanced(const string& expr) {
    stack<char> s;
    for (char c : expr) {
        if (c == '(' || c == '{' || c == '[') s.push(c);
        else if (c == ')' || c == '}' || c == ']') {
            if (s.empty() || !arePairs(s.top(), c)) return false;
            s.pop();
        }
    }
    return s.empty();
}

int main() {
    for (string e : {"{[()]}", "{([)}]", "(hello){}[bye]"})
        cout << e << " -> " << boolalpha << areParenthesesBalanced(e) << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 중위 표기법과 후위 표기법
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [중위]{.hl} 표기법은 각 연산자를 피연산자 *사이*에 놓는, 우리가 식을 쓰는 일반적인 방식입니다. 예: `a + b * (c - d) / e`.

- [후위]{.hl}(역폴란드) 표기법은 각 연산자를 피연산자 *뒤*에 놓으며, 괄호가 필요 없습니다.

- 우선순위에 따라 완전히 괄호를 친 뒤, 각 연산자를 닫는 괄호 바로 뒤로 옮기고, 마지막으로 괄호를 지웁니다.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">a + b * (c - d) / e &nbsp;→&nbsp; abcd-*e/+</div>
<div class="theorem-box-body">

<div style="font-family: monospace; font-size: 0.85rem; line-height: 1.7;">
a+(b*(c-d))/e<br/>
a+((b*(c-d))/e)<br/>
(a+((b*(c-d))/e))<br/>
(a+((b*(cd)-)/e))<br/>
(a+((b(cd)-)*/e))<br/>
(a+((b(cd)-)*e)/)<br/>
(a((b(cd)-)*e)/)+<br/>
<b>abcd-*e/+</b>
</div>

</div>
</div>

</div>
</div>

---
layout: prism
heading: "DIY: 중위에서 후위로 변환"
---

<CppRunner>

```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool isOperand(char c) {
    return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9');
}

int precedence(char op) {
    switch (op) {
        case '^': return 3;
        case '*': case '/': return 2;
        case '+': case '-': return 1;
        default:  return -1;
    }
}

string infixToPostfix(const string& infix) {
    stack<char> s;
    string postfix;
    for (char c : infix) {
        if (isOperand(c)) postfix += c;
        else if (c == '(') s.push(c);
        else if (c == ')') {
            while (!s.empty() && s.top() != '(') { postfix += s.top(); s.pop(); }
            if (!s.empty()) s.pop();                 // '(' 를 버림
        } else {
            while (!s.empty() && precedence(s.top()) >= precedence(c)) {
                postfix += s.top(); s.pop();
            }
            s.push(c);
        }
    }
    while (!s.empty()) { postfix += s.top(); s.pop(); }
    return postfix;
}

int main() {
    string infix = "a+b*(c-d)/e";
    cout << "Infix:   " << infix << "\n";
    cout << "Postfix: " << infixToPostfix(infix) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "W02_DIY04: 후위 표기식 계산"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [후위]{.hl} 표기법으로 주어진 식의 값을 계산합니다.

- [피연산자 스택]{.hl}을 사용하여 왼쪽에서 오른쪽으로 스캔합니다:
  - 각 숫자를 `push`하고;
  - 연산자를 만나면 두 피연산자를 `pop`하여 연산을 적용한 뒤 결과를 `push`합니다.
  - 스택에 마지막으로 남는 값이 답입니다.

- `53+82-*` $= (5+3)\times(8-2) = 48$.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int evalPostfix(const string& expr) {
    stack<int> s;
    for (char c : expr) {
        if (c >= '0' && c <= '9') s.push(c - '0');
        else {
            int b = s.top(); s.pop();
            int a = s.top(); s.pop();
            switch (c) {
                case '+': s.push(a + b); break;
                case '-': s.push(a - b); break;
                case '*': s.push(a * b); break;
                case '/': s.push(a / b); break;
            }
        }
    }
    return s.top();
}

int main() {
    string expr = "53+82-*";
    cout << expr << " = " << evalPostfix(expr) << endl;
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
