# 문제 13 · 그래디언트

::: info 문제 13 [3점]
함수 $h(x,y,z)$에 대해 $\nabla h(1,2,3)$을 구하시오.

$$
h(x,y,z)=x^2+y^2+z^2
$$
:::

::: details 풀이 및 해설
그래디언트<span class="gloss">gradient</span>는 각 변수에 대한 편미분을 성분으로 갖는 벡터이다.

$$
\nabla h=\left(\frac{\partial h}{\partial x},\ \frac{\partial h}{\partial y},\ \frac{\partial h}{\partial z}\right)=(2x,\ 2y,\ 2z).
$$

점 $(1,2,3)$ 을 대입하면

$$
\nabla h(1,2,3)=(2\cdot1,\ 2\cdot2,\ 2\cdot3)=(2,\ 4,\ 6).
$$

$$
\boxed{\;\nabla h(1,2,3)=(2,\ 4,\ 6)\;}
$$

👉 [실습(Python)에서 확인하기](./lab-13)
:::
