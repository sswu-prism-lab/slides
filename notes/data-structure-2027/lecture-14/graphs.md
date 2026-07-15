# 그래프 · 최단 경로 · 최소 신장 트리

그래프의 기본 용어와 표현 방법을 정리하고, 대표적인 두 문제인 **최단 경로**(다익스트라)와
**최소 신장 트리**(프림·크루스칼)를 살펴본다.

## 그래프

그래프<span class="gloss">graph</span> $G=(V, E)$는 정점<span class="gloss">vertex</span> $V$와
간선<span class="gloss">edge</span> $E$의 집합이다.

- 각 간선은 순서쌍 $(v, w)$로 표현된다(단 $v, w \in V$).
- 간선을 나타내는 순서쌍에 순서가 있으면 그 그래프는 유향<span class="gloss">directed</span>이다.
- $(v, w) \in E$일 때에만 정점 $w$가 정점 $v$에 인접<span class="gloss">adjacent</span>했다고 한다.
- 무향 그래프<span class="gloss">undirected graph</span>에서 간선 $(v, w)$가 있으면 $(w, v)$도 성립하며, 두 정점은 서로 인접한다.
- 간선은 때때로 세 번째 요소<span class="gloss">component</span>인 가중치<span class="gloss">weight</span> 또는 비용<span class="gloss">cost</span>을 가진다.

경로와 순환 관련 용어를 정리하면 다음과 같다.

- **경로**<span class="gloss">path</span>: 정점들의 나열 $w_1, w_2, \dots, w_N$으로, $(w_i, w_{i+1}) \in E$($1 \le i < N$)를 만족한다.
- **경로의 길이**<span class="gloss">length</span>: 경로 위 간선의 수 $N-1$. 간선이 없는 자기 자신으로의 경로는 길이 $0$이다.
- **루프**<span class="gloss">loop</span>: 간선 $(v, v)$, 즉 자기 자신으로 향하는 경로.
- **단순 경로**<span class="gloss">simple path</span>: 처음과 마지막 정점을 제외하고 방문하는 모든 정점이 서로 다른 경로.
- **순환**<span class="gloss">cycle</span>: 유향 그래프에서 길이가 최소 $1$이고 $w_1 = w_N$인 경로. 순환이 없으면 비순환<span class="gloss">acyclic</span>이다.
  - 무향 그래프에서 $u, v, u$는 순환으로 보지 않는다. $(u, v)$와 $(v, u)$가 같은 간선이기 때문이다.
  - 유향 그래프에서는 $(u, v)$와 $(v, u)$가 다른 간선이므로 $u, v, u$를 순환이라 부를 수 있다.

연결성도 그래프의 중요한 성질이다.

- 무향 그래프에서 모든 정점이 서로 연결되어 있으면 연결<span class="gloss">connected</span>되었다고 한다.
- 유향 그래프가 (방향을 고려해도) 연결되어 있으면 강하게 연결<span class="gloss">strongly connected</span>되었다고 한다.
  - 방향을 모두 없앤 기저 그래프만 연결되어 있으면 약하게 연결<span class="gloss">weakly connected</span>되었다고 한다.
- 모든 정점 쌍 사이에 간선이 있으면 완전 그래프<span class="gloss">complete graph</span>라고 한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-12.svg" alt="유향 그래프 예시" style="max-width: 360px;" />
  <figcaption class="cap">루프를 포함한 유향 그래프 예시</figcaption>
</figure>

### 인접 행렬 vs 인접 리스트

그래프를 표현하는 두 가지 대표적 방법이 있다.

- **인접 행렬**<span class="gloss">adjacency matrix</span>: 2차원 배열로, 간선 $(u, v)$가 있으면 `A[u][v]`를 `true`, 없으면 `false`로 둔다.
  - 가중치가 있으면 `A[u][v]`를 가중치 값으로 두고, 없는 간선은 아주 크거나 아주 작은 값으로 미리 채운다.
  - 공간이 $\Theta(|V|^2)$이므로 간선이 적은 그래프에는 낭비가 크다. 밀집<span class="gloss">dense</span>($|E| = \Theta(|V|^2)$) 그래프에 적합하다.
- **인접 리스트**<span class="gloss">adjacency list</span>: 각 정점마다 인접한 정점들을 나열한다.
  - 공간이 $\mathcal{O}(|E| + |V|)$로 그래프 크기에 선형 비례하므로, 희소<span class="gloss">sparse</span>한 그래프에 적절하다.

$$
A=\begin{bmatrix}
0 & 1 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 & 1 \\
1 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0
\end{bmatrix}
$$

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-13.svg" alt="인접 리스트 표현" style="max-width: 320px;" />
  <figcaption class="cap">같은 그래프의 인접 리스트 표현</figcaption>
</figure>

