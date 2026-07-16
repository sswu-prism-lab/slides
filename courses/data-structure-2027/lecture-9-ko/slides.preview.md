---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 9 (KO)
download: true
info: |
  ## 자료구조 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-9/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">자료구조</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">9주차: 힙</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">2027년 봄학기</p>
</div>

---
layout: prism
heading: 과목 커리큘럼
---

<div class="absolute left-10 right-10" style="top: 0rem; bottom: 0rem; display: grid; grid-template-columns: 1.2fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">과목 소개</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">기초 수학과 C++ 상세</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">알고리즘 분석</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">리스트, 스택, 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">원형 큐와 우선순위 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">트리와 트라이</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span class="text-gray-900 dark:text-gray-100">힙</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">그래프와 가중치 그래프</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">집합과 맵</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">해시 테이블</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">알고리즘 설계 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 힙
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [힙]{.hl}<sup>heap</sup> 자료구조는 고유한 성질 — *구조 성질*과 *힙-순서 성질* — 을 가지고 있어 다양한 응용에 사용될 수 있습니다.

- 힙은 [우선순위 큐]{.hl} 자료구조를 구현하는 데 사용됩니다.

- 효율적인 *정렬 알고리즘*인 [힙 정렬]{.hl}이 존재합니다.

- 힙은 최단 경로를 찾는 *다익스트라 알고리즘*이나 최소 스패닝 트리를 추정하는 *프림 알고리즘*과 같은 다양한 그래프 알고리즘의 기반이 됩니다.

- 이번 강의에서는 다양한 힙 자료구조를 다룹니다:

<div class="sub-item-enum">

1. `스며오르기(percolate up)`와 `스며내리기(percolate down)` 알고리즘을 구현합니다.
2. $d$-힙을 소개합니다.
3. 좌향 힙과 그 연산을 소개합니다.

</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">힙</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">힙</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스며오르기</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스며내리기</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><em>d</em>-힙</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">좌향 힙</span></p>
  </div>

</div>

---
layout: prism
heading: "요약: 힙 특성"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 힙은 *완전히 채워진* 이진 트리이며, 예외적으로 가장 아래 층만 왼쪽에서 오른쪽으로 채워질 수 있습니다.
  - 이 규칙을 [구조 성질]{.hl}이라고 합니다.

- 루트(부모가 없음)를 제외한 모든 노드 $X$에 대해, $X$의 부모의 키는 $X$의 키보다 작거나 같습니다.
  - 이 규칙을 [힙-순서 성질]{.hl}이라고 합니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-01.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "요약: insert — 스며오르기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 원소 $X$를 삽입하기 위해, 가장 먼저 사용 가능한 위치에 구멍을 만듭니다 — 그렇지 않으면 트리가 완전하지 않게 됩니다.
  - $X$가 힙-순서를 위반하지 않고 구멍에 들어갈 수 있다면, 그 자리에 놓고 연산을 마칩니다.
  - 그렇지 않으면 구멍의 부모에 있는 원소를 구멍으로 내려, 구멍을 루트 방향으로 올려 보내고, $X$를 놓을 수 있을 때까지 반복합니다.

- 이러한 방식을 [스며오르기]{.hl}라고 합니다: 새 원소가 알맞은 위치를 찾을 때까지 힙 위쪽으로 스며올라갑니다.

- (각 교환마다 여러 번의 할당이 필요할 수 있는) 반복적인 교환 대신 구멍만 이동시켜 작업량을 줄입니다.

- 삽입한 원소가 새로운 최소값이어서 루트까지 스며올라가는 경우, 삽입 시간은 최대 $\mathcal{O}(\log N)$까지 걸릴 수 있습니다.

---
layout: prism
heading: "요약: insert — 예시"
---

<div class="flex justify-center" style="margin-top: 1.5rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-02.svg" class="tikz-fig" style="width: 78%;" />
</div>

---
layout: prism
heading: "요약: removeMin — 스며내리기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- `removeMin` 연산은 삽입과 매우 유사하게 처리됩니다.

- 최소값이 제거되면, 루트에 구멍이 생깁니다.

- 힙이 하나 작아지므로, 힙의 마지막 원소 $X$는 어딘가로 이동해야 합니다:
  - $X$를 구멍에 놓을 수 있다면 연산을 마칩니다.
  - 이는 드문 경우이므로, 구멍의 두 자식 중 더 작은 쪽을 구멍으로 올리고 구멍을 한 단계 아래로 밀며, $X$를 놓을 수 있을 때까지 반복합니다.

- 이러한 방식을 [스며내리기]{.hl}라고 합니다.

- 이 연산의 최악의 경우 실행 시간은 $\mathcal{O}(\log N)$입니다.

---
layout: prism
heading: "요약: removeMin — 예시"
---

<div class="flex justify-center" style="margin-top: 2rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-03.svg" class="tikz-fig" style="width: 92%;" />
</div>

