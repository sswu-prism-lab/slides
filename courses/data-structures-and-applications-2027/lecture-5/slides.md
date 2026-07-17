---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 5
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-5-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 05: Trees, Priority Queues, and Graphs</p>

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
heading: Overview
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- In this lecture, we recap the data structures introduced so far and build up toward graph algorithms:

  - Review [trees]{.hl}, [binary trees]{.hl}, and [heaps]{.hl}, and how a heap backs a [priority queue]{.hl}.

  - Implement a [graph]{.hl} with an [adjacency matrix]{.hl} and an [adjacency list]{.hl}.

  - Traverse graphs with [depth-first search]{.hl} and [breadth-first search]{.hl}, then apply them to practice problems.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Recap: Trees, Heaps, and Priority Queues</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Tree, Binary Tree, and Heap</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Priority Queue Class</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Graph Implementation and Algorithms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Adjacency Matrix and Adjacency List</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Dijkstra and Floyd-Warshall</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Graph Traversal and Practice</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Depth-First and Breadth-First Search</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Target Number and Network</span></p>
  </div>

</div>

---
layout: prism
heading: "Recap: Tree, Binary Tree, and Heap"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [tree]{.hl} is a hierarchical structure of nodes with a single [root]{.hl}; every other node has exactly one parent.

- A [binary tree]{.hl} is a tree in which each node has at most two children (a *left* and a *right* child).

<div class="theorem-box">
<div class="theorem-box-title">Two special shapes</div>
<div class="theorem-box-body">

A [full binary tree]{.hl} has every node with either $0$ or $2$ children, and all leaves on the same level.
A [complete binary tree]{.hl} is filled on every level except possibly the last, which is filled from left to right.

</div>
</div>

- A [heap]{.hl} is a complete binary tree with the [heap-order property]{.hl}: in a [max heap]{.hl}, every parent is $\geq$ its children (the maximum sits at the root).

---
layout: prism
heading: "Recap: Heap as an Array"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Because a heap is a *complete* binary tree, it maps neatly onto an array (index $1 \ldots n$).

- For a node at index $i$:
  - parent is at $\lfloor i/2 \rfloor$,
  - children are at $2i$ and $2i+1$.

- "Sift-down" restores the max-heap order from the root downward.

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

Level-order array (1-indexed):

`[_, 11, 10, 9, 9, 7, 6, 4, 3, 5, 2, 2, 0]`

</div>
</div>

---
layout: prism
heading: "DIY: Building a Max Heap"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

// sift a value down to restore the max-heap order (1-indexed array)
void siftDown(vector<int>& h, int i, int n) {
    while (2 * i <= n) {
        int child = 2 * i;                          // left child
        if (child + 1 <= n && h[child + 1] > h[child]) child++;  // larger child
        if (h[i] >= h[child]) break;                // order already satisfied
        swap(h[i], h[child]);
        i = child;
    }
}

