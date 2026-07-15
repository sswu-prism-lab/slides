# 트리

트리는 루트 노드 $r$과, 비어 있거나 혹은 비어 있지 않은 서브트리들 $T_1, T_2, \dots, T_k$로 구성되며, 각 서브트리는 $r$과 엣지<span class="gloss">edge</span>(링크<span class="gloss">link</span>라고도 함)로 연결되어 있다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-12.svg" alt="루트 r과 서브트리 T1..Tk로 구성된 트리" style="max-width: 460px;" />
  <figcaption class="cap">트리는 루트 $r$과 여러 서브트리 $T_1, \dots, T_k$의 재귀적 구조이다.</figcaption>
</figure>

각 서브트리의 루트 노드는 $r$의 자식 노드이며, $r$은 각 서브트리 루트들의 부모 노드이다.

- 각 노드는 임의의 수의 자식을 가질 수 있으며, 없을 수도 있다.
- 조부모<span class="gloss">grandparent</span>, 손자<span class="gloss">grandchildren</span> 관계도 비슷한 방식으로 정의된다.

## 트리 용어

아래 트리를 기준으로 용어를 정리한다.

- **루트<span class="gloss">root</span>**: 부모가 없는 최상위 노드. 아래 트리에서는 $A$.
- **부모/자식**: 노드 $F$는 $A$를 부모로 가지고, $K$, $L$, $M$을 자식으로 가진다.
- **리프<span class="gloss">leaf</span>**: 자식이 없는 노드. 아래 트리에서는 $B$, $C$, $H$, $I$, $P$, $Q$, $L$, $M$, $N$.
- **형제자매<span class="gloss">sibling</span>**: 같은 부모를 가진 노드. $K$, $L$, $M$은 형제자매이다.
- **깊이<span class="gloss">depth</span>**: 루트에서 그 노드까지의 경로 길이(루트의 깊이는 0).
- **높이<span class="gloss">height</span>**: 그 노드에서 가장 깊은 리프까지의 경로 길이(리프의 높이는 0). 트리의 높이는 루트의 높이이다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-13.svg" alt="일반 트리 예시 (루트 A와 여러 자식)" style="max-width: 620px;" />
  <figcaption class="cap">일반 트리: 노드는 임의 개수의 자식을 가질 수 있다.</figcaption>
</figure>

## 일반 트리의 구현: 왼쪽 자식-오른쪽 형제

일반 트리는 노드마다 자식 수가 다르므로, 자식마다 포인터를 두면 공간이 낭비된다. 대신 임의 노드의 **첫 번째 자식 노드**와 **바로 옆 형제자매 노드**를 잇는 연결 리스트를 사용하는 것이 합리적이다(왼쪽 자식-오른쪽 형제<span class="gloss">left-child right-sibling</span> 표현).

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-14.svg" alt="왼쪽 자식-오른쪽 형제 방식의 트리 표현" style="max-width: 620px;" />
  <figcaption class="cap">각 노드는 "첫 자식"과 "다음 형제" 두 포인터만으로 임의 개수의 자식을 표현한다.</figcaption>
</figure>

## 이진 트리

이진 트리<span class="gloss">binary tree</span>란 어떠한 노드도 2개보다 많은 자식을 갖지 않는 트리를 의미한다.

- 이진 트리의 깊이는 $N$보다 현저하게 작을 수 있으며, 이는 이진 트리의 중요한 성질이다.
- 평균적으로 $\mathcal{O}(\sqrt{N})$의 깊이를 가지며, 이진 트리의 특별한 경우인 이진 탐색 트리는 $\mathcal{O}(\log N)$만큼의 깊이를 가진다.

일반적인 트리와 달리, 이진 트리는 자식을 최대 2개만 가지므로 노드 클래스를 선언할 때 자식 노드를 직접 가리키는 포인터를 사용해도 공간 복잡도<span class="gloss">space complexity</span>의 낭비가 없다.

### 표현 트리와 순회

아래 표현 트리<span class="gloss">expression tree</span>는 $(a + b \cdot c) + ((d \cdot e + f) \cdot g)$를 표현한 이진 트리이다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-15.svg" alt="수식의 표현 트리" style="max-width: 560px;" />
  <figcaption class="cap">$(a + b \cdot c) + ((d \cdot e + f) \cdot g)$의 표현 트리.</figcaption>
</figure>

