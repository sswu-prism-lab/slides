# 5 · 커널 방법론

> 지금까지 다룬 선형 매개변수 모델은 입력에서 출력까지의 사상이 매개변수에 종속적이었고, 훈련 데이터는 매개변수의 점 추정치나 사후 분포를 구한 뒤 버려졌다. 이와 달리 훈련 데이터의 전부 혹은 일부를 예측 단계에서도 사용하는 패턴 인식 방법론이 있다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/photos/sec05.png" style="max-width:34rem;" />
</div>

## 5.1 듀얼 표현

- 많은 선형 매개변수 모델은 **듀얼 표현**<span class="gloss">dual representation</span>으로 재구성할 수 있으며, 이 형태에서는 훈련 데이터에서 계산한 **커널 함수**<span class="gloss">kernel function</span>들의 선형 결합으로 표적값을 예측한다. 고정된 비선형 **특징 공간**<span class="gloss">feature space</span> 사상 $\boldsymbol{\phi}(\mathbf{x})$에 대해 커널은

$$
k(\mathbf{x},\mathbf{x}')=\boldsymbol{\phi}(\mathbf{x})^{\top}\boldsymbol{\phi}(\mathbf{x}')
$$

  로 정의되며, 인자에 대해 대칭이다($k(\mathbf{x},\mathbf{x}')=k(\mathbf{x}',\mathbf{x})$). 커널을 특징 공간의 내적으로 정의할 수 있다는 점을 이용해 알고리즘을 확장하는 기법을 **커널 트릭**<span class="gloss">kernel trick</span>이라 한다.

- 정규화된 제곱합 오류 $J(\mathbf{w})=\frac{1}{2}\sum_n\{\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x}_n)-t_n\}^2+\frac{\lambda}{2}\mathbf{w}^{\top}\mathbf{w}$를 $\mathbf{w}$에 대해 풀면, 해가 $\boldsymbol{\phi}(\mathbf{x}_n)$들의 선형 결합임을 알 수 있다.

$$
\mathbf{w}=\sum_{n=1}^N a_n\boldsymbol{\phi}(\mathbf{x}_n)=\boldsymbol{\Phi}^{\top}\mathbf{a},\qquad a_n=-\frac{1}{\lambda}\{\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x}_n)-t_n\}
$$

- $\mathbf{w}=\boldsymbol{\Phi}^{\top}\mathbf{a}$를 대입하면 오류 함수는 **그램 행렬**<span class="gloss">Gram matrix</span> $\mathbf{K}=\boldsymbol{\Phi}\boldsymbol{\Phi}^{\top}$($K_{nm}=k(\mathbf{x}_n,\mathbf{x}_m)$)만으로 표현된다.

$$
J(\mathbf{a})=\frac{1}{2}\mathbf{a}^{\top}\mathbf{K}\mathbf{K}\mathbf{a}-\mathbf{a}^{\top}\mathbf{K}\mathsf{t}+\frac{1}{2}\mathsf{t}^{\top}\mathsf{t}+\frac{\lambda}{2}\mathbf{a}^{\top}\mathbf{K}\mathbf{a}
$$

- $\mathbf{a}$에 대해 풀면 $\mathbf{a}=(\mathbf{K}+\lambda\mathbf{I}_N)^{-1}\mathsf{t}$이고, 새 입력에 대한 예측은 커널만으로 표현된다.

$$
y(\mathbf{x})=\mathbf{k}(\mathbf{x})^{\top}(\mathbf{K}+\lambda\mathbf{I}_N)^{-1}\mathsf{t},\qquad k_n(\mathbf{x})=k(\mathbf{x}_n,\mathbf{x})
$$

  이렇게 해를 커널만으로 표현하는 것을 **듀얼 공식화**<span class="gloss">dual formulation</span>라 한다. 특징 벡터 $\boldsymbol{\phi}(\mathbf{x})$를 명시적으로 다루지 않고 커널 값만 계산하면 되는 것이 핵심이다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.1a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.1b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.1c.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.1d.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.1e.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.1f.png" />
