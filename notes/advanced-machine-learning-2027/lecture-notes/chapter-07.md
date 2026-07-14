# 7 · 혼합 모델과 EM

> 관측 변수와 잠재 변수의 결합 분포를 정의하면, 복잡한 관측 변수의 주변 분포를 상대적으로 더 다루기 쉬운 확장 공간(관측+잠재)의 결합 분포로 표현할 수 있다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/photos/sec07.png" style="max-width:34rem;" />
</div>

## 7.1 $K$ 평균 집단화

- $D$차원 데이터 $\{\mathbf{x}_1,\ldots,\mathbf{x}_N\}$을 $K$개 집단으로 나누는 문제에서, 각 집단의 **원형**<span class="gloss">prototype</span>(중심) $\boldsymbol{\mu}_k$와 이진 표시 변수 $r_{nk}\in\{0,1\}$(원 핫)을 도입한다. 목표는 각 점에서 가장 가까운 중심까지의 거리 제곱합인 **뒤틀림 척도**<span class="gloss">distortion measure</span>를 최소화하는 것이다.

$$
J=\sum_{n=1}^N\sum_{k=1}^K r_{nk}\|\mathbf{x}_n-\boldsymbol{\mu}_k\|^2
$$

- $J$를 두 단계로 번갈아 최소화한다. **E 단계**에서 $\boldsymbol{\mu}_k$를 고정하고 각 점을 가장 가까운 중심에 할당하고($r_{nk}=1$ if $k=\arg\min_j\|\mathbf{x}_n-\boldsymbol{\mu}_j\|^2$), **M 단계**에서 $r_{nk}$를 고정하고 중심을 갱신한다.

$$
\boldsymbol{\mu}_k=\frac{\sum_n r_{nk}\mathbf{x}_n}{\sum_n r_{nk}}
$$

  즉 집단 $k$에 할당된 점들의 평균이다. 이를 **$K$-평균**<span class="gloss">K-means</span> 알고리즘이라 하며, 제곱 유클리드 거리 대신 일반 거리 $\mathcal{V}(\cdot,\cdot)$를 쓰면 **$K$-메도이드**<span class="gloss">K-medoids</span>가 된다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.1a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.1b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.1c.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.1d.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.1e.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.1f.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.1g.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.1h.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.1i.png" />
</div>
<div class="cap">

그림 7.1 · (a) 데이터와 두 초기 중심(적·청 $\times$). (b) E 단계: 각 점을 가까운 중심에 할당. (c) M 단계: 중심 재계산. (d)~(i) 수렴까지 EM 반복.

</div>
</div>

::: tip 실습 · $K$-평균 집단화
E 단계(가까운 중심에 할당)와 M 단계(중심을 집단 평균으로 갱신)를 번갈아 반복하며, 뒤틀림 척도 $J$가 단조 감소해 수렴하는 것을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)
X = np.vstack([rng.normal([0,0], 0.6, (80,2)),
               rng.normal([3,3], 0.6, (80,2)),
               rng.normal([0,3], 0.6, (80,2))])
K = 3; mu = X[rng.choice(len(X), K, replace=False)].copy()
prev = None
for it in range(12):
    d = ((X[:,None,:]-mu[None,:,:])**2).sum(2); r = d.argmin(1)     # E: 할당
    J = d[np.arange(len(X)), r].sum()
    for k in range(K):
        if (r==k).any(): mu[k] = X[r==k].mean(0)                    # M: 중심 갱신
    print(f"반복 {it+1}: J={J:.2f}")
    if prev is not None and abs(J-prev) < 1e-9: break
    prev = J
