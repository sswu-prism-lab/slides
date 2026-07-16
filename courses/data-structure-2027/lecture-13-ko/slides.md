---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 13 (KO)
download: true
info: |
  ## 자료구조 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-13/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">13주차: 알고리즘 설계 기법</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">리스트, 스택, 큐</span></p>
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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span class="text-gray-900 dark:text-gray-100">알고리즘 설계 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: "요약: 개별 체이닝"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 어떤 원소가 입력되었을 때 이미 입력되어 있던 원소와 같은 해시값을 갖는다면, [충돌]{.hl}이 발생하며 이를 해소할 필요가 있다.

- 첫 번째 전략인 [개별 체이닝]{.hl}은 같은 해시값을 갖는 모든 원소를 하나의 리스트로 보관하는 방식이다.

- 해시 함수 $hash(x) = x \bmod 10$을 가정하면, 각 버킷은 그곳으로 매핑되는 키들의 연결 리스트를 담는다:

<div class="sub-item">

$0 \to 0, 90 \quad\bullet\quad 1 \to 81 \quad\bullet\quad 2 \to 64 \quad\bullet\quad 4 \to 4, 54 \quad\bullet\quad 6 \to 36 \quad\bullet\quad 9 \to 49$

</div>

---
layout: prism
heading: "요약: 선형 조사"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [선형 조사]{.hl}에서 $f$는 $i$의 선형 함수이며, 보통 $f(i) = i$를 사용한다.
  - 이는 비어 있는 칸을 찾기 위해 칸을 순차적으로 시도하는 것과 같다.

- 표는 키 $\{89, 18, 49, 58, 69\}$를 삽입한 결과를 보여준다.

- 테이블이 비교적 비어 있더라도, 원소가 채워진 칸들의 군집이 형성되기 시작한다.
  - [1차 군집]{.hl}이라 불리는 이 현상은, 군집으로 해싱되는 키가 여러 번의 시도를 거친 뒤 그 군집에 다시 추가됨을 의미한다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w13-01.svg" class="tikz-fig" style="width: 65%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "요약: 이차 조사"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [이차 조사]{.hl}는 선형 조사의 1차 군집 문제를 없애는 충돌 해결 방법이다.

- 여기서 충돌 함수는 제곱식이며, 보통 $f(i) = i^2$를 사용한다.

- 이차 조사가 1차 군집을 없애더라도, 같은 위치로 해싱되는 원소들은 동일한 대체 칸들을 조사하게 된다.
  - 이러한 현상을 [2차 군집]{.hl}이라 한다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w13-02.svg" class="tikz-fig" style="width: 65%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "요약: 더블 해싱"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 우리가 살펴볼 마지막 충돌 해결 방법은 [더블 해싱]{.hl}이다.

- 더블 해싱에서는 보통 $f(i) = i \cdot hash_2(x)$를 선택한다.

- 표는 $hash_2(x) = x \bmod 9$를 채택하여 더블 해싱 전략을 활용한다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w13-03.svg" class="tikz-fig" style="width: 65%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: 알고리즘 디자인 방법론
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 지금까지 우리는 자료구조의 효율적인 *구현*에 관심을 두어 왔다.
  - 어떤 알고리즘이 주어졌을 때, 실제 자료구조가 특정될 필요는 없다.
  - 적절한 자료구조를 선택하여 수행 시간을 최대한 줄이는 것은 프로그래머의 몫이다.

- 이제 우리는 관심을 자료구조의 구현에서 [알고리즘의 디자인]{.hl}으로 옮긴다.
  - 문제를 풀기 위해 사용되는 다섯 가지의 일반적인 알고리즘 유형에 집중한다.
  - 많은 문제들에서는 이들 방법 중 최소한 하나가 작동할 가능성이 높다.

- 각 알고리즘 유형에 대해 일반적인 접근법을 보고, 몇몇 예제를 살펴보며, 적절한 경우 시간 및 공간 복잡도를 논의할 것이다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">탐욕 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">탐욕 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">스케쥴링 문제</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">허프만 코드</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">분할정복</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">동적 프로그래밍</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">무작위 알고리즘</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">백트래킹 알고리즘</span></p>
  </div>

