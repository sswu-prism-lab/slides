# 문제 6 · 베이즈망 추론

::: info 문제 6 [5점]
이항 변수 $A$, $B$, $C$, $D$, $E$에 대해 $p(A=1)=\tfrac13$이고 아래와 같은 조건부 분포가 주어졌다.

$$
p(B=1\mid A=1)=\tfrac34,\quad p(D=1\mid A=1)=\tfrac23,\quad p(C=1\mid B=1)=\tfrac45
$$

$$
p(E=1\mid C=c,D=d)=\begin{cases}\tfrac25, & c+d=0\\[2pt]\tfrac35, & c+d=1\\[2pt]1, & c+d=2\end{cases}
$$

이 때, $p(A=1\mid E=1)$, $p(C=1\mid D=1,E=1)$을 각각 구하시오.
:::

::: details 풀이 및 해설
**그래프 구조** — $A\to B$, $A\to D$, $B\to C$, $(C,D)\to E$.

결합확률은 $p(A)p(B\mid A)p(D\mid A)p(C\mid B)p(E\mid C,D)$이다. 보완된 CPT로 모든 항이 정해지므로 필요한 조건을 걸고 주변화한다.

**$p(A=1\mid E=1)$**:

$$
p(A=1\mid E=1)=\frac{p(A=1,E=1)}{p(E=1)}=\boxed{\dfrac{75}{187}}\approx0.401
$$

**$p(C=1\mid D=1,E=1)$** — $D=1,E=1$을 조건으로 $C$를 주변화하면

$$
p(C=1\mid D=1,E=1)=\frac{p(C=1,D=1,E=1)}{p(D=1,E=1)}=\boxed{\dfrac{5}{8}}=0.625
$$

$D=1$인 상태에서 $E=1$이 관측되면, $c+d$가 클수록 $E=1$ 확률이 커지므로($c{+}d{=}2$일 때 $p(E{=}1)=1$) $C=1$이었을 가능성이 사전보다 높아진다.
:::
