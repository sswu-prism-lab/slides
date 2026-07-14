# 8 · 근사 추정

> 확률 모델에서 가장 중요한 일 중 하나는 사후 분포나 그 기댓값을 계산하는 것이지만, 실제로는 이 계산이 불가능할 수 있다. 결정론적 근사 방법을 쓰면 유한한 시간 안에 근사해를 찾을 수 있다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/photos/sec08.png" style="max-width:34rem;" />
</div>

## 8.1 변분적 추론

- 변분적 방법은 **변분법**<span class="gloss">calculus of variations</span>에 기반한다. 함수가 값을 받아 값을 내는 사상이라면, **범함수**<span class="gloss">functional</span>는 함수를 받아 값을 내는 사상이다(예: 엔트로피 $\mathrm{H}[p]=-\int p(x)\ln p(x)\,\mathrm{d}x$). 잠재 변수·매개변수 전체를 $\mathbf{Z}$, 관측 변수를 $\mathbf{X}$로 두면 로그 주변 확률은 다음처럼 분해된다.

$$
\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p) \tag{10.2}
$$

$$
\mathcal{L}(q)=\int q(\mathbf{Z})\ln\frac{p(\mathbf{X},\mathbf{Z})}{q(\mathbf{Z})}\,\mathrm{d}\mathbf{Z},\qquad
\mathrm{KL}(q\|p)=-\int q(\mathbf{Z})\ln\frac{p(\mathbf{Z}\mid\mathbf{X})}{q(\mathbf{Z})}\,\mathrm{d}\mathbf{Z}
$$

- 하한 $\mathcal{L}(q)$를 최대화하는 것은 **쿨백–라이블러 발산**<span class="gloss">Kullback–Leibler divergence</span>을 최소화하는 것과 같다. $q(\mathbf{Z})=p(\mathbf{Z}\mid\mathbf{X})$이면 $\mathrm{KL}=0$이지만 실제 사후 분포는 다루기 어려우므로, $q$를 더 제한된 종류로 한정해 그 안에서 최적해를 찾는다.

### 8.1.1 인수분해된 분포

- $\mathbf{Z}$를 서로소 집합 $\mathbf{Z}_i$로 나누고 $q$가 이들에 대해 인수분해된다고 가정한다(**평균장 근사**<span class="gloss">mean-field approximation</span>).

$$
q(\mathbf{Z})=\prod_{i=1}^M q_i(\mathbf{Z}_i) \tag{10.5}
$$

- 각 인자 $q_j$에 대해 $\mathcal{L}(q)$를 자유 형태로 변분 최적화하면, 최적 인자는 나머지 인자들에 대한 결합 로그 분포의 기댓값으로 주어진다.

$$
\ln q_j^{\star}(\mathbf{Z}_j)=\mathbb{E}_{i\neq j}[\ln p(\mathbf{X},\mathbf{Z})]+\text{const} \tag{10.9}
$$

  각 인자가 다른 인자의 기댓값에 의존하므로, 인자들을 번갈아 갱신해 수렴시킨다.

### 8.1.2 인수분해 근사의 성질

- 상관된 2변수 가우시안 $p(\mathbf{z})=\mathcal{N}(\mathbf{z}\mid\boldsymbol{\mu},\boldsymbol{\Lambda}^{-1})$를 $q(\mathbf{z})=q_1(z_1)q_2(z_2)$로 근사하면, (10.9)에서 각 인자가 가우시안이 되고

$$
q_1^{\star}(z_1)=\mathcal{N}(z_1\mid m_1,\Lambda_{11}^{-1}),\quad m_1=\mu_1-\Lambda_{11}^{-1}\Lambda_{12}(\mathbb{E}[z_2]-\mu_2)
$$

  $q_2$도 대칭적으로 얻는다. 평균은 $\mathbb{E}[z_1]=\mu_1$, $\mathbb{E}[z_2]=\mu_2$로 정확하지만, 각 축의 분산은 조건부 분산 $\Lambda_{kk}^{-1}$이라 참 주변 분산 $(\boldsymbol{\Lambda}^{-1})_{kk}$보다 **작다**. 즉 $\mathrm{KL}(q\|p)$ 기반 변분 근사는 분산을 과소평가한다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.2a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.2b.png" />
