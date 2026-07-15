# 문제 9 · 베이즈 정리 — 공장 불량품

::: info 문제 9 [3점]
공장에서 기계 A는 하루에 전체 제품의 40\%, 기계 B는 나머지 60\%를 생산한다. A에서 생산된 제품의 불량률은 2\%, B에서 생산된 제품의 불량률은 5\%이다. 무작위로 뽑은 제품이 불량품일 때 그 제품이 A에서 왔을 확률을 구하시오.
:::

::: details 풀이 및 해설
사건을 정의하자. $A$: A가 생산, $B$: B가 생산, $D$: 불량품. 주어진 값은

$$
P(A)=0.4,\quad P(B)=0.6,\quad P(D\mid A)=0.02,\quad P(D\mid B)=0.05.
$$

**전체 확률의 법칙<span class="gloss">law of total probability</span>** 으로 불량품 확률을 구한다.

$$
P(D)=P(D\mid A)P(A)+P(D\mid B)P(B)=0.02\cdot0.4+0.05\cdot0.6=0.008+0.030=0.038.
$$

**베이즈 정리<span class="gloss">Bayes' theorem</span>** 로 사후확률을 구한다.

$$
P(A\mid D)=\frac{P(D\mid A)P(A)}{P(D)}=\frac{0.008}{0.038}=\frac{8}{38}=\frac{4}{19}.
$$

$$
\boxed{\;P(A\mid D)=\dfrac{4}{19}\approx 0.2105\;}
$$

👉 [실습(Python)에서 확인하기](./lab-09)
:::
