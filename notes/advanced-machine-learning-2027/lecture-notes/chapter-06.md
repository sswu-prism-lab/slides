# 6 · 그래프 모델

> 아무리 복잡한 확률적 추론이나 학습 알고리즘이라도 결국은 확률의 합의 법칙과 곱의 법칙을 반복 적용한 것과 같다. 확률적 모델은 대수적으로 공식화하고 풀 수 있지만, 이를 도식으로 표현하면 많은 장점을 가진다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/photos/sec06.png" style="max-width:34rem;" />
</div>

## 6.1 베이지안 네트워크

- **확률적 그래프 모델**<span class="gloss">probabilistic graphical model</span>은 모델의 구조를 시각화하고, 조건부 독립 같은 성질을 그래프에서 읽어내며, 학습·추론의 복잡한 계산을 그래프 조작으로 표현하게 해 준다. 그래프는 **노드**<span class="gloss">node</span>(확률 변수)와 **링크**<span class="gloss">link</span>(변수 간 확률적 관계)로 이루어진다. **베이지안 네트워크**<span class="gloss">Bayesian network</span>는 링크가 방향(화살표)을 갖는 **방향성 그래프 모델**<span class="gloss">directed graphical model</span>이다.

- 결합 분포 $p(a,b,c)$를 곱의 법칙으로 분해하면 $p(a,b,c)=p(c\mid a,b)p(b\mid a)p(a)$이고, 각 조건부 분포마다 조건절 변수 노드에서 화살표를 그린다. $a\to b$이면 $a$를 $b$의 **부모**<span class="gloss">parent</span>, $b$를 $a$의 **자식**<span class="gloss">child</span>이라 한다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.1.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.2.png" />
</div>
<div class="cap">그림 8.1·8.2 · (왼쪽) 세 변수 $a,b,c$의 방향성 그래프. (오른쪽) 완전 연결이 아닌 방향성 비순환 그래프 $x_1,\ldots,x_7$의 예.</div>
</div>

- $K$개 노드의 결합 분포는 각 노드의 조건부 분포 곱으로 인수분해된다.

$$
p(\mathbf{x})=\prod_{k=1}^K p(x_k\mid\mathrm{pa}_k) \tag{8.5}
$$

  $\mathrm{pa}_k$는 $x_k$의 부모 노드들이다. 우리가 다루는 그래프는 **방향성 비순환 그래프**<span class="gloss">directed acyclic graph; DAG</span>로, 링크를 방향대로 따라가 원래 노드로 돌아오는 순환이 없어야 한다. 각 조건부 분포가 정규화되어 있으면 (8.5)의 곱도 항상 정규화된다.

### 6.1.1 다항 근사 예시

- 베이지안 다항 회귀는 계수 $\mathbf{w}$와 관측값 $\mathsf{t}$를 확률 변수로 갖는다. 결합 분포는 $p(\mathsf{t},\mathbf{w})=p(\mathbf{w})\prod_{n=1}^N p(t_n\mid\mathbf{w})$이다. $t_1,\ldots,t_N$을 일일이 그리는 대신 대표 노드 하나를 **판**<span class="gloss">plate</span> 상자로 둘러싸고 개수 $N$을 라벨로 표시한다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.3.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.4.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.5.png" />
</div>
<div class="cap">그림 8.3~8.5 · 다항 회귀의 결합 분포. (왼쪽) 명시적 표현, (가운데) 판 표기, (오른쪽) 결정 매개변수(작은 점)를 추가한 표현.</div>
</div>

- 결정 매개변수($\mathbf{x}$, $\alpha$, $\sigma^2$)를 명시하면 $p(\mathsf{t},\mathbf{w}\mid\mathsf{x},\alpha,\sigma^2)=p(\mathbf{w}\mid\alpha)\prod_n p(t_n\mid\mathbf{w},x_n,\sigma^2)$이다. **확률 변수**는 열린 원, **결정 변수**는 작은 점, **관측 변수**<span class="gloss">observed variable</span>는 음영으로 표기하며, 관측되지 않은 $\mathbf{w}$는 **잠재 변수**<span class="gloss">latent variable</span>다. 새 입력 $\widehat{x}$에 대한 예측은 $\mathbf{w}$를 적분해 얻는다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.6.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.7.png" />
</div>
<div class="cap">그림 8.6·8.7 · (왼쪽) 관측 변수 $\{t_n\}$에 음영을 더한 모델. (오른쪽) 새 입력 $\widehat{x}$와 예측 $\widehat{t}$를 추가한 모델.</div>
</div>

