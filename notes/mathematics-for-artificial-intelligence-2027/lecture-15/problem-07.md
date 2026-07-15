# 문제 7 · 복소수 방정식

::: info 문제 7 [2점]
복소수 $z$가 아래 조건을 만족한다고 할 때 $z$의 값을 모두 구하시오.

$$
z+\frac{1}{z}=2i,\qquad z\neq 0
$$
:::

::: details 풀이 및 해설
$z\neq0$ 이므로 양변에 $z$를 곱하여 이차방정식으로 만든다.

$$
z^2+1=2iz\;\;\Longrightarrow\;\; z^2-2iz+1=0.
$$

근의 공식<span class="gloss">quadratic formula</span> $z=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$ 에서 $a=1,\ b=-2i,\ c=1$ 이므로

$$
z=\frac{2i\pm\sqrt{(-2i)^2-4}}{2}=\frac{2i\pm\sqrt{-4-4}}{2}=\frac{2i\pm\sqrt{-8}}{2}.
$$

$\sqrt{-8}=2\sqrt{2}\,i$ 이므로

$$
z=\frac{2i\pm 2\sqrt{2}\,i}{2}=(1\pm\sqrt{2})\,i.
$$

$$
\boxed{\;z=(1+\sqrt{2})\,i\quad\text{또는}\quad z=(1-\sqrt{2})\,i\;}
$$

검산: $z=(1+\sqrt2)i$ 이면 $\dfrac1z=\dfrac{1}{(1+\sqrt2)i}=-(\sqrt2-1)i$ 이므로 $z+\dfrac1z=(1+\sqrt2)i-(\sqrt2-1)i=2i$ 로 조건을 만족한다.

👉 [실습(Python)에서 확인하기](./lab-07)
:::
