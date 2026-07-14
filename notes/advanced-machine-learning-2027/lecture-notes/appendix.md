# 부록 · 참고 자료

> 본문에서 반복적으로 쓰이는 확률 분포, 행렬 항등식, 변분법과 라그랑주 승수법을 정리했습니다. $\psi(a)\equiv\frac{\mathrm{d}}{\mathrm{d}a}\ln\Gamma(a)$는 **디감마**<span class="gloss">digamma</span> 함수입니다.

## A. 확률 분포

### A.1 베르누이 분포

- 단일 이진 변수 $x\in\{0,1\}$에 대한 분포로 $\mu\in[0,1]$이 $x=1$일 확률이다. 켤레 사전 분포는 베타 분포다.

$$
\operatorname{Bern}(x\mid\mu)=\mu^x(1-\mu)^{1-x},\quad
\mathbb{E}[x]=\mu,\quad \operatorname{var}[x]=\mu(1-\mu),\quad
\mathrm{H}[x]=-\mu\ln\mu-(1-\mu)\ln(1-\mu)
$$

### A.2 베타 분포

- 연속 변수 $\mu\in[0,1]$에 대한 분포로 $a>0$, $b>0$을 매개변수로 갖는다. 베르누이·이항 분포의 켤레 사전 분포이며 $a$, $b$는 $x=1$·$x=0$의 유효 관측 수로 해석된다.

$$
\operatorname{Beta}(\mu\mid a,b)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\mu^{a-1}(1-\mu)^{b-1},\quad
\mathbb{E}[\mu]=\frac{a}{a+b},\quad
\operatorname{var}[\mu]=\frac{ab}{(a+b)^2(a+b+1)},\quad
\operatorname{mode}[\mu]=\frac{a-1}{a+b-2}
$$

### A.3 이항 분포

- 베르누이 시행 $N$번 중 $x=1$을 $m$번 관측할 확률의 분포다. $N=1$이면 베르누이, $N$이 크면 가우시안에 가까워진다.

$$
\operatorname{Bin}(m\mid N,\mu)=\binom{N}{m}\mu^m(1-\mu)^{N-m},\quad
\mathbb{E}[m]=N\mu,\quad \operatorname{var}[m]=N\mu(1-\mu),\quad
\operatorname{mode}[m]=\lfloor(N+1)\mu\rfloor
$$

### A.4 디리클레 분포

- $\sum_k\mu_k=1$, $0\leqslant\mu_k\leqslant1$인 $K$차원 벡터에 대한 분포로 다항 분포의 켤레 사전 분포이며 베타 분포의 일반화다($\widehat{\alpha}=\sum_k\alpha_k$).

$$
\operatorname{Dir}(\boldsymbol{\mu}\mid\boldsymbol{\alpha})=C(\boldsymbol{\alpha})\prod_{k=1}^K\mu_k^{\alpha_k-1},\qquad
C(\boldsymbol{\alpha})=\frac{\Gamma(\widehat{\alpha})}{\Gamma(\alpha_1)\cdots\Gamma(\alpha_K)}
$$

$$
\mathbb{E}[\mu_k]=\frac{\alpha_k}{\widehat{\alpha}},\quad
\operatorname{var}[\mu_k]=\frac{\alpha_k(\widehat{\alpha}-\alpha_k)}{\widehat{\alpha}^2(\widehat{\alpha}+1)},\quad
\operatorname{cov}[\mu_j\mu_k]=-\frac{\alpha_j\alpha_k}{\widehat{\alpha}^2(\widehat{\alpha}+1)},\quad
\mathbb{E}[\ln\mu_k]=\psi(\alpha_k)-\psi(\widehat{\alpha})
$$

### A.5 감마 분포

- 양의 변수 $\tau>0$에 대한 분포로 단변량 가우시안 정밀도의 켤레 사전 분포다. $a=1$이면 지수 분포다.

