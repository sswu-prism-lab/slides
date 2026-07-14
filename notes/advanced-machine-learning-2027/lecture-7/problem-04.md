# 문제 4 · 최대가능도추정

::: info 문제 4 — 최대가능도추정
우리가 관찰한 데이터가 가우시안 분포<span class="gloss">Gaussian distribution</span>로부터 독립적이고 동일하게 분포<span class="gloss">independently and identically distributed</span>되었다고 가정하자.

$$
p(x_n)\sim\mathcal{N}(x_n\mid\mu,\sigma^2)
$$

이 때 가능도<span class="gloss">likelihood</span> 함수를 정의하고, 데이터가 추출된 가우시안 분포의 평균과 분산값을 최대가능도추정<span class="gloss">maximum likelihood estimation</span> 방법을 이용하여 구하라. 또한, 구한 결과가 과적합<span class="gloss">overfitting</span> 현상에 미치는 영향에 대해 서술하여라.

---

가우시안 분포의 정의를 사용하고, 가능도 함수에 로그를 취한 결과를 사용하여야 한다.

$$
\mathcal{N}(x_n\mid\mu,\sigma^2)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x_n-\mu)^2}{2\sigma^2}\right)
$$
:::

::: details 풀이 및 해설
**가능도 함수** — 데이터 $\mathbf{x}=\{x_1,\ldots,x_N\}$가 i.i.d.이므로 결합 확률은 곱으로 쓰인다.

$$
p(\mathbf{x}\mid\mu,\sigma^2)=\prod_{n=1}^{N}\mathcal{N}(x_n\mid\mu,\sigma^2)
$$

**로그 가능도** — 곱을 합으로 바꾸기 위해 로그를 취한다.

$$
\ln p(\mathbf{x}\mid\mu,\sigma^2)=-\frac{1}{2\sigma^2}\sum_{n=1}^{N}(x_n-\mu)^2-\frac{N}{2}\ln\sigma^2-\frac{N}{2}\ln(2\pi)
$$

**평균** — $\mu$에 대해 미분하여 $0$으로 둔다.

$$
\frac{\partial}{\partial\mu}\ln p=\frac{1}{\sigma^2}\sum_{n=1}^{N}(x_n-\mu)=0
\quad\Longrightarrow\quad
\boxed{\ \mu_{\mathrm{ML}}=\frac{1}{N}\sum_{n=1}^{N}x_n\ }
$$

**분산** — $\sigma^2$에 대해 미분하여 $0$으로 둔다.

$$
\frac{\partial}{\partial\sigma^2}\ln p=\frac{1}{2\sigma^4}\sum_{n=1}^{N}(x_n-\mu)^2-\frac{N}{2\sigma^2}=0
\quad\Longrightarrow\quad
\boxed{\ \sigma^2_{\mathrm{ML}}=\frac{1}{N}\sum_{n=1}^{N}(x_n-\mu_{\mathrm{ML}})^2\ }
$$

**과적합과의 관계** — 두 추정량의 기댓값을 구하면 평균은 불편(unbiased)이지만 분산은 편향(biased)되어 있다.

$$
\mathbb{E}[\mu_{\mathrm{ML}}]=\mu,\qquad
\mathbb{E}[\sigma^2_{\mathrm{ML}}]=\frac{N-1}{N}\,\sigma^2<\sigma^2
$$

즉 최대가능도 분산은 참 분산을 **과소추정**한다. 이는 같은 데이터로 평균 $\mu_{\mathrm{ML}}$을 먼저 추정한 뒤 그 평균을 다시 분산 계산에 사용하기 때문으로, 모델이 학습 데이터에 지나치게 맞춰지는 과적합의 한 단면이다. 불편 추정을 원하면 $\tilde{\sigma}^2=\frac{N}{N-1}\sigma^2_{\mathrm{ML}}=\frac{1}{N-1}\sum_n (x_n-\mu_{\mathrm{ML}})^2$로 보정한다. 데이터 수 $N$이 커질수록 편향 $\frac{N-1}{N}\to 1$이 되어 사라진다.
:::
