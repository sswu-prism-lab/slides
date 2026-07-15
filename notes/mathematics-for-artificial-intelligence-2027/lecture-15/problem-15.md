# 문제 15 · 방향도함수 — 최대 증가 방향

::: info 문제 15 [4점]
함수 $u(x,y)$의 $(1,1)$에서의 증가 방향을 찾으시오.

$$
u(x,y)=\frac{x}{x^2+y^2}
$$
:::

::: details 풀이 및 해설
함수가 가장 빠르게 증가하는 방향은 그래디언트<span class="gloss">gradient</span> $\nabla u$ 의 방향이다. 먼저 편미분을 구한다.

**$x$에 대한 편미분** (몫의 미분법, $x^2+y^2$을 $v$로 두면):

$$
\frac{\partial u}{\partial x}=\frac{1\cdot(x^2+y^2)-x\cdot 2x}{(x^2+y^2)^2}=\frac{y^2-x^2}{(x^2+y^2)^2}.
$$

**$y$에 대한 편미분:**

$$
\frac{\partial u}{\partial y}=\frac{0\cdot(x^2+y^2)-x\cdot 2y}{(x^2+y^2)^2}=\frac{-2xy}{(x^2+y^2)^2}.
$$

점 $(1,1)$ 에서 $x^2+y^2=2$ 이므로 분모는 $2^2=4$ 이고

$$
\frac{\partial u}{\partial x}\Big|_{(1,1)}=\frac{1-1}{4}=0,\qquad
\frac{\partial u}{\partial y}\Big|_{(1,1)}=\frac{-2}{4}=-\frac12.
$$

따라서 그래디언트는

$$
\nabla u(1,1)=\left(0,\ -\tfrac12\right).
$$

증가 방향(단위벡터)은 이를 정규화한 것이다.

$$
\boxed{\;\nabla u(1,1)=\left(0,\ -\tfrac12\right),\quad\text{최대 증가 방향}=(0,\ -1)\;}
$$

즉 $(1,1)$ 에서는 $-y$ 방향으로 움직일 때 $u$가 가장 빠르게 증가한다.

👉 [실습(Python)에서 확인하기](./lab-15)
:::
