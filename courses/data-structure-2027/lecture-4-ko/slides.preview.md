---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 4 (KO)
download: true
info: |
  ## 자료구조 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-4/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">4주차: 리스트, 스택, 큐</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">기초 수학과 C++ 세부사항</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">알고리즘 분석</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span class="text-gray-900 dark:text-gray-100">리스트, 스택, 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">원형 큐와 우선순위 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">트리와 트라이</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">힙</span></p>
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
heading: "요약: 수학적 배경"
---

<div style="height: 1.5rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Def. 함수들 사이의 상대적 순서</div>
<div class="theorem-box-body">

$T(N)=\mathcal{O}(f(N))$ if $\exists$ positive _constants_ $c, n_0$ s.t. $T(N)\leq cf(N)$ when $N\geq n_0$.

$T(N)=\Omega(g(N))$ if $\exists$ positive _constants_ $c, n_0$ s.t. $T(N)\geq cg(N)$ when $N\geq n_0$.

$T(N)=\Theta(h(N))$ iff. $T(N)=\mathcal{O}(h(N))$ and $T(N)=\Omega(h(N))$.

$T(N)=o(p(N))$ if, $\forall$ positive constants $c$, $\exists\, n_0$ s.t. $T(N)<cp(N)$ when $N>n_0$.

</div>
</div>

---
layout: prism
heading: "요약: 일반적 규칙"
---

<div style="height: 1.5rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">일반적 규칙</div>
<div class="theorem-box-body">

**규칙 1.** `for` 루프의 수행 시간은 (검사를 포함한) 루프 내부 문장들의 수행 시간에 반복 횟수를 곱한 값을 넘지 않는다.

**규칙 2.** 중첩된 루프 그룹 안에 있는 문장의 전체 수행 시간은, 그 문장의 수행 시간에 모든 루프의 크기의 곱을 곱한 값이다.

**규칙 3.** 연속된 문장들은 단순히 더해지며, 이는 곧 그중 최댓값이 중요하다는 것을 의미한다.

**규칙 4.** `if`/`else` 문장의 수행 시간은, 검사의 수행 시간에 각 조건부 문장의 수행 시간 중 더 큰 것을 더한 값을 결코 넘지 않는다.

</div>
</div>

---
layout: prism
heading: 리스트, 스택, 큐
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 이번 강의에서는 가장 간단하고 기본적인 세 가지 자료구조를 다룬다.

- 대부분의 중요한 프로그램은 이 구조들 중 적어도 하나를 명시적으로 사용하며, [스택]{.hl}은 선언 여부와 관계없이 프로그램 내에서 항상 _묵시적으로_ 사용된다.

- 이번 강의에서는 이 세 가지 자료구조를 다루고 이들을 구현한다:

<div class="sub-item-enum">

1. [추상 데이터 타입]{.hl}의 개념을 소개한다.
2. [리스트]{.hl}에서의 연산을 효율적으로 수행하는 방법을 보인다.
3. [스택]{.hl} 추상 데이터 타입과 그 구현을 소개한다.
4. [큐]{.hl} 추상 데이터 타입과 그 구현을 소개한다.

</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">추상 데이터 타입</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">추상 데이터 타입</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">리스트 ADT</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">스택 ADT</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">큐 ADT</span></p>
  </div>

</div>

---
layout: prism
heading: 추상 데이터 타입
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [추상 데이터 타입]{.hl}(ADT)은 객체들의 집합과 연산들의 집합을 함께 묶은 것이다.

- ADT는 _수학적 추상화_이며, ADT의 정의 어디에도 이 연산들의 집합이 _어떻게_ 구현되는지에 대한 언급은 없다.

- 정수, 실수, 부울 값이 데이터 타입인 것처럼, 리스트·집합·그래프와 같은 객체들도 그 연산들과 함께 ADT로 볼 수 있다.
  - 정수, 실수, 부울 값에는 그와 연관된 연산이 있으며, ADT도 마찬가지이다.

- 집합 ADT에 대해서는 _add_, _remove_, _size_, _contains_와 같은 연산을 가질 수 있다.
  - 다른 방식으로는, 집합에 대해 서로 다른 ADT를 정의하는 _union_과 _find_ 두 연산만을 원할 수도 있다.

