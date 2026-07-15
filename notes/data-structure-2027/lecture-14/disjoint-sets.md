# 동적 동치 · 서로소 집합

원소들을 서로소인 집합들로 나누고, "두 원소가 같은 집합에 속하는가"를 빠르게 판정하는
문제를 다룬다. 이 문제를 푸는 자료구조가 **서로소 집합(union-find)**이다.

## 동적 동치 문제

집합 $S$에서 관계<span class="gloss">relation</span> $R$은 원소 쌍 $(a, b)$($a, b \in S$)마다
$a\ R\ b$가 참<span class="gloss">true</span> 또는 거짓<span class="gloss">false</span>으로 결정되는 것이다.
$a\ R\ b$가 참이면 $a$가 $b$와 관계되었다고 한다.

동치 관계<span class="gloss">equivalence relation</span> $R$은 다음 **세 가지 성질**을 만족한다.

1. **반사성**<span class="gloss">reflexive</span>: 모든 $a \in S$에 대해 $a\ R\ a$.
2. **대칭성**<span class="gloss">symmetric</span>: $a\ R\ b$이면, 그리고 그럴 때에만 $b\ R\ a$.
3. **전이성**<span class="gloss">transitive</span>: $a\ R\ b$이고 $b\ R\ c$이면 $a\ R\ c$.

예를 들어 $\le$ 관계는 동치 관계가 **아니다**. $a \le a$(반사성)와 $a \le b,\ b \le c \Rightarrow a \le c$(전이성)는
성립하지만, $a \le b$라고 해서 $b \le a$가 성립하지는 않아 **대칭성이 없기** 때문이다.

주어진 동치 관계 $\sim$에 대해, 우리가 보통 풀려는 문제는 $a$와 $b$가 주어졌을 때 $a \sim b$인지
판정하는 것이다.

- 관계를 부울 변수<span class="gloss">Boolean variable</span>의 2차원 배열에 담아 두면 상수 시간에 답할 수 있다.
- 그러나 이런 관계는 보통 명시적으로<span class="gloss">explicitly</span> 주어지지 않고 묵시적으로<span class="gloss">implicitly</span> 주어져 문제가 된다.
  - 예를 들어 $\{a_1, a_2, a_3, a_4, a_5\}$에 대한 동치 관계라면 확인해야 할 원소 쌍이 $25$개다.
  - 하지만 $a_1 \sim a_2$, $a_3 \sim a_4$, $a_5 \sim a_1$, $a_4 \sim a_2$만으로도 모든 원소가 서로 연관됨을 **추론**할 수 있다. 이 추론을 빠르게 하는 것이 목표다.

원소 $a \in S$의 동치 클래스<span class="gloss">equivalence class</span>는 $a$와 연관된 모든 원소를 모은
$S$의 부분집합이다.

- $S$의 모든 원소는 정확히 하나의 동치 클래스에 속한다.
- 따라서 $a \sim b$ 판정은 **$a$와 $b$가 같은 동치 클래스에 있는지** 확인하는 것으로 충분하다.

동적 동치 문제의 입력은 각각 원소 하나씩을 가진 $N$개의 집합이다. 초기에는 반사성을 제외한
모든 관계가 거짓이고, 집합들은 서로 겹치지 않으므로($S_i \cap S_j = \emptyset$) 모두 **서로소**이다.
이 문제는 두 연산을 필요로 한다.

- 관계 $a \sim b$를 추가하려면, 먼저 `find`로 $a$와 $b$가 이미 같은 동치 클래스에 있는지 확인한다.
- 그렇지 않다면 `union`으로 두 클래스를 합친다.

이 알고리즘을 서로소 집합<span class="gloss">disjoint set</span>의 union/find 알고리즘이라 부른다.

## 서로소 집합

동적 동치 문제에서는 `union` 연산에 의해 집합 구성이 계속 바뀐다. 이때 우리가 필요로 하는
정보는 원소의 값 자체가 아니라 **그 원소가 어느 집합에 속하는가**뿐이며, 각 동치 클래스(집합)의
이름은 임의로 붙여도 문제의 답에 영향을 주지 않는다. 서로소 집합은 두 가지 방식으로 표현할 수 있다.

### 연결 리스트 표현

연결 리스트<span class="gloss">linked list</span>로 구현하면 각 원소가 자기 집합의 대표를 가리키게 하여
`find` 연산을 $\mathcal{O}(1)$에 수행할 수 있다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-29.svg" alt="연결 리스트 기반 서로소 집합" style="max-width: 520px;" />
  <figcaption class="cap">두 집합 {A,B,C}, {D,…,H}의 연결 리스트 표현</figcaption>
</figure>

동치 클래스의 **크기**도 함께 저장하면, `union` 시 항상 더 작은 클래스를 더 큰 클래스에
붙일 수 있다. 이렇게 하면 최종적으로 $N-1$번의 병합에 대해 전체 $\mathcal{O}(N \log N)$이 든다.

### 트리(배열) 표현

트리로 구현하면 `union` 연산을 $\mathcal{O}(1)$에 수행할 수 있다.

