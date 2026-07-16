---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 11 (KO)
download: true
info: |
  ## 자료구조 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-11/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">11주차: 집합과 맵</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">기초 수학과 C++ 세부 사항</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">알고리즘 분석</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">리스트, 스택, 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">원형 큐와 우선순위 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">트리와 트라이</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">힙</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">그래프와 가중치 그래프</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span class="text-gray-900 dark:text-gray-100">집합과 맵</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">해시 테이블</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">알고리즘 설계 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: "요약: 그래프의 표현"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- 유향 그래프를 가정한다 (무향 그래프도 비슷한 방식으로 표현할 수 있다).

- 간단한 방법 하나는 2차원 배열, 즉 [인접 행렬]{.hl} 표현을 사용하는 것이다.
  - 각 간선 $(u, v)$에 대해 $A[u][v]$를 `true`로 설정하고, 그렇지 않으면 `false`로 둔다.
  - 간선에 가중치가 있다면 $A[u][v]$를 가중치 값으로 설정하고, 존재하지 않는 간선에는 매우 큰 값이나 매우 작은 값을 감시값으로 사용한다.

$$
A=\begin{bmatrix}
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

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-01.svg" class="tikz-fig" style="width: 70%; margin: 0rem auto 0;" />

</div>
</div>

---
layout: prism
heading: "요약: 그래프의 표현"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.2fr 1fr;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 인접 행렬은 극도로 간단하지만 공간 요구량이 $\Theta(|V|^2)$이므로, 간선이 적은 그래프에는 부적합하다.
  - 그래프가 [밀집]{.hl}한 경우, 즉 $|E| = \Theta(|V|^2)$인 경우에만 적절하다.

- 그래프가 [희소]{.hl}하다면 더 나은 방법은 [인접 리스트]{.hl}이다: 각 정점에 대해 인접한 모든 정점의 리스트를 유지한다.
  - 이때 공간 요구량은 $\mathcal{O}(|E| + |V|)$로, 그래프 크기에 선형으로 비례한다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-02.svg" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "요약: 최소경로 문제"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- $v_1$에서 $v_6$로 향하는 최단 가중치 경로의 비용은 $6$이다: $v_1 \to v_4 \to v_7 \to v_6$.
  - 두 정점 사이의 최단 *비가중치* 경로의 길이는 $2$이다.

- 비가중치 그래프에서는 경로 상의 간선 개수만 센다.
  - 이는 모든 간선의 가중치를 $1$로 두는 가중치 최단 경로 문제의 특수한 경우이다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-03.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "요약: 최소 신장 트리"
---

- 다음 문제는 무향 그래프에서 [최소 신장 트리]{.hl}를 찾는 것이다 — 이는 $G$의 모든 정점을 가장 적은 총비용으로 연결하는 그래프 간선들의 트리이다.
  - 이는 $G$가 연결되어 있을 때에만 존재한다.
  - 비순환이므로 *트리*이고, 모든 정점을 덮으므로 *신장*이며, 명백한 이유로 *최소*이다.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-04.svg" class="tikz-fig" style="width: 82%; margin: 0 auto;" />

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-05.svg" class="tikz-fig" style="width: 82%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: 집합과 맵
---

- 리스트, 스택, 큐, 우선순위 큐, 트리, 그래프와 같은 자료구조들은 각각 자료를 담는 데에 있어 그들만의 역량을 가지고 있다.

- 이들은 기본적이고 많은 알고리즘에 충분하지만, 몇몇 발전된 문제들은 이들만으로 쉽게 풀리지 않는다.
  - 예를 들어, 크루스칼 알고리즘에서 [순환]{.hl}을 어떻게 판단할 수 있을까? 간단한 방법 하나는 또 다른 자료구조인 [집합]{.hl}을 사용하는 것이다.

- 또한 [맵]{.hl}을 사용하여 키-값 쌍을 다룰 수 있다.

- 이번 강의에서는 집합과 맵을 다룰 것이다:

<div class="sub-item-enum">

1. 집합과 서로소 집합 자료구조를 소개한다.
2. 서로소 집합의 구현을 보인다.
3. 맵 자료구조를 소개한다.
4. 두 C++ 컨테이너 `set`과 `map`을 소개한다.

</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">집합과 서로소 집합</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">집합</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">동치 관계</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">동적 동치 문제</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">서로소 집합</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">진보된 합집합 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">경로 압축</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">STL에서의 <code>set</code></span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">맵</span></p>
  </div>

</div>

