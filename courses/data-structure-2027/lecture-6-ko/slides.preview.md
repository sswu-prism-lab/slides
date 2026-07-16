---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 6 (KO)
download: true
info: |
  ## 자료구조 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-6/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">자료구조</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">6주차: 트리와 트라이</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">2027년 봄학기</p>
</div>

---
layout: prism
heading: 과목 커리큘럼
---

<div class="absolute left-10 right-10" style="top: 0rem; bottom: 0rem; display: grid; grid-template-columns: 1.2fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">과목 소개</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">기초 수학과 C++ 세부사항</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">알고리즘 분석</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">리스트, 스택, 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">원형 큐와 우선순위 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span class="text-gray-900 dark:text-gray-100">트리와 트라이</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">힙</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">그래프와 가중치 그래프</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">집합과 맵</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">해시 테이블</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">알고리즘 설계 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: "요약: 원형 큐 모델"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 배열 기반 큐 구현에는 한 가지 약점이 있다: `pop` 연산 이후, 앞쪽의 비워진 공간이 사용되지 않은 채로 남는다.

- [원형 큐]{.hl}는 *링 버퍼*라고도 불리며, 고정 크기의 단일 버퍼를 양 끝이 연결된 것처럼 사용한다.

- 연산은 *선입선출(FIFO)* 원칙을 따르지만, 저장 공간을 원형으로 감아 효율적으로 활용한다.

- 큐의 크기는 고정되어 있으며, 구현을 시작하는 시점에 결정된다.

</div>
<div>

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-01.svg" class="tikz-fig" style="width: 85%;" />

</div>
</div>

---
layout: prism
heading: "요약: 원형 큐 모델 — 포인터"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 큐의 시작과 끝이 원형으로 감겨 원을 이룬다.

- 원형 큐는 일반적으로 `front`와 `rear` 두 개의 포인터를 사용하여 첫 원소와 마지막 원소를 추적한다.
  - `front` 포인터는 큐의 *시작*을, `rear` 포인터는 그 *끝*을 가리킨다.

- 선형 큐와 마찬가지로, 이 구조는 각각 `push`와 `pop`에 해당하는 `enqueue`와 `dequeue` 연산을 가진다.

- `front`는 원소를 큐에서 제거하지 않고 맨 앞 원소를 반환한다.

---
layout: prism
heading: "요약: 우선순위 큐 모델"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [우선순위 큐]{.hl}는 최소 두 가지 연산을 허용하는 자료구조이다: 당연한 일을 하는 `insert`, 그리고 최소 원소를 찾아 반환하고 제거하는 `removeMin`.
  - `insert`는 `push`에 해당하고, `removeMin`은 우선순위 큐에서 `pop`에 해당한다.

- 대부분의 자료구조가 그렇듯 다른 연산을 추가할 수도 있지만, 이는 확장일 뿐 기본 모델의 일부는 아니다.

- 우선순위 큐는 운영체제, 정렬, 탐욕 알고리즘 등 다양한 응용을 가진다.

<div style="margin-top: 1.5rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-02.svg" class="tikz-fig" style="width: 55%;" />
</div>

---
layout: prism
heading: 트리와 트라이
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 많은 양의 입력에 대해, 연결 리스트의 선형 접근 시간은 감당하기 어렵다.

- 이번 강의에서는 대부분 연산의 평균 수행 시간이 $\mathcal{O}(\log N)$인 간단한 자료구조 — [이진 탐색 트리]{.hl} — 를 살펴보고, *최악의 경우*에도 이 한계를 보장하는 개념적으로 간단한 변형을 개략적으로 소개한다.

- 이번 강의에서는 이진 탐색 트리와 그 개선을 다룬다:

<div class="sub-item-enum">

1. 트리의 구조와 구현을 살펴본다.
2. 트리를 이용해 산술 표현식을 계산하는 방법을 살펴본다.
3. 평균 $\mathcal{O}(\log N)$ 시간의 탐색을 지원하고, 이 아이디어를 최악의 경우 $\mathcal{O}(\log N)$ 한계로 개선한다.
4. 다진 탐색 트리를 소개한다.

</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">이진 탐색 트리 ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">사전 지식</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">이진 트리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">이진 탐색 트리 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">AVL 트리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">레드-블랙 트리</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">다진 트리</span></p>
  </div>

</div>