</div>
<div class="cap">

그림 8.1 · 상관된 가우시안 $p(\mathbf{z})$(녹색)를 인수분해 가우시안 $q(\mathbf{z})$(적색)로 근사. (a) $\mathrm{KL}(q\|p)$ 최소화, (b) $\mathrm{KL}(p\|q)$ 최소화.

</div>
</div>

- $\mathrm{KL}(q\|p)$를 최소화하면 분포의 한 최빈값으로 붙는(mode-seeking) 경향이, $\mathrm{KL}(p\|q)$를 최소화하면 모든 최빈값을 평균 내는(mean-covering) 경향이 있다. 두 발산은 모두 **알파족**<span class="gloss">alpha family</span> 발산 $\mathrm{D}_\alpha$의 특수한 경우다($\mathrm{KL}(p\|q)$는 $\alpha\to1$, $\mathrm{KL}(q\|p)$는 $\alpha\to-1$, $\alpha=0$은 대칭적 **헬링거 거리**<span class="gloss">Hellinger distance</span>).

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.3a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.3b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.3c.png" />
</div>
<div class="cap">

그림 8.2 · 양봉 분포 $p(\mathbf{Z})$(청색)를 단일 가우시안 $q$(적색)로 근사. (왼쪽) $\mathrm{KL}(p\|q)$는 두 봉우리를 덮고, (가운데·오른쪽) $\mathrm{KL}(q\|p)$는 한 봉우리에 붙는다(지역 최솟값 둘).

</div>
</div>

::: tip 실습 · 인수분해 변분 근사의 분산 과소평가
상관된 2변수 가우시안을 $q_1(z_1)q_2(z_2)$로 근사할 때, 평균장 갱신 $m_1=\mu_1-\Lambda_{11}^{-1}\Lambda_{12}(\mathbb{E}[z_2]-\mu_2)$를 반복하면 평균은 맞지만 축별 분산이 참 주변 분산보다 작아지는 것을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
mu = np.array([0.0, 0.0])
Lam = np.array([[2.0, 1.6], [1.6, 2.0]])       # 정밀도 (상관이 큼)
Sigma = np.linalg.inv(Lam)
m = np.array([2.0, -1.0])                        # 초기값
for it in range(30):
    m1 = mu[0] - Lam[0,0]**-1 * Lam[0,1]*(m[1]-mu[1])
    m2 = mu[1] - Lam[1,1]**-1 * Lam[1,0]*(m1-mu[0])
    new = np.array([m1, m2])
    if np.linalg.norm(new-m) < 1e-12: m = new; break
    m = new
print("수렴 평균 q :", np.round(m, 4).tolist(), " (참 평균 [0, 0])")
print("q 분산(축별):", [round(float(1/Lam[0,0]),4), round(float(1/Lam[1,1]),4)])
print("참 주변 분산:", [round(float(Sigma[0,0]),4), round(float(Sigma[1,1]),4)])
print("→ 변분 근사가 주변 분산을 과소평가")
```

</PyRunner>

::: tip 실습 · 두 방향의 KL 발산 ($\mathrm{KL}(q\|p)$ vs $\mathrm{KL}(p\|q)$)
양봉 목표 분포를 단일 가우시안으로 근사할 때, $\mathrm{KL}(p\|q)$ 최소화(모멘트 매칭)는 두 봉우리를 넓게 덮고, $\mathrm{KL}(q\|p)$ 최소화는 한 봉우리에 붙는 것을 비교합니다.
:::

<PyRunner>

```python
import numpy as np
def p(x):
    return (0.5*np.exp(-(x+2)**2/(2*0.5**2)) + 0.5*np.exp(-(x-2)**2/(2*0.5**2)))/np.sqrt(2*np.pi*0.5**2)
def gauss(x, mu, s): return np.exp(-(x-mu)**2/(2*s**2))/np.sqrt(2*np.pi*s**2)
xs = np.linspace(-8, 8, 4001); dx = xs[1]-xs[0]; px = p(xs)
# KL(p||q): 모멘트 매칭 (해석적)
Ep = np.sum(xs*px)*dx; Ep2 = np.sum(xs**2*px)*dx
mu_pm, s_pm = Ep, np.sqrt(Ep2-Ep**2)
# KL(q||p): 그리드 최소화
best = None
for mu_ in np.linspace(-4, 4, 81):
    for s_ in np.linspace(0.2, 3, 57):
        q = gauss(xs, mu_, s_); mk = q > 1e-12
        kl = np.sum(q[mk]*(np.log(q[mk])-np.log(px[mk]+1e-300)))*dx
        if best is None or kl < best[0]: best = (kl, mu_, s_)
