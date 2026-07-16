---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 2 (KO)
download: true
info: |
  ## 자료구조 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-2/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">2주차: 기초 수학과 C++ 문법</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span class="text-gray-900 dark:text-gray-100">기초 수학과 C++ 문법</span></p>
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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">알고리즘 설계 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 기초 수학과 C++ 문법
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 이번 강의에서는 본 과목 전반에 걸쳐 사용되는 이산수학과 프로그래밍 개념을 간단히 리뷰합니다:

  - 이후 과정에 필요한 기본적인 수학적 배경을 요약합니다.

  - [재귀]{.hl}를 간단히 리뷰합니다.

  - 본 과목 전반에서 사용되는 [C++]{.hl}의 중요한 기능 몇 가지를 요약합니다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">수학 리뷰</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">지수와 로그</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">급수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">모듈러 연산</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">증명</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">재귀</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ 클래스</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ 세부 사항</span></p>
  </div>

</div>

---
layout: prism
heading: 지수
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 아래는 반드시 *기억*하거나 *전개*할 수 있어야 하는 [지수]{.hl}에 관한 기본적인 수식들입니다.

$$
\begin{gather*}
X^A X^B = X^{A+B} \qquad \frac{X^A}{X^B} = X^{A-B} \qquad (X^A)^B = X^{AB}\\[0.4em]
X^N + X^N = 2X^N \neq X^{2N} \qquad 2^N + 2^N = 2^{N+1}
\end{gather*}
$$

- 특히 마지막 두 식은 틀리기 쉬우니 유의해 두세요.

---
layout: prism
heading: 로그
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 컴퓨터 과학에서는 따로 특정되지 않는 한 모든 로그의 밑은 [2]{.hl}입니다.

<div class="theorem-box">
<div class="theorem-box-title">로그의 정의</div>
<div class="theorem-box-body">

$X^A = B$ _일 필요충분조건은_ $\log_X B = A$입니다.

</div>
</div>

- 이 정의로부터 몇 가지 편리한 등식을 얻을 수 있습니다:

<div class="sub-item-enum">

1. $\log_A B = \log_C B / \log_C A,\ \forall A, B, C > 0,\ A \neq 1$
2. $\log AB = \log A + \log B \quad(\forall A, B > 0) \qquad \log A/B = \log A - \log B \qquad \log(A^B) = B\log A$
3. $\log X < X\ (\forall X > 0) \qquad \log 1 = 0,\quad \log 2 = 1,\quad \log 1024 = 10$

</div>

---
layout: prism
heading: 기하급수
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 가장 기억하기 쉬운 수식은 다음과 같습니다

$$
\sum_{i=0}^{N} 2^i = 2^{N+1} - 1 \qquad\text{그리고 이와 짝을 이루는}\qquad \sum_{i=0}^{N} A^i = \frac{A^{N+1} - 1}{A - 1}.
$$

- 후자의 경우, $0 < A < 1$이면

$$
\sum_{i=0}^{N} A^i \leq \frac{1}{1 - A},
$$

이고 $N \to \infty$일 때 합은 $1/(1-A)$에 점근합니다. 이것이 [기하급수]{.hl} 공식입니다.

---
layout: prism
heading: 기하급수의 유도
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- $0 < A < 1$일 때 $\sum_{i=0}^{\infty} A^i$를 다음과 같이 유도할 수 있습니다(합을 $S$라 하면):

$$
S = 1 + A + A^2 + A^3 + \cdots \qquad AS = A + A^2 + A^3 + A^4 + \cdots
$$

- 두 식을 서로 빼면(*수렴하는* 급수에서만 유효) 우변의 거의 모든 항이 소거됩니다:

$$
S - AS = 1 \;\Rightarrow\; S = \frac{1}{1 - A}.
$$

- 같은 방식으로 자주 등장하는 합 $\sum_{i=0}^{\infty} (1/2)^i = 2$도 얻을 수 있습니다.

---
layout: prism
heading: 등차급수와 거듭제곱 급수
---

<style>
.slidev-layout ul > li {
  margin-top: 2.8em;
}
</style>

- 또 다른 일반적인 급수는 [등차급수]{.hl}입니다:

$$
\sum_{i=1}^{N} i = \frac{N(N+1)}{2} \approx \frac{N^2}{2}.
$$

- 다음 두 식은 덜 흔하지만 여전히 유용합니다:

$$
\sum_{i=1}^{N} i^2 = \frac{N(N+1)(2N+1)}{6} \approx \frac{N^3}{3} \qquad
\sum_{i=1}^{N} i^k \approx \frac{N^{k+1}}{|k+1|},\ \forall k \neq -1.
$$

---
layout: prism
heading: 조화수
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 다음 식은 다른 분야보다 컴퓨터 과학에서 훨씬 자주 등장합니다:

$$
H_N = \sum_{i=1}^{N} \frac{1}{i} \approx \log_e N,
$$

<div class="sub-item">

여기서 $H_N$을 [조화수]{.hl}, 이 합을 [조화합]{.hl}이라고 합니다.

</div>

- 이 근사의 오차는 [오일러 상수]{.hl} $\gamma \approx 0.57721566$에 수렴합니다.

- 다음은 좀 더 일반적인 두 가지 대수적 처리입니다:

$$
\sum_{i=1}^{N} f(N) = N f(N) \qquad \sum_{i=n_0}^{N} f(i) = \sum_{i=1}^{N} f(i) - \sum_{i=1}^{n_0 - 1} f(i).
$$

---
layout: prism
heading: 모듈러 연산
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- $N$이 $A - B$를 나누어떨어뜨리면, $A$는 모듈로 $N$에 대해 $B$와 [합동]{.hl}이라 하고 $A \equiv B \ (\operatorname{mod}\ N)$로 씁니다.
  - 이는 $A$와 $B$를 $N$으로 나눈 *나머지*가 같다는 뜻으로, 예를 들어 $81 \equiv 61 \equiv 1\ (\operatorname{mod}\ 10)$입니다.

- 등식과 마찬가지로, $A \equiv B\ (\operatorname{mod}\ N)$이면 $A + C \equiv B + C$이고 $AD \equiv BD \ (\operatorname{mod}\ N)$입니다.

- $N$이 [소수]{.hl}일 때 세 가지 중요한 정리가 성립합니다:

<div class="sub-item-enum">

1. $ab \equiv 0\ (\operatorname{mod}\ N)$ *일 필요충분조건은* $a \equiv 0$ 또는 $b \equiv 0\ (\operatorname{mod}\ N)$입니다.
2. $ax \equiv 1\ (\operatorname{mod}\ N)$은 모든 $0 < a < N$에 대해 유일한 해를 가지며, 그 해가 [곱셈에 대한 역원]{.hl}입니다.
3. $x^2 \equiv a\ (\operatorname{mod}\ N)$은 모든 $0 < a < N$에 대해 두 개의 해를 갖거나, 아니면 해가 없습니다.

</div>

---
layout: prism
heading: 반례에 의한 증명
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 자료구조 분석에서 명제를 증명하는 가장 흔한 두 가지 방법은 [귀납법]{.hl}과 [귀류법]{.hl}입니다.

- 어떤 정리가 *거짓*임을 보이는 가장 좋은 방법은 [반례를 제시하는 것]{.hl}입니다.

<div class="theorem-box">
<div class="theorem-box-title">정리. 명제 $F_k \leq k^2$은 거짓입니다.</div>
<div class="theorem-box-body">

이를 증명하는 가장 쉬운 방법은 $F_{13} = 233 > 13^2 = 169$을 계산하는 것입니다.

</div>
</div>

---
layout: prism
heading: 귀납법
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [귀납법에 의한 증명]{.hl}은 두 개의 표준적인 부분으로 이루어집니다:
  - *기초 경우* — 정리가 몇몇 작은 값에 대해 성립함을 확립하는 것으로, 보통 자명합니다.
  - *귀납적 가설* — 어떤 한계 $k$까지 정리가 성립한다고 가정한 뒤, $k+1$에 대해서도 성립함을 보이는 것입니다.

<div class="theorem-box">
<div class="theorem-box-title">정리. 피보나치 수는 $F_i < (5/3)^i$를 만족합니다.</div>
<div class="theorem-box-body">

$F_1 = 1 < 5/3$이고 $F_2 = 1 < 25/9$입니다. 그러면

