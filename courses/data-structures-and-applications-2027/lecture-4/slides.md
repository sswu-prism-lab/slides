---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 4
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-4-ko/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Data Structures and Applications</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 04: Trees, Heaps, Priority Queues, and Graphs</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">Wonjun Ko, Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">Fall 2027</p>
</div>

---
layout: prism
heading: "Recap: the stack Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- C++ provides a generic [`stack`]{.hl} class in `#include <stack>`.

- A stack is a [LIFO]{.hl} (last-in, first-out) container.
  - `push` adds to the top, `pop` removes the top, and `top` reads it.

- Declare one with `stack<elementType> name;`.

</div>
<div>

```cpp
#include <stack>
stack<int> s;
s.push(3);   // add on top
s.pop();     // remove the top
s.top();     // read the top
s.size();    // number of elements
s.empty();   // true if empty
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
    while (!s.empty()) {          // pops in LIFO order
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
heading: "Recap: the queue Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- C++ provides a generic [`queue`]{.hl} class in `#include <queue>`.

- A queue is a [FIFO]{.hl} (first-in, first-out) container.
  - `push` adds to the back, `pop` removes from the front, `front` reads it.

- Declare one with `queue<elementType> name;`.

</div>
<div>

```cpp
#include <queue>
queue<int> q;
q.push(3);   // add at the back
q.pop();     // remove the front
q.front();   // read the front
q.size();    // number of elements
q.empty();   // true if empty
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
    while (!q.empty()) {          // pops in FIFO order
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
heading: "Tree, Binary Tree, and Heap (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A [tree]{.hl} represents a hierarchical *tree structure* with a set of connected nodes.
  - Each node can be connected to many children.
  - There are no cycles or loops, and every child is itself the root of its own [subtree]{.hl}.

- In a [binary tree]{.hl} (이진 트리), an arbitrary node has fewer than three (0, 1, or 2) child nodes.

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
heading: "Tree, Binary Tree, and Heap (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- In a [full binary tree]{.hl} (포화 이진 트리), every node except the leaves (terminal nodes) has exactly two children.

- A [complete binary tree]{.hl} (완전 이진 트리) is a binary tree in which every level, except possibly the last, is completely filled, and all nodes on the last level are as far *left* as possible.

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
heading: "Tree, Binary Tree, and Heap (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [heap]{.hl} must satisfy two constraints:
  - A heap is a *complete binary tree*.
  - Every node's value is [not larger than]{.hl} its children (a [Min Heap]{.hl}; 최소 힙), or [not smaller than]{.hl} its children (a [Max Heap]{.hl}; 최대 힙).

- Thus the minimum (or maximum) always sits at the [root]{.hl}.

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
heading: Complete Binary Tree Implementation
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- A [list (array)]{.hl} is appropriate for representing a complete binary tree; for easier implementation we *skip* index 0.

- With a [1-based index]{.hl}, for an element at index `i`:
  - left child is at `2i` (`2i+1` for 0-based)
  - right child is at `2i+1` (`2i+2` for 0-based)
  - parent is at `i/2` (`(i-1)/2` for 0-based)

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
    // 1-based complete binary tree; index 0 unused
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
heading: The Priority Queue ADT
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [priority queue]{.hl} stores elements so that the highest-priority one is always accessible first. Its ADT typically supports:

<div class="sub-item">

| Operation | Description |
|---|---|
| `insert` | insert an element |
| `deleteMax` | remove the highest-priority (maximum) element |
| `max` | return the maximum element |
| `isEmpty` | check whether the priority queue is empty |
| `clear` | remove all elements |

</div>

- ...or any others you need (e.g., `sort`, `size`, and so on).

---
layout: prism
heading: "Priority Queue Implementation (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- We can use a *sorted array*, a *sorted linked list*, or any other structure to implement a priority queue.

- A [heap]{.hl} is the most effective way to implement a priority queue.
  - It takes $O(\log N)$ time to insert or remove an element.

- We store the heap in an array; `insert(8)` first appends `8` at the next free slot `A[10]`.

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
heading: "Priority Queue Implementation (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- For `insert`, the new element is compared with its parent and [percolated up]{.hl} until it is no larger than its parent (in a max heap).

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class MaxHeap {
    vector<int> a{0};                 // index 0 unused
public:
    void insert(int x) {
        a.push_back(x);
        int i = a.size() - 1;
        while (i > 1 && a[i / 2] < a[i]) {   // percolate up
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
    h.insert(8);                      // 8 percolates up
    cout << "after insert(8): "; h.print();
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Priority Queue Implementation (3/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- For `deleteMax`, the *last* element replaces the root, which is then [percolated down]{.hl} by swapping with its larger child until the heap order is restored.

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
        while (2 * i <= n) {                          // percolate down
            int c = 2 * i;
            if (c + 1 <= n && a[c + 1] > a[c]) c++;   // larger child
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
heading: "Priority Queue using the queue Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- C++ provides a generic [`priority_queue`]{.hl} in `#include <queue>`.
  - By default it is a [max heap]{.hl}: `top()` returns the largest element.