순회<span class="gloss">traversal</span>는 노드를 방문하는 순서에 따라 세 가지로 나뉜다. 방문(노드값 출력)의 위치가 **가운데/뒤/앞** 중 어디인지가 이름과 결과를 결정한다.

**중위 순회<span class="gloss">inorder traversal</span>** — 방문이 `가운데`. 표현 트리를 중위 순회하면 중위 표기법<span class="gloss">infix notation</span>의 수식을 얻는다.

```cpp
void inOrder(BinaryNode* node) {
    if (node != nullptr) {
        inOrder(node->left);         // 왼쪽 자식
        cout << node->key << " ";    // in-order 방문
        inOrder(node->right);        // 오른쪽 자식
    }
}
```

**후위 순회<span class="gloss">postorder traversal</span>** — 방문이 `뒤`. 표현 트리를 후위 순회하면 후위 표기법<span class="gloss">postfix notation</span> $a\ b\ c\cdot +\ d\ e\cdot f + g\cdot +$를 얻는다.

```cpp
void postOrder(BinaryNode* node) {
    if (node != nullptr) {
        postOrder(node->left);       // 왼쪽 자식
        postOrder(node->right);      // 오른쪽 자식
        cout << node->key << " ";    // post-order 방문
    }
}
```

**전위 순회<span class="gloss">preorder traversal</span>** — 방문이 `앞`. 표현 트리를 전위 순회하면 전위 표기법<span class="gloss">prefix notation</span> $+ + a \cdot b\ c \cdot + \cdot d\ e\ f\ g$를 얻는다.

```cpp
void preOrder(BinaryNode* node) {
    if (node != nullptr) {
        cout << node->key << " ";    // pre-order 방문
        preOrder(node->left);        // 왼쪽 자식
        preOrder(node->right);       // 오른쪽 자식
    }
}
```

이 세 순회는 깊이 우선(재귀)인 반면, **레벨 순서 순회**<span class="gloss">level-order traversal</span>는 너비 우선으로 루트부터 레벨을 따라 위에서 아래로, 각 레벨은 왼쪽에서 오른쪽으로 방문한다. 큐를 이용해 구현한다.

::: tip 순회 이름 외우는 법
방문(출력) 시점이 **앞이면 전위(pre)**, **가운데면 중위(in)**, **뒤면 후위(post)**. 세 순회 모두 왼쪽 → 오른쪽 순서로 자식을 내려간다는 점은 같다.
:::

---

# 이진 탐색 트리

이진 트리가 사용되는 중요한 응용은 탐색<span class="gloss">searching</span>이다.

이진 탐색 트리<span class="gloss">binary search tree</span>는 이진 트리 중 하나이며, 임의의 노드 $X$에 대해 그 **왼쪽 서브트리의 원소들은 전부 $X$보다 작고, 오른쪽 서브트리의 원소들은 전부 $X$보다 크다**는 성질을 가진다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-16.svg" alt="이진 탐색 트리인 경우와 아닌 경우" style="max-width: 560px;" />
  <figcaption class="cap">왼쪽은 이진 탐색 트리이지만, 오른쪽은 4의 오른쪽 자식 `7`이 조상 6보다 커서 성질을 위반한다.</figcaption>
</figure>

## BST의 다섯 가지 연산

- `contains`: 찾고자 하는 원소 $X$가 트리 $T$에 있으면 `true`, 없으면 `false`를 반환한다. 루트에서 시작해 $X$와 비교하며 작으면 왼쪽, 크면 오른쪽으로 내려간다.
- `findMin`: 루트부터 시작하여 가장 왼쪽 리프까지 가면 가장 작은 원소를 찾는다.
- `findMax`: 루트부터 시작하여 가장 오른쪽 리프까지 가면 가장 큰 원소를 찾는다.
- `insert`: 우선 $X$의 위치를 탐색하고, 이미 $X$가 있으면 종료, 없으면 그 자리(리프)에 삽입한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-17.svg" alt="BST에 5를 삽입하는 과정" style="max-width: 460px;" />
  <figcaption class="cap"><code>insert(5)</code>: 탐색이 끝난 리프 자리에 새 노드를 붙인다.</figcaption>
</figure>

`remove` 연산은 몇 가지 경우로 나누어 고려한다.