</div>

---
layout: prism
heading: 탐욕 알고리즘
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 우리가 살펴볼 첫 번째 알고리즘 유형은 [탐욕 알고리즘]{.hl}이다.
  - 다익스트라, 프림, 크루스칼 알고리즘은 탐욕적이다. 각 단계에서 미래의 결과를 고려하지 않고 지금 좋아 보이는 결정을 내린다.
  - 이는 어떤 *국소적 최적*이 선택될 수 있음을 의미한다.

- 알고리즘이 종료될 때, 우리는 이 국소적 최적이 [전역적 최적]{.hl}과 같기를 기대한다.
  - 그렇다면 이 알고리즘은 올바르며, 그렇지 않으면 *최적이 아닌* 해를 만들어낸다.
  - 반드시 최적의 답이 요구되지 않을 때에는, 간단한 탐욕 알고리즘이 근사적인 답을 만들어내는 데 쓰이기도 한다.

- 가장 명확한 실생활 예시는 [거스름돈 문제]{.hl}이다.
  - 17,610원을 거슬러 주기 위해 10,000원 지폐 1장, 5,000원 지폐 1장, 1,000원 지폐 2장, 500원 동전 1개, 100원 동전 1개, 10원 동전 1개를 사용한다 — 이는 지폐와 동전의 개수를 최소화하도록 보장된다.

---
layout: prism
heading: "DIY: 탐욕 거스름돈"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> denom = {10000, 5000, 1000, 500, 100, 50, 10}; // 원
    int amount = 17610, pieces = 0;

    cout << "Change for " << amount << " KRW:\n";
    for (int d : denom) {
        int cnt = amount / d;   // 탐욕: 가장 큰 단위를 가능한 한 많이 사용
        if (cnt > 0) {
            cout << "  " << cnt << " x " << d << "\n";
            pieces += cnt;
            amount -= cnt * d;   // 남은 금액을 줄임
        }
    }
    cout << "Total pieces = " << pieces << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "스케쥴링 문제"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 수행 시간 $t_1, t_2, \ldots, t_N$이 알려진 작업 $j_1, j_2, \ldots, j_N$이 주어졌다고 하자.

- 단일 프로세서와 *비선제적* 스케쥴링(시작된 작업은 완료될 때까지 수행됨) 상황에서, 어떤 스케쥴이 평균 종료 시간을 최소화하는가?

- 간단한 선착순 방식은 평균 종료 시간 $25$를 준다.

</div>
<div>

<div style="height: 1.5rem;"></div>

| 작업  | 시간 |
|:-----:|:----:|
| $j_1$ | $15$ |
| $j_2$ | $8$  |
| $j_3$ | $3$  |
| $j_4$ | $10$ |

<div class="sub-item" style="margin-top: 1rem;">

선착순 $j_1 j_2 j_3 j_4$: 종료 시각 $15, 23, 26, 36$; 평균 $= 100/4 = 25$.

</div>

</div>
</div>

---
layout: prism
heading: "스케쥴링 문제 — 최단 작업 우선"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [최단 작업 우선]{.hl}으로 스케쥴링하면 — 순서 $j_3, j_2, j_4, j_1$ — 평균 종료 시간 $17.75$를 얻는다.
  - 종료 시각 $3, 11, 21, 36$; 평균 $= 71/4 = 17.75$.

- 스케쥴을 $j_{i_1}, j_{i_2}, \ldots, j_{i_N}$이라 하자. 첫 작업은 $t_{i_1}$에, 두 번째는 $t_{i_1}+t_{i_2}$에, 세 번째는 $t_{i_1}+t_{i_2}+t_{i_3}$에 종료되며, 이런 식으로 이어진다.

- 총 비용 $C$는:

$$
C = \sum_{k=1}^{N}(N-k+1)\,t_{i_k} = (N+1)\sum_{k=1}^{N} t_{i_k} - \sum_{k=1}^{N} k\cdot t_{i_k}.
$$

<div class="sub-item">

총 비용에 영향을 주는 것은 두 번째 합계뿐이므로, 짧은 작업을 먼저 스케쥴링하여 $C$를 최소화한다.

</div>

---
layout: prism
heading: "스케쥴링 문제 — 다중 프로세서"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- 이 문제를 [다중 프로세서]{.hl}의 경우로 확장할 수 있다.

- 9개의 작업 $j_1, \ldots, j_9$(수행 시간 $3, 5, 6, 10, 11, 14, 15, 18, 20$)과 3개의 프로세서가 주어지면, 최적해는 다시 짧은 작업을 먼저 스케쥴링하며 이를 프로세서들에 라운드 로빈 방식으로 분배한다.
  - 프로세서 1: $j_1, j_4, j_7 \;\to\; 3, 13, 28$
  - 프로세서 2: $j_2, j_5, j_8 \;\to\; 5, 16, 34$
  - 프로세서 3: $j_3, j_6, j_9 \;\to\; 6, 20, 40$

- 이는 모든 프로세서에 걸친 *평균* 종료 시간을 최소화한다.

---
layout: prism
heading: "스케쥴링 문제 — 최종 종료 시간"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 이번에는 대신 우리가 [마지막 작업이 끝나는 시간]{.hl}에만 관심이 있다고 하자.

- 같은 9개의 작업을 다르게 배치하면 최소 최종 종료 시간 $34$를 달성한다.
  - 이 스케쥴이 최소 *평균* 종료 시간을 갖지는 않지만, 전체 작업이 더 일찍 끝난다는 장점이 있다.

- *최소 평균 종료 시간*과 *최소 최종 종료 시간*은 매우 비슷해 보이지만, 이 새로운 문제는 첫 번째 문제보다 [훨씬 어려운]{.hl} 것으로 밝혀졌다.

---
layout: prism
heading: "허프만 코드"
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

- 탐욕 알고리즘의 두 번째 응용은 [파일 압축]{.hl}이다.

- 어떤 파일이 문자 `a`, `e`, `i`, `s`, `t`, 공백(`sp`), 개행(`nl`)만 포함한다고 하자.

- 고정 3비트 코드를 사용하면 이 파일은 $174$비트가 필요하다: $58$개의 문자 $\times\ 3$비트.

</div>
<div>

| 문자 | 코드 | 빈도 | 비트 |
|:----:|:----:|:----:|:----:|
| `a`  | 000  | 10   | 30   |
| `e`  | 001  | 15   | 45   |
| `i`  | 010  | 12   | 36   |
| `s`  | 011  | 3    | 9    |
| `t`  | 100  | 4    | 12   |
| `sp` | 101  | 13   | 39   |
| `nl` | 110  | 1    | 3    |
| **합계** | | | **174** |

</div>
</div>

---
layout: prism
heading: "허프만 코드 — 가변 길이 코드"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 일반적인 전략은 코드 길이를 [글자마다 다르게]{.hl} 하여, 자주 등장하는 문자가 짧은 코드를 갖도록 하는 것이다.
  - 모든 문자가 같은 빈도로 등장한다면 절약될 여지는 거의 없다.

- 우리는 문자가 리프에 위치하는 [트라이]{.hl}로 코드를 표현하며, 루트에서부터의 경로(왼쪽 $= 0$, 오른쪽 $= 1$)가 각 코드를 나타낸다.

- 기존의 고정 길이 전략은 깊이 $3$의 *꽉 찬 균형* 트라이에 해당한다 — 모든 문자가 같은 깊이에 있어 절약이 없다.

---
layout: prism
heading: "허프만 코드 — 접두사 코드"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- 문자를 [리프 노드에만]{.hl} 배치하면, 어떠한 비트 나열도 항상 모호함 없이 해석될 수 있다.
  - 이러한 인코딩을 [접두사 코드]{.hl}라 하며, 어떤 코드도 다른 코드의 접두사가 되지 않는다.

