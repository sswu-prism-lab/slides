# 문제 1 · 시그모이드 함수의 그래프

::: info 문제 1 [1점]
아래 함수의 그래프를 그리시오. $x\to-\infty$, $x\to\infty$, $y$절편을 정확하게 표기하시오.

$$
y=(1+e^{-x})^{-1}
$$
:::

::: details 풀이 및 해설
주어진 함수는 시그모이드<span class="gloss">sigmoid</span> 함수 $y=\dfrac{1}{1+e^{-x}}$ 이다.

**극한 (수평 점근선)** — $x\to-\infty$ 이면 $e^{-x}\to\infty$ 이므로 분모가 발산하여

$$
\lim_{x\to-\infty} y = \frac{1}{1+\infty}=0.
$$

$x\to\infty$ 이면 $e^{-x}\to0$ 이므로

$$
\lim_{x\to\infty} y = \frac{1}{1+0}=1.
$$

따라서 $y=0$ 과 $y=1$ 이 수평 점근선<span class="gloss">horizontal asymptote</span>이다.

**$y$절편** — $x=0$ 을 대입하면

$$
y(0)=\frac{1}{1+e^{0}}=\frac{1}{2}.
$$

**단조성** — $y'=\dfrac{e^{-x}}{(1+e^{-x})^2}>0$ 이므로 함수는 항상 증가하며, $(0,\tfrac12)$ 을 중심으로 대칭인 S자 곡선을 그린다.

$$
\boxed{\;x\to-\infty:\ y\to0,\quad x\to\infty:\ y\to1,\quad y\text{절편}=\tfrac{1}{2}\;}
$$

그래프는 왼쪽에서 $y=0$ 에 붙어 오다가 $(0,\tfrac12)$ 을 지나 오른쪽에서 $y=1$ 에 수렴하는 완만한 S자 곡선이다.
:::