</div>
<div class="cap">그림 6.1 · 기저 함수 집합으로부터 커널을 구성하는 도식. 각 열의 위쪽은 기저 함수, 아래쪽은 커널 $k(x,x')$. 다항식(왼쪽)·가우시안(가운데)·시그모이드(오른쪽) 기저 함수.</div>
</div>

::: tip 실습 · 커널 릿지 회귀 (듀얼 표현)
가우시안 커널의 그램 행렬 $\mathbf{K}$로 $\mathbf{a}=(\mathbf{K}+\lambda\mathbf{I})^{-1}\mathsf{t}$를 풀고, 새 입력을 $y(\mathbf{x})=\mathbf{k}(\mathbf{x})^{\top}\mathbf{a}$로 예측해 $\sin(2\pi x)$를 근사합니다. 특징 벡터를 전혀 명시하지 않고 커널만으로 회귀가 이루어집니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)
N = 20; x = np.linspace(0, 1, N); t = np.sin(2*np.pi*x) + 0.1*rng.standard_normal(N)
def gk(a, b, s=0.1):                                    # 가우시안 커널
    return np.exp(-(a[:,None]-b[None,:])**2/(2*s**2))
lam = 1e-2
K = gk(x, x)
a = np.linalg.solve(K + lam*np.eye(N), t)              # a = (K+λI)⁻¹ t
xt = np.linspace(0, 1, 6); yp = gk(xt, x) @ a          # y(x) = k(x)ᵀ a
for xi, yi in zip(xt, yp):
    print(f"x={xi:.2f}: y_pred={yi:+.3f}   sin(2πx)={np.sin(2*np.pi*xi):+.3f}")