### 6.1.2 이산 변수

- $K$개 상태의 이산 변수 하나는 $p(\mathbf{x}\mid\boldsymbol{\mu})=\prod_k\mu_k^{x_k}$($\sum_k\mu_k=1$)로, $K-1$개의 매개변수가 필요하다. 변수가 $M$개인 임의의 결합 분포는 $K^M-1$개의 매개변수가 필요해 기하급수적으로 늘지만, 링크를 제거해 독립성을 도입하면 크게 줄어든다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.9a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.9b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.10.png" />
</div>
<div class="cap">그림 8.9·8.10 · (왼쪽·가운데) 두 이산 변수의 완전 연결($K^2-1$)과 링크 제거($2(K-1)$). (오른쪽) $M$개 노드의 사슬은 $K-1+(M-1)K(K-1)$개로 $M$에 선형이다.</div>
</div>

- 매개변수 **공유**<span class="gloss">sharing</span>(매듭<span class="gloss">tying</span>)로 사슬의 모든 조건부 분포가 같은 $K(K-1)$개를 쓰게 하면 전체 $K^2-1$개로 줄어든다. 디리클레 사전 분포를 도입하면 이산 그래프를 베이지안 모델로 전환할 수 있다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.11.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.12.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.13.png" />
</div>
<div class="cap">그림 8.11~8.13 · (왼쪽) 디리클레 사전 분포 추가, (가운데) 매개변수 매듭, (오른쪽) $M$개 부모와 단일 자식 $y$.</div>
</div>

- 조건부 분포 테이블 대신 매개변수화된 모델을 쓰면 기하급수적 증가를 막을 수 있다. $M$개 부모에 대한 자식의 조건부 분포를 로지스틱 시그모이드로 두면 매개변수가 $M$에 선형이다.

$$
p(y=1\mid x_1,\ldots,x_M)=\sigma\Bigl(w_0+\sum_{i=1}^M w_i x_i\Bigr)=\sigma(\mathbf{w}^{\top}\mathbf{x})
$$

::: tip 실습 · 매개변수 수 증가 비교
$K$개 상태의 $M$개 이산 변수에서, 완전 연결($K^M-1$)·사슬($K-1+(M-1)K(K-1)$)·완전 독립($M(K-1)$)의 매개변수 수를 비교합니다. 완전 연결만 $M$에 대해 기하급수적으로 폭발합니다.
:::

<PyRunner>

```python
K = 3
print("  M   완전연결(K^M-1)   사슬(K-1+(M-1)K(K-1))   독립(M(K-1))")
for M in [1, 2, 4, 6, 8, 10]:
    full = K**M - 1
    chain = K-1 + (M-1)*K*(K-1)
    indep = M*(K-1)
    print(f" {M:2d}   {full:12d}   {chain:18d}   {indep:8d}")
```

</PyRunner>

### 6.1.3 선형 가우시안 모델

- 각 노드가 부모의 선형 결합을 평균으로 갖는 가우시안일 때, 결합 분포는 다변량 가우시안이 된다.

$$
p(x_i\mid\mathrm{pa}_i)=\mathcal{N}\Bigl(x_i\;\Big|\;\sum_{j\in\mathrm{pa}_i}w_{ij}x_j+b_i,\ v_i\Bigr) \tag{8.11}
$$

- $x_i=\sum_{j\in\mathrm{pa}_i}w_{ij}x_j+b_i+\sqrt{v_i}\,\epsilon_i$이므로($\epsilon_i\sim\mathcal{N}(0,1)$), 평균과 공분산을 낮은 순번 노드부터 재귀적으로 구할 수 있다.

$$
\mathbb{E}[x_i]=\sum_{j\in\mathrm{pa}_i}w_{ij}\mathbb{E}[x_j]+b_i \tag{8.15}
$$

