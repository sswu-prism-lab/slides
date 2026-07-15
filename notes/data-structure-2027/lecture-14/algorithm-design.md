# 알고리즘 설계 기법 (Algorithm Design)

같은 문제라도 어떤 **설계 전략**을 택하느냐에 따라 코드의 단순함과 수행 시간이 크게
달라진다. 이 절에서는 탐욕, 분할정복, 동적 계획법, 무작위, 백트래킹의 다섯 가지
대표적인 알고리즘 설계 기법을 정리한다.

> 어떤 알고리즘이 주어졌을 때 그 문제를 풀기 위해 자료구조가 반드시 특정될 필요는 없다.
> **적절한 자료구조를 선택해 수행 시간을 최소화하는 것**은 프로그래머의 역량에 달려 있다.

## 탐욕 알고리즘

탐욕 알고리즘<span class="gloss">greedy algorithm</span>은 각 단계에서 미래에 대한 고려 없이
현재 가장 좋아 보이는 것을 *탐욕적*으로 선택하는 알고리즘이다.

- 다익스트라, 프림, 크루스칼 알고리즘이 탐욕 알고리즘의 예시이다.
- 탐욕 알고리즘이 종료됐을 때, 얻어낸 해가 국소적 최적<span class="gloss">local optimum</span>이 아니라 전역적 최적<span class="gloss">global optimum</span>과 일치해야 한다.
  - 이 경우 알고리즘은 올바르며, 그렇지 않으면 최적이 아닌<span class="gloss">suboptimal</span> 해를 찾는다.
  - 반드시 최적이 요구되지 않는 상황이라면, 간단한 탐욕 알고리즘으로 근사적인 답을 빠르게 얻는 편이 복잡한 정확 알고리즘보다 나을 수 있다.

### 작업 스케쥴링

탐욕이 적용되는 예로 운영체제<span class="gloss">operating system</span>의 작업 스케쥴링<span class="gloss">job scheduling</span> 문제가 있다.

- 비선제적<span class="gloss">nonpreemptive</span>, 단일 프로세서<span class="gloss">single processor</span>의 경우, **수행 시간이 짧은 작업 순서대로** 수행하는 것이 평균 종료 시간<span class="gloss">mean completion time</span>을 가장 짧게 한다.
- 다중 프로세서<span class="gloss">multi processor</span>의 경우에도 비슷하게, 짧은 순서대로 부여하는 것이 평균 종료 시간을 최소화한다.
- 최종 종료 시간<span class="gloss">final completion time</span>을 가장 짧게 하는 것은 별개의 문제이며, 이를 계산하는 것은 복잡하다.

### 허프만 코딩

또다른 예로 파일 압축<span class="gloss">file compression</span> 문제가 있다. 문자
a, e, i, s, t, 공백(sp), 개행(nl)으로 이루어진 파일에서 각 문자의 빈도가 아래와 같다고 하자.
모든 문자를 고정 길이 3비트로 인코딩하면 총 $58 \times 3 = 174$ 비트가 든다.

| 문자 | 고정 길이 코드 | 빈도 | 비트 |
| :--: | :--: | :--: | :--: |
| a | 000 | 10 | 30 |
| e | 001 | 15 | 45 |
| i | 010 | 12 | 36 |
| s | 011 | 3 | 9 |
| t | 100 | 4 | 12 |
| sp | 101 | 13 | 39 |
| nl | 110 | 1 | 3 |
| **합계** | | | **174** |

고정 길이 코드는 아래처럼 모든 문자가 깊이 3의 잎에 놓인 **완전한** 이진 트리에 대응한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-37.svg" alt="고정 길이 3비트 코드에 대응하는 이진 트리" style="max-width: 460px;" />
  <figcaption class="cap">고정 길이 코드: 모든 문자가 깊이 3의 잎에 놓인다 (174비트)</figcaption>
</figure>

