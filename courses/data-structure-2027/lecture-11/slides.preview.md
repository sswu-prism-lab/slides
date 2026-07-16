---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 11
download: true
info: |
  ## Data Structure Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-11-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 11: Sets and Maps</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">Graphs and Weighted Graphs</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span class="text-gray-900 dark:text-gray-100">Sets and Maps</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Hash Tables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Algorithm Design Techniques</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: "Recap: Representation of Graphs (Adjacency Matrix)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- We will consider directed graphs (undirected graphs are similarly represented).

- One simple way is a two-dimensional array — an [adjacency matrix]{.hl} representation.
  - For each edge $(u, v)$ we set $A[u][v]$ to `true`; otherwise the entry is `false`.
  - For a weighted edge, set $A[u][v]$ to the weight, using a very large or very small sentinel for nonexistent edges.

</div>
<div>

<div style="height: 1rem;"></div>

$$
A=\begin{bmatrix}
0 & 1 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 & 1 \\
1 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0
\end{bmatrix}
$$

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-01.svg" class="tikz-fig" style="width: 80%; margin: 0.6rem auto 0;" />

</div>
</div>

---
layout: prism
heading: "Recap: Representation of Graphs (Adjacency List)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The adjacency matrix has extreme simplicity, but its space requirement is $\Theta(|V|^2)$, prohibitive for graphs with few edges.
  - It is appropriate only if the graph is [dense]{.hl}: $|E| = \Theta(|V|^2)$.

- If the graph is [sparse]{.hl}, a better solution is an [adjacency list]{.hl}: for each vertex keep a list of all adjacent vertices.
  - The space requirement is then $\mathcal{O}(|E| + |V|)$, linear in the size of the graph.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-02.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Recap: Shortest-Path Problem"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The shortest weighted path from $v_1$ to $v_6$ has cost $6$: $v_1 \to v_4 \to v_7 \to v_6$.
  - The shortest *unweighted* path between them is $2$.

- For an unweighted graph, we only count the number of edges on the path.
  - This is a special case of the weighted shortest-path problem — assign every edge a weight of $1$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-03.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Recap: Minimum Spanning Tree"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- The next problem is finding a [minimum spanning tree]{.hl} in an undirected graph — a tree of graph edges connecting all vertices of $G$ at lowest total cost.
  - It exists *if and only if* $G$ is connected.
  - It is a *tree* because it is acyclic, *spanning* because it covers every vertex, and *minimum* for the obvious reason.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-04.svg" class="tikz-fig" style="width: 92%; margin: 0 auto;" />

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-05.svg" class="tikz-fig" style="width: 92%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: Sets and Maps
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Data structures such as lists, stacks, queues, priority queues, trees, and graphs each have their own caliber for carrying data.

- They are basic and sufficient for many algorithms, yet some advanced problems cannot be solved easily with them.
  - For instance, how can we detect a [cycle]{.hl} within Kruskal's algorithm? One simple way uses another data structure, the [set]{.hl}.

- We can also handle key–value pairs using the [map]{.hl}.

- In this lecture, we will discuss sets and maps:

<div class="sub-item-enum">

1. Introduce sets and disjoint sets data structures.
2. Show the implementation of disjoint sets.
3. Introduce the map data structure.
4. Show two C++ containers, `set` and `map`.

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Sets and Disjoint Sets</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Sets</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Equivalence Relations</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Dynamic Equivalence Problem</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Disjoint Sets</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Smart Union Algorithms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Path Compression</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>set</code> in the STL</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Maps</span></p>
  </div>

</div>

---
layout: prism
heading: Sets
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [set]{.hl} is an ordered container that does not allow duplicates.

- Many idioms used to access items in arrays and linked lists also work for a set.

- Some operations change under the set's definition:
  - `printSet`, `find`, `remove`, etc. behave the same as in other containers.
  - `insert` may require a `find` first, adding the new element only if there is no *duplicate*.

- We can also consider advanced operations:
  - `union` merges two sets without the duplicated elements — one way is to `find` identical elements, `remove` each, and `merge`.
  - `intersect` simply `find`s the twin elements and returns them.

---
layout: prism
heading: Equivalence Relations
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- A [relation]{.hl} $R$ is defined on a set $S$ if for every pair $(a, b)$, $a, b \in S$, the statement $a\ R\ b$ is either true or false. If true, we say $a$ is related to $b$.

- An [equivalence relation]{.hl} is a relation $R$ satisfying three properties:

<div class="sub-item-enum">

