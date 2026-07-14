# 문제 9 · 거부 표집법

::: info 문제 9 [5점]
$0\leqslant x\leqslant1$ 구간에서 분포 $f(x)=\tfrac32(1-x^2)$에 거부 표집법<span class="gloss">rejection sampling</span>을 적용하기 위해 제안 분포를 $g(x)=1$로 설정하였다. 이 때 거부 표집 상수 $k$를 구하고, $x=0.25$, $u=0.8$이 표집되었을 때 채택/거부 여부를 판단하시오. 또한, 한 번의 채택을 얻기 위해 평균적으로 몇 번의 표집이 필요한지 계산하시오.
:::

::: details 풀이 및 해설
**거부 상수** — 모든 $x$에서 $f(x)\leqslant k\,g(x)$를 만족하는 최소 $k$는

$$
k=\max_{x\in[0,1]}\frac{f(x)}{g(x)}=\max_{x}\tfrac32(1-x^2)
$$

$f(x)=\tfrac32(1-x^2)$은 $x=0$에서 최대이므로

$$
k=\tfrac32(1-0)=\boxed{1.5}
$$

**채택/거부** — 후보 $x=0.25$의 채택 임계는 $\dfrac{f(x)}{k\,g(x)}$이다.

$$
f(0.25)=\tfrac32(1-0.0625)=1.40625,\qquad \frac{f(0.25)}{k\,g(0.25)}=\frac{1.40625}{1.5}=0.9375
$$

$u=0.8$이 $0.9375$ **이하**이므로

$$
u=0.8\leqslant0.9375\ \Longrightarrow\ \boxed{\text{채택(accept)}}
$$

**평균 표집 횟수** — $f$와 $g$가 모두 정규화되어 있으므로 채택 확률은 $\dfrac1k=\dfrac1{1.5}=\dfrac23$이고, 평균 표집 횟수는

$$
\mathbb{E}[\text{시도 횟수}]=k=\boxed{1.5}\ \text{회}
$$

👉 [실습(Python)에서 계산하기](./lab-09)
:::
