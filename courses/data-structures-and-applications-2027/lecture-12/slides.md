---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 12
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-12-ko/
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
.htab {
  border-collapse: collapse;
  font-size: 0.95rem;
  margin: 0 auto;
}
.htab td {
  border: 1px solid #cbd5e1;
  padding: 0.12rem 0.9rem;
  text-align: center;
  min-width: 2.4rem;
}
.htab td.idx {
  background: #e5e7eb;
  color: #374151;
  font-weight: 600;
}
.htab td.hit { background: #a7d8d4; }
.htab td.del { color: #b91c1c; font-style: italic; }
.dark .htab td.idx { background: #374151; color: #e5e7eb; }
.dark .htab td { border-color: #4b5563; }
</style>

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.png" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Data Structures and Applications</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 12: Hash Tables</p>

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
heading: "Recap: AVL Trees"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- An [AVL tree]{.hl} is the classic example of a binary search tree that is kept [balanced]{.hl} at all times. It was devised by [Adelson-Velskii and Landis]{.hl}.

- For *every* node in the tree, the heights of its left and right subtrees differ by [at most 1]{.hl}.

<div class="theorem-box">
<div class="theorem-box-title">AVL balance condition</div>
<div class="theorem-box-body">

For any node $t$: $\;\bigl|\,\operatorname{height}(t.\text{left}) - \operatorname{height}(t.\text{right})\,\bigr| \leq 1.$

</div>
</div>

- This guarantees a height of $O(\log N)$, so search, insertion, and deletion all run in $O(\log N)$ worst-case time.

---
layout: prism
heading: "AVL Trees: Rebalancing"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- After an insertion, the balance condition may be violated at some node. We restore it with one or two [rotations]{.hl}, classified by *where* the offending descendant was inserted:

<div class="sub-item-enum">

1. [LL]{.hl} — inserted into the **left** subtree of the **left** child &rarr; single right rotation.
2. [RR]{.hl} — inserted into the **right** subtree of the **right** child &rarr; single left rotation.
3. [LR]{.hl} — inserted into the **right** subtree of the **left** child &rarr; left rotation, then right rotation (double).
4. [RL]{.hl} — inserted into the **left** subtree of the **right** child &rarr; right rotation, then left rotation (double).

</div>

- LL and RR are *single* rotations; LR and RL are *double* rotations. Only the deepest unbalanced node needs to be fixed.

---
layout: prism
heading: "AVL Rotations: LL and RR"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<p style="text-align:center; font-weight:bold; margin-bottom:0.4rem;">LL &mdash; single right rotation</p>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w12/dsa-w12-image2.jpg" class="tikz-fig" style="width: 100%;" />

</div>
<div>

<p style="text-align:center; font-weight:bold; margin-bottom:0.4rem;">RR &mdash; single left rotation</p>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w12/dsa-w12-image5.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

<div style="margin-top: 1.5rem;"></div>

- A single rotation lifts the middle key to the root of the subtree; the previous root becomes a child, and one subtree is reattached on the other side.

---
layout: prism
heading: "AVL Rotations: LR and RL"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<p style="text-align:center; font-weight:bold; margin-bottom:0.4rem;">LR &mdash; left then right rotation</p>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w12/dsa-w12-image3.jpg" class="tikz-fig" style="width: 100%;" />

</div>
<div>

<p style="text-align:center; font-weight:bold; margin-bottom:0.4rem;">RL &mdash; right then left rotation</p>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w12/dsa-w12-image4.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

<div style="margin-top: 1.2rem;"></div>

- A double rotation first rotates the *lower* pair so the case reduces to LL or RR, then applies the corresponding single rotation. The grandchild $z$ ends up at the root of the subtree.

---
layout: prism
heading: "DIY: AVL Insertion with Rotations"
---

<CppRunner>

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct Node {
    int key, height;
    Node *left, *right;
    Node(int k) : key(k), height(1), left(nullptr), right(nullptr) {}
};

int  h(Node* n)   { return n ? n->height : 0; }
int  bf(Node* n)  { return n ? h(n->left) - h(n->right) : 0; }
void upd(Node* n) { n->height = 1 + max(h(n->left), h(n->right)); }

Node* rotateRight(Node* y) {   // fixes LL
    Node* x = y->left;
    y->left = x->right;
    x->right = y;
    upd(y); upd(x);
    return x;
}
Node* rotateLeft(Node* x) {    // fixes RR
    Node* y = x->right;
    x->right = y->left;
    y->left = x;
    upd(x); upd(y);
    return y;
}

Node* insert(Node* node, int key) {
    if (!node) return new Node(key);
    if (key < node->key)      node->left  = insert(node->left, key);
    else if (key > node->key) node->right = insert(node->right, key);
    else return node;                       // no duplicates

    upd(node);
    int b = bf(node);
    if (b > 1 && key < node->left->key)  return rotateRight(node);          // LL
    if (b < -1 && key > node->right->key) return rotateLeft(node);          // RR
    if (b > 1 && key > node->left->key) {                                   // LR
        node->left = rotateLeft(node->left);
        return rotateRight(node);
    }
    if (b < -1 && key < node->right->key) {                                 // RL
        node->right = rotateRight(node->right);
        return rotateLeft(node);
    }
    return node;
}

void inorder(Node* n) { if (!n) return; inorder(n->left); cout << n->key << " "; inorder(n->right); }

int main() {
    Node* root = nullptr;
    int keys[] = {10, 20, 30, 40, 50, 25};   // triggers RR, RR, RL
    for (int k : keys) root = insert(root, k);

    cout << "In-order: "; inorder(root); cout << "\n";
    cout << "Root  = " << root->key << "\n";
    cout << "Height = " << root->height << " (balanced)\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: Red-Black Trees"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [red-black tree]{.hl} is another balanced binary search tree. Each `null` link that has no child is treated as a black [leaf node]{.hl}.

- Every node is colored red or black so that the following [properties]{.hl} always hold:

<div class="sub-item-enum">

1. The [root]{.hl} is black.
2. Every leaf (`null`) is black.
3. On any root-to-leaf path, no two [red]{.hl} nodes appear consecutively (a red node cannot have a red child).
4. Every root-to-leaf path passes through the same number of [black]{.hl} nodes (equal *black-height*).

</div>

- These constraints keep the longest path at most twice the shortest, guaranteeing $O(\log N)$ height.

---
layout: prism
heading: "Red-Black Trees: Insertion Repair"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A new node $x$ is inserted colored [red]{.hl}. If its parent $p$ is black, no property is broken. The problem is only when $p$ is also red — two consecutive red nodes violate property 3.

- Since the tree was valid before, $p$'s parent $p_2$ (the grandparent) must be [black]{.hl}.

- The repair splits into two cases based on the color of $p$'s sibling $s$ (the [uncle]{.hl} of $x$):

<div class="sub-item-enum">

1. [Case 1]{.hl}: $s$ is **red** &rarr; recolor only.
2. [Case 2]{.hl}: $s$ is **black** &rarr; rotate. *Case 2-1*: $x$ is the right child of $p$. *Case 2-2*: $x$ is the left child of $p$.

</div>

---
layout: prism
heading: "RB Repair: Case 1 (Recolor)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- When the uncle $s$ is [red]{.hl}, recolor $p$ and $s$ from red to [black]{.hl}, and recolor the grandparent $p_2$ from black to [red]{.hl}.

- This preserves the black-height on every path while pushing the possible violation *up* the tree:

<div class="sub-item-enum">

1. If $p_2$ is now the root, recolor it back to black &mdash; done.
2. Otherwise inspect $p_2$'s parent $p_3$: if $p_3$ is black we are finished; if $p_3$ is red, repeat the repair recursively with $p_2$ playing the role of $x$.

</div>

- Case 1 performs no rotation; it only recolors and may cascade toward the root.

---
layout: prism
heading: "RB Repair: Case 2 (Rotations)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- When the uncle $s$ is [black]{.hl}, we fix the double-red with rotations at $p$ and $p_2$:

<div class="sub-item-enum">

1. [Case 2-1]{.hl} ($x$ is the right child of $p$): [left-rotate]{.hl} around $p$. This straightens the "zig-zag" and reduces the situation to Case 2-2.
2. [Case 2-2]{.hl} ($x$ is the left child of $p$): [right-rotate]{.hl} around the grandparent $p_2$, then [swap the colors]{.hl} of $p$ and $p_2$.

</div>

- After Case 2 the subtree root is black with two red children, so the violation is resolved locally &mdash; no cascade is needed. (The mirror image applies on the right side.)

---
layout: prism
heading: "DIY: Red-Black Tree Insertion"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

enum Color { RED, BLACK };
struct Node {
    int key; Color color;
    Node *left, *right, *parent;
    Node(int k) : key(k), color(RED), left(nullptr), right(nullptr), parent(nullptr) {}
};

Node* root = nullptr;
bool isRed(Node* n) { return n && n->color == RED; }   // null is black

void rotateLeft(Node* x) {
    Node* y = x->right;
    x->right = y->left;
    if (y->left) y->left->parent = x;
    y->parent = x->parent;
    if (!x->parent) root = y;
    else if (x == x->parent->left) x->parent->left = y;
    else x->parent->right = y;
    y->left = x; x->parent = y;
}
void rotateRight(Node* x) {
    Node* y = x->left;
    x->left = y->right;
    if (y->right) y->right->parent = x;
    y->parent = x->parent;
    if (!x->parent) root = y;
    else if (x == x->parent->right) x->parent->right = y;
    else x->parent->left = y;
    y->right = x; x->parent = y;
}

void fixup(Node* z) {
    while (isRed(z->parent)) {
        Node* p = z->parent;
        Node* g = p->parent;
        if (p == g->left) {
            Node* s = g->right;                 // uncle
            if (isRed(s)) {                      // Case 1: recolor
                p->color = s->color = BLACK; g->color = RED; z = g;
            } else {
                if (z == p->right) {             // Case 2-1: left-rotate
                    z = p; rotateLeft(z); p = z->parent;
                }
                p->color = BLACK; g->color = RED; // Case 2-2: right-rotate + recolor
                rotateRight(g);
            }
        } else {                                 // mirror image
            Node* s = g->left;
            if (isRed(s)) {
                p->color = s->color = BLACK; g->color = RED; z = g;
            } else {
                if (z == p->left) { z = p; rotateRight(z); p = z->parent; }
                p->color = BLACK; g->color = RED;
                rotateLeft(g);
            }
        }
    }
    root->color = BLACK;
}

void insert(int key) {
    Node* z = new Node(key);
    Node* y = nullptr; Node* x = root;
    while (x) { y = x; x = (key < x->key) ? x->left : x->right; }
    z->parent = y;
    if (!y) root = z;
    else if (key < y->key) y->left = z; else y->right = z;
    fixup(z);
}

void inorder(Node* n) {
    if (!n) return;
    inorder(n->left);
    cout << n->key << (n->color == RED ? "(R) " : "(B) ");
    inorder(n->right);
}
int blackHeight(Node* n) { if (!n) return 1; return blackHeight(n->left) + (n->color == BLACK ? 1 : 0); }

int main() {
    int keys[] = {10, 20, 30, 15, 25, 5, 1};
    for (int k : keys) insert(k);
    cout << "In-order: "; inorder(root); cout << "\n";
    cout << "Root = " << root->key << " (black)\n";
    cout << "Black-height = " << blackHeight(root) << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Recap: B-Trees"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A node of a [B-tree]{.hl} stores up to $k$ keys in sorted order. A node holding $k$ keys has $k+1$ children.

- Let the subtrees be $T_0, T_1, T_2, \ldots$ Every key in subtree $T_i$ is [greater than]{.hl} $\text{key}_{i-1}$ and [less than]{.hl} $\text{key}_i$.

- This multi-way branching keeps the tree shallow, which is ideal for disk-based storage.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w12/dsa-w12-image6.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Balanced vs. Unbalanced Height"
---

<CppRunner>

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct Node { int key, height; Node *left, *right;
    Node(int k) : key(k), height(1), left(nullptr), right(nullptr) {} };

int  h(Node* n)   { return n ? n->height : 0; }
int  bf(Node* n)  { return n ? h(n->left) - h(n->right) : 0; }
void upd(Node* n) { n->height = 1 + max(h(n->left), h(n->right)); }
Node* rotR(Node* y){ Node* x=y->left;  y->left=x->right;  x->right=y; upd(y); upd(x); return x; }
Node* rotL(Node* x){ Node* y=x->right; x->right=y->left; y->left=x;  upd(x); upd(y); return y; }

Node* bstInsert(Node* n, int k) {              // plain BST (no balancing)
    if (!n) return new Node(k);
    if (k < n->key) n->left = bstInsert(n->left, k);
    else            n->right = bstInsert(n->right, k);
    upd(n);
    return n;
}
Node* avlInsert(Node* n, int k) {              // self-balancing
    if (!n) return new Node(k);
    if (k < n->key) n->left = avlInsert(n->left, k);
    else if (k > n->key) n->right = avlInsert(n->right, k);
    else return n;
    upd(n);
    int b = bf(n);
    if (b > 1 && k < n->left->key)  return rotR(n);
    if (b < -1 && k > n->right->key) return rotL(n);
    if (b > 1 && k > n->left->key)  { n->left = rotL(n->left); return rotR(n); }
    if (b < -1 && k < n->right->key){ n->right = rotR(n->right); return rotL(n); }
    return n;
}

int main() {
    Node *bst = nullptr, *avl = nullptr;
    for (int k = 1; k <= 15; k++) {            // already-sorted input: the worst case for a BST
        bst = bstInsert(bst, k);
        avl = avlInsert(avl, k);
    }
    cout << "Inserting 1..15 in sorted order\n";
    cout << "Plain BST height = " << h(bst) << " (degenerates to a linked list)\n";
    cout << "AVL tree  height = " << h(avl) << " (stays ~log2(15))\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Hash Tables: The Idea"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- A [hash table]{.hl} is a data structure that pushes storage and search to their *extreme* efficiency — ideally [constant time]{.hl} for both.

- A search tree locates an element by [comparing]{.hl} it against keys along a root-to-leaf path. To reach true constant time, we must *avoid comparisons between elements altogether*.

- In a hash table, an element's [position is decided directly by its value]{.hl} — not by comparing it against other elements.

<div class="theorem-box">
<div class="theorem-box-title">Key idea</div>
<div class="theorem-box-body">

The value itself is fed into a [hash function]{.hl} $h$, which computes the [address]{.hl} where the element belongs. No traversal, no comparison chain.

</div>
</div>

---
layout: prism
heading: "Hash Tables: Direct Addressing by Value"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- To store an element, compute its hash value with $h$. For a table of size $m$, $h$ returns an address in $\{0, 1, \ldots, m-1\}$.

- The simplest choice: use the [remainder]{.hl} of the value divided by $m$.

  - $h(x) = x \bmod 13$

- Searching works the same way — recompute $h(x)$ and look at that single slot.

</div>
<div>

<p style="text-align:center; margin-bottom:0.4rem;">Input: 25, 13, 16, 15, 7 &nbsp;($m = 13$)</p>

<table class="htab">
<tr><td class="idx">0</td><td>13</td></tr>
<tr><td class="idx">1</td><td></td></tr>
<tr><td class="idx">2</td><td>15</td></tr>
<tr><td class="idx">3</td><td>16</td></tr>
<tr><td class="idx">4</td><td></td></tr>
<tr><td class="idx">5</td><td></td></tr>
<tr><td class="idx">6</td><td></td></tr>
<tr><td class="idx">7</td><td>7</td></tr>
<tr><td class="idx">8</td><td></td></tr>
<tr><td class="idx">9</td><td></td></tr>
<tr><td class="idx">10</td><td></td></tr>
<tr><td class="idx">11</td><td></td></tr>
<tr><td class="idx">12</td><td>25</td></tr>
</table>

</div>
</div>

---
layout: prism
heading: "Hash Tables: Load Factor"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.7em;
}
</style>

- Every insertion and search is a single hash computation, so both are handled in [constant time]{.hl} on average.

- The fraction of the table that is occupied strongly affects performance. This ratio is the [load factor]{.hl} $\alpha$.

  - For the previous example, $\alpha = 5/13$.

- Hash tables reach their addresses in one step — but there is a [crucial obstacle]{.hl}: two different values may map to the *same* address. Handling that is the central problem of the rest of this lecture.

---
layout: prism
heading: "Hash Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- A [hash function]{.hl} takes a key value as input and returns an address in the hash table.

- A good hash function has two [properties]{.hl}:

<div class="sub-item-enum">

1. Input elements should be spread [evenly]{.hl} across the whole table.
2. The computation should be [simple]{.hl}.

</div>

- Satisfying the first property well is what keeps the probability of two distinct elements [colliding]{.hl} at one address low.

- In practice, designing a function that satisfies the first property almost never requires an excessively complicated calculation.

---
layout: prism
heading: "Hash Functions: The Division Method"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- The [division method]{.hl} uses the simplest possible form:

<div class="sub-item">

$$ h(x) = x \bmod m $$

</div>

- Here $m$ is the [table size]{.hl}. Since valid addresses are $0, 1, \ldots, m-1$, taking the remainder modulo $m$ is a natural fit.

- Choose $m$ to be a [prime number]{.hl} that is *not* close to a power of 2. Powers of 2 make $h$ depend only on the low-order bits.

- Using [all the bits]{.hl} of the input tends to give a probabilistically better distribution.

---
layout: prism
heading: "Hash Functions: The Multiplication Method"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The division method *shrinks* a large number into the table-size range. The [multiplication method]{.hl} instead maps the input into $(0,1)$ and then expands it to the table size.

  - It needs a constant $A$ with $0 < A < 1$ that determines the behavior of the function.

- For an element $x$, multiply by $A$, keep only the [fractional part]{.hl}, then multiply by $m$ and take the integer part:

<div class="sub-item">

$$ h(x) = \bigl\lfloor\, m\,(x A \bmod 1)\,\bigr\rfloor $$

</div>

- The table size $m$ can be *anything* here; instead the value of $A$ strongly influences the distribution. A known good choice is $A = (\sqrt{5} - 1)/2 \approx 0.618$.

---
layout: prism
heading: "DIY: Division vs. Multiplication Hashing"
---

<CppRunner>

```cpp
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int divisionHash(int x, int m) {          // h(x) = x mod m
    return x % m;
}
int multiplicationHash(int x, int m) {    // h(x) = floor(m * (x*A mod 1))
    double A = (sqrt(5.0) - 1) / 2;       // ~0.6180339887 (golden ratio - 1)
    double xa = x * A;
    double frac = xa - floor(xa);         // keep only the fractional part
    return (int)(m * frac);
}

int main() {
    int m = 13;
    vector<int> keys = {25, 13, 16, 15, 7, 28, 31, 20, 1, 38};
    cout << "key   division(mod 13)   multiplication(A=(sqrt5-1)/2)\n";
    for (int x : keys)
        cout << " " << x << "\t      " << divisionHash(x, m)
             << "\t\t   " << multiplicationHash(x, m) << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Collision"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Suppose 28 is inserted next. With $h(x)=x \bmod 13$, $h(28)=2$ — but address 2 already holds 15.

- When two or more elements are assigned to the *same* address, we have a [collision]{.hl}.

- There are two broad families of [collision resolution]{.hl}:

<div class="sub-item-enum">

1. Resolve using space [outside]{.hl} the table (chaining).
2. Resolve [within]{.hl} the table itself (open addressing).

</div>

</div>
<div>

<p style="text-align:center; margin-bottom:0.4rem;">28 collides at address 2</p>

<table class="htab">
<tr><td class="idx">0</td><td>13</td></tr>
<tr><td class="idx">1</td><td></td></tr>
<tr><td class="idx">2</td><td class="hit">15 &larr; 28?</td></tr>
<tr><td class="idx">3</td><td>16</td></tr>
<tr><td class="idx">4</td><td></td></tr>
<tr><td class="idx">5</td><td></td></tr>
<tr><td class="idx">6</td><td></td></tr>
<tr><td class="idx">7</td><td>7</td></tr>
<tr><td class="idx">8</td><td></td></tr>
<tr><td class="idx">9</td><td></td></tr>
<tr><td class="idx">10</td><td></td></tr>
<tr><td class="idx">11</td><td></td></tr>
<tr><td class="idx">12</td><td>25</td></tr>
</table>

</div>
</div>

---
layout: prism
heading: "Collision Resolution: Chaining"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- In [chaining]{.hl} (separate chaining), all elements that hash to the same address are hung on a single [linked list]{.hl} at that slot.

- A big advantage: it still works even when the [load factor exceeds 1]{.hl}, because each bucket can grow without bound.

- Search cost is proportional to the length of the chain at $h(x)$, so keeping chains short (low $\alpha$) keeps it fast.

</div>
<div>

<p style="text-align:center; margin-bottom:0.4rem; font-size:0.9rem;">$h(x)=x \bmod 13$</p>

<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; line-height: 1.5;">

`0 -> 39 -> 13`
`1 -> 40`
`2 -> (empty)`
`3 -> 94 -> 3 -> 42 -> 55`
`4 -> 43`
`5 -> 44 -> 70`
`6 -> (empty)`
`7 -> (empty)`
`8 -> 86 -> 47`
`9 -> 74`
`10 -> (empty)`
`11 -> 76`
`12 -> (empty)`

</div>

</div>
</div>

---
layout: prism
heading: "DIY: Separate Chaining"
---

<CppRunner>

```cpp
#include <iostream>
#include <list>
#include <vector>
using namespace std;

struct HashTable {
    int m;
    vector<list<int>> buckets;
    HashTable(int size) : m(size), buckets(size) {}

    int h(int x) { return x % m; }                     // division method
    void insert(int x) { buckets[h(x)].push_back(x); } // append to the chain
    bool contains(int x) {
        for (int v : buckets[h(x)]) if (v == x) return true;
        return false;
    }
    void print() {
        for (int i = 0; i < m; i++) {
            cout << i << " -> ";
            for (int v : buckets[i]) cout << v << " -> ";
            cout << "NULL\n";
        }
    }
};

int main() {
    HashTable t(13);
    int keys[] = {39, 13, 40, 94, 3, 42, 55, 43, 44, 70, 86, 47, 74, 76};
    for (int k : keys) t.insert(k);
    t.print();
    cout << "contains(42)? " << (t.contains(42) ? "yes" : "no") << "\n";
    cout << "contains(99)? " << (t.contains(99) ? "yes" : "no") << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Collision Resolution: Open Addressing (1/5)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [Open addressing]{.hl} allows *no* extra space. When a collision happens, it must be resolved somewhere inside the given table.

  - Therefore the load factor can [never exceed 1]{.hl}.
  - There is no guarantee that every element sits at the address matching its own hash value.

- If the computed address is already taken by another element, we find a new slot using the [next probing rule]{.hl}.

- Several rules exist for choosing the next address. The main ones are [linear probing]{.hl}, [quadratic probing]{.hl}, and [double hashing]{.hl}.

---
layout: prism
heading: "Open Addressing (2/5): Linear Probing"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [Linear probing]{.hl} is the simplest scheme: on a collision, check the slot immediately *after* it.

- The $i$-th probe is $i$ slots away from $h(x)$:

<div class="sub-item">

$$ h_i(x) = (h(x) + i) \bmod m,\quad i = 0, 1, 2, \ldots $$

</div>

- E.g. inserting 28 ($h=2$) skips 2, 3, and lands at 4; 20 ($h=7$) lands at 8; 38 ($h=12$) wraps around to 6.

</div>
<div>

<p style="text-align:center; margin-bottom:0.4rem; font-size:0.85rem;">Input: 25,13,16,15,7,28,31,20,1,38</p>

<table class="htab">
<tr><td class="idx">0</td><td>13</td></tr>
<tr><td class="idx">1</td><td>1</td></tr>
<tr><td class="idx">2</td><td>15</td></tr>
<tr><td class="idx">3</td><td>16</td></tr>
<tr><td class="idx">4</td><td class="hit">28</td></tr>
<tr><td class="idx">5</td><td>31</td></tr>
<tr><td class="idx">6</td><td class="hit">38</td></tr>
<tr><td class="idx">7</td><td>7</td></tr>
<tr><td class="idx">8</td><td class="hit">20</td></tr>
<tr><td class="idx">9</td><td></td></tr>
<tr><td class="idx">10</td><td></td></tr>
<tr><td class="idx">11</td><td></td></tr>
<tr><td class="idx">12</td><td>25</td></tr>
</table>

</div>
</div>

---
layout: prism
heading: "Open Addressing (3/5): Quadratic Probing"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Linear probing degrades badly when elements pile up in one region. This effect is called [primary clustering]{.hl}.

- [Quadratic probing]{.hl} widens the stride using a quadratic function instead of stepping to the very next slot:

<div class="sub-item">

$$ h_i(x) = (h(x) + c_1 i^2 + c_2 i) \bmod m,\quad i = 0, 1, 2, \ldots $$

</div>

- Increasing the constants $c_1$ and $c_2$ lets a probe escape a primary cluster quickly.

- However, if many elements share the *same initial* hash value, they still probe in the [same order]{.hl} and become inefficient — this is [secondary clustering]{.hl}.

---
layout: prism
heading: "Open Addressing (4/5): Double Hashing"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [Double hashing]{.hl} combines *two* hash functions:

<div class="sub-item">

$$ h_i(x) = \bigl(h(x) + i \cdot f(x)\bigr) \bmod m,\quad i = 0, 1, 2, \ldots $$

where $h(x)$ and $f(x)$ are two different hash functions.

</div>

- Even when a collision occurs (i.e. two elements share the same $h(x)$), the chance that they also share the same $f(x)$ is very small, so they jump by [different strides]{.hl} — resolving secondary clustering.

- A common choice for the two functions is:

<div class="sub-item-enum">

1. $h(x) = x \bmod m$
2. $f(x) = 1 + (x \bmod m')$, where $m'$ is a prime slightly smaller than $m$.

</div>

---
layout: prism
heading: "DIY: Linear Probing vs. Double Hashing"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int EMPTY = -1;

// -------- linear probing:  h_i(x) = (x mod m + i) mod m --------
vector<int> linearProbe(const vector<int>& keys, int m) {
    vector<int> a(m, EMPTY);
    for (int x : keys) {
        int i = 0;
        while (a[(x % m + i) % m] != EMPTY) i++;
        a[(x % m + i) % m] = x;
    }
    return a;
}

// -------- double hashing:  h_i(x) = (x mod m + i*(1 + x mod m')) mod m --------
vector<int> doubleHash(const vector<int>& keys, int m, int mp) {
    vector<int> a(m, EMPTY);
    for (int x : keys) {
        int step = 1 + (x % mp);
        int i = 0;
        while (a[(x % m + i * step) % m] != EMPTY) i++;
        a[(x % m + i * step) % m] = x;
    }
    return a;
}

void show(const string& name, const vector<int>& a) {
    cout << name << ":\n";
    for (int i = 0; i < (int)a.size(); i++)
        cout << "  " << i << ": " << (a[i] == EMPTY ? "." : to_string(a[i])) << "\n";
}

int main() {
    vector<int> keys = {25, 13, 16, 15, 7, 28, 31, 20, 1, 38};
    show("Linear probing (m=13)", linearProbe(keys, 13));
    show("Double hashing (m=13, m'=11)", doubleHash(keys, 13, 11));
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Open Addressing (5/5): Rehashing & Deletion"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Open addressing degrades sharply as the load factor rises. Set a [threshold]{.hl}; once it is crossed, grow the table (typically [double]{.hl} it) and [rehash]{.hl} every element.

- Deletion needs care: you cannot simply empty a slot, or a later probe might stop early and miss elements past it.

- Instead, mark the slot as [DELETED]{.hl} (lazy deletion) so probe sequences still pass through it.

</div>
<div>

<p style="text-align:center; margin-bottom:0.4rem; font-size:0.85rem;">Delete 1 &rarr; mark slot 1 DELETED</p>

<table class="htab">
<tr><td class="idx">0</td><td>13</td></tr>
<tr><td class="idx">1</td><td class="del">DELETED</td></tr>
<tr><td class="idx">2</td><td>15</td></tr>
<tr><td class="idx">3</td><td>16</td></tr>
<tr><td class="idx">4</td><td>28</td></tr>
<tr><td class="idx">5</td><td>31</td></tr>
<tr><td class="idx">6</td><td>38</td></tr>
<tr><td class="idx">7</td><td>7</td></tr>
<tr><td class="idx">8</td><td>20</td></tr>
<tr><td class="idx">9</td><td></td></tr>
<tr><td class="idx">10</td><td></td></tr>
<tr><td class="idx">11</td><td></td></tr>
<tr><td class="idx">12</td><td>25</td></tr>
</table>

</div>
</div>

---
layout: prism
heading: "C++ unordered_map"
---

<CppRunner>

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, int> hash;   // hash table; note: std::map is a balanced BST

    cout << hash.empty() << endl;       // 1 (true) -- currently empty

    hash.insert(make_pair("Korea", 82));
    hash["USA"] = 1;
    hash.insert({"Japan", 81});

    cout << hash.size() << endl;         // 3
    cout << hash.count("Korea") << endl; // 1

    // iteration order is unspecified for unordered_map
    for (pair<string, int> element : hash)
        cout << "Key: " << element.first << " Value: " << element.second << endl;

    // find() returns an iterator, or end() if the key is absent
    if (hash.find("USA") != hash.end())
        hash.erase("USA");

    cout << hash.size() << endl;         // 2
    for (auto element : hash)
        cout << "Key: " << element.first << " Value: " << element.second << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Problem: The Runner Who Couldn't Finish (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Many runners take part in a marathon, and [all but one]{.hl} finish the race.

- Given an array `participant` of all runners' names and an array `completion` of the finishers, return the name of the [single runner who did not finish]{.hl}.

- Constraints:

<div class="sub-item-enum">

1. $1 \le |\texttt{participant}| \le 100{,}000$, and $|\texttt{completion}| = |\texttt{participant}| - 1$.
2. Names are lowercase letters, length 1 to 20. There may be [duplicate names]{.hl}.

</div>

- Idea: count each participant in a hash map, decrement for each finisher, and the leftover with a positive count is the answer. (Duplicates make plain set comparison fail — counting fixes it.)

---
layout: prism
heading: "Problem: The Runner Who Couldn't Finish (2/2)"
---

<CppRunner>

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer;
    unordered_map<string, int> hash;

    for (auto& player : participant) {          // count each participant (handles duplicates)
        if (hash.find(player) == hash.end()) hash.insert(make_pair(player, 1));
        else hash[player]++;
    }
    for (auto& player : completion)             // one who finished -> decrement
        hash[player]--;

    for (auto& player : participant)            // the one left with count > 0
        if (hash[player] > 0) { answer = player; break; }

    return answer;
}

int main() {
    cout << solution({"leo", "kiki", "eden"}, {"eden", "kiki"}) << "\n";                       // leo
    cout << solution({"marina","josipa","nikola","vinko","filipa"},
                     {"josipa","filipa","marina","nikola"}) << "\n";                          // vinko
    cout << solution({"mislav","stanko","mislav","ana"}, {"stanko","ana","mislav"}) << "\n";  // mislav
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Problem: Phone Book (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Check whether, among a list of phone numbers, any number is a [prefix]{.hl} of another.

  - e.g. rescue line `119` is a prefix of `9767 4223`'s neighbor `1195524421`.

- Given `phone_book`, return `false` if some number is a prefix of another, otherwise `true`.

- Constraints:

<div class="sub-item-enum">

1. $1 \le |\texttt{phone\_book}| \le 1{,}000{,}000$; each number has length 1 to 20.
2. No duplicate numbers appear.

</div>

- Idea: put every number in a hash map, then for each number test every one of its [proper prefixes]{.hl} — if a prefix is itself a stored number, return `false`.

---
layout: prism
heading: "Problem: Phone Book (2/2)"
---

<CppRunner>

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

bool solution(vector<string> phone_book) {
    unordered_map<string, int> hash;

    for (int i = 0; i < (int)phone_book.size(); i++)
        hash[phone_book[i]]++;                          // register every number

    for (int i = 0; i < (int)phone_book.size(); i++) {
        for (int j = 1; j < (int)phone_book[i].size(); j++) {
            // is a proper prefix of this number itself a stored number?
            if (hash.find(phone_book[i].substr(0, j)) != hash.end())
                return false;
        }
    }
    return true;
}

int main() {
    cout << boolalpha;
    cout << solution({"119", "97674223", "1195524421"}) << "\n";   // false
    cout << solution({"123", "456", "789"}) << "\n";               // true
    cout << solution({"12", "123", "1235", "567", "88"}) << "\n";  // false
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Problem: Outfits (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- A spy likes to wear a *different combination* of clothes every day. Each clothing item has a [name]{.hl} and a [category]{.hl} (e.g. headgear, eyewear, top).

- Rules: at most [one item per category]{.hl} may be worn, and at least [one item total]{.hl} must be worn. Count the number of distinct outfit combinations.

- Given a 2-D array `clothes` where each row is `[name, category]`, return the number of ways.

- Idea: group items by category. If a category has $n_i$ items, there are $n_i + 1$ choices (pick one, or wear none of that category). Multiply across all categories, then [subtract 1]{.hl} to remove the "wear nothing at all" case.

<div class="sub-item">

$$ \text{answer} = \Bigl(\prod_i (n_i + 1)\Bigr) - 1 $$

</div>

---
layout: prism
heading: "Problem: Outfits (2/2)"
---

<CppRunner>

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, vector<string>> hash;   // category -> list of item names

    for (int i = 0; i < (int)clothes.size(); i++)
        hash[clothes[i][1]].push_back(clothes[i][0]);

    for (auto& element : hash)
        answer *= element.second.size() + 1;       // pick one item, or none, in this category

    return answer - 1;                              // remove the "wear nothing" case
}

int main() {
    cout << solution({{"yellow_hat","headgear"},
                      {"blue_sunglasses","eyewear"},
                      {"green_turban","headgear"}}) << "\n";   // 5
    cout << solution({{"crow_mask","face"},
                      {"blue_sunglasses","face"},
                      {"smoky_makeup","face"}}) << "\n";       // 3
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY_W12"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.7em;
}
</style>

- In [double hashing]{.hl} (open addressing), the two hash functions are commonly chosen as:

<div class="sub-item-enum">

1. $h(x) = x \bmod m$
2. $f(x) = 1 + (x \bmod m')$, where $m'$ is a prime slightly smaller than $m$.

</div>

- [Think about]{.hl} *why* this design is effective. (Hint: what would go wrong if $f(x)$ could return 0, and why should the two moduli differ?)

- Also, in double hashing there is something to be careful about when the second hash value is [compared against the table size]{.hl}. Think about what that is.

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
