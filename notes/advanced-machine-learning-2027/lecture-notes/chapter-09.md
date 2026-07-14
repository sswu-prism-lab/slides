# 9 · 표집법

> 실제로 사용하는 확률 모델 중 많은 것은 정확한 추론이 매우 까다롭다. 결정론적 근사 외에도, 수치적 표집에 기반한 근사 추론이 널리 쓰이며 강력하다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/photos/sec09.png" style="max-width:34rem;" />
</div>

## 9.1 기본적인 표집 알고리즘

- 표집법의 목표는 함수 $f(\mathbf{z})$의 분포 $p(\mathbf{z})$에 대한 기댓값을 구하는 것이다. $p(\mathbf{z})$에서 독립 표본 $\mathbf{z}^{(l)}$을 뽑아 유한 합으로 근사한다.

$$
\widehat{f}=\frac{1}{L}\sum_{l=1}^L f(\mathbf{z}^{(l)}),\qquad
\operatorname{var}[\widehat{f}]=\frac{1}{L}\mathbb{E}[(f-\mathbb{E}[f])^2]
$$

  추정량의 분산은 $L$에 반비례해 줄지만, 표본이 독립이 아니면 더 많은 표본이 필요하다.

### 9.1.1 표준 분포 (역변환 표집)

- $(0,1)$ 균등 변수 $z$를 $y=f(z)$로 변환하면 $p(y)=p(z)|\mathrm{d}z/\mathrm{d}y|$이다. 원하는 $p(y)$의 누적 분포 $z=h(y)\equiv\int_{-\infty}^y p(\widehat{y})\,\mathrm{d}\widehat{y}$의 역함수로 변환하면 된다.

$$
y=h^{-1}(z) \tag{11.6}
$$

  예컨대 **지수 분포**<span class="gloss">exponential distribution</span> $p(y)=\lambda e^{-\lambda y}$는 $h(y)=1-e^{-\lambda y}$이므로 $y=-\lambda^{-1}\ln(1-z)$로 생성한다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure11.2.png" style="width:20rem;" />
<div class="cap">

그림 9.1 · 역변환 표집. $h(y)$는 $p(y)$의 누적 분포이며, 균등 변수 $z$를 $y=h^{-1}(z)$로 변환하면 $y\sim p(y)$가 된다.

</div>
</div>

::: tip 실습 · 역변환 표집 (지수 분포)
균등 난수 $z$를 $y=-\lambda^{-1}\ln(1-z)$로 변환하면 지수 분포가 됨을, 표본 평균·분산이 $1/\lambda$·$1/\lambda^2$에 수렴함으로 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0); lam = 1.5; L = 200000
z = rng.uniform(0, 1, L)
y = -np.log(1-z)/lam                                    # y = -λ⁻¹ ln(1-z)
print(f"표본 평균={y.mean():.4f} (이론 1/λ={1/lam:.4f})")
print(f"표본 분산={y.var():.4f} (이론 1/λ²={1/lam**2:.4f})")
```

</PyRunner>

### 9.1.2 거부 표집법

- **거부 표집법**<span class="gloss">rejection sampling</span>은 정규화 상수를 모르는 $p(z)=\widetilde{p}(z)/Z_p$에서 표집한다. 표집이 쉬운 **제안 분포**<span class="gloss">proposal distribution</span> $q(z)$와 $kq(z)\geqslant\widetilde{p}(z)\,(\forall z)$인 상수 $k$를 잡는다. $q$에서 $z_0$을 뽑고 $[0,kq(z_0)]$에서 $u_0$을 뽑아, $u_0>\widetilde{p}(z_0)$이면 거부한다. 승인된 표본은 $p(z)$를 따르며, 승인 확률은

$$
p(a)=\int\frac{\widetilde{p}(z)}{kq(z)}q(z)\,\mathrm{d}z=\frac{1}{k}\int\widetilde{p}(z)\,\mathrm{d}z
$$

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure11.4.png" style="width:22rem;" />
<div class="cap">

그림 9.2 · 거부 표집법. $q(z)$에서 뽑은 표본이 $\widetilde{p}(z)$와 $kq(z)$ 사이 음영 구간에 들면 거부한다. 남은 표본은 $p(z)$를 따른다.

</div>
</div>

::: tip 실습 · 거부 표집법
$kq(z)\geqslant\widetilde{p}(z)$인 가우시안 제안으로 정규화 안 된 양봉 목표에서 표집합니다. 승인율이 $\frac{1}{k}\int\widetilde{p}$에 맞고, 승인 표본의 평균이 참값과 일치함을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(1)
def ptil(z):                                            # 정규화 안 된 목표 p̃(z)
    return 0.6*np.exp(-(z+1)**2/(2*0.5**2)) + 0.4*np.exp(-(z-1.5)**2/(2*0.4**2))
sq = 1.5
def q(z): return np.exp(-z**2/(2*sq**2))/np.sqrt(2*np.pi*sq**2)
zg = np.linspace(-5, 5, 2001); dz = zg[1]-zg[0]
k = np.max(ptil(zg)/q(zg))*1.02                         # kq(z) ≥ p̃(z)
L = 200000; z0 = rng.normal(0, sq, L); u = rng.uniform(0, k*q(z0), L)
acc = u <= ptil(z0); zs = z0[acc]
Zp = np.sum(ptil(zg))*dz                                # ∫p̃ (수치 적분)
print(f"k={k:.3f}, 승인율={acc.mean():.3f} (이론 (1/k)∫p̃={Zp/k:.3f})")
truemean = np.sum(zg*ptil(zg))*dz/Zp
print(f"승인 표본 평균={zs.mean():.3f} (참 평균={truemean:.3f})")
```