$$
\operatorname{cov}[x_i,x_j]=\sum_{k\in\mathrm{pa}_j}w_{jk}\operatorname{cov}[x_i,x_k]+I_{ij}v_j \tag{8.16}
$$

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.14.png" style="width:18rem;" />
<div class="cap">그림 8.14 · 링크 하나($x_1\to x_3$)가 빠진 가우시안 변수들의 방향성 그래프.</div>
</div>

::: tip 실습 · 선형 가우시안 DAG의 조상 표집
$x_1\to x_2\to x_3$ 사슬에서 (8.14)로 조상 표집<span class="gloss">ancestral sampling</span>을 수행하고, 표본의 평균·공분산이 재귀식 (8.15)·(8.16)의 닫힌 형태와 일치하는지 확인합니다.
:::

<PyRunner>

```python
import numpy as np
rng = np.random.default_rng(0)
b1, b2, b3 = 1.0, -0.5, 0.2; w21, w32 = 0.8, 1.3; v1, v2, v3 = 0.5, 0.3, 0.4
M = 200000
e1, e2, e3 = rng.standard_normal((3, M))
x1 = b1 + np.sqrt(v1)*e1                                # 조상 표집 (8.14)
x2 = w21*x1 + b2 + np.sqrt(v2)*e2
x3 = w32*x2 + b3 + np.sqrt(v3)*e3
X = np.vstack([x1, x2, x3])
mu_th = np.array([b1, b2+w21*b1, b3+w32*b2+w32*w21*b1])         # (8.15)
S = np.array([[v1,         w21*v1,             w32*w21*v1],     # (8.16)
              [w21*v1,     v2+w21**2*v1,       w32*(v2+w21**2*v1)],
              [w32*w21*v1, w32*(v2+w21**2*v1), v3+w32**2*(v2+w21**2*v1)]])
print("평균  이론:", np.round(mu_th,3).tolist(), " 표본:", np.round(X.mean(1),3).tolist())
print("공분산 최대 오차:", f"{np.abs(np.cov(X)-S).max():.4f}")
```

</PyRunner>

## 6.2 조건부 독립

- $c$가 주어졌을 때 $a$가 $b$에 독립이면 $p(a\mid b,c)=p(a\mid c)$, 즉 $p(a,b\mid c)=p(a\mid c)p(b\mid c)$이며 $a\perp\!\!\!\perp b\mid c$로 표기한다. 그래프에서는 해석적 조작 없이 조건부 독립을 읽어낼 수 있는데, 이 방법을 **d 분리**<span class="gloss">d-separation</span>라 한다('d'는 방향성).

### 6.2.1 세 가지 예시 그래프

- **꼬리 대 꼬리**<span class="gloss">tail-to-tail</span> ($a\leftarrow c\rightarrow b$): $c$가 관측되지 않으면 경로가 열려 $a\not\perp\!\!\!\perp b\mid\emptyset$, $c$가 관측되면 경로가 막혀 $a\perp\!\!\!\perp b\mid c$.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.15.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.16.png" />
</div>
<div class="cap">그림 8.15·8.16 · 꼬리 대 꼬리 노드 $c$. (왼쪽) 미관측 → 종속, (오른쪽) 관측 → 조건부 독립.</div>
</div>

- **머리 대 꼬리**<span class="gloss">head-to-tail</span> ($a\rightarrow c\rightarrow b$): $c$ 미관측이면 $a\not\perp\!\!\!\perp b\mid\emptyset$, $c$ 관측이면 $a\perp\!\!\!\perp b\mid c$.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.17.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.18.png" />
</div>
<div class="cap">그림 8.17·8.18 · 머리 대 꼬리 노드 $c$. (왼쪽) 미관측 → 종속, (오른쪽) 관측 → 조건부 독립.</div>
</div>

- **머리 대 머리**<span class="gloss">head-to-head</span> ($a\rightarrow c\leftarrow b$): 반대로 동작한다. $c$ 미관측이면 $a\perp\!\!\!\perp b\mid\emptyset$(독립), $c$(또는 그 자손)가 관측되면 $a\not\perp\!\!\!\perp b\mid c$가 되어 종속이 생긴다. 이를 **설명해내기**<span class="gloss">explaining away</span>라 한다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.19.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.20.png" />
</div>
<div class="cap">그림 8.19·8.20 · 머리 대 머리 노드 $c$. (왼쪽) 미관측 → 독립, (오른쪽) 관측 → 종속(설명해내기).</div>
</div>

