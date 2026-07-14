# 문제 1 · 최대가능도추정

::: info 문제 1 [4점]
$N$개의 데이터가 아래 가우시안 분포로부터 독립적이고 동일하게 분포되었다고 가정한다. 이 때, 분포의 평균 $\mu$와 분산 $\sigma^2$을 최대 가능도<span class="gloss">maximum likelihood</span> 방법을 이용하여 추정하시오. 또한 이 결과가 과적합<span class="gloss">overfitting</span>에 미치는 영향을 서술하시오.

$$
p(x_n)\sim\mathcal{N}(x_n\mid\mu,\sigma^2)
$$
:::

::: details 풀이 및 해설
i.i.d. 가정에서 로그 가능도는

$$
\ln p(\mathbf{x}\mid\mu,\sigma^2)=-\frac{1}{2\sigma^2}\sum_{n=1}^{N}(x_n-\mu)^2-\frac{N}{2}\ln\sigma^2-\frac{N}{2}\ln(2\pi)
$$

$\mu$, $\sigma^2$로 각각 미분하여 $0$으로 두면

$$
\boxed{\ \mu_{\mathrm{ML}}=\frac{1}{N}\sum_{n=1}^{N}x_n\ },\qquad
\boxed{\ \sigma^2_{\mathrm{ML}}=\frac{1}{N}\sum_{n=1}^{N}(x_n-\mu_{\mathrm{ML}})^2\ }
$$

**과적합과의 관계** — 기댓값을 취하면

$$
\mathbb{E}[\mu_{\mathrm{ML}}]=\mu,\qquad \mathbb{E}[\sigma^2_{\mathrm{ML}}]=\frac{N-1}{N}\sigma^2<\sigma^2
$$

즉 분산 추정이 참값을 **과소추정**(편향)한다. 같은 데이터로 추정한 $\mu_{\mathrm{ML}}$을 분산 계산에 재사용하기 때문으로, 학습 데이터에 과하게 맞춰지는 과적합의 한 단면이다. $N$이 커지면 편향은 사라지며($\tfrac{N-1}{N}\to1$), 불편 추정은 $\tfrac{1}{N-1}\sum_n(x_n-\mu_{\mathrm{ML}})^2$로 얻는다.
:::
