# 2 · 확률 분포

> 확률 분포는 복잡한 모델을 만드는 데 중요한 역할을 한다. 핵심 문제 중 하나는, 관찰된 데이터가 주어졌을 때 그를 가장 잘 표현하는 확률 분포를 모델링하는 것이다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/photos/sec02.png" style="max-width:34rem;" />
</div>

## 2.1 이산 확률 변수

- 이진 **확률 변수**<span class="gloss">random variable</span> $x\in\{0,1\}$에서 $x=1$일 확률을 $\mu$로 두면 $p(x=1\mid\mu)=\mu$, $p(x=0\mid\mu)=1-\mu$이다. 이 분포를 **베르누이 분포**<span class="gloss">Bernoulli distribution</span>라 한다.

$$
\operatorname{Bern}(x\mid\mu)=\mu^x(1-\mu)^{1-x},\qquad \mathbb{E}[x]=\mu,\quad \operatorname{var}[x]=\mu(1-\mu)
$$

- 관측 $\mathcal{D}=\{x_1,\ldots,x_N\}$이 i.i.d.라면 로그 가능도는 $\ln p(\mathcal{D}\mid\mu)=\sum_n\{x_n\ln\mu+(1-x_n)\ln(1-\mu)\}$이고, $\sum_n x_n$을 통해서만 데이터에 의존한다(이는 **충분 통계량**<span class="gloss">sufficient statistic</span>). $\mu$로 미분하여 $0$으로 두면

$$
\mu_\mathrm{ML}=\frac{1}{N}\sum_{n=1}^{N}x_n \tag{2.7}
$$

  으로 **표본 평균**<span class="gloss">sample mean</span>이 된다.
- $N$개 중 $x=1$인 관측 수 $m$의 분포가 **이항 분포**<span class="gloss">binomial distribution</span>이다.

$$
\mathrm{Bin}(m\mid N,\mu)=\binom{N}{m}\mu^m(1-\mu)^{N-m},\qquad \mathbb{E}[m]=N\mu,\quad \operatorname{var}[m]=N\mu(1-\mu) \tag{2.8}
$$

### 2.1.1 베타 분포

- 베르누이에 베이지안적으로 접근하려면 $\mu$의 사전 분포 $p(\mu)$가 필요하다. 가능도가 $\mu^x(1-\mu)^{1-x}$ 꼴이므로, $\mu$와 $(1-\mu)$의 거듭제곱에 비례하는 사전 분포를 쓰면 사후 분포도 같은 함수 형태를 갖는다. 이 성질을 **켤레성**<span class="gloss">conjugacy</span>이라 한다.
- 사전 분포로 **베타 분포**<span class="gloss">beta distribution</span>를 쓴다.

$$
\mathrm{Beta}(\mu\mid a, b)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\mu^{a-1}(1-\mu)^{b-1},\qquad
\mathbb{E}[\mu]=\frac{a}{a+b},\quad \operatorname{var}[\mu]=\frac{ab}{(a+b)^2(a+b+1)} \tag{2.11}
$$

- 이항 가능도(2.8)에 베타 사전(2.11)을 곱하고 정규화하면($l=N-m$)

$$
p(\mu\mid m,l,a,b)\propto\mu^{m+a-1}(1-\mu)^{l+b-1} \tag{2.15}
$$

  으로 다시 베타 분포가 된다. 사후에서 $a$는 $m$만큼, $b$는 $l$만큼 증가하며, $a$·$b$는 각각 $x=1$·$x=0$의 **유효 관찰수**<span class="gloss">effective number of observation</span>로 해석된다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.3a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.3b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.3c.png" />
</div>
<div class="cap">그림 2.3 · 사전 $a=b=2$에 관측 하나($x=1$)를 반영하면 사후는 $a=3,b=2$인 베타 분포가 된다.</div>
</div>

- 관측 수가 늘수록 사후 분포는 더 뾰족해지고($a\to\infty$ 또는 $b\to\infty$면 분산 $\to0$) 불확실성이 꾸준히 감소한다. 이는 베이지안 학습의 일반적 성질로, 데이터를 하나씩 반영하는 **순차적**<span class="gloss">sequential</span> 학습이 자연스럽다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.2a.png" style="width:40%;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.2b.png" style="width:40%;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.2c.png" style="width:40%;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.2d.png" style="width:40%;" />
</div>
<div class="cap">그림 2.2 · 다양한 초매개변수 $a,b$에 따른 베타 분포.</div>
</div>

