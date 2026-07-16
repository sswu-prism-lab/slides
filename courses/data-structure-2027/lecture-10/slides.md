---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 10
download: true
info: |
  ## Data Structure Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-10-ko/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Data Structure</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 10: Graphs and Weighted Graphs</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">Wonjun Ko, Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">Spring 2027</p>
</div>

---
layout: prism
heading: Course Schedule
---

<div class="absolute left-10 right-10" style="top: 0rem; bottom: 0rem; display: grid; grid-template-columns: 1.2fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">Course Introduction</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">Basic Mathematics and C++ Details</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">Algorithm Analysis</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">Lists, Stacks, and Queues</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">Circular Queues and Priority Queues</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">Trees and Tries</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">Midterm Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">Midterm Exam</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">Heaps</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span class="text-gray-900 dark:text-gray-100">Graphs and Weighted Graphs</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">Sets and Maps</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Hash Tables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Algorithm Design Techniques</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: "Recap: d-Heaps"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Binary heaps are so simple that they are almost always used when priority queues are needed.

- A simple generalization is a [$d$-heap]{.hl}, which is exactly like a binary heap except that all nodes have $d$ children (so a binary heap is a $2$-heap).

- The figure on the right is an example of a $3$-heap.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-01.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Recap: Leftist Heaps"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The [leftist heap property]{.hl} states that for every node $X$, the null path length of the left child is at least as large as that of the right child.
  - Nodes in the figures denote null path lengths; only the left one is a leftist heap.

- This property deliberately makes the tree *unbalanced*, biasing it to get deep toward the left.
  - A long path of left nodes is possible (and preferable, to facilitate merging) — hence the name *leftist* heap.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-02.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Graphs and Weighted Graphs
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- The [graph]{.hl} data structure is not only useful in practice, but also interesting: in many *real-life* applications the algorithms are too slow unless careful attention is paid to the choice of data structures.

- In this lecture, we discuss graph data structures and some useful algorithms:

<div class="sub-item-enum">

1. Show several real-life problems that can be converted to problems on graphs.
2. Give algorithms to solve several common graph problems.
3. Show how the proper choice of data structures can drastically reduce the running time of these algorithms.

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Graphs</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Definitions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Representation of Graphs</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Shortest-Path Algorithms</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Minimum Spanning Tree</span></p>
  </div>

</div>

---
layout: prism
heading: "Definitions: Vertices and Edges"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A graph $G = (V, E)$ consists of a set of [vertices]{.hl}, $V$, and a set of [edges]{.hl}, $E$.
  - Each edge is a pair $(v, w)$, where $v, w \in V$. Edges are sometimes referred to as [arcs]{.hl}.

- If the pair is ordered, then the graph is [directed]{.hl}.
  - Directed graphs are sometimes referred to as [digraphs]{.hl}.

- Vertex $w$ is [adjacent]{.hl} to $v$ if and only if $(v, w) \in E$.
  - In an undirected graph with edge $(v, w)$ — and hence $(w, v)$ — $w$ is adjacent to $v$ and $v$ is adjacent to $w$.

- Sometimes an edge has a third component, known as either a [weight]{.hl} or a [cost]{.hl}.

---
layout: prism
heading: "Definitions: Paths"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [path]{.hl} in a graph is a sequence of vertices $w_1, w_2, w_3, \ldots, w_N$ such that $(w_i, w_{i+1}) \in E$ for $1 \leq i < N$.

- The [length]{.hl} of such a path is the number of edges on the path, equal to $N - 1$.
  - We allow a path from a vertex to itself; if this path contains no edges, its length is $0$.

- If the graph contains an edge $(v, v)$ from a vertex to itself, then the path $v, v$ is sometimes referred to as a [loop]{.hl}.
  - The graphs we consider will generally be loopless.

- A [simple path]{.hl} is a path such that all vertices are distinct, except that the first and last could be the same.

---
layout: prism
heading: "Definitions: Cycles and Connectivity"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- A [cycle]{.hl} in a directed graph is a path of length at least $1$ such that $w_1 = w_N$; the cycle is *simple* if the path is simple.
  - For undirected graphs, we require the edges to be distinct: the path $u, v, u$ should not count as a cycle, since $(u, v)$ and $(v, u)$ are the same edge.
  - In a directed graph, $(u, v)$ and $(v, u)$ are different edges, so $u, v, u$ *is* a cycle.

- A directed graph is [acyclic]{.hl} if it has no cycles. A directed acyclic graph is abbreviated [DAG]{.hl}.

