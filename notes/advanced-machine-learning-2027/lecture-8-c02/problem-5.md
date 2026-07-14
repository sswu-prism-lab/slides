# 문제 5 · 확률적 생성 모델 (결정 경계)

::: info 문제 5 [6점]
이진 분류($k=1,2$)에서 데이터 $\mathbf{x}$의 조건부 밀도가 다음과 같이 주어졌다. 이 때, 결정 경계 $p(\mathcal{C}_1\mid\mathbf{x})$를 구하시오. $Z$는 임의의 $0$이 아닌 상수이다.

$$
p(\mathbf{x}\mid\mathcal{C}_k)=\frac{1}{Z}\exp\left\{-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_k)^\top\boldsymbol{\Sigma}_k^{-1}(\mathbf{x}-\boldsymbol{\mu}_k)\right\}
$$
:::

::: details 풀이 및 해설
사후확률을 로지스틱 시그모이드로 정리한다.

$$
p(\mathcal{C}_1\mid\mathbf{x})=\frac{p(\mathbf{x}\mid\mathcal{C}_1)p(\mathcal{C}_1)}{p(\mathbf{x}\mid\mathcal{C}_1)p(\mathcal{C}_1)+p(\mathbf{x}\mid\mathcal{C}_2)p(\mathcal{C}_2)}=\sigma(a),\qquad \sigma(a)=\frac{1}{1+e^{-a}}
$$

여기서

$$
a=\ln\frac{p(\mathbf{x}\mid\mathcal{C}_1)p(\mathcal{C}_1)}{p(\mathbf{x}\mid\mathcal{C}_2)p(\mathcal{C}_2)}
$$

두 밀도의 정규화 상수 $Z$가 같으므로 상쇄되고, 지수부만 남는다.

$$
a=-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_1)^\top\boldsymbol{\Sigma}_1^{-1}(\mathbf{x}-\boldsymbol{\mu}_1)+\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_2)^\top\boldsymbol{\Sigma}_2^{-1}(\mathbf{x}-\boldsymbol{\mu}_2)+\ln\frac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}
$$

$$
\boxed{\ p(\mathcal{C}_1\mid\mathbf{x})=\sigma(a)\ }
$$

**경계의 형태** — 결정 경계는 $p(\mathcal{C}_1\mid\mathbf{x})=\tfrac12$, 즉 $a=0$이다.

- $\boldsymbol{\Sigma}_1\neq\boldsymbol{\Sigma}_2$이면 $a$에 $\mathbf{x}^\top(\boldsymbol{\Sigma}_1^{-1}-\boldsymbol{\Sigma}_2^{-1})\mathbf{x}$ 형태의 **이차항이 남아 경계가 곡선(비선형, QDA)** 이 된다.
- $\boldsymbol{\Sigma}_1=\boldsymbol{\Sigma}_2=\boldsymbol{\Sigma}$이면 이차항이 상쇄되어

$$
a=\mathbf{w}^\top\mathbf{x}+w_0,\quad \mathbf{w}=\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2),\quad
w_0=-\tfrac12\boldsymbol{\mu}_1^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_1+\tfrac12\boldsymbol{\mu}_2^\top\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}_2+\ln\tfrac{p(\mathcal{C}_1)}{p(\mathcal{C}_2)}
$$

가 되어 $p(\mathcal{C}_1\mid\mathbf{x})=\sigma(\mathbf{w}^\top\mathbf{x}+w_0)$인 **선형 경계(LDA)** 로 단순화된다.
:::
