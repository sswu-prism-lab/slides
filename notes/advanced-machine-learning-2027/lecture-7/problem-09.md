# 문제 9 · 라플라스 근사법

::: info 문제 9 — 라플라스 근사법
아래와 같은 형태의 확률밀도함수 $p(x)$가 주어졌다.

$$
p(x)=\frac{1}{Z}\exp(-3x^2-x^4),\quad -\infty<x<\infty,\qquad
Z=\int_{-\infty}^{\infty}\exp(-3x^2-x^4)\,\mathrm{d}x
$$

이 때, $p(x)$의 최빈값<span class="gloss">mode</span>을 구하고, 라플라스 근사법<span class="gloss">Laplace approximation</span>을 이용하여 정규화 상수 $Z$의 근삿값을 계산하라.

표준 가우시안 적분은 다음의 형태로 알려져 있다.

$$
\int_{-\infty}^{\infty}\exp\!\big(-a(x-b)^2\big)\,\mathrm{d}x=\sqrt{\frac{\pi}{a}},\quad (a>0)
$$

---

최빈값은 확률밀도가 최대가 되는 값이므로, 지수 부분 $-(3x^2+x^4)$가 최대(즉 $3x^2+x^4$가 최소)가 되는 점을 찾는다. $Z$ 근사는 지수부의 함수를 최솟값 근처에서 테일러 전개<span class="gloss">Taylor expansion</span>한 뒤 표준 가우시안 적분 형태로 정리하면 된다.
:::

::: details 풀이 및 해설
**최빈값** — $f(x)=3x^2+x^4$를 최소화한다.

$$
f'(x)=6x+4x^3=2x(3+2x^2)=0
$$

$3+2x^2>0$이므로 실근은 $x=0$뿐이다. $f''(x)=6+12x^2$, $f''(0)=6>0$이므로 $x_0=0$이 최소점, 즉 $p(x)$의 **최빈값은 $x_0=0$**이다.

**라플라스 근사** — 지수부 $-f(x)$를 최빈값 $x_0=0$ 근처에서 2차까지 전개한다. $f(0)=0$, $f'(0)=0$이므로

$$
f(x)\approx f(0)+\tfrac{1}{2}f''(0)(x-0)^2=\tfrac{1}{2}\cdot 6\cdot x^2=3x^2
$$

따라서 피적분 함수는 $\exp(-f(x))\approx\exp(-3x^2)$로 근사되고, 표준 가우시안 적분($a=3$)을 적용하면

$$
Z\approx\int_{-\infty}^{\infty}\exp(-3x^2)\,\mathrm{d}x=\sqrt{\frac{\pi}{3}}\approx \boxed{1.0233}
$$

**검증** — 수치 적분으로 얻은 참값은 $Z_{\text{true}}\approx 0.9617$이다. 라플라스 근사는 약 $6.4\%$ 과대추정하는데, 이는 무시한 $x^4$ 항이 봉우리 주변에서 밀도를 추가로 감쇠시키기 때문이다. 근사는 봉우리의 곡률만 반영하므로 꼬리가 실제보다 두꺼워져 $Z$를 다소 크게 잡는다.

👉 [실습(Python)에서 근사값과 수치적분 비교](./lab-09)
:::