$$
\operatorname{Gam}(\tau\mid a,b)=\frac{1}{\Gamma(a)}b^a\tau^{a-1}e^{-b\tau},\quad
\mathbb{E}[\tau]=\frac{a}{b},\quad \operatorname{var}[\tau]=\frac{a}{b^2},\quad
\operatorname{mode}[\tau]=\frac{a-1}{b}\ (a\geqslant1),\quad
\mathbb{E}[\ln\tau]=\psi(a)-\ln b
$$

### A.6 가우시안 분포

- 단변량은 평균 $\mu$·분산 $\sigma^2$, 다변량은 평균 $\boldsymbol{\mu}$·공분산 $\boldsymbol{\Sigma}$(대칭 양의 정부호)로 결정된다. $\boldsymbol{\mu}$의 켤레 사전 분포는 가우시안, 정밀도 행렬의 켤레 사전 분포는 위샤트 분포다.

$$
\mathcal{N}(x\mid\mu,\sigma^2)=\frac{1}{(2\pi\sigma^2)^{1/2}}\exp\Bigl\{-\frac{(x-\mu)^2}{2\sigma^2}\Bigr\},\qquad
\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu},\boldsymbol{\Sigma})=\frac{1}{(2\pi)^{D/2}|\boldsymbol{\Sigma}|^{1/2}}\exp\Bigl\{-\tfrac12(\mathbf{x}-\boldsymbol{\mu})^{\top}\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})\Bigr\}
$$

- 선형 가우시안 관계에서 주변·조건부 분포는 다음과 같다. $p(\mathbf{x})=\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu},\boldsymbol{\Lambda}^{-1})$, $p(\mathbf{y}\mid\mathbf{x})=\mathcal{N}(\mathbf{y}\mid\mathbf{A}\mathbf{x}+\mathbf{b},\mathbf{L}^{-1})$일 때

$$
p(\mathbf{y})=\mathcal{N}(\mathbf{y}\mid\mathbf{A}\boldsymbol{\mu}+\mathbf{b},\mathbf{L}^{-1}+\mathbf{A}\boldsymbol{\Lambda}^{-1}\mathbf{A}^{\top}),\quad
p(\mathbf{x}\mid\mathbf{y})=\mathcal{N}(\mathbf{x}\mid\boldsymbol{\Sigma}\{\mathbf{A}^{\top}\mathbf{L}(\mathbf{y}-\mathbf{b})+\boldsymbol{\Lambda}\boldsymbol{\mu}\},\boldsymbol{\Sigma}),\ \ \boldsymbol{\Sigma}=(\boldsymbol{\Lambda}+\mathbf{A}^{\top}\mathbf{L}\mathbf{A})^{-1}
$$

- 분할 $\mathbf{x}=(\mathbf{x}_a,\mathbf{x}_b)$, $\boldsymbol{\Lambda}=\boldsymbol{\Sigma}^{-1}$에서 조건부·주변 분포는

$$
p(\mathbf{x}_a\mid\mathbf{x}_b)=\mathcal{N}(\mathbf{x}_a\mid\boldsymbol{\mu}_a-\boldsymbol{\Lambda}_{aa}^{-1}\boldsymbol{\Lambda}_{ab}(\mathbf{x}_b-\boldsymbol{\mu}_b),\boldsymbol{\Lambda}_{aa}^{-1}),\qquad
p(\mathbf{x}_a)=\mathcal{N}(\mathbf{x}_a\mid\boldsymbol{\mu}_a,\boldsymbol{\Sigma}_{aa})
$$

### A.7 가우시안 감마 · 가우시안 위샤트 분포

- 평균·정밀도가 둘 다 미지인 가우시안의 켤레 사전 분포다. 단변량은 **정규 감마**<span class="gloss">normal-gamma</span>, 다변량은 **정규 위샤트**<span class="gloss">normal-Wishart</span>이다.