---
layout: prism
heading: "사전 지식 — 트리의 정의"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [트리]{.hl}는 여러 방식으로 정의할 수 있으며, 자연스러운 한 가지 방법은 *재귀적* 정의이다.

- 트리는 노드들의 모임이다. 이 모임은 비어 있을 수 있고, 그렇지 않으면 [루트]{.hl}라 불리는 구별된 노드 $r$과, 각각의 루트가 $r$로부터 방향성 [엣지]{.hl}로 연결된 0개 이상의 비어 있지 않은 서브트리 $T_1, T_2, \ldots, T_k$로 구성된다.
  - 각 서브트리의 루트는 $r$의 *자식*이고, $r$은 각 서브트리 루트의 *부모*이다.

- $N$개의 노드를 가진 트리는 정확히 $N - 1$개의 엣지를 가진다.

</div>
<div>

<div style="height: 2.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-03.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "사전 지식 — 용어"
---

- 아래에서 *루트*는 $A$이고, 노드 $F$는 $A$를 부모로, $K$, $L$, $M$을 자식으로 가진다.
  - 각 노드는 임의의 개수의 자식을 가질 수 있으며, 없을 수도 있다. *조부모*와 *손자* 관계도 비슷하게 정의된다.

- 자식이 없는 노드는 [리프]{.hl}이며, 여기서 리프는 $B$, $C$, $H$, $I$, $P$, $Q$, $L$, $M$, $N$이다.

- 같은 부모를 가진 노드는 [형제자매]{.hl}이며, 따라서 $K$, $L$, $M$은 모두 형제자매이다.

<div style="margin-top: 0.5rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-04.svg" class="tikz-fig" style="width: 50%;" />
</div>

---
layout: prism
heading: "사전 지식 — 구현"
---

- 트리를 구현하는 한 가지 방법은 각 노드에 데이터 외에도 *각* 자식으로의 링크를 두는 것이다.
  - 노드당 자식 수는 다양하고 미리 알 수 없으므로, 자식들을 직접 링크로 두면 너무 많은 공간을 낭비할 수 있다.

- 이를 해결하기 위해, 각 노드의 자식들을 트리 노드의 *연결 리스트*로 유지한다.

<div style="margin-top: 1rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-05.svg" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: "사전 지식 — 첫 자식 / 다음 형제"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 그림은 구현에서 트리가 어떻게 표현되는지를 보여준다.

- 아래로 향하는 화살표는 `firstChild` 링크이고, 왼쪽에서 오른쪽으로 향하는 화살표는 `nextSibling` 링크이다.
  - 널 링크는 너무 많아 그리지 않았다.

- 노드 $E$는 형제($F$)로의 링크와 자식($I$)으로의 링크를 모두 가지는 반면, 어떤 노드는 둘 다 가지지 않는다.

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
heading: "이진 트리"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [이진 트리]{.hl}는 어떤 노드도 두 개를 초과하는 자식을 가질 수 없는 트리이다.
  - 이진 트리는 루트와 두 개의 서브트리 $T_L$, $T_R$로 구성되며, 둘 다 비어 있을 수 있다.

- 평균적인 이진 트리의 깊이는 $N$보다 상당히 작다.
  - 평균 깊이는 $\mathcal{O}(\sqrt{N})$이고, *이진 탐색 트리*의 경우 평균 깊이는 $\mathcal{O}(\log N)$이다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-06.svg" class="tikz-fig" style="width: 85%;" />

</div>
</div>

---
layout: prism
heading: "이진 트리 — 노드 선언"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>


- 이진 트리 노드는 최대 두 개의 자식을 가지므로, 그들로의 직접 링크를 유지할 수 있다.
  - 안타깝게도 깊이는 여전히 $N - 1$까지 커질 수 있다.

- 이 선언은 이중 연결 리스트의 것과 유사하다: 노드는 `element` 정보와 다른 노드를 가리키는 두 개의 포인터(`left`와 `right`)를 가진 구조체이다.

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
heading: "응용 — 표현 트리"
---

<div style="margin-top: 0.5rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-08.svg" class="tikz-fig" style="width: 68%;" />
</div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 위는 [표현 트리]{.hl}이다: 리프는 피연산자(상수 또는 변수 이름)이고, 나머지 노드는 연산자를 담는다.
  - 이는 $(a + b \cdot c) + ((d \cdot e + f) \cdot g)$를 나타낸다.