---
layout: prism
heading: 집합
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [집합]{.hl}은 중복을 허용하지 않는 정연한 컨테이너이다.

- 배열과 연결 리스트에서 아이템에 접근하기 위해 사용되는 여러 관용적 방식들은 집합에서도 동작한다.

- 집합의 정의에 따라 몇몇 연산이 달라진다:
  - `printSet`, `find`, `remove` 등은 다른 컨테이너에서와 동일하게 동작한다.
  - `insert`는 먼저 `find`를 수행해야 할 수 있으며, *중복*이 없을 때만 새 원소를 추가한다.

- 추가적인 연산도 고려할 수 있다:
  - `union`은 두 집합을 중복된 원소 없이 병합한다 — 한 가지 방법은 동일한 원소를 `find`로 찾아 각각 `remove`하고 `merge`하는 것이다.
  - `intersect`는 단순히 짝이 되는 원소를 `find`로 찾아 반환한다.

---
layout: prism
heading: 동치 관계
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- 집합 $S$에서 [관계]{.hl} $R$은, 모든 쌍 $(a, b)$, $a, b \in S$에 대해 $a\ R\ b$라는 명제가 참 또는 거짓으로 결정될 때 정의된다. 참이면 $a$가 $b$와 관계되었다고 한다.

- [동치 관계]{.hl}는 세 가지 성질을 만족하는 관계 $R$이다:

<div class="sub-item-enum">

1. *재귀성.* $a\ R\ a$, $\forall a \in S$.
2. *대칭성.* $a\ R\ b$이면 그리고 그럴 때만 $b\ R\ a$.
3. *전이성.* $a\ R\ b$이고 $b\ R\ c$이면 $a\ R\ c$이다.

</div>

- $\leq$ 관계는 동치 관계가 *아니다*: 재귀적이고($a \leq a$) 전이적이지만, $a \leq b$가 $b \leq a$를 내포하지 않으므로 대칭적이지 않다.

- [전기적 연결]{.hl}은 동치 관계*이다* — 재귀적이고(어떤 요소든 자기 자신과 연결됨), 대칭적이며, 전이적이다.

---
layout: prism
heading: "동적 동치 문제: 동치 클래스"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 동치 관계 $\sim$가 주어졌을 때, 자연스러운 문제는 임의의 $a$와 $b$에 대해 $a \sim b$인지를 결정하는 것이다.

- 부울 값의 2차원 배열로 저장하면 상수 시간이 걸리지만, 관계는 보통 명시적이 아니라 *묵시적*으로 정의된다.

- $\sim$이 $\{a_1, a_2, a_3, a_4, a_5\}$ 위에서 정의된다고 하자. $25$개의 쌍이 있으며, 각각 관계되어 있거나 아니다.
  - $a_1 \sim a_2,\ a_3 \sim a_4,\ a_5 \sim a_1,\ a_4 \sim a_2$라는 정보만으로도 *모든* 쌍이 관계되어 있음을 알 수 있으며, 우리는 이를 빠르게 추론하고자 한다.

- $a \in S$의 [동치 클래스]{.hl}는 $a$와 관계된 모든 원소를 포함하는 $S$의 부분집합이다.
  - $S$의 모든 원소는 정확히 하나의 동치 클래스에 속한다.
  - $a \sim b$인지 결정하려면 $a$와 $b$가 같은 동치 클래스에 있는지만 확인하면 된다.

---
layout: prism
heading: "동적 동치 문제: find와 union"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 입력은 처음에 각각 하나의 원소를 가진 $N$개의 집합의 모임이며, 재귀성을 제외한 모든 관계는 거짓이다.

- 각 집합은 서로 다른 원소를 가지므로 $S_i \cap S_j = \emptyset$이며, 이는 집합들을 [서로소]{.hl}로 만든다.

- 허용되는 연산은 두 가지, [`find`]{.hl}와 [`union`]{.hl}이다:
  - 관계 $a \sim b$를 추가하려면, 먼저 $a$와 $b$에 대해 `find`를 수행하여 둘이 같은 동치 클래스에 있는지 확인한다.
  - 그렇지 않다면 `union`을 적용한다.

- 이러한 이유로 이 알고리즘은 흔히 서로소 집합의 [union/find 알고리즘]{.hl}으로 불린다.

---
layout: prism
heading: "동적 동치 문제: 동적과 온라인"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- union/find 알고리즘은 [동적]{.hl}인데, 알고리즘이 수행되는 동안 집합들이 `union`에 의해 변할 수 있기 때문이다.

