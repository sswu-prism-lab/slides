# 문제 2 · 확률적 그래프 모델 계산

::: info 문제 2 — 확률적 그래프 모델 계산
이진 확률 변수 $A$, $B$, $C$, $D$, $E$에 대해, 아래와 같은 조건부 확률 분포가 주어졌다.

$$
p(A=1)=0.3,\quad p(B=1)=0.4
$$

$$
p(C=1\mid A,B)=\begin{cases}0.9 & A=1,B=1\\0.6 & A=1,B=0\\0.5 & A=0,B=1\\0.1 & \text{otherwise}\end{cases},\quad
p(D=1\mid A)=\begin{cases}0.7 & A=1\\0.2 & \text{otherwise}\end{cases},\quad
p(E=1\mid D)=\begin{cases}0.8 & D=1\\0.3 & \text{otherwise}\end{cases}
$$

이 때, $p(B=1\mid E=1)$을 구하시오.

---

확률적 그래프 모델을 그린 후, 확률의 성질에 따라서 역산하여 구할 수 있다.
:::

::: details 풀이 및 해설
**그래프 구조** — 조건부 분포로부터 부모 관계를 읽으면 $A\to C$, $B\to C$, $A\to D$, $D\to E$이다. 즉 구조는

$$
B\longrightarrow C\longleftarrow A\longrightarrow D\longrightarrow E
$$

**핵심 관찰(d-분리)** — $B$에서 $E$로 가는 유일한 경로는 $B\to C\leftarrow A\to D\to E$이다. 이 경로의 $C$는 **머리-머리(head-to-head) 노드, 즉 콜라이더**이며, $C$나 그 자손은 관측되지 않았다($C$는 자손이 없는 말단 노드). 따라서 콜라이더에서 경로가 **차단**되어 $B$와 $E$는 조건부 독립이다.

$$
B \perp\!\!\!\perp E\ \Longrightarrow\ p(B=1\mid E=1)=p(B=1)=\boxed{0.4}
$$

**검산** — 다섯 변수의 결합확률 $p(A)p(B)p(C\mid A,B)p(D\mid A)p(E\mid D)$을 모두 나열해 직접 계산해도

$$
p(B=1\mid E=1)=\frac{p(B=1,E=1)}{p(E=1)}=\frac{0.1900}{0.4750}=0.4000
$$

으로 같다. $E$의 확률은 $A\to D\to E$ 경로로만 결정되고 $B$와는 무관하기 때문이다.

👉 [실습(Python)에서 전수 계산으로 확인](./lab-02)
:::
