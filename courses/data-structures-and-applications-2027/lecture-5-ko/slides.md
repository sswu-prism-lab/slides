---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 5 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-5/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">5주차: 트리, 우선순위 큐, 그래프</p>

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
heading: Overview
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 이번 강의에서는 지금까지 배운 자료구조를 복습하고 그래프 알고리즘으로 나아갑니다:

  - [트리]{.hl}, [이진 트리]{.hl}, [힙]{.hl}을 복습하고, 힙이 어떻게 [우선순위 큐]{.hl}를 뒷받침하는지 살펴봅니다.

  - [인접 행렬]{.hl}과 [인접 리스트]{.hl}로 [그래프]{.hl}를 구현합니다.

  - [깊이 우선 탐색]{.hl}과 [너비 우선 탐색]{.hl}으로 그래프를 순회하고, 이를 연습 문제에 적용합니다.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">복습: 트리, 힙, 우선순위 큐</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">트리, 이진 트리, 힙</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">우선순위 큐 클래스</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">그래프 구현과 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">인접 행렬과 인접 리스트</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">다익스트라와 플로이드-워셜</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">그래프 순회와 실습</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">깊이 우선 탐색과 너비 우선 탐색</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">타겟 넘버와 네트워크</span></p>
  </div>

</div>

---
layout: prism
heading: "복습: 트리, 이진 트리, 힙"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [트리]{.hl}는 하나의 [루트]{.hl}를 가지는 노드들의 계층 구조로, 루트를 제외한 모든 노드는 정확히 하나의 부모를 가집니다.

- [이진 트리]{.hl}는 각 노드가 최대 두 개의 자식(*왼쪽* 자식과 *오른쪽* 자식)을 가지는 트리입니다.

<div class="theorem-box">
<div class="theorem-box-title">두 가지 특별한 형태</div>
<div class="theorem-box-body">

[포화 이진 트리]{.hl}는 모든 노드가 $0$개 또는 $2$개의 자식을 가지며, 모든 리프가 같은 레벨에 있는 트리입니다.
[완전 이진 트리]{.hl}는 마지막 레벨을 제외한 모든 레벨이 꽉 차 있고, 마지막 레벨은 왼쪽부터 채워지는 트리입니다.

</div>
</div>

- [힙]{.hl}은 [힙 순서 성질]{.hl}을 만족하는 완전 이진 트리입니다: [최대 힙]{.hl}에서는 모든 부모가 자식보다 크거나 같아($\geq$) 최댓값이 루트에 위치합니다.

---
layout: prism
heading: "복습: 배열로 표현한 힙"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 힙은 *완전* 이진 트리이므로 배열(인덱스 $1 \ldots n$)에 깔끔하게 대응됩니다.

- 인덱스 $i$에 있는 노드에 대해:
  - 부모는 $\lfloor i/2 \rfloor$에,
  - 자식은 $2i$와 $2i+1$에 위치합니다.

- "sift-down"은 루트에서 아래로 내려가며 최대 힙 순서를 복원합니다.

</div>
<div>

<div style="height: 1rem;"></div>

```text
        11
      /    \
    10      9
   /  \    / \
  9    7  6   4
 / \  /  /
3  5 2  2  0
```

레벨 순서 배열 (1부터 시작):

`[_, 11, 10, 9, 9, 7, 6, 4, 3, 5, 2, 2, 0]`

</div>
</div>

---
layout: prism
heading: "DIY: 최대 힙 만들기"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

// 값을 아래로 내려보내 최대 힙 순서를 복원한다 (1부터 시작하는 배열)
void siftDown(vector<int>& h, int i, int n) {
    while (2 * i <= n) {
        int child = 2 * i;                          // 왼쪽 자식
        if (child + 1 <= n && h[child + 1] > h[child]) child++;  // 더 큰 자식
        if (h[i] >= h[child]) break;                // 이미 순서 만족
        swap(h[i], h[child]);
        i = child;
    }
}