::: tip 실습 · 베타–이항 켤레와 순차적 사후 갱신
사전 $\mathrm{Beta}(2,2)$에 관측을 하나씩 반영하면 $a{+}{=}1$(성공) 또는 $b{+}{=}1$(실패)로 갱신되며, 분산이 줄어드는(불확실성 감소) 과정을 확인하세요.
:::

<PyRunner>

```python
a, b = 2.0, 2.0                          # 사전 Beta(2, 2)
def mv(a, b):
    m = a/(a+b); v = a*b/((a+b)**2*(a+b+1)); return m, v
obs = [1, 1, 0, 1, 1, 1, 0, 1]          # 순차 관측 (x=1 → a 증가)
m, v = mv(a, b)
print(f"사전 Beta(a=2, b=2):  평균={m:.3f}, 분산={v:.4f}")
for i, x in enumerate(obs, 1):
    a += x; b += 1-x                     # 켤레 갱신
    m, v = mv(a, b)
    print(f"관측 {i}개 후 Beta(a={a:.0f}, b={b:.0f}): 평균={m:.3f}, 분산={v:.4f}")
print("\n관측이 늘수록 분산이 줄어(사후가 뾰족해짐) 불확실성이 감소한다.")
```

</PyRunner>

## 2.2 다항 변수

- $K$개 값 중 하나를 취하는 이산 변수는 **원 핫 인코딩**<span class="gloss">one hot encoding</span>으로 $K$차원 벡터 $\mathbf{x}$($x_k$ 중 하나만 $1$)로 표현한다. $x_k=1$일 확률을 $\mu_k$라 하면 $p(\mathbf{x}\mid\boldsymbol{\mu})=\prod_k\mu_k^{x_k}$이고 $\sum_k\mu_k=1$, $\mathbb{E}[\mathbf{x}]=\boldsymbol{\mu}$이다.
- $N$개 관측의 가능도는 $p(\mathcal{D}\mid\boldsymbol{\mu})=\prod_k\mu_k^{m_k}$($m_k=\sum_n x_{nk}$, 충분 통계량)이다. 제약 $\sum_k\mu_k=1$ 하에 **라그랑주 승수**<span class="gloss">Lagrange multiplier</span> $\lambda$로 $\sum_k m_k\ln\mu_k+\lambda(\sum_k\mu_k-1)$을 최대화하면 $\mu_k=-m_k/\lambda$, 제약 대입 시 $\lambda=-N$이므로

$$
\mu_k^\text{ML}=\frac{m_k}{N}
$$

  ($x_k=1$인 관측의 비율)이 된다.
- $m_1,\ldots,m_K$의 결합 분포가 **다항 분포**<span class="gloss">multinomial distribution</span>이다.

$$
\operatorname{Mult}(m_1,\ldots,m_K\mid\boldsymbol{\mu}, N)=\binom{N}{m_1\,m_2\cdots m_K}\prod_{k=1}^{K}\mu_k^{m_k},\qquad \binom{N}{m_1\cdots m_K}=\frac{N!}{m_1!\cdots m_K!} \tag{2.23}
$$

### 2.2.1 디리클레 분포

- 다항 분포의 켤레 사전 분포가 **디리클레 분포**<span class="gloss">Dirichlet distribution</span>이다($0\le\mu_k\le1$, $\sum_k\mu_k=1$).

$$
\mathrm{Dir}(\boldsymbol{\mu}\mid\boldsymbol{\alpha})=\frac{\Gamma(\alpha_0)}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_K)}\prod_{k=1}^{K}\mu_k^{\alpha_k-1},\qquad \alpha_0=\sum_{k=1}^{K}\alpha_k \tag{2.25}
$$

