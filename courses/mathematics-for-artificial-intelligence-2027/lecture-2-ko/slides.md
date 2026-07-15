---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: MAI - Lecture 2 (KO)
download: true
info: |
  ## 인공지능수학 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/mathematics-for-artificial-intelligence-2027/lecture-2/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">인공지능수학</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">2주차: 수와 연산, 체계</p>

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

<div class="absolute left-10 right-10" style="top: 1rem; bottom: 5rem; display: grid; grid-template-columns: 1fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">과목 개요</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span class="text-gray-900 dark:text-gray-100">수와 연산, 체계</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">함수 해석</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">확률 1부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">확률 2부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">통계</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">선형대수 1부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">선형대수 2부</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">행렬 미분</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">신경망의 데이터 흐름</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 수와 연산, 체계
---



- 우리에게 익숙한 자연수나 실수 외에도, 허수, 집합, 행렬 등 다양한 방식을 통해 자연 현상을 표현할 수 있으며, 사칙연산과 마찬가지로 이들을 갖가지 방식으로 연산할 수 있다.

- 다양한 수 체계와 연산 방식을 이해하는 것은 인공지능을 비롯한 공학 전반에서 필요한 기초 개념이다.
  - 복소수를 통한 신호의 표현, 집합을 이용한 데이터의 표현 및 연산 등

- 오늘 수업에서는 다음과 같은 것들을 다룰 것이다:
  - 수 체계에 적용되는 다양한 연산들
  - 집합과 수열의 기본 개념들, 특별한 집합과 수열
  - 복소수의 의미와 표현

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">수와 연산</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">진법</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">지수와 로그</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">합과 곱 연산</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">집합과 수열</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">복소수</span></p>
  </div>

</div>

---
layout: prism
heading: 진법
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [$n$진법(base $n$)]{.hl}은 수를 셀 때, 자릿수가 올라가는 단위의 기준을 $n$으로 하는 셈법을 의미한다.
  - 우리가 흔히 사용하는 방법은 $10$진법이며, 컴퓨터는 주로 $2$진법(이진법)과 $16$진법(십육진법)을 사용한다.

- 임의의 자연수 $a$와 $n \geq 2$에 대해, 다음을 만족하는 정수들의 순서쌍 $(a_k, a_{k-1}, \ldots, a_1, a_0)$을 언제나 유일하게 찾을 수 있다.

$$
a = a_k n^k + a_{k-1} n^{k-1} + \cdots + a_1 n + a_0,\quad 0 \leq a_0, a_1, \ldots, a_k < n,\ a_k \neq 0.
$$

- 이때 $a = \overline{a_k a_{k-1} \cdots a_1 a_0}_{(n)}$으로 표기하고, $a$를 $n$진법으로 표현한다고 한다.
  - 일반적으로 $10$진법은 아래첨자를 생략한다.

- 유리수, 무리수, 심지어 복소수 진법도 사용할 수 있다.

---
layout: prism
heading: "DIY: 진법 변환"
---

<div style="height: 1rem;"></div>

<PyRunner>

```python
# Convert a base-10 integer into an arbitrary base n (2 <= n <= 16),
# and convert it back to verify.
digits = "0123456789ABCDEF"

def to_base(a, n):
    if a == 0:
        return "0"
    out = ""
    while a > 0:
        out = digits[a % n] + out
        a //= n
    return out

def from_base(s, n):
    return sum(digits.index(c) * n**i for i, c in enumerate(reversed(s)))

for a, n in [(2024, 2), (2024, 16), (255, 2), (255, 16)]:
    rep = to_base(a, n)
    print(f"{a:>5} (base 10) = {rep:>12} (base {n:>2})  ->  back: {from_base(rep, n)}")
```

</PyRunner>

---
layout: prism
heading: 지수
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 아래는 [지수(exponent)]{.hl}가 가지고 있는 다양한 성질들이다.

$$
\begin{gather*}
X^A X^B = X^{A+B}\\
\frac{X^A}{X^B} = X^{A-B}\\
(X^A)^B = X^{AB}\\
X^N + X^N = 2X^N \neq X^{2N}\\
2^N + 2^N = 2^{N+1}
\end{gather*}
$$

