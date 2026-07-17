---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 2
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-2-ko/
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
  <h1 style="color:#5c60a8; font-size: 3rem; font-weight: bold; margin: 0rem;">Data Structures and Applications</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 02: Abstract Data Types and the List ADT</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 4rem;">Wonjun Ko, Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">Fall 2027</p>
</div>

---
layout: prism
heading: Abstract Data Types and the List ADT
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- In this lecture we introduce our first data structure, the [List]{.hl}, together with the idea of an *abstract data type*:

  - Define what an [abstract data type (ADT)]{.hl} is and why it matters.

  - Specify the [List ADT]{.hl} and its operations.

  - Compare the [array]{.hl} and [linked-list]{.hl} implementations of a list.

  - Practice with classic list problems: rotation, maximum subarray, palindromes, and Josephus.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Abstract Data Types</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Idea of an ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The List ADT</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">List Implementations</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Array Implementation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Singly, Circular, and Doubly Linked Lists</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Practice with Lists</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Rotation, Maximum Subarray, Palindrome, Josephus</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">The Stack ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Stacks and Their Implementation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Cooler Days, Reversal, Balanced Parentheses, Postfix</span></p>
  </div>

</div>

---
layout: prism
heading: Abstract Data Type
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- An [abstract data type (ADT)]{.hl} is a set of objects together with a set of *operations* on those objects.

- Many programming languages (e.g., C++, Python) support the implementation of ADTs, with appropriate *hiding of implementation details*.
  - If the implementation must be changed, it should be easy to do so by merely changing the routines that perform the ADT operations.
  - Ideally, that change is completely *transparent* to the rest of the program.

- There is no rule telling us which operations must be supported for each ADT — this is a [design decision]{.hl}.

---
layout: prism
heading: The List ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [list]{.hl} is an ordered sequence of elements $a_0, a_1, \ldots, a_{N-1}$.

- The List ADT bundles the sequence with the operations we want to perform on it.

- Any others we need may be added (for example `sort`).

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">List ADT operations</div>
<div class="theorem-box-body">

- `printList` — print the list
- `makeEmpty` — empty the list
- `insert` — insert `x` at the `i`-th position
- `remove` — remove the `i`-th element (or `x`)
- `find` — find the index of an element `x`
- `findKth` — return the element at an index
- `size` — return the number of elements

</div>
</div>

</div>
</div>