1. $X$가 **리프 노드**이면 그냥 삭제 후 종료한다.
2. $X$의 자식 노드가 **1개**이면, 그 자식 노드를 $X$의 부모 노드에 연결시킨 후 종료한다.
3. $X$의 자식 노드가 **2개**이면, $X$의 오른쪽 서브트리 중 가장 작은 원소(후계자<span class="gloss">successor</span>)를 찾아 $X$ 자리에 옮긴 뒤, 오른쪽 서브트리에서 그 후계자를 재귀적으로 제거한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-18.svg" alt="BST에서 노드를 삭제하는 과정" style="max-width: 620px;" />
  <figcaption class="cap"><code>remove</code>: 자식이 하나면 자식을 끌어올리고, 둘이면 오른쪽 서브트리의 최소값(후계자)으로 대체한다.</figcaption>
</figure>

## 편향의 문제

BST의 연산 비용은 트리의 높이에 비례한다. 균형이 잘 잡히면 평균 $\mathcal{O}(\log N)$이지만, 정렬된 순서로 삽입하는 등 트리가 한쪽으로 **편향**되면 사실상 연결 리스트가 되어 최악의 경우 $\mathcal{O}(N)$이 된다. 이 문제를 해결하는 것이 아래의 AVL 트리와 레드-블랙 트리이다.

## 실습 — BST와 세 가지 순회

노드를 삽입하고 전위·중위·후위 순회의 방문 순서를 출력한다. **중위 순회는 항상 정렬된 순서**로 나온다는 점, 그리고 자식이 2개인 노드를 삭제할 때 후계자로 대체된다는 점을 확인하자. (시험의 전위/후위 순회 문제와 직결된다.)

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class BinaryNode {
public:
    int key;
    BinaryNode* left;
    BinaryNode* right;
    BinaryNode(int value) : key(value), left(nullptr), right(nullptr) {}
};

class BinarySearchTree {
public:
    BinarySearchTree() : root(nullptr) {}

    void insert(int key) { root = _insert(root, key); }
    void remove(int key) { root = _remove(root, key); }

    int findMin() {
        if (root == nullptr) { cout << "The tree is empty." << endl; return -1; }
        return _findMin(root)->key;
    }
    int findMax() {
        if (root == nullptr) { cout << "The tree is empty." << endl; return -1; }
        return _findMax(root)->key;
    }

    void preOrder()  { _preOrder(root);  cout << endl; }
    void inOrder()   { _inOrder(root);   cout << endl; }
    void postOrder() { _postOrder(root); cout << endl; }

private:
    BinaryNode* root;

    BinaryNode* _insert(BinaryNode* node, int key) {
        if (node == nullptr) return new BinaryNode(key);
        else if (key < node->key) node->left  = _insert(node->left, key);
        else if (key > node->key) node->right = _insert(node->right, key);
        return node;
    }

    BinaryNode* _remove(BinaryNode* node, int key) {
        if (node == nullptr) return node;
        if (key < node->key)      node->left  = _remove(node->left, key);
        else if (key > node->key) node->right = _remove(node->right, key);
        else {
            if (node->left == nullptr) {          // 오른쪽 자식만 존재
                BinaryNode* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == nullptr) {  // 왼쪽 자식만 존재
                BinaryNode* temp = node->left;
                delete node;
                return temp;
            }
            BinaryNode* temp = _findMin(node->right); // 자식 2개: 후계자로 대체
            node->key = temp->key;
            node->right = _remove(node->right, temp->key);
        }
        return node;
    }

    void _preOrder(BinaryNode* node) {
        if (node != nullptr) {
            cout << node->key << " ";
            _preOrder(node->left);
            _preOrder(node->right);
        }
    }
    void _inOrder(BinaryNode* node) {
        if (node != nullptr) {
            _inOrder(node->left);
            cout << node->key << " ";
            _inOrder(node->right);
        }
    }
    void _postOrder(BinaryNode* node) {
        if (node != nullptr) {
            _postOrder(node->left);
            _postOrder(node->right);
            cout << node->key << " ";
        }
    }

    BinaryNode* _findMin(BinaryNode* node) {
        BinaryNode* current = node;
        while (current && current->left != nullptr) current = current->left;
        return current;
    }
    BinaryNode* _findMax(BinaryNode* node) {
        BinaryNode* current = node;
        while (current && current->right != nullptr) current = current->right;
        return current;
    }
};

