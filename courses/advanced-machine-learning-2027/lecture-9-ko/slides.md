---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: AML - Lecture 9 (KO)
download: true
info: |
  ## 고급 기계학습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/advanced-machine-learning-2027/lecture-9/
---

<style>
.dark .slidev-page,
.dark .slidev-layout,
.dark .slide-container,
.dark #slide-content,
.dark .slidev-nav-go-container {
  background: #000000 !important;
}
</style>

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.png" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">고급 기계학습</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">9주차: 그래프 모델</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">2027년 봄학기</p>
</div>

---
layout: prism
heading: 강좌 일정
---

<div class="absolute left-10 right-10" style="top: 1rem; bottom: 5rem; display: grid; grid-template-columns: 1fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">강좌 소개</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">예비 지식</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">확률 분포</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">선형 회귀 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">선형 분류 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">커널 방법론</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간고사 복습</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span class="text-gray-900 dark:text-gray-100">그래프 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">혼합 모델</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">근사 추론</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">샘플링 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">연속 잠재 변수</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말고사 복습</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">베이지안 네트워크</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">조건부 독립</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">마르코프 무작위장</span></p>
</div>
</div>

---
layout: prism
heading: 베이지안 네트워크 (1/4)
---

<style>
.slidev-layout ul > li { margin-top: 2.8em; }
</style>

- 확률 분포를 의미론적으로 표현하는 [확률적 그래프 모델(probabilistic graphical models; PGMs)]{.hl}을 활용할 수 있습니다.

<div class="sub-item">

확률적 그래프 모델은 모델을 시각화하고, 조건부 독립 같은 성질을 드러내며, 학습과 추론을 위한 복잡한 계산을 그래프 연산으로 표현합니다.

</div>

- [그래프(graph)]{.hl}는 [노드(nodes)]{.hl}(꼭짓점)와 [링크(links)]{.hl}(변 또는 호)로 구성됩니다.

- 각 노드는 확률 변수를 나타내고, 링크는 변수들 사이의 확률적 관계를 나타냅니다.

---
layout: prism
heading: 베이지안 네트워크 (2/4)
---

<style>
.slidev-layout ul > li { margin-top: 1.2em; }
</style>

- [베이지안 네트워크(Bayesian network)]{.hl}, 즉 [방향성 그래프 모델(directed graphical model)]{.hl}은 링크가 방향성(화살표로 표현)을 갖는 그래프입니다.

- 곱의 법칙으로 분해한 세 변수의 결합 분포를 생각해 봅시다:

$$
p(a,b,c)=p(c|a,b)p(a,b)=p(c|a,b)p(b|a)p(a)
$$

- 위 식의 우변은 간단한 그래프로 표현됩니다:

<div class="sub-item-enum">

1. $a$, $b$, $c$ 각각에 대해 노드를 하나씩 도입합니다.
2. 각 노드를 해당 조건부 분포와 연결합니다.
3. 각 조건부 분포마다 방향성 링크를 추가합니다(예: $p(c|a,b)$는 $a\to c$와 $b\to c$를 그리며, 이때 $c$는 부모($a$, $b$)의 [자식(child)]{.hl}이고 $a$, $b$는 [부모(parents)]{.hl}입니다).

</div>

---
layout: prism
heading: 베이지안 네트워크 (3/4)
---

<div style="display:grid; grid-template-columns: 1.9fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2em; }
</style>

- $K$개 변수에 대한 일반화된 인수분해:

$$
p(x_1,\ldots,x_K)=p(x_K|x_1,\ldots,x_{K-1})\cdots p(x_2|x_1)p(x_1)
$$

<div class="sub-item">

각 노드는 자신보다 낮은 순번의 노드로부터 방향성 링크를 받는 조건부 분포입니다. 모든 노드 쌍이 연결되어 있으면 그래프는 [완전 연결(fully connected)]{.hl}이라고 합니다.

</div>

- 대신 [부재(absent)]{.hl}하는 링크를 가질 수도 있습니다(오른쪽 그래프는 완전 연결이 아닙니다).

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.2.png" class="img-center" style="width: 12rem;" />
</div>
</div>

