# 문제 8 · 매개변수 미분 $dy/dx$

::: info 문제 8 [3점]
다음과 같이 함수 $x(t)$와 $y(t)$가 정의될 때, $dy/dx$를 구하시오.

$$
x(t)=t^2+\sin t,\qquad y(t)=e^{t^3}
$$
:::

::: details 풀이 및 해설
매개변수<span class="gloss">parameter</span> $t$로 주어진 곡선에서는 연쇄법칙에 의해

$$
\frac{dy}{dx}=\frac{dy/dt}{dx/dt}
$$

가 성립한다($dx/dt\neq0$ 인 곳에서).

**각 도함수** —

$$
\frac{dx}{dt}=2t+\cos t,\qquad
\frac{dy}{dt}=e^{t^3}\cdot 3t^2=3t^2 e^{t^3}.
$$

따라서

$$
\boxed{\;\frac{dy}{dx}=\frac{3t^2 e^{t^3}}{2t+\cos t}\;}
$$

👉 [실습(Python)에서 확인하기](./lab-08)
:::