print(f"KL(p||q) 모멘트매칭: μ={mu_pm:+.3f}, σ={s_pm:.3f}  (두 봉우리를 넓게 덮음)")
print(f"KL(q||p) 최빈값탐색: μ={best[1]:+.3f}, σ={best[2]:.3f}  (한 봉우리에 붙음)")
```

</PyRunner>

## 8.2 변분적 가우시안 혼합 분포 예시

- 베이지안 가우시안 혼합에서 잠재 변수 $p(\mathbf{Z}\mid\boldsymbol{\pi})=\prod_n\prod_k\pi_k^{z_{nk}}$, 관측 $p(\mathbf{X}\mid\mathbf{Z},\boldsymbol{\mu},\boldsymbol{\Lambda})=\prod_n\prod_k\mathcal{N}(\mathbf{x}_n\mid\boldsymbol{\mu}_k,\boldsymbol{\Lambda}_k^{-1})^{z_{nk}}$에, 켤레 사전 분포로 $\boldsymbol{\pi}$에 디리클레, $(\boldsymbol{\mu},\boldsymbol{\Lambda})$에 가우시안–위샤트를 둔다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.5.png" style="width:20rem;" />
<div class="cap">

그림 8.3 · 베이지안 가우시안 혼합의 방향성 그래프. 판은 $N$개 관측이며 $\boldsymbol{\Lambda}\to\boldsymbol{\mu}$ 링크가 있다.

</div>
</div>

### 8.2.1 변분적 분포

- $q(\mathbf{Z},\boldsymbol{\pi},\boldsymbol{\mu},\boldsymbol{\Lambda})=q(\mathbf{Z})q(\boldsymbol{\pi},\boldsymbol{\mu},\boldsymbol{\Lambda})$로 인수분해하면 잠재 변수 인자는

$$
\ln q^{\star}(\mathbf{Z})=\sum_{n=1}^N\sum_{k=1}^K z_{nk}\ln\rho_{nk}+\text{const},\qquad
r_{nk}=\frac{\rho_{nk}}{\sum_{j=1}^K\rho_{nj}} \tag{10.45}
$$

  로 정규화되며 $\mathbb{E}[z_{nk}]=r_{nk}$가 책임값 역할을 한다. 책임값으로 통계량 $N_k=\sum_n r_{nk}$, $\overline{\mathbf{x}}_k=\frac{1}{N_k}\sum_n r_{nk}\mathbf{x}_n$, $\mathbf{S}_k=\frac{1}{N_k}\sum_n r_{nk}(\mathbf{x}_n-\overline{\mathbf{x}}_k)(\mathbf{x}_n-\overline{\mathbf{x}}_k)^{\top}$를 정의하며, 이는 EM의 값들과 유사하다.

## 8.3 변분적 선형 회귀

- 선형 회귀에 가능도 $p(\mathsf{t}\mid\mathbf{w})=\prod_n\mathcal{N}(t_n\mid\mathbf{w}^{\top}\boldsymbol{\phi}_n,\beta^{-1})$, 사전 분포 $p(\mathbf{w}\mid\alpha)=\mathcal{N}(\mathbf{w}\mid\mathbf{0},\alpha^{-1}\mathbf{I})$, $\alpha$에 켤레 감마 사전 $p(\alpha)=\mathrm{Gam}(\alpha\mid a_0,b_0)$을 둔다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.8.png" style="width:18rem;" />
<div class="cap">

그림 8.4 · 베이지안 선형 회귀 $p(\mathsf{t},\mathbf{w},\alpha)=p(\mathsf{t}\mid\mathbf{w})p(\mathbf{w}\mid\alpha)p(\alpha)$의 그래프 모델.

</div>
</div>

### 8.3.1 변분적 분포

- $q(\mathbf{w},\alpha)=q(\mathbf{w})q(\alpha)$로 두면 $q^{\star}(\alpha)$는 감마 분포, $q^{\star}(\mathbf{w})$는 가우시안이 된다.

$$
q^{\star}(\alpha)=\mathrm{Gam}(\alpha\mid a_N,b_N),\quad a_N=a_0+\tfrac{M}{2},\quad b_N=b_0+\tfrac{1}{2}\mathbb{E}[\mathbf{w}^{\top}\mathbf{w}]
$$

$$
q^{\star}(\mathbf{w})=\mathcal{N}(\mathbf{w}\mid\mathbf{m}_N,\mathbf{S}_N),\quad
\mathbf{m}_N=\beta\mathbf{S}_N\boldsymbol{\Phi}^{\top}\mathsf{t},\quad
\mathbf{S}_N=(\mathbb{E}[\alpha]\mathbf{I}+\beta\boldsymbol{\Phi}^{\top}\boldsymbol{\Phi})^{-1}
$$

  증거 최대화 EM 결과와 거의 같되, $\alpha$의 점 추정이 기댓값 $\mathbb{E}[\alpha]$로 바뀐 것이 차이다.

### 8.3.2 예측 분포

- 예측 분포는 $q(\mathbf{w})$로 주변화해 얻는다.

$$
p(t\mid\mathbf{x},\mathsf{t})=\mathcal{N}(t\mid\mathbf{m}_N^{\top}\boldsymbol{\phi}(\mathbf{x}),\sigma^2(\mathbf{x})),\qquad
\sigma^2(\mathbf{x})=\frac{1}{\beta}+\boldsymbol{\phi}(\mathbf{x})^{\top}\mathbf{S}_N\boldsymbol{\phi}(\mathbf{x})
$$

## 8.4 지수족 분포

- 매개변수 $\boldsymbol{\theta}$는 수가 고정된 **집중적**<span class="gloss">intensive</span> 변수, 잠재 변수 $\mathbf{Z}$는 데이터가 늘수록 늘어나는 **광역적**<span class="gloss">extensive</span> 변수다. 결합 분포가 지수족 $p(\mathbf{X},\mathbf{Z}\mid\boldsymbol{\eta})=\prod_n h(\mathbf{x}_n,\mathbf{z}_n)g(\boldsymbol{\eta})\exp\{\boldsymbol{\eta}^{\top}\mathbf{u}(\mathbf{x}_n,\mathbf{z}_n)\}$이고 $\boldsymbol{\eta}$에 켤레 사전 분포를 두면, $q(\mathbf{Z},\boldsymbol{\eta})=q(\mathbf{Z})q(\boldsymbol{\eta})$의 두 인자를 닫힌 형태로 갱신할 수 있다($\nu_N=\nu_0+N$).

## 8.5 지역적 변분 방법론

- 전역 변분법이 전체 사후 분포를 근사하는 반면, **지역적 변분법**은 개별 변수·함수의 경계를 찾는다. 볼록 함수 $f(x)$의 접선은 하한이며, 기울기 $\eta$의 접선을 $\eta x-g(\eta)$로 쓰면 **볼록 쌍대성**<span class="gloss">convex duality</span>으로

$$
f(x)=\max_\eta\{\eta x-g(\eta)\},\qquad g(\eta)=\max_x\{\eta x-f(x)\}
$$

  를 얻는다. 예컨대 $f(x)=\exp(-x)$의 접선 하한은 $\eta=-\exp(-\xi)$로 매개변수화되며, 엄밀한 경계를 위해 $\eta$를 최적화한다. 오목 함수면 $\max\leftrightarrow\min$이 바뀌어 상한을 준다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.10a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.10b.png" />
</div>
<div class="cap">

그림 8.5 · (왼쪽) $\exp(-x)$(적색)와 $x=\xi=1$의 접선(청색). (오른쪽) $\eta\xi-g(\eta)$는 $\eta=-1/e$에서 최대.

</div>
</div>

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.11a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.11b.png" />
</div>
<div class="cap">

그림 8.6 · 볼록 함수 $f(x)$(적색)와 하한 $\eta x$(청색). 듀얼 함수 $g(\eta)$는 기울기 $\eta$ 접선의 절편이다.

</div>
</div>

## 8.6 변분적 로지스틱 회귀

### 8.6.1 변분적 사후 분포

- 로지스틱 회귀의 주변 가능도 $p(\mathsf{t})=\int\prod_n p(t_n\mid\mathbf{w})\,p(\mathbf{w})\,\mathrm{d}\mathbf{w}$는 다룰 수 없다. $p(t\mid\mathbf{w})=e^{at}\sigma(-a)$($a=\mathbf{w}^{\top}\boldsymbol{\phi}$)에 시그모이드의 변분 하한을 적용한다.

$$
\sigma(z)\geqslant\sigma(\xi)\exp\{(z-\xi)/2-\lambda(\xi)(z^2-\xi^2)\},\qquad
\lambda(\xi)=\frac{1}{2\xi}\Bigl[\sigma(\xi)-\frac{1}{2}\Bigr]
$$

- 관측마다 변분 매개변수 $\xi_n$을 두면 결합 분포의 하한이 $\mathbf{w}$에 대한 이차식이 되어, 사후 분포의 가우시안 근사를 얻는다.

$$
q(\mathbf{w})=\mathcal{N}(\mathbf{w}\mid\mathbf{m}_N,\mathbf{S}_N),\quad
\mathbf{m}_N=\mathbf{S}_N\Bigl(\mathbf{S}_0^{-1}\mathbf{m}_0+\sum_n(t_n-\tfrac12)\boldsymbol{\phi}_n\Bigr),\quad
\mathbf{S}_N^{-1}=\mathbf{S}_0^{-1}+2\sum_n\lambda(\xi_n)\boldsymbol{\phi}_n\boldsymbol{\phi}_n^{\top}
$$

::: tip 실습 · 로지스틱 시그모이드의 변분 하한
$\sigma(z)\geqslant\sigma(\xi)\exp\{(z-\xi)/2-\lambda(\xi)(z^2-\xi^2)\}$이 $z=\pm\xi$에서 시그모이드에 접하고 다른 곳에서 하한임을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
def sig(z): return 1/(1+np.exp(-z))
def lam(xi): return (sig(xi)-0.5)/(2*xi)
def bound(z, xi): return sig(xi)*np.exp((z-xi)/2 - lam(xi)*(z**2-xi**2))
xi = 2.0
print(f"변분 매개변수 ξ={xi} (z=±ξ에서 등호)")
print(f"  {'z':>4} {'σ(z)':>8} {'하한':>8} {'차이':>9}")
for z in [-3, -2, -1, 0, 1, 2, 3]:
    print(f"  {z:>4} {sig(z):>8.4f} {bound(z, xi):>8.4f} {sig(z)-bound(z, xi):>9.5f}")
```