$$
F_{k+1} = F_k + F_{k-1} < (5/3)^k + (5/3)^{k-1} < (24/25)(5/3)^{k+1} < (5/3)^{k+1}.
$$

</div>
</div>

---
layout: prism
heading: 귀류법
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [귀류법에 의한 증명]{.hl}은 정리가 거짓이라고 가정하고, 이 가정이 이미 알려진 어떤 성질을 거짓으로 만든다는 것을 보임으로써 그 가정이 틀렸음을 밝히는 방법입니다.

<div class="theorem-box">
<div class="theorem-box-title">정리. 소수는 무한히 많습니다.</div>
<div class="theorem-box-body">

정리가 거짓이라고 가정하면, 가장 큰 소수 $P_k$가 존재합니다. $P_1, P_2, \ldots, P_k$를 순서대로 나열한 모든 소수라 하고, $N = P_1 P_2 \cdots P_k + 1$을 생각합니다. 그러면 $N > P_k$이므로 가정에 따라 $N$은 소수가 아닙니다. 그러나 $P_1, \ldots, P_k$ 중 어느 것도 $N$을 정확히 나누지 못합니다(항상 나머지 $1$이 남습니다) — 이는 모든 수가 소수이거나 소수들의 곱이라는 사실에 모순입니다. 따라서 정리는 참입니다.

</div>
</div>

---
layout: prism
heading: 재귀에 대한 간단한 소개
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 대부분의 익숙한 함수는 간단한 수식을 갖지만, 어떤 함수는 덜 통상적인 방식으로 정의됩니다.
  - 음이 아닌 정수에서 $f(0) = 0$과 $f(x) = 2 f(x-1) + x^2$으로 $f$를 정의합니다.

- 자기 자신을 이용해 정의된 함수를 [재귀적]{.hl}이라 합니다. C++는 (많은 현대 언어처럼) 재귀 함수를 허용합니다.

</div>

<div>

<div style="height: 5rem;"></div>

```cpp
int f(int x) {
    if (x == 0)   // 기초 경우
        return 0;
    else          // 재귀 호출
        return 2 * f(x - 1) + x * x;
}
```

</div>
</div>

---
layout: prism
heading: 재귀 — 흔한 함정
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 컴퓨터는 대기 중인 재귀 호출과 그 변수들에 대한 관리를 자동으로 처리합니다.
  - 호출은 기초 경우에 도달할 때까지 계속됩니다 — `f(-1)`을 평가하면 `f(-2)`, `f(-3)`, … 을 호출하며 결코 끝나지 않습니다.

- 좀 더 미묘한 오류: 이 코드는 `bad(1)`이 실제로 무엇인지 전혀 알려주지 않습니다.

</div>
<div>

<div style="height: 5rem;"></div>

```cpp
int bad(int n) {
    if (n == 0)   // 기초 경우처럼 보임
        return 0;
    else          // bad(1)을 추정할 수 없음
        return bad(n / 3 + 1) + n - 1;
}
```

</div>
</div>

---
layout: prism
heading: 재귀 — 숫자 출력
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 이로부터 재귀의 처음 두 가지 기본 규칙을 얻습니다:
  - 항상 재귀 없이 풀 수 있는 *기초 경우*를 두어야 합니다.
  - 모든 재귀 호출은 기초 경우를 향해 *진전*해야 합니다.

- `printDigit`로 한 자리 숫자만 출력할 수 있다고 가정합시다. 재귀는 깔끔한 해법을 제공합니다.

</div>
<div>

<div style="height: 5rem;"></div>

```cpp
void printOut(int n) { // print nonnegative n
    if (n >= 10)
        printOut(n / 10);
    printDigit(n % 10);
}
```

</div>
</div>

---
layout: prism
heading: 재귀와 귀납
---

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- 앞의 숫자 출력 프로그램이 옳음을 귀납법으로 증명할 수 있습니다.

<div class="theorem-box">
<div class="theorem-box-title">정리. 재귀적 숫자 출력 알고리즘은 $n \geq 0$에 대해 옳습니다.</div>
<div class="theorem-box-body">