```

</PyRunner>

## 5.2 커널의 구성

- 유효한 커널을 만드는 한 방법은 특징 사상 $\boldsymbol{\phi}(\cdot)$을 정하고 대응하는 커널 $k(x,x')=\sum_i\phi_i(x)\phi_i(x')$을 찾는 것이다. 다른 방법은 커널을 직접 정의하되, 특징 공간의 내적으로 표현될 수 있음을 보장하는 규칙을 따르는 것이다.

::: info 커널 규칙
유효한 커널 $k_1$, $k_2$가 주어졌을 때 아래 방식으로 만든 커널 역시 유효하다.

$$
\begin{aligned}
&k(\mathbf{x},\mathbf{x}')=c\,k_1(\mathbf{x},\mathbf{x}') &\quad
&k(\mathbf{x},\mathbf{x}')=f(\mathbf{x})k_1(\mathbf{x},\mathbf{x}')f(\mathbf{x}') \\
&k(\mathbf{x},\mathbf{x}')=q(k_1(\mathbf{x},\mathbf{x}')) &\quad
&k(\mathbf{x},\mathbf{x}')=\exp(k_1(\mathbf{x},\mathbf{x}')) \\
&k(\mathbf{x},\mathbf{x}')=k_1(\mathbf{x},\mathbf{x}')+k_2(\mathbf{x},\mathbf{x}') &\quad
&k(\mathbf{x},\mathbf{x}')=k_1(\mathbf{x},\mathbf{x}')\,k_2(\mathbf{x},\mathbf{x}') \\
&k(\mathbf{x},\mathbf{x}')=k_3(\boldsymbol{\phi}(\mathbf{x}),\boldsymbol{\phi}(\mathbf{x}')) &\quad
&k(\mathbf{x},\mathbf{x}')=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}'
\end{aligned}
$$

$c>0$은 상수, $f(\cdot)$은 임의의 함수, $q(\cdot)$은 음이 아닌 계수의 다항식, $\mathbf{A}$는 대칭 양의 준정부호 행렬이다.
:::

- 널리 쓰이는 **가우시안 커널** $k(\mathbf{x},\mathbf{x}')=\exp(-\|\mathbf{x}-\mathbf{x}'\|^2/2\sigma^2)$은 위 규칙으로 유효성을 확인할 수 있다. 생성 모델로 정의하는 **피셔 커널**<span class="gloss">Fisher kernel</span>은 **피셔 점수** $\mathbf{g}(\boldsymbol{\theta},\mathbf{x})=\nabla_{\boldsymbol{\theta}}\ln p(\mathbf{x}\mid\boldsymbol{\theta})$와 **피셔 정보 행렬** $\mathbf{F}=\mathbb{E}_{\mathbf{x}}[\mathbf{g}\mathbf{g}^{\top}]$로 $k(\mathbf{x},\mathbf{x}')=\mathbf{g}(\boldsymbol{\theta},\mathbf{x})^{\top}\mathbf{F}^{-1}\mathbf{g}(\boldsymbol{\theta},\mathbf{x}')$이다.

## 5.3 가우시안 과정

### 5.3.1 선형 회귀 재검토

- $M$개의 기저 함수 선형 결합 $y(\mathbf{x})=\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x})$에 가우시안 사전 분포 $p(\mathbf{w})=\mathcal{N}(\mathbf{w}\mid\mathbf{0},\alpha^{-1}\mathbf{I})$를 두자. 훈련 포인트에서의 함숫값 벡터 $\mathsf{y}=\boldsymbol{\Phi}\mathbf{w}$는 가우시안의 선형 결합이므로 가우시안이며, 평균과 공분산은

$$
\mathbb{E}[\mathsf{y}]=\mathbf{0},\qquad
\operatorname{cov}[\mathsf{y}]=\frac{1}{\alpha}\boldsymbol{\Phi}\boldsymbol{\Phi}^{\top}=\mathbf{K},\quad
K_{nm}=\frac{1}{\alpha}\boldsymbol{\phi}(\mathbf{x}_n)^{\top}\boldsymbol{\phi}(\mathbf{x}_m)
$$

- 이 모델이 **가우시안 과정**<span class="gloss">Gaussian process</span>의 한 예다. 가우시안 과정은 임의의 유한 포인트 집합에서 함숫값들이 결합 가우시안이 되도록 하는 $y(\mathbf{x})$에 대한 분포이며, 평균과 공분산(커널)만으로 완전히 정의된다. 보통 평균은 $0$으로 두고 커널로 공분산을 정한다.

### 5.3.2 가우시안 과정을 통한 회귀

- 표적값에 노이즈 $t_n=y_n+\epsilon_n$, $p(t_n\mid y_n)=\mathcal{N}(t_n\mid y_n,\beta^{-1})$을 두면, 주변 분포 $p(\mathsf{y})=\mathcal{N}(\mathsf{y}\mid\mathbf{0},\mathbf{K})$와 결합해

$$
p(\mathsf{t})=\mathcal{N}(\mathsf{t}\mid\mathbf{0},\mathbf{C}),\qquad
C(\mathbf{x}_n,\mathbf{x}_m)=k(\mathbf{x}_n,\mathbf{x}_m)+\beta^{-1}\delta_{nm}
$$

  를 얻는다. 널리 쓰이는 공분산 함수는 지수 이차항에 상수·선형항을 더한 $k(\mathbf{x}_n,\mathbf{x}_m)=\theta_0\exp\{-\frac{\theta_1}{2}\|\mathbf{x}_n-\mathbf{x}_m\|^2\}+\theta_2+\theta_3\mathbf{x}_n^{\top}\mathbf{x}_m$이다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.6.png" style="width:20rem;" />
<div class="cap">그림 6.6 · 가우시안 과정에서 추출한 표본. 청색은 함수에 대한 사전 분포, 적색 원은 $y_n$, 녹색 원은 노이즈를 더한 $t_n$.</div>
</div>

- 새 입력 $\mathbf{x}_{N+1}$에 대한 예측은 결합 분포 $p(\mathsf{t}_{N+1})=\mathcal{N}(\mathsf{t}_{N+1}\mid\mathbf{0},\mathbf{C}_{N+1})$의 공분산을 분할해 얻는 조건부 가우시안이다.

$$
\mathbf{C}_{N+1}=\begin{pmatrix}\mathbf{C}_N & \mathbf{k}\\ \mathbf{k}^{\top} & c\end{pmatrix},\qquad
m(\mathbf{x}_{N+1})=\mathbf{k}^{\top}\mathbf{C}_N^{-1}\mathsf{t} \tag{6.66}
$$

$$
\sigma^2(\mathbf{x}_{N+1})=c-\mathbf{k}^{\top}\mathbf{C}_N^{-1}\mathbf{k} \tag{6.67}
$$

  예측 분포의 평균과 분산 모두 시험 입력 $\mathbf{x}_{N+1}$에 종속한다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.7.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.8.png" />
</div>
<div class="cap">그림 6.7·6.8 · (왼쪽) 훈련·시험 포인트 하나씩에 대한 결합 분포 $p(t_1,t_2)$와 조건부 $p(t_2\mid t_1)$. (오른쪽) 사인 곡선 데이터에 대한 가우시안 과정 회귀. 적색 선은 예측 평균, 음영은 $\pm2\sigma$ 구간이며 데이터가 없는 오른쪽에서 불확실성이 커진다.</div>
</div>

::: tip 실습 · 가우시안 과정 회귀 (예측 평균·분산)
공분산 $\mathbf{C}_N=\mathbf{K}+\beta^{-1}\mathbf{I}$를 만들고, 시험 입력마다 (6.66)의 평균 $\mathbf{k}^{\top}\mathbf{C}_N^{-1}\mathsf{t}$와 (6.67)의 분산 $c-\mathbf{k}^{\top}\mathbf{C}_N^{-1}\mathbf{k}$를 계산합니다. 데이터 범위 $[-1,1]$ 밖에서 불확실성이 급증하는 것을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)
Xtr = np.sort(rng.uniform(-1, 1, 8)); ttr = np.sin(3*Xtr) + 0.05*rng.standard_normal(8)
th = (1.0, 10.0, 0.0, 0.0)                              # θ0 exp(-θ1/2‖·‖²)+θ2+θ3 x x'
def kern(A, B):
    d = (A[:,None]-B[None,:])**2
    return th[0]*np.exp(-th[1]/2*d) + th[2] + th[3]*(A[:,None]*B[None,:])
beta = 100.0
C = kern(Xtr, Xtr) + np.eye(len(Xtr))/beta             # C = K + β⁻¹ I
Cinv = np.linalg.inv(C)
for xs in [-0.5, 0.0, 0.9, 1.8]:
    xs = np.array([xs]); k = kern(xs, Xtr)[0]; c = kern(xs, xs)[0,0] + 1/beta
    m = k @ Cinv @ ttr                                  # (6.66) 평균
    v = c - k @ Cinv @ k                                # (6.67) 분산
    print(f"x*={xs[0]:+.2f}: 평균={m:+.3f}  표준편차={np.sqrt(max(v,0)):.3f}")
```

