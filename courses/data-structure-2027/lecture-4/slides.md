---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 4
download: true
info: |
  ## Data Structure Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-4-ko/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Data Structure</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 04: Lists, Stacks, and Queues</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">Wonjun Ko, Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">Spring 2027</p>
</div>

---
layout: prism
heading: Course Schedule
---

<div class="absolute left-10 right-10" style="top: 0rem; bottom: 0rem; display: grid; grid-template-columns: 1.2fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">Course Introduction</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">Basic Mathematics and C++ Details</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">Algorithm Analysis</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span class="text-gray-900 dark:text-gray-100">Lists, Stacks, and Queues</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">Circular Queues and Priority Queues</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">Trees and Tries</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">Midterm Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">Midterm Exam</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">Heaps</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">Graphs and Weighted Graphs</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">Sets and Maps</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Hash Tables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Algorithm Design Techniques</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: "Recap: Mathematical Background"
---

<div style="height: 1.5rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Def. A relative order among functions</div>
<div class="theorem-box-body">

$T(N)=\mathcal{O}(f(N))$ if $\exists$ positive _constants_ $c, n_0$ s.t. $T(N)\leq cf(N)$ when $N\geq n_0$.

$T(N)=\Omega(g(N))$ if $\exists$ positive _constants_ $c, n_0$ s.t. $T(N)\geq cg(N)$ when $N\geq n_0$.

$T(N)=\Theta(h(N))$ iff. $T(N)=\mathcal{O}(h(N))$ and $T(N)=\Omega(h(N))$.

$T(N)=o(p(N))$ if, $\forall$ positive constants $c$, $\exists\, n_0$ s.t. $T(N)<cp(N)$ when $N>n_0$.

</div>
</div>

---
layout: prism
heading: "Recap: General Rules"
---

<div style="height: 1.5rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">General Rules</div>
<div class="theorem-box-body">

**Rule 1.** The running time of a `for` loop is at most the running time of the statements inside the `for` loop (including tests) times the number of iterations.

**Rule 2.** The total running time of a statement inside a group of nested loops is the running time of the statement multiplied by the product of the sizes of all the loops.

**Rule 3.** Consecutive statements just add, which means that the maximum is the one that counts.

**Rule 4.** The running time of an `if`/`else` statement is never more than the running time of the test plus the larger of the running times of each conditional statement.

</div>
</div>

---
layout: prism
heading: Lists, Stacks, and Queues
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- This lecture discusses three of the most simple and basic data structures.

- Most significant programs will use at least one of these structures explicitly, and a [stack]{.hl} is always _implicitly_ used in a program, whether or not it is declared.

- In this lecture, we will discuss these three data structures and implement them:

<div class="sub-item-enum">

1. Introduce the concept of [abstract data types]{.hl}.
2. Show how to efficiently perform operations on [lists]{.hl}.
3. Introduce the [stack]{.hl} abstract data type and its implementation.
4. Introduce the [queue]{.hl} abstract data type and its implementation.

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Abstract Data Types</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Abstract Data Types</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The List ADT</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Stack ADT</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Queue ADT</span></p>
  </div>

</div>

---
layout: prism
heading: Abstract Data Types
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- An [abstract data type]{.hl} (ADT) is a set of objects together with a set of operations.

- ADTs are _mathematical abstractions_; nowhere in an ADT's definition is there any mention of _how_ the set of operations is implemented.

- Objects such as lists, sets, and graphs, along with their operations, can be viewed as ADTs, just as integers, reals, and booleans are data types.
  - Integers, reals, and booleans have operations associated with them, and so do ADTs.

- For the set ADT, we might have operations such as _add_, _remove_, _size_, and _contains_.
  - Alternatively, we might only want the two operations _union_ and _find_, which would define a different ADT on the set.

---
layout: prism
heading: "Abstract Data Types — Design Decisions"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- The C++ [class]{.hl} allows for the implementation of ADTs, with appropriate hiding of implementation details.
  - Any other part of the program that needs to perform an operation on the ADT can do so by calling the appropriate method.

- If implementation details need to be changed, it should be easy to do so by merely changing the routines that perform the ADT operations.
  - This change, in a perfect world, would be completely _transparent_ to the rest of the program.

- There is no rule telling us which operations must be supported for each ADT — this is a [design decision]{.hl}. Error handling and tie breaking are also up to the program designer.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Abstract Data Types</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">The List ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">List Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Simple Array Implementation of Lists</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Simple Linked Lists</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>vector</code> and <code>list</code> in the STL</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Stack ADT</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Queue ADT</span></p>
  </div>