- 가능도(2.23)를 곱하면 사후 분포 $p(\boldsymbol{\mu}\mid\mathcal{D},\boldsymbol{\alpha})\propto\prod_k\mu_k^{\alpha_k+m_k-1}$로 다시 디리클레 분포가 되어 순차적 성질을 가진다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.4.png" style="width:18rem;" />
<div class="cap">그림 2.4 · 세 변수 $\mu_1,\mu_2,\mu_3$에 대한 디리클레 분포는 $\sum_k\mu_k=1$ 제약으로 인해 단체<span class="gloss">simplex</span> 위로 제한된다.</div>
</div>

## 2.3 가우시안 분포

- 단일·다변량 가우시안 분포는 각각 다음과 같다($\boldsymbol{\mu}$: 평균, $\boldsymbol{\Sigma}$: 공분산).

$$
\mathcal{N}(x\mid\mu,\sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\!\left\{-\frac{(x-\mu)^2}{2\sigma^2}\right\},\quad
\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}, \boldsymbol{\Sigma})=\frac{1}{(2\pi)^{D/2}|\boldsymbol{\Sigma}|^{1/2}}\exp\!\left\{-\tfrac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right\}
$$

- **중심 극한 정리**<span class="gloss">central limit theorem</span>에 따라 여러 확률 변수의 합은 변수 수가 늘수록 가우시안에 가까워진다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.6a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.6b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.6c.png" />
</div>
<div class="cap">그림 2.6 · 균등분포 $N$개 값의 평균 히스토그램. $N$이 커질수록 가우시안 형태가 된다.</div>
</div>

::: tip 실습 · 중심 극한 정리
$[0,1]$ 균등분포 $N$개의 평균이 $N$이 커질수록 가우시안에 가까워지고, 분산이 $\tfrac{1}{12N}$로 줄어듦을 확인하세요.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)
trials = 200000
print("N개 균등분포 U(0,1)의 평균 분포:")
for N in [1, 2, 10]:
    m = rng.uniform(0, 1, (trials, N)).mean(1)
    print(f"  N={N:2d}: 표본평균={m.mean():.3f}(이론 0.5), 표본분산={m.var():.4f}(이론 {1/12/N:.4f})")
