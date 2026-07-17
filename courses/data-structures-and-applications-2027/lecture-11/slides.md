---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 11
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-11-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 11: Search Trees — BST, AVL, Red-Black, and B-Trees</p>

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
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.6rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Foundations</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Records, Indices, and Keys</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0.4rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Binary Search Trees (search, insert, delete, traversal)</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0.4rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Parametric Search</span></p>
    <p style="margin: 0.6rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Balanced Search Trees</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">AVL Trees (definition and repair: LL, RR, LR, RL)</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0.4rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Red-Black Trees (definition and repair)</span></p>
    <p style="margin: 0.6rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">External Search Trees</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">B-Trees (search, insert, delete)</span></p>
  </div>

</div>

---
layout: prism
heading: "Records, Indices, and Keys"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A [record]{.hl} holds the information about some entity.
  - A *person* record might contain a student ID, name, address, mobile number, and so on. Each such piece of information is a [field]{.hl}.

- An [index]{.hl} is used to *search* for the records of entities.
  - We *could* store every record inside the index, but then the index would be no different from the database itself.
  - Instead, an index is built from a field that can *represent* each record — for a person record, the student ID can serve as that representative field.

- A field that [distinguishes]{.hl} each record without duplicating another is used in the index; this is called a [key]{.hl}.
  - A key may consist of a single field or of several fields together.

---
layout: prism
heading: "Binary Search Trees"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [binary search tree]{.hl} (BST) has the following properties:
  - Each node stores a single key, and all keys are *distinct*.
  - A [root]{.hl} node sits at the top level, and every node has *at most two* children.
  - For any node, its key is *greater* than every key below it on the left, and *smaller* than every key below it on the right.

</div>
<div>

<div style="height: 1rem;"></div>

<svg viewBox="0 0 300 230" style="width: 100%; background:#fff; border-radius:8px;" font-family="monospace" font-size="13">
  <line x1="150" y1="30" x2="90"  y2="80"  stroke="#333"/>
  <line x1="150" y1="30" x2="210" y2="80"  stroke="#333"/>
  <line x1="90"  y1="80" x2="55"  y2="140" stroke="#333"/>
  <line x1="90"  y1="80" x2="125" y2="140" stroke="#333"/>
  <line x1="210" y1="80" x2="175" y2="140" stroke="#333"/>
  <line x1="210" y1="80" x2="245" y2="140" stroke="#333"/>
  <g stroke="#5c60a8" fill="#fff">
    <circle cx="150" cy="30"  r="18"/>
    <circle cx="90"  cy="80"  r="18"/>
    <circle cx="210" cy="80"  r="18"/>
    <circle cx="55"  cy="140" r="18"/>
    <circle cx="125" cy="140" r="18"/>
    <circle cx="175" cy="140" r="18"/>
    <circle cx="245" cy="140" r="18"/>
  </g>
  <g fill="#333" text-anchor="middle" dominant-baseline="middle">
    <text x="150" y="30">30</text>
    <text x="90"  y="80">20</text>
    <text x="210" y="80">40</text>
    <text x="55"  y="140">10</text>
    <text x="125" y="140">25</text>
    <text x="175" y="140">35</text>
    <text x="245" y="140">45</text>
  </g>
</svg>

<p style="text-align:center; color:#9aa0a6; font-size:0.85rem; margin-top:0.3rem;">in-order keys: 10 20 25 30 35 40 45</p>

</div>
</div>

---
layout: prism
heading: "BST — Search"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- To search for a node with key $x$, return that node if it exists, and `null` otherwise.

- If needed, the record whose key is $x$ can be returned instead of the node.

- The search recurses left when $x$ is smaller than the current key and right when it is larger — each step discards one subtree.

</div>
<div>

<div style="height: 1rem;"></div>

```text
search(t, x):
  // t: root of the (sub)tree
  // x: key being searched for
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
heading: "BST — Insertion"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- To insert an element $x$, the tree must not already contain a node whose key is $x$.

- Finding the place for $x$ is exactly one *unsuccessful* search:
  - Search from the root until we reach a `null` link at some leaf position; $x$ is then hung in place of that `null`.

</div>
<div>

<div style="height: 1rem;"></div>

```text
insert(t, x):
  // t: root of the (sub)tree
  // x: key to insert
  if (t == null):
      hang a new node with key x
      under t's parent, then stop
  else if (x < t.item):
      insert(t.left, x)
  else:
      insert(t.right, x)