1. *Reflexive.* $a\ R\ a$, $\forall a \in S$.
2. *Symmetric.* $a\ R\ b$ iff $b\ R\ a$.
3. *Transitive.* $a\ R\ b$ and $b\ R\ c$ implies $a\ R\ c$.

</div>

- The $\leq$ relationship is *not* an equivalence relation: it is reflexive ($a \leq a$) and transitive, but not symmetric, since $a \leq b$ does not imply $b \leq a$.

- [Electrical connectivity]{.hl} *is* an equivalence relation — it is reflexive (a component connects to itself), symmetric, and transitive.

---
layout: prism
heading: "The Dynamic Equivalence Problem: Equivalence Classes"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- Given an equivalence relation $\sim$, the natural problem is to decide, for any $a$ and $b$, whether $a \sim b$.

- Stored as a 2-D array of Booleans, this takes constant time — but the relation is usually defined *implicitly*, not explicitly.

- Suppose $\sim$ is defined over $\{a_1, a_2, a_3, a_4, a_5\}$. There are $25$ pairs, each related or not.
  - The information $a_1 \sim a_2,\ a_3 \sim a_4,\ a_5 \sim a_1,\ a_4 \sim a_2$ implies that *all* pairs are related — we would like to infer this quickly.

- The [equivalence class]{.hl} of $a \in S$ is the subset of $S$ containing all elements related to $a$.
  - Every member of $S$ appears in exactly one equivalence class.
  - To decide if $a \sim b$, check only whether $a$ and $b$ are in the same equivalence class.

---
layout: prism
heading: "The Dynamic Equivalence Problem: find and union"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The input is initially a collection of $N$ sets, each with one element — all relations except reflexive ones are false.

- Each set has a different element, so $S_i \cap S_j = \emptyset$; this makes the sets [disjoint]{.hl}.

- There are two permissible operations, [`find`]{.hl} and [`union`]{.hl}:
  - To add the relation $a \sim b$, first `find` $a$ and $b$ and check whether they are in the same equivalence class.
  - If they are not, apply `union`.

- For this reason, the algorithm is frequently known as the disjoint set [union/find algorithm]{.hl}.

---
layout: prism
heading: "The Dynamic Equivalence Problem: Dynamic and Online"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- The union/find algorithm is [dynamic]{.hl} because the sets can change via `union` during the course of the algorithm.

- It must also operate [online]{.hl}: when a `find` is performed, it must give an answer before continuing.
  - An [offline]{.hl} algorithm, by contrast, would be allowed to see the entire sequence of `union`s and `find`s in advance.

- We never compare the relative *values* of elements — we only need knowledge of their location.
  - Hence we assume elements are numbered sequentially from $0$ to $N-1$, the numbering determined easily by some hashing scheme.

- The name of the set returned by `find` is actually fairly arbitrary.

---
layout: prism
heading: "The Dynamic Equivalence Problem: Two Strategies"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- An efficient data structure to solve the equivalence problem is known as [disjoint sets]{.hl}. Two strategies exist:

<div class="sub-item-enum">

1. Ensure `find` runs in constant worst-case time — *linked list* implementation.
2. Ensure `union` runs in constant worst-case time — *tree* implementation.

</div>

- For fast `find`, maintain the name of each element's equivalence class in an array:
  - Then `find` is a simple $\mathcal{O}(1)$ lookup.
  - But `union(a, b)` with `a` in class $i$ and `b` in class $j$ must scan the array, taking $\Theta(N)$.
  - If there are about $N^2$ `find` operations, this performance is fine.

- One idea is to keep all elements of the same equivalence class in a linked list.

---
layout: prism
heading: "Disjoint Sets: Linked List (Merging)"
---

<div style="margin-top: 0.5rem;"></div>

- The linked list implementation saves time when updating, because we need not search the entire array.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-06.svg" class="tikz-fig" style="width: 78%; margin: 1.5rem auto 0; display: block;" />

---
layout: prism
heading: "Disjoint Sets: Linked List (Union-by-Size)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- If we also keep track of the *size* of each equivalence class, and when performing `union`s change the name of the smaller class to that of the larger, then the total time for $N - 1$ merges is $\mathcal{O}(N \log N)$.

<div class="theorem-box">
<div class="theorem-box-title">Why union-by-size helps</div>
<div class="theorem-box-body">

Each time an element's class name is rewritten, its class at least *doubles* in size. An element can therefore be renamed at most $\log N$ times, giving $\mathcal{O}(N \log N)$ total renaming work across all merges.

