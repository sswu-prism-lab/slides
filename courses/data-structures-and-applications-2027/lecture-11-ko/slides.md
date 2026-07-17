---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 11 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-11/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">자료구조실습</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">11주차: 검색 트리 — 이진 검색 트리, AVL, 레드-블랙, B-트리</p>

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
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.6rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">기초</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">레코드, 인덱스, 키</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0.4rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">이진 검색 트리 (검색, 삽입, 삭제, 순회)</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0.4rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">파라메트릭 서치</span></p>
    <p style="margin: 0.6rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">균형 검색 트리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">AVL 트리 (정의와 수선: LL, RR, LR, RL)</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0.4rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">레드-블랙 트리 (정의와 수선)</span></p>
    <p style="margin: 0.6rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">외장 검색 트리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">B-트리 (검색, 삽입, 삭제)</span></p>
  </div>

</div>

---
layout: prism
heading: "레코드, 인덱스, 키"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [레코드]{.hl}에는 어떤 개체에 대한 정보가 들어 있습니다.
  - *사람* 레코드에는 학번, 이름, 주소, 휴대폰 번호 등의 정보가 포함될 수 있습니다. 이러한 각각의 정보를 [필드]{.hl}라고 합니다.

- [인덱스]{.hl}는 개체의 레코드를 *검색*하기 위해 사용됩니다.
  - 인덱스에 모든 레코드를 저장할 *수도* 있으나, 그러면 인덱스가 데이터베이스 자체와 다를 바 없어집니다.
  - 대신, 인덱스는 각 레코드를 *대표*할 수 있는 필드로 구성합니다 — 사람 레코드라면 학번을 그 대표 필드로 삼을 수 있습니다.

- 다른 레코드와 중복되지 않으면서 각 레코드를 [구분]{.hl}할 수 있는 필드를 인덱스에 사용하며, 이를 [키]{.hl}라고 합니다.
  - 키는 필드 하나 또는 여러 개로 이루어질 수 있습니다.

---
layout: prism
heading: "이진 검색 트리"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [이진 검색 트리]{.hl}(BST)는 다음과 같은 특성을 가집니다.
  - 각 노드는 하나의 키를 저장하며, 모든 키는 *서로 다릅니다*.
  - 최상위 레벨에 [루트]{.hl} 노드가 있고, 각 노드는 *최대 2개*의 자식을 가집니다.
  - 임의의 노드에 대해, 그 키는 왼쪽 아래에 있는 모든 키보다 *크고*, 오른쪽 아래에 있는 모든 키보다 *작습니다*.

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

<p style="text-align:center; color:#9aa0a6; font-size:0.85rem; margin-top:0.3rem;">중위 순회 키: 10 20 25 30 35 40 45</p>

</div>
</div>

---
layout: prism
heading: "BST — 검색"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 키가 $x$인 노드를 검색할 때, 그런 노드가 존재하면 해당 노드를 반환하고, 존재하지 않으면 `null`을 반환합니다.

- 필요하다면, 노드 대신 키가 $x$인 레코드를 반환할 수도 있습니다.

- 검색은 $x$가 현재 키보다 작으면 왼쪽으로, 크면 오른쪽으로 재귀하며 — 매 단계마다 서브 트리 하나를 버립니다.

</div>
<div>

<div style="height: 1rem;"></div>

```text
search(t, x):
  // t: (서브) 트리의 루트
  // x: 검색하는 키
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
heading: "BST — 삽입"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 원소 $x$를 삽입하려면, 트리에 키가 $x$인 노드가 이미 있어서는 안 됩니다.

- $x$의 자리를 찾는 것은 *실패하는* 검색을 정확히 한 번 수행하는 것과 같습니다.
  - 루트에서부터 검색을 수행해 임의의 리프 위치에서 `null` 링크에 이르면, 그 `null` 자리에 $x$를 매답니다.

</div>
<div>

<div style="height: 1rem;"></div>

```text
insert(t, x):
  // t: (서브) 트리의 루트
  // x: 삽입하고자 하는 키
  if (t == null):
      x를 키로 하는 새 노드를
      t의 부모 밑에 매달고 종료
  else if (x < t.item):
      insert(t.left, x)
  else:
      insert(t.right, x)