</div>

---
layout: prism
heading: List Model
---

- We will deal with a general list of the form $A_0, A_1, A_2, \ldots, A_{N-1}$, and the [size]{.hl} of the list is $N$.
  - We call the special list of size $0$ an [empty list]{.hl}.
  - $A_i$ _follows_ (succeeds) $A_{i-1}$ $(i<N)$ and $A_{i-1}$ _precedes_ $A_i$ $(i>0)$; the first element is $A_0$ and the last is $A_{N-1}$.
  - The [position]{.hl} of element $A_i$ in the list is $i$.

- Associated with these definitions is a set of operations on the list ADT:
  - `printList` and `makeEmpty` do the obvious things.
  - `find` returns the position of the first occurrence of an item.
  - `insert` and `remove` insert and remove an element from some position.
  - `findKth` returns the element in some position.

- The interpretation of what is appropriate for a function — and the handling of special cases — is entirely up to the programmer (e.g., we could add `next` and `previous`).

---
layout: prism
heading: Simple Array Implementation of Lists
---

- All these list ADT instructions can be implemented by using an [array]{.hl}.
  - Although arrays are created with a fixed capacity, the `vector` class, which internally stores an array, allows the array to grow by _doubling_ its capacity when needed.

- An array implementation allows `printList` to run in linear time, and `findKth` takes _constant_ time — as good as can be expected.

- `insert` and `remove` are potentially expensive, depending on where they occur.
  - Inserting at position $0$ requires pushing the entire array down one spot; deleting the first element requires shifting all elements up one spot — worst case $\mathcal{O}(N)$.
  - On average, half of the list must be moved, so linear time is still required.
  - If all operations occur at the high end, no elements are shifted, so adding and deleting take $\mathcal{O}(1)$ time.

---
layout: prism
heading: "Array Implementation — Operations"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- `findKth` is a constant-time indexed access.

- `insert` at position $p$ must _shift the tail right_, and `remove` at position $p$ must _shift the tail left_.

- Both movements are $\mathcal{O}(N)$ in the worst case — the price of storing the list _contiguously_.

</div>
<div>

```cpp
// findKth(i): O(1) indexed access
int findKth(const vector<int>& a, int i) {
    return a[i];
}
// insert x at position p: O(N)
void insert(vector<int>& a, int p, int x) {
    a.push_back(a.back());        // grow by 1
    for (int j = a.size()-1; j > p; j--)
        a[j] = a[j - 1];          // push down
    a[p] = x;
}
// remove at position p: O(N)
void remove(vector<int>& a, int p) {
    for (int j = p; j+1 < (int)a.size(); j++)
        a[j] = a[j + 1];          // shift up
    a.pop_back();
}
```

</div>
</div>

---
layout: prism
heading: Simple Linked List
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- When insertions and deletions occur throughout the list — particularly at the front — the array is not a good option, so we turn to the [linked list]{.hl}.

- To avoid the linear cost of insertion and deletion, the list is _not_ stored contiguously.
  - A linked list is a series of [nodes]{.hl} that need not be adjacent in memory.
  - Each node contains the element and a link to a node containing its successor.
  - This is the `next` link; the last cell's `next` points to a null pointer (`nullptr`).

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-01.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Linked List — Traversal and remove"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- To execute `printList()` or `find(x)`, we start at the first node and traverse by following the `next` links — clearly _linear-time_, as in the array (though the constant is likely larger).

- `findKth` is no longer as efficient: `findKth(i)` takes $\mathcal{O}(i)$ time.
  - In practice this bound is pessimistic, because calls are frequently in sorted order — `findKth(2)`, `findKth(3)`, `findKth(4)`, `findKth(6)` can all be done in one scan.

- The `remove` method can be executed by a single `next` pointer change.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-02.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Linked List — insert"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- The `insert` method obtains a new node from the system via a `new` call and then performs _two_ `next` pointer maneuvers.

- If we know where the change is to be made, inserting or removing does not require moving many items — only a _constant_ number of link changes.

- Adding to the front or removing the first item is thus a constant-time operation, and adding at the end can be constant-time.
  - Removing the last item is trickier: we must find the next-to-last item, set its `next` link to `nullptr`, and update the last-node link.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-03.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Toward the Doubly Linked List"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- In the classic linked list, having a link to the last node provides _no_ information about the next-to-last node.

- Maintaining a third link to the next-to-last node doesn't work, because it too would need updating during a remove.