$$
p(\mu,\lambda\mid\mu_0,\beta,a,b)=\mathcal{N}(\mu\mid\mu_0,(\beta\lambda)^{-1})\operatorname{Gam}(\lambda\mid a,b),\qquad
p(\boldsymbol{\mu},\boldsymbol{\Lambda}\mid\boldsymbol{\mu}_0,\beta,\mathbf{W},\nu)=\mathcal{N}(\boldsymbol{\mu}\mid\boldsymbol{\mu}_0,(\beta\boldsymbol{\Lambda})^{-1})\mathcal{W}(\boldsymbol{\Lambda}\mid\mathbf{W},\nu)
$$

### A.8 다항 분포

- 원 핫 이산 변수의 일반화. $N$개 관측에서 상태 $k$의 개수 $m_k$에 대한 분포다.

$$
\operatorname{Mult}(m_1,\ldots,m_K\mid\boldsymbol{\mu},N)=\binom{N}{m_1\cdots m_K}\prod_{k=1}^K\mu_k^{m_k},\quad
\mathbb{E}[m_k]=N\mu_k,\quad \operatorname{var}[m_k]=N\mu_k(1-\mu_k),\quad \operatorname{cov}[m_jm_k]=-N\mu_j\mu_k
$$

### A.9 스튜던트 t 분포

- 같은 평균·다른 분산의 가우시안들의 무한 혼합이다. 자유도 $\nu>0$이며 $\nu=1$이면 코시 분포, $\nu\to\infty$이면 가우시안이 된다.

$$
\operatorname{St}(x\mid\mu,\lambda,\nu)=\frac{\Gamma(\nu/2+1/2)}{\Gamma(\nu/2)}\Bigl(\frac{\lambda}{\pi\nu}\Bigr)^{1/2}\Bigl[1+\frac{\lambda(x-\mu)^2}{\nu}\Bigr]^{-\nu/2-1/2},\quad
\mathbb{E}[x]=\mu\ (\nu>1),\quad \operatorname{var}[x]=\frac{1}{\lambda}\frac{\nu}{\nu-2}\ (\nu>2)
$$

### A.10 균등 · 폰 미제스 · 위샤트 분포

- **균등 분포** $\mathrm{U}(x\mid a,b)=\frac{1}{b-a}$, $\mathbb{E}[x]=\frac{a+b}{2}$, $\operatorname{var}[x]=\frac{(b-a)^2}{12}$.
- **폰 미제스 분포**<span class="gloss">von Mises</span>는 주기 변수 $\theta\in[0,2\pi]$에 대한 가우시안 유사 분포다. $p(\theta\mid\theta_0,m)=\frac{1}{2\pi I_0(m)}\exp\{m\cos(\theta-\theta_0)\}$($I_0$은 0차 베셀 함수, $m$은 집중 매개변수).
- **위샤트 분포**<span class="gloss">Wishart</span>는 다변량 가우시안 정밀도 행렬의 켤레 사전 분포다.

$$
\mathcal{W}(\boldsymbol{\Lambda}\mid\mathbf{W},\nu)=B(\mathbf{W},\nu)|\boldsymbol{\Lambda}|^{(\nu-D-1)/2}\exp\Bigl\{-\tfrac12\operatorname{Tr}(\mathbf{W}^{-1}\boldsymbol{\Lambda})\Bigr\},\qquad
\mathbb{E}[\boldsymbol{\Lambda}]=\nu\mathbf{W}
$$