```

</div>
</div>

---
layout: prism
heading: "BST — 삭제"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 노드 $r$의 삭제는 세 가지 경우에 따라 처리됩니다.

<div class="sub-item-enum">

1. **Case 1** — $r$이 *리프* 노드인 경우: 그냥 $r$을 버립니다.
2. **Case 2** — $r$의 자식이 *하나*인 경우: $r$을 버린 후, $r$의 부모를 $r$의 자식과 직접 연결합니다.
3. **Case 3** — $r$의 자식이 *둘*인 경우: $r$의 오른쪽 서브 트리에서 최소 키를 가진 노드 $s$를 찾아 $r$의 자리에 복사한 뒤, $s$를 삭제합니다.

</div>

<div style="height: 0.6rem;"></div>

- Case 3에서 [중위 후속자]{.hl} $s$는 자식이 최대 하나임이 보장되므로, 그 제거는 Case 1 또는 Case 2로 귀착됩니다.

---
layout: prism
heading: "DIY: BST 검색, 삽입, 삭제"
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
    return t;                                   // 중복은 무시
}
Node* search(Node* t, int x) {
    if (!t || t->key == x) return t;
    return x < t->key ? search(t->left, x) : search(t->right, x);
}
Node* removeNode(Node* t, int x) {
    if (!t) return nullptr;
    if (x < t->key)      t->left  = removeNode(t->left,  x);
    else if (x > t->key) t->right = removeNode(t->right, x);
    else {                                      // 노드를 찾음
        if (!t->left)  return t->right;         // Case 1 / Case 2
        if (!t->right) return t->left;
        Node* s = t->right;                     // Case 3: 중위 후속자
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
heading: "트리 순회"
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
전위 순회&nbsp;: A B D E G C F<br>
중위 순회&nbsp;&nbsp;: D B E G A C F<br>
후위 순회: D G E B F C A
</div>

</div>
</div>

---
layout: prism
heading: "DIY: 트리 순회"
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
heading: "파라메트릭 서치"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [파라메트릭 서치]{.hl}는 [최적화 문제]{.hl}를 [결정 문제]{.hl}로 바꾸어 해결합니다.
  - *정육점에서 고기 무게를 다는 것*을 떠올려 보세요. 답을 직접 계산하지 않고, "너무 많은가, 부족한가?"를 계속 물어봅니다.

- *예/아니오* 판단을 내려주는 함수를 사용하며, 그 판단을 바탕으로 후보 답(최적화된 값)을 반복해서 조정합니다.

- 어떤 조건을 만족하는 값들 중 *최소값* 또는 *최대값*을 찾는 데 쓰입니다.
  - 예산: `27`
  - 물건 가격: `[17, 28, 15, 30, 22, 19]`

---
layout: prism
heading: "DIY: 파라메트릭 서치"
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

    // 최적화: 예산 내에서 가장 싼 물건을 몇 개까지 살 수 있는가?
    // 결정 문제 check(k): k개를 살 수 있는가?  (k에 대해 단조)
    auto check = [&](int k) {
        int cost = 0;
        for (int i = 0; i < k; i++) cost += price[i];
        return cost <= budget;
    };

    int lo = 0, hi = price.size(), ans = 0;         // 답에 대한 이진 탐색
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (check(mid)) { ans = mid; lo = mid + 1; } // 가능 -> 더 많이 시도
        else              hi = mid - 1;              // 불가능 -> 더 적게 시도
    }
    cout << "max items within budget " << budget << " = " << ans << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "균형 검색 트리"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 평범한 BST는 퇴화할 수 있습니다. 키를 정렬된 순서로 삽입하면 깊이가 $O(n)$인 "연결 리스트" 모양이 되어 검색이 $O(n)$이 됩니다.

- [균형 검색 트리]{.hl}는 높이를 $\log n$ 근처로 능동적으로 유지하여, 검색·삽입·삭제가 모두 $O(\log n)$을 유지하도록 합니다.

<div style="text-align:center; margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image2.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: "AVL 트리"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [AVL 트리]{.hl}는 언제나 스스로 *균형*을 유지하는 BST의 대표적인 예시입니다.
  - [Adelson-Velskii와 Landis]{.hl}가 고안했습니다(그래서 "AVL").

- AVL 트리는 *임의의* 노드에 대해, 그 왼쪽 서브 트리와 오른쪽 서브 트리의 높이 차가 **1보다 크지 않은** 상태를 유지합니다.

<div class="theorem-box">
<div class="theorem-box-title">AVL 균형 조건</div>
<div class="theorem-box-body">

모든 노드 $t$에 대해: $\bigl|\,\text{height}(t.\text{left}) - \text{height}(t.\text{right})\,\bigr| \leq 1$.

</div>
</div>

---
layout: prism
heading: "AVL 트리 — 예시"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.0rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image4.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.85rem;">AVL 트리</p>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image3.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.85rem;">AVL 트리가 아님</p>

</div>
</div>

<div style="font-size: 0.9rem; margin-top: 0.4rem;">

- 오른쪽에서 키 `10`을 가진 노드는 왼쪽 서브 트리 높이가 `0`, 오른쪽 서브 트리 높이가 `2`로 — 차이가 `2`이며, 균형 조건을 위반합니다.
- AVL 노드는 보통의 `key`, `left`, `right`에 더해, 서브 트리의 높이를 담는 `height` 필드를 가집니다.

</div>

---
layout: prism
heading: "AVL 트리 — 노드 구조"
---

<div style="height: 1.5rem;"></div>

```cpp
class Node {
public:
    int   key;
    Node *left;
    Node *right;
    int   height;                       // 이 노드를 루트로 하는 서브 트리의 높이
    Node(int k)
        : key(k), left(nullptr), right(nullptr), height(1) {}
};
```

<div style="height: 1rem;"></div>

- BST 노드와 비교하면 추가된 것은 [`height`]{.hl} 하나뿐이며, 이 덕분에 각 노드의 [균형 인수]{.hl} = $\text{height(left)} - \text{height(right)}$ 를 $O(1)$에 계산할 수 있습니다.

---
layout: prism
heading: "AVL 수선 — 균형이 깨질 때"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- *삽입* 또는 *삭제* 후에 AVL 트리는 불균형해질 수 있습니다.

- 불균형은 **한** 노드에서 나타날 수도, **둘 이상의** 노드에서 나타날 수도 있습니다.
  - 삽입/삭제가 일어난 곳과 전혀 관계없는 자리에서 나타나는 일은 없습니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image5.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">왼쪽: 한 곳에서 불균형 &nbsp;·&nbsp; 오른쪽: 두 곳에서 불균형</p>

</div>
</div>

---
layout: prism
heading: "AVL 수선 — 좌회전"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

- 수선은 *가장 낮은* 곳의 불균형 서브 트리에서 시작해 위로 올라갑니다.

```text
leftRotate(t):  // t: 회전의 중심 노드
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
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">좌회전 후 균형을 맞춤</p>

