# 1 · 소개

> 주어진 데이터에서 어떤 특정한 패턴을 찾아내는 것은 아주 중요한 문제이다. 이 문제에 대해 인류는 오랜 시간 동안 답을 구해왔으며, 성공적으로 패턴을 찾아내곤 했다. 요하네스 케플러<span class="gloss">Johannes Kepler</span>는 티코 브라헤<span class="gloss">Tycho Brahe</span>가 16세기에 관찰하여 축적해 놓은 대량의 천문학 데이터에서 패턴을 찾아내어 케플러의 행성 운동 법칙을 발견했다.

## 1.1 다항식 곡선 피팅

- 아래와 같은 다항식을 이용한 **회귀**<span class="gloss">regression</span> 문제를 생각하자.

$$
y(x, \mathbf{w})=w_0+w_1x+w_2x^2+\cdots+w_Mx^M=\sum_{j=0}^{M}w_jx^j \tag{1.1}
$$

  - $M$은 이 다항식의 **차수**<span class="gloss">order</span>이며, 계수 $w_0,\ldots,w_M$을 모아 벡터 $\mathbf{w}$로 표현한다.
  - 다항 함수 $y(x,\mathbf{w})$는 $x$에 대해서는 비선형이지만, 계수 $\mathbf{w}$에 대해서는 선형이다.
- 다항식을 훈련 집합<span class="gloss">training set</span> 데이터에 피팅<span class="gloss">fitting</span>하여 계수 값을 정한다.
  - 표적값<span class="gloss">target</span> $t$와 함숫값 $y(x,\mathbf{w})$의 오차를 측정하는 **오차 함수**<span class="gloss">error function</span>를 정의하고, 이를 최소화한다.
  - 자주 쓰는 오차 함수는 각 데이터 포인트에서 예측치와 표적값의 차이를 제곱해 합산한 것이다.

$$
E(\mathbf{w})=\frac{1}{2}\sum_{n=1}^{N}\{y(x_n, \mathbf{w})-t_n\}^2 \tag{1.2}
$$

  - 이 값은 항상 양수이며, 함숫값이 정확히 표적값을 지날 때만 $0$이 된다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure1.3.png" style="width:22rem;" />
<div class="cap">그림 1.3 · 오차 함수는 각 데이터 포인트의 함숫값(적색 선)과 실제 표적값(청색 점) 간 오차(녹색 선)의 제곱의 합이다.</div>
</div>

- $E(\mathbf{w})$는 계수에 대한 이차 형태이므로, 미분하여 $0$으로 두면 유일한 최소해 $\mathbf{w}^\star$를 얻는다.
- 남은 문제는 차수 $M$을 정하는 것으로, **모델 선택**<span class="gloss">model selection</span> 문제에 해당한다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure1.4a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure1.4b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure1.4c.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure1.4d.png" />
</div>
<div class="cap">그림 1.4 · 청색 점은 삼각 함수(녹색 선)에 노이즈<span class="gloss">noise</span>가 더해진 값이며, 다양한 차수에 따른 피팅 곡선(적색 선)이 그려져 있다.</div>
</div>

- 상수($M=0$)·일차($M=1$)는 피팅이 잘 안 되고, 삼차($M=3$)는 적절히 표현한다.
- 차수를 높이면($M=9$) 훈련 집합을 완벽히 피팅하여 $E(\mathbf{w}^\star)=0$이지만, 곡선이 심하게 진동하며 삼각 함수를 표현하지 못한다. 이것이 **과적합**<span class="gloss">overfitting</span>의 예다.
- 과적합을 막는 대표적 기법이 **정규화**<span class="gloss">regularization</span>이다. 오차 함수에 계수 크기를 억제하는 페널티항을 더한다.

$$
\widetilde{E}(\mathbf{w})=\frac{1}{2}\sum_{n=1}^{N}\{y(x_n, \mathbf{w})-t_n\}^2+\frac{\lambda}{2}\|\mathbf{w}\|^2 \tag{1.3}
$$

  - 여기서 $\|\mathbf{w}\|^2=\mathbf{w}^\top\mathbf{w}=w_0^2+\cdots+w_M^2$이고($w_0$은 종종 제외), $\lambda$가 정규화항의 상대적 중요도를 정한다.
  - 이 방식을 수축법<span class="gloss">shrinkage method</span> 또는 **리지 회귀**<span class="gloss">ridge regression</span>라 하며, 신경망 관점에서는 가중치 감쇠<span class="gloss">weight decay</span>라 한다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure1.7a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure1.7b.png" />