```

</PyRunner>

## 7.2 혼합 가우시안

- 가우시안 혼합은 가우시안들의 선형 중첩이다.

$$
p(\mathbf{x})=\sum_{k=1}^K\pi_k\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k) \tag{9.7}
$$

- 원 핫 잠재 변수 $\mathbf{z}$($z_k\in\{0,1\}$, $\sum_k z_k=1$)를 도입해 $p(z_k=1)=\pi_k$, 즉 $p(\mathbf{z})=\prod_k\pi_k^{z_k}$로 두고, 조건부 분포를 $p(\mathbf{x}\mid\mathbf{z})=\prod_k\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)^{z_k}$로 두면, $\mathbf{z}$를 주변화해 (9.7)을 얻는다. $\mathbf{x}$가 주어졌을 때 성분 $k$의 사후 확률(**책임**<span class="gloss">responsibility</span>)은

$$
\gamma(z_k)\equiv p(z_k=1\mid\mathbf{x})=\frac{\pi_k\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)}{\sum_{j=1}^K\pi_j\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_j,\boldsymbol{\Sigma}_j)}
$$

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.5a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.5b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.5c.png" />
</div>
<div class="cap">

그림 7.2 · (a) 결합 분포 $p(\mathbf{z})p(\mathbf{x}\mid\mathbf{z})$의 표본. (b) 주변 분포 $p(\mathbf{x})$의 표본. (c) 책임값 $\gamma(z_{nk})$로 색칠한 점들.

</div>
</div>

### 7.2.1 최대 가능도 방법

- 로그 가능도는 다음과 같다.

$$
\ln p(\mathbf{X}\mid\boldsymbol{\pi},\boldsymbol{\mu},\boldsymbol{\Sigma})=\sum_{n=1}^N\ln\Bigl\{\sum_{k=1}^K\pi_k\mathcal{N}(\mathbf{x}_n\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)\Bigr\} \tag{9.14}
$$

- 최대 가능도는 **특이점**<span class="gloss">singularity</span> 문제를 갖는다. 어떤 성분이 한 데이터 포인트로 붕괴하면 $\sigma_j\to0$이 되어 로그 가능도가 무한대로 발산한다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.6.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.7.png" />
</div>
<div class="cap">

그림 7.3·7.4 · (왼쪽) $N$개 데이터에 대한 가우시안 혼합의 그래프 표현($\{\mathbf{z}_n\}$은 잠재). (오른쪽) 한 성분이 데이터 포인트로 붕괴해 특이점이 생기는 모습.

</div>
</div>

### 7.2.2 가우시안 혼합 분포에 대한 EM

- (9.14)를 $\boldsymbol{\mu}_k$, $\boldsymbol{\Sigma}_k$, $\pi_k$에 대해 미분해 $0$으로 두면(마지막은 $\sum_k\pi_k=1$ 제약에 라그랑주 승수) 다음을 얻는다($N_k=\sum_n\gamma(z_{nk})$는 성분 $k$의 유효 데이터 수).

$$
\boldsymbol{\mu}_k=\frac{1}{N_k}\sum_{n=1}^N\gamma(z_{nk})\mathbf{x}_n \tag{9.17}
$$

$$
\boldsymbol{\Sigma}_k=\frac{1}{N_k}\sum_{n=1}^N\gamma(z_{nk})(\mathbf{x}_n-\boldsymbol{\mu}_k)(\mathbf{x}_n-\boldsymbol{\mu}_k)^{\top},\qquad
\pi_k=\frac{N_k}{N} \tag{9.19}
$$

- 이 식들은 책임값 $\gamma(z_{nk})$가 매개변수에 복잡하게 의존하므로 닫힌 형태의 해가 아니다. 대신 E 단계(현재 매개변수로 책임값 계산)와 M 단계(책임값으로 매개변수 재추정)를 번갈아 반복한다. 보통 $K$-평균으로 초기화한 뒤 EM을 적용한다.

::: info 가우시안 혼합 분포에 대한 EM 알고리즘
1. 평균 $\boldsymbol{\mu}_k$, 공분산 $\boldsymbol{\Sigma}_k$, 혼합 계수 $\pi_k$를 초기화하고 로그 가능도를 계산한다.

2. **E 단계** — 책임값을 계산한다.

$$
\gamma(z_{nk})=\frac{\pi_k\mathcal{N}(\mathbf{x}_n\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)}{\sum_{j=1}^K\pi_j\mathcal{N}(\mathbf{x}_n\mid\boldsymbol{\mu}_j,\boldsymbol{\Sigma}_j)}
$$

3. **M 단계** — 매개변수를 재추정한다($N_k=\sum_n\gamma(z_{nk})$).

$$
\boldsymbol{\mu}_k^{\mathrm{new}}=\frac{1}{N_k}\sum_n\gamma(z_{nk})\mathbf{x}_n,\quad
\boldsymbol{\Sigma}_k^{\mathrm{new}}=\frac{1}{N_k}\sum_n\gamma(z_{nk})(\mathbf{x}_n-\boldsymbol{\mu}_k^{\mathrm{new}})(\mathbf{x}_n-\boldsymbol{\mu}_k^{\mathrm{new}})^{\top},\quad
\pi_k^{\mathrm{new}}=\frac{N_k}{N}
$$

4. 로그 가능도를 계산하고, 수렴하지 않았으면 2단계로 돌아간다.
:::

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.8a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.8b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.8c.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.8d.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.8e.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.8f.png" />
</div>
<div class="cap">

그림 7.5 · (a) 초기 두 성분. (b) 최초 E 단계 후 책임값으로 색칠. (c) 최초 M 단계 후 평균·공분산 갱신. (d)~(f) 2·5·20단계 후, (f)에서 거의 수렴.

</div>
</div>

::: tip 실습 · 가우시안 혼합 EM
E 단계(책임값 $\gamma$ 계산)와 M 단계($\boldsymbol{\mu},\boldsymbol{\Sigma},\pi$ 재추정)를 반복하며 로그 가능도가 단조 증가해 수렴하고, 참 평균·혼합 계수를 회복하는 것을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
def gauss(X, mu, S):
    D = X.shape[1]; d = X-mu; Si = np.linalg.inv(S)
    return np.exp(-0.5*np.einsum('ni,ij,nj->n', d, Si, d))/np.sqrt((2*np.pi)**D*np.linalg.det(S))
rng = np.random.default_rng(1)
X = np.vstack([rng.multivariate_normal([0,0], [[0.5,0],[0,0.5]], 120),
               rng.multivariate_normal([3,3], [[0.6,0.3],[0.3,0.6]], 120)])
K = 2; N = len(X)
mu = X[rng.choice(N, K, replace=False)].copy(); S = [np.eye(2) for _ in range(K)]; pi = np.ones(K)/K
prev = -np.inf
for it in range(40):
    R = np.stack([pi[k]*gauss(X, mu[k], S[k]) for k in range(K)], 1)     # E 단계
    ll = np.log(R.sum(1)).sum(); R = R/R.sum(1, keepdims=True)
    Nk = R.sum(0)
    for k in range(K):                                                    # M 단계
        mu[k] = (R[:,k,None]*X).sum(0)/Nk[k]
        d = X-mu[k]; S[k] = (R[:,k,None,None]*np.einsum('ni,nj->nij', d, d)).sum(0)/Nk[k]
    pi = Nk/N
    if it < 4 or it % 6 == 0: print(f"반복 {it+1:2d}: 로그가능도={ll:.2f}")
    if ll-prev < 1e-6: print(f"수렴 (반복 {it+1})"); break
    prev = ll
print("추정 π:", np.round(pi,3).tolist(), " 평균:", np.round(mu,2).tolist())
```