- 드문 문자가 더 깊이 위치하도록 트라이를 재조정하면, 비용 $173$비트의 코드를 얻을 수 있다.
  - 이는 고정 길이의 $174$보다 약간 낫지만, 여전히 최적과는 거리가 멀다.

- 따라서 문제는 모든 문자가 리프에 있는 *총 비용이 최소인 꽉 찬 이진 트라이*를 찾는 것이다.

---
layout: prism
heading: "허프만 코드 — 최적 코드"
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

- 오른쪽 코드는 $146$비트만 필요하다.
  - 이러한 코딩 체계를 흔히 [허프만 코드]{.hl}라 한다.

- 자주 나오는 문자(`e`, `i`, `sp`)는 짧은 2비트 코드를 받고, 드문 문자(`s`, `nl`)는 긴 5비트 코드를 받는다.

</div>
<div>

| 문자 | 코드 | 빈도 | 비트 |
|:----:|:----:|:----:|:----:|
| `a`  | 001   | 10   | 30   |
| `e`  | 01    | 15   | 30   |
| `i`  | 10    | 12   | 24   |
| `s`  | 00000 | 3    | 15   |
| `t`  | 0001  | 4    | 16   |
| `sp` | 11    | 13   | 26   |
| `nl` | 00001 | 1    | 5    |
| **합계** | | | **146** |

</div>
</div>

---
layout: prism
heading: "허프만 알고리즘"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 허프만 알고리즘은 가장 가벼운 두 트리를 반복적으로 병합하여 탐욕적으로 최적 트라이를 만든다:

<div class="sub-item-enum">

1. 트리들의 *포레스트*를 유지한다 — 처음에는 $C$개의 트리이며, $C$는 문자의 개수이다.
2. 트리의 [가중치]{.hl}는 그 리프들의 빈도의 합이다.
3. $C-1$번에 걸쳐, 가중치가 가장 작은 두 트리 $T_1$과 $T_2$를 선택하고(동점이면 임의로 선택) $T_1$과 $T_2$를 서브트리로 갖는 새로운 트리를 만든다.

</div>

- 가중치를 키로 하는 우선순위 큐를 사용하면 각 병합은 $\mathcal{O}(\log C)$가 들며, 전체적으로 $\mathcal{O}(C \log C)$ 알고리즘이 된다.

---
layout: prism
heading: "DIY: 허프만 코드 길이"
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
    // 현재 포레스트에 대한 (가중치, 인덱스)의 최소 힙
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
    for (int k = 0; k < (int)freq.size(); k++) {
        t.push_back({freq[k], k, -1, -1});
        pq.push({freq[k], k});
    }
    while (pq.size() > 1) {                 // C-1번 병합
        auto [w1, a] = pq.top(); pq.pop();
        auto [w2, b] = pq.top(); pq.pop();
        int id = t.size();
        t.push_back({w1 + w2, -1, a, b});   // 새로운 내부 노드
        pq.push({w1 + w2, id});
    }
    // 각 리프의 깊이(코드 길이)를 구하기 위해 트리를 순회
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
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">탐욕 알고리즘</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">분할정복</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">분할정복</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">분할정복 알고리즘의 수행 시간</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">최근접점 문제</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">동적 프로그래밍</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">무작위 알고리즘</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">백트래킹 알고리즘</span></p>
  </div>

</div>

---
layout: prism
heading: 분할정복
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 알고리즘을 설계하기 위한 또 다른 일반적인 기법은 [분할정복]{.hl}이다.

- 분할정복 알고리즘은 두 부분으로 이루어진다:

<div class="sub-item-enum">

1. *분할.* 더 작은 문제들을 재귀적으로 푼다(물론 기본 케이스는 제외).
2. *정복.* 하위 문제들의 해로부터 원래 문제의 해를 구성한다.

</div>