- 또한 [온라인]{.hl}으로 동작해야 한다: `find`가 수행되면 다음으로 넘어가기 전에 답을 내놓아야 한다.
  - 반면 [오프라인]{.hl} 알고리즘은 `union`과 `find`의 전체 연속을 미리 볼 수 있다.

- 우리는 원소들의 상대적 *값*을 결코 비교하지 않으며, 오직 그들의 위치에 대한 정보만 필요하다.
  - 따라서 원소들이 $0$부터 $N-1$까지 순서대로 번호가 매겨져 있다고 가정하며, 이 번호는 어떤 해싱 방식으로 쉽게 정할 수 있다.

- `find`가 반환하는 집합의 이름은 사실 꽤 임의적이다.

---
layout: prism
heading: "동적 동치 문제: 두 가지 전략"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 동치 문제를 푸는 효율적인 자료구조로 [서로소 집합]{.hl}이 있다. 두 가지 전략이 존재한다:

<div class="sub-item-enum">

1. `find`가 최악의 경우 상수 시간에 수행되도록 한다 — *연결 리스트* 구현.
2. `union`이 최악의 경우 상수 시간에 수행되도록 한다 — *트리* 구현.

</div>

- 빠른 `find`를 위해, 각 원소의 동치 클래스 이름을 배열에 유지한다:
  - 그러면 `find`는 단순한 $\mathcal{O}(1)$ 조회이다.
  - 그러나 `a`가 클래스 $i$, `b`가 클래스 $j$에 있는 `union(a, b)`는 배열을 전부 훑어야 하므로 $\Theta(N)$이 걸린다.
  - 약 $N^2$개의 `find` 연산이 있다면 이 성능은 무난하다.

- 한 가지 아이디어는 같은 동치 클래스에 속한 모든 원소를 연결 리스트로 유지하는 것이다.

---
layout: prism
heading: "서로소 집합: 연결 리스트 (병합)"
---

<div style="margin-top: 0rem;"></div>

- 연결 리스트 구현은 업데이트 시 시간을 절약하는데, 배열 전체를 탐색할 필요가 없기 때문이다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-06.svg" class="tikz-fig" style="width: 58%; margin: 0rem auto 0; display: block;" />

---
layout: prism
heading: "서로소 집합: 연결 리스트 (크기에 따른 합집합)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 각 동치 클래스의 *크기*도 함께 추적하고, `union`을 수행할 때 더 작은 클래스의 이름을 더 큰 클래스의 이름으로 바꾸면, $N - 1$번의 병합에 드는 총 시간은 $\mathcal{O}(N \log N)$이다.

<div class="theorem-box">
<div class="theorem-box-title">크기에 따른 합집합이 도움이 되는 이유</div>
<div class="theorem-box-body">

원소의 클래스 이름이 다시 쓰일 때마다 그 클래스의 크기는 적어도 *두 배*가 된다. 따라서 한 원소는 최대 $\log N$번 이름이 바뀔 수 있으며, 모든 병합에 걸친 전체 이름 변경 작업은 $\mathcal{O}(N \log N)$이 된다.

</div>
</div>

---
layout: prism
heading: "서로소 집합: 트리 (부모 링크 포레스트)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- `find`는 어떤 특정한 이름을 반환할 필요가 없으며, 두 원소에 대한 `find`가 같은 집합에 있을 때에만 같은 답을 반환하면 된다는 것을 상기하자.

- 한 가지 아이디어는 각 집합을 [트리]{.hl}로 표현하는 것이다. 트리 안의 모든 원소는 같은 루트를 가지며, 이 루트가 집합의 이름이 될 수 있기 때문이다.
  - 트리들의 모임을 [포레스트]{.hl}라고 한다.

- 처음에 각 집합은 하나의 원소를 가지며, 트리는 반드시 이진 트리일 필요는 없다.
  - 필요한 정보는 오직 [부모 링크]{.hl}뿐이므로, 트리는 배열에 *묵시적으로* 저장된다.
  - 각 원소 `s[i]`는 원소 $i$의 부모이며, $i$가 루트이면 `s[i] = -1`이다.

---
layout: prism
heading: "서로소 집합: 트리 (초기 포레스트)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 두 집합을 `union`하려면, 한 트리의 루트가 다른 트리의 루트를 가리키도록 하여 두 트리를 병합한다 — 명백히 [상수 시간]{.hl}이다.

- `find(x)`는 `x`가 포함된 트리의 루트를 반환한다.
  - 그 시간은 `x` 노드의 깊이에 비례한다.
  - 깊이가 $N - 1$인 트리도 가능하므로, 최악의 경우 `find`는 $\Theta(N)$이다.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-08.svg" class="tikz-fig" style="width: 100%;" />