::: tip 실습 · 분포 모멘트 공식 검증
베타·감마·디리클레·스튜던트 t 분포에서 표본을 뽑아, 위 표의 평균·분산 공식과 일치하는지 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0); N = 500000
a, b = 2.0, 5.0                                         # Beta(a, b)
s = rng.beta(a, b, N)
print(f"Beta({a},{b}): 평균 {s.mean():.4f} (이론 {a/(a+b):.4f}), 분산 {s.var():.5f} (이론 {a*b/((a+b)**2*(a+b+1)):.5f})")
ag, bg = 3.0, 2.0                                       # Gam(a, b): rate b → scale 1/b
g = rng.gamma(ag, 1/bg, N)
print(f"Gam({ag},{bg}): 평균 {g.mean():.4f} (이론 {ag/bg:.4f}), 분산 {g.var():.5f} (이론 {ag/bg**2:.5f})")
al = np.array([2.0, 3.0, 5.0])                          # Dirichlet
d = rng.dirichlet(al, N)
print(f"Dir{al.tolist()}: 평균 {np.round(d.mean(0),4).tolist()} (이론 {np.round(al/al.sum(),4).tolist()})")
nu = 5.0                                                # Student-t
t = rng.standard_t(nu, N)
print(f"St(ν={nu}): 분산 {t.var():.4f} (이론 ν/(ν-2)={nu/(nu-2):.4f})")
```

</PyRunner>

## B. 행렬의 성질

### B.1 기본 성질

$$
(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top},\quad
(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1},\quad
(\mathbf{A}^{\top})^{-1}=(\mathbf{A}^{-1})^{\top}
$$

- 유용한 항등식과 **우드베리 항등식**<span class="gloss">Woodbury identity</span>은 다음과 같다($M\ll N$이면 우변 계산이 훨씬 효율적).

$$
(\mathbf{P}^{-1}+\mathbf{B}^{\top}\mathbf{R}^{-1}\mathbf{B})^{-1}\mathbf{B}^{\top}\mathbf{R}^{-1}=\mathbf{P}\mathbf{B}^{\top}(\mathbf{B}\mathbf{P}\mathbf{B}^{\top}+\mathbf{R})^{-1}
$$

$$
(\mathbf{A}+\mathbf{B}\mathbf{D}^{-1}\mathbf{C})^{-1}=\mathbf{A}^{-1}-\mathbf{A}^{-1}\mathbf{B}(\mathbf{D}+\mathbf{C}\mathbf{A}^{-1}\mathbf{B})^{-1}\mathbf{C}\mathbf{A}^{-1}
$$

### B.2 대각합과 행렬식

$$
\operatorname{Tr}(\mathbf{A}\mathbf{B})=\operatorname{Tr}(\mathbf{B}\mathbf{A}),\quad
\operatorname{Tr}(\mathbf{A}\mathbf{B}\mathbf{C})=\operatorname{Tr}(\mathbf{C}\mathbf{A}\mathbf{B})=\operatorname{Tr}(\mathbf{B}\mathbf{C}\mathbf{A}),\quad
|\mathbf{A}\mathbf{B}|=|\mathbf{A}||\mathbf{B}|,\quad |\mathbf{A}^{-1}|=\frac{1}{|\mathbf{A}|}
$$

- $\mathbf{A}$, $\mathbf{B}$가 $N\times M$이면 $|\mathbf{I}_N+\mathbf{A}\mathbf{B}^{\top}|=|\mathbf{I}_M+\mathbf{A}^{\top}\mathbf{B}|$이고, 벡터에 대해 $|\mathbf{I}_N+\mathbf{a}\mathbf{b}^{\top}|=1+\mathbf{a}^{\top}\mathbf{b}$이다.

### B.3 행렬 미분

$$
\frac{\partial}{\partial\mathbf{x}}(\mathbf{x}^{\top}\mathbf{a})=\mathbf{a},\quad
\frac{\partial}{\partial x}(\mathbf{A}^{-1})=-\mathbf{A}^{-1}\frac{\partial\mathbf{A}}{\partial x}\mathbf{A}^{-1},\quad
\frac{\partial}{\partial x}\ln|\mathbf{A}|=\operatorname{Tr}\Bigl(\mathbf{A}^{-1}\frac{\partial\mathbf{A}}{\partial x}\Bigr)
$$

$$
\frac{\partial}{\partial\mathbf{A}}\operatorname{Tr}(\mathbf{A}\mathbf{B})=\mathbf{B}^{\top},\quad
\frac{\partial}{\partial\mathbf{A}}\operatorname{Tr}(\mathbf{A}^{\top}\mathbf{B})=\mathbf{B},\quad
\frac{\partial}{\partial\mathbf{A}}\operatorname{Tr}(\mathbf{A}\mathbf{B}\mathbf{A}^{\top})=\mathbf{A}(\mathbf{B}+\mathbf{B}^{\top}),\quad
\frac{\partial}{\partial\mathbf{A}}\ln|\mathbf{A}|=(\mathbf{A}^{-1})^{\top}
$$

### B.4 고윳값 공식

- 정방 행렬 $\mathbf{A}$의 **고유벡터**<span class="gloss">eigenvector</span> $\mathbf{u}_i$·**고윳값**<span class="gloss">eigenvalue</span> $\lambda_i$는 $\mathbf{A}\mathbf{u}_i=\lambda_i\mathbf{u}_i$이며, 해의 존재 조건인 **특성 방정식**<span class="gloss">characteristic equation</span>은 $|\mathbf{A}-\lambda_i\mathbf{I}|=0$이다.

::: tip 실습 · 행렬 항등식 검증 (우드베리 · 행렬식 보조정리)
우드베리 항등식과 $|\mathbf{I}_N+\mathbf{A}\mathbf{B}^{\top}|=|\mathbf{I}_M+\mathbf{A}^{\top}\mathbf{B}|$을 무작위 행렬로 수치 검증합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)
n, m = 5, 2
A = rng.standard_normal((n, n)); A = A@A.T + n*np.eye(n)         # 양의 정부호
B = rng.standard_normal((n, m)); C = rng.standard_normal((m, n))
D = rng.standard_normal((m, m)); D = D@D.T + np.eye(m)
lhs = np.linalg.inv(A + B@np.linalg.inv(D)@C)
rhs = np.linalg.inv(A) - np.linalg.inv(A)@B@np.linalg.inv(D + C@np.linalg.inv(A)@B)@C@np.linalg.inv(A)
print(f"우드베리 항등식 최대 오차: {np.abs(lhs-rhs).max():.2e}")
Am = rng.standard_normal((n, m)); Bm = rng.standard_normal((n, m))
d1 = np.linalg.det(np.eye(n) + Am@Bm.T); d2 = np.linalg.det(np.eye(m) + Am.T@Bm)
print(f"|I_N+ABᵀ|={d1:.4f}, |I_M+AᵀB|={d2:.4f}, 오차={abs(d1-d2):.2e}")
```

