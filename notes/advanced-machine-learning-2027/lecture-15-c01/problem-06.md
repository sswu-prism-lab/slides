# 문제 6 · 베이즈망 추론

::: info 문제 6 [5점]
이항 변수 $A$, $B$, $C$, $D$, $E$에 대해 $p(A=1)=\tfrac12$이고 아래와 같은 조건부 분포가 주어졌다.

$$
p(B=1\mid A=1)=\tfrac23,\quad p(C=1\mid A=1)=\tfrac34,\quad p(E=1\mid D=1)=\tfrac45
$$

$$
p(D=1\mid B=b,C=c)=\begin{cases}\tfrac14, & b+c=0\\[2pt]\tfrac34, & \text{otherwise}\end{cases}
$$

이 때, $p(A=1\mid E=1)$, $p(B=1\mid C=1,E=1)$을 각각 구하시오.
:::

::: details 풀이 및 해설
**그래프 구조** — $A\to B$, $A\to C$, $(B,C)\to D$, $D\to E$.

결합확률은 $p(A)p(B\mid A)p(C\mid A)p(D\mid B,C)p(E\mid D)$이다. 보완된 CPT로 모든 항이 정해지므로 $E=1$(또는 $C=1,E=1$)로 주변화하여 조건부확률을 계산한다.

**$p(A=1\mid E=1)$** — $E$는 $D$를 통해서만 $A$와 연결된다.

$$
p(A=1\mid E=1)=\frac{p(A=1,E=1)}{p(E=1)}=\boxed{\dfrac{5}{9}}\approx0.556
$$

$A=1$이면 $B,C$가 켜질 확률이 커져 $D=1$, 나아가 $E=1$일 확률이 높아지므로 사후확률이 사전 $\tfrac12$보다 상승한다.

**$p(B=1\mid C=1,E=1)$** — $C=1,E=1$을 조건으로 $B$를 주변화하면

$$
p(B=1\mid C=1,E=1)=\frac{p(B=1,C=1,E=1)}{p(C=1,E=1)}=\boxed{\dfrac{7}{12}}\approx0.583
$$

$C=1$과 $E=1$(즉 $D$가 켜졌을 가능성)이 함께 관측되면 $D$의 공통 원인인 $B$가 켜졌을 확률이 사전보다 높아진다.
:::