</div>
</div>

---
layout: prism
heading: "Disjoint Sets: Tree (Parent-Link Forest)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- Recall that `find` need not return any specific name — only that `find`s on two elements return the same answer *iff* they are in the same set.

- One idea is to represent each set by a [tree]{.hl}, since every element in a tree has the same root, which can name the set.
  - A collection of trees is a [forest]{.hl}.

- Initially each set contains one element; the trees are not necessarily binary.
  - The only information we need is a [parent link]{.hl}, so the tree is stored *implicitly* in an array.
  - Each entry `s[i]` is the parent of element $i$; if $i$ is a root, then `s[i] = -1`.

---
layout: prism
heading: "Disjoint Sets: Tree (Initial Forest)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- To `union` two sets, merge the two trees by making one tree's root link to the root of the other — clearly [constant time]{.hl}.

- A `find(x)` returns the root of the tree containing `x`.
  - Its time is proportional to the depth of `x`'s node.
  - A tree of depth $N - 1$ is possible, so the worst-case `find` is $\Theta(N)$.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-08.svg" class="tikz-fig" style="width: 100%;" />

<p style="text-align:center; color:#9aa0a6; font-size:0.85rem; margin-top:0.4rem;">Eight single-element sets: every root stores <code>-1</code>.</p>

</div>
</div>

---
layout: prism
heading: "Disjoint Sets: Tree (Union Example)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Consider `union(4, 5)`, `union(6, 7)`, and then `union(4, 6)`. The array `s[]` records each element's parent, with `-1` marking a root.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-09.svg" class="tikz-fig" style="width: 72%; margin: 1.2rem auto 0; display: block;" />

---
layout: prism
heading: "Smart Union Algorithms: Union-by-Size"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The `union`s so far were performed arbitrarily, making the second tree a subtree of the first.

- A simple improvement always makes the smaller tree a subtree of the larger, breaking ties arbitrarily — [union-by-size]{.hl}.

- If `union`s are done by size, the depth of any node is never more than $\log N$:
  - A node starts at depth $0$.
  - When its depth increases due to a `union`, it lands in a tree at least *twice* as large as before.
  - Thus its depth can increase at most $\log N$ times.

- To implement, keep another array holding the size of each disjoint set; on `union`, the new size is the sum of the old ones.

---
layout: prism
heading: "Smart Union Algorithms: Union-by-Height"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- An alternative that also guarantees depth at most $\mathcal{O}(\log N)$ is [union-by-height]{.hl}: track the *height* rather than the size, and make the shallower tree a subtree of the deeper one.
  - The height increases only when two equally deep trees are joined (then it grows by one) — a trivial modification of union-by-size.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-10.svg" class="tikz-fig" style="width: 100%;" />

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-11.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Path Compression: Motivation"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- The union/find algorithm so far is acceptable for most cases, but the worst case of $\mathcal{O}(M \log N)$ can occur fairly easily and naturally.

- There are probably no more improvements possible for the `union` algorithm, so the only way to speed things up — without reworking the data structure — is to do something clever on `find`.

- This clever operation is [path compression]{.hl}:
  - It is performed *during* a `find` and is independent of the `union` strategy.
  - Its effect: *every* node on the path from `x` to the root has its parent changed to the root.

- When `union`s are arbitrary, path compression is especially good — deep nodes abound and are brought near the root.

---
layout: prism
heading: "Path Compression: Union-by-Rank"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Path compression is perfectly compatible with union-by-size, but *not* entirely with union-by-height, because compression can change tree heights.
  - The stored heights become estimated heights — called [ranks]{.hl} — so the combined strategy is known as [union-by-rank]{.hl}.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-12.svg" class="tikz-fig" style="width: 100%;" />

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-13.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Path Compression: find(14) and Running Time"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Performing `find(14)` reroots every node on the path from `14` to the root directly under the root, flattening the tree for all future `find`s.

- Combining [union-by-rank]{.hl} with [path compression]{.hl} makes any sequence of $M$ operations run in *nearly linear* time:

$$
\Theta\!\left(M\,\alpha(M, N)\right),
$$

<div class="sub-item">

where $\alpha(M, N)$ is the [inverse Ackermann function]{.hl} — it grows so slowly that $\alpha(M, N) \leq 4$ for all practical $M, N$.

</div>

- A simpler analysis gives the bound $\mathcal{O}(M \log^{*} N)$, where $\log^{*} N$ (the *iterated logarithm*) counts how many times $\log$ is applied to reach $1$; even $\log^{*}(2^{65536}) = 5$.