- 우리는 이미 여러 분할정복 알고리즘을 보았다 — 최대 부분합 문제와 트리 순회 전략.
  - [병합정렬]{.hl}과 [퀵정렬]{.hl} 같은 정렬 알고리즘도 분할정복 알고리즘이다.

- 다음으로 이 패러다임의 또 다른 예제인 계산기하 문제를 살펴본다.

---
layout: prism
heading: 분할정복 알고리즘의 수행 시간
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 어떤 분할정복 알고리즘이 원래의 절반 크기인 두 문제를 다루고, 추가로 $\mathcal{O}(N)$의 작업을 수행한다고 하자. 이는 다음 점화식을 낳는다:

$$
T(N) = 2\,T(N/2) + \mathcal{O}(N).
$$

<div class="theorem-box">
<div class="theorem-box-title">정리. 분할정복 알고리즘의 수행 시간 (마스터 정리)</div>
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

- $T(N) = 2T(N/2) + \mathcal{O}(N)$의 경우 $a = b = 2$, $k = 1$이므로 $a = b^k$이고 $T(N) = \mathcal{O}(N \log N)$이다.

---
layout: prism
heading: "최근접점 문제"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [최근접점 문제]{.hl}의 입력은 평면 위 점들의 리스트 $P$이다.

- $p_1 = (x_1, y_1)$, $p_2 = (x_2, y_2)$라면, 두 점 사이의 유클리드 거리는 $\big[(x_1 - x_2)^2 + (y_1 - y_2)^2\big]^{1/2}$이다.

- 우리는 [가장 가까운 점들의 쌍]{.hl}을 찾아야 한다.
  - 두 점이 같은 위치에 있다면 그 쌍이 가장 가까우며, 거리는 0이다.

- $N$개의 점이 있으면 $N(N-1)/2$개의 거리 쌍이 있다.
  - 매우 짧은 프로그램으로 이들을 모두 확인할 수 있지만, $\mathcal{O}(N^2)$ 알고리즘을 감수해야 한다.
  - 이는 단순한 전수 탐색이므로, 더 나은 방법을 기대해 볼 수 있다.

---
layout: prism
heading: "최근접점 문제 — 분할 단계"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 점들이 $x$ 좌표에 따라 정렬되어 있다고 하자.
  - 이는 최종 수행 시간에 $\mathcal{O}(N \log N)$를 더한다.

- 점 집합을 두 절반 $P_L$과 $P_R$로 나누는 가상의 수직선을 긋는다.
  - 점들이 $x$로 정렬되어 있으므로 이는 분명히 간단한 작업이다.

- 최근접점은 둘 다 $P_L$에 있거나, 둘 다 $P_R$에 있거나, 각 절반에 하나씩 있다.
  - 이 거리들을 각각 $d_L$, $d_R$, $d_C$라 하자.

- $d_L$과 $d_R$은 [재귀적으로]{.hl} 계산한 뒤 결합할 수 있다.

---
layout: prism
heading: "최근접점 문제 — 스트립"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 그러면 문제는 $d_C$를 계산하는 것이다. $\delta = \min(d_L, d_R)$이라 하자.
  - 만약 $d_C$가 $\delta$를 개선한다면, $d_C$를 이루는 두 점은 분할선으로부터 $\delta$ 이내에 있어야 하며 — 이 영역을 [스트립]{.hl}이라 한다.

- 스트립 안의 점들이 $y$ 좌표로 정렬되어 있다고 하자.
  - $p_i$와 $p_j$의 $y$ 좌표 차이가 $\delta$보다 크다면, 다음 점 $p_{i+1}$로 넘어가면 된다.

- $y$ 좌표가 $p_i$로부터 $\delta$ 이내인 점들만 $\delta$를 이길 수 있으므로, 비교 횟수가 크게 제한된다.

---
layout: prism
heading: "최근접점 문제 — 수행 시간"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 최악의 경우에도 임의의 점 $p_i$에 대해 최대 [7개]{.hl}의 점 $p_j$만 고려하면 된다.
  - 이러한 점들은 스트립의 왼쪽 절반에 있는 $\delta \times \delta$ 정사각형이나 오른쪽 절반에 있는 정사각형 안에 있어야 한다.
  - 각 $\delta \times \delta$ 정사각형 안의 모든 점들은 적어도 $\delta$만큼 떨어져 있다.