</PyRunner>

### 5.3.3 초매개변수 학습

- 공분산 함수의 매개변수 $\boldsymbol{\theta}$(상관 길이 척도, 노이즈 정밀도 등)는 로그 가능도를 최대화해 추정한다.

$$
\ln p(\mathsf{t}\mid\boldsymbol{\theta})=-\frac{1}{2}\ln|\mathbf{C}_N|-\frac{1}{2}\mathsf{t}^{\top}\mathbf{C}_N^{-1}\mathsf{t}-\frac{N}{2}\ln(2\pi)
$$

  기울기는 $\dfrac{\partial}{\partial\theta_i}\ln p=-\dfrac{1}{2}\operatorname{Tr}\!\bigl(\mathbf{C}_N^{-1}\tfrac{\partial\mathbf{C}_N}{\partial\theta_i}\bigr)+\dfrac{1}{2}\mathsf{t}^{\top}\mathbf{C}_N^{-1}\tfrac{\partial\mathbf{C}_N}{\partial\theta_i}\mathbf{C}_N^{-1}\mathsf{t}$이다. $\ln p(\mathsf{t}\mid\boldsymbol{\theta})$는 일반적으로 비볼록이라 여러 극댓값을 가질 수 있다.

### 5.3.4 가우시안 과정을 통한 분류

- 가우시안 과정은 실수축 전체의 값을 내므로, 출력에 로지스틱 시그모이드를 씌워 $(0,1)$ 확률로 만든다. 2클래스 문제에서 함수 $a(\mathbf{x})$에 가우시안 과정을 두고 $y=\sigma(a)$로 변환하면, 표적값 분포는 베르누이 $p(t\mid a)=\sigma(a)^t(1-\sigma(a))^{1-t}$이다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.11a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.11b.png" />
</div>
<div class="cap">그림 6.11 · (왼쪽) $a(\mathbf{x})$에 대한 가우시안 과정 표본. (오른쪽) 로지스틱 시그모이드로 변환한 결과.</div>
</div>

- 예측 분포 $p(t_{N+1}=1\mid\mathsf{t}_N)=\int\sigma(a_{N+1})\,p(a_{N+1}\mid\mathsf{t}_N)\,\mathrm{d}a_{N+1}$은 해석적으로 풀 수 없어, 변분 추론·기대 전파·라플라스 근사 중 하나로 근사한다. 분류에서는 모든 훈련값이 정확하다고 보므로 노이즈항 대신 수치 안정용 $\nu\delta_{nm}$을 더한 $C(\mathbf{x}_n,\mathbf{x}_m)=k(\mathbf{x}_n,\mathbf{x}_m)+\nu\delta_{nm}$을 쓴다.