---
layout: prism
heading: Array Implementation of Lists
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The List ADT can be implemented simply by using an [array]{.hl}.
  - `printList` runs in *linear* time, and `findKth` runs in *constant* time.
  - `insert` and `remove` are potentially expensive — $\mathcal{O}(1) \sim \mathcal{O}(N)$ — depending on where the change occurs.

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
heading: "DIY: Array-Based List"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class ArrayList {          // an array-backed List ADT
    vector<int> a;
public:
    void insert(int i, int x) { a.insert(a.begin() + i, x); } // shift right
    void remove(int i)        { a.erase(a.begin() + i); }     // shift left
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
heading: Singly Linked Lists (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- To avoid the linear cost of `insert` and `remove`, we ensure that the list is [not stored contiguously]{.hl}.

- A [linked list]{.hl} consists of a series of *nodes*, which are not necessarily adjacent in memory.
  - Each node contains the element and a `next` link to the node holding its successor.
  - The last node's `next` link points to `nullptr`.

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
heading: Singly Linked Lists (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `printList` and `find` are clearly *linear-time*, as in the array implementation.

- The `findKth` operation is no longer as efficient as with an array.
  - `findKth(i)` takes $\mathcal{O}(i)$ time and works by traversing down the list in the obvious manner.
  - In practice this bound is pessimistic, because calls to `findKth` are frequently in sorted order (by `i`).

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
heading: Singly Linked Lists (3/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The `remove` method can be executed with a *single* `next` pointer change.

- The `insert` method obtains a new node via `new`, then performs *two* `next` pointer maneuvers.

- In principle, if we know *where* a change is to be made, inserting or removing an item [does not require moving many items]{.hl}.

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
heading: "DIY: Singly Linked List"
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
    void pushBack(int x) {                 // append at the end
        Node* n = new Node(x);
        if (!head) { head = n; return; }
        Node* t = head;
        while (t->next) t = t->next;
        t->next = n;
    }
    void insertAfter(int val, int x) {     // insert x right after node 'val'
        for (Node* t = head; t; t = t->next)
            if (t->data == val) {
                Node* n = new Node(x);
                n->next = t->next;         // maneuver 1
                t->next = n;               // maneuver 2
                return;
            }
    }
    void removeVal(int x) {                // one next-pointer change
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
heading: Circular Linked Lists
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- In a plain linked list, accessibility of the first and last nodes is [dramatically different]{.hl}.
  - We can reach the first node immediately, but must follow every link to reach the final node.
  - For an $N$-element list, `insert`/`remove` at the front is $\mathcal{O}(1)$, but at the end is $\mathcal{O}(N)$.

- In a [circular linked list]{.hl}, the last node's `next` pointer points back at the first node, removing this asymmetry (often with a `tail` pointer as well).

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
heading: Doubly Linked Lists
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Nodes in a singly or circular linked list are linked in a [unidirectional]{.hl} manner.
  - Given an arbitrary node, we cannot go back unless the previous node was saved.

- In a [doubly linked list]{.hl}, each node is linked in a *bidirectional* manner — connected to both neighbors via `next` and `prev`.

- Furthermore, a doubly linked list can itself be *circular*.

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
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Abstract Data Types</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">List Implementations</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Practice with Lists</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Rotating an Array</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Maximum Subarray (Brute Force and Kadane)</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Palindrome via a Doubly Linked List</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Josephus Problem</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Multiply or Add</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Stack ADT</span></p>
  </div>

</div>

---
layout: prism
heading: Rotating an Array
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Given an array, push each element back by a given amount $k$ and wrap the pushed-off elements around to the front.
  - Input: `[1, -2, 3, 5, -4, 2, 5]`, `k = 3`
  - Output: `[-4, 2, 5, 1, -2, 3, 5]`

- A [brute-force]{.hl} approach rotates one position at a time, repeated $k$ times — the cost grows with $k$.

- More efficiently, we can [cut off the last $k$ elements and attach them at the front]{.hl}. A neat trick achieves this with three array *reversals* in $\mathcal{O}(N)$ time.

---
layout: prism
heading: "DIY: Rotating an Array"
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
    for (int i = 0; i < k; ++i) {          // shift right by one, k times
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
    rev(0, n - 1); rev(0, k - 1); rev(k, n - 1);   // reverse-all, then two halves
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
heading: Maximum Subarray
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Among all *contiguous* subarrays, find the one with the largest sum and report its start/end indices.
  - Input: `[1, -2, 3, 5, -4, 2, 5]`
  - Output: start `2`, end `6` (the subarray `[3, 5, -4, 2, 5]`, sum $= 11$)

- The [brute-force]{.hl} method sums every subarray $A[i..j]$ and keeps the maximum.

- It is easy to implement but runs in $\mathcal{O}(N^2)$ — enough to be blocked by time limits in a coding test.

---
layout: prism
heading: "Maximum Subarray: Kadane's Algorithm"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Using [dynamic programming]{.hl}, we lower the complexity to $\mathcal{O}(N)$.

- At each position, the best subarray *ending here* either *extends* the previous best or *restarts* from the current element.

<div class="flex justify-center" style="margin-top: 1.4rem;">
  <table style="border-collapse: collapse; font-family: monospace; text-align: center;">
    <tr>
      <td style="padding: 0.3rem 0.6rem; color:#4a6fa5;">element</td>
      <td class="cell">1</td><td class="cell">-2</td><td class="cell">3</td><td class="cell">5</td><td class="cell">-4</td><td class="cell">2</td><td class="cell">5</td>
    </tr>
    <tr>
      <td style="padding: 0.3rem 0.6rem; color:#4a6fa5;">best sum</td>
      <td class="cell">1</td><td class="cell">-1</td><td class="cell">3</td><td class="cell">8</td><td class="cell">4</td><td class="cell">6</td><td class="cell cell-hl">11</td>
    </tr>
  </table>
</div>

---
layout: prism
heading: "DIY: Maximum Subarray"
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
        if (a[i] > cur + a[i]) { cur = a[i]; tmp = i; }   // restart
        else                     cur += a[i];             // extend
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
heading: Palindrome
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A [palindrome]{.hl} is a word or phrase that reads the same forward and backward.
  - `noon`, `eye`, `kayak`, `level`, `racecar`, ...

- Insert the given string into a [doubly linked list]{.hl}, then compare characters from *both ends* moving inward.
  - Because each node links to its predecessor, walking from the tail toward the head is convenient.

---
layout: prism
heading: "DIY: Palindrome via a Doubly Linked List"
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
        while (s && e && s != e && e->next != s) {   // walk inward from both ends
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
heading: The Josephus Problem
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- $N$ people stand in a circle. Repeatedly count off and eliminate every $M$-th person; return the index of the last survivor.
  - Input: $N = 10$, $M = 3$
  - Output: person `4`

- Model the circle with a [circular linked list]{.hl}: insert the $N$ indices, then walk around in steps of $M$, deleting each person reached until a single node remains.

---
layout: prism
heading: "DIY: Josephus via a Circular Linked List"
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
        while (ptr->next != ptr) {          // until one node remains
            int count = 1;
            while (count != m) { prev = ptr; ptr = ptr->next; ++count; }
            prev->next = ptr->next;         // unlink the m-th node
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
heading: Multiply or Add
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Given a string of digits (`0`–`9`), place either `+` or `×` between each pair of adjacent digits to maximize the result. All operations are applied *left to right*.
  - Input: `02984` &nbsp;→&nbsp; Output: `576`
  - Input: `567` &nbsp;→&nbsp; Output: `210`

- [Greedy rule]{.hl}: multiplying grows a number faster than adding, *except* when a `0` or `1` is involved — in that case add instead.

---
layout: prism
heading: "DIY: Multiply or Add"
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
        if (result <= 1 || d <= 1) result += d;   // add when 0 or 1 is involved
        else                       result *= d;   // otherwise multiply
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
heading: "W02_DIY01: Is the Linked List Circular?"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Write a function that decides whether a given linked list is *circular*.

- Use [Floyd's tortoise and hare]{.hl}: advance one pointer by one step and another by two.
  - If they ever meet, the list contains a cycle.
  - If the fast pointer reaches `nullptr`, the list is a plain (acyclic) list.

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
    a->next->next->next = a;        // close the loop
    cout << "loop:  " << isCircular(a) << "\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "W02_DIY02: Remove a Node from a Doubly Linked List"
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
    void remove(int x) {                       // fix up to four links
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
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Abstract Data Types</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">List Implementations</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Practice with Lists</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">The Stack ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Stacks and Their Implementation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Next Cooler Day and String Reversal</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Balanced Parentheses</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Infix to Postfix and Postfix Evaluation</span></p>
  </div>

</div>

---
layout: prism
heading: The Stack ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [stack]{.hl} is a list with the restriction that insertions and deletions may be performed in *only one position* — the end of the list, called the [top]{.hl}.
  - Stacks are known as [LIFO]{.hl} (last in, first out) lists.
  - Only the top element is accessible.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">Stack ADT operations</div>
<div class="theorem-box-body">

- `push` — add an element on the top
- `top` — inspect the top element
- `pop` — remove the top element
- or any others (for example `popAll`)

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
  <div style="font-size: 0.8rem; color:#4a6fa5;">← <code>top</code><br/>(only this is<br/>accessible)</div>
</div>

</div>
</div>

---
layout: prism
heading: Implementation of Stacks
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Since a stack is a list, [any list implementation]{.hl} will do.

- `push` and `pop` run in not merely constant time but *very fast* constant time.
  - On some machines they compile to a single instruction using auto-increment/auto-decrement addressing, and most modern machines have stack operations built into the instruction set.
  - The stack is the most fundamental data structure in computer science, after the array.

- An [array implementation]{.hl} may not know the final length in advance, so it must reserve enough space, which can lower efficiency.
  - A [linked-list implementation]{.hl} is a flexible alternative that grows exactly as needed.

---
layout: prism
heading: "DIY: Basic Stack Operations"
---

<CppRunner>

```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    for (int x : {10, 77, 3, 21, 83, 34}) {   // push in order
        s.push(x);
        cout << "push(" << x << ")  top = " << s.top() << ", size = " << s.size() << "\n";
    }
    cout << "--- popping (LIFO order) ---\n";
    while (!s.empty()) {
        cout << "pop " << s.top() << "\n";     // last in comes out first
        s.pop();
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Next Cooler Day
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Given a week of temperatures, for each day print the temperature of the *next* day that is cooler; print `-1` if no later day is cooler.
  - Input: `[4, 5, 2, 10, 8, 6, 12]`
  - Output: `[2, 2, -1, 8, 6, -1, -1]`

- Solve it with a [stack of indices]{.hl}: while the current temperature is cooler than the day on top of the stack, that day has found its answer, so pop it and record the result.
  - Each index is pushed and popped at most once, giving an $\mathcal{O}(N)$ scan.

---
layout: prism
heading: "DIY: Next Cooler Day"
---

<CppRunner>

```cpp
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

vector<int> nextCoolerDay(const vector<int>& t) {
    vector<int> result(t.size(), -1);   // default: no cooler day ahead
    stack<int> s;                       // indices of days still waiting
    for (int i = 0; i < (int)t.size(); ++i) {
        while (!s.empty() && t[s.top()] > t[i]) {   // today is cooler
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
heading: Reversing a String
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Print the given string in reverse order.
  - Input: `Sungshin` &nbsp;→&nbsp; Output: `nihsgnuS`

- Push every character onto a [stack]{.hl}, then pop them back off: the LIFO order naturally produces the characters in reverse, which we concatenate into the new string.

---
layout: prism
heading: "DIY: Reversing a String"
---

<CppRunner>

```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

string reverseString(const string& input) {
    stack<char> s;
    for (char ch : input) s.push(ch);   // push each character
    string reversed;
    while (!s.empty()) {                 // pop in LIFO order
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
heading: Balanced Parentheses
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Brackets of several kinds — `()`, `{}`, `[]` — must be closed in the correct order after they are opened.
  - Print `true` if every bracket is properly matched, `false` otherwise.
  - `{[()]}` → `true` &nbsp;&nbsp; `{([)}]` → `false` &nbsp;&nbsp; `(hello){}[bye]` → `true`

- [Push]{.hl} each opening bracket onto a stack; on a closing bracket, check the [top]{.hl} and `pop` only when it is the matching opener. The expression is balanced exactly when the stack ends empty.

---
layout: prism
heading: "DIY: Balanced Parentheses"
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
heading: Infix and Postfix Notation
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [Infix]{.hl} notation places each operator *between* its operands — the usual way we write expressions, e.g. `a + b * (c - d) / e`.

- [Postfix]{.hl} (reverse Polish) notation places each operator *after* its operands, needing no parentheses.

- Fully parenthesize by precedence, move each operator just past its closing parenthesis, then erase the parentheses.

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
heading: "DIY: Infix to Postfix"
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
            if (!s.empty()) s.pop();                 // discard '('
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
heading: "W02_DIY04: Evaluate a Postfix Expression"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Compute the value of an expression given in [postfix]{.hl} form.

- Scan left to right with a [stack of operands]{.hl}:
  - `push` each digit;
  - on an operator, `pop` the two operands, apply it, and `push` the result.
  - The final value left on the stack is the answer.

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

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
