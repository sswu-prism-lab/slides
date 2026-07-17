---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 6
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-6-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 06: The List ADT and C++ Containers</p>

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
heading: Overview
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- In this lecture we review the core linear and hierarchical data structures and their C++ standard-library containers:

  - The [List ADT]{.hl} and its [array]{.hl} and [linked]{.hl} implementations.

  - [Stacks]{.hl}, [queues]{.hl}, and [deques]{.hl} — restricted lists — with `stack`, `queue`, and `deque`.

  - [Trees]{.hl}, [heaps]{.hl}, and [priority queues]{.hl}, and the array view of a complete binary tree.

  - [Graphs]{.hl} with their traversal (DFS, BFS) and spanning-tree / shortest-path algorithms.

---
layout: prism
heading: The List ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [list]{.hl} is an ordered sequence $a_0, a_1, \ldots, a_{N-1}$ of elements.

- Like every [abstract data type]{.hl} (ADT), it is defined by the *operations* it supports, not by how it is stored.

- Any concrete implementation (array, linked list, ...) must provide these operations.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">List ADT operations</div>
<div class="theorem-box-body">

- `printList` — print the list
- `makeEmpty` — empty the list
- `insert` — insert `x` at position `i`
- `remove` — remove the `i`-th element (or `x`)
- `find` — index of an element `x`
- `findKth` — element at a given index
- `size` — number of elements
- ... or anything else you need (e.g. `sort`).

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

- Storing the list in a *contiguous* array makes `findKth` an $O(1)$ operation.

- The cost is that `insert` and `remove` are $O(N)$: elements must be [shifted]{.hl} to keep the array contiguous.

<div style="margin-top: 1rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 1.05rem; line-height: 2.1;">
  <div><span style="color:#9aa0a6;">start&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span> [ 10 &nbsp; 3 &nbsp; 21 &nbsp; 83 &nbsp; 34 ]</div>
  <div><span style="color:#4a6fa5;">insert(1, 77)</span> [ 10 &nbsp; <span style="color:#c2410c; font-weight:bold;">77</span> &nbsp; 3 &nbsp; 21 &nbsp; 83 &nbsp; 34 ]</div>
  <div><span style="color:#4a6fa5;">remove(0)&nbsp;&nbsp;&nbsp;&nbsp;</span> [ 77 &nbsp; 3 &nbsp; 21 &nbsp; 83 &nbsp; 34 ]</div>
</div>