int main() {
    // index 0 unused; build a heap out of these values
    vector<int> h = {0, 3, 5, 2, 2, 0, 6, 4, 9, 7, 10, 9, 11};
    int n = h.size() - 1;

    for (int i = n / 2; i >= 1; i--)  // heapify from the last internal node up
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
heading: "Recap: The Priority Queue Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A [priority queue]{.hl} always dequeues the element of highest priority. C++ provides one backed by a heap in `<queue>`.

- By default `priority_queue<T>` is a [max heap]{.hl}: `top()` returns the *largest* element.

- Key operations: `push()`, `top()`, `pop()`, `empty()`, `size()` — each `push`/`pop` costs $\mathcal{O}(\log n)$.

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
heading: "Recap: Min-Heap Priority Queue"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- To make `top()` return the *smallest* element, declare the comparator explicitly:

  - `priority_queue<int, vector<int>, greater<int>>`.

- The three template arguments are the [element type]{.hl}, the [underlying container]{.hl}, and the [comparator]{.hl}.

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
heading: "DIY: Max-Heap and Min-Heap Priority Queues"
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
heading: "Recap: Graph Implementation"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- We can represent a graph using an [adjacency matrix]{.hl} (인접 행렬).

- Entry $(i, j)$ is $1$ if node $i$ is connected to node $j$, and $0$ otherwise.

- For an [undirected]{.hl} graph the matrix is symmetric: $A_{ij} = A_{ji}$.

- Space is $\mathcal{O}(V^2)$ — simple, but wasteful for [sparse]{.hl} graphs.

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

<div class="text-center" style="margin-top: 0.8rem; color:#9aa0a6; font-size: 0.85rem;">edges: 0-1, 0-2, 0-3, 0-5, 1-2, 2-4, 3-5, 4-5</div>

</div>
</div>

---
layout: prism
heading: "Recap: Adjacency List"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- An [adjacency list]{.hl} stores, for each node, only the neighbors it is actually connected to.

- Space is $\mathcal{O}(V + E)$ — the preferred choice for [sparse]{.hl} graphs and for traversal.

- In C++ this is naturally a `vector<vector<int>>`.

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
heading: "DIY: Adjacency Matrix and List"
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
heading: "Recap: Dijkstra's Algorithm"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [Dijkstra's algorithm]{.hl} finds shortest paths from a single source in a graph with [non-negative]{.hl} edge weights.

- It repeatedly settles the closest unvisited node, then [relaxes]{.hl} its outgoing edges.

- A [min-heap priority queue]{.hl} makes this efficient: $\mathcal{O}((V + E)\log V)$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w05/dsa-w05-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Dijkstra with a Priority Queue"
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
heading: "Recap: Floyd-Warshall Algorithm"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [Floyd-Warshall]{.hl} computes shortest paths between [all pairs]{.hl} of nodes.

- For every intermediate node $k$, it checks whether going $i \to k \to j$ beats the current $i \to j$ distance.

- Time is $\mathcal{O}(V^3)$; it also handles negative edges (but no negative cycles).

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w05/dsa-w05-image3.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Floyd-Warshall All-Pairs Shortest Paths"
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
heading: "DIY: Double-Ended Priority Queue"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [double priority queue]{.hl} supports both operations at once:
  - `I n` — insert $n$,
  - `D 1` — delete the [maximum]{.hl},
  - `D -1` — delete the [minimum]{.hl}.

- After all operations, report `[max, min]`, or `[0, 0]` if empty.

- A `multiset` keeps elements sorted, so both ends are $\mathcal{O}(\log n)$ to reach.

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
heading: "DIY: Double-Ended Priority Queue (Code)"
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
heading: "Depth-First Search (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [Depth-First Search]{.hl} (DFS; 깊이 우선 탐색) searches deeper into the graph whenever possible.

- It explores edges out of the most recently discovered node that still has unexplored edges, then [backtracks]{.hl} once a node is exhausted.

- If undiscovered nodes remain, DFS picks one as a new source and repeats.

- DFS uses a [stack]{.hl} (often the implicit call stack of recursion) and runs in $\mathcal{O}(V + E)$.

---
layout: prism
heading: "Depth-First Search (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Algorithm outline:
  - Choose a start node and create an empty stack.
  - Mark the start node as visited.
  - Push unvisited neighbors, marking them visited; otherwise pop and continue.
  - Repeat until every node is visited.

- Written recursively:

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

For the example graph, one visiting
order is `1 → 2 → 7 → 6 → 8 → 3 → 4 → 5`.

</div>
</div>

---
layout: prism
heading: "Depth-First Search (3/3)"
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
heading: "Breadth-First Search (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [Breadth-First Search]{.hl} (BFS; 너비 우선 탐색) expands the frontier between discovered and undiscovered nodes uniformly.

- It visits every node reachable from the source in order of increasing [distance]{.hl} (number of edges).

- BFS is the archetype for many graph algorithms — e.g. Prim's MST and Dijkstra's algorithm.

- BFS uses a [queue]{.hl} and runs in $\mathcal{O}(V + E)$.

---
layout: prism
heading: "Breadth-First Search (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Algorithm outline:
  - Choose a start node, create an empty queue, and mark the start visited.
  - Dequeue a node; push each unvisited neighbor and mark it visited.
  - Repeat until the queue is empty.

- Because BFS discovers nodes level by level, it directly yields shortest paths in [unweighted]{.hl} graphs.

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
heading: "Breadth-First Search (3/3)"
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
heading: "Practice: Target Number"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Given $n$ non-negative integers, add a `+` or `-` sign to each and count how many sign choices reach a [target]{.hl} value.

- This is a natural [DFS]{.hl} over a binary decision tree: at each number, branch on adding or subtracting.

- Example: `[1,1,1,1,1]`, target `3` → **5** ways.

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
heading: "Practice: Target Number (Code)"
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
heading: "Practice: Network"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Computers form a [network]{.hl} when connected directly or indirectly. Count the number of separate networks.

- The input `computers` is an [adjacency matrix]{.hl}; each network is a [connected component]{.hl}.

- Run DFS/BFS from every unvisited node — each new search discovers exactly one component.

- Example: `[[1,1,0],[1,1,0],[0,0,1]]` → **2**.

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
heading: "Practice: Network (Code)"
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
heading: "Homework: HW_W05"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Using your preferred coding-test platform (Baekjoon, Programmers, a problem set, etc.), find and solve [three problems]{.hl} that use a [priority queue]{.hl} or a [graph]{.hl}.
  - The six Programmers problems covered in class are excluded. Using additional data structures or algorithms is fine.

- For each problem, capture the [problem statement]{.hl}, your [solution code]{.hl}, and the [test result]{.hl}, and paste them into a single document.

- Try to solve the problems on your own without looking at the solutions. If you run out of time, submitting an honest unfinished attempt (even a failing result) is fine and will not be penalized.

- Save as `HW_W05_20XXXXXX.pdf` and upload it to the LMS.

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
