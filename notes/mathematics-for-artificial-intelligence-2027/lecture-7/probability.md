# 확률

4–5주차의 확률을 정리한다. 확률의 기본 개념과 법칙에서 시작해 조건부 확률·베이즈 정리, 이산/연속 확률 분포, 기댓값·분산, 그리고 중심 극한 정리로 마무리한다.

## 확률의 기본 개념

- 확률<span class="gloss">probability</span> $P$는 어떤 일이 일어날 가능성을 $[0,1]$ 구간의 수치로 나타낸 것이다($P\in[0,1]$). 일어날 수 없으면 $0$, 반드시 일어나면 $1$이다.
- 표본 공간<span class="gloss">sample space</span> $\Omega$는 한 사건<span class="gloss">event</span>의 모든 가능한 결과<span class="gloss">outcome</span>를 모은 이산 집합 또는 연속 구간이다. 개별 사건은 $\Omega$의 부분집합, 즉 하나의 표본<span class="gloss">sample</span>에 해당한다. 예를 들어 동전 던지기의 표본 공간은 $\Omega=\{\text{앞면},\text{뒷면}\}$이다.
- 어떤 사건이 일어날 가능성을 나타내는 값을 가능도<span class="gloss">likelihood</span>(우도)라 한다. 확률이 사건의 발생 가능성을 나타낸다면, 가능도는 관측된 사건이 주어졌을 때 그 사건이 발생했을 가능성을 나타내는 함수이다.
- 표본 공간에서 특정 확률로 값을 취하는 변수를 확률 변수<span class="gloss">random variable</span>라 한다. 이산 표본 공간이면 이산 확률 변수<span class="gloss">discrete random variable</span>(대문자 표기), 연속이면 연속 확률 변수<span class="gloss">continuous random variable</span>(소문자 표기)이다.

$$
P(X=\text{앞면})=P(X=\text{뒷면})=0.5\quad(\text{공정한 동전})
$$

## 확률 법칙

- 표본 공간의 모든 확률의 합은 $1$이므로, 임의의 사건 $A$에 대해 $0\leq P(A)\leq 1$이고 $\sum_i P(A_i)=1$이다. 사건 $A$의 여사건<span class="gloss">complementary event</span> 확률은 다음과 같다.

$$
P(\bar{A})\equiv 1-P(A)
$$

- 두 사건이 동시에 일어날 수 없으면 상호 배반적<span class="gloss">mutually exclusive</span>, 한 사건이 다른 사건의 발생 여부에 영향을 주지 않으면 독립적<span class="gloss">independent</span>이라 한다.
- 합의 법칙<span class="gloss">sum rule</span>은 "$A$ 또는 $B$"의 확률, 곱의 법칙<span class="gloss">product rule</span>은 "$A$ 그리고 $B$"의 확률을 다룬다.

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B),\qquad \text{(상호 배반 시)}\ P(A\cup B)=P(A)+P(B)
$$

$$
\text{(독립 시)}\ P(A\cap B)=P(A)\cdot P(B)
$$

- 사건 $A$의 발생을 조건으로 한 $B$의 확률을 조건부 확률<span class="gloss">conditional probability</span> $P(B\mid A)$라 한다. 두 사건이 종속<span class="gloss">dependent</span>일 때 곱의 법칙은 다음과 같으며, 일반적으로 $P(A\mid B)\neq P(B\mid A)$이다.

$$
P(A, B) = P(A\mid B)\cdot P(B)
$$

- 표본 공간을 서로소<span class="gloss">disjoint</span>인 영역 $\{B_i\}$로 나눈 것을 분할<span class="gloss">partition</span>이라 한다. 이때 $A$의 전체 확률<span class="gloss">total probability</span>은 다음과 같다.

$$
P(A)=\sum_i P(A\mid B_i)\cdot P(B_i)
$$

::: info 생일 역설<span class="gloss">birthday paradox</span>
한 해를 $365$일로 가정하면 두 사람의 생일이 다를 확률은 $\tfrac{364}{365}\approx 0.9973$이다. $n$번의 비교에서 모두 생일이 다를 확률은 $\left(\tfrac{364}{365}\right)^n$이며, 이 값이 $0.5$ 미만이 되려면 $n=253$번의 비교가 필요하다. $m$명 중 $2$명을 택하는 조합<span class="gloss">combination</span> $\binom{m}{2}=\tfrac{m!}{2!(m-2)!}$이 $253$ 이상이 되는 최소 $m$은 $23$이다. 즉, **단 23명만 모여도** 생일이 같은 쌍이 있을 확률이 50%를 넘는다.
:::

## 결합 확률과 주변 확률

- 결합 확률<span class="gloss">joint probability</span> $P(X=x, Y=y)$는 여러 조건이 동시에 참일 확률이고, 주변 확률<span class="gloss">marginal probability</span>은 다른 변수의 값과 무관하게 한 부분집합에 대해서만 계산한 확률이다. 주변 확률은 다른 변수의 모든 값에 대해 합산해 구한다.
- 예를 들어 $1{,}000$명의 남녀별 색맹 여부를 정리한 결합 확률표<span class="gloss">joint probability table</span>에서 $P(Y=\text{색맹})=P(\text{남},\text{색맹})+P(\text{여},\text{색맹})=0.042+0.003=0.045$처럼 주변 확률을 구한다.
- 곱의 법칙을 일반화한 것을 확률의 연쇄법칙<span class="gloss">chain rule for probability</span>이라 한다.