---
layout: prism
heading: "추상 데이터 타입 — 디자인 결정"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- C++의 [클래스]{.hl}는 구현 세부 사항을 적절히 은닉하면서 ADT의 구현을 지원한다.
  - ADT에 대한 연산 수행이 필요한 프로그램의 다른 부분에서는 적절한 메소드를 호출하여 이를 수행할 수 있다.

- 구현 세부 사항을 변경해야 한다면, 단지 ADT 연산을 수행하는 루틴만 변경함으로써 쉽게 처리할 수 있어야 한다.
  - 이상적인 경우, 이 변경은 프로그램의 나머지 부분에 완벽하게 _무관하게(transparent)_ 이루어진다.

- 각 ADT에 어떤 연산이 지원되어야 하는지 알려주는 규칙은 없으며, 이것은 [디자인 결정]{.hl}이다. 에러 처리와 평형 상태를 깨는 것(tie breaking) 또한 프로그램 설계자에게 달려 있다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">추상 데이터 타입</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">리스트 ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">리스트 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">단순 배열 기반 리스트 구현</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">단순 연결 리스트</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">STL에서의 <code>vector</code> 및 <code>list</code></span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">스택 ADT</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">큐 ADT</span></p>
  </div>

</div>

---
layout: prism
heading: 리스트 모델
---

- 우리는 $A_0, A_1, A_2, \ldots, A_{N-1}$ 형태의 일반적인 리스트를 다루며, 이 리스트의 [크기]{.hl}는 $N$이다.
  - 크기가 $0$인 특수한 리스트를 [비어있는 리스트]{.hl}라고 한다.
  - $A_i$는 $A_{i-1}$에 _후행_(succeed)하고 $(i<N)$, $A_{i-1}$은 $A_i$에 _선행_(precede)한다 $(i>0)$; 첫 번째 원소는 $A_0$, 마지막은 $A_{N-1}$이다.
  - 리스트에서 원소 $A_i$의 [위치]{.hl}는 $i$이다.

- 이 정의들과 함께 리스트 ADT에 대한 연산들의 집합이 존재한다:
  - `printList`와 `makeEmpty`는 이름 그대로의 작업을 수행한다.
  - `find`는 어떤 항목이 처음으로 나타나는 위치를 반환한다.
  - `insert`와 `remove`는 어떤 위치에 원소를 삽입하거나 삭제한다.
  - `findKth`는 어떤 위치의 원소를 반환한다.

- 어떤 함수가 적절한지에 대한 해석과 특이한 경우의 처리는 전적으로 프로그래머에게 달려 있다(예를 들어, `next`와 `previous`를 추가할 수 있다).

---
layout: prism
heading: 단순 배열 기반 리스트 구현
---

- 이 모든 리스트 ADT 연산은 [배열]{.hl}을 이용하여 구현될 수 있다.
  - 배열은 고정된 용량으로 생성되지만, 내부적으로 배열을 저장하는 `vector` 클래스는 필요할 때 용량을 _두 배로_ 늘려 배열이 커질 수 있게 한다.

- 배열 기반 구현은 `printList`를 선형 시간에 수행하게 하고, `findKth`는 _상수_ 시간이 걸린다 — 기대할 수 있는 최선이다.

- `insert`와 `remove`는 어디에서 일어나는지에 따라 잠재적으로 비용이 크다.
  - 위치 $0$에 삽입하려면 배열 전체를 한 칸씩 밀어내려야 하고, 첫 번째 원소를 삭제하려면 모든 원소를 한 칸씩 끌어올려야 한다 — 최악의 경우 $\mathcal{O}(N)$.
  - 평균적으로 리스트의 절반을 움직여야 하므로, 여전히 선형 시간이 필요하다.
  - 모든 연산이 리스트의 끝 부분에서 일어난다면 어떤 원소도 이동하지 않으므로, 추가와 삭제는 $\mathcal{O}(1)$ 시간이 걸린다.

---
layout: prism
heading: "배열 기반 구현 — 연산"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- `findKth`는 상수 시간의 인덱스 접근이다.

- 위치 $p$에서의 `insert`는 _뒷부분을 오른쪽으로 이동_해야 하고, 위치 $p$에서의 `remove`는 _뒷부분을 왼쪽으로 이동_해야 한다.