</div>
</div>

---
layout: prism
heading: "AVL 수선 — 좌회전(C++)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<div style="height: 1rem;"></div>

```cpp
// x를 루트로 하는 서브 트리를 좌회전
Node* leftRotate(Node *x) {
    Node *y  = x->right;
    Node *T2 = y->left;
    // 회전 수행
    y->left  = x;
    x->right = T2;
    // 높이 갱신
    x->height =
        max(height(x->left),
            height(x->right)) + 1;
    y->height =
        max(height(y->left),
            height(y->right)) + 1;
    return y;                 // 새 서브 트리 루트
}
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image7.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">한 번의 좌회전으로 두 곳의 불균형을 동시에 해소</p>

</div>
</div>

---
layout: prism
heading: "AVL 수선 — 우회전"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

```text
rightRotate(t):  // t: 회전의 중심 노드
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
// y를 루트로 하는 서브 트리를 우회전
Node* rightRotate(Node *y) {
    Node *x  = y->left;
    Node *T2 = x->right;
    x->right = y;            // 회전 수행
    y->left  = T2;
    y->height =             // 높이 갱신
        max(height(y->left), height(y->right)) + 1;
    x->height =
        max(height(x->left), height(x->right)) + 1;
    return x;                // 새 서브 트리 루트
}
```

</div>
</div>

---
layout: prism
heading: "AVL 수선 — 단순 회전이 실패할 때"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 서브 트리의 모양에 따라, *단순* 회전으로는 균형이 **복원되지 않을** 수 있습니다.

- [LR 서브 트리]{.hl}가 [LL 서브 트리]{.hl}보다 깊으면, 우회전을 해도 불균형이 옮겨갈 뿐 — 높이 차가 그대로 남습니다.

- 먼저 불균형의 *유형*을 파악한 뒤, 그에 맞는 규칙을 적용해야 합니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image9.jpg" class="tikz-fig" style="width: 100%;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image10.jpg" class="tikz-fig" style="width: 100%; margin-top: 0.4rem;" />

</div>
</div>

---
layout: prism
heading: "AVL 수선 — LL 경우"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- **LL** — *왼쪽-왼쪽* 손자 서브 트리가 가장 깊은 경우입니다.

- 문제가 된 노드 $t$를 기준으로 [우회전]{.hl}을 한 번 수행합니다.

- 회전 한 번으로 충분합니다. 서브 트리 높이가 1 줄어들며 균형이 복원됩니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image11.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "AVL 수선 — LR 경우"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- **LR** — *왼쪽 자식의 오른쪽* 손자 서브 트리가 가장 깊은 경우입니다.

- 먼저 `t.left`를 기준으로 [좌회전]{.hl}하여 LL 모양으로 만든 뒤, $t$를 기준으로 [우회전]{.hl}합니다.

- 두 패널은 내부의 두 모양(*type I*과 *type II*)을 보여주며, 둘 다 동일하게 해결됩니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image13.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "AVL 수선 — RR 경우"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- **RR** — *오른쪽-오른쪽* 손자 서브 트리가 가장 깊은 경우입니다.

- $t$를 기준으로 [좌회전]{.hl}을 한 번 수행합니다.

- 이는 LL 경우의 거울상이며, 좌우를 뒤집은 같은 원리가 적용됩니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image14.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "AVL 수선 — RL 경우"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- **RL** — *오른쪽 자식의 왼쪽* 손자 서브 트리가 가장 깊은 경우입니다.

- LR 경우의 거울상입니다. 먼저 `t.right`를 기준으로 [우회전]{.hl}하여 RR 모양으로 만든 뒤, $t$를 기준으로 [좌회전]{.hl}합니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image15.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "AVL 수선 — 균형 규칙"
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

- [삽입]{.hl} 시 불균형은 늘어난 깊이에서 비롯되며, 알맞은 유형으로 한 번만 수선하면 높이가 복원되어 *더 이상* 문제가 전파되지 않습니다.

- [삭제]{.hl} 시에는 수선이 서브 트리를 짧게 만들어 위쪽에 *새로운* 불균형을 드러낼 수 있으므로, 수선을 트리 위쪽으로 [재귀적]{.hl}으로 계속해야 합니다.

</div>
</div>

---
layout: prism
heading: "AVL 수선 — 삽입 경우들(C++)"
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
heading: "AVL 수선 — 좀 더 큰 예제"
---

<div class="grid grid-cols-2 gap-2" style="margin-top: 0.4rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image16.jpg" class="tikz-fig" style="width: 100%;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image17.jpg" class="tikz-fig" style="width: 100%;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image18.jpg" class="tikz-fig" style="width: 100%;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image19.jpg" class="tikz-fig" style="width: 100%;" />
</div>

<p style="text-align:center; color:#9aa0a6; font-size:0.82rem; margin-top:0.2rem;">모든 노드가 균형을 이룰 때까지 잇따른 회전이 트리 위쪽으로 전파됨</p>

---
layout: prism
heading: "DIY: 회전을 포함한 AVL 삽입"
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
    cout << "preorder : "; preorder(root); cout << "\n";     // 균형 잡힌 모양이 드러남
    cout << "root = " << root->key << ", height = " << root->height << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "레드-블랙 트리"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [레드-블랙 트리]{.hl}는 AVL 트리와 마찬가지로 높이를 제어하며 유지하는 *균형* BST입니다.

- 자식이 없는 링크의 `null` 값은 [리프 노드]{.hl}로 간주합니다.

- 그 특성은 다음과 같습니다.
  - 루트는 [블랙]{.hl}입니다.
  - 모든 리프(`null`)는 블랙입니다.
  - 루트에서 리프에 이르는 경로에는 [레드]{.hl} 노드가 연속으로 두 개 있을 수 없습니다.
  - 루트에서 리프에 이르는 모든 경로는 *같은* 수의 블랙 노드를 지납니다.

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
<p style="text-align:center; color:#9aa0a6; font-size:0.8rem;">명료함을 위해 블랙 null 리프는 생략함</p>

</div>
</div>

---
layout: prism
heading: "레드-블랙 수선 — 개요"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 검색은 트리를 바꾸지 않으므로 BST 검색과 동일하며, *삽입*과 *삭제*도 처음에는 BST와 똑같이 시작합니다.

- 삽입이나 삭제 후에는 레드-블랙 특성이 위반될 수 있으므로, 트리를 [수선]{.hl}해야 합니다.

- 삽입 시, 새 노드는 항상 [레드]{.hl}로 칠합니다.
  - 그런 다음 새 노드의 **부모**가 레드인지 블랙인지에 따라 수선합니다.

---
layout: prism
heading: "레드-블랙 수선 — 부모가 블랙"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 삽입한 노드의 부모가 [블랙]{.hl}이면, 레드 자식을 추가해도 **아무것도** 위반하지 않습니다.
  - "레드가 연속으로 둘일 수 없다"는 규칙이 그대로 유지되고,
  - 루트에서 리프에 이르는 모든 경로의 블랙 개수가 변하지 않습니다(레드 노드는 어떤 경로에도 블랙을 더하지 않으므로).

- 따라서 이 경우는 **수선이 필요 없으며** — 삽입이 완료됩니다.

---
layout: prism
heading: "레드-블랙 수선 — 부모가 레드(경우들)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 부모 $p$가 [레드]{.hl}이면, $p$와 새 노드 $x$가 연속으로 두 개의 레드가 되어 — 위반이 발생합니다.

- 삽입 전에는 트리가 *유효했으므로*, $p$의 부모 $p_2$는 반드시 [블랙]{.hl}입니다.

- $p$의 형제 노드 $s$의 색상에 따라 나눕니다.

<div class="sub-item">

- **Case 1**: $s$가 레드.
- **Case 2**: $s$가 블랙.
  - **Case 2-1**: $x$가 $p$의 *오른쪽* 자식.
  - **Case 2-2**: $x$가 $p$의 *왼쪽* 자식.

</div>

</div>
<div>

<div style="height: 2rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">핵심 사실</div>
<div class="theorem-box-body">

조부모 $p_2$는 항상 블랙이며, 이것이 재색칠/회전 수선을 안전하게 만드는 근거입니다.

</div>
</div>

</div>
</div>

---
layout: prism
heading: "레드-블랙 수선 — Case 1 (재색칠)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- **Case 1** ($s$가 레드): $p$와 $s$를 레드에서 [블랙]{.hl}으로, $p_2$를 블랙에서 [레드]{.hl}로 재색칠합니다.

- 그런 다음:
  - $p_2$가 루트이면 다시 블랙으로 칠하고 종료하며,
  - 그렇지 않으면 $p_2$의 부모 $p_3$을 살펴 [재귀적]{.hl}으로 반복합니다.

- $p_3$이 블랙이면 완료이고, $p_3$이 레드이면 같은 충돌이 위로 옮겨간 것이므로 재귀합니다.

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
<p style="text-align:center; color:#9aa0a6; font-size:0.8rem;">p, s를 블랙으로, p₂를 레드로 바꾼 뒤 p₂의 부모를 확인</p>

</div>
</div>

---
layout: prism
heading: "레드-블랙 수선 — Case 2 (회전)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- **Case 2-1** ($s$가 블랙, $x$ = 오른쪽 자식): $p$를 중심으로 좌회전하여 Case 2-2로 변환합니다.

- **Case 2-2** ($s$가 블랙, $x$ = 왼쪽 자식): $p_2$를 중심으로 우회전한 뒤, $p$와 $p_2$의 [색상을 맞바꿉니다]{.hl}.

- 이 과정을 거치면 레드 두 개 위반이 사라지고 블랙 높이가 보존됩니다.

</div>
<div>

<div style="height: 0.5rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Case 2-1 &#8594; Case 2-2</div>
<div class="theorem-box-body" style="font-size:0.9rem;">

$p$를 중심으로 좌회전하여 $x$를 왼쪽 자식으로 만들면 Case 2-2로 귀착됩니다.

</div>
</div>

<div class="theorem-box" style="margin-top:0.8rem;">
<div class="theorem-box-title">Case 2-2 (마무리)</div>
<div class="theorem-box-body" style="font-size:0.9rem;">

$p_2$를 중심으로 우회전한 뒤, $p$(이제 서브 트리의 루트)와 $p_2$의 색상을 맞바꿉니다. $p$는 블랙이 되고 $p_2$는 레드가 됩니다.

</div>
</div>

</div>
</div>

---
layout: prism
heading: "DIY: 레드-블랙 삽입"
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
            if (s->color == RED) {                       // Case 1: 재색칠
                z->parent->color = BLACK; s->color = BLACK; z->parent->parent->color = RED; z = z->parent->parent;
            } else {
                if (z == z->parent->right) { z = z->parent; leftRotate(z); }   // Case 2-1 -> 2-2
                z->parent->color = BLACK; z->parent->parent->color = RED; rightRotate(z->parent->parent);
            }
        } else {                                         // 거울상
            Node* s = z->parent->parent->left;
            if (s->color == RED) {
                z->parent->color = BLACK; s->color = BLACK; z->parent->parent->color = RED; z = z->parent->parent;
            } else {
                if (z == z->parent->left) { z = z->parent; rightRotate(z); }
                z->parent->color = BLACK; z->parent->parent->color = RED; leftRotate(z->parent->parent);
            }
        }
    }
    root->color = BLACK;                                 // 루트는 항상 블랙
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
heading: "B-트리 — 동기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [디스크 접근]{.hl}은 메인 메모리 접근보다 엄청나게 느립니다 — 디스크 한 블록을 읽는 데 수백만 개의 기계어 명령을 처리하는 시간이 들 수 있습니다.

- 디스크 데이터는 [블록]{.hl} 단위로 접근합니다. 단 한 바이트를 읽거나 쓰더라도 블록 전체를 통째로 옮겨야 합니다.

- 앞에서 다룬 BST는 색인이 메모리에 있다고 가정했으나([내장 색인]{.hl}), 색인이 너무 크면 디스크에 두어야 합니다([외장 색인]{.hl}).

- 디스크에 색인을 둔다면, 디스크의 특성을 활용해 디스크 접근 시간으로 인한 비효율을 최소화해야 합니다.

---
layout: prism
heading: "B-트리 — 다진 검색"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 검색 트리의 [분기 수]{.hl}를 늘리면 기대 깊이가 낮아집니다.

- 10억 개의 키를 관리하는 완벽히 균형 잡힌 이진 트리는 깊이가 ~30으로 — 연산마다 최대 30번의 디스크 접근이 필요합니다.

- 1000진 분기라면 깊이가 단 4로 떨어져 — 연산마다 디스크 접근이 최대 4번입니다.

- 분기 수가 2를 넘는 검색 트리를 [다진 검색 트리]{.hl}라 하며, [B-트리]{.hl}는 디스크 환경에 잘 맞는 외장 다진 검색 트리입니다.

---
layout: prism
heading: "B-트리 — 노드 구조"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- B-트리 노드는 최대 $k$개의 키를 크기순으로 저장하며, 키가 $k$개이면 자식은 $k+1$개입니다.

- 서브 트리를 $T_0, T_1, T_2, \ldots$라 하면, 서브 트리 $T_i$의 모든 키는 $\text{key}_{i-1}$보다 크고 $\text{key}_{i}$보다 작습니다.

- 키의 자식 포인터 $p_i$는 디스크 [페이지]{.hl}를 가리킵니다. B-트리는 페이지를 효율적으로 쓰도록 각 노드가 적어도 *절반*은 차 있어야 하고($\lceil k/2 \rceil$개에서 $k$개 사이의 키), 모든 리프가 *같은* 깊이에 있어야 합니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image20.jpg" class="tikz-fig" style="width: 100%;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image22.jpg" class="tikz-fig" style="width: 100%; margin-top: 0.4rem;" />

</div>
</div>

---
layout: prism
heading: "B-트리 — 검색"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- B-트리 검색은 BST 검색과 같은 원리로 동작합니다.

- BST는 검색 키가 노드의 *유일한* 키와 일치하는지 확인하지만, B-트리는 노드에 있는 *여러* 키 중 일치하는 것이 있는지 확인합니다.

- BST는 하나의 키를 기준으로 왼쪽 또는 오른쪽으로 분기하지만, B-트리는 $\text{key}_{i-1} < x < \text{key}_{i}$인 쌍을 찾아 내려갈 자식을 정합니다.

- 그런 다음 리프에 이를 때까지 [재귀적]{.hl}으로 반복합니다.

---
layout: prism
heading: "B-트리 — 삽입"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- 키 $x$를 삽입하려면:
  - $x$가 들어갈 리프 노드 $r$을 검색하고,
  - $r$에 여유가 있으면 삽입 후 종료하며,
  - 없으면 *형제* 노드에 여유가 있는지 확인해 — 있으면 키를 하나 넘기고 종료하고,
  - 형제에도 여유가 없으면 노드를 둘로 [분리]{.hl}하며, 이때 키 하나가 부모로 올라갑니다.

<div class="sub-item" style="font-size:0.9rem;">

설정: 루트를 제외한 모든 노드는 **2~5개**의 키를 가져야 합니다.

</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image23.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">시작 B-트리</p>

</div>
</div>

---
layout: prism
heading: "B-트리 — 삽입 (여유와 재분배)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image24.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">9, 31 삽입: 리프에 여유가 있으므로 그냥 삽입</p>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image25.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">5 삽입: 오버플로우 — 형제에 여유가 있으므로 재분배</p>

</div>
</div>

---
layout: prism
heading: "B-트리 — 삽입 (분리)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image26.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">39 삽입: 형제에 여유가 없음 — 노드를 분리하고 키를 위로 올림</p>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image27.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">23, 35, 36 삽입: 리프에 여유가 있으므로 그냥 삽입</p>

</div>
</div>

---
layout: prism
heading: "DIY: B-트리 삽입"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int T = 3;                 // 최소 차수: 2*T-1 = 최대 5개 키 ("2~5개 키" 규칙에 대응)

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
heading: "B-트리 — 삭제"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 키 $x$를 삭제하려면:
  - $x$를 가진 노드를 검색하고,
  - 그 노드가 리프가 아니면 $x$의 [중위 후속자]{.hl} $y$를 가진 리프 $r$을 찾아 $x$와 $y$를 맞바꾸며,
  - 리프 $r$에서 $x$를 제거하고,
  - 제거로 [언더플로우]{.hl}가 발생하면 재분배로 해소합니다.

<div class="sub-item" style="font-size:0.9rem;">

설정: 루트를 제외한 모든 노드는 **2~5개**의 키를 가져야 합니다.

</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image28.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">시작 B-트리</p>

</div>
</div>

---
layout: prism
heading: "B-트리 — 삭제 (단순 삭제와 재분배)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image29.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">7 삭제: 그 리프에 키가 3개 있으므로 그냥 제거 후 종료</p>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w11/dsa-w11-image30.jpg" class="tikz-fig" style="width: 100%;" />
<p style="text-align:center; color:#9aa0a6; font-size:0.82rem;">4 삭제: 후속자 5와 맞바꿔 제거한 뒤, 언더플로우를 재분배</p>

</div>
</div>

---
layout: prism
heading: "B-트리 — 삭제 (언더플로우와 병합)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- **9 삭제**: 리프에서 제거한 후 [언더플로우]{.hl}가 발생합니다.

- 이를 해소하려고 *부모*에서 키를 하나 빌립니다. 이 때문에 위쪽에서 새 언더플로우가 생길 수 있으며, 이는 [재귀적]{.hl}으로(빌리기 / 병합) 처리합니다.

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

- 선호하는 코딩테스트 연습 플랫폼(백준, 프로그래머스 등)을 자유롭게 이용하세요.
  - 수업 시간에 다룬 프로그래머스 문제는 *제외*입니다.

- [정렬 또는 탐색]{.hl} 알고리즘을 사용하는 문제 **세 개**를 찾아 풀어보세요.
  - 나머지 조건은 지난 과제들과 같습니다.

- **또는**, 정렬 또는 탐색 알고리즘 *하나*를 골라 직접 손으로 정리해보세요.
  - 먼저 교과서로 한 번 복습한 뒤, *백지 상태*에서 시작하세요.

- `HW_W11_20XXXXXX.pdf`로 저장해 LMS에 업로드하세요.

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