```

</div>
</div>

---
layout: prism
heading: "BST — Deletion"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Deleting a node $r$ is handled by three cases:

<div class="sub-item-enum">

1. **Case 1** — $r$ is a *leaf* node: simply discard $r$.
2. **Case 2** — $r$ has a *single* child: discard $r$, then link $r$'s parent directly to $r$'s child.
3. **Case 3** — $r$ has *two* children: find the node $s$ holding the minimum key in $r$'s right subtree, copy $s$ into $r$'s position, then delete $s$.

</div>

<div style="height: 0.6rem;"></div>

- In Case 3, the [in-order successor]{.hl} $s$ is guaranteed to have at most one child, so removing it reduces to Case 1 or Case 2.

---
layout: prism
heading: "DIY: BST Search, Insert, and Delete"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int key; Node *left, *right; Node(int k): key(k), left(nullptr), right(nullptr) {} };

Node* insert(Node* t, int x) {
    if (!t) return new Node(x);
    if (x < t->key)      t->left  = insert(t->left,  x);
    else if (x > t->key) t->right = insert(t->right, x);
    return t;                                   // duplicates ignored
}
Node* search(Node* t, int x) {
    if (!t || t->key == x) return t;
    return x < t->key ? search(t->left, x) : search(t->right, x);
}
Node* removeNode(Node* t, int x) {
    if (!t) return nullptr;
    if (x < t->key)      t->left  = removeNode(t->left,  x);
    else if (x > t->key) t->right = removeNode(t->right, x);
    else {                                      // found the node
        if (!t->left)  return t->right;         // Case 1 / Case 2
        if (!t->right) return t->left;
        Node* s = t->right;                     // Case 3: in-order successor
        while (s->left) s = s->left;
        t->key = s->key;
        t->right = removeNode(t->right, s->key);
    }
    return t;
}
void inorder(Node* t) { if (!t) return; inorder(t->left); cout << t->key << " "; inorder(t->right); }

int main() {
    Node* root = nullptr;
    for (int x : {30, 20, 40, 10, 25, 35, 45}) root = insert(root, x);
    cout << "inorder      : "; inorder(root); cout << "\n";
    cout << "search(25)   : " << (search(root, 25) ? "found" : "not found") << "\n";
    cout << "search(33)   : " << (search(root, 33) ? "found" : "not found") << "\n";
    root = removeNode(root, 30);                // Case 3
    cout << "after del 30 : "; inorder(root); cout << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Tree Traversals"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.0rem;">
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

<div style="height: 1.2rem;"></div>

<svg viewBox="0 0 300 220" style="width: 100%; background:#fff; border-radius:8px;" font-family="monospace" font-size="13">
  <line x1="150" y1="30" x2="95"  y2="80"  stroke="#333"/>
  <line x1="150" y1="30" x2="215" y2="80"  stroke="#333"/>
  <line x1="95"  y1="80" x2="55"  y2="130" stroke="#333"/>
  <line x1="95"  y1="80" x2="140" y2="130" stroke="#333"/>
  <line x1="140" y1="130" x2="140" y2="180" stroke="#333"/>
  <line x1="215" y1="80" x2="255" y2="130" stroke="#333"/>
  <g stroke="#5c60a8" fill="#fff">
    <circle cx="150" cy="30"  r="16"/>
    <circle cx="95"  cy="80"  r="16"/>
    <circle cx="215" cy="80"  r="16"/>
    <circle cx="55"  cy="130" r="16"/>
    <circle cx="140" cy="130" r="16"/>
    <circle cx="255" cy="130" r="16"/>
    <circle cx="140" cy="180" r="16"/>
  </g>
  <g fill="#333" text-anchor="middle" dominant-baseline="middle">
    <text x="150" y="30">A</text><text x="95" y="80">B</text><text x="215" y="80">C</text>
    <text x="55" y="130">D</text><text x="140" y="130">E</text><text x="255" y="130">F</text>
    <text x="140" y="180">G</text>
  </g>
</svg>

<div style="font-size:0.8rem; color:#555; margin-top:0.4rem; line-height:1.5;">
pre-order&nbsp;: A B D E G C F<br>
in-order&nbsp;&nbsp;: D B E G A C F<br>
post-order: D G E B F C A
</div>

</div>
</div>

---
layout: prism
heading: "DIY: Tree Traversals"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { char key; Node *left, *right; Node(char k): key(k), left(nullptr), right(nullptr) {} };

void preOrder (Node* r) { if (!r) return; cout << r->key << " "; preOrder(r->left);  preOrder(r->right); }
void inOrder  (Node* r) { if (!r) return; inOrder(r->left);  cout << r->key << " ";  inOrder(r->right); }
void postOrder(Node* r) { if (!r) return; postOrder(r->left); postOrder(r->right); cout << r->key << " "; }

int main() {
    //        A
    //      /   \
    //     B     C
    //    / \     \
    //   D   E     F
    //        \
    //         G
    Node* A = new Node('A'); Node* B = new Node('B'); Node* C = new Node('C');
    Node* D = new Node('D'); Node* E = new Node('E'); Node* F = new Node('F'); Node* G = new Node('G');
    A->left = B; A->right = C; B->left = D; B->right = E; E->right = G; C->right = F;

    cout << "pre-order  : "; preOrder(A);  cout << "\n";
    cout << "in-order   : "; inOrder(A);   cout << "\n";
    cout << "post-order : "; postOrder(A); cout << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Parametric Search"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [Parametric search]{.hl} solves an [optimization problem]{.hl} by turning it into a [decision problem]{.hl}.
  - Think of *weighing meat at a butcher shop*: we do not compute the answer directly, we keep asking "is this too much or too little?"

- It uses a function that makes a *yes/no* judgment, and repeatedly adjusts the candidate answer (the optimized value) based on that judgment.

- It is used to find the *minimum* or *maximum* value among those satisfying some condition.
  - budget: `27`
  - item prices: `[17, 28, 15, 30, 22, 19]`

---
layout: prism
heading: "DIY: Parametric Search"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> price = {17, 28, 15, 30, 22, 19};
    int budget = 27;
    sort(price.begin(), price.end());               // 15 17 19 22 28 30

    // Optimization: how many of the cheapest items can we buy within the budget?
    // Decision problem check(k): can we afford k items?  (monotone in k)
    auto check = [&](int k) {
        int cost = 0;
        for (int i = 0; i < k; i++) cost += price[i];
        return cost <= budget;
    };

    int lo = 0, hi = price.size(), ans = 0;         // binary search on the answer
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (check(mid)) { ans = mid; lo = mid + 1; } // feasible -> try more
        else              hi = mid - 1;              // infeasible -> try fewer
    }
    cout << "max items within budget " << budget << " = " << ans << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Balanced Search Trees"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A plain BST can degenerate: inserting keys in sorted order produces a "linked-list" shape of depth $O(n)$, making search $O(n)$.

- A [balanced search tree]{.hl} actively keeps its height near $\log n$, so search, insert, and delete stay $O(\log n)$.

<div style="text-align:center; margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image2.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: "AVL Trees"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- An [AVL tree]{.hl} is the classic example of a BST that always keeps itself *balanced*.
  - Invented by [Adelson-Velskii and Landis]{.hl} (hence "AVL").

- An AVL tree maintains the property that, for *any* node, the height difference between its left subtree and its right subtree is **never greater than 1**.

<div class="theorem-box">
<div class="theorem-box-title">AVL balance condition</div>
<div class="theorem-box-body">

For every node $t$: $\bigl|\,\text{height}(t.\text{left}) - \text{height}(t.\text{right})\,\bigr| \leq 1$.

</div>
</div>

---
layout: prism
heading: "AVL Trees — Examples"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.0rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image4.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.85rem;">An AVL tree</p>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image3.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.85rem;">Not an AVL tree</p>

</div>
</div>

<div style="font-size: 0.9rem; margin-top: 0.4rem;">

- On the right, the node with key `10` has a left subtree of height `0` and a right subtree of height `2` — a difference of `2`, which violates the balance condition.
- Each AVL node keeps the usual `key`, `left`, `right`, plus a `height` field for its subtree.

</div>

---
layout: prism
heading: "AVL Trees — Node Structure"
---

<div style="height: 1.5rem;"></div>

```cpp
class Node {
public:
    int   key;
    Node *left;
    Node *right;
    int   height;                       // height of the subtree rooted here
    Node(int k)
        : key(k), left(nullptr), right(nullptr), height(1) {}
};
```

<div style="height: 1rem;"></div>

- Compared with a BST node, the only addition is [`height`]{.hl}, which lets us compute each node's [balance factor]{.hl} = $\text{height(left)} - \text{height(right)}$ in $O(1)$.

---
layout: prism
heading: "AVL Repair — When Balance Breaks"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- After an *insertion* or *deletion*, an AVL tree may become unbalanced.

- Imbalance may appear at **one** node, or at **two or more** nodes.
  - It never appears at a place entirely unrelated to where the insertion/deletion happened.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image5.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">left: one unbalanced node &nbsp;·&nbsp; right: two unbalanced nodes</p>

</div>
</div>

---
layout: prism
heading: "AVL Repair — Left Rotation"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

- Repair starts from the *lowest* unbalanced subtree and works upward.

```text
leftRotate(t):  // t: pivot node
  RChild  <- t.right
  RLChild <- RChild.left
  RChild.left <- t
  t.right     <- RLChild
  RChild.height <-
    max(RChild.right.height,
        RChild.left.height) + 1
  t.height <-
    max(t.right.height,
        t.left.height) + 1
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image6.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">balanced after a left rotation</p>