::: tip 실습 · 설명해내기 (머리 대 머리)
독립인 원인 $a$, $b$와 공통 결과 $c$의 결합 분포에서, 무조건 상관 $\operatorname{corr}(a,b)\approx0$이지만 $c$를 관측하면 상관이 생기는 것을 확인합니다.
:::

<PyRunner>

```python
import numpy as np
pa = np.array([0.5, 0.5]); pb = np.array([0.5, 0.5])   # a, b 독립 사전
pc1 = np.array([[0.1, 0.8], [0.8, 0.95]])              # p(c=1 | a, b)
joint = np.zeros((2, 2, 2))                             # p(a, b, c)
for a in range(2):
    for b in range(2):
        joint[a, b, 1] = pa[a]*pb[b]*pc1[a, b]
        joint[a, b, 0] = pa[a]*pb[b]*(1-pc1[a, b])
def corr_ab(P):
    P = P/P.sum(); Ea = P.sum(1)[1]; Eb = P.sum(0)[1]; Eab = P[1, 1]
    return (Eab - Ea*Eb)/np.sqrt(Ea*(1-Ea)*Eb*(1-Eb))
print("무조건   corr(a,b)      =", f"{corr_ab(joint.sum(2)):+.3f}  (≈0, 독립)")
print("c=1 조건 corr(a,b|c=1)  =", f"{corr_ab(joint[:,:,1]):+.3f}  (설명해내기)")
```

</PyRunner>

### 6.2.2 d 분리

- 겹치지 않는 노드 집합 $A$, $B$, $C$에 대해 $A$의 노드에서 $B$의 노드로 가는 모든 경로를 본다. 경로에 (1) $C$에 속하는 머리 대 꼬리·꼬리 대 꼬리 노드가 있거나, (2) 그 노드와 모든 자손이 $C$에 속하지 않는 머리 대 머리 노드가 있으면 그 경로는 **폐쇄**<span class="gloss">blocked</span>된다. 모든 경로가 폐쇄되면 $A$는 $C$에 의해 $B$로부터 d 분리되고 $A\perp\!\!\!\perp B\mid C$이다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.22a.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.22b.png" />
</div>
<div class="cap">그림 8.22 · d 분리. (왼쪽) d 분리되지 않음, (오른쪽) d 분리됨.</div>
</div>

- 그래프를 필터로 보면, 모든 가능한 $p(\mathbf{x})$ 중 (8.5)의 방향성 인수분해를 만족하는 분포들의 집합 **방향성 인수분해**<span class="gloss">directed factorization</span> 집합 $\mathcal{DF}$가 남으며, 이는 d 분리가 함의하는 모든 조건부 독립을 만족하는 분포 집합과 정확히 같다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.25.png" style="max-width:32rem;" />
<div class="cap">그림 8.25 · 방향성 그래프를 필터로 보는 관점. 인수분해를 만족하는 분포 집합과 d 분리 조건부 독립을 만족하는 분포 집합이 일치한다.</div>
</div>

## 6.3 마르코프 무작위장

- **마르코프 무작위장**<span class="gloss">Markov random field</span>(마르코프 네트워크, **비방향성 그래프 모델**<span class="gloss">undirected graphical model</span>)은 방향 없는 링크로 노드를 잇는다.

### 6.3.1 조건부 독립 성질

- 비방향성 그래프에서 $A\perp\!\!\!\perp B\mid C$ 확인은 훨씬 단순하다. $A$와 $B$를 잇는 모든 경로가 $C$의 노드를 하나 이상 지나면(막히면) 조건부 독립이 성립한다. 방향의 비대칭성(머리 대 머리의 복잡함)이 사라진다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.27.png" style="width:20rem;" />
<div class="cap">그림 8.27 · $A$에서 $B$로의 모든 경로가 $C$를 지나므로 $A\perp\!\!\!\perp B\mid C$가 성립한다.</div>
</div>

