---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 3 (KO)
download: true
info: |
  ## 자료구조 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-3/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">3주차: 알고리즘 분석</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">기초 수학 및 C++ 내용</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span class="text-gray-900 dark:text-gray-100">알고리즘 분석</span></p>
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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">알고리즘 설계 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: "요약: 재귀의 4가지 규칙"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 재귀의 4가지 기본 규칙은 다음과 같다:

<div class="sub-item-enum">

1. *Base cases.* 재귀 없이 풀 수 있는 기본 상태(base case)를 항상 두어야 한다.
2. *Making progress.* 재귀적으로 푸는 경우, 각 재귀 호출은 반드시 기본 상태를 향해 진전해야 한다.
3. *Design rule.* 모든 재귀 호출이 올바르게 동작한다고 가정한다.
4. *Compound interest rule.* 서로 다른 재귀 호출에서 같은 문제 인스턴스를 다시 풀어 작업을 중복해서는 안 된다.

</div>

---
layout: prism
heading: "요약: 일반적 class 문법"
---

<div style="height: 1rem;"></div>

```cpp
class IntCell {
public:
    /* 기본 매개변수, 초기화 리스트,
     * 그리고 explicit 생성자
     */
    explicit IntCell(int initialValue = 0)
        : storedValue{initialValue} {}
    // 상수 멤버 함수
    int read() const { return storedValue; }
    void write(int x) { storedValue = x; }

private:
    int storedValue;
};
```

---
layout: prism
heading: "요약: 클래스 템플릿"
---

<div style="height: 1.5rem;"></div>

```cpp
int main() {
    MemoryCell<int> m1;
    MemoryCell<string> m2{"hello"};

    m1.write(37);
    m2.write(m2.read() + " world");
    cout << m1.read() << endl << m2.read() << endl;

    return 0;
}
```

---
layout: prism
heading: 알고리즘 분석
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [알고리즘]{.hl}<sup>algorithm</sup>은 어떤 문제를 풀기 위해 따라야 하는, 명확하게 표현된 단순한 명령들의 집합이다.

- 어떤 알고리즘이 주어지고 올바른 것으로 결정되면, 그 다음 중요한 단계는 그 알고리즘이 요구하는 *자원* — 시간이나 공간 같은 — 이 얼마나 되는지를 계산하는 것이다.
  - 문제를 풀 수는 있지만 1년이 걸리는 알고리즘은 거의 쓸모가 없다.
  - 수천 기가바이트의 메인 메모리를 요구하는 알고리즘은 (현재로는) 대부분의 기계에서 쓸모없다.

- 이번 강의에서는 몇몇 수학적 배경지식과 알고리즘의 수행 시간을 추정하는 방법을 다룬다:

<div class="sub-item-enum">

1. 프로그램이 요구하는 시간을 추정하는 방법.
2. 며칠 또는 수 년이 걸리는 수행 시간을 순식간으로 줄이는 방법.
3. 부주의한 재귀 사용의 결과.

</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">수학적 배경</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">상대적 성장률과 점근 표기법</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">모델</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">수행 시간 계산</span></p>
  </div>

</div>

---
layout: prism
heading: "수학적 배경: 점근 표기법"
---

- 알고리즘의 자원 사용량을 추정하는 것은 일반적으로 이론적인 문제이므로, 정형화된 프레임워크가 요구된다. 우리는 함수들 사이의 [관계적 순서]{.hl}<sup>relative order</sup>를 수립하기 위해 네 가지 정의를 사용한다.

<div class="theorem-box">
<div class="theorem-box-title">Definition. A relative order among functions</div>
<div class="theorem-box-body">

$T(N) = \mathcal{O}(f(N))$ if there exist positive *constants* $c, n_0$ s.t. $T(N) \leq c\,f(N)$ when $N \geq n_0$.

$T(N) = \Omega(g(N))$ if there exist positive *constants* $c, n_0$ s.t. $T(N) \geq c\,g(N)$ when $N \geq n_0$.

$T(N) = \Theta(h(N))$ if and only if $T(N) = \mathcal{O}(h(N))$ *and* $T(N) = \Omega(h(N))$.

$T(N) = o(p(N))$ if, for *all* positive constants $c$, there exists $n_0$ s.t. $T(N) < c\,p(N)$ when $N > n_0$.

</div>
</div>