### 5.3.5 라플라스 근사법

- 사후 분포 $p(\mathbf{a}_N\mid\mathsf{t}_N)$의 로그 $\boldsymbol{\Psi}(\mathbf{a}_N)=\ln p(\mathbf{a}_N)+\ln p(\mathsf{t}_N\mid\mathbf{a}_N)$의 기울기와 헤시안은

$$
\nabla\boldsymbol{\Psi}=\mathsf{t}_N-\boldsymbol{\sigma}_N-\mathbf{C}_N^{-1}\mathbf{a}_N,\qquad
\nabla\nabla\boldsymbol{\Psi}=-\mathbf{W}_N-\mathbf{C}_N^{-1}
$$

  $\boldsymbol{\sigma}_N$은 $\sigma(a_n)$을, $\mathbf{W}_N$은 $\sigma(a_n)(1-\sigma(a_n))$을 대각 원소로 갖는다. $\boldsymbol{\sigma}_N$이 $\mathbf{a}_N$에 비선형 종속이라 기울기를 $0$으로 두는 대신 뉴턴–라프슨(반복 재가중 최소 제곱)으로 최빈값을 찾는다.

$$
\mathbf{a}_N^{\mathrm{new}}=\mathbf{C}_N(\mathbf{I}+\mathbf{W}_N\mathbf{C}_N)^{-1}(\mathsf{t}_N-\boldsymbol{\sigma}_N+\mathbf{W}_N\mathbf{a}_N)
$$

- 최빈값 $\mathbf{a}_N^{\star}$에서 헤시안 $\mathbf{H}=\mathbf{W}_N+\mathbf{C}_N^{-1}$으로 가우시안 근사 $q(\mathbf{a}_N)=\mathcal{N}(\mathbf{a}_N\mid\mathbf{a}_N^{\star},\mathbf{H}^{-1})$을 얻고, 시험 입력에 대한 잠재값의 평균·분산은

$$
\mathbb{E}[a_{N+1}\mid\mathsf{t}_N]=\mathbf{k}^{\top}(\mathsf{t}_N-\boldsymbol{\sigma}_N),\qquad
\operatorname{var}[a_{N+1}\mid\mathsf{t}_N]=c-\mathbf{k}^{\top}(\mathbf{W}_N^{-1}+\mathbf{C}_N)^{-1}\mathbf{k}
$$

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.12a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure6.12b.png" />
</div>
<div class="cap">그림 6.12 · 가우시안 과정 분류. (왼쪽) 데이터와 최적 결정 경계(녹색), 가우시안 과정 결정 경계(흑색). (오른쪽) 예측 사후 확률.</div>
</div>

::: tip 실습 · 가우시안 과정 분류 (라플라스/뉴턴)
잠재 함수의 사후 최빈값을 뉴턴 갱신 $\mathbf{a}^{\mathrm{new}}=\mathbf{C}_N(\mathbf{I}+\mathbf{W}\mathbf{C}_N)^{-1}(\mathsf{t}-\boldsymbol{\sigma}+\mathbf{W}\mathbf{a})$로 구한 뒤, 시험 입력의 $\mathbb{E}[a_*]$·$\operatorname{var}[a_*]$로 클래스 확률을 근사합니다.
:::

<PyRunner>

```python
import numpy as np
def sig(z): return 1/(1+np.exp(-z))
def rbf(A, B, s=1.0): return np.exp(-(A[:,None]-B[None,:])**2/(2*s**2))
rng = np.random.default_rng(2)
Xtr = np.sort(rng.uniform(-3, 3, 20))
ttr = (rng.uniform(size=20) < sig(1.5*Xtr)).astype(float)
nu = 1e-2; CN = rbf(Xtr, Xtr) + nu*np.eye(len(Xtr)); a = np.zeros(len(Xtr))
for it in range(20):                                   # 뉴턴–라프슨 최빈값 탐색
    s = sig(a); W = s*(1-s)
    a_new = CN @ np.linalg.solve(np.eye(len(a)) + CN*W[None,:], ttr - s + W*a)
    step = np.linalg.norm(a_new - a); a = a_new
    if step < 1e-8: break
print(f"Newton 수렴: {it+1}회,  |Δa|={step:.1e}")
s = sig(a); W = s*(1-s)
for xs in [-2.0, 0.0, 2.0]:
    xs = np.array([xs]); k = rbf(xs, Xtr)[0]; c = 1.0 + nu
    Ea = k @ (ttr - s)                                  # E[a_*] = kᵀ(t-σ)
    va = c - k @ np.linalg.solve(np.diag(1/W) + CN, k)  # var[a_*]
    p = sig(Ea/np.sqrt(1 + np.pi*va/8))                 # 시그모이드-가우시안 근사
    print(f"x*={xs[0]:+.1f}: E[a]={Ea:+.3f}  var={va:.3f}  p(t=1)={p:.3f}")
```

