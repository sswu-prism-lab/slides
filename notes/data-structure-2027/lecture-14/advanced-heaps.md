# d-힙 · 좌향 힙

기본 이진 힙을 두 방향으로 확장한다. 하나는 자식 수를 늘려 트리를 얕게 만드는
**d-힙**이고, 다른 하나는 두 힙을 효율적으로 합칠 수 있게 하는 **좌향 힙**이다.

## d-힙

이진 힙<span class="gloss">binary heap</span>을 간단히 일반화한 것이 $d$-힙<span class="gloss">d-heap</span>이다.
이진 힙과 동일한 성질을 가지되, 리프 노드<span class="gloss">leaf node</span>를 제외한 모든 노드가
$d$개의 자식<span class="gloss">child</span>을 가진다는 점만 다르다.

- 이진 힙은 곧 $2$-힙이다.
- $d$-힙도 결국 이진 힙의 성질을 따르므로, 배열<span class="gloss">array</span>로 간단히 구현할 수 있다.

아래 그림은 $3$-힙의 예시이다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-02.svg" alt="3-힙 예시" style="max-width: 420px;" />
  <figcaption class="cap">모든 내부 노드가 세 개의 자식을 가지는 3-힙</figcaption>
</figure>

배열로 구현할 때, 노드를 $0$번부터 저장하면 인덱스 $i$의 부모와 자식은 다음과 같다.

$$
\text{부모}(i) = \left\lfloor \frac{i-1}{d} \right\rfloor, \qquad
\text{자식}(i) = d\,i + 1,\ d\,i + 2,\ \dots,\ d\,i + d
$$

복잡도는 다음과 같이 정리된다.

- $d$-힙은 이진 힙보다 훨씬 얕으므로, `insert` 연산을 $\mathcal{O}(\log_d N)$으로 단축한다.
- 반면 $d$가 크면 `deleteMin`은 더 비싸진다. 트리가 얕더라도 $d$개의 자식 중 최솟값을
  찾아야 하므로 $d-1$번의 비교<span class="gloss">comparison</span>가 필요하기 때문이다.
  - 즉 이 연산은 $\mathcal{O}(d \log_d N)$이다.
  - $d$는 상수이므로, `insert`와 `deleteMin` 모두 결국 $\mathcal{O}(\log N)$이다.

## 좌향 힙

힙 자료구조의 약점 중 하나는 **두 힙을 하나로 합치는** 일이다. 이 추가 연산을 `merge`라
부른다. 힙을 배열로 구현하면, 같은 크기의 배열 두 개를 합칠 때 적어도 한 배열을 복사해
다른 배열에 붙여야 하므로 $\Theta(N)$이 든다. 결국 배열 기반 힙은 병합<span class="gloss">merging</span>을
효율적으로 지원하기 어렵다.

좌향 힙<span class="gloss">leftist heap</span>은 이진 힙과 마찬가지로 두 가지 성질을 가진다.

1. **구조 성질.** 임의의 노드에 대해, 왼쪽 자식의 널 경로 길이<span class="gloss">null path length</span>는
   오른쪽 자식의 널 경로 길이보다 크거나 같아야 한다.
2. **힙-순서 성질.** 일반적인 힙의 순서 성질과 동일하다.

### 널 경로 길이

널 경로 길이란 그 노드로부터 **자식이 없거나 하나뿐인 노드까지의 최소 경로 길이**를 말한다.

- 자식이 없거나 하나인 노드의 널 경로 길이는 $0$이다.
- 임의의 노드의 널 경로 길이는, 그 왼쪽·오른쪽 자식의 널 경로 길이 중 **최솟값보다 $1$만큼 크다.**

아래 두 트리에서 노드 안의 숫자는 각 노드의 널 경로 길이이며, **왼쪽 트리만 좌향 힙**이다.
(오른쪽 트리는 파랗게 칠한 노드에서 왼쪽 자식의 널 경로 길이가 오른쪽보다 작아 구조 성질을 위반한다.)

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-03.svg" alt="널 경로 길이와 좌향 성질" style="max-width: 460px;" />
  <figcaption class="cap">각 노드의 널 경로 길이. 왼쪽만 구조 성질을 만족하는 좌향 힙이다</figcaption>
</figure>

이 구조 성질 때문에 좌향 힙은 전체적으로 **왼쪽 서브트리가 더 깊어지는** 경향을 가지며,
이것이 '좌향(leftist)'이라는 이름의 유래이다.

### 병합(merge) 연산

좌향 힙의 모든 연산은 **병합** 위에서 정의된다. 힙에 원소 하나를 넣는 스며오르기 연산조차,
임의의 힙과 노드 하나짜리 힙을 병합하는 것으로 볼 수 있다.

병합 규칙은 다음과 같다.

1. 임의의 힙과 **비어 있는**<span class="gloss">empty</span> 힙을 병합하면, 그 힙을 그대로 반환하고 끝낸다.
2. 그렇지 않으면 재귀적으로 처리한다.

아래 두 힙 $H_1$, $H_2$를 병합하는 과정을 따라가 보자.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-04.svg" alt="병합할 두 힙 H1, H2" style="max-width: 480px;" />
  <figcaption class="cap">병합 대상인 두 좌향 힙 H₁, H₂</figcaption>
</figure>

