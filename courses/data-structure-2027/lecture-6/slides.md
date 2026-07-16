---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 6
download: true
info: |
  ## Data Structure Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-6-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 06: Trees and Tries</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span class="text-gray-900 dark:text-gray-100">Trees and Tries</span></p>
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
heading: "Recap: Circular Queue Model"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- An array-based queue implementation has a weakness: after a `pop`, the vacated space at the front remains unused.

- A [circular queue]{.hl}, also known as a *ring buffer*, uses a single fixed-size buffer as if it were connected end-to-end.

- Operations follow the *FIFO* principle, but the storage space is utilized efficiently by wrapping around.

- The size of the queue is fixed and determined at the start of its implementation.

</div>
<div>

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-01.svg" class="tikz-fig" style="width: 85%;" />

</div>
</div>

---
layout: prism
heading: "Recap: Circular Queue Model — Pointers"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- The start and end of the queue wrap around to form a circle.

- Circular queues typically use two pointers, `front` and `rear`, to track the first and last elements.
  - The `front` pointer indicates the *start* of the queue, and the `rear` pointer signifies its *end*.

- Like the linear queue, this structure has `enqueue` and `dequeue` operations, equivalent to `push` and `pop`, respectively.

- `front` retrieves the front element without removing it from the queue.

---
layout: prism
heading: "Recap: Priority Queue Model"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [priority queue]{.hl} is a data structure that allows at least two operations: `insert`, which does the obvious thing, and `removeMin`, which finds, returns, and removes the minimum element.
  - `insert` is the equivalent of `push`, and `removeMin` is the priority queue equivalent of `pop`.

- As with most data structures, other operations can sometimes be added, but these are extensions and not part of the basic model.

- Priority queues have many applications: operating systems, sorting, greedy algorithms, and more.

<div style="margin-top: 1.5rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-02.svg" class="tikz-fig" style="width: 55%;" />
</div>

---
layout: prism
heading: Trees and Tries
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- For large amounts of input, the linear access time of linked lists is prohibitive.

- This lecture looks at a simple data structure for which the average running time of most operations is $\mathcal{O}(\log N)$ — the [binary search tree]{.hl} — and sketches conceptually simple modifications that guarantee this bound even in the *worst case*.

- In this lecture, we discuss the binary search tree and its refinements:

<div class="sub-item-enum">

1. See structures and implementations of trees.
2. See how trees can be used to evaluate arithmetic expressions.
3. Support searching in $\mathcal{O}(\log N)$ average time, and refine these ideas for $\mathcal{O}(\log N)$ worst-case bounds.
4. Introduce multiway search trees.

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">The Binary Search Tree ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Preliminaries</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Binary Trees</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Binary Search Tree Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">AVL Trees</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Red-Black Trees</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Multiway Tree</span></p>
  </div>

</div>

---
layout: prism
heading: "Preliminaries — Defining a Tree"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [tree]{.hl} can be defined in several ways; one natural way is *recursively*.

- A tree is a collection of nodes. The collection can be empty; otherwise it consists of a distinguished node $r$, called the [root]{.hl}, and zero or more nonempty subtrees $T_1, T_2, \ldots, T_k$, each of whose roots is connected by a directed [edge]{.hl} from $r$.
  - The root of each subtree is a *child* of $r$, and $r$ is the *parent* of each subtree root.

- A tree of $N$ nodes has exactly $N - 1$ edges.

</div>
<div>

<div style="height: 2.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-03.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Preliminaries — Terminology"
---

- Below, the *root* is $A$; node $F$ has $A$ as a parent and $K$, $L$, $M$ as children.
  - Each node may have an arbitrary number of children, possibly zero. *Grandparent* and *grandchild* relations are defined similarly.

- Nodes with no children are [leaves]{.hl}; here the leaves are $B$, $C$, $H$, $I$, $P$, $Q$, $L$, $M$, $N$.

- Nodes with the same parent are [siblings]{.hl}; thus $K$, $L$, $M$ are all siblings.

<div style="margin-top: 0.5rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-04.svg" class="tikz-fig" style="width: 50%;" />
</div>

---
layout: prism
heading: "Preliminaries — Implementation"
---

- One way to implement a tree is to keep in each node, besides its data, a link to *each* child.
  - The number of children per node can vary and is not known in advance, so making the children direct links may waste too much space.