빈도가 다른 문자에 같은 길이를 주는 것은 낭비이다. 허프만 알고리즘<span class="gloss">Huffman's algorithm</span>은 다음과 같이 빈도에 따라 코드 길이를 조절한다.

- $C$ 종류의 글자가 있을 때, $C$ 개의 트리(포레스트)로 시작한다.
- 각 트리의 가중치는 그 글자가 나타나는 빈도이다.
- 가장 작은 가중치를 가진 트리 2개 $T_1$, $T_2$ 를 선택(동점이면 임의 선택)해 이들을 서브트리로 갖는 새 트리를 만들고, 이를 $C-1$ 번 반복한다.

이렇게 얻은, 용량이 최소가 되는 체계를 허프만 코드<span class="gloss">Huffman code</span>라 한다.
빈번한 문자(e, i, sp)는 짧은 코드를, 드문 문자(s, nl)는 긴 코드를 갖게 되어 총
$146$ 비트로 줄어든다.

| 문자 | 허프만 코드 | 빈도 | 비트 |
| :--: | :--: | :--: | :--: |
| a | 001 | 10 | 30 |
| e | 01 | 15 | 30 |
| i | 10 | 12 | 24 |
| s | 00000 | 3 | 15 |
| t | 0001 | 4 | 16 |
| sp | 11 | 13 | 26 |
| nl | 00001 | 1 | 5 |
| **합계** | | | **146** |

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-38.svg" alt="허프만 코드에 대응하는 이진 트리" style="max-width: 460px;" />
  <figcaption class="cap">허프만 트리: 빈번한 문자일수록 뿌리에 가까운 잎에 놓인다 (146비트)</figcaption>
</figure>

### 실습 — 허프만 코딩

우선순위 큐(최소 힙)로 가중치가 가장 작은 두 트리를 반복해서 병합한다.
동점 처리는 생성 순서로 결정적으로 고정했다. 각 문자의 코드 길이와 총 비트 수를 출력하면
위 표의 **총 146비트**가 재현된다.

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

struct Node {
    string sym;      // 잎일 때만 문자 이름
    int weight;
    int order;       // 결정적 타이브레이크용
    Node *left, *right;
    Node(string s, int w, int o) : sym(s), weight(w), order(o), left(nullptr), right(nullptr) {}
    Node(Node* l, Node* r, int o) : sym(""), weight(l->weight + r->weight), order(o), left(l), right(r) {}
};

struct Cmp {
    bool operator()(Node* a, Node* b) const {
        if (a->weight != b->weight) return a->weight > b->weight; // 작은 가중치 우선
        return a->order > b->order;                               // 동점이면 먼저 생성된 것
    }
};

void collect(Node* n, int depth, int& totalBits) {
    if (!n->left && !n->right) {           // 잎
        int d = (depth == 0 ? 1 : depth);
        cout << "  " << n->sym << " : 길이 " << d
             << " x 빈도 " << n->weight << " = " << d * n->weight << " 비트\n";
        totalBits += d * n->weight;
        return;
    }
    collect(n->left, depth + 1, totalBits);
    collect(n->right, depth + 1, totalBits);
}

