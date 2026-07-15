# 문제 4 · 로그미분법 — $x^{\sin x}$

::: info 문제 4 [2점]
다음 함수를 미분하시오.

$$
f(x)=x^{\sin x}
$$
:::

::: details 풀이 및 해설
밑과 지수에 모두 $x$가 들어 있으므로 로그미분법<span class="gloss">logarithmic differentiation</span>을 사용한다. 양변에 자연로그를 취하면

$$
\ln f(x)=\sin x\cdot\ln x.
$$

양변을 $x$에 대해 미분한다. 좌변은 연쇄법칙으로 $\dfrac{f'(x)}{f(x)}$, 우변은 곱의 미분법으로

$$
\frac{f'(x)}{f(x)}=\cos x\cdot\ln x+\sin x\cdot\frac{1}{x}.
$$

양변에 $f(x)=x^{\sin x}$ 를 곱하면

$$
\boxed{\;f'(x)=x^{\sin x}\left(\cos x\,\ln x+\frac{\sin x}{x}\right)\;}
$$

👉 [실습(Python)에서 확인하기](./lab-04)
:::