- To tackle this, we keep the children of each node in a *linked list* of tree nodes.

<div style="margin-top: 1rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-05.svg" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: "Preliminaries — First-Child / Next-Sibling"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The figure shows how the tree is represented in the implementation.

- Arrows that point downward are `firstChild` links; arrows that go left to right are `nextSibling` links.
  - Null links are not drawn, because there are too many.

- Node $E$ has both a link to a sibling ($F$) and a link to a child ($I$), while some nodes have neither.

</div>
<div>

<div style="height: 4rem;"></div>

```cpp
struct TreeNode {
    Object element;
    TreeNode* firstChild;
    TreeNode* nextSibling;
};
```

</div>
</div>

---
layout: prism
heading: "Binary Trees"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A [binary tree]{.hl} is a tree in which no node can have more than two children.
  - A binary tree consists of a root and two subtrees, $T_L$ and $T_R$, both of which could possibly be empty.

- The depth of an average binary tree is considerably smaller than $N$.
  - The average depth is $\mathcal{O}(\sqrt{N})$, and for the *binary search tree* the average depth is $\mathcal{O}(\log N)$.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-06.svg" class="tikz-fig" style="width: 85%;" />

</div>
</div>

---
layout: prism
heading: "Binary Trees — Node Declaration"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>


- Because a binary tree node has at most two children, we can keep direct links to them.
  - Unfortunately, the depth can still be as large as $N - 1$.

- The declaration resembles that for doubly linked lists: a node is a structure with the `element` information plus two pointers (`left` and `right`) to other nodes.

```cpp
struct BinaryNode {
    Object element;
    BinaryNode* left;
    BinaryNode* right;
};
```

</div>
<div>

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-07.svg" class="tikz-fig" style="width: 55%;" />

</div>
</div>

---
layout: prism
heading: "Applications — Expression Trees"
---

<div style="margin-top: 0.5rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-08.svg" class="tikz-fig" style="width: 68%;" />
</div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- The above is an [expression tree]{.hl}: the leaves are operands (constants or variable names) and the other nodes contain operators.
  - It denotes $(a + b \cdot c) + ((d \cdot e + f) \cdot g)$.

- It is possible for a node to have only one child, as with the unary minus operator.

---
layout: prism
heading: "Applications — Traversals"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Producing a parenthesized left expression, then the operator at the root, then a parenthesized right expression gives an *infix* expression. This (left, node, right) strategy is an [inorder traversal]{.hl}.

- Printing the left subtree, the right subtree, then the operator gives the *postfix* form $a\ b\ c\cdot +\ d\ e\cdot f + g\cdot +$ — a [postorder traversal]{.hl}.

- Printing the operator first, then the left and right subtrees, gives the *prefix* form $+ + a \cdot b\ c \cdot + \cdot d\ e\ f\ g$ — a [preorder traversal]{.hl}.

---
layout: prism
heading: "DIY: Tree Traversals"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node {
    char val;
    Node* left;
    Node* right;
    Node(char v) : val(v), left(nullptr), right(nullptr) {}
};

void preorder(Node* t)  { if (!t) return; cout << t->val; preorder(t->left);  preorder(t->right); }
void inorder(Node* t)   { if (!t) return; inorder(t->left);   cout << t->val;  inorder(t->right); }
void postorder(Node* t) { if (!t) return; postorder(t->left); postorder(t->right); cout << t->val; }