</PyRunner>

## 7.3 EM에 대한 다른 관점

- 관측 데이터 $\mathbf{X}$, 잠재 변수 $\mathbf{Z}$, 매개변수 $\boldsymbol{\theta}$에 대해 로그 가능도는 $\ln p(\mathbf{X}\mid\boldsymbol{\theta})=\ln\{\sum_{\mathbf{Z}}p(\mathbf{X},\mathbf{Z}\mid\boldsymbol{\theta})\}$이다. $\{\mathbf{X},\mathbf{Z}\}$를 **완전한**<span class="gloss">complete</span> 데이터, $\mathbf{X}$만을 **불완전한**<span class="gloss">incomplete</span> 데이터라 한다. 잠재 변수에 대한 지식은 사후 분포 $p(\mathbf{Z}\mid\mathbf{X},\boldsymbol{\theta})$로만 주어진다.

::: info 일반적인 EM 알고리즘
결합 분포 $p(\mathbf{X},\mathbf{Z}\mid\boldsymbol{\theta})$에서 가능도 $p(\mathbf{X}\mid\boldsymbol{\theta})$를 $\boldsymbol{\theta}$에 대해 최대화한다.

1. $\boldsymbol{\theta}^{\mathrm{old}}$를 초기화한다.

2. **E 단계** — 사후 분포 $p(\mathbf{Z}\mid\mathbf{X},\boldsymbol{\theta}^{\mathrm{old}})$를 계산한다.

3. **M 단계** — 완전 데이터 로그 가능도의 기댓값을 최대화한다.

