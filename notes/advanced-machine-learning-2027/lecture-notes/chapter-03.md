# 3 · 선형 회귀 모델

> 회귀 모델의 목표는 입력 데이터가 주어졌을 때 그에 해당하는 연속 표적값을 예측하는 것이다. 선형 회귀 모델은 조절 가능한 매개변수를 바탕으로 한 선형 함수를 사용한다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/photos/sec03.png" style="max-width:34rem;" />
</div>

## 3.1 선형 기저 함수 모델

- 가장 단순한 **선형 회귀**<span class="gloss">linear regression</span>는 입력의 선형 결합 $y(\mathbf{x},\mathbf{w})=w_0+w_1x_1+\cdots+w_Dx_D$이지만, 입력에 대한 고정 비선형 함수(**기저 함수**<span class="gloss">basis function</span>)의 선형 결합으로 확장한다.

$$
y(\mathbf{x}, \mathbf{w})=w_0+\sum_{j=1}^{M-1} w_j \phi_j(\mathbf{x})=\sum_{j=0}^{M-1}w_j\phi_j(\mathbf{x})=\mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x})
$$

  여기서 $\phi_0(\mathbf{x})=1$(의사 기저 함수), $w_0$은 **편향**<span class="gloss">bias</span> 매개변수다. 기저 함수는 전처리·특징 추출로 이해할 수 있다.
- 대표적 기저 함수로 가우시안 $\phi_j(x)=\exp\{-\frac{(x-\mu_j)^2}{2s^2}\}$, **시그모이드**<span class="gloss">sigmoid</span> $\phi_j(x)=\sigma(\frac{x-\mu_j}{s})$가 있다($\sigma(a)=\frac{1}{1+e^{-a}}$는 **로지스틱 시그모이드**<span class="gloss">logistic sigmoid</span>).

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure3.1a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure3.1b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure3.1c.png" />
</div>
<div class="cap">

그림 3.1 · 다항 · 가우시안 · 시그모이드 기저 함수.

</div>
</div>

### 3.1.1 최대 가능도와 최소 제곱

- 표적값이 $t=y(\mathbf{x},\mathbf{w})+\epsilon$, $\epsilon\sim\mathcal{N}(0,\beta^{-1})$이라 가정하면 $p(t\mid\mathbf{x},\mathbf{w},\beta)=\mathcal{N}(t\mid y(\mathbf{x},\mathbf{w}),\beta^{-1})$이고, 제곱 오류 하에서 최적 예측은 조건부 평균 $\mathbb{E}[t\mid\mathbf{x}]=y(\mathbf{x},\mathbf{w})$이다.
- i.i.d. 데이터의 로그 가능도는 $\ln p(\boldsymbol{\mathsf{t}}\mid\mathbf{w},\beta)=\frac{N}{2}\ln\beta-\frac{N}{2}\ln(2\pi)-\beta E_D(\mathbf{w})$이고, **제곱합 오류 함수**는

$$
E_D(\mathbf{w})=\frac{1}{2}\sum_{n=1}^N\{t_n-\mathbf{w}^\top\boldsymbol{\phi}(\mathbf{x}_n)\}^2 \tag{3.12}
$$

- 기울기를 $0$으로 두고 $\mathbf{w}$에 대해 풀면 최소 제곱 문제의 **정규 방정식**<span class="gloss">normal equation</span>을 얻는다.