---
layout: prism
heading: 로그
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- [로그(log)]{.hl}는 아래 정의를 따른다.
  - 컴퓨터 과학에서는 따로 정의하지 않는 이상 로그의 밑은 $2$로 설정된다.
  - 자연과학을 비롯한 공학에서는 $e$를, 경제학 등 일상에서는 $10$을 사용한다.

<div class="theorem-box">
<div class="theorem-box-title">로그의 정의</div>
<div class="theorem-box-body">

$X^A = B$ 인 것은 $\log_X B = A$ 인 것과 동치이다.

</div>
</div>

- 정의에 따라, 몇몇 로그의 성질을 알 수 있다:

$$
\begin{gather*}
\log_A B = \log_C B / \log_C A,\ \forall A, B, C > 0,\ A \neq 1 \qquad \log AB = \log A + \log B\\
\log A/B = \log A - \log B \qquad \log(A^B) = B \log A \qquad \log X < X,\ \forall X > 0
\end{gather*}
$$

---
layout: prism
heading: "DIY: 로그의 성질"
---

<div style="height: 0.6rem;"></div>

<PyRunner>

```python
import numpy as np

A, B, C = 7.0, 12.0, 2.0

# Change of base: log_A(B) = log_C(B) / log_C(A)
lhs = np.log(B) / np.log(A)          # log_A(B) via natural logs
rhs = (np.log(B) / np.log(C)) / (np.log(A) / np.log(C))
print("change of base :", np.isclose(lhs, rhs))

# Product / power rules (base-2, as in computer science)
print("log2(AB)=log2 A+log2 B :", np.isclose(np.log2(A * B), np.log2(A) + np.log2(B)))
print("log2(A^B)=B log2 A     :", np.isclose(np.log2(A ** B), B * np.log2(A)))
print("log2(1024)             :", np.log2(1024))
```

</PyRunner>

---
layout: prism
heading: 합 연산
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 연산자 $\sum$는 다음과 같이 정의된다:

$$
\sum_{k=i}^{j} a_k = a_i + a_{i+1} + a_{i+2} + \cdots + a_j
$$

- $\sum$ 연산자는 다음과 같은 성질을 가진다:

$$
\sum_{k=1}^{n} (a_k \pm b_k) = \sum_{k=1}^{n} a_k \pm \sum_{k=1}^{n} b_k \qquad
\sum_{k=1}^{n} c\, a_k = c \sum_{k=1}^{n} a_k \qquad
\sum_{k=1}^{n} c = cn
$$

---
layout: prism
heading: 곱 연산
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 연산자 $\prod$는 다음과 같이 정의된다:

$$
\prod_{k=i}^{j} a_k = a_i\, a_{i+1}\, a_{i+2} \cdots a_j
$$

<PyRunner>

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
c = 3