---
layout: prism
heading: 베이지안 네트워크 (4/4)
---

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- $K$개 노드를 가진 그래프에는 일반적인 인수분해를 사용합니다:

$$
p(\mathbf{x})=\prod_{k=1}^{K}p(x_k|\mathrm{pa}_k)
$$

<div class="sub-item">

$\mathrm{pa}_k$는 $x_k$의 부모 노드들입니다. 각 조건부 분포가 정규화되어 있으면 곱도 항상 정규화됩니다.

</div>

- 우리는 [방향성 순환(directed cycle)]{.hl}이 없는 그래프, 즉 [방향성 비순환 그래프(directed acyclic graph; DAG)]{.hl}만 다룹니다. 어떤 노드에서 링크를 따라가도 원래 노드로 돌아오지 않습니다.

---
layout: prism
heading: 다항 근사 (1/3)
---

<div style="display:grid; grid-template-columns: 1.9fr 1.1fr; gap: 2.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.0em; }
</style>

- 베이지안 다항 회귀 모델의 확률 변수는 계수 $\mathbf{w}$와 표적값 $\boldsymbol{\mathsf{t}}=(t_1,\ldots,t_N)^\top$입니다.

$$
p(\boldsymbol{\mathsf{t}},\mathbf{w})=p(\mathbf{w})\prod_{n=1}^{N}p(t_n|\mathbf{w})
$$

- $t_1,\ldots,t_N$을 일일이 그리는 대신, 대표 노드 $t_n$ 하나를 $N$으로 표시한 [판(plate)]{.hl}으로 둘러쌉니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.3.png" class="img-center" style="width: 15rem; margin-bottom: 4rem;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.4.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: 다항 근사 (2/3)
---

<div style="display:grid; grid-template-columns: 1.9fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.2em; }
</style>

- 결정 매개변수를 명시적으로 표현할 수 있습니다:

$$
p(\boldsymbol{\mathsf{t}}, \mathbf{w} | \boldsymbol{\mathsf{x}}, \alpha, \sigma^2)=p(\mathbf{w} | \alpha) \prod_{n=1}^N p(t_n | \mathbf{w}, x_n, \sigma^2)
$$

<div class="sub-item">

열린 원은 확률 변수, 작은 점은 결정 변수입니다.

</div>

- [관측 변수(observed variables)]{.hl}(예: 표적값) 노드는 음영으로 표시하며, $\mathbf{w}$처럼 관측되지 않은 변수는 [잠재(latent)]{.hl}(은닉) 변수입니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.5.png" class="img-center" style="width: 15rem;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.6.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: 다항 근사 (3/3)
---

<div style="display:grid; grid-template-columns: 1.9fr 1.1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.2em; }
</style>

- 처음 보는 입력 $\widehat{x}$에 대한 모든 확률 변수의 결합 분포는:

$$
p(\widehat{t}, \boldsymbol{\mathsf{t}}, \mathbf{w} | \widehat{x}, \boldsymbol{\mathsf{x}}, \alpha, \sigma^2)=\Big[\prod_{n=1}^N p(t_n | x_n, \mathbf{w}, \sigma^2)\Big] p(\mathbf{w} | \alpha)\, p(\widehat{t} | \widehat{x}, \mathbf{w}, \sigma^2)
$$

- 예측 분포는 합의 법칙($\mathbf{w}$에 대한 주변화)으로 얻습니다:

$$
p(\widehat{t} | \widehat{x}, \boldsymbol{\mathsf{x}}, \boldsymbol{\mathsf{t}}, \alpha, \sigma^2) \propto \int p(\widehat{t}, \boldsymbol{\mathsf{t}}, \mathbf{w} | \widehat{x}, \boldsymbol{\mathsf{x}}, \alpha, \sigma^2)\, \mathrm{d}\mathbf{w}
$$

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.7.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: 이산 변수 (1/4)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- 그래프 모델링은 지수족의 원소들이 어떻게 연결되는지 보여주는 데 유용하며, 켤레인 부모–자식 쌍은 유용한 성질을 가집니다.