---
layout: prism
heading: "빅-오 표기법"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- $T(N) = \mathcal{O}(f(N))$은 $N \geq n_0$일 때 $T(N) \leq c\,f(N)$을 만족하는 양의 상수 $c, n_0$가 존재함을 의미함을 상기하자.

- 작은 $N$에 대해서는 $1{,}000N$이 $N^2$보다 크지만, $N^2$은 *더 빠른 속도*로 성장하여 결국 더 큰 함수가 된다 — 그래서 우리는 이들의 [상대적 성장 비율]{.hl}<sup>relative rates of growth</sup>을 비교한다. 여기서 전환점은 $N = 1{,}000$이다.

- 이 정의는 어떤 점 $n_0$ 이후로 $c \cdot f(N)$이 항상 최소한 $T(N)$만큼 크다는 것을 말한다. 즉, 상수 인자를 무시하면 $f(N)$은 최소한 $T(N)$만큼 크다.
  - 여기서 $T(N) = 1{,}000N$, $f(N) = N^2$, $n_0 = 1{,}000$, $c = 1$이다.

- 따라서 $1{,}000N = \mathcal{O}(N^2)$ (*order $N$-squared* 또는 *big-oh $N$-squared*)이다. 이것이 [빅-오 표기법]{.hl}<sup>Big-Oh notation</sup>이다.

---
layout: prism
heading: "성장률 비교"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 전통적인 부등호 기호를 사용하여 성장률을 비교하면:
  - $T(N) = \mathcal{O}(f(N))$은 $T(N)$의 성장률이 $f(N)$의 성장률보다 *작거나 같음* ($\leq$)을 말한다.
  - $T(N) = \Omega(g(N))$ (*omega*)은 $T(N)$의 성장률이 $g(N)$의 성장률보다 *크거나 같음* ($\geq$)을 말한다.
  - $T(N) = \Theta(h(N))$ (*theta*)은 $T(N)$의 성장률이 $h(N)$의 성장률과 *같음* ($=$)을 말한다.
  - $T(N) = o(p(N))$ (*little-oh*)은 $T(N)$의 성장률이 $p(N)$의 성장률보다 *엄격히 작음* ($<$)을 말한다.

- Little-oh는 $\mathcal{O}(\cdot)$와 다르다: 빅-오는 성장률이 같을 가능성을 *허용*하지만, little-oh는 그렇지 않다.

---
layout: prism
heading: "상계와 하계"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- $T(N) = \mathcal{O}(f(N))$을 증명하기 위해, 우리는 보통 정의를 형식적으로 적용하기보다는 알려진 결과들의 *레퍼토리*를 사용한다. 증명은 단순한 계산이어야 하며, 미적분을 포함하는 경우는 드물다.

- $T(N) = \mathcal{O}(f(N))$일 때, 우리는 $T(N)$이 $f(N)$보다 빠르게 성장하지 않음을 보장한다. 따라서 $f(N)$은 $T(N)$의 [상계]{.hl}<sup>upper bound</sup>이다. 이는 $f(N) = \Omega(T(N))$을 함의하므로, $T(N)$은 $f(N)$의 [하계]{.hl}<sup>lower bound</sup>이다.
  - $N^3$은 $N^2$보다 빠르게 성장하므로, $N^2 = \mathcal{O}(N^3)$ 또는 $N^3 = \Omega(N^2)$이다.
  - $f(N) = N^2$과 $g(N) = 2N^2$은 같은 속도로 성장하므로, $f(N) = \mathcal{O}(g(N))$과 $f(N) = \Omega(g(N))$이 모두 성립한다.

- $g(N) = 2N^2$이라면, $g(N) = \mathcal{O}(N^4)$, $\mathcal{O}(N^3)$, $\mathcal{O}(N^2)$이 모두 기술적으로는 옳지만, $\mathcal{O}(N^2)$이 가장 좋다.
  - $g(N) = \Theta(N^2)$이라고 쓰면 결과가 가능한 한 *촘촘함(tight)*을 나타낸다.

---
layout: prism
heading: "빅-오 규칙"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- 몇 가지 유용한 규칙:

<div class="sub-item-enum">