### 6.3.2 인수분해 성질

- 링크로 연결되지 않은 두 노드는 나머지 모든 변수가 주어졌을 때 조건부 독립이어야 하므로, 인수분해에서 같은 인자에 나타나면 안 된다. **클리크**<span class="gloss">clique</span>는 모든 노드 쌍이 링크로 연결된 부분 집합이고, 더 키울 수 없는 것이 **최대 클리크**<span class="gloss">maximal clique</span>다. 결합 분포는 최대 클리크의 **포텐셜 함수**<span class="gloss">potential function</span> $\psi_C(\mathbf{x}_C)\geqslant0$의 곱이다.

$$
p(\mathbf{x})=\frac{1}{Z}\prod_C\psi_C(\mathbf{x}_C),\qquad Z=\sum_{\mathbf{x}}\prod_C\psi_C(\mathbf{x}_C)
$$

  $Z$는 **분할 함수**<span class="gloss">partition function</span>다. 방향성 그래프의 인자는 조건부 분포였지만, 포텐셜 함수는 특정 확률적 해석에 제한되지 않는다.

## 6.4 그래프 모델에서의 추론

- 추론은 관측된 노드로부터 다른 노드의 사후 분포를 계산하는 것이며, **메시지**<span class="gloss">message</span> 전파로 표현된다. $p(x,y)=p(x)p(y\mid x)$에서 $y$를 관측하면 $p(x\mid y)=\frac{p(y\mid x)p(x)}{p(y)}$로 은닉 변수 $x$의 사후 분포를 얻는다.

<div class="fig">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.37.png" style="max-width:30rem;" />
<div class="cap">그림 8.37 · 베이즈 정리의 그래프 표현. (왼쪽) $p(x,y)$, (가운데) $y$ 관측, (오른쪽) $p(y)p(x\mid y)$.</div>
</div>

### 6.4.1 사슬에서의 추론

- 비방향성 사슬 $p(\mathbf{x})=\frac{1}{Z}\prod_{n}\psi_{n-1,n}(x_{n-1},x_n)$에서 노드 $x_n$의 주변 분포를 순진하게 구하면 $K^N$에 비례하는 비용이 든다. 대신 합산을 안쪽부터 그룹지으면 두 방향의 메시지 곱으로 표현된다.

$$
p(x_n)=\frac{1}{Z}\,\mu_\alpha(x_n)\,\mu_\beta(x_n)
$$

$$
\mu_\alpha(x_n)=\sum_{x_{n-1}}\psi_{n-1,n}(x_{n-1},x_n)\,\mu_\alpha(x_{n-1}),\qquad
\mu_\beta(x_n)=\sum_{x_{n+1}}\psi_{n,n+1}(x_n,x_{n+1})\,\mu_\beta(x_{n+1})
$$

  $\mu_\alpha$는 앞으로(전방), $\mu_\beta$는 뒤로(후방) 전달되는 메시지다. 이런 사슬을 **마르코프 연쇄**<span class="gloss">Markov chain</span>라 하며, 비용이 $N$에 선형이 된다.

<div class="fig">
<div class="fig-row">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.32b.png" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-note/Figure8.38.png" />
</div>
<div class="cap">그림 8.32·8.38 · (왼쪽) 비방향성 사슬. (오른쪽) 양 끝에서 전방·후방 메시지를 전달해 $p(x_n)=\mu_\alpha(x_n)\mu_\beta(x_n)/Z$를 구한다.</div>
</div>

- 인접 노드 쌍의 결합 분포도 메시지로 표현된다: $p(x_{n-1},x_n)=\frac{1}{Z}\mu_\alpha(x_{n-1})\psi_{n-1,n}(x_{n-1},x_n)\mu_\beta(x_n)$.

::: tip 실습 · 사슬의 합-곱 알고리즘
길이 $N$·상태 $K$의 마르코프 연쇄에서 전방 메시지 $\mu_\alpha$와 후방 메시지 $\mu_\beta$로 중간 노드의 주변 분포를 구하고, 전체 결합 분포를 직접 열거한 브루트포스 결과와 일치하는지 확인합니다.
:::

<PyRunner>