int main() {
    vector<pair<string,int>> freq = {
        {"a",10}, {"e",15}, {"i",12}, {"s",3}, {"t",4}, {"sp",13}, {"nl",1}
    };
    priority_queue<Node*, vector<Node*>, Cmp> pq;
    int order = 0;
    for (auto& f : freq) pq.push(new Node(f.first, f.second, order++));

    while (pq.size() > 1) {                 // C-1번 병합
        Node* t1 = pq.top(); pq.pop();
        Node* t2 = pq.top(); pq.pop();
        pq.push(new Node(t1, t2, order++));
    }
    Node* root = pq.top();

    int totalBits = 0;
    cout << "허프만 코드 길이:\n";
    collect(root, 0, totalBits);
    cout << "총 " << totalBits << " 비트 (고정 길이 3비트 코드는 174 비트)\n";
    return 0;
}
```

</CppRunner>

### 실습 — 동전 거스름돈 (탐욕과 그 한계)

또 하나의 고전적인 탐욕 문제는 **동전 거스름돈**이다. 매 단계에서 남은 금액을 넘지 않는
가장 큰 동전을 고른다. 표준 화폐 체계에서는 항상 최적이지만, 비표준 체계에서는
탐욕이 최적이 아닌 해를 낼 수 있다는 점을 함께 확인한다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 탐욕: 매 단계에서 남은 금액을 넘지 않는 가장 큰 동전을 고른다.
vector<int> greedyChange(vector<int> coins, int amount) {
    sort(coins.rbegin(), coins.rend());
    vector<int> used;
    for (int c : coins)
        while (amount >= c) { used.push_back(c); amount -= c; }
    return used;
}

void report(const string& title, vector<int> coins, int amount) {
    vector<int> r = greedyChange(coins, amount);
    cout << title << " (" << amount << "원): ";
    int sum = 0;
    for (int c : r) { cout << c << " "; sum += c; }
    cout << "-> " << r.size() << "개";
    if (sum != amount) cout << " (거스름 실패)";
    cout << "\n";
}

int main() {
    // 표준 화폐 체계: 탐욕이 항상 최적
    report("표준 동전 {1,5,10,25,50}", {1,5,10,25,50}, 63);
    // 비표준 체계: 탐욕이 최적이 아닐 수 있다
    report("비표준 동전 {1,3,4}   ", {1,3,4}, 6); // 탐욕 4+1+1=3개, 최적 3+3=2개
    return 0;
}
```

</CppRunner>

::: warning 탐욕의 함정
비표준 동전 $\{1,3,4\}$ 로 6원을 거슬러 주면 탐욕은 $4+1+1$ 로 3개를 쓰지만,
최적은 $3+3$ 으로 2개면 된다. 탐욕이 **전역 최적과 일치하는지**는 문제마다 증명이 필요하다.
:::

## 분할정복 알고리즘

분할정복<span class="gloss">divide and conquer</span> 알고리즘은 두 파트로 구성된다.

1. *분할*<span class="gloss">divide</span>. 기본 케이스를 제외하고, 재귀적으로 풀 수 있는 더 작은 문제들로 나눈다.
2. *정복*<span class="gloss">conquer</span>. 이 하위 문제들을 풀어 원래 문제의 해답을 얻는다.

문제를 2개로 분할하고, 각 분할된 문제가 기존의 절반 크기이며, $\mathcal{O}(N)$ 의
추가 작업이 드는 경우의 수행 시간은 다음과 같다.

$$T(N) = 2\,T(N/2) + \mathcal{O}(N)$$

### 마스터 정리 개요

일반적으로 분할정복의 수행 시간은 세 경우로 나뉜다. 이것이 **마스터 정리**<span class="gloss">master theorem</span>이다.

$$
T(N) = a\,T(N/b) + \Theta(N^k) =
\begin{cases}
\mathcal{O}(N^{\log_b a}) & \text{if } a > b^k \\[2pt]
\mathcal{O}(N^k \log N) & \text{if } a = b^k \\[2pt]
\mathcal{O}(N^k) & \text{if } a < b^k
\end{cases}
$$

- 여기서 $a$ 는 하위 문제의 개수, $b$ 는 각 하위 문제의 크기 축소 비율, $\Theta(N^k)$ 는 분할·병합에 드는 추가 작업이다.
- 예로 병합 정렬은 $a=2$, $b=2$, $k=1$ 이므로 $a = b^k$ 인 두 번째 경우에 해당해 $\mathcal{O}(N \log N)$ 이다.

## 동적 계획법

