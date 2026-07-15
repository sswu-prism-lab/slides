# 문제 6 · 역함수 구하기

::: info 문제 6 [2점]
함수 $f(x)=e^{2x+1}$의 역함수를 구하시오.
:::

::: details 풀이 및 해설
$y=f(x)=e^{2x+1}$ 로 놓고 $x$에 대해 푼다. 지수함수는 항상 양수이므로 $y>0$ 이며, 양변에 자연로그를 취하면

$$
\ln y=2x+1.
$$

$x$에 대해 정리하면

$$
x=\frac{\ln y-1}{2}.
$$

$x$와 $y$를 서로 바꾸어 역함수<span class="gloss">inverse function</span>를 표현하면

$$
\boxed{\;f^{-1}(x)=\frac{\ln x-1}{2}\quad(x>0)\;}
$$

검산하면 $f\big(f^{-1}(x)\big)=e^{2\cdot\frac{\ln x-1}{2}+1}=e^{\ln x}=x$ 로 확인된다.

👉 [실습(Python)에서 확인하기](./lab-06)
:::