int main() {
    BinarySearchTree bst;
    int keys[] = {6, 2, 8, 1, 4, 3, 7};
    for (int k : keys) bst.insert(k);

    cout << "preorder : "; bst.preOrder();
    cout << "inorder  : "; bst.inOrder();
    cout << "postorder: "; bst.postOrder();
    cout << "min = " << bst.findMin() << ", max = " << bst.findMax() << endl;

    bst.remove(2); // 자식 2개 -> 후계자 3으로 대체
    cout << "after remove(2), inorder: "; bst.inOrder();
    return 0;
}
```

</CppRunner>

출력에서 중위 순회는 `1 2 3 4 6 7 8`로 항상 정렬됨을 확인하라.

---

# AVL 트리

만약 이진 트리의 균형<span class="gloss">balance</span>이 맞지 않다면, 평균적으로 $\mathcal{O}(\log N)$인 연산들이 최악의 경우 $\mathcal{O}(N)$의 시간 복잡도를 소모하게 된다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-19.svg" alt="오른쪽으로 편향된 트리" style="max-width: 300px;" />
  <figcaption class="cap">임의 노드의 자식이 2개 이하이므로 이진 트리이지만, 오른쪽으로 편향<span class="gloss">right-heavy</span>되어 대부분의 연산이 $\mathcal{O}(N)$이다.</figcaption>
</figure>

균형을 유지하는 트리는, 어떠한 서브트리도 너무 깊어지지 않도록 제한하여 최악의 경우에도 $\mathcal{O}(\log N)$의 성능을 보장한다.

AVL 트리<span class="gloss">Adelson-Velskii and Landis tree</span>는 균형 조건<span class="gloss">balance condition</span>을 만족하는 이진 탐색 트리이다.

- AVL 트리는 임의의 노드에서, 왼쪽 서브트리와 오른쪽 서브트리의 깊이<span class="gloss">depth</span> 차가 $1$ 이하인 성질을 가진다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-20.svg" alt="AVL 트리인 경우와 아닌 경우" style="max-width: 560px;" />
  <figcaption class="cap">왼쪽은 AVL 트리이지만, 오른쪽은 `7` 노드의 좌우 서브트리 깊이 차가 2라서 AVL 트리가 아니다.</figcaption>
</figure>

## 회전으로 균형 맞추기

AVL 트리의 삽입과 삭제는 연산 후 AVL 특성을 깰 수 있으므로, 연산 종료 전에 트리를 수선하여 균형을 다시 맞춰야 한다. 이는 회전<span class="gloss">rotation</span>이라 불리는 간단한 트리 변형으로 이루어진다.

AVL 균형을 깬 노드(왼쪽·오른쪽 서브트리 깊이 차가 $2$ 이상 발생한 노드)를 중심으로 4가지 경우를 고려한다.

1. **LL**: 균형을 깬 노드가 왼쪽 서브트리의 왼쪽 자식인 경우 → 우회전<span class="gloss">right rotation</span> 1회
2. **LR**: 균형을 깬 노드가 왼쪽 서브트리의 오른쪽 자식인 경우 → 좌회전<span class="gloss">left rotation</span> 후 우회전
3. **RL**: 균형을 깬 노드가 오른쪽 서브트리의 왼쪽 자식인 경우 → 우회전 후 좌회전
4. **RR**: 균형을 깬 노드가 오른쪽 서브트리의 오른쪽 자식인 경우 → 좌회전 1회

LL과 RR은 거울 대칭이고 LR과 RL도 거울 대칭이므로, 이론적으로는 2가지 경우만 고려하면 충분하다. 다만 구현을 위해서는 4가지를 모두 다뤄야 한다.

### 단일 회전 (LL, RR)

LL과 RR은 불균형이 트리의 바깥쪽<span class="gloss">outside</span>에서 일어나는 경우로, 단일 회전<span class="gloss">single rotation</span>으로 수선된다. 아래 트리를 수선하려면 $X$를 한 단계 올리고 $Z$를 한 단계 낮추면 된다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-21.svg" alt="LL 단일 회전 일반형" style="max-width: 560px;" />
  <figcaption class="cap">단일 우회전: 피봇 $k_1$이 새 루트가 되고, $k_2 > k_1$이므로 $k_2$는 $k_1$의 오른쪽 자식, 가운데 서브트리 $Y$는 $k_2$의 왼쪽 자식이 된다.</figcaption>
</figure>

LL의 시나리오는 다음과 같다. 트리가 유연하다고 가정하고, 불균형 노드 $k_2$의 왼쪽 자식(피봇 노드<span class="gloss">pivot node</span>) $k_1$을 잡아 중력에 따라 재배열되는 것을 상상하면, $k_1$이 새 루트가 된다.

- BST 성질상 $k_2 > k_1$이므로 $k_2$는 $k_1$의 오른쪽 자식이 된다.
- $X$와 $Z$는 그대로 각각 $k_1$의 왼쪽 자식, $k_2$의 오른쪽 자식이 된다.
- 기존에 $k_1$과 $k_2$ 사이에 있던 서브트리 $Y$는 $k_2$의 왼쪽 자식이 되어, BST 성질을 유지한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-22.svg" alt="LL 케이스 구체적 예시" style="max-width: 560px;" />
  <figcaption class="cap">`8`이 불균형 노드, 피봇은 `7`. LL이므로 1회 우회전하여 균형을 맞춘다.</figcaption>
</figure>

### 이중 회전 (LR, RL)

단일 회전 알고리즘은 LR, RL 경우를 수선할 수 없다. 아래처럼 안쪽 서브트리 $Y$를 피봇으로 우회전해도 불균형이 그대로 남는다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-23.svg" alt="단일 회전으로는 LR을 수선할 수 없음" style="max-width: 560px;" />
  <figcaption class="cap">안쪽에서 불균형이 난 경우, 단일 회전으로는 $Y$가 여전히 불균형으로 남는다.</figcaption>
</figure>

LR, RL은 불균형이 트리의 안쪽<span class="gloss">inside</span>에서 일어나는 경우로, 이중 회전<span class="gloss">double rotation</span>으로 수선된다. 우선 단일 회전으로 LR은 LL로, RL은 RR로 변환한 뒤, 다시 단일 회전하여 균형을 맞춘다.

LR의 시나리오는 다음과 같다.

- 불균형 노드 $k_3$의 왼쪽 자식 $k_1$의 오른쪽 자식 $k_2$를 피봇으로 잡아 **좌회전**한다. 그러면 $k_3$의 왼쪽 자식은 $k_2$, $k_2$의 왼쪽 자식은 $k_1$이 되어 LL 형태가 된다.
- 이제 $k_2$를 피봇으로 **우회전**한다. $k_2$가 새 루트가 되고, $k_1$과 $k_3$가 각각 $k_2$의 왼쪽·오른쪽 자식이 된다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-24.svg" alt="LR 이중 회전 일반형" style="max-width: 640px;" />
  <figcaption class="cap">LR 이중 회전: 좌회전으로 LL로 만든 뒤 우회전. $k_2$가 최종 루트가 된다.</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-25.svg" alt="RL 케이스 구체적 예시" style="max-width: 640px;" />
  <figcaption class="cap">`7`이 불균형 노드인 RL 경우. 피봇은 오른쪽-왼쪽 자식 `15`. 우회전으로 RR로 바꾼 뒤 좌회전하여 균형을 맞춘다.</figcaption>
</figure>

## 실습 — AVL 삽입과 자동 재균형

$1$부터 $7$까지 순서대로 삽입한다. 일반 BST라면 오른쪽으로 완전히 편향되어 높이 7이 되겠지만, AVL은 매 삽입마다 회전하여 균형을 유지한다. 루트가 편향된 `1`이 아니라 `4`가 되는 것을 확인하자. 공개 메서드와 순회는 앞의 BST 구현을 그대로 채워 넣었다.

<CppRunner>

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

class AVLNode {
public:
    int key; int height;
    AVLNode* left; AVLNode* right;
    AVLNode(int value) : key(value), left(nullptr), right(nullptr), height(1) {}
};

class AVLTree {
public:
    AVLTree() : root(nullptr) {}

    void insert(int key) { root = _insert(root, key); }
    void remove(int key) { root = _remove(root, key); }
    int  rootKey()  { return root ? root->key : -1; }
    void preOrder() { _preOrder(root); cout << endl; }
    void inOrder()  { _inOrder(root);  cout << endl; }

private:
    AVLNode* root;

    int height(AVLNode* node) { return node == nullptr ? 0 : node->height; }
    int getBalance(AVLNode* node) {
        return node == nullptr ? 0 : height(node->left) - height(node->right);
    }

    AVLNode* rightRotate(AVLNode* y) {
        AVLNode* x = y->left;
        AVLNode* T2 = x->right;
        x->right = y;
        y->left = T2;
        y->height = max(height(y->left), height(y->right)) + 1;
        x->height = max(height(x->left), height(x->right)) + 1;
        return x;
    }
    AVLNode* leftRotate(AVLNode* x) {
        AVLNode* y = x->right;
        AVLNode* T2 = y->left;
        y->left = x;
        x->right = T2;
        x->height = max(height(x->left), height(x->right)) + 1;
        y->height = max(height(y->left), height(y->right)) + 1;
        return y;
    }

    AVLNode* _insert(AVLNode* node, int key) {
        if (node == nullptr) return new AVLNode(key);
        if (key < node->key)      node->left  = _insert(node->left, key);
        else if (key > node->key) node->right = _insert(node->right, key);
        else return node;
        node->height = 1 + max(height(node->left), height(node->right));
        int balance = getBalance(node);
        if (balance > 1 && key < node->left->key)   return rightRotate(node);   // LL
        if (balance < -1 && key > node->right->key) return leftRotate(node);    // RR
        if (balance > 1 && key > node->left->key) {                             // LR
            node->left = leftRotate(node->left); // LL로 변환
            return rightRotate(node);
        }
        if (balance < -1 && key < node->right->key) {                           // RL
            node->right = rightRotate(node->right); // RR로 변환
            return leftRotate(node);
        }
        return node;
    }

    AVLNode* _findMin(AVLNode* node) {
        AVLNode* current = node;
        while (current && current->left != nullptr) current = current->left;
        return current;
    }

    AVLNode* _remove(AVLNode* node, int key) {
        if (node == nullptr) return node;
        if (key < node->key)      node->left  = _remove(node->left, key);
        else if (key > node->key) node->right = _remove(node->right, key);
        else {
            if ((node->left == nullptr) || (node->right == nullptr)) {
                AVLNode* temp = node->left ? node->left : node->right;
                if (temp == nullptr) { temp = node; node = nullptr; }
                else *node = *temp;
                delete temp;
            } else {
                AVLNode* temp = _findMin(node->right);
                node->key = temp->key;
                node->right = _remove(node->right, temp->key);
            }
        }
        if (node == nullptr) return node;
        node->height = 1 + max(height(node->left), height(node->right));
        int balance = getBalance(node);
        if (balance > 1 && getBalance(node->left) >= 0)   return rightRotate(node); // LL
        if (balance < -1 && getBalance(node->right) <= 0) return leftRotate(node);  // RR
        if (balance > 1 && getBalance(node->left) < 0) {                            // LR
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }
        if (balance < -1 && getBalance(node->right) > 0) {                          // RL
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }
        return node;
    }

    void _preOrder(AVLNode* node) {
        if (node != nullptr) {
            cout << node->key << " ";
            _preOrder(node->left);
            _preOrder(node->right);
        }
    }
    void _inOrder(AVLNode* node) {
        if (node != nullptr) {
            _inOrder(node->left);
            cout << node->key << " ";
            _inOrder(node->right);
        }
    }
};

int main() {
    AVLTree avl;
    for (int k = 1; k <= 7; ++k) avl.insert(k); // 편향될 뻔하지만 회전으로 균형

    cout << "root = " << avl.rootKey() << endl;  // 균형 잡힌 루트
    cout << "preorder: "; avl.preOrder();         // 완전 균형 트리
    cout << "inorder : "; avl.inOrder();          // 항상 정렬됨
    avl.remove(1); avl.remove(2);
    cout << "after remove(1), remove(2) -> root = " << avl.rootKey()
         << ", preorder: ";
    avl.preOrder();
    return 0;
}
```

