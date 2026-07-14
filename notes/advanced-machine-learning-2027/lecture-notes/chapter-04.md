# 4 · 선형 분류 모델

> 분류 모델의 목표는 입력 데이터들이 주어졌을 때, 그에 해당하는 이산 클래스 변수를 예측하는 것이다. 선형 분류 모델에서는 결정 표면들이 입력 데이터에 대해 선형 함수를 사용한다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/photos/sec04.png" style="max-width:34rem;" />
</div>

## 4.1 판별 함수

- 분류 문제에서 입력값들은 $K$개의 이산 클래스 $\mathcal{C}_k$, $k=1,\ldots,K$ 중 하나에 할당되며, 입력 공간은 **결정 경계**<span class="gloss">decision boundary</span> 또는 **결정 표면**<span class="gloss">decision surface</span>이라 불리는 경계를 바탕으로 여러 **결정 구역**<span class="gloss">decision region</span>으로 나뉜다. 클래스들이 선형 결정 표면들로 정확히 나뉘는 데이터 집합을 **선형 분리 가능**<span class="gloss">linearly separable</span>한 집합이라 한다.
- 실수 표적값을 쓰는 회귀와 달리 분류에서는 **원 핫 인코딩**<span class="gloss">one-hot encoding</span>된 표적값 벡터를 사용한다. $K$개의 클래스가 있고 $\mathcal{C}_j$에 속하면 $\mathbf{t}$는 $K$차원 벡터로 $t_j=1$, 나머지는 $0$이다.
- **판별 함수**<span class="gloss">discriminant function</span>는 입력 벡터 $\mathbf{x}$를 $K$개의 클래스 중 하나에 배정하는 함수이며, 결정 표면이 초평면인 경우를 **선형 판별**<span class="gloss">linear discriminant</span>이라 한다.

### 4.1.1 두 개의 클래스

- 선형 판별 함수는 입력 벡터의 선형 함수다.

$$
y(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}+w_0
$$

  $\mathbf{w}$는 **가중 벡터**<span class="gloss">weight vector</span>, $w_0$은 **편향**<span class="gloss">bias</span>이다. 클래스가 둘이므로 $y(\mathbf{x})\geqslant0$이면 $\mathcal{C}_1$, 아니면 $\mathcal{C}_2$에 배정한다. 결정 경계는 $y(\mathbf{x})=0$이다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.1.png" style="width:20rem;" />
<div class="cap">그림 4.1 · 이차원 선형 판별 함수의 기하학. 적색 결정 표면은 $\mathbf{w}$에 수직이며, 원점으로부터의 거리는 $w_0$이 결정한다.</div>
</div>

- $\mathbf{w}$는 결정 표면의 방향을, $w_0$은 위치를 결정한다. 가변수 $x_0=1$을 도입해 $\widetilde{\mathbf{w}}=(w_0,\mathbf{w})$, $\widetilde{\mathbf{x}}=(x_0,\mathbf{x})$로 두면 $y(\mathbf{x})=\widetilde{\mathbf{w}}^{\top}\widetilde{\mathbf{x}}$로 간단해지고, 결정 표면은 $D+1$차원 확장 공간에서 원점을 지나는 $D$차원 초평면이 된다.

### 4.1.2 다중 클래스

- $K>2$인 경우, 클래스 $\mathcal{C}_k$에 포함되는 점과 그렇지 않은 점을 구분하는 이진 분류기를 $K-1$개 쓰는 **일대다**<span class="gloss">one-versus-the-rest</span> 분류기, 또는 모든 클래스 쌍에 대해 $K(K-1)/2$개의 이진 분류기를 쓰는 **일대일**<span class="gloss">one-versus-one</span> 분류기를 생각할 수 있다. 둘 다 불확실한 영역이 생긴다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.2a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.2b.png" />
</div>
<div class="cap">그림 4.2 · 이진 분류기 집합으로 $K$클래스 판별을 구성할 때 생기는 불확실 영역(녹색). 왼쪽은 일대다, 오른쪽은 일대일 분류기.</div>
</div>

- $K$개의 선형 함수로 이루어진 하나의 $K$클래스 판별 함수를 쓰면 이 문제를 피할 수 있다.

$$
y_k(\mathbf{x})=\mathbf{w}_k^{\top}\mathbf{x}+w_{k0}
$$

  $j\neq k$인 모든 $j$에 대해 $y_k(\mathbf{x})>y_j(\mathbf{x})$면 $\mathbf{x}$를 $\mathcal{C}_k$에 배정한다. $\mathcal{C}_k$와 $\mathcal{C}_j$ 사이 결정 경계 $y_k(\mathbf{x})=y_j(\mathbf{x})$는 다음 $(D-1)$차원 초평면이다.

$$
(\mathbf{w}_k-\mathbf{w}_j)^{\top}\mathbf{x}+(w_{k0}-w_{j0})=0
$$

  이런 판별의 결정 영역은 언제나 단일하게 연결되어 있으며 볼록하다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.3.png" style="width:20rem;" />
<div class="cap">그림 4.3 · 다중 클래스 선형 판별의 결정 경계. 결정 영역은 단일하게 연결되어 있으며 볼록하다.</div>
</div>

### 4.1.3 분류를 위한 최소 제곱법

- $K$개 클래스 모델을 $\mathbf{y}(\mathbf{x})=\widetilde{\mathbf{W}}^{\top}\widetilde{\mathbf{x}}$로 쓸 수 있다($\widetilde{\mathbf{W}}$의 $k$번째 열은 $\widetilde{\mathbf{w}}_k=(w_{k0},\mathbf{w}_k^{\top})^{\top}$). $n$번째 행이 $\mathbf{t}_n^{\top}$인 $\mathbf{T}$, $\widetilde{\mathbf{x}}_n^{\top}$인 $\widetilde{\mathbf{X}}$를 정의하면 제곱합 오류는

