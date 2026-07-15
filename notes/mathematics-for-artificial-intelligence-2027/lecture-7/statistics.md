# 통계

6주차의 통계를 정리한다. 데이터의 종류에서 시작해 요약 통계량, 분위수와 상자 그림, 상관관계, 그리고 가설 검정을 다룬다.

## 데이터의 종류

- 데이터는 값들 사이의 관계에 따라 네 가지로 나뉜다.

::: info 네 가지 데이터 척도
- 명목형 데이터<span class="gloss">nominal data</span>(범주형<span class="gloss">categorical data</span>): 순서 관계가 없음(예: 눈 색깔). 신경망에 쓸 때는 원핫 부호화<span class="gloss">one-hot encoding</span>로 변환한다.
- 순서형 데이터<span class="gloss">ordinal data</span>: 순서는 있으나 값들의 차이에 수학적 의미가 없음(예: 설문의 "매우 그렇다").
- 구간 데이터<span class="gloss">interval data</span>: 차이에 의미가 있으나 절대적 영점이 없음(예: 섭씨·화씨 온도).
- 비율 데이터<span class="gloss">ratio data</span>: 차이에 의미가 있고 진정한 영점<span class="gloss">zero point</span>이 존재함(예: 키, 나이, 절대온도).
:::

## 요약 통계량

- 데이터셋을 효과적으로 파악하는 방법은 요약 통계량<span class="gloss">summary statistic</span>을 구하는 것이다. 가장 대표적인 것은 산술 평균<span class="gloss">arithmetic mean</span>으로, 가중치를 부여하면 가중<span class="gloss">weighted</span> 평균이 된다.

$$
\bar{x}=\frac{1}{n}\sum_{i=0}^{n-1}x_i,\qquad \bar{x}=\sum_{i=0}^{n-1}w_i x_i\ \left(\sum_i w_i=1\right)
$$

- 기하 평균<span class="gloss">geometric mean</span>과 조화 평균<span class="gloss">harmonic mean</span>도 자주 쓰인다.

$$
\bar{x}_g=\sqrt[n]{\prod_{i=0}^{n-1}x_i},\qquad \bar{x}_h=\left(\frac{1}{n}\sum_{i=0}^{n-1}\frac{1}{x_i}\right)^{-1}
$$

  - 기계학습의 F1 점수<span class="gloss">F1 score</span>는 재현율<span class="gloss">recall</span>과 정밀도<span class="gloss">precision</span>의 조화 평균이다.

$$
\mathrm{F1}=\left(\frac{1}{2}\left(\frac{1}{\text{recall}}+\frac{1}{\text{precision}}\right)\right)^{-1},\quad \text{recall}=\frac{\text{TP}}{\text{TP}+\text{FN}},\quad \text{precision}=\frac{\text{TP}}{\text{TP}+\text{FP}}
$$

- 중앙값<span class="gloss">median</span>은 정렬된 데이터의 가운데 값이다(원소가 짝수 개이면 가운데 두 값의 평균). 순서가 중요한 중앙값과 값의 합이 반영되는 평균은 서로 다른 정보를 준다.
- 데이터의 변동<span class="gloss">variation</span>을 재는 방법으로 범위<span class="gloss">range</span>(최댓값 − 최솟값), 평균 편차<span class="gloss">mean deviation</span>, 분산이 있다.

$$
\text{MD}=\frac{1}{n}\sum_{i=0}^{n-1}|x_i-\bar{x}|
$$

- 절댓값 대신 제곱을 쓰는 분산이 더 흔하다. 편향 표본 분산<span class="gloss">biased sample variance</span>과 비편향 표본 분산<span class="gloss">unbiased sample variance</span>은 다음과 같다.

$$
s_n^2=\frac{1}{n}\sum_{i=0}^{n-1}(x_i-\bar{x})^2,\qquad s^2=\frac{1}{n-1}\sum_{i=0}^{n-1}(x_i-\bar{x})^2
$$

  - 분모에 $n$ 대신 $n-1$을 쓰는 것을 베셀 보정<span class="gloss">Bessel's correction</span>이라 하며, 표본 분산의 편향성을 낮춘다. 모평균 $\mu$와 분산 $\sigma^2$를 모르므로 표본으로 추정하는데, 데이터가 충분히 크면 두 분산의 차이는 거의 없다.
- 분산의 제곱근이 표준편차<span class="gloss">standard deviation</span>(모집단 $\sigma$, 표본 $s$)이고, 표본 평균들의 표준편차를 평균 표준오차<span class="gloss">standard error of the mean</span>라 한다.

$$
\text{SE}=\frac{s}{\sqrt{n}}
$$