</PyRunner>

### 8.6.2 변분적 매개변수의 최적화

- $\xi_n$은 하한 $\mathcal{L}(\boldsymbol{\xi})=\ln\int h(\mathbf{w},\boldsymbol{\xi})p(\mathbf{w})\,\mathrm{d}\mathbf{w}\leqslant\ln p(\mathsf{t})$를 최대화해 정한다. EM 접근에서 재추정식은

$$
(\xi_n^{\mathrm{new}})^2=\boldsymbol{\phi}_n^{\top}\mathbb{E}[\mathbf{w}\mathbf{w}^{\top}]\boldsymbol{\phi}_n=\boldsymbol{\phi}_n^{\top}(\mathbf{S}_N+\mathbf{m}_N\mathbf{m}_N^{\top})\boldsymbol{\phi}_n
$$

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.13a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.13b.png" />
</div>
<div class="cap">

그림 8.7 · 변분적 베이지안 로지스틱 회귀. (왼쪽) 예측 분포와 결정 경계, 데이터에서 멀수록 불확실성 증가. (오른쪽) 사후 분포에서 뽑은 $\mathbf{w}$ 표본 다섯의 결정 경계.

</div>
</div>

### 8.6.3 초매개변수 추론

- 초매개변수 $\alpha$까지 데이터로부터 추론하려면 전역 변분법과 지역 변분법을 결합한다. $q(\mathbf{w},\alpha)=q(\mathbf{w})q(\alpha)$로 두면 $q(\mathbf{w})$는 가우시안, $q(\alpha)$는 감마 분포가 되어 번갈아 갱신한다.