$$
E_D(\widetilde{\mathbf{W}})=\frac{1}{2}\operatorname{Tr}\{(\widetilde{\mathbf{X}}\widetilde{\mathbf{W}}-\mathbf{T})^{\top}(\widetilde{\mathbf{X}}\widetilde{\mathbf{W}}-\mathbf{T})\} \tag{4.15}
$$

- $\widetilde{\mathbf{W}}$에 대한 미분을 $0$으로 두고 정리하면 닫힌 형태의 해와 판별 함수를 얻는다.

$$
\widetilde{\mathbf{W}}=(\widetilde{\mathbf{X}}^{\top}\widetilde{\mathbf{X}})^{-1}\widetilde{\mathbf{X}}^{\top}\mathbf{T}=\widetilde{\mathbf{X}}^{\dagger}\mathbf{T},\qquad
\mathbf{y}(\mathbf{x})=\mathbf{T}^{\top}(\widetilde{\mathbf{X}}^{\dagger})^{\top}\widetilde{\mathbf{x}}
$$

- 최소 제곱법은 해를 정확히 닫힌 형태로 구할 수 있으나, 이상값에 강건하지 못하다. 또한 가우시안 조건부 분포 가정하의 최대 가능도와 연관되어 있어, 표적값이 명확히 가우시안이 아니면 제대로 작동하지 않는다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.4a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.4b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.5a.png" />
</div>
<div class="cap">그림 4.4 · (왼쪽) 두 클래스에 대한 최소 제곱 결정 경계(보라색). (가운데) 이상값이 추가되면 결정 경계가 크게 흔들린다. (오른쪽) 세 클래스에서 녹색 클래스가 대부분 오분류된다.</div>
</div>

### 4.1.4 피셔의 선형 판별

- 선형 분류는 차원 감소로도 해석된다. $D$차원 $\mathbf{x}$를 $y=\mathbf{w}^{\top}\mathbf{x}$로 일차원에 투영할 때, $\mathbf{w}$를 잘 고르면 클래스 간 분리를 최대화할 수 있다. 두 클래스의 평균은

$$
\mathbf{m}_1=\frac{1}{N_1}\sum_{n\in\mathcal{C}_1}\mathbf{x}_n,\qquad
\mathbf{m}_2=\frac{1}{N_2}\sum_{n\in\mathcal{C}_2}\mathbf{x}_n
$$

- 투영 후 평균 차이 $m_2-m_1=\mathbf{w}^{\top}(\mathbf{m}_2-\mathbf{m}_1)$만 키우면 $\mathbf{w}$의 크기로 임의로 값을 키울 수 있으므로, 피셔는 **클래스 간 분리는 최대화**하면서 **각 클래스 내 분산은 최소화**하는 기준을 제안했다. 클래스 내 분산 $s_k^2=\sum_{n\in\mathcal{C}_k}(y_n-m_k)^2$에 대해 피셔 기준은

$$
J(\mathbf{w})=\frac{(m_2-m_1)^2}{s_1^2+s_2^2}=\frac{\mathbf{w}^{\top}\mathbf{S}_{\mathrm{B}}\mathbf{w}}{\mathbf{w}^{\top}\mathbf{S}_{\mathrm{W}}\mathbf{w}}
$$

  여기서 **클래스 간**<span class="gloss">between-class</span> 공분산 $\mathbf{S}_{\mathrm{B}}$와 **클래스 내**<span class="gloss">within-class</span> 공분산 $\mathbf{S}_{\mathrm{W}}$는

$$
\mathbf{S}_{\mathrm{B}}=(\mathbf{m}_2-\mathbf{m}_1)(\mathbf{m}_2-\mathbf{m}_1)^{\top},\quad
\mathbf{S}_{\mathrm{W}}=\sum_{n\in\mathcal{C}_1}(\mathbf{x}_n-\mathbf{m}_1)(\mathbf{x}_n-\mathbf{m}_1)^{\top}+\sum_{n\in\mathcal{C}_2}(\mathbf{x}_n-\mathbf{m}_2)(\mathbf{x}_n-\mathbf{m}_2)^{\top}
$$

- $J(\mathbf{w})$를 미분해 정리하면 **피셔의 선형 판별**<span class="gloss">Fisher's linear discriminant</span>을 얻는다.

$$
\mathbf{w}\propto\mathbf{S}_{\mathrm{W}}^{-1}(\mathbf{m}_2-\mathbf{m}_1)
$$

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.6a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.6b.png" />
</div>
<div class="cap">그림 4.6 · (왼쪽) 클래스 평균을 잇는 선에 투영하면 중복이 크다. (오른쪽) 피셔 판별 투영은 클래스 분리가 개선된다.</div>
</div>

::: tip 실습 · 피셔의 선형 판별
클래스 내 산포가 평균 차이 방향으로 늘어나 있어, 평균을 잇는 방향에 투영하면 두 클래스가 겹칩니다. $\mathbf{w}\propto\mathbf{S}_{\mathrm{W}}^{-1}(\mathbf{m}_2-\mathbf{m}_1)$가 분리 척도 $J$를 얼마나 키우는지 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(7)
N1 = N2 = 100
cov = np.array([[3.0, 0.0], [0.0, 0.25]])               # 한 방향으로 길쭉한 산포
th = np.deg2rad(-35); R = np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
cov = R @ cov @ R.T
X1 = rng.multivariate_normal([0, 0],   cov, N1)
X2 = rng.multivariate_normal([2.2, 0], cov, N2)
m1, m2 = X1.mean(0), X2.mean(0)
Sw = (X1-m1).T@(X1-m1) + (X2-m2).T@(X2-m2)              # 클래스 내 공분산
w_fisher = np.linalg.solve(Sw, m2-m1); w_fisher /= np.linalg.norm(w_fisher)
w_mean   = (m2-m1)/np.linalg.norm(m2-m1)                # 평균 연결 방향
def J(w):
    p1, p2 = X1@w, X2@w
    return (p1.mean()-p2.mean())**2 / (p1.var()+p2.var())
