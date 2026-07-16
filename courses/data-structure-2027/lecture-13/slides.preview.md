---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 13
download: true
info: |
  ## Data Structure Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-13-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 13: Algorithm Design Techniques</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">Sets and Maps</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Hash Tables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span class="text-gray-900 dark:text-gray-100">Algorithm Design Techniques</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: "Recap: Separate Chaining"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- When an element is inserted and it hashes to the same value as an already-inserted element, we have a [collision]{.hl} and need to resolve it.

- The first strategy, commonly known as [separate chaining]{.hl}, is to keep a list of all elements that hash to the same value.

- Assuming the hashing function $hash(x) = x \bmod 10$, each bucket holds the linked list of keys that map to it:

<div class="sub-item">

$0 \to 0, 90 \quad\bullet\quad 1 \to 81 \quad\bullet\quad 2 \to 64 \quad\bullet\quad 4 \to 4, 54 \quad\bullet\quad 6 \to 36 \quad\bullet\quad 9 \to 49$

</div>

---
layout: prism
heading: "Recap: Linear Probing"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- In [linear probing]{.hl}, $f$ is a linear function of $i$, typically $f(i) = i$.
  - This amounts to trying cells sequentially in search of an empty cell.

- The table shows the result of inserting keys $\{89, 18, 49, 58, 69\}$.

- Even if the table is relatively empty, blocks of occupied cells start forming.
  - This effect, known as [primary clustering]{.hl}, means any key hashing into the cluster needs several attempts and then adds to it.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w13-01.svg" class="tikz-fig" style="width: 65%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "Recap: Quadratic Probing"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [Quadratic probing]{.hl} is a collision resolution method that eliminates the primary clustering problem of linear probing.

- Here the collision function is quadratic; the popular choice is $f(i) = i^2$.

- Although quadratic probing eliminates primary clustering, elements that hash to the same position probe the same alternative cells.
  - This is known as [secondary clustering]{.hl}.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w13-02.svg" class="tikz-fig" style="width: 65%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "Recap: Double Hashing"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- The last collision resolution method we examine is [double hashing]{.hl}.

- For double hashing, one popular choice is $f(i) = i \cdot hash_2(x)$.

- The table exploits the double hashing strategy with $hash_2(x) = x \bmod 9$.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w13-03.svg" class="tikz-fig" style="width: 65%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: Algorithm Design Techniques
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- So far we have been concerned with the efficient *implementation* of data structures.
  - When an algorithm is given, the actual data structures need not be specified.
  - It is up to the programmer to choose the appropriate data structure to make the running time as small as possible.

- We now switch our attention from the implementation of data structures to the [design of algorithms]{.hl}.
  - We focus on five common types of algorithms used to solve problems.
  - For many problems, it is quite likely that at least one of these methods will work.

- For each type of algorithm, we will see the general approach, look at several examples, and discuss the time and space complexity where appropriate.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Greedy Algorithm</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Greedy Algorithm</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">A Scheduling Problem</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Huffman Codes</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Divide and Conquer</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Dynamic Programming</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Randomized Algorithms</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Backtracking Algorithms</span></p>
  </div>

</div>

---
layout: prism
heading: Greedy Algorithm
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The first type of algorithm we examine is the [greedy algorithm]{.hl}.
  - Dijkstra's, Prim's, and Kruskal's algorithms are greedy: in each phase, a decision is made that appears good, without regard for future consequences.
  - This means that some *local optimum* could be chosen.

- When the algorithm terminates, we hope that the local optimum equals the [global optimum]{.hl}.
  - If so, the algorithm is correct; otherwise it produces a *suboptimal* solution.
  - When the absolute best answer is not required, simple greedy algorithms are sometimes used to generate approximate answers.

- The most obvious real-life example is the [coin-changing problem]{.hl}.
  - To give 17,610 KRW in change: a 10,000 bill, a 5,000 bill, two 1,000 bills, a 500 coin, a 100 coin, and a 10 coin — guaranteed to minimize the number of bills and coins.

---
layout: prism
heading: "DIY: Greedy Coin Change"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> denom = {10000, 5000, 1000, 500, 100, 50, 10}; // KRW
    int amount = 17610, pieces = 0;

    cout << "Change for " << amount << " KRW:\n";
    for (int d : denom) {
        int cnt = amount / d;   // greedy: take as many of the largest as possible
        if (cnt > 0) {
            cout << "  " << cnt << " x " << d << "\n";
            pieces += cnt;
            amount -= cnt * d;   // reduce the remaining amount
        }
    }
    cout << "Total pieces = " << pieces << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "A Scheduling Problem"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- We are given jobs $j_1, j_2, \ldots, j_N$ with known running times $t_1, t_2, \ldots, t_N$.

