# 10 · 연속 잠재 변수

> 많은 데이터 집합은 원 공간의 차원보다 낮은 차원의 매니폴드에 가깝게 놓인다. 잠재 변수를 연속적으로 표현하는 모델로 데이터의 내재적 정보를 추출할 수 있다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/photos/sec10.png" style="max-width:34rem;" />
</div>

## 10.1 주성분 분석

- 큰 이미지에 작은 숫자를 임의 위치·각도로 삽입하면 자유도가 $3$(수직·수평·회전)이라, 데이터의 **내재적 차원**<span class="gloss">intrinsic dimensionality</span>은 $3$이다. **주성분 분석**<span class="gloss">principal component analysis; PCA</span>은 가장 단순한 연속 잠재 변수 모델로, 차원 감소·압축·특징 추출·시각화에 쓰인다. PCA는 두 방식으로 정의된다: (1) 분산이 최대가 되는 **주 부분공간**<span class="gloss">principal subspace</span>으로의 직교 투영, (2) 평균 투영 제곱 오류의 최소화. 두 정의는 같은 결과를 준다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.1.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.2.png" />
</div>
<div class="cap">

그림 10.1·10.2 · (왼쪽) 숫자를 임의 위치·각도로 삽입해 만든 인공 데이터. (오른쪽) 주 부분공간(자주색)은 투영(녹색)의 분산을 최대화하고 투영 오류(청색)를 최소화한다.

</div>
</div>

### 10.1.1 최대 분산 공식화

- 단위 벡터 $\mathbf{u}_1$에 투영한 데이터 $\mathbf{u}_1^{\top}\mathbf{x}_n$의 분산은 $\mathbf{u}_1^{\top}\mathbf{S}\mathbf{u}_1$이다($\mathbf{S}$는 데이터 공분산). 제약 $\mathbf{u}_1^{\top}\mathbf{u}_1=1$ 하에 라그랑주 승수로 최대화하면

$$
\mathbf{S}\mathbf{u}_1=\lambda_1\mathbf{u}_1
$$

  즉 $\mathbf{u}_1$은 $\mathbf{S}$의 고유벡터다. 분산 $\mathbf{u}_1^{\top}\mathbf{S}\mathbf{u}_1=\lambda_1$이 최대가 되려면 가장 큰 고윳값의 고유벡터를 골라야 하며, 이것이 제1주성분이다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.9.png" style="max-width:32rem;" />
<div class="cap">

그림 10.3 · 확률적 PCA의 생성적 관점. 잠재 변수 $\widehat{z}\sim p(z)$에서 평균 $\mathbf{w}\widehat{z}+\boldsymbol{\mu}$·공분산 $\sigma^2\mathbf{I}$의 가우시안으로 $\mathbf{x}$를 생성한다.

</div>
</div>