</PyRunner>

### 9.1.3 중요도 표집법

- **중요도 표집법**<span class="gloss">importance sampling</span>은 표본을 뽑는 대신 기댓값을 직접 근사한다. 제안 분포 $q$에서 표본을 뽑고 **중요도 가중치**<span class="gloss">importance weight</span> $r_l=p(\mathbf{z}^{(l)})/q(\mathbf{z}^{(l)})$로 보정한다.

$$
\mathbb{E}[f]=\int f(\mathbf{z})\frac{p(\mathbf{z})}{q(\mathbf{z})}q(\mathbf{z})\,\mathrm{d}\mathbf{z}\simeq\frac{1}{L}\sum_{l=1}^L\frac{p(\mathbf{z}^{(l)})}{q(\mathbf{z}^{(l)})}f(\mathbf{z}^{(l)})
$$

  가중치는 잘못된 분포에서 표집해 생긴 편향을 바로잡는다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure11.8.png" style="width:22rem;" />
<div class="cap">

그림 9.3 · 중요도 표집법. 표본을 $q(z)$에서 뽑고, 각 항을 비율 $p(z^{(l)})/q(z^{(l)})$로 가중해 $\mathbb{E}_p[f]$를 근사한다.

</div>
</div>

::: tip 실습 · 중요도 표집법
$p=\mathcal{N}(0,1)$의 $\mathbb{E}[z^2]$·$\mathbb{E}[z^4]$을, 더 넓은 제안 $q=\mathcal{N}(0,1.5^2)$에서 뽑은 표본에 가중치 $p/q$를 곱해 추정하고 참값(1, 3)과 비교합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(2)
L = 200000; sq = 1.5; z = rng.normal(0, sq, L)          # 제안 q=N(0,1.5²)에서 표집
pz = np.exp(-z**2/2)/np.sqrt(2*np.pi)                    # 목표 p=N(0,1)
qz = np.exp(-z**2/(2*sq**2))/np.sqrt(2*np.pi*sq**2)
w = pz/qz                                                # 중요도 가중치
print(f"E_p[z²] 추정={np.mean(w*z**2):.4f} (참=1.0)")
print(f"E_p[z⁴] 추정={np.mean(w*z**4):.4f} (참=3.0)")
```

</PyRunner>

### 9.1.4 표집법과 EM 알고리즘

- EM의 E 단계를 해석적으로 풀기 어려우면 표집으로 근사한다. M 단계에서 최적화하는 완전 데이터 로그 가능도의 기댓값을 표본 합으로 근사한다.

$$
Q(\boldsymbol{\theta},\boldsymbol{\theta}^{\mathrm{old}})\simeq\frac{1}{L}\sum_{l=1}^L\ln p(\mathbf{Z}^{(l)},\mathbf{X}\mid\boldsymbol{\theta})
$$

  이를 **몬테 카를로 EM**<span class="gloss">Monte Carlo EM</span>이라 하고, 각 E 단계에서 표본 하나만 뽑으면 **확률적 EM**<span class="gloss">stochastic EM</span>이 된다. 완전 베이지안에서는 매개변수 사후 분포에서도 표집해야 하며, **데이터 증가**<span class="gloss">data augmentation</span>(IP) 알고리즘이 이를 다룬다.

::: info IP 알고리즘
1. **I 단계(대치)** — $p(\mathbf{Z}\mid\mathbf{X})=\int p(\mathbf{Z}\mid\boldsymbol{\theta},\mathbf{X})p(\boldsymbol{\theta}\mid\mathbf{X})\,\mathrm{d}\boldsymbol{\theta}$를 이용해, 현재 $p(\boldsymbol{\theta}\mid\mathbf{X})$에서 $\boldsymbol{\theta}^{(l)}$을 뽑고 이어서 $p(\mathbf{Z}\mid\boldsymbol{\theta}^{(l)},\mathbf{X})$에서 $\mathbf{Z}^{(l)}$을 뽑는다.

2. **P 단계(사후)** — 표본 $\{\mathbf{Z}^{(l)}\}$로 매개변수 사후 분포를 갱신한다.

$$
p(\boldsymbol{\theta}\mid\mathbf{X})\simeq\frac{1}{L}\sum_{l=1}^L p(\boldsymbol{\theta}\mid\mathbf{Z}^{(l)},\mathbf{X})
$$
:::

## 9.2 마르코프 연쇄 몬테 카를로

- 거부·중요도 표집은 고차원에서 한계가 있다. **마르코프 연쇄 몬테 카를로**<span class="gloss">Markov chain Monte Carlo; MCMC</span>는 현재 상태 $\mathbf{z}^{(\tau)}$에 의존하는 제안 분포 $q(\mathbf{z}\mid\mathbf{z}^{(\tau)})$로 후보를 뽑아 표본 열 $\mathbf{z}^{(1)},\mathbf{z}^{(2)},\ldots$가 마르코프 연쇄를 이루게 한다. **메트로폴리스**<span class="gloss">Metropolis</span> 알고리즘은 대칭 제안 분포를 가정하고 후보를 다음 확률로 승인한다.

$$
A(\mathbf{z}^{\star},\mathbf{z}^{(\tau)})=\min\Bigl(1,\frac{\widetilde{p}(\mathbf{z}^{\star})}{\widetilde{p}(\mathbf{z}^{(\tau)})}\Bigr)
$$

  $(0,1)$ 균등 난수 $u<A$이면 승인($\mathbf{z}^{(\tau+1)}=\mathbf{z}^{\star}$)하고, 거부하면 $\mathbf{z}^{(\tau+1)}=\mathbf{z}^{(\tau)}$로 둔다.

### 9.2.1 메트로폴리스–헤이스팅스 알고리즘

- **메트로폴리스–헤이스팅스**<span class="gloss">Metropolis–Hastings</span>는 비대칭 제안 분포로 일반화한다. 제안 분포 $q_k(\mathbf{z}\mid\mathbf{z}^{(\tau)})$의 비대칭성을 승인 확률에서 보정한다.

$$
A_k(\mathbf{z}^{\star},\mathbf{z}^{(\tau)})=\min\Bigl(1,\frac{\widetilde{p}(\mathbf{z}^{\star})\,q_k(\mathbf{z}^{(\tau)}\mid\mathbf{z}^{\star})}{\widetilde{p}(\mathbf{z}^{(\tau)})\,q_k(\mathbf{z}^{\star}\mid\mathbf{z}^{(\tau)})}\Bigr)
$$

::: tip 실습 · 메트로폴리스–헤이스팅스
양봉 목표 분포에 무작위 걷기 제안으로 MCMC를 돌려 표본 평균·분산이 참값에 수렴함을 확인합니다(초기 구간은 버림).
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(3)
def ptil(z): return 0.5*np.exp(-(z+2)**2/(2*0.5**2)) + 0.5*np.exp(-(z-2)**2/(2*0.5**2))
L = 100000; step = 1.5; z = 0.0; samples = np.empty(L); nacc = 0
for t in range(L):
    zstar = z + rng.normal(0, step)                     # 대칭 무작위 걷기 제안
    if rng.uniform() < min(1, ptil(zstar)/ptil(z)):     # 메트로폴리스 승인
        z = zstar; nacc += 1
    samples[t] = z
s = samples[2000:]                                      # 초기 구간(번인) 제거
print(f"승인율={nacc/L:.3f}")
print(f"표본 평균={s.mean():+.3f} (참 0), 표본 분산={s.var():.3f} (참 {0.25+4:.2f})")
```