</div>
<div class="cap">그림 1.7 · $M=9$ 다항식에 정규화된 오차 함수를 사용한 결과.</div>
</div>

::: tip 실습 · 다항식 곡선 피팅과 과적합
아래 코드로 차수 $M$을 높일수록 훈련 오차는 줄지만 계수 크기 $\|\mathbf{w}\|$가 폭발함(과적합)을, 그리고 정규화 $\lambda$가 이를 억제함을 직접 확인하세요.
:::

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(0)
N = 10
x = np.linspace(0, 1, N)
t = np.sin(2*np.pi*x) + 0.15*rng.standard_normal(N)     # sin(2πx) + 노이즈

def fit(x, t, M, lam=0.0):
    Phi = np.vander(x, M+1, increasing=True)            # [1, x, ..., x^M]
    return np.linalg.solve(Phi.T @ Phi + lam*np.eye(M+1), Phi.T @ t)

def rmse(x, t, w):
    Phi = np.vander(x, len(w), increasing=True)
    return np.sqrt(np.mean((Phi @ w - t)**2))

print("차수 M별 훈련 RMSE (정규화 없음):")
for M in [0, 1, 3, 9]:
    w = fit(x, t, M)
    print(f"  M={M}: train RMSE={rmse(x,t,w):.4f},  ||w||={np.linalg.norm(w):.1f}")

print("\nM=9에서 정규화 λ의 효과:")
for lam in [0.0, 1e-6, 1e-2]:
    w = fit(x, t, 9, lam)
    print(f"  λ={lam:<6g}: ||w||={np.linalg.norm(w):10.1f},  train RMSE={rmse(x,t,w):.4f}")