::: tip 실습 · PCA (최대 분산 = 최대 고유벡터)
데이터 공분산 $\mathbf{S}$의 고유분해로 제1주성분을 구하고, 투영 분산 $\mathbf{u}_1^{\top}\mathbf{S}\mathbf{u}_1$이 최대 고윳값 $\lambda_1$과 같음을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)
A = np.array([[2.0, 0.0], [1.3, 0.7]])
X = (rng.standard_normal((1000, 2)) @ A.T) + [1.0, -2.0]
Xc = X - X.mean(0); S = Xc.T @ Xc / len(X)              # 공분산
w, V = np.linalg.eigh(S); idx = np.argsort(w)[::-1]; w = w[idx]; V = V[:, idx]
u1 = V[:, 0]                                            # 제1주성분
print("고윳값:", np.round(w, 4).tolist())
print("제1주성분 u1 =", np.round(u1, 3).tolist())
print(f"투영 분산 u1ᵀSu1 = {u1@S@u1:.4f}  (= λ1 = {w[0]:.4f})")
print(f"분산 설명 비율 = {w[0]/w.sum():.3f}")
```

</PyRunner>

### 10.1.2 최소 오류 공식화

- 정규직교 기저 $\{\mathbf{u}_i\}$($\mathbf{u}_i^{\top}\mathbf{u}_j=\delta_{ij}$)로 $\mathbf{x}_n$을 표현하고, 첫 $M$개 기저로 근사할 때의 평균 제곱 오류는

$$
J=\frac{1}{N}\sum_{n=1}^N\|\mathbf{x}_n-\widetilde{\mathbf{x}}_n\|^2=\sum_{i=M+1}^D\mathbf{u}_i^{\top}\mathbf{S}\mathbf{u}_i
$$

  이를 정규직교 제약 하에 최소화하면 다시 $\mathbf{S}\mathbf{u}_i=\lambda_i\mathbf{u}_i$를 얻는다. 즉 버려지는 방향들이 가장 작은 고윳값에 대응하도록 하면 오류가 최소가 되어, 최대 분산 공식화와 같은 결과를 준다.

## 10.2 확률적 주성분 분석

- **확률적 주성분 분석**<span class="gloss">probabilistic PCA</span>은 PCA를 선형 가우시안 잠재 변수 모델의 최대 가능도 해로 표현한다. 잠재 변수 사전 분포와 조건부 분포를 두면

$$
p(\mathbf{z})=\mathcal{N}(\mathbf{z}\mid\mathbf{0},\mathbf{I}),\qquad
p(\mathbf{x}\mid\mathbf{z})=\mathcal{N}(\mathbf{x}\mid\mathbf{W}\mathbf{z}+\boldsymbol{\mu},\sigma^2\mathbf{I})
$$

  이고 $\mathbf{x}=\mathbf{W}\mathbf{z}+\boldsymbol{\mu}+\boldsymbol{\epsilon}$($\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\sigma^2\mathbf{I})$)이다. 잠재→데이터 사상이 기반인 점이 일반 PCA와 다르다. 주변 분포와 사후 분포는

$$
p(\mathbf{x})=\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu},\mathbf{C}),\quad \mathbf{C}=\mathbf{W}\mathbf{W}^{\top}+\sigma^2\mathbf{I},\qquad
p(\mathbf{z}\mid\mathbf{x})=\mathcal{N}(\mathbf{z}\mid\mathbf{M}^{-1}\mathbf{W}^{\top}(\mathbf{x}-\boldsymbol{\mu}),\sigma^2\mathbf{M}^{-1})
$$

  이며 $\mathbf{M}=\mathbf{W}^{\top}\mathbf{W}+\sigma^2\mathbf{I}$이다.

### 10.2.1 최대 가능도 주성분 분석

- $\boldsymbol{\mu}=\overline{\mathbf{x}}$이고, $\mathbf{W}$·$\sigma^2$의 최대 가능도 해는 닫힌 형태로 구해진다.

$$
\mathbf{W}_{\mathrm{ML}}=\mathbf{U}_M(\mathbf{L}_M-\sigma^2\mathbf{I})^{1/2}\mathbf{R},\qquad
\sigma_{\mathrm{ML}}^2=\frac{1}{D-M}\sum_{i=M+1}^D\lambda_i
$$

  $\mathbf{U}_M$은 $\mathbf{S}$의 상위 $M$개 고유벡터, $\mathbf{L}_M$은 그 고윳값 대각 행렬, $\mathbf{R}$은 임의의 직교 행렬(잠재 공간 회전)이다. $\sigma_{\mathrm{ML}}^2$은 버려진 고윳값들의 평균(잃은 분산)이다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.10.png" style="width:18rem;" />
<div class="cap">

그림 10.4 · 확률적 PCA의 방향성 그래프. 각 관측 $\mathbf{x}_n$이 잠재 변수 $\mathbf{z}_n$과 연결된다.

</div>
</div>

::: tip 실습 · 확률적 PCA 최대가능도
공분산 $\mathbf{S}$의 고유분해로 $\mathbf{W}_{\mathrm{ML}}$·$\sigma_{\mathrm{ML}}^2$을 구하고, 복원한 $\mathbf{C}=\mathbf{W}\mathbf{W}^{\top}+\sigma^2\mathbf{I}$가 데이터 공분산 $\mathbf{S}$를 잘 근사함을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)
D, M, N = 5, 2, 2000
Wtrue = rng.standard_normal((D, M)); Z = rng.standard_normal((N, M))
X = Z @ Wtrue.T + 0.3*rng.standard_normal((N, D)) + rng.standard_normal(D)
Xc = X - X.mean(0); S = Xc.T @ Xc / N
lam, U = np.linalg.eigh(S); idx = np.argsort(lam)[::-1]; lam = lam[idx]; U = U[:, idx]
sig2 = lam[M:].mean()                                   # σ²_ML = 버린 고윳값 평균
WML = U[:, :M] @ np.diag(np.sqrt(np.maximum(lam[:M]-sig2, 0)))
C = WML @ WML.T + sig2*np.eye(D)                        # 복원 공분산
print(f"σ²_ML = {sig2:.4f}  (버린 고윳값 평균)")
print(f"‖C - S‖_max = {np.abs(C-S).max():.4f}  (주변 공분산 복원 오차)")
print("상위 M개 고윳값:", np.round(lam[:M], 3).tolist())
```