<PyRunner>

```python
import numpy as np

x = np.array([37, 44, 55, 63, 65, 69, 71, 73, 74, 87], dtype=float)

print("산술평균 =", x.mean())
print("중앙값   =", np.median(x))

gmean = np.exp(np.mean(np.log(x)))   # 기하평균
hmean = 1 / np.mean(1 / x)           # 조화평균
print(f"기하평균 = {gmean:.3f},  조화평균 = {hmean:.3f}")

print("편향 표본분산  s_n^2 =", round(x.var(ddof=0), 3))
print("비편향 표본분산 s^2  =", round(x.var(ddof=1), 3))
print("표준편차 =", round(x.std(ddof=1), 3),
      " 표준오차 =", round(x.std(ddof=1) / np.sqrt(len(x)), 3))
```

</PyRunner>

## 분위수와 상자 그림

- 분위수<span class="gloss">quantile</span>는 데이터를 고정된 크기의 그룹으로 나누는 값이다. 중앙값은 데이터를 반으로 나누므로 이분위수<span class="gloss">2-quantile</span>, 즉 50 백분위수<span class="gloss">50th percentile</span>이다.
- 데이터를 넷으로 나누는 사분위<span class="gloss">quartile</span>가 흔히 쓰인다. Q1(25%), Q2(50%, 중앙값), Q3(75%)로 나누며, 상자 그림<span class="gloss">box plot</span>으로 시각화한다.
- 상자 그림에는 Q1·Q2·Q3가 표기되며, Q3와 Q1의 차이를 사분범위<span class="gloss">interquartile range; IQR</span>라 한다. 상자에서 뻗은 선을 수염<span class="gloss">whisker</span>이라 하고, 그 바깥의 값을 잠재적 이상치<span class="gloss">possible outlier</span>라 한다.

$$
\text{IQR}=Q_3-Q_1
$$

## 상관관계

- 한 특징이 변할 때 다른 특징이 함께 변하는 연관 관계를 상관관계<span class="gloss">correlation</span>라 한다. 기계학습에서 높은 상관관계는 새로운 정보를 주지 않으므로, 특징 선택<span class="gloss">feature selection</span>으로 이를 줄인다.
- 피어슨 상관계수<span class="gloss">Pearson correlation coefficient</span> $r\in[-1,1]$은 두 특징의 **선형**<span class="gloss">linear</span> 상관관계의 강도이다. 기댓값<span class="gloss">expectation value</span> $E(\cdot)$로 다음과 같이 정의된다.

$$
r = \frac{E(\mathbf{v}\mathbf{w})-E(\mathbf{v})E(\mathbf{w})}{\sqrt{E(\mathbf{v}^2)-E(\mathbf{v})^2}\,\sqrt{E(\mathbf{w}^2)-E(\mathbf{w})^2}}
$$

- 스피어먼 상관계수<span class="gloss">Spearman correlation coefficient</span> $\rho\in[-1,1]$은 값 자체가 아닌 순위<span class="gloss">rank</span>에 기초해 **단조적** 연관 관계를 찾는다. 피어슨 상관은 선형 관계만, 스피어먼 상관은 비선형(단조) 관계도 반영한다.

$$
\rho=1-\left(\frac{6}{n(n^2-1)}\right)\sum_{i=0}^{n-1}d_i^2,\qquad d=\operatorname{rank}(\mathbf{v})-\operatorname{rank}(\mathbf{w})
$$

<PyRunner>

```python
import numpy as np

v = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)
w = np.array([2, 1, 4, 3, 7, 5, 8], dtype=float)

def pearson(a, b):   # 기댓값 정의를 그대로 구현
    return ((a*b).mean() - a.mean()*b.mean()) / (a.std()*b.std())

def rank(a):
    order = a.argsort()
    r = np.empty(len(a))
    r[order] = np.arange(len(a))
    return r

def spearman(a, b):
    d = rank(a) - rank(b)
    n = len(a)
    return 1 - 6*np.sum(d**2) / (n*(n**2 - 1))

print(f"피어슨 r   = {pearson(v, w):.4f}")
print(f"스피어먼 ρ = {spearman(v, w):.4f}")
print("numpy 검증 (피어슨) =", round(np.corrcoef(v, w)[0, 1], 4))
```

</PyRunner>

## 가설 검정

- 가설 검정<span class="gloss">hypothesis testing</span>은 두 그룹 간의 차이를 통계적으로 분석하는 도구이다. 두 종류의 가설을 사용한다.