print(f"평균 연결 방향  J = {J(w_mean):.2f}")
print(f"피셔 판별 방향  J = {J(w_fisher):.2f}   (더 큼 = 더 잘 분리)")
```

</PyRunner>

### 4.1.5 퍼셉트론

- **퍼셉트론**<span class="gloss">perceptron</span>은 입력을 고정된 비선형 변환으로 특징 벡터 $\boldsymbol{\phi}(\mathbf{x})$로 바꾼 뒤 일반화된 선형 모델 $y(\mathbf{x})=f(\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x}))$을 만든다. **비선형 활성화 함수**<span class="gloss">nonlinear activation function</span>는 $f(a)=+1\,(a\geqslant0)$, $-1\,(a<0)$이며, 표적값은 $t\in\{-1,1\}$을 쓴다.
- **퍼셉트론 기준**<span class="gloss">perceptron criterion</span> $E_P(\mathbf{w})=-\sum_{n\in\mathcal{M}}\mathbf{w}^{\top}\boldsymbol{\phi}_n t_n$($\mathcal{M}$: 오분류 집합)에 확률적 경사 하강법을 적용하면

$$
\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}+\eta\,\boldsymbol{\phi}_n t_n
$$

  선형 분리 가능한 데이터에 대해서는 유한 번의 갱신으로 수렴함이 보장된다(퍼셉트론 수렴 정리).

::: tip 실습 · 퍼셉트론 학습
선형 분리 가능한 두 클래스에 대해 오분류된 표본마다 $\mathbf{w}\leftarrow\mathbf{w}+\eta\,\boldsymbol{\phi}_n t_n$을 적용합니다. 에폭마다 오분류 수가 줄어 $0$에 도달하는 것을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(4)
Np = 40
X = np.vstack([rng.normal([-1.4,-1.4], 0.85, (Np,2)),
               rng.normal([ 1.4, 1.4], 0.85, (Np,2))])
t = np.concatenate([-np.ones(Np), np.ones(Np)])          # 표적값 t ∈ {-1, +1}
Phi = np.column_stack([np.ones(len(X)), X])              # 편향 + 특징 2개
w = np.zeros(3); eta = 0.1
for epoch in range(30):
    mis = 0
    for n in rng.permutation(len(X)):
        pred = 1.0 if Phi[n]@w >= 0 else -1.0
        if pred != t[n]:
            w = w + eta*Phi[n]*t[n]; mis += 1           # w ← w + η φ_n t_n
    print(f"에폭 {epoch+1}: 오분류 {mis}개")
    if mis == 0: break
print("최종 w =", np.round(w, 3).tolist())
```

</PyRunner>

## 4.2 확률적 생성 모델

- 생성적 접근은 클래스별 조건부 밀도 $p(\mathbf{x}\mid\mathcal{C}_k)$와 클래스 사전 분포 $p(\mathcal{C}_k)$를 모델링한 뒤 베이즈 정리로 사후 확률 $p(\mathcal{C}_k\mid\mathbf{x})$를 계산한다. 두 클래스의 경우 사후 확률은 **로지스틱 시그모이드**<span class="gloss">logistic sigmoid</span> $\sigma$로 표현된다.

$$
p(\mathcal{C}_1\mid\mathbf{x})=\frac{p(\mathbf{x}\mid\mathcal{C}_1)p(\mathcal{C}_1)}{p(\mathbf{x}\mid\mathcal{C}_1)p(\mathcal{C}_1)+p(\mathbf{x}\mid\mathcal{C}_2)p(\mathcal{C}_2)}=\sigma(a),\quad
a=\ln\frac{p(\mathbf{x}\mid\mathcal{C}_1)p(\mathcal{C}_1)}{p(\mathbf{x}\mid\mathcal{C}_2)p(\mathcal{C}_2)}
$$

- 시그모이드는 대칭성 $\sigma(-a)=1-\sigma(a)$를 만족하며, 그 역함수를 **로짓**<span class="gloss">logit</span> 함수 $a=\ln\{\sigma/(1-\sigma)\}$라 한다. $K>2$인 경우는 시그모이드를 일반화한 **소프트맥스 함수**<span class="gloss">softmax function</span>를 쓴다.

$$
p(\mathcal{C}_k\mid\mathbf{x})=\frac{\exp(a_k)}{\sum_j\exp(a_j)},\qquad a_k=\ln\bigl(p(\mathbf{x}\mid\mathcal{C}_k)p(\mathcal{C}_k)\bigr)
$$

### 4.2.1 연속 입력

- 클래스별 조건부 밀도를 가우시안으로 두고 모든 클래스가 **같은 공분산 $\boldsymbol{\Sigma}$를 공유**한다고 가정하면, 두 클래스의 사후 확률은 $\mathbf{x}$에 대한 선형 함수의 시그모이드가 된다.

$$
p(\mathcal{C}_1\mid\mathbf{x})=\sigma(\mathbf{w}^{\top}\mathbf{x}+w_0),\quad
\mathbf{w}=\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)
$$

$$
w_0=-\frac{1}{2}\boldsymbol{\mu}_1^{\top}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_1+\frac{1}{2}\boldsymbol{\mu}_2^{\top}\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_2+\ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}
$$

  공분산 공유 가정으로 가우시안 지수부의 $\mathbf{x}$ 이차항이 상쇄되어, 시그모이드의 입력이 $\mathbf{x}$에 대한 선형 함수가 되었다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.10a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.10b.png" />