</PyRunner>

### 10.2.2 주성분 분석에서의 EM 알고리즘

- 완전 데이터 로그 가능도의 기댓값을 최대화하는 EM으로도 확률적 PCA를 학습한다. E 단계에서 사후 통계량을, M 단계에서 매개변수를 갱신한다.

$$
\mathbb{E}[\mathbf{z}_n]=\mathbf{M}^{-1}\mathbf{W}^{\top}(\mathbf{x}_n-\overline{\mathbf{x}}),\qquad
\mathbb{E}[\mathbf{z}_n\mathbf{z}_n^{\top}]=\sigma^2\mathbf{M}^{-1}+\mathbb{E}[\mathbf{z}_n]\mathbb{E}[\mathbf{z}_n]^{\top}
$$

$$
\mathbf{W}_{\mathrm{new}}=\Bigl[\sum_n(\mathbf{x}_n-\overline{\mathbf{x}})\mathbb{E}[\mathbf{z}_n]^{\top}\Bigr]\Bigl[\sum_n\mathbb{E}[\mathbf{z}_n\mathbf{z}_n^{\top}]\Bigr]^{-1}
$$

  고윳값·고유벡터를 직접 구하지 않아 고차원에서 효율적이고, 누락된 값도 다룰 수 있다. $\sigma^2\to0$이면 표준 PCA가 된다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.12a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.12b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.12c.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.12d.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.12e.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.12f.png" />
</div>
<div class="cap">

그림 10.5 · PCA를 위한 EM. (a) 데이터와 실제 주성분. (b) 초기 부분공간. (c)~(f) M·E 단계를 번갈아 갱신하며 수렴한다.

</div>
</div>

::: tip 실습 · PCA를 위한 EM
E 단계($\mathbb{E}[\mathbf{z}_n]$, $\mathbb{E}[\mathbf{z}_n\mathbf{z}_n^{\top}]$)와 M 단계($\mathbf{W}$, $\sigma^2$)를 반복해 찾은 부분공간이, 고유분해로 얻은 상위 $M$ 주성분 공간과 일치함(주각 코사인 $\approx1$)을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)
D, M, N = 5, 2, 2000
Wtrue = rng.standard_normal((D, M)); Zt = rng.standard_normal((N, M))
X = Zt @ Wtrue.T + 0.3*rng.standard_normal((N, D)) + rng.standard_normal(D)
mu = X.mean(0); Xc = X - mu; S = Xc.T @ Xc / N
lam, U = np.linalg.eigh(S); U = U[:, np.argsort(lam)[::-1]]
W = rng.standard_normal((D, M)); sig2 = 1.0
for it in range(100):                                   # EM 반복
    Minv = np.linalg.inv(W.T@W + sig2*np.eye(M))
    Ez = Xc @ W @ Minv.T                                # E[z_n]
    Ezz = N*sig2*Minv + Ez.T@Ez                         # Σ E[z zᵀ]
    W = (Xc.T@Ez) @ np.linalg.inv(Ezz)                  # M 단계
    sig2 = (np.sum(Xc**2) - 2*np.sum((Ez@W.T)*Xc) + np.trace(Ezz@(W.T@W)))/(N*D)
