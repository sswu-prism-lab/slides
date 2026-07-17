---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 13
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-13-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 13: Genetic Algorithms and Final Review</p>

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
heading: "DIY_W12: Double Hashing"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- In [open addressing]{.hl} with [double hashing]{.hl}, collisions are resolved using *two* hash functions:

$$
h(x) = x \bmod m
$$

$$
f(x) = 1 + (x \bmod m'),\quad m' \text{ a prime slightly smaller than } m
$$

- **Think about it:** why is combining these two functions effective at spreading out probe sequences?

- **Also think about it:** why must the second value $f(x)$ be handled carefully relative to the table size $m$?

</div>
<div>

<div style="height: 1rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int m = 13, mp = 11;   // m' < m, both prime
    int table[13];
    for (int i = 0; i < m; i++) table[i] = -1;

    auto h = [&](int x){ return x % m; };
    auto f = [&](int x){ return 1 + (x % mp); };

    int keys[] = {18, 41, 22, 44, 59, 32};
    for (int x : keys) {
        int i = h(x), step = f(x), probes = 0;
        while (table[i] != -1) {     // collision -> jump by f(x)
            i = (i + step) % m; probes++;
        }
        table[i] = x;
        cout << "x=" << x << " -> slot " << i
             << " (step " << step << ", " << probes << " probes)\n";
    }
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: Genetic Algorithms (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A [genetic algorithm]{.hl} searches for an optimal solution by *imitating the process of biological evolution*.

- Each candidate solution is encoded as a [gene]{.hl}, and fitter genes are chosen by [natural selection]{.hl} (survival of the fittest).

- Fitter genes are combined through [crossover]{.hl} to produce offspring — though an offspring is not *guaranteed* to be closer to the optimum than its parents.

- With low probability, an offspring undergoes a [mutation]{.hl}; a mutated gene may also move away from the optimum.

- The process is [repeated]{.hl} until an optimal (or good enough) solution is found.

---
layout: prism
heading: Genetic Algorithms (2/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- We evolve a random string toward a fixed [target]{.hl} (here, a short homage to *Sungshin*).

- The building blocks:
  - a [gene pool]{.hl} of allowed characters,
  - a [population]{.hl} of candidate strings,
  - a [fitness]{.hl} function counting matching positions.

- [Selection]{.hl} favors high-fitness genes, [crossover]{.hl} mixes two parents at a pivot, and [mutation]{.hl} randomly replaces characters.

</div>
<div>

<div style="height: 0.5rem;"></div>

```cpp
// fitness: number of positions
// matching the target
int fitness(const string& g) {
    int s = 0;
    for (int i = 0; i < (int)g.size(); i++)
        if (g[i] == TARGET[i]) s++;
    return s;
}

// single-point crossover
string crossover(const string& a,
                 const string& b) {
    int pivot = 1 + rand() % (a.size()-1);
    return a.substr(0, pivot)
         + b.substr(pivot);
}
```

</div>
</div>

---
layout: prism
heading: Genetic Algorithms (3/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The main loop drives the [evolution]{.hl}:
  - evaluate the fitness of every gene,
  - track and print the *fittest* gene so far,
  - stop as soon as the target is reached.

- Otherwise, [select]{.hl} good parents and build the next generation via `mutate(crossover(...))`.

- Each generation tends to raise the best fitness until the target string emerges.

</div>
<div>

<div style="height: 1.5rem;"></div>

```cpp
while (gen < MAX_GEN) {
    // find the fittest of this generation
    int best = 0;
    for (int i = 1; i < POP; i++)
        if (fitness(pop[i]) >
            fitness(pop[best])) best = i;

    if (pop[best] == TARGET) break;

    vector<string> next;      // selection +
    for (int i = 0; i < POP; i++)   // crossover
        next.push_back(mutate(
            crossover(select(pop),
                      select(pop))));
    pop = next; gen++;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: Evolving a Target String"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;

const string TARGET = "SUNGSHIN";
const string GENE   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .";
const int POP = 100, MAX_GEN = 5000;
const double MUT = 0.06;

int fitness(const string& g) {
    int s = 0;
    for (int i = 0; i < (int)g.size(); i++)
        if (g[i] == TARGET[i]) s++;
    return s;
}
char randGene() { return GENE[rand() % GENE.size()]; }
string randInd() {
    string g;
    for (size_t i = 0; i < TARGET.size(); i++) g += randGene();
    return g;
}
// tournament selection: best of 3 random picks
const string& select(const vector<string>& pop) {
    int best = rand() % POP;
    for (int t = 0; t < 2; t++) {
        int c = rand() % POP;
        if (fitness(pop[c]) > fitness(pop[best])) best = c;
    }
    return pop[best];
}
string crossover(const string& a, const string& b) {
    int pivot = 1 + rand() % (TARGET.size() - 1);
    return a.substr(0, pivot) + b.substr(pivot);
}
string mutate(string g) {
    for (auto& c : g)
        if ((double)rand() / RAND_MAX < MUT) c = randGene();
    return g;
}

int main() {
    srand(1);                       // deterministic
    vector<string> pop(POP);
    for (auto& g : pop) g = randInd();

    int bestSoFar = -1;
    for (int gen = 0; gen < MAX_GEN; gen++) {
        int b = 0;
        for (int i = 1; i < POP; i++)
            if (fitness(pop[i]) > fitness(pop[b])) b = i;
        int fb = fitness(pop[b]);
        if (fb > bestSoFar) {       // print only on improvement
            bestSoFar = fb;
            cout << "Gen " << gen << ": " << pop[b]
                 << " (fitness " << fb << ")\n";
        }
        if (pop[b] == TARGET) break;
        vector<string> next;
        for (int i = 0; i < POP; i++)
            next.push_back(mutate(crossover(select(pop), select(pop))));
        pop = next;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Topological Sort (1/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- When several tasks must be done and some tasks must precede others, that ordering has to be respected for the work to complete.

- If an edge $(i, j)$ exists, task $i$ must be performed *before* task $j$.

- An ordering of all vertices of a [directed acyclic graph]{.hl} $G = (V, E)$ satisfying every such constraint is a [topological sort]{.hl}.

- It only exists when the graph has *no cycle* and is *directed*.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">Cooking instant noodles (a DAG)</div>
<div class="theorem-box-body">

Tasks: `pour water`, `open packet`, `ignite stove`, `add noodles`, `add soup`, `add egg`.

Precedences: you must *pour water* and *ignite stove* before *adding noodles*; *open the packet* before *adding noodles*; *add soup* before the final *add egg*, and so on.

Several valid orders exist — any of them completes the dish.

</div>
</div>

</div>
</div>

---
layout: prism
heading: Topological Sort (2/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The intuitive algorithm repeatedly removes a vertex with [no incoming edge]{.hl}:

<div class="sub-item">

```text
topologicalSort(G):
  for i in 1..n:
    pick a vertex u with no in-edge
    A[i] = u
    delete u and its out-edges
  // A[1..n] is a topological order
```

</div>

- Finding a zero-indegree vertex naively costs $O(n)$ each step. Keeping the current in-degree in an array `c[]` and a list `d` of zero-indegree vertices makes each lookup [constant time]{.hl} (Kahn's algorithm).

</div>
<div>

<div style="height: 1rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    // 0 water 1 packet 2 stove 3 noodles 4 soup 5 egg
    const char* name[] = {"water","packet","stove",
                          "noodles","soup","egg"};
    int n = 6;
    vector<vector<int>> adj(n);
    auto edge = [&](int u,int v){ adj[u].push_back(v); };
    edge(0,2); edge(2,3); edge(1,3);
    edge(3,4); edge(4,5); edge(2,5);

    vector<int> indeg(n,0);
    for (int u=0;u<n;u++) for(int v:adj[u]) indeg[v]++;
    queue<int> q;
    for (int u=0;u<n;u++) if(!indeg[u]) q.push(u);

    cout << "Topological order:";
    while (!q.empty()) {
        int u = q.front(); q.pop();
        cout << " " << name[u];
        for (int v: adj[u]) if(--indeg[v]==0) q.push(v);
    }
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: Topological Sort (3/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Besides the intuitive method, a topological sort can be produced with [depth-first search]{.hl}:

<div class="sub-item">

```text
topologicalSort-DFS(G):
  for v in V: visited[v] = false
  for v in V:
    if not visited[v]: DFS-TS(v)

DFS-TS(v):
  visited[v] = true
  for x in adj(v):
    if not visited[x]: DFS-TS(x)
  push v to the front of list R
```

</div>

- Vertices finish in *reverse* topological order, so prepending each finished vertex to `R` yields the sort.

</div>
<div>

<div style="height: 1rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n = 6;
vector<vector<int>> adj(6);
vector<bool> vis(6,false);
vector<int> order;

void dfs(int v){
    vis[v]=true;
    for(int x:adj[v]) if(!vis[x]) dfs(x);
    order.push_back(v);          // finish time
}
int main(){
    const char* name[]={"water","packet","stove",
                        "noodles","soup","egg"};
    adj[0]={2}; adj[2]={3,5}; adj[1]={3};
    adj[3]={4}; adj[4]={5};
    for(int v=0;v<n;v++) if(!vis[v]) dfs(v);
    reverse(order.begin(), order.end());
    cout << "DFS topological order:";
    for(int v:order) cout << " " << name[v];
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: Dynamic Programming (1/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Computing Fibonacci numbers by plain recursion causes [overlapping subproblems]{.hl} — the same call is recomputed *exponentially* often.

- The inefficiency is simply recomputing a value that could have been *stored once* and reused.

- Storing partial results while building the solution is the heart of [dynamic programming]{.hl}.

</div>
<div>

<div style="height: 2rem;"></div>

```text
fib-recursion(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fib-recursion(n-1)
         + fib-recursion(n-2)
```

<div style="margin-top: 1rem;"></div>

The call tree for `fib(7)` repeats `fib(2)` eight times — work explodes as $n$ grows.

</div>
</div>

---
layout: prism
heading: Dynamic Programming (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- DP applies to problems with two properties:

<div class="sub-item-enum">

1. they have [optimal substructure]{.hl}, and
2. a naive recursion suffers severe inefficiency from overlapping calls.

</div>

- [Bottom-up]{.hl}: fill a table with a single loop → [linear]{.hl} time instead of exponential.

- [Top-down (memoization)]{.hl}: keep the recursion but *memo* each computed value in `f[n]` and reuse it on repeated calls.

```text
fib-DP1(n): // bottom-up          fib-DP2(n): // top-down (memoized)
  f[1]=1; f[2]=1;                   if f[n] != 0: return f[n]
  for i in 3..n:                    if n==1 or n==2: f[n]=1
    f[i]=f[i-1]+f[i-2]              else: f[n]=fib-DP2(n-1)+fib-DP2(n-2)
  return f[n]                       return f[n]
```

---
layout: prism
heading: "DIY: Fibonacci — Recursion vs DP"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

long long calls = 0;
long long fibRec(int n){            // naive: exponential calls
    calls++;
    if (n <= 2) return 1;
    return fibRec(n-1) + fibRec(n-2);
}
long long fibBU(int n){            // bottom-up: O(n)
    vector<long long> f(n+1);
    f[1]=f[2]=1;
    for(int i=3;i<=n;i++) f[i]=f[i-1]+f[i-2];
    return f[n];
}
vector<long long> memo(64,0);
long long fibMemo(int n){          // top-down memoized: O(n)
    if (memo[n]) return memo[n];
    if (n<=2) return memo[n]=1;
    return memo[n]=fibMemo(n-1)+fibMemo(n-2);
}
int main(){
    int n = 30;
    cout << "fibRec("<<n<<")  = " << fibRec(n)
         << "  (" << calls << " recursive calls)\n";
    cout << "fibBU("<<n<<")   = " << fibBU(n)   << "  (n steps)\n";
    cout << "fibMemo("<<n<<") = " << fibMemo(n) << "  (n steps)\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Practice: Integer Triangle"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- From the apex to the base, at each step you may move to the adjacent cell *down-left* or *down-right*. Find the path with the [maximum sum]{.hl}.

- Classic bottom-up DP: each cell accumulates the best of its two possible predecessors; the answer is the largest value in the last row.

<div class="tikz-fig" style="font-family: monospace; text-align:center; margin-top: 1rem; font-size: 1.1rem;">

7<br/>
3&nbsp;&nbsp;8<br/>
8&nbsp;&nbsp;1&nbsp;&nbsp;0<br/>
2&nbsp;&nbsp;7&nbsp;&nbsp;4&nbsp;&nbsp;4<br/>
4&nbsp;&nbsp;5&nbsp;&nbsp;2&nbsp;&nbsp;6&nbsp;&nbsp;5<br/>
<span style="color:#5c60a8;">max path sum = 30</span>

</div>

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> t) {
    for (int i = 1; i < (int)t.size(); i++)
        for (int j = 0; j <= i; j++) {
            if (j == 0)
                t[i][j] += t[i-1][j];
            else if (j == i)
                t[i][j] += t[i-1][j-1];
            else
                t[i][j] += max(t[i-1][j-1], t[i-1][j]);
        }
    vector<int>& last = t.back();
    return *max_element(last.begin(), last.end());
}

int main() {
    vector<vector<int>> tri =
        {{7},{3,8},{8,1,0},{2,7,4,4},{4,5,2,6,5}};
    cout << "max path sum = " << solution(tri) << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Practice: Express with N"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Using only the digit `N` and the four arithmetic operators, represent `number`. Return the *minimum* count of `N` used (or `-1` if it exceeds 8).

- E.g. $12 = 5 + 5 + 5/5 + 5/5$ uses five `5`s; the best uses only [four]{.hl}.

- DP over the number of `N`s: `dp[i]` = every value expressible with exactly `i` copies of `N`, built from the *repunit* `N, NN, NNN, …` and by combining smaller `dp[j]` and `dp[i-1-j]`.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <set>
using namespace std;

int solution(int N, int number) {
    set<int> dp[9];
    int num = 0;
    for (int i = 1; i <= 8; i++) {   // N, NN, NNN...
        num = 10*num + N;
        dp[i].insert(num);
    }
    for (int i = 1; i <= 8; i++)
        for (int j = 1; j < i; j++)
            for (int a : dp[j])
                for (int b : dp[i-j]) {
                    dp[i].insert(a+b);
                    dp[i].insert(a-b);
                    dp[i].insert(a*b);
                    if (b) dp[i].insert(a/b);
                }
    for (int i = 1; i <= 8; i++)
        if (dp[i].count(number)) return i;
    return -1;
}
int main() {
    cout << "N=5, 12 -> " << solution(5,12) << "\n";
    cout << "N=2, 11 -> " << solution(2,11) << "\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Sorting Algorithms"
---

<div style="margin-top: 1.5rem; margin-left: 2rem">

- The next slides recap the sorting algorithms covered this semester, each with a runnable C++ demo on the sample array

<div class="tikz-fig" style="font-family: monospace; text-align:center; margin-top: 1.5rem; font-size: 1.2rem; display:inline-block;">
A[] = 8, 31, 48, 15, 3, 11, 20, 29, 65, 73
</div>

- [Comparison sorts]{.hl}: selection, bubble, insertion, merge, quick, heap, shell.

- [Non-comparison sorts]{.hl}: counting, radix, bucket.

</div>

---
layout: prism
heading: "Review: Selection Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Repeatedly select the [maximum]{.hl} among the unsorted prefix and swap it to the *back*.

- After each pass the largest remaining element is placed in its final position.

- Time complexity is $O(n^2)$ regardless of the input; it performs few *swaps*.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> a = {8,31,48,15,3,11,20,29,65,73};
    int n = a.size();
    for (int last = n-1; last > 0; last--) {
        int mx = 0;                 // index of max in a[0..last]
        for (int i = 1; i <= last; i++)
            if (a[i] > a[mx]) mx = i;
        swap(a[mx], a[last]);       // send max to the back
    }
    for (int x : a) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Bubble Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Scan left to right, comparing adjacent elements and [swapping]{.hl} when the left is larger.

- Each pass *bubbles* the largest remaining element to the end; the last element is then excluded.

- Time complexity is $O(n^2)$; an early-exit flag detects an already-sorted array.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> a = {8,31,48,15,3,11,20,29,65,73};
    int n = a.size();
    for (int last = n-1; last > 0; last--) {
        bool swapped = false;
        for (int i = 0; i < last; i++)
            if (a[i] > a[i+1]) {
                swap(a[i], a[i+1]);
                swapped = true;
            }
        if (!swapped) break;        // already sorted
    }
    for (int x : a) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Insertion Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Keep a sorted prefix; take the next element and [insert]{.hl} it into its correct place, shifting larger elements right.

- Very efficient on *nearly sorted* data — close to $O(n)$ in the best case.

- Worst and average case are $O(n^2)$.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> a = {8,31,48,15,3,11,20,29,65,73};
    int n = a.size();
    for (int i = 1; i < n; i++) {
        int key = a[i], j = i - 1;
        while (j >= 0 && a[j] > key) { // shift larger right
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = key;                  // drop key into place
    }
    for (int x : a) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Merge Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [Divide and conquer]{.hl}: split the array in half, sort each half recursively, then [merge]{.hl} the two sorted halves.

- The merge walks both halves with indices `i`, `j` into a temporary buffer `tmp`.

- Guaranteed $O(n \log n)$ time and *stable*, at the cost of $O(n)$ extra space.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void mergeSort(vector<int>& a, int p, int r) {
    if (p >= r) return;
    int q = (p + r) / 2;
    mergeSort(a, p, q);
    mergeSort(a, q+1, r);
    vector<int> tmp;
    int i = p, j = q+1;
    while (i <= q && j <= r)
        tmp.push_back(a[i] <= a[j] ? a[i++] : a[j++]);
    while (i <= q) tmp.push_back(a[i++]);
    while (j <= r) tmp.push_back(a[j++]);
    for (int k = 0; k < (int)tmp.size(); k++) a[p+k] = tmp[k];
}
int main() {
    vector<int> a = {8,31,48,15,3,11,20,29,65,73};
    mergeSort(a, 0, a.size()-1);
    for (int x : a) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Quick Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Choose a [pivot]{.hl}, [partition]{.hl} the array so smaller elements go left and larger go right, then recurse on each side.

- Average time is $O(n \log n)$; a bad pivot gives $O(n^2)$ worst case.

- Sorts *in place* and is usually the fastest comparison sort in practice.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void quickSort(vector<int>& a, int lo, int hi) {
    if (lo >= hi) return;
    int pivot = a[hi], i = lo - 1;    // Lomuto partition
    for (int j = lo; j < hi; j++)
        if (a[j] < pivot) swap(a[++i], a[j]);
    swap(a[i+1], a[hi]);
    int p = i + 1;
    quickSort(a, lo, p-1);
    quickSort(a, p+1, hi);
}
int main() {
    vector<int> a = {8,31,48,15,3,11,20,29,65,73};
    quickSort(a, 0, a.size()-1);
    for (int x : a) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Heap Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Build a [max-heap]{.hl} from the array, then repeatedly swap the root (the max) to the back and *sift down* the reduced heap.

- Guaranteed $O(n \log n)$ time and sorts *in place*.

- Uses the array-as-heap indexing: children of `i` are `2i+1` and `2i+2`.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void siftDown(vector<int>& a, int i, int n) {
    while (true) {
        int l = 2*i+1, r = 2*i+2, big = i;
        if (l < n && a[l] > a[big]) big = l;
        if (r < n && a[r] > a[big]) big = r;
        if (big == i) break;
        swap(a[i], a[big]); i = big;
    }
}
int main() {
    vector<int> a = {8,31,48,15,3,11,20,29,65,73};
    int n = a.size();
    for (int i = n/2 - 1; i >= 0; i--) siftDown(a, i, n);
    for (int last = n-1; last > 0; last--) {
        swap(a[0], a[last]);
        siftDown(a, 0, last);
    }
    for (int x : a) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Shell Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A generalization of insertion sort: sort elements that are a [gap]{.hl} `h` apart, then shrink `h` down to `1`.

- Early large-gap passes move elements long distances, so the final `h = 1` pass has little work left.

- Performance depends on the gap sequence; here we use $h = \ldots, 4, 2, 1$.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> a = {8,31,48,15,3,11,20,29,65,73};
    int n = a.size();
    for (int h = n/2; h > 0; h /= 2)        // shrinking gap
        for (int i = h; i < n; i++) {
            int key = a[i], j = i;
            while (j >= h && a[j-h] > key) { // gapped insertion
                a[j] = a[j-h]; j -= h;
            }
            a[j] = key;
        }
    for (int x : a) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Counting Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Count how many times each value $0..k$ occurs in `C[]`, then turn `C` into a *prefix sum* so `C[i]` holds the number of elements $\le i$.

- Scanning `A` from the back and using `C` places each element directly into its output slot — a [stable]{.hl} sort.

- Runs in $O(n + k)$ time; efficient only when $k$ is not too large.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> a = {8,31,48,15,3,11,20,29,65,73};
    int n = a.size(), k = 73;
    vector<int> c(k+1, 0), b(n);
    for (int x : a) c[x]++;              // counts
    for (int i = 1; i <= k; i++) c[i] += c[i-1]; // prefix sums
    for (int j = n-1; j >= 0; j--)       // stable placement
        b[--c[a[j]]] = a[j];
    for (int x : b) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Radix Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Sort by [digit]{.hl}, from least significant to most significant, using a stable pass (counting sort) at each digit.

- Because each pass is stable, earlier orderings are preserved when later digits tie.

- Runs in $O(d(n + b))$ for $d$ digits and base $b$.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> a = {1560,4,123,222,2154,1061,283,2150};
    int n = a.size();
    for (int exp = 1; exp <= 1000; exp *= 10) { // 4 digits
        vector<int> cnt(10,0), out(n);
        for (int x : a) cnt[(x/exp)%10]++;
        for (int i = 1; i < 10; i++) cnt[i] += cnt[i-1];
        for (int j = n-1; j >= 0; j--) {
            int d = (a[j]/exp)%10;
            out[--cnt[d]] = a[j];
        }
        a = out;
    }
    for (int x : a) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Bucket Sort"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- For values uniformly distributed in $[0, 1)$, scatter each `A[i]` into bucket `B[n*A[i]]`.

- [Sort each bucket]{.hl} (e.g. insertion sort), then concatenate the buckets in order.

- Expected $O(n)$ time when the input is uniformly distributed.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<double> a = {0.78,0.17,0.39,0.26,0.72,
                        0.94,0.21,0.12,0.23,0.68};
    int n = a.size();
    vector<vector<double>> b(n);
    for (double x : a) b[(int)(n*x)].push_back(x); // scatter
    for (auto& bk : b) sort(bk.begin(), bk.end()); // sort each
    for (auto& bk : b)                             // gather
        for (double x : bk) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Records, Indexes, and Keys"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- A [record]{.hl} holds information about an entity — a person's record might contain a student ID, name, address, and phone number. Each such piece is a [field]{.hl}.

- An [index]{.hl} is used to *search* for a record. It is built from a field that can represent the record (e.g. the student ID); storing *every* field in the index would just duplicate the database.

- A field that is unique across records and thus distinguishes each one is a [key]{.hl}. A key can consist of one field or several fields combined.

---
layout: prism
heading: "Review: Binary Search Trees"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [binary search tree]{.hl} (BST) has the properties:
  - each node holds a unique key,
  - a root at the top; each node has at most two children,
  - every key is *greater* than all keys in its left subtree and *less* than all keys in its right subtree.

- An [in-order traversal]{.hl} therefore visits the keys in *ascending* order.

</div>
<div>

<div class="tikz-fig" style="font-family: monospace; text-align:center; margin-top: 1rem; font-size: 1.05rem; line-height: 1.6;">

<div style="color:#5c60a8; font-weight:bold;">BST on 30 20 40 10 25 35 45</div>
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;30<br/>
&nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp;&nbsp;\\<br/>
&nbsp;20&nbsp;&nbsp;&nbsp;&nbsp;40<br/>
/&nbsp;\\&nbsp;&nbsp;&nbsp;/&nbsp;\\<br/>
10&nbsp;25&nbsp;35&nbsp;45<br/>
<br/>
<span style="color:#9aa0a6;">in-order: 10 20 25 30 35 40 45</span>

</div>

</div>
</div>

---
layout: prism
heading: "Review: BST — Search, Insert, Delete"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [Search]{.hl}: compare `x` with the current key and recurse left or right; a `null` means *not found*.

- [Insert]{.hl}: perform a failing search; the `null` position reached is where the new node is hung.

- [Delete]{.hl} `r` splits into three cases:
  - **Case 1** — `r` is a leaf: just remove it.
  - **Case 2** — one child: link `r`'s parent to `r`'s child.
  - **Case 3** — two children: replace `r` with the *minimum of its right subtree*, then delete that node.

</div>
<div>

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int key; Node *l=0,*r=0; Node(int k):key(k){} };

Node* insert(Node* t, int x){
    if(!t) return new Node(x);
    if(x < t->key) t->l = insert(t->l, x);
    else if(x > t->key) t->r = insert(t->r, x);
    return t;
}
Node* findMin(Node* t){ while(t->l) t=t->l; return t; }
Node* erase(Node* t, int x){
    if(!t) return 0;
    if(x < t->key) t->l = erase(t->l, x);
    else if(x > t->key) t->r = erase(t->r, x);
    else {
        if(!t->l) return t->r;
        if(!t->r) return t->l;
        Node* s = findMin(t->r);      // Case 3
        t->key = s->key;
        t->r = erase(t->r, s->key);
    }
    return t;
}
bool search(Node* t, int x){
    if(!t) return false;
    if(t->key==x) return true;
    return x<t->key ? search(t->l,x) : search(t->r,x);
}
void inorder(Node* t){ if(t){inorder(t->l);cout<<t->key<<" ";inorder(t->r);} }

int main(){
    Node* root=0;
    for(int x:{30,20,40,10,25,35,45}) root=insert(root,x);
    cout<<"search 25: "<<search(root,25)<<"\n";
    root = erase(root, 30);          // delete node with 2 children
    cout<<"after delete 30: "; inorder(root); cout<<endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Tree Traversals"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Three depth-first orders differ only in *when* a node is visited relative to its subtrees:

<div class="sub-item-enum">

1. [pre-order]{.hl}: node, left, right.
2. [in-order]{.hl}: left, node, right.
3. [post-order]{.hl}: left, right, node.

</div>

- On a BST, in-order yields the keys in ascending order.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int key; Node *l=0,*r=0; Node(int k):key(k){} };
Node* ins(Node* t,int x){
    if(!t) return new Node(x);
    (x<t->key?t->l:t->r)=ins(x<t->key?t->l:t->r,x); return t;
}
void pre(Node* t){ if(t){cout<<t->key<<" ";pre(t->l);pre(t->r);} }
void in (Node* t){ if(t){in(t->l);cout<<t->key<<" ";in(t->r);} }
void post(Node* t){ if(t){post(t->l);post(t->r);cout<<t->key<<" ";} }

int main(){
    Node* r=0;
    for(int x:{30,20,40,10,25,35,45}) r=ins(r,x);
    cout<<"pre  : "; pre(r);  cout<<"\n";
    cout<<"in   : "; in(r);   cout<<"\n";
    cout<<"post : "; post(r); cout<<endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: AVL Trees"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- An [AVL tree]{.hl} (Adelson-Velskii and Landis) is the classic example of keeping a BST *balanced* at all times.

- Invariant: for every node, the [heights]{.hl} of its left and right subtrees differ by *at most 1*.

- This bounds the tree height at $O(\log n)$, so search, insert, and delete stay $O(\log n)$ in the worst case.

- After an insertion or deletion breaks the invariant, the tree is repaired with [rotations]{.hl}.

---
layout: prism
heading: "Review: AVL Trees — Rebalancing"
---

- Repairs come in four shapes depending on where the imbalance occurs — [LL, LR, RL, RR]{.hl}:

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div style="text-align:center;">

**LL** (single right rotation)
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w13/dsa-w13-image18.jpg" class="tikz-fig" style="width: 90%; margin-top: 0.3rem;" />

**RL** (right then left rotation)
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w13/dsa-w13-image20.jpg" class="tikz-fig" style="width: 90%; margin-top: 0.3rem;" />

</div>
<div style="text-align:center;">

**LR** (left then right rotation)
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w13/dsa-w13-image19.jpg" class="tikz-fig" style="width: 90%; margin-top: 0.3rem;" />

**RR** (single left rotation)
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w13/dsa-w13-image21.jpg" class="tikz-fig" style="width: 90%; margin-top: 0.3rem;" />

</div>
</div>

---
layout: prism
heading: "Review: Red-Black Trees"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [red-black tree]{.hl} is another balanced BST; the `null` links at the bottom are treated as *black leaf* nodes.

- Its defining properties:

<div class="sub-item-enum">

1. the root is [black]{.hl},
2. every leaf (`null`) is [black]{.hl},
3. a [red]{.hl} node cannot have a red child (no two reds in a row on any root-to-leaf path),
4. every root-to-leaf path passes through the *same number* of black nodes.

</div>

- These guarantee the longest path is at most twice the shortest, keeping height $O(\log n)$. (C++ `std::map` / `std::set` are red-black trees.)

---
layout: prism
heading: "Review: Red-Black Trees — Repair"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A newly inserted node is red. If its parent `p` is also red, property 3 is violated; since the tree was valid before, the grandparent `p2` must be black. The fix depends on the color of `p`'s sibling `s`:

<div class="sub-item-enum">

1. **Case 1 — `s` is red:** recolor `p` and `s` to black and `p2` to red, then recurse upward from `p2` (if `p2` is the root, color it black and stop).
2. **Case 2 — `s` is black:**
   - *Case 2-1* (`x` is the "inner" child): rotate about `p` to reduce it to Case 2-2.
   - *Case 2-2* (`x` is the "outer" child): rotate about `p2` and swap the colors of `p` and `p2`.

</div>

- Deletion repairs follow an analogous set of recoloring-and-rotation cases.

---
layout: prism
heading: "Review: B-Trees"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [B-tree]{.hl} node stores up to `k` keys in sorted order; a node with `k` keys has `k + 1` children.

- If the subtrees are $T_0, T_1, T_2, \ldots$, then every key in subtree $T_i$ is *greater* than $key_{i-1}$ and *less* than $key_i$.

- Keeping many keys per node makes B-trees ideal for [disk-based]{.hl} indexes, where each node maps to a block.

</div>
<div>

<div style="height: 1.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w13/dsa-w13-image22.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "Review: Hash Tables"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A [hash table]{.hl} finds an element's slot with a *single* computation: a [hash function]{.hl} `h` maps a key to an address in $0, 1, \ldots, m-1$.

- The simplest choice is `h(x) = x mod m`. For input `25, 13, 16, 15, 7` with $m = 13$:

<div class="tikz-fig" style="font-family: monospace; font-size: 0.95rem; margin-top: 0.5rem;">

0:13&nbsp;&nbsp;2:15&nbsp;&nbsp;3:16&nbsp;&nbsp;7:7&nbsp;&nbsp;12:25

</div>

- Each key lands in one probe — the ideal $O(1)$ lookup.

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int m = 13;
    int table[13];
    for (int i = 0; i < m; i++) table[i] = -1;

    int keys[] = {25, 13, 16, 15, 7};
    for (int x : keys) table[x % m] = x;   // h(x)=x mod 13

    for (int i = 0; i < m; i++)
        if (table[i] != -1)
            cout << "slot " << i << " : " << table[i] << "\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Review: Hash Tables — Collision Resolution"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Adding `28` to the previous table hits slot `2`, where `15` already sits — a [collision]{.hl}: two or more keys mapped to one address.

- [Collision resolution]{.hl} takes two broad approaches:

<div class="sub-item-enum">

1. use *extra space outside* the table — [separate chaining]{.hl} (each slot holds a list),
2. resolve *inside* the table — [open addressing]{.hl} (probe for another empty slot, as in the double hashing on the first slide).

</div>

</div>
<div>

<div style="height: 0.5rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int m = 13;
    vector<int> chain[13];             // separate chaining
    int keys[] = {25, 13, 16, 15, 7, 28, 2};
    for (int x : keys) chain[x % m].push_back(x);

    for (int i = 0; i < m; i++)
        if (!chain[i].empty()) {
            cout << "slot " << i << " :";
            for (int x : chain[i]) cout << " " << x;
            cout << "\n";
        }
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "HW_W13"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Use any coding-test practice platform you prefer (Baekjoon, Programmers, etc.).
  - The Programmers problems solved in class are *excluded*.

- Pick any topic and find and solve [three problems]{.hl}. The remaining conditions are the same as previous assignments.

- *Alternatively*, choose one data structure or algorithm on any topic and write up your own [handwritten notes]{.hl} on it.
  - Review once via the textbook first, then start from a *blank page*.

- Save as `HW_W13_20XXXXXX.pdf` and upload it to the LMS.

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