</div>
<div class="cap">그림 4.10 · (왼쪽) 두 클래스의 조건부 밀도. (오른쪽) 사후 확률 $p(\mathcal{C}_1\mid\mathbf{x})$.</div>
</div>

### 4.2.2 최대 가능도 해

- 클래스 조건부 밀도의 함수 형태를 정하면 최대 가능도로 매개변수와 사전 확률을 추정할 수 있다. 두 클래스·공유 공분산·$p(\mathcal{C}_1)=\pi$ 가정하에서 가능도는

$$
p(\mathsf{t},\mathbf{X}\mid\pi,\boldsymbol{\mu}_1,\boldsymbol{\mu}_2,\boldsymbol{\Sigma})=\prod_{n=1}^N\bigl[\pi\mathcal{N}(\mathbf{x}_n\mid\boldsymbol{\mu}_1,\boldsymbol{\Sigma})\bigr]^{t_n}\bigl[(1-\pi)\mathcal{N}(\mathbf{x}_n\mid\boldsymbol{\mu}_2,\boldsymbol{\Sigma})\bigr]^{1-t_n}
$$

- 각 매개변수에 대해 미분을 $0$으로 두면 직관적인 최대 가능도 추정값을 얻는다. 사전 확률은 클래스 비율, 평균은 각 클래스 표본 평균, 공유 공분산은 클래스별 공분산의 가중 평균이다.

$$
\pi=\frac{N_1}{N},\qquad
\boldsymbol{\mu}_1=\frac{1}{N_1}\sum_{n=1}^N t_n\mathbf{x}_n,\qquad
\boldsymbol{\mu}_2=\frac{1}{N_2}\sum_{n=1}^N(1-t_n)\mathbf{x}_n
$$

$$
\mathbf{S}=\frac{N_1}{N}\mathbf{S}_1+\frac{N_2}{N}\mathbf{S}_2,\quad
\mathbf{S}_k=\frac{1}{N_k}\sum_{n\in\mathcal{C}_k}(\mathbf{x}_n-\boldsymbol{\mu}_k)(\mathbf{x}_n-\boldsymbol{\mu}_k)^{\top}
$$

::: tip 실습 · 생성적 가우시안 분류기 (공유 공분산)
두 클래스의 평균·공유 공분산을 최대 가능도로 추정한 뒤 $\mathbf{w}=\mathbf{S}^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)$, $w_0$을 계산하고, 사후 확률 $\sigma(\mathbf{w}^{\top}\mathbf{x}+w_0)$로 분류합니다.
:::

<PyRunner>

```python
import numpy as np
def sig(a): return 1/(1+np.exp(-a))
rng = np.random.default_rng(3)
Nc = 80
C1 = rng.multivariate_normal([ 1,  1],   [[1,0.3],[0.3,1]], Nc)
C2 = rng.multivariate_normal([-1, -1.5], [[1,0.3],[0.3,1]], Nc)
mu1, mu2 = C1.mean(0), C2.mean(0)
pi = Nc/(2*Nc)
S1 = (C1-mu1).T@(C1-mu1)/Nc; S2 = (C2-mu2).T@(C2-mu2)/Nc
S  = pi*S1 + (1-pi)*S2                                   # 공유 공분산
Sinv = np.linalg.inv(S)
w  = Sinv@(mu1-mu2)
w0 = -0.5*mu1@Sinv@mu1 + 0.5*mu2@Sinv@mu2 + np.log(pi/(1-pi))
print("w  =", np.round(w, 3).tolist(), "  w0 =", round(float(w0), 3))
for x in [mu1, mu2, (mu1+mu2)/2]:
    print(f"  x={np.round(x,2).tolist()}: p(C1|x)={sig(w@x+w0):.3f}")
Xall = np.vstack([C1, C2]); tall = np.concatenate([np.ones(Nc), np.zeros(Nc)])
acc = np.mean((sig(Xall@w + w0) > 0.5) == tall)
print("분류 정확도 =", f"{acc:.1%}")
```

</PyRunner>

## 4.3 확률적 판별 모델

- 판별적 접근은 일반화된 선형 모델의 함수 형태를 명시적으로 쓰고 최대 가능도로 매개변수를 **직접** 구한다. 생성적 모델링과 달리 조절할 매개변수가 대체로 더 적고, 클래스 조건부 밀도 가정이 실제 분포와 어긋날 때 더 나은 성능을 보인다. 이 해를 구하는 효율적 알고리즘이 **반복 재가중 최소 제곱법**<span class="gloss">iterative reweighted least squares; IRLS</span>이다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.12a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.12b.png" />
</div>
<div class="cap">그림 4.12 · 비선형 기저 함수의 역할. (왼쪽) 원 입력 공간 $(x_1,x_2)$에서 겹쳐 있는 두 클래스. (오른쪽) 가우시안 기저 함수로 변환한 특징 공간 $(\phi_1,\phi_2)$에서는 선형 결정 경계로 분리된다.</div>
</div>

### 4.3.1 고정된 기저 함수

- 앞의 알고리즘들은 원 입력 $\mathbf{x}$뿐 아니라 기저 함수 벡터 $\boldsymbol{\phi}(\mathbf{x})$에 대해서도 그대로 적용된다. 결정 경계는 특징 공간 $\boldsymbol{\phi}$에서 선형이지만 $\mathbf{x}$ 공간에서는 비선형일 수 있다. 적절한 비선형 변환은 클래스 조건부 밀도가 크게 겹치는 경우에도 사후 확률 모델링을 쉽게 만든다.

### 4.3.2 로지스틱 회귀

- 두 클래스 문제에서 $\mathcal{C}_1$의 사후 확률을 특징 벡터의 선형 함수에 대한 시그모이드로 쓴 모델을 **로지스틱 회귀**<span class="gloss">logistic regression</span>라 한다.