print("sum linearity  :", np.isclose((c * a).sum(), c * a.sum()))
print("prod of c*a    :", np.prod(c * a), "= c^n * prod(a) =", c**len(a) * np.prod(a))
print("prod(a) = 5!   :", np.prod(a))
```

</PyRunner>

- [DIY]{.hl} 곱 연산의 다양한 성질을 찾아보라.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">수와 연산</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">집합과 수열</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">집합</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">특별한 집합</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">수열과 급수</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">복소수</span></p>
  </div>

</div>

---
layout: prism
heading: 집합과 원소, 부분집합
---


- [집합(set)]{.hl} $A$에 [원소(element)]{.hl} $a$가 속하면 $a \in A$, 그렇지 않으면 $a \notin A$라고 쓴다.
  - 모임(collection), 집합체(aggregate), 족(family)은 모두 집합의 동의어이며, 객체(object)는 원소의 동의어이다.

- $\{x : \cdots\}$는 조건 $\cdots$을 만족하는 모든 원소 $x$의 집합을 의미한다.

- 원소를 가지지 않는 집합을 [공집합(empty set)]{.hl}이라고 하며, $\emptyset$로 표기한다.

- $A$의 모든 원소가 $B$의 원소이면, $A$는 $B$의 [부분집합(subset)]{.hl}이라고 하며, $A \subset B$로 표기한다.
  - [DIY]{.hl} $A \subset B$를 조건제시법(집합 표현식)을 이용하여 다시 정의하라.

---
layout: prism
heading: 멱집합과 색인 집합
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 집합 $A$의 모든 부분집합을 모은 집합을 $A$의 [멱집합(power set)]{.hl}이라고 하고, $\mathcal{P}(A)$로 표현한다.
  - $X \in \mathcal{P}(A) \Rightarrow X \subset A$
  - $A$ 자신을 제외한 $A$의 모든 부분집합을 $A$의 [진부분집합(proper subset)]{.hl}이라고 한다.

- 집합 $A$와 모든 원소 $a \in A$에 대한 집합 $M_a$가 주어졌을 때, 집합의 모임 $\{M_a : a \in A\}$(또는 $\{M_a\}_{a \in A}$로도 표기)를 $A$에 대해 [색인(indexed)]{.hl}되었다고 하고, 집합 $A$를 [색인 집합(index set)]{.hl}이라고 한다.

$$
\mathcal{L} = \{ L_a : a \in \mathbb{R} \}, \quad\text{where } L_a = \{ x \in \mathbb{R} : x < a \}
$$

<div class="sub-item">

예를 들어, 위 $\mathcal{L}$은 실수 $\mathbb{R}$에 대해 색인되고, $\mathcal{A} = \{A_i : i = 1,2,3,4\}$는 $\{1,2,3,4\}$에 대해 색인된다.

</div>

---
layout: prism
heading: 합집합과 교집합
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [합집합(union)]{.hl} $A \cup B$는 $A$ 또는 $B$ 중 적어도 한 집합에 속하는 모든 원소 $x$의 집합이다.
  - $A \cup B = \{ x : x \in A \text{ or } x \in B \}$

- [교집합(intersection)]{.hl} $A \cap B$는 $A$와 $B$에 모두 속하는 모든 원소 $x$의 집합이다.
  - $A \cap B = \{ x : x \in A \text{ and } x \in B \}$

- $A \cap B = \emptyset$이면 집합 $A$와 $B$는 [서로소(disjoint)]{.hl}이다.

- 임의의 집합 $A$, $B$, $C$에 대해, 다음의 [분배 법칙(distributive laws)]{.hl}이 성립한다:

<div class="sub-item-enum">

1. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
2. $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$

</div>

---
layout: prism
heading: "DIY: 집합 연산과 분배 법칙"
---

<div style="height: 0.5rem;"></div>

<PyRunner>

```python
A = {0, 1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}

print("A ∪ B      :", A | B)
print("A ∩ B      :", A & B)
print("B \\ A      :", B - A)
print("disjoint?  :", A.isdisjoint({7, 8}))

# Distributive law: A ∪ (B ∩ C) == (A ∪ B) ∩ (A ∪ C)
print("distributive:", (A | (B & C)) == ((A | B) & (A | C)))

