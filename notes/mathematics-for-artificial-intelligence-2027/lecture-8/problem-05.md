# 문제 5 · 로그 방정식

::: info 문제 5 [2점]
집합 $\{x:\log_x 16=\log_{16}x,\ x\ge 0,\ \forall x\in\mathbb{R}\}$의 원소(들)를 찾으시오.
:::

::: details 풀이 및 해설
로그의 밑이 되려면 $x>0,\ x\neq 1$이어야 합니다. $t=\log_{16}x$로 두면, 밑변환 공식에 의해

$$
\log_x 16 = \frac{1}{\log_{16}x} = \frac{1}{t}.
$$

주어진 조건 $\log_x 16 = \log_{16}x$는 $\dfrac{1}{t}=t$, 즉

$$
t^2 = 1 \quad\Longrightarrow\quad t=\pm 1.
$$

- $t=1$: $\log_{16}x = 1 \Rightarrow x = 16$.
- $t=-1$: $\log_{16}x = -1 \Rightarrow x = 16^{-1} = \dfrac{1}{16}$.

두 값 모두 $x>0,\ x\neq 1$을 만족합니다.

$$
\boxed{\;x\in\left\{\tfrac{1}{16},\ 16\right\}\;}
$$

👉 [실습(Python)에서 확인하기](./lab-05)
:::