</CppRunner>

`1~7`을 넣어도 루트는 `4`, 전위 순회는 `4 2 1 3 6 5 7`인 완전 균형 트리가 된다.

---

# 레드-블랙 트리

레드-블랙 트리<span class="gloss">red-black tree</span>는 수선을 통해 균형을 맞추는 이진 탐색 트리의 일종이다.

- 레드-블랙 트리의 깊이는 최대 $2\log(N+1)$이다.
- 따라서 모든 연산은 $\mathcal{O}(\log N)$이다.

## 색깔 성질

레드-블랙 트리는 아래 색깔<span class="gloss">color</span> 성질을 따른다.

1. 모든 노드는 **레드** 혹은 **블랙**이다.
2. 루트는 블랙이다.
3. 임의의 레드 노드의 자식 노드는 블랙이다(레드가 연속될 수 없다).
4. 루트부터 임의의 리프 노드(`nullptr`)까지의 모든 경로는 **같은 수의 블랙 노드**를 포함한다(블랙 높이가 일정하다).

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-26.svg" alt="레드-블랙 트리 예시" style="max-width: 520px;" />
  <figcaption class="cap">레드-블랙 트리의 예. 레드가 연속되지 않고, 어느 경로든 블랙 노드 수가 같다.</figcaption>
</figure>

