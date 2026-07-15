# 우선순위 큐

우선순위 큐<span class="gloss">priority queue</span>는 `insert` 연산과 함께, **최소값**을 가진 원소를 찾아 반환하고 제거하는 `removeMin`(흔히 `deleteMin`이라고도 함) 연산을 포함하는 자료구조이다.

- `insert` 연산은 큐 자료구조의 `push` 연산과 비슷하다.
- `removeMin`은 큐의 `pop`과 비슷한 일을 수행하는 우선순위 큐의 연산이다. 다만 "가장 먼저 들어온 것"이 아니라 "가장 우선순위가 높은(가장 작은) 것"이 나온다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-08.svg" alt="우선순위 큐의 removeMin / insert 연산" style="max-width: 460px;" />
  <figcaption class="cap">우선순위 큐는 <code>insert</code>로 원소를 넣고 <code>removeMin</code>으로 최소값을 꺼낸다.</figcaption>
</figure>

## 왜 이진 힙인가

우선순위 큐를 구현할 수 있는 방법은 다양하지만, 이진 힙<span class="gloss">binary heap</span> 구조를 사용하는 것이 가장 합리적이다.

- **리스트**를 사용할 경우, 경우에 따라 삽입 혹은 삭제에서 $\mathcal{O}(N)$이 소모된다.
- **이진 탐색 트리**<span class="gloss">binary search tree</span>를 사용할 경우, 삽입과 삭제에서 평균적으로 $\mathcal{O}(\log N)$이 소모된다.

이진 힙은 우선순위 큐를 구현하기 위한 사실상 표준<span class="gloss">de facto standard</span>이다.

## 이진 힙의 두 가지 성질

이진 힙에는 2가지 성질이 존재한다.

### 1. 구조 성질

이진 힙은 완전히 차 있는 이진 트리<span class="gloss">binary tree</span>이며, 가장 마지막 레벨에서는 왼쪽에서 오른쪽으로만 차도록 예외를 허용한다(완전 이진 트리<span class="gloss">complete binary tree</span>).

- 이러한 성질은 힙을 단순한 **배열**로 구현할 수 있게 만들며, 보통 `1`번째 인덱스부터 시작한다.
- 배열의 $i$번째 원소에 대해:
  - 왼쪽 자식<span class="gloss">left child</span>의 위치는 $2i$
  - 오른쪽 자식<span class="gloss">right child</span>의 위치는 $2i+1$
  - 부모<span class="gloss">parent</span>의 위치는 $\lfloor i/2 \rfloor$

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-09.svg" alt="완전 이진 트리와 그 배열 표현" style="max-width: 560px;" />
  <figcaption class="cap">완전 이진 트리는 인덱스 1부터 시작하는 배열로 빈틈없이 표현된다. (루트 A는 인덱스 1)</figcaption>
</figure>

::: tip 부모/자식 인덱스 공식 (1-based)
- 왼쪽 자식: $2i$
- 오른쪽 자식: $2i+1$
- 부모: $\lfloor i/2 \rfloor$

인덱스 0을 비워두고 1부터 쓰는 이유가 바로 이 공식을 깔끔하게 만들기 위해서이다.
:::

### 2. 힙-순서 성질

힙 안의 임의의 노드<span class="gloss">node</span> $X$에 대해, $X$의 자식 노드들은 모두 $X$보다 크거나 같아야 한다.

- 이러한 성질을 만족하면 **최소 힙**<span class="gloss">minimum heap</span>이다.
- 반대로 최대값이 루트<span class="gloss">root</span>에 있고, 임의의 노드 $X$의 모든 자식 노드가 $X$보다 작거나 같으면 **최대 힙**<span class="gloss">maximum heap</span>이다.

이 노트에서는 별다른 표기가 없을 경우 **최소 힙**을 기준으로 서술한다.

## insert — 스며올리기(percolate up)

원소 $X$를 힙에 `insert`하기 위해, 우선 가능한 자리(마지막 레벨의 다음 빈 칸)에 공간<span class="gloss">hole</span>을 만든다. 그렇지 않으면 구조 성질을 위반한다.

- 만약 $X$가 힙 순서를 위반하지 않는다면 그대로 그 자리에 넣는다.
- 그렇지 않을 경우, 이 공간을 부모 노드와 자리를 바꾸며, $X$가 그 공간에 들어갈 수 있을 때까지 이 공간을 루트 방향으로 **스며올린다**<span class="gloss">percolate up</span>.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-10.svg" alt="insert 시 새 원소를 루트 방향으로 스며올리는 과정" style="max-width: 620px;" />
  <figcaption class="cap">새 원소 14를 삽입하면, 마지막 자리에서 시작해 부모(31 → 21)를 끌어내리며 제자리까지 스며올린다.</figcaption>
</figure>

## removeMin — 스며내리기(percolate down)

`removeMin`도 비슷한 방식으로 이루어진다. 루트 원소가 제거되고, 가장 마지막 원소 $X$가 그 빈 공간(루트)에 들어간다.