int main() {
    // 인덱스 0은 사용하지 않음; 이 값들로 힙을 만든다
    vector<int> h = {0, 3, 5, 2, 2, 0, 6, 4, 9, 7, 10, 9, 11};
    int n = h.size() - 1;

    for (int i = n / 2; i >= 1; i--)  // 마지막 내부 노드부터 위로 힙화
        siftDown(h, i, n);

    cout << "Max heap (level order): ";
    for (int i = 1; i <= n; i++) cout << h[i] << " ";
    cout << "\nRoot (maximum) = " << h[1] << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: 우선순위 큐 클래스"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [우선순위 큐]{.hl}는 항상 우선순위가 가장 높은 원소를 꺼냅니다. C++은 `<queue>`에서 힙으로 구현된 우선순위 큐를 제공합니다.

- 기본적으로 `priority_queue<T>`는 [최대 힙]{.hl}입니다: `top()`은 *가장 큰* 원소를 반환합니다.

- 주요 연산: `push()`, `top()`, `pop()`, `empty()`, `size()` — 각 `push`/`pop`은 $\mathcal{O}(\log n)$이 듭니다.

</div>
<div>

<div style="height: 1.5rem;"></div>

```cpp
#include <queue>

priority_queue<int> pq;
pq.push(1);
pq.push(9);
pq.push(3);
pq.top();   // 9  (largest)

// pair: ordered by .first, then .second
priority_queue<pair<int,int>> pq2;
pq2.push({1, 2});
pq2.push({1, 3});
pq2.push({3, 2});
pq2.top().first;   // 3
```

</div>
</div>

---
layout: prism
heading: "복습: 최소 힙 우선순위 큐"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- `top()`이 *가장 작은* 원소를 반환하게 하려면 비교자를 명시적으로 지정합니다:

  - `priority_queue<int, vector<int>, greater<int>>`.

- 세 개의 템플릿 인자는 각각 [원소 타입]{.hl}, [기반 컨테이너]{.hl}, [비교자]{.hl}입니다.

</div>
<div>

<div style="height: 2rem;"></div>

```cpp
// max heap (default)
priority_queue<int> maxPq;

// min heap
priority_queue<int,
               vector<int>,
               greater<int>> minPq;

minPq.push(1);
minPq.push(9);
minPq.push(3);
minPq.top();   // 1  (smallest)
```

</div>
</div>

---
layout: prism
heading: "DIY: 최대 힙과 최소 힙 우선순위 큐"
---

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int data[] = {1, 9, 3, 7, 5};

    priority_queue<int> maxPq;                              // max heap
    priority_queue<int, vector<int>, greater<int>> minPq;   // min heap
    for (int x : data) { maxPq.push(x); minPq.push(x); }

    cout << "max-heap pop order: ";
    while (!maxPq.empty()) { cout << maxPq.top() << " "; maxPq.pop(); }
    cout << "\nmin-heap pop order: ";
    while (!minPq.empty()) { cout << minPq.top() << " "; minPq.pop(); }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: 그래프 구현"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 그래프는 [인접 행렬]{.hl}(인접 행렬)로 표현할 수 있습니다.

- 원소 $(i, j)$는 노드 $i$가 노드 $j$와 연결되어 있으면 $1$, 그렇지 않으면 $0$입니다.

- [무방향]{.hl} 그래프에서는 행렬이 대칭입니다: $A_{ij} = A_{ji}$.

- 공간은 $\mathcal{O}(V^2)$입니다 — 단순하지만 [희소]{.hl} 그래프에는 낭비가 큽니다.

</div>
<div>

<div style="height: 0.5rem;"></div>

<div class="text-center" style="font-family: 'JetBrains Mono', Consolas, monospace; font-size: 0.95rem;">

|       | 0 | 1 | 2 | 3 | 4 | 5 |
|:-----:|:-:|:-:|:-:|:-:|:-:|:-:|
| **0** | 0 | 1 | 1 | 1 | 0 | 1 |
| **1** | 1 | 0 | 1 | 0 | 0 | 0 |
| **2** | 1 | 1 | 0 | 0 | 1 | 0 |
| **3** | 1 | 0 | 0 | 0 | 0 | 1 |
| **4** | 0 | 0 | 1 | 0 | 0 | 1 |
| **5** | 1 | 0 | 0 | 1 | 1 | 0 |

</div>

<div class="text-center" style="margin-top: 0.8rem; color:#9aa0a6; font-size: 0.85rem;">간선: 0-1, 0-2, 0-3, 0-5, 1-2, 2-4, 3-5, 4-5</div>

</div>
</div>

---
layout: prism
heading: "복습: 인접 리스트"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [인접 리스트]{.hl}는 각 노드에 대해 실제로 연결된 이웃만 저장합니다.

- 공간은 $\mathcal{O}(V + E)$입니다 — [희소]{.hl} 그래프와 순회에 선호되는 방식입니다.

- C++에서는 자연스럽게 `vector<vector<int>>`로 표현됩니다.

</div>
<div>

<div style="height: 1.5rem;"></div>

```text
0 -> 1, 2, 3, 5
1 -> 0, 2
2 -> 0, 1, 4
3 -> 0, 5
4 -> 2, 5
5 -> 0, 3, 4
```

</div>
</div>

---
layout: prism
heading: "DIY: 인접 행렬과 인접 리스트"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int V = 6;
    int edges[][2] = {{0,1},{0,2},{0,3},{0,5},{1,2},{2,4},{3,5},{4,5}};

    vector<vector<int>> mat(V, vector<int>(V, 0));  // adjacency matrix
    vector<vector<int>> adj(V);                     // adjacency list
    for (auto& e : edges) {
        int u = e[0], v = e[1];
        mat[u][v] = mat[v][u] = 1;                  // undirected
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    cout << "Adjacency matrix:\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) cout << mat[i][j] << " ";
        cout << "\n";
    }
    cout << "\nAdjacency list:\n";
    for (int i = 0; i < V; i++) {
        cout << i << " -> ";
        for (int v : adj[i]) cout << v << " ";
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: 다익스트라 알고리즘"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [다익스트라 알고리즘]{.hl}은 간선 가중치가 [음이 아닌]{.hl} 그래프에서 하나의 출발점으로부터의 최단 경로를 구합니다.

- 방문하지 않은 노드 중 가장 가까운 노드를 반복적으로 확정한 뒤, 그 노드에서 나가는 간선을 [완화(relax)]{.hl}합니다.

- [최소 힙 우선순위 큐]{.hl}를 쓰면 효율적입니다: $\mathcal{O}((V + E)\log V)$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w05/dsa-w05-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 우선순위 큐를 이용한 다익스트라"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
const int INF = 1e9;

int main() {
    int V = 5;                          // nodes s=0, t=1, x=2, y=3, z=4
    vector<vector<pair<int,int>>> adj(V);   // adj[u] = {(v, weight), ...}
    auto add = [&](int u, int v, int w) { adj[u].push_back({v, w}); };
    add(0,1,10); add(0,3,5); add(1,2,1); add(1,3,2); add(3,1,3);
    add(3,2,9); add(3,4,2); add(2,4,4); add(4,2,6); add(4,0,7);

    vector<int> dist(V, INF);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    dist[0] = 0;
    pq.push({0, 0});                    // (distance, node)

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;      // stale entry
        for (auto [v, w] : adj[u])
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
    }
    cout << "shortest distances from s: ";
    for (int i = 0; i < V; i++) cout << dist[i] << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "복습: 플로이드-워셜 알고리즘"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [플로이드-워셜]{.hl}은 [모든 노드 쌍]{.hl} 사이의 최단 경로를 계산합니다.

- 모든 중간 노드 $k$에 대해, $i \to k \to j$로 가는 것이 현재의 $i \to j$ 거리보다 짧은지 확인합니다.

- 시간 복잡도는 $\mathcal{O}(V^3)$이며, 음의 간선도 처리할 수 있습니다(단, 음의 사이클은 불가).

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w05/dsa-w05-image3.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 플로이드-워셜 모든 쌍 최단 경로"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;
const int INF = 1e9;

int main() {
    int V = 4;                                  // nodes 1..4 -> index 0..3
    vector<vector<int>> d = {
        {0,   8,   INF, 1  },
        {INF, 0,   1,   INF},
        {4,   INF, 0,   INF},
        {INF, 2,   9,   0  }
    };

    for (int k = 0; k < V; k++)                 // intermediate node
        for (int i = 0; i < V; i++)
            for (int j = 0; j < V; j++)
                if (d[i][k] + d[k][j] < d[i][j])
                    d[i][j] = d[i][k] + d[k][j];

    cout << "all-pairs shortest distances:\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) cout << d[i][j] << " ";
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY: 이중 우선순위 큐"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [이중 우선순위 큐]{.hl}는 두 연산을 동시에 지원합니다:
  - `I n` — $n$을 삽입,
  - `D 1` — [최댓값]{.hl}을 삭제,
  - `D -1` — [최솟값]{.hl}을 삭제.

- 모든 연산이 끝나면 `[max, min]`을 보고하고, 비어 있으면 `[0, 0]`을 보고합니다.

- `multiset`은 원소를 정렬 상태로 유지하므로 양쪽 끝 모두 $\mathcal{O}(\log n)$에 접근할 수 있습니다.

</div>
<div>

<div style="height: 3rem;"></div>

```text
["I 16","I -5643","D -1",
 "D 1","D 1","I 123","D -1"]
                     -> [0, 0]

["I -45","I 653","D 1","I -642",
 "I 45","I 97","D 1","D -1","I 333"]
                     -> [333, -45]
```

</div>
</div>

---
layout: prism
heading: "DIY: 이중 우선순위 큐 (코드)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
using namespace std;

vector<int> solution(vector<string> operations) {
    multiset<int> s;                            // always kept sorted
    for (const string& op : operations) {
        stringstream ss(op);
        string cmd; int num;
        ss >> cmd >> num;
        if (cmd == "I") s.insert(num);
        else if (!s.empty()) {
            if (num == 1) s.erase(prev(s.end()));  // delete maximum
            else s.erase(s.begin());               // delete minimum
        }
    }
    if (s.empty()) return {0, 0};
    return {*s.rbegin(), *s.begin()};           // {max, min}
}

int main() {
    auto a = solution({"I 16","I -5643","D -1","D 1","D 1","I 123","D -1"});
    auto b = solution({"I -45","I 653","D 1","I -642","I 45","I 97","D 1","D -1","I 333"});
    cout << "[" << a[0] << ", " << a[1] << "]\n";
    cout << "[" << b[0] << ", " << b[1] << "]\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "깊이 우선 탐색 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [깊이 우선 탐색]{.hl}(DFS; 깊이 우선 탐색)은 가능한 한 그래프의 더 깊은 곳으로 탐색해 들어갑니다.

- 아직 탐색하지 않은 간선이 남아 있는, 가장 최근에 발견된 노드에서 나가는 간선을 탐색하고, 그 노드를 모두 탐색하면 [백트래킹]{.hl}합니다.

- 발견되지 않은 노드가 남아 있으면, DFS는 그중 하나를 새로운 출발점으로 선택하여 반복합니다.

- DFS는 [스택]{.hl}(흔히 재귀 호출의 암묵적 호출 스택)을 사용하며 $\mathcal{O}(V + E)$에 동작합니다.

---
layout: prism
heading: "깊이 우선 탐색 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 알고리즘 개요:
  - 시작 노드를 고르고 빈 스택을 만든다.
  - 시작 노드를 방문 처리한다.
  - 방문하지 않은 이웃을 스택에 넣고 방문 처리한다; 없으면 하나를 꺼내(pop) 계속한다.
  - 모든 노드를 방문할 때까지 반복한다.

- 재귀로 작성하면:

</div>
<div>

<div style="height: 2rem;"></div>

```text
DFS(graph, v, visited):
    visited[v] = true
    for u in graph[v]:
        if not visited[u]:
            DFS(graph, u, visited)
```

<div style="height: 1rem;"></div>

예시 그래프에서 방문 순서의
한 가지는 `1 → 2 → 7 → 6 → 8 → 3 → 4 → 5` 입니다.

</div>
</div>

---
layout: prism
heading: "깊이 우선 탐색 (3/3)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> graph;
vector<bool> visited;

void dfs(int v) {
    visited[v] = true;
    cout << v << " ";
    for (int u : graph[v])
        if (!visited[u]) dfs(u);
}

int main() {
    int n = 8;                                  // nodes 1..8
    graph.assign(n + 1, {});
    visited.assign(n + 1, false);
    int edges[][2] = {{1,2},{1,3},{1,5},{2,7},{3,4},{4,5},{7,6},{7,8}};
    for (auto& e : edges) {                     // build sorted adjacency list
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }
    for (int v = 1; v <= n; v++) sort(graph[v].begin(), graph[v].end());

    cout << "DFS from 1: ";
    dfs(1);
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "너비 우선 탐색 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [너비 우선 탐색]{.hl}(BFS; 너비 우선 탐색)은 발견된 노드와 발견되지 않은 노드 사이의 경계를 균일하게 확장합니다.

- 출발점에서 도달 가능한 모든 노드를 [거리]{.hl}(간선 수)가 증가하는 순서로 방문합니다.

- BFS는 많은 그래프 알고리즘의 원형입니다 — 예를 들어 프림의 최소 신장 트리(MST)와 다익스트라 알고리즘이 그렇습니다.

- BFS는 [큐]{.hl}를 사용하며 $\mathcal{O}(V + E)$에 동작합니다.

---
layout: prism
heading: "너비 우선 탐색 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 알고리즘 개요:
  - 시작 노드를 고르고 빈 큐를 만든 뒤 시작 노드를 방문 처리한다.
  - 노드를 하나 꺼내(dequeue) 방문하지 않은 이웃을 각각 큐에 넣고 방문 처리한다.
  - 큐가 빌 때까지 반복한다.

- BFS는 노드를 레벨 단위로 발견하므로, [비가중]{.hl} 그래프에서 곧바로 최단 경로를 얻습니다.

</div>
<div>

<div style="height: 2rem;"></div>

```text
BFS(graph, s):
    q.push(s); visited[s] = true
    while q not empty:
        v = q.pop()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = true
                q.push(u)
```

</div>
</div>

---
layout: prism
heading: "너비 우선 탐색 (3/3)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
    int n = 8;                                  // nodes 1..8
    vector<vector<int>> graph(n + 1);
    int edges[][2] = {{1,2},{1,3},{1,5},{2,7},{3,4},{4,5},{7,6},{7,8}};
    for (auto& e : edges) {
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }
    for (int v = 1; v <= n; v++) sort(graph[v].begin(), graph[v].end());

    vector<bool> visited(n + 1, false);
    queue<int> q;
    q.push(1); visited[1] = true;

    cout << "BFS from 1: ";
    while (!q.empty()) {
        int v = q.front(); q.pop();
        cout << v << " ";
        for (int u : graph[v])
            if (!visited[u]) { visited[u] = true; q.push(u); }
    }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "실습: 타겟 넘버"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- $n$개의 음이 아닌 정수가 주어질 때, 각 수에 `+` 또는 `-` 부호를 붙여 [타겟]{.hl} 값에 도달하는 부호 선택이 몇 가지인지 셉니다.

- 이는 이진 결정 트리에 대한 자연스러운 [DFS]{.hl}입니다: 각 수에서 더할지 뺄지로 분기합니다.

- 예시: `[1,1,1,1,1]`, 타겟 `3` → **5** 가지.

</div>
<div>

<div style="height: 3rem;"></div>

```text
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
```

</div>
</div>

---
layout: prism
heading: "실습: 타겟 넘버 (코드)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int cnt = 0;

void dfs(const vector<int>& nums, int idx, int sum, int target) {
    if (idx == (int)nums.size()) {          // used every number
        if (sum == target) cnt++;
        return;
    }
    dfs(nums, idx + 1, sum + nums[idx], target);   // add
    dfs(nums, idx + 1, sum - nums[idx], target);   // subtract
}

int solution(vector<int> numbers, int target) {
    cnt = 0;
    dfs(numbers, 0, 0, target);
    return cnt;
}

int main() {
    cout << solution({1, 1, 1, 1, 1}, 3) << "\n";   // 5
    cout << solution({4, 1, 2, 1}, 4) << "\n";       // 2
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "실습: 네트워크"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 컴퓨터들이 직접 또는 간접적으로 연결되면 하나의 [네트워크]{.hl}를 이룹니다. 서로 분리된 네트워크의 개수를 셉니다.

- 입력 `computers`는 [인접 행렬]{.hl}이며, 각 네트워크는 하나의 [연결 요소]{.hl}입니다.

- 방문하지 않은 모든 노드에서 DFS/BFS를 실행합니다 — 새로운 탐색마다 정확히 하나의 연결 요소를 발견합니다.

- 예시: `[[1,1,0],[1,1,0],[0,0,1]]` → **2**.

</div>
<div>

<div style="height: 3rem;"></div>

```text
n = 3
[[1,1,0],
 [1,1,0],   -> 2 networks
 [0,0,1]]

[[1,1,0],
 [1,1,1],   -> 1 network
 [0,1,1]]
```

</div>
</div>

---
layout: prism
heading: "실습: 네트워크 (코드)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> computers;
vector<bool> visited;

void dfs(int v, int n) {
    visited[v] = true;
    for (int u = 0; u < n; u++)
        if (computers[v][u] == 1 && !visited[u]) dfs(u, n);
}

int solution(int n, vector<vector<int>> c) {
    computers = c;
    visited.assign(n, false);
    int networks = 0;
    for (int v = 0; v < n; v++)
        if (!visited[v]) { dfs(v, n); networks++; }  // one new component
    return networks;
}

int main() {
    cout << solution(3, {{1,1,0},{1,1,0},{0,0,1}}) << "\n";   // 2
    cout << solution(3, {{1,1,0},{1,1,1},{0,1,1}}) << "\n";   // 1
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "과제: HW_W05"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 선호하는 코딩 테스트 연습 수단(백준, 프로그래머스, 문제집 등)을 이용해, [우선순위 큐]{.hl} 또는 [그래프]{.hl}가 쓰인 [세 문제]{.hl}를 찾아 풀어보세요.
  - 수업 시간에 다룬 프로그래머스 6개 문제는 제외입니다. 다른 자료구조나 알고리즘이 추가로 쓰이는 것은 상관없습니다.

- 각 문제에 대해 [문제 설명]{.hl}, 본인의 [풀이 코드]{.hl}, [테스트 결과]{.hl}를 캡처하여 하나의 문서에 붙여넣으세요.

- 해답을 참고하지 않고 최대한 스스로 풀어보세요. 기한 내에 다 풀지 못했더라도, 해답을 보지 않고 솔직하게 시도한 결과(통과하지 못한 결과라도)를 그대로 제출하면 감점하지 않습니다.

- `HW_W05_20XXXXXX.pdf`로 저장한 뒤 LMS에 업로드하세요.

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
