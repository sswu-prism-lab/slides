---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 12 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-12/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">자료구조실습</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">12주차: 해시 테이블</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">2027년 가을학기</p>
</div>

---
layout: prism
heading: "요약: AVL 트리"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [AVL 트리]{.hl}는 이진 검색 트리가 항상 [균형]{.hl}을 유지하도록 운영하는 대표적인 예시입니다. [Adelson-Velskii와 Landis]{.hl}에 의해 고안되었습니다.

- 트리 내 *모든* 노드에 대해, 왼쪽 서브 트리와 오른쪽 서브 트리의 높이 차가 [최대 1]{.hl}입니다.

<div class="theorem-box">
<div class="theorem-box-title">AVL 균형 조건</div>
<div class="theorem-box-body">

임의의 노드 $t$에 대해: $\;\bigl|\,\operatorname{height}(t.\text{left}) - \operatorname{height}(t.\text{right})\,\bigr| \leq 1.$

</div>
</div>

- 이 조건은 높이를 $O(\log N)$으로 보장하므로, 검색·삽입·삭제가 모두 최악의 경우에도 $O(\log N)$ 시간에 수행됩니다.

---
layout: prism
heading: "AVL 트리: 재균형"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 삽입 후에는 어떤 노드에서 균형 조건이 깨질 수 있습니다. 문제가 된 자손이 *어디에* 삽입되었는지에 따라 분류하여, 한 번 또는 두 번의 [회전]{.hl}으로 균형을 복원합니다:

<div class="sub-item-enum">

1. [LL]{.hl} — **왼쪽** 자식의 **왼쪽** 서브 트리에 삽입 &rarr; 단일 우회전.
2. [RR]{.hl} — **오른쪽** 자식의 **오른쪽** 서브 트리에 삽입 &rarr; 단일 좌회전.
3. [LR]{.hl} — **왼쪽** 자식의 **오른쪽** 서브 트리에 삽입 &rarr; 좌회전 후 우회전 (이중).
4. [RL]{.hl} — **오른쪽** 자식의 **왼쪽** 서브 트리에 삽입 &rarr; 우회전 후 좌회전 (이중).

</div>

- LL과 RR은 *단일* 회전이고, LR과 RL은 *이중* 회전입니다. 가장 깊은 곳의 불균형 노드만 수선하면 됩니다.

---
layout: prism
heading: "AVL 회전: LL과 RR"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<p style="text-align:center; font-weight:bold; margin-bottom:0.4rem;">LL &mdash; 단일 우회전</p>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w12/dsa-w12-image2.jpg" class="tikz-fig" style="width: 100%;" />

</div>
<div>

<p style="text-align:center; font-weight:bold; margin-bottom:0.4rem;">RR &mdash; 단일 좌회전</p>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w12/dsa-w12-image5.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

<div style="margin-top: 1.5rem;"></div>

- 단일 회전은 가운데 키를 서브 트리의 루트로 끌어올립니다. 이전 루트는 자식이 되고, 하나의 서브 트리가 반대쪽으로 다시 연결됩니다.

---
layout: prism
heading: "AVL 회전: LR과 RL"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<p style="text-align:center; font-weight:bold; margin-bottom:0.4rem;">LR &mdash; 좌회전 후 우회전</p>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w12/dsa-w12-image3.jpg" class="tikz-fig" style="width: 100%;" />

</div>
<div>

<p style="text-align:center; font-weight:bold; margin-bottom:0.4rem;">RL &mdash; 우회전 후 좌회전</p>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w12/dsa-w12-image4.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

<div style="margin-top: 1.2rem;"></div>

- 이중 회전은 먼저 *아래쪽* 쌍을 회전시켜 상황을 LL 또는 RR로 축소한 뒤, 대응하는 단일 회전을 적용합니다. 손자 노드 $z$가 서브 트리의 루트에 자리하게 됩니다.

---
layout: prism
heading: "DIY: 회전을 통한 AVL 삽입"
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