- An undirected graph is [connected]{.hl} if there is a path from every vertex to every other vertex.
  - A directed graph with this property is called [strongly connected]{.hl}.
  - If a directed graph is not strongly connected, but its underlying undirected graph is connected, the graph is [weakly connected]{.hl}.

- A [complete graph]{.hl} is a graph with an edge between every pair of vertices.

---
layout: prism
heading: "Example: Modeling with Graphs"
---

- A real-life situation modeled by a graph is the [airport system]{.hl}.
  - Each airport is a vertex; two vertices are connected by an edge if there is a nonstop flight between them.
  - The edge could carry a weight representing time, distance, or cost of the flight.
  - It is reasonable to assume the graph is *directed*, since flying in different directions may take longer or cost more.

- We would like the airport system to be [strongly connected]{.hl}, so that it is always possible to fly from any airport to any other.
  - We might also want to quickly determine the best flight between any two airports.

- [Traffic flow]{.hl} can likewise be modeled by a graph: each street intersection is a vertex, each street an edge, with edge costs such as a speed limit or capacity.
  - We could then ask for the shortest route, or find likely locations for bottlenecks.

---
layout: prism
heading: "HW_W10: Real-Life Examples Modeled by Graphs"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- Give an example of a real-life situation that can be modeled by a graph (or graphs).

- You have to define the [vertex]{.hl} and [edge]{.hl} clearly.

- You also have to provide the properties of your system (i.e., directed or undirected, connected, complete) and a real-world problem (e.g., find the best flight between two airports).

- Come up with your description and upload it to LMS.
  - You could write it in Korean.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Graphs</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Definitions</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Representation of Graphs</span></p>
  </div>

</div>

---
layout: prism
heading: "Representation of Graphs: Adjacency Matrix"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.5fr 1fr;">
<div>

- We consider directed graphs (undirected graphs are represented similarly).

- One simple way to represent a graph is a two-dimensional array — the [adjacency matrix]{.hl} representation.
  - For each edge $(u, v)$, set $A[u][v]$ to `true`; otherwise the entry is `false`.
  - If the edge has a weight, set $A[u][v]$ to the weight, using a very large or very small sentinel for nonexistent edges.

$$
A = \begin{bmatrix}
0 & 1 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 & 1 \\
1 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0
\end{bmatrix}
$$

</div>
<div>

<div style="height: 0rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-03.svg" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "Representation of Graphs: Adjacency List"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- Although the adjacency matrix is extremely simple, its space requirement is $\Theta(|V|^2)$, which can be prohibitive if the graph has few edges.
  - It is appropriate when the graph is [dense]{.hl}: $|E| = \Theta(|V|^2)$.

- If the graph is [sparse]{.hl}, a better solution is the [adjacency list]{.hl} representation.

- For each vertex we keep a list of all adjacent vertices; the space requirement is $\mathcal{O}(|E| + |V|)$, linear in the size of the graph.

</div>
<div>

<div style="height: 0rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-04.svg" class="tikz-fig" style="width: 95%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Adjacency List Representation"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int N = 5;                       // vertices 1..5
    // directed edges (u, v) of the example graph
    vector<pair<int,int>> edges = {
        {1,2},{1,3}, {2,2},{2,3},{2,4},
        {3,4},{3,5}, {4,1},{4,4}, {5,4}
    };

    vector<vector<int>> adj(N + 1);        // adjacency list
    for (auto [u, v] : edges) adj[u].push_back(v);

    for (int u = 1; u <= N; u++) {
        cout << u << " -> ";
        for (int v : adj[u]) cout << v << " ";
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Graphs</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Shortest-Path Algorithms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Shortest-Path Problem</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Unweighted Shortest Paths</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Dijkstra's Algorithm</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Graphs with Negative Edge Costs</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Minimum Spanning Tree</span></p>
  </div>

</div>

---
layout: prism
heading: The Shortest-Path Problem
---

- We examine various shortest-path problems. The input is a [weighted graph]{.hl}: associated with each edge $(v_i, v_j)$ is a cost $c_{i,j}$ to traverse the edge.

- The cost of a path $v_1 v_2 \ldots v_N$ is $\sum_{i=1}^{N-1} c_{i, i+1}$, referred to as the [weighted path length]{.hl}.
  - The [unweighted path length]{.hl} is merely the number of edges on the path, namely $N - 1$.

<div style="height: 1rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Single-Source Shortest-Path Problem</div>
<div class="theorem-box-body">

Given as input a weighted graph $G = (V, E)$ and a distinguished vertex $s$, find the shortest weighted path from $s$ to every other vertex in $G$.

</div>
</div>

---
layout: prism
heading: "Shortest-Path Problem: Example"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- On the right, the shortest weighted path from $v_1$ to $v_6$ has cost $6$, going $v_1 \to v_4 \to v_7 \to v_6$.
  - The shortest *unweighted* path between these vertices is $2$.

- For an [unweighted graph]{.hl}, we care only about the number of edges on the path, so there are no weights.
  - This is a special case of the weighted problem — assign every edge a weight of $1$.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-05.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Unweighted Shortest Paths
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Suppose we choose $s$ to be $v_3$.
  - The shortest path from $s$ to $v_3$ is a path of length $0$, so we can mark this immediately.
  - Then we look for all vertices a distance $1$ away from $s$, and so on.

- This strategy for searching a graph is known as [breadth-first search]{.hl}.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-06.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: Unweighted Shortest Paths (BFS)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    const int N = 7;                       // vertices v1..v7
    vector<vector<int>> adj(N + 1);
    auto add = [&](int u, int v){ adj[u].push_back(v); };
    add(1,2); add(1,4); add(2,4); add(2,5);
    add(3,1); add(3,6); add(4,3); add(4,5);
    add(4,6); add(4,7); add(5,7); add(7,6);

    int s = 3;                             // start vertex v3
    vector<int> dist(N + 1, -1);
    queue<int> q;
    dist[s] = 0; q.push(s);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u])
            if (dist[v] == -1) { dist[v] = dist[u] + 1; q.push(v); }
    }

    for (int v = 1; v <= N; v++)
        cout << "dist(v" << s << " -> v" << v << ") = " << dist[v] << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Dijkstra's Algorithm: Idea"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- If the graph is weighted, the problem apparently becomes harder, but we reuse the ideas from the unweighted case:

<div class="sub-item-enum">

1. Each vertex is marked as either *known* or *unknown*.
2. A tentative distance $d_v$ is kept for each vertex, as before.
3. This distance is the shortest path length from $s$ to $v$ using only *known* vertices as intermediates.
4. We record $p_v$, the last vertex to cause a change to $d_v$.

</div>

- This general method to solve the single-source shortest-path problem is known as [Dijkstra's algorithm]{.hl}, and proceeds in *stages*, like the unweighted algorithm.

- At each stage, Dijkstra's algorithm selects the vertex $v$ with the smallest $d_v$ among all *unknown* vertices, declares its shortest path *known*, then updates the values of $d_w$.

---
layout: prism
heading: "Dijkstra's Algorithm: Initialization"
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 1px 12px; line-height: 1.12; }
.slidev-layout table { font-size: 0.9em; }
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1fr 1fr;">
<div>

- The tables trace Dijkstra's algorithm on the weighted graph at the right.
  - Assume $v_1$ is the starting point.

- Initially every vertex is *unknown* (`F`), with $d_{v_1} = 0$ and all other distances $\infty$.

<div style="margin-top: 0rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-07.svg" class="tikz-fig" style="width: 80%;" />

</div>
<div>

| $v$ | *known* | $d_v$ | $p_v$ |
|:---:|:---:|:---:|:---:|
| $v_1$ | F | $0$ | $0$ |
| $v_2$ | F | $\infty$ | $0$ |
| $v_3$ | F | $\infty$ | $0$ |
| $v_4$ | F | $\infty$ | $0$ |
| $v_5$ | F | $\infty$ | $0$ |
| $v_6$ | F | $\infty$ | $0$ |
| $v_7$ | F | $\infty$ | $0$ |


</div>
</div>

---
layout: prism
heading: "Dijkstra's Algorithm: Stages 1-3"
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 1px 12px; line-height: 1.12; }
.slidev-layout table { font-size: 0.9em; }
</style>

<div class="grid grid-cols-3 gap-3" style="margin-top: 1rem;">
<div>

After $v_1$ is *known*:

| $v$ | *k* | $d_v$ | $p_v$ |
|:---:|:---:|:---:|:---:|
| $v_1$ | T | $0$ | $0$ |
| $v_2$ | F | $2$ | $v_1$ |
| $v_3$ | F | $\infty$ | $0$ |
| $v_4$ | F | $1$ | $v_1$ |
| $v_5$ | F | $\infty$ | $0$ |
| $v_6$ | F | $\infty$ | $0$ |
| $v_7$ | F | $\infty$ | $0$ |

</div>
<div>

After $v_4$ is *known*:

| $v$ | *k* | $d_v$ | $p_v$ |
|:---:|:---:|:---:|:---:|
| $v_1$ | T | $0$ | $0$ |
| $v_2$ | F | $2$ | $v_1$ |
| $v_3$ | F | $3$ | $v_4$ |
| $v_4$ | T | $1$ | $v_1$ |
| $v_5$ | F | $3$ | $v_4$ |
| $v_6$ | F | $9$ | $v_4$ |
| $v_7$ | F | $5$ | $v_4$ |

