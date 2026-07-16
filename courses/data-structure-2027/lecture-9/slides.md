---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 9
download: true
info: |
  ## Data Structure Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-9-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 09: Heaps</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">Circular Queues and Priority Queues</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">Trees and Tries</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">Midterm Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">Midterm Exam</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span class="text-gray-900 dark:text-gray-100">Heaps</span></p>
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
heading: Heaps
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The [heap]{.hl} data structure has its own properties — the *structure property* and the *heap-order property* — and thus can be used for many applications.

- Heaps are used for the implementation of the [priority queue]{.hl} data structure.

- There is an efficient *sorting algorithm*, [heap sort]{.hl}.

- Heaps power various graph algorithms, such as *Dijkstra's algorithm* for finding the shortest path, or *Prim's algorithm* for estimating the minimum spanning tree.

- In this lecture, we will discuss various heap data structures:

<div class="sub-item-enum">

1. Implement `percolate up` and `percolate down` algorithms.
2. Introduce $d$-heaps.
3. Introduce leftist heaps and their operations.

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Heaps</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Heaps</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Percolate Up</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Percolate Down</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><em>d</em>-heaps</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Leftist Heaps</span></p>
  </div>

</div>

---
layout: prism
heading: "Recap: Heap Properties"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A heap is a binary tree that is *completely filled*, with the possible exception of the bottom level, which is filled from left to right.
  - This rule is known as the [structure property]{.hl}.

- For every node $X$, the key in the parent of $X$ is smaller than (or equal to) the key in $X$, except at the root (which has no parent).
  - This rule is known as the [heap-order property]{.hl}.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-01.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Recap: insert — Percolate Up"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- To insert an element $X$, we create a hole in the next available location — otherwise the tree would not be complete.
  - If $X$ fits in the hole without violating heap order, we place it there and are done.
  - Otherwise, we slide the element in the hole's parent into the hole, bubbling the hole up toward the root, and repeat until $X$ can be placed.

- This strategy is known as [percolate up]{.hl}: the new element is percolated up the heap until its correct location is found.

- Rather than repeated swaps (each swap may need several assignments), we move only the hole, saving work.

- The insertion time can be as much as $\mathcal{O}(\log N)$, when the inserted element is the new minimum and percolates all the way to the root.

---
layout: prism
heading: "Recap: insert — Example"
---

<div class="flex justify-center" style="margin-top: 0rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-02.svg" class="tikz-fig" style="width: 58%;" />
</div>

---
layout: prism
heading: "Recap: removeMin — Percolate Down"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The `removeMin` operation is handled much like insertion.

- When the minimum is removed, a hole is created at the root.

- Since the heap becomes one smaller, the last element $X$ in the heap must move somewhere:
  - If $X$ can be placed in the hole, we are done.
  - This is unlikely, so we slide the smaller of the hole's children into the hole, pushing the hole down one level, and repeat until $X$ can be placed.

- This strategy is known as [percolate down]{.hl}.

- The worst-case running time of this operation is $\mathcal{O}(\log N)$.

---
layout: prism
heading: "Recap: removeMin — Example"
---

<div class="flex justify-center" style="margin-top: 0rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-03.svg" class="tikz-fig" style="width: 82%;" />
</div>

---
layout: prism
heading: "DIY: Percolate Up and Down"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Binary heap stored in a[1..n]; parent(i)=i/2, children=2i, 2i+1
vector<int> a{0};   // a[0] unused as a sentinel slot

void percolateUp(int hole) {
    int x = a[hole];
    while (hole > 1 && x < a[hole / 2]) { // bubble the hole toward root
        a[hole] = a[hole / 2];
        hole /= 2;
    }
    a[hole] = x;
}
void insert(int x) { a.push_back(x); percolateUp(a.size() - 1); }

void percolateDown(int hole) {
    int n = a.size() - 1, x = a[hole], child;
    while (2 * hole <= n) {
        child = 2 * hole;
        if (child != n && a[child + 1] < a[child]) child++; // smaller child
        if (a[child] < x) { a[hole] = a[child]; hole = child; }
        else break;
    }
    a[hole] = x;
}
int removeMin() {
    int mn = a[1];
    a[1] = a.back(); a.pop_back();
    if (a.size() > 1) percolateDown(1);
    return mn;
}