Node* rotateRight(Node* y) {   // LL 수선
    Node* x = y->left;
    y->left = x->right;
    x->right = y;
    upd(y); upd(x);
    return x;
}
Node* rotateLeft(Node* x) {    // RR 수선
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
    else return node;                       // 중복 없음

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
    int keys[] = {10, 20, 30, 40, 50, 25};   // RR, RR, RL 유발
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
heading: "요약: 레드-블랙 트리"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [레드-블랙 트리]{.hl}는 또 다른 균형 이진 검색 트리입니다. 자식이 없는 `null` 링크는 블랙 [리프 노드]{.hl}로 간주됩니다.

- 모든 노드는 레드 또는 블랙으로 색칠되며, 다음 [특성]{.hl}들이 항상 성립합니다:

<div class="sub-item-enum">

1. [루트]{.hl}는 블랙입니다.
2. 모든 리프(`null`)는 블랙입니다.
3. 루트에서 리프에 이르는 임의의 경로에서 [레드]{.hl} 노드가 2개 연속으로 나타나지 않습니다 (레드 노드는 레드 자식을 가질 수 없습니다).
4. 루트에서 리프에 이르는 모든 경로는 같은 수의 [블랙]{.hl} 노드를 지납니다 (*블랙 높이*가 동일).

</div>

- 이 제약들은 가장 긴 경로가 가장 짧은 경로의 최대 2배가 되도록 유지하여, $O(\log N)$의 높이를 보장합니다.

---
layout: prism
heading: "레드-블랙 트리: 삽입 수선"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 새 노드 $x$는 [레드]{.hl}로 색칠하여 삽입합니다. 부모 $p$가 블랙이면 어떤 특성도 깨지지 않습니다. 문제는 $p$ 역시 레드일 때뿐인데, 이때 레드 노드가 2개 연속되어 특성 3을 위반합니다.

- 삽입 전에는 트리가 유효했으므로, $p$의 부모 $p_2$(조부모)는 반드시 [블랙]{.hl}입니다.

- 수선은 $p$의 형제 $s$($x$의 [삼촌]{.hl})의 색상에 따라 두 경우로 나뉩니다:

<div class="sub-item-enum">

1. [Case 1]{.hl}: $s$가 **레드** &rarr; 재색칠만.
2. [Case 2]{.hl}: $s$가 **블랙** &rarr; 회전. *Case 2-1*: $x$가 $p$의 오른쪽 자식. *Case 2-2*: $x$가 $p$의 왼쪽 자식.

</div>

---
layout: prism
heading: "RB 수선: Case 1 (재색칠)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 삼촌 $s$가 [레드]{.hl}일 때는, $p$와 $s$를 레드에서 [블랙]{.hl}으로 재색칠하고, 조부모 $p_2$를 블랙에서 [레드]{.hl}로 재색칠합니다.

- 이렇게 하면 모든 경로의 블랙 높이가 유지되면서, 위반 가능성이 트리의 *위쪽*으로 밀려납니다:

<div class="sub-item-enum">

1. $p_2$가 이제 루트라면 다시 블랙으로 재색칠하고 &mdash; 완료.
2. 그렇지 않으면 $p_2$의 부모 $p_3$을 확인합니다: $p_3$이 블랙이면 끝나고, $p_3$이 레드이면 $p_2$를 $x$의 역할로 두고 수선을 재귀적으로 반복합니다.

</div>

- Case 1은 회전을 수행하지 않고, 재색칠만 하며 루트 쪽으로 연쇄될 수 있습니다.

---
layout: prism
heading: "RB 수선: Case 2 (회전)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 삼촌 $s$가 [블랙]{.hl}일 때는, $p$와 $p_2$에서의 회전으로 이중 레드를 수선합니다:

<div class="sub-item-enum">

1. [Case 2-1]{.hl} ($x$가 $p$의 오른쪽 자식): $p$를 중심으로 [좌회전]{.hl}합니다. 이는 "지그재그"를 곧게 펴서 상황을 Case 2-2로 축소합니다.
2. [Case 2-2]{.hl} ($x$가 $p$의 왼쪽 자식): 조부모 $p_2$를 중심으로 [우회전]{.hl}한 뒤, $p$와 $p_2$의 [색상을 맞바꿉니다]{.hl}.

</div>

- Case 2 이후에는 서브 트리의 루트가 블랙이고 두 레드 자식을 가지므로, 위반이 국소적으로 해결되어 &mdash; 연쇄가 필요하지 않습니다. (오른쪽에서는 대칭적으로 적용됩니다.)

---
layout: prism
heading: "DIY: 레드-블랙 트리 삽입"
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
bool isRed(Node* n) { return n && n->color == RED; }   // null 은 블랙

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
            Node* s = g->right;                 // 삼촌
            if (isRed(s)) {                      // Case 1: 재색칠
                p->color = s->color = BLACK; g->color = RED; z = g;
            } else {
                if (z == p->right) {             // Case 2-1: 좌회전
                    z = p; rotateLeft(z); p = z->parent;
                }
                p->color = BLACK; g->color = RED; // Case 2-2: 우회전 + 재색칠
                rotateRight(g);
            }
        } else {                                 // 대칭
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
heading: "요약: B-트리"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [B-트리]{.hl}의 한 노드에는 최대 $k$개의 키가 크기순으로 저장됩니다. 키를 $k$개 가진 노드는 $k+1$개의 자식을 가집니다.

- 서브 트리를 $T_0, T_1, T_2, \ldots$라 하면, 서브 트리 $T_i$의 모든 키는 $\text{key}_{i-1}$보다 [크고]{.hl} $\text{key}_i$보다 [작습니다]{.hl}.

- 이러한 다진 분기는 트리를 얕게 유지하므로, 디스크 기반 저장에 이상적입니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w12/dsa-w12-image6.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 균형 트리 vs. 불균형 트리의 높이"
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

Node* bstInsert(Node* n, int k) {              // 일반 BST (균형 없음)
    if (!n) return new Node(k);
    if (k < n->key) n->left = bstInsert(n->left, k);
    else            n->right = bstInsert(n->right, k);
    upd(n);
    return n;
}
Node* avlInsert(Node* n, int k) {              // 자가 균형
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
    for (int k = 1; k <= 15; k++) {            // 이미 정렬된 입력: BST 최악의 경우
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
heading: "해시 테이블: 아이디어"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [해시 테이블]{.hl}은 저장과 검색을 *극단적인* 효율까지 밀어붙인 자료구조로, 이상적으로는 두 연산 모두 [상수 시간]{.hl}에 수행됩니다.

- 검색 트리는 루트에서 리프에 이르는 경로를 따라 키와 [비교하며]{.hl} 원소를 찾습니다. 진정한 상수 시간에 도달하려면 *원소들 간의 비교 자체를 피해야* 합니다.

- 해시 테이블에서는 다른 원소와 비교하는 것이 아니라, 원소의 [값이 그 위치를 직접 결정합니다]{.hl}.

<div class="theorem-box">
<div class="theorem-box-title">핵심 아이디어</div>
<div class="theorem-box-body">

값 자체를 [해시 함수]{.hl} $h$에 넣으면, 원소가 놓일 [주소]{.hl}가 계산됩니다. 순회도, 비교의 연쇄도 없습니다.

</div>
</div>

---
layout: prism
heading: "해시 테이블: 값에 의한 직접 주소 지정"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 원소를 저장하려면 $h$로 해시 값을 계산합니다. 크기가 $m$인 테이블에서 $h$는 $\{0, 1, \ldots, m-1\}$ 범위의 주소를 반환합니다.

- 가장 단순한 선택: 값을 $m$으로 나눈 [나머지]{.hl}를 사용합니다.

  - $h(x) = x \bmod 13$

- 검색도 같은 방식으로 동작합니다 — $h(x)$를 다시 계산해 그 한 칸만 확인합니다.

</div>
<div>

<p style="text-align:center; margin-bottom:0.4rem;">입력: 25, 13, 16, 15, 7 &nbsp;($m = 13$)</p>

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
heading: "해시 테이블: 적재율"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.7em;
}
</style>

- 삽입과 검색은 모두 한 번의 해시 계산이므로, 평균적으로 두 연산 모두 [상수 시간]{.hl}에 처리됩니다.

- 테이블이 얼마나 채워졌는지가 성능에 큰 영향을 줍니다. 이 비율을 [적재율]{.hl} $\alpha$라고 합니다.

  - 앞의 예에서는 $\alpha = 5/13$입니다.

- 해시 테이블은 한 단계로 주소에 도달하지만, [결정적인 장애물]{.hl}이 있습니다: 서로 다른 두 값이 *같은* 주소로 대응될 수 있습니다. 이를 처리하는 것이 이 강의 나머지의 핵심 문제입니다.

---
layout: prism
heading: "해시 함수"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [해시 함수]{.hl}는 키 값을 입력으로 받아 해시 테이블상의 주소를 반환합니다.

- 좋은 해시 함수는 두 가지 [성질]{.hl}을 가집니다:

<div class="sub-item-enum">

1. 입력 원소가 테이블 전체에 [골고루]{.hl} 퍼져야 합니다.
2. 계산이 [간단]{.hl}해야 합니다.

</div>

- 첫 번째 성질을 잘 만족해야 서로 다른 두 원소가 한 주소에서 [충돌]{.hl}할 확률이 작아집니다.

- 실제로 첫 번째 성질을 만족하는 함수를 설계하는 데 지나치게 복잡한 계산이 필요한 경우는 거의 없습니다.

---
layout: prism
heading: "해시 함수: 나누기 방법"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [나누기 방법]{.hl}은 가능한 가장 단순한 형태를 사용합니다:

<div class="sub-item">

$$ h(x) = x \bmod m $$

</div>

- 여기서 $m$은 [테이블 크기]{.hl}입니다. 유효한 주소가 $0, 1, \ldots, m-1$이므로, $m$으로 나눈 나머지를 취하는 것이 자연스럽습니다.

- $m$은 2의 거듭제곱에 *가깝지 않은* [소수]{.hl}로 선택합니다. 2의 거듭제곱은 $h$가 하위 비트에만 의존하게 만듭니다.

- 입력의 [모든 비트]{.hl}를 사용하는 편이 확률적으로 더 나은 분포를 주는 경향이 있습니다.

---
layout: prism
heading: "해시 함수: 곱하기 방법"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 나누기 방법은 큰 수를 테이블 크기 범위로 *줄입니다*. [곱하기 방법]{.hl}은 대신 입력을 $(0,1)$로 대응시킨 뒤 테이블 크기로 확대합니다.

  - 이 방법은 함수의 동작을 결정하는 $0 < A < 1$인 상수 $A$가 필요합니다.

- 원소 $x$에 대해 $A$를 곱하고, [소수부]{.hl}만 남긴 뒤, $m$을 곱하고 정수부를 취합니다:

<div class="sub-item">

$$ h(x) = \bigl\lfloor\, m\,(x A \bmod 1)\,\bigr\rfloor $$

</div>

- 여기서 테이블 크기 $m$은 *무엇이든* 될 수 있으며, 대신 $A$의 값이 분포에 크게 영향을 줍니다. 잘 알려진 좋은 선택은 $A = (\sqrt{5} - 1)/2 \approx 0.618$입니다.

---
layout: prism
heading: "DIY: 나누기 vs. 곱하기 해싱"
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
    double A = (sqrt(5.0) - 1) / 2;       // ~0.6180339887 (황금비 - 1)
    double xa = x * A;
    double frac = xa - floor(xa);         // 소수부만 남김
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
heading: "충돌"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 이제 28을 삽입한다고 합시다. $h(x)=x \bmod 13$이므로 $h(28)=2$인데, 주소 2에는 이미 15가 들어 있습니다.

- 둘 이상의 원소가 *같은* 주소에 배정되는 경우를 [충돌]{.hl}이라고 합니다.

- [충돌 해결]{.hl}에는 크게 두 가지 방식이 있습니다:

<div class="sub-item-enum">

1. 테이블 [밖]{.hl}의 공간을 사용하여 해결 (체이닝).
2. 테이블 [내부]{.hl}에서 해결 (개방 주소법).

</div>

</div>
<div>

<p style="text-align:center; margin-bottom:0.4rem;">28이 주소 2에서 충돌</p>

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
heading: "충돌 해결: 체이닝"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [체이닝]{.hl}(분리 연쇄법)에서는 같은 주소로 해싱되는 모든 원소를 그 칸의 하나의 [연결 리스트]{.hl}에 매답니다.

- 큰 장점: 각 버킷이 제한 없이 늘어날 수 있으므로, [적재율이 1을 넘어도]{.hl} 여전히 동작합니다.

- 검색 비용은 $h(x)$에 있는 연쇄의 길이에 비례하므로, 연쇄를 짧게(낮은 $\alpha$) 유지하면 빠르게 유지됩니다.

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
heading: "DIY: 분리 연쇄법"
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

    int h(int x) { return x % m; }                     // 나누기 방법
    void insert(int x) { buckets[h(x)].push_back(x); } // 연쇄에 추가
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
heading: "충돌 해결: 개방 주소법 (1/5)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [개방 주소법]{.hl}은 *어떤* 추가 공간도 허용하지 않습니다. 충돌이 일어나면 주어진 테이블 내부 어딘가에서 해결해야 합니다.

  - 따라서 적재율은 [1을 넘어설 수 없습니다]{.hl}.
  - 모든 원소가 자신의 해시 값과 일치하는 주소에 놓인다는 보장은 없습니다.

- 계산된 주소를 이미 다른 원소가 차지하고 있으면, [다음 조사 규칙]{.hl}에 따라 새 칸을 찾습니다.

- 다음 주소를 정하는 규칙에는 여러 가지가 있습니다. 대표적으로 [선형 조사]{.hl}, [이차 조사]{.hl}, [더블 해싱]{.hl}이 있습니다.

---
layout: prism
heading: "개방 주소법 (2/5): 선형 조사"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [선형 조사]{.hl}는 가장 단순한 방식입니다: 충돌이 나면 바로 *다음* 칸을 확인합니다.

- $i$번째 조사는 $h(x)$에서 $i$칸 떨어진 위치입니다:

<div class="sub-item">

$$ h_i(x) = (h(x) + i) \bmod m,\quad i = 0, 1, 2, \ldots $$

</div>

- 예: 28($h=2$)은 2, 3을 건너뛰고 4에 안착하고, 20($h=7$)은 8에, 38($h=12$)은 순환하여 6에 놓입니다.

</div>
<div>

<p style="text-align:center; margin-bottom:0.4rem; font-size:0.85rem;">입력: 25,13,16,15,7,28,31,20,1,38</p>

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
heading: "개방 주소법 (3/5): 이차 조사"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 선형 조사는 원소가 한 영역에 몰릴 때 성능이 크게 나빠집니다. 이 현상을 [1차 군집]{.hl}이라고 합니다.

- [이차 조사]{.hl}는 바로 다음 칸으로 넘어가는 대신 이차 함수를 사용해 보폭을 넓힙니다:

<div class="sub-item">

$$ h_i(x) = (h(x) + c_1 i^2 + c_2 i) \bmod m,\quad i = 0, 1, 2, \ldots $$

</div>

- 상수 $c_1$과 $c_2$를 키우면 조사가 1차 군집을 빠르게 벗어날 수 있습니다.

- 그러나 많은 원소가 *같은 초기* 해시 값을 공유하면, 이들은 여전히 [같은 순서]{.hl}로 조사하여 비효율적이 됩니다 — 이를 [2차 군집]{.hl}이라고 합니다.

---
layout: prism
heading: "개방 주소법 (4/5): 더블 해싱"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [더블 해싱]{.hl}은 *두 개*의 해시 함수를 결합합니다:

<div class="sub-item">

$$ h_i(x) = \bigl(h(x) + i \cdot f(x)\bigr) \bmod m,\quad i = 0, 1, 2, \ldots $$

여기서 $h(x)$와 $f(x)$는 서로 다른 두 해시 함수입니다.

</div>

- 충돌이 일어나도(즉, 두 원소가 같은 $h(x)$를 가져도), 이들이 같은 $f(x)$까지 공유할 확률은 매우 작으므로 [서로 다른 보폭]{.hl}으로 이동하여 2차 군집을 해결합니다.

- 두 함수로 흔히 쓰는 선택은 다음과 같습니다:

<div class="sub-item-enum">

1. $h(x) = x \bmod m$
2. $f(x) = 1 + (x \bmod m')$, 여기서 $m'$은 $m$보다 약간 작은 소수입니다.

</div>

---
layout: prism
heading: "DIY: 선형 조사 vs. 더블 해싱"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int EMPTY = -1;

// -------- 선형 조사:  h_i(x) = (x mod m + i) mod m --------
vector<int> linearProbe(const vector<int>& keys, int m) {
    vector<int> a(m, EMPTY);
    for (int x : keys) {
        int i = 0;
        while (a[(x % m + i) % m] != EMPTY) i++;
        a[(x % m + i) % m] = x;
    }
    return a;
}

// -------- 더블 해싱:  h_i(x) = (x mod m + i*(1 + x mod m')) mod m --------
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
heading: "개방 주소법 (5/5): 재해싱과 삭제"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 개방 주소법은 적재율이 높아지면 성능이 급격히 저하됩니다. [임계값]{.hl}을 설정하고, 이를 넘으면 테이블을 키운(보통 [2배]{.hl}) 뒤 모든 원소를 [재해싱]{.hl}합니다.

- 삭제는 주의가 필요합니다: 칸을 단순히 비우면, 이후의 조사가 일찍 멈춰 그 뒤의 원소들을 놓칠 수 있습니다.

- 대신 칸을 [DELETED]{.hl}로 표시(지연 삭제)하여 조사 순서가 그 칸을 계속 지나가도록 합니다.

</div>
<div>

<p style="text-align:center; margin-bottom:0.4rem; font-size:0.85rem;">1 삭제 &rarr; 칸 1을 DELETED로 표시</p>

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
    unordered_map<string, int> hash;   // 해시 테이블; 참고: std::map 은 균형 BST

    cout << hash.empty() << endl;       // 1 (true) -- 현재 비어 있음

    hash.insert(make_pair("Korea", 82));
    hash["USA"] = 1;
    hash.insert({"Japan", 81});

    cout << hash.size() << endl;         // 3
    cout << hash.count("Korea") << endl; // 1

    // unordered_map 의 순회 순서는 정해져 있지 않음
    for (pair<string, int> element : hash)
        cout << "Key: " << element.first << " Value: " << element.second << endl;

    // find() 는 iterator 를 반환하고, key 가 없으면 end() 를 반환
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
heading: "문제: 완주하지 못한 선수 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 많은 선수가 마라톤에 참가하는데, [단 한 명을 제외한 모두]{.hl}가 완주합니다.

- 모든 선수의 이름 배열 `participant`와 완주자의 배열 `completion`이 주어질 때, [완주하지 못한 단 한 명]{.hl}의 이름을 반환하세요.

- 제약 조건:

<div class="sub-item-enum">

1. $1 \le |\texttt{participant}| \le 100{,}000$이고, $|\texttt{completion}| = |\texttt{participant}| - 1$입니다.
2. 이름은 소문자이며 길이는 1에서 20입니다. [중복된 이름]{.hl}이 있을 수 있습니다.

</div>

- 아이디어: 해시 맵으로 각 참가자를 세고, 완주자마다 하나씩 빼면, 양의 카운트가 남는 값이 답입니다. (중복이 있으면 단순 집합 비교는 실패하므로, 개수를 세는 방식으로 해결합니다.)

---
layout: prism
heading: "문제: 완주하지 못한 선수 (2/2)"
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

    for (auto& player : participant) {          // 각 참가자를 셈 (중복 처리)
        if (hash.find(player) == hash.end()) hash.insert(make_pair(player, 1));
        else hash[player]++;
    }
    for (auto& player : completion)             // 완주자 -> 하나 감소
        hash[player]--;

    for (auto& player : participant)            // 카운트가 0보다 크게 남은 한 명
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
heading: "문제: 전화번호 목록 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 전화번호 목록 중 어떤 번호가 다른 번호의 [접두어]{.hl}인지 확인하세요.

  - 예: 구조 요청 번호 `119`는 `9767 4223`의 이웃인 `1195524421`의 접두어입니다.

- `phone_book`이 주어질 때, 어떤 번호가 다른 번호의 접두어이면 `false`를, 그렇지 않으면 `true`를 반환하세요.

- 제약 조건:

<div class="sub-item-enum">

1. $1 \le |\texttt{phone\_book}| \le 1{,}000{,}000$이고, 각 번호의 길이는 1에서 20입니다.
2. 중복된 번호는 없습니다.

</div>

- 아이디어: 모든 번호를 해시 맵에 넣은 뒤, 각 번호의 [진부분 접두어]{.hl}를 하나씩 확인합니다 — 어떤 접두어가 저장된 번호이면 `false`를 반환합니다.

---
layout: prism
heading: "문제: 전화번호 목록 (2/2)"
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
        hash[phone_book[i]]++;                          // 모든 번호를 등록

    for (int i = 0; i < (int)phone_book.size(); i++) {
        for (int j = 1; j < (int)phone_book[i].size(); j++) {
            // 이 번호의 진부분 접두어가 저장된 번호인가?
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
heading: "문제: 의상 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 한 스파이는 매일 *서로 다른 옷 조합*을 입는 것을 좋아합니다. 각 의상 항목에는 [이름]{.hl}과 [종류]{.hl}(예: 모자, 안경, 상의)가 있습니다.

- 규칙: 각 종류당 [최대 한 개]{.hl}의 항목만 착용할 수 있고, 적어도 [한 개 이상]{.hl}은 착용해야 합니다. 서로 다른 의상 조합의 수를 세세요.

- 각 행이 `[이름, 종류]`인 2차원 배열 `clothes`가 주어질 때, 가짓수를 반환하세요.

- 아이디어: 항목을 종류별로 묶습니다. 어떤 종류에 항목이 $n_i$개 있으면 $n_i + 1$가지 선택(하나를 고르거나, 그 종류는 착용하지 않음)이 있습니다. 모든 종류에 걸쳐 곱한 뒤, "아무것도 입지 않는" 경우를 없애기 위해 [1을 뺍니다]{.hl}.

<div class="sub-item">

$$ \text{answer} = \Bigl(\prod_i (n_i + 1)\Bigr) - 1 $$

</div>

---
layout: prism
heading: "문제: 의상 (2/2)"
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
    unordered_map<string, vector<string>> hash;   // 종류 -> 항목 이름 목록

    for (int i = 0; i < (int)clothes.size(); i++)
        hash[clothes[i][1]].push_back(clothes[i][0]);

    for (auto& element : hash)
        answer *= element.second.size() + 1;       // 이 종류에서 하나를 고르거나, 고르지 않음

    return answer - 1;                              // "아무것도 입지 않는" 경우 제거
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

- [더블 해싱]{.hl}(개방 주소법)에서 두 해시 함수는 흔히 다음과 같이 선택합니다:

<div class="sub-item-enum">

1. $h(x) = x \bmod m$
2. $f(x) = 1 + (x \bmod m')$, 여기서 $m'$은 $m$보다 약간 작은 소수입니다.

</div>

- 이 설계가 *왜* 효과적인지 [생각해 보세요]{.hl}. (힌트: $f(x)$가 0을 반환할 수 있다면 무엇이 잘못될까요? 두 모듈러스는 왜 달라야 할까요?)

- 또한 더블 해싱에서는 두 번째 해시 값을 [테이블 크기와 비교]{.hl}할 때 주의해야 할 점이 있습니다. 그것이 무엇인지 생각해 보세요.

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