## 삽입 시 재조정

원소 $X$를 삽입할 때는 우선 반드시 $X$를 **레드**로 칠한다. 그 후 $X$의 부모 노드 $P$의 색깔에 따라 경우가 나뉜다.

### 경우 1: $P$가 블랙

규칙 위반이 발생하지 않는다. 그대로 둔다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-27.svg" alt="부모가 블랙인 경우 삽입" style="max-width: 560px;" />
  <figcaption class="cap">부모 $P$가 블랙이면 레드 자식 $X$를 붙여도 위반이 없다.</figcaption>
</figure>

### 경우 2: $P$가 레드

삽입 이전에는 레드-블랙 트리였으므로, $P$의 부모(조부모 $G$)는 블랙이었다. $P$의 형제자매 $S$의 색깔에 따라 수선 방식이 달라진다.

**(a) $S$가 레드**: $P$와 $S$를 블랙으로 바꾸고 $G$를 레드로 바꾼다.

- $G$가 루트였다면 다시 블랙으로 되돌린다.
- 그렇지 않다면 $G$의 부모(증조부모)에서 레드-블랙 특성을 재귀적으로 확인한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-28.svg" alt="삼촌이 레드인 경우: 색깔 뒤집기" style="max-width: 460px;" />
  <figcaption class="cap">$S$가 레드면 $P$, $S$를 블랙으로, $G$를 레드로 바꾸는 색깔 뒤집기<span class="gloss">recoloring</span>.</figcaption>