- 단항 마이너스 연산자처럼, 노드가 하나의 자식만 가질 수도 있다.

---
layout: prism
heading: "응용 — 순회"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 괄호로 묶인 왼쪽 표현식, 그다음 루트의 연산자, 그다음 괄호로 묶인 오른쪽 표현식을 생성하면 *중위* 표현식이 된다. 이 (왼쪽, 노드, 오른쪽) 전략이 [중위 순회]{.hl}이다.

- 왼쪽 서브트리, 오른쪽 서브트리, 그다음 연산자를 출력하면 *후위* 형태 $a\ b\ c\cdot +\ d\ e\cdot f + g\cdot +$ — [후위 순회]{.hl} — 가 된다.

- 연산자를 먼저 출력하고, 그다음 왼쪽과 오른쪽 서브트리를 출력하면 *전위* 형태 $+ + a \cdot b\ c \cdot + \cdot d\ e\ f\ g$ — [전위 순회]{.hl} — 가 된다.

---
layout: prism
heading: "DIY: 트리 순회"
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
    // (a + b) * c 에 대한 표현 트리
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
heading: "이진 탐색 트리 모델"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 이진 트리의 중요한 응용 중 하나는 *탐색*이다. 각 노드가 항목을 저장한다고 가정하자.

- 이진 트리를 [이진 탐색 트리]{.hl}로 만드는 성질은 다음과 같다: 모든 노드 $X$에 대해, 왼쪽 서브트리의 모든 항목은 $X$의 항목보다 *작고*, 오른쪽 서브트리의 모든 항목은 *크다*.

- 왼쪽 트리는 이진 탐색 트리이지만, 오른쪽 트리는 `7` 때문에 그렇지 않다.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-09.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "이진 탐색 트리 — contains, findMin, insert"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 이진 탐색 트리에는 다섯 가지 중요한 연산이 있다. `contains`는 $T$의 어떤 노드가 $X$를 담고 있으면 `true`를, 그렇지 않으면 `false`를 반환한다.

- `findMin`을 수행하려면, 루트에서 시작해 왼쪽 자식이 있는 한 계속 왼쪽으로 간다. 멈추는 지점이 *가장 작은* 원소이다.
  - `findMax`도 같지만 오른쪽으로 분기하여 *가장 큰* 원소에서 끝난다.

- $X$를 `insert`하려면 `contains`처럼 아래로 내려간다. $X$가 발견되면 아무것도 하지 않고, 그렇지 않으면 경로의 마지막 지점에 $X$를 삽입한다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-10.svg" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "이진 탐색 트리 — 제거"
---

- 삭제할 노드를 찾은 후에는 여러 경우가 발생한다:
  - 노드가 *리프*이면 즉시 삭제할 수 있다.
  - 노드가 *자식 하나*를 가지면, 부모가 링크로 그 노드를 건너뛴 뒤 삭제된다 (아래 왼쪽의 `remove` `4`).

- 복잡한 경우는 *자식 둘*을 가진 노드이다: 그 데이터를 오른쪽 서브트리의 가장 작은 데이터(쉽게 찾을 수 있음)로 바꾸고, 그 노드를 재귀적으로 삭제한다 (아래 오른쪽의 `remove` `2`).

<div style="margin-top: 0.8rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-11.svg" class="tikz-fig" style="width: 82%;" />
</div>

---
layout: prism
heading: "이진 탐색 트리 — 구현 (구조와 탐색)"
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
    else                       return true;         // 일치 발견
}

BinaryNode* findMin(BinaryNode* t) const {          // 가장 왼쪽 노드
    if (t == nullptr)          return nullptr;
    if (t->left == nullptr)    return t;
    return findMin(t->left);
}
```

---
layout: prism
heading: "이진 탐색 트리 — 구현 (insert와 remove)"
---

```cpp
void insert(const Comparable& x, BinaryNode*& t) {
    if (t == nullptr)          t = new BinaryNode{x, nullptr, nullptr};
    else if (x < t->element)   insert(x, t->left);
    else if (t->element < x)   insert(x, t->right);
    else                       ;                     // 중복: 아무것도 하지 않음
}