$$
\boldsymbol{\theta}^{\mathrm{new}}=\underset{\boldsymbol{\theta}}{\arg\max}\ \mathcal{Q}(\boldsymbol{\theta},\boldsymbol{\theta}^{\mathrm{old}}),\qquad
\mathcal{Q}(\boldsymbol{\theta},\boldsymbol{\theta}^{\mathrm{old}})=\sum_{\mathbf{Z}}p(\mathbf{Z}\mid\mathbf{X},\boldsymbol{\theta}^{\mathrm{old}})\ln p(\mathbf{X},\mathbf{Z}\mid\boldsymbol{\theta})
$$

4. 수렴하지 않으면 $\boldsymbol{\theta}^{\mathrm{old}}\leftarrow\boldsymbol{\theta}^{\mathrm{new}}$로 두고 2단계로 돌아간다.
:::

### 7.3.1 베르누이 분포들의 혼합

- 이진 변수들에 대한 베르누이 혼합(**잠재 클래스 분석**<span class="gloss">latent class analysis</span>)을 생각하자. 각 성분은 $p(\mathbf{x}\mid\boldsymbol{\mu}_k)=\prod_{i=1}^D\mu_{ki}^{x_i}(1-\mu_{ki})^{1-x_i}$이고 혼합은 $p(\mathbf{x}\mid\boldsymbol{\mu},\boldsymbol{\pi})=\sum_k\pi_k p(\mathbf{x}\mid\boldsymbol{\mu}_k)$이다. 책임값과 M 단계는

$$
\gamma(z_{nk})=\frac{\pi_k p(\mathbf{x}_n\mid\boldsymbol{\mu}_k)}{\sum_{j=1}^K\pi_j p(\mathbf{x}_n\mid\boldsymbol{\mu}_j)},\qquad
\boldsymbol{\mu}_k=\overline{\mathbf{x}}_k=\frac{1}{N_k}\sum_n\gamma(z_{nk})\mathbf{x}_n,\qquad
\pi_k=\frac{N_k}{N}
$$

  가우시안 혼합과 달리 $\mu_{ki}\in(0,1)$이라 특이점이 생기지 않는다.

::: tip 실습 · 베르누이 혼합 EM (이진 데이터 군집화)
두 이진 원형 패턴에서 생성한 잡음 섞인 데이터를 베르누이 혼합 EM으로 군집화하면, 각 성분의 $\boldsymbol{\mu}_k$가 원래 패턴을 회복하는 것을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(2)
proto = np.array([[1,1,1,0,0,0], [0,0,0,1,1,1]], float)     # 두 원형 패턴
X = np.vstack([(rng.uniform(size=(60,6)) < 0.85*proto[0]+0.05).astype(float),
               (rng.uniform(size=(60,6)) < 0.85*proto[1]+0.05).astype(float)])
K = 2; N, D = X.shape
mu = rng.uniform(0.25, 0.75, (K, D)); pi = np.ones(K)/K; prev = -np.inf
def bern(X, mu):                                             # p(x|μ_k), (N,K)
    return np.prod(mu**X[:,None,:]*(1-mu)**(1-X[:,None,:]), 2)
for it in range(60):
    P = pi*bern(X, mu); ll = np.log(P.sum(1)).sum(); R = P/P.sum(1, keepdims=True)   # E
    Nk = R.sum(0); mu = (R.T@X)/Nk[:,None]; pi = Nk/N                                # M
    if ll-prev < 1e-7: break
    prev = ll