print("\nM=9·λ=0은 점 10개를 완벽 피팅(RMSE≈0)하지만 ||w||가 폭발 → 과적합.")
print("정규화(λ↑)가 계수 크기를 억제해 과적합을 완화한다.")
```

</PyRunner>

## 1.2 확률론

::: info 확률의 기본 법칙
$X$와 $Y$의 결합 확률<span class="gloss">joint probability</span>이 $p(X,Y)$, $X$에 대한 $Y$의 조건부 확률<span class="gloss">conditional probability</span>이 $p(Y\mid X)$, $X$의 확률(주변 확률<span class="gloss">marginal probability</span>)이 $p(X)$일 때 다음이 성립한다.

$$
\text{합의 법칙}\quad p(X)=\sum_Y p(X, Y),\qquad
\text{곱의 법칙}\quad p(X, Y)=p(Y\mid X)p(X)
$$
:::

- 곱의 법칙과 대칭성 $p(X,Y)=p(Y,X)$으로부터 **베이즈 정리**<span class="gloss">Bayes' theorem</span>를 얻는다.

$$
p(Y\mid X)=\frac{p(X\mid Y)p(Y)}{p(X)}
$$

  - $p(Y)$를 **사전 확률**<span class="gloss">prior probability</span>(관찰 전), $p(Y\mid X)$를 **사후 확률**<span class="gloss">posterior probability</span>(관찰 후)이라 한다.

### 1.2.1 확률 밀도

- 연속 공간에서 변수 $x$가 $(x,x+\delta x)$ 구간의 값을 가질 확률이 $p(x)\delta x$ $(\delta x\to0)$로 주어지면, $p(x)$를 $x$의 **확률 밀도**<span class="gloss">probability density</span>라 한다.
- $x$가 $(a,b)$ 구간의 값을 가질 확률과 밀도의 조건은 다음과 같다.

$$
p(x\in(a,b))=\int_a^b p(x)\,\mathrm{d}x,\qquad p(x)\geqslant 0,\qquad \int_{-\infty}^{\infty}p(x)\,\mathrm{d}x=1
$$

- $x$가 $(-\infty,z)$에 속할 확률은 **누적 분포 함수**<span class="gloss">cumulative distribution function</span> $P(z)=\int_{-\infty}^z p(x)\,\mathrm{d}x$로 표현한다.
- $x$가 이산 변수일 경우 $p(x)$를 **확률 질량 함수**<span class="gloss">probability mass function</span>라 부르기도 한다.

### 1.2.2 기댓값과 공분산

- 밀도 $p(x)$ 하에서 함수 $f(x)$의 평균을 **기댓값**<span class="gloss">expectation</span> $\mathbb{E}[f]$라 한다.

$$
\mathbb{E}[f]=\sum_x p(x)f(x)\ \text{(이산)},\qquad \mathbb{E}[f]=\int p(x)f(x)\,\mathrm{d}x\ \text{(연속)}
$$

- $N$개의 데이터 포인트로는 $\mathbb{E}[f]\approx\frac{1}{N}\sum_{n=1}^{N}f(x_n)$으로 근사한다. 조건부 분포에 대한 **조건부 기댓값**<span class="gloss">conditional expectation</span>도 비슷하게 정의된다.
- $f(x)$의 **분산**<span class="gloss">variance</span>과 두 변수의 **공분산**<span class="gloss">covariance</span>은 다음과 같다.

$$
\operatorname{var}[f]=\mathbb{E}[f(x)^2]-\mathbb{E}[f(x)]^2,\qquad
\operatorname{cov}[x,y]=\mathbb{E}_{x,y}[xy]-\mathbb{E}[x]\mathbb{E}[y]
$$

  - 공분산은 $x$와 $y$가 얼마나 함께 변동하는지의 지표이며, 두 변수가 벡터이면 공분산은 행렬 $\operatorname{cov}[\mathbf{x},\mathbf{y}]=\mathbb{E}[\mathbf{x}\mathbf{y}^\top]-\mathbb{E}[\mathbf{x}]\mathbb{E}[\mathbf{y}^\top]$이 된다.

### 1.2.3 베이지안 확률

- 확률을 '반복 가능한 사건의 빈도수'로 해석하는 것을 **빈도적**<span class="gloss">frequentist</span> 관점이라 한다. 이 경우 한 번도 관찰하지 못한 사건에 확률을 부여하기 어렵다.
- 확률로 불확실성을 정량화하고 증거가 주어질 때마다 수정하는 관점을 **베이지안**<span class="gloss">Bayesian</span> 관점이라 한다. 데이터 관측 전 $\mathbf{w}$에 대한 가정을 사전 분포 $p(\mathbf{w})$로, 관측 데이터 $\mathcal{D}$를 $p(\mathcal{D}\mid\mathbf{w})$로 두면

$$
p(\mathbf{w}\mid\mathcal{D})=\frac{p(\mathcal{D}\mid\mathbf{w})p(\mathbf{w})}{p(\mathcal{D})}
$$

  - $p(\mathcal{D}\mid\mathbf{w})$는 **매개변수**<span class="gloss">parameter</span> $\mathbf{w}$의 함수로 볼 때 **가능도 함수**<span class="gloss">likelihood function</span>라 하며, 관측된 데이터가 얼마나 '그럴듯한지'를 나타낸다.
- 빈도적 관점의 대표 추정값이 **최대 가능도**<span class="gloss">maximum likelihood</span>이다. 기계학습에서는 음의 로그 가능도<span class="gloss">negative log-likelihood</span>를 오차 함수로 쓰며, 로그가 단조 증가하므로 가능도 최대화와 오차 최소화가 동일하다.

### 1.2.4 가우시안 분포

- **정규 분포**<span class="gloss">normal distribution</span>(=**가우시안 분포**<span class="gloss">Gaussian distribution</span>)는 단일 변수 $x$에 대해 다음과 같다.

$$
\mathcal{N}(x\mid\mu, \sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{-\frac{1}{2\sigma^2}(x-\mu)^2\right\} \tag{1.20}
$$

  - **평균**<span class="gloss">mean</span> $\mu$와 **분산**<span class="gloss">variance</span> $\sigma^2$의 두 매개변수로 정해진다. $\sigma$는 **표준 편차**<span class="gloss">standard deviation</span>, $\beta=1/\sigma^2$는 **정밀도**<span class="gloss">precision</span>이다.
- $D$차원 벡터 $\mathbf{x}$에 대한 가우시안 분포는 다음과 같다($\boldsymbol{\mu}$는 평균, $\boldsymbol{\Sigma}$는 $D\times D$ 공분산 행렬, $|\boldsymbol{\Sigma}|$는 행렬식).

$$
\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu}, \boldsymbol{\Sigma})=\frac{1}{(2\pi)^{D/2}}\frac{1}{|\boldsymbol{\Sigma}|^{1/2}}\exp\left\{-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\right\}
$$

### 1.2.5 곡선 피팅

- 곡선 피팅의 목표는 입력 $\boldsymbol{\mathsf{x}}=(x_1,\ldots,x_N)^\top$과 표적값 $\boldsymbol{\mathsf{t}}=(t_1,\ldots,t_N)^\top$이 주어질 때, 새 입력 $x$에 대한 $t$를 예측하는 것이다. (가우시안 변수 $\mathbf{x}$와 구분하기 위해 $\boldsymbol{\mathsf{x}}$로 표기.)
- $t$가 $y(x,\mathbf{w})$를 평균으로 갖는 가우시안을 따른다고 가정하면

$$
p(t\mid x,\mathbf{w},\beta)=\mathcal{N}(t\mid y(x,\mathbf{w}), \beta^{-1}) \tag{1.22}
$$

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure1.16.png" style="width:24rem;" />
<div class="cap">그림 1.16 · $x$가 주어졌을 때 $t$의 가우시안 조건부 분포(식 1.22). 평균은 $y(x,\mathbf{w})$, 정밀도는 $\beta$로 주어진다.</div>
</div>

- 최대 가능도로 $\mathbf{w}$와 $\beta$를 구한다. 가능도 $p(\boldsymbol{\mathsf{t}}\mid\boldsymbol{\mathsf{x}},\mathbf{w},\beta)=\prod_{n=1}^N\mathcal{N}(t_n\mid y(x_n,\mathbf{w}),\beta^{-1})$에 로그를 취하면

$$
\ln p(\boldsymbol{\mathsf{t}}\mid\boldsymbol{\mathsf{x}},\mathbf{w},\beta) = -\frac{\beta}{2}\sum_{n=1}^{N}\{y(x_n,\mathbf{w})- t_n\}^2+\frac{N}{2}\ln\beta-\frac{N}{2}\ln(2\pi) \tag{1.23}
$$

  - $\mathbf{w}_\text{ML}$을 구하는 것은 뒤 두 항과 $\beta$가 무관하므로, 결국 제곱합 오차 식 (1.2)를 최소화하는 것과 같다.
  - 정밀도의 최대 가능도 해는 $\frac{1}{\beta_\text{ML}}=\frac{1}{N}\sum_{n=1}^{N}\{y(x_n,\mathbf{w}_\text{ML})-t_n\}^2$이다.
- 예측은 점 추정이 아니라 **예측 분포**<span class="gloss">predictive distribution</span> $p(t\mid x,\mathbf{w}_\text{ML},\beta_\text{ML})=\mathcal{N}(t\mid y(x,\mathbf{w}_\text{ML}),\beta_\text{ML}^{-1})$로 표현된다.
- 나아가 계수 $\mathbf{w}$에 사전 분포를 도입한다(단순화를 위해 가우시안).

$$
p(\mathbf{w}\mid\alpha)=\mathcal{N}(\mathbf{w}\mid\mathbf{0},\alpha^{-1}\mathbf{I})
$$

  - $\alpha$처럼 모델 매개변수의 분포를 제어하는 변수를 **초매개변수**<span class="gloss">hyperparameter</span>라 한다.
  - 베이즈 정리로 사후 분포는 $p(\mathbf{w}\mid\boldsymbol{\mathsf{x}},\boldsymbol{\mathsf{t}},\alpha,\beta)\propto p(\boldsymbol{\mathsf{t}}\mid\boldsymbol{\mathsf{x}},\mathbf{w},\beta)p(\mathbf{w}\mid\alpha)$이며, 이를 최대화하는 방식을 **최대 사후 분포**<span class="gloss">maximum a posterior</span>라 한다.
  - 전개하면 사후 분포 최대화는 $\frac{\beta}{2}\sum_{n}\{y(x_n,\mathbf{w})-t_n\}^2+\frac{\alpha}{2}\mathbf{w}^\top\mathbf{w}$의 최소화, 즉 정규화 매개변수 $\lambda=\alpha/\beta$인 정규화 제곱합 오차 식 (1.3)의 최소화와 동일하다.

### 1.2.6 베이지안 곡선 피팅

- 최대 사후 분포도 여전히 $\mathbf{w}$의 점 추정이므로 완전한 베이지안은 아니다. 완전한 베이지안은 모든 $\mathbf{w}$에 대해 적분하여 주변화한다.

$$
p(t\mid x, \boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}})=\int p(t\mid x, \mathbf{w})p(\mathbf{w}\mid\boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}})\,\mathrm{d}\mathbf{w} \tag{1.30}
$$

- 이 적분을 수행하면 예측 분포가 가우시안 $p(t\mid x,\boldsymbol{\mathsf{x}},\boldsymbol{\mathsf{t}})=\mathcal{N}(t\mid m(x),s^2(x))$로 주어지고, 평균과 분산은

$$
\begin{aligned}
m(x)&=\beta \boldsymbol{\phi}(x)^\top\mathbf{S}\sum_{n=1}^{N}\boldsymbol{\phi}(x_n)t_n\\
s^2(x)&=\beta^{-1}+\boldsymbol{\phi}(x)^\top\mathbf{S}\boldsymbol{\phi}(x)
\end{aligned} \tag{1.33}
$$

  - 여기서 $\mathbf{S}^{-1}=\alpha\mathbf{I}+\beta\sum_{n=1}^{N}\boldsymbol{\phi}(x_n)\boldsymbol{\phi}(x_n)^\top$이고 $\phi_i(x)=x^i$ $(i=0,\ldots,M)$이다.
  - 식 (1.33)의 첫 항은 표적값 노이즈로 인한 불확실성, 마지막 항은 $\mathbf{w}$의 불확실성으로 인한 것으로 베이지안 접근의 산물이다.

## 1.3 모델 선택

- 훈련 집합의 좋은 성능이 좋은 예측 성능을 보장하지 않는다(과적합).
- 일부 데이터로 여러 모델·매개변수를 학습하고 독립적인 **검증 집합**<span class="gloss">validation set</span>에서 비교·선택하며, 최종 성능은 별도의 **시험 집합**<span class="gloss">test set</span>으로 판단한다.
- 대표 방법이 **교차 검증법**<span class="gloss">cross validation</span>으로, 전체 데이터를 $S$등분해 $(S-1)/S$로 훈련하고 나머지로 검증하는 것을 $S$-접힘<span class="gloss">S-fold</span> 교차 검증법이라 한다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure1.18.png" style="width:20rem;" />
<div class="cap">그림 1.18 · $S$-접힘 교차 검증법. $S$번 실행의 성능 점수를 평균내어 최종 점수를 도출한다.</div>
</div>

## 1.4 차원의 저주

- 실제 문제는 입력이 하나가 아니라 여러 변수로 이루어진 고차원 공간을 다룬다. $D$개의 입력에 대해 3차 다항식은

$$
y(\mathbf{x}, \mathbf{w})=w_0+\sum_{i=1}^{D}w_ix_i + \sum_{i=1}^{D}\sum_{j=1}^{D}w_{ij}x_i x_j + \sum_{i=1}^{D}\sum_{j=1}^{D}\sum_{k=1}^{D}w_{ijk}x_i x_j x_k
$$

  - $D$가 커질수록 계수 수가 $D^3$에 비례해 증가하고, $M$차 다항식은 $D^M$에 비례한다.
- 고차원에서 발생하는 문제를 **차원의 저주**<span class="gloss">curse of dimensionality</span>라 한다. 다만 실제 고차원 데이터는 유의미한 차원 수가 제한적이고, (적어도 지역적으로) '매끈한' 특성을 가져 효과적인 학습이 가능하다.

## 1.5 결정 이론

- 불확실성이 존재하는 상황에서 최적의 의사 결정을 위해 **결정 이론**<span class="gloss">decision theory</span>을 사용한다. 엑스레이 이미지 $\mathbf{x}$로 암 여부 $t$를 판단하는 진단 문제를 생각하자(암이면 $\mathcal{C}_1$, 아니면 $\mathcal{C}_2$).
- 베이즈 정리로 각 클래스의 사후 확률을 구한다.

$$
p(\mathcal{C}_k\mid\mathbf{x})=\frac{p(\mathbf{x}\mid\mathcal{C}_k)p(\mathcal{C}_k)}{p(\mathbf{x})}
$$

  - $p(\mathcal{C}_k)$는 이미지 확인 전의 사전 확률, $p(\mathcal{C}_k\mid\mathbf{x})$는 이미지 정보를 반영한 사후 확률이다.

### 1.5.1 오분류 비율의 최소화

- 잘못된 분류의 수를 줄이려면 입력 공간을 **결정 구역**<span class="gloss">decision region</span> $\mathcal{R}_k$로 나누는 규칙이 필요하다. 구역 사이 경계를 **결정 경계**<span class="gloss">decision boundary</span>라 한다.
- 두 클래스에서 오류 확률은

$$
p(m)=\int_{\mathcal{R}_1}p(\mathbf{x},\mathcal{C}_2)\,\mathrm{d}\mathbf{x}+\int_{\mathcal{R}_2}p(\mathbf{x}, \mathcal{C}_1)\,\mathrm{d}\mathbf{x} \tag{1.37}
$$

  - 이를 최소화하려면 각 $\mathbf{x}$를 결합 확률이 더 큰 클래스, 즉 **사후 확률 $p(\mathcal{C}_k\mid\mathbf{x})$가 최대인 클래스**에 할당하면 된다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure1.24.png" style="width:26rem;" />
<div class="cap">그림 1.24 · 결정 경계에 따른 두 클래스의 결합 확률. 최적 경계 $x_0$에서 오분류 구역(적색)이 사라진다.</div>
</div>

### 1.5.2 기대 손실의 최소화

- 오분류 수를 줄이는 것보다 복잡한 경우가 많다(암 환자를 정상으로 오진하는 실수가 그 반대보다 훨씬 심각).
- **손실 함수**<span class="gloss">loss function</span>(=**비용 함수**<span class="gloss">cost function</span>) $L_{kj}$를 도입한다(클래스 $k$를 $j$로 오분류할 때의 페널티). 목표는 평균 손실 최소화이다.

$$
\mathbb{E}[L]=\sum_k\sum_j\int_{\mathcal{R}_j}L_{kj}\,p(\mathbf{x},\mathcal{C}_k)\,\mathrm{d}\mathbf{x} \tag{1.38}
$$

  - 구역 $\mathcal{R}_j$를 적절히 선택해 식 (1.38)을 최소화한다.

### 1.5.3 거부 옵션

- 사후 확률들이 비슷해 확신이 낮은 구역에서는 결정을 피하는 것이 적절할 수 있으며, 이를 **거부 옵션**<span class="gloss">reject option</span>이라 한다. 임계값 $\theta$를 두어, 최대 사후 확률이 $\theta$ 이하이면 결정을 거부한다.

### 1.5.4 추론과 결정

- 분류 문제는 두 단계로 나뉜다: **추론 단계**<span class="gloss">inference stage</span>(사후 확률 $p(\mathcal{C}_k\mid\mathbf{x})$ 학습)와 **결정 단계**<span class="gloss">decision stage</span>(사후 확률로 최적 클래스 할당). $\mathbf{x}$에서 결정값을 직접 돌려주는 함수를 **판별 함수**<span class="gloss">discriminant function</span>라 한다.
- 결정 문제의 세 가지 접근:
  1. **생성 모델**<span class="gloss">generative model</span> — 조건부 밀도 $p(\mathbf{x}\mid\mathcal{C}_k)$와 사전 $p(\mathcal{C}_k)$를 구해 베이즈 정리로 사후 확률을 얻는다. 주변 밀도 $p(\mathbf{x})=\sum_k p(\mathbf{x}\mid\mathcal{C}_k)p(\mathcal{C}_k)$도 얻지만 자원 요구가 크다.
  2. **판별 모델**<span class="gloss">discriminative model</span> — 사후 확률 $p(\mathcal{C}_k\mid\mathbf{x})$를 직접 모델링한다. 결정만이 목표일 때 더 효율적이다.
  3. **판별 함수** — 확률 없이 입력을 클래스로 직접 사상한다. 가장 간단하지만 사후 확률의 장점을 잃는다.

## 1.6 정보 이론

- 이산 변수 $x$가 갖는 정보량은 '놀라움의 정도'로, 일어나기 힘든 사건일수록 정보량이 크다. 정보량 함수는

$$
h(x)=-\log_2 p(x) \tag{1.92}
$$

  - 독립인 두 사건이 함께 일어날 때 정보량은 합, 확률은 곱이므로 정보량은 확률의 로그에 해당한다.
- 전송에 필요한 평균 정보량이 확률 변수 $x$의 **엔트로피**<span class="gloss">entropy</span>이다.

$$
\mathrm{H}[x]=-\sum_x p(x) \log_2 p(x)
$$

  - $\log_2$ 대신 $\ln$을 쓰면 단위가 비트<span class="gloss">bit</span> 대신 내트<span class="gloss">nat</span>가 된다.
- $N$개의 물체를 통에 넣는 총 가짓수를 **다중도**<span class="gloss">multiplicity</span> $W=\frac{N!}{\prod_i n_i!}$라 한다. 엔트로피는 다중도의 로그로, 스털링 근사<span class="gloss">Stirling's approximation</span> $\ln N!\simeq N\ln N-N$을 적용하면

$$
\mathrm{H}=-\lim_{N\to\infty}\sum_i\left(\frac{n_i}{N}\right)\ln\left(\frac{n_i}{N}\right)=-\sum_i p_i \ln p_i
$$

  - 통 안 물체의 순서를 미시 상태<span class="gloss">microstate</span>, 통별 물체 수 비율을 거시 상태<span class="gloss">macrostate</span>라 하며, $W$를 거시 상태의 가중치<span class="gloss">weight</span>라 한다.

## 연습문제

::: details 문제 1.1 · 제곱합 오차의 정규방정식
식 (1.2)의 제곱합 오차 함수에 식 (1.1)의 $y(x,\mathbf{w})$를 사용할 때, 다음 선형 방정식을 풀어 오차를 최소화하는 계수 $\mathbf{w}=\{w_i\}$를 구할 수 있음을 증명하라.

$$
\sum_{j=0}^M A_{ij} w_j=T_i,\qquad A_{ij}=\sum_{n=1}^{N}x_n^{\,i+j},\qquad T_i=\sum_{n=1}^{N}x_n^{\,i} t_n
$$

**풀이.** $E(\mathbf{w})=\tfrac12\sum_n\{\sum_j w_j x_n^j - t_n\}^2$을 $w_i$에 대해 편미분한다.

$$
\frac{\partial E}{\partial w_i}=\sum_{n=1}^{N}\Big\{\sum_{j=0}^{M} w_j x_n^{\,j}-t_n\Big\}x_n^{\,i}=0
$$

전개하면 $\sum_n\sum_j w_j x_n^{i+j}=\sum_n t_n x_n^{i}$, 즉

$$
\sum_{j=0}^{M}\Big(\underbrace{\sum_{n=1}^{N}x_n^{\,i+j}}_{A_{ij}}\Big)w_j=\underbrace{\sum_{n=1}^{N}x_n^{\,i}t_n}_{T_i}
$$

이 되어 주어진 정규방정식을 얻는다. ($E$가 $\mathbf{w}$에 대해 볼록이므로 이 정류점이 최소이다. 원문의 $x_N^{i+j}$는 $x_n^{i+j}$의 오타로 바로잡았다.)
:::

::: details 문제 1.2 · 상자와 과일 (베이즈 정리)
세 상자 r, b, g가 있다. r에는 사과 3·오렌지 4·라임 3, b에는 사과 1·오렌지 1, g에는 사과 3·오렌지 3·라임 4가 들어 있다. 상자 선택 확률은 $p(r)=0.2$, $p(b)=0.2$, $p(g)=0.6$이다. 사과를 뽑을 확률과, 뽑은 과일이 오렌지일 때 그것이 g에서 왔을 확률을 구하라.

**풀이.** 합의 법칙 $p(\text{과일})=\sum_{\text{box}}p(\text{box})p(\text{과일}\mid\text{box})$을 쓴다.

$$
p(\text{사과})=0.2\cdot\tfrac{3}{10}+0.2\cdot\tfrac{1}{2}+0.6\cdot\tfrac{3}{10}=\boxed{0.34}
$$

$$
p(\text{오렌지})=0.2\cdot\tfrac{4}{10}+0.2\cdot\tfrac{1}{2}+0.6\cdot\tfrac{3}{10}=0.36
$$

베이즈 정리로

$$
p(g\mid\text{오렌지})=\frac{p(g)\,p(\text{오렌지}\mid g)}{p(\text{오렌지})}=\frac{0.6\cdot 0.3}{0.36}=\boxed{0.5}
$$

<PyRunner>

```python
p_box = {'r': 0.2, 'b': 0.2, 'g': 0.6}
counts = {'r': (3, 4, 3), 'b': (1, 1, 0), 'g': (3, 3, 4)}   # (사과, 오렌지, 라임)

