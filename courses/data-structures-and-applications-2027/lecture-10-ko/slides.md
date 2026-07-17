---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 10 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-10/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">10주차: 계수·기수·버킷 정렬과 이진 검색 트리</p>

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
heading: 개요
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 이번 강의에서는 먼저 비교를 사용하지 않는 세 가지 [선형 시간]{.hl} 정렬 알고리즘을 *복습*한 뒤, 첫 번째 검색 트리 구조를 소개합니다.

  - [계수 정렬]{.hl}, [기수 정렬]{.hl}, [버킷 정렬]{.hl}의 복습.

  - [레코드, 인덱스, 키]{.hl} — 검색을 위해 데이터를 어떻게 조직하는가.

  - [이진 검색 트리]{.hl}(BST): 검색, 삽입, 삭제, 순회.

  - [파라메트릭 서치]{.hl}(답에 대한 이진 검색)로 푸는 두 가지 연습 문제.

---
layout: prism
heading: "요약: 계수 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [계수 정렬]{.hl}은 $0 \ldots k$ 범위에서 뽑은 $n$개의 정수를 아무런 비교 없이 $O(n + k)$ 시간에 정렬합니다.

- 각 정수 $i$가 입력 $A$에서 몇 번 나타나는지를 기록하는 리스트 $C[0 \ldots k]$를 사용합니다.

<div class="theorem-box">
<div class="theorem-box-title">세 단계</div>
<div class="theorem-box-body">

1. *셈.* $C[i]$ = $A$에서 값 $i$가 나타난 횟수.
2. *누적 합.* $C[i]$가 $i$ *이하*인 원소의 개수를 갖도록 $C$를 다시 씀.
3. *배치.* $C$를 이용해 $A$의 각 원소가 $B$에서 들어갈 정확한 위치를 계산함(오른쪽에서 왼쪽으로 훑으면 정렬이 [안정적]{.hl}으로 유지됨).

</div>
</div>

---
layout: prism
heading: "요약: 계수 정렬 — 구현"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> countingSort(const vector<int>& A, int k) {
    int n = A.size();
    vector<int> C(k + 1, 0), B(n);
    for (int j = 0; j < n; j++) C[A[j]]++;          // 1단계: 셈
    for (int i = 1; i <= k; i++) C[i] += C[i - 1];   // 2단계: 누적 합
    for (int j = n - 1; j >= 0; j--)                 // 3단계: 배치 (안정적)
        B[--C[A[j]]] = A[j];
    return B;
}