- 두 이동 모두 최악의 경우 $\mathcal{O}(N)$이다 — 리스트를 _연속적으로_ 저장하는 대가이다.

</div>
<div>

```cpp
// findKth(i): O(1) 인덱스 접근
int findKth(const vector<int>& a, int i) {
    return a[i];
}
// 위치 p에 x 삽입: O(N)
void insert(vector<int>& a, int p, int x) {
    a.push_back(a.back());        // 하나 늘림
    for (int j = a.size()-1; j > p; j--)
        a[j] = a[j - 1];          // 뒤로 밀기
    a[p] = x;
}
// 위치 p에서 삭제: O(N)
void remove(vector<int>& a, int p) {
    for (int j = p; j+1 < (int)a.size(); j++)
        a[j] = a[j + 1];          // 앞으로 당기기
    a.pop_back();
}
```

</div>
</div>

---
layout: prism
heading: 단순 연결 리스트
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 삽입과 삭제가 리스트 전반에서 — 특히 앞부분에서 — 일어난다면 배열은 좋은 선택이 아니므로, [연결 리스트]{.hl}로 눈을 돌린다.

- 삽입과 삭제의 선형 비용을 피하기 위해, 리스트는 _연속적으로_ 저장되지 _않는다_.
  - 연결 리스트는 메모리상에서 인접할 필요가 없는 [노드]{.hl}들의 연쇄이다.
  - 각 노드는 원소와, 그 후행자를 담고 있는 노드로의 링크를 포함한다.
  - 이것이 `next` 링크이며, 마지막 셀의 `next`는 빈 포인터(`nullptr`)를 가리킨다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-01.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "연결 리스트 — 순회와 remove"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `printList()`나 `find(x)`를 실행하려면, 첫 번째 노드에서 시작하여 `next` 링크를 따라 순회한다 — 배열에서와 같이 명백히 _선형 시간_이다(다만 상수 항은 더 클 가능성이 높다).

- `findKth`는 더 이상 그만큼 효율적이지 않다: `findKth(i)`는 $\mathcal{O}(i)$ 시간이 걸린다.
  - 실제로 이 경계는 비관적인데, 호출이 흔히 정렬된 순서로 이루어지기 때문이다 — `findKth(2)`, `findKth(3)`, `findKth(4)`, `findKth(6)`은 모두 한 번의 스캔으로 수행될 수 있다.

- `remove` 메소드는 단 한 번의 `next` 포인터 변경으로 실행될 수 있다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-02.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "연결 리스트 — insert"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- `insert` 메소드는 `new` 호출을 통해 시스템으로부터 새 노드를 얻은 뒤 _두 번_의 `next` 포인터 기동을 수행한다.

- 변경이 일어날 위치를 알고 있다면, 삽입이나 삭제는 많은 항목을 이동시킬 필요가 없다 — 오직 _상수_ 개수의 링크 변경만으로 충분하다.

- 따라서 앞부분에 추가하거나 첫 항목을 삭제하는 것은 상수 시간 연산이며, 끝에 추가하는 것도 상수 시간일 수 있다.
  - 마지막 항목을 삭제하는 것은 더 까다롭다: 마지막 직전 항목을 찾아 그 `next` 링크를 `nullptr`로 설정하고, 마지막 노드 링크를 갱신해야 한다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-03.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "이중 연결 리스트를 향하여"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 고전적인 연결 리스트에서, 마지막 노드로의 링크가 있어도 마지막 직전 노드에 대한 정보는 _전혀_ 제공하지 않는다.

- 마지막 직전 노드로의 세 번째 링크를 유지하는 것도 소용이 없는데, 그것 역시 삭제 시 갱신되어야 하기 때문이다.

- 대신, 모든 노드가 자신의 _이전_ 노드로의 링크를 유지하도록 하며, 이를 [이중 연결 리스트]{.hl}라고 한다.

</div>
<div>

<div style="height: 4rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-04.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "이중 연결 리스트 — 센티널 노드"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>


- 순환자 클래스는 _현재 노드_로의 포인터를 저장하고 끝 표시자가 유효한 위치이므로, 끝 표시자를 나타내기 위한 별도의 노드를 끝에 만드는 것이 합리적이다.