# Power set of {0,1,2}
from itertools import combinations
S = [0, 1, 2]
power = [set(c) for r in range(len(S) + 1) for c in combinations(S, r)]
print("power set   :", power)
```

</PyRunner>

---
layout: prism
heading: 차집합과 여집합
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [차집합(set difference)]{.hl} $B \setminus A$는 $A$에 포함되지 않는 $B$의 모든 원소의 집합이다.
  - $B \setminus A = \{ x : x \in B \text{ and } x \notin A \}$

- $A \subset X$일 때, 차집합 $X \setminus A$를 $X$에 대한 $A$의 [여집합(complement)]{.hl}이라고 한다.

<div class="theorem-box">
<div class="theorem-box-title">드 모르간의 법칙(De Morgan's laws)</div>
<div class="theorem-box-body">

집합 $A$와 $B$가 집합 $X$의 부분집합이면, 다음이 성립한다.

$$
X \setminus (A \cup B) = (X \setminus A) \cap (X \setminus B) \qquad
X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B)
$$

</div>
</div>

---
layout: prism
heading: 색인을 이용한 정의
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- $\{A_i : i \in I\}$를 색인 집합 $I$에 대해 색인된 집합의 모임이라고 하면, 이 모임의 합집합은 다음과 같이 정의된다.

$$
\bigcup_{i \in I} A_i = \{ x : \exists\, i \in I \text{ s.t. } x \in A_i \}.
$$

- 비슷하게, 이 모임의 교집합은 다음과 같이 정의된다.

$$
\bigcap_{i \in I} A_i = \{ x : \forall\, i \in I,\ x \in A_i \}.
$$

- 같은 방식으로 분배 법칙과 드 모르간의 법칙을 다시 쓸 수 있다:
  - $A \cap \bigcup_{i \in I} B_i = \bigcup_{i \in I} (A \cap B_i)$ and $A \cup \bigcap_{i \in I} B_i = \bigcap_{i \in I} (A \cup B_i)$
  - $X \setminus \left( \bigcup_{i \in I} A_i \right) = \bigcap_{i \in I} (X \setminus A_i)$ and $X \setminus \left( \bigcap_{i \in I} A_i \right) = \bigcup_{i \in I} (X \setminus A_i)$

---
layout: prism
heading: 수 체계 집합 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 0.5em;
}
</style>

- [자연수(natural number)]{.hl}는 $1, 2, 3, \ldots$와 같이 나아가는 수이다.

- 자연수의 엄밀한 정의는 [페아노 공리계(Peano's axioms)]{.hl}를 따르며, 다음을 만족하는 집합 $\mathbb{N}$을 자연수 집합이라고 한다.

<div class="sub-item-enum">

1. $\mathbb{N}$은 $1$이라고 불리는 특별한 한 원소를 가진다.
2. 각 $n \in \mathbb{N}$에 대해, 그 다음 수 $n^+ \in \mathbb{N}$이다.
3. $1$을 다음 수로 갖는 원소는 $\mathbb{N}$에 존재하지 않는다.
4. $\mathbb{N}$의 두 원소가 같은 다음 수를 가지면, 두 원소는 같다.
5. $S \subset \mathbb{N}$이 $1 \in S$이고, 임의의 $n \in S$에 대해 $n^+ \in S$이면 $S = \mathbb{N}$이다.

</div>

- 덧셈의 항등원 $0$이 빠져 있는 것이 불편하기 때문에, 현대 수학에서는 $0$을 포함한 [범자연수(whole numbers)]{.hl} $\mathbb{N}_0 = \mathbb{N} \cup \{0\}$을 사용하기도 한다.

- [정수(integer)]{.hl}는 $\mathbb{Z} = \{ x : n + x = 0,\ \forall n \in \mathbb{N}_0 \}$로 정의된다.

---
layout: prism
heading: 수 체계 집합 (2/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- [유리수(rational number)]{.hl}는 다음과 같이 정의된다.

$$
\mathbb{Q} = \left\{ x : x = \frac{m}{n},\ \forall m, n \in \mathbb{Z},\ n \neq 0 \right\}.
$$

- [무리수(irrational number)]{.hl} $\mathbb{I}$는 두 정수의 비로 나타낼 수 없는 수이며, [실수(real number)]{.hl} $\mathbb{R}$는 유리수와 무리수를 통틀어 의미한다.

- [허수 단위(imaginary unit)]{.hl} $i \equiv \sqrt{-1}$에 대해, [복소수(complex number)]{.hl}는 다음과 같이 정의된다.

$$
\mathbb{C} = \{ a + bi : \forall a, b \in \mathbb{R},\ i = \sqrt{-1} \}.
$$

---
layout: prism
heading: 볼록 집합
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 아래 성질을 만족하는 집합 $A$를 [볼록 집합(convex set)]{.hl}이라고 한다.
  - $tx + (1-t)y \in A,\ \forall x, y \in A,\ t \in [0, 1]$
    - 집합 $A$ 안의 임의의 두 점을 잡았을 때, 그 두 점을 잇는 선분 위의 모든 점도 $A$에 포함된다.

- 볼록 집합들의 교집합도 볼록 집합이며, 볼록 집합을 평행이동하거나 양의 선형 결합을 취해도 볼록성이 유지된다.

- 볼록 집합은 기계학습에서 중요한 의미를 가진다:
  - 최적화 문제의 목적 함수와 제약 조건이 볼록할 때 해를 찾기 더 쉬우며, [서포트 벡터 머신(support vector machine)]{.hl}의 결정 경계를 찾는 문제는 볼록 최적화 문제이다.
  - [뉴럴 네트워크(neural network)]{.hl}의 손실 함수가 볼록하면 학습이 더 안정적으로 진행된다.

---
layout: prism
heading: "DIY: 볼록성 판별"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)

# A disk of radius 1 is convex; a ring (annulus) is not.
def in_disk(p):  return p[0]**2 + p[1]**2 <= 1.0
def in_ring(p):  return 0.5 <= p[0]**2 + p[1]**2 <= 1.0

def convex_test(membership, n=20000):
    ok = 0
    for _ in range(n):
        x, y = rng.uniform(-1, 1, 2), rng.uniform(-1, 1, 2)
        if membership(x) and membership(y):
            t = rng.random()
            if membership(t * x + (1 - t) * y):
                ok += 1
            else:
                return False   # found two points whose segment leaves the set
    return True

print("disk is convex :", convex_test(in_disk))
print("ring is convex :", convex_test(in_ring))
```