</PyRunner>

## 5.4 최대 마진 분류기

- 커널 기법의 한계는 모든 데이터 쌍에 대해 커널을 계산해야 한다는 점이다. **희박한**<span class="gloss">sparse</span> 해를 갖는 방법은 데이터의 부분 집합에만 의존한다. 대표적인 **서포트 벡터 머신**<span class="gloss">support vector machine; SVM</span>은 **볼록 최적화**<span class="gloss">convex optimization</span> 문제를 풀어 지역 최적해가 곧 전역 최적해가 되며, 사후 확률이 아니라 결정을 출력한다.

- $y(\mathbf{x})=\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x})+b$로 정확히 분리되는 해가 여럿일 때, SVM은 **마진**<span class="gloss">margin</span>(결정 경계와 가장 가까운 점 사이의 거리)을 최대화하는 경계를 고른다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure7.1a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure7.1b.png" />
</div>
<div class="cap">그림 7.1 · 마진은 결정 경계와 가장 가까운 데이터 포인트 사이의 거리다. 마진을 최대화하면 오른쪽 경계를 얻으며, 경계를 결정하는 부분 집합이 서포트 벡터(원 표시)다.</div>
</div>

- 가장 가까운 점에 대해 $t_n(\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x}_n)+b)=1$로 정규화(정준 표현)하면 모든 점이 $t_n(\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x}_n)+b)\geqslant1$을 만족하고, 마진 최대화는 $\frac{1}{2}\|\mathbf{w}\|^2$ 최소화가 된다.

$$
\underset{\mathbf{w},b}{\arg\min}\ \frac{1}{2}\|\mathbf{w}\|^2\quad\text{s.t.}\quad t_n(\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x}_n)+b)\geqslant1 \tag{7.5}
$$

- 라그랑주 승수 $a_n\geqslant0$을 도입하고 $\mathbf{w}$, $b$를 소거하면 커널만 등장하는 **듀얼 표현**을 얻는다.

$$
\widetilde{L}(\mathbf{a})=\sum_{n=1}^N a_n-\frac{1}{2}\sum_{n=1}^N\sum_{m=1}^N a_n a_m t_n t_m k(\mathbf{x}_n,\mathbf{x}_m),\qquad
a_n\geqslant0,\ \sum_{n=1}^N a_n t_n=0
$$

  예측은 $y(\mathbf{x})=\sum_n a_n t_n k(\mathbf{x},\mathbf{x}_n)+b$이며, $a_n\neq0$인 점(서포트 벡터)만 기여한다. 편향은 서포트 벡터 집합 $\mathcal{S}$의 평균으로 안정적으로 구한다.

$$
b=\frac{1}{N_{\mathcal{S}}}\sum_{n\in\mathcal{S}}\Bigl(t_n-\sum_{m\in\mathcal{S}}a_m t_m k(\mathbf{x}_n,\mathbf{x}_m)\Bigr)
$$

### 5.4.1 클래스 분포 간의 중첩

- 클래스가 겹칠 때는 오분류를 허용하되 벌점을 주기 위해 **느슨한 변수**<span class="gloss">slack variable</span> $\xi_n\geqslant0$을 도입한다. 올바른 마진 안쪽이면 $\xi_n=0$, 아니면 $\xi_n=|t_n-y(\mathbf{x}_n)|$이며 제약은 $t_n y(\mathbf{x}_n)\geqslant1-\xi_n$이 된다. $\xi_n>1$을 금지하면 **강한 마진**<span class="gloss">hard margin</span>, 허용하면 **약한 마진**<span class="gloss">soft margin</span>이다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure7.3.png" style="width:20rem;" />
<div class="cap">그림 7.3 · 느슨한 변수를 적용한 SVM. 원으로 강조된 점이 서포트 벡터다.</div>
</div>