int main() {
    vector<int> A = {2, 5, 3, 0, 2, 3, 0, 3};
    vector<int> B = countingSort(A, 5);
    cout << "input : "; for (int x : A) cout << x << ' ';
    cout << "\nsorted: "; for (int x : B) cout << x << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "요약: 기수 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [기수 정렬]{.hl}은 여러 자리로 이루어진 키를 [최하위 자릿수]{.hl}부터 최상위 자릿수까지 한 자리씩 정렬하며, 매 패스마다 *안정적인* 정렬(계수 정렬)을 사용합니다.

- [안정적인 정렬]{.hl}은 값이 같은 원소들의 원래 상대 순서를 유지합니다 — 이것이 자릿수별 접근을 올바르게 만드는 요소입니다.

<div class="tikz-fig" style="margin-top: 0.5rem;">

| 초기 | 첫째 자릿수 | 둘째 자릿수 | 셋째 자릿수 | 넷째 자릿수 |
|:---:|:---:|:---:|:---:|:---:|
| 0123 | 1560 | 0004 | 0004 | **0004** |
| 2154 | 2150 | 0222 | 1061 | **0123** |
| 0222 | 1061 | 0123 | 0123 | **0222** |
| 0004 | 0222 | 2150 | 2150 | **0283** |
| 0283 | 0123 | 2154 | 2154 | **1061** |
| 1560 | 0283 | 1560 | 0222 | **1560** |
| 1061 | 2154 | 1061 | 0283 | **2150** |
| 2150 | 0004 | 0283 | 1560 | **2154** |

</div>

---
layout: prism
heading: "요약: 기수 정렬 — 구현"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void countingByDigit(vector<int>& A, int exp) {  // 한 자릿수에 대한 안정적인 정렬
    int n = A.size();
    vector<int> out(n), C(10, 0);
    for (int x : A) C[(x / exp) % 10]++;
    for (int d = 1; d < 10; d++) C[d] += C[d - 1];
    for (int j = n - 1; j >= 0; j--) {
        int d = (A[j] / exp) % 10;
        out[--C[d]] = A[j];
    }
    A = out;
}

int main() {
    vector<int> A = {123, 2154, 222, 4, 283, 1560, 1061, 2150};
    for (int exp = 1; exp <= 1000; exp *= 10) {   // 4자리 키에 대해 4번의 패스
        countingByDigit(A, exp);
        cout << "digit " << exp << ": ";
        for (int x : A) cout << x << ' ';
        cout << '\n';
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "요약: 버킷 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [버킷 정렬]{.hl}은 입력이 [균등 분포]{.hl}에서 뽑혔다고 가정합니다 — 범위 안의 모든 지점에 데이터가 들어 있을 *가능성*이 동일하다는 뜻이지, 데이터가 완벽하게 고르게 분포한다는 뜻은 아닙니다.

- $[0, 1)$ 범위의 실수로 이루어진 $A[0 \ldots n-1]$에 대해: 각 $A[i]$를 버킷 $B[\lfloor n \cdot A[i] \rfloor]$에 흩뿌리고, 각 버킷을 정렬(삽입 정렬)한 뒤, 버킷들을 순서대로 이어 붙입니다.

- 평균 수행 시간은 $O(n)$이지만 [상수 인자가 큽니다]{.hl}: 버킷 리스트를 만들고 유지하는 데 상당한 오버헤드가 있으며, 이를 동적으로 할당하면 추가 공간을 소모합니다.

---
layout: prism
heading: "요약: 버킷 정렬 — 구현"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void bucketSort(vector<double>& A) {
    int n = A.size();
    vector<vector<double>> B(n);
    for (double x : A) B[(int)(n * x)].push_back(x);   // 흩뿌리기
    int idx = 0;
    for (auto& bucket : B) {
        sort(bucket.begin(), bucket.end());            // 각 버킷을 삽입 정렬
        for (double x : bucket) A[idx++] = x;          // 모으기
    }
}

int main() {
    vector<double> A = {0.78, 0.17, 0.39, 0.26, 0.72,
                        0.94, 0.21, 0.12, 0.23, 0.68};
    bucketSort(A);
    cout << "sorted:";
    for (double x : A) cout << ' ' << x;
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "HW_W09: 더 빠른 버킷 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 단순한 버킷 정렬은 각 버킷 안에 연결 리스트를 만들다가 [공간 부족]{.hl}에 걸리는 경우가 많습니다. 별도의 버킷이나 리스트를 물리적으로 유지하지 *않으면서* 구현하는 아이디어가 있는데, 이렇게 하면 [퀵 정렬보다 빨라질]{.hl} 수 있습니다.

- 계수 정렬이 개별 값의 개수를 센다면, 버킷 정렬은 사실상 *특정 범위* 안의 값의 개수를 셉니다. 이 개수로부터 각 버킷의 원소들이 차지해야 할 $A[\,]$의 정확한 범위를 계산할 수 있으므로, 별도의 버킷을 쓰지 않고 $A[0 \ldots n-1]$에 바로 되써넣을 수 있습니다.

- **과제.** 위 아이디어에 기반해 이 개선된 제자리(in-place) 버킷 정렬을 구현하세요. `HW_W09_20XXXXXX.cpp`(`.py` 등)로 저장한 후 LMS에 업로드하세요.

---
layout: prism
heading: "레코드, 인덱스, 키 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [레코드]{.hl}에는 어떤 개체에 대한 정보가 들어 있습니다. 사람 레코드에는 학번, 이름, 주소, 휴대폰 번호 등이 포함될 수 있습니다. 이러한 각각의 정보를 [필드]{.hl}라고 합니다.

- [인덱스]{.hl}는 개체의 레코드를 검색하기 위해 사용됩니다.
  - 모든 레코드를 인덱스에 저장*할 수도* 있지만, 그러면 인덱스가 결국 데이터베이스 그 자체가 되어 버립니다.
  - 대신 인덱스는 레코드를 *대표하는* 필드로 구성합니다 — 사람 레코드의 경우 학번이 좋은 대표 필드가 됩니다.

- 다른 레코드와 중복되지 않으면서 각 레코드를 구분할 수 있는 필드를 [키]{.hl}라고 합니다. 키는 필드 하나 또는 여러 개로 이루어질 수 있습니다.

---
layout: prism
heading: "레코드, 인덱스, 키 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

- 가장 단순한 인덱스는 그저 [키를 배열에 정렬해 두는 것]{.hl}입니다.
  - 이 경우 검색은 평균 $O(\log N)$이 들지만, 삽입과 삭제는 평균 $O(N)$이 듭니다.

- 다양한 [검색 트리]{.hl} 구조는 이 트레이드오프를 개선합니다:

</div>
<div>

<div class="tikz-fig">
<svg viewBox="0 0 460 300" style="width: 100%;">
  <line x1="120" y1="150" x2="250" y2="70"  stroke="#888" stroke-width="1.5"/>
  <line x1="120" y1="150" x2="250" y2="230" stroke="#888" stroke-width="1.5"/>
  <line x1="330" y1="70"  x2="410" y2="30"  stroke="#888" stroke-width="1.5"/>
  <line x1="330" y1="70"  x2="410" y2="90"  stroke="#888" stroke-width="1.5"/>
  <line x1="330" y1="70"  x2="410" y2="150" stroke="#888" stroke-width="1.5"/>
  <line x1="330" y1="230" x2="410" y2="230" stroke="#888" stroke-width="1.5"/>
  <g font-size="13" text-anchor="middle" font-family="sans-serif">
    <rect x="55"  y="132" width="110" height="34" rx="6" fill="#4a6fa5"/>
    <text x="110" y="154" fill="#fff">Search Tree</text>
    <rect x="252" y="52"  width="90" height="34" rx="6" fill="#3a8f9c"/>
    <text x="297" y="74"  fill="#fff">Binary Tree</text>
    <rect x="252" y="212" width="90" height="34" rx="6" fill="#3a8f9c"/>
    <text x="297" y="234" fill="#fff">Multiway Tree</text>
    <rect x="360" y="14"  width="100" height="30" rx="6" fill="#eef" stroke="#888"/>
    <text x="410" y="34"  fill="#333">BST</text>
    <rect x="360" y="76"  width="100" height="30" rx="6" fill="#eef" stroke="#888"/>
    <text x="410" y="96"  fill="#333">AVL Tree</text>
    <rect x="360" y="136" width="100" height="30" rx="6" fill="#eef" stroke="#888"/>
    <text x="410" y="156" fill="#333">Red-Black</text>
    <rect x="360" y="216" width="100" height="30" rx="6" fill="#eef" stroke="#888"/>
    <text x="410" y="236" fill="#333">B-Tree</text>
  </g>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: "이진 검색 트리 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 검색 트리는 저장되는 *장소*에 따라 나뉩니다: [내장 검색 트리]{.hl}는 메인 메모리에 존재하고, [외장 검색 트리]{.hl}는 외부 저장 장치(예: 디스크)에 존재합니다.
  - 트리 전체가 메인 메모리에 올라가지 않을 수도 있으며, 외장 트리의 경우 대부분 [디스크 접근 시간]{.hl}이 성능을 좌우합니다.

- [이진 검색 트리]{.hl}(BST)는 다음과 같은 특성을 가집니다:

<div class="sub-item">

- 각 노드는 하나의 키를 가지며, 모든 키는 서로 다릅니다.
- 최상위 레벨에 루트가 있고, 각 노드는 최대 2개의 자식을 가집니다.
- 임의의 노드에 대해, 그 키는 왼쪽 서브 트리의 모든 키보다 [크며]{.hl}, 오른쪽 서브 트리의 모든 키보다 [작습니다]{.hl}.

</div>

---
layout: prism
heading: "이진 검색 트리 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div class="tikz-fig">
<svg viewBox="0 0 460 250" style="width: 100%;">
  <g stroke="#888" stroke-width="1.5">
    <line x1="230" y1="30" x2="120" y2="110"/><line x1="230" y1="30" x2="340" y2="110"/>
    <line x1="120" y1="110" x2="60" y2="190"/><line x1="120" y1="110" x2="180" y2="190"/>
    <line x1="340" y1="110" x2="300" y2="190"/><line x1="340" y1="110" x2="420" y2="190"/>
  </g>
  <g font-size="15" text-anchor="middle" font-family="sans-serif">
    <circle cx="230" cy="30"  r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="230" y="35">30</text>
    <circle cx="120" cy="110" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="120" y="115">20</text>
    <circle cx="340" cy="110" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="340" y="115">40</text>
    <circle cx="60"  cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="60"  y="195">10</text>
    <circle cx="180" cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="180" y="195">25</text>
    <circle cx="300" cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="300" y="195">35</text>
    <circle cx="420" cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="420" y="195">45</text>
  </g>
</svg>
<p style="text-align:center; color:#555; font-size:0.85rem; margin:0.2rem 0 0;">균형 잡힘 &mdash; 높이 3</p>
</div>
<div class="tikz-fig">
<svg viewBox="0 0 460 330" style="width: 100%;">
  <g stroke="#888" stroke-width="1.5">
    <line x1="230" y1="30" x2="140" y2="110"/><line x1="230" y1="30" x2="360" y2="110"/>
    <line x1="140" y1="110" x2="80" y2="190"/><line x1="140" y1="110" x2="200" y2="190"/>
    <line x1="80" y1="190" x2="40" y2="270"/><line x1="80" y1="190" x2="120" y2="270"/>
  </g>
  <g font-size="15" text-anchor="middle" font-family="sans-serif">
    <circle cx="230" cy="30"  r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="230" y="35">40</text>
    <circle cx="140" cy="110" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="140" y="115">30</text>
    <circle cx="360" cy="110" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="360" y="115">45</text>
    <circle cx="80"  cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="80"  y="195">20</text>
    <circle cx="200" cy="190" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="200" y="195">35</text>
    <circle cx="40"  cy="270" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="40"  y="275">10</text>
    <circle cx="120" cy="270" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="120" y="275">25</text>
  </g>
</svg>
<p style="text-align:center; color:#555; font-size:0.85rem; margin:0.2rem 0 0;">균형 잡히지 않음 &mdash; 높이 4</p>
</div>
</div>

<p style="text-align:center; margin-top: 0.8rem;">둘 다 유효한 BST이지만, 트리의 <span class="hl">높이는 효율성에 큰 영향을 미칩니다</span>.</p>

---
layout: prism
heading: "이진 검색 트리 — 검색"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 키가 $x$인 노드를 찾으려면: 그런 노드가 존재하면 반환하고, 없으면 `null`을 반환합니다.

- 각 노드에서 $x$를 그 노드의 키와 비교해 정확히 [하나]{.hl}의 서브 트리로만 재귀하므로, 검색은 루트에서 리프까지 하나의 경로를 따라갑니다.

</div>
<div>

```text
search(t, x):
// t: (서브) 트리의 루트, x: 검색하는 키
  if (t == null || t.item == x):
      return t
  else if (x < t.item):
      return search(t.left, x)
  else:
      return search(t.right, x)
```

</div>
</div>

---
layout: prism
heading: "이진 검색 트리 — 검색 (데모)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int item; Node *left = nullptr, *right = nullptr; };

Node* insert(Node* t, int x) {
    if (!t) { Node* r = new Node; r->item = x; return r; }
    if (x < t->item) t->left  = insert(t->left, x);
    else             t->right = insert(t->right, x);
    return t;
}
Node* search(Node* t, int x) {
    if (!t || t->item == x) return t;
    return x < t->item ? search(t->left, x) : search(t->right, x);
}

int main() {
    Node* root = nullptr;
    for (int v : {30, 20, 40, 10, 25, 35, 45}) root = insert(root, v);
    for (int q : {25, 33}) {
        Node* f = search(root, q);
        cout << "search(" << q << ") -> " << (f ? "found" : "null") << '\n';
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "이진 검색 트리 — 삽입 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

- $x$를 삽입하려면, 먼저 키 $x$를 이미 가진 노드가 없어야 합니다.

- $x$가 들어갈 자리를 찾는 것은 정확히 한 번의 *실패하는* 검색과 같습니다: 루트에서 검색 경로를 따라가다 `null` 링크에 이르면 거기에 $x$를 매답니다.

- `30, 20, 25, 40, 10, 35`를 순서대로 삽입하면 잘 균형 잡힌 트리가 됩니다.

</div>
<div>

```text
insert(t, x):
// t: (서브) 트리의 루트, x: 삽입할 키
  if (t == null):
      키가 x인 노드를
      t의 부모 밑에 매달고 종료
  else if (x < t.item):
      insert(t.left, x)
  else:
      insert(t.right, x)
```

</div>
</div>

---
layout: prism
heading: "이진 검색 트리 — 삽입 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 재귀 버전은 (새로워졌을 수도 있는) 서브 트리의 루트를 반환하여 부모에 다시 연결합니다:

```text
insertItem(t, x):
  if (t == null):
      r.item ← x; r.left ← r.right ← null
      return r        // 새 노드
  else if (x < t.item):
      t.left ← insertItem(t.left, x)
  else:
      t.right ← insertItem(t.right, x)
  return t
```

- `10, 20, 25, 30, 40, 45`(이미 정렬됨)를 삽입하면 높이 6의 연결 리스트로 [퇴화]{.hl}합니다.

</div>
<div>

<div class="tikz-fig" style="margin-top: 2.5rem;">
<svg viewBox="0 0 560 300" style="width: 100%;">
  <g stroke="#888" stroke-width="1.5">
    <line x1="60" y1="40" x2="150" y2="80"/>
    <line x1="150" y1="80" x2="240" y2="120"/>
    <line x1="240" y1="120" x2="330" y2="160"/>
    <line x1="330" y1="160" x2="420" y2="200"/>
    <line x1="420" y1="200" x2="510" y2="240"/>
  </g>
  <g font-size="15" text-anchor="middle" font-family="sans-serif">
    <circle cx="60"  cy="40"  r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="60"  y="45">10</text>
    <circle cx="150" cy="80"  r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="150" y="85">20</text>
    <circle cx="240" cy="120" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="240" y="125">25</text>
    <circle cx="330" cy="160" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="330" y="165">30</text>
    <circle cx="420" cy="200" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="420" y="205">40</text>
    <circle cx="510" cy="240" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="510" y="245">45</text>
  </g>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: "이진 검색 트리 — 삽입 (데모)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int item; Node *left = nullptr, *right = nullptr; };

Node* insertItem(Node* t, int x) {
    if (!t) { Node* r = new Node; r->item = x; return r; }  // 새 노드
    if (x < t->item) t->left  = insertItem(t->left, x);
    else             t->right = insertItem(t->right, x);
    return t;
}
int height(Node* t) {
    if (!t) return 0;
    return 1 + max(height(t->left), height(t->right));
}

int main() {
    Node *a = nullptr, *b = nullptr;
    for (int v : {30, 20, 25, 40, 10, 35}) a = insertItem(a, v);
    for (int v : {10, 20, 25, 30, 40, 45}) b = insertItem(b, v);  // 정렬된 입력
    cout << "balanced insert height  : " << height(a) << '\n';
    cout << "sorted insert height    : " << height(b) << '\n';
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "이진 검색 트리 — 삭제 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 노드 $r$을 삭제하는 것은 세 가지 경우로 나뉩니다:

<div class="sub-item-enum">

1. **Case 1 — $r$이 리프.** 삭제해도 아무런 영향이 없습니다: 부모가 $r$을 가리키던 링크를 `null`로 바꿉니다.
2. **Case 2 — $r$의 자식이 하나.** 부모의 포인터를 $r$의 유일한 자식으로 곧바로 재연결합니다.
3. **Case 3 — $r$의 자식이 둘.** *직후 원소*(successor, $r$의 오른쪽 서브 트리의 최소 키)를 가진 노드 $s$를 찾아 $s$를 $r$ 자리로 복사한 뒤, 오른쪽 서브 트리에서 $s$를 삭제합니다.

</div>

- Case 3은 $s$를 삭제하는 것으로 귀결되는데, $s$는 최소값이므로 자식이 최대 하나뿐이라 결국 Case 1 또는 Case 2 삭제가 됩니다.

---
layout: prism
heading: "이진 검색 트리 — 삭제 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- `delete`는 키까지 내려간 뒤 `deleteNode`가 세 가지 경우를 처리하고, `deleteMinItem`이 Case 3을 위한 직후 원소를 뽑아냅니다.

</div>
<div>

```text
delete(t, x):
  if (t == null): raiseError("not found")
  else if (x == t.item): return deleteNode(t)
  else if (x < t.item):
      t.left ← delete(t.left, x);  return t
  else:
      t.right ← delete(t.right, x); return t
```

</div>
</div>

---
layout: prism
heading: "이진 검색 트리 — 삭제 (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

```text
deleteNode(t):
  if (t.left == null && t.right == null):  // Case 1
      return null
  else if (t.left == null):                // Case 2
      return t.right
  else if (t.right == null):               // Case 2
      return t.left
  else:                                    // Case 3
      (minItem, node) ← deleteMinItem(t.right)
      t.item ← minItem; t.right ← node
      return t
```

</div>
<div>

```text
deleteMinItem(t):
  if (t.left == null):
      return (t.item, t.right)   // 최소값 찾음
  else:
      (minItem, node) ← deleteMinItem(t.left)
      t.left ← node
      return (minItem, t)
```

</div>
</div>

---
layout: prism
heading: "이진 검색 트리 — 삭제 (데모)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Node { int item; Node *left = nullptr, *right = nullptr; };

Node* insert(Node* t, int x) {
    if (!t) { Node* r = new Node; r->item = x; return r; }
    if (x < t->item) t->left = insert(t->left, x);
    else             t->right = insert(t->right, x);
    return t;
}
pair<int, Node*> deleteMin(Node* t) {
    if (!t->left) return {t->item, t->right};
    auto [m, node] = deleteMin(t->left);
    t->left = node;
    return {m, t};
}
Node* remove(Node* t, int x) {
    if (!t) return nullptr;
    if (x < t->item) t->left = remove(t->left, x);
    else if (x > t->item) t->right = remove(t->right, x);
    else {                                   // 찾음
        if (!t->left)  return t->right;      // Case 1 / 2
        if (!t->right) return t->left;       // Case 2
        auto [m, node] = deleteMin(t->right);// Case 3
        t->item = m; t->right = node;
    }
    return t;
}
void inorder(Node* t) { if (t) { inorder(t->left); cout << t->item << ' '; inorder(t->right); } }

int main() {
    Node* root = nullptr;
    for (int v : {55, 15, 60, 8, 28, 90, 3, 18, 30, 48, 38, 50, 33, 32, 36})
        root = insert(root, v);
    cout << "before      : "; inorder(root); cout << '\n';
    root = remove(root, 18);   // Case 1 (leaf)
    root = remove(root, 30);   // Case 2 (one child)
    root = remove(root, 28);   // Case 3 (two children)
    cout << "after deletes: "; inorder(root); cout << '\n';
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "트리 순회 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 트리의 모든 노드를 방문하는 것을 [순회]{.hl}라고 합니다. 세 가지 재귀적 순서가 표준입니다:

<div class="sub-item-enum">

1. [전위 순회]{.hl} — *루트*를 먼저 방문한 뒤, 왼쪽 서브 트리, 오른쪽 서브 트리 순으로 방문.
2. [중위 순회]{.hl} — 왼쪽 서브 트리, *루트*, 오른쪽 서브 트리 순으로 방문. BST에서는 키가 [정렬된 순서]{.hl}로 나옵니다.
3. [후위 순회]{.hl} — 왼쪽 서브 트리, 오른쪽 서브 트리, *루트* 순으로 방문.

</div>

---
layout: prism
heading: "트리 순회 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

```text
preOrder(r):
  if (r != null):
      visit(r)
      preOrder(r.left)
      preOrder(r.right)

inOrder(r):
  if (r != null):
      inOrder(r.left)
      visit(r)
      inOrder(r.right)

postOrder(r):
  if (r != null):
      postOrder(r.left)
      postOrder(r.right)
      visit(r)
```

</div>
<div>

<div class="tikz-fig" style="margin-top: 1rem;">
<svg viewBox="0 0 480 300" style="width: 100%;">
  <g stroke="#888" stroke-width="1.5">
    <line x1="240" y1="30" x2="140" y2="100"/><line x1="240" y1="30" x2="360" y2="100"/>
    <line x1="140" y1="100" x2="80" y2="170"/><line x1="140" y1="100" x2="200" y2="170"/>
    <line x1="360" y1="100" x2="420" y2="170"/>
    <line x1="200" y1="170" x2="150" y2="240"/><line x1="200" y1="170" x2="250" y2="240"/>
  </g>
  <g font-size="15" text-anchor="middle" font-family="sans-serif">
    <circle cx="240" cy="30"  r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="240" y="35">6</text>
    <circle cx="140" cy="100" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="140" y="105">2</text>
    <circle cx="360" cy="100" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="360" y="105">8</text>
    <circle cx="80"  cy="170" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="80"  y="175">1</text>
    <circle cx="200" cy="170" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="200" y="175">4</text>
    <circle cx="420" cy="170" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="420" y="175">9</text>
    <circle cx="150" cy="240" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="150" y="245">3</text>
    <circle cx="250" cy="240" r="20" fill="#fff" stroke="#5c60a8" stroke-width="2"/><text x="250" y="245">5</text>
  </g>
</svg>
</div>

</div>
</div>

---
layout: prism
heading: "트리 순회 (데모)"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int item; Node *left = nullptr, *right = nullptr; };
Node* insert(Node* t, int x) {
    if (!t) { Node* r = new Node; r->item = x; return r; }
    if (x < t->item) t->left = insert(t->left, x);
    else             t->right = insert(t->right, x);
    return t;
}
void pre(Node* t)  { if (t) { cout << t->item << ' '; pre(t->left);  pre(t->right); } }
void in(Node* t)   { if (t) { in(t->left);  cout << t->item << ' '; in(t->right); } }
void post(Node* t) { if (t) { post(t->left); post(t->right); cout << t->item << ' '; } }

int main() {
    Node* root = nullptr;
    for (int v : {6, 2, 8, 1, 4, 9, 3, 5}) root = insert(root, v);
    cout << "preorder : "; pre(root);  cout << '\n';
    cout << "inorder  : "; in(root);   cout << "  (sorted!)\n";
    cout << "postorder: "; post(root); cout << '\n';
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "연습: 입국심사 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- $n$명이 입국심사를 받으려고 한 줄로 대기합니다. 각 심사대는 한 사람을 심사하는 데 걸리는 시간이 서로 다릅니다. 모든 심사대는 비어 있는 상태로 시작하며, 한 번에 한 명씩 처리합니다. 맨 앞 사람은 비어 있는 아무 심사대로 가거나 — 더 빠른 심사대가 빌 때까지 기다릴 수 있습니다.

- 우리는 *모든 사람*의 심사가 끝날 때까지의 총 시간을 [최소화]{.hl}하려 합니다. $n$과 사람당 심사 시간 `times[]`가 주어졌을 때 그 최솟값을 반환하세요.

<div class="theorem-box">
<div class="theorem-box-title">파라메트릭 서치 — 답에 대한 이진 검색</div>
<div class="theorem-box-body">

후보 시간 $T$에 대해, 심사대 $i$는 $\lfloor T / \text{times}[i] \rfloor$명을 처리할 수 있습니다. 총 처리 인원은 $T$에 대해 [단조]{.hl}이므로, $\sum_i \lfloor T/\text{times}[i]\rfloor \geq n$을 만족하는 가장 작은 $T$를 이진 검색합니다. `n = 6, times = [7, 10]`일 때 답은 `28`입니다.

</div>
</div>

---
layout: prism
heading: "연습: 입국심사 (2/2)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long solution(int n, vector<int> times) {
    long long lo = 1, hi = (long long)*max_element(times.begin(), times.end()) * n;
    long long ans = hi;
    while (lo <= hi) {
        long long mid = (lo + hi) / 2, cnt = 0;
        for (int t : times) cnt += mid / t;   // 시간 mid까지 처리한 인원
        if (cnt >= n) { ans = mid; hi = mid - 1; }
        else            lo = mid + 1;
    }
    return ans;
}

int main() {
    cout << "answer = " << solution(6, {7, 10}) << endl;  // expected 28
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "연습: 징검다리 (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 출발점에서 `distance`만큼 떨어진 곳에 도착점이 있고, 그 사이에 바위들이 놓여 있습니다. 우리는 정확히 `n`개의 바위를 제거합니다. 제거 후, 연속된 지점(출발점, 남은 바위들, 도착점) 사이의 간격을 보고 그중 [최소]{.hl} 간격을 취합니다.

- `n`개의 바위를 제거하는 모든 방법 중에서, [가능한 가장 큰]{.hl} 최소 간격을 반환하세요. `distance = 25, rocks = [2, 14, 11, 21, 17], n = 2`일 때 답은 `4`입니다.

<div class="theorem-box">
<div class="theorem-box-title">파라메트릭 서치 — 답에 대한 이진 검색</div>
<div class="theorem-box-body">

후보 최소 간격 $d$를 이진 검색합니다. 왼쪽에서 오른쪽으로 훑으며, 마지막으로 남긴 지점으로부터 $d$보다 가까운 바위를 탐욕적으로 제거하고 제거 횟수를 셉니다. 그 횟수가 $\leq n$이면 간격 $d$는 [실현 가능]{.hl}하므로 더 큰 값을 찾습니다.

</div>
</div>

---
layout: prism
heading: "연습: 징검다리 (2/2)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    sort(rocks.begin(), rocks.end());
    rocks.push_back(distance);            // 도착점을 마지막 지점으로 취급
    int lo = 1, hi = distance, ans = 0;
    while (lo <= hi) {
        int mid = (lo + hi) / 2, prev = 0, removed = 0;
        for (int p : rocks) {
            if (p - prev < mid) removed++;   // 너무 가까움: 이 바위 제거
            else                prev = p;    // 남김
        }
        if (removed <= n) { ans = mid; lo = mid + 1; }
        else               hi = mid - 1;
    }
    return ans;
}

int main() {
    cout << "answer = " << solution(25, {2, 14, 11, 21, 17}, 2) << endl;  // expected 4
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY_W10"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- `search`, `insert`, `delete`, `isEmpty`, `clear`(전부 비우기)까지 전체 ADT를 지원하는 [이진 검색 트리]{.hl}를 구현하세요.

- 오늘 두 연습 문제의 배경이 된 "답에 대한 이진 검색" 기법인 [파라메트릭 서치]{.hl}에 대해 찾아보고, 여러분만의 문제에 적용해 보세요.

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