</PyRunner>

---
layout: prism
heading: 수열의 정의
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [수열(sequence)]{.hl}은 $\mathbb{N}$(또는 어떤 자연수 $N$ 이하의 자연수 집합)을 정의역으로 하는 _함수_로, $n$번째 항을 $x_n$이라 할 때 $\{x_n\}_{n=1}^{\infty}$ 또는 $\{x_n\}_{n=1}^{N}$과 같이 나타낸다.

- [등차수열(arithmetic sequence)]{.hl}은 연속한 두 항의 차가 일정한 수열이며, 공차가 $d$일 때 일반항은 $a_n = a + (n-1)d$이다.

- [등비수열(geometric sequence)]{.hl}은 연속한 두 항의 비가 일정한 수열이며, 공비가 $r$일 때 일반항은 $a_n = a r^{n-1}$이다.

- 각 항의 역수가 등차수열을 이루는 수열을 [조화수열(harmonic sequence)]{.hl}이라 하며, 일반항은 $a_n = \dfrac{a}{1 + a(n-1)d}$이다.

- 각 항에서 앞 항을 뺀 값들의 수열을 [계차수열(difference sequence)]{.hl}이라고 한다.

---
layout: prism
heading: 피보나치 수열
---

<style>
.slidev-layout ul > li {
  margin-top: 3.4em;
}
</style>

- 다양한 자연계의 현상을 표현하는 [피보나치 수열(Fibonacci sequence)]{.hl}은 다음 점화식으로 정의된다.

$$
F_1 = 1,\quad F_2 = 1,\quad F_{n+2} = F_{n+1} + F_n.
$$

- 그 일반항의 닫힌 형식은 다음과 같다.

$$
F_n = \frac{1}{\sqrt{5}} \left[ \left( \frac{1 + \sqrt{5}}{2} \right)^n - \left( \frac{1 - \sqrt{5}}{2} \right)^n \right].
$$

- [DIY]{.hl} 피보나치 수열의 이웃한 두 항이 항상 서로소임을 보여라.

---
layout: prism
heading: "DIY: 피보나치 수열 계산"
---

<PyRunner>

```python
import numpy as np

# Recurrence vs. the closed-form (Binet) formula
phi, psi = (1 + 5**0.5) / 2, (1 - 5**0.5) / 2
F = [0, 1]
for _ in range(18):
    F.append(F[-1] + F[-2])

print(f"{'n':>3} | {'recurrence':>10} | {'closed form':>12}")
for n in range(1, 13):
    binet = (phi**n - psi**n) / 5**0.5
    print(f"{n:>3} | {F[n]:>10} | {binet:>12.4f}")

# Consecutive Fibonacci numbers are coprime
from math import gcd
print("all coprime:", all(gcd(F[n], F[n+1]) == 1 for n in range(1, 18)))
```

</PyRunner>

---
layout: prism
heading: 급수의 정의
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 수열 $\{a_n\}$의 부분합 $S_n = a_1 + a_2 + \cdots + a_n$이 주어질 때, [급수(series)]{.hl}는 다음의 _극한_으로 정의된다.

$$
\lim_{n \to \infty} S_n = \lim_{n \to \infty} \sum_{k=1}^{n} a_k.
$$

- 극한값 $S$가 어떤 실수로 수렴하면 그 급수는 [수렴한다(converge)]{.hl}고 하고, 그렇지 않으면 [발산한다(diverge)]{.hl}고 한다.

- 급수는 부분합의 극한이며, 이는 "무한히 여러 번 더하는 것"과는 다른 개념이다.
  - 이는 [리만 재배열 정리(Riemann series theorem)]{.hl}를 통해 이해할 수 있다.

$$
\frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \cdots
$$

