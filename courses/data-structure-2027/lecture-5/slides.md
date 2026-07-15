---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 5
download: true
info: |
  ## Data Structure Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 05: Circular Queues and Priority Queues</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">Lists, Stacks, and Queues</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span class="text-gray-900 dark:text-gray-100">Circular Queues and Priority Queues</span></p>
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
heading: "Recap: List Model"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- We deal with a general list of the form $A_0, A_1, A_2, \ldots, A_{N-1}$, whose *size* is $N$.
  - The list of size $0$ is the [empty list]{.hl}.
  - Except for the empty list, $A_i$ *follows* (succeeds) $A_{i-1}$ $(i < N)$ and $A_{i-1}$ *precedes* $A_i$ $(i > 0)$.
  - The [position]{.hl} of element $A_i$ in the list is $i$; the first element is $A_0$ and the last is $A_{N-1}$.

- Associated with these definitions is a set of operations on the list ADT:
  - `printList` and `makeEmpty` do the obvious things.
  - `find` returns the position of the first occurrence of an item.
  - `insert` and `remove` insert and remove an element from some position.
  - `findKth` returns the element at some position.

- The interpretation of what is appropriate for a function — and the handling of special cases — is entirely up to the programmer (e.g. we could add `next` and `previous`).

---
layout: prism
heading: "Recap: Stack Model"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [stack]{.hl} is a list with the restriction that insertions and deletions may be performed in only one position — *the end of the list*, called the [top]{.hl}.
  - Last-In-First-Out (LIFO) property.

- The fundamental operations are `push` (an insert) and `pop` (deletes the most recently inserted element).

- The most recently inserted element can be examined before a `pop` via the `top` routine.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-01.svg" class="tikz-fig" style="width: 55%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "Recap: Queue Model"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [queue]{.hl} is also a list, but insertion is done at one end while deletion is performed at *the other end*, called the [front]{.hl}.
  - First-In-First-Out (FIFO) property.

- The fundamental operations are `push` (an insert) and `pop` (deletes the earliest inserted element).

- The earliest inserted element can be examined before a `pop` via the `front` routine.

<div style="margin-top: 2rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-02.svg" class="tikz-fig" style="width: 70%; margin: 0 auto;" />
</div>

---
layout: prism
heading: Circular Queues and Priority Queues
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- This lecture discusses two modified versions of the queue data structure.

- With these two modified queues, we can design efficient and effective algorithms for various problems.
  - The data structures we will see are among the most *elegant* in computer science.

- In this lecture, we discuss these two data structures and implement them:

<div class="sub-item-enum">

1. Introduce the [circular queue]{.hl} abstract data type and its implementation.
2. Introduce the basic [heap]{.hl} abstract data type.
3. Introduce the [priority queue]{.hl} abstract data type and its implementation.

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">The Circular Queue ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Circular Queue Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Implementation of Circular Queues</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Double-Ended Queues</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>deque</code> in the STL</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Priority Queue ADT</span></p>
  </div>

</div>

---
layout: prism
heading: "Circular Queue Model (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- An array-based queue implementation has a weakness: if we `pop` an element, there remains unused space.

- A [circular queue]{.hl}, also known as a *ring buffer*, uses a single, fixed-size buffer as if it were connected end-to-end.

- It represents a circular arrangement where operations follow the *FIFO* principle, but with an efficient way to utilize the storage space.

- The size of the queue is fixed and determined at the start of its implementation.

</div>
<div>

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-03.svg" class="tikz-fig" style="width: 90%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "Circular Queue Model (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The start and end of the queue wrap around to form a circle.

- Circular queues typically use two pointers, `front` and `rear`, to track the first and the last elements.
  - The `front` pointer indicates the *start* of the queue.
  - The `rear` pointer signifies the *end* of the queue.

- Like linear queues, this structure has [`enqueue`]{.hl} and [`dequeue`]{.hl} operations, equivalent to `push` and `pop`, respectively.

- `front` retrieves the front element without removing it from the queue.

---
layout: prism
heading: Implementation of Circular Queues
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The implementation uses a fixed-size array serving as the queue, along with two pointers, `front` and `rear`.
  - These two pointers are initialized to a special value such as `-1`.