---
layout: prism
heading: "DIY: 스며오르기와 스며내리기"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

// a[1..n]에 저장된 이진 힙; parent(i)=i/2, children=2i, 2i+1
vector<int> a{0};   // a[0]은 감시(sentinel) 자리로 사용하지 않음

void percolateUp(int hole) {
    int x = a[hole];
    while (hole > 1 && x < a[hole / 2]) { // 구멍을 루트 방향으로 올림
        a[hole] = a[hole / 2];
        hole /= 2;
    }
    a[hole] = x;
}
void insert(int x) { a.push_back(x); percolateUp(a.size() - 1); }

void percolateDown(int hole) {
    int n = a.size() - 1, x = a[hole], child;
    while (2 * hole <= n) {
        child = 2 * hole;
        if (child != n && a[child + 1] < a[child]) child++; // 더 작은 자식
        if (a[child] < x) { a[hole] = a[child]; hole = child; }
        else break;
    }
    a[hole] = x;
}
int removeMin() {
    int mn = a[1];
    a[1] = a.back(); a.pop_back();
    if (a.size() > 1) percolateDown(1);
    return mn;
}

int main() {
    for (int v : {13, 21, 16, 24, 31, 19, 68, 65, 26, 32})
        insert(v);
    cout << "insert 14 -> heap array: ";
    insert(14);
    for (size_t i = 1; i < a.size(); i++) cout << a[i] << " ";
    cout << "\nremoveMin order: ";
    while (a.size() > 1) cout << removeMin() << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "d-힙"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 이진 힙은 매우 단순하여, 우선순위 큐가 필요할 때 거의 항상 사용됩니다.

- 간단한 일반화가 [$d$-힙]{.hl}으로, 모든 노드가 $d$개의 자식을 갖는다는 점만 제외하면 이진 힙과 완전히 같습니다(즉, 이진 힙은 $2$-힙입니다).

- 그림은 $3$-힙의 예시를 보여줍니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-04.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "d-힙 — 분석"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- $d$-힙은 이진 힙보다 훨씬 얕아서, `insert`의 실행 시간을 $\mathcal{O}(\log_d N)$으로 개선합니다.

- $d$가 클 경우 `deleteMin` 연산은 더 비싸집니다: 트리가 더 얕더라도, 표준 알고리즘으로 $d$개 자식의 최소값을 찾으려면 $d-1$번의 비교가 필요합니다.
  - 이로 인해 이 연산의 시간은 $\mathcal{O}(d \log_d N)$으로 늘어납니다.
  - $d$는 상수이므로 두 연산 모두 $\mathcal{O}(\log N)$입니다.

- 구현에는 여전히 *배열*을 사용할 수 있습니다.

- 우선순위 큐가 너무 커서 메인 메모리에 담을 수 없을 때, $d$-힙을 고려할 만합니다.

- 실제로 $4$-힙이 이진 힙보다 성능이 나을 수 있다는 근거가 있습니다.

---
layout: prism
heading: "DIY: d-힙 인덱스 연산"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

// a[1..n]에 저장된 d-힙의 경우:
//   parent(i)      = (i + d - 2) / d
//   k번째 child(i) = d*(i - 1) + k + 1   (k = 1..d)
int parent(int i, int d) { return (i + d - 2) / d; }
int child(int i, int k, int d) { return d * (i - 1) + k + 1; }

int main() {
    // 3-힙:  10 / (20 30 35) / (40 50 60 70 80 90 100 110)
    vector<int> a{0, 10, 20, 30, 35, 40, 50, 60, 70, 80, 90, 100, 110};
    int d = 3, n = a.size() - 1;
    for (int i = 1; i <= 4; i++) {
        cout << "node a[" << i << "]=" << a[i] << " children:";
        for (int k = 1; k <= d; k++) {
            int c = child(i, k, d);
            if (c <= n) cout << " " << a[c];
        }
        cout << "  parent=a[" << parent(i, d) << "]=" << a[parent(i, d)] << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">힙</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">좌향 힙</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>merge</code> 연산</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">좌향 힙</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">좌향 힙 연산</span></p>
  </div>

</div>

---
layout: prism
heading: "merge 연산"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 힙 구현의 가장 두드러진 약점은 두 힙을 하나로 합치는 것이 어려운 연산이라는 점입니다.
  - 이 추가 연산을 [`merge`]{.hl}라고 합니다.

- 이진 힙처럼 배열만 사용하면서 병합을 효율적으로 지원하는 자료구조를 설계하기는 어려워 보입니다.

- 그 이유는, 병합에는 한 배열을 다른 배열로 복사하는 작업이 필요해 보이며, 크기가 같은 두 힙의 경우 이는 $\Theta(N)$ 시간이 걸리기 때문입니다.

- 이러한 이유로, 효율적인 병합을 지원하는 모든 고급 자료구조는 *연결형* 자료구조를 필요로 합니다.

- 실제로 이로 인해 다른 모든 연산이 느려질 것으로 예상할 수 있습니다.

---
layout: prism
heading: "좌향 힙 — 널 경로 길이"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 이진 힙처럼 [좌향 힙]{.hl}도 구조 성질과 순서 성질을 모두 가집니다.

- 좌향 힙 역시 이진 트리이며, 다만 완벽하게 균형 잡히지 않고 오히려 매우 *불균형*하게 되려고 한다는 점만 다릅니다.

- 임의의 노드 $X$의 [널 경로 길이]{.hl} $npl(X)$를, $X$에서 자식이 둘 미만인 노드까지의 최단 경로 길이로 정의합니다.
  - 따라서 자식이 없거나 하나인 노드의 $npl$은 $0$입니다.
  - $npl(\texttt{nullptr}) = -1$.

- 임의의 노드의 널 경로 길이는 그 자식들의 널 경로 길이 중 *최소값*보다 $1$ 큽니다.

---
layout: prism
heading: "좌향 힙 — 좌향 성질"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [좌향 힙 성질]{.hl}: 모든 노드 $X$에 대해, *왼쪽* 자식의 널 경로 길이는 *오른쪽* 자식의 널 경로 길이보다 크거나 같습니다.
  - 그림의 노드에 적힌 값은 널 경로 길이이며, *왼쪽* 트리만 좌향 힙입니다.

- 이 성질은 트리를 의도적으로 불균형하게 만들어, 왼쪽으로 깊게 자라도록 편향시킵니다.
  - 왼쪽 노드로 이어지는 긴 경로가 가능해지며(병합을 용이하게 하므로 오히려 바람직합니다), 이것이 *좌향* 힙이라는 이름의 유래입니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-05.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "좌향 힙 연산 — merge (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 좌향 힙의 기본 연산은 *병합*입니다.
  - 삽입은 그 특수한 경우일 뿐입니다: 삽입은 노드 하나짜리 힙을 더 큰 힙과 병합하는 것입니다.

- 두 힙 중 하나가 비어 있으면, 다른 힙을 반환합니다.

- 그렇지 않으면 두 힙을 병합하기 위해 그들의 루트를 비교합니다.
  - 병합할 두 힙 $H_1$과 $H_2$를 생각해 봅시다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-06.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "좌향 힙 연산 — merge (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 먼저, *더 큰* 루트를 가진 힙을, 더 작은 루트를 가진 힙의 *오른쪽 서브힙*과 재귀적으로 병합합니다.
  - 그 오른쪽 서브힙이 비어 있으면, 다른 힙을 오른쪽 서브힙으로 붙입니다.

- 병합된 루트의 $npl$을 갱신하고, 병합 결과가 좌향 성질을 유지하도록 필요하다면 루트 바로 아래의 왼쪽 서브트리와 오른쪽 서브트리를 교환합니다.

<div class="flex justify-center" style="margin-top: 0.6rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w09-07.svg" class="tikz-fig" style="width: 52%;" />
</div>

---
layout: prism
heading: "DIY: 두 힙 병합하기"
---

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    // H1과 H2를 최소 힙으로 (greater<>를 사용한 std::priority_queue)
    priority_queue<int, vector<int>, greater<int>> H1, H2;
    for (int v : {3, 10, 21, 14, 23, 8, 17, 26}) H1.push(v);
    for (int v : {6, 12, 18, 24, 33, 7, 37, 18}) H2.push(v);

    // H2를 H1에 병합
    while (!H2.empty()) { H1.push(H2.top()); H2.pop(); }

    cout << "merged deleteMin order: ";
    while (!H1.empty()) { cout << H1.top() << " "; H1.pop(); }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY_W09: 스큐 힙과 이항 큐"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [스큐 힙]{.hl}은 좌향 힙의 *자가-수선* 버전으로, 구현이 놀랄 만큼 간단합니다.
  - 스큐 힙은 힙 순서를 가지는 이진 트리이지만 구조적 제약이 없어, 널 경로 길이 정보를 유지하지 않습니다.
  - 오른쪽 경로가 임의로 길어질 수 있으므로 모든 연산의 최악의 경우 시간은 $\mathcal{O}(N)$입니다.
  - 그럼에도 스큐 힙은 연산당 $\mathcal{O}(\log N)$의 *분할 상환* 비용을 가집니다.

- [이항 큐]{.hl}는 세 가지 연산을 모두 최악의 경우 $\mathcal{O}(\log N)$ 시간에 지원하며, 삽입은 *평균적으로 상수 시간*이 걸립니다.
  - 이항 큐는 힙 순서 트리 하나가 아니라, *포레스트*라고 하는 힙 순서 트리들의 *모음*입니다.

- 과제: 스큐 힙과 이항 큐를 찾아 학습해 보세요.

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