$n$이 한 자리 숫자이면 프로그램은 단지 `printDigit`을 호출하므로 자명하게 옳습니다. `printOut`이 $k$자리 이하의 모든 수에 대해 동작한다고 가정합시다. $(k+1)$자리 수는 첫 $k$자리 뒤에 마지막 자리를 붙인 것입니다. 첫 $k$자리는 정확히 $\lfloor n/10 \rfloor$이며 귀납적 가설에 의해 올바르게 출력되고, 마지막 자리는 $n \bmod 10$입니다. 따라서 모든 수가 올바르게 출력됩니다.

</div>
</div>

- 재귀 프로그램을 설계할 때, 기초 경우로 가는 경로 위의 더 작은 모든 사례는 옳다고 *가정*할 수 있습니다.

---
layout: prism
heading: 재귀의 네 가지 규칙
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 재귀 프로그램은 더 작은 문제들의 해를 조합하기만 하면 됩니다 — 이것이 *세 번째* 규칙입니다: 모든 재귀 호출이 동작한다고 가정합니다.

- 재귀의 주된 비용은 보이지 않는 관리 작업이니, 단순한 `for` 루프의 대체물로 사용하지 마십시오.

- 재귀의 네 가지 기본 규칙:

<div class="sub-item-enum">

1. *기초 경우.* 항상 재귀 없이 풀 수 있는 기초 경우를 둡니다.
2. *진전.* 재귀 호출은 기초 경우를 향해 진전해야 합니다.
3. *설계 규칙.* 모든 재귀 호출이 동작한다고 가정합니다.
4. *복리 규칙.* 같은 사례를 별개의 재귀 호출에서 풀어 작업을 중복하지 마십시오.

</div>

---
layout: prism
heading: "DIY: 재귀 추적하기"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// f(0) = 0,  f(x) = 2 f(x-1) + x^2
int f(int x) {
    if (x == 0) return 0;         // 기초 경우
    return 2 * f(x - 1) + x * x;  // 재귀 호출
}

void printDigit(int d) { cout << d; }   // 우리가 가진 유일한 출력 루틴

void printOut(int n) {                  // 음이 아닌 정수를 출력
    if (n >= 10) printOut(n / 10);
    printDigit(n % 10);
}

int main() {
    for (int x = 0; x <= 5; x++)
        cout << "f(" << x << ") = " << f(x) << "\n";
    cout << "printOut(31415) -> ";
    printOut(31415);
    cout << endl;
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
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">수학 리뷰</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">C++ 클래스</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">기본 <code>class</code> 문법</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">추가 생성자 문법과 접근자</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>vector</code>와 <code>string</code></span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ 세부 사항</span></p>
  </div>

</div>

---
layout: prism
heading: "기본 class 문법"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 우리의 모든 자료구조는 데이터를 저장하고 그 집합을 조작하는 함수를 제공하는 [객체]{.hl}가 됩니다. C++에서는 이를 [클래스]{.hl}로 구현합니다.

- 클래스는 데이터 또는 함수인 [멤버]{.hl}들로 이루어집니다.
  - 함수는 [멤버 함수]{.hl}(흔히 [메소드]{.hl}라고 함)입니다.
  - 각 클래스의 인스턴스는 [객체]{.hl}이며, `static`으로 선언되지 않는 한 클래스에 지정된 데이터 요소들을 담습니다.

- `IntCell` 클래스를 구현할 것입니다: 하나의 데이터 멤버 `storedValue`를 가지며, `read`, `write`와 두 개의 생성자로 이루어진 네 개의 메소드를 갖습니다.

---
layout: prism
heading: "기본 class 문법 — IntCell"
---

```cpp
class IntCell {                 // Simulating an integer memory cell
public:
    IntCell() {                 // Constructor
        storedValue = 0;
    }
    IntCell(int initialValue) { // Constructor with parameter
        storedValue = initialValue;
    }
    int read() {                // return the stored value
        return storedValue;
    }
    void write(int x) {         // change the stored value to x
        storedValue = x;
    }

private:
    int storedValue;
};
```

---
layout: prism
heading: "기본 class 문법 — 접근성"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `public`과 `private` 라벨은 클래스 멤버의 접근성을 결정합니다.
  - `public` 멤버는 어떤 클래스의 어떤 메소드에서도 접근할 수 있습니다.
  - `private` 멤버는 자기 클래스의 메소드에서만 접근할 수 있습니다.

- 일반적으로 데이터 멤버는 `private`, 범용 메소드는 `public`으로 두어 내부 세부 사항으로의 접근을 제한하는데, 이것이 [정보 은닉]{.hl}입니다.

- 두 [생성자]{.hl}는 클래스의 인스턴스가 어떻게 *생성*되는지를 기술합니다.

---
layout: prism
heading: 추가 생성자 문법과 접근자
---

<div style="height: 3rem;"></div>

```cpp
class IntCell {
public:
    /* default parameter, initialization list,
     * and explicit constructor
     */
    explicit IntCell(int initialValue = 0)
        : storedValue{initialValue} {}
    // constant member function
    int read() const { return storedValue; }
    void write(int x) { storedValue = x; }

private:
    int storedValue;
};
```

---
layout: prism
heading: "생성자: 기본값, 리스트, explicit"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- [기본 변수]{.hl} `0`은 인수가 주어지지 않을 때 `0`이 사용됨을 의미합니다 — 사실상 하나로 두 개의 생성자를 만든 셈입니다.

- [초기화 리스트]{.hl} `: storedValue{initialValue}`는 데이터 멤버를 직접 초기화합니다.

- 이 생성자는 [explicit]{.hl}입니다: 보이지 않는 형변환을 막기 위해 모든 단일 인수 생성자를 `explicit`로 지정합니다.

- 객체의 상태를 살피기만 하고 바꾸지 않는 메소드는 [접근자]{.hl}, 바꾸는 메소드는 [설정자]{.hl}입니다. 여기서 `read`는 접근자이므로 [상수 멤버 함수]{.hl}(`const`)입니다.

---
layout: prism
heading: "vector와 string"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.1em;
}
</style>