## 8.7 기대 전파 (EP)

- **기대 전파**<span class="gloss">expectation propagation; EP</span>도 결정적 근사이지만, 변분법과 반대로 $\mathrm{KL}(p\|q)$를 최소화한다. $q$가 지수족일 때 $\mathrm{KL}(p\|q)$ 최소화는 충분 통계량의 기댓값을 맞추는 **모멘트 매칭**<span class="gloss">moment matching</span>과 같다($\mathbb{E}_q[\mathbf{u}]=\mathbb{E}_p[\mathbf{u}]$).

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.14a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure10.14b.png" />
</div>
<div class="cap">

그림 8.8 · 라플라스(적색)·전역 변분(녹색)·EP(청색) 근사 비교. EP는 $\mathrm{KL}(p\|q)$를 써서 변분 근사보다 넓은 분포를 낸다.

</div>
</div>

::: info EP 알고리즘
결합 분포가 인자들의 곱 $p(\mathcal{D},\boldsymbol{\theta})=\prod_i f_i(\boldsymbol{\theta})$일 때, 사후 분포를 $q(\boldsymbol{\theta})=\frac{1}{Z}\prod_i\widetilde{f}_i(\boldsymbol{\theta})$로 근사한다.

1. 근사 인자 $\widetilde{f}_i$를 초기화하고 $q(\boldsymbol{\theta})\propto\prod_i\widetilde{f}_i(\boldsymbol{\theta})$로 둔다.