</figure>

**(b) $S$가 블랙이거나 없다(`nullptr`)**: $X$가 $P$의 왼쪽/오른쪽 자식인지에 따라 다시 나뉜다.

- $X$가 $P$의 **오른쪽** 자식이면, $X$를 피봇으로 좌회전하여 경우 2.(b).ii로 바꾼다.
- $X$가 $P$의 **왼쪽** 자식이면, $P$를 피봇으로 우회전한 후 $P$와 $G$의 색깔을 맞바꾼다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-29.svg" alt="삼촌이 블랙인 경우: 회전과 색 교환" style="max-width: 640px;" />
  <figcaption class="cap">$S$가 블랙이면 회전(왼쪽: 좌회전으로 정렬, 오른쪽: 우회전 후 색 교환)으로 수선한다.</figcaption>
</figure>

## 삭제 시 재조정

삭제는 조금 더 복잡하며, 삭제할 원소 $X$, $X$의 자식, $X$의 부모 $P$의 색깔에 따라 경우가 나뉜다.

### 경우 1: $X$가 레드이거나, $X$는 블랙이지만 유일한 자식 $M$이 레드

문제가 발생하지 않으며, 일반 BST의 노드 삭제와 같은 방식을 따른다(레드였던 $M$을 블랙으로 칠해 블랙 높이를 보존).

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-30.svg" alt="삭제 경우 1" style="max-width: 640px;" />
  <figcaption class="cap">$X$가 레드거나 자식 $M$이 레드면 단순 삭제로 처리된다.</figcaption>
</figure>

### 경우 2: $X$와 $M$이 블랙, $P$가 레드

$X$를 삭제하고 $M$을 그 자리에 넣은 뒤 결정한다. $X$의 형제자매 $B$는 반드시 블랙이었으며, $B$의 왼쪽·오른쪽 자식 $L$, $R$에 따라 나뉜다.

**(a) $L$, $R$이 모두 블랙**: $P$와 $B$의 색깔을 맞바꾼다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-31.svg" alt="삭제 경우 2a" style="max-width: 520px;" />
  <figcaption class="cap">$L$, $R$이 블랙이면 $P$와 $B$의 색만 맞바꾼다.</figcaption>
</figure>

**(b) $L$은 레드 또는 블랙, $R$이 레드**: $B$를 피봇으로 좌회전한 뒤, $P$와 $B$의 색깔을 바꾸고 $R$을 레드에서 블랙으로 바꾼다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-32.svg" alt="삭제 경우 2b" style="max-width: 520px;" />
  <figcaption class="cap">$R$이 레드면 좌회전 후 색을 조정한다.</figcaption>
</figure>

**(c) $L$이 레드, $R$이 블랙**: $L$을 피봇으로 우회전한 후 $L$과 $B$의 색깔을 맞바꾸면 경우 2.(b)로 바뀐다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-33.svg" alt="삭제 경우 2c" style="max-width: 520px;" />
  <figcaption class="cap">$L$만 레드면 우회전으로 경우 2.(b)로 환원한다.</figcaption>