print("N이 커질수록 평균의 분포가 가우시안에 가까워진다(중심극한정리).")
```

</PyRunner>

- 가우시안의 기하는 지수부의 이차식 $\Delta^2=(\mathbf{x}-\boldsymbol{\mu})^\top\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})$로 드러난다. $\Delta$는 **마할라노비스 거리**<span class="gloss">Mahalanobis distance</span>이며, $\boldsymbol{\Sigma}=\mathbf{I}$이면 **유클리드 거리**<span class="gloss">Euclidean distance</span>가 된다.
- $\boldsymbol{\Sigma}$의 고유분해 $\boldsymbol{\Sigma}\mathbf{u}_i=\lambda_i\mathbf{u}_i$($\mathbf{u}_i$는 정규직교<span class="gloss">orthonormal</span>)를 쓰면 $\boldsymbol{\Sigma}=\sum_i\lambda_i\mathbf{u}_i\mathbf{u}_i^\top$, $\boldsymbol{\Sigma}^{-1}=\sum_i\frac{1}{\lambda_i}\mathbf{u}_i\mathbf{u}_i^\top$이고, $y_i=\mathbf{u}_i^\top(\mathbf{x}-\boldsymbol{\mu})$로 좌표를 바꾸면 $\Delta^2=\sum_i y_i^2/\lambda_i$이다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.7.png" style="width:18rem;" />
<div class="cap">그림 2.7 · 상수 밀도 타원의 축은 공분산의 고유벡터 $\mathbf{u}_i$, 축의 길이는 고윳값 $\lambda_i$로 정해진다.</div>
</div>

- 새 좌표 $\mathbf{y}=\mathbf{U}(\mathbf{x}-\boldsymbol{\mu})$에서 야코비안 $|\mathbf{J}|=1$, $|\boldsymbol{\Sigma}|^{1/2}=\prod_j\lambda_j^{1/2}$이므로 $p(\mathbf{y})=\prod_j\frac{1}{(2\pi\lambda_j)^{1/2}}\exp\{-y_j^2/2\lambda_j\}$로 **$D$개의 독립 단변량 가우시안의 곱**이 된다. 즉 고유벡터 축을 따라 인수분해된다.
- 큰 $D$에서 완전 공분산은 계산이 비싸므로 **대각 행렬**<span class="gloss">diagonal matrix</span> 공분산을 쓰기도 한다. 또 가우시안은 **단봉**<span class="gloss">unimodal</span> 분포라 **다봉**<span class="gloss">multimodal</span> 분포를 근사하지 못하는데, **잠재 변수**<span class="gloss">latent variable</span> 등으로 이를 해소한다.

### 2.3.1 조건부 가우시안 분포

- 결합 분포가 가우시안이면 조건부 분포와 주변 분포도 가우시안이다. $\mathbf{x}$를 $\mathbf{x}_a$(앞 $M$개)와 $\mathbf{x}_b$로 나누고, **정밀도 행렬**<span class="gloss">precision matrix</span> $\boldsymbol{\Lambda}=\boldsymbol{\Sigma}^{-1}$을 같은 방식으로 분할하면

$$
\boldsymbol{\Sigma}=\begin{pmatrix}\boldsymbol{\Sigma}_{aa}&\boldsymbol{\Sigma}_{ab}\\\boldsymbol{\Sigma}_{ba}&\boldsymbol{\Sigma}_{bb}\end{pmatrix},\qquad
\boldsymbol{\Lambda}=\begin{pmatrix}\boldsymbol{\Lambda}_{aa}&\boldsymbol{\Lambda}_{ab}\\\boldsymbol{\Lambda}_{ba}&\boldsymbol{\Lambda}_{bb}\end{pmatrix}
$$

- 지수부의 이차식에 **제곱식의 완성**<span class="gloss">completing the square</span>을 적용하면 조건부 분포 $p(\mathbf{x}_a\mid\mathbf{x}_b)$의 평균·공분산을 얻는다.

$$
\begin{aligned}
\boldsymbol{\mu}_{a\mid b}&=\boldsymbol{\mu}_a-\boldsymbol{\Lambda}_{aa}^{-1}\boldsymbol{\Lambda}_{ab}(\mathbf{x}_b-\boldsymbol{\mu}_b)=\boldsymbol{\mu}_a+\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}(\mathbf{x}_b-\boldsymbol{\mu}_b)\\
\boldsymbol{\Sigma}_{a\mid b}&=\boldsymbol{\Lambda}_{aa}^{-1}=\boldsymbol{\Sigma}_{aa}-\boldsymbol{\Sigma}_{ab}\boldsymbol{\Sigma}_{bb}^{-1}\boldsymbol{\Sigma}_{ba}
\end{aligned} \tag{2.46–2.47}
$$

  평균은 $\mathbf{x}_b$의 일차식, 공분산은 $\mathbf{x}_b$에 독립이다(**선형 가우시안 모델**<span class="gloss">linear Gaussian model</span>). 분할 행렬 역행렬에서 $\mathbf{M}^{-1}=\mathbf{A}-\mathbf{B}\mathbf{D}^{-1}\mathbf{C}$를 $\mathbf{D}$에 대한 **슈어 보수**<span class="gloss">Schur complement</span>라 한다.

::: tip 실습 · 조건부 가우시안 공식 검증
$\boldsymbol{\mu}_{a\mid b}=\mu_a+\Sigma_{ab}\Sigma_{bb}^{-1}(x_b-\mu_b)$, $\Sigma_{a\mid b}=\Sigma_{aa}-\Sigma_{ab}\Sigma_{bb}^{-1}\Sigma_{ba}$를 몬테카를로 표본과 비교합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)
mu  = np.array([1.0, 2.0])
Sig = np.array([[2.0, 0.8], [0.8, 1.0]])
xb = 3.0
mu_ab  = mu[0] + Sig[0,1]/Sig[1,1]*(xb - mu[1])      # μ_a + Σ_ab Σ_bb^-1 (x_b-μ_b)
var_ab = Sig[0,0] - Sig[0,1]**2/Sig[1,1]             # Σ_aa - Σ_ab Σ_bb^-1 Σ_ba
print(f"이론 조건부 평균 μ_a|b (x_b={xb}) = {mu_ab:.4f}")
print(f"이론 조건부 분산 Σ_a|b          = {var_ab:.4f}")
X = rng.multivariate_normal(mu, Sig, 2_000_000)
mask = np.abs(X[:,1]-xb) < 0.05
print(f"[MC] x_b≈{xb} 표본에서  x_a 평균={X[mask,0].mean():.4f}, 분산={X[mask,0].var():.4f}")
```