2. 수렴할 때까지 각 인자 $\widetilde{f}_j$에 대해 반복한다.

  - 제거: $q^{\backslash j}(\boldsymbol{\theta})=q(\boldsymbol{\theta})/\widetilde{f}_j(\boldsymbol{\theta})$

  - 갱신: $q^{\mathrm{new}}$의 모멘트를 $q^{\backslash j}(\boldsymbol{\theta})f_j(\boldsymbol{\theta})$의 모멘트와 맞추고 $Z_j=\int q^{\backslash j}f_j\,\mathrm{d}\boldsymbol{\theta}$를 계산한다.

  - 인자 갱신: $\widetilde{f}_j(\boldsymbol{\theta})=Z_j\,q^{\mathrm{new}}(\boldsymbol{\theta})/q^{\backslash j}(\boldsymbol{\theta})$

3. 모델 증거를 $p(\mathcal{D})\simeq\int\prod_i\widetilde{f}_i(\boldsymbol{\theta})\,\mathrm{d}\boldsymbol{\theta}$로 근사한다.
:::

## 연습문제

::: info 문제 8.1
관측 데이터의 로그 주변 분포 $\ln p(\mathbf{X})$가 (10.2)의 형태 $\mathcal{L}(q)+\mathrm{KL}(q\|p)$로 분해됨을 증명하라.
:::

::: details 풀이
임의의 분포 $q(\mathbf{Z})$($\int q\,\mathrm{d}\mathbf{Z}=1$)에 대해, $p(\mathbf{X},\mathbf{Z})=p(\mathbf{Z}\mid\mathbf{X})p(\mathbf{X})$를 이용한다. $\ln p(\mathbf{X})$는 $\mathbf{Z}$에 무관하므로

$$
\ln p(\mathbf{X})=\int q(\mathbf{Z})\ln p(\mathbf{X})\,\mathrm{d}\mathbf{Z}
=\int q(\mathbf{Z})\ln\frac{p(\mathbf{X},\mathbf{Z})}{p(\mathbf{Z}\mid\mathbf{X})}\,\mathrm{d}\mathbf{Z}
$$

우변에 $q(\mathbf{Z})/q(\mathbf{Z})$를 곱해 분리한다.

$$
=\int q(\mathbf{Z})\ln\frac{p(\mathbf{X},\mathbf{Z})}{q(\mathbf{Z})}\,\mathrm{d}\mathbf{Z}
+\int q(\mathbf{Z})\ln\frac{q(\mathbf{Z})}{p(\mathbf{Z}\mid\mathbf{X})}\,\mathrm{d}\mathbf{Z}
$$