1. $T_1(N) = \mathcal{O}(f(N))$이고 $T_2(N) = \mathcal{O}(g(N))$이면, $T_1(N) + T_2(N) = \mathcal{O}(\max(f(N), g(N)))$이고 $T_1(N)\cdot T_2(N) = \mathcal{O}(f(N)\cdot g(N))$이다.
2. $T(N)$이 차수 $k$의 다항식이면, $T(N) = \Theta(N^k)$이다.
3. 임의의 상수 $k$에 대해 $\log^k N = \mathcal{O}(N)$이다.

</div>

- 몇 가지 유의할 점:

<div class="sub-item-enum">

1. $\mathcal{O}(\cdot)$ 안에 상수나 낮은 차수의 항을 넣는 것은 매우 좋지 못한 표기이다: $\mathcal{O}(2N^2)$이나 $\mathcal{O}(N^2 + N)$이 아니라 $T(N) = \mathcal{O}(N^2)$으로 쓴다.
2. 우리는 필요하면 *로피탈 정리*를 사용하여 $\lim_{N\to\infty} f(N)/g(N)$을 계산함으로써 상대적 성장률을 항상 결정할 수 있다: $\lim f(N) = \lim g(N) = \infty$이면 $\lim f(N)/g(N) = \lim f'(N)/g'(N)$이다.

</div>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">수학적 배경</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">계산 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">분석해야 하는 것</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">수행 시간 계산</span></p>
  </div>

</div>

---
layout: prism
heading: "계산 모델"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 알고리즘을 정형화된 프레임워크 안에서 분석하려면, [계산 모델]{.hl}이 필요하다. 우리의 모델은 기본적으로 명령들이 *순차적으로* 수행되는 일반적인 컴퓨터이다.

- 이 모델은 단순한 명령들 — 덧셈, 곱셈, 비교, 할당 — 의 표준적인 레퍼토리를 갖지만, 실제 컴퓨터와 달리 무엇을 하든 정확히 *하나의 단위 시간*을 소모한다.

- 합리적인 가정을 위해, 우리는 이 모델이 고정된 크기(예: 32비트)의 정수를 가지며, 행렬 역변환이나 정렬처럼 (명백히 하나의 단위 시간에 할 수 없는) 특별한 연산은 없고, *무한한 메모리*를 갖는다고 가정한다.

- 이 모델은 분명히 약점을 가진다:
  - 실제 세계에서는 모든 연산이 정확히 같은 시간을 소모하지는 않는다.
  - 무한한 메모리를 가정하면, 더 큰 요구량에 대해 더 느린 메모리를 사용할 때 메모리 접근 비용이 더 커질 수 있다는 사실을 무시하게 된다.

---
layout: prism
heading: "분석해야 하는 것"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 일반적으로 분석해야 할 가장 중요한 자원은 [수행 시간]{.hl}<sup>running time</sup>이다.
  - 사용하는 컴파일러나 컴퓨터 같은 요소들이 이에 영향을 주지만, 이들은 우리의 이론적 모델을 벗어난다.
  - 다른 주요 요소는 사용되는 *알고리즘*과 알고리즘에 주어지는 *입력*이며, 보통 입력의 *크기*가 주된 고려 사항이다.

- 우리는 $T_\text{avg}(N)$과 $T_\text{worst}(N)$을 크기 $N$의 입력에 대한 평균 및 최악의 경우 수행 시간으로 정의하며, 따라서 $T_\text{avg}(N) \leq T_\text{worst}(N)$이다.

- 최선의 경우 성능은 좀처럼 관심 대상이 아니다 — 전형적인 동작을 나타내지 않기 때문이다.
  - *평균의 경우* 성능은 흔히 전형적인 동작을 반영한다.
  - *최악의 경우* 성능은 가능한 모든 입력에 대한 *보장*이다.

---
layout: prism
heading: "분석해야 하는 것 — 최악의 경우"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 우리의 분석 범위는 사실 *프로그램*이 아니라 *알고리즘*에 대한 범위이다.
  - 프로그램은 특정 언어로 이루어진 알고리즘의 구현이다.
  - 거의 항상 프로그래밍 언어의 세부 사항은 $\mathcal{O}(\cdot)$ 결과에 영향을 주지 않는다.