- 마찬가지로 앞쪽에도 별도의 노드를 만들어 논리적으로 시작 표시자를 나타낼 수 있다.

- 이들이 [센티널 노드]{.hl}이다: 앞과 끝의 노드를 각각 [머리 노드]{.hl}($H$)와 [꼬리 노드]{.hl}($T$)라고 한다.
  - 이들은 많은 특수 케이스를 없애 코딩을 크게 단순화한다 — 예를 들어, 머리 노드가 없다면 첫 노드를 삭제하는 것이 특수 케이스가 된다.

</div>
<div>

<div style="height: 3.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-05.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "이중 연결 리스트 — 노드"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 각 `Node`는 데이터 원소와 함께 두 개의 링크를 저장한다 — 하나는 _선행자_(`prev`)로, 다른 하나는 _후행자_(`next`)로.

- 두 링크가 모두 있으면, 노드를 리스트에 끼워 넣거나 빼내는 것은 상수 개수의 포인터 대입으로 이루어진다.

</div>
<div>

<div style="height: 2.5rem;"></div>

```cpp
struct Node {
    Object data;
    Node*  prev;
    Node*  next;
    Node(const Object& d,
         Node* p, Node* n)
        : data{d}, prev{p}, next{n} {}
};
```

</div>
</div>

---
layout: prism
heading: "이중 연결 리스트 — insert와 erase"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- `insert`는 새 노드를 할당하고, 그 `prev`/`next`가 현재 위치 _앞_에 노드를 끼워 넣는다 — 이웃 노드들에 대한 두 번의 링크 갱신.

- `erase`는 이웃 노드들을 서로 다시 연결하여 현재 노드를 건너뛰게 한 뒤 그것을 `delete`한다.

- 위치를 알고 있다면 각 연산은 $\mathcal{O}(1)$이다.

</div>
<div>

