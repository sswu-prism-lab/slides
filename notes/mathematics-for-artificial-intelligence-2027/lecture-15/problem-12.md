# 문제 12 · 이계 편미분

::: info 문제 12 [3점]
함수 $f(x,y)$에 대해 $\dfrac{\partial^2 f}{\partial x\,\partial y}$를 구하시오.

$$
f(x,y)=\sin(xy)+x^3y^2
$$
:::

::: details 풀이 및 해설
먼저 $y$에 대해 편미분<span class="gloss">partial derivative</span>한다. $x$는 상수로 취급한다.

$$
\frac{\partial f}{\partial y}=x\cos(xy)+2x^3 y.
$$

이제 이 결과를 $x$에 대해 편미분한다.

- $\dfrac{\partial}{\partial x}\big[x\cos(xy)\big]=\cos(xy)+x\cdot\big(-\sin(xy)\big)\cdot y=\cos(xy)-xy\sin(xy)$ (곱의 미분법과 연쇄법칙),
- $\dfrac{\partial}{\partial x}\big[2x^3 y\big]=6x^2 y.$

따라서

$$
\boxed{\;\frac{\partial^2 f}{\partial x\,\partial y}=\cos(xy)-xy\sin(xy)+6x^2 y\;}
$$

👉 [실습(Python)에서 확인하기](./lab-12)
:::