$$
p(\mathcal{C}_1\mid\boldsymbol{\phi})=y(\boldsymbol{\phi})=\sigma(\mathbf{w}^{\top}\boldsymbol{\phi})
$$

  $M$차원 특징 공간에서 로지스틱 회귀는 $M$개의 매개변수를 가진다. 생성적 방법이 평균에 $2M$개, 공분산에 $M(M+1)/2$개로 $M$에 대해 이차로 증가하는 것과 달리, 로지스틱 회귀는 선형으로 증가한다.

- 데이터 $\{\boldsymbol{\phi}_n,t_n\}$($t_n\in\{0,1\}$)에 대한 가능도 $p(\mathsf{t}\mid\mathbf{w})=\prod_n y_n^{t_n}(1-y_n)^{1-t_n}$의 음의 로그값이 **교차 엔트로피**<span class="gloss">cross-entropy</span> 오류 함수다.

$$
E(\mathbf{w})=-\ln p(\mathsf{t}\mid\mathbf{w})=-\sum_{n=1}^N\{t_n\ln y_n+(1-t_n)\ln(1-y_n)\},\quad y_n=\sigma(\mathbf{w}^{\top}\boldsymbol{\phi}_n)
$$

- 시그모이드의 미분 $\dfrac{\mathrm{d}\sigma}{\mathrm{d}a}=\sigma(1-\sigma)$를 이용하면 기울기가 회귀와 같은 간단한 형태가 된다.

$$
\nabla E(\mathbf{w})=\sum_{n=1}^N(y_n-t_n)\boldsymbol{\phi}_n
$$

### 4.3.3 반복 재가중 최소 제곱법

- 로지스틱 회귀는 시그모이드의 비선형성 때문에 해가 닫힌 형태가 아니지만, 오류 함수가 볼록해 유일한 최솟값을 가진다. **뉴턴–라프슨**<span class="gloss">Newton–Raphson</span> 갱신 $\mathbf{w}^{(\mathrm{new})}=\mathbf{w}^{(\mathrm{old})}-\mathbf{H}^{-1}\nabla E(\mathbf{w})$을 적용한다. 교차 엔트로피에 대한 기울기와 헤시안은

$$
\nabla E(\mathbf{w})=\boldsymbol{\Phi}^{\top}(\mathsf{y}-\mathsf{t}),\qquad
\mathbf{H}=\boldsymbol{\Phi}^{\top}\mathbf{R}\boldsymbol{\Phi},\quad R_{nn}=y_n(1-y_n)
$$

- 헤시안이 $\mathbf{R}$을 통해 $\mathbf{w}$에 종속되므로 갱신을 반복해야 한다. 갱신식은 가중 최소 제곱의 정규 방정식 형태를 띤다.