<p style="text-align:center; color:#9aa0a6; font-size:0.85rem; margin-top:0.4rem;">하나의 원소로 된 여덟 개의 집합: 모든 루트는 <code>-1</code>을 저장한다.</p>

</div>
</div>

---
layout: prism
heading: "서로소 집합: 트리 (합집합 예시)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `union(4, 5)`, `union(6, 7)`, 그리고 `union(4, 6)`를 차례로 수행한다고 하자. 배열 `s[]`는 각 원소의 부모를 기록하며, `-1`은 루트를 나타낸다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-09.svg" class="tikz-fig" style="width: 72%; margin: 1.2rem auto 0; display: block;" />

---
layout: prism
heading: "진보된 합집합 알고리즘: 크기에 따른 합집합"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 지금까지의 `union`은 임의로 수행되어, 두 번째 트리가 첫 번째 트리의 서브트리가 되도록 했다.

- 간단한 개선법은 항상 더 작은 트리가 더 큰 트리의 서브트리가 되도록 하고, 동점은 임의로 처리하는 것으로, 이를 [크기에 따른 합집합]{.hl}이라 한다.

- `union`을 크기에 따라 수행하면, 어떤 노드의 깊이도 $\log N$을 넘지 않는다:
  - 노드는 깊이 $0$에서 시작한다.
  - `union`으로 인해 깊이가 늘어나면, 그 노드는 이전보다 적어도 *두 배* 큰 트리에 속하게 된다.
  - 따라서 깊이는 최대 $\log N$번 늘어날 수 있다.

- 구현을 위해 각 서로소 집합의 크기를 담는 배열을 하나 더 유지한다. `union` 시 새 크기는 기존 크기들의 합이다.

---
layout: prism
heading: "진보된 합집합 알고리즘: 높이에 따른 합집합"
---

- 깊이가 최대 $\mathcal{O}(\log N)$임을 역시 보장하는 대안은 [높이에 따른 합집합]{.hl}이다: 크기 대신 *높이*를 추적하고, 더 얕은 트리가 더 깊은 트리의 서브트리가 되도록 한다.
  - 높이는 깊이가 같은 두 트리가 결합될 때만 (그때 하나 늘어난다) 증가하며, 이는 크기에 따른 합집합의 사소한 변형이다.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-10.svg" class="tikz-fig" style="width: 100%;" />

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w11-11.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "경로 압축: 동기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 지금까지의 union/find 알고리즘은 대부분의 경우에 무난하지만, 최악의 경우인 $\mathcal{O}(M \log N)$이 꽤 쉽고 자연스럽게 발생할 수 있다.

- `union` 알고리즘에는 더 이상의 개선이 아마 불가능하므로, 자료구조를 새로 뜯어고치지 않고 속도를 높이는 유일한 방법은 `find`에서 무언가 영리한 일을 하는 것이다.

- 이 영리한 연산이 [경로 압축]{.hl}이다:
  - 이는 `find`를 수행하는 *도중에* 이루어지며, `union` 전략과 무관하다.
  - 그 효과는: `x`에서 루트까지의 경로에 있는 *모든* 노드의 부모가 루트로 바뀌는 것이다.

- `union`이 임의로 수행될 때 경로 압축은 특히 좋은데, 깊은 노드가 많고 이들이 루트 가까이로 옮겨지기 때문이다.

---
layout: prism
heading: "경로 압축: 랭크에 따른 합집합"
---

- 경로 압축은 크기에 따른 합집합과는 완벽히 어울리지만, 높이에 따른 합집합과는 *완전히* 어울리지는 않는데, 압축이 트리의 높이를 바꿀 수 있기 때문이다.
  - 저장된 높이는 계산된 높이, 즉 [랭크]{.hl}가 되며, 이 결합된 전략을 [랭크에 따른 합집합]{.hl}이라 한다.

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
heading: "경로 압축: find(14)와 수행 시간"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `find(14)`를 수행하면 `14`에서 루트까지의 경로에 있는 모든 노드가 루트 바로 아래로 옮겨지며, 이후의 모든 `find`를 위해 트리가 평탄화된다.

- [랭크에 따른 합집합]{.hl}과 [경로 압축]{.hl}을 결합하면 $M$개의 연산으로 이루어진 임의의 연속이 *거의 선형* 시간에 수행된다:

$$
\Theta\!\left(M\,\alpha(M, N)\right),
$$