- With a single processor and *nonpreemptive* scheduling (a started job runs to completion), what schedule minimizes the average completion time?

- A simple first-come first-serve solution gives an average completion time of $25$.

</div>
<div>

<div style="height: 1.5rem;"></div>

| Job   | Time |
|:-----:|:----:|
| $j_1$ | $15$ |
| $j_2$ | $8$  |
| $j_3$ | $3$  |
| $j_4$ | $10$ |

<div class="sub-item" style="margin-top: 1rem;">

FCFS $j_1 j_2 j_3 j_4$: completions $15, 23, 26, 36$; mean $= 100/4 = 25$.

</div>

</div>
</div>

---
layout: prism
heading: "A Scheduling Problem — Shortest Job First"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Scheduling by [shortest job first]{.hl} — order $j_3, j_2, j_4, j_1$ — yields a mean completion time of $17.75$.
  - Completions $3, 11, 21, 36$; mean $= 71/4 = 17.75$.

- Let the schedule be $j_{i_1}, j_{i_2}, \ldots, j_{i_N}$. The first job finishes at $t_{i_1}$, the second at $t_{i_1}+t_{i_2}$, the third at $t_{i_1}+t_{i_2}+t_{i_3}$, and so on.

- The total cost $C$ is:

$$
C = \sum_{k=1}^{N}(N-k+1)\,t_{i_k} = (N+1)\sum_{k=1}^{N} t_{i_k} - \sum_{k=1}^{N} k\cdot t_{i_k}.
$$

<div class="sub-item">

Only the second sum affects the total cost, so we minimize $C$ by scheduling shorter jobs first.

</div>

---
layout: prism
heading: "A Scheduling Problem — Multiple Processors"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- We can extend this problem to the case of [several processors]{.hl}.

- With nine jobs $j_1, \ldots, j_9$ (times $3, 5, 6, 10, 11, 14, 15, 18, 20$) and three processors, the optimal solution again schedules shortest jobs first, distributing them round-robin across processors.
  - Processor 1: $j_1, j_4, j_7 \;\to\; 3, 13, 28$
  - Processor 2: $j_2, j_5, j_8 \;\to\; 5, 16, 34$
  - Processor 3: $j_3, j_6, j_9 \;\to\; 6, 20, 40$

- This minimizes the *mean* completion time across all processors.

---
layout: prism
heading: "A Scheduling Problem — Final Completion"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- Suppose instead we are only concerned with [when the last job finishes]{.hl}.

- A different arrangement of the same nine jobs achieves a minimum final completion time of $34$.
  - Although this schedule does not have minimum *mean* completion time, its merit is that the whole sequence completes earlier.

- Although *minimum mean completion time* and *minimum final completion time* look very similar, this new problem turns out to be [much harder]{.hl} than the first.

---
layout: prism
heading: "Huffman Codes"
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 1px 12px; line-height: 1.12; }
.slidev-layout table { font-size: 0.9em; }
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A second application of greedy algorithms is [file compression]{.hl}.

- Suppose a file contains only the characters `a`, `e`, `i`, `s`, `t`, blanks (`sp`), and newlines (`nl`).

- With a fixed 3-bit code, the file needs $174$ bits: $58$ characters $\times\ 3$ bits each.

</div>
<div>

| Char | Code | Freq | Bits |
|:----:|:----:|:----:|:----:|
| `a`  | 000  | 10   | 30   |
| `e`  | 001  | 15   | 45   |
| `i`  | 010  | 12   | 36   |
| `s`  | 011  | 3    | 9    |
| `t`  | 100  | 4    | 12   |
| `sp` | 101  | 13   | 39   |
| `nl` | 110  | 1    | 3    |
| **Total** | | | **174** |

</div>
</div>

---
layout: prism
heading: "Huffman Codes — Variable-Length Codes"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- The general strategy is to let the code length [vary from character to character]{.hl}, ensuring that frequently occurring characters have short codes.
  - If all characters occur with the same frequency, there are unlikely to be any savings.

- We represent codes with a [trie]{.hl} in which characters sit at the leaves; the path from the root (left $= 0$, right $= 1$) spells out each code.