- For a [min heap]{.hl}, pass `greater<T>` as the comparator.

- With `pair`, ordering is by `.first`, then `.second`.

</div>
<div>

```cpp
priority_queue<int> pq;
pq.push(1);
pq.push(9);
pq.push(3);
pq.top();   // 9 (max heap)

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
    priority_queue<int> pq;                 // max heap
    pq.push(1); pq.push(9); pq.push(3);
    cout << "max-heap top: " << pq.top() << "\n";                 // 9

    priority_queue<pair<int,int>> pq2;
    pq2.push({1, 2}); pq2.push({1, 3}); pq2.push({3, 2});
    cout << "pair top.first: " << pq2.top().first << "\n";        // 3

    priority_queue<int, vector<int>, greater<int>> minpq;         // min heap
    minpq.push(1); minpq.push(9); minpq.push(3);
    cout << "min-heap top: " << minpq.top() << endl;              // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Practice — Make It Spicier (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Leo, who loves spicy food, wants *every* food's Scoville score to be at least `K`. To do so he repeatedly mixes the [two least-spicy]{.hl} foods:

<div class="theorem-box">
<div class="theorem-box-title">Mixing rule</div>
<div class="theorem-box-body">

mixed score = (least spicy score) $+$ (second least spicy score) $\times\ 2$

</div>
</div>

- Given the array `scoville` and target `K`, return the *minimum* number of mixings needed so that all foods reach at least `K`. If it is impossible, return `-1`.

- Example: `scoville = [1, 2, 3, 9, 10, 12]`, `K = 7` → answer `2`.

---
layout: prism
heading: "Practice — Make It Spicier (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- This uses the priority queue ADT — the `push()`, `top()`, `pop()` operations.

- Repeatedly feed the `scoville` values into a priority queue, then pop off the smallest ones and mix, until every remaining food is at least `K`.

- To solve it in C++, you must:
  - be able to use the `priority_queue` class, and
  - turn C++'s default *max-heap* `priority_queue` into a *min-heap* (with `greater<int>`), since we always need the two *smallest* scores.

---
layout: prism
heading: "Practice — Make It Spicier (3/3)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, greater<int>> pq;   // min heap
    for (int s : scoville) pq.push(s);

    while (pq.size() >= 2 && pq.top() < K) {
        int a = pq.top(); pq.pop();          // least spicy
        int b = pq.top(); pq.pop();          // second least spicy
        answer++;
        pq.push(a + b * 2);                  // mix and push back
    }
    if (!pq.empty() && pq.top() < K) return -1;   // impossible
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
heading: "Practice — Disk Controller (1/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A hard disk can perform only *one* job at a time. The most naive controller processes requests [in the order they arrive]{.hl} (FCFS).

- Suppose three requests arrive:
  - `A`: at 0 ms, takes 3 ms
  - `B`: at 1 ms, takes 9 ms
  - `C`: at 2 ms, takes 6 ms

- Processing in arrival order `A → B → C`, the turnaround times (request → completion) are `3`, `11`, and `16` ms, for an average of `(3 + 11 + 16) / 3 = 10` ms.

---
layout: prism
heading: "Practice — Disk Controller (2/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- But if we instead process in the order `A → C → B`:
  - `A`: completes at 3 ms → turnaround `3` ms
  - `C`: waits from 2 ms, runs 3–9 ms → turnaround `7` ms
  - `B`: waits from 1 ms, runs 9–18 ms → turnaround `17` ms

- The average becomes `(3 + 7 + 17) / 3 = 9` ms — better than FCFS.

- Given a 2-D array `jobs` where each row is `[request time, duration]`, return the *minimum possible* average turnaround time (truncated to an integer).

---
layout: prism
heading: "Practice — Disk Controller (3/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Again this uses the priority queue ADT — `push()`, `top()`, `pop()`.

- The strategy is [shortest-job-first]{.hl} among the currently available jobs:
  - When no job is waiting, jump forward to the next arriving job and run it.
  - When jobs are waiting, always run the one with the [shortest duration]{.hl} next.

- A min-heap keyed on duration gives us that shortest waiting job in $O(\log N)$.

---
layout: prism
heading: "Practice — Disk Controller (4/4)"
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
    sort(jobs.begin(), jobs.end());          // by request time
    // min heap keyed on (duration, request time)
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

    int idx = 0, time = 0;
    while (idx < (int)jobs.size() || !pq.empty()) {
        if (idx < (int)jobs.size() && time >= jobs[idx][0]) {
            pq.push({jobs[idx][1], jobs[idx][0]});   // (duration, request)
            idx++;
            continue;
        }
        if (!pq.empty()) {
            time += pq.top().first;              // run shortest job
            answer += time - pq.top().second;    // add its turnaround
            pq.pop();
        } else {
            time = jobs[idx][0];                 // jump to next arrival
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
heading: "DIY_W04 — Double-Ended Priority Queue"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- A [double-ended priority queue]{.hl} supports these commands:

<div class="sub-item" style="font-size: 0.9em;">

| Command | Meaning |
|---|---|
| `I n` | insert integer `n` |
| `D 1` | delete the *maximum* |
| `D -1` | delete the *minimum* |

</div>

- Given a list of `operations`, after applying all of them return `[max, min]` of the queue, or `[0, 0]` if it is empty. Deletions on an empty queue are ignored.

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
            if (num == 1) s.erase(prev(s.end()));   // delete max
            else          s.erase(s.begin());       // delete min
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
heading: "Graph (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A [graph]{.hl} represents data using [nodes (vertices)]{.hl} and [edges]{.hl}.

- Graphs can represent pathways between cities, hyperlinks between websites, behavioral patterns between people, connectivity between brain cells, and much more.
  - There exist [directed]{.hl}, [undirected]{.hl}, and [weighted]{.hl} graphs.

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
heading: "Graph (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Every graph can be considered a [1-dimensional simplicial complex]{.hl}: vertices are 0-simplices and edges are 1-simplices.

- Adding the *filled* triangle `(A,B,C)` — a 2-simplex — yields a higher-dimensional complex.

- From a data-science viewpoint, we can consider data in a [topological]{.hl} manner; this approach is called [topological data analysis]{.hl}.

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
heading: "Graph Implementation (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- We can represent a graph with a [matrix]{.hl}.

- An [adjacency matrix]{.hl} (인접 행렬) has `1` at row `i`, column `j` if node `i` is connected to node `j`, and `0` otherwise.

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
heading: "Graph Implementation (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The adjacency-matrix implementation requires $O(N^2)$ space and time.

- We can use a [linked list]{.hl} instead of a matrix.
  - Each node stores a list of its [neighbors]{.hl}.

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
heading: "Graph Implementation (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The linked-list implementation is [efficient for sparse graphs]{.hl}, but [not good for dense graphs]{.hl}.

- Since graphs tend to be [static]{.hl} in the algorithmic viewpoint (rarely changed once built), we can store the neighbor lists in fixed [arrays]{.hl} instead of linked lists.
  - Each row keeps a degree count and a compact array of neighbors — cache-friendly and simple to iterate.

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
heading: Dijkstra's Algorithm
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [Dijkstra's algorithm]{.hl} finds shortest paths from a single source in a graph with [non-negative]{.hl} edge weights.

- Keep a [min-priority queue]{.hl} of vertices keyed by their tentative distance:
  - extract the closest vertex, then [relax]{.hl} each of its outgoing edges.

- Source `s = 0`; expected distances: `s=0, t=8, x=9, y=5, z=7`.

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
    vector<vector<pair<int,int>>> adj(N);   // (neighbor, weight)
    auto add = [&](int u, int v, int w) { adj[u].push_back({v, w}); };
    add(0,1,10); add(0,3,5);
    add(1,2,1);  add(1,3,2);
    add(3,1,3);  add(3,2,9); add(3,4,2);
    add(2,4,4);
    add(4,2,6);  add(4,0,7);

    vector<int> dist(N, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    dist[0] = 0; pq.push({0, 0});               // (distance, vertex)
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u])
            if (dist[u] + w < dist[v]) {        // relax
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
heading: Floyd-Warshall Algorithm
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [Floyd-Warshall]{.hl} computes shortest paths between [all pairs]{.hl} of vertices in $O(N^3)$.

- It gradually allows intermediate vertices `1..k`:

<div class="theorem-box">
<div class="theorem-box-title">Update rule</div>
<div class="theorem-box-body">

$d_{ij}^{(k)} = \min\!\left( d_{ij}^{(k-1)},\ d_{ik}^{(k-1)} + d_{kj}^{(k-1)} \right)$

</div>
</div>

- One shared matrix `d` can be updated in place.

</div>
<div>

<div class="tikz-fig" style="display:inline-block; margin-top: 1.0rem; font-family: monospace; font-size: 0.8rem;">

Initial weights `W`:

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
heading: "Practice — Ranking (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- `n` boxers, numbered `1..n`, compete in one-on-one matches. If boxer `A` is stronger than `B`, then `A` [always beats]{.hl} `B`.

- A referee wants to rank the players from the match results, but some results are lost, so not every rank can be determined.

- Given `n` and a 2-D array `results` (each row `[A, B]` meaning `A` beat `B`), return how many players' [exact ranks]{.hl} can be determined.

- Constraints: `n ≤ 100`, up to `4500` results, no contradictions. Example: `n = 5`, `results = [[4,3],[4,2],[3,2],[1,2],[2,5]]` → `2`.

---
layout: prism
heading: "Practice — Ranking (2/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The [Floyd-Warshall]{.hl} algorithm computes shortest paths, e.g. if `a → c` costs 100 while `a → b` is 10 and `b → c` is 20, it corrects `a → c` to 30 through the intermediate `b`.

- We can apply the *same transitive-closure* idea to win/lose relations:
  - if `a` beats `b` and `b` beats `c`, then we can [infer]{.hl} `a` beats `c`.

- A player's rank is fully determined exactly when their [win/lose relation is known against all]{.hl} `n - 1` other players.

---
layout: prism
heading: "Practice — Ranking (3/3)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int solution(int n, vector<vector<int>> results) {
    // win[i][j] = true means i is known to beat j
    vector<vector<bool>> win(n + 1, vector<bool>(n + 1, false));
    for (auto& r : results) win[r[0]][r[1]] = true;

    // Floyd-Warshall-style transitive closure
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (win[i][k] && win[k][j]) win[i][j] = true;

    int answer = 0;
    for (int i = 1; i <= n; i++) {
        int cnt = 0;
        for (int j = 1; j <= n; j++)
            if (i != j && (win[i][j] || win[j][i])) cnt++;
        if (cnt == n - 1) answer++;     // relation known against everyone
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

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