</figure>

### 경우 3: $X$, $M$, $P$가 모두 블랙

마찬가지로 $X$를 삭제하고 $M$을 넣은 뒤, $B$, $L$, $R$의 색깔에 따라 나뉜다.

**(a) $B$, $L$, $R$이 모두 블랙**: $B$를 레드로 바꾼 뒤 $P$에서 재귀적으로 반복한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-34.svg" alt="삭제 경우 3a" style="max-width: 520px;" />
  <figcaption class="cap">모두 블랙이면 $B$를 레드로 바꾸고 부족한 블랙을 위로 전파한다.</figcaption>
</figure>

- **(b)** $B$는 블랙, $L$은 레드 또는 블랙, $R$이 레드인 경우: 경우 2.(b)와 $P$의 색만 다르며 처리에 영향이 없으므로 **2.(b)와 동일**하게 처리한다.
- **(c)** $B$와 $R$은 블랙, $L$이 레드인 경우: 경우 2.(c)와 $P$의 색만 다르므로 **2.(c)와 동일**하게 처리한다.
- **(d)** $B$가 레드, $L$과 $R$이 모두 블랙인 경우: $B$를 피봇으로 좌회전한 후 $P$와 $B$의 색을 맞바꾸면, 경우 2.(a)·2.(b)·2.(c) 중 하나로 이동한다.

## 복잡도

- 탐색: $\mathcal{O}(\log N)$.
- 삽입·삭제: 대부분은 상수 시간 $\mathcal{O}(1)$의 색 조정으로 끝나지만, 최악의 경우 재조정이 루트까지 재귀적으로 반복되므로 $\mathcal{O}(\log N)$이다.

---

# 트라이

트라이<span class="gloss">trie</span>는 전위 트리<span class="gloss">prefix tree</span> 또는 디지털 트리<span class="gloss">digital tree</span>라고도 불리며, 특정한 키(주로 문자열)를 사용하는 탐색 트리의 일종이다.

## 성질

- 트라이 노드들은 문자열 키값들의 공용 접두어<span class="gloss">prefix</span>를 공유하여, 메모리 사용량을 최적화하고 검색 효율을 높인다.
- 문자열 안의 문자들을 따라 트리를 순회하며 문자열을 검색한다.
- 문자열의 끝을 의미하는 노드는 보통 플래그<span class="gloss">flag</span>나 문자열 값과 같은 특별한 방식으로 표시되어, 트라이 안에 그 문자열이 존재함을 나타낸다.
- 대부분 루트 노드는 빈 문자열을 나타내기 위해 어떤 문자도 포함하지 않으며, 각 자식 노드는 문자열의 다음 글자를 나타낸다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-35.svg" alt="cat, car, dog, duck를 저장한 트라이" style="max-width: 460px;" />
  <figcaption class="cap">`cat`, `car`, `dog`, `duck`를 저장한 트라이. `ca-`, `d-` 같은 접두어를 공유한다.</figcaption>
</figure>

## 복잡도와 공간 효율

다루고자 하는 문자열의 길이가 $m$일 때, 트라이에서의 검색 시간은 $\mathcal{O}(m)$이다(저장된 문자열 개수 $N$과 무관). 데이터셋에 많은 양의 문자열이 있을 때 검색을 대단히 효율적으로 수행할 수 있게 한다.

- 짧은 길이의 문자열이 많은 경우에는, 각 노드와 포인터 값들로 인해 메모리 공간을 과도하게 차지할 수 있다.
- 그러나 접두어들이 많이 공유되는 경우(겹치는 문자열이 많은 경우)에는, 트라이가 훨씬 더 공간적으로 효율적일 수 있다.

::: tip 트리 종류 한눈에 정리
| 트리 | 균형 보장 | 대표 연산 복잡도 |
| --- | --- | --- |
| 이진 탐색 트리(BST) | 없음(편향 시 $\mathcal{O}(N)$) | 평균 $\mathcal{O}(\log N)$ |
| AVL 트리 | 좌우 깊이 차 $\le 1$ | $\mathcal{O}(\log N)$ |
| 레드-블랙 트리 | 깊이 $\le 2\log(N+1)$ | $\mathcal{O}(\log N)$ |
| 트라이 | — (문자열 기반) | 검색 $\mathcal{O}(m)$ |
:::
