---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 10 (KO)
download: true
info: |
  ## 자료구조 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-10/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">10주차: 그래프와 가중치 그래프</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span class="text-gray-900 dark:text-gray-100">그래프와 가중치 그래프</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">집합과 맵</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">해시 테이블</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">알고리즘 설계 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: "요약: d-힙"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 이진 힙은 매우 단순하기 때문에, 우선순위 큐가 필요한 대부분의 경우에 사용된다.

- 간단한 일반화는 [$d$-힙]{.hl}<sup>$d$-heap</sup>으로, 모든 노드가 $d$개의 자식을 가진다는 점만 제외하면 이진 힙과 완전히 같다(따라서 이진 힙은 $2$-힙이다).

- 오른쪽 그림은 $3$-힙의 예시이다.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-01.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "요약: 좌향 힙"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [좌향 힙 성질]{.hl}<sup>leftist heap property</sup>이란, 모든 노드 $X$에 대해 왼쪽 자식의 널 경로 길이가 오른쪽 자식의 널 경로 길이보다 최소한 크거나 같아야 한다는 것이다.
  - 그림의 노드에 쓰인 값은 각각의 널 경로 길이이며, 왼쪽 트리만 좌향 힙이다.

- 이 성질은 트리가 왼쪽으로 깊어지도록 편향시켜, 트리를 의도적으로 *불균형*하게 만든다.
  - 왼쪽 노드들로 이어지는 긴 경로가 가능하며(또한 병합을 용이하게 하므로 선호되며), 그래서 *좌향*(leftist) 힙이라는 이름이 붙었다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-02.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 그래프와 가중치 그래프
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- [그래프]{.hl}<sup>graph</sup> 자료구조는 실용적으로 유용할 뿐만 아니라 흥미롭기도 하다. 많은 *실생활* 응용에서, 자료구조 선택에 세심하게 주의를 기울이지 않으면 알고리즘이 지나치게 느려지기 때문이다.

- 이번 강의에서는 그래프 자료구조와 몇몇 유용한 알고리즘을 다룬다:

<div class="sub-item-enum">

1. 그래프 문제로 변환될 수 있는 여러 실생활 문제를 소개한다.
2. 흔한 그래프 문제 몇 가지를 푸는 알고리즘을 제시한다.
3. 적절한 자료구조의 선택이 이러한 알고리즘의 수행 시간을 어떻게 획기적으로 줄일 수 있는지 보인다.

</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">그래프</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">정의</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">그래프의 표현</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">최소경로 알고리즘</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">최소 신장 트리</span></p>
  </div>

</div>

---
layout: prism
heading: "정의: 정점과 간선"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 그래프 $G = (V, E)$는 [정점]{.hl}<sup>vertex</sup>의 집합 $V$와 [간선]{.hl}<sup>edge</sup>의 집합 $E$로 이루어진다.
  - 각 간선은 순서쌍 $(v, w)$이며, $v, w \in V$이다. 간선은 때때로 [아크]{.hl}<sup>arc</sup>라고도 불린다.

- 순서쌍에 순서가 있다면, 그 그래프는 [유향]{.hl}<sup>directed</sup>이다.
  - 유향 그래프는 [다이그래프]{.hl}<sup>digraph</sup>라고도 불린다.

- 정점 $w$가 $v$에 [인접]{.hl}<sup>adjacent</sup>하다는 것은 $(v, w) \in E$일 때, 그리고 오직 그때에만 성립한다.
  - 간선 $(v, w)$를 가지는 무향 그래프에서는 $(w, v)$도 성립하므로, $w$는 $v$에 인접하고 $v$는 $w$에 인접한다.

- 때때로 간선은 세 번째 요소를 가지는데, 이를 [가중치]{.hl}<sup>weight</sup> 또는 [비용]{.hl}<sup>cost</sup>이라고 한다.

---
layout: prism
heading: "정의: 경로"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 그래프에서 [경로]{.hl}<sup>path</sup>는 $1 \leq i < N$에 대해 $(w_i, w_{i+1}) \in E$를 만족하는 정점들의 나열 $w_1, w_2, w_3, \ldots, w_N$이다.

- 이러한 경로의 [길이]{.hl}<sup>length</sup>는 경로 상의 간선 수로, $N - 1$과 같다.
  - 정점에서 자기 자신으로 향하는 경로도 허용하며, 이 경로에 간선이 없으면 그 길이는 $0$이다.