---
layout: prism
heading: "DIY: 라이프니츠 급수로 π 계산"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# Leibniz: pi/4 = sum_{n=0}^inf (-1)^n / (2n+1)
def leibniz(N):
    n = np.arange(N)
    return 4.0 * np.sum((-1.0)**n / (2*n + 1))

print(f"{'terms':>8} | {'estimate':>12} | {'|error|':>10}")
for N in [10, 100, 1000, 100000]:
    est = leibniz(N)
    print(f"{N:>8} | {est:>12.6f} | {abs(est - np.pi):>10.6f}")

print(f"\ntrue pi = {np.pi:.6f}  (convergence is famously slow!)")
```

</PyRunner>

---
layout: prism
heading: 푸리에 급수
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- _임의의_ 함수를 [삼각함수(trigonometric)]{.hl}와 [지수함수(exponential)]{.hl}의 일차결합으로 나타내는 것을 [푸리에 해석(Fourier analysis)]{.hl}이라 한다.

- 주기가 $T$인 함수는 삼각함수의 합으로 전개할 수 있으며, 이를 [푸리에 급수(Fourier series)]{.hl}라고 한다.

$$
f(x) = \sum_{n=1}^{\infty} a_n \sin(n \omega x) + \sum_{n=1}^{\infty} b_n \cos(n \omega x) + b_0,\quad \omega = \frac{2\pi}{T}.
$$

- [푸리에 계수(Fourier coefficients)]{.hl}는 다음과 같이 정의된다.

$$
a_n = \frac{2}{T} \int_{x_0}^{x_0+T} f(x) \sin(n \omega x)\, \mathrm{d}x, \quad
b_n = \frac{2}{T} \int_{x_0}^{x_0+T} f(x) \cos(n \omega x)\, \mathrm{d}x.
$$

---
layout: prism
heading: "DIY: 사인 함수로 사각파 만들기"
---

<div style="height: 0.4rem;"></div>

<PyRunner>

```python
import numpy as np

# A square wave equals the Fourier sum of odd harmonics:
#   f(x) = (4/pi) * sum_{k=1,3,5,...} sin(k x) / k
x = np.linspace(0, 2 * np.pi, 8)     # sample a few points
target = np.sign(np.sin(x))          # ideal square wave

for n_harm in [1, 3, 9, 49]:
    ks = np.arange(1, 2 * n_harm, 2)                 # 1, 3, 5, ...
    approx = (4 / np.pi) * sum(np.sin(k * x) / k for k in ks)
    err = np.mean(np.abs(approx - target))
    print(f"{len(ks):>2} harmonics -> mean |error| = {err:.4f}")
```

</PyRunner>

---
layout: prism
heading: 멱급수
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 멱급수는 변수의 거듭제곱으로 이루어진 무한 급수로, 함수나 수열을 표현하거나 근사하는 데 사용된다.

- 변수 $x_1, x_2, \ldots, x_n$에 대하여, $(x_1', x_2', \ldots, x_n')$에서의 [멱급수(power series)]{.hl}는 다음과 같다.

$$
\sum_{(k_1, \ldots, k_n) \in \mathbb{N}^n} a_{k_1, \ldots, k_n} \prod_{i=1}^{n} (x_i - x_i')^{k_i}.
$$

- [DIY]{.hl} 등차수열 $\{a_n\}$과 등비수열 $\{b_n\}$에 대하여 항별 곱 $c_n = a_n b_n$을 고려하고, 이 "등차등비" 급수 $S_n = \sum_{k=1}^{n} c_k$를 계산하라.

---
layout: prism
heading: 테일러 급수 (1/2)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- [테일러 급수(Taylor series)]{.hl}(또는 테일러 전개)는 임의의 함수 $f(x)$를 점 $a$ 주변에서 무한한 다항식의 합으로 표현한다.

- 이는 그 점에서의 모든 도함수를 사용하여 함수의 값을 근사한다.

$$
f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots
$$

- 특별히 $a = 0$인 경우를 [매클로린 급수(Maclaurin series)]{.hl}라고 한다.

$$
f(x) \approx f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots
$$

---
layout: prism
heading: 테일러 급수 (2/2)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 전개 차수가 높을수록(즉, 항이 많아질수록), 근사가 목표 함수에 더 가까워진다.
  - [DIY]{.hl} $\sin x$의 매클로린 급수를 전개해보라.

- 테일러 급수와 매클로린 급수는 함수 계산을 매우 간단하게 해주므로, 신호처리 등 공학 전반에서 널리 사용된다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W02_taylor.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "DIY: 테일러 급수 계산"
---

<PyRunner>

```python
import numpy as np
from math import factorial