- Instead, we have every node maintain a link to its _previous_ node, which is known as a [doubly linked list]{.hl}.

</div>
<div>

<div style="height: 4rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-04.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Doubly Linked List — Sentinel Nodes"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>


- Because iterator classes store a pointer to the _current node_ and the end marker is a valid position, it makes sense to create an extra node at the end to represent the endmarker.

- We can also create an extra node at the front, logically representing the beginning marker.

- These are [sentinel nodes]{.hl}: the front and end nodes are respectively the [header node]{.hl} ($H$) and the [tail node]{.hl} ($T$).
  - They greatly simplify coding by removing many special cases — e.g., without a header node, removing the first node becomes a special case.

</div>
<div>

<div style="height: 3.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-05.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Doubly Linked List — The Node"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Each `Node` stores the data element together with two links — one to its _predecessor_ (`prev`) and one to its _successor_ (`next`).

- With both links available, splicing a node in or out of the list is a constant number of pointer assignments.

</div>
<div>

<div style="height: 2.5rem;"></div>

```cpp
struct Node {
    Object data;
    Node*  prev;
    Node*  next;
    Node(const Object& d,
         Node* p, Node* n)
        : data{d}, prev{p}, next{n} {}
};
```

</div>
</div>

---
layout: prism
heading: "Doubly Linked List — insert and erase"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- `insert` allocates a new node whose `prev`/`next` splice it in _before_ the current position — two link updates on the neighbors.

- `erase` bypasses the current node by relinking its neighbors to each other, then `delete`s it.

- Each operation is $\mathcal{O}(1)$ once the position is known.

</div>
<div>