첫 항은 $\mathcal{L}(q)$, 둘째 항은 $-\int q\ln\frac{p(\mathbf{Z}\mid\mathbf{X})}{q}=\mathrm{KL}(q\|p)$이다. 따라서 $\ln p(\mathbf{X})=\mathcal{L}(q)+\mathrm{KL}(q\|p)$. $\mathrm{KL}\geqslant0$이므로 $\mathcal{L}(q)$는 하한이다. $\blacksquare$
:::

::: info 문제 8.2
로그 로지스틱 함수 $f(x)=-\ln(1+e^{-x})$가 오목 함수임을 이차 미분으로 증명하고, $x=\xi$ 주변 일차 테일러 전개로 변분적 상한 경계를 유도하라.
:::

::: details 풀이
$f(x)=-\ln(1+e^{-x})=\ln\sigma(x)$이다. 일차 미분은

$$
f'(x)=\frac{\sigma'(x)}{\sigma(x)}=\frac{\sigma(x)(1-\sigma(x))}{\sigma(x)}=1-\sigma(x)=\sigma(-x)
$$

이차 미분은

$$
f''(x)=-\sigma'(x)=-\sigma(x)(1-\sigma(x))<0
$$

모든 $x$에서 $f''(x)<0$이므로 $f$는 오목이다. 오목 함수는 접선이 함수 위에 있으므로, $x=\xi$에서의 일차 테일러 전개가 **상한**이 된다.

$$
f(x)\leqslant f(\xi)+f'(\xi)(x-\xi)=-\ln(1+e^{-\xi})+\sigma(-\xi)(x-\xi)
$$

이 선형 상한의 기울기 $\sigma(-\xi)$가 변분 매개변수 역할을 하며, $x=\xi$에서 등호가 성립한다. $\blacksquare$
:::

::: info 문제 8.3
고정 분포 $p(\mathbf{x})$를 가우시안 $q(\mathbf{x})=\mathcal{N}(\mathbf{x}\mid\boldsymbol{\mu},\boldsymbol{\Sigma})$로 근사할 때, $\mathrm{KL}(p\|q)$를 $\boldsymbol{\mu}$·$\boldsymbol{\Sigma}$에 대해 미분해 최소해가 모멘트 매칭임을 보여라.
:::

::: details 풀이
$\mathrm{KL}(p\|q)=\int p\ln p\,\mathrm{d}\mathbf{x}-\int p\ln q\,\mathrm{d}\mathbf{x}$에서 첫 항은 $q$에 무관하다. 둘째 항에 가우시안 로그

$$
-\ln q(\mathbf{x})=\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^{\top}\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})+\frac{1}{2}\ln|\boldsymbol{\Sigma}|+\frac{D}{2}\ln(2\pi)
$$

를 대입하면 $q$에 의존하는 부분은 $\int p(\mathbf{x})\{\tfrac12(\mathbf{x}-\boldsymbol{\mu})^{\top}\boldsymbol{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})+\tfrac12\ln|\boldsymbol{\Sigma}|\}\,\mathrm{d}\mathbf{x}$이다.

**$\boldsymbol{\mu}$에 대해** — 미분해 $0$으로 두면

$$
\frac{\partial}{\partial\boldsymbol{\mu}}=-\boldsymbol{\Sigma}^{-1}\int p(\mathbf{x})(\mathbf{x}-\boldsymbol{\mu})\,\mathrm{d}\mathbf{x}=\mathbf{0}\ \Longrightarrow\ \boldsymbol{\mu}=\mathbb{E}_p[\mathbf{x}]
$$

**$\boldsymbol{\Sigma}$에 대해** — $\frac{\partial}{\partial\boldsymbol{\Sigma}^{-1}}$를 취하면 $\frac12\int p\{(\mathbf{x}-\boldsymbol{\mu})(\mathbf{x}-\boldsymbol{\mu})^{\top}-\boldsymbol{\Sigma}\}\,\mathrm{d}\mathbf{x}=\mathbf{0}$에서

$$
\boldsymbol{\Sigma}=\mathbb{E}_p[(\mathbf{x}-\boldsymbol{\mu})(\mathbf{x}-\boldsymbol{\mu})^{\top}]=\operatorname{cov}_p[\mathbf{x}]
$$

즉 $\mathrm{KL}(p\|q)$의 최소해는 $q$의 평균·공분산을 $p$의 것과 맞추는 모멘트 매칭이다. $\blacksquare$
:::