def p_fruit(box, idx):
    c = counts[box]
    return c[idx] / sum(c)

p_apple  = sum(p_box[b]*p_fruit(b, 0) for b in p_box)       # 사과
p_orange = sum(p_box[b]*p_fruit(b, 1) for b in p_box)       # 오렌지
p_g_orange = p_box['g']*p_fruit('g', 1) / p_orange          # 베이즈 정리

print(f"P(사과)            = {p_apple:.3f}")
print(f"P(오렌지)          = {p_orange:.3f}")
print(f"P(상자=g | 오렌지) = {p_g_orange:.3f}")
```

</PyRunner>
:::

::: details 문제 1.3 · 가우시안 적분과 정규화
$I=\int_{-\infty}^{\infty}\exp\!\left(-\tfrac{1}{2\sigma^2}x^2\right)\mathrm{d}x$의 제곱을 극좌표로 바꾸고 $u=r^2$를 대입해 $I=(2\pi\sigma^2)^{1/2}$임을 증명하고, 이를 이용해 $\mathcal{N}(x\mid\mu,\sigma^2)$가 정규화되어 있음을 보여라.

**풀이.** 제곱을 이중적분으로 쓰고 극좌표 $(x,y)=(r\cos\theta,r\sin\theta)$, $\mathrm{d}x\,\mathrm{d}y=r\,\mathrm{d}r\,\mathrm{d}\theta$로 바꾼다.

$$
I^2=\int_0^{2\pi}\!\!\int_0^{\infty}\exp\!\left(-\frac{r^2}{2\sigma^2}\right)r\,\mathrm{d}r\,\mathrm{d}\theta
$$

$u=r^2$($\mathrm{d}u=2r\,\mathrm{d}r$)를 대입하면 $\int_0^\infty \tfrac12 e^{-u/2\sigma^2}\mathrm{d}u=\sigma^2$이므로

$$
I^2=2\pi\cdot\sigma^2=2\pi\sigma^2\ \Longrightarrow\ I=(2\pi\sigma^2)^{1/2}
$$

따라서 $\int\mathcal{N}(x\mid\mu,\sigma^2)\,\mathrm{d}x=\frac{1}{(2\pi\sigma^2)^{1/2}}\int\exp\!\left(-\tfrac{(x-\mu)^2}{2\sigma^2}\right)\mathrm{d}x=\frac{(2\pi\sigma^2)^{1/2}}{(2\pi\sigma^2)^{1/2}}=1$ (치환 $x\to x-\mu$는 적분값을 바꾸지 않는다).
:::

::: details 문제 1.4 · 감마 함수
$\Gamma(x)\equiv\int_0^{\infty}u^{x-1}e^{-u}\,\mathrm{d}u$에 대해 부분적분으로 $\Gamma(x+1)=x\Gamma(x)$, $\Gamma(1)=1$, 그리고 음이 아닌 정수 $x$에 대해 $\Gamma(x+1)=x!$임을 증명하라.

**풀이.** 부분적분 $u=u^{x}$, $\mathrm{d}v=e^{-u}\mathrm{d}u$로 두면

$$
\Gamma(x+1)=\int_0^\infty u^{x}e^{-u}\mathrm{d}u=\big[-u^{x}e^{-u}\big]_0^\infty+x\int_0^\infty u^{x-1}e^{-u}\mathrm{d}u=x\,\Gamma(x)
$$

경계항은 $0$이다. 또 $\Gamma(1)=\int_0^\infty e^{-u}\mathrm{d}u=1$. 따라서 정수 $x$에 대해 $\Gamma(x+1)=x\,\Gamma(x)=x(x-1)\cdots1\cdot\Gamma(1)=x!$이다.
:::
