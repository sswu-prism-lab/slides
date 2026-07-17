---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 13 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-13/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">13주차: 유전 알고리즘, 위상 정렬, 동적 계획법과 종합 복습</p>

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
heading: "DIY_W12: 이중 해싱"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [개방 주소법]{.hl}과 [이중 해싱]{.hl}에서는 *두 개*의 해시 함수를 사용해 충돌을 해결합니다:

$$
h(x) = x \bmod m
$$

$$
f(x) = 1 + (x \bmod m'),\quad m' \text{ 는 } m \text{ 보다 약간 작은 소수}
$$

- **생각해 봅시다:** 이 두 함수를 결합하면 왜 탐사(probe) 순서를 효과적으로 분산시킬 수 있을까요?

- **또 생각해 봅시다:** 두 번째 값 $f(x)$ 를 테이블 크기 $m$ 에 대해 왜 신중하게 다뤄야 할까요?

</div>
<div>

<div style="height: 1rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int m = 13, mp = 11;   // m' < m, 둘 다 소수
    int table[13];
    for (int i = 0; i < m; i++) table[i] = -1;

    auto h = [&](int x){ return x % m; };
    auto f = [&](int x){ return 1 + (x % mp); };

    int keys[] = {18, 41, 22, 44, 59, 32};
    for (int x : keys) {
        int i = h(x), step = f(x), probes = 0;
        while (table[i] != -1) {     // 충돌 -> f(x)만큼 점프
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
heading: 유전 알고리즘 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [유전 알고리즘]{.hl}은 *생물의 진화 과정을 모방하여* 최적해를 탐색하는 방법입니다.

- 각 후보 해는 [유전자]{.hl}로 표현되며, 더 알맞은 유전자가 [자연 선택]{.hl}(적자 생존)으로 선택됩니다.

- 더 알맞은 유전자끼리 [교차]{.hl}를 통해 후대 유전자를 만들지만, 후대가 선대보다 반드시 최적해에 더 가깝다고 *보장되지는* 않습니다.

- 낮은 확률로 후대 유전자에 [돌연변이]{.hl}가 일어나며, 돌연변이가 발생한 유전자 역시 최적해에서 멀어질 수 있습니다.

- 최적해(또는 충분히 좋은 해)를 찾을 때까지 이 과정을 [반복]{.hl}합니다.

---
layout: prism
heading: 유전 알고리즘 (2/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 무작위 문자열을 고정된 [타겟]{.hl}(여기서는 *Sungshin*에 대한 짧은 오마주)으로 진화시킵니다.

- 구성 요소는 다음과 같습니다:
  - 허용된 문자들의 [유전자 풀]{.hl},
  - 후보 문자열들의 [개체군]{.hl},
  - 일치하는 위치의 수를 세는 [적합도]{.hl} 함수.

- [선택]{.hl}은 적합도가 높은 유전자를 선호하고, [교차]{.hl}는 두 부모를 한 지점에서 섞으며, [돌연변이]{.hl}는 문자를 무작위로 바꿉니다.

</div>
<div>

<div style="height: 0.5rem;"></div>

```cpp
// 적합도: 타겟과 일치하는
// 위치의 개수
int fitness(const string& g) {
    int s = 0;
    for (int i = 0; i < (int)g.size(); i++)
        if (g[i] == TARGET[i]) s++;
    return s;
}

// 일점 교차(single-point crossover)
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
heading: 유전 알고리즘 (3/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 메인 루프가 [진화]{.hl}를 이끕니다:
  - 모든 유전자의 적합도를 평가하고,
  - 지금까지 *가장 적합한* 유전자를 추적·출력하며,
  - 타겟에 도달하는 즉시 중단합니다.

- 그렇지 않으면 좋은 부모를 [선택]{.hl}하여 `mutate(crossover(...))`로 다음 세대를 만듭니다.

- 각 세대는 타겟 문자열이 나타날 때까지 최고 적합도를 점점 끌어올리는 경향이 있습니다.

</div>
<div>

<div style="height: 1.5rem;"></div>

```cpp
while (gen < MAX_GEN) {
    // 이번 세대에서 가장 적합한 것 찾기
    int best = 0;
    for (int i = 1; i < POP; i++)
        if (fitness(pop[i]) >
            fitness(pop[best])) best = i;

    if (pop[best] == TARGET) break;

    vector<string> next;      // 선택 +
    for (int i = 0; i < POP; i++)   // 교차
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
heading: "DIY: 타겟 문자열 진화시키기"
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
// 토너먼트 선택: 무작위 3개 중 최적
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
    srand(1);                       // 결정론적 실행
    vector<string> pop(POP);
    for (auto& g : pop) g = randInd();

    int bestSoFar = -1;
    for (int gen = 0; gen < MAX_GEN; gen++) {
        int b = 0;
        for (int i = 1; i < POP; i++)
            if (fitness(pop[i]) > fitness(pop[b])) b = i;
        int fb = fitness(pop[b]);
        if (fb > bestSoFar) {       // 개선될 때만 출력
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
heading: 위상 정렬 (1/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 해결해야 할 작업이 여러 개 있고 일부 작업이 다른 작업보다 먼저 수행되어야 할 때, 그 순서를 지켜야 작업이 완료됩니다.

- 간선 $(i, j)$ 가 존재하면 작업 $i$ 를 작업 $j$ *보다 먼저* 수행해야 합니다.

- 이런 모든 제약을 만족하는 [방향 비순환 그래프]{.hl} $G = (V, E)$ 의 모든 정점에 대한 순서를 [위상 정렬]{.hl}이라고 합니다.

- 이는 그래프가 *순환이 없고* *방향성이 있을* 때에만 존재합니다.

</div>
<div>

<div class="theorem-box">
<div class="theorem-box-title">라면 끓이기 (하나의 DAG)</div>
<div class="theorem-box-body">

작업: `물 붓기`, `봉지 뜯기`, `점화`, `면 넣기`, `스프 넣기`, `계란 넣기`.

선후 관계: *면을 넣기* 전에 *물을 붓고* *점화*해야 하며, *면을 넣기* 전에 *봉지를 뜯어야* 하고, 마지막에 *계란을 넣기* 전에 *스프를 넣어야* 합니다.

여러 가지 유효한 순서가 존재하며, 그 중 무엇을 따라도 요리가 완성됩니다.

</div>
</div>

</div>
</div>

---
layout: prism
heading: 위상 정렬 (2/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 직관적인 알고리즘은 [진입 간선이 없는]{.hl} 정점을 반복적으로 제거합니다:

<div class="sub-item">

```text
topologicalSort(G):
  for i in 1..n:
    진입 간선이 없는 정점 u 선택
    A[i] = u
    u와 u의 진출 간선 제거
  // A[1..n]가 위상 정렬 순서
```

</div>

- 진입 차수가 0인 정점을 단순하게 찾으면 매 단계 $O(n)$ 이 듭니다. 현재 진입 차수를 배열 `c[]`에, 진입 차수 0인 정점 목록을 리스트 `d`에 유지하면 각 조회가 [상수 시간]{.hl}이 됩니다(칸(Kahn) 알고리즘).

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
heading: 위상 정렬 (3/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 직관적인 방법 외에도, [깊이 우선 탐색]{.hl}으로 위상 정렬을 만들 수 있습니다:

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
  리스트 R의 맨 앞에 v를 삽입
```

</div>

- 정점들은 위상 정렬의 *역순*으로 완료되므로, 완료된 정점을 `R`의 맨 앞에 붙이면 정렬 순서를 얻습니다.

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
    order.push_back(v);          // 완료 시각
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
heading: 동적 계획법 (1/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 단순 재귀로 피보나치 수를 계산하면 [중복되는 부분 문제]{.hl}가 생깁니다 — 같은 호출이 *지수적으로* 자주 다시 계산됩니다.

- 이 비효율은 결국, *한 번만 저장*해 두었다가 재사용하면 될 값을 매번 다시 계산하는 데서 비롯됩니다.

- 해를 만들어 나가는 동안 부분 결과를 저장하는 것이 [동적 계획법]{.hl}의 핵심입니다.

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

`fib(7)`의 호출 트리는 `fib(2)`를 여덟 번 반복하며, $n$ 이 커질수록 작업량이 폭발합니다.

</div>
</div>

---
layout: prism
heading: 동적 계획법 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- DP는 다음 두 가지 성질을 가진 문제에 적용됩니다:

<div class="sub-item-enum">

1. [최적 부분 구조]{.hl}를 이루며,
2. 단순 재귀가 중복 호출로 인해 심각한 비효율을 겪습니다.

</div>

- [상향식(Bottom-up)]{.hl}: 단일 반복문으로 테이블을 채워 지수 시간 대신 [선형]{.hl} 시간을 달성합니다.

- [하향식(Top-down, 메모이제이션)]{.hl}: 재귀는 유지하되 계산된 값을 `f[n]`에 *메모*해 두고 반복 호출 시 재사용합니다.

```text
fib-DP1(n): // 상향식               fib-DP2(n): // 하향식 (메모이제이션)
  f[1]=1; f[2]=1;                   if f[n] != 0: return f[n]
  for i in 3..n:                    if n==1 or n==2: f[n]=1
    f[i]=f[i-1]+f[i-2]              else: f[n]=fib-DP2(n-1)+fib-DP2(n-2)
  return f[n]                       return f[n]
```

---
layout: prism
heading: "DIY: 피보나치 — 재귀 vs DP"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

long long calls = 0;
long long fibRec(int n){            // 단순: 지수적 호출
    calls++;
    if (n <= 2) return 1;
    return fibRec(n-1) + fibRec(n-2);
}
long long fibBU(int n){            // 상향식: O(n)
    vector<long long> f(n+1);
    f[1]=f[2]=1;
    for(int i=3;i<=n;i++) f[i]=f[i-1]+f[i-2];
    return f[n];
}
vector<long long> memo(64,0);
long long fibMemo(int n){          // 하향식 메모이제이션: O(n)
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
heading: "실습: 정수 삼각형"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 꼭대기에서 밑변까지, 각 단계에서 인접한 *아래-왼쪽* 또는 *아래-오른쪽* 칸으로 이동할 수 있습니다. [합이 최대]{.hl}가 되는 경로를 찾으세요.

- 전형적인 상향식 DP: 각 칸은 가능한 두 선행 칸 중 더 큰 값을 누적하며, 답은 마지막 행의 최댓값입니다.

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
heading: "실습: N으로 표현"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 숫자 `N`과 사칙연산자만 사용해 `number`를 표현합니다. 사용된 `N`의 *최소* 개수를 반환하되(8을 초과하면 `-1`) 반환합니다.

- 예: $12 = 5 + 5 + 5/5 + 5/5$ 는 `5`를 다섯 개 쓰지만, 최선은 [네 개]{.hl}만 씁니다.

- `N`의 개수에 대한 DP: `dp[i]` = 정확히 `i`개의 `N`으로 표현 가능한 모든 값. *반복 숫자* `N, NN, NNN, …`과 더 작은 `dp[j]`와 `dp[i-1-j]`를 조합해 만듭니다.

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
heading: "복습: 정렬 알고리즘"
---

<div style="margin-top: 1.5rem; margin-left: 2rem">

- 다음 슬라이드들은 이번 학기에 다룬 정렬 알고리즘을, 각각 예시 배열에 대한 실행 가능한 C++ 데모와 함께 정리합니다

<div class="tikz-fig" style="font-family: monospace; text-align:center; margin-top: 1.5rem; font-size: 1.2rem; display:inline-block;">
A[] = 8, 31, 48, 15, 3, 11, 20, 29, 65, 73
</div>

- [비교 기반 정렬]{.hl}: 선택, 버블, 삽입, 병합, 퀵, 힙, 셸.

- [비교 없는 정렬]{.hl}: 계수, 기수, 버킷.

</div>

---
layout: prism
heading: "복습: 선택 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 정렬되지 않은 앞부분에서 [최대]{.hl} 원소를 반복적으로 선택해 *맨 뒤*로 보냅니다.

- 각 회차가 끝날 때마다 남은 원소 중 가장 큰 것이 최종 위치에 놓입니다.

- 시간 복잡도는 입력과 무관하게 $O(n^2)$ 이며, *교환* 횟수는 적습니다.

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
        int mx = 0;                 // a[0..last]에서 최대의 인덱스
        for (int i = 1; i <= last; i++)
            if (a[i] > a[mx]) mx = i;
        swap(a[mx], a[last]);       // 최대를 맨 뒤로 보냄
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
heading: "복습: 버블 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 왼쪽에서 오른쪽으로 훑으며 인접한 원소를 비교하고, 왼쪽이 더 크면 [교환]{.hl}합니다.

- 각 회차가 남은 원소 중 가장 큰 것을 끝으로 *떠올리며*, 그 후 마지막 원소는 제외됩니다.

- 시간 복잡도는 $O(n^2)$ 이며, 조기 종료 플래그로 이미 정렬된 배열을 감지합니다.

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
        if (!swapped) break;        // 이미 정렬됨
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
heading: "복습: 삽입 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 정렬된 앞부분을 유지하고, 다음 원소를 가져와 더 큰 원소들을 오른쪽으로 밀며 올바른 자리에 [삽입]{.hl}합니다.

- *거의 정렬된* 데이터에서는 매우 효율적이며, 최선의 경우 $O(n)$ 에 가깝습니다.

- 최악과 평균의 경우는 $O(n^2)$ 입니다.

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
        while (j >= 0 && a[j] > key) { // 더 큰 원소를 오른쪽으로
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = key;                  // key를 제자리에 넣음
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
heading: "복습: 병합 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [분할 정복]{.hl}: 배열을 반으로 나누어 각 절반을 재귀적으로 정렬한 뒤, 정렬된 두 절반을 [병합]{.hl}합니다.

- 병합은 두 절반을 인덱스 `i`, `j`로 훑으며 임시 버퍼 `tmp`에 담습니다.

- $O(n \log n)$ 시간이 보장되고 *안정적*이지만, $O(n)$ 의 추가 공간이 듭니다.

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
heading: "복습: 퀵 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [피벗]{.hl}을 고르고, 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 가도록 배열을 [분할]{.hl}한 뒤 양쪽을 재귀 처리합니다.

- 평균 시간은 $O(n \log n)$ 이며, 나쁜 피벗을 고르면 최악의 경우 $O(n^2)$ 입니다.

- *제자리(in place)*에서 정렬하며, 실제로는 대개 가장 빠른 비교 기반 정렬입니다.

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
    int pivot = a[hi], i = lo - 1;    // Lomuto 분할
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
heading: "복습: 힙 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 배열로 [최대 힙]{.hl}을 만든 뒤, 루트(최댓값)를 맨 뒤로 반복해 교환하고 줄어든 힙을 *아래로 내리며 정리*합니다.

- $O(n \log n)$ 시간이 보장되고 *제자리*에서 정렬합니다.

- 배열을 힙으로 보는 인덱싱을 사용합니다: `i`의 자식은 `2i+1`과 `2i+2`.

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
heading: "복습: 셸 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 삽입 정렬의 일반화: [간격]{.hl} `h`만큼 떨어진 원소들을 정렬한 뒤, `h`를 `1`까지 줄여 나갑니다.

- 초반의 큰 간격 회차가 원소를 먼 거리로 옮겨 놓아, 마지막 `h = 1` 회차에서 할 일이 거의 남지 않습니다.

- 성능은 간격 수열에 따라 달라지며, 여기서는 $h = \ldots, 4, 2, 1$ 을 사용합니다.

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
    for (int h = n/2; h > 0; h /= 2)        // 줄어드는 간격
        for (int i = h; i < n; i++) {
            int key = a[i], j = i;
            while (j >= h && a[j-h] > key) { // 간격 삽입
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
heading: "복습: 계수 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 각 값 $0..k$ 가 `C[]`에서 몇 번 나타나는지 센 뒤, `C`를 *누적 합*으로 바꿔 `C[i]`가 $i$ 이하인 원소의 개수를 담게 합니다.

- `A`를 뒤에서부터 훑으며 `C`를 이용해 각 원소를 출력 자리에 직접 배치하면 [안정]{.hl} 정렬이 됩니다.

- $O(n + k)$ 시간에 동작하며, $k$ 가 너무 크지 않을 때에만 효율적입니다.

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
    for (int x : a) c[x]++;              // 개수 세기
    for (int i = 1; i <= k; i++) c[i] += c[i-1]; // 누적 합
    for (int j = n-1; j >= 0; j--)       // 안정적 배치
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
heading: "복습: 기수 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 최하위 자릿수부터 최상위 자릿수까지 [자릿수]{.hl}별로, 매 자릿수마다 안정적인 회차(계수 정렬)를 사용해 정렬합니다.

- 각 회차가 안정적이므로, 뒤의 자릿수가 같을 때 앞선 순서가 보존됩니다.

- 자릿수 $d$ 와 진법 $b$ 에 대해 $O(d(n + b))$ 시간에 동작합니다.

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
heading: "복습: 버킷 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- $[0, 1)$ 범위에 균등 분포된 값들에 대해, 각 `A[i]`를 버킷 `B[n*A[i]]`에 흩뿌립니다.

- [각 버킷을 정렬]{.hl}한 뒤(예: 삽입 정렬), 버킷들을 순서대로 이어 붙입니다.

- 입력이 균등 분포일 때 기댓값 $O(n)$ 시간입니다.

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
    for (double x : a) b[(int)(n*x)].push_back(x); // 흩뿌리기
    for (auto& bk : b) sort(bk.begin(), bk.end()); // 각 버킷 정렬
    for (auto& bk : b)                             // 모으기
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
heading: "복습: 레코드, 인덱스, 키"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [레코드]{.hl}는 어떤 개체에 대한 정보를 담습니다 — 사람 레코드에는 학번, 이름, 주소, 전화번호 등이 들어갈 수 있습니다. 이러한 각각의 조각을 [필드]{.hl}라고 합니다.

- [인덱스]{.hl}는 레코드를 *검색*하는 데 사용됩니다. 레코드를 대표할 수 있는 필드(예: 학번)로 구성하며, *모든* 필드를 인덱스에 저장하면 데이터베이스를 그대로 복제하는 셈이 됩니다.

- 레코드마다 고유하여 각각을 구분할 수 있는 필드를 [키]{.hl}라고 합니다. 키는 하나의 필드 또는 여러 필드의 조합으로 구성될 수 있습니다.

---
layout: prism
heading: "복습: 이진 검색 트리"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [이진 검색 트리]{.hl}(BST)는 다음 특성을 가집니다:
  - 각 노드는 고유한 키를 가지고,
  - 최상위에 루트가 있으며, 각 노드는 최대 두 개의 자식을 갖고,
  - 모든 키는 자신의 왼쪽 서브트리의 모든 키보다 *크고*, 오른쪽 서브트리의 모든 키보다 *작습니다*.

- 따라서 [중위 순회]{.hl}는 키를 *오름차순*으로 방문합니다.

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
heading: "복습: BST — 검색, 삽입, 삭제"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [검색]{.hl}: `x`를 현재 키와 비교해 왼쪽 또는 오른쪽으로 재귀하며, `null`을 만나면 *찾지 못한* 것입니다.

- [삽입]{.hl}: 실패하는 검색을 수행하여, 도달한 `null` 자리에 새 노드를 매답니다.

- [삭제]{.hl} `r`은 세 가지 경우로 나뉩니다:
  - **Case 1** — `r`이 리프인 경우: 그냥 제거합니다.
  - **Case 2** — 자식이 하나인 경우: `r`의 부모를 `r`의 자식과 연결합니다.
  - **Case 3** — 자식이 둘인 경우: `r`을 *오른쪽 서브트리의 최솟값*으로 대체한 뒤, 그 노드를 삭제합니다.

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
    root = erase(root, 30);          // 자식이 둘인 노드 삭제
    cout<<"after delete 30: "; inorder(root); cout<<endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "복습: 트리 순회"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 세 가지 깊이 우선 순서는 노드를 서브트리에 대해 *언제* 방문하는지만 다릅니다:

<div class="sub-item-enum">

1. [전위 순회]{.hl}: 노드, 왼쪽, 오른쪽.
2. [중위 순회]{.hl}: 왼쪽, 노드, 오른쪽.
3. [후위 순회]{.hl}: 왼쪽, 오른쪽, 노드.

</div>

- BST에서는 중위 순회가 키를 오름차순으로 내줍니다.

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
heading: "복습: AVL 트리"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- [AVL 트리]{.hl}(Adelson-Velskii, Landis)는 BST를 항상 *균형* 상태로 유지하는 대표적인 예시입니다.

- 불변식: 모든 노드에 대해, 왼쪽과 오른쪽 서브트리의 [높이]{.hl} 차이가 *최대 1*입니다.

- 이로써 트리 높이가 $O(\log n)$ 으로 제한되어, 검색·삽입·삭제가 최악의 경우에도 $O(\log n)$ 을 유지합니다.

- 삽입이나 삭제로 불변식이 깨지면, [회전]{.hl}으로 트리를 수선합니다.

---
layout: prism
heading: "복습: AVL 트리 — 재균형"
---

- 수선은 불균형이 발생한 위치에 따라 네 가지 형태 — [LL, LR, RL, RR]{.hl} — 로 나뉩니다:

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div style="text-align:center;">

**LL** (단일 우회전)
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w13/dsa-w13-image18.jpg" class="tikz-fig" style="width: 90%; margin-top: 0.3rem;" />

**RL** (우회전 후 좌회전)
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w13/dsa-w13-image20.jpg" class="tikz-fig" style="width: 90%; margin-top: 0.3rem;" />

</div>
<div style="text-align:center;">

**LR** (좌회전 후 우회전)
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w13/dsa-w13-image19.jpg" class="tikz-fig" style="width: 90%; margin-top: 0.3rem;" />

**RR** (단일 좌회전)
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w13/dsa-w13-image21.jpg" class="tikz-fig" style="width: 90%; margin-top: 0.3rem;" />

</div>
</div>

---
layout: prism
heading: "복습: 레드-블랙 트리"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [레드-블랙 트리]{.hl}는 또 다른 균형 BST로, 맨 아래의 `null` 링크를 *블랙 리프* 노드로 취급합니다.

- 정의 특성은 다음과 같습니다:

<div class="sub-item-enum">

1. 루트는 [블랙]{.hl}이고,
2. 모든 리프(`null`)는 [블랙]{.hl}이며,
3. [레드]{.hl} 노드는 레드 자식을 가질 수 없고(루트-리프 경로에서 레드가 연속 둘일 수 없음),
4. 루트에서 리프까지의 모든 경로는 *같은 수*의 블랙 노드를 지납니다.

</div>

- 이 특성들이 가장 긴 경로가 가장 짧은 경로의 최대 두 배임을 보장하여 높이를 $O(\log n)$ 으로 유지합니다. (C++ `std::map` / `std::set`이 레드-블랙 트리입니다.)

---
layout: prism
heading: "복습: 레드-블랙 트리 — 수선"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 새로 삽입된 노드는 레드입니다. 부모 `p`도 레드라면 특성 3이 위반되며, 삽입 전에는 유효했으므로 조부모 `p2`는 반드시 블랙입니다. 수선 방법은 `p`의 형제 `s`의 색에 따라 달라집니다:

<div class="sub-item-enum">

1. **Case 1 — `s`가 레드:** `p`와 `s`를 블랙으로, `p2`를 레드로 바꾼 뒤 `p2`에서 위로 재귀합니다(만약 `p2`가 루트이면 블랙으로 칠하고 종료).
2. **Case 2 — `s`가 블랙:**
   - *Case 2-1* (`x`가 "안쪽" 자식): `p`를 중심으로 회전하여 Case 2-2로 만듭니다.
   - *Case 2-2* (`x`가 "바깥쪽" 자식): `p2`를 중심으로 회전한 뒤 `p`와 `p2`의 색을 맞바꿉니다.

</div>

- 삭제 수선도 이와 유사한 재색칠·회전 경우들을 따릅니다.

---
layout: prism
heading: "복습: B-트리"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [B-트리]{.hl} 노드는 최대 `k`개의 키를 정렬된 순서로 저장하며, 키가 `k`개인 노드는 `k + 1`개의 자식을 가집니다.

- 서브트리를 $T_0, T_1, T_2, \ldots$ 라 하면, 서브트리 $T_i$ 의 모든 키는 $key_{i-1}$ 보다 *크고* $key_i$ 보다 *작습니다*.

- 노드당 많은 키를 유지하는 특성 덕분에 B-트리는 각 노드가 블록에 대응되는 [디스크 기반]{.hl} 인덱스에 이상적입니다.

</div>
<div>

<div style="height: 1.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w13/dsa-w13-image22.jpg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "복습: 해시 테이블"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [해시 테이블]{.hl}은 *단 한 번의* 계산으로 원소의 슬롯을 찾습니다: [해시 함수]{.hl} `h`가 키를 $0, 1, \ldots, m-1$ 의 주소로 매핑합니다.

- 가장 단순한 선택은 `h(x) = x mod m`입니다. 입력 `25, 13, 16, 15, 7`과 $m = 13$ 에 대해:

<div class="tikz-fig" style="font-family: monospace; font-size: 0.95rem; margin-top: 0.5rem;">

0:13&nbsp;&nbsp;2:15&nbsp;&nbsp;3:16&nbsp;&nbsp;7:7&nbsp;&nbsp;12:25

</div>

- 각 키가 한 번의 탐사로 자리를 잡습니다 — 이상적인 $O(1)$ 조회입니다.

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
heading: "복습: 해시 테이블 — 충돌 해결"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 이전 테이블에 `28`을 추가하면 이미 `15`가 있는 슬롯 `2`에 부딪힙니다 — 두 개 이상의 키가 한 주소로 매핑되는 [충돌]{.hl}입니다.

- [충돌 해결]{.hl}에는 크게 두 가지 접근이 있습니다:

<div class="sub-item-enum">

1. 테이블 *바깥의 추가 공간*을 사용 — [분리 연결법(체이닝)]{.hl}(각 슬롯이 리스트를 가짐),
2. 테이블 *내부에서* 해결 — [개방 주소법]{.hl}(첫 슬라이드의 이중 해싱처럼 빈 슬롯을 탐사).

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
    vector<int> chain[13];             // 분리 연결법(체이닝)
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

- 선호하는 코딩 테스트 연습 플랫폼을 자유롭게 사용하세요(백준, 프로그래머스 등).
  - 수업 시간에 다룬 프로그래머스 문제는 *제외*입니다.

- 아무 주제나 골라 [세 문제]{.hl}를 찾아 풀어보세요. 나머지 조건은 지난 과제들과 같습니다.

- *또는*, 아무 주제의 자료구조나 알고리즘 중 하나를 골라 직접 [손 필기]{.hl}로 정리해보세요.
  - 먼저 교과서로 한 번 복습한 뒤, *백지 상태*에서 시작하는 것을 권합니다.

- `HW_W13_20XXXXXX.pdf`로 저장해 LMS에 업로드하세요.

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