Qem, _ = np.linalg.qr(W)                                # EM 부분공간
cos = np.linalg.svd(Qem.T @ U[:, :M], compute_uv=False) # 주각 코사인
print(f"σ² 수렴값 = {sig2:.4f}")
print("EM vs PCA 부분공간 주각 코사인:", np.round(cos, 4).tolist(), "(1이면 일치)")
```

</PyRunner>

### 10.2.3 베이지안 주성분 분석

- 주 부분공간 차원 $M$을 데이터로부터 정하려면 베이지안 접근이 필요하다. $\mathbf{W}$의 각 열에 정밀도 $\alpha_i$로 조절되는 독립 가우시안 사전 분포를 두고(**증거 근사**<span class="gloss">evidence approximation</span>), $\mathbf{W}$를 주변화한 가능도를 최대화해 $\alpha_i$를 반복 추정한다.

$$
\alpha_i^{\mathrm{new}}=\frac{D}{\mathbf{w}_i^{\top}\mathbf{w}_i}
$$

  불필요한 방향은 $\alpha_i\to\infty$가 되어 해당 열이 $0$으로 눌리므로, 주 부분공간 차원이 자동으로 결정된다(자동 적합성 결정).

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.13.png" style="width:18rem;" />
<div class="cap">

그림 10.6 · 베이지안 PCA의 그래프 모델. $\mathbf{W}$의 분포가 초매개변수 $\boldsymbol{\alpha}$로 조절된다.

</div>
</div>

## 10.3 커널 주성분 분석

- **커널 주성분 분석**<span class="gloss">kernel PCA</span>은 커널 트릭으로 PCA를 비선형으로 일반화한다. 특징 공간 $\boldsymbol{\phi}(\mathbf{x})$의 공분산 고유벡터 $\mathbf{v}_i=\sum_n a_{in}\boldsymbol{\phi}(\mathbf{x}_n)$를 대입하면, 특징 공간을 직접 다루지 않고 그램 행렬 $\mathbf{K}$의 고윳값 문제로 환원된다.

$$
\mathbf{K}\mathbf{a}_i=\lambda_i N\mathbf{a}_i,\qquad
y_i(\mathbf{x})=\boldsymbol{\phi}(\mathbf{x})^{\top}\mathbf{v}_i=\sum_{n=1}^N a_{in}k(\mathbf{x},\mathbf{x}_n)
$$

  정규화 조건은 $\lambda_i N\mathbf{a}_i^{\top}\mathbf{a}_i=1$이다. 특징 공간에서 선형인 투영이 원 데이터 공간에서는 비선형이라, 선형 PCA로는 못 잡는 구조를 포착한다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.16a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.16b.png" />
</div>
<div class="cap">

그림 10.7 · 커널 PCA. 원 데이터 공간(왼쪽)이 비선형 변환 $\boldsymbol{\phi}$로 특징 공간(오른쪽)에 사상되고, 특징 공간의 선형 투영(녹색)이 데이터 공간에서는 비선형이 된다.

</div>
</div>

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure12.17.png" style="max-width:32rem;" />
<div class="cap">

그림 10.8 · 가우시안 커널 PCA. 선들은 각 주성분 투영값이 상수인 윤곽선이다.

</div>
</div>

::: tip 실습 · 커널 PCA (비선형 분리)
동심원 데이터에 가우시안 커널 PCA를 적용합니다. 커널 행렬을 중심화하고 $\mathbf{K}\mathbf{a}=\lambda N\mathbf{a}$를 풀면, 제1 커널 주성분만으로 두 원이 완전히 분리됩니다(선형 PCA로는 불가능).
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(3)
def ring(r, n):
    t = rng.uniform(0, 2*np.pi, n); rr = r + 0.08*rng.standard_normal(n)
    return np.c_[rr*np.cos(t), rr*np.sin(t)]
X = np.vstack([ring(1.0, 150), ring(3.0, 150)]); y = np.r_[np.zeros(150), np.ones(150)]
N = len(X); one = np.ones((N, N))/N
d2 = ((X[:, None, :]-X[None, :, :])**2).sum(2)
K = np.exp(-d2/(2*1.5**2))                              # 가우시안 커널 (σ=1.5)
Kc = K - one@K - K@one + one@K@one                      # 커널 중심화
lam, al = np.linalg.eigh(Kc); idx = np.argsort(lam)[::-1]; al = al[:, idx]
proj = Kc @ al[:, 0]                                    # 제1 커널 주성분
m0, m1 = proj[y==0].mean(), proj[y==1].mean(); thr = (m0+m1)/2
acc = max(np.mean((proj>thr)==(y==1)), np.mean((proj<thr)==(y==1)))
print(f"제1 커널 주성분 — 내부 원 평균={m0:+.3f}, 외부 원 평균={m1:+.3f}")
print(f"제1 성분만으로 두 원 분리 정확도={acc:.1%} (선형 PCA로는 불가능)")
```

</PyRunner>

## 연습문제

::: info 문제 10.1
투영 분산을 $\mathbf{u}_{M+1}$에 대해 최대화하되 $\mathbf{u}_{M+1}$이 $\mathbf{u}_1,\ldots,\mathbf{u}_M$과 직교하고 단위 길이라는 제약을 라그랑주 승수로 부과하여, $\mathbf{u}_{M+1}$이 $\mathbf{S}$의 고유벡터임을 보이고, 고윳값 크기 역순 정렬 시 $\lambda_{M+1}$의 고유벡터를 고르면 분산이 최대가 됨을 증명하라.
:::

::: details 풀이
투영 분산 $\mathbf{u}_{M+1}^{\top}\mathbf{S}\mathbf{u}_{M+1}$에 단위 길이 제약과 직교 제약을 라그랑주 승수 $\lambda_{M+1}$, $\{\eta_j\}$로 부과한다.