---
layout: prism
heading: "DIY: An Array-Backed List"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct List {                      // a tiny array-backed List ADT
    vector<int> a;
    void insert(int i, int x) { a.insert(a.begin() + i, x); } // O(N): shift right
    void remove(int i)        { a.erase(a.begin() + i); }     // O(N): shift left
    int  findKth(int i) const { return a[i]; }                // O(1)
    int  find(int x) const {                                  // index of x, or -1
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
heading: "C++ Array and vector Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A built-in [array]{.hl} has a fixed size fixed at compile time; multi-dimensional arrays are also supported.

- The [`vector`]{.hl} class (in `<vector>`) is a *resizable* array: `push_back`, `pop_back`, `size`, and indexing with `[]`.

- `vector` is the standard replacement for the troublesome built-in array.

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
heading: Simply Linked Lists
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- To avoid the linear cost of `insert` and `remove`, the list should *not* be stored contiguously.

- A [linked list]{.hl} is a series of [nodes]{.hl}, not necessarily adjacent in memory. Each node holds an element and a [link]{.hl} (pointer) to its successor; the last node's link is `nullptr`.

<div style="margin-top: 0.8rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 1.05rem;">
  <span style="color:#9aa0a6;">head&nbsp;→</span>
  [ 10 |·]→ [ 3 |·]→ [ 21 |·]→ [ 83 |·]→ [ 34 |<span style="color:#c2410c;">/</span>]
</div>

---
layout: prism
heading: "DIY: Building a Singly Linked List"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int data; Node* next; };

int main() {
    Node* head = nullptr;
    int vals[] = {34, 83, 21, 3, 10};     // insert at front -> reverses
    for (int x : vals) head = new Node{x, head};

    for (Node* p = head; p != nullptr; p = p->next) // traverse
        cout << p->data << (p->next ? " -> " : "\n");

    // free the nodes
    while (head) { Node* t = head; head = head->next; delete t; }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Pointers
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A [pointer]{.hl} is a variable that stores the *address* of another variable: `datatype *pointerName`.

- The [`&`]{.hl} operator gives the address of a variable; the [`*`]{.hl} operator dereferences a pointer to the variable it points to.

- Writing through the pointer (`*a = 1`) changes the pointed-to variable `b`.

</div>
<div>

```cpp
int *a;
int  b = 3;

a = &b;                 // a holds the address of b
cout << b << endl;      // 3

*a = 1;                 // write through the pointer
cout << b << endl;      // 1  (b changed!)
```

</div>
</div>

---
layout: prism
heading: "DIY: Pointers in Action"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int b = 3;
    int* a = &b;                    // a points to b
    cout << "b       = " << b  << "\n";   // 3
    cout << "*a      = " << *a << "\n";   // 3
    *a = 1;                          // write through the pointer
    cout << "after *a = 1, b = " << b << endl; // 1
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
  margin-top: 1.4em;
}
</style>

- In a [circular linked list]{.hl}, the last node's link points *back to the head* instead of `nullptr`.

- Traversal can start anywhere and loop forever — useful for round-robin scheduling and problems such as Josephus.

<div style="margin-top: 0.8rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 1.05rem;">
  <span style="color:#9aa0a6;">head&nbsp;→</span>
  [ 10 |·]→ [ 3 |·]→ [ 21 |·]→ [ 83 |·]→ [ 34 |·]<span style="color:#c2410c;">─┐</span><br/>
  <span style="color:#c2410c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──────────────────────────────────────────┘</span>
</div>

---
layout: prism
heading: "DIY: Traversing a Circular List"
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
    tail->next = head;                       // close the circle

    Node* p = head;                          // walk around twice
    for (int step = 0; step < 10; step++) { cout << p->data << " "; p = p->next; }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Doubly Linked Lists
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Nodes in a singly or circular linked list are linked in one direction only: given an arbitrary node, we cannot go *back*.

- In a [doubly linked list]{.hl} each node links to both its predecessor and its successor, so it can be traversed in either direction. It can also be made circular.

<div style="margin-top: 0.8rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 1.05rem;">
  <span style="color:#9aa0a6;">head&nbsp;⇄</span>
  [ 10 ]⇄ [ 3 ]⇄ [ 21 ]⇄ [ 83 ]⇄ [ 34 ]
</div>

---
layout: prism
heading: "DIY: A Doubly Linked List (std::list)"
---

<CppRunner>

```cpp
#include <iostream>
#include <list>
using namespace std;

int main() {
    list<int> L = {10, 3, 21, 83, 34};   // std::list is doubly linked

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
heading: The Stack ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [stack]{.hl} is a list restricted so that insertions and deletions happen at only one end, the [top]{.hl}.

- Stacks are [LIFO]{.hl} (last in, first out) lists — only the top element is accessible.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">Stack ADT operations</div>
<div class="theorem-box-body">

- `push` — add an element on the top
- `top` — read the top element
- `pop` — remove the top element
- ... or others (e.g. `popAll`).

</div>
</div>

<div style="margin-top: 1rem; font-family: 'JetBrains Mono', Consolas, monospace; text-align:center;">
  top → [ 10 ]<br/>[ 77 ]<br/>[ &nbsp;3 ]<br/>[ 21 ]<br/>[ 83 ]<br/>[ 34 ]
</div>

</div>
</div>

---
layout: prism
heading: "C++ stack Class"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The [`stack`]{.hl} class (in `<stack>`) provides `push`, `top`, `pop`, `size`, and `empty`.

- Classic applications: [parentheses checking]{.hl}, [postfix expression evaluation]{.hl}, and the [depth-first search]{.hl} algorithm.

```cpp
stack<int> s;              // needs #include <stack>
s.push(3); s.push(2); s.push(1);
cout << s.top() << " " << s.size() << endl;  // 1 3
s.pop();
cout << s.top() << " " << s.empty() << endl; // 2 0 (false)
```

---
layout: prism
heading: "DIY: Stack — Parentheses Checker"
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
heading: The Queue ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [queue]{.hl} is a list where insertions happen at the [rear]{.hl} and deletions at the [front]{.hl}.

- Queues are [FIFO]{.hl} (first in, first out) lists — insert at the rear, remove from the front.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">Queue ADT operations</div>
<div class="theorem-box-body">

- `push` — add an element at the rear
- `front` — read the front element
- `pop` — remove the front element
- ... or others (e.g. `popAll`).

</div>
</div>

<div style="margin-top: 1rem; font-family: 'JetBrains Mono', Consolas, monospace; text-align:center;">
  front → [ 34 | 83 | 21 | 3 | 77 | 10 ] ← rear
</div>

</div>
</div>

---
layout: prism
heading: "C++ queue Class"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The [`queue`]{.hl} class (in `<queue>`) provides `push`, `front`, `pop`, `size`, and `empty`.

- A classic application is the [Josephus problem]{.hl}, easily simulated by rotating a queue.

```cpp
queue<int> q;              // needs #include <queue>
q.push(3); q.push(2); q.push(1);
cout << q.front() << " " << q.size() << endl;  // 3 3
q.pop();
cout << q.front() << " " << q.empty() << endl; // 2 0 (false)
```

---
layout: prism
heading: "DIY: Queue — Josephus Problem"
---

<CppRunner>

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    int n = 7, k = 3;             // n people in a circle, remove every k-th
    queue<int> q;
    for (int i = 1; i <= n; i++) q.push(i);

    cout << "elimination order: ";
    while (!q.empty()) {
        for (int i = 1; i < k; i++) { q.push(q.front()); q.pop(); } // skip k-1
        cout << q.front() << " ";                                    // remove k-th
        q.pop();
    }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Double Ended Queue
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [double-ended queue]{.hl} (deque) extends the queue so that insertion and removal can happen at *both* the front and the rear.

- A deque can be implemented on top of a [circular queue]{.hl}.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w06/dsa-w06-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "C++ deque Class"
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
heading: Tree, Binary Tree, and Heap
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A [tree]{.hl} is a hierarchical structure of nodes; a [binary tree]{.hl} gives each node at most two children.

- A [full binary tree]{.hl} has every node with either $0$ or $2$ children; a [complete binary tree]{.hl} is filled level by level, left to right.

- A [heap]{.hl} is a complete binary tree with the [heap-order property]{.hl}: in a [max heap]{.hl}, every parent is $\geq$ its children (so the maximum sits at the root).

---
layout: prism
heading: Complete Binary Tree Implementation
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [list]{.hl} (array) neatly represents a complete binary tree — no pointers needed.

- Using a [1-based index]{.hl} (we skip `A[0]`), for the element at index `i`:

<div class="sub-item-enum">

1. left child is at `2i` &nbsp;(`2i+1` for 0-based)
2. right child is at `2i+1` &nbsp;(`2i+2` for 0-based)
3. parent is at `i/2` &nbsp;(`(i-1)/2` for 0-based)

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
heading: "DIY: Array View of a Complete Binary Tree"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    // 1-based: A[0] is unused; level-order values of the tree
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
heading: The Priority Queue ADT
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [priority queue]{.hl} always makes the element of highest priority (here, the [maximum]{.hl}) available first.

- It is implemented with a [binary heap]{.hl}, giving $O(\log N)$ insert and delete-max.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">Priority Queue ADT operations</div>
<div class="theorem-box-body">

- `insert` — insert an element
- `deleteMax` — remove the maximum
- `max` — read the maximum
- `isEmpty` — test if empty
- `clear` — empty the queue

</div>
</div>

</div>
</div>

---
layout: prism
heading: "DIY: A Binary Max-Heap"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> h = {0};                 // 1-based heap; h[0] unused

void insert(int x) {                 // percolate up
    h.push_back(x);
    int i = h.size() - 1;
    while (i > 1 && h[i/2] < h[i]) { swap(h[i/2], h[i]); i /= 2; }
}
int deleteMax() {                    // percolate down
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
heading: "C++ priority_queue Class"
---

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    priority_queue<int> pq1;                 // max-heap (default)
    pq1.push(1); pq1.push(9); pq1.push(3);
    cout << pq1.top() << "\n";               // 9

    priority_queue<pair<int,int>> pq2;       // orders by .first then .second
    pq2.push({1,2}); pq2.push({1,3}); pq2.push({3,2});
    cout << pq2.top().first << " " << pq2.top().second << "\n"; // 3 2

    priority_queue<int, vector<int>, greater<int>> pq3; // min-heap
    pq3.push(1); pq3.push(9); pq3.push(3);
    cout << pq3.top() << endl;               // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Graph
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [graph]{.hl} represents data as [vertices]{.hl} (nodes) connected by [edges]{.hl}.

- Graphs model pathways between cities, hyperlinks between websites, relationships between people, connections between brain cells, and much more.

- There are [directed]{.hl}, [undirected]{.hl}, and [weighted]{.hl} graphs.

<div style="margin-top: 0.6rem; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 1.05rem;">
  G = { A, B, C, (A, B), (A, C), (B, C) }
</div>

---
layout: prism
heading: Graph Implementation
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A graph can be stored as an [adjacency matrix]{.hl}: entry $(i, j)$ is $1$ if node $i$ is connected to node $j$, and $0$ otherwise.

- For an undirected graph the matrix is [symmetric]{.hl}.

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
heading: "DIY: Building an Adjacency Matrix"
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
    for (auto& e : edges) { A[e[0]][e[1]] = 1; A[e[1]][e[0]] = 1; } // undirected

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
heading: Minimum Spanning Tree
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- For an undirected graph of $n$ nodes, the minimum number of edges that can interconnect all nodes is $n - 1$; such a connected, acyclic subgraph is a [spanning tree]{.hl}.

- A [minimum spanning tree]{.hl} (MST) is a spanning tree with the smallest sum of edge weights.

  - It can be used to build an optimal electrical circuit, set up an optimal network, lay an optimal cable, and so on.

- Two classic greedy algorithms compute an MST: [Kruskal's]{.hl} (sort edges, join with union-find) and [Prim's]{.hl} (grow a tree from one vertex).

---
layout: prism
heading: "DIY: Kruskal's Algorithm"
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
    // {u, v, w} on the 6-node weighted graph
    vector<array<int,3>> e = {{0,1,6},{0,2,1},{0,3,5},{0,5,4},
                              {1,2,2},{2,4,3},{3,5,7},{4,5,8}};
    sort(e.begin(), e.end(), [](auto&a, auto&b){ return a[2] < b[2]; });
    for (int i = 0; i < 6; i++) par[i] = i;

    int total = 0;
    cout << "MST edges: ";
    for (auto& ed : e) {
        if (findSet(ed[0]) != findSet(ed[1])) {          // no cycle
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
heading: "DIY: Prim's Algorithm"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int n = 6;
    vector<vector<pair<int,int>>> adj(n);                // (neighbor, weight)
    int E[][3] = {{0,1,6},{0,2,1},{0,3,5},{0,5,4},{1,2,2},{2,4,3},{3,5,7},{4,5,8}};
    for (auto& e : E) { adj[e[0]].push_back({e[1],e[2]}); adj[e[1]].push_back({e[0],e[2]}); }

    vector<int> done(n, 0);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq; // (weight, node)
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
heading: "DIY: Dijkstra's Algorithm"
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
heading: "DIY: Floyd-Warshall Algorithm"
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

    for (int k = 0; k < n; k++)                          // all-pairs shortest paths
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
heading: Depth-First Search
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [Depth-first search]{.hl} (DFS) explores as far as possible along each branch before backtracking.

- DFS uses a [stack]{.hl} (or recursion) and runs in $O(N)$ over the graph.

</div>
<div>

```text
DFS(graph, v, visited):
    visited[v] = True          // mark v
    for i in graph[v]:         // visit recursively
        if not visited[i]:
            DFS(graph, i, visited)
```

</div>
</div>

---
layout: prism
heading: "DIY: Recursive DFS"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> g(9);   // 1..8; adjacency in visit order
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
heading: Recursive Programming
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Some computations are awkward to express with loops but natural to express in terms of *themselves* — this is [recursion]{.hl}.

- To avoid an infinite loop, a recursion needs two ingredients:

<div class="sub-item-enum">

1. [Base case]{.hl} — at least one case solved *without* recursion, which stops the recursion.
2. [Recursive case]{.hl} — the general case that makes progress toward a base case.

</div>

---
layout: prism
heading: Recursion Examples
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w06/dsa-w06-image10.png" class="tikz-fig" style="width: 100%;" />

<div style="text-align:center; font-size: 0.8rem; color:#9aa0a6;">factorial: unwinding the calls</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w06/dsa-w06-image11.png" class="tikz-fig" style="width: 100%;" />

<div style="text-align:center; font-size: 0.8rem; color:#9aa0a6;">fibonacci: the call tree</div>

</div>
</div>

---
layout: prism
heading: "DIY: factorial and fibonacci"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int factorial(int n) {
    if (n == 0) return 1;                 // base case
    return n * factorial(n - 1);          // recursive case
}
int fib(int n) {
    if (n == 0) return 0;                 // base cases
    if (n == 1) return 1;
    return fib(n - 1) + fib(n - 2);       // recursive case
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
heading: Breadth-First Search
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [Breadth-first search]{.hl} (BFS) explores all neighbors at the current depth before moving deeper.

- BFS uses a [queue]{.hl} and runs in $O(N)$; it is normally slightly faster than DFS in practice.

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
heading: "DIY: Queue-Based BFS"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    vector<vector<int>> g(9);   // 1..8; adjacency in visit order
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

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