</div>
<div>

After $v_2$ is *known*:

| $v$ | *k* | $d_v$ | $p_v$ |
|:---:|:---:|:---:|:---:|
| $v_1$ | T | $0$ | $0$ |
| $v_2$ | T | $2$ | $v_1$ |
| $v_3$ | F | $3$ | $v_4$ |
| $v_4$ | T | $1$ | $v_1$ |
| $v_5$ | F | $3$ | $v_4$ |
| $v_6$ | F | $9$ | $v_4$ |
| $v_7$ | F | $5$ | $v_4$ |

</div>
</div>

---
layout: prism
heading: "Dijkstra's Algorithm: Stages 4-6"
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 1px 12px; line-height: 1.12; }
.slidev-layout table { font-size: 0.9em; }
</style>

<div class="grid grid-cols-3 gap-3" style="margin-top: 0.6rem;">
<div>

After $v_5$ then $v_3$:

| $v$ | *k* | $d_v$ | $p_v$ |
|:---:|:---:|:---:|:---:|
| $v_1$ | T | $0$ | $0$ |
| $v_2$ | T | $2$ | $v_1$ |
| $v_3$ | T | $3$ | $v_4$ |
| $v_4$ | T | $1$ | $v_1$ |
| $v_5$ | T | $3$ | $v_4$ |
| $v_6$ | F | $8$ | $v_3$ |
| $v_7$ | F | $5$ | $v_4$ |

</div>
<div>

After $v_7$ is *known*:

| $v$ | *k* | $d_v$ | $p_v$ |
|:---:|:---:|:---:|:---:|
| $v_1$ | T | $0$ | $0$ |
| $v_2$ | T | $2$ | $v_1$ |
| $v_3$ | T | $3$ | $v_4$ |
| $v_4$ | T | $1$ | $v_1$ |
| $v_5$ | T | $3$ | $v_4$ |
| $v_6$ | F | $6$ | $v_7$ |
| $v_7$ | T | $5$ | $v_4$ |

</div>
<div>

After $v_6$ (terminates):

| $v$ | *k* | $d_v$ | $p_v$ |
|:---:|:---:|:---:|:---:|
| $v_1$ | T | $0$ | $0$ |
| $v_2$ | T | $2$ | $v_1$ |
| $v_3$ | T | $3$ | $v_4$ |
| $v_4$ | T | $1$ | $v_1$ |
| $v_5$ | T | $3$ | $v_4$ |
| $v_6$ | T | $6$ | $v_7$ |
| $v_7$ | T | $5$ | $v_4$ |

</div>
</div>

<div style="margin-top: 1rem;"></div>

- Each phase takes $\mathcal{O}(|V|)$ time to find the minimum, so $\mathcal{O}(|V|^2)$ time is spent finding minima over the whole algorithm.

---
layout: prism
heading: "DIY: Dijkstra's Shortest Paths"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int main() {
    const int N = 7;                       // vertices v1..v7
    vector<vector<pair<int,int>>> adj(N + 1);   // (neighbor, cost)
    auto add = [&](int u, int v, int c){ adj[u].push_back({v, c}); };
    add(1,2,2); add(1,4,1); add(2,4,3); add(2,5,10);
    add(3,1,4); add(3,6,5); add(4,3,2); add(4,5,2);
    add(4,6,8); add(4,7,4); add(5,7,6); add(7,6,1);

    int s = 1;                             // start vertex v1
    vector<int> dist(N + 1, INT_MAX);
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    dist[s] = 0; pq.push({0, s});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, c] : adj[u])
            if (dist[u] + c < dist[v]) { dist[v] = dist[u] + c; pq.push({dist[v], v}); }
    }

    for (int v = 1; v <= N; v++)
        cout << "dist(v" << s << " -> v" << v << ") = " << dist[v] << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Graphs with Negative Edge Costs
---

<style>
.slidev-layout ul > li {
  margin-top: 2.6em;
}
</style>

- If the graph has [negative edge costs]{.hl}, then Dijkstra's algorithm does not work.

- The problem is that once a vertex $u$ is declared *known*, some other *unknown* vertex $v$ might still offer a path back to $u$ that is very negative.

- A tempting solution is to add a constant $\Delta$ to each edge cost — removing negative edges — compute a shortest path on the new graph, and apply the result to the original. *This does not work either*, since it penalizes paths with more edges.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Graphs</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Shortest-Path Algorithms</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Minimum Spanning Tree</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Minimum Spanning Tree</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Prim's Algorithm</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Kruskal's Algorithm</span></p>
  </div>