$$
L=\mathbf{u}_{M+1}^{\top}\mathbf{S}\mathbf{u}_{M+1}+\lambda_{M+1}(1-\mathbf{u}_{M+1}^{\top}\mathbf{u}_{M+1})+\sum_{j=1}^M\eta_j\,\mathbf{u}_{M+1}^{\top}\mathbf{u}_j
$$

$\mathbf{u}_{M+1}$에 대해 미분해 $0$으로 두면

$$
2\mathbf{S}\mathbf{u}_{M+1}-2\lambda_{M+1}\mathbf{u}_{M+1}+\sum_{j=1}^M\eta_j\mathbf{u}_j=\mathbf{0}
$$

양변에 $\mathbf{u}_k^{\top}$($k\leqslant M$)를 곱하면, 정규직교성 $\mathbf{u}_k^{\top}\mathbf{u}_{M+1}=0$·$\mathbf{u}_k^{\top}\mathbf{u}_j=\delta_{kj}$와 $\mathbf{u}_k$가 이미 $\mathbf{S}$의 고유벡터($\mathbf{u}_k^{\top}\mathbf{S}\mathbf{u}_{M+1}=\lambda_k\mathbf{u}_k^{\top}\mathbf{u}_{M+1}=0$)라는 사실에서 $\eta_k=0$을 얻는다. 모든 $\eta_j=0$이므로

$$
\mathbf{S}\mathbf{u}_{M+1}=\lambda_{M+1}\mathbf{u}_{M+1}
$$

즉 $\mathbf{u}_{M+1}$은 $\mathbf{S}$의 고유벡터다. 이때 분산은 $\mathbf{u}_{M+1}^{\top}\mathbf{S}\mathbf{u}_{M+1}=\lambda_{M+1}$이므로, 이미 쓰인 상위 $M$개를 제외한 나머지 중 가장 큰 고윳값 $\lambda_{M+1}$의 고유벡터를 고르면 분산이 최대가 된다. $\blacksquare$
:::

::: info 문제 10.2
$\mathbf{x}\sim\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu},\boldsymbol{\Sigma})$이고 $\mathbf{y}=\mathbf{A}\mathbf{x}+\mathbf{b}$($\mathbf{A}$는 $M\times D$)일 때 $\mathbf{y}$가 가우시안임을 보이고 평균·공분산을 구하라. $M<D$, $M=D$, $M>D$ 각각을 논하라.
:::

::: details 풀이
**가우시안성** — 가우시안 확률 변수의 아핀 변환은 가우시안이다(선형 결합의 특성 함수가 다시 가우시안 형태). 평균과 공분산은 기댓값의 선형성으로

$$
\mathbb{E}[\mathbf{y}]=\mathbf{A}\mathbb{E}[\mathbf{x}]+\mathbf{b}=\mathbf{A}\boldsymbol{\mu}+\mathbf{b}
$$

$$
\operatorname{cov}[\mathbf{y}]=\mathbb{E}[(\mathbf{y}-\mathbb{E}[\mathbf{y}])(\mathbf{y}-\mathbb{E}[\mathbf{y}])^{\top}]=\mathbf{A}\,\mathbb{E}[(\mathbf{x}-\boldsymbol{\mu})(\mathbf{x}-\boldsymbol{\mu})^{\top}]\,\mathbf{A}^{\top}=\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top}
$$

따라서 $\mathbf{y}\sim\mathcal{N}(\mathbf{y}\mid\mathbf{A}\boldsymbol{\mu}+\mathbf{b},\ \mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top})$이다.

**경우별 논의** — 공분산 $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top}$은 $M\times M$이고, $\boldsymbol{\Sigma}\succ0$이면 계수는 $\operatorname{rank}(\mathbf{A})$로 정해진다.

- $M<D$: $\mathbf{A}$가 완전 행 계수($\operatorname{rank}=M$)이면 $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top}\succ0$인 비퇴화 $M$차원 가우시안이다(차원 감소·투영).

- $M=D$: $\mathbf{A}$가 가역이면 전단사 변환으로 비퇴화 $D$차원 가우시안이다.

- $M>D$: $\operatorname{rank}(\mathbf{A})\leqslant D<M$이라 $\mathbf{A}\boldsymbol{\Sigma}\mathbf{A}^{\top}$이 특이(계수 부족)해진다. $\mathbf{y}$는 $M$차원 공간 안의 $D$차원 부분공간에 갇힌 **퇴화 가우시안**<span class="gloss">degenerate Gaussian</span>이 되어 정규 밀도가 존재하지 않는다. $\blacksquare$
:::