$$
P(X_n, X_{n-1},\ldots,X_1)=\prod_{i=1}^{n} P(X_i \mid X_1, X_2, \ldots, X_{i-1})
$$

## 베이즈 정리

- 결합 확률의 대칭성 $P(A,B)=P(B,A)$과 $P(A,B)\equiv P(B\mid A)P(A)$로부터 베이즈 정리<span class="gloss">Bayes' theorem</span>를 얻는다.

::: info 베이즈 정리
$$
P(B\mid A)=\frac{P(A\mid B)\cdot P(B)}{P(A)}
$$

사후 확률<span class="gloss">posterior probability</span> $P(B\mid A)$는 가능도 $P(A\mid B)$와 사전 확률<span class="gloss">prior probability</span> $P(B)$의 곱을 주변 확률 $P(A)$로 정규화<span class="gloss">normalization</span>한 결과이다.
:::

- **암 진단 예제.** 무작위로 뽑은 40대 여성의 유방암 보유 확률 $P(bc+)=0.008$, 유방암이 있을 때 검사 양성 확률 $P(+\mid bc+)=0.9$, 없을 때 양성 확률 $P(+\mid bc-)=0.07$이 주어진다. 주변 확률과 사후 확률은 다음과 같다.

$$
P(+)=0.9\cdot 0.008 + 0.07\cdot 0.992 = 0.07664,\qquad P(bc+\mid +)=\frac{0.9\cdot 0.008}{0.07664}\approx 0.094
$$

  - 다른 병원에서 재검사도 양성이면, 앞의 사후 확률을 새로운 사전 확률로 삼아 갱신한다. $P(+)=0.9\cdot 0.094+0.07\cdot 0.906=0.14802$이고 $P(bc+\mid +)\approx 0.5715$로, **증거가 쌓일수록 믿음의 정도가 커진다.**
- 베이즈 정리는 단순 베이즈 분류기<span class="gloss">naïve Bayes classifier</span>의 기반이다. 분류명<span class="gloss">class label</span> $y$와 특징 벡터<span class="gloss">feature vector</span> $\mathbf{x}$에 대해, 주변 확률을 무시하면 다음 비례식이 성립하며, 모든 특징이 독립이라 가정해 결합 확률을 개별 확률의 곱으로 근사한다.

$$
P(y\mid\mathbf{x})\propto P(\mathbf{x}\mid y)\cdot P(y),\qquad P(\mathbf{x})=\prod_{i=0}^{n-1}P(x_i)\ (\text{독립 가정})
$$

<PyRunner>

```python
# 베이즈 정리로 유방암 진단 확률을 반복 갱신
p_bc = 0.008           # 사전확률 P(bc+)
p_pos_given_bc = 0.9   # P(+ | bc+)
p_pos_given_no = 0.07  # P(+ | bc-)

def update(prior):
    marg = p_pos_given_bc*prior + p_pos_given_no*(1 - prior)  # 주변확률 P(+)
    return p_pos_given_bc*prior / marg                         # 사후확률 P(bc+ | +)

post1 = update(p_bc)     # 1차 양성 결과 반영
post2 = update(post1)    # 2차 양성 결과 반영

print(f"사전확률           P(bc+)     = {p_bc:.4f}")
print(f"1차 양성 후 사후확률 P(bc+|+) = {post1:.4f}")
print(f"2차 양성 후 사후확률 P(bc+|+) = {post2:.4f}")
```

</PyRunner>

## 확률 분포

- 확률 분포<span class="gloss">probability distribution</span>는 미리 정의된 확률에 따라 무작위로 값을 생성하는 함수이다. 주사위처럼 각 값이 $1/6$의 균등한 확률로 나오는 분포를 균등 분포<span class="gloss">uniform distribution</span>라 한다.
- **이산 확률 분포**<span class="gloss">discrete probability distribution</span>는 확률 질량 함수<span class="gloss">probability mass function</span>로 규정된다. 대표적인 이산 분포는 다음과 같다.

$$
\text{이항 분포}\ P(X=k)=\binom{n}{k}p^k(1-p)^{n-k},\qquad \text{푸아송 분포}\ P(k)=\frac{\lambda^k e^{-\lambda}}{k!}
$$

  - 이항 분포<span class="gloss">binomial distribution</span>는 확률 $p$인 사건을 $n$번 시행<span class="gloss">trial</span>할 때 $k$번 발생할 확률이다. $n=1$인 특수 사례<span class="gloss">special case</span>가 베르누이 분포<span class="gloss">Bernoulli distribution</span>이다. 푸아송 분포<span class="gloss">Poisson distribution</span>는 평균 발생 횟수 $\lambda$만 알 때 유용하다.
