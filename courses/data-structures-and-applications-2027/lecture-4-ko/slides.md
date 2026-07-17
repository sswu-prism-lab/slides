---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 4 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-4/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">4주차: 스택, 큐, 트리, 힙, 그래프</p>

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
heading: "복습: stack 클래스"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- C++는 `#include <stack>`에서 제네릭 [`stack`]{.hl} 클래스를 제공합니다.

- 스택은 [LIFO]{.hl}(last-in, first-out; 후입선출) 컨테이너입니다.
  - `push`는 맨 위에 추가하고, `pop`은 맨 위를 제거하며, `top`은 맨 위를 읽습니다.

- `stack<elementType> name;` 형태로 선언합니다.

</div>
<div>

```cpp
#include <stack>
stack<int> s;
s.push(3);   // 맨 위에 추가
s.pop();     // 맨 위 제거
s.top();     // 맨 위 읽기
s.size();    // 원소 개수
s.empty();   // 비어 있으면 true
```

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    for (int x : {1, 2, 3}) s.push(x);
    cout << "size = " << s.size() << "\n";
    while (!s.empty()) {          // LIFO 순서로 꺼냄
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;                 // 3 2 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: queue 클래스"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- C++는 `#include <queue>`에서 제네릭 [`queue`]{.hl} 클래스를 제공합니다.

- 큐는 [FIFO]{.hl}(first-in, first-out; 선입선출) 컨테이너입니다.
  - `push`는 뒤에 추가하고, `pop`은 앞에서 제거하며, `front`는 앞을 읽습니다.

- `queue<elementType> name;` 형태로 선언합니다.

</div>
<div>

```cpp
#include <queue>
queue<int> q;
q.push(3);   // 뒤에 추가
q.pop();     // 앞을 제거
q.front();   // 앞을 읽기
q.size();    // 원소 개수
q.empty();   // 비어 있으면 true
```

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    for (int x : {1, 2, 3}) q.push(x);
    cout << "size = " << q.size() << "\n";
    while (!q.empty()) {          // FIFO 순서로 꺼냄
        cout << q.front() << " ";
        q.pop();
    }
    cout << endl;                 // 1 2 3
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "트리, 이진 트리, 힙 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [트리]{.hl}는 연결된 노드들의 집합으로 계층적인 *트리 구조*를 나타냅니다.
  - 각 노드는 여러 개의 자식과 연결될 수 있습니다.
  - 사이클이나 루프가 없으며, 모든 자식은 그 자체로 자신의 [서브트리]{.hl}의 루트가 됩니다.

- [이진 트리]{.hl}(binary tree)에서는 임의의 노드가 세 개 미만(0, 1, 2)의 자식 노드를 가집니다.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 0.4rem;">
<svg width="300" height="220" viewBox="0 0 300 220" xmlns="http://www.w3.org/2000/svg">
  <g stroke="#475569" stroke-width="1.5">
    <line x1="150" y1="25" x2="85" y2="70"/><line x1="150" y1="25" x2="225" y2="70"/>
    <line x1="85" y1="70" x2="40" y2="125"/><line x1="85" y1="70" x2="95" y2="125"/><line x1="85" y1="70" x2="150" y2="125"/>
    <line x1="225" y1="70" x2="225" y2="125"/>
    <line x1="150" y1="125" x2="120" y2="180"/><line x1="150" y1="125" x2="180" y2="180"/>
    <line x1="225" y1="125" x2="225" y2="180"/>
  </g>
  <g font-size="14" font-family="monospace" text-anchor="middle">
    <circle cx="150" cy="25" r="15" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="150" y="25" dy=".35em">2</text>
    <circle cx="85" cy="70" r="15" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="85" y="70" dy=".35em">7</text>
    <circle cx="225" cy="70" r="15" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="225" y="70" dy=".35em">5</text>
    <circle cx="40" cy="125" r="15" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="40" y="125" dy=".35em">2</text>
    <circle cx="95" cy="125" r="15" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="95" y="125" dy=".35em">10</text>
    <circle cx="150" cy="125" r="15" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="150" y="125" dy=".35em">6</text>
    <circle cx="225" cy="125" r="15" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="225" y="125" dy=".35em">9</text>
    <circle cx="120" cy="180" r="15" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="120" y="180" dy=".35em">5</text>
    <circle cx="180" cy="180" r="15" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="180" y="180" dy=".35em">11</text>
    <circle cx="225" cy="180" r="15" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="225" y="180" dy=".35em">4</text>
  </g>
  <text x="95" y="212" font-size="13" font-family="monospace" text-anchor="middle" fill="#64748b">tree</text>
  <text x="225" y="212" font-size="13" font-family="monospace" text-anchor="middle" fill="#64748b">binary tree</text>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: "트리, 이진 트리, 힙 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [포화 이진 트리]{.hl}(full binary tree)에서는 리프(단말 노드)를 제외한 모든 노드가 정확히 두 개의 자식을 가집니다.

- [완전 이진 트리]{.hl}(complete binary tree)는 마지막 레벨을 제외한 모든 레벨이 완전히 채워져 있고, 마지막 레벨의 노드들이 최대한 *왼쪽*으로 몰려 있는 이진 트리입니다.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 0.4rem;">
<svg width="300" height="230" viewBox="0 0 300 230" xmlns="http://www.w3.org/2000/svg">
  <g stroke="#475569" stroke-width="1.5">
    <line x1="80" y1="25" x2="45" y2="80"/><line x1="80" y1="25" x2="115" y2="80"/>
    <line x1="45" y1="80" x2="25" y2="135"/><line x1="45" y1="80" x2="65" y2="135"/>
    <line x1="115" y1="80" x2="95" y2="135"/><line x1="115" y1="80" x2="135" y2="135"/>
  </g>
  <g stroke="#475569" stroke-width="1.5">
    <line x1="230" y1="25" x2="195" y2="80"/><line x1="230" y1="25" x2="265" y2="80"/>
    <line x1="195" y1="80" x2="175" y2="135"/><line x1="195" y1="80" x2="215" y2="135"/>
    <line x1="265" y1="80" x2="245" y2="135"/>
    <line x1="175" y1="135" x2="165" y2="190"/><line x1="175" y1="135" x2="185" y2="190"/>
    <line x1="215" y1="135" x2="205" y2="190"/>
  </g>
  <g font-size="13" font-family="monospace" text-anchor="middle">
    <circle cx="80" cy="25" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="80" y="25" dy=".35em">2</text>
    <circle cx="45" cy="80" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="45" y="80" dy=".35em">7</text>
    <circle cx="115" cy="80" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="115" y="80" dy=".35em">5</text>
    <circle cx="25" cy="135" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="25" y="135" dy=".35em">2</text>
    <circle cx="65" cy="135" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="65" y="135" dy=".35em">6</text>
    <circle cx="95" cy="135" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="95" y="135" dy=".35em">9</text>
    <circle cx="135" cy="135" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="135" y="135" dy=".35em">4</text>
    <circle cx="230" cy="25" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="230" y="25" dy=".35em">2</text>
    <circle cx="195" cy="80" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="195" y="80" dy=".35em">7</text>
    <circle cx="265" cy="80" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="265" y="80" dy=".35em">5</text>
    <circle cx="175" cy="135" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="175" y="135" dy=".35em">2</text>
    <circle cx="215" cy="135" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="215" y="135" dy=".35em">6</text>
    <circle cx="245" cy="135" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="245" y="135" dy=".35em">9</text>
    <circle cx="165" cy="190" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="165" y="190" dy=".35em">4</text>
    <circle cx="185" cy="190" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="185" y="190" dy=".35em">0</text>
    <circle cx="205" cy="190" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="205" y="190" dy=".35em">5</text>
  </g>
  <text x="80" y="222" font-size="12" font-family="monospace" text-anchor="middle" fill="#64748b">full binary tree</text>
  <text x="222" y="222" font-size="12" font-family="monospace" text-anchor="middle" fill="#64748b">complete binary tree</text>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: "트리, 이진 트리, 힙 (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [힙]{.hl}은 다음 두 조건을 만족해야 합니다:
  - 힙은 *완전 이진 트리*입니다.
  - 모든 노드의 값이 자식보다 [크지 않거나]{.hl}([최소 힙]{.hl}; Min Heap), 자식보다 [작지 않습니다]{.hl}([최대 힙]{.hl}; Max Heap).

- 따라서 최솟값(또는 최댓값)이 항상 [루트]{.hl}에 위치합니다.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 0.4rem;">
<svg width="300" height="210" viewBox="0 0 300 210" xmlns="http://www.w3.org/2000/svg">
  <g stroke="#475569" stroke-width="1.5">
    <line x1="70" y1="25" x2="40" y2="85"/><line x1="70" y1="25" x2="100" y2="85"/>
    <line x1="40" y1="85" x2="20" y2="150"/><line x1="40" y1="85" x2="55" y2="150"/>
    <line x1="100" y1="85" x2="90" y2="150"/><line x1="100" y1="85" x2="125" y2="150"/>
    <line x1="230" y1="25" x2="200" y2="85"/><line x1="230" y1="25" x2="260" y2="85"/>
    <line x1="200" y1="85" x2="180" y2="150"/><line x1="200" y1="85" x2="215" y2="150"/>
    <line x1="260" y1="85" x2="250" y2="150"/><line x1="260" y1="85" x2="285" y2="150"/>
  </g>
  <g font-size="13" font-family="monospace" text-anchor="middle">
    <circle cx="70" cy="25" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="70" y="25" dy=".35em">1</text>
    <circle cx="40" cy="85" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="40" y="85" dy=".35em">2</text>
    <circle cx="100" cy="85" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="100" y="85" dy=".35em">4</text>
    <circle cx="20" cy="150" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="20" y="150" dy=".35em">3</text>
    <circle cx="55" cy="150" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="55" y="150" dy=".35em">7</text>
    <circle cx="90" cy="150" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="90" y="150" dy=".35em">5</text>
    <circle cx="125" cy="150" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="125" y="150" dy=".35em">9</text>
    <circle cx="230" cy="25" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="230" y="25" dy=".35em">9</text>
    <circle cx="200" cy="85" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="200" y="85" dy=".35em">7</text>
    <circle cx="260" cy="85" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="260" y="85" dy=".35em">6</text>
    <circle cx="180" cy="150" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="180" y="150" dy=".35em">5</text>
    <circle cx="215" cy="150" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="215" y="150" dy=".35em">3</text>
    <circle cx="250" cy="150" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="250" y="150" dy=".35em">4</text>
    <circle cx="285" cy="150" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="285" y="150" dy=".35em">2</text>
  </g>
  <text x="70" y="188" font-size="13" font-family="monospace" text-anchor="middle" fill="#64748b">min heap</text>
  <text x="230" y="188" font-size="13" font-family="monospace" text-anchor="middle" fill="#64748b">max heap</text>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: 완전 이진 트리 구현
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 완전 이진 트리를 나타내는 데는 [리스트(배열)]{.hl}가 적합하며, 구현을 쉽게 하기 위해 인덱스 0은 *건너뜁니다*.

- [1-기반 인덱스]{.hl}(1-based index)에서 인덱스 `i`의 원소에 대해:
  - 왼쪽 자식은 `2i`(0-기반은 `2i+1`)
  - 오른쪽 자식은 `2i+1`(0-기반은 `2i+2`)
  - 부모는 `i/2`(0-기반은 `(i-1)/2`)

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 0.2rem;">
<svg width="300" height="150" viewBox="0 0 300 150" xmlns="http://www.w3.org/2000/svg">
  <g stroke="#475569" stroke-width="1.5">
    <line x1="150" y1="20" x2="90" y2="65"/><line x1="150" y1="20" x2="230" y2="65"/>
    <line x1="90" y1="65" x2="50" y2="115"/><line x1="90" y1="65" x2="125" y2="115"/>
    <line x1="230" y1="65" x2="195" y2="115"/><line x1="230" y1="65" x2="270" y2="115"/>
  </g>
  <g font-size="13" font-family="monospace" text-anchor="middle">
    <circle cx="150" cy="20" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="150" y="20" dy=".35em">2</text>
    <circle cx="90" cy="65" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="90" y="65" dy=".35em">7</text>
    <circle cx="230" cy="65" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="230" y="65" dy=".35em">5</text>
    <circle cx="50" cy="115" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="50" y="115" dy=".35em">2</text>
    <circle cx="125" cy="115" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="125" y="115" dy=".35em">6</text>
    <circle cx="195" cy="115" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="195" y="115" dy=".35em">9</text>
    <circle cx="270" cy="115" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="270" y="115" dy=".35em">4</text>
  </g>
  <text x="168" y="18" font-size="11" font-family="monospace" fill="#64748b">A[1]</text>
  <text x="108" y="63" font-size="11" font-family="monospace" fill="#64748b">A[2]</text>
  <text x="248" y="63" font-size="11" font-family="monospace" fill="#64748b">A[3]</text>
</svg>
</div>

<div class="tikz-fig" style="display:inline-block; margin-top: 0.4rem; font-family: monospace; font-size: 0.85rem;">
<table style="border-collapse: collapse; text-align:center;">
<tr>
<td style="border:1px solid #475569; width:2rem;">0</td>
<td style="border:1px solid #475569; width:2rem;">2</td>
<td style="border:1px solid #475569; width:2rem;">7</td>
<td style="border:1px solid #475569; width:2rem;">5</td>
<td style="border:1px solid #475569; width:2rem;">2</td>
<td style="border:1px solid #475569; width:2rem;">6</td>
<td style="border:1px solid #475569; width:2rem;">9</td>
<td style="border:1px solid #475569; width:2rem;">4</td>
</tr>
</table>
<div style="display:flex; justify-content:space-between; color:#64748b; font-size:0.7rem;"><span>A[0]</span><span>A[7]</span></div>
</div>

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // 1-기반 완전 이진 트리; 인덱스 0은 사용하지 않음
    vector<int> A = {0, 2, 7, 5, 2, 6, 9, 4, 10, 5, 11, 3};
    int n = 11;
    for (int i = 1; i <= n; i++) {
        cout << "A[" << i << "]=" << A[i];
        if (2 * i <= n)     cout << "  left=A[" << 2 * i << "]=" << A[2 * i];
        if (2 * i + 1 <= n) cout << "  right=A[" << 2 * i + 1 << "]=" << A[2 * i + 1];
        if (i > 1)          cout << "  parent=A[" << i / 2 << "]=" << A[i / 2];
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 우선순위 큐 ADT
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [우선순위 큐]{.hl}는 가장 우선순위가 높은 원소에 항상 먼저 접근할 수 있도록 원소를 저장합니다. 그 ADT는 일반적으로 다음을 지원합니다:

<div class="sub-item">

| 연산 | 설명 |
|---|---|
| `insert` | 원소를 삽입 |
| `deleteMax` | 우선순위가 가장 높은(최대) 원소를 제거 |
| `max` | 최대 원소를 반환 |
| `isEmpty` | 우선순위 큐가 비어 있는지 확인 |
| `clear` | 모든 원소를 제거 |

</div>

- ...또는 필요한 다른 연산(예: `sort`, `size` 등)도 지원할 수 있습니다.

---
layout: prism
heading: "우선순위 큐 구현 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 우선순위 큐는 *정렬된 배열*, *정렬된 연결 리스트* 등 어떤 구조로도 구현할 수 있습니다.

- [힙]{.hl}은 우선순위 큐를 구현하는 가장 효과적인 방법입니다.
  - 원소를 삽입하거나 제거하는 데 $O(\log N)$ 시간이 걸립니다.

- 힙을 배열에 저장합니다. `insert(8)`은 먼저 다음 빈 자리 `A[10]`에 `8`을 덧붙입니다.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 1.0rem; font-family: monospace; font-size: 0.8rem;">
<table style="border-collapse: collapse; text-align:center;">
<tr>
<td style="border:1px solid #475569; width:1.7rem;">9</td>
<td style="border:1px solid #475569; width:1.7rem;">7</td>
<td style="border:1px solid #475569; width:1.7rem;">8</td>
<td style="border:1px solid #475569; width:1.7rem;">4</td>
<td style="border:1px solid #475569; width:1.7rem;">3</td>
<td style="border:1px solid #475569; width:1.7rem;">3</td>
<td style="border:1px solid #475569; width:1.7rem;">5</td>
<td style="border:1px solid #475569; width:1.7rem;">2</td>
<td style="border:1px solid #475569; width:1.7rem;">1</td>
<td style="border:1px solid #0d9488; width:1.7rem; background:#0d9488; color:#fff;">8</td>
</tr>
</table>
<div style="display:flex; justify-content:space-between; color:#64748b; font-size:0.7rem;"><span>A[1]</span><span>A[10]</span></div>
<div style="text-align:center; color:#64748b; margin-top:0.4rem;">insert(8)</div>
</div>

</div>
</div>

---
layout: prism
heading: "우선순위 큐 구현 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- `insert`에서는 새 원소를 부모와 비교하여, (최대 힙 기준) 부모보다 크지 않을 때까지 [위로 올려 보냅니다(percolate up)]{.hl}.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class MaxHeap {
    vector<int> a{0};                 // 인덱스 0은 사용하지 않음
public:
    void insert(int x) {
        a.push_back(x);
        int i = a.size() - 1;
        while (i > 1 && a[i / 2] < a[i]) {   // 위로 올려 보내기
            swap(a[i / 2], a[i]);
            i /= 2;
        }
    }
    void print() {
        for (int i = 1; i < (int)a.size(); i++) cout << a[i] << " ";
        cout << "\n";
    }
};

int main() {
    MaxHeap h;
    for (int v : {9, 7, 8, 4, 3, 3, 5, 2, 1}) h.insert(v);
    cout << "heap:            "; h.print();
    h.insert(8);                      // 8이 위로 올라감
    cout << "after insert(8): "; h.print();
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "우선순위 큐 구현 (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- `deleteMax`에서는 *마지막* 원소가 루트를 대체한 뒤, 힙 순서가 복원될 때까지 더 큰 자식과 교환하며 [아래로 내려 보냅니다(percolate down)]{.hl}.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class MaxHeap {
    vector<int> a{0};
public:
    void insert(int x) {
        a.push_back(x);
        int i = a.size() - 1;
        while (i > 1 && a[i / 2] < a[i]) { swap(a[i / 2], a[i]); i /= 2; }
    }
    int deleteMax() {
        int mx = a[1];
        a[1] = a.back(); a.pop_back();
        int i = 1, n = a.size() - 1;
        while (2 * i <= n) {                          // 아래로 내려 보내기
            int c = 2 * i;
            if (c + 1 <= n && a[c + 1] > a[c]) c++;   // 더 큰 자식
            if (a[i] >= a[c]) break;
            swap(a[i], a[c]); i = c;
        }
        return mx;
    }
    void print() {
        for (int i = 1; i < (int)a.size(); i++) cout << a[i] << " ";
        cout << "\n";
    }
};

int main() {
    MaxHeap h;
    for (int v : {9, 8, 8, 4, 7, 3, 5, 2, 1, 3}) h.insert(v);
    cout << "heap:        "; h.print();
    cout << "deleteMax -> " << h.deleteMax() << "\n";
    cout << "after:       "; h.print();
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "queue 클래스를 이용한 우선순위 큐"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- C++는 `#include <queue>`에서 제네릭 [`priority_queue`]{.hl}를 제공합니다.
  - 기본값은 [최대 힙]{.hl}입니다: `top()`이 가장 큰 원소를 반환합니다.

- [최소 힙]{.hl}으로 쓰려면 비교자로 `greater<T>`를 전달합니다.

- `pair`의 경우 `.first` 우선, 그다음 `.second` 순으로 정렬됩니다.

</div>
<div>

```cpp
priority_queue<int> pq;
pq.push(1);
pq.push(9);
pq.push(3);
pq.top();   // 9 (최대 힙)

priority_queue<pair<int,int>> pq2;
pq2.push({1, 2});
pq2.push({1, 3});
pq2.push({3, 2});
pq2.top().first;   // 3
```

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <utility>
using namespace std;

int main() {
    priority_queue<int> pq;                 // 최대 힙
    pq.push(1); pq.push(9); pq.push(3);
    cout << "max-heap top: " << pq.top() << "\n";                 // 9

    priority_queue<pair<int,int>> pq2;
    pq2.push({1, 2}); pq2.push({1, 3}); pq2.push({3, 2});
    cout << "pair top.first: " << pq2.top().first << "\n";        // 3

    priority_queue<int, vector<int>, greater<int>> minpq;         // 최소 힙
    minpq.push(1); minpq.push(9); minpq.push(3);
    cout << "min-heap top: " << minpq.top() << endl;              // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "실습 — 더 맵게 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 매운 음식을 좋아하는 Leo는 *모든* 음식의 스코빌 지수를 최소 `K` 이상으로 만들고 싶어 합니다. 이를 위해 [가장 맵지 않은 두 음식]{.hl}을 반복해서 섞습니다:

<div class="theorem-box">
<div class="theorem-box-title">섞는 규칙</div>
<div class="theorem-box-body">

섞은 지수 = (가장 맵지 않은 지수) $+$ (두 번째로 맵지 않은 지수) $\times\ 2$

</div>
</div>

- 배열 `scoville`와 목표값 `K`가 주어질 때, 모든 음식이 `K` 이상이 되기까지 필요한 섞기 횟수의 *최솟값*을 반환하세요. 불가능하면 `-1`을 반환합니다.

- 예: `scoville = [1, 2, 3, 9, 10, 12]`, `K = 7` → 정답 `2`.

---
layout: prism
heading: "실습 — 더 맵게 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 이 문제는 우선순위 큐 ADT — `push()`, `top()`, `pop()` 연산을 활용합니다.

- `scoville` 값들을 우선순위 큐에 넣고, 남은 모든 음식이 `K` 이상이 될 때까지 가장 작은 값들을 꺼내어 섞기를 반복합니다.

- C++로 풀려면 다음을 할 수 있어야 합니다:
  - `priority_queue` 클래스를 사용할 수 있어야 하고,
  - 항상 가장 *작은* 두 지수가 필요하므로, C++의 기본 *최대 힙* `priority_queue`를 *최소 힙*으로(`greater<int>`로) 바꿔야 합니다.

---
layout: prism
heading: "실습 — 더 맵게 (3/3)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq;   // 최소 힙
    for (int s : scoville) pq.push(s);

    while (pq.size() >= 2 && pq.top() < K) {
        int a = pq.top(); pq.pop();          // 가장 맵지 않은 음식
        int b = pq.top(); pq.pop();          // 두 번째로 맵지 않은 음식
        answer++;
        pq.push(a + b * 2);                  // 섞어서 다시 넣기
    }
    if (!pq.empty() && pq.top() < K) return -1;   // 불가능
    return answer;
}

int main() {
    cout << solution({1, 2, 3, 9, 10, 12}, 7) << endl;   // 2
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "실습 — 디스크 컨트롤러 (1/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 하드 디스크는 한 번에 *하나*의 작업만 수행할 수 있습니다. 가장 단순한 컨트롤러는 요청을 [도착한 순서대로]{.hl} 처리합니다(FCFS).

- 세 개의 요청이 도착한다고 합시다:
  - `A`: 0 ms에 도착, 3 ms 소요
  - `B`: 1 ms에 도착, 9 ms 소요
  - `C`: 2 ms에 도착, 6 ms 소요

- 도착 순서 `A → B → C`로 처리하면, 반환 시간(요청 → 완료)은 각각 `3`, `11`, `16` ms이며, 평균은 `(3 + 11 + 16) / 3 = 10` ms입니다.

---
layout: prism
heading: "실습 — 디스크 컨트롤러 (2/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 하지만 대신 `A → C → B` 순서로 처리하면:
  - `A`: 3 ms에 완료 → 반환 시간 `3` ms
  - `C`: 2 ms부터 대기, 3–9 ms 실행 → 반환 시간 `7` ms
  - `B`: 1 ms부터 대기, 9–18 ms 실행 → 반환 시간 `17` ms

- 평균이 `(3 + 7 + 17) / 3 = 9` ms가 되어 FCFS보다 낫습니다.

- 각 행이 `[요청 시각, 소요 시간]`인 2차원 배열 `jobs`가 주어질 때, 평균 반환 시간의 *가능한 최솟값*(정수로 내림)을 반환하세요.

---
layout: prism
heading: "실습 — 디스크 컨트롤러 (3/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 이 문제도 우선순위 큐 ADT — `push()`, `top()`, `pop()`을 활용합니다.

- 전략은 현재 처리 가능한 작업들 중에서 [최단 작업 우선]{.hl}(shortest-job-first)입니다:
  - 대기 중인 작업이 없으면, 다음에 도착하는 작업으로 시간을 건너뛴 뒤 실행합니다.
  - 대기 중인 작업이 있으면, 항상 [소요 시간이 가장 짧은]{.hl} 작업을 다음으로 실행합니다.

- 소요 시간을 키로 하는 최소 힙을 쓰면 그 가장 짧은 대기 작업을 $O(\log N)$에 얻습니다.

---
layout: prism
heading: "실습 — 디스크 컨트롤러 (4/4)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    sort(jobs.begin(), jobs.end());          // 요청 시각 기준 정렬
    // (소요 시간, 요청 시각)을 키로 하는 최소 힙
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

    int idx = 0, time = 0;
    while (idx < (int)jobs.size() || !pq.empty()) {
        if (idx < (int)jobs.size() && time >= jobs[idx][0]) {
            pq.push({jobs[idx][1], jobs[idx][0]});   // (소요 시간, 요청 시각)
            idx++;
            continue;
        }
        if (!pq.empty()) {
            time += pq.top().first;              // 가장 짧은 작업 실행
            answer += time - pq.top().second;    // 반환 시간 더하기
            pq.pop();
        } else {
            time = jobs[idx][0];                 // 다음 도착으로 건너뛰기
        }
    }
    return answer / (int)jobs.size();
}

int main() {
    cout << solution({{0, 3}, {1, 9}, {2, 6}}) << endl;   // 9
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY_W04 — 양방향 우선순위 큐"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [양방향 우선순위 큐]{.hl}(double-ended priority queue)는 다음 명령을 지원합니다:

<div class="sub-item" style="font-size: 0.9em;">

| 명령 | 의미 |
|---|---|
| `I n` | 정수 `n` 삽입 |
| `D 1` | *최댓값* 삭제 |
| `D -1` | *최솟값* 삭제 |

</div>

- 명령 목록 `operations`가 주어질 때, 모든 명령을 적용한 뒤 큐의 `[최댓값, 최솟값]`을 반환하고, 비어 있으면 `[0, 0]`을 반환하세요. 빈 큐에 대한 삭제는 무시됩니다.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 0.2rem; font-size: 0.78rem;">

| operations | return |
|---|---|
| `["I 16","I -5643","D -1","D 1","D 1","I 123","D -1"]` | `[0, 0]` |
| `["I -45","I 653","D 1","I -642","I 45","I 97","D 1","D -1","I 333"]` | `[333, -45]` |

</div>

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <sstream>
using namespace std;

vector<int> solution(vector<string> operations) {
    multiset<int> s;
    for (auto& op : operations) {
        istringstream iss(op);
        string cmd; int num; iss >> cmd >> num;
        if (cmd == "I") s.insert(num);
        else if (!s.empty()) {
            if (num == 1) s.erase(prev(s.end()));   // 최댓값 삭제
            else          s.erase(s.begin());       // 최솟값 삭제
        }
    }
    if (s.empty()) return {0, 0};
    return { *prev(s.end()), *s.begin() };
}

int main() {
    auto r1 = solution({"I 16","I -5643","D -1","D 1","D 1","I 123","D -1"});
    cout << "[" << r1[0] << ", " << r1[1] << "]\n";   // [0, 0]
    auto r2 = solution({"I -45","I 653","D 1","I -642","I 45","I 97","D 1","D -1","I 333"});
    cout << "[" << r2[0] << ", " << r2[1] << "]\n";   // [333, -45]
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "그래프 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [그래프]{.hl}는 [노드(정점)]{.hl}와 [간선]{.hl}으로 데이터를 나타냅니다.

- 그래프는 도시 간 경로, 웹사이트 간 하이퍼링크, 사람들 사이의 행동 패턴, 뇌세포 간 연결성 등 다양한 것을 표현할 수 있습니다.
  - [유향]{.hl}, [무향]{.hl}, [가중]{.hl} 그래프가 있습니다.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 1.2rem;">
<svg width="220" height="200" viewBox="0 0 220 200" xmlns="http://www.w3.org/2000/svg">
  <g stroke="#475569" stroke-width="1.5">
    <line x1="110" y1="30" x2="55" y2="150"/>
    <line x1="110" y1="30" x2="175" y2="165"/>
    <line x1="55" y1="150" x2="175" y2="165"/>
  </g>
  <g font-size="14" font-family="monospace">
    <circle cx="110" cy="30" r="6" fill="#0f172a"/><text x="122" y="30" dy=".35em">A</text>
    <circle cx="55" cy="150" r="6" fill="#0f172a"/><text x="30" y="150" dy=".35em">B</text>
    <circle cx="175" cy="165" r="6" fill="#0f172a"/><text x="187" y="165" dy=".35em">C</text>
  </g>
  <text x="110" y="195" font-size="12" font-family="monospace" text-anchor="middle" fill="#64748b">{A, B, C, (A,B), (A,C), (B,C)}</text>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: "그래프 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 모든 그래프는 [1차원 단체 복합체]{.hl}(1-dimensional simplicial complex)로 볼 수 있습니다: 정점은 0-단체, 간선은 1-단체입니다.

- *채워진* 삼각형 `(A,B,C)` — 2-단체 — 를 추가하면 더 높은 차원의 복합체가 됩니다.

- 데이터 과학의 관점에서는 데이터를 [위상적으로]{.hl} 다룰 수 있으며, 이 접근을 [위상적 데이터 분석]{.hl}(topological data analysis)이라고 합니다.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 1.4rem;">
<svg width="260" height="130" viewBox="0 0 260 130" xmlns="http://www.w3.org/2000/svg">
  <g font-size="12" font-family="monospace">
    <circle cx="30" cy="20" r="5" fill="#0f172a"/><text x="40" y="20" dy=".35em">A</text>
    <circle cx="15" cy="90" r="5" fill="#0f172a"/><text x="0" y="90" dy=".35em">B</text>
    <circle cx="55" cy="95" r="5" fill="#0f172a"/><text x="63" y="95" dy=".35em">C</text>
  </g>
  <g stroke="#475569" stroke-width="1.5" font-size="12" font-family="monospace">
    <line x1="120" y1="20" x2="105" y2="90"/><line x1="120" y1="20" x2="150" y2="95"/><line x1="105" y1="90" x2="150" y2="95"/>
    <circle cx="120" cy="20" r="5" fill="#0f172a" stroke="none"/><text x="130" y="20" dy=".35em" stroke="none" fill="#0f172a">A</text>
    <circle cx="105" cy="90" r="5" fill="#0f172a" stroke="none"/><text x="88" y="90" dy=".35em" stroke="none" fill="#0f172a">B</text>
    <circle cx="150" cy="95" r="5" fill="#0f172a" stroke="none"/><text x="158" y="95" dy=".35em" stroke="none" fill="#0f172a">C</text>
  </g>
  <g stroke="#475569" stroke-width="1.5" font-size="12" font-family="monospace">
    <polygon points="220,20 205,90 250,95" fill="#3b6ea5" stroke="#475569"/>
    <text x="230" y="20" dy=".35em" stroke="none" fill="#0f172a">A</text>
    <text x="188" y="90" dy=".35em" stroke="none" fill="#0f172a">B</text>
    <text x="255" y="95" dy=".35em" stroke="none" fill="#0f172a">C</text>
  </g>
  <text x="35" y="122" font-size="9" font-family="monospace" text-anchor="middle" fill="#64748b">{A,B,C}</text>
  <text x="128" y="122" font-size="9" font-family="monospace" text-anchor="middle" fill="#64748b">+ edges</text>
  <text x="225" y="122" font-size="9" font-family="monospace" text-anchor="middle" fill="#64748b">+ (A,B,C)</text>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: "그래프 구현 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 그래프는 [행렬]{.hl}로 나타낼 수 있습니다.

- [인접 행렬]{.hl}(adjacency matrix)은 노드 `i`가 노드 `j`와 연결되어 있으면 `i`행 `j`열의 원소가 `1`, 그렇지 않으면 `0`입니다.

<div class="tikz-fig" style="display:inline-block; margin-top: 0.4rem;">
<svg width="200" height="150" viewBox="0 0 200 150" xmlns="http://www.w3.org/2000/svg">
  <g stroke="#475569" stroke-width="1.5">
    <line x1="60" y1="30" x2="25" y2="70"/><line x1="60" y1="30" x2="45" y2="120"/>
    <line x1="60" y1="30" x2="110" y2="70"/><line x1="60" y1="30" x2="175" y2="70"/>
    <line x1="25" y1="70" x2="45" y2="120"/><line x1="45" y1="120" x2="125" y2="120"/>
    <line x1="110" y1="70" x2="175" y2="70"/><line x1="125" y1="120" x2="175" y2="70"/>
  </g>
  <g font-size="13" font-family="monospace" text-anchor="middle">
    <circle cx="60" cy="30" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="60" y="30" dy=".35em">0</text>
    <circle cx="25" cy="70" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="25" y="70" dy=".35em">1</text>
    <circle cx="110" cy="70" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="110" y="70" dy=".35em">3</text>
    <circle cx="175" cy="70" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="175" y="70" dy=".35em">5</text>
    <circle cx="45" cy="120" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="45" y="120" dy=".35em">2</text>
    <circle cx="125" cy="120" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="125" y="120" dy=".35em">4</text>
  </g>
</svg>
</div>

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 1.2rem; font-family: monospace; font-size: 0.85rem;">

|   | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| **0** | 0 | 1 | 1 | 1 | 0 | 1 |
| **1** | 1 | 0 | 1 | 0 | 0 | 0 |
| **2** | 1 | 1 | 0 | 0 | 1 | 0 |
| **3** | 1 | 0 | 0 | 0 | 0 | 1 |
| **4** | 0 | 0 | 1 | 0 | 0 | 1 |
| **5** | 1 | 0 | 0 | 1 | 1 | 0 |

</div>

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N = 6;
    vector<vector<int>> adj(N, vector<int>(N, 0));
    int edges[][2] = {{0,1},{0,2},{0,3},{0,5},{1,2},{2,4},{3,5},{4,5}};
    for (auto& e : edges) { adj[e[0]][e[1]] = 1; adj[e[1]][e[0]] = 1; }

    cout << "   ";
    for (int j = 0; j < N; j++) cout << j << " ";
    cout << "\n";
    for (int i = 0; i < N; i++) {
        cout << i << ": ";
        for (int j = 0; j < N; j++) cout << adj[i][j] << " ";
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "그래프 구현 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 인접 행렬 구현은 $O(N^2)$의 공간과 시간을 필요로 합니다.

- 행렬 대신 [연결 리스트]{.hl}를 사용할 수 있습니다.
  - 각 노드가 자신의 [이웃]{.hl} 목록을 저장합니다.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 0.6rem; font-family: monospace; font-size: 0.9rem; line-height: 1.9;">

`0 →` `1 → 2 → 3 → 5 /`<br>
`1 →` `0 → 2 /`<br>
`2 →` `0 → 1 → 4 /`<br>
`3 →` `0 → 5 /`<br>
`4 →` `2 → 5 /`<br>
`5 →` `0 → 3 → 4 /`

</div>

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N = 6;
    vector<vector<int>> adj(N);
    int edges[][2] = {{0,1},{0,2},{0,3},{0,5},{1,2},{2,4},{3,5},{4,5}};
    for (auto& e : edges) {
        adj[e[0]].push_back(e[1]);
        adj[e[1]].push_back(e[0]);
    }
    for (int i = 0; i < N; i++) {
        cout << i << " -> ";
        for (int v : adj[i]) cout << v << " ";
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "그래프 구현 (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 연결 리스트 구현은 [희소 그래프에는 효율적]{.hl}이지만 [밀집 그래프에는 좋지 않습니다]{.hl}.

- 알고리즘 관점에서 그래프는 한 번 만들어지면 거의 바뀌지 않는 [정적]{.hl} 성질을 가지므로, 이웃 목록을 연결 리스트 대신 고정 크기 [배열]{.hl}에 저장할 수 있습니다.
  - 각 행은 차수(degree)와 이웃들의 압축된 배열을 유지합니다 — 캐시 친화적이고 순회하기 간단합니다.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 0.8rem; font-family: monospace; font-size: 0.85rem; line-height: 1.9;">

| node | deg | neighbors |
|---|---|---|
| 0 | 4 | `1 2 3 5` |
| 1 | 2 | `0 2` |
| 2 | 3 | `0 1 4` |
| 3 | 2 | `0 5` |
| 4 | 2 | `2 5` |
| 5 | 3 | `0 3 4` |

</div>

</div>
</div>

---
layout: prism
heading: 다익스트라 알고리즘
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [다익스트라 알고리즘]{.hl}(Dijkstra's algorithm)은 간선 가중치가 [음이 아닌]{.hl} 그래프에서 하나의 출발점으로부터의 최단 경로를 찾습니다.

- 정점들을 잠정 거리로 정렬한 [최소 우선순위 큐]{.hl}를 유지합니다:
  - 가장 가까운 정점을 꺼낸 뒤, 그 정점의 나가는 간선을 각각 [완화(relax)]{.hl}합니다.

- 출발점 `s = 0`; 기대 거리: `s=0, t=8, x=9, y=5, z=7`.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 0.4rem;">
<svg width="230" height="170" viewBox="0 0 230 170" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <path d="M0,0 L7,3 L0,6 Z" fill="#475569"/>
    </marker>
  </defs>
  <g stroke="#475569" stroke-width="1.3" font-size="11" font-family="monospace" fill="#64748b">
    <line x1="30" y1="85" x2="95" y2="35" marker-end="url(#ah)"/><text x="52" y="45">10</text>
    <line x1="30" y1="85" x2="95" y2="135" marker-end="url(#ah)"/><text x="52" y="130">5</text>
    <line x1="120" y1="35" x2="185" y2="35" marker-end="url(#ah)"/><text x="150" y="28">1</text>
    <line x1="118" y1="50" x2="105" y2="120" marker-end="url(#ah)"/><text x="96" y="90">2</text>
    <line x1="123" y1="120" x2="130" y2="52" marker-end="url(#ah)"/><text x="132" y="90">3</text>
    <line x1="130" y1="130" x2="185" y2="48" marker-end="url(#ah)"/><text x="167" y="100">9</text>
    <line x1="130" y1="135" x2="185" y2="135" marker-end="url(#ah)"/><text x="152" y="150">2</text>
    <line x1="198" y1="50" x2="198" y2="120" marker-end="url(#ah)"/><text x="205" y="90">4</text>
  </g>
  <g font-size="12" font-family="monospace" text-anchor="middle">
    <circle cx="20" cy="85" r="14" fill="#dbeafe" stroke="#0d9488" stroke-width="2"/><text x="20" y="85" dy=".35em">s</text>
    <circle cx="108" cy="35" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="108" y="35" dy=".35em">t</text>
    <circle cx="198" cy="35" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="198" y="35" dy=".35em">x</text>
    <circle cx="108" cy="135" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="108" y="135" dy=".35em">y</text>
    <circle cx="198" cy="135" r="14" fill="#fff" stroke="#0d9488" stroke-width="2"/><text x="198" y="135" dy=".35em">z</text>
  </g>
</svg>
</div>

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int main() {
    int N = 5;                      // 0=s, 1=t, 2=x, 3=y, 4=z
    vector<vector<pair<int,int>>> adj(N);   // (이웃, 가중치)
    auto add = [&](int u, int v, int w) { adj[u].push_back({v, w}); };
    add(0,1,10); add(0,3,5);
    add(1,2,1);  add(1,3,2);
    add(3,1,3);  add(3,2,9); add(3,4,2);
    add(2,4,4);
    add(4,2,6);  add(4,0,7);

    vector<int> dist(N, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});               // (거리, 정점)
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u])
            if (dist[u] + w < dist[v]) {        // 완화
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
    }
    const char* name = "stxyz";
    for (int i = 0; i < N; i++)
        cout << "dist(" << name[i] << ") = " << dist[i] << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 플로이드-워셜 알고리즘
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [플로이드-워셜]{.hl}(Floyd-Warshall)은 모든 정점 [쌍]{.hl} 사이의 최단 경로를 $O(N^3)$에 계산합니다.

- 중간 정점 `1..k`를 점진적으로 허용해 나갑니다:

<div class="theorem-box">
<div class="theorem-box-title">갱신 규칙</div>
<div class="theorem-box-body">

$d_{ij}^{(k)} = \min\!\left( d_{ij}^{(k-1)},\ d_{ik}^{(k-1)} + d_{kj}^{(k-1)} \right)$

</div>
</div>

- 하나의 공유 행렬 `d`를 제자리에서 갱신할 수 있습니다.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 1.0rem; font-family: monospace; font-size: 0.8rem;">

초기 가중치 `W`:

|   | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 0 | 3 | ∞ | 7 |
| 1 | 8 | 0 | 2 | ∞ |
| 2 | 5 | ∞ | 0 | 1 |
| 3 | 2 | ∞ | ∞ | 0 |

</div>

</div>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int INF = 1e9;
    int n = 4;
    vector<vector<int>> d = {
        {0,   3,   INF, 7  },
        {8,   0,   2,   INF},
        {5,   INF, 0,   1  },
        {2,   INF, INF, 0  }
    };
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (d[i][k] + d[k][j] < d[i][j])
                    d[i][j] = d[i][k] + d[k][j];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (d[i][j] >= INF) cout << "INF ";
            else                cout << d[i][j] << "   ";
        }
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "실습 — 순위 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `1..n`로 번호가 매겨진 `n`명의 복서가 일대일 경기를 합니다. 복서 `A`가 `B`보다 강하면, `A`는 `B`를 [항상 이깁니다]{.hl}.

- 심판은 경기 결과로부터 선수들의 순위를 매기고 싶지만, 일부 결과가 유실되어 모든 순위를 확정할 수는 없습니다.

- `n`과 (각 행 `[A, B]`가 `A`가 `B`를 이겼음을 의미하는) 2차원 배열 `results`가 주어질 때, [정확한 순위]{.hl}를 확정할 수 있는 선수의 수를 반환하세요.

- 제약: `n ≤ 100`, 결과는 최대 `4500`개, 모순 없음. 예: `n = 5`, `results = [[4,3],[4,2],[3,2],[1,2],[2,5]]` → `2`.

---
layout: prism
heading: "실습 — 순위 (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [플로이드-워셜]{.hl} 알고리즘은 최단 경로를 계산합니다. 예를 들어 `a → c`의 비용이 100인데 `a → b`가 10, `b → c`가 20이라면, 중간 정점 `b`를 거쳐 `a → c`를 30으로 보정합니다.

- 이 *동일한 전이 폐포(transitive closure)* 아이디어를 승패 관계에 적용할 수 있습니다:
  - `a`가 `b`를 이기고 `b`가 `c`를 이기면, `a`가 `c`를 이긴다고 [유추]{.hl}할 수 있습니다.

- 한 선수의 순위는 나머지 `n - 1`명 전원에 대해 [승패 관계가 알려질 때]{.hl} 정확히 확정됩니다.

---
layout: prism
heading: "실습 — 순위 (3/3)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int solution(int n, vector<vector<int>> results) {
    // win[i][j] = true 이면 i가 j를 이긴 것으로 알려짐
    vector<vector<bool>> win(n + 1, vector<bool>(n + 1, false));
    for (auto& r : results) win[r[0]][r[1]] = true;

    // 플로이드-워셜 방식의 전이 폐포
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (win[i][k] && win[k][j]) win[i][j] = true;

    int answer = 0;
    for (int i = 1; i <= n; i++) {
        int cnt = 0;
        for (int j = 1; j <= n; j++)
            if (i != j && (win[i][j] || win[j][i])) cnt++;
        if (cnt == n - 1) answer++;     // 모두에 대해 관계가 알려짐
    }
    return answer;
}

int main() {
    cout << solution(5, {{4,3},{4,2},{3,2},{1,2},{2,5}}) << endl;   // 2
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