</PyRunner>

## 9.3 기브스 표집법

- **기브스 표집법**<span class="gloss">Gibbs sampling</span>은 메트로폴리스–헤이스팅스의 특수 경우로, 각 변수를 나머지 변수에 대한 조건부 분포에서 차례로 갱신한다. 각 갱신의 승인 확률이 항상 $1$이라 거부가 없다.

::: info 기브스 표집법
1. $\{z_i:i=1,\ldots,M\}$을 초기화한다.

2. $\tau=1,\ldots,T$에 대해 각 변수를 조건부 분포에서 차례로 갱신한다.

$$
\begin{aligned}
z_1^{(\tau+1)}&\sim p(z_1\mid z_2^{(\tau)},\ldots,z_M^{(\tau)})\\
z_2^{(\tau+1)}&\sim p(z_2\mid z_1^{(\tau+1)},z_3^{(\tau)},\ldots,z_M^{(\tau)})\\
&\ \,\vdots\\
z_M^{(\tau+1)}&\sim p(z_M\mid z_1^{(\tau+1)},\ldots,z_{M-1}^{(\tau+1)})
\end{aligned}
$$
:::

::: tip 실습 · 기브스 표집법 (이변량 가우시안)
상관 $\rho$인 이변량 가우시안을 조건부 분포 $z_1\mid z_2\sim\mathcal{N}(\rho z_2,1-\rho^2)$로 번갈아 표집해, 표본 평균·공분산이 참값을 회복함을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(4)
rho = 0.8; L = 100000; z1 = z2 = 0.0; S = np.empty((L, 2))
for t in range(L):
    z1 = rng.normal(rho*z2, np.sqrt(1-rho**2))          # z1 | z2 ~ N(ρz2, 1-ρ²)
    z2 = rng.normal(rho*z1, np.sqrt(1-rho**2))          # z2 | z1 ~ N(ρz1, 1-ρ²)
    S[t] = [z1, z2]