</div>
</div>

---
layout: prism
heading: "AVL Repair — Left Rotation in C++"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<div style="height: 1rem;"></div>

```cpp
// left rotate subtree rooted at x
Node* leftRotate(Node *x) {
    Node *y  = x->right;
    Node *T2 = y->left;
    // perform rotation
    y->left  = x;
    x->right = T2;
    // update heights
    x->height =
        max(height(x->left),
            height(x->right)) + 1;
    y->height =
        max(height(y->left),
            height(y->right)) + 1;
    return y;                 // new subtree root
}
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image7.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">a single left rotation can fix two imbalances at once</p>

</div>
</div>

---
layout: prism
heading: "AVL Repair — Right Rotation"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

```text
rightRotate(t):  // t: pivot node
  LChild  <- t.left
  LRChild <- LChild.right
  LChild.right <- t
  t.left       <- LRChild
  LChild.height <-
    max(LChild.right.height,
        LChild.left.height) + 1
  t.height <-
    max(t.right.height,
        t.left.height) + 1
```

</div>
<div>

<div style="height: 1rem;"></div>

```cpp
// right rotate subtree rooted at y
Node* rightRotate(Node *y) {
    Node *x  = y->left;
    Node *T2 = x->right;
    x->right = y;            // perform rotation
    y->left  = T2;
    y->height =             // update heights
        max(height(y->left), height(y->right)) + 1;
    x->height =
        max(height(x->left), height(x->right)) + 1;
    return x;                // new subtree root
}
```

</div>
</div>

---
layout: prism
heading: "AVL Repair — When a Single Rotation Fails"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Depending on the subtree shape, a *single* rotation may **not** restore balance.

- If the [LR subtree]{.hl} is deeper than the [LL subtree]{.hl}, a right rotation just shifts the imbalance — the height gap persists.

- We must first identify the imbalance *type*, then apply the matching rule.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image9.jpg" class="tikz-fig" style="width: 100%;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image10.jpg" class="tikz-fig" style="width: 100%; margin-top: 0.4rem;" />

</div>
</div>

---
layout: prism
heading: "AVL Repair — LL Case"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- **LL** — the *left-left* grandchild subtree is the deepest.

- Perform a single [right rotation]{.hl} about the offending node $t$.

- One rotation is enough: the subtree height shrinks by one and balance is restored.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image11.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "AVL Repair — LR Case"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- **LR** — the *left child's right* grandchild subtree is the deepest.

- First [left-rotate]{.hl} about `t.left` to convert it into the LL shape, then [right-rotate]{.hl} about $t$.

- The two panels show the two internal shapes (*type I* and *type II*); both resolve identically.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image13.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "AVL Repair — RR Case"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- **RR** — the *right-right* grandchild subtree is the deepest.

- Perform a single [left rotation]{.hl} about $t$.

- This is the mirror image of the LL case; the same principle applies left-to-right reversed.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image14.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "AVL Repair — RL Case"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- **RL** — the *right child's left* grandchild subtree is the deepest.

- The mirror of the LR case: first [right-rotate]{.hl} about `t.right` to make it the RR shape, then [left-rotate]{.hl} about $t$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image15.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "AVL Repair — The Balancing Rule"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

```text
balanceAVL(t, type):
  // type in {LL, LR, RR, RL}
  switch type:
    case LL: rightRotate(t)
    case LR: leftRotate(t.left)
             balanceAVL(t, LL)
    case RR: leftRotate(t)
    case RL: rightRotate(t.right)
             balanceAVL(t, RR)