```cpp
// itr 앞에 x 삽입
iterator insert(iterator itr, const Object& x) {
    Node* p = itr.current;
    theSize++;
    Node* n = new Node{x, p->prev, p};
    p->prev->next = n;
    p->prev = n;
    return iterator{n};
}
// itr 위치의 노드 삭제
iterator erase(iterator itr) {
    Node* p = itr.current;
    iterator retVal{p->next};
    p->prev->next = p->next;
    p->next->prev = p->prev;
    delete p;
    theSize--;
    return retVal;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: 단일 연결 리스트"
---

<div style="height: 0rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int d, Node* n = nullptr) : data{d}, next{n} {}
};
int main() {
    // 앞쪽에 삽입하며 A0 -> A1 -> A2 -> nullptr 만들기
    Node* head = nullptr;
    for (int v : {2, 1, 0})          // 2, 그 다음 1, 그 다음 0을 앞에 넣기
        head = new Node{v, head};

    // 첫 번째 노드 뒤에 9 삽입 (두 번의 next 포인터 기동)
    Node* p = head;
    p->next = new Node{9, p->next};

    cout << "list: ";
    for (Node* cur = head; cur != nullptr; cur = cur->next)
        cout << cur->data << " -> ";
    cout << "nullptr" << endl;

    while (head) { Node* t = head; head = head->next; delete t; }  // 해제
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "STL에서의 vector 및 list"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- C++ 언어는 흔히 [표준 템플릿 라이브러리]{.hl}(STL)로 알려진 일반적인 자료구조들의 구현을 포함한다.
  - 리스트 ADT는 그중 하나이며, STL의 자료구조는 [컬렉션]{.hl} 또는 [컨테이너]{.hl}라고 불린다.

- [`vector`]{.hl}는 리스트 ADT의 _크기 변경 가능한 배열_ 구현을 제공한다.
  - 장점: _상수_ 시간에 인덱싱이 가능하다.
  - 단점: _끝_에서 하지 않는 한 삽입과 삭제의 비용이 크다.

- [`list`]{.hl}는 리스트 ADT의 _이중 연결 리스트_ 구현을 제공한다.
  - 장점: 위치를 알고 있다면 삽입과 삭제의 비용이 낮다.
  - 단점: `list`는 인덱싱이 쉽지 않다.

---
layout: prism
heading: "STL 컨테이너 — 공통 메소드"
---

- `vector`와 `list`는 모두 저장할 항목의 타입으로 실체화되는 _클래스 템플릿_이다.

- _모든_ STL 컨테이너에서 사용할 수 있는 세 가지 메소드가 있다:
  - `int size() const`는 원소의 개수를 반환한다.
  - `void clear()`는 모든 원소를 제거한다.
  - `bool empty() const`는 컨테이너에 원소가 없으면 `true`를 반환한다.

- 두 컨테이너 모두 끝에서의 추가/삭제와 앞의 접근을 상수 시간에 지원한다:
  - `void push_back(const Object& x)`는 `x`를 리스트의 끝에 추가한다.
  - `void pop_back()`는 리스트 끝의 객체를 제거한다.
  - `const Object& back() const`는 끝의 객체를 반환한다.
  - `const Object& front() const`는 앞의 객체를 반환한다.

---
layout: prism
heading: "vector 전용 및 list 전용 메소드"
---

- `vector`는 `list`에는 없는 자신만의 메소드를 가지고 있다. 그중 둘은 효율적인 _인덱싱_을 지원한다:
  - `Object& operator[](int idx)`는 경계 검사 _없이_ `idx`의 객체를 반환한다.
  - `Object& at(int idx)`는 경계 검사와 _함께_ `idx`의 객체를 반환한다.

- 다른 둘은 프로그래머가 내부 용량을 확인하고 변경할 수 있게 한다:
  - `int capacity() const`는 `vector`의 내부 용량을 반환한다.
  - `void reserve(int newCapacity)`는 새 용량을 설정한다.

- 이중 연결 리스트는 앞부분의 효율적인 변경을 허용하지만 `vector`는 그렇지 않으므로, 아래 두 메소드는 `list`에서만 사용할 수 있다:
  - `void push_front(const Object& x)`는 `x`를 `list`의 앞에 추가한다.
  - `void pop_front()`는 `list` 앞의 객체를 제거한다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">추상 데이터 타입</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">리스트 ADT</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">스택 ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스택 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스택의 구현</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">STL에서의 <code>stack</code></span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스택의 응용</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">큐 ADT</span></p>
  </div>

</div>

---
layout: prism
heading: 스택 모델
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- [스택]{.hl}은 삽입과 삭제가 오직 한 위치에서만 — 리스트의 끝, 즉 [탑]{.hl}에서만 — 수행되도록 제한된 리스트이다.
  - [후입선출]{.hl}(LIFO) 특성.

- 기본 연산은 삽입에 해당하는 [`push`]{.hl}와, 가장 최근에 삽입된 원소를 삭제하는 [`pop`]{.hl}이다.

- 가장 최근에 삽입된 원소는 `pop` 이전에 `top` 연산을 이용해 확인할 수 있다.

</div>
<div>

<div style="height: 0rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-06.svg" class="tikz-fig" style="width: 60%;" />

</div>
</div>

---
layout: prism
heading: 연결 리스트 기반 스택 구현
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 스택은 리스트이므로, 어떤 리스트 구현이든 사용할 수 있다.
  - `list`와 `vector`는 스택 연산을 지원하며, 99%의 경우 가장 합리적인 선택이다.

- 때로는 특수 목적의 구현이 더 빠를 수 있다.
  - 스택 연산은 상수 시간이므로, 아주 특수한 환경을 제외하고는 눈에 띄는 향상을 가져오기 어렵다.

- 스택의 첫 번째 구현은 _단일 연결 리스트_를 사용한다:
  - 리스트의 _앞_에 삽입하여 `push`한다.
  - 리스트의 _앞_ 원소를 삭제하여 `pop`한다.
  - `top` 연산은 단지 앞 원소를 확인하여 그 값을 반환한다(때로는 `pop`과 `top`이 하나로 합쳐지기도 한다).

---
layout: prism
heading: "연결 리스트 기반 스택 — 구현"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- `push`는 새 노드를 앞에 붙여 새로운 `topOfStack`으로 만든다.

- `pop`은 앞 노드의 연결을 끊고 그것을 `delete`한다.

- `top`은 앞 노드의 값을 반환한다. 모든 연산은 오직 앞부분만 건드리므로 전부 $\mathcal{O}(1)$이다.

</div>
<div>

```cpp
class Stack {
public:
    bool isEmpty() const {
        return topOfStack == nullptr;
    }
    void push(int x) {              // 앞에 삽입
        topOfStack = new Node{x, topOfStack};
    }
    int top() const { return topOfStack->data; }
    void pop() {                    // 앞에서 삭제
        Node* oldTop = topOfStack;
        topOfStack = topOfStack->next;
        delete oldTop;
    }
private:
    struct Node {
        int data;  Node* next;
        Node(int d, Node* n = nullptr)
            : data{d}, next{n} {}
    };
    Node* topOfStack = nullptr;
};
```

</div>
</div>

---
layout: prism
heading: 배열 기반 스택 구현
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 또 다른 구현은 링크를 배제한다.
  - `vector`의 `back`, `push_back`, `pop_back` 연산을 활용하므로 구현이 _간단하다_.
  - 각 스택에는 `theArray`와 `topOfStack`이 연관되며, `topOfStack`은 빈 스택에 대해 `-1`이다.
  - 원소 `x`를 `push`하려면 `topOfStack`을 증가시키고 `theArray[topOfStack] = x`로 설정한다.
  - `pop`하려면 반환값을 `theArray[topOfStack]`으로 하고 `topOfStack`을 감소시킨다.

- 이 연산들은 단지 상수 시간일 뿐만 아니라 매우 _빠른_ 상수 시간에 수행된다.
  - 어떤 기계에서는 정수의 `push`와 `pop`이, 자동 증가/감소 주소 지정을 사용하는 레지스터를 이용해 단일 기계 명령으로 이루어질 수 있다.

- 대부분의 현대적 기계가 명령어 집합에 스택 연산을 갖추고 있다는 사실은, 스택이 배열 다음으로 컴퓨터 과학에서 가장 기본적인 자료구조임을 뒷받침한다.

---
layout: prism
heading: "DIY: 배열 기반 스택 (HW_W04_01)"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class ArrayStack {
public:
    void push(int x) { theArray.push_back(x); topOfStack++; }
    void pop()       { theArray.pop_back();   topOfStack--; }
    int  top() const { return theArray[topOfStack]; }
    bool empty() const { return topOfStack == -1; }
private:
    vector<int> theArray;
    int topOfStack = -1;
};

int main() {
    ArrayStack stack;
    stack.push(10);
    stack.push(20);
    stack.push(30);
    cout << "Top element is " << stack.top() << endl;  // 30
    stack.pop();
    cout << "Top element is " << stack.top() << endl;  // 20
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "STL에서의 stack"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- C++는 일반적 [`stack`]{.hl} 클래스를 포함한다.
  - `#include <stack>`
  - `stack<elementType> stackName;`

