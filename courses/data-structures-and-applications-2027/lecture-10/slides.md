---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 10
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-10-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 10: Counting, Radix, Bucket Sort, and Binary Search Trees</p>

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
  margin-top: 1.8em;
}
</style>

- This lecture first *recaps* three [linear-time]{.hl} sorting algorithms that avoid comparisons, then introduces our first search-tree structure:

  - Recap of [counting sort]{.hl}, [radix sort]{.hl}, and [bucket sort]{.hl}.

  - [Records, indexes, and keys]{.hl} — how data is organized for searching.

  - The [binary search tree]{.hl} (BST): searching, insertion, deletion, and traversal.

  - Two practice problems solved with [parametric search]{.hl} (binary search on the answer).

---
layout: prism
heading: "Recap: Counting Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [Counting sort]{.hl} sorts $n$ integers drawn from the range $0 \ldots k$ without any comparisons, in $O(n + k)$ time.

- It uses a list $C[0 \ldots k]$ that records, for each integer $i$, how many times $i$ appears in the input $A$.

<div class="theorem-box">
<div class="theorem-box-title">The three phases</div>
<div class="theorem-box-body">

1. *Count.* $C[i]$ = number of occurrences of value $i$ in $A$.
2. *Prefix sum.* Rewrite $C$ so that $C[i]$ holds the number of elements *less than or equal to* $i$.
3. *Place.* Using $C$, compute the exact output position in $B$ for each element of $A$ (scanning right to left keeps the sort [stable]{.hl}).

</div>
</div>

---
layout: prism
heading: "Recap: Counting Sort — Implementation"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> countingSort(const vector<int>& A, int k) {
    int n = A.size();
    vector<int> C(k + 1, 0), B(n);
    for (int j = 0; j < n; j++) C[A[j]]++;          // phase 1: count
    for (int i = 1; i <= k; i++) C[i] += C[i - 1];   // phase 2: prefix sum
    for (int j = n - 1; j >= 0; j--)                 // phase 3: place (stable)
        B[--C[A[j]]] = A[j];
    return B;
}