$$
\mathbf{w}^{(\mathrm{new})}=(\boldsymbol{\Phi}^{\top}\mathbf{R}\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^{\top}\mathbf{R}\,\mathsf{z},\qquad
\mathsf{z}=\boldsymbol{\Phi}\mathbf{w}^{(\mathrm{old})}-\mathbf{R}^{-1}(\mathsf{y}-\mathsf{t}) \tag{4.99}
$$

  매 반복마다 새 $\mathbf{w}$로 가중 행렬 $\mathbf{R}$을 다시 구하므로 반복 재가중 최소 제곱법이라 부른다.

::: tip 실습 · 로지스틱 회귀 (IRLS/뉴턴–라프슨)
$\mathbf{H}=\boldsymbol{\Phi}^{\top}\mathbf{R}\boldsymbol{\Phi}$, $\nabla E=\boldsymbol{\Phi}^{\top}(\mathsf{y}-\mathsf{t})$로 뉴턴–라프슨 갱신을 반복합니다. 교차 엔트로피가 빠르게(이차 수렴) 줄어드는 것을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
def sig(a): return 1/(1+np.exp(-a))
rng = np.random.default_rng(2)
Na = 60
X = np.vstack([rng.normal([-1,-1], 1.3, (Na,2)),
               rng.normal([1.2,1.2], 1.3, (Na,2))])
t = np.concatenate([np.zeros(Na), np.ones(Na)])
Phi = np.column_stack([np.ones(len(X)), X])             # 편향 + 특징 2개
w = np.zeros(3)
for it in range(8):
    y = sig(Phi@w); R = y*(1-y)                          # R_nn = y_n(1-y_n)
    H = (Phi*R[:,None]).T@Phi + 1e-8*np.eye(3)          # 헤시안 ΦᵀRΦ
    w_new = w - np.linalg.solve(H, Phi.T@(y-t))         # 뉴턴–라프슨 갱신
    step = np.linalg.norm(w_new-w); w = w_new
    ce = -np.sum(t*np.log(y+1e-12) + (1-t)*np.log(1-y+1e-12))
    print(f"반복 {it+1}: 교차엔트로피={ce:7.3f}  |Δw|={step:.2e}")
    if step < 1e-6: break
print("수렴 w =", np.round(w,3).tolist(),
      "  정확도 =", f"{np.mean((sig(Phi@w)>0.5)==t):.1%}")
```

</PyRunner>

## 4.4 라플라스 근사

- **라플라스 근사**<span class="gloss">Laplace approximation</span>는 연속 변수 집합에 대한 확률 밀도의 가우시안 근사를 찾는 방법이다.

::: info 라플라스 근사법
단일 연속 변수 $z$에 대해 $p(z)=\dfrac{1}{Z}f(z)$, $Z=\int f(z)\,\mathrm{d}z$인 분포를 가정한다. 정규화 계수 $Z$를 모를 때, 최빈값을 중심으로 한 가우시안 근사 $q(z)$를 다음 단계로 찾는다.

1. 최빈값 $z_0$을 구한다: $\left.\dfrac{\mathrm{d}f(z)}{\mathrm{d}z}\right|_{z=z_0}=0$.

2. $z_0$ 주변에서 $\ln f(z)$를 테일러 전개한다: $\ln f(z)\simeq\ln f(z_0)-\dfrac{1}{2}A(z-z_0)^2$, $A=-\left.\dfrac{\mathrm{d}^2}{\mathrm{d}z^2}\ln f(z)\right|_{z=z_0}$.

3. $z_0$이 지역적 최댓값이라 일차항이 사라지고, 지수를 취하면 $f(z)\simeq f(z_0)\exp\{-\tfrac{A}{2}(z-z_0)^2\}$.

4. 정규화하면 $q(z)=\left(\dfrac{A}{2\pi}\right)^{1/2}\exp\{-\tfrac{A}{2}(z-z_0)^2\}$.
:::

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.14a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure4.14b.png" />
</div>
<div class="cap">그림 4.14 · 분포 $p(z)\propto\exp(-z^2/2)\,\sigma(20z+4)$의 라플라스 근사. (왼쪽) 황색은 정규화 분포 $p(z)$, 적색은 최빈값 중심 라플라스 근사. (오른쪽) 각 곡선의 음의 로그값.</div>
</div>

- $M$차원 $\mathbf{z}$로 확장하면 임계점 $\nabla f(\mathbf{z}_0)=0$에서 전개해 다변량 가우시안 근사를 얻는다.

$$
q(\mathbf{z})=\frac{|\mathbf{A}|^{1/2}}{(2\pi)^{M/2}}\exp\Bigl\{-\frac{1}{2}(\mathbf{z}-\mathbf{z}_0)^{\top}\mathbf{A}(\mathbf{z}-\mathbf{z}_0)\Bigr\}=\mathcal{N}(\mathbf{z}\mid\mathbf{z}_0,\mathbf{A}^{-1}),\quad
\mathbf{A}=-\nabla\nabla\ln f(\mathbf{z})\big|_{\mathbf{z}=\mathbf{z}_0}
$$

  중심 극한 정리에 따라 데이터가 많을수록 사후 분포가 가우시안에 가까워지므로, 데이터가 많을 때 라플라스 근사가 더 유용하다.

::: tip 실습 · 라플라스 근사 (그림 4.14 재현)
$f(z)=\exp(-z^2/2)\,\sigma(20z+4)$의 최빈값 $z_0$과 곡률 $A=-\left.\frac{\mathrm{d}^2}{\mathrm{d}z^2}\ln f\right|_{z_0}$을 구해 근사 분산 $A^{-1}$과 정규화 상수 $Z$를 추정하고, 수치 적분값과 비교합니다.
:::

<PyRunner>

```python
import numpy as np
def sig(a): return 1/(1+np.exp(-a))
def lnf(z): return -0.5*z*z + np.log(sig(20*z+4))       # ln f(z)
zs = np.linspace(-3, 3, 60001); dz = zs[1]-zs[0]
z0 = zs[np.argmax(lnf(zs))]                              # 최빈값
u = 20*z0 + 4; s = sig(u)
A = 1 + 400*s*(1-s)                                     # 곡률 A = -d²/dz² ln f
print(f"최빈값 z0 = {z0:.4f},  곡률 A = {A:.3f},  근사 분산 A⁻¹ = {1/A:.5f}")
fz = np.exp(lnf(zs))
Z_num = float(np.sum(fz)*dz)                             # 수치 적분
Z_lap = float(np.exp(lnf(z0)) * np.sqrt(2*np.pi/A))     # 라플라스 근사
print(f"Z(수치 적분) = {Z_num:.4f}   Z(라플라스) = {Z_lap:.4f}")
```

</PyRunner>

### 4.4.1 모델 비교와 베이지안 정보 기준

- 라플라스 근사로 정규화 상수 $Z\simeq f(\mathbf{z}_0)\dfrac{(2\pi)^{M/2}}{|\mathbf{A}|^{1/2}}$를 얻는다. 이를 모델 증거 $p(\mathcal{D})=\int p(\mathcal{D}\mid\boldsymbol{\theta})p(\boldsymbol{\theta})\,\mathrm{d}\boldsymbol{\theta}$에 적용하면

$$
\ln p(\mathcal{D})\simeq\ln p(\mathcal{D}\mid\boldsymbol{\theta}_{\mathrm{MAP}})+\ln p(\boldsymbol{\theta}_{\mathrm{MAP}})+\frac{M}{2}\ln(2\pi)-\frac{1}{2}\ln|\mathbf{A}| \tag{4.137}
$$

  첫 항은 최적 매개변수의 로그 가능도, 나머지는 모델 복잡도에 벌점을 주는 **오컴 인자**<span class="gloss">Occam factor</span>다.

- 사전 분포가 넓게 퍼지고 헤시안이 최대 계수라 가정하면 위 식은 다음으로 근사되며, 이를 **베이지안 정보 기준**<span class="gloss">Bayesian information criterion; BIC</span> 또는 **슈바르츠 기준**<span class="gloss">Schwarz criterion</span>이라 한다($N$: 데이터 수, $M$: 매개변수 수).

$$
\ln p(\mathcal{D})\simeq\ln p(\mathcal{D}\mid\boldsymbol{\theta}_{\mathrm{MAP}})-\frac{1}{2}M\ln N
$$

## 4.5 베이지안 로지스틱 회귀

### 4.5.1 사후 분포 계산

- 베이지안 로지스틱 회귀의 사후 분포는 가능도가 각 데이터 포인트의 시그모이드를 곱한 형태라 정확한 계산이 어렵다. 라플라스 근사로 비교적 쉽게 다룬다. 가우시안 사전 분포 $p(\mathbf{w})=\mathcal{N}(\mathbf{w}\mid\mathbf{m}_0,\mathbf{S}_0)$을 두면 로그 사후 분포는

$$
\ln p(\mathbf{w}\mid\mathsf{t})=-\frac{1}{2}(\mathbf{w}-\mathbf{m}_0)^{\top}\mathbf{S}_0^{-1}(\mathbf{w}-\mathbf{m}_0)+\sum_{n=1}^N\{t_n\ln y_n+(1-t_n)\ln(1-y_n)\}+\text{const}
$$

- 이를 최대화해 $\mathbf{w}_{\mathrm{MAP}}$를 구하고, 공분산은 음의 로그 사후 분포의 헤시안의 역으로 얻는다.

$$
\mathbf{S}_N^{-1}=-\nabla\nabla\ln p(\mathbf{w}\mid\mathsf{t})=\mathbf{S}_0^{-1}+\sum_{n=1}^N y_n(1-y_n)\boldsymbol{\phi}_n\boldsymbol{\phi}_n^{\top}
$$

  따라서 사후 분포의 가우시안 근사는 $q(\mathbf{w})=\mathcal{N}(\mathbf{w}\mid\mathbf{w}_{\mathrm{MAP}},\mathbf{S}_N)$이다.

### 4.5.2 예측 분포

- 새 특징 벡터 $\boldsymbol{\phi}$에 대한 예측 분포는 $q(\mathbf{w})$에 대해 주변화해 구한다. $a=\mathbf{w}^{\top}\boldsymbol{\phi}$가 가우시안 $\mathcal{N}(a\mid\mu_a,\sigma_a^2)$을 따르므로

$$
\mu_a=\mathbf{w}_{\mathrm{MAP}}^{\top}\boldsymbol{\phi},\qquad
\sigma_a^2=\boldsymbol{\phi}^{\top}\mathbf{S}_N\boldsymbol{\phi}
$$

$$
p(\mathcal{C}_1\mid\boldsymbol{\phi},\mathsf{t})=\int\sigma(a)\,p(a)\,\mathrm{d}a=\int\sigma(a)\,\mathcal{N}(a\mid\mu_a,\sigma_a^2)\,\mathrm{d}a
$$

  이 일차원 적분은 사후 분포의 불확실성을 반영해, 결정 경계에서 멀어질수록 예측이 더 완만해진다.

## 연습문제

::: info 문제 4.1
로지스틱 시그모이드 함수가 $\sigma(-a)=1-\sigma(a)$를 만족함을 증명하고, 그 역함수를 구하라.
:::

::: details 풀이
**대칭성** — 정의 $\sigma(a)=\dfrac{1}{1+e^{-a}}$에서

$$
\sigma(-a)=\frac{1}{1+e^{a}}=\frac{e^{-a}}{e^{-a}+1}=\frac{1+e^{-a}-1}{1+e^{-a}}=1-\frac{1}{1+e^{-a}}=1-\sigma(a)
$$

**역함수** — $y=\sigma(a)$로 두면 $y=\dfrac{1}{1+e^{-a}}$이므로 $1+e^{-a}=\dfrac{1}{y}$, $e^{-a}=\dfrac{1-y}{y}$. 양변에 로그를 취하면

$$
a=\ln\frac{y}{1-y}
$$

이것이 **로짓** 함수다.
:::

::: info 문제 4.2
데이터 집합 $\{\mathbf{x}_n\}$의 **최소 볼록 집합**<span class="gloss">convex hull</span>을 $\mathbf{x}=\sum_n\alpha_n\mathbf{x}_n$ ($\alpha_n\geqslant0$, $\sum_n\alpha_n=1$)인 모든 점 $\mathbf{x}$로 정의한다. 두 집합 $\{\mathbf{x}_n\}$, $\{\mathbf{y}_n\}$의 최소 볼록 집합이 교차하면 두 집합은 선형 분리 불가능함을, 선형 분리 가능하면 두 볼록 집합이 교차하지 않음을 증명하라.
:::

::: details 풀이
**정의** — 선형 분리 가능이란 모든 $\mathbf{x}_n$에 대해 $\widehat{\mathbf{w}}^{\top}\mathbf{x}_n+w_0>0$, 모든 $\mathbf{y}_n$에 대해 $\widehat{\mathbf{w}}^{\top}\mathbf{y}_n+w_0<0$인 $(\widehat{\mathbf{w}},w_0)$이 존재함을 뜻한다.

**볼록 집합이 교차하면 분리 불가능** — 두 볼록 집합이 공통점 $\mathbf{z}$를 가진다고 하자. 그러면 $\mathbf{z}=\sum_n\alpha_n\mathbf{x}_n=\sum_m\beta_m\mathbf{y}_m$ ($\alpha_n,\beta_m\geqslant0$, $\sum\alpha_n=\sum\beta_m=1$). 선형 분리 가능하다고 가정하면 $\{\mathbf{x}_n\}$ 쪽 표현에서

$$
\widehat{\mathbf{w}}^{\top}\mathbf{z}+w_0=\sum_n\alpha_n(\widehat{\mathbf{w}}^{\top}\mathbf{x}_n+w_0)>0
$$

(각 항이 양수이고 $\sum\alpha_n=1$이므로). 동시에 $\{\mathbf{y}_m\}$ 쪽 표현에서

$$
\widehat{\mathbf{w}}^{\top}\mathbf{z}+w_0=\sum_m\beta_m(\widehat{\mathbf{w}}^{\top}\mathbf{y}_m+w_0)<0
$$

같은 값이 양수이면서 음수일 수는 없으므로 모순이다. 따라서 볼록 집합이 교차하면 선형 분리가 불가능하다.

**대우** — 위 명제의 대우가 곧 "선형 분리 가능하면 두 볼록 집합은 교차하지 않는다"이므로 함께 증명된다. $\blacksquare$
:::

::: info 문제 4.3
식 (4.15)의 제곱합 오류 최소화를 고려하자. 훈련 집합의 모든 표적값 벡터가 선형 제약 $\mathbf{a}^{\top}\mathbf{t}_n+b=0$($\mathbf{t}_n$은 $\mathbf{T}$의 $n$번째 행)을 만족하면, 모델의 예측도 $\mathbf{a}^{\top}\mathbf{y}(\mathbf{x})+b=0$을 만족함을 증명하라. (기저 함수 중 $\phi_0(\mathbf{x})=1$이고 $w_0$이 편향 역할을 한다고 가정한다.)
:::

::: details 풀이
최소 제곱 해는 $\widetilde{\mathbf{W}}=(\widetilde{\mathbf{X}}^{\top}\widetilde{\mathbf{X}})^{-1}\widetilde{\mathbf{X}}^{\top}\mathbf{T}$이고 예측은 $\mathbf{y}(\mathbf{x})=\widetilde{\mathbf{W}}^{\top}\widetilde{\mathbf{x}}$이다. 제약 조건을 모든 $n$에 모으면 행렬 형태로 $\mathbf{T}\mathbf{a}+b\mathbf{1}=\mathbf{0}$, 즉

$$
\mathbf{T}\mathbf{a}=-b\mathbf{1}
$$

여기서 $\mathbf{1}$은 모든 성분이 $1$인 $N$차원 벡터다. 예측에 $\mathbf{a}$를 곱하면

$$
\mathbf{a}^{\top}\mathbf{y}(\mathbf{x})=\mathbf{a}^{\top}\mathbf{T}^{\top}(\widetilde{\mathbf{X}}^{\dagger})^{\top}\widetilde{\mathbf{x}}=(\mathbf{T}\mathbf{a})^{\top}(\widetilde{\mathbf{X}}^{\dagger})^{\top}\widetilde{\mathbf{x}}=-b\,\mathbf{1}^{\top}(\widetilde{\mathbf{X}}^{\dagger})^{\top}\widetilde{\mathbf{x}}
$$

$\widetilde{\mathbf{X}}^{\dagger}=(\widetilde{\mathbf{X}}^{\top}\widetilde{\mathbf{X}})^{-1}\widetilde{\mathbf{X}}^{\top}$이므로 $\mathbf{1}^{\top}(\widetilde{\mathbf{X}}^{\dagger})^{\top}\widetilde{\mathbf{x}}=\mathbf{1}^{\top}\widetilde{\mathbf{X}}(\widetilde{\mathbf{X}}^{\top}\widetilde{\mathbf{X}})^{-1}\widetilde{\mathbf{x}}$이다. 가변수 $\phi_0=1$ 가정에서 $\widetilde{\mathbf{X}}$의 첫 열은 $\mathbf{1}$이므로 $\widetilde{\mathbf{X}}^{\top}\mathbf{1}=(\widetilde{\mathbf{X}}^{\top}\widetilde{\mathbf{X}})_{:,0}$, 결국 $\mathbf{1}^{\top}\widetilde{\mathbf{X}}(\widetilde{\mathbf{X}}^{\top}\widetilde{\mathbf{X}})^{-1}=\mathbf{e}_0^{\top}$(첫 성분만 $1$)이 되어 $\mathbf{1}^{\top}(\widetilde{\mathbf{X}}^{\dagger})^{\top}\widetilde{\mathbf{x}}=\widetilde{x}_0=1$. 따라서

$$
\mathbf{a}^{\top}\mathbf{y}(\mathbf{x})=-b\quad\Longrightarrow\quad\mathbf{a}^{\top}\mathbf{y}(\mathbf{x})+b=0
$$

즉 표적값에 걸린 선형 제약이 예측값에서도 그대로 성립한다. $\blacksquare$
:::

::: info 문제 4.4
사전 클래스 확률 $p(\mathcal{C}_k)=\pi_k$와 클래스 조건부 밀도 $p(\boldsymbol{\phi}\mid\mathcal{C}_k)$로 정의된 $K$클래스 생성 모델을 고려하자(표적값은 원 핫 인코딩). 데이터가 독립적으로 추출될 때 사전 확률의 최대 가능도 해가 $\pi_k=\dfrac{N_k}{N}$($N_k$: $\mathcal{C}_k$에 할당된 데이터 수)임을 증명하라.
:::

::: details 풀이
데이터 $\{\boldsymbol{\phi}_n,\mathbf{t}_n\}$에서 $t_{nk}$를 원 핫 표적값의 $k$번째 성분이라 하자. 로그 가능도 중 $\{\pi_k\}$에 종속된 부분은

$$
\sum_{n=1}^N\sum_{k=1}^K t_{nk}\ln\pi_k=\sum_{k=1}^K N_k\ln\pi_k,\qquad N_k=\sum_{n=1}^N t_{nk}
$$

제약 $\sum_k\pi_k=1$을 라그랑주 승수 $\lambda$로 넣어

$$
L=\sum_{k=1}^K N_k\ln\pi_k+\lambda\Bigl(\sum_{k=1}^K\pi_k-1\Bigr)
$$

$\pi_k$로 미분해 $0$으로 두면 $\dfrac{N_k}{\pi_k}+\lambda=0$, 즉 $\pi_k=-\dfrac{N_k}{\lambda}$. 제약에 대입하면 $\sum_k\pi_k=-\dfrac{1}{\lambda}\sum_k N_k=-\dfrac{N}{\lambda}=1$이므로 $\lambda=-N$. 따라서

$$
\pi_k=\frac{N_k}{N}
$$

각 클래스의 사전 확률 최대 가능도 추정값은 그 클래스에 속한 데이터의 비율이다. $\blacksquare$
:::