print(f"수렴 (반복 {it+1}), 로그가능도={ll:.2f}")
print("성분1 μ:", np.round(mu[0], 2).tolist())
print("성분2 μ:", np.round(mu[1], 2).tolist())
```

</PyRunner>

### 7.3.2 베이지안 선형 회귀에 대한 EM

- 베이지안 선형 회귀에서 가중치 $\mathbf{w}$를 잠재 변수로 보면 초매개변수 $\alpha$, $\beta$를 EM으로 추정할 수 있다. $\mathbf{w}$의 사후 분포에 대한 완전 데이터 로그 가능도의 기댓값을 $\alpha$에 대해 최대화하면

$$
\alpha=\frac{M}{\mathbb{E}[\mathbf{w}^{\top}\mathbf{w}]}=\frac{M}{\mathbf{m}_N^{\top}\mathbf{m}_N+\operatorname{Tr}(\mathbf{S}_N)}
$$

  $\mathbf{m}_N$·$\mathbf{S}_N$은 사후 분포의 평균·공분산이며, $\beta$도 비슷하게 재추정한다.

## 7.4 일반적 EM 알고리즘

- 잠재 변수 분포 $q(\mathbf{Z})$를 도입하면 로그 가능도가 다음처럼 분해된다.

$$
\ln p(\mathbf{X}\mid\boldsymbol{\theta})=\mathcal{L}(q,\boldsymbol{\theta})+\mathrm{KL}(q\|p) \tag{9.70}
$$

$$
\mathcal{L}(q,\boldsymbol{\theta})=\sum_{\mathbf{Z}}q(\mathbf{Z})\ln\frac{p(\mathbf{X},\mathbf{Z}\mid\boldsymbol{\theta})}{q(\mathbf{Z})},\qquad
\mathrm{KL}(q\|p)=-\sum_{\mathbf{Z}}q(\mathbf{Z})\ln\frac{p(\mathbf{Z}\mid\mathbf{X},\boldsymbol{\theta})}{q(\mathbf{Z})}
$$

- $\mathrm{KL}(q\|p)\geqslant0$이므로 $\mathcal{L}(q,\boldsymbol{\theta})$는 로그 가능도의 **하한**이다. EM은 이 하한을 두 단계로 올린다. **E 단계**에서 $\boldsymbol{\theta}^{\mathrm{old}}$를 고정하고 $q(\mathbf{Z})=p(\mathbf{Z}\mid\mathbf{X},\boldsymbol{\theta}^{\mathrm{old}})$로 두면 $\mathrm{KL}=0$이 되어 하한이 로그 가능도와 같아진다. **M 단계**에서 $q$를 고정하고 $\mathcal{L}(q,\boldsymbol{\theta})$를 $\boldsymbol{\theta}$에 대해 최대화하면, 하한이 오르고 로그 가능도도 최소한 그만큼 오른다(이때 $q$가 새 사후 분포와 달라져 $\mathrm{KL}>0$).

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.11.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.12.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure9.13.png" />
</div>
<div class="cap">

그림 7.6~7.8 · (왼쪽) $\ln p(\mathbf{X})=\mathcal{L}(q,\boldsymbol{\theta})+\mathrm{KL}(q\|p)$ 분해. (가운데) E 단계: $q$를 사후 분포로 두어 $\mathrm{KL}=0$. (오른쪽) M 단계: $q$ 고정, $\boldsymbol{\theta}$ 최대화로 하한 상승.

</div>
</div>

::: tip 실습 · ELBO 분해 $\ln p(\mathbf{X})=\mathcal{L}(q,\boldsymbol{\theta})+\mathrm{KL}(q\|p)$
가우시안 혼합의 한 스냅샷에서, 임의의 $q$에 대해 $\mathcal{L}+\mathrm{KL}$이 로그 가능도와 같음을, 그리고 $q$를 사후 분포로 두면 $\mathrm{KL}=0$이 되어 $\mathcal{L}$이 로그 가능도와 일치함을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
def gauss(X, mu, S):
    D = X.shape[1]; d = X-mu; Si = np.linalg.inv(S)
    return np.exp(-0.5*np.einsum('ni,ij,nj->n', d, Si, d))/np.sqrt((2*np.pi)**D*np.linalg.det(S))
rng = np.random.default_rng(3)
X = np.vstack([rng.multivariate_normal([0,0], np.eye(2)*0.4, 50),
               rng.multivariate_normal([2.5,2.5], np.eye(2)*0.4, 50)])
K = 2; mu = np.array([[0.5,0.0],[2.0,2.0]]); S = [np.eye(2)*0.5]*2; pi = np.array([0.5,0.5])
px = np.stack([pi[k]*gauss(X, mu[k], S[k]) for k in range(K)], 1)
lnpX = np.log(px.sum(1)).sum()
post = px/px.sum(1, keepdims=True)                          # 사후 분포
def elbo(q):
    L = KL = 0.0
    for k in range(K):
        m = q[:,k] > 1e-12
        L  += np.sum(q[m,k]*(np.log(px[m,k]) - np.log(q[m,k])))
        KL += np.sum(q[m,k]*(np.log(q[m,k]) - np.log(post[m,k])))
    return L, KL
Lb, KLb = elbo(np.full_like(post, 0.5))                     # 임의의 q
Lg, KLg = elbo(post)                                        # q = 사후 분포
print(f"ln p(X)           = {lnpX:.3f}")
print(f"임의 q : L={Lb:.3f}, KL={KLb:.3f}, L+KL={Lb+KLb:.3f}")
print(f"q=사후 : L={Lg:.3f}, KL={KLg:.3f}, L+KL={Lg+KLg:.3f}  (KL≈0 → L=ln p(X))")
```