- $K$개 상태를 갖는 이산 변수 $\mathbf{x}$는 다음과 같이 씁니다:

$$
p(\mathbf{x} | \boldsymbol{\mu})=\prod_{k=1}^K \mu_k^{x_k}
$$

<div class="sub-item">

제약 $\sum_k\mu_k=1$ 하에서 $K-1$개의 매개변수가 필요합니다. 변수가 $M$개이면 임의의 결합 분포에 $K^M-1$개가 필요합니다.

</div>

---
layout: prism
heading: 이산 변수 (2/4)
---

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- 변수를 사슬로 연결하면 매개변수 수가 줄어듭니다. $M$개 노드의 사슬은 $K-1+(M-1)K(K-1)$개로 $M$에 선형입니다.

- 매개변수를 [매듭(tie)]{.hl}(공유)으로 묶어 수를 더 줄이거나, 디리클레 사전 분포를 추가해 베이지안 모델로 만들 수 있습니다.

<div class="img-row" style="max-width: 88%">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.10.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.11.png"/>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.12.png"/>
</div>

---
layout: prism
heading: 이산 변수 (3/4)
---

<div style="display:grid; grid-template-columns: 1.7fr 1.3fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.2em; }
</style>

- 전체 조건부 분포 테이블($M$에 지수적) 대신 매개변수화된 모델을 쓰면 매개변수 수를 작게 유지할 수 있습니다.

- 부모들의 선형 결합에 로지스틱 시그모이드를 적용하면:

$$
p(y=1 | x_1, \ldots, x_M)=\sigma\Big(w_0+\sum_{i=1}^M w_i x_i\Big)=\sigma(\mathbf{w}^{\top} \mathbf{x})
$$

<div class="sub-item">

매개변수 수가 $M$에 대해 지수적이 아니라 선형으로 늘어납니다.

</div>

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.13.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: 이산 변수 (4/4)
---

<PyRunner>