<div class="sub-item">

여기서 $\alpha(M, N)$은 [역 애커만 함수]{.hl}로, 매우 느리게 증가하여 실용적인 모든 $M, N$에 대해 $\alpha(M, N) \leq 4$이다.

</div>

- 더 간단한 분석은 $\mathcal{O}(M \log^{*} N)$의 상한을 준다. 여기서 $\log^{*} N$(*반복 로그*)은 $1$에 도달하기까지 $\log$를 몇 번 적용하는지를 세며, 심지어 $\log^{*}(2^{65536}) = 5$이다.

---
layout: prism
heading: "서로소 집합: 구현"
---

```cpp
class DisjSets {
public:
    explicit DisjSets(int numElements) : s(numElements, -1) {}

    int find(int x) const {              // 압축 없는 find
        if (s[x] < 0) return x;
        else return find(s[x]);
    }
    int find(int x) {                    // 경로 압축을 적용한 find
        if (s[x] < 0) return x;
        else return s[x] = find(s[x]);   // x를 루트 아래로 재연결
    }
    void unionSets(int root1, int root2) {   // 크기에 따른 합집합
        if (s[root2] < s[root1]) {           // root2가 더 크다 (더 작은 음수)
            s[root2] += s[root1];
            s[root1] = root2;                // root2를 새 루트로
        } else {
            s[root1] += s[root2];
            s[root2] = root1;                // root1을 새 루트로
        }
    }
private:
    vector<int> s;   // s[i] = i의 부모, i가 루트이면 -(크기)
};
```

---
layout: prism
heading: "DIY: Union-Find 연결성"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class DisjSets {
public:
    explicit DisjSets(int n) : s(n, -1) {}
    int find(int x) {                        // 크기에 따른 합집합 루트, 또는 -(크기)
        if (s[x] < 0) return x;
        return s[x] = find(s[x]);            // 경로 압축
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
    DisjSets ds(8);                          // 원소 0..7
    ds.unionSets(4, 5);
    ds.unionSets(6, 7);
    ds.unionSets(4, 6);                      // 이제 {4,5,6,7}이 하나의 집합
    ds.unionSets(0, 1);

    cout << "same(5,7)? " << (ds.find(5) == ds.find(7)) << "\n";
    cout << "same(0,4)? " << (ds.find(0) == ds.find(4)) << "\n";

    int components = 0;
    for (int i = 0; i < 8; i++)
        if (ds.find(i) == i) components++;   // 루트는 하나의 컴포넌트를 나타냄
    cout << "number of components = " << components << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "STL에서의 set"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- C++은 일반적인 [`set`]{.hl} 클래스를 제공한다:
  - `#include <set>`
  - `set<elementType> setName;`

- 중복을 삽입해도 크기는 변하지 않으며, 원소가 없으면 `find`는 `end()`를 반환한다.

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
    s.insert(20);               // 중복
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
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">집합과 서로소 집합</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">맵</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">맵</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">STL에서의 <code>map</code></span></p>
  </div>

</div>

---
layout: prism
heading: 맵
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [맵]{.hl}은 [키]{.hl}와 그에 대응하는 [값]{.hl}으로 이루어진 정연한 항목들의 모임을 저장한다.

- 키는 반드시 유일해야 하지만, 여러 키가 같은 값을 가리킬 수 있으므로 값은 유일할 필요가 없다.

- 맵 안의 키들은 논리적으로 정렬된 순서로 유지된다.

- 맵은 *쌍*으로 초기화된 집합처럼 동작하되, 그 비교 함수는 오직 키만 참조한다.

- 보통 자가-조정 이진 탐색 트리가 맵을 구현하는 데 사용된다.
  - C++에서는 [레드-블랙 트리]{.hl}가 `map` STL을 구현하는 데 사용된다.

---
layout: prism
heading: "STL에서의 map"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- C++은 일반적인 [`map`]{.hl} 클래스를 제공한다:
  - `#include <map>`
  - `map<keyType, valueType> mapName;`

- 각 항목은 키-값 `pair`이며, 키에 대한 `find`는 키가 없으면 `end()`를 반환한다.

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
heading: "DIY: map을 이용한 단어 세기"
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
    map<string, int> count;             // 키는 정렬된 순서로 유지됨

    istringstream in(text);
    string word;
    while (in >> word)
        count[word]++;                  // operator[]는 키가 없으면 삽입

    for (const auto& kv : count)        // 정렬된 순서로 키를 순회
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

# ***감사합니다!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