</PyRunner>

### 2.3.2 주변 가우시안 분포

::: info 분할 가우시안
결합 가우시안 $\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu},\boldsymbol{\Sigma})$을 $\mathbf{x}=(\mathbf{x}_a,\mathbf{x}_b)$로 분할하면, 조건부 분포와 주변 분포는 모두 가우시안이다.

$$
\begin{aligned}
p(\mathbf{x}_a\mid\mathbf{x}_b)&=\mathcal{N}(\mathbf{x}_a\mid\boldsymbol{\mu}_{a\mid b},\boldsymbol{\Lambda}_{aa}^{-1}),\quad \boldsymbol{\mu}_{a\mid b}=\boldsymbol{\mu}_a-\boldsymbol{\Lambda}_{aa}^{-1}\boldsymbol{\Lambda}_{ab}(\mathbf{x}_b-\boldsymbol{\mu}_b)\\
p(\mathbf{x}_a)&=\mathcal{N}(\mathbf{x}_a\mid\boldsymbol{\mu}_a,\boldsymbol{\Sigma}_{aa})
\end{aligned}
$$
:::

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.9a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.9b.png" />
</div>
<div class="cap">그림 2.9 · (좌) 결합 분포 $p(x_a,x_b)$. (우) 주변 분포 $p(x_a)$(청색)와 $x_b=0.7$의 조건부 분포(적색).</div>
</div>

### 2.3.3 가우시안 변수에 대한 베이지안 정리

- 선형 가우시안 모델 $p(\mathbf{x})=\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu},\boldsymbol{\Lambda}^{-1})$, $p(\mathbf{y}\mid\mathbf{x})=\mathcal{N}(\mathbf{y}\mid\mathbf{A}\mathbf{x}+\mathbf{b},\mathbf{L}^{-1})$에서 결합 $\mathbf{z}=(\mathbf{x},\mathbf{y})$의 로그를 이차식으로 정리하면 주변·조건부 분포를 얻는다.

$$
\begin{aligned}
p(\mathbf{y})&=\mathcal{N}(\mathbf{y}\mid\mathbf{A}\boldsymbol{\mu}+\mathbf{b},\ \mathbf{L}^{-1}+\mathbf{A}\boldsymbol{\Lambda}^{-1}\mathbf{A}^\top)\\
p(\mathbf{x}\mid\mathbf{y})&=\mathcal{N}\big(\mathbf{x}\mid(\boldsymbol{\Lambda}+\mathbf{A}^\top\mathbf{L}\mathbf{A})^{-1}\{\mathbf{A}^\top\mathbf{L}(\mathbf{y}-\mathbf{b})+\boldsymbol{\Lambda}\boldsymbol{\mu}\},\ (\boldsymbol{\Lambda}+\mathbf{A}^\top\mathbf{L}\mathbf{A})^{-1}\big)
\end{aligned}
$$

  $p(\mathbf{x})$를 사전, $p(\mathbf{x}\mid\mathbf{y})$를 사후로 보면 이는 가우시안에 대한 베이즈 정리이다. $\mathbf{A}=\mathbf{I}$이면 $p(\mathbf{y})$는 두 가우시안의 **컨볼루션**<span class="gloss">convolution</span>(평균과 공분산이 각각 합)이 된다.

### 2.3.4 가우시안 분포의 최대 가능도

- i.i.d. 데이터 $\mathbf{X}=(\mathbf{x}_1,\ldots,\mathbf{x}_N)^\top$의 로그 가능도는 $\sum_n\mathbf{x}_n$과 $\sum_n\mathbf{x}_n\mathbf{x}_n^\top$(충분 통계량)에만 의존하며, 최대 가능도 해는

$$
\boldsymbol{\mu}_\mathrm{ML}=\frac{1}{N}\sum_{n=1}^N\mathbf{x}_n,\qquad \boldsymbol{\Sigma}_\mathrm{ML}=\frac{1}{N}\sum_{n=1}^N(\mathbf{x}_n-\boldsymbol{\mu}_\mathrm{ML})(\mathbf{x}_n-\boldsymbol{\mu}_\mathrm{ML})^\top
$$