# Maclaurin series of sin(x): sum (-1)^k x^(2k+1)/(2k+1)!
def sin_taylor(x, order):
    return sum((-1)**k * x**(2*k+1) / factorial(2*k+1) for k in range((order+1)//2 + 1))

x = 1.0
for order in [1, 3, 5, 7]:
    print(f"order {order}: {sin_taylor(x, order):.6f}   (true sin 1 = {np.sin(x):.6f})")
```

</PyRunner>

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">수와 연산</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">집합과 수열</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">복소수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">정의와 켤레복소수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">연산</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">행렬 표현</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">극형식</span></p>
  </div>

</div>

---
layout: prism
heading: 복소수
---

<style>
.slidev-layout ul > li {
  margin-top: 2.6em;
}
</style>

- 과학과 공학에서는 여러 복합적인 단위로 이루어진 식을 하나의 수로 취급해야 할 때가 많다. $1$, $2$, $3$과 같은 하나의 값이 아니라 $a + bi$처럼 표현되는 이러한 수를 [복소수(complex number)]{.hl}라고 한다.

- 복소수는 하나의 보통 수로 해를 표현하는 것이 불가능한 공간에서 그 해를 표현하기 위해 고안된 것이다.

- 모든 $a, b \in \mathbb{R}$에 대해 복소수는 $i \equiv \sqrt{-1}$와 함께 $a + bi$로 쓰며, $\mathfrak{R}(a+bi) = a$를 [실수부(real part)]{.hl}, $\mathfrak{I}(a+bi) = b$를 [허수부(imaginary part)]{.hl}라고 한다.

---
layout: prism
heading: 켤레복소수
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- $z = a + bi \in \mathbb{C}$에 대해, [켤레복소수(complex conjugate)]{.hl} $\bar{z}$는 다음과 같이 정의된다.

$$
\bar{z} \equiv \mathfrak{R}(z) - i\,\mathfrak{I}(z) = a - bi.
$$

- [절댓값(absolute value)]{.hl}(모듈러스) $|z|$는 다음과 같이 정의된다.

$$
|z| = \sqrt{z \bar{z}} = \sqrt{\mathfrak{R}(z)^2 + \mathfrak{I}(z)^2} = \sqrt{a^2 + b^2}.
$$

- [DIY]{.hl} 복소평면에 $z = -1 + i$와 $\bar{z}$를 나타내고, $|z|$를 기하적으로 해석하라.
- [DIY]{.hl} $z^2 + 2z + 5 = 0$의 해를 구하고, 그 해들이 서로 켤레복소수 관계인지 확인하라.

---
layout: prism
heading: 복소수 연산
---

- 두 복소수 $a + bi$와 $c + di$에 대해, 덧셈은 다음과 같이 정의된다.

$$
(a + bi) + (c + di) = (a + c) + (b + d)i.
$$

- 곱셈은 다음과 같이 정의된다.

$$
(a + bi)(c + di) = (ac - bd) + (ad + bc)i.
$$

<div class="sub-item">

복소수의 덧셈과 곱셈은 모두 결합법칙과 교환법칙을 만족하며, 항등원과 역원이 항상 존재한다.

</div>

- [DIY]{.hl} 복소수의 역원을 계산해보고 나눗셈을 정의할 수 있는지 확인하라.

<PyRunner>

```python
z1 = complex(2, 3)   # 2 + 3i
z2 = complex(1, -1)  # 1 - i

print("z1 + z2 :", z1 + z2)
print("z1 * z2 :", z1 * z2, " = (ac-bd)+(ad+bc)i =", complex(2*1 - 3*(-1), 2*(-1) + 3*1))
print("conj z1 :", z1.conjugate(), " |z1| =", abs(z1))
print("1 / z1  :", 1 / z1, " -> z1 * (1/z1) =", z1 * (1 / z1))
```

</PyRunner>

---
layout: prism
heading: 행렬 표현 (1/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 3.4em;
}
</style>

- 복소수는 [선형대수(linear algebra)]{.hl}의 [행렬 표현(matrix representation)]{.hl}으로도 잘 나타낼 수 있다.

$$
z = a + bi = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}.
$$

- $z_1 = a + bi$와 $z_2 = c + di$에 대해, 그 합과 곱은 다음과 같이 된다.

$$
z_1 + z_2 = \begin{pmatrix} a+c & -(b+d) \\ b+d & a+c \end{pmatrix}, \quad
z_1 z_2 = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}\begin{pmatrix} c & -d \\ d & c \end{pmatrix} = \begin{pmatrix} ac-bd & -(ad+bc) \\ ad+bc & ac-bd \end{pmatrix}.
$$

---
layout: prism
heading: 행렬 표현 (2/3)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 허수 단위 $i$를 행렬로 나타내면 $i = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$이 되며, 이를 거듭제곱하면 다음을 얻는다.

$$
i^n = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}^n =
\begin{cases}
\ \ 1 & \text{if } n \equiv 0 \\
\ \ i & \text{if } n \equiv 1 \\
-1 & \text{if } n \equiv 2 \\
-i & \text{if } n \equiv 3
\end{cases} \pmod 4
$$

<div class="sub-item">

이는 익숙한 순환 $i^0 = 1,\ i^1 = i,\ i^2 = -1,\ i^3 = -i,\ i^4 = 1, \ldots$을 정확히 재현한다.

</div>

---
layout: prism
heading: 행렬 표현 (3/3)
---

<div class="grid grid-cols-2 gap-1" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [회전 행렬(rotation matrix)]{.hl}에 같은 방식으로 연산하면 $i$와 $\pi/2$ 회전 사이의 깊은 연관을 알 수 있다.

$$
\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
$$

- 이를 일반화하면 다음을 얻는다.

$$
i^n = \begin{pmatrix} \cos\frac{n\pi}{2} & -\sin\frac{n\pi}{2} \\ \sin\frac{n\pi}{2} & \cos\frac{n\pi}{2} \end{pmatrix}.
$$

</div>
<div>

<PyRunner>

```python
import numpy as np

def cx(a, b):        # complex a+bi as a matrix
    return np.array([[a, -b], [b, a]], float)

z1, z2 = cx(2, 3), cx(1, -1)
# matrix product == complex product?
prod = z1 @ z2
print("matrix product :\n", prod)
print("(ac-bd, ad+bc) :", (2*1-3*-1, 2*-1+3*1))

# i^n via matrix power equals rotation by n*pi/2
i = cx(0, 1)
for n in range(1, 5):
    R = np.linalg.matrix_power(i, n)
    th = n * np.pi / 2
    rot = np.array([
      [np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]
    ])
    print(f"i^{n}: matches rotation? {np.allclose(R, rot)}")
```

</PyRunner>

</div>
</div>

---
layout: prism
heading: 극형식
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 그림은 복소평면 위의 복소수를 시각화한 것이며, 이러한 표현 방식을 [극형식(polar form)]{.hl}이라 한다.

- 편각이 $\theta$인 복소수 $z = a + bi$에 대해, 극형식은 다음과 같다.

$$
z = |z|(\cos\theta + i\sin\theta).
$$

- [DIY]{.hl} $a$와 $b$가 주어졌을 때, 편각 $\theta$를 계산하라.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/mai/mai-2027/W02_polar.svg" class="tikz-fig" style="width: 100%;" />

</div>
</div>

- 같은 방식으로 [오일러 공식(Euler's formula)]{.hl} $\ e^{ix} \equiv \cos x + i\sin x$를 얻는다.
  - [DIY]{.hl} $x = \pi$를 대입하여 [오일러 등식(Euler's identity)]{.hl} $e^{i\pi} + 1 = 0$을 얻어라.

---
layout: prism
heading: "DIY: 오일러 등식 계산"
---

<PyRunner>

```python
import numpy as np

for z in [complex(2, 1.5), complex(-1, 1)]:
    r, theta = abs(z), np.angle(z)
    print(f"z = {z}:  r = {r:.4f}, theta = {theta:.4f} rad")
    print("   polar reconstruct :", r * (np.cos(theta) + 1j*np.sin(theta)))

print("\nEuler's identity  e^(i*pi) + 1 =", np.exp(1j*np.pi) + 1)
```

</PyRunner>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