- $X$가 빈 공간을 채울 수 있다면(양쪽 자식보다 작거나 같다면) 연산을 종료한다.
- 그렇지 않을 경우, 빈 공간의 **더 작은** 자식 노드와 값을 교환하여, $X$가 빈 공간에 들어갈 수 있을 때까지 **스며내린다**<span class="gloss">percolate down</span>.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-11.svg" alt="removeMin 시 마지막 원소를 루트로 옮겨 스며내리는 과정" style="max-width: 620px;" />
  <figcaption class="cap">최소값(루트 13)을 제거하고 마지막 원소를 루트에 올린 뒤, 더 작은 자식과 교환하며 아래로 스며내린다.</figcaption>
</figure>

## buildHeap — $N$개 원소로 힙 만들기

이미 배열에 담긴 $N$개의 원소를 힙으로 만들 때, 원소마다 `insert`를 부르면 $\mathcal{O}(N\log N)$이 든다. 하지만 배열의 **마지막 내부 노드**($\lfloor N/2 \rfloor$번째)부터 인덱스 1까지 차례로 `percolateDown`을 적용하면, 전체 비용은

$$\boxed{\text{buildHeap} = \mathcal{O}(N)}$$

이다. 낮은 레벨의 노드일수록 개수는 많지만 스며내릴 높이가 작다는 사실을 합산하면(높이별 노드 수 × 높이의 합이 유한한 등비급수로 수렴) 선형 시간이 됨을 보일 수 있다.

## 실습 — 이진 최소 힙 직접 구현하기

배열(1-based)로 최소 힙을 구현하여 `insert`와 `deleteMin`을 수행한다. 순서 없이 넣은 원소들을 `deleteMin`으로 계속 꺼내면 **오름차순**으로 나온다(힙 정렬의 핵심).

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;

class BinaryHeap {
public:
    BinaryHeap() : array(1) {} // 인덱스 0은 사용하지 않음

    bool empty() const { return array.size() == 1; }

    void insert(int x) {
        array.push_back(x);          // 마지막에 새 공간(hole)
        int hole = array.size() - 1; // percolate up 시작
        while (hole > 1 && x < array[hole / 2]) {
            array[hole] = array[hole / 2]; // 부모를 끌어내림
            hole /= 2;                     // 루트 방향으로 이동
        }
        array[hole] = x;
    }

    int deleteMin() {
        if (empty()) throw runtime_error("heap is empty");
        int minItem = array[1];       // 루트가 최소값
        int last = array.back();
        array.pop_back();
        if (!empty()) {
            int hole = 1;             // 루트에 빈 공간
            int n = array.size() - 1;
            while (2 * hole <= n) {   // percolate down
                int child = 2 * hole; // 왼쪽 자식
                if (child != n && array[child + 1] < array[child])
                    child++;          // 더 작은 자식 선택
                if (array[child] < last)
                    array[hole] = array[child];
                else
                    break;
                hole = child;
            }
            array[hole] = last;
        }
        return minItem;
    }

private:
    vector<int> array; // 1-based 배열
};

int main() {
    BinaryHeap h;
    int data[] = {13, 21, 16, 24, 31, 19, 68, 65, 26, 32};
    for (int x : data) h.insert(x);

    cout << "deleteMin sequence: ";
    while (!h.empty()) cout << h.deleteMin() << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

`deleteMin`을 반복하면 정렬된 수열이 출력된다. `13 16 19 21 24 26 31 32 65 68`

## 실습 — STL `priority_queue`

C++ 표준 라이브러리는 우선순위 큐를 직접 제공한다. 다만 기본은 **최대 힙**이라 `top()`이 가장 큰 값을 준다(최소 힙이 필요하면 `priority_queue<int, vector<int>, greater<int>>`).

<CppRunner>

```cpp
#include <iostream>
#include <queue>
using namespace std;
int main() {
    priority_queue<int> pq;
    pq.push(4); pq.push(1); pq.push(10);
    while (!pq.empty()) {
        cout << pq.top() << endl; // 최대값부터
        pq.pop();
    }
    return 0;
}
```

</CppRunner>

## 연산별 복잡도

| 연산 | 이진 힙 | 정렬 안 된 리스트 | 정렬된 리스트 | 이진 탐색 트리(평균) |
| --- | --- | --- | --- | --- |
| `insert` | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(\log N)$ |
| `findMin` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | $\mathcal{O}(\log N)$ |
| `removeMin` / `deleteMin` | $\mathcal{O}(\log N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | $\mathcal{O}(\log N)$ |
| `buildHeap`($N$개) | $\mathcal{O}(N)$ | — | $\mathcal{O}(N\log N)$ | $\mathcal{O}(N\log N)$ |

::: tip 핵심 정리
- 이진 힙 = **완전 이진 트리(구조 성질)** + **부모 ≤ 자식(힙-순서 성질)**.
- 배열로 구현, 1-based에서 자식은 $2i,\,2i+1$, 부모는 $\lfloor i/2 \rfloor$.
- `insert`는 percolate up, `removeMin`은 percolate down, 둘 다 트리 높이만큼 = $\mathcal{O}(\log N)$.
- $N$개를 한꺼번에 힙으로 만드는 `buildHeap`은 $\mathcal{O}(N)$.
:::