int main() {
    // expression tree for (a + b) * c
    Node* mul  = new Node('*');
    Node* plus = new Node('+');
    mul->left  = plus;         mul->right  = new Node('c');
    plus->left = new Node('a'); plus->right = new Node('b');

    cout << "preorder  (prefix):  "; preorder(mul);   cout << "\n";
    cout << "inorder   (infix):   "; inorder(mul);    cout << "\n";
    cout << "postorder (postfix): "; postorder(mul);  cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Binary Search Tree Model"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- An important application of binary trees is *searching*. Assume each node stores an item.

- The property that makes a binary tree a [binary search tree]{.hl} is: for every node $X$, all items in its left subtree are *smaller* than the item in $X$, and all items in its right subtree are *larger*.

- The left tree is a binary search tree; the right one is not, because of the `7`.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-09.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "BST — contains, findMin, insert"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- The BST has five important operations. `contains` returns `true` if some node in $T$ holds $X$, else `false`.

- To perform `findMin`, start at the root and go left as long as there is a left child; the stopping point is the *smallest* element.
  - `findMax` is the same, but branching right, ending at the *largest*.

- To `insert` $X$, proceed down as with `contains`. If $X$ is found, do nothing; otherwise insert $X$ at the last spot on the path.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-10.svg" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "BST — Removal"
---

- Once we have found the node to be deleted, several cases arise:
  - If the node is a *leaf*, it can be deleted immediately.
  - If the node has *one child*, it is deleted after its parent bypasses it with a link (`remove` `4` at below left).

- The complicated case is a node with *two children*: replace its data with the smallest data of the right subtree (easily found) and recursively delete that node (`remove` `2` at below right).

<div style="margin-top: 0.8rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-11.svg" class="tikz-fig" style="width: 82%;" />
</div>

---
layout: prism
heading: "BST — Implementation (Structure & Search)"
---

```cpp
struct BinaryNode {
    Comparable element;
    BinaryNode* left;
    BinaryNode* right;
    BinaryNode(const Comparable& e, BinaryNode* l, BinaryNode* r)
        : element{e}, left{l}, right{r} {}
};

bool contains(const Comparable& x, BinaryNode* t) const {
    if (t == nullptr)          return false;
    else if (x < t->element)   return contains(x, t->left);
    else if (t->element < x)   return contains(x, t->right);
    else                       return true;         // match found
}

BinaryNode* findMin(BinaryNode* t) const {          // leftmost node
    if (t == nullptr)          return nullptr;
    if (t->left == nullptr)    return t;
    return findMin(t->left);
}
```

---
layout: prism
heading: "BST — Implementation (insert & remove)"
---

```cpp
void insert(const Comparable& x, BinaryNode*& t) {
    if (t == nullptr)          t = new BinaryNode{x, nullptr, nullptr};
    else if (x < t->element)   insert(x, t->left);
    else if (t->element < x)   insert(x, t->right);
    else                       ;                     // duplicate: do nothing
}

void remove(const Comparable& x, BinaryNode*& t) {
    if (t == nullptr)          return;               // item not found
    if (x < t->element)        remove(x, t->left);
    else if (t->element < x)   remove(x, t->right);
    else if (t->left != nullptr && t->right != nullptr) {   // two children
        t->element = findMin(t->right)->element;
        remove(t->element, t->right);
    } else {                                         // one or zero children
        BinaryNode* oldNode = t;
        t = (t->left != nullptr) ? t->left : t->right;
        delete oldNode;
    }
}
```

---
layout: prism
heading: "DIY: BST Insert + Inorder Traversal"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
    Node(int k) : key(k), left(nullptr), right(nullptr) {}
};

void insert(Node*& t, int x) {
    if (t == nullptr)     t = new Node(x);
    else if (x < t->key)  insert(t->left, x);
    else if (x > t->key)  insert(t->right, x);   // duplicates ignored
}

void inorder(Node* t) {                          // left, node, right
    if (!t) return;
    inorder(t->left);
    cout << t->key << ' ';
    inorder(t->right);
}

int findMin(Node* t) { while (t->left) t = t->left; return t->key; }

