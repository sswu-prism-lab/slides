# 문제 6 · 라플라스 근사법

::: info 문제 6 [4점]
아래와 같은 확률 밀도함수가 주어졌을 때, 이 분포의 최빈값<span class="gloss">mode</span>을 구하고 최빈값에서 아래 함수의 라플라스 근사<span class="gloss">Laplace approximation</span>를 구하시오.

$$
p(\theta)\propto\exp\left(-\frac{(\theta-2)^4}{4}-(\theta-2)^2\right),\quad -\infty<\theta<\infty
$$
:::

::: details 풀이 및 해설
지수부를 $-g(\theta)$로 두면 $g(\theta)=\tfrac{(\theta-2)^4}{4}+(\theta-2)^2$. 치환 $u=\theta-2$로 두면 $g=\tfrac{u^4}{4}+u^2$.

**최빈값** — $g$를 최소화한다.

$$
g'(u)=u^3+2u=u(u^2+2)=0
$$

$u^2+2>0$이므로 실근은 $u=0$, 즉 **최빈값 $\theta_0=2$**.

**곡률** — $g''(u)=3u^2+2$, $g''(0)=2>0$이므로 최소점이 맞다.

**라플라스 근사** — 최빈값 주변에서 $g$를 2차까지 전개하면 $g(\theta)\approx g(2)+\tfrac{1}{2}g''(0)(\theta-2)^2=(\theta-2)^2$이므로

$$
p(\theta)\approx\exp\!\big(-(\theta-2)^2\big)\ \propto\ \mathcal{N}\!\left(\theta\,\middle|\,2,\ \tfrac{1}{2}\right)
$$

즉 가우시안 근사는 평균 $\theta_0=2$, 분산 $\sigma^2=1/g''(\theta_0)=\boxed{1/2}$인 정규분포 $q(\theta)=\mathcal{N}(\theta\mid2,\tfrac12)$이다.

👉 [실습(Python)에서 근사 곡선 비교](./lab-6)
:::