- **연속 확률 분포**<span class="gloss">continuous probability distribution</span>에서는 특정 한 값이 선택될 확률이 $0$이며, 확률은 구간에 대한 적분<span class="gloss">integration</span>으로 계산된다. 확률 밀도 함수<span class="gloss">probability density function</span>가 이를 규정한다. 대표적인 연속 분포는 다음과 같다.

$$
\text{정규 분포}\ p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-(x-\mu)^2/2\sigma^2},\qquad
\text{감마 분포}\ p(x)=x^{k-1}\frac{e^{-x/\theta}}{\theta^k\Gamma(k)}
$$

$$
\text{베타 분포}\ p(x)=\frac{x^{a-1}(1-x)^{b-1}}{\mathrm{B}(a,b)},\qquad \mathrm{B}(a,b)=\int_0^1 t^{a-1}(1-t)^{b-1}\,\mathrm{d}t
$$

  - 정규 분포<span class="gloss">normal distribution</span>(가우스 분포<span class="gloss">Gaussian distribution</span>, 종 곡선<span class="gloss">bell curve</span>)는 평균<span class="gloss">mean</span> $\mu$와 표준편차<span class="gloss">standard deviation</span> $\sigma$로 정해지는 대칭 곡선이다. 감마 분포<span class="gloss">gamma distribution</span>는 형태<span class="gloss">shape</span> $k$와 규모<span class="gloss">scale</span> $\theta$, 베타 분포<span class="gloss">beta distribution</span>는 $a,b$로 다양한 모양을 만든다.

<PyRunner>

```python
import numpy as np
from math import comb

# 이항 분포 B(10, 0.5) 의 확률 질량 함수
n, p = 10, 0.5
pmf = [comb(n, k) * p**k * (1-p)**(n-k) for k in range(n+1)]
print("이항분포 B(10, 0.5) pmf:")
for k in range(n+1):
    print(f"  P(X={k:2d}) = {pmf[k]:.4f}")
print("확률의 합 =", round(sum(pmf), 6))

# 시뮬레이션으로 이론 평균(np) 확인
rng = np.random.default_rng(0)
s = rng.binomial(n, p, size=100000)
print(f"표본평균 = {s.mean():.4f}  (이론 평균 np = {n*p})")
```

</PyRunner>

<PyRunner>

```python
import numpy as np
from math import exp, factorial

# 푸아송 분포 (λ=3) 의 확률 질량 함수
lam = 3.0
pmf = [lam**k * exp(-lam) / factorial(k) for k in range(10)]
print("푸아송 분포 (λ=3) P(k):")
for k in range(10):
    print(f"  P({k}) = {pmf[k]:.4f}")

# 푸아송 분포는 평균과 분산이 모두 λ 이다
rng = np.random.default_rng(1)
s = rng.poisson(lam, size=100000)
print(f"\n표본평균 = {s.mean():.3f},  표본분산 = {s.var():.3f}  (둘 다 λ=3 에 근접)")
```

</PyRunner>

## 기댓값 · 분산 · 극한 정리

- 확률 변수 $X$의 기댓값<span class="gloss">expectation</span>과 분산<span class="gloss">variance</span>은 다음과 같이 정의된다(이산의 경우 합, 연속의 경우 적분).

$$
\mathbb{E}[X]=\sum_x x\,p(x)\ \text{ 또는 }\int x\,p(x)\,\mathrm{d}x,\qquad \operatorname{var}[X]=\mathbb{E}[X^2]-\mathbb{E}[X]^2
$$

  - 예를 들어 이항 분포는 $\mathbb{E}[X]=np$, $\operatorname{var}[X]=np(1-p)$이고, 푸아송 분포는 $\mathbb{E}[X]=\operatorname{var}[X]=\lambda$이다.
- 중심 극한 정리<span class="gloss">central limit theorem</span>는, 원래 분포의 형태와 무관하게 **표본 평균들이 이루는 분포가 점점 정규 분포에 가까워진다**는 정리이다. 이는 표본 크기가 클수록 표본 평균이 모평균에 가까워진다는 큰 수의 법칙<span class="gloss">law of large numbers</span>과는 다르다. 큰 수의 법칙은 하나의 표본 평균과 모평균의 관계를, 중심 극한 정리는 여러 표본 평균들의 분포를 말한다.

<PyRunner>

```python
import numpy as np

# 중심 극한 정리: 베르누이(p=0.5) 표본의 평균을 여러 번 계산하면 정규분포에 근접
rng = np.random.default_rng(2)
N, reps = 30, 20000
means = rng.binomial(1, 0.5, size=(reps, N)).mean(axis=1)   # 각 행이 표본평균 하나

print(f"표본평균들의 평균     = {means.mean():.4f}  (모평균 0.5)")
print(f"표본평균들의 표준편차 = {means.std():.4f}")
print(f"이론적 표준오차 sqrt(pq/N) = {np.sqrt(0.25/N):.4f}")

# 정규분포라면 약 68.3% 가 ±1σ 안에 든다
lo, hi = means.mean() - means.std(), means.mean() + means.std()
frac = np.mean((means > lo) & (means < hi))
print(f"±1σ 안에 든 비율 = {frac:.3f}  (정규분포면 ≈ 0.683)")
```

</PyRunner>