- 목표 함수는 $C\sum_n\xi_n+\frac{1}{2}\|\mathbf{w}\|^2$이며($C>0$은 벌점과 마진의 트레이드오프), 듀얼은 강한 마진과 동일하되 제약이 $0\leqslant a_n\leqslant C$로 바뀐다.

$$
C\sum_{n=1}^N\xi_n+\frac{1}{2}\|\mathbf{w}\|^2 \tag{7.21}
$$

### 5.4.2 로지스틱 회귀와의 관계

- 목표 함수를 $\sum_n E_{\mathrm{SV}}(y_n t_n)+\lambda\|\mathbf{w}\|^2$($\lambda=(2C)^{-1}$) 형태로 쓰면 $E_{\mathrm{SV}}$는 **힌지**<span class="gloss">hinge</span> 오류 $[1-y_n t_n]_+$이다. 정규화된 로지스틱 회귀의 오류는 $E_{\mathrm{LR}}(yt)=\ln(1+\exp(-yt))$로, 둘 다 오분류 오류의 연속 근사이며 형태가 유사하다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure7.5.png" style="width:22rem;" />
<div class="cap">그림 7.5 · 힌지 오류(청색), $1/\ln2$로 재척도한 로지스틱 오류(적색), 제곱 오류(녹색), 오분류 오류(흑색).</div>
</div>

::: tip 실습 · 힌지 · 로지스틱 · 0–1 오류 비교
$z=y\cdot t$에 대해 힌지 $[1-z]_+$, 재척도 로지스틱 $\ln(1+e^{-z})/\ln2$, 0–1 오류를 계산해 비교합니다. 두 연속 오류가 $z=1$ 근처에서 오분류 오류를 매끄럽게 근사함을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
z = np.array([-2, -1, 0, 0.5, 1, 2], dtype=float)      # z = y·t
hinge = np.maximum(0, 1-z)
logistic = np.log(1+np.exp(-z))/np.log(2)              # 1/ln2 재척도
zero_one = (z < 0).astype(float)
print("   z(=y·t)   hinge   logistic   0-1")
for i in range(len(z)):
    print(f"  {z[i]:+5.1f}   {hinge[i]:6.3f}   {logistic[i]:7.3f}   {zero_one[i]:3.0f}")