- 그래프가 정점에서 자기 자신으로 향하는 간선 $(v, v)$를 가진다면, 경로 $v, v$는 때때로 [루프]{.hl}<sup>loop</sup>라고 불린다.
  - 우리가 다루는 그래프는 일반적으로 루프가 없다.

- [단순 경로]{.hl}<sup>simple path</sup>는 처음과 마지막 정점이 같을 수 있다는 점을 제외하고 모든 정점이 서로 다른 경로이다.

---
layout: prism
heading: "정의: 순환과 연결성"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 유향 그래프에서 [순환]{.hl}<sup>cycle</sup>은 $w_1 = w_N$을 만족하는 길이 $1$ 이상의 경로이며, 그 경로가 단순하면 순환도 *단순*하다고 한다.
  - 무향 그래프에서는 간선이 서로 달라야 한다. 경로 $u, v, u$는 순환으로 치지 않는데, $(u, v)$와 $(v, u)$가 같은 간선이기 때문이다.
  - 유향 그래프에서는 $(u, v)$와 $(v, u)$가 서로 다른 간선이므로, $u, v, u$는 순환이다.

- 유향 그래프가 순환을 가지지 않으면 [비순환]{.hl}<sup>acyclic</sup>이라고 한다. 유향 비순환 그래프는 [DAG]{.hl}로 줄여 부른다.

- 무향 그래프에서 모든 정점으로부터 다른 모든 정점으로 가는 경로가 존재하면 그 그래프는 [연결]{.hl}<sup>connected</sup>되었다고 한다.
  - 이 성질을 가진 유향 그래프는 [강하게 연결]{.hl}<sup>strongly connected</sup>되었다고 한다.
  - 유향 그래프가 강하게 연결되지는 않았지만 그 기저의 무향 그래프가 연결되어 있다면, 그 그래프는 [약하게 연결]{.hl}<sup>weakly connected</sup>되었다고 한다.

- [완전 그래프]{.hl}<sup>complete graph</sup>는 모든 정점 쌍 사이에 간선이 존재하는 그래프이다.

---
layout: prism
heading: "예시: 그래프로 모델링하기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 그래프로 모델링되는 실생활 상황의 예로 [공항 시스템]{.hl}이 있다.
  - 각 공항은 정점이며, 두 공항 사이에 직항편이 있으면 두 정점을 간선으로 연결한다.
  - 간선은 비행의 시간, 거리, 비용을 나타내는 가중치를 가질 수 있다.
  - 방향에 따라 시간이 더 걸리거나 비용이 더 들 수 있으므로, 이 그래프를 *유향*으로 가정하는 것이 합리적이다.

- 우리는 공항 시스템이 [강하게 연결]{.hl}되어 있어서, 어떤 공항에서든 다른 어떤 공항으로도 항상 갈 수 있기를 바란다.
  - 또한 임의의 두 공항 사이의 최선의 항공편을 빠르게 알아내고 싶을 수 있다.

- [교통 흐름]{.hl}도 마찬가지로 그래프로 모델링할 수 있다. 각 교차로는 정점, 각 도로는 간선이며, 간선 비용은 속도 제한이나 용량 등이 된다.
  - 그러면 최단 경로를 묻거나, 병목이 발생할 가능성이 높은 지점을 찾을 수 있다.

---
layout: prism
heading: "HW_W10: 그래프로 모델링되는 실생활 예시"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- 그래프(또는 여러 그래프)로 모델링될 수 있는 실생활 상황의 예를 하나 제시하시오.

- [정점]{.hl}과 [간선]{.hl}을 명확하게 정의해야 합니다.

- 또한 자신의 시스템이 가지는 성질(즉, 유향인지 무향인지, 연결인지, 완전인지)과 실생활 문제(예: 두 공항 사이의 최선의 항공편 찾기)를 제시해야 합니다.

- 설명을 작성하여 LMS에 업로드하시오.
  - 한국어로 작성해도 됩니다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">그래프</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">정의</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">그래프의 표현</span></p>
  </div>

</div>

---
layout: prism
heading: "그래프의 표현: 인접 행렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 유향 그래프를 다룬다(무향 그래프도 비슷한 방식으로 표현한다).

- 그래프를 표현하는 간단한 한 가지 방법은 2차원 배열, 즉 [인접 행렬]{.hl}<sup>adjacency matrix</sup> 표현이다.
  - 각 간선 $(u, v)$에 대해 $A[u][v]$를 `true`로 설정하고, 그렇지 않으면 그 항목은 `false`이다.
  - 간선에 가중치가 있으면 $A[u][v]$를 그 가중치로 설정하고, 존재하지 않는 간선에는 매우 크거나 매우 작은 미리 정해둔 값을 사용한다.

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