## 최소 경로 문제

가중치 그래프에서 간선 $(v_i, v_j)$를 지나는 데 비용 $c_{i,j}$가 든다고 할 때,
최소 경로<span class="gloss">shortest-path</span> 문제를 생각할 수 있다.

- 경로 $v_1 v_2 \dots v_N$의 비용은 $\sum_{i=1}^{N-1} c_{i, i+1}$이며, 이를 가중치 경로 길이<span class="gloss">weighted path length</span>라고 한다.
- 비가중치 경로 길이<span class="gloss">unweighted path length</span>는 경로 위 간선의 개수 $N-1$이다.
- 비가중치 문제는 **모든 간선의 가중치가 $1$인** 가중치 최소 경로 문제의 특수한 경우이다.

아래 그래프에서 $v_1$에서 $v_6$으로 가는 최소 비용 경로는 $v_1 \to v_4 \to v_7 \to v_6$으로 비용 $6$이며,
비가중치로 보면 최단 길이는 $2$이다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-14.svg" alt="가중치 유향 그래프" style="max-width: 420px;" />
  <figcaption class="cap">최소 경로 문제의 예시 가중치 유향 그래프</figcaption>
</figure>

### 다익스트라 알고리즘

단일-소스 최소 경로 문제<span class="gloss">single-source shortest-path problem</span>를 푸는
대표적인 방법이 다익스트라 알고리즘<span class="gloss">Dijkstra's algorithm</span>이다. 비가중치 경우와
비슷한 아이디어를 쓰되, 각 정점에 다음 정보를 유지한다.

1. 각 정점을 *known* 또는 *unknown*으로 표기한다.
2. 시험적인 거리 $d_v$를 각 정점에 기록한다.
3. 이 거리는 해당 정점이 *known*이 될 때 비로소 최소 경로로 확정된다.
4. $p_v$에는 $d_v$를 마지막으로 바꾸게 만든 정점을 기록한다.

각 단계에서 **아직 *unknown*인 정점 중 $d_v$가 가장 작은 정점 $v$를 선택**해 *known*으로
선언하고, $v$에 인접한 정점들의 $d$ 값을 갱신한다. 인접 노드 중 최솟값을 찾는 데 한 단계마다
$\mathcal{O}(|V|)$가 들어, 배열 기반 구현의 전체 복잡도는 $\mathcal{O}(|V|^2)$이다.

위 그래프에서 $v_1$을 시작점으로 알고리즘을 끝까지 수행한 최종 결과는 다음과 같다.

| 정점 | known | $d_v$ | $p_v$ |
| --- | --- | --- | --- |
| $v_1$ | T | $0$ | $0$ |
| $v_2$ | T | $2$ | $v_1$ |
| $v_3$ | T | $3$ | $v_4$ |
| $v_4$ | T | $1$ | $v_1$ |
| $v_5$ | T | $3$ | $v_4$ |
| $v_6$ | T | $6$ | $v_7$ |
| $v_7$ | T | $5$ | $v_4$ |

::: warning 음의 간선 주의
그래프에 **음의 간선 비용**이 있으면 다익스트라 알고리즘은 정상 동작하지 않는다.
보통은 모든 간선에 상수 $\Delta$를 더해 음의 간선을 없앤 뒤 알고리즘을 적용한다.
:::

### 실습: 다익스트라 알고리즘