- 따로 명시되지 않는 한, 요구되는 양은 [최악의 경우 수행 시간]{.hl}이다. 두 가지 이유가 있다:
  - 이는 평균의 경우 분석이 제공하지 못하는, 특히 나쁜 입력을 포함한 *모든* 입력에 대한 범위를 제공한다.
  - 평균의 경우 범위는 보통 계산하기 훨씬 어려운데, "평균"의 정의 자체가 결과에 영향을 줄 수 있기 때문이다 (*주어진 문제에 대한 평균적인 입력은 무엇인가?*).

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">수학적 배경</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">모델</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">수행 시간 계산</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">간단한 예시</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">일반 규칙</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">최대 부분합 문제</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">수행 시간에서의 로그</span></p>
  </div>

</div>

---
layout: prism
heading: "수행 시간 계산"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 보통 여러 알고리즘 아이디어가 있으며, 나쁜 것들을 일찍 제거하고 싶으므로 대개 분석이 필요하다.

- 분석을 수행하는 능력은 보통 효율적인 알고리즘을 *설계*하는 통찰을 주며, 일반적으로 신중하게 코딩할 가치가 있는 *병목*을 정확히 짚어낸다.

- 분석을 단순화하기 위해, 우리는 특정한 시간 단위가 없다는 관례를 채택하고 선행 상수와 낮은 차수의 항을 버린다 — 본질적으로 [빅-오 수행 시간]{.hl}을 계산하는 것이다.

- 빅-오는 *상계*이므로, 우리는 결코 수행 시간을 과소평가해서는 안 된다.
  - 그 답은 프로그램이 어떤 정해진 시간 안에 종료됨을 보장한다.
  - 프로그램은 더 일찍 멈출 수는 있지만, 결코 더 늦게 멈추지는 않는다.

---
layout: prism
heading: "간단한 예시"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- $\sum_{i=1}^{N} i^3$을 계산하는 코드 조각.

- 선언은 시간을 소모하지 않으며, 할당(라인 3)과 반환(라인 6)은 각각 1 단위를 소모한다.

- 라인 5는 실행마다 4 단위(곱셈 2회, 덧셈 1회, 할당 1회)를 소모하며 $N$번 실행되므로 $4N$ 단위이다.

- 라인 4는 `i = 1`, `i <= n`, `i++`의 비용을 숨기고 있다: $1 + (N{+}1) + N$.

- 총합은 $6N + 4$이므로, 이 함수는 $\mathcal{O}(N)$이다.

</div>
<div>

<div style="height: 3rem;"></div>

```cpp
int sum(int n) {
    int partialSum;
    partialSum = 0;
    for (int i = 1; i <= n; i++)
        partialSum += i * i * i;
    return partialSum;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: 수행 시간 추정"
---

<div style="height: 0.3rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

long long ops = 0;                       // 기본 연산 카운터

long long sum(int n) {
    long long partialSum = 0;   ops += 1;         // 할당 1회
    for (int i = 1; i <= n; i++) {                // 아래는 숨겨진 반복문 비용
        partialSum += (long long)i * i * i;
        ops += 4;                                 // 곱 2회, 합 1회, 할당 1회
    }
    ops += 1 + (n + 1) + n;                       // 초기화 + 검사 + 증가
    ops += 1;                                     // 반환
    return partialSum;
}

int main() {
    for (int n : {10, 100, 1000}) {
        ops = 0;
        long long s = sum(n);
        cout << "N=" << n << "  sum=" << s
             << "  ops=" << ops << "  (6N+4=" << 6 * n + 4 << ")\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "일반 규칙 — 반복문"
---

<div class="theorem-box">
<div class="theorem-box-title">Rule 1 — FOR loops</div>
<div class="theorem-box-body">

The running time of a `for` loop is at most the running time of the statements inside the loop (including tests) times the number of iterations.

</div>
</div>

<div class="theorem-box">
<div class="theorem-box-title">Rule 2 — Nested loops</div>
<div class="theorem-box-body">

The total running time of a statement inside a group of nested loops is the running time of the statement multiplied by the product of the sizes of all the loops.

</div>
</div>

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

다음 코드 조각은 $\mathcal{O}(N^2)$이다:

</div>
<div>

```cpp
for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
        k++;
```

</div>
</div>

---
layout: prism
heading: "일반 규칙 — 연속 문장"
---

<div style="height: 1rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Rule 3 — Consecutive statements</div>
<div class="theorem-box-body">

Consecutive statements just add, which means that the *maximum* is the one that counts.

</div>
</div>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

이 코드 조각은 $\mathcal{O}(N)$ 작업 뒤에 $\mathcal{O}(N^2)$ 작업이 이어지므로, 전체적으로 $\mathcal{O}(N^2)$이다.

</div>
<div>

```cpp
for (i = 0; i < n; i++)
    a[i] = 0;