- 어떤 수식이 재귀적인 형태로 정의되어 있다면 바로 재귀 알고리즘으로 옮길 수 있지만, 컴파일러가 실제로 수행하는 재귀는 직관과 다르게 매우 비효율적일 수 있다.
- 이런 경우가 예상된다면 재귀를 비재귀 방식으로 바꾸어, 각 하위 문제의 답을 체계적으로 기록해 컴파일러를 도와줄 수 있다.
- 이러한 접근을 동적 계획법<span class="gloss">dynamic programming</span>이라 한다.
- 예를 들어 피보나치 수열을 단순 재귀로 계산하면 코드는 간단하지만 **지수 시간복잡도**를 요구한다.
- 그러나 $N$ 번째 피보나치 수를 구하는 데는 바로 직전 두 값($N-1$, $N-2$ 번째)만 있으면 되므로, 동적 계획법을 쓰면 $\mathcal{O}(N)$ 이 된다.

아래는 $F_6$ 을 단순 재귀로 계산할 때의 호출 트리이다. $F_4$, $F_3$, $F_2$ 등
같은 하위 문제가 **여러 번 중복 계산**되는 것이 문제의 핵심이다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-39.svg" alt="F6를 계산하는 재귀 호출 트리" style="max-width: 520px;" />
  <figcaption class="cap">단순 재귀 피보나치의 호출 트리 — 같은 하위 문제가 중복 계산된다</figcaption>
</figure>

### 실습 — 피보나치: 재귀 vs 동적 계획법

같은 $F(30)$ 을 단순 재귀와 동적 계획법으로 계산하면서 **재귀 호출 횟수**를 세어 본다.
지수 시간과 선형 시간의 차이를 수치로 체감할 수 있다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

long long naiveCalls = 0;
long long fibNaive(int n) {           // 지수 시간: 같은 하위 문제를 반복 계산
    naiveCalls++;
    if (n < 2) return n;
    return fibNaive(n - 1) + fibNaive(n - 2);
}

long long fibDP(int n) {              // 동적 계획법: 직전 두 값만 유지, O(N)
    long long prev = 0, cur = 1;
    if (n == 0) return 0;
    for (int i = 2; i <= n; i++) {
        long long next = prev + cur;
        prev = cur; cur = next;
    }
    return cur;
}