$$
\mathbf{w}_\mathrm{ML}=(\boldsymbol{\Phi}^\top\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^\top\boldsymbol{\mathsf{t}} \tag{3.15}
$$

  $\boldsymbol{\Phi}$는 $\Phi_{nj}=\phi_j(\mathbf{x}_n)$인 $N\times M$ **설계 행렬**<span class="gloss">design matrix</span>이고, $\boldsymbol{\Phi}^\dagger=(\boldsymbol{\Phi}^\top\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^\top$는 **무어–펜로즈 유사역행렬**<span class="gloss">Moore–Penrose pseudo-inverse</span>이다.
- 편향을 명시하면 $w_0=\bar t-\sum_{j\ge1}w_j\bar\phi_j$($\bar t$, $\bar\phi_j$는 각 평균)로, 편향이 표적값 평균과 기저 함숫값 평균의 차이를 보정한다. 정밀도는 $\frac{1}{\beta_\mathrm{ML}}=\frac{1}{N}\sum_n\{t_n-\mathbf{w}_\mathrm{ML}^\top\boldsymbol{\phi}(\mathbf{x}_n)\}^2$이다.

::: tip 실습 · 가우시안 기저 함수 회귀 (정규방정식)
설계 행렬 $\boldsymbol{\Phi}$(기저 9개 + 편향)로 $\mathbf{w}=(\boldsymbol{\Phi}^\top\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^\top\boldsymbol{\mathsf{t}}$를 풀어 $\sin(2\pi x)$를 근사합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)
N = 25
x = np.linspace(0, 1, N); t = np.sin(2*np.pi*x) + 0.1*rng.standard_normal(N)
mus = np.linspace(0, 1, 9); s = 0.1
def design(x):                                   # [1, 가우시안 기저 9개]
    return np.column_stack([np.ones(len(x)), np.exp(-(x[:,None]-mus[None,:])**2/(2*s**2))])
Phi = design(x)
w = np.linalg.solve(Phi.T@Phi + 1e-8*np.eye(Phi.shape[1]), Phi.T@t)   # 정규방정식
xt = np.linspace(0, 1, 6)
print("가우시안 기저 함수 회귀 (기저 9개 + 편향):")
for xi, yi in zip(xt, design(xt)@w):
    print(f"  x={xi:.2f}: y_pred={yi:+.3f}   sin(2πx)={np.sin(2*np.pi*xi):+.3f}")
```

</PyRunner>

### 3.1.2 최소 제곱의 기하학적 의미

- $N$차원 공간($t_n$ 축)에서 $\boldsymbol{\mathsf{t}}$는 벡터이고, 기저 함수 $\boldsymbol{\varphi}_j$($\boldsymbol{\Phi}$의 $j$번째 열)들이 $M$차원 부분 공간 $\mathcal{S}$를 이룬다. 예측 $\boldsymbol{\mathsf{y}}$는 $\mathcal{S}$ 위에 있으며, 제곱합 오류는 $\boldsymbol{\mathsf{y}}$와 $\boldsymbol{\mathsf{t}}$의 제곱 유클리드 거리이므로, **최소 제곱 해는 $\boldsymbol{\mathsf{t}}$를 $\mathcal{S}$에 직교 투영**한 것이다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure3.2.png" style="width:20rem;" />
<div class="cap">

그림 3.2 · 최소 제곱 회귀는 표적값 벡터 $\boldsymbol{\mathsf{t}}$를 부분 공간 $\mathcal{S}$에 투영해 얻는다.

</div>
</div>

### 3.1.3 순차적 학습

- 전체 데이터를 한 번에 처리하기 어려울 때 **순차적**<span class="gloss">sequential</span> 학습을 쓴다. **확률적 경사 하강법**<span class="gloss">stochastic gradient descent</span>은 $\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}-\eta\nabla E_n$으로 갱신하며($\eta$: 학습률), 제곱합 오류에 적용한 경우를 **최소 제곱 평균**<span class="gloss">least mean square; LMS</span> 알고리즘이라 한다.

### 3.1.4 정규화된 최소 제곱법

- 정규화 오류 $E_D(\mathbf{w})+\lambda E_W(\mathbf{w})$에서 가장 단순한 형태(**가중치 감쇠**<span class="gloss">weight decay</span>)는 $\frac{\lambda}{2}\mathbf{w}^\top\mathbf{w}$이며, 해는

$$
\mathbf{w}=(\lambda\mathbf{I}+\boldsymbol{\Phi}^\top\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^\top\boldsymbol{\mathsf{t}}
$$

- 일반화하면 $\frac{\lambda}{2}\sum_j|w_j|^q$이고, $q=2$는 가중치 감쇠, $q=1$은 **라쏘**<span class="gloss">lasso</span>이다. 라쏘는 $\lambda$가 충분히 크면 일부 계수를 정확히 $0$으로 만들어 **희박한**<span class="gloss">sparse</span> 모델을 준다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure3.3.png" style="width:24rem;" />
<div class="cap">

그림 3.3 · 다양한 $q$에 따른 정규화항 $\sum_j|w_j|^q$의 윤곽선.

</div>
</div>

## 3.2 편향–분산 분해

- 최적 예측은 조건부 기댓값 $h(\mathbf{x})=\mathbb{E}[t\mid\mathbf{x}]$이다. 유한한 데이터 집합 $\mathcal{D}$로 학습한 예측 $y(\mathbf{x};\mathcal{D})$의 기대 제곱 오류는 다음처럼 분해된다.

$$
\mathbb{E}_{\mathcal{D}}[\{y(\mathbf{x};\mathcal{D})-h(\mathbf{x})\}^2]=\underbrace{\{\mathbb{E}_{\mathcal{D}}[y(\mathbf{x};\mathcal{D})]-h(\mathbf{x})\}^2}_{(\text{편향})^2}+\underbrace{\mathbb{E}_{\mathcal{D}}[\{y(\mathbf{x};\mathcal{D})-\mathbb{E}_{\mathcal{D}}[y(\mathbf{x};\mathcal{D})]\}^2]}_{\text{분산}}
$$

- **편향**<span class="gloss">bias</span>은 전체 데이터 집합에 대한 평균 예측이 회귀 함수와 얼마나 차이 나는지, **분산**<span class="gloss">variance</span>은 각 데이터 집합의 해가 그 평균에서 얼마나 흩어지는지를 나타낸다. 기대 오류는 (편향)² + 분산 + 노이즈로 분해되며, **편향–분산 트레이드오프**<span class="gloss">bias–variance tradeoff</span>가 존재한다(유연한 모델: 낮은 편향·높은 분산, 엄격한 모델: 그 반대).

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure3.6.png" style="width:20rem;" />
<div class="cap">

그림 3.6 · (편향)²·분산·합. 둘의 균형점에서 시험 오차가 최소가 된다.

</div>
</div>

::: tip 실습 · 편향–분산 트레이드오프
같은 함수를 여러 데이터 집합으로 학습해 $\lambda$에 따른 편향²·분산을 측정합니다. $\lambda$가 커질수록 편향은 증가하고 분산은 감소합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)
h = lambda x: np.sin(2*np.pi*x)
xtest = np.linspace(0, 1, 50)
mus = np.linspace(0, 1, 9); s = 0.1
def design(x):
    return np.column_stack([np.ones(len(x)), np.exp(-(x[:,None]-mus[None,:])**2/(2*s**2))])
def run(lam, L=300, N=25):
    preds = np.zeros((L, len(xtest)))
    for l in range(L):
        x = rng.uniform(0, 1, N); t = h(x) + 0.15*rng.standard_normal(N)
        Phi = design(x); w = np.linalg.solve(Phi.T@Phi + lam*np.eye(Phi.shape[1]), Phi.T@t)
        preds[l] = design(xtest)@w
    mean = preds.mean(0)
    return np.mean((mean-h(xtest))**2), np.mean(preds.var(0))     # bias^2, variance
print("정규화 λ에 따른 편향²·분산 (가우시안 기저 9개):")
print(f"{'λ':>8} | {'bias^2':>8} | {'variance':>9} | {'합':>8}")
for lam in [1e-3, 0.1, 1.0, 10.0]:
    b, v = run(lam)
    print(f"{lam:>8.3g} | {b:>8.4f} | {v:>9.4f} | {b+v:>8.4f}")
print("λ↑ → 편향 증가, 분산 감소 (편향–분산 트레이드오프).")
```

</PyRunner>

## 3.3 베이지안 선형 회귀

- 최대 가능도는 기저 함수 수로 복잡도를 조절해야 해 과적합에 취약하다. 매개변수에 사전 분포를 도입하면 이를 피할 수 있다.

### 3.3.1 매개변수 분포

- 가능도가 $\mathbf{w}$의 이차식 지수 형태이므로 켤레 사전 분포는 가우시안 $p(\mathbf{w})=\mathcal{N}(\mathbf{w}\mid\mathbf{m}_0,\mathbf{S}_0)$이다. 제곱식의 완성을 적용하면 사후 분포도 가우시안이다.

$$
p(\mathbf{w}\mid\boldsymbol{\mathsf{t}})=\mathcal{N}(\mathbf{w}\mid\mathbf{m}_N,\mathbf{S}_N),\quad
\mathbf{m}_N=\mathbf{S}_N(\mathbf{S}_0^{-1}\mathbf{m}_0+\beta\boldsymbol{\Phi}^\top\boldsymbol{\mathsf{t}}),\quad
\mathbf{S}_N^{-1}=\mathbf{S}_0^{-1}+\beta\boldsymbol{\Phi}^\top\boldsymbol{\Phi} \tag{3.49–3.51}
$$

  사후 분포가 가우시안이므로 최빈값=평균이고 최대 사후 해는 $\mathbf{w}_\mathrm{MAP}=\mathbf{m}_N$이다. 순차적으로 데이터를 넣으면 각 단계의 사후가 다음 단계의 사전이 된다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure3.7.png" style="width:26rem;" />
<div class="cap">

그림 3.7 · 데이터가 늘수록 $\mathbf{w}$의 사후 분포가 좁아지고, 표본 함수 $y(x,\mathbf{w})$들이 데이터에 수렴한다.

</div>
</div>

### 3.3.2 예측 분포

- 새 $\mathbf{x}$에 대한 **예측 분포**<span class="gloss">predictive distribution</span>는 $\mathbf{w}$에 대해 주변화하여 얻는다.

$$
p(t\mid\mathbf{x},\boldsymbol{\mathsf{t}},\alpha,\beta)=\mathcal{N}(t\mid\mathbf{m}_N^\top\boldsymbol{\phi}(\mathbf{x}),\ \sigma_N^2(\mathbf{x})),\qquad
\sigma_N^2(\mathbf{x})=\frac{1}{\beta}+\boldsymbol{\phi}(\mathbf{x})^\top\mathbf{S}_N\boldsymbol{\phi}(\mathbf{x})
$$

  분산의 첫 항은 노이즈, 둘째 항은 $\mathbf{w}$의 불확실성이며, 데이터가 늘수록 둘째 항이 줄어든다.

::: tip 실습 · 예측 분포의 불확실성
데이터 수 $N$이 늘수록 $x=0.5$에서의 예측 표준편차 $\sigma_N(x)$가 감소함을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(2)
alpha, beta = 2.0, 25.0                          # 사전 정밀도, 노이즈 정밀도
mus = np.linspace(0, 1, 9); s = 0.1
def design(x):
    return np.column_stack([np.ones(len(x)), np.exp(-(x[:,None]-mus[None,:])**2/(2*s**2))])
xt = np.array([0.5])
print("데이터 수 N에 따른 x=0.5의 예측 분포 (베이지안 선형 회귀):")
for N in [1, 5, 25, 100]:
    x = rng.uniform(0, 1, N); t = np.sin(2*np.pi*x) + 0.1*rng.standard_normal(N)
    Phi = design(x)
    SN = np.linalg.inv(alpha*np.eye(Phi.shape[1]) + beta*Phi.T@Phi)   # S_N
    mN = beta * SN @ Phi.T @ t                                        # m_N
    phit = design(xt)
    mean = (phit@mN)[0]
    var = 1/beta + (phit@SN*phit).sum(1)[0]                           # σ_N^2(x)
    print(f"  N={N:3d}: 예측 평균={mean:+.3f}, 예측 표준편차={np.sqrt(var):.3f}")
print("데이터가 늘수록 예측 불확실성(표준편차)이 감소한다.")
```

</PyRunner>

## 3.4 베이지안 모델 비교

- 매개변수를 주변화하면 과적합을 피할 수 있고, 모델 선택의 불확실성도 확률로 다룬다. $L$개의 모델 $\{\mathcal{M}_i\}$에 대해 $p(\mathcal{M}_i\mid\mathcal{D})\propto p(\mathcal{M}_i)p(\mathcal{D}\mid\mathcal{M}_i)$이다.
- **모델 증거**<span class="gloss">model evidence</span> $p(\mathcal{D}\mid\mathcal{M}_i)=\int p(\mathcal{D}\mid\mathbf{w},\mathcal{M}_i)p(\mathbf{w}\mid\mathcal{M}_i)\,\mathrm{d}\mathbf{w}$는 **주변 가능도**<span class="gloss">marginal likelihood</span>라고도 하며, 두 모델 증거의 비 $p(\mathcal{D}\mid\mathcal{M}_i)/p(\mathcal{D}\mid\mathcal{M}_j)$를 **베이즈 요인**<span class="gloss">Bayes factor</span>이라 한다.
- 예측 분포 $p(t\mid\mathbf{x},\mathcal{D})=\sum_i p(t\mid\mathbf{x},\mathcal{M}_i,\mathcal{D})p(\mathcal{M}_i\mid\mathcal{D})$는 모델들의 사후 확률로 가중 평균한 **혼합 분포**<span class="gloss">mixture distribution</span>다. 가장 확률 높은 하나만 쓰는 근사가 **모델 선택**<span class="gloss">model selection</span>이다. 모델 증거는 사후 분포 계산 시 베이즈 정리의 분모(정규화항)에 해당한다.

## 연습문제

::: details 문제 3.1 · 최소 제곱 해의 직교 투영
행렬 $\mathbf{P}=\boldsymbol{\Phi}(\boldsymbol{\Phi}^\top\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^\top$가 임의의 벡터를 $\boldsymbol{\Phi}$의 열공간(부분 공간 $\mathcal{S}$)에 투영함을 보이고, 식 (3.15)의 최소 제곱 해가 $\boldsymbol{\mathsf{t}}$를 $\mathcal{S}$에 직교 투영하는 것임을 증명하라.

**풀이.** ① $\mathbf{P}$는 **투영 행렬**이다. 임의의 $\mathbf{v}$에 대해 $\mathbf{P}\mathbf{v}=\boldsymbol{\Phi}\mathbf{a}$ (단 $\mathbf{a}=(\boldsymbol{\Phi}^\top\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^\top\mathbf{v}$)이므로 $\mathbf{P}\mathbf{v}\in\mathcal{S}$이다. 또

$$
\mathbf{P}^2=\boldsymbol{\Phi}(\boldsymbol{\Phi}^\top\boldsymbol{\Phi})^{-1}\underbrace{\boldsymbol{\Phi}^\top\boldsymbol{\Phi}(\boldsymbol{\Phi}^\top\boldsymbol{\Phi})^{-1}}_{=\mathbf{I}}\boldsymbol{\Phi}^\top=\mathbf{P},\qquad \mathbf{P}^\top=\mathbf{P}
$$

즉 $\mathbf{P}$는 멱등·대칭이므로 $\mathcal{S}$로의 **직교 투영**이다.

② 예측 $\boldsymbol{\mathsf{y}}=\boldsymbol{\Phi}\mathbf{w}_\mathrm{ML}=\boldsymbol{\Phi}(\boldsymbol{\Phi}^\top\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^\top\boldsymbol{\mathsf{t}}=\mathbf{P}\boldsymbol{\mathsf{t}}$이다. 잔차는 $\boldsymbol{\mathsf{t}}-\boldsymbol{\mathsf{y}}=(\mathbf{I}-\mathbf{P})\boldsymbol{\mathsf{t}}$이고, $\boldsymbol{\Phi}^\top(\boldsymbol{\mathsf{t}}-\boldsymbol{\mathsf{y}})=\boldsymbol{\Phi}^\top\boldsymbol{\mathsf{t}}-\boldsymbol{\Phi}^\top\boldsymbol{\Phi}\mathbf{w}_\mathrm{ML}=\mathbf{0}$이므로 잔차가 $\mathcal{S}$에 직교한다. 따라서 최소 제곱 해는 $\boldsymbol{\mathsf{t}}$의 $\mathcal{S}$ 직교 투영이다.
:::

::: details 문제 3.2 · 사후 분포 (3.49)의 제곱식 완성
가능도 $p(\boldsymbol{\mathsf{t}}\mid\mathbf{w})\propto\exp\{-\tfrac{\beta}{2}(\boldsymbol{\mathsf{t}}-\boldsymbol{\Phi}\mathbf{w})^\top(\boldsymbol{\mathsf{t}}-\boldsymbol{\Phi}\mathbf{w})\}$와 사전 $p(\mathbf{w})=\mathcal{N}(\mathbf{w}\mid\mathbf{m}_0,\mathbf{S}_0)$을 곱한 사후 분포의 지수부를 $\mathbf{w}$에 대해 정리한다.

$$
-\frac{1}{2}\mathbf{w}^\top\underbrace{(\mathbf{S}_0^{-1}+\beta\boldsymbol{\Phi}^\top\boldsymbol{\Phi})}_{\mathbf{S}_N^{-1}}\mathbf{w}+\mathbf{w}^\top\underbrace{(\mathbf{S}_0^{-1}\mathbf{m}_0+\beta\boldsymbol{\Phi}^\top\boldsymbol{\mathsf{t}})}_{\mathbf{S}_N^{-1}\mathbf{m}_N}+\text{const}
$$

가우시안 지수부의 표준형 $-\tfrac12(\mathbf{w}-\mathbf{m}_N)^\top\mathbf{S}_N^{-1}(\mathbf{w}-\mathbf{m}_N)$과 이차항·일차항을 비교하면

$$
\mathbf{S}_N^{-1}=\mathbf{S}_0^{-1}+\beta\boldsymbol{\Phi}^\top\boldsymbol{\Phi},\qquad \mathbf{m}_N=\mathbf{S}_N(\mathbf{S}_0^{-1}\mathbf{m}_0+\beta\boldsymbol{\Phi}^\top\boldsymbol{\mathsf{t}})
$$

를 얻어 식 (3.49)–(3.51)이 증명된다.
:::
