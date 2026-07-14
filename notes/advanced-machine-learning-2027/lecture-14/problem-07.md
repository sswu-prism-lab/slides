# 문제 7 · 거부 표집법

::: info 문제 7 — 거부 표집법
$x\in[0,1]$에서 찾고자 하는 분포의 확률밀도함수는 $p(x)=6x(1-x)$이고, 제안 분포로 $q(x)=\mathrm{Uniform}[0,1]$을 사용한다. 이 때, 거부 표집 상수 $k$를 구하고, 한 차례 표집에서 $x=0.8$, $u=0.2$가 추출되었을 때 이 후보가 수락되는지 거부되는지 확인하시오.

---

균등 분포 $\mathrm{Uniform}[a,b]$의 확률 밀도 함수는 $\frac{1}{b-a}$이다.
:::

::: details 풀이 및 해설
$q(x)=\mathrm{Uniform}[0,1]$이므로 $q(x)=1$이다. 거부 표집에서는 모든 $x$에 대해 $p(x)\leqslant k\,q(x)$를 만족하는 최소의 $k$를 택한다.

$$
k=\max_x\frac{p(x)}{q(x)}=\max_{x\in[0,1]}6x(1-x)
$$

$p(x)=6x-6x^2$을 미분하면 $p'(x)=6-12x=0\Rightarrow x=0.5$에서 최대이고

$$
k=6\cdot0.5\cdot(1-0.5)=\boxed{1.5}
$$

**수락/거부 판정** — 후보 $x=0.8$에 대해 수락 확률은 $\dfrac{p(x)}{k\,q(x)}$이다.

$$
p(0.8)=6\cdot0.8\cdot0.2=0.96,\qquad \frac{p(0.8)}{k\,q(0.8)}=\frac{0.96}{1.5\cdot1}=0.64
$$

$u=0.2$가 $0.64$ **이하**이므로

$$
u=0.2\leqslant0.64\ \Longrightarrow\ \boxed{\text{수락(accept)}}
$$

👉 [실습(Python)에서 계산하기](./lab-07)
:::