int main() {
    cout << "재귀(naive) F(30) = " << fibNaive(30)
         << ", 호출 횟수 = " << naiveCalls << "\n";
    cout << "동적계획법 F(30) = " << fibDP(30) << ", 덧셈 29회\n";
    cout << "동적계획법 F(90) = " << fibDP(90) << " (naive로는 사실상 불가능)\n";
    return 0;
}
```

</CppRunner>

## 무작위 알고리즘

무작위 알고리즘<span class="gloss">randomized algorithm</span>에서는 의사결정을 위해 수행 중
적어도 한 번의 난수<span class="gloss">random number</span>가 발생한다.

- 이런 알고리즘은 입력뿐 아니라 발생하는 난수에도 수행 시간이 의존한다.
- 최악 수행 시간은 보통 무작위가 아닌 알고리즘<span class="gloss">unrandomized algorithm</span>의 최악 수행 시간과 같다.
- 무작위 알고리즘을 쓰면 수행 시간에 있어 특정 입력이 더 이상 중요하지 않다.
  - 대신 난수가 중요해지며, 모든 입력의 평균이 아니라 가능한 난수의 평균으로 *기대 수행 시간*<span class="gloss">expected running time</span>을 계산한다.

### 유사난수 생성

- 알고리즘이 난수를 요구한다면 이를 생성할 방법이 있어야 한다.
- 진정한 무작위성은 컴퓨터에서 불가능한데, 난수가 알고리즘에 의존해 생성되므로 정말로 무작위일 수 없기 때문이다.
- 일반적으로 *유사난수*<span class="gloss">pseudorandom number</span>를 생성하는 것으로 충분하다.
  - 난수는 여러 알려진 통계적 성질을 가지며, 유사난수도 대부분의 성질을 만족하면 충분하다.
- 가장 간단한 방식은 레머<span class="gloss">Lehmer</span>가 제안한 선형 합동 생성기<span class="gloss">linear congruential generator</span>이다.
- 숫자들 $x_1, x_2, \ldots$ 이 다음으로 생성된다고 하자.

$$x_{i+1} = A\,x_i \bmod M$$

- 수열을 시작하려면 첫 수 $x_0$ 가 주어져야 하며, 이 값을 *시드*<span class="gloss">seed</span>라 한다.
  - $x_0 = 0$ 이면 무작위성을 많이 잃지만, $A$ 와 $M$ 이 잘 선택되면 임의의 $1 \le x_0 < M$ 은 동등하게 유효하다.
  - $M$ 이 소수라면 $x_i$ 는 결코 $0$ 이 되지 않는다.
  - $M=11$, $A=7$, $x_0=1$ 이면 난수들은 $7, 5, 2, 3, 10, 4, 6, 9, 8, 1$ 로, $M-1=10$ 개 이후 수열이 반복된다.
- $M$ 이 소수라면 주기를 최대화하는 $A$ 가 항상 존재한다.
  - 다만 $M$ 이 소수라도 $A$ 선택에 따라 주기가 최대화되지 않을 수 있는데, $A=5$ 라면 위 수열은 더 짧은 주기 $5, 3, 4, 9, 1$ 을 가진다.
- 레머는 31비트 소수 $M = 2^{31} - 1 = 2147483647$ 과 주기를 최대화하는 $A = 48271$ 을 제안했다.
- 최근에는 많은 난수 발생 방식이 $x_{i+1} = (A\,x_i + c) \bmod 2^B$ 를 사용한다.
  - 여기서 $B$ 는 컴퓨터가 사용하는 정수의 비트값이고, $A$, $c$ 는 홀수이다.

### 실습 — 선형 합동 생성기

$M=11$ 로 좋은 승수 $A=7$ 과 나쁜 승수 $A=5$ 를 비교한다. 원문과 같이
$A=7$ 은 최대 주기 10, $A=5$ 는 짧은 주기 5를 재현한다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// 레머의 선형 합동 생성기: x_{i+1} = A * x_i mod M
int main() {
    long long M = 11, A = 7, x = 1;     // 소수 M=11, 승수 A=7, 시드 x0=1
    cout << "M=11, A=7, seed=1: ";
    for (int i = 0; i < 13; i++) {
        x = (A * x) % M;
        cout << x << (i < 12 ? ", " : "\n");
    }
    cout << "-> M-1=10개마다 반복 (최대 주기)\n";

    x = 1; A = 5;                        // 나쁜 승수 A=5 는 주기가 짧다
    cout << "M=11, A=5, seed=1: ";
    for (int i = 0; i < 8; i++) {
        x = (A * x) % M;
        cout << x << (i < 7 ? ", " : "\n");
    }
    cout << "-> 5개마다 반복 (주기 짧음)\n";
    return 0;
}
```

</CppRunner>

## 백트래킹 알고리즘

백트래킹<span class="gloss">backtracking</span> 알고리즘은 보통 철저한 탐색<span class="gloss">exhaustive search</span> 외에 개선의 여지가 없는 문제에 사용된다.

- 일반적으로 수행 성능은 좋지 않을 수 있지만, 그럼에도 부르트-포스<span class="gloss">brute-force</span> 탐색을 효과적으로 개선한다.
- 매우 많은 가능성이 있어도, 먼저 제외할 수 있는 선택지를 조기에 걸러 많은 부분집합을 일찍 제거한다.
  - 이렇게 많은 가능성을 제거하는 과정을 *가지치기*<span class="gloss">pruning</span>라 한다.

### 징수소 재건 문제