```cpp
// insert x before itr
iterator insert(iterator itr, const Object& x) {
    Node* p = itr.current;
    theSize++;
    Node* n = new Node{x, p->prev, p};
    p->prev->next = n;
    p->prev = n;
    return iterator{n};
}
// remove the node at itr
iterator erase(iterator itr) {
    Node* p = itr.current;
    iterator retVal{p->next};
    p->prev->next = p->next;
    p->next->prev = p->prev;
    delete p;
    theSize--;
    return retVal;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: A Singly Linked List"
---

<div style="height: 0rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int d, Node* n = nullptr) : data{d}, next{n} {}
};
int main() {
    // Build A0 -> A1 -> A2 -> nullptr by inserting at the front
    Node* head = nullptr;
    for (int v : {2, 1, 0})          // push 2, then 1, then 0 to the front
        head = new Node{v, head};

    // insert 9 after the first node (two next-pointer maneuvers)
    Node* p = head;
    p->next = new Node{9, p->next};

    cout << "list: ";
    for (Node* cur = head; cur != nullptr; cur = cur->next)
        cout << cur->data << " -> ";
    cout << "nullptr" << endl;

    while (head) { Node* t = head; head = head->next; delete t; }  // free
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "vector and list in the STL"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The C++ language includes an implementation of common data structures, popularly known as the [standard template library]{.hl} (STL).
  - The list ADT is one of these; data structures in the STL are called [collections]{.hl} or [containers]{.hl}.

- The [`vector`]{.hl} provides a _growable array_ implementation of the list ADT.
  - Advantage: it is indexable in _constant_ time.
  - Disadvantage: insertion and removal are expensive, unless made at the _end_.

- The [`list`]{.hl} provides a _doubly linked list_ implementation of the list ADT.
  - Advantage: insertion and removal are cheap, provided the position is known.
  - Disadvantage: the `list` is not easily indexable.

---
layout: prism
heading: "STL Containers — Common Methods"
---

- Both `vector` and `list` are _class templates_ instantiated with the type of items they store.

- Three methods are available for _all_ STL containers:
  - `int size() const` returns the number of elements.
  - `void clear()` removes all elements.
  - `bool empty() const` returns `true` if the container has no elements.

- Both support adding/removing at the end and accessing the front in constant time:
  - `void push_back(const Object& x)` adds `x` to the end of the list.
  - `void pop_back()` removes the object at the end of the list.
  - `const Object& back() const` returns the object at the end.
  - `const Object& front() const` returns the object at the front.

---
layout: prism
heading: "vector-only and list-only Methods"
---

- The `vector` has its own methods that are not part of `list`. Two allow efficient _indexing_:
  - `Object& operator[](int idx)` returns the object at `idx`, with _no_ bounds-checking.
  - `Object& at(int idx)` returns the object at `idx`, _with_ bounds-checking.

- Two more let the programmer view and change internal capacity:
  - `int capacity() const` returns the internal capacity of the `vector`.
  - `void reserve(int newCapacity)` sets the new capacity.

- Because a doubly linked list allows efficient changes at the front — but a `vector` does not — these two methods are available only for `list`:
  - `void push_front(const Object& x)` adds `x` to the front of the `list`.
  - `void pop_front()` removes the object at the front of the `list`.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Abstract Data Types</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The List ADT</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">The Stack ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Stack Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Implementation of Stacks</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>stack</code> in the STL</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Applications of Stacks</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Queue ADT</span></p>
  </div>

</div>

---
layout: prism
heading: Stack Model
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- A [stack]{.hl} is a list with the restriction that insertions and deletions can be performed in only one position — _the end of the list_, called the [top]{.hl}.
  - [Last-In-First-Out]{.hl} (LIFO) property.

- The fundamental operations are [`push`]{.hl}, equivalent to an insert, and [`pop`]{.hl}, which deletes the most recently inserted element.

- The most recently inserted element can be examined before a `pop` by use of the `top` routine.

</div>
<div>

<div style="height: 0rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-06.svg" class="tikz-fig" style="width: 60%;" />

</div>
</div>

---
layout: prism
heading: Linked List Implementation of Stacks
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Since a stack is a list, any list implementation will do.
  - `list` and `vector` support stack operations, and 99% of the time they are the most reasonable choice.

- Occasionally a special-purpose implementation can be faster.
  - Stack operations are constant-time, this is unlikely to yield any discernible improvement except under very unique circumstances.

- The first implementation of a stack uses a _singly linked list_:
  - We `push` by inserting at the _front_ of the list.
  - We `pop` by deleting the element at the _front_ of the list.
  - A `top` operation merely examines the front element, returning its value (sometimes `pop` and `top` are combined into one).

---
layout: prism
heading: "Linked List Stack — Implementation"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- `push` prepends a new node, making it the new `topOfStack`.

- `pop` unlinks the front node and `delete`s it.

- `top` returns the front node's value. Every operation touches only the front — all $\mathcal{O}(1)$.

</div>
<div>

```cpp
class Stack {
public:
    bool isEmpty() const {
        return topOfStack == nullptr;
    }
    void push(int x) {              // insert at front
        topOfStack = new Node{x, topOfStack};
    }
    int top() const { return topOfStack->data; }
    void pop() {                    // delete front
        Node* oldTop = topOfStack;
        topOfStack = topOfStack->next;
        delete oldTop;
    }
private:
    struct Node {
        int data;  Node* next;
        Node(int d, Node* n = nullptr)
            : data{d}, next{n} {}
    };
    Node* topOfStack = nullptr;
};
```

</div>
</div>

---
layout: prism
heading: Array Implementation of Stacks
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- An alternative implementation avoids links.
  - It exploits the `back`, `push_back`, and `pop_back` operations of `vector`, so the implementation is _trivial_.
  - Associated with each stack are `theArray` and `topOfStack`, which is `-1` for an empty stack.
  - To `push` an element `x`, we increment `topOfStack` and set `theArray[topOfStack] = x`.
  - To `pop`, we set the return value to `theArray[topOfStack]` and decrement `topOfStack`.

- These operations run in not only constant time but very _fast_ constant time.
  - On some machines, `push`es and `pop`s of integers can be a single machine instruction, using a register with auto-increment/decrement addressing.

- That most modern machines have stack operations in their instruction set reinforces that the stack is probably the most fundamental data structure in computer science, after the array.

---
layout: prism
heading: "DIY: An Array Stack (HW_W04_01)"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class ArrayStack {
public:
    void push(int x) { theArray.push_back(x); topOfStack++; }
    void pop()       { theArray.pop_back();   topOfStack--; }
    int  top() const { return theArray[topOfStack]; }
    bool empty() const { return topOfStack == -1; }
private:
    vector<int> theArray;
    int topOfStack = -1;
};

int main() {
    ArrayStack stack;
    stack.push(10);
    stack.push(20);
    stack.push(30);
    cout << "Top element is " << stack.top() << endl;  // 30
    stack.pop();
    cout << "Top element is " << stack.top() << endl;  // 20
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "stack in the STL"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- C++ contains a generic [`stack`]{.hl} class.
  - `#include <stack>`
  - `stack<elementType> stackName;`

- `push`, `top`, and `pop` behave exactly like the LIFO model we described.

</div>
<div>

