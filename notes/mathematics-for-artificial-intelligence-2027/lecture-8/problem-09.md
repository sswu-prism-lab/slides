# 문제 9 · 포아송분포

::: info 문제 9 [2점]
어떤 도시에서 평균적으로 1년에 $7$번의 폭우가 내린다고 하자. 이번 해에 폭우가 $5$번 내릴 확률 $P(\text{heavy rain}=5)$과 $9$번 내릴 확률 $P(\text{heavy rain}=9)$의 대소 관계를 비교하시오.
:::

::: details 풀이 및 해설
연간 폭우 횟수 $X$는 평균 $\lambda=7$인 포아송분포<span class="gloss">Poisson distribution</span>를 따릅니다.

$$
P(X=k) = \frac{e^{-\lambda}\lambda^{k}}{k!} = \frac{e^{-7}\,7^{k}}{k!}.
$$

두 확률의 비를 계산하면 공통 인자 $e^{-7}$이 소거됩니다.

$$
\frac{P(X=5)}{P(X=9)} = \frac{7^{5}/5!}{7^{9}/9!} = \frac{9!}{5!\cdot 7^{4}} = \frac{9\cdot 8\cdot 7\cdot 6}{7^{4}} = \frac{3024}{2401} \approx 1.259 > 1.
$$

따라서 $P(X=5)>P(X=9)$입니다. 실제 값은

$$
P(X=5)\approx 0.1277,\qquad P(X=9)\approx 0.1014.
$$

$$
\boxed{\,P(X=5) > P(X=9)\,}
$$

평균 $7$에서 거리가 가까운 $5$가 더 먼 $9$보다 확률이 큽니다.

👉 [실습(Python)에서 확인하기](./lab-09)
:::
