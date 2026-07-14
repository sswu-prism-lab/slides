# 문제 8 · 변분 추론 (ELBO)

::: info 문제 8 [5점]
완전 베이지안 모델의 잠재 변수 및 매개변수가 $\mathbf{Z}=\{\mathbf{z}_1,\ldots,\mathbf{z}_N\}$, 관측 변수가 $\mathbf{X}=\{\mathbf{x}_1,\ldots,\mathbf{x}_N\}$으로 주어졌다. 변분 추론<span class="gloss">variational inference</span>에 사용되는 목적 함수를 유도하고, 이 목적 함수의 최댓값을 찾는 것이 어떤 의미를 가지는지 서술하시오.
:::

::: details 풀이 및 해설
임의의 변분 분포 $q(\mathbf{Z})$에 대해 로그 주변 가능도를 정확히 분해하면

$$
\ln p(\mathbf{X})=\underbrace{\mathbb{E}_q[\ln p(\mathbf{X},\mathbf{Z})]-\mathbb{E}_q[\ln q(\mathbf{Z})]}_{\displaystyle \mathcal{L}(q)\ \text{(ELBO)}}+\mathrm{KL}\!\big(q(\mathbf{Z})\,\|\,p(\mathbf{Z}\mid\mathbf{X})\big)
$$

$\mathrm{KL}\geqslant0$이므로 ELBO는 로그 증거의 **하한**이다. 관측이 고정되면 $\ln p(\mathbf{X})$가 상수이므로

$$
\mathcal{L}(q)\ \text{최대화}\ \Longleftrightarrow\ \mathrm{KL}\!\big(q\,\|\,p(\mathbf{Z}\mid\mathbf{X})\big)\ \text{최소화}
$$

즉 ELBO 최대화는 **다루기 어려운 참 사후분포에 변분 분포 $q$를 가장 가깝게(KL 기준) 근사**하는 것을 뜻하며, 어려운 사후 추론을 최적화 문제로 바꾼다.
:::