</div>

---
layout: prism
heading: Minimum Spanning Tree
---

- The next problem is finding a [minimum spanning tree]{.hl} in an undirected graph.
  - The problem makes sense for directed graphs but appears to be more difficult.

- Informally, a minimum spanning tree of an undirected graph $G$ is a tree formed from graph edges that connects all the vertices of $G$ at lowest total cost.
  - A minimum spanning tree exists *if and only if* $G$ is connected.
  - It is a *tree* because it is acyclic, *spanning* because it covers every vertex, and *minimum* for the obvious reason.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-08.svg" class="tikz-fig" style="width: 65%; margin: 0 auto;" />

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-09.svg" class="tikz-fig" style="width: 65%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "Prim's Algorithm: Idea"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- One way to compute a minimum spanning tree is to grow the tree in successive stages.
  - In each stage, one node is picked as the root, and we add an edge — and an associated vertex — to the tree.

- At any point, we have a set of vertices already included in the tree; the rest have not been.

- The algorithm finds, at each stage, a new vertex to add by choosing the edge $(u, v)$ of smallest cost among all edges where $u$ is in the tree and $v$ is not.

- [Prim's algorithm]{.hl} is essentially identical to Dijkstra's algorithm.
  - For each vertex we keep $d_v$, $p_v$, and whether it is *known*.
  - $d_v$ is the weight of the shortest edge connecting $v$ to a *known* vertex; $p_v$ is the last vertex to change $d_v$.
  - After a vertex $v$ is selected, for each *unknown* $w$ adjacent to $v$: $d_w = \min(d_w, c_{w,v})$.

---
layout: prism
heading: "Prim's Algorithm: Growing the Tree"
---

- Starting from $v_1$, Prim's algorithm adds one vertex per stage until the tree spans all vertices:

<div class="grid grid-cols-3 gap-2" style="margin-top: 1rem;">
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-10.svg" class="tikz-fig" style="width: 70%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-11.svg" class="tikz-fig" style="width: 70%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-12.svg" class="tikz-fig" style="width: 70%;" />
</div>
</div>

<div class="grid grid-cols-3 gap-2" style="margin-top: 0.6rem;">
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-13.svg" class="tikz-fig" style="width: 70%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-14.svg" class="tikz-fig" style="width: 70%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-15.svg" class="tikz-fig" style="width: 70%;" />
</div>
</div>

---
layout: prism
heading: "Kruskal's Algorithm: Idea"
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 1px 12px; line-height: 1.12; }
.slidev-layout table { font-size: 0.9em; }
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem; grid-template-columns: 1.5fr 1fr;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A second greedy strategy is to continually select the edges in order of smallest weight and accept an edge if it does not cause a cycle.
  - This is [Kruskal's algorithm]{.hl}.

- Formally, Kruskal's algorithm maintains a [forest]{.hl} — a collection of trees.
  - When it terminates, there is only one tree: the minimum spanning tree.

- The worst-case running time is $\mathcal{O}(|E| \log |E|)$.

</div>
<div>

<div style="height: 1rem;"></div>

| Edge | Weight | Action |
|:---:|:---:|:---:|
| $(v_1, v_4)$ | $1$ | Accepted |
| $(v_6, v_7)$ | $1$ | Accepted |
| $(v_1, v_2)$ | $2$ | Accepted |
| $(v_3, v_4)$ | $2$ | Accepted |
| $(v_2, v_4)$ | $3$ | Rejected |
| $(v_1, v_3)$ | $4$ | Rejected |
| $(v_4, v_7)$ | $4$ | Accepted |
| $(v_3, v_6)$ | $5$ | Rejected |
| $(v_5, v_7)$ | $6$ | Accepted |

</div>
</div>

---
layout: prism
heading: "Kruskal's Algorithm: Building the Forest"
---

- Edges are added in order of weight, skipping any that would create a cycle, until a single spanning tree remains:

<div class="grid grid-cols-3 gap-2" style="margin-top: 1rem;">
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-16.svg" class="tikz-fig" style="width: 100%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-17.svg" class="tikz-fig" style="width: 100%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-18.svg" class="tikz-fig" style="width: 100%;" />
</div>
</div>

<div class="grid grid-cols-3 gap-2" style="margin-top: 0.6rem;">
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-19.svg" class="tikz-fig" style="width: 100%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-20.svg" class="tikz-fig" style="width: 100%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-21.svg" class="tikz-fig" style="width: 100%;" />
</div>
</div>

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