### 2.3.5 가우시안 분포에서의 베이지안 추론

- 분산 $\sigma^2$을 아는 상태에서 평균 $\mu$를 추정할 때, 가능도가 $\mu$의 이차식 지수 형태이므로 사전 분포 $p(\mu)=\mathcal{N}(\mu\mid\mu_0,\sigma_0^2)$가 켤레다. 사후 분포는

$$
p(\mu\mid\boldsymbol{\mathsf{x}})=\mathcal{N}(\mu\mid\mu_N,\sigma_N^2),\quad
\mu_N=\frac{\sigma^2}{N\sigma_0^2+\sigma^2}\mu_0+\frac{N\sigma_0^2}{N\sigma_0^2+\sigma^2}\mu_\mathrm{ML},\quad
\frac{1}{\sigma_N^2}=\frac{1}{\sigma_0^2}+\frac{N}{\sigma^2} \tag{2.141}
$$

  사후 평균은 사전 평균 $\mu_0$와 최대 가능도 해 $\mu_\mathrm{ML}$의 절충이다($N=0$이면 사전 평균, $N\to\infty$이면 최대 가능도 해).

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.12.png" style="width:22rem;" />
<div class="cap">그림 2.12 · 데이터 수가 늘수록 평균 $\mu$의 사후 분포가 최대 가능도 해로 이동·수축한다.</div>
</div>

### 2.3.6 가우시안 분포의 혼합

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.21a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.21b.png" />
</div>
<div class="cap">그림 2.21 · '오래된 믿음' 데이터. (좌) 단일 가우시안은 두 무리를 잡지 못한다. (우) 두 가우시안의 결합은 잘 표현한다.</div>
</div>

- 충분히 많은 가우시안을 선형 중첩하면 거의 모든 연속 밀도를 근사할 수 있다. **가우시안 혼합 분포**<span class="gloss">mixture of Gaussians</span>는

$$
p(\mathbf{x})=\sum_{k=1}^K \pi_k\,\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k),\qquad \sum_k\pi_k=1,\ 0\leqslant\pi_k\leqslant1
$$

  각 $\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)$를 **성분**<span class="gloss">component</span>, $\pi_k=p(k)$를 **혼합 계수**<span class="gloss">mixing coefficient</span>라 하며, 사후 확률 $p(k\mid\mathbf{x})$를 **책임값**<span class="gloss">responsibilities</span>이라 한다. 로그 가능도 $\ln p(\mathbf{X})=\sum_n\ln\{\sum_k\pi_k\mathcal{N}(\mathbf{x}_n\mid\boldsymbol{\mu}_k,\boldsymbol{\Sigma}_k)\}$의 최대화가 학습 목표다(로그 안에 합이 있어 닫힌 해가 없으며, EM을 사용한다 → 7장).

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.23a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.23b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure2.23c.png" />
</div>
<div class="cap">그림 2.23 · 세 가우시안 혼합. (a) 성분별 밀도, (b) 주변 밀도 $p(\mathbf{x})$, (c) 밀도 표면.</div>
</div>

## 2.4 지수족

- 가우시안 등 많은 분포는 **지수족**<span class="gloss">exponential family</span>의 특수 경우다.

$$
p(\mathbf{x}\mid\boldsymbol{\eta})=h(\mathbf{x})\,g(\boldsymbol{\eta})\exp\{\boldsymbol{\eta}^\top\mathbf{u}(\mathbf{x})\} \tag{2.194}
$$

  $\boldsymbol{\eta}$는 **자연 매개변수**<span class="gloss">natural parameter</span>, $\mathbf{u}(\mathbf{x})$는 $\mathbf{x}$의 함수, $g(\boldsymbol{\eta})$는 정규화 계수로 $g(\boldsymbol{\eta})\int h(\mathbf{x})\exp\{\boldsymbol{\eta}^\top\mathbf{u}(\mathbf{x})\}\,\mathrm{d}\mathbf{x}=1$을 만족한다.

### 2.4.1 최대 가능도와 충분 통계량