for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
        a[i] += a[j] + i + j;
```

</div>
</div>

---
layout: prism
heading: "일반 규칙 — If/Else와 재귀"
---

<div class="theorem-box">
<div class="theorem-box-title">Rule 4 — IF/ELSE</div>
<div class="theorem-box-body">

The running time of an `if/else` statement is never more than the running time of the test plus the *larger* of the running times of each branch.

</div>
</div>

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 재귀 함수의 경우, 몇 가지 선택지가 있다.
  - 재귀가 사실상 얇게 가려진 `for` 반복문에 불과하다면, 분석은 자명하다.

- 오른쪽의 함수는 단순한 반복문일 뿐이며 $\mathcal{O}(N)$이다.

</div>
<div>

<div style="height: 2rem;"></div>

```cpp
long factorial(int n) {
    if (n <= 1)
        return 1;
    else
        return n * factorial(n - 1);
}
```

</div>
</div>

---
layout: prism
heading: "일반 규칙 — 부주의한 재귀"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 재귀가 적절하게 사용되면, 이를 단순한 반복문으로 바꾸기는 어렵다.

- 이 프로그램의 수행 시간은 *지수적으로* 증가한다.

- 이는 재귀의 네 번째 규칙([복리 규칙]{.hl}<sup>compound interest rule</sup>)을 위반하여 엄청난 양의 *중복 작업*이 발생하기 때문에 느리다.

</div>
<div>

<div style="height: 3rem;"></div>

```cpp
long fib(int n) {
    if (n <= 1)
        return 1;
    else
        return fib(n - 1) + fib(n - 2);
}
```

</div>
</div>

---
layout: prism
heading: "최대 부분합 문제"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- (음수일 수 있는) 정수 $A_1, A_2, \ldots, A_N$이 주어졌을 때, 부분합 $\sum_{k=i}^{j} A_k$의 최댓값을 구하라.
  - 편의를 위해, 모든 정수가 음수이면 최대 부분합은 $0$으로 한다.
  - *예:* 입력 $-2, 11, -4, 13, -5, -2$에 대해 답은 $20$이다($A_2$부터 $A_4$까지).

- 이 문제는 주로 이를 푸는 알고리즘이 매우 많고, 그 성능이 *극단적으로* 다르기 때문에 흥미롭다.

- 이 문제를 풀기 위한 [네 가지 알고리즘]{.hl}을 다룰 것이다.

---
layout: prism
heading: "최대 부분합 — 해답 1"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

```cpp
int maxSubSum1(const vector<int> &a) {
    int maxSum = 0;
    for (int i = 0; i < a.size(); i++)
        for (int j = i; j < a.size(); j++) {
            int thisSum = 0;
            for (int k = i; k <= j; k++)
                thisSum += a[k];
            if (thisSum > maxSum)
                maxSum = thisSum;
        }
    return maxSum;
}
```

</div>
<div>

<div style="height: 3rem;"></div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 이 알고리즘은 $\mathcal{O}(N^3)$이다.

- 수행 시간은 전적으로 *세 번째* 중첩 `for` 반복문 때문이다.

</div>
</div>

---
layout: prism
heading: "최대 부분합 — 해답 2"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

```cpp
int maxSubSum2(const vector<int> &a) {
    int maxSum = 0;
    for (int i = 0; i < a.size(); i++) {
        int thisSum = 0;
        for (int j = i; j < a.size(); j++) {
            thisSum += a[j];
            if (thisSum > maxSum)
                maxSum = thisSum;
        }
    }
    return maxSum;
}
```

</div>
<div>

<div style="height: 3rem;"></div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 누적되는 `thisSum`을 재사용함으로써, 가장 안쪽 반복문을 제거한다.

- 이 알고리즘은 명백히 $\mathcal{O}(N^2)$이며, 이전보다 분석이 훨씬 간단하다.

</div>
</div>

---
layout: prism
heading: "최대 부분합 — 해답 3 (1/2)"
---

<div style="height: 0.3rem;"></div>

- [분할정복]{.hl}<sup>divide-and-conquer</sup> 전략을 사용할 수 있다: 배열을 반으로 나누면, 최적의 합은 왼쪽에 있거나, 오른쪽에 있거나, 중앙을 *가로지른다*.

```cpp
int maxSumRec(const vector<int> &a, int left, int right) {
    if (left == right)          // 기본 상태
        if (a[left] > 0) return a[left];
        else             return 0;
    int center = (left + right) / 2;
    int maxLeftSum  = maxSumRec(a, left, center);
    int maxRightSum = maxSumRec(a, center + 1, right);

    int maxLeftBorderSum = 0, leftBorderSum = 0;
    for (int i = center; i >= left; i--) {
        leftBorderSum += a[i];
        if (leftBorderSum > maxLeftBorderSum) maxLeftBorderSum = leftBorderSum;
    }
    /* CONTINUE */
```

---
layout: prism
heading: "최대 부분합 — 해답 3 (2/2)"
---

<div style="height: 0.3rem;"></div>

```cpp
    /* CONTINUE */
    int maxRightBorderSum = 0, rightBorderSum = 0;
    for (int j = center + 1; j <= right; j++) {
        rightBorderSum += a[j];
        if (rightBorderSum > maxRightBorderSum) maxRightBorderSum = rightBorderSum;
    }
    return max(maxLeftSum, maxRightSum,
               maxLeftBorderSum + maxRightBorderSum);
}