```

</PyRunner>

### 5.4.3 서포트 벡터 머신을 이용한 회귀

- 회귀에서 희박성을 얻기 위해 **$\epsilon$-둔감 오류 함수**<span class="gloss">ε-insensitive error</span>를 쓴다. $|y(\mathbf{x})-t|<\epsilon$이면 $0$, 아니면 $|y(\mathbf{x})-t|-\epsilon$이다. 두 느슨한 변수 $\xi_n$, $\widehat{\xi}_n$을 도입해

$$
t_n\leqslant y(\mathbf{x}_n)+\epsilon+\xi_n,\qquad t_n\geqslant y(\mathbf{x}_n)-\epsilon-\widehat{\xi}_n
$$

  제약하에 $C\sum_n(\xi_n+\widehat{\xi}_n)+\frac{1}{2}\|\mathbf{w}\|^2$을 최소화한다. 듀얼을 풀면 예측은 커널로 표현된다.

$$
y(\mathbf{x})=\sum_{n=1}^N(a_n-\widehat{a}_n)k(\mathbf{x},\mathbf{x}_n)+b,\qquad 0\leqslant a_n\leqslant C,\ 0\leqslant\widehat{a}_n\leqslant C
$$

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure7.7.png" style="width:20rem;" />
<div class="cap">그림 7.7 · 서포트 벡터 회귀. $\epsilon$-튜브 바깥의 점만 느슨한 변수로 벌점을 받는다.</div>
</div>

## 연습문제

::: info 문제 5.1
최소 제곱 선형 회귀의 듀얼 공식화에서, 해 $\mathbf{w}$가 특징 벡터 $\boldsymbol{\phi}(\mathbf{x}_n)$들의 선형 결합으로 표현됨을 보이고, 듀얼 표현으로 얻은 예측이 원래 매개변수 표현의 예측과 일치함을 증명하라.
:::

::: details 풀이
**선형 결합 표현** — 정규화된 오류 $J(\mathbf{w})=\frac{1}{2}\sum_n\{\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x}_n)-t_n\}^2+\frac{\lambda}{2}\mathbf{w}^{\top}\mathbf{w}$의 기울기를 $0$으로 두면

$$
\nabla_{\mathbf{w}}J=\sum_{n=1}^N\{\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x}_n)-t_n\}\boldsymbol{\phi}(\mathbf{x}_n)+\lambda\mathbf{w}=\mathbf{0}
$$

이를 $\mathbf{w}$에 대해 정리하면

$$
\mathbf{w}=-\frac{1}{\lambda}\sum_{n=1}^N\{\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x}_n)-t_n\}\boldsymbol{\phi}(\mathbf{x}_n)=\sum_{n=1}^N a_n\boldsymbol{\phi}(\mathbf{x}_n)=\boldsymbol{\Phi}^{\top}\mathbf{a}
$$

즉 계수 $a_n=-\frac{1}{\lambda}\{\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x}_n)-t_n\}$을 갖는 특징 벡터들의 선형 결합이다.

**예측 일치** — 원래 표현의 예측은 $y(\mathbf{x})=\mathbf{w}^{\top}\boldsymbol{\phi}(\mathbf{x})$이다. 위 결과를 대입하면

$$
y(\mathbf{x})=\mathbf{a}^{\top}\boldsymbol{\Phi}\boldsymbol{\phi}(\mathbf{x})=\sum_{n=1}^N a_n\,\boldsymbol{\phi}(\mathbf{x}_n)^{\top}\boldsymbol{\phi}(\mathbf{x})=\sum_{n=1}^N a_n\,k(\mathbf{x}_n,\mathbf{x})=\mathbf{k}(\mathbf{x})^{\top}\mathbf{a}
$$

$J(\mathbf{a})$를 $\mathbf{a}$에 대해 최소화하면 $\mathbf{a}=(\mathbf{K}+\lambda\mathbf{I}_N)^{-1}\mathsf{t}$이므로 $y(\mathbf{x})=\mathbf{k}(\mathbf{x})^{\top}(\mathbf{K}+\lambda\mathbf{I}_N)^{-1}\mathsf{t}$. 이는 $\mathbf{w}$를 통한 예측과 정확히 같다. 즉 듀얼 표현은 커널 $k(\mathbf{x},\mathbf{x}')=\boldsymbol{\phi}(\mathbf{x})^{\top}\boldsymbol{\phi}(\mathbf{x}')$만으로 동일한 예측을 재현한다. $\blacksquare$
:::

::: info 문제 5.2
고정 집합 $D$의 모든 부분집합 $A$에 대해 $k(A_1,A_2)=2^{|A_1\cap A_2|}$로 정의된 함수가, $\phi_U(A)=1\ (U\subseteq A)$, $0\ (\text{그 외})$로 인덱스되는 $2^{|D|}$차원 특징 공간의 내적임을 증명하라.
:::

::: details 풀이
특징 사상 $\boldsymbol{\phi}(A)$는 $D$의 모든 부분집합 $U$로 인덱스되며(따라서 차원은 $2^{|D|}$), 성분은 $\phi_U(A)=\mathbb{1}[U\subseteq A]$이다. 두 부분집합 $A_1$, $A_2$의 특징 벡터 내적은

$$
\boldsymbol{\phi}(A_1)^{\top}\boldsymbol{\phi}(A_2)=\sum_{U\subseteq D}\phi_U(A_1)\phi_U(A_2)=\sum_{U\subseteq D}\mathbb{1}[U\subseteq A_1]\,\mathbb{1}[U\subseteq A_2]
$$

곱 $\mathbb{1}[U\subseteq A_1]\,\mathbb{1}[U\subseteq A_2]$은 $U\subseteq A_1$이면서 $U\subseteq A_2$일 때, 즉 $U\subseteq A_1\cap A_2$일 때만 $1$이다. 따라서 합은 $A_1\cap A_2$의 부분집합의 개수와 같다.

$$
\boldsymbol{\phi}(A_1)^{\top}\boldsymbol{\phi}(A_2)=\bigl|\{U:U\subseteq A_1\cap A_2\}\bigr|=2^{|A_1\cap A_2|}=k(A_1,A_2)
$$

크기가 $m$인 집합의 부분집합은 $2^m$개이므로 마지막 등식이 성립한다. 이렇게 $k$가 특징 공간의 내적으로 표현되었으므로 유효한 커널이다. $\blacksquare$
:::