```python
K = 3
print("Parameters vs. #variables M (K = 3 states):")
print(f"{'M':>3} | {'fully connected':>16} | {'chain':>8} | {'independent':>12}")
for M in [1, 2, 4, 6, 8]:
    full = K**M - 1                       # arbitrary joint
    chain = K-1 + (M-1)*K*(K-1)           # chain of nodes
    indep = M*(K-1)                       # fully factorized
    print(f"{M:>3} | {full:>16} | {chain:>8} | {indep:>12}")
print("\nOnly the fully connected graph explodes exponentially in M.")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">베이지안 네트워크</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">조건부 독립</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">마르코프 무작위장</span></p>
</div>
</div>

---
layout: prism
heading: 조건부 독립
---

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- 세 변수 $a$, $b$, $c$에 대해, $c$가 주어졌을 때 $a$가 $b$에 독립이면:

$$
p(a|b,c)=p(a|c)
$$

- 마찬가지로, $c$가 주어졌을 때 $a$, $b$의 결합 분포가 인수분해됩니다:

$$
p(a,b|c)=p(a|b,c)p(b|c)=p(a|c)p(b|c)
$$

<div class="sub-item">

이를 간단히 $a \perp\!\!\!\perp b \mid c$로 표기합니다.

</div>

---
layout: prism
heading: 예시 (1/3) — 꼬리 대 꼬리
---

<div style="display:grid; grid-template-columns: 1.6fr 1.4fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3em; }
</style>

- 노드 $c$는 [꼬리 대 꼬리(tail-to-tail)]{.hl} 노드입니다: $p(a,b,c)=p(a|c)p(b|c)p(c)$.

- $c$가 관측되지 않으면 주변화 결과 $p(a,b)=\sum_c p(a|c)p(b|c)p(c)$가 인수분해되지 않으므로 $a\not\perp\!\!\!\perp b\mid\emptyset$입니다.

- $c$가 관측되면 $p(a,b|c)=p(a|c)p(b|c)$가 되어 경로를 [막고(blocks)]{.hl} $a\perp\!\!\!\perp b\mid c$입니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.15.png" class="img-center" style="width: 15rem;" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.16.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: 예시 (2/3) — 머리 대 꼬리
---

<div style="display:grid; grid-template-columns: 1.6fr 1.4fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- 노드 $c$는 [머리 대 꼬리(head-to-tail)]{.hl} 노드입니다: $p(a,b,c)=p(a)p(c|a)p(b|c)$.

- $c$가 관측되지 않으면 $p(a,b)=p(a)\sum_c p(c|a)p(b|c)=p(a)p(b|a)$이므로 $a\not\perp\!\!\!\perp b\mid\emptyset$입니다.

- $c$가 관측되면 $p(a,b|c)=\dfrac{p(a)p(c|a)p(b|c)}{p(c)}=p(a|c)p(b|c)$이므로 $a\perp\!\!\!\perp b\mid c$입니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.17.png" class="img-center" style="width: 15rem; margin-bottom: 6rem" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.18.png" class="img-center" style="width: 15rem;" />
</div>
</div>

---
layout: prism
heading: 예시 (3/3) — 머리 대 머리
---

<div style="display:grid; grid-template-columns: 1.6fr 1.4fr; gap: 1rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- 노드 $c$는 [머리 대 머리(head-to-head)]{.hl} 노드입니다: $p(a,b,c)=p(a)p(b)p(c|a,b)$.

- $c$가 관측되지 않으면 $p(a,b)=p(a)p(b)$이므로 $a\perp\!\!\!\perp b\mid\emptyset$입니다.

- $c$(또는 그 자손)가 관측되면 일반적으로 $p(a,b|c)\neq p(a|c)p(b|c)$이므로 $a\not\perp\!\!\!\perp b\mid c$입니다([설명해내기(explaining away)]{.hl}).

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.19.png" class="img-center" style="width: 12rem; margin-bottom: 4rem" />
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.20.png" class="img-center" style="width: 12rem;" />
</div>
</div>

---
layout: prism
heading: d 분리
---

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- DAG에서 서로소인 노드 집합 $A$, $B$, $C$에 대해 $A\perp\!\!\!\perp B\mid C$를 판정하려면 $A$에서 $B$로 가는 모든 경로를 살펴봅니다.

- 경로가 다음 중 하나를 만족하는 노드를 포함하면 그 경로는 [막힘(blocked)]{.hl}입니다:

<div class="sub-item-enum">

1. 노드에서 화살표가 머리 대 꼬리 또는 꼬리 대 꼬리로 만나고 그 노드가 $C$에 속하거나,
2. 노드에서 화살표가 머리 대 머리로 만나고 그 노드와 모든 자손이 $C$에 속하지 않는 경우.

</div>

- 모든 경로가 막히면 $A$는 $C$에 의해 $B$로부터 d 분리되며, 따라서 $A\perp\!\!\!\perp B\mid C$입니다.

---
layout: prism
heading: 조건부 독립 다시 보기
---

<PyRunner>

```python
import numpy as np
# head-to-head: a, b independent causes; c a common effect (explaining away)
pa = np.array([0.5, 0.5]); pb = np.array([0.5, 0.5])
pc1 = np.array([[0.1, 0.8], [0.8, 0.95]])           # p(c=1 | a, b)
joint = np.zeros((2, 2, 2))
for a in range(2):
    for b in range(2):
        joint[a, b, 1] = pa[a]*pb[b]*pc1[a, b]
        joint[a, b, 0] = pa[a]*pb[b]*(1-pc1[a, b])
def corr_ab(P):
    P = P/P.sum(); Ea = P.sum(1)[1]; Eb = P.sum(0)[1]; Eab = P[1, 1]
    return (Eab - Ea*Eb)/np.sqrt(Ea*(1-Ea)*Eb*(1-Eb))