int main() {
    int data[] = {6, 2, 8, 1, 4, 3, 5, 7};
    Node* root = nullptr;
    for (int x : data) insert(root, x);

    cout << "inorder (sorted): ";
    inorder(root);
    cout << "\nmin = " << findMin(root) << endl;   // inorder always yields sorted order
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "BST — Average-Case Analysis"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- We *expect* every operation (`contains`, `findMin`, `findMax`, `insert`, `remove`) to take $\mathcal{O}(\log N)$ time: in constant time we descend a level, operating on a tree roughly half as large.

- The running time is $\mathcal{O}(d)$, where $d$ is the *depth* of the node holding the accessed item.

- The sum of the depths of all nodes is the [internal path length]{.hl} $D(N)$, with $D(1) = 0$. Its average satisfies

$$
D(N) = \frac{2}{N}\left[\sum_{j=0}^{N-1} D(j)\right] + N - 1.
$$

- After many random `insert` / `remove` operations, trees tend to become *right-heavy*.

---
layout: prism
heading: "BST — The Need for Balance"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- If input arrives *presorted*, a series of inserts takes quadratic time, giving an expensive linked list: the tree consists only of nodes with no left children.

- One solution is an extra structural condition called [balance]{.hl}: no node is allowed to get too deep.
  - Many balanced-tree algorithms exist; most are more complicated than a standard BST and take longer on average for updates.

- A second method forgoes balance, allowing the tree to be arbitrarily deep, but applies a *restructuring rule* after each operation to keep future operations efficient. Such structures are [self-adjusting]{.hl}.

---
layout: prism
heading: "AVL Trees"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- An [Adelson-Velskii and Landis (AVL) tree]{.hl} is a binary search tree with a *balance condition*.
  - The condition must be easy to maintain and ensure the depth is $\mathcal{O}(\log N)$.
  - Requiring the left and right subtrees to have the same height is *not* sufficient.

- Insisting that every node have subtrees of equal height is too rigid: with an empty subtree of height $-1$, only perfectly balanced trees of $2^k - 1$ nodes qualify — so the condition must be relaxed.

</div>
<div>

<div style="height: 0rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-12.svg" class="tikz-fig" style="width: 65%;" />

</div>
</div>

---
layout: prism
heading: "AVL Trees — Balance Condition"
---

- An AVL tree is a binary search tree in which, for every node, the heights of the left and right subtrees differ by at most $1$.
  - Only the below *left* tree is an AVL tree.

- The height of an AVL tree is at most roughly $1.44 \log(N + 2) - 1.328$, but in practice only slightly more than $\log N$.

- All tree operations can be performed in $\mathcal{O}(\log N)$ time, except possibly insertion and deletion.

<div style="margin-top: 0rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-13.svg" class="tikz-fig" style="width: 52%;" />
</div>

---
layout: prism
heading: "AVL Trees — The Four Cases"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- On insertion, we update balancing information for nodes on the path back to the root. Inserting a node could violate the AVL property, which must be restored before the insertion is over.
  - This can always be done with a simple modification called a [rotation]{.hl}.

- Let $\alpha$ be the node to be rebalanced. A violation can occur in four cases:

<div class="sub-item-enum">

1. An insertion into the *left* subtree of the *left* child of $\alpha$.
2. An insertion into the *right* subtree of the *left* child of $\alpha$.
3. An insertion into the *left* subtree of the *right* child of $\alpha$.
4. An insertion into the *right* subtree of the *right* child of $\alpha$.

</div>

- Cases 1 and 4 are mirror images (as are 2 and 3): two basic cases in theory, still four cases in programming.

---
layout: prism
heading: "AVL — Single Rotation"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The first and last cases — insertion on the *outside* (left–left or right–right) — are fixed by a [single rotation]{.hl}.

- To rebalance, move $X$ up a level and $Z$ down a level, rearranging the nodes into an equivalent tree.

- An intuitive picture: grab the child (pivot) $k_1$, and let gravity take hold — $k_1$ becomes the new root.
  - Since $k_2 > k_1$, $k_2$ becomes the right child of $k_1$; $X$ and $Z$ stay as the left child of $k_1$ and the right child of $k_2$.
  - Subtree $Y$, holding items between $k_1$ and $k_2$, becomes $k_2$'s left child and satisfies all ordering requirements.

---
layout: prism
heading: "AVL — Single Rotation (Abstract)"
---

<div style="margin-top: 0rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-14.svg" class="tikz-fig" style="width: 60%;" />
</div>

- The pivot $k_1$ rises to the root; $k_2$ becomes its right child, and subtree $Y$ (between $k_1$ and $k_2$) reattaches as $k_2$'s left child.

---
layout: prism
heading: "AVL — Single Rotation (Example)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- Below, the AVL property is destroyed by the insertion of `6`, then fixed by a *single rotation*.

- The fourth case is a symmetric image, and is fixed by a single rotation as well.

<div style="margin-top: 1rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-15.svg" class="tikz-fig" style="width: 72%;" />
</div>

---
layout: prism
heading: "AVL — Double Rotation"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- The single-rotation algorithm does *not* work for the second and third cases: subtree $Y$ is too deep, and a single rotation leaves it just as deep.

- The second and third cases — insertion on the *inside* (left–right or right–left) — are handled by the slightly more complex [double rotation]{.hl}.

- To fix these, turn the left-right tree into a left-left tree via one rotation, then balance it with an additional rotation (and vice versa).

---
layout: prism
heading: "AVL — Why a Single Rotation Fails"
---

<div style="margin-top: 0rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-16.svg" class="tikz-fig" style="width: 60%;" />
</div>

- Rotating $k_2$ and $k_1$ leaves the deep subtree $Y$ (red) at the same depth — the imbalance is not resolved, so a single rotation is insufficient here.

---
layout: prism
heading: "AVL — Double Rotation (Example)"
---

- We cannot leave $k_3$ as the root, and a rotation between $k_3$ and $k_1$ does not work — so $k_2$ becomes the new root.

- This forces $k_1$ to be $k_2$'s left child and $k_3$ to be its right child, and fully determines the locations of the four subtrees.

- The result satisfies the AVL property and restores the height to its pre-insertion value, so all rebalancing and height updating is complete.

<div style="margin-top: 0.6rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-17.svg" class="tikz-fig" style="width: 60%;" />
</div>

---
layout: prism
heading: "AVL — Double Rotation (Abstract)"
---

<div style="margin-top: 0rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-18.svg" class="tikz-fig" style="width: 60%;" />
</div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The middle node $k_2$ rises to the root; $k_1$ and $k_3$ become its children, and the four subtrees $A$, $B$, $C$, $D$ are distributed to satisfy the ordering property.

---
layout: prism
heading: "AVL — Implementation (Node & Rotations)"
---

```cpp
struct AvlNode {
    Comparable element;
    AvlNode* left;
    AvlNode* right;
    int height;
    AvlNode(const Comparable& e, AvlNode* l, AvlNode* r, int h = 0)
        : element{e}, left{l}, right{r}, height{h} {}
};
int height(AvlNode* t) const { return t == nullptr ? -1 : t->height; }
void rotateWithLeftChild(AvlNode*& k2) {            // single rotation (LL case)
    AvlNode* k1 = k2->left;
    k2->left  = k1->right;
    k1->right = k2;
    k2->height = max(height(k2->left), height(k2->right)) + 1;
    k1->height = max(height(k1->left), k2->height) + 1;
    k2 = k1;
}
void doubleWithLeftChild(AvlNode*& k3) {            // double rotation (LR case)
    rotateWithRightChild(k3->left);
    rotateWithLeftChild(k3);
}
```

---
layout: prism
heading: "AVL — Implementation (insert & balance)"
---

```cpp
static const int ALLOWED_IMBALANCE = 1;

void insert(const Comparable& x, AvlNode*& t) {
    if (t == nullptr)          t = new AvlNode{x, nullptr, nullptr};
    else if (x < t->element)   insert(x, t->left);
    else if (t->element < x)   insert(x, t->right);
    balance(t);                                      // rebalance on the way up
}

void balance(AvlNode*& t) {
    if (t == nullptr) return;
    if (height(t->left) - height(t->right) > ALLOWED_IMBALANCE) {
        if (height(t->left->left) >= height(t->left->right))  rotateWithLeftChild(t);
        else                                                  doubleWithLeftChild(t);
    } else if (height(t->right) - height(t->left) > ALLOWED_IMBALANCE) {
        if (height(t->right->right) >= height(t->right->left)) rotateWithRightChild(t);
        else                                                   doubleWithRightChild(t);
    }
    t->height = max(height(t->left), height(t->right)) + 1;
}
```

---
layout: prism
heading: "HW: Implement a Complete AVL Tree Class"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Extend the AVL tree code above and implement the `remove` method as well.
  - Test it with the driver below.

- Upload your C++ code to the LMS as `20XXXXXX_HW_W06.cpp`.

```cpp
int main() {
    AVLTree tree;
    AVLNode* root = nullptr;
    root = tree.insert(root, 10);   root = tree.insert(root, 20);
    root = tree.insert(root, 30);   root = tree.insert(root, 40);
    root = tree.insert(root, 50);   root = tree.insert(root, 25);
    tree.inOrder(root);
    tree.remove(25);
    tree.inOrder(root);
    return 0;
}
```

---
layout: prism
heading: "Red-Black Trees"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- A historically popular alternative to the AVL tree is the [red-black tree]{.hl}. Operations take $\mathcal{O}(\log N)$ time in the worst case, and a careful nonrecursive `insert` is relatively effortless compared with AVL trees.

- A red-black tree is a binary search tree with the following coloring properties:

<div class="sub-item-enum">

1. Every node is colored either *red* or *black*.
2. The root is *black*.
3. If a node is *red*, its children must be *black*.
4. Every path from a node to a null pointer must contain the same number of *black* nodes.

</div>

- A consequence is that the height is at most $2\log(N + 1)$, so searching is guaranteed logarithmic.

---
layout: prism
heading: "Red-Black Trees — Example"
---

<div style="margin-top: 0rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-19.svg" class="tikz-fig" style="width: 70%;" />
</div>

- Every root-to-null path passes through the same number of black nodes, and no red node has a red child.

---
layout: prism
heading: "Red-Black Trees — Insertion"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The inserted item $X$ must be colored *red*, because of the fourth condition.

- If the parent $P$ of the newly inserted node is *black*, there is no violation.

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-20.svg" class="tikz-fig" style="width: 68%;" />
</div>

- If the parent is already *red*, we violate condition 3 with consecutive red nodes, and must adjust the tree (without violating condition 4). The basic operations for this are *color changes* and *tree rotations*.

---
layout: prism
heading: "Red-Black Trees — Case 1 (Red Sibling)"
---

- Although $P$ is red, its parent $G$ (the grandparent of $X$) must be black. There are two cases, based on the color of $P$'s sibling $S$:

<div class="sub-item-enum">

1. $S$ is *red*.
2. $S$ is *black* or *empty* — with subcases (a) $X$ is $P$'s right child, (b) $X$ is $P$'s left child.

</div>

- For case 1, change $P$ and $S$ to *black* and $G$ to *red*.
  - If $G$ is the root, change it back to black; otherwise recursively check its parent (the great-grandparent of $X$).

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-21.svg" class="tikz-fig" style="width: 52%;" />
</div>

---
layout: prism
heading: "Red-Black Trees — Case 2 (Black Sibling)"
---

- For case 2.1, perform a *left rotation* with pivot $P$, converting the tree into case 2.2.

<div style="margin-top: 0.3rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-22.svg" class="tikz-fig" style="width: 40%;" />
</div>

- For case 2.2, perform a *right rotation* with pivot $G$, and swap the colors of $P$ and $G$.

<div style="margin-top: 0.3rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-23.svg" class="tikz-fig" style="width: 40%;" />
</div>

---
layout: prism
heading: "HW: Implement a Red-Black Tree Class"
---

- Find the deletion mechanism of the red-black tree.
  - It has separated cases, similar to the insertion mechanism.

- Based on the AVL tree class, implement the red-black tree class and test it.

```cpp
enum Color { RED, BLACK };

class RedBlackNode {
public:
    int data;
    bool color;
    RedBlackNode* left;
    RedBlackNode* right;
    RedBlackNode* parent;

    RedBlackNode(int data)
        : data(data), color(RED),
          left(nullptr), right(nullptr), parent(nullptr) {}
};
```

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">The Binary Search Tree ADT</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">The Multiway Tree</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Multiway Tree Model</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">B-Trees</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">2-3 and 2-3-4 Trees</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Tries</span></p>
  </div>

</div>

---
layout: prism
heading: "Multiway Tree Model — Disk I/O"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- So far we assumed the entire data structure fits in main memory. Suppose instead we have more data than fits, so it must reside on *disk*.

- A Big-Oh analysis assumes all operations are equal, but this is untrue when disk I/O is involved.
  - Modern computers execute billions of instructions per second, but a disk is *mechanical* — its speed depends on spinning the disk and moving the head.

- With 10,000,000 items that cannot fit in main memory:
  - An unbalanced BST is a disaster — linear depth, up to 10,000,000 disk accesses.
  - An AVL tree would use about 25 disk accesses on average.
  - We want to reduce disk accesses to a very small constant, such as three or four.

---
layout: prism
heading: "Multiway Tree Model"
---

- A [multiway tree]{.hl} (also known as an [$M$-ary tree]{.hl}) allows $M$-way branching.

- We can create a multiway *search* tree much as we build a binary search tree.

- In a BST we need one key to decide between two branches; in a multiway search tree we need $M - 1$ keys to decide which branch to take.
  - To make this efficient in the worst case, the search tree must be *balanced*.

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-24.svg" class="tikz-fig" style="width: 68%;" />
</div>

---
layout: prism
heading: "B-Trees"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.55em;
}
</style>