위 그래프를 인접 리스트로 구성하고, 우선순위 큐를 이용해 $v_1$에서 각 정점까지의 최단
거리를 구한다. 출력이 위 최종 표의 $d_v$ 열과 정확히 일치하는지 확인해 보자.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int main() {
    const int N = 7;                 // 정점 v1..v7 (인덱스 1..7)
    vector<vector<pair<int,int>>> adj(N + 1);   // adj[u] = {(v, cost), ...}
    auto add = [&](int u, int v, int w){ adj[u].push_back({v, w}); };

    add(1,2,2); add(1,4,1);
    add(2,4,3); add(2,5,10);
    add(3,1,4); add(3,6,5);
    add(4,3,2); add(4,5,2); add(4,6,8); add(4,7,4);
    add(5,7,6);
    add(7,6,1);

    int s = 1;
    vector<int> dist(N + 1, INT_MAX);
    dist[s] = 0;
    // (거리, 정점) 최소 힙
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    pq.push({0, s});

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;       // 이미 더 짧은 경로로 확정된 정점
        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }

    cout << "v1 에서 각 정점까지의 최단 거리:" << endl;
    for (int v = 1; v <= N; ++v)
        cout << "  v" << v << " : " << dist[v] << endl;
    return 0;
}
```

</CppRunner>

::: tip 무가중 · 위상 정렬
모든 간선의 가중치가 같은 **무가중 그래프**에서는 단순한 BFS로 최단 거리를 구할 수 있다.
또한 방향성 비순환 그래프(DAG)라면 **위상 정렬** 순서대로 정점을 처리해 음의 가중치가 있어도
한 번의 순회로 최단 경로를 계산할 수 있다.
:::

## 최소 신장 트리

그래프 $G$의 최소 신장 트리<span class="gloss">minimum spanning tree</span>는 $G$의 모든 정점을
**가장 적은 비용으로 연결하는 트리**이다. $G$가 연결되어 있을 때에만 정의된다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-15.svg" alt="원본 가중치 그래프" style="max-width: 300px;" />
  <figcaption class="cap">원본 무향 가중치 그래프</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-16.svg" alt="최소 신장 트리" style="max-width: 300px;" />
  <figcaption class="cap">위 그래프의 최소 신장 트리</figcaption>
</figure>

### 프림 알고리즘

프림 알고리즘<span class="gloss">Prim's algorithm</span>은 트리를 한 정점씩 키워 가는 방식으로,
최소 경로 문제의 다익스트라 알고리즘과 근본적으로 동일하다.

- 각 정점에 대해 $d_v$, $p_v$, *known*/*unknown* 여부를 기록한다.
- $d_v$는 $v$를 *known* 정점 집합에 연결하는 **최소 간선의 비용**, $p_v$는 $d_v$를 바꾼 마지막 정점이다.
- 정점 $v$가 선택되면, 인접한 각 *unknown* 정점 $w$에 대해 $d_w = \min(d_w, c_{w, v})$로 갱신한다.

다익스트라와 마찬가지로 배열 기반 구현은 $\mathcal{O}(|V|^2)$이다. 아래는 $v_1$에서 시작한
프림 알고리즘이 트리를 키워 가는 과정이다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-17.svg" alt="프림 1단계" style="max-width: 220px;" />
  <figcaption class="cap">프림 1단계</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-18.svg" alt="프림 2단계" style="max-width: 220px;" />
  <figcaption class="cap">프림 2단계</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-19.svg" alt="프림 3단계" style="max-width: 220px;" />
  <figcaption class="cap">프림 3단계</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-20.svg" alt="프림 4단계" style="max-width: 220px;" />
  <figcaption class="cap">프림 4단계</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-21.svg" alt="프림 5단계" style="max-width: 220px;" />
  <figcaption class="cap">프림 5단계</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-22.svg" alt="프림 6단계" style="max-width: 220px;" />
  <figcaption class="cap">프림 6단계 — 완성된 최소 신장 트리</figcaption>
</figure>

### 크루스칼 알고리즘

크루스칼 알고리즘<span class="gloss">Kruskal's algorithm</span>은 여러 트리가 모인
**포레스트**<span class="gloss">forest</span>에서 출발한다.

- 비용이 작은 간선부터 순서대로 선택하되, 순환을 만들지 않는 간선만 추가한다.
- 알고리즘이 끝나면 트리 하나만 남고, 그것이 최소 신장 트리이다.
- 수행 시간은 $\mathcal{O}(|E| \log |E|)$이다. 순환 여부 판정 비용은 이보다 작다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-23.svg" alt="크루스칼 1단계" style="max-width: 220px;" />
  <figcaption class="cap">크루스칼 1단계</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-24.svg" alt="크루스칼 2단계" style="max-width: 220px;" />
  <figcaption class="cap">크루스칼 2단계</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-25.svg" alt="크루스칼 3단계" style="max-width: 220px;" />
  <figcaption class="cap">크루스칼 3단계</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-26.svg" alt="크루스칼 4단계" style="max-width: 220px;" />
  <figcaption class="cap">크루스칼 4단계 (두 개의 부분 트리)</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-27.svg" alt="크루스칼 5단계" style="max-width: 220px;" />
  <figcaption class="cap">크루스칼 5단계</figcaption>
</figure>

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-28.svg" alt="크루스칼 6단계" style="max-width: 220px;" />
  <figcaption class="cap">크루스칼 6단계 — 완성된 최소 신장 트리</figcaption>
</figure>

### 성능 비교

| 알고리즘 | 방식 | 시간 복잡도(배열 기반) |
| --- | --- | --- |
| 프림 | 트리를 한 정점씩 키움(정점 중심) | $\mathcal{O}(\vert V\vert^2)$ |
| 크루스칼 | 작은 간선부터 선택, 순환 회피(간선 중심) | $\mathcal{O}(\vert E\vert \log \vert E\vert)$ |

프림은 정점이 적고 간선이 많은 **밀집 그래프**에, 크루스칼은 간선이 적은 **희소 그래프**에
유리한 경향이 있다. 크루스칼은 순환 여부 판정을 위해 다음 페이지의
[서로소 집합](./disjoint-sets) 자료구조를 활용한다.