- C++ 표준 라이브러리는 유용한 두 클래스 [`vector`]{.hl}와 [`string`]{.hl}을 정의합니다.

- `vector`는 다루기 까다로운 C++ 내장 배열을 대체하기 위한 것입니다.

<div style="height: 2rem;"></div>

```cpp
// int squares[] = {1, 4, 9, 16, 25, 36, 49, 64, 81};
vector<int> squares = {1, 4, 9, 16, 25, 36, 49, 64, 81};
```

- `string`은 모든 관계 연산자와 상등 연산자(`str1 == str2`는 값이 같을 때 `true`)를 지원하며, 문자열 길이를 반환하는 `length` 메소드를 제공합니다.

---
layout: prism
heading: "vector와 string — 반복"
---

<div class="grid grid-cols-3 gap-3" style="margin-top: 0.6rem;">
<div>

`[]`로 인덱싱:

```cpp
int sum = 0;
for (int i = 0;
     i < squares.size();
     i++)
    sum += squares[i];
```

</div>
<div>

범위 `for`:

```cpp
int sum = 0;
for (int x : squares)
    sum += x;
```

</div>
<div>

`auto` 사용:

```cpp
int sum = 0;
for (auto x : squares)
    sum += x;
```

</div>
</div>

<div style="margin-top: 1rem;"></div>

- [범위 `for`]{.hl} 문법은 원소를 직접 순회하며, [`auto`]{.hl}는 컴파일러가 적절한 자료형을 자동으로 추론하게 합니다.

---
layout: prism
heading: "DIY: IntCell과 vector"
---

<div style="height: 0.3rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class IntCell {
public:
    explicit IntCell(int initialValue = 0) : storedValue{initialValue} {}
    int read() const { return storedValue; }
    void write(int x) { storedValue = x; }
private:
    int storedValue;
};