- The original fixed-length strategy corresponds to a *full, balanced* trie of depth $3$ — every character at the same depth, giving no savings.

---
layout: prism
heading: "Huffman Codes — Prefix Codes"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- If characters are placed [only at the leaves]{.hl}, any sequence of bits can always be decoded unambiguously.
  - Such an encoding is known as a [prefix code]{.hl}: no code is a prefix of another.

- By rebalancing the trie so that rarer characters sit deeper, we can obtain a code of cost $173$ bits.
  - This is slightly better than the fixed-length $174$, but still far from optimal.

- The problem is thus to find the *full binary trie of minimum total cost*, where all characters are at the leaves.

---
layout: prism
heading: "Huffman Codes — The Optimal Code"
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 1px 12px; line-height: 1.12; }
.slidev-layout table { font-size: 0.9em; }
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The code on the right requires only $146$ bits.
  - This coding system is commonly referred to as a [Huffman code]{.hl}.

- Frequent characters (`e`, `i`, `sp`) get short 2-bit codes; rare ones (`s`, `nl`) get long 5-bit codes.

</div>
<div>

| Char | Code | Freq | Bits |
|:----:|:----:|:----:|:----:|
| `a`  | 001   | 10   | 30   |
| `e`  | 01    | 15   | 30   |
| `i`  | 10    | 12   | 24   |
| `s`  | 00000 | 3    | 15   |
| `t`  | 0001  | 4    | 16   |
| `sp` | 11    | 13   | 26   |
| `nl` | 00001 | 1    | 5    |
| **Total** | | | **146** |

</div>
</div>

---
layout: prism
heading: "Huffman's Algorithm"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Huffman's algorithm builds the optimal trie greedily by repeatedly merging the two lightest trees:

<div class="sub-item-enum">

1. Maintain a *forest* of trees — initially $C$ trees, where $C$ is the number of characters.
2. The [weight]{.hl} of a tree is the sum of the frequencies of its leaves.
3. $C-1$ times, select the two trees $T_1$ and $T_2$ of smallest weight (breaking ties arbitrarily) and form a new tree with subtrees $T_1$ and $T_2$.

</div>

- Using a priority queue keyed on weight, each merge costs $\mathcal{O}(\log C)$, giving an $\mathcal{O}(C \log C)$ algorithm overall.

---
layout: prism
heading: "DIY: Huffman Code Lengths"
---

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

struct Node { int weight; int leaf; int l, r; };