- A [B-tree]{.hl} guarantees only a few disk accesses. A B-tree of order $M$ is an $M$-ary tree with:

<div class="sub-item-enum">

1. The data items are stored at *leaves*.
2. Nonleaf nodes store up to $M - 1$ keys to guide searching; key $i$ is the smallest key in subtree $i + 1$.
3. The root is either a leaf or has between $2$ and $M$ children.
4. All nonleaf nodes (except the root) have between $\lceil M/2 \rceil$ and $M$ children.
5. All leaves are at the same depth, with between $\lceil L/2 \rceil$ and $L$ data items.

</div>

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-25.svg" class="tikz-fig" style="width: 74%;" />
</div>

---
layout: prism
heading: "2-3 Trees"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [2-3 tree]{.hl} is a tree in which every internal node has either two children and one data element (a *2-node*) or three children and two data elements (a *3-node*).
  - A 2-3 tree is a B-tree of order 3.

- 2-3 trees are required to be *balanced*: every leaf is at the same level.

- Each left, center, and right subtree of a node contains the same or close to the same amount of data.

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-26.svg" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: "2-3-4 Trees"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [2-3-4 tree]{.hl} (also called a 2-4 tree) is a self-balancing data structure that can implement *dictionaries*.
  - A 2-3-4 tree is a B-tree of order 4.