---
layout: prism
heading: "Disjoint Sets: Implementation"
---

```cpp
class DisjSets {
public:
    explicit DisjSets(int numElements) : s(numElements, -1) {}

    int find(int x) const {              // find without compression
        if (s[x] < 0) return x;
        else return find(s[x]);
    }
    int find(int x) {                    // find with path compression
        if (s[x] < 0) return x;
        else return s[x] = find(s[x]);   // reroot x under the root
    }
    void unionSets(int root1, int root2) {   // union-by-size
        if (s[root2] < s[root1]) {           // root2 is larger (more negative)
            s[root2] += s[root1];
            s[root1] = root2;                // make root2 the new root
        } else {
            s[root1] += s[root2];
            s[root2] = root1;                // make root1 the new root
        }
    }
private:
    vector<int> s;   // s[i] = parent of i, or -(size) if i is a root
};
```

---
layout: prism
heading: "DIY: Union-Find Connectivity"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class DisjSets {
public:
    explicit DisjSets(int n) : s(n, -1) {}
    int find(int x) {                        // union-by-size root, or -(size)
        if (s[x] < 0) return x;
        return s[x] = find(s[x]);            // path compression
    }
    void unionSets(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return;
        if (s[rb] < s[ra]) { s[rb] += s[ra]; s[ra] = rb; }
        else               { s[ra] += s[rb]; s[rb] = ra; }
    }
private:
    vector<int> s;
};

int main() {
    DisjSets ds(8);                          // elements 0..7
    ds.unionSets(4, 5);
    ds.unionSets(6, 7);
    ds.unionSets(4, 6);                      // now {4,5,6,7} are one set
    ds.unionSets(0, 1);

    cout << "same(5,7)? " << (ds.find(5) == ds.find(7)) << "\n";
    cout << "same(0,4)? " << (ds.find(0) == ds.find(4)) << "\n";

    int components = 0;
    for (int i = 0; i < 8; i++)
        if (ds.find(i) == i) components++;   // a root marks a component
    cout << "number of components = " << components << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "set in the STL"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- C++ contains a generic [`set`]{.hl} class:
  - `#include <set>`
  - `set<elementType> setName;`

- Inserting a duplicate leaves the size unchanged, and `find` returns `end()` when the element is absent.

</div>
<div>

```cpp
#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> s;
    s.insert(10); s.insert(20);
    cout << s.size() << endl;   // 2
    s.insert(20);               // duplicate
    cout << s.size() << endl;   // 2
    if (s.find(30) != s.end())
        cout << "Exists" << endl;
    else
        cout << "Does Not Exist" << endl;
}
```

</div>
</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Sets and Disjoint Sets</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Maps</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Maps</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>map</code> in the STL</span></p>
  </div>

</div>

---
layout: prism
heading: Maps
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A [map]{.hl} stores a collection of ordered entries consisting of [keys]{.hl} and their [values]{.hl}.

- Keys must be unique, but several keys can map to the same value — so values need not be unique.

- The keys in the map are maintained in logically sorted order.

- A map behaves like a set instantiated with a *pair*, whose comparison function refers only to the key.

- Normally a self-adjusting binary search tree is used to implement maps.
  - In C++, a [red-black tree]{.hl} is used to implement the `map` STL.

---
layout: prism
heading: "map in the STL"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- C++ contains a generic [`map`]{.hl} class:
  - `#include <map>`
  - `map<keyType, valueType> mapName;`

- Each entry is a key–value `pair`; `find` on a key returns `end()` when the key is absent.

</div>
<div>

```cpp
#include <iostream>
#include <map>
using namespace std;

int main() {
    map<string, int> m;
    m.insert({"A+", 60});
    m.insert({"A0", 50});
    m.insert({"B+", 25});

    if (m.find("A+") != m.end())
        cout << "Exists" << endl;
    else
        cout << "Does Not Exist" << endl;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: Word Count with map"
---

<CppRunner>

```cpp
#include <iostream>
#include <map>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string text = "set map set tree map set heap tree map";
    map<string, int> count;             // keys kept in sorted order

    istringstream in(text);
    string word;
    while (in >> word)
        count[word]++;                  // operator[] inserts key if absent

    for (const auto& kv : count)        // iterate keys in sorted order
        cout << kv.first << " : " << kv.second << "\n";

    cout << "distinct words = " << count.size() << endl;
    return 0;
}
```

</CppRunner>

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