- 각 $p_i$마다 최대 7개의 점만 고려하므로, $\delta$보다 나은 $d_C$를 계산하는 데 $\mathcal{O}(N)$이 든다.

- 따라서 우리는 $\mathcal{O}(N \log N)$ 해답을 가진 것으로 보인다 — 절반 크기의 재귀 호출 두 번과 선형의 결합 작업.
  - 아직 *완전히* 얻은 것은 아니지만, 간단한 변형(매 단계에서 $\mathcal{O}(N \log N)$ 정렬을 피하는 것)으로 이를 달성할 수 있다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">탐욕 알고리즘</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">분할정복</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">동적 프로그래밍</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">동적 프로그래밍</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">재귀 대신 표를 사용하기</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">무작위 알고리즘</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">백트래킹 알고리즘</span></p>
  </div>

</div>

---
layout: prism
heading: 동적 프로그래밍
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- 재귀적인 수식은 어떤 것이든 바로 재귀 알고리즘으로 옮길 수 있지만, 컴파일러가 이를 제대로 처리하지 못해 *비효율적인* 프로그램이 되는 경우가 많다.

- 이러한 경우가 의심될 때에는, 하위 문제들의 답을 [표]{.hl}에 체계적으로 기록하는 [비재귀적인]{.hl} 알고리즘으로 다시 작성하여 컴파일러를 돕는다.

- 이러한 접근법을 활용하는 기법 중 하나가 [동적 프로그래밍]{.hl}이다.

---
layout: prism
heading: 재귀 대신 표를 사용하기
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [피보나치 수]{.hl}를 계산하는 자연스러운 재귀 프로그램은 매우 비효율적이다.
  - 같은 값을 계속해서 다시 계산하기 때문에 [지수]{.hl} 수행 시간을 요구한다.

- $N$번째 피보나치 수를 계산하려면 가장 최근에 계산된 두 값($F_{N-1}$과 $F_{N-2}$)만 필요하다.
  - 이들을 표에 기록하면 $\mathcal{O}(N)$ 알고리즘이 된다.

</div>
<div>