void remove(const Comparable& x, BinaryNode*& t) {
    if (t == nullptr)          return;               // 항목을 찾지 못함
    if (x < t->element)        remove(x, t->left);
    else if (t->element < x)   remove(x, t->right);
    else if (t->left != nullptr && t->right != nullptr) {   // 자식 둘
        t->element = findMin(t->right)->element;
        remove(t->element, t->right);
    } else {                                         // 자식 하나 또는 없음
        BinaryNode* oldNode = t;
        t = (t->left != nullptr) ? t->left : t->right;
        delete oldNode;
    }
}
```

---
layout: prism
heading: "DIY: 이진 탐색 트리 삽입 + 중위 순회"
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
    else if (x > t->key)  insert(t->right, x);   // 중복은 무시
}

void inorder(Node* t) {                          // 왼쪽, 노드, 오른쪽
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
    cout << "\nmin = " << findMin(root) << endl;   // 중위 순회는 항상 정렬된 순서를 낸다
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "이진 탐색 트리 — 평균 케이스 분석"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 우리는 모든 연산(`contains`, `findMin`, `findMax`, `insert`, `remove`)이 $\mathcal{O}(\log N)$ 시간이 걸리길 *기대*한다: 상수 시간에 한 레벨 내려가면서, 대략 절반 크기의 트리를 다루기 때문이다.

- 수행 시간은 $\mathcal{O}(d)$이며, 여기서 $d$는 접근된 항목을 담은 노드의 *깊이*이다.

- 모든 노드의 깊이의 합이 [내부 경로 길이]{.hl} $D(N)$이며, $D(1) = 0$이다. 그 평균은 다음을 만족한다

$$
D(N) = \frac{2}{N}\left[\sum_{j=0}^{N-1} D(j)\right] + N - 1.
$$

- 무작위 `insert` / `remove` 연산을 많이 수행하면, 트리는 *오른쪽으로 치우치는* 경향이 있다.

---
layout: prism
heading: "이진 탐색 트리 — 균형의 필요성"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 입력이 *정렬된 상태*로 들어오면, 연속된 삽입은 제곱 시간이 걸려 값비싼 연결 리스트가 된다: 트리가 왼쪽 자식이 없는 노드들로만 구성된다.

- 한 가지 해결책은 [균형]{.hl}이라 불리는 추가 구조 조건이다: 어떤 노드도 너무 깊어지지 못하게 한다.
  - 많은 균형 트리 알고리즘이 있으며, 대부분 표준 이진 탐색 트리보다 복잡하고 갱신에 평균적으로 더 오래 걸린다.

- 두 번째 방법은 균형을 포기하고 트리가 임의로 깊어지도록 허용하되, 각 연산 후 *재구조화 규칙*을 적용해 이후 연산을 효율적으로 유지한다. 이러한 구조를 [자가 수선]{.hl}이라 한다.

---
layout: prism
heading: "AVL 트리"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- [Adelson-Velskii와 Landis (AVL) 트리]{.hl}는 *균형 조건*을 가진 이진 탐색 트리이다.
  - 이 조건은 유지하기 쉬워야 하고 깊이가 $\mathcal{O}(\log N)$가 되도록 보장해야 한다.
  - 왼쪽과 오른쪽 서브트리의 높이가 같도록 요구하는 것만으로는 *충분하지 않다*.

- 모든 노드가 같은 높이의 서브트리를 갖도록 강요하는 것은 너무 엄격하다: 비어 있는 서브트리의 높이를 $-1$로 두면 $2^k - 1$개 노드의 완전 균형 트리만이 조건을 만족하므로, 조건을 완화해야 한다.

</div>
<div>

<div style="height: 0rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-12.svg" class="tikz-fig" style="width: 65%;" />

</div>
</div>

---
layout: prism
heading: "AVL 트리 — 균형 조건"
---

- AVL 트리는 모든 노드에 대해 왼쪽과 오른쪽 서브트리의 높이 차이가 최대 $1$인 이진 탐색 트리이다.
  - 아래 *왼쪽* 트리만이 AVL 트리이다.

- AVL 트리의 높이는 최대 약 $1.44 \log(N + 2) - 1.328$이지만, 실제로는 $\log N$보다 약간만 크다.

- 삽입과 삭제를 제외하면, 모든 트리 연산은 $\mathcal{O}(\log N)$ 시간에 수행할 수 있다.

<div style="margin-top: 0rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-13.svg" class="tikz-fig" style="width: 52%;" />
</div>

---
layout: prism
heading: "AVL 트리 — 네 가지 경우"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 삽입 시, 루트로 돌아가는 경로상의 노드들에 대해 균형 정보를 갱신한다. 삽입이 AVL 성질을 위반할 수 있으며, 삽입이 끝나기 전에 이를 복구해야 한다.
  - 이는 언제나 [회전]{.hl}이라는 간단한 변형으로 해결할 수 있다.

- 재균형할 노드를 $\alpha$라 하자. 위반은 네 가지 경우에 발생할 수 있다:

<div class="sub-item-enum">

1. $\alpha$의 *왼쪽* 자식의 *왼쪽* 서브트리에 삽입.
2. $\alpha$의 *왼쪽* 자식의 *오른쪽* 서브트리에 삽입.
3. $\alpha$의 *오른쪽* 자식의 *왼쪽* 서브트리에 삽입.
4. $\alpha$의 *오른쪽* 자식의 *오른쪽* 서브트리에 삽입.

</div>

- 경우 1과 4는 거울 대칭이고(2와 3도 마찬가지), 이론적으로는 두 가지 기본 경우지만 프로그래밍에서는 여전히 네 가지 경우이다.

---
layout: prism
heading: "AVL — 단일 회전"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 첫 번째와 마지막 경우 — *바깥쪽*(왼쪽-왼쪽 또는 오른쪽-오른쪽) 삽입 — 은 [단일 회전]{.hl}으로 해결된다.

- 재균형하려면 $X$를 한 레벨 올리고 $Z$를 한 레벨 내려서, 노드들을 동등한 트리로 재배열한다.

- 직관적인 그림: 자식(피봇) $k_1$을 잡고 중력에 맡기면 $k_1$이 새 루트가 된다.
  - $k_2 > k_1$이므로 $k_2$는 $k_1$의 오른쪽 자식이 되고, $X$와 $Z$는 각각 $k_1$의 왼쪽 자식과 $k_2$의 오른쪽 자식으로 남는다.
  - $k_1$과 $k_2$ 사이의 항목을 담은 서브트리 $Y$는 $k_2$의 왼쪽 자식이 되어 모든 순서 요구를 만족한다.

---
layout: prism
heading: "AVL — 단일 회전 (추상)"
---

<div style="margin-top: 0rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-14.svg" class="tikz-fig" style="width: 60%;" />
</div>

- 피봇 $k_1$이 루트로 올라가고, $k_2$가 그 오른쪽 자식이 되며, ($k_1$과 $k_2$ 사이의) 서브트리 $Y$가 $k_2$의 왼쪽 자식으로 다시 붙는다.

---
layout: prism
heading: "AVL — 단일 회전 (예시)"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 아래에서 `6`을 삽입하여 AVL 성질이 깨지고, 이후 *단일 회전*으로 복구된다.

- 네 번째 경우는 대칭이며, 마찬가지로 단일 회전으로 해결된다.

<div style="margin-top: 1rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-15.svg" class="tikz-fig" style="width: 72%;" />
</div>

---
layout: prism
heading: "AVL — 이중 회전"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- 단일 회전 알고리즘은 두 번째와 세 번째 경우에는 작동하지 *않는다*: 서브트리 $Y$가 너무 깊어서, 단일 회전을 해도 여전히 그만큼 깊다.

- 두 번째와 세 번째 경우 — *안쪽*(왼쪽-오른쪽 또는 오른쪽-왼쪽) 삽입 — 은 약간 더 복잡한 [이중 회전]{.hl}으로 처리한다.

- 이를 고치려면, 한 번의 회전으로 왼쪽-오른쪽 트리를 왼쪽-왼쪽 트리로 바꾼 뒤, 추가 회전으로 균형을 맞춘다 (반대의 경우도 마찬가지).

---
layout: prism
heading: "AVL — 단일 회전이 실패하는 이유"
---

<div style="margin-top: 0rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-16.svg" class="tikz-fig" style="width: 60%;" />
</div>

- $k_2$와 $k_1$을 회전해도 깊은 서브트리 $Y$(빨강)가 같은 깊이에 남는다 — 불균형이 해소되지 않으므로 여기서는 단일 회전으로 충분하지 않다.

---
layout: prism
heading: "AVL — 이중 회전 (예시)"
---

- $k_3$를 루트로 남겨둘 수 없고, $k_3$와 $k_1$ 사이의 회전도 작동하지 않으므로 $k_2$가 새 루트가 된다.

- 이로 인해 $k_1$은 $k_2$의 왼쪽 자식, $k_3$는 오른쪽 자식이 되며, 네 서브트리의 위치가 완전히 결정된다.

- 그 결과는 AVL 성질을 만족하고 높이를 삽입 전 값으로 복원하므로, 모든 재균형과 높이 갱신이 완료된다.

<div style="margin-top: 0.6rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-17.svg" class="tikz-fig" style="width: 60%;" />
</div>

---
layout: prism
heading: "AVL — 이중 회전 (추상)"
---

<div style="margin-top: 0rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-18.svg" class="tikz-fig" style="width: 60%;" />
</div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 가운데 노드 $k_2$가 루트로 올라가고, $k_1$과 $k_3$가 그 자식이 되며, 네 서브트리 $A$, $B$, $C$, $D$가 순서 성질을 만족하도록 배치된다.

---
layout: prism
heading: "AVL — 구현 (노드와 회전)"
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
void rotateWithLeftChild(AvlNode*& k2) {            // 단일 회전 (LL 경우)
    AvlNode* k1 = k2->left;
    k2->left  = k1->right;
    k1->right = k2;
    k2->height = max(height(k2->left), height(k2->right)) + 1;
    k1->height = max(height(k1->left), k2->height) + 1;
    k2 = k1;
}
void doubleWithLeftChild(AvlNode*& k3) {            // 이중 회전 (LR 경우)
    rotateWithRightChild(k3->left);
    rotateWithLeftChild(k3);
}
```