- 정규화 조건 (2.195)의 양변을 $\boldsymbol{\eta}$로 미분하면 $-\nabla\ln g(\boldsymbol{\eta})=\mathbb{E}[\mathbf{u}(\mathbf{x})]$로, 단순 미분으로 모멘트를 얻는다. i.i.d. 데이터에서 최대 가능도 해는

$$
-\nabla\ln g(\boldsymbol{\eta}_\text{ML})=\frac{1}{N}\sum_{n=1}^N\mathbf{u}(\mathbf{x}_n)
$$

  으로, $\sum_n\mathbf{u}(\mathbf{x}_n)$을 통해서만 데이터에 의존한다(충분 통계량).

### 2.4.2 켤레 사전 분포

- 모든 지수족 분포에는 켤레 사전 분포 $p(\boldsymbol{\eta}\mid\boldsymbol{\chi},\nu)=f(\boldsymbol{\chi},\nu)g(\boldsymbol{\eta})^\nu\exp\{\nu\boldsymbol{\eta}^\top\boldsymbol{\chi}\}$가 존재하며, 사후 분포는 $p(\boldsymbol{\eta}\mid\mathbf{X},\boldsymbol{\chi},\nu)\propto g(\boldsymbol{\eta})^{\nu+N}\exp\{\boldsymbol{\eta}^\top(\sum_n\mathbf{u}(\mathbf{x}_n)+\nu\boldsymbol{\chi})\}$이다.
- 사전 정보가 불분명할 때는 **무정보적 사전 분포**<span class="gloss">uninformative prior</span>로 사전의 영향을 최소화한다.

> *"Letting the data speak for themselves." — Peter Gould*

## 연습문제

::: details 문제 2.1 · 베르누이가 지수족인지 확인
$\operatorname{Bern}(x\mid\mu)=\mu^x(1-\mu)^{1-x}$를 지수 형태로 쓴다.

$$
\operatorname{Bern}(x\mid\mu)=\exp\{x\ln\mu+(1-x)\ln(1-\mu)\}=(1-\mu)\exp\!\left\{x\ln\frac{\mu}{1-\mu}\right\}
$$

식 (2.194)와 비교하면 $\boldsymbol{\eta}=\ln\frac{\mu}{1-\mu}$(로짓), $u(x)=x$, $h(x)=1$, $g(\eta)=1-\mu=\sigma(-\eta)=\frac{1}{1+e^{\eta}}$이다. 따라서 베르누이는 **지수족**이며, 자연 매개변수는 로짓, 충분 통계량은 $x$이다.
:::

::: details 문제 2.2 · 우드베리 역행렬 공식
$(\mathbf{A}+\mathbf{B}\mathbf{C}\mathbf{D})^{-1}=\mathbf{A}^{-1}-\mathbf{A}^{-1}\mathbf{B}(\mathbf{C}^{-1}+\mathbf{D}\mathbf{A}^{-1}\mathbf{B})^{-1}\mathbf{D}\mathbf{A}^{-1}$를 증명한다.

**풀이.** 우변을 $\mathbf{X}$라 두고 $(\mathbf{A}+\mathbf{B}\mathbf{C}\mathbf{D})\mathbf{X}=\mathbf{I}$임을 보인다. 전개하면

$$
(\mathbf{A}+\mathbf{B}\mathbf{C}\mathbf{D})\mathbf{X}=\mathbf{I}-\mathbf{B}(\mathbf{C}^{-1}+\mathbf{D}\mathbf{A}^{-1}\mathbf{B})^{-1}\mathbf{D}\mathbf{A}^{-1}+\mathbf{B}\mathbf{C}\mathbf{D}\mathbf{A}^{-1}-\mathbf{B}\mathbf{C}\mathbf{D}\mathbf{A}^{-1}\mathbf{B}(\mathbf{C}^{-1}+\mathbf{D}\mathbf{A}^{-1}\mathbf{B})^{-1}\mathbf{D}\mathbf{A}^{-1}
$$