S = S[1000:]                                            # 번인 제거
c = np.cov(S.T)
print("표본 평균  :", np.round(S.mean(0), 3).tolist(), "(참 [0, 0])")
print(f"표본 공분산: [[{c[0,0]:.3f}, {c[0,1]:.3f}], [{c[1,0]:.3f}, {c[1,1]:.3f}]]  (참 대각 1, 비대각 {rho})")
```

</PyRunner>

## 9.4 조각 표집법

- 메트로폴리스는 단계 크기에 민감하다. **조각 표집법**<span class="gloss">slice sampling</span>은 분포에 맞춰 단계 크기를 자동 조절한다. 변수 $z$에 보조 변수 $u$를 더해 결합 공간에서 균등 표집한다.

$$
\widehat{p}(z,u)=\begin{cases}1/Z_p & 0\leqslant u\leqslant\widetilde{p}(z)\\ 0 & \text{그 외}\end{cases}
$$

- $u$에 대해 주변화하면 $\int\widehat{p}(z,u)\,\mathrm{d}u=\widetilde{p}(z)/Z_p=p(z)$이므로, $\widehat{p}(z,u)$에서 표집해 $u$를 버리면 $p(z)$ 표본을 얻는다. $z$를 고정해 $0\leqslant u\leqslant\widetilde{p}(z)$에서 $u$를 뽑고, $u$를 고정해 조각 $\{z:\widetilde{p}(z)>u\}$에서 $z$를 균등 표집하는 것을 번갈아 한다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure11.13a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure11.13b.png" />
</div>
<div class="cap">

그림 9.4 · 조각 표집법. (a) $z^{(\tau)}$에서 $0\leqslant u\leqslant\widetilde{p}(z^{(\tau)})$의 $u$를 뽑아 조각(청색 실선)을 정한다. (b) $z^{(\tau)}$를 포함하는 $z_{\min}\leqslant z\leqslant z_{\max}$ 구간에서 새 표본을 뽑는다.

</div>
</div>

## 연습문제

::: info 문제 9.1
$(0,1)$ 균등 변수 $z$를 $y=h^{-1}(z)$로 변환할 때($h(y)=\int_{-\infty}^y p(\widehat{y})\,\mathrm{d}\widehat{y}$), $y$가 분포 $p(y)$를 가짐을 증명하라.
:::

::: details 풀이
$z$는 $(0,1)$에서 균등하므로 밀도가 $p(z)=1$이다. 변수 변환 공식에서

$$
p(y)=p(z)\left|\frac{\mathrm{d}z}{\mathrm{d}y}\right|=\left|\frac{\mathrm{d}z}{\mathrm{d}y}\right|
$$

$z=h(y)=\int_{-\infty}^y p(\widehat{y})\,\mathrm{d}\widehat{y}$이므로, 미적분학의 기본정리에 의해

$$
\frac{\mathrm{d}z}{\mathrm{d}y}=\frac{\mathrm{d}}{\mathrm{d}y}\int_{-\infty}^y p(\widehat{y})\,\mathrm{d}\widehat{y}=p(y)
$$

$p(y)\geqslant0$이므로 절댓값을 벗겨 $p(y)=p(y)$가 되어, 변환된 변수 $y$가 정확히 목표 분포 $p(y)$를 가진다. (누적 분포 $h$는 단조 증가라 역함수 $h^{-1}$이 잘 정의된다.) $\blacksquare$
:::

::: info 문제 9.2
$(0,1)$ 균등 변수 $z$에서 코시 분포 $p(y)=\dfrac{1}{\pi}\dfrac{1}{1+y^2}$가 되도록 하는 변환 $y=f(z)$를 찾아라.
:::

::: details 풀이
누적 분포 $h(y)$를 적분한다.

$$
z=h(y)=\int_{-\infty}^y\frac{1}{\pi}\frac{1}{1+\widehat{y}^2}\,\mathrm{d}\widehat{y}=\frac{1}{\pi}\Bigl[\arctan\widehat{y}\Bigr]_{-\infty}^y=\frac{1}{\pi}\Bigl(\arctan y+\frac{\pi}{2}\Bigr)=\frac{1}{2}+\frac{1}{\pi}\arctan y
$$

$y$에 대해 풀면

$$
\arctan y=\pi\Bigl(z-\frac{1}{2}\Bigr)\ \Longrightarrow\ y=f(z)=\tan\Bigl(\pi\Bigl(z-\frac{1}{2}\Bigr)\Bigr)=\tan\Bigl(\pi z-\frac{\pi}{2}\Bigr)
$$

즉 균등 변수 $z$를 $y=\tan(\pi(z-\tfrac12))$로 변환하면 코시 분포를 얻는다. $\blacksquare$
:::

::: info 문제 9.3
$y$가 균등 분포를 가질 때, $z=b\tan y+c$가 코시 분포 $q(z)=\dfrac{k}{1+(z-c)^2/b^2}$를 가짐을 증명하라.
:::

::: details 풀이
$y$가 균등 분포이므로 밀도 $p(y)$는 상수다. 변수 변환 $q(z)=p(y)\left|\dfrac{\mathrm{d}y}{\mathrm{d}z}\right|$를 쓴다. $z=b\tan y+c$에서 $y=\arctan\dfrac{z-c}{b}$이므로

$$
\frac{\mathrm{d}y}{\mathrm{d}z}=\frac{\mathrm{d}}{\mathrm{d}z}\arctan\frac{z-c}{b}=\frac{1/b}{1+\bigl(\frac{z-c}{b}\bigr)^2}=\frac{b}{b^2+(z-c)^2}
$$

따라서

$$
q(z)=p(y)\cdot\frac{b}{b^2+(z-c)^2}=\frac{p(y)/b}{1+(z-c)^2/b^2}=\frac{k}{1+(z-c)^2/b^2}
$$

여기서 $k=p(y)/b$는 상수다. 이는 위치 $c$·척도 $b$의 코시 분포이므로, $z=b\tan y+c$가 코시 분포를 따름이 증명된다. $\blacksquare$
:::