</PyRunner>

## C. 변분법

- **범함수**<span class="gloss">functional</span> $F[y]$는 함수 $y(x)$를 입력받아 값을 내는 연산자다. 함수의 미소 변화 $y(x)\to y(x)+\epsilon\eta(x)$에 대한 **범함수 미분**<span class="gloss">functional derivative</span>은

$$
F[y(x)+\epsilon\eta(x)]=F[y(x)]+\epsilon\int\frac{\delta F}{\delta y(x)}\eta(x)\,\mathrm{d}x+O(\epsilon^2)
$$

  로 정의된다. 임의의 $\eta(x)$에 대해 정류 조건 $\int\frac{\delta F}{\delta y(x)}\eta(x)\,\mathrm{d}x=0$이 성립하려면 모든 $x$에서 범함수 미분이 $0$이어야 한다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/FigureD.1.png" style="width:22rem;" />
<div class="cap">

그림 C.1 · 범함수 미분은 $y(x)\to y(x)+\epsilon\eta(x)$의 변화에 대한 $F[y]$의 변화로 정의된다($\eta(x)$는 임의 함수).

</div>
</div>

- $F[y]=\int G(y,y',x)\,\mathrm{d}x$ 형태의 범함수를 정류시키는 함수는 **오일러–라그랑주 방정식**<span class="gloss">Euler–Lagrange equation</span>을 만족한다.

$$
\frac{\partial G}{\partial y}-\frac{\mathrm{d}}{\mathrm{d}x}\Bigl(\frac{\partial G}{\partial y'}\Bigr)=0
$$

## D. 라그랑주 승수법

- **라그랑주 승수법**<span class="gloss">Lagrange multiplier</span>은 제약 조건 하의 임계점을 찾는다. 제약 $g(\mathbf{x})=0$의 표면에서 $\nabla g$는 표면에 수직이고, $f(\mathbf{x})$의 최적점에서 $\nabla f$도 표면에 수직이어야 하므로 두 기울기가 평행하다.

$$
\nabla f+\lambda\nabla g=0,\qquad
L(\mathbf{x},\lambda)\equiv f(\mathbf{x})+\lambda g(\mathbf{x})
$$

  라그랑주 함수 $L$의 $\mathbf{x}$·$\lambda$에 대한 임계점을 찾으면 된다($\partial L/\partial\lambda=0$이 곧 제약 $g(\mathbf{x})=0$).

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/FigureE.1.png" style="width:20rem;" />
<div class="cap">

그림 D.1 · 라그랑주 승수법의 기하. 제약 $g(\mathbf{x})=0$(적색) 하에서 $f(\mathbf{x})$를 최대화하며, $L(\mathbf{x},\lambda)=f(\mathbf{x})+\lambda g(\mathbf{x})$를 최적화해 푼다.

</div>
</div>

- **부등식 제약**<span class="gloss">inequality constraint</span> $g(\mathbf{x})\geqslant0$ 하의 최대화는 다음 **카루시–쿤–터커**<span class="gloss">Karush–Kuhn–Tucker; KKT</span> 조건 하에 $L$을 최적화한다.

$$
g(\mathbf{x})\geqslant0,\qquad \lambda\geqslant0,\qquad \lambda g(\mathbf{x})=0
$$

  제약이 **비활성**<span class="gloss">inactive</span>이면($g>0$) $\lambda=0$이라 $\nabla f=0$, **활성**<span class="gloss">active</span>이면($g=0$) 등식 제약과 같다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/FigureE.3.png" style="width:20rem;" />
<div class="cap">

그림 D.2 · 부등식 제약 $g(\mathbf{x})\geqslant0$ 하에서 $f(\mathbf{x})$를 최대화하는 문제.

</div>
</div>

::: tip 실습 · 라그랑주 승수법
$g(\mathbf{x})=x^2+y^2-1=0$ 제약 하에 $f(\mathbf{x})=x+y$를 최대화합니다. 해석해 $(1/\sqrt2,1/\sqrt2)$에서 $\nabla f=\lambda\nabla g$가 성립하고, 원 위 격자 탐색의 최댓값 $\sqrt2$와 일치함을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
# max f=x+y  s.t. g=x²+y²-1=0.  ∇f=λ∇g → (1,1)=λ(2x,2y) → x=y=1/√2
xst = 1/np.sqrt(2)
gradf = np.array([1.0, 1.0]); gradg = np.array([2*xst, 2*xst]); lam = gradf[0]/gradg[0]
print(f"최적점 (x,y)=({xst:.4f},{xst:.4f}), f={xst+xst:.4f} (최댓값 √2={np.sqrt(2):.4f})")
print(f"∇f={gradf.tolist()},  λ∇g={(lam*gradg).round(4).tolist()}  (∇f=λ∇g 성립, λ={lam:.4f})")
th = np.linspace(0, 2*np.pi, 100000); vals = np.cos(th) + np.sin(th)   # 원 위 격자
print(f"격자 탐색 최댓값={vals.max():.4f} at θ={th[vals.argmax()]:.4f} (π/4={np.pi/4:.4f})")
```

</PyRunner>