- 각 집합을 트리로 나타내되, 이 트리는 이진 트리일 필요가 없다.
- 필요한 정보는 오직 **부모 노드로의 링크**뿐이므로 배열 하나로 간단히 구현된다.
  - 배열의 각 원소 `s[i]`는 원소 $i$의 부모를 가리킨다.
  - $i$가 루트이면 `s[i] = -1`이다.
- 두 집합을 `union`하려면, 한 트리의 루트가 다른 트리의 루트를 가리키도록 링크 하나만 바꾸면 된다.

아래는 `union(4, 5)`, `union(6, 7)`, `union(4, 6)`을 차례로 수행한 결과와 그에 대응하는 배열이다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-31.svg" alt="트리·배열 기반 서로소 집합" style="max-width: 520px;" />
  <figcaption class="cap">부모 링크 트리와 그에 대응하는 배열 표현</figcaption>
</figure>

`find(x)`는 `x`가 속한 트리의 루트를 반환하는데, 트리가 한쪽으로 길어지면 최악의 경우
$\Theta(N)$이 든다. 트리가 너무 깊어지는 것을 막기 위해 두 가지 개선된 합집합 방법을 쓴다.

1. **크기에 따른 합집합**<span class="gloss">union-by-size</span>: 각 집합의 크기를 배열에 기록하여, 항상 더 작은 트리가 더 큰 트리의 서브트리가 되게 한다.
2. **높이에 따른 합집합**<span class="gloss">union-by-height</span>: 비슷하게 각 집합의 깊이를 기록하여, 더 얕은 트리가 더 깊은 트리의 서브트리가 되게 한다.

크기 또는 높이에 따라서만 `union`을 수행하면, 어떤 트리의 깊이도 $\mathcal{O}(\log N)$을 넘지 않는다.

또한 `find`를 개선하기 위해 **경로 압축**<span class="gloss">path compression</span>을 함께 쓴다.
어떤 원소를 검색할 때, 그 경로 위의 노드들을 곧바로 루트에 직접 연결해 버리는 방식이다.

- 경로 압축과는 크기에 따른 합집합을 함께 쓸 수 있다.
- 높이에 따른 합집합은 경로 압축과 함께 쓰면 계산이 복잡해지므로, 보통 랭크에 따른 합집합<span class="gloss">union-by-rank</span>을 대신 사용한다.

### 연산별 복잡도

| 표현 | `find` | `union` | 비고 |
| --- | --- | --- | --- |
| 연결 리스트 | $\mathcal{O}(1)$ | — | 크기 기록 시 전체 병합 $\mathcal{O}(N\log N)$ |
| 트리(개선 전) | $\Theta(N)$ 최악 | $\mathcal{O}(1)$ | 트리가 한쪽으로 치우칠 수 있음 |
| 트리 + 크기/높이 합집합 | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | 깊이가 $\mathcal{O}(\log N)$로 억제 |
| 트리 + 랭크 합집합 + 경로 압축 | 거의 상수 | $\mathcal{O}(1)$ | 실무에서 가장 널리 쓰임 |

### 실습: 서로소 집합 (union-by-rank + 경로 압축)

랭크에 따른 합집합과 경로 압축을 모두 적용한 구현이다. 초기에는 각 원소를 자기 자신을 부모로
두어 표현한다(`-1` 대신 자기 자신). `find`가 반환하는 대표 원소를 비교해 두 원소가 같은 집합에
속하는지 확인할 수 있다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;
class DisjointSet {
public:
    DisjointSet(int n) : parent(n), rank(n, 0) { // 생성자
        for (int i = 0; i < n; ++i) {
            parent[i] = i; // -1 대신 자기 자신을 부모로 초기화
        }
    }
    int find(int x) {                 // find 연산
        return _find(x);
    }
    void unionSets(int x, int y) {    // union 연산
        _unionSets(x, y);
    }
private:
    vector<int> parent;   // 부모 노드
    vector<int> rank;     // 랭크
    int _find(int x) {
        if (parent[x] != x)
            parent[x] = _find(parent[x]); // 경로 압축(path compression)
        return parent[x];
    }
    void _unionSets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {             // 랭크에 따른 합집합(union-by-rank)
            if (rank[rootX] > rank[rootY])
                parent[rootY] = rootX;
            else if (rank[rootX] < rank[rootY])
                parent[rootX] = rootY;
            else {
                parent[rootY] = rootX;
                rank[rootX] += 1;
            }
        }
    }
};
int main() {
    DisjointSet ds(10);
    ds.unionSets(0, 1);
    ds.unionSets(2, 3);
    cout << "Find(2): " << ds.find(2) << endl;                       // 2
    ds.unionSets(1, 3);
    cout << "Find(0): " << ds.find(0) << ", Find(1): " << ds.find(1) << endl; // 0, 0
    cout << "Find(3): " << ds.find(3) << ", Find(4): " << ds.find(4) << endl; // 0, 4
    return 0;
}
```

</CppRunner>

::: tip STL
C++에서 `set` STL 컨테이너는 일반적인 집합을 지원하지만, 여기서 다룬 union/find 자료구조와는
목적이 다르다. union/find는 "어느 집합에 속하는가"를 빠르게 판정하기 위한 전용 구조이다.
:::