int main() {
    vector<int> A = {2, 5, 3, 0, 2, 3, 0, 3};
    vector<int> B = countingSort(A, 5);
    cout << "input : "; for (int x : A) cout << x << ' ';
    cout << "\nsorted: "; for (int x : B) cout << x << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Radix Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [Radix sort]{.hl} sorts multi-digit keys one digit at a time, from the [least significant digit]{.hl} to the most significant, using a *stable* sort (counting sort) at each pass.

- A [stable sort]{.hl} preserves the original relative order of elements that compare equal — this is what makes the digit-by-digit approach correct.

<div class="tikz-fig" style="margin-top: 0.5rem;">

| initial | by 1st digit | by 2nd digit | by 3rd digit | by 4th digit |
|:---:|:---:|:---:|:---:|:---:|
| 0123 | 1560 | 0004 | 0004 | **0004** |
| 2154 | 2150 | 0222 | 1061 | **0123** |
| 0222 | 1061 | 0123 | 0123 | **0222** |
| 0004 | 0222 | 2150 | 2150 | **0283** |
| 0283 | 0123 | 2154 | 2154 | **1061** |
| 1560 | 0283 | 1560 | 0222 | **1560** |
| 1061 | 2154 | 1061 | 0283 | **2150** |
| 2150 | 0004 | 0283 | 1560 | **2154** |

</div>

---
layout: prism
heading: "Recap: Radix Sort — Implementation"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void countingByDigit(vector<int>& A, int exp) {  // stable sort on one digit
    int n = A.size();
    vector<int> out(n), C(10, 0);
    for (int x : A) C[(x / exp) % 10]++;
    for (int d = 1; d < 10; d++) C[d] += C[d - 1];
    for (int j = n - 1; j >= 0; j--) {
        int d = (A[j] / exp) % 10;
        out[--C[d]] = A[j];
    }
    A = out;
}

int main() {
    vector<int> A = {123, 2154, 222, 4, 283, 1560, 1061, 2150};
    for (int exp = 1; exp <= 1000; exp *= 10) {   // 4 passes for 4-digit keys
        countingByDigit(A, exp);
        cout << "digit " << exp << ": ";
        for (int x : A) cout << x << ' ';
        cout << '\n';
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Bucket Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [Bucket sort]{.hl} assumes the input is drawn from a [uniform distribution]{.hl} — every point in the range is equally *likely* to contain data (not that the data is perfectly even).

- For $A[0 \ldots n-1]$ of reals in $[0, 1)$: scatter each $A[i]$ into bucket $B[\lfloor n \cdot A[i] \rfloor]$, sort each bucket (insertion sort), then concatenate the buckets in order.

- The average running time is $O(n)$, but the [constant factor is large]{.hl}: creating and maintaining the bucket lists has significant overhead, and dynamically allocating them consumes extra space.

---
layout: prism
heading: "Recap: Bucket Sort — Implementation"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void bucketSort(vector<double>& A) {
    int n = A.size();
    vector<vector<double>> B(n);
    for (double x : A) B[(int)(n * x)].push_back(x);   // scatter
    int idx = 0;
    for (auto& bucket : B) {
        sort(bucket.begin(), bucket.end());            // insertion-sort each bucket
        for (double x : bucket) A[idx++] = x;          // gather
    }
}

int main() {
    vector<double> A = {0.78, 0.17, 0.39, 0.26, 0.72,
                        0.94, 0.21, 0.12, 0.23, 0.68};
    bucketSort(A);
    cout << "sorted:";
    for (double x : A) cout << ' ' << x;
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "HW_W09: Faster Bucket Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A naive bucket sort builds a linked list inside each bucket and often runs into [space pressure]{.hl}. There is an idea to implement it *without* physically maintaining separate buckets or lists — and it can end up [faster than quicksort]{.hl}.

- Where counting sort counts individual values, bucket sort effectively counts values *within a range*. From those counts we can compute, for each bucket, the exact range of $A[\,]$ its elements should occupy — so we can write directly back into $A[0 \ldots n-1]$ instead of using separate buckets.

- **Task.** Implement this improved, in-place bucket sort based on the idea above. Save it as `HW_W09_20XXXXXX.cpp` (`.py`, etc.) and upload it to the LMS.

---
layout: prism
heading: "Records, Indexes, and Keys (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- A [record]{.hl} holds the information about some entity. A person record might contain a student ID, name, address, phone number, and so on. Each such piece of information is a [field]{.hl}.

- An [index]{.hl} is used to look up the record for an entity.
  - We *could* store every record in the index, but then the index would just be the database itself.
  - Instead, an index is built from a field that *represents* the record — for a person record, the student ID makes a good representative field.

- A field that distinguishes each record without duplicating another is called a [key]{.hl}. A key may consist of one field or several.

---
layout: prism
heading: "Records, Indexes, and Keys (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

- The simplest index just [sorts the keys in an array]{.hl}.
  - Then search costs $O(\log N)$ on average, but insertion and deletion cost $O(N)$ on average.

- A variety of [search-tree]{.hl} structures improve on this trade-off:

</div>
<div>

<div class="tikz-fig">
<svg viewBox="0 0 460 300" style="width: 100%;">
  <line x1="120" y1="150" x2="250" y2="70"  stroke="#888" stroke-width="1.5"/>
  <line x1="120" y1="150" x2="250" y2="230" stroke="#888" stroke-width="1.5"/>
  <line x1="330" y1="70"  x2="410" y2="30"  stroke="#888" stroke-width="1.5"/>
  <line x1="330" y1="70"  x2="410" y2="90"  stroke="#888" stroke-width="1.5"/>
  <line x1="330" y1="70"  x2="410" y2="150" stroke="#888" stroke-width="1.5"/>
  <line x1="330" y1="230" x2="410" y2="230" stroke="#888" stroke-width="1.5"/>
  <g font-size="13" text-anchor="middle" font-family="sans-serif">
    <rect x="55"  y="132" width="110" height="34" rx="6" fill="#4a6fa5"/>
    <text x="110" y="154" fill="#fff">Search Tree</text>
    <rect x="252" y="52"  width="90" height="34" rx="6" fill="#3a8f9c"/>
    <text x="297" y="74"  fill="#fff">Binary Tree</text>
    <rect x="252" y="212" width="90" height="34" rx="6" fill="#3a8f9c"/>
    <text x="297" y="234" fill="#fff">Multiway Tree</text>
    <rect x="360" y="14"  width="100" height="30" rx="6" fill="#eef" stroke="#888"/>
    <text x="410" y="34"  fill="#333">BST</text>
    <rect x="360" y="76"  width="100" height="30" rx="6" fill="#eef" stroke="#888"/>
    <text x="410" y="96"  fill="#333">AVL Tree</text>
    <rect x="360" y="136" width="100" height="30" rx="6" fill="#eef" stroke="#888"/>
    <text x="410" y="156" fill="#333">Red-Black</text>
    <rect x="360" y="216" width="100" height="30" rx="6" fill="#eef" stroke="#888"/>
    <text x="410" y="236" fill="#333">B-Tree</text>
  </g>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: "Binary Search Trees (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- Search trees split by *where* they are stored: an [internal search tree]{.hl} lives in main memory, while an [external search tree]{.hl} lives on external storage (e.g. disk).
  - A whole tree may not fit in main memory; for external trees, [disk-access time]{.hl} usually dominates performance.

- A [binary search tree]{.hl} (BST) has the following properties:

<div class="sub-item">

- Each node holds one key, and all keys are distinct.
- There is a root at the top level, and every node has at most two children.
- For any node, its key is [greater]{.hl} than all keys in its left subtree and [less]{.hl} than all keys in its right subtree.

</div>

---
layout: prism
heading: "Binary Search Trees (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div class="tikz-fig">
<svg viewBox="0 0 460 250" style="width: 100%;">
  <g stroke="#888" stroke-width="1.5">
    <line x1="230" y1="30" x2="120" y2="110"/><line x1="230" y1="30" x2="340" y2="110"/>
    <line x1="120" y1="110" x2="60" y2="190"/><line x1="120" y1="110" x2="180" y2="190"/>
    <line x1="340" y1="110" x2="300" y2="190"/><line x1="340" y1="110" x2="420" y2="190"/>
  </g>
  <g font-size="15" text-anchor="middle" font-family="sans-serif">
    <circle cx="230" cy="30"  r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="230" y="35">30</text>
    <circle cx="120" cy="110" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="120" y="115">20</text>
    <circle cx="340" cy="110" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="340" y="115">40</text>
    <circle cx="60"  cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="60"  y="195">10</text>
    <circle cx="180" cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="180" y="195">25</text>
    <circle cx="300" cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="300" y="195">35</text>
    <circle cx="420" cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="420" y="195">45</text>
  </g>
</svg>
<p style="text-align:center; color:#555; font-size:0.85rem; margin:0.2rem 0 0;">balanced &mdash; height 3</p>
</div>
<div class="tikz-fig">
<svg viewBox="0 0 460 330" style="width: 100%;">
  <g stroke="#888" stroke-width="1.5">
    <line x1="230" y1="30" x2="140" y2="110"/><line x1="230" y1="30" x2="360" y2="110"/>
    <line x1="140" y1="110" x2="80" y2="190"/><line x1="140" y1="110" x2="200" y2="190"/>
    <line x1="80" y1="190" x2="40" y2="270"/><line x1="80" y1="190" x2="120" y2="270"/>
  </g>
  <g font-size="15" text-anchor="middle" font-family="sans-serif">
    <circle cx="230" cy="30"  r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="230" y="35">40</text>
    <circle cx="140" cy="110" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="140" y="115">30</text>
    <circle cx="360" cy="110" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="360" y="115">45</text>
    <circle cx="80"  cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="80"  y="195">20</text>
    <circle cx="200" cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="200" y="195">35</text>
    <circle cx="40"  cy="270" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="40"  y="275">10</text>
    <circle cx="120" cy="270" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="120" y="275">25</text>
  </g>
</svg>
<p style="text-align:center; color:#555; font-size:0.85rem; margin:0.2rem 0 0;">unbalanced &mdash; height 4</p>
</div>
</div>

<p style="text-align:center; margin-top: 0.8rem;">Both are valid BSTs, but a tree's <span class="hl">height strongly affects efficiency</span>.</p>

---
layout: prism
heading: "Binary Search Tree — Search"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- To find a node with key $x$: return that node if it exists, otherwise return `null`.

- At each node we compare $x$ with the node's key and recurse into exactly [one]{.hl} subtree, so a search follows a single root-to-leaf path.

</div>
<div>

```text
search(t, x):
// t: root of (sub)tree, x: key sought
  if (t == null || t.item == x):
      return t
  else if (x < t.item):
      return search(t.left, x)
  else:
      return search(t.right, x)
```

</div>
</div>

---
layout: prism
heading: "Binary Search Tree — Search (Demo)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int item; Node *left = nullptr, *right = nullptr; };

Node* insert(Node* t, int x) {
    if (!t) { Node* r = new Node; r->item = x; return r; }
    if (x < t->item) t->left  = insert(t->left, x);
    else             t->right = insert(t->right, x);
    return t;
}
Node* search(Node* t, int x) {
    if (!t || t->item == x) return t;
    return x < t->item ? search(t->left, x) : search(t->right, x);
}

int main() {
    Node* root = nullptr;
    for (int v : {30, 20, 40, 10, 25, 35, 45}) root = insert(root, v);
    for (int q : {25, 33}) {
        Node* f = search(root, q);
        cout << "search(" << q << ") -> " << (f ? "found" : "null") << '\n';
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Binary Search Tree — Insertion (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

- To insert $x$, first there must be no node already holding key $x$.

- Finding the spot for $x$ is exactly one *unsuccessful* search: follow the search path from the root until we reach a `null` link, and hang $x$ there.

- Inserting `30, 20, 25, 40, 10, 35` in order yields a well-balanced tree.

</div>
<div>

```text
insert(t, x):
// t: root of (sub)tree, x: key to insert
  if (t == null):
      hang a node with key x
      below t's parent; done
  else if (x < t.item):
      insert(t.left, x)
  else:
      insert(t.right, x)
```

</div>
</div>

---
layout: prism
heading: "Binary Search Tree — Insertion (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- A recursive version returns the (possibly new) subtree root and re-links it to the parent:

```text
insertItem(t, x):
  if (t == null):
      r.item ← x; r.left ← r.right ← null
      return r        // new node
  else if (x < t.item):
      t.left ← insertItem(t.left, x)
  else:
      t.right ← insertItem(t.right, x)
  return t
```

- Inserting `10, 20, 25, 30, 40, 45` (already sorted) [degenerates]{.hl} into a linked list of height 6.

</div>
<div>

<div class="tikz-fig" style="margin-top: 2.5rem;">
<svg viewBox="0 0 560 300" style="width: 100%;">
  <g stroke="#888" stroke-width="1.5">
    <line x1="60" y1="40" x2="150" y2="80"/>
    <line x1="150" y1="80" x2="240" y2="120"/>
    <line x1="240" y1="120" x2="330" y2="160"/>
    <line x1="330" y1="160" x2="420" y2="200"/>
    <line x1="420" y1="200" x2="510" y2="240"/>
  </g>
  <g font-size="15" text-anchor="middle" font-family="sans-serif">
    <circle cx="60"  cy="40"  r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="60"  y="45">10</text>
    <circle cx="150" cy="80"  r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="150" y="85">20</text>
    <circle cx="240" cy="120" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="240" y="125">25</text>
    <circle cx="330" cy="160" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="330" y="165">30</text>
    <circle cx="420" cy="200" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="420" y="205">40</text>
    <circle cx="510" cy="240" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="510" y="245">45</text>
  </g>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: "Binary Search Tree — Insertion (Demo)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int item; Node *left = nullptr, *right = nullptr; };

Node* insertItem(Node* t, int x) {
    if (!t) { Node* r = new Node; r->item = x; return r; }  // new node
    if (x < t->item) t->left  = insertItem(t->left, x);
    else             t->right = insertItem(t->right, x);
    return t;
}
int height(Node* t) {
    if (!t) return 0;
    return 1 + max(height(t->left), height(t->right));
}

int main() {
    Node *a = nullptr, *b = nullptr;
    for (int v : {30, 20, 25, 40, 10, 35}) a = insertItem(a, v);
    for (int v : {10, 20, 25, 30, 40, 45}) b = insertItem(b, v);  // sorted input
    cout << "balanced insert height  : " << height(a) << '\n';
    cout << "sorted insert height    : " << height(b) << '\n';
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Binary Search Tree — Deletion (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Deleting a node $r$ falls into three cases:

<div class="sub-item-enum">

1. **Case 1 — $r$ is a leaf.** Removing it affects nothing: set the parent's link to $r$ to `null`.
2. **Case 2 — $r$ has one child.** Re-link the parent's pointer directly to $r$'s single child.
3. **Case 3 — $r$ has two children.** Find the node $s$ holding the *successor* (minimum key of $r$'s right subtree), copy $s$ into $r$'s place, then delete $s$ from the right subtree.

</div>

- Case 3 reduces to deleting $s$, which — being a minimum — has at most one child, so it is really a Case 1 or Case 2 deletion.

---
layout: prism
heading: "Binary Search Tree — Deletion (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- `delete` walks down to the key, then `deleteNode` handles the three cases, and `deleteMinItem` extracts the successor for Case 3.

</div>
<div>

```text
delete(t, x):
  if (t == null): raiseError("not found")
  else if (x == t.item): return deleteNode(t)
  else if (x < t.item):
      t.left ← delete(t.left, x);  return t
  else:
      t.right ← delete(t.right, x); return t
```

</div>
</div>

---
layout: prism
heading: "Binary Search Tree — Deletion (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

```text
deleteNode(t):
  if (t.left == null && t.right == null):  // Case 1
      return null
  else if (t.left == null):                // Case 2
      return t.right
  else if (t.right == null):               // Case 2
      return t.left
  else:                                    // Case 3
      (minItem, node) ← deleteMinItem(t.right)
      t.item ← minItem; t.right ← node
      return t
```

</div>
<div>

```text
deleteMinItem(t):
  if (t.left == null):
      return (t.item, t.right)   // min found
  else:
      (minItem, node) ← deleteMinItem(t.left)
      t.left ← node
      return (minItem, t)
```

</div>
</div>

---
layout: prism
heading: "Binary Search Tree — Deletion (Demo)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Node { int item; Node *left = nullptr, *right = nullptr; };

Node* insert(Node* t, int x) {
    if (!t) { Node* r = new Node; r->item = x; return r; }
    if (x < t->item) t->left = insert(t->left, x);
    else             t->right = insert(t->right, x);
    return t;
}
pair<int, Node*> deleteMin(Node* t) {
    if (!t->left) return {t->item, t->right};
    auto [m, node] = deleteMin(t->left);
    t->left = node;
    return {m, t};
}
Node* remove(Node* t, int x) {
    if (!t) return nullptr;
    if (x < t->item) t->left = remove(t->left, x);
    else if (x > t->item) t->right = remove(t->right, x);
    else {                                   // found
        if (!t->left)  return t->right;      // Case 1 / 2
        if (!t->right) return t->left;       // Case 2
        auto [m, node] = deleteMin(t->right);// Case 3
        t->item = m; t->right = node;
    }
    return t;
}
void inorder(Node* t) { if (t) { inorder(t->left); cout << t->item << ' '; inorder(t->right); } }

int main() {
    Node* root = nullptr;
    for (int v : {55, 15, 60, 8, 28, 90, 3, 18, 30, 48, 38, 50, 33, 32, 36})
        root = insert(root, v);
    cout << "before      : "; inorder(root); cout << '\n';
    root = remove(root, 18);   // Case 1 (leaf)
    root = remove(root, 30);   // Case 2 (one child)
    root = remove(root, 28);   // Case 3 (two children)
    cout << "after deletes: "; inorder(root); cout << '\n';
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Tree Traversal (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Visiting every node of a tree is called a [traversal]{.hl}. Three recursive orders are standard:

<div class="sub-item-enum">

1. [Preorder]{.hl} — visit the *root*, then the left subtree, then the right subtree.
2. [Inorder]{.hl} — visit the left subtree, then the *root*, then the right subtree. On a BST this yields the keys in [sorted order]{.hl}.
3. [Postorder]{.hl} — visit the left subtree, then the right subtree, then the *root*.

</div>

---
layout: prism
heading: "Tree Traversal (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

```text
preOrder(r):
  if (r != null):
      visit(r)
      preOrder(r.left)
      preOrder(r.right)

inOrder(r):
  if (r != null):
      inOrder(r.left)
      visit(r)
      inOrder(r.right)

postOrder(r):
  if (r != null):
      postOrder(r.left)
      postOrder(r.right)
      visit(r)
```

</div>
<div>

<div class="tikz-fig" style="margin-top: 1rem;">
<svg viewBox="0 0 480 300" style="width: 100%;">
  <g stroke="#888" stroke-width="1.5">
    <line x1="240" y1="30" x2="140" y2="100"/><line x1="240" y1="30" x2="360" y2="100"/>
    <line x1="140" y1="100" x2="80" y2="170"/><line x1="140" y1="100" x2="200" y2="170"/>
    <line x1="360" y1="100" x2="420" y2="170"/>
    <line x1="200" y1="170" x2="150" y2="240"/><line x1="200" y1="170" x2="250" y2="240"/>
  </g>
  <g font-size="15" text-anchor="middle" font-family="sans-serif">
    <circle cx="240" cy="30"  r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="240" y="35">6</text>
    <circle cx="140" cy="100" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="140" y="105">2</text>
    <circle cx="360" cy="100" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="360" y="105">8</text>
    <circle cx="80"  cy="170" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="80"  y="175">1</text>
    <circle cx="200" cy="170" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="200" y="175">4</text>
    <circle cx="420" cy="170" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="420" y="175">9</text>
    <circle cx="150" cy="240" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="150" y="245">3</text>
    <circle cx="250" cy="240" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="250" y="245">5</text>
  </g>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: "Tree Traversal (Demo)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int item; Node *left = nullptr, *right = nullptr; };
Node* insert(Node* t, int x) {
    if (!t) { Node* r = new Node; r->item = x; return r; }
    if (x < t->item) t->left = insert(t->left, x);
    else             t->right = insert(t->right, x);
    return t;
}
void pre(Node* t)  { if (t) { cout << t->item << ' '; pre(t->left);  pre(t->right); } }
void in(Node* t)   { if (t) { in(t->left);  cout << t->item << ' '; in(t->right); } }
void post(Node* t) { if (t) { post(t->left); post(t->right); cout << t->item << ' '; } }

int main() {
    Node* root = nullptr;
    for (int v : {6, 2, 8, 1, 4, 9, 3, 5}) root = insert(root, v);
    cout << "preorder : "; pre(root);  cout << '\n';
    cout << "inorder  : "; in(root);   cout << "  (sorted!)\n";
    cout << "postorder: "; post(root); cout << '\n';
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Practice: Immigration Inspection (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- $n$ people wait in one line for immigration inspection. Each booth takes a different amount of time to inspect one person. All booths start empty; a booth handles one person at a time. The person at the front goes to any free booth — or waits for a faster one to free up.

- We want to [minimize]{.hl} the total time until *everyone* has been inspected. Given $n$ and the per-person times `times[]`, return that minimum.

<div class="theorem-box">
<div class="theorem-box-title">Parametric search — binary search on the answer</div>
<div class="theorem-box-body">

For a candidate time $T$, booth $i$ can process $\lfloor T / \text{times}[i] \rfloor$ people. The total is [monotonic]{.hl} in $T$, so binary-search the smallest $T$ with $\sum_i \lfloor T/\text{times}[i]\rfloor \geq n$. For `n = 6, times = [7, 10]`, the answer is `28`.

</div>
</div>

---
layout: prism
heading: "Practice: Immigration Inspection (2/2)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long solution(int n, vector<int> times) {
    long long lo = 1, hi = (long long)*max_element(times.begin(), times.end()) * n;
    long long ans = hi;
    while (lo <= hi) {
        long long mid = (lo + hi) / 2, cnt = 0;
        for (int t : times) cnt += mid / t;   // people processed by time mid
        if (cnt >= n) { ans = mid; hi = mid - 1; }
        else            lo = mid + 1;
    }
    return ans;
}

int main() {
    cout << "answer = " << solution(6, {7, 10}) << endl;  // expected 28
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Practice: Stepping Stones (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- A destination sits `distance` away from the start, with rocks placed in between. We remove exactly `n` rocks. After removal, look at the gaps between consecutive points (start, remaining rocks, destination) and take the [minimum]{.hl} gap.

- Among all ways to remove `n` rocks, return the [largest possible]{.hl} minimum gap. For `distance = 25, rocks = [2, 14, 11, 21, 17], n = 2`, the answer is `4`.

<div class="theorem-box">
<div class="theorem-box-title">Parametric search — binary search on the answer</div>
<div class="theorem-box-body">

Binary-search a candidate minimum gap $d$. Walking left to right, greedily remove any rock closer than $d$ to the last kept point and count the removals. If the count $\leq n$, gap $d$ is [feasible]{.hl}; search for a larger one.

</div>
</div>

---
layout: prism
heading: "Practice: Stepping Stones (2/2)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    sort(rocks.begin(), rocks.end());
    rocks.push_back(distance);            // treat destination as final point
    int lo = 1, hi = distance, ans = 0;
    while (lo <= hi) {
        int mid = (lo + hi) / 2, prev = 0, removed = 0;
        for (int p : rocks) {
            if (p - prev < mid) removed++;   // too close: remove this rock
            else                prev = p;    // keep it
        }
        if (removed <= n) { ans = mid; lo = mid + 1; }
        else               hi = mid - 1;
    }
    return ans;
}

int main() {
    cout << "answer = " << solution(25, {2, 14, 11, 21, 17}, 2) << endl;  // expected 4
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY_W10"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- Implement a [binary search tree]{.hl} supporting the full ADT: `search`, `insert`, `delete`, `isEmpty`, and `clear` (remove all).

- Read up on [parametric search]{.hl} — the "binary search on the answer" technique behind today's two practice problems — and try applying it to a problem of your own.

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