```

</div>
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- On [insertion]{.hl}, the imbalance comes from added depth; a single repair of the right type restores the height, so *no further* problem propagates.

- On [deletion]{.hl}, a repair may shorten a subtree and expose a *new* imbalance higher up, so repairs must continue [recursively]{.hl} up the tree.

</div>
</div>

---
layout: prism
heading: "AVL Repair — Insertion Cases in C++"
---

<div style="height: 1rem;"></div>

```cpp
int balance = height(node->left) - height(node->right);

// Left-Left
if (balance > 1 && key < node->left->key)
    return rightRotate(node);
// Right-Right
if (balance < -1 && key > node->right->key)
    return leftRotate(node);
// Left-Right
if (balance > 1 && key > node->left->key) {
    node->left = leftRotate(node->left);
    return rightRotate(node);
}
// Right-Left
if (balance < -1 && key < node->right->key) {
    node->right = rightRotate(node->right);
    return leftRotate(node);
}
```

---
layout: prism
heading: "AVL Repair — A Larger Worked Example"
---

<div class="grid grid-cols-2 gap-2" style="margin-top: 0.4rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image16.jpg" class="tikz-fig" style="width: 100%;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image17.jpg" class="tikz-fig" style="width: 100%;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image18.jpg" class="tikz-fig" style="width: 100%;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image19.jpg" class="tikz-fig" style="width: 100%;" />
</div>

<p style="text-align:center; color:#9aa0a6; font-size:0.82rem; margin-top:0.2rem;">successive rotations propagate up the tree until every node is balanced</p>

---
layout: prism
heading: "DIY: AVL Insertion with Rotations"
---

<CppRunner>

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct Node { int key, height; Node *left, *right;
              Node(int k): key(k), height(1), left(nullptr), right(nullptr) {} };

int  h(Node* n)   { return n ? n->height : 0; }
int  bf(Node* n)  { return n ? h(n->left) - h(n->right) : 0; }
void upd(Node* n) { n->height = 1 + max(h(n->left), h(n->right)); }

Node* rightRotate(Node* y) { Node* x = y->left;  Node* T = x->right; x->right = y; y->left  = T; upd(y); upd(x); return x; }
Node* leftRotate (Node* x) { Node* y = x->right; Node* T = y->left;  y->left  = x; x->right = T; upd(x); upd(y); return y; }

Node* insert(Node* node, int key) {
    if (!node) return new Node(key);
    if (key < node->key)      node->left  = insert(node->left,  key);
    else if (key > node->key) node->right = insert(node->right, key);
    else return node;
    upd(node);
    int b = bf(node);
    if (b >  1 && key < node->left->key)  return rightRotate(node);                       // LL
    if (b < -1 && key > node->right->key) return leftRotate(node);                        // RR
    if (b >  1 && key > node->left->key)  { node->left  = leftRotate(node->left);  return rightRotate(node); } // LR
    if (b < -1 && key < node->right->key) { node->right = rightRotate(node->right); return leftRotate(node); } // RL
    return node;
}
void inorder(Node* n) { if (!n) return; inorder(n->left);  cout << n->key << " "; inorder(n->right); }
void preorder(Node* n){ if (!n) return; cout << n->key << " "; preorder(n->left); preorder(n->right); }

int main() {
    Node* root = nullptr;
    for (int x : {40, 20, 10, 25, 30, 55, 70, 17, 35, 45, 50, 15}) root = insert(root, x);
    cout << "inorder  : "; inorder(root);  cout << "\n";
    cout << "preorder : "; preorder(root); cout << "\n";     // reveals the balanced shape
    cout << "root = " << root->key << ", height = " << root->height << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Red-Black Trees"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- A [red-black tree]{.hl} is, like the AVL tree, a *balanced* BST that keeps its height controlled.

- A `null` value on a childless link is treated as a [leaf node]{.hl}.

- Its properties:
  - The root is [black]{.hl}.
  - Every leaf (`null`) is black.
  - No path from the root to a leaf has two [red]{.hl} nodes in a row.
  - Every root-to-leaf path passes through the *same* number of black nodes.

</div>
<div>

<div style="height: 3rem;"></div>

<svg viewBox="0 0 320 240" style="width: 100%; background:#fff; border-radius:8px;" font-family="monospace" font-size="12">
  <line x1="180" y1="30" x2="110" y2="80"  stroke="#333"/>
  <line x1="180" y1="30" x2="250" y2="80"  stroke="#333"/>
  <line x1="110" y1="80" x2="70"  y2="130" stroke="#333"/>
  <line x1="110" y1="80" x2="150" y2="130" stroke="#333"/>
  <line x1="250" y1="80" x2="290" y2="130" stroke="#333"/>
  <line x1="70"  y1="130" x2="45" y2="180" stroke="#333"/>
  <line x1="150" y1="130" x2="130" y2="180" stroke="#333"/>
  <g stroke="#333">
    <circle cx="180" cy="30"  r="15" fill="#111"/>
    <circle cx="110" cy="80"  r="15" fill="#e11d48"/>
    <circle cx="250" cy="80"  r="15" fill="#111"/>
    <circle cx="70"  cy="130" r="15" fill="#111"/>
    <circle cx="150" cy="130" r="15" fill="#111"/>
    <circle cx="290" cy="130" r="15" fill="#e11d48"/>
    <circle cx="45"  cy="180" r="15" fill="#e11d48"/>
    <circle cx="130" cy="180" r="15" fill="#e11d48"/>
  </g>
  <g fill="#000" font-size="9" text-anchor="middle">
    <text x="182" y="215">black = ● &nbsp; red = ●</text>
  </g>
</svg>
<p style="text-align:center; color:#9aa0a6; font-size:0.8rem;">the black null leaves are omitted for clarity</p>

</div>
</div>

---
layout: prism
heading: "Red-Black Repair — Overview"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Search never changes the tree, so it is identical to a BST search; *insertion* and *deletion* also start out exactly as in a BST.

- After an insert or delete, a red-black property may be violated, so the tree must be [repaired]{.hl}.

- On insertion, the new node is always painted [red]{.hl}.
  - We then repair according to whether the new node's **parent** is red or black.

---
layout: prism
heading: "Red-Black Repair — Black Parent"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- If the inserted node's parent is [black]{.hl}, adding a red child violates **nothing**:
  - the "no two reds in a row" rule still holds, and
  - the black-count on every root-to-leaf path is unchanged (a red node adds no black to any path).

- So this case needs **no repair** — insertion is complete.

---
layout: prism
heading: "Red-Black Repair — Red Parent (Cases)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- If the parent $p$ is [red]{.hl}, then $p$ and the new node $x$ are two reds in a row — a violation.

- Since the tree *was* valid before, $p$'s parent $p_2$ must be [black]{.hl}.

- We split by the color of $p$'s sibling $s$:

<div class="sub-item">

- **Case 1**: $s$ is red.
- **Case 2**: $s$ is black.
  - **Case 2-1**: $x$ is $p$'s *right* child.
  - **Case 2-2**: $x$ is $p$'s *left* child.

</div>

</div>
<div>

<div style="height: 2rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Key fact</div>
<div class="theorem-box-body">

The grandparent $p_2$ is always black, which is what makes the recolor / rotation repairs safe.

</div>
</div>

</div>
</div>

---
layout: prism
heading: "Red-Black Repair — Case 1 (Recolor)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- **Case 1** ($s$ red): recolor $p$ and $s$ from red to [black]{.hl}, and recolor $p_2$ from black to [red]{.hl}.

- Then:
  - if $p_2$ is the root, recolor it black and finish;
  - otherwise, inspect $p_2$'s parent $p_3$ and repeat [recursively]{.hl}.

- If $p_3$ is black we are done; if $p_3$ is red, the same conflict moved up and we recurse.

</div>
<div>

<div style="height: 1rem;"></div>

<svg viewBox="0 0 340 170" style="width: 100%; background:#fff; border-radius:8px;" font-family="monospace" font-size="12">
  <text x="60" y="14" fill="#555" font-size="11">before</text>
  <line x1="60" y1="40" x2="30" y2="90" stroke="#333"/>
  <line x1="60" y1="40" x2="90" y2="90" stroke="#333"/>
  <circle cx="60" cy="40" r="14" fill="#111" stroke="#333"/>
  <circle cx="30" cy="90" r="14" fill="#e11d48" stroke="#333"/>
  <circle cx="90" cy="90" r="14" fill="#e11d48" stroke="#333"/>
  <line x1="30" y1="90" x2="15" y2="135" stroke="#333"/>
  <circle cx="15" cy="135" r="12" fill="#e11d48" stroke="#333"/>
  <text x="70" y="44" fill="#fff" font-size="10">p₂</text>
  <text x="30" y="94" fill="#fff" font-size="10" text-anchor="middle">p</text>
  <text x="90" y="94" fill="#fff" font-size="10" text-anchor="middle">s</text>
  <text x="15" y="139" fill="#fff" font-size="9" text-anchor="middle">x</text>
  <text x="200" y="80" fill="#333" font-size="20">&#8594;</text>
  <text x="260" y="14" fill="#555" font-size="11">after</text>
  <line x1="260" y1="40" x2="230" y2="90" stroke="#333"/>
  <line x1="260" y1="40" x2="290" y2="90" stroke="#333"/>
  <circle cx="260" cy="40" r="14" fill="#e11d48" stroke="#333"/>
  <circle cx="230" cy="90" r="14" fill="#111" stroke="#333"/>
  <circle cx="290" cy="90" r="14" fill="#111" stroke="#333"/>
  <line x1="230" y1="90" x2="215" y2="135" stroke="#333"/>
  <circle cx="215" cy="135" r="12" fill="#e11d48" stroke="#333"/>
  <text x="270" y="44" fill="#fff" font-size="10">p₂</text>
  <text x="230" y="94" fill="#fff" font-size="10" text-anchor="middle">p</text>
  <text x="290" y="94" fill="#fff" font-size="10" text-anchor="middle">s</text>
  <text x="215" y="139" fill="#fff" font-size="9" text-anchor="middle">x</text>
</svg>
<p style="text-align:center; color:#9aa0a6; font-size:0.8rem;">recolor p, s to black and p₂ to red, then check p₂'s parent</p>

</div>
</div>

---
layout: prism
heading: "Red-Black Repair — Case 2 (Rotations)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- **Case 2-1** ($s$ black, $x$ = right child): left-rotate about $p$ to convert it into Case 2-2.

- **Case 2-2** ($s$ black, $x$ = left child): right-rotate about $p_2$, then [swap the colors]{.hl} of $p$ and $p_2$.

- After this, the two-reds violation is gone and the black-heights are preserved.

</div>
<div>

<div style="height: 0.5rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Case 2-1 &#8594; Case 2-2</div>
<div class="theorem-box-body" style="font-size:0.9rem;">

Left-rotate about $p$ so that $x$ becomes the left child, reducing to Case 2-2.

</div>
</div>

<div class="theorem-box" style="margin-top:0.8rem;">
<div class="theorem-box-title">Case 2-2 (finish)</div>
<div class="theorem-box-body" style="font-size:0.9rem;">

Right-rotate about $p_2$, then swap the colors of $p$ (now the subtree root) and $p_2$: $p$ becomes black, $p_2$ becomes red.

</div>
</div>

</div>
</div>

---
layout: prism
heading: "DIY: Red-Black Insertion"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

enum Color { RED, BLACK };
struct Node { int key; Color color; Node *left, *right, *parent; };
Node *NIL, *root;

void leftRotate(Node* x) {
    Node* y = x->right; x->right = y->left;
    if (y->left != NIL) y->left->parent = x;
    y->parent = x->parent;
    if (x->parent == NIL) root = y; else if (x == x->parent->left) x->parent->left = y; else x->parent->right = y;
    y->left = x; x->parent = y;
}
void rightRotate(Node* x) {
    Node* y = x->left; x->left = y->right;
    if (y->right != NIL) y->right->parent = x;
    y->parent = x->parent;
    if (x->parent == NIL) root = y; else if (x == x->parent->right) x->parent->right = y; else x->parent->left = y;
    y->right = x; x->parent = y;
}
void fixup(Node* z) {
    while (z->parent->color == RED) {
        if (z->parent == z->parent->parent->left) {
            Node* s = z->parent->parent->right;
            if (s->color == RED) {                       // Case 1: recolor
                z->parent->color = BLACK; s->color = BLACK; z->parent->parent->color = RED; z = z->parent->parent;
            } else {
                if (z == z->parent->right) { z = z->parent; leftRotate(z); }   // Case 2-1 -> 2-2
                z->parent->color = BLACK; z->parent->parent->color = RED; rightRotate(z->parent->parent);
            }
        } else {                                         // mirror image
            Node* s = z->parent->parent->left;
            if (s->color == RED) {
                z->parent->color = BLACK; s->color = BLACK; z->parent->parent->color = RED; z = z->parent->parent;
            } else {
                if (z == z->parent->left) { z = z->parent; rightRotate(z); }
                z->parent->color = BLACK; z->parent->parent->color = RED; leftRotate(z->parent->parent);
            }
        }
    }
    root->color = BLACK;                                 // root is always black
}
void insert(int key) {
    Node* z = new Node{key, RED, NIL, NIL, NIL};
    Node* y = NIL; Node* x = root;
    while (x != NIL) { y = x; x = (key < x->key) ? x->left : x->right; }
    z->parent = y;
    if (y == NIL) root = z; else if (key < y->key) y->left = z; else y->right = z;
    fixup(z);
}
void inorder(Node* n) { if (n == NIL) return; inorder(n->left); cout << n->key << (n->color == RED ? "(R) " : "(B) "); inorder(n->right); }
int  blackHeight(Node* n) { if (n == NIL) return 1; return blackHeight(n->left) + (n->color == BLACK ? 1 : 0); }

int main() {
    NIL = new Node{0, BLACK, nullptr, nullptr, nullptr}; root = NIL;
    for (int x : {10, 20, 30, 15, 25, 5, 35, 1}) insert(x);
    cout << "inorder      : "; inorder(root); cout << "\n";
    cout << "root         : " << root->key << " (black)\n";
    cout << "black-height : " << blackHeight(root) << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "B-Trees — Motivation"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [Disk access]{.hl} is enormously slower than main-memory access — reading one disk block can cost as much as millions of machine instructions.

- Disk data is accessed in [blocks]{.hl}: even to read or write a single byte, an entire block must be transferred.

- The BSTs so far assumed the index lives in memory (an [internal index]{.hl}); but if the index is too large it must live on disk (an [external index]{.hl}).

- With an on-disk index, we must exploit disk characteristics to minimize the inefficiency of disk access time.

---
layout: prism
heading: "B-Trees — Multiway Search"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Increasing the [branching factor]{.hl} of a search tree lowers its expected depth.

- A perfectly balanced binary tree over one billion keys has depth ~30 — up to 30 disk accesses per operation.

- With 1000-way branching, the depth drops to just 4 — at most 4 disk accesses per operation.

- A search tree with branching factor greater than two is a [multiway search tree]{.hl}; a [B-tree]{.hl} is an external multiway search tree well suited to the disk environment.

---
layout: prism
heading: "B-Trees — Node Structure"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- A B-tree node stores up to $k$ keys in sorted order; with $k$ keys it has $k+1$ children.

- Letting the subtrees be $T_0, T_1, T_2, \ldots$, every key in subtree $T_i$ is greater than $\text{key}_{i-1}$ and smaller than $\text{key}_{i}$.

- A key's child pointer $p_i$ points to a disk [page]{.hl}; a B-tree is required to keep each node at least *half* full (between $\lceil k/2 \rceil$ and $k$ keys) so pages are used efficiently, and all leaves lie at the *same* depth.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image20.jpg" class="tikz-fig" style="width: 100%;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image22.jpg" class="tikz-fig" style="width: 100%; margin-top: 0.4rem;" />

</div>
</div>

---
layout: prism
heading: "B-Trees — Search"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- B-tree search works on the same principle as BST search.

- A BST checks whether the search key matches a node's *single* key; a B-tree checks whether the key matches any of the *several* keys in a node.

- A BST branches left or right against its one key; a B-tree finds which child to descend into by locating the pair $\text{key}_{i-1} < x < \text{key}_{i}$.

- The process then repeats [recursively]{.hl} down to a leaf.

---
layout: prism
heading: "B-Trees — Insertion"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- To insert a key $x$:
  - search for the leaf node $r$ where $x$ belongs;
  - if $r$ has room, insert and stop;
  - if not, check whether a *sibling* has room — if so, shift a key over and stop;
  - if no sibling has room, [split]{.hl} the node into two, which pushes a key up to the parent.

<div class="sub-item" style="font-size:0.9rem;">

Setup: every node except the root must hold between **2 and 5** keys.

</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image23.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">the starting B-tree</p>

</div>
</div>

---
layout: prism
heading: "B-Trees — Insertion (Room and Redistribution)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image24.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">insert 9, 31: the leaves have room, so just insert</p>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image25.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">insert 5: overflow — a sibling has room, so redistribute</p>

</div>
</div>

---
layout: prism
heading: "B-Trees — Insertion (Split)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image26.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">insert 39: no sibling room — split the node and push a key up</p>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image27.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">insert 23, 35, 36: leaves have room, so just insert</p>

</div>
</div>

---
layout: prism
heading: "DIY: B-Tree Insertion"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int T = 3;                 // minimum degree: 2*T-1 = 5 keys max (matches the "2..5 keys" rule)

struct BNode {
    vector<int> keys;
    vector<BNode*> child;
    bool leaf;
    BNode(bool l): leaf(l) {}
};
BNode* root = nullptr;

void splitChild(BNode* x, int i) {
    BNode* y = x->child[i];
    BNode* z = new BNode(y->leaf);
    for (int j = 0; j < T - 1; j++) z->keys.push_back(y->keys[j + T]);
    if (!y->leaf) for (int j = 0; j < T; j++) z->child.push_back(y->child[j + T]);
    int mid = y->keys[T - 1];
    y->keys.resize(T - 1);
    if (!y->leaf) y->child.resize(T);
    x->child.insert(x->child.begin() + i + 1, z);
    x->keys.insert(x->keys.begin() + i, mid);
}
void insertNonFull(BNode* x, int k) {
    int i = (int)x->keys.size() - 1;
    if (x->leaf) {
        x->keys.push_back(0);
        while (i >= 0 && k < x->keys[i]) { x->keys[i + 1] = x->keys[i]; i--; }
        x->keys[i + 1] = k;
    } else {
        while (i >= 0 && k < x->keys[i]) i--;
        i++;
        if ((int)x->child[i]->keys.size() == 2 * T - 1) { splitChild(x, i); if (k > x->keys[i]) i++; }
        insertNonFull(x->child[i], k);
    }
}
void insert(int k) {
    if (!root) { root = new BNode(true); root->keys.push_back(k); return; }
    if ((int)root->keys.size() == 2 * T - 1) {
        BNode* s = new BNode(false); s->child.push_back(root); splitChild(s, 0); root = s;
    }
    insertNonFull(root, k);
}
void traverse(BNode* x) {
    for (size_t i = 0; i < x->keys.size(); i++) {
        if (!x->leaf) traverse(x->child[i]);
        cout << x->keys[i] << " ";
    }
    if (!x->leaf) traverse(x->child[x->keys.size()]);
}
int main() {
    for (int x : {7,13,25,34,1,2,3,4,6,8,10,15,17,19,20,27,28,30,33,37,38,40,41,45,9,31,5,39})
        insert(x);
    cout << "sorted keys : "; traverse(root); cout << "\n";
    cout << "root keys   : "; for (int k : root->keys) cout << k << " "; cout << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "B-Trees — Deletion"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- To delete a key $x$:
  - search for the node holding $x$;
  - if that node is not a leaf, find the leaf $r$ holding $x$'s [in-order successor]{.hl} $y$ and swap $x$ with $y$;
  - remove $x$ from leaf $r$;
  - if removal causes an [underflow]{.hl}, resolve it by redistribution.

<div class="sub-item" style="font-size:0.9rem;">

Setup: every node except the root must hold between **2 and 5** keys.

</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image28.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">the starting B-tree</p>

</div>
</div>

---
layout: prism
heading: "B-Trees — Deletion (Simple and Redistribution)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image29.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">delete 7: its leaf has 3 keys, so just remove and stop</p>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image30.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">delete 4: swap with successor 5, remove, then redistribute the underflow</p>

</div>
</div>

---
layout: prism
heading: "B-Trees — Deletion (Underflow and Merge)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- **Delete 9**: after removing it from the leaf, an [underflow]{.hl} occurs.

- Borrow a key from the *parent* to resolve it; this may cause a new underflow further up, which is handled [recursively]{.hl} (borrow / merge).

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image31.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "HW_W11"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Use whatever coding-test practice platform you prefer (Baekjoon, Programmers, etc.).
  - The Programmers problems covered in class are *excluded*.

- Find and solve **three** problems that use [sorting or searching]{.hl} algorithms.
  - The remaining conditions are the same as in previous assignments.

- **Alternatively**, pick *one* sorting or searching algorithm and write up your own handwritten summary of it.
  - Review it once from the textbook first, then start from a *blank page*.

- Save as `HW_W11_20XXXXXX.pdf` and upload to the LMS.

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
