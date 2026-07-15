# 문제 5 · 몫의 미분법

::: info 문제 5 [2점]
다음 함수를 미분하시오.

$$
f(x)=\frac{e^{3x}}{x^2+1}
$$
:::

::: details 풀이 및 해설
몫의 미분법<span class="gloss">quotient rule</span> $\left(\dfrac{u}{v}\right)'=\dfrac{u'v-uv'}{v^2}$ 을 적용한다. 여기서 $u=e^{3x}$, $v=x^2+1$ 이고

$$
u'=3e^{3x},\qquad v'=2x.
$$

따라서

$$
f'(x)=\frac{3e^{3x}(x^2+1)-e^{3x}\cdot 2x}{(x^2+1)^2}.
$$

분자에서 $e^{3x}$ 를 묶어 정리하면

$$
\boxed{\;f'(x)=\frac{e^{3x}\left(3x^2-2x+3\right)}{(x^2+1)^2}\;}
$$

👉 [실습(Python)에서 확인하기](./lab-05)
:::