int maxSubSum3(const vector<int> &a) {   // 드라이버 함수
    return maxSumRec(a, 0, a.size() - 1);
}
```

<div style="height: 0.5rem;"></div>

- 이 알고리즘은 $\mathcal{O}(N \log N)$이다.

---
layout: prism
heading: "최대 부분합 — 해답 4"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

```cpp
int maxSubSum4(const vector<int> &a) {
    int maxSum = 0, thisSum = 0;
    for (int j = 0; j < a.size(); j++) {
        thisSum += a[j];
        if (thisSum > maxSum)
            maxSum = thisSum;
        else if (thisSum < 0)
            thisSum = 0;
    }
    return maxSum;
}
```

</div>
<div>

<div style="height: 2.5rem;"></div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- $\mathcal{O}(N)$ 성능을 갖는, 더 영리한 단일 순회 방법.

- 누적되는 `thisSum`이 음수가 되면 이후의 부분열에 도움이 될 수 없으므로, 이를 $0$으로 *재설정*한다.

</div>
</div>

---
layout: prism
heading: "DIY: 최대 부분합"
---

<div style="height: 0rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxSubSum1(const vector<int> &a) {                 // O(N^3)
    int maxSum = 0;
    for (int i = 0; i < (int)a.size(); i++)
        for (int j = i; j < (int)a.size(); j++) {
            int thisSum = 0;
            for (int k = i; k <= j; k++) thisSum += a[k];
            if (thisSum > maxSum) maxSum = thisSum;
        }
    return maxSum;
}
int maxSubSum2(const vector<int> &a) {                 // O(N^2)
    int maxSum = 0;
    for (int i = 0; i < (int)a.size(); i++) {
        int thisSum = 0;
        for (int j = i; j < (int)a.size(); j++) {
            thisSum += a[j];
            if (thisSum > maxSum) maxSum = thisSum;
        }
    }
    return maxSum;
}
int maxSumRec(const vector<int> &a, int left, int right) {   // O(N log N)
    if (left == right) return a[left] > 0 ? a[left] : 0;
    int center = (left + right) / 2;
    int mL = maxSumRec(a, left, center);
    int mR = maxSumRec(a, center + 1, right);
    int mLB = 0, s = 0;
    for (int i = center; i >= left; i--) { s += a[i]; mLB = max(mLB, s); }
    int mRB = 0; s = 0;
    for (int j = center + 1; j <= right; j++) { s += a[j]; mRB = max(mRB, s); }
    return max({mL, mR, mLB + mRB});
}
int maxSubSum3(const vector<int> &a) { return maxSumRec(a, 0, a.size() - 1); }
int maxSubSum4(const vector<int> &a) {                 // O(N)
    int maxSum = 0, thisSum = 0;
    for (int j = 0; j < (int)a.size(); j++) {
        thisSum += a[j];
        if (thisSum > maxSum) maxSum = thisSum;
        else if (thisSum < 0) thisSum = 0;
    }
    return maxSum;
}

int main() {
    vector<int> a = {-2, 11, -4, 13, -5, -2};
    cout << "Input: -2 11 -4 13 -5 -2\n";
    cout << "Solution 1  O(N^3)      = " << maxSubSum1(a) << "\n";
    cout << "Solution 2  O(N^2)      = " << maxSubSum2(a) << "\n";
    cout << "Solution 3  O(N log N)  = " << maxSubSum3(a) << "\n";
    cout << "Solution 4  O(N)        = " << maxSubSum4(a) << "\n";
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "수행 시간에서의 로그"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 알고리즘 분석에서 가장 혼란스러운 측면은 아마도 [로그]{.hl}일 것이다.

- 우리는 이미 일부 분할정복 알고리즘이 $\mathcal{O}(N \log N)$ 시간에 수행됨을 보았다.

- 그 외에, 로그가 가장 빈번하게 나타나는 경우는 다음 일반 규칙을 따른다:
  - 어떤 알고리즘이 문제의 크기를 일정 *비율*(보통 $1/2$)만큼 줄이는 데 상수 $\mathcal{O}(1)$ 시간이 걸린다면, 그 알고리즘은 $\mathcal{O}(\log N)$이다.

- 오직 특수한 종류의 문제들만 $\mathcal{O}(\log N)$일 수 있다.
  - 입력이 $N$개의 수로 이루어진 리스트라면, 알고리즘은 입력을 *읽는* 데에만 $\Omega(N)$을 소모해야 한다.
  - 따라서 그러한 문제에 대한 $\mathcal{O}(\log N)$ 알고리즘에서는, 보통 입력이 *미리 읽혀진* 상태라고 전제한다.

---
layout: prism
heading: "이진 탐색"
---

<div style="height: 0.5rem;"></div>

<div class="theorem-box">
<div class="theorem-box-title">Binary Search</div>
<div class="theorem-box-body">

Given an integer $X$ and integers $A_0, A_1, \ldots, A_{N-1}$, which are *presorted* and already in memory, find $i$ such that $A_i = X$, or return $i = -1$ if $X$ is not in the input.

</div>
</div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 명백한 해법은 리스트를 왼쪽에서 오른쪽으로 선형 시간에 훑는 것이지만, 리스트가 정렬되어 있다는 사실을 활용하지 못하므로 최선이기 어렵다.

- 더 좋은 전략은 $X$가 *가운데* 원소인지를 확인하는 것이다.
  - 그렇다면 답을 찾은 것이다.
  - $X$가 가운데 원소보다 작으면 왼쪽 부분 배열에 같은 전략을 적용하고, 크면 오른쪽 절반을 살펴본다.

---
layout: prism
heading: "이진 탐색 — 구현"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

```cpp
template <typename Comparable>
int binarySearch(const vector<Comparable> &a,
                 const Comparable &x) {
    int low = 0, high = a.size() - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (a[mid] < x)
            low = mid + 1;
        else if (a[mid] > x)
            high = mid - 1;
        else
            return mid;   // 찾음
    }
    return NOT_FOUND;     // NOT_FOUND는 -1
}
```

</div>
<div>

<div style="height: 3rem;"></div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 각 반복이 탐색 범위를 절반으로 줄이므로, 이진 탐색은 $\mathcal{O}(\log N)$ 시간에 수행된다.

- 반복마다 모든 작업이 $\mathcal{O}(1)$이고, 반복은 최대 $\lceil \log N \rceil$번이다.

</div>
</div>

---
layout: prism
heading: "DIY: 이진 탐색"
---

<div style="height: 0rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int NOT_FOUND = -1;

template <typename Comparable>
int binarySearch(const vector<Comparable> &a, const Comparable &x) {
    int low = 0, high = (int)a.size() - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (a[mid] < x)      low = mid + 1;
        else if (a[mid] > x) high = mid - 1;
        else                 return mid;   // 찾음
    }
    return NOT_FOUND;
}
int main() {
    vector<int> a = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};  // 미리 정렬됨
    for (int x : {23, 91, 2, 17}) {
        int idx = binarySearch(a, x);
        cout << "search " << x << " -> index " << idx;
        if (idx == NOT_FOUND) cout << "  (not found)";
        cout << "\n";
    }
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