</PyRunner>

## 연습문제

::: info 문제 7.1
잠재 변수의 주변 분포가 (9.10) $p(\mathbf{z})=\prod_k\pi_k^{z_k}$, 조건부 분포가 (9.11) $p(\mathbf{x}\mid\mathbf{z})=\prod_k\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)^{z_k}$일 때, $\sum_{\mathbf{z}}p(\mathbf{z})p(\mathbf{x}\mid\mathbf{z})$가 (9.7)의 가우시안 혼합임을 보여라.
:::

::: details 풀이
$\mathbf{z}$는 원 핫이므로 정확히 한 성분만 $1$이고, 가능한 상태는 $\mathbf{z}=\mathbf{e}_k$($k$번째만 $1$), $k=1,\ldots,K$의 $K$가지다. 각 상태에서

$$
p(\mathbf{z}=\mathbf{e}_k)=\prod_{j=1}^K\pi_j^{z_j}=\pi_k,\qquad
p(\mathbf{x}\mid\mathbf{z}=\mathbf{e}_k)=\prod_{j=1}^K\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_j,\boldsymbol{\Sigma}_j)^{z_j}=\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)
$$

($z_j=0$인 항은 $\pi_j^0=1$, $\mathcal{N}^0=1$이라 사라진다). 모든 상태에 대해 합하면

$$
\sum_{\mathbf{z}}p(\mathbf{z})p(\mathbf{x}\mid\mathbf{z})=\sum_{k=1}^K p(\mathbf{z}=\mathbf{e}_k)\,p(\mathbf{x}\mid\mathbf{z}=\mathbf{e}_k)=\sum_{k=1}^K\pi_k\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)
$$

이는 정확히 (9.7)의 가우시안 혼합이다. $\blacksquare$
:::

::: info 문제 7.2
혼합 밀도 $p(\mathbf{x})=\sum_{k=1}^K\pi_k p(\mathbf{x}\mid k)$에서 $\mathbf{x}=(\mathbf{x}_a,\mathbf{x}_b)$로 나눌 때, 조건부 밀도 $p(\mathbf{x}_b\mid\mathbf{x}_a)$가 그 자체로 혼합 분포임을 보이고 혼합 계수와 성분 밀도를 구하라.
:::

::: details 풀이
조건부 분포의 정의에서

$$
p(\mathbf{x}_b\mid\mathbf{x}_a)=\frac{p(\mathbf{x}_a,\mathbf{x}_b)}{p(\mathbf{x}_a)}=\frac{\sum_{k=1}^K\pi_k\,p(\mathbf{x}_a,\mathbf{x}_b\mid k)}{\sum_{j=1}^K\pi_j\,p(\mathbf{x}_a\mid j)}
$$

성분 내에서 $p(\mathbf{x}_a,\mathbf{x}_b\mid k)=p(\mathbf{x}_b\mid\mathbf{x}_a,k)\,p(\mathbf{x}_a\mid k)$로 분해하면

$$
p(\mathbf{x}_b\mid\mathbf{x}_a)=\sum_{k=1}^K\underbrace{\frac{\pi_k\,p(\mathbf{x}_a\mid k)}{\sum_{j=1}^K\pi_j\,p(\mathbf{x}_a\mid j)}}_{\lambda_k}\;p(\mathbf{x}_b\mid\mathbf{x}_a,k)
$$

따라서 $p(\mathbf{x}_b\mid\mathbf{x}_a)$는 성분 밀도 $p(\mathbf{x}_b\mid\mathbf{x}_a,k)$와 혼합 계수

$$
\lambda_k=\frac{\pi_k\,p(\mathbf{x}_a\mid k)}{\sum_{j=1}^K\pi_j\,p(\mathbf{x}_a\mid j)}
$$

를 갖는 혼합 분포다. $\lambda_k\geqslant0$이고 $\sum_k\lambda_k=1$이므로 유효한 혼합 계수이며, 이는 $\mathbf{x}_a$를 관측한 뒤의 성분 사후 확률에 해당한다. $\blacksquare$
:::