<div style="height: 4rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-03.svg" class="tikz-fig" style="width: 90%;" />

</div>
</div>

---
layout: prism
heading: "그래프의 표현: 인접 리스트"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 인접 행렬은 매우 간단하지만 공간 요구량이 $\Theta(|V|^2)$이므로, 그래프에 간선이 적으면 부담이 될 수 있다.
  - 그래프가 [밀집]{.hl}<sup>dense</sup>한 경우, 즉 $|E| = \Theta(|V|^2)$일 때 적절하다.

- 그래프가 [희소]{.hl}<sup>sparse</sup>하다면, [인접 리스트]{.hl}<sup>adjacency list</sup> 표현이 더 나은 해법이다.

- 각 정점에 대해 인접한 모든 정점의 리스트를 유지하며, 공간 요구량은 $\mathcal{O}(|E| + |V|)$로 그래프 크기에 선형이다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-04.svg" class="tikz-fig" style="width: 95%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 인접 리스트 표현"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int N = 5;                       // 정점 1..5
    // 예시 그래프의 유향 간선 (u, v)
    vector<pair<int,int>> edges = {
        {1,2},{1,3}, {2,2},{2,3},{2,4},
        {3,4},{3,5}, {4,1},{4,4}, {5,4}
    };

    vector<vector<int>> adj(N + 1);        // 인접 리스트
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
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">그래프</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">최소경로 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">최소경로 문제</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">비가중치 최소경로</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">다익스트라 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">음의 간선 비용을 가진 그래프</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">최소 신장 트리</span></p>
  </div>

</div>

---
layout: prism
heading: 최소경로 문제
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 다양한 최소경로 문제를 살펴본다. 입력은 [가중치 그래프]{.hl}<sup>weighted graph</sup>로, 각 간선 $(v_i, v_j)$에는 그 간선을 지나는 비용 $c_{i,j}$가 연관되어 있다.

- 경로 $v_1 v_2 \ldots v_N$의 비용은 $\sum_{i=1}^{N-1} c_{i, i+1}$이며, 이를 [가중치 경로 길이]{.hl}<sup>weighted path length</sup>라고 한다.
  - [비가중치 경로 길이]{.hl}<sup>unweighted path length</sup>는 단순히 경로 상의 간선 수, 즉 $N - 1$이다.

<div style="height: 1rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">단일 출발점 최소경로 문제</div>
<div class="theorem-box-body">

입력으로 가중치 그래프 $G = (V, E)$와 특정 정점 $s$가 주어질 때, $s$에서 $G$의 다른 모든 정점으로 가는 최소 가중치 경로를 찾아라.

</div>
</div>

---
layout: prism
heading: "최소경로 문제: 예시"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 오른쪽에서 $v_1$부터 $v_6$까지의 최소 가중치 경로는 비용이 $6$이며, $v_1 \to v_4 \to v_7 \to v_6$을 따라간다.
  - 이 두 정점 사이의 최소 *비가중치* 경로는 $2$이다.

- [비가중치 그래프]{.hl}<sup>unweighted graph</sup>에서는 경로 상의 간선 수에만 관심을 두므로 가중치가 없다.
  - 이는 모든 간선에 가중치 $1$을 부여한, 가중치 문제의 특수한 경우이다.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-05.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 비가중치 최소경로
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 출발점 $s$를 $v_3$으로 정한다고 하자.
  - $s$에서 $v_3$까지의 최소경로는 길이 $0$의 경로이므로 곧바로 표시할 수 있다.
  - 그다음 $s$로부터 거리 $1$에 있는 모든 정점을 찾고, 이런 식으로 계속한다.

- 그래프를 탐색하는 이 전략을 [너비-우선 탐색]{.hl}<sup>breadth-first search</sup>이라고 한다.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-06.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 비가중치 최소경로 (BFS)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    const int N = 7;                       // 정점 v1..v7
    vector<vector<int>> adj(N + 1);
    auto add = [&](int u, int v){ adj[u].push_back(v); };
    add(1,2); add(1,4); add(2,4); add(2,5);
    add(3,1); add(3,6); add(4,3); add(4,5);
    add(4,6); add(4,7); add(5,7); add(7,6);

    int s = 3;                             // 시작 정점 v3
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
heading: "다익스트라 알고리즘: 아이디어"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 그래프에 가중치가 있으면 문제가 언뜻 더 어려워지지만, 비가중치의 경우에서 얻은 아이디어를 재사용한다:

<div class="sub-item-enum">

1. 각 정점을 *known* 또는 *unknown*으로 표기한다.
2. 앞에서처럼 각 정점에 대해 잠정 거리 $d_v$를 유지한다.
3. 이 거리는 *known* 정점만을 중간 경유지로 사용하여 $s$에서 $v$까지 가는 최소경로 길이이다.
4. $d_v$를 바꾸게 만든 마지막 정점 $p_v$를 기록한다.

</div>

- 단일 출발점 최소경로 문제를 푸는 이 일반적인 방법을 [다익스트라 알고리즘]{.hl}<sup>Dijkstra's algorithm</sup>이라 하며, 비가중치 알고리즘처럼 *단계*별로 진행된다.

- 각 단계에서 다익스트라 알고리즘은 모든 *unknown* 정점 중 $d_v$가 가장 작은 정점 $v$를 선택하여 그 최소경로를 *known*으로 선언하고, 이어서 $d_w$ 값들을 갱신한다.

---
layout: prism
heading: "다익스트라 알고리즘: 초기화"
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 1px 12px; line-height: 1.12; }
.slidev-layout table { font-size: 0.9em; }
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 아래 표들은 오른쪽 가중치 그래프에 대한 다익스트라 알고리즘의 과정을 보여준다.
  - $v_1$이 출발점이라고 가정한다.

- 처음에는 모든 정점이 *unknown*(`F`)이며, $d_{v_1} = 0$이고 나머지 거리는 모두 $\infty$이다.

<div style="margin-top: 1.5rem;"></div>

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
<div>

<div style="height: 4rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-07.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "다익스트라 알고리즘: 1~3단계"
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 1px 12px; line-height: 1.12; }
.slidev-layout table { font-size: 0.9em; }
</style>

<div class="grid grid-cols-3 gap-3" style="margin-top: 1rem;">
<div>

$v_1$이 *known*이 된 후:

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

$v_4$가 *known*이 된 후:

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

$v_2$가 *known*이 된 후:

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
heading: "다익스트라 알고리즘: 4~6단계"
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 1px 12px; line-height: 1.12; }
.slidev-layout table { font-size: 0.9em; }
</style>

<div class="grid grid-cols-3 gap-3" style="margin-top: 0.6rem;">
<div>

$v_5$에 이어 $v_3$이 된 후:

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

$v_7$이 *known*이 된 후:

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

$v_6$ 이후 (종료):

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

- 각 단계마다 최솟값을 찾는 데 $\mathcal{O}(|V|)$ 시간이 걸리므로, 알고리즘 전체에서 최솟값을 찾는 데 $\mathcal{O}(|V|^2)$ 시간이 쓰인다.