```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    s.push(10);
    s.push(20);
    s.push(30);
    cout << s.top() << endl;   // 30
    s.pop();
    cout << s.top() << endl;   // 20
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: "Applications of Stacks — Balancing Symbols"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Compilers check programs for syntax errors, but frequently a single missing symbol (such as a missing brace or comment starter) causes the compiler to spill out a hundred lines of diagnostics without identifying the real error.

- We just check the _balancing_ of parentheses, brackets, and braces, ignoring any other characters. The simple algorithm uses a [stack]{.hl}:

<div class="sub-item-enum">

1. Make an empty stack.
2. Read characters until end of file.
3. If the character is an _opening_ symbol, push it onto the stack.
4. If it is a _closing_ symbol and the stack is empty, report an error.
5. Otherwise, pop the stack.
6. If the popped symbol is not the corresponding opening symbol, report an error.
7. At end of file, if the stack is not empty, report an error.

</div>

---
layout: prism
heading: "Applications of Stacks — Postfix Expressions"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Assume that we have a calculation:

$$
4.99 * 1.06 + 5.99 + 6.99 * 1.06 =
$$

- Owing to the operation orders, we can rewrite the above as the following sequence:

$$
4.99\ \ 1.06\ *\ \ 5.99\ +\ \ 6.99\ \ 1.06\ *\ \ +
$$

- This notation is known as [postfix]{.hl}, or [reverse Polish notation]{.hl}, and can be evaluated using a stack. As an exercise, let us evaluate:

<div class="sub-item">

$6\ \ 5\ \ 2\ \ 3\ \ +\ \ 8\ \ *\ \ +\ \ 3\ \ +\ \ *$

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Abstract Data Types</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The List ADT</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Stack ADT</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">The Queue ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Queue Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Array Implementation of Queues</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>queue</code> in the STL</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Applications of Queues</span></p>
  </div>

</div>

---
layout: prism
heading: Queue Model
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [queue]{.hl} is also a list; however, insertion is done at one end whereas deletion is performed at _the other end_, called the [front]{.hl}.
  - [First-In-First-Out]{.hl} (FIFO) property.

- The fundamental operations are [`push`]{.hl}, equivalent to an insert, and [`pop`]{.hl}, which deletes the earliest inserted element. The earliest inserted element can be examined before a `pop` by use of the `front` routine.

<div style="margin-top: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-07.svg" class="tikz-fig" style="width: 75%; margin-left: auto; margin-right: auto;" />

---
layout: prism
heading: Array Implementation of Queues
---

<style>
.slidev-layout ul > li {
  margin-top: 2.6em;
}
</style>

- As with stacks, any list implementation is legal for queues.

- Like stacks, both the linked list and array implementations give fast $\mathcal{O}(1)$ running times for every operation.

- The linked list implementation is straightforward, but the array implementation is a little tricky.

---
layout: prism
heading: "DIY: An Array Queue (DIY_W04)"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class ArrayQueue {
public:
    void push(int x) { theArray.push_back(x); rearOfQueue++; }
    void pop()       { frontOfQueue++; }
    int  front() const { return theArray[frontOfQueue]; }
    bool empty() const { return frontOfQueue > rearOfQueue; }
private:
    vector<int> theArray;
    int frontOfQueue = 0;
    int rearOfQueue  = -1;
};

int main() {
    ArrayQueue queue;
    queue.push(10);
    queue.push(20);
    queue.push(30);
    cout << "Front element is " << queue.front() << endl;  // 10
    queue.pop();
    cout << "Front element is " << queue.front() << endl;  // 20
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "queue in the STL"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- C++ contains a generic [`queue`]{.hl} class.
  - `#include <queue>`
  - `queue<elementType> queueName;`

- `push` enqueues at the rear; `front` and `pop` inspect and remove from the front — the FIFO model.

</div>
<div>

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    q.push(10);
    q.push(20);
    q.push(30);
    cout << q.front() << endl;   // 10
    q.pop();
    cout << q.front() << endl;   // 20
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: Applications of Queues
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- There are many algorithms that use queues to give efficient running times; several of these are found in [graph theory]{.hl}. Here are some simple examples of queue usage.

- When jobs are submitted to a printer, they are arranged in order of arrival — essentially, jobs sent to a printer are placed on a queue.

- In many networks of personal computers, the disk is attached to one machine, known as the [file server]{.hl}; users on other machines are given access to files on a _first-come first-served_ basis.

- Virtually every real-life line is (supposed to be) a queue — lines at ticket counters are queues, because service is first-come first-served.

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