print("unconditional corr(a,b)   =", f"{corr_ab(joint.sum(2)):+.3f}  (~0, independent)")
print("corr(a,b | c=1)           =", f"{corr_ab(joint[:,:,1]):+.3f}  (explaining away)")
```

</PyRunner>

---
layout: prism
heading: 목차
---

<div style="margin-top: 1.5rem; margin-left: 3rem">
<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">베이지안 네트워크</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">조건부 독립</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">마르코프 무작위장</span></p>
</div>
</div>

---
layout: prism
heading: 마르코프 무작위장
---

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- [마르코프 네트워크(Markov network)]{.hl}, 즉 [비방향성 그래프 모델(undirected graphical model)]{.hl} 또는 [마르코프 무작위장(Markov random field)]{.hl}은 노드와 링크로 이루어집니다.

- 링크에 방향성이 없으므로 화살표를 쓰지 않습니다.

- 여기서 조건부 독립은 더 간단합니다: $A$에서 $B$로 가는 모든 경로가 $C$의 노드를 하나 이상 지나면 $A\perp\!\!\!\perp B\mid C$가 성립합니다.

---
layout: prism
heading: 조건부 독립 성질
---

<div style="display:grid; grid-template-columns: 1.5fr 1fr; gap: 1.5rem; align-items:center;">
<div>

<style>
.slidev-layout ul > li { margin-top: 3.5em; }
</style>

- 방향성 그래프에서는 d 분리로 경로가 막혔는지 판정하며, 머리 대 머리 노드가 막힘 판정을 미묘하게 만듭니다.

- 방향성을 제거하면 부모–자식 비대칭이 사라져 비방향성 모델이 됩니다.

- $A\perp\!\!\!\perp B\mid C$를 확인하려면 $A$와 $B$ 사이 모든 경로를 살펴, 전부 $C$를 지나면 성질이 성립합니다.

</div>
<div>
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/aml/aml-2027/Figure8.27.png" class="img-center" style="width: 18rem;" />
</div>
</div>

---
layout: prism
heading: 그래프 모델에서의 추론 (1/2)
---

<style>
.slidev-layout ul > li { margin-top: 2.5em; }
</style>

- 그래프 모델에서는 관측된 노드가 주어졌을 때 하나 이상의 노드의 사후 분포를 [추론(infer)]{.hl}하며, 이는 [메시지 전달(message passing)]{.hl}로 표현됩니다.

- 결합 분포 $p(x,y)=p(x)p(y|x)$에서 $y$가 관측되면, 주변 분포 $p(x)$는 은닉 변수 $x$의 사전 분포이고, 베이즈 정리로 그 사후 분포를 추론합니다.

- 비방향성 사슬에서 주변 분포 $p(x_n)=\dfrac{1}{Z}\mu_\alpha(x_n)\mu_\beta(x_n)$는 전방·후방 메시지의 곱이며, $O(N)$으로 재귀적으로 계산됩니다.

---
layout: prism
heading: 그래프 모델에서의 추론 (2/2)
---

<PyRunner>

```python
import numpy as np, itertools
rng = np.random.default_rng(1)
N, K = 5, 3
psi = [rng.uniform(0.2, 1.8, (K, K)) for _ in range(N-1)]      # chain potentials
# brute force: enumerate the full joint
marg = np.zeros((N, K)); Z = 0.0
for x in itertools.product(range(K), repeat=N):
    p = 1.0
    for i in range(N-1): p *= psi[i][x[i], x[i+1]]
    Z += p
    for i in range(N): marg[i, x[i]] += p
marg /= Z
# forward / backward message passing at node 2
node = 2
mu_a = np.ones(K)
for i in range(node): mu_a = mu_a @ psi[i]
mu_b = np.ones(K)
for i in range(N-1, node, -1): mu_b = psi[i-1] @ mu_b
p_msg = mu_a*mu_b; p_msg /= p_msg.sum()
print("marginal p(x2) brute force :", np.round(marg[node], 4).tolist())
print("marginal p(x2) messages    :", np.round(p_msg, 4).tolist())
print("max error                  :", f"{np.abs(marg[node]-p_msg).max():.1e}")
```

</PyRunner>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