int main() {
    for (int v : {13, 21, 16, 24, 31, 19, 68, 65, 26, 32})
        insert(v);
    cout << "insert 14 -> heap array: ";
    insert(14);
    for (size_t i = 1; i < a.size(); i++) cout << a[i] << " ";
    cout << "\nremoveMin order: ";
    while (a.size() > 1) cout << removeMin() << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "d-heaps"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Binary heaps are so simple that they are almost always used when priority queues are needed.

- A simple generalization is a [$d$-heap]{.hl}, exactly like a binary heap except that all nodes have $d$ children (so a binary heap is a $2$-heap).

- The figure shows an example of a $3$-heap.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-04.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "d-heaps — Analysis"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A $d$-heap is much shallower than a binary heap, improving the running time of `insert` to $\mathcal{O}(\log_d N)$.

- For large $d$, the `deleteMin` operation is more expensive: even though the tree is shallower, finding the minimum of $d$ children takes $d-1$ comparisons with a standard algorithm.
  - This raises the time of the operation to $\mathcal{O}(d \log_d N)$.
  - Since $d$ is a constant, both operations are $\mathcal{O}(\log N)$.

- For the implementation, we can still use an *array*.

- When the priority queue is too large to fit in main memory, a $d$-heap is worth considering.

- There is evidence that $4$-heaps may outperform binary heaps in practice.

---
layout: prism
heading: "DIY: d-heap Index Arithmetic"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

// For a d-heap stored in a[1..n]:
//   parent(i)      = (i + d - 2) / d
//   k-th child(i)  = d*(i - 1) + k + 1   (k = 1..d)
int parent(int i, int d) { return (i + d - 2) / d; }
int child(int i, int k, int d) { return d * (i - 1) + k + 1; }

int main() {
    // 3-heap:  10 / (20 30 35) / (40 50 60 70 80 90 100 110)
    vector<int> a{0, 10, 20, 30, 35, 40, 50, 60, 70, 80, 90, 100, 110};
    int d = 3, n = a.size() - 1;
    for (int i = 1; i <= 4; i++) {
        cout << "node a[" << i << "]=" << a[i] << " children:";
        for (int k = 1; k <= d; k++) {
            int c = child(i, k, d);
            if (c <= n) cout << " " << a[c];
        }
        cout << "  parent=a[" << parent(i, d) << "]=" << a[parent(i, d)] << "\n";
    }
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
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Heaps</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Leftist Heaps</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>merge</code> operation</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Leftist Heaps</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Leftist Heap Operations</span></p>
  </div>

</div>

---
layout: prism
heading: "The merge Operation"
---

- The most glaring weakness of the heap implementation is that combining two heaps into one is a hard operation.
  - This extra operation is known as a [`merge`]{.hl}.

- It seems difficult to design a data structure that efficiently supports merging while using only an array, as a binary heap does.

- The reason is that merging would seem to require copying one array into another, which takes $\Theta(N)$ time for equal-sized heaps.

- For this reason, all the advanced data structures that support efficient merging require a *linked* data structure.

- In practice, we can expect this to make all the other operations slower.

---
layout: prism
heading: "Leftist Heaps — Null Path Length"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Like a binary heap, a [leftist heap]{.hl} has both the structural property and the ordering property.

- A leftist heap is also a binary tree; the only difference is that leftist heaps are not perfectly balanced but actually attempt to be very *unbalanced*.

- We define the [null path length]{.hl} $npl(X)$ of any node $X$ as the length of the shortest path from $X$ to a node without two children.
  - Thus the $npl$ of a node with zero or one child is $0$.
  - $npl(\texttt{nullptr}) = -1$.

- The null path length of any node is $1$ more than the *minimum* of the null path lengths of its children.

---
layout: prism
heading: "Leftist Heaps — Leftist Property"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The [leftist heap property]{.hl}: for every node $X$, the null path length of the *left* child is at least as large as that of the *right* child.
  - Nodes in the figures show null path lengths; only the *left* one is a leftist heap.

- The property deliberately makes the tree unbalanced, biasing it to grow deep toward the left.
  - A long path of left nodes is possible (and preferable, to facilitate merging) — hence the name *leftist* heap.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-05.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Leftist Operations — merge (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The fundamental operation on leftist heaps is *merging*.
  - Insertion is merely a special case: an insertion is a merge of a one-node heap with a larger heap.

- If either heap is empty, we return the other heap.

- Otherwise, to merge the two heaps, we compare their roots.
  - Let us consider two heaps to be merged, $H_1$ and $H_2$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-06.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Leftist Operations — merge (2/2)"
---

- First, we recursively merge the heap with the *larger* root with the *right subheap* of the heap with the smaller root.
  - If that right subheap is empty, we attach the other heap as the right subheap.

- We update the $npl$ of the merged root and swap the left and right subtrees just below the root, if needed, to keep the leftist property of the merged result.

<div class="flex justify-center" style="margin-top: 0.6rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-07.svg" class="tikz-fig" style="width: 32%;" />
</div>

---
layout: prism
heading: "DIY: Merging Two Heaps"
---

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    // H1 and H2 as min-heaps (std::priority_queue with greater<>)
    priority_queue<int, vector<int>, greater<int>> H1, H2;
    for (int v : {3, 10, 21, 14, 23, 8, 17, 26}) H1.push(v);
    for (int v : {6, 12, 18, 24, 33, 7, 37, 18}) H2.push(v);

    // merge H2 into H1
    while (!H2.empty()) { H1.push(H2.top()); H2.pop(); }

    cout << "merged deleteMin order: ";
    while (!H1.empty()) { cout << H1.top() << " "; H1.pop(); }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY_W09: Skew Heaps and Binomial Queues"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- A [skew heap]{.hl} is a *self-adjusting* version of a leftist heap that is incredibly simple to implement.
  - Skew heaps are binary trees with heap order, but with no structural constraint — no null path length information is maintained.
  - The right path can be arbitrarily long, so the worst-case time of all operations is $\mathcal{O}(N)$.
  - Still, skew heaps have $\mathcal{O}(\log N)$ *amortized* cost per operation.

- [Binomial queues]{.hl} support all three operations in $\mathcal{O}(\log N)$ worst-case time, and insertions take *constant time on average*.
  - A binomial queue is not a heap-ordered tree but a *collection* of heap-ordered trees, known as a *forest*.

- Assignment: find and study skew heaps and binomial queues.

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
