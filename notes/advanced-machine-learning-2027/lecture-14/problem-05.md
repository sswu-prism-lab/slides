# 문제 5 · 변분 추론 (ELBO 유도)

::: info 문제 5 — 변분 추론
완전 베이지안 모델의 잠재 변수 및 매개변수가 $\mathbf{Z}=\{\mathbf{z}_1,\ldots,\mathbf{z}_N\}$, 관측 변수가 $\mathbf{X}=\{\mathbf{x}_1,\ldots,\mathbf{x}_N\}$으로 주어졌을 때, 변분 추론에 사용되는 ELBO 목적 함수를 유도하고, ELBO 함수의 최댓값을 찾는 것이 어떤 의미를 가지는지 서술하시오.
:::

::: details 풀이 및 해설
**유도** — 임의의 변분 분포 $q(\mathbf{Z})$에 대해 로그 주변 가능도를 분해한다.

$$
\ln p(\mathbf{X})=\ln\int p(\mathbf{X},\mathbf{Z})\,\mathrm{d}\mathbf{Z}
=\ln\int q(\mathbf{Z})\frac{p(\mathbf{X},\mathbf{Z})}{q(\mathbf{Z})}\,\mathrm{d}\mathbf{Z}
$$

옌센 부등식을 적용하거나, 항을 더하고 빼서 정확히 분해하면

$$
\ln p(\mathbf{X})=\underbrace{\int q(\mathbf{Z})\ln\frac{p(\mathbf{X},\mathbf{Z})}{q(\mathbf{Z})}\,\mathrm{d}\mathbf{Z}}_{\displaystyle \mathcal{L}(q)\ \text{(ELBO)}}
+\underbrace{\left(-\int q(\mathbf{Z})\ln\frac{p(\mathbf{Z}\mid\mathbf{X})}{q(\mathbf{Z})}\,\mathrm{d}\mathbf{Z}\right)}_{\displaystyle \mathrm{KL}(q\,\|\,p(\mathbf{Z}\mid\mathbf{X}))}
$$

즉

$$
\boxed{\ \ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}\!\big(q(\mathbf{Z})\,\|\,p(\mathbf{Z}\mid\mathbf{X})\big)\ }
$$

여기서 ELBO(증거 하한, Evidence Lower BOund)는

$$
\mathcal{L}(q)=\mathbb{E}_q[\ln p(\mathbf{X},\mathbf{Z})]-\mathbb{E}_q[\ln q(\mathbf{Z})]
$$

**의미** — $\mathrm{KL}\geqslant0$이므로 $\mathcal{L}(q)\leqslant\ln p(\mathbf{X})$, 즉 ELBO는 로그 증거의 **하한**이다. 관측이 고정되면 $\ln p(\mathbf{X})$는 상수이므로,

$$
\mathcal{L}(q)\ \text{최대화}\quad\Longleftrightarrow\quad \mathrm{KL}\!\big(q\,\|\,p(\mathbf{Z}\mid\mathbf{X})\big)\ \text{최소화}
$$

가 된다. 따라서 ELBO를 최대화하는 것은 **다루기 어려운 참 사후분포 $p(\mathbf{Z}\mid\mathbf{X})$에 변분 분포 $q$를 가장 가깝게(KL 기준) 근사**하는 것을 의미하며, 동시에 로그 증거에 대한 가장 조인 하한을 얻는 것이다. 이로써 어려운 사후 추론 문제를 최적화 문제로 바꾼다.
:::