---
layout: prism
heading: "AVL — 구현 (insert와 balance)"
---

```cpp
static const int ALLOWED_IMBALANCE = 1;

void insert(const Comparable& x, AvlNode*& t) {
    if (t == nullptr)          t = new AvlNode{x, nullptr, nullptr};
    else if (x < t->element)   insert(x, t->left);
    else if (t->element < x)   insert(x, t->right);
    balance(t);                                      // 올라오는 길에 재균형
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
heading: "HW: 완전한 AVL 트리 클래스 구현하기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 위의 AVL 트리 코드를 확장하여 `remove` 메서드도 구현하라.
  - 아래 드라이버로 테스트하라.

- C++ 코드를 LMS에 `20XXXXXX_HW_W06.cpp`로 업로드하라.

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
heading: "레드-블랙 트리"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 역사적으로 AVL 트리의 인기 있는 대안은 [레드-블랙 트리]{.hl}이다. 연산은 최악의 경우 $\mathcal{O}(\log N)$ 시간이 걸리며, 세심하게 작성한 비재귀적 `insert`는 AVL 트리에 비해 비교적 수월하다.

- 레드-블랙 트리는 다음 컬러링 성질을 가진 이진 탐색 트리이다:

<div class="sub-item-enum">

1. 모든 노드는 *레드* 또는 *블랙*으로 칠해진다.
2. 루트는 *블랙*이다.
3. 노드가 *레드*이면, 그 자식은 반드시 *블랙*이어야 한다.
4. 노드에서 널 포인터까지의 모든 경로는 같은 수의 *블랙* 노드를 포함해야 한다.

</div>

- 그 결과 높이는 최대 $2\log(N + 1)$이므로, 탐색은 로그 시간이 보장된다.

---
layout: prism
heading: "레드-블랙 트리 — 예시"
---

<div style="margin-top: 0rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-19.svg" class="tikz-fig" style="width: 70%;" />
</div>

- 루트에서 널까지의 모든 경로는 같은 수의 블랙 노드를 지나며, 어떤 레드 노드도 레드 자식을 갖지 않는다.

---
layout: prism
heading: "레드-블랙 트리 — 삽입"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 네 번째 조건 때문에, 삽입된 항목 $X$는 반드시 *레드*로 칠해야 한다.

- 새로 삽입된 노드의 부모 $P$가 *블랙*이면, 위반이 없다.

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-20.svg" class="tikz-fig" style="width: 68%;" />
</div>

- 부모가 이미 *레드*이면, 연속된 레드 노드로 조건 3을 위반하므로, (조건 4를 위반하지 않으면서) 트리를 조정해야 한다. 이를 위한 기본 연산은 *색 변경*과 *트리 회전*이다.

---
layout: prism
heading: "레드-블랙 트리 — 경우 1 (레드 형제)"
---

- $P$는 레드이지만, 그 부모 $G$($X$의 조부모)는 반드시 블랙이다. $P$의 형제 $S$의 색에 따라 두 가지 경우가 있다:

<div class="sub-item-enum">

1. $S$가 *레드*이다.
2. $S$가 *블랙* 또는 *비어 있음* — 하위 경우 (a) $X$가 $P$의 오른쪽 자식, (b) $X$가 $P$의 왼쪽 자식.

</div>

- 경우 1에서는 $P$와 $S$를 *블랙*으로, $G$를 *레드*로 바꾼다.
  - $G$가 루트이면 다시 블랙으로 바꾸고, 그렇지 않으면 그 부모($X$의 증조부모)를 재귀적으로 확인한다.

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-21.svg" class="tikz-fig" style="width: 52%;" />
</div>

---
layout: prism
heading: "레드-블랙 트리 — 경우 2 (블랙 형제)"
---

- 경우 2.1에서는 $P$를 피봇으로 *좌회전*하여 트리를 경우 2.2로 변환한다.

<div style="margin-top: 0.3rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-22.svg" class="tikz-fig" style="width: 40%;" />
</div>

- 경우 2.2에서는 $G$를 피봇으로 *우회전*하고, $P$와 $G$의 색을 서로 바꾼다.

<div style="margin-top: 0.3rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-23.svg" class="tikz-fig" style="width: 40%;" />
</div>

---
layout: prism
heading: "HW: 레드-블랙 트리 클래스 구현하기"
---

- 레드-블랙 트리의 삭제 메커니즘을 찾아보라.
  - 삽입 메커니즘과 비슷하게 경우가 나뉜다.

- AVL 트리 클래스를 바탕으로, 레드-블랙 트리 클래스를 구현하고 테스트하라.

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
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">이진 탐색 트리 ADT</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">다진 트리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">다진 트리 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">B-트리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">2-3 및 2-3-4 트리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">트라이</span></p>
  </div>

</div>

---
layout: prism
heading: "다진 트리 모델 — 디스크 입출력"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 지금까지 우리는 전체 자료구조가 메인 메모리에 들어간다고 가정했다. 대신 메모리에 들어가지 않을 만큼 데이터가 많아서 *디스크*에 있어야 한다고 하자.

- 빅오 분석은 모든 연산이 동등하다고 가정하지만, 디스크 입출력이 관여하면 이는 사실이 아니다.
  - 현대 컴퓨터는 초당 수십억 개의 명령을 실행하지만, 디스크는 *기계적*이어서 그 속도는 디스크를 회전시키고 헤드를 이동하는 데 달려 있다.

- 메인 메모리에 들어가지 않는 10,000,000개의 항목이 있다면:
  - 불균형 이진 탐색 트리는 재앙이다 — 선형 깊이로, 최대 10,000,000번의 디스크 접근.
  - AVL 트리는 평균 약 25번의 디스크 접근을 사용한다.
  - 디스크 접근을 3이나 4 같은 아주 작은 상수로 줄이고자 한다.

---
layout: prism
heading: "다진 트리 모델"
---

- [다진 트리]{.hl}([$M$진 트리]{.hl}라고도 함)는 $M$-갈래 분기를 허용한다.

- 이진 탐색 트리를 만드는 것과 거의 같은 방식으로 다진 *탐색* 트리를 만들 수 있다.

- 이진 탐색 트리에서는 두 갈래 중 하나를 결정하는 데 키 하나가 필요하지만, 다진 탐색 트리에서는 어느 갈래로 갈지 결정하는 데 $M - 1$개의 키가 필요하다.
  - 최악의 경우에도 효율적이려면, 탐색 트리는 *균형*이 맞아야 한다.

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-24.svg" class="tikz-fig" style="width: 68%;" />
</div>

---
layout: prism
heading: "B-트리"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.55em;
}
</style>

- [B-트리]{.hl}는 소수의 디스크 접근만을 보장한다. $M$차 B-트리는 다음을 만족하는 $M$진 트리이다:

<div class="sub-item-enum">

1. 데이터 항목은 *리프*에 저장된다.
2. 리프가 아닌 노드는 탐색을 안내하기 위한 최대 $M - 1$개의 키를 저장하며, 키 $i$는 서브트리 $i + 1$의 가장 작은 키이다.
3. 루트는 리프이거나, $2$개에서 $M$개 사이의 자식을 가진다.
4. 루트를 제외한 리프가 아닌 모든 노드는 $\lceil M/2 \rceil$개에서 $M$개 사이의 자식을 가진다.
5. 모든 리프는 같은 깊이에 있으며, $\lceil L/2 \rceil$개에서 $L$개 사이의 데이터 항목을 가진다.

</div>

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-25.svg" class="tikz-fig" style="width: 74%;" />
</div>

---
layout: prism
heading: "2-3 트리"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [2-3 트리]{.hl}는 모든 내부 노드가 두 자식과 하나의 데이터 원소(*2-노드*)를 갖거나 세 자식과 두 데이터 원소(*3-노드*)를 갖는 트리이다.
  - 2-3 트리는 3차 B-트리이다.

- 2-3 트리는 *균형*이 맞아야 한다: 모든 리프가 같은 레벨에 있다.

- 노드의 왼쪽, 가운데, 오른쪽 서브트리는 각각 같거나 비슷한 양의 데이터를 담는다.

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-26.svg" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: "2-3-4 트리"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [2-3-4 트리]{.hl}(2-4 트리라고도 함)는 *딕셔너리*를 구현할 수 있는 자기 균형 자료구조이다.
  - 2-3-4 트리는 4차 B-트리이다.

- 이 숫자들은 모든 내부 노드가 두 개, 세 개, 또는 네 개의 자식 노드를 갖는 트리를 뜻한다.

- 2-3-4 트리는 레드-블랙 트리와 *동형*이다 — 이들은 동등한 자료구조이다.

<div style="margin-top: 0.4rem; display: flex; justify-content: center;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-27.svg" class="tikz-fig" style="width: 74%;" />
</div>

---
layout: prism
heading: "트라이"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [트라이]{.hl}(*전위 트리* 또는 *디지털 트리*라고도 함)는 집합 내에서 특정 키를 찾는 데 사용되는 탐색 트리의 일종이다.
  - 이 이름은 re[trie]{.hl}val tree에서 유래했다.

- 이 키들은 보통 문자열이며, 트라이는 자동완성, 맞춤법 검사, IP 라우팅 등 대규모 문자열 데이터셋을 다루는 응용에 탁월한 선택이 된다.

- 중요한 성질:
  - 노드들은 표현하는 문자열 키의 공통 접두사를 공유하여, 메모리 사용과 탐색 효율을 최적화한다.
  - 문자열을 탐색하려면, 그 문자들이 지시하는 경로를 따라 트리를 순회한다.
  - 문자열의 끝을 나타내는 노드는 문자열의 존재를 표시하기 위해 특별히(값이나 플래그로) 표시된다.

---
layout: prism
heading: "트라이 — 구조"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 트라이의 루트 노드는 보통 *빈 문자열*을 나타내며 어떤 문자도 담지 않는다.
  - 각 자식은 문자열의 *다음 문자*를 나타낸다.
  - 이 구조는 각 레벨이 문자열의 한 문자에 대응하는 계층적 트리를 만든다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w06-28.svg" class="tikz-fig" style="width: 65%;" />

</div>
</div>

---
layout: prism
heading: "트라이 — 복잡도"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 트라이는 주로 문자열 집합을 표현하며, 탐색, 삽입, 삭제를 효율적으로 지원한다.

- 트라이에서 문자열을 탐색하는 시간 복잡도는 $\mathcal{O}(m)$이며, $m$은 문자열의 길이이다.
  - 이는 특히 문자열 수가 많은 데이터셋에서 탐색을 매우 효율적으로 만든다.

- 트라이는 노드와 포인터를 저장하기 때문에, 특히 짧은 문자열이 많을 때 메모리를 많이 소모할 수 있다.
  - 공통 접두사가 노드 간에 공유되므로, 겹치는 문자열을 많이 저장할 때 트라이가 다른 구조보다 공간 효율적일 수 있다.

---
layout: prism
heading: "DIY: 트라이 삽입 + 탐색"
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
    cur->isEnd = true;                       // 저장된 단어의 끝을 표시
}

bool search(TrieNode* root, const string& word) {
    TrieNode* cur = root;
    for (char c : word) {
        int i = c - 'a';
        if (!cur->child[i]) return false;    // 접두사가 없음
        cur = cur->child[i];
    }
    return cur->isEnd;                        // 플래그가 있어야만 완전한 단어
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

# ***감사합니다!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