int main() {
    IntCell c;                       // default value 0
    c.write(5);
    cout << "IntCell after write(5): " << c.read() << "\n";

    vector<int> squares = {1, 4, 9, 16, 25, 36, 49, 64, 81};
    int sum = 0;
    for (auto x : squares) sum += x; // range-based for + auto
    cout << "sum of squares = " << sum << endl;
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
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">수학 리뷰</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ 클래스</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">C++ 세부 사항</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">포인터</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Lvalue, Rvalue, 참조</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">The Big-Five</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">템플릿</span></p>
  </div>

</div>

---
layout: prism
heading: 포인터
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [포인터 변수]{.hl}는 다른 객체가 존재하는 *주소*를 저장합니다 — 많은 자료구조의 근본 메커니즘입니다.

- 이 코드는 `IntCell`을 동적으로 할당합니다.

- [address-of 연산자]{.hl} `&`는 객체가 존재하는 메모리 위치를 반환합니다.

</div>
<div>

```cpp
int main() {
    IntCell* m;  // m is a pointer

    m = new IntCell{0};  // dynamic allocation
    m->write(5);
    cout << "Cell contents: "
         << m->read() << endl;

    delete m;  // free the memory
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: Lvalue, Rvalue, 참조
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- [lvalue]{.hl}는 임시가 아닌 객체를 가리킵니다.

- [rvalue]{.hl}는 임시 객체, 또는 어떤 객체와도 연관되지 않은 값(리터럴 등)을 가리킵니다.

</div>
<div>

```cpp
vector<string> arr(3);
const int x = 2;
int y;
int z = x + y;
string str = "foo";
vector<string>* ptr = &arr;
```

</div>
</div>

- `arr`, `str`, `arr[x]`, `&x`, `y`, `z`, `ptr`, `*ptr`, `(*ptr)[x]`는 모두 [lvalue]{.hl}입니다.
- `2`, `"foo"`, `x + y`, `str.substr(0, 1)`은 모두 [rvalue]{.hl}입니다.

---
layout: prism
heading: Lvalue 참조
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [lvalue 참조]{.hl}는 자료형 뒤에 `&`를 붙여 선언하며, 참조하는 객체의 동의어 — 또 다른 이름 — 가 됩니다.

- lvalue 참조는 임시(rvalue)에 바인딩할 수 없으므로 마지막 세 줄은 컴파일 오류입니다.

</div>
<div>

```cpp
string str = "hell";
string& rstr = str;  // another name for str
rstr += "o";         // changes str to "hello"
bool cond = (&str == &rstr);  // true

string& bad1 = "hello";          // error
string& bad2 = str + "";         // error
string& sub  = str.substr(0, 4); // error
```

</div>
</div>

---
layout: prism
heading: Rvalue 참조
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [rvalue 참조]{.hl}는 자료형 뒤에 `&&`를 붙여 선언합니다.

- lvalue 참조와 같은 특성을 갖지만, lvalue 참조와 달리 rvalue(임시)에도 바인딩할 수 있습니다.

- 따라서 이제 세 선언 모두 합법입니다.

</div>
<div>

<div style="height: 4rem;"></div>

```cpp
string str = "hell";

string&& bad1 = "hello";          // legal
string&& bad2 = str + "";         // legal
string&& sub  = str.substr(0, 4); // legal
```

</div>
</div>

---
layout: prism
heading: The Big-Five
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- C++ 클래스에는 기본적으로 이미 작성된 *다섯* 개의 특수 함수가 딸려 옵니다: [소멸자]{.hl}, [복사 생성자]{.hl}, [이동 생성자]{.hl}, [복사 할당 연산자]{.hl}, [이동 할당 연산자]{.hl}.

- [소멸자]{.hl}는 객체가 범위를 벗어나거나 `delete`될 때마다 호출됩니다.

- 두 개의 특수 생성자는 같은 자료형의 다른 객체와 동일한 상태로 초기화된 새 객체를 만듭니다:
  - 원본이 lvalue이면 [복사 생성자]{.hl}, rvalue(어차피 곧 소멸될 임시)이면 [이동 생성자]{.hl}를 사용합니다.

---
layout: prism
heading: The Big-Five — 할당
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 할당 연산자는 이미 생성된 두 객체에 `=`가 적용될 때 호출됩니다.

- `lhs = rhs`는 `rhs`의 상태를 `lhs`로 복사합니다:
  - `rhs`가 lvalue이면 [복사 할당 연산자]{.hl}를 통해,
  - `rhs`가 rvalue이면 [이동 할당 연산자]{.hl}를 통해 이루어집니다.

</div>
<div>

<div style="height: 4rem;"></div>

```cpp
// signatures for IntCell
~IntCell();                    // destructor
IntCell(const IntCell& rhs);   // copy ctor
IntCell(IntCell&& rhs);        // move ctor
IntCell& operator=
    (const IntCell& rhs);      // copy assign
IntCell& operator=
    (IntCell&& rhs);           // move assign
```

</div>
</div>

---
layout: prism
heading: 함수 템플릿
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- *자료형-독립적*인 알고리즘의 경우, 자료형마다 다시 코딩하기보다 코드를 한 번만 작성하는 편이 좋습니다.
  - 이러한 [범용 알고리즘]{.hl}은 C++에서 [템플릿]{.hl}으로 작성합니다.

- [함수 템플릿]{.hl}은 실제 함수가 아니라 함수를 위한 *패턴*입니다.

</div>
<div>

<div style="height: 3rem;"></div>

```cpp
template <typename Comparable>
const Comparable& findMax(
        const vector<Comparable>& a) {
    int maxIndex = 0;
    for (int i = 1; i < a.size(); i++)
        if (a[maxIndex] < a[i])
            maxIndex = i;
    return a[maxIndex];
}
```

</div>
</div>

---
layout: prism
heading: 함수 템플릿 — 인스턴스화
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 함수 템플릿은 필요에 따라 자동으로 확장되며, 각 확장은 코드를 생성하는데 이를 [코드 팽창]{.hl}이라 합니다.

- `findMax(v4)`는 `IntCell`에 `operator<`가 정의되어 있지 않아 실패합니다.

</div>
<div>

```cpp
int main() {
    vector<int> v1(37);
    vector<double> v2(40);
    vector<string> v3(80);
    vector<IntCell> v4(75);
    // Assume the vectors are filled.
    cout << findMax(v1) << endl; // int
    cout << findMax(v2) << endl; // double
    cout << findMax(v3) << endl; // string
    cout << findMax(v4) << endl; // error!
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: 클래스 템플릿
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [클래스 템플릿]{.hl}은 함수 템플릿과 거의 같은 방식으로 동작합니다.

- `MemoryCell`은 `IntCell`과 비슷하지만, 인수 없는 생성자, 복사 생성자, 복사 할당 연산자를 가진 임의의 자료형 `Object`에 대해 동작합니다.

</div>
<div>

```cpp
template <typename Object>
class MemoryCell {
public:
    explicit MemoryCell(
        const Object& initialValue = Object{})
        : storedValue{initialValue} {}
    const Object& read() const {
        return storedValue;
    }
    void write(const Object& x) {
        storedValue = x;
    }
private:
    Object storedValue;
};
```

</div>
</div>

---
layout: prism
heading: 클래스 템플릿 — 사용
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `Object`는 상수 참조로 전달되며, 기본 변수는 `0`(유효하지 않은 `Object`일 수 있음)이 *아닙니다*.
  - 대신 기본값은 인수 없는 생성자로 만든 `Object`, 즉 `Object{}`입니다.

</div>
<div>

```cpp
int main() {
    MemoryCell<int> m1;
    MemoryCell<string> m2{"hello"};

    m1.write(37);
    m2.write(m2.read() + " world");
    cout << m1.read() << endl
         << m2.read() << endl;

    return 0;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: 함수와 클래스 템플릿"
---

<div style="height: 0rem;"></div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

template <typename Comparable>
const Comparable& findMax(const vector<Comparable>& a) {
    int maxIndex = 0;
    for (int i = 1; i < (int)a.size(); i++)
        if (a[maxIndex] < a[i]) maxIndex = i;
    return a[maxIndex];
}

template <typename Object>
class MemoryCell {
public:
    explicit MemoryCell(const Object& initialValue = Object{}) : storedValue{initialValue} {}
    const Object& read() const { return storedValue; }
    void write(const Object& x) { storedValue = x; }
private:
    Object storedValue;
};

int main() {
    vector<int> vi = {3, 1, 4, 1, 5, 9, 2, 6};
    vector<string> vs = {"apple", "pear", "kiwi", "fig"};
    cout << "findMax(int)    = " << findMax(vi) << "\n";
    cout << "findMax(string) = " << findMax(vs) << "\n";

    MemoryCell<string> m{"hello"};
    m.write(m.read() + " world");
    cout << "MemoryCell      = " << m.read() << endl;
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