징수소 재건 문제<span class="gloss">turnpike reconstruction problem</span>는 $x$ 축 위에
놓인 $N$ 개의 점 $p_1, p_2, \ldots, p_N$ 을 복원하는 문제이다.

- $x_i$ 는 $p_i$ 의 $x$ 좌표이고, $N$ 개의 점은 $N(N-1)/2$ 개의 (중복될 수 있는) 거리 $\{|x_i - x_j|\}$ 를 만든다.
- 이 거리들의 집합으로부터 각 점의 위치를 재건하는 것이 목표이다.
  - 물리, 분자생물학 등 여러 분야에서 다뤄지는 문제이다.
  - 다항식의 인수분해가 곱셈보다 어렵듯, 재건 문제는 건설 문제보다 더 어렵다.
- 이 문제를 푸는 다항 시간<span class="gloss">polynomial algorithm</span> 알고리즘은 아직 알려지지 않았다.
  - 이 알고리즘은 일반적으로 $\mathcal{O}(N^2 \log N)$, 최악의 경우 지수 시간<span class="gloss">exponential time</span>을 소모한다.

거리의 중복집합<span class="gloss">multiset</span>이
$D = \{1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 10\}$ 이라 하면 $N=6$ 임을 알 수 있다.
알고리즘은 다음과 같이 진행된다.

**1단계.** $x_1 = 0$ 으로 시작하고, $D$ 의 최댓값이 $10$ 이므로 곧바로 $x_6 = 10$ 임을 안다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-40.svg" alt="징수소 재건: x1=0, x6=10 배치" style="max-width: 520px;" />
  <figcaption class="cap">1단계: 양 끝점 $x_1=0$, $x_6=10$ 을 확정</figcaption>
</figure>

**2단계.** 남은 가장 큰 거리는 $8$ 이며 $x_2=2$ 또는 $x_5=8$ 을 뜻한다. 둘은 대칭이므로
어느 것을 골라도 무방하다. $x_5=8$ 을 택하고 거리 $x_6 - x_5 = 2$, $x_5 - x_1 = 8$ 을 $D$ 에서 제거한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-41.svg" alt="징수소 재건: x5=8 배치" style="max-width: 520px;" />
  <figcaption class="cap">2단계: $x_5=8$ 확정, $D$ 에서 거리 8, 2 제거</figcaption>
</figure>

**3단계.** 다음은 명확하지 않다. 남은 최대 거리 $7$ 은 $x_4=7$ 또는 $x_2=3$ 을 뜻한다.
어느 쪽인지 알 수 없으므로 하나를 골라 시도하고, 답에 이르지 못하면 되돌아온다.
먼저 $x_4=7$ 을 고려한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-42.svg" alt="징수소 재건: x4=7 시도" style="max-width: 520px;" />
  <figcaption class="cap">3단계: $x_4=7$ 을 시도 (분기 선택)</figcaption>
</figure>

이때 남은 최대 거리 $6$ 은 $x_3=6$ 또는 $x_2=4$ 를 뜻하지만,

- $x_3=6$ 이면 $x_4 - x_3 = 1$ 이 거리 집합에 없으므로 불가능하다.
- $x_2=4$ 이면 $x_2 - x_1 = 4$ 와 $x_5 - x_2 = 4$ 가 모두 필요한데 역시 불가능하다.

따라서 더 이상 진행할 수 없으므로 철회<span class="gloss">backtrack</span>한다.

**4단계.** $x_4=7$ 이 실패했으므로 $x_2=3$ 을 시도한다. (이마저 실패하면 답이 없음으로 종료한다.)

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-43.svg" alt="징수소 재건: x2=3 시도" style="max-width: 520px;" />
  <figcaption class="cap">4단계: 철회 후 $x_2=3$ 을 시도</figcaption>
</figure>