- The numbers mean a tree where every internal node has either two, three, or four child nodes.

- 2-3-4 trees are *isomorphic* to red-black trees — they are equivalent data structures.

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-27.svg" class="tikz-fig" style="width: 74%;" />
</div>

---
layout: prism
heading: "Tries"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [trie]{.hl} (also known as a *prefix tree* or *digital tree*) is a type of search tree used for locating specific keys within a set.
  - The name comes from re[trie]{.hl}val tree.

- These keys are usually strings, making tries an excellent choice for autocomplete, spell checking, IP routing, and other applications involving large datasets of strings.

- Important properties:
  - Nodes share common prefixes of the string keys they represent, optimizing memory usage and search efficiency.
  - To search for a string, we traverse the tree following the path dictated by its characters.
  - Nodes representing the end of a string are marked specially (a value or flag) to indicate the string's presence.

---
layout: prism
heading: "Tries — Structure"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The root node of a trie typically represents an *empty string* and contains no character.
  - Each of its children represents the *next character* in a string.
  - This structure creates a hierarchical tree where each level corresponds to a character in the strings.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-28.svg" class="tikz-fig" style="width: 65%;" />

</div>
</div>

---
layout: prism
heading: "Tries — Complexity"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Tries primarily represent a set of strings, supporting searching, insertion, and deletion efficiently.