```python
import numpy as np, itertools
rng = np.random.default_rng(1)
N, K = 5, 3
psi = [rng.uniform(0.2, 1.8, (K, K)) for _ in range(N-1)]   # ψ_{n,n+1}
# 브루트포스: 전체 결합 분포 열거
marg = np.zeros((N, K)); Z = 0.0
for x in itertools.product(range(K), repeat=N):
    p = 1.0
    for i in range(N-1): p *= psi[i][x[i], x[i+1]]
    Z += p
    for i in range(N): marg[i, x[i]] += p
marg /= Z
# 메시지 전달
node = 2
mu_a = np.ones(K)
for i in range(node): mu_a = mu_a @ psi[i]                   # 전방 μ_α
mu_b = np.ones(K)
for i in range(N-1, node, -1): mu_b = psi[i-1] @ mu_b        # 후방 μ_β
p_msg = mu_a*mu_b; p_msg /= p_msg.sum()
print(f"노드 x{node} 주변분포 (brute)  :", np.round(marg[node], 4).tolist())
print(f"노드 x{node} 주변분포 (message):", np.round(p_msg, 4).tolist())
print("최대 오차:", f"{np.abs(marg[node]-p_msg).max():.1e}")
```

</PyRunner>

## 연습문제

::: info 문제 6.1
각 조건부 분포가 정규화되어 있다는 가정하에, 방향성 그래프의 결합 분포 (8.5)가 올바르게 정규화되어 있음을 증명하라.
:::

::: details 풀이
노드를 위상 정렬<span class="gloss">topological order</span>하여 $x_1,\ldots,x_K$로 번호를 매기면, 각 노드의 부모는 자신보다 낮은 번호를 갖는다($\mathrm{pa}_k\subseteq\{x_1,\ldots,x_{k-1}\}$). 가장 높은 번호 $x_K$부터 차례로 합(또는 적분)한다.

$$
\sum_{\mathbf{x}}\prod_{k=1}^K p(x_k\mid\mathrm{pa}_k)=\sum_{x_1}\cdots\sum_{x_{K-1}}\prod_{k=1}^{K-1}p(x_k\mid\mathrm{pa}_k)\underbrace{\sum_{x_K}p(x_K\mid\mathrm{pa}_K)}_{=1}
$$

$x_K$는 다른 어떤 조건부 분포의 조건절에도 나타나지 않으므로($x_K$는 위상 정렬에서 마지막이라 자식이 없다) $\sum_{x_K}p(x_K\mid\mathrm{pa}_K)=1$로 소거된다. 남은 곱은 $K-1$개 노드의 그래프에 대한 같은 형태이므로, 이 과정을 $x_{K-1},x_{K-2},\ldots,x_1$ 순서로 반복하면 매 단계마다 정규화 조건으로 $1$이 곱해진다. 최종적으로

$$
\sum_{\mathbf{x}}\prod_{k=1}^K p(x_k\mid\mathrm{pa}_k)=1
$$

따라서 (8.5)는 올바르게 정규화되어 있다. $\blacksquare$
:::

::: info 문제 6.2
$a\perp\!\!\!\perp b,c\mid d$이면 $a\perp\!\!\!\perp b\mid d$임을 증명하라.
:::

::: details 풀이
조건부 독립 $a\perp\!\!\!\perp b,c\mid d$의 정의는

$$
p(a,b,c\mid d)=p(a\mid d)\,p(b,c\mid d)
$$

양변을 $c$에 대해 주변화(합 또는 적분)한다. 좌변은 $\sum_c p(a,b,c\mid d)=p(a,b\mid d)$, 우변은

$$
\sum_c p(a\mid d)\,p(b,c\mid d)=p(a\mid d)\sum_c p(b,c\mid d)=p(a\mid d)\,p(b\mid d)
$$

$p(a\mid d)$는 $c$에 무관하므로 합 밖으로 나오고, $\sum_c p(b,c\mid d)=p(b\mid d)$이다. 따라서

$$
p(a,b\mid d)=p(a\mid d)\,p(b\mid d)
$$

이는 곧 $a\perp\!\!\!\perp b\mid d$이다. $\blacksquare$
:::