먼저 두 힙의 루트<span class="gloss">root</span>를 비교하여, **더 작은 루트를 가진 힙의 오른쪽 서브힙<span class="gloss">subheap</span>을 선택**한다.
$H_1$의 루트($3$)가 더 작으므로 $H_1$의 오른쪽 서브힙을 떼어 낸다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-05.svg" alt="H1의 오른쪽 서브힙 선택" style="max-width: 480px;" />
  <figcaption class="cap">더 작은 루트를 가진 H₁의 오른쪽 서브힙(H₁′)을 H₂와 병합</figcaption>
</figure>

다시 두 루트를 비교해, 더 작은 힙($H_2$)의 오른쪽 서브힙을 선택한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-06.svg" alt="H2의 오른쪽 서브힙 선택" style="max-width: 460px;" />
  <figcaption class="cap">재귀적으로 H₂의 오른쪽 서브힙(H₂′)을 선택</figcaption>
</figure>

같은 과정을 반복해 $H_2'$의 오른쪽 서브힙을 선택한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-07.svg" alt="재귀 진행" style="max-width: 420px;" />
  <figcaption class="cap">더 이상 오른쪽 서브힙이 없는 단계까지 재귀적으로 내려간다</figcaption>
</figure>

이제 더 작은 루트를 가진 $H_1'$의 오른쪽 서브힙이 존재하지 않으므로 둘을 병합한다.
힙-순서 성질을 지키기 위해, **더 큰 루트의 트리를 더 작은 루트의 오른쪽 서브트리로 매단다.**

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-08.svg" alt="바닥에서의 병합" style="max-width: 420px;" />
  <figcaption class="cap">더 큰 루트를 작은 루트의 오른쪽 서브트리로 연결</figcaption>
</figure>

병합 후에는 널 경로 길이를 계산해 좌향 조건을 확인한다. 문제가 없으면 그대로 두고,
**구조 성질을 위반하면 왼쪽과 오른쪽 서브트리의 위치를 바꾼다.** 아래 단계에서는 위반이
생겨 위치를 교환한 뒤 병합을 이어 간다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-09.svg" alt="좌우 서브트리 교환" style="max-width: 520px;" />
  <figcaption class="cap">널 경로 길이 위반 시 좌우 서브트리를 교환하고 병합을 계속</figcaption>
</figure>

이 과정을 위로 올라가며 재귀적으로 반복한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-10.svg" alt="재귀적으로 반복" style="max-width: 520px;" />
  <figcaption class="cap">상위 단계로 되돌아오며 병합·교환을 반복</figcaption>
</figure>

최종 결과는 다음과 같다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-11.svg" alt="최종 병합 결과" style="max-width: 520px;" />
  <figcaption class="cap">병합이 끝난 좌향 힙(루트가 최솟값 3)</figcaption>
</figure>

이렇게 병합만 정의하면 나머지 연산은 자연스럽게 따라온다.

- `insert`: 노드 하나짜리 힙과의 병합.
- `deleteMin`: 루트를 제거한 뒤, 남은 왼쪽·오른쪽 서브힙을 서로 병합.

병합은 오른쪽 경로<span class="gloss">right path</span>를 따라서만 진행되고, 좌향 성질 덕분에
오른쪽 경로의 길이가 $\mathcal{O}(\log N)$으로 억제되므로 세 연산 모두 $\mathcal{O}(\log N)$이다.

### 실습: 좌향 힙 병합

위 예시의 두 힙을 그대로 만들어 병합한 뒤, `deleteMin`을 반복해 원소가 정렬 순으로
빠져나오는지 확인한다. 병합의 핵심(더 작은 루트 선택 → 오른쪽 서브힙 재귀 병합 →
널 경로 길이 위반 시 좌우 교환)이 `merge` 함수 한 곳에 담겨 있다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int val;
    int npl;            // 널 경로 길이(null path length)
    Node *left, *right;
    Node(int v) : val(v), npl(0), left(nullptr), right(nullptr) {}
};

int npl(Node* h) { return h ? h->npl : -1; }

// 두 좌향 힙을 병합한다.
Node* merge(Node* h1, Node* h2) {
    if (!h1) return h2;
    if (!h2) return h1;
    if (h1->val > h2->val) swap(h1, h2);      // 더 작은 루트를 h1 으로
    h1->right = merge(h1->right, h2);         // 오른쪽 서브힙과 재귀 병합
    if (npl(h1->left) < npl(h1->right))       // 구조 성질 위반 시
        swap(h1->left, h1->right);            // 좌우 교환
    h1->npl = npl(h1->right) + 1;
    return h1;
}

Node* insert(Node* h, int v) { return merge(h, new Node(v)); }

Node* deleteMin(Node* h, int& out) {
    out = h->val;
    Node* res = merge(h->left, h->right);
    delete h;
    return res;
}

int main() {
    Node *H1 = nullptr, *H2 = nullptr;
    for (int v : {3, 10, 21, 14, 23, 8, 17, 26}) H1 = insert(H1, v);
    for (int v : {6, 12, 18, 24, 33, 7, 37, 18}) H2 = insert(H2, v);

    Node* H = merge(H1, H2);
    cout << "병합 후 루트(최솟값): " << H->val
         << ", 루트의 npl: " << H->npl << endl;

    cout << "deleteMin 순서: ";
    while (H) {
        int x;
        H = deleteMin(H, x);
        cout << x << (H ? " " : "\n");
    }
    return 0;
}
```

</CppRunner>

::: tip 핵심
좌향 힙은 "합치기 어렵다"는 힙의 약점을 **병합 한 연산**으로 해결한다. `insert`와
`deleteMin`을 모두 병합으로 환원하고, 구조 성질로 오른쪽 경로를 짧게 유지하는 것이 요점이다.
:::