```cpp
// 단순 방식: 지수 시간
int fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}

// 동적 프로그래밍: O(N)
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
heading: "DIY: 동적 프로그래밍 — 피보나치"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

long long calls = 0;                 // 재귀 호출 횟수 세기
long long fib(int n) {               // 단순 방식, 지수 시간
    calls++;
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

long long fibDP(int n) {             // 표 기반, O(N)
    if (n <= 1) return n;
    long long prev = 0, cur = 1;
    for (int i = 2; i <= n; i++) {
        long long next = prev + cur; // 마지막 두 값만 기록
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
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">탐욕 알고리즘</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">분할정복</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">동적 프로그래밍</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">무작위 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">무작위 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">난수발생기</span></p>
    <p style="margin: 1.4rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">백트래킹 알고리즘</span></p>
  </div>

</div>

---
layout: prism
heading: 무작위 알고리즘
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [무작위 알고리즘]{.hl}에서는 알고리즘 수행 중 최소한 한 번, 의사결정을 위해 난수가 사용된다.
  - 수행 시간은 특정 입력뿐만 아니라 발생하는 난수에도 의존한다.

- 무작위 알고리즘의 최악 수행 시간은 흔히 무작위가 아닌 알고리즘의 최악 수행 시간과 같다.
  - 중요한 차이점은, 좋은 무작위 알고리즘에는 *나쁜 입력이 없고* (입력에 대한) 나쁜 난수만 있다는 것이다.

- 무작위 알고리즘을 사용하면 특정 입력은 더 이상 중요하지 않다.
  - 중요한 것은 난수이며, 우리는 모든 가능한 입력이 아니라 모든 가능한 난수에 대해 평균한 [기대 수행 시간]{.hl}을 얻는다.

---
layout: prism
heading: "난수발생기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 이러한 알고리즘은 난수를 필요로 하므로, 이를 생성할 방법이 필요하다.
  - 생성되는 수가 알고리즘에 의존하므로 진정한 무작위일 수 없어, 컴퓨터에서 진정한 무작위성은 사실상 불가능하다.

- 일반적으로는 단지 무작위처럼 보이는 [의사무작위]{.hl} 수를 생성하는 것으로 충분하다.
  - 난수는 알려진 통계적 성질을 많이 가지며, 의사난수는 그 대부분을 만족한다.

- $0$이나 $1$을 무작위로 생성하는 조잡한 방법 하나는 시스템 시계를 확인하는 것이다.
  - 당연히 이 전략은 많은 약점을 가진다.

- 가장 간단한 실용적 방법은 1951년 레머가 처음 제안한 [선형 합동 생성기]{.hl}이다.

---
layout: prism
heading: "난수발생기 — 선형 합동"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- $x_{i+1} = A\,x_i \bmod M$을 만족하는 수 $x_1, x_2, \ldots$가 생성된다.

- [시드]{.hl}인 $x_0$의 값이 주어져야 한다.
  - $x_0 = 0$이면 수열은 무작위와 거리가 멀지만, $A$와 $M$을 잘 고르면 임의의 $1 \le x_0 < M$이 동등하게 유효하다.
  - $M$이 소수라면 $x_i$는 결코 $0$이 되지 않는다.

- $M = 11$, $A = 7$, $x_0 = 1$이면: $7, 5, 2, 3, 10, 4, 6, 9, 8, 1, \ldots$ — 수열은 $M-1 = 10$개의 숫자 이후 반복된다.

</div>
<div>

<div style="height: 2rem;"></div>

```cpp
// 선형 합동 생성기
long long M = 11, A = 7;
long long x = 1;          // 시드 x0