$\mathbf{B}$로 왼쪽, $\mathbf{D}\mathbf{A}^{-1}$로 오른쪽을 묶으면 가운데가 $-(\mathbf{C}^{-1}+\mathbf{D}\mathbf{A}^{-1}\mathbf{B})^{-1}+\mathbf{C}-\mathbf{C}\mathbf{D}\mathbf{A}^{-1}\mathbf{B}(\mathbf{C}^{-1}+\mathbf{D}\mathbf{A}^{-1}\mathbf{B})^{-1}$이 되고, $\mathbf{C}\mathbf{D}\mathbf{A}^{-1}\mathbf{B}=\mathbf{C}(\mathbf{C}^{-1}+\mathbf{D}\mathbf{A}^{-1}\mathbf{B})-\mathbf{I}$를 대입하면 전부 상쇄되어 $(\mathbf{A}+\mathbf{B}\mathbf{C}\mathbf{D})\mathbf{X}=\mathbf{I}$이다. 따라서 성립한다.
:::

::: details 문제 2.3 · 다항 분포가 지수족인지 확인
$p(\mathbf{x}\mid\boldsymbol{\mu})=\prod_{k}\mu_k^{x_k}=\exp\{\sum_k x_k\ln\mu_k\}$이므로, $\boldsymbol{\eta}=(\ln\mu_1,\ldots,\ln\mu_M)^\top$, $\mathbf{u}(\mathbf{x})=\mathbf{x}$, $h(\mathbf{x})=1$, $g(\boldsymbol{\eta})=1$로 두면 식 (2.194) 형태다. 따라서 **지수족**이다(단, $\sum_k\mu_k=1$ 제약으로 자연 매개변수는 종속적이다. 이를 소거하면 $\eta_k=\ln(\mu_k/\mu_M)$인 소프트맥스 형태가 된다).
:::

::: details 문제 2.4 · 베타 분포의 평균·분산·최빈값
$\mathrm{Beta}(\mu\mid a,b)\propto\mu^{a-1}(1-\mu)^{b-1}$. 정규화 상수 $\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}$와 $\int_0^1\mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu=\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$를 이용한다.

**평균.** $\mathbb{E}[\mu]=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\int_0^1\mu^{a}(1-\mu)^{b-1}\mathrm{d}\mu=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\cdot\frac{\Gamma(a+1)\Gamma(b)}{\Gamma(a+b+1)}=\dfrac{a}{a+b}$ ($\Gamma(a+1)=a\Gamma(a)$ 사용).

**분산.** 같은 방식으로 $\mathbb{E}[\mu^2]=\frac{(a+1)a}{(a+b+1)(a+b)}$를 구하고 $\operatorname{var}[\mu]=\mathbb{E}[\mu^2]-\mathbb{E}[\mu]^2=\dfrac{ab}{(a+b)^2(a+b+1)}$.

**최빈값.** $\frac{\mathrm{d}}{\mathrm{d}\mu}\{(a-1)\ln\mu+(b-1)\ln(1-\mu)\}=\frac{a-1}{\mu}-\frac{b-1}{1-\mu}=0\Rightarrow\operatorname{mode}[\mu]=\dfrac{a-1}{a+b-2}$ ($a,b>1$).
:::

::: details 문제 2.5 · 두 가우시안 합의 미분 엔트로피
$x_1\sim\mathcal{N}(\mu_1,\tau_1^{-1})$, $x_2\sim\mathcal{N}(\mu_2,\tau_2^{-1})$이고 $x=x_1+x_2$일 때 $p(x)=\int p(x\mid x_2)p(x_2)\,\mathrm{d}x_2$이다. $p(x\mid x_2)=\mathcal{N}(x\mid x_2+\mu_1,\tau_1^{-1})$이고, 지수부에 제곱식의 완성을 적용하면 두 가우시안의 **컨볼루션**<span class="gloss">convolution</span>이 되어

$$
p(x)=\mathcal{N}\!\left(x\ \middle|\ \mu_1+\mu_2,\ \tau_1^{-1}+\tau_2^{-1}\right)
$$

즉 평균은 합, 분산은 $\sigma^2=\tau_1^{-1}+\tau_2^{-1}$이다. 단변량 가우시안의 미분 엔트로피 공식 $H[x]=\tfrac12\{1+\ln(2\pi\sigma^2)\}$에 대입하면

$$
H[x]=\frac{1}{2}\left\{1+\ln\!\left(2\pi\!\left(\tau_1^{-1}+\tau_2^{-1}\right)\right)\right\}
$$
:::