**5단계.** 이제 $x_4=6$ 또는 $x_3=4$ 인데, $x_3=4$ 는 불가능하므로 $x_4=6$ 을 택한다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-44.svg" alt="징수소 재건: x4=6 배치" style="max-width: 520px;" />
  <figcaption class="cap">5단계: $x_4=6$ 확정</figcaption>
</figure>

**6단계.** 마지막 남은 선택은 $x_3=5$ 이며, $D$ 가 공집합이 되어 최종 해답을 찾았다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-45.svg" alt="징수소 재건: x3=5 최종 해답" style="max-width: 520px;" />
  <figcaption class="cap">6단계: $x_3=5$ 로 완성 — 점들은 $\{0,3,5,6,8,10\}$</figcaption>
</figure>

### 실습 — 징수소 재건

위 과정을 그대로 재귀 백트래킹으로 구현한다. 남은 최대 거리를 기준으로 후보 위치를
시도하고, `feasible` 검사에 실패하면 가지치기하며, 막다른 길에 이르면 삽입했던 거리를
`D` 에 되돌리고 철회한다. 출력은 위 과정의 최종 해답 $\{0,3,5,6,8,10\}$ 과 일치한다.

<CppRunner>

```cpp
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

set<int> X;                 // 지금까지 확정된 점들의 좌표
multiset<int> D;            // 아직 배치되지 않은 거리들의 중복집합
int width;

// X 안의 모든 점과 후보 좌표 y 사이의 거리가 D 안에 존재하는지 검사
bool feasible(int y, vector<int>& removed) {
    removed.clear();
    for (int x : X) {
        int dist = abs(x - y);
        auto it = D.find(dist);
        if (it == D.end()) {            // 필요한 거리가 없다 -> 가지치기
            for (int d : removed) D.insert(d);
            return false;
        }
        D.erase(it);
        removed.push_back(dist);
    }
    return true;
}

bool place() {
    if (D.empty()) return true;         // 모든 거리를 소진 -> 성공
    int y = *D.rbegin();                // 남은 가장 큰 거리
    vector<int> removed;

    // 후보 1: x = y
    int cand = y;
    if (X.find(cand) == X.end() && feasible(cand, removed)) {
        X.insert(cand);
        if (place()) return true;       // 성공하면 그대로 반환
        X.erase(cand);                  // 실패하면 철회(backtrack)
        for (int d : removed) D.insert(d);
    }
    // 후보 2: x = width - y (대칭적인 다른 선택)
    cand = width - y;
    if (X.find(cand) == X.end() && feasible(cand, removed)) {
        X.insert(cand);
        if (place()) return true;
        X.erase(cand);
        for (int d : removed) D.insert(d);
    }
    return false;                       // 두 선택 모두 실패
}

int main() {
    int arr[] = {1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 10};
    for (int v : arr) D.insert(v);

    width = *D.rbegin();                 // 최대 거리 = 가장 먼 두 점 사이 거리
    D.erase(D.find(width));
    X.insert(0);                         // x1 = 0
    X.insert(width);                     // xN = width

    if (place()) {
        cout << "재건된 점들: ";
        for (int x : X) cout << x << " ";
        cout << "\n";
    } else {
        cout << "해가 없습니다.\n";
    }
    return 0;
}
```

</CppRunner>

::: tip 다섯 가지 설계 기법 요약

| 기법 | 핵심 아이디어 | 대표 예시 |
| :-- | :-- | :-- |
| 탐욕 | 매 단계 국소 최적 선택 | 다익스트라, 허프만, 거스름돈 |
| 분할정복 | 문제를 쪼개 재귀로 정복 | 병합 정렬, 마스터 정리 |
| 동적 계획법 | 하위 문제의 답을 기록해 재사용 | 피보나치, 최단 경로 |
| 무작위 | 난수로 특정 입력 의존 제거 | 무작위 퀵정렬, LCG |
| 백트래킹 | 가지치기하며 철저 탐색 | 징수소 재건, N-퀸 |

:::