int main() {
    vector<string> name = {"a","e","i","s","t","sp","nl"};
    vector<int> freq     = { 10, 15, 12,  3,  4, 13,   1 };
    vector<Node> t;
    // min-heap of (weight, index) over the current forest
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    for (int k = 0; k < (int)freq.size(); k++) {
        t.push_back({freq[k], k, -1, -1});
        pq.push({freq[k], k});
    }
    while (pq.size() > 1) {                 // C-1 merges
        auto [w1, a] = pq.top(); pq.pop();
        auto [w2, b] = pq.top(); pq.pop();
        int id = t.size();
        t.push_back({w1 + w2, -1, a, b});   // new internal node
        pq.push({w1 + w2, id});
    }
    // walk the tree to get each leaf's depth (code length)
    vector<int> depth(t.size(), 0);
    int total = 0, root = t.size() - 1;
    vector<int> stk = {root};
    while (!stk.empty()) {
        int u = stk.back(); stk.pop_back();
        if (t[u].leaf >= 0) { total += depth[u] * t[u].weight; continue; }
        depth[t[u].l] = depth[t[u].r] = depth[u] + 1;
        stk.push_back(t[u].l); stk.push_back(t[u].r);
    }
    cout << "Fixed-length code : 174 bits\n";
    cout << "Huffman code      : " << total << " bits" << endl;
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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Greedy Algorithm</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Divide and Conquer</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Divide and Conquer</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Running Time of Divide and Conquer Algorithms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Closest-Points Problem</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Dynamic Programming</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Randomized Algorithms</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Backtracking Algorithms</span></p>
  </div>

</div>

---
layout: prism
heading: Divide and Conquer
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Another common technique for designing algorithms is [divide and conquer]{.hl}.

- Divide and conquer algorithms consist of two parts:

<div class="sub-item-enum">

1. *Divide.* Smaller problems are solved recursively (except, of course, base cases).
2. *Conquer.* The solution to the original problem is formed from the solutions to the subproblems.

</div>

- We have already seen several divide and conquer algorithms — the maximum subsequence sum problem and the tree traversal strategies.
  - Sorting algorithms such as [mergesort]{.hl} and [quicksort]{.hl} are also divide and conquer algorithms.

- Next we see another example of the paradigm: a problem in computational geometry.

---
layout: prism
heading: Running Time of Divide and Conquer Algorithms
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Assume a divide and conquer algorithm operates on two problems, each half the size of the original, plus $\mathcal{O}(N)$ additional work. This yields the recurrence:

$$
T(N) = 2\,T(N/2) + \mathcal{O}(N).
$$

<div class="theorem-box">
<div class="theorem-box-title">Theorem. Running time of divide and conquer algorithms (Master Theorem)</div>
<div class="theorem-box-body">

$$
T(N) = a\,T(N/b) + \Theta(N^k) =
\begin{cases}
\mathcal{O}(N^{\log_b a}) & \text{if } a > b^k,\\[0.2em]
\mathcal{O}(N^k \log N)   & \text{if } a = b^k,\\[0.2em]
\mathcal{O}(N^k)          & \text{if } a < b^k.
\end{cases}
$$

</div>
</div>

- For $T(N) = 2T(N/2) + \mathcal{O}(N)$ we have $a = b = 2$, $k = 1$, so $a = b^k$ and $T(N) = \mathcal{O}(N \log N)$.

---
layout: prism
heading: "Closest-Points Problem"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The input to the [closest-points problem]{.hl} is a list $P$ of points in a plane.

- If $p_1 = (x_1, y_1)$ and $p_2 = (x_2, y_2)$, the Euclidean distance between them is $\big[(x_1 - x_2)^2 + (y_1 - y_2)^2\big]^{1/2}$.

- We are required to find the [closest pair of points]{.hl}.
  - If two points share a position, that pair is the closest, with distance zero.

- With $N$ points there are $N(N-1)/2$ pairs of distances.
  - We can check all of them with a very short program, but at the expense of an $\mathcal{O}(N^2)$ algorithm.
  - Since this is just an exhaustive search, we should expect to do better.

---
layout: prism
heading: "Closest-Points — Divide Step"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Assume the points have been sorted by $x$ coordinate.
  - This adds $\mathcal{O}(N \log N)$ to the final time bound.

- Draw an imaginary vertical line that partitions the point set into two halves, $P_L$ and $P_R$.
  - Since the points are sorted by $x$, this is certainly simple to do.

- Either the closest points are both in $P_L$, both in $P_R$, or one is in each half.
  - Let us call these distances $d_L$, $d_R$, and $d_C$.

- We can compute $d_L$ and $d_R$ [recursively]{.hl}, then combine.

---
layout: prism
heading: "Closest-Points — The Strip"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- The problem, then, is to compute $d_C$. Let $\delta = \min(d_L, d_R)$.
  - If $d_C$ improves on $\delta$, the two points defining $d_C$ must be within $\delta$ of the dividing line — we call this area the [strip]{.hl}.

- Suppose the points in the strip are sorted by their $y$ coordinates.
  - If $p_i$ and $p_j$'s $y$ coordinates differ by more than $\delta$, we can proceed to $p_{i+1}$.

- Only points whose $y$ coordinates are within $\delta$ of $p_i$ can possibly beat $\delta$, dramatically limiting the comparisons.

---
layout: prism
heading: "Closest-Points — Running Time"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- In the worst case, for any point $p_i$, at most [seven]{.hl} points $p_j$ need to be considered.
  - These points must lie in the $\delta$-by-$\delta$ square in the left half of the strip or the one in the right half.
  - All points in each $\delta$-by-$\delta$ square are separated by at least $\delta$.

- Because at most seven points are considered per $p_i$, computing a $d_C$ better than $\delta$ takes $\mathcal{O}(N)$.

- Thus, we appear to have an $\mathcal{O}(N \log N)$ solution — two half-sized recursive calls plus linear combining work.
  - We do not *quite* have it yet, but it can be achieved with a simple modification (avoiding an $\mathcal{O}(N \log N)$ sort at every level).

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Greedy Algorithm</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Divide and Conquer</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Dynamic Programming</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Dynamic Programming</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Using a Table Instead of Recursion</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Randomized Algorithms</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Backtracking Algorithms</span></p>
  </div>

</div>

---
layout: prism
heading: Dynamic Programming
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- Any recursive mathematical formula can be translated directly into a recursive algorithm — but often the compiler does not do justice to it, and an *inefficient* program results.

- When we suspect this is the case, we help the compiler by rewriting the recursive algorithm as a [nonrecursive]{.hl} one that systematically records answers to subproblems in a [table]{.hl}.

- One technique that makes use of this approach is known as [dynamic programming]{.hl}.

---
layout: prism
heading: Using a Table Instead of Recursion
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The natural recursive program to compute the [Fibonacci numbers]{.hl} is very inefficient.
  - It requires [exponential]{.hl} running time, because it recomputes the same values over and over.

- To compute the $N$-th Fibonacci number we only need the two most recently computed values ($F_{N-1}$ and $F_{N-2}$).
  - Recording these in a table yields an $\mathcal{O}(N)$ algorithm.

</div>
<div>

```cpp
// naive: exponential time
int fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}

// dynamic programming: O(N)
int fibDP(int n) {
    if (n <= 1) return n;
    int prev = 0, cur = 1;
    for (int i = 2; i <= n; i++) {
        int next = prev + cur;
        prev = cur;
        cur  = next;
    }
    return cur;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: Dynamic Programming — Fibonacci"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

long long calls = 0;                 // count recursive calls
long long fib(int n) {               // naive, exponential
    calls++;
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

long long fibDP(int n) {             // table-based, O(N)
    if (n <= 1) return n;
    long long prev = 0, cur = 1;
    for (int i = 2; i <= n; i++) {
        long long next = prev + cur; // record only the last two
        prev = cur; cur = next;
    }
    return cur;
}

int main() {
    int n = 30;
    cout << "fibDP(" << n << ")  = " << fibDP(n) << "\n";
    cout << "fib(" << n << ")    = " << fib(n) << "\n";
    cout << "naive calls  = " << calls << "  (exponential!)" << endl;
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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Greedy Algorithm</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Divide and Conquer</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Dynamic Programming</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Randomized Algorithms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Randomized Algorithms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Random-Number Generators</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Backtracking Algorithms</span></p>
  </div>

</div>

---
layout: prism
heading: Randomized Algorithms
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- In [randomized algorithms]{.hl}, at least once during the algorithm a random number is used to make a decision.
  - The running time depends not only on the particular input, but also on the random numbers that occur.

- The worst-case running time of a randomized algorithm is often the same as that of the nonrandomized algorithm.
  - The important difference is that a good randomized algorithm has *no bad inputs*, only bad random numbers (relative to the input).

- By using a randomized algorithm, the particular input is no longer important.
  - The random numbers matter, and we obtain an [expected running time]{.hl}, averaged over all possible random numbers instead of over all possible inputs.

---
layout: prism
heading: "Random-Number Generators"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Since these algorithms require random numbers, we need a method to generate them.
  - True randomness is virtually impossible on a computer, since generated numbers depend on the algorithm and thus cannot be truly random.

- Generally it suffices to produce [pseudorandom]{.hl} numbers, which merely appear random.
  - Random numbers have many known statistical properties; pseudorandom numbers satisfy most of them.

- To generate a $0$ or $1$ randomly, one crude way is to examine the system clock.
  - Obviously, this strategy has many weaknesses.

- The simplest practical method is the [linear congruential generator]{.hl}, first described by Lehmer in 1951.

---
layout: prism
heading: "Random-Number Generators — Linear Congruential"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Numbers $x_1, x_2, \ldots$ are generated satisfying $x_{i+1} = A\,x_i \bmod M$.

- Some value of $x_0$, the [seed]{.hl}, must be given.
  - If $x_0 = 0$ the sequence is far from random; if $A$ and $M$ are chosen well, any $1 \le x_0 < M$ is equally valid.
  - If $M$ is prime, $x_i$ is never $0$.

- With $M = 11$, $A = 7$, $x_0 = 1$: $7, 5, 2, 3, 10, 4, 6, 9, 8, 1, \ldots$ — the sequence repeats after $M-1 = 10$ numbers.

</div>
<div>

<div style="height: 2rem;"></div>

```cpp
// linear congruential generator
long long M = 11, A = 7;
long long x = 1;          // seed x0

for (int i = 0; i < 10; i++) {
    x = (A * x) % M;      // x_{i+1}
    cout << x << " ";
}
// 7 5 2 3 10 4 6 9 8 1
```

<div class="sub-item" style="margin-top: 1rem;">

A poor choice such as $A = 5$ gives a short period of $5$: $5, 3, 4, 9, 1, \ldots$

</div>

</div>
</div>

---
layout: prism
heading: "Random-Number Generators — Practical Choices"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- Lehmer suggested the 31-bit prime $M = 2^{31} - 1 = 2147483647$ and $A = 48271$ for a [full-period]{.hl} generator.

- This seems simple to implement.
  - We can generate a random real number in $[0, 1)$ by dividing $x_i$ by $M$.

- Recently, many libraries use generators based on

$$
x_{i+1} = (A\,x_i + c) \bmod 2^B,
$$

where $B$ matches the number of bits in the machine's integer, and $A$ and $c$ are odd.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Greedy Algorithm</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Divide and Conquer</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Dynamic Programming</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Randomized Algorithms</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Backtracking Algorithms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Backtracking Algorithms</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Turnpike Reconstruction Problem</span></p>
  </div>

</div>

---
layout: prism
heading: Backtracking Algorithms
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The last algorithm design technique we examine is [backtracking]{.hl}.

- In many cases, a backtracking algorithm amounts to a clever implementation of exhaustive search, with generally unfavorable performance.
  - This is not always the case, however, and even so, the savings over a brute-force search can be significant.

- A practical example is the problem of *arranging furniture* in a new house.
  - There are many possibilities to try, but typically only a few are actually considered.
  - Many bad arrangements are discarded early, because an undesirable subset of the arrangement is detected.
  - Eliminating a large group of possibilities in one step is known as [pruning]{.hl}.

---
layout: prism
heading: "The Turnpike Reconstruction Problem"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Suppose we are given $N$ points $p_1, p_2, \ldots, p_N$ located on the $x$-axis.

- Let $x_i$ be the coordinate of $p_i$; these $N$ points determine $N(N-1)/2$ (not necessarily unique) distances of the form $|x_i - x_j|$.

- The [turnpike reconstruction problem]{.hl} is to reconstruct a point set from the distances.
  - This finds applications in physics, molecular biology, and elsewhere.
  - Just as factoring seems harder than multiplication, reconstruction seems harder than construction.

- Nobody has found an algorithm guaranteed to run in polynomial time.
  - The algorithm we present generally runs in $\mathcal{O}(N^2 \log N)$ but can take exponential time in the worst case.

- Let $D = \{1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 10\}$; then we know $N = 6$.

---
layout: prism
heading: "Turnpike — Starting the Search"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- We start by setting $x_1 = 0$; clearly $x_6 = 10$, since $10$ is the largest element of $D$.
  - Remove $10$ from $D$.

- The largest remaining distance is $8$, so either $x_2 = 2$ or $x_5 = 8$.
  - By symmetry, the choice is unimportant, so set $x_5 = 8$.
  - Remove $x_6 - x_5 = 2$ and $x_5 - x_1 = 8$ from $D$.

- Points so far: $\{0, 8, 10\}$, with $D = \{1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7\}$.

---
layout: prism
heading: "Turnpike — Backtracking"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- Now $7$ is the largest value in $D$, so either $x_4 = 7$ or $x_2 = 3$.
  - If $x_4 = 7$, then $x_6 - 7 = 3$ and $x_5 - 7 = 1$ must be present in $D$.
  - If $x_2 = 3$, then $3 - x_1 = 3$ and $x_5 - 3 = 5$ must be present in $D$.
  - We have no guidance, so we try one and see if it leads to a solution.

- Trying the first choice, set $x_4 = 7$. The largest distance is now $6$, so $x_3 = 6$ or $x_2 = 4$.
  - If $x_3 = 6$, then $x_4 - x_3 = 1$, impossible since $1$ is no longer in $D$.
  - If $x_2 = 4$, then $x_2 - x_1 = 4$ and $x_5 - x_2 = 4$, also impossible.

- This line of reasoning leaves no solution, so we [backtrack]{.hl}.

---
layout: prism
heading: "Turnpike — Finding the Solution"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Since $x_4 = 7$ failed, we try $x_2 = 3$.
  - If this also fails, we must give up and report no solution.

- Once again we choose between $x_4 = 6$ and $x_3 = 4$.
  - $x_3 = 4$ is impossible, whereas $x_4 = 6$ is possible.

- The only remaining choice is to assign $x_3 = 5$, so we have a solution: the point set is
$$
\{\,x_1, x_2, x_3, x_4, x_5, x_6\,\} = \{\,0, 3, 5, 6, 8, 10\,\}.
$$

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