for (int i = 0; i < 10; i++) {
    x = (A * x) % M;      // x_{i+1}
    cout << x << " ";
}
// 7 5 2 3 10 4 6 9 8 1
```

<div class="sub-item" style="margin-top: 1rem;">

$A = 5$와 같은 나쁜 선택은 짧은 주기 $5$를 준다: $5, 3, 4, 9, 1, \ldots$

</div>

</div>
</div>

---
layout: prism
heading: "난수발생기 — 실용적인 선택"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 레머는 [최대 주기]{.hl} 생성기를 위해 31비트 소수 $M = 2^{31} - 1 = 2147483647$과 $A = 48271$을 제안했다.

- 이는 구현하기 간단해 보인다.
  - $x_i$를 $M$으로 나누면 $[0, 1)$ 범위의 무작위 실수를 생성할 수 있다.

- 최근에는 많은 라이브러리가 다음에 기반한 생성기를 사용한다:

$$
x_{i+1} = (A\,x_i + c) \bmod 2^B,
$$

여기서 $B$는 기계의 정수 비트 수와 일치하며, $A$와 $c$는 홀수이다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">탐욕 알고리즘</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">분할정복</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">동적 프로그래밍</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">무작위 알고리즘</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">백트래킹 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">백트래킹 알고리즘</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">징수소 재건 문제</span></p>
  </div>

</div>

---
layout: prism
heading: 백트래킹 알고리즘
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 우리가 살펴볼 마지막 알고리즘 설계 기법은 [백트래킹]{.hl}이다.

- 많은 경우에 백트래킹 알고리즘은 전수 탐색의 영리한 구현에 해당하며, 일반적으로 성능이 좋지 않다.
  - 그러나 항상 그런 것은 아니며, 그렇더라도 부루트-포스 탐색 대비 절약은 상당할 수 있다.

- 실용적인 예시는 새 집에 *가구를 배치하는* 문제이다.
  - 시도해 볼 가능성은 많지만, 실제로 고려되는 것은 보통 몇 가지뿐이다.
  - 배치의 바람직하지 않은 부분집합이 감지되므로, 나쁜 배치는 조기에 버려진다.
  - 한 단계에서 많은 수의 가능성을 제거하는 것을 [가지치기]{.hl}라 한다.

---
layout: prism
heading: "징수소 재건 문제"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- $x$-축 위에 놓인 $N$개의 점 $p_1, p_2, \ldots, p_N$이 주어졌다고 하자.

- $x_i$를 $p_i$의 좌표라 하면, 이 $N$개의 점은 $|x_i - x_j|$ 형태의 (반드시 유일하지는 않은) $N(N-1)/2$개의 거리를 결정한다.

- [징수소 재건 문제]{.hl}는 거리들로부터 점 집합을 재건하는 문제이다.
  - 이는 물리학, 분자생물학 등 여러 분야에서 응용된다.
  - 인수분해가 곱셈보다 어려워 보이듯, 재건은 건설보다 어려워 보인다.

- 다항 시간에 수행됨이 보장되는 알고리즘은 아직 아무도 찾지 못했다.
  - 우리가 제시하는 알고리즘은 일반적으로 $\mathcal{O}(N^2 \log N)$에 수행되지만, 최악의 경우 지수 시간이 걸릴 수 있다.

- $D = \{1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 10\}$이라 하면, $N = 6$임을 알 수 있다.

---
layout: prism
heading: "징수소 재건 — 탐색 시작"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- $x_1 = 0$으로 설정하며 시작한다. $10$이 $D$의 가장 큰 원소이므로 분명히 $x_6 = 10$이다.
  - $D$에서 $10$을 제거한다.

- 남은 가장 큰 거리는 $8$이므로 $x_2 = 2$이거나 $x_5 = 8$이다.
  - 대칭성에 의해 선택은 중요하지 않으므로 $x_5 = 8$로 설정한다.
  - $D$에서 $x_6 - x_5 = 2$와 $x_5 - x_1 = 8$을 제거한다.

- 지금까지의 점: $\{0, 8, 10\}$, $D = \{1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 7\}$.

---
layout: prism
heading: "징수소 재건 — 백트래킹"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 이제 $7$이 $D$에서 가장 큰 값이므로 $x_4 = 7$이거나 $x_2 = 3$이다.
  - 만약 $x_4 = 7$이면, $x_6 - 7 = 3$과 $x_5 - 7 = 1$이 $D$에 있어야 한다.
  - 만약 $x_2 = 3$이면, $3 - x_1 = 3$과 $x_5 - 3 = 5$가 $D$에 있어야 한다.
  - 지침이 없으므로 하나를 시도해 보고 그것이 해답으로 이어지는지 확인한다.

- 첫 번째 선택을 시도하여 $x_4 = 7$로 설정한다. 이제 가장 큰 거리는 $6$이므로 $x_3 = 6$이거나 $x_2 = 4$이다.
  - 만약 $x_3 = 6$이면 $x_4 - x_3 = 1$인데, $1$은 더 이상 $D$에 없으므로 불가능하다.
  - 만약 $x_2 = 4$이면 $x_2 - x_1 = 4$와 $x_5 - x_2 = 4$인데, 역시 불가능하다.

- 이 추론은 어떤 해답도 남기지 않으므로, 우리는 [백트랙]{.hl}한다.

---
layout: prism
heading: "징수소 재건 — 해답 찾기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- $x_4 = 7$이 실패했으므로 $x_2 = 3$을 시도한다.
  - 이 또한 실패한다면, 포기하고 해답이 없음을 보고해야 한다.

- 다시 한번 $x_4 = 6$과 $x_3 = 4$ 중에서 선택한다.
  - $x_3 = 4$는 불가능한 반면, $x_4 = 6$은 가능하다.

- 남은 유일한 선택은 $x_3 = 5$를 할당하는 것이며, 이로써 해답을 얻는다: 점 집합은
$$
\{\,x_1, x_2, x_3, x_4, x_5, x_6\,\} = \{\,0, 3, 5, 6, 8, 10\,\}.
$$

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