- The array *wraps around* to the beginning when the end is reached — hence the term *circular*.

- Based on the pointer values, we can check whether the queue is empty or full, easily handling both [overflow]{.hl} and [underflow]{.hl}.

- Circular queues eliminate the wasted-space problem of linear queues by reusing the space from which elements are dequeued.

- It provides [$\mathcal{O}(1)$]{.hl} time complexity for insertion and removal operations.

---
layout: prism
heading: "Circular Queue — Implementation"
---

```cpp
class CircularQueue {
public:
    explicit CircularQueue(int capacity)
        : arr(capacity), cap(capacity), front(-1), rear(-1) {}

    bool isEmpty() const { return front == -1; }
    bool isFull()  const { return (rear + 1) % cap == front; }

    void enqueue(int x) {              // push at the rear
        if (isFull()) return;          // overflow
        if (isEmpty()) front = 0;
        rear = (rear + 1) % cap;       // wrap around
        arr[rear] = x;
    }
private:
    vector<int> arr;
    int cap, front, rear;
    // ... dequeue() and getFront() on the next slide
};
```

---
layout: prism
heading: "Circular Queue — dequeue and front"
---

<div style="height: 1.5rem;"></div>

```cpp
int dequeue() {                    // pop from the front
    if (isEmpty()) return -1;      // underflow
    int x = arr[front];
    if (front == rear)             // was the last element
        front = rear = -1;         // reset to empty
    else
        front = (front + 1) % cap; // wrap around
    return x;
}

int getFront() const {             // peek without removing
    return isEmpty() ? -1 : arr[front];
}
```

---
layout: prism
heading: "DIY: Circular Queue"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class CircularQueue {
public:
    explicit CircularQueue(int capacity)
        : arr(capacity), cap(capacity), front(-1), rear(-1) {}
    bool isEmpty() const { return front == -1; }
    bool isFull()  const { return (rear + 1) % cap == front; }
    void enqueue(int x) {
        if (isFull()) { cout << "overflow\n"; return; }
        if (isEmpty()) front = 0;
        rear = (rear + 1) % cap;
        arr[rear] = x;
    }
    int dequeue() {
        if (isEmpty()) return -1;
        int x = arr[front];
        if (front == rear) front = rear = -1;
        else front = (front + 1) % cap;
        return x;
    }
private:
    vector<int> arr;
    int cap, front, rear;
};