- `push`, `top`, `pop`은 우리가 설명한 LIFO 모델과 정확히 동일하게 동작한다.

</div>
<div>

```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    s.push(10);
    s.push(20);
    s.push(30);
    cout << s.top() << endl;   // 30
    s.pop();
    cout << s.top() << endl;   // 20
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: "스택 응용 — 기호 균형 맞추기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 컴파일러는 프로그램의 문법 오류를 검사하지만, 종종 하나의 빠진 기호(예: 빠진 중괄호나 주석 시작 기호)가 실제 오류를 짚어내지 못한 채 수백 줄의 진단 메시지를 쏟아내게 만든다.

- 우리는 다른 문자는 모두 무시하고 소괄호·대괄호·중괄호의 _균형_만 확인한다. 이 간단한 알고리즘은 [스택]{.hl}을 사용한다:

<div class="sub-item-enum">

1. 빈 스택을 만든다.
2. 파일의 끝까지 문자를 읽는다.
3. 읽은 문자가 _여는_ 기호이면 스택에 push한다.
4. _닫는_ 기호인데 스택이 비어 있으면 오류를 보고한다.
5. 그렇지 않으면 스택을 pop한다.
6. pop된 기호가 대응하는 여는 기호가 아니면 오류를 보고한다.
7. 파일의 끝에서 스택이 비어 있지 않으면 오류를 보고한다.

</div>

---
layout: prism
heading: "스택 응용 — 후위 표현"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 다음과 같은 계산이 있다고 가정하자:

$$
4.99 * 1.06 + 5.99 + 6.99 * 1.06 =
$$

- 연산 순서에 따라, 위 식을 다음과 같은 수열로 다시 쓸 수 있다:

$$
4.99\ \ 1.06\ *\ \ 5.99\ +\ \ 6.99\ \ 1.06\ *\ \ +
$$

- 이 표기법을 [후위]{.hl}, 또는 [역폴란드 표기법]{.hl}이라고 하며, 스택을 이용해 계산할 수 있다. 연습으로 다음을 계산해 보자:

<div class="sub-item">

$6\ \ 5\ \ 2\ \ 3\ \ +\ \ 8\ \ *\ \ +\ \ 3\ \ +\ \ *$

</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">추상 데이터 타입</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">리스트 ADT</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">스택 ADT</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">큐 ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">큐 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">배열 기반 큐 구현</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">STL에서의 <code>queue</code></span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">큐의 응용</span></p>
  </div>

</div>

---
layout: prism
heading: 큐 모델
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [큐]{.hl} 또한 리스트이다; 다만 삽입은 한쪽 끝에서 이루어지고 삭제는 _다른 쪽 끝_, 즉 [프론트]{.hl}에서 수행된다.
  - [선입선출]{.hl}(FIFO) 특성.

- 기본 연산은 삽입에 해당하는 [`push`]{.hl}와, 가장 먼저 삽입된 원소를 삭제하는 [`pop`]{.hl}이다. 가장 먼저 삽입된 원소는 `pop` 이전에 `front` 연산을 이용해 확인할 수 있다.

<div style="margin-top: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w04-07.svg" class="tikz-fig" style="width: 75%; margin-left: auto; margin-right: auto;" />

---
layout: prism
heading: 배열 기반 큐 구현
---

<style>
.slidev-layout ul > li {
  margin-top: 2.6em;
}
</style>

- 스택과 마찬가지로, 어떤 리스트 구현이든 큐에 사용할 수 있다.

- 스택처럼, 연결 리스트 구현과 배열 구현 모두 모든 연산에 대해 빠른 $\mathcal{O}(1)$ 수행 시간을 제공한다.

- 연결 리스트 구현은 직관적이지만, 배열 구현은 약간 까다롭다.

---
layout: prism
heading: "DIY: 배열 기반 큐 (DIY_W04)"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class ArrayQueue {
public:
    void push(int x) { theArray.push_back(x); rearOfQueue++; }
    void pop()       { frontOfQueue++; }
    int  front() const { return theArray[frontOfQueue]; }
    bool empty() const { return frontOfQueue > rearOfQueue; }
private:
    vector<int> theArray;
    int frontOfQueue = 0;
    int rearOfQueue  = -1;
};

int main() {
    ArrayQueue queue;
    queue.push(10);
    queue.push(20);
    queue.push(30);
    cout << "Front element is " << queue.front() << endl;  // 10
    queue.pop();
    cout << "Front element is " << queue.front() << endl;  // 20
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "STL에서의 queue"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- C++는 일반적 [`queue`]{.hl} 클래스를 포함한다.
  - `#include <queue>`
  - `queue<elementType> queueName;`

- `push`는 뒤에서 삽입하고, `front`와 `pop`은 앞에서 확인하고 제거한다 — 곧 FIFO 모델이다.

</div>
<div>

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    q.push(10);
    q.push(20);
    q.push(30);
    cout << q.front() << endl;   // 10
    q.pop();
    cout << q.front() << endl;   // 20
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: 큐의 응용
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 큐를 사용해 효율적인 수행 시간을 얻는 알고리즘이 많으며, 그중 여럿은 [그래프 이론]{.hl}에서 발견된다. 다음은 큐 사용의 몇 가지 간단한 예이다.

- 작업이 프린터에 제출되면 도착 순서대로 정렬된다 — 본질적으로 프린터로 보내진 작업들은 큐에 놓인다.

- 많은 개인용 컴퓨터 네트워크에서는 디스크가 [파일 서버]{.hl}라 불리는 한 기계에 연결되며, 다른 기계의 사용자들은 _선착순_으로 파일에 접근할 수 있다.

- 실생활의 거의 모든 줄은 (원칙적으로) 큐이다 — 매표소의 줄은 먼저 온 순서대로 서비스되므로 큐이다.

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