- The time complexity for searching a string in a trie is $\mathcal{O}(m)$, where $m$ is the length of the string.
  - This makes searching extremely efficient, especially for datasets with a large number of strings.

- Tries can be memory-intensive due to the storage of nodes and pointers, especially for many short strings.
  - Because common prefixes are shared among nodes, tries can be more space-efficient than other structures when storing many *overlapping* strings.

---
layout: prism
heading: "DIY: Trie Insert + Search"
---

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

struct TrieNode {
    TrieNode* child[26];
    bool isEnd;
    TrieNode() : isEnd(false) {
        for (int i = 0; i < 26; i++) child[i] = nullptr;
    }
};

void insert(TrieNode* root, const string& word) {
    TrieNode* cur = root;
    for (char c : word) {
        int i = c - 'a';
        if (!cur->child[i]) cur->child[i] = new TrieNode();
        cur = cur->child[i];
    }
    cur->isEnd = true;                       // mark end of a stored word
}

bool search(TrieNode* root, const string& word) {
    TrieNode* cur = root;
    for (char c : word) {
        int i = c - 'a';
        if (!cur->child[i]) return false;    // prefix not present
        cur = cur->child[i];
    }
    return cur->isEnd;                        // full word only if flagged
}

int main() {
    TrieNode* root = new TrieNode();
    for (string w : {"cat", "car", "dog", "duck"}) insert(root, w);

    for (string q : {"car", "care", "dog", "do"})
        cout << q << " -> " << (search(root, q) ? "found" : "absent") << "\n";
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