int main() {
    CircularQueue q(4);              // capacity 4, holds up to 3
    for (int v : {10, 20, 30}) q.enqueue(v);
    cout << "dequeue -> " << q.dequeue() << "\n";   // 10 leaves
    q.enqueue(40);                   // reuse the freed slot (wrap)
    q.enqueue(50);                   // overflow (full)
    cout << "drain -> ";
    while (!q.isEmpty()) cout << q.dequeue() << " "; // 20 30 40
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Double-Ended Queue Model
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A [double-ended queue]{.hl}, commonly referred to as a [deque]{.hl} (pronounced *"deck"*), generalizes the queue by allowing insertions and removals at both the front and the rear ends.

- Unlike the simpler queue (insertions at the rear, removals at the front), a deque supports four main operations: `enqueueFront`, `enqueueRear`, `dequeueFront`, and `dequeueRear`.

- This versatility makes deques suitable for a variety of applications where queues would be too restrictive.

<div style="margin-top: 1.5rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-04.svg" class="tikz-fig" style="width: 70%; margin: 0 auto;" />
</div>

---
layout: prism
heading: "DIY: A Deque via a Circular Queue"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Starting from the circular-queue implementation, modify `enqueue` and `dequeue` appropriately.

- Add an `enqueueFront` and a `dequeueRear`.
  - You can simply check the head and the tail elements.

- Trace the test code and predict the printed value.

</div>
<div>

```cpp
int main() {
    Deque dq(10);
    dq.enqueueFront(3);
    dq.enqueueFront(4);
    dq.enqueueRear(11);
    dq.enqueueFront(6);
    dq.dequeueRear();
    dq.dequeueRear();
    cout << dq.front() << endl;
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: "deque in the STL"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- C++ contains a generic [`deque`]{.hl} class.

<div class="sub-item">

`#include <deque>`

</div>

<div class="sub-item">

`deque<elementType> dequeName;`

</div>

- It supports `push_front`, `push_back`, `pop_front`, `pop_back`, and indexing with `[]`.

</div>
<div>

```cpp
#include <iostream>
#include <deque>
using namespace std;
int main() {
    deque<int> dq;
    dq.push_front(3);
    dq.push_front(4);
    dq.push_back(11);
    dq.push_front(6);
    dq.pop_back();
    dq.pop_front();
    cout << dq[0] << endl;
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Circular Queue ADT</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">The Priority Queue ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Priority Queue Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Simple Implementations</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Binary Heap</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>queue</code> in the STL</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Applications of Priority Queues</span></p>
  </div>

</div>

---
layout: prism
heading: Priority Queue Model
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [priority queue]{.hl} allows at least two operations: [`insert`]{.hl}, which does the obvious thing, and [`removeMin`]{.hl}, which finds, returns, and removes the minimum element.
  - `insert` is the equivalent of `push` for a queue.
  - `removeMin` is the priority-queue equivalent of the queue's `pop`.

- As with most data structures, other operations can sometimes be added, but these are extensions and not part of the basic model.

- Priority queues have many applications: operating systems, sorting, greedy algorithms, and more.

<div style="margin-top: 1.2rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-05.svg" class="tikz-fig" style="width: 62%; margin: 0 auto;" />
</div>

---
layout: prism
heading: "Simple Implementations (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- There are several obvious ways to implement a priority queue.
  - A simple *linked list*: insert at the front in $\mathcal{O}(1)$, but traverse the list in $\mathcal{O}(N)$ to delete the minimum.
  - A *sorted list*: `insert` is expensive ($\mathcal{O}(N)$), but `removeMin` is cheap ($\mathcal{O}(1)$).

- Another way would be to use a [binary search tree]{.hl}.
  - This gives an $\mathcal{O}(\log N)$ average running time for both operations.
  - True even though insertions are random while removals are not.

</div>
<div>

<div style="height: 1.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-06.svg" class="tikz-fig" style="width: 92%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "Simple Implementations (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Recall that the only element we ever remove is the minimum.

- Repeatedly removing a node in the *left* subtree would seem to hurt the balance of the tree by making the right subtree heavy.
  - In the worst case, once `removeMin` has depleted the left subtree, the right subtree has at most twice as many elements as it should.

- Using a search tree could be overkill — it supports a host of operations that are not required.

- We can implement the priority queue with *no links* and both operations in [$\mathcal{O}(\log N)$]{.hl} worst-case time (insertions take constant time on average).

---
layout: prism
heading: Binary Heap
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- The implementation we will use is known as a [binary heap]{.hl}, which we refer to merely as a *heap*.

- Its use is so common for priority-queue implementations that, in this context, the word *heap* without a qualifier generally refers to this data structure.

- Like binary search trees, heaps have two properties: a [structure property]{.hl} and a [heap-order property]{.hl}.

- An operation on a heap can destroy one of the properties, so a heap operation must not terminate until all heap properties are back in order.

---
layout: prism
heading: "Structure Property (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A heap is a binary tree that is *completely filled*, with the possible exception of the bottom level, which is filled from left to right.
  - This rule is the [structure property]{.hl}.
  - Such a tree is a [complete binary tree]{.hl}.

- A complete binary tree of height $h$ has between $2^h$ and $2^{h+1}-1$ nodes.
  - This implies a height of [$\mathcal{O}(\log N)$]{.hl}.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-07.svg" class="tikz-fig" style="width: 100%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "Structure Property (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Because a complete binary tree is so regular, it can be represented in an [array]{.hl} — no links are necessary. (Note that the $0$-th element is left empty.)
  - For any element in array position $i$, the left child is in position $2i$ and the right child is in the next cell, $2i+1$; the parent is in $\lfloor i/2 \rfloor$.

- The operations to traverse the tree are extremely simple and likely to be very fast.
  - The only drawback is that an estimate of the maximum heap size is required in advance, but typically this is not a problem.

- A heap will consist of an array and an integer representing the current heap size.

<div style="margin-top: 1rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-08.svg" class="tikz-fig" style="width: 82%; margin: 0 auto;" />
</div>

---
layout: prism
heading: Heap-Order Property
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The property that allows operations to be performed quickly is the [heap-order property]{.hl}.

- Since we want to find the minimum quickly, the smallest element should be at the *root*.
  - If every subtree is also a heap, then any node is smaller than all of its descendants.

- Heap-order property: for every node $X$, the key in the parent of $X$ is smaller than (or equal to) the key in $X$, with the exception of the root.

</div>
<div>

<div style="height: 2.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-09.svg" class="tikz-fig" style="width: 100%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "Heap Operations — insert (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- To insert an element $X$, we create a *hole* in the next available location (otherwise the tree would not be complete).
  - If $X$ can be placed in the hole without violating heap order, we do so and are done.
  - Otherwise, we slide the element in the hole's parent into the hole, bubbling the hole up toward the root, and continue until $X$ can be placed.

- This general strategy is a [percolate up]{.hl}: the new element percolates up the heap until the correct location is found.

- We could implement percolation with repeated *swaps*, but a swap needs several assignments; sliding is cheaper.

- The insertion could take as much as [$\mathcal{O}(\log N)$]{.hl} time if the new element is the minimum and percolates all the way to the root.

---
layout: prism
heading: "Heap Operations — insert (2/2)"
---

<div style="margin-top: 0.5rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-10.svg" class="tikz-fig" style="width: 74%; margin: 0 auto;" />
</div>

<div class="sub-item" style="margin-top: 1rem;">

Inserting $14$: the hole percolates up from the last position until $14$ finds a spot where its parent ($13$) is smaller.

</div>

---
layout: prism
heading: "Heap Operations — removeMin (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The `removeMin` operation is handled much like insertion.

- When the minimum is removed, a hole is created at the *root*. Since the heap becomes one smaller, the last element $X$ must move somewhere in the heap.
  - If $X$ can be placed in the hole, we are done.
  - This is unlikely, so we slide the *smaller* of the hole's children into the hole, pushing the hole down one level, and repeat until $X$ fits.

- This general strategy is a [percolate down]{.hl}.

- The worst-case running time of this operation is [$\mathcal{O}(\log N)$]{.hl}.

---
layout: prism
heading: "Heap Operations — removeMin (2/2)"
---

<div style="margin-top: 0.5rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-11.svg" class="tikz-fig" style="width: 100%; margin: 0 auto;" />
</div>

<div class="sub-item" style="margin-top: 1rem;">

Removing $13$: the last element ($31$) fills the root hole, then percolates down past the smaller child at each level until heap order is restored.

</div>

---
layout: prism
heading: "Binary Heap — insert (percolate up)"
---

<div style="height: 0.5rem;"></div>

```cpp
class BinaryHeap {                       // min-heap, 1-indexed array
public:
    explicit BinaryHeap(int capacity = 100)
        : array(capacity + 1), currentSize(0) {}
    bool isEmpty() const { return currentSize == 0; }
    const int& findMin() const { return array[1]; }

    void insert(int x) {                 // O(log N)
        if (currentSize == (int)array.size() - 1)
            array.resize(array.size() * 2);
        int hole = ++currentSize;        // new hole at the end
        array[0] = x;                    // sentinel stops the loop
        for (; x < array[hole / 2]; hole /= 2)
            array[hole] = array[hole / 2];   // slide parent down
        array[hole] = x;                 // place x
    }
private:
    vector<int> array;
    int currentSize;
    void percolateDown(int hole);        // on the next slide
};
```

---
layout: prism
heading: "Binary Heap — deleteMin and buildHeap"
---

<div style="height: 0.3rem;"></div>

```cpp
void deleteMin() {                       // O(log N)
    if (isEmpty()) return;
    array[1] = array[currentSize--];     // move last to the root
    percolateDown(1);
}
void buildHeap() {                       // O(N): heapify in place
    for (int i = currentSize / 2; i > 0; i--)
        percolateDown(i);
}
void percolateDown(int hole) {
    int child, tmp = array[hole];
    for (; hole * 2 <= currentSize; hole = child) {
        child = hole * 2;                // left child
        if (child != currentSize && array[child + 1] < array[child])
            child++;                     // pick the smaller child
        if (array[child] < tmp) array[hole] = array[child];
        else break;
    }
    array[hole] = tmp;
}
```

---
layout: prism
heading: "DIY: Binary Heap (insert / deleteMin)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class BinaryHeap {                       // min-heap, 1-indexed
public:
    explicit BinaryHeap(int capacity = 100)
        : array(capacity + 1), currentSize(0) {}
    bool isEmpty() const { return currentSize == 0; }
    int findMin() const { return array[1]; }
    void insert(int x) {
        int hole = ++currentSize;
        array[0] = x;                    // sentinel
        for (; x < array[hole / 2]; hole /= 2)
            array[hole] = array[hole / 2];
        array[hole] = x;
    }
    void deleteMin() {
        array[1] = array[currentSize--];
        percolateDown(1);
    }
private:
    vector<int> array;
    int currentSize;
    void percolateDown(int hole) {
        int child, tmp = array[hole];
        for (; hole * 2 <= currentSize; hole = child) {
            child = hole * 2;
            if (child != currentSize && array[child + 1] < array[child]) child++;
            if (array[child] < tmp) array[hole] = array[child];
            else break;
        }
        array[hole] = tmp;
    }
};

int main() {
    BinaryHeap h;
    for (int v : {13, 21, 16, 24, 31, 19, 68, 65, 26, 32})
        h.insert(v);
    cout << "sorted by repeated deleteMin: ";
    while (!h.isEmpty()) {               // heap-sort order
        cout << h.findMin() << " ";
        h.deleteMin();
    }
    cout << endl;
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
  margin-top: 1.6em;
}
</style>

- C++ contains a generic [`priority_queue`]{.hl} class supporting the priority-queue data structure.

<div class="sub-item">

`#include <queue>`

</div>

<div class="sub-item">

`priority_queue<elementType> pqName;`

</div>

- By default it is a *max-heap*: `top` returns the largest element.

</div>
<div>

```cpp
#include <iostream>
#include <queue>
using namespace std;
int main() {
    priority_queue<int> pq;
    pq.push(4);
    pq.push(1);
    pq.push(10);
    while (!pq.empty()) {
        cout << pq.top() << endl;
        pq.pop();
    }
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: STL priority_queue"
---

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    // default: max-heap (largest on top)
    priority_queue<int> maxpq;
    for (int v : {4, 1, 10, 3, 7}) maxpq.push(v);
    cout << "max-heap order: ";
    while (!maxpq.empty()) { cout << maxpq.top() << " "; maxpq.pop(); }
    cout << "\n";

    // min-heap via greater<> comparator
    priority_queue<int, vector<int>, greater<int>> minpq;
    for (int v : {4, 1, 10, 3, 7}) minpq.push(v);
    cout << "min-heap order: ";
    while (!minpq.empty()) { cout << minpq.top() << " "; minpq.pop(); }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Applications — Operating Systems"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- In operating systems, priority queues are an effective method to manage processes and tasks based on their [priority]{.hl}.
  - The main purpose is to ensure that higher-priority tasks are executed before lower-priority ones, optimizing performance and responsiveness.

- One primary application is the [scheduling]{.hl} of processes.
  - In [priority scheduling]{.hl}, each process is assigned a priority level, and the scheduler selects processes from the priority queue based on these levels.

- This approach can be *preemptive* or *non-preemptive*:

<div class="sub-item-enum">

1. *Preemptive*: if a new process arrives with a higher priority than the running one, the current process is preempted (temporarily halted) and added back to the queue, and the new process runs first.
2. *Non-preemptive*: the running process completes even if a higher-priority process arrives; the new process runs next.

</div>

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