::: info 귀무가설과 대안가설
- 귀무가설<span class="gloss">null hypothesis</span> $H_0$: 두 그룹이 같은 모집단에서 나왔다(같은 평균)고 가정하는 가설.
- 대안가설<span class="gloss">alternative hypothesis</span> $H_a$: 두 그룹이 다른 모집단에서 나왔다는, 우리가 보이려는 가설. $H_0$가 기각되면 암묵적으로 $H_a$가 승인된다.
:::

- 검정은 두 분포가 다른지만 보는 양꼬리<span class="gloss">two-tailed</span> 검정과 한쪽이 크거나 작은지 보는 한꼬리<span class="gloss">one-tailed</span> 검정으로 나뉜다. 대부분 데이터의 독립 동일 분포<span class="gloss">independent and identically distributed; i.i.d.</span>를 가정한다.
- $t$-검정<span class="gloss">$t$-test</span>은 검정 통계량 $t$를 $t$-분포<span class="gloss">$t$-distribution</span>와 비교해 $p$값을 구하는 모수적<span class="gloss">parametric</span> 검정으로, 데이터가 정규분포를 따른다고 가정한다. 두 표본의 분산이 같다고 가정하지 않는 웰치 $t$-검정<span class="gloss">Welch's $t$-test</span>의 통계량과 자유도<span class="gloss">degree of freedom</span>는 다음과 같다.

$$
t=\frac{\bar{x}_1-\bar{x}_2}{\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}},\qquad
df=\frac{\left(\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2/n_1)^2}{n_1-1}+\frac{(s_2^2/n_2)^2}{n_2-1}}
$$

- $p$값은 $H_0$가 참일 때 관측된 차이가 나타날 확률로, 미리 정한 값(주로 $0.05$)보다 작으면 $H_0$를 기각하고 통계적으로 유의미한<span class="gloss">statistically significant</span> 차이가 있다고 한다.
- 신뢰구간<span class="gloss">confidence interval</span>은 반복된 표본에서 참 모평균 차이가 일정 비율로 속하는 구간이다. 신뢰수준 $\alpha$와 임계값<span class="gloss">critical value</span> $t_{1-\alpha/2,df}$로 다음과 같이 정의된다.

$$
CI_\alpha=(\bar{x}_1-\bar{x}_2)\pm t_{1-\alpha/2,df}\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}
$$

- $p$값이 유의미해도 현실적 의미가 크지 않을 수 있으므로, 효과 크기<span class="gloss">effect size</span>를 함께 본다. 웰치 $t$-검정에서 코헨 $d$<span class="gloss">Cohen's $d$</span>는 다음과 같다.

$$
d=\frac{\bar{x}_2-\bar{x}_1}{\sqrt{\frac{1}{2}(s_1^2 + s_2^2)}}
$$

- 데이터가 정규분포를 따르지 않으면 분포에 아무 가정도 하지 않는 비모수적<span class="gloss">nonparametric</span> 검정을 쓴다. 대표적으로 윌콕슨 순위합 검정<span class="gloss">Wilcoxon's rank-sum test</span>이라고도 하는 맨-휘트니 $U$-검정<span class="gloss">Mann-Whitney's $U$-test</span>이 있으며, 값의 순위를 이용해 통계량 $U$를 계산한다.

$$
U= n_1 n_2 + \min\left(\frac{n_1(n_1-1)}{2} - R_1,\ \frac{n_2(n_2-1)}{2} - R_2\right)
$$

  - $t$-검정의 귀무가설은 "두 그룹의 평균 차이가 $0$"인 반면, 맨-휘트니 $U$-검정의 귀무가설은 "그룹 1에서 뽑은 값이 그룹 2에서 뽑은 값보다 클 확률이 $0.5$"이다.

<PyRunner>

```python
import numpy as np

rng = np.random.default_rng(0)
g1 = rng.normal(10.0, 2.0, size=40)   # 평균 10
g2 = rng.normal(11.5, 3.0, size=50)   # 평균 11.5

# 사분위수와 IQR
q1, q2, q3 = np.percentile(g1, [25, 50, 75])
print(f"g1  Q1={q1:.2f}, 중앙값={q2:.2f}, Q3={q3:.2f}, IQR={q3-q1:.2f}")

# 웰치 t-검정 통계량 (분산이 같다고 가정하지 않음)
def welch_t(a, b):
    return (a.mean() - b.mean()) / np.sqrt(a.var(ddof=1)/len(a) + b.var(ddof=1)/len(b))

t = welch_t(g1, g2)
# 코헨 d (효과 크기)
d = (g2.mean() - g1.mean()) / np.sqrt(0.5*(g1.var(ddof=1) + g2.var(ddof=1)))
print(f"웰치 t = {t:.4f},  코헨 d = {d:.4f}")
```

</PyRunner>