---
layout: prism
heading: "DIY: 다익스트라 최소경로"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int main() {
    const int N = 7;                       // 정점 v1..v7
    vector<vector<pair<int,int>>> adj(N + 1);   // (이웃, 비용)
    auto add = [&](int u, int v, int c){ adj[u].push_back({v, c}); };
    add(1,2,2); add(1,4,1); add(2,4,3); add(2,5,10);
    add(3,1,4); add(3,6,5); add(4,3,2); add(4,5,2);
    add(4,6,8); add(4,7,4); add(5,7,6); add(7,6,1);

    int s = 1;                             // 시작 정점 v1
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
heading: 음의 간선 비용을 가진 그래프
---

<style>
.slidev-layout ul > li {
  margin-top: 2.6em;
}
</style>

- 그래프에 [음의 간선 비용]{.hl}<sup>negative edge costs</sup>이 있으면 다익스트라 알고리즘은 동작하지 않는다.

- 문제는, 정점 $u$가 일단 *known*으로 선언된 뒤에도 어떤 다른 *unknown* 정점 $v$가 $u$로 되돌아가는, 매우 음의 값을 가진 경로를 제공할 수 있다는 데 있다.

- 그럴듯한 해법은 각 간선 비용에 상수 $\Delta$를 더해 음의 간선을 없앤 뒤, 새 그래프에서 최소경로를 계산하여 그 결과를 원래 그래프에 적용하는 것이다. *이 방법 역시 동작하지 않는데*, 간선이 더 많은 경로에 불이익을 주기 때문이다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">그래프</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">최소경로 알고리즘</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">최소 신장 트리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">최소 신장 트리</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">프림 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">크루스칼 알고리즘</span></p>
  </div>

</div>

---
layout: prism
heading: 최소 신장 트리
---

<style>
.slidev-layout ul > li {
  margin-top: 0.7em;
}
</style>

- 다음 문제는 무향 그래프에서 [최소 신장 트리]{.hl}<sup>minimum spanning tree</sup>를 찾는 것이다.
  - 이 문제는 유향 그래프에서도 의미가 있지만 더 어려워 보인다.

- 비형식적으로, 무향 그래프 $G$의 최소 신장 트리는 그래프의 간선들로 이루어져 $G$의 모든 정점을 가장 적은 총비용으로 연결하는 트리이다.
  - 최소 신장 트리는 $G$가 연결되어 있을 때, 그리고 오직 그때에만 존재한다.
  - 비순환이므로 *트리*이고, 모든 정점을 덮으므로 *신장*이며, 명백한 이유로 *최소*이다.

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-08.svg" class="tikz-fig" style="width: 80%; margin: 0 auto;" />

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-09.svg" class="tikz-fig" style="width: 80%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "프림 알고리즘: 아이디어"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 최소 신장 트리를 계산하는 한 가지 방법은 트리를 연속된 단계에 걸쳐 키워 나가는 것이다.
  - 각 단계에서 하나의 노드를 루트로 잡고, 간선 하나와 그에 연관된 정점 하나를 트리에 추가한다.

- 임의의 시점에 우리는 이미 트리에 포함된 정점 집합을 가지며, 나머지는 아직 포함되지 않았다.

- 알고리즘은 각 단계에서, $u$는 트리 안에 있고 $v$는 트리 밖에 있는 모든 간선 중 비용이 가장 작은 간선 $(u, v)$를 선택하여 추가할 새 정점을 찾는다.

- [프림 알고리즘]{.hl}<sup>Prim's algorithm</sup>은 본질적으로 다익스트라 알고리즘과 동일하다.
  - 각 정점에 대해 $d_v$, $p_v$, 그리고 *known* 여부를 유지한다.
  - $d_v$는 $v$를 *known* 정점에 연결하는 최소 간선의 가중치이고, $p_v$는 $d_v$를 바꾸게 만든 마지막 정점이다.
  - 정점 $v$가 선택되면, $v$에 인접한 각 *unknown* $w$에 대해 $d_w = \min(d_w, c_{w,v})$이다.

---
layout: prism
heading: "프림 알고리즘: 트리 키우기"
---

- $v_1$에서 시작하여, 프림 알고리즘은 트리가 모든 정점을 덮을 때까지 단계마다 정점을 하나씩 추가한다:

<div class="grid grid-cols-3 gap-2" style="margin-top: 1rem;">
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-10.svg" class="tikz-fig" style="width: 100%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-11.svg" class="tikz-fig" style="width: 100%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-12.svg" class="tikz-fig" style="width: 100%;" />
</div>
</div>

<div class="grid grid-cols-3 gap-2" style="margin-top: 0.6rem;">
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-13.svg" class="tikz-fig" style="width: 100%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-14.svg" class="tikz-fig" style="width: 100%;" />
</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w10-15.svg" class="tikz-fig" style="width: 100%;" />
</div>
</div>

---
layout: prism
heading: "크루스칼 알고리즘: 아이디어"
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 1px 12px; line-height: 1.12; }
.slidev-layout table { font-size: 0.9em; }
</style>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 또 다른 탐욕적 전략은, 가중치가 가장 작은 순서대로 간선을 계속 선택하되 순환을 만들지 않는 간선만 받아들이는 것이다.
  - 이것이 [크루스칼 알고리즘]{.hl}<sup>Kruskal's algorithm</sup>이다.

- 형식적으로, 크루스칼 알고리즘은 [포레스트]{.hl}<sup>forest</sup>, 즉 트리들의 모임을 유지한다.
  - 알고리즘이 종료되면 트리는 하나만 남으며, 이것이 최소 신장 트리이다.

- 최악의 경우 수행 시간은 $\mathcal{O}(|E| \log |E|)$이다.

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
heading: "크루스칼 알고리즘: 포레스트 만들기"
---

- 간선을 가중치 순서대로 추가하되 순환을 만드는 간선은 건너뛰며, 하나의 신장 트리만 남을 때까지 진행한다:

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

# ***감사합니다!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
