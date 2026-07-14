# 문제 10 · 커널 방법론

::: info 문제 10 — 커널 방법론
데이터셋 $\{(\mathbf{x}_i,t_i)\mid i=1,\ldots,N,\ \mathbf{x}_i\in\mathbb{R}^d,\ t_i\in\mathbb{R}\}$이 주어졌다고 할 때, 데이터를 비선형 특징 공간<span class="gloss">feature space</span>으로 사상시키는 함수 $\phi(\cdot)$를 이용하여 아래와 같은 커널 기반 회귀 문제를 정의하였다.

$$
J(\mathbf{w})=\frac{1}{2}\sum_{i=1}^{N}\big(t_i-\mathbf{w}^\top\phi(\mathbf{x}_i)\big)^2+\frac{\lambda}{2}\|\mathbf{w}\|^2
$$

위 목적함수에서 최적해 $\mathbf{w}^\star$가 다음과 같은 형태로 표현됨을 유도하라.

$$
\mathbf{w}^\star=\sum_{i=1}^{N}a_i\,\phi(\mathbf{x}_i)\qquad\text{즉, } \phi(\mathbf{x}_i)\text{들의 선형 결합}
$$

위 결과를 이용하여 원래의 목적함수를 $\mathbf{a}$에 관한 듀얼 표현<span class="gloss">dual representation</span>으로 명확히 표현하고, $\mathbf{a}$를 구하는 정규방정식을 명확히 유도하라.

---

먼저 $J(\mathbf{w})$를 미분한 후 $0$으로 두어 $\mathbf{w}^\star$를 얻는다. 이후 그 결과를 목적함수에 대입해 $J(\mathbf{a})$를 얻고(필요하면 그램 행렬<span class="gloss">Gram matrix</span>을 정의), 다시 미분하여 $0$으로 두면 정규방정식을 얻는다.
:::

::: details 풀이 및 해설
**$\mathbf{w}^\star$의 형태** — $J(\mathbf{w})$를 $\mathbf{w}$로 미분하여 $0$으로 둔다.

$$
\nabla_\mathbf{w}J=-\sum_{i=1}^{N}\big(t_i-\mathbf{w}^\top\phi(\mathbf{x}_i)\big)\phi(\mathbf{x}_i)+\lambda\mathbf{w}=0
$$

$$
\therefore\ \mathbf{w}=\frac{1}{\lambda}\sum_{i=1}^{N}\big(t_i-\mathbf{w}^\top\phi(\mathbf{x}_i)\big)\phi(\mathbf{x}_i)=\sum_{i=1}^{N}a_i\,\phi(\mathbf{x}_i)=\boldsymbol{\Phi}^\top\mathbf{a}
$$

여기서 $a_i=\tfrac{1}{\lambda}\big(t_i-\mathbf{w}^\top\phi(\mathbf{x}_i)\big)$이고, $\boldsymbol{\Phi}$는 $i$번째 행이 $\phi(\mathbf{x}_i)^\top$인 설계 행렬이다. 즉 최적해는 특징 벡터들의 선형 결합으로 표현된다.

**듀얼 표현** — $\mathbf{w}=\boldsymbol{\Phi}^\top\mathbf{a}$를 $J$에 대입하고 그램 행렬 $\mathbf{K}=\boldsymbol{\Phi}\boldsymbol{\Phi}^\top$ ($K_{ij}=\phi(\mathbf{x}_i)^\top\phi(\mathbf{x}_j)=k(\mathbf{x}_i,\mathbf{x}_j)$)를 도입하면

$$
J(\mathbf{a})=\frac{1}{2}\mathbf{a}^\top\mathbf{K}\mathbf{K}\mathbf{a}-\mathbf{a}^\top\mathbf{K}\mathbf{t}+\frac{1}{2}\mathbf{t}^\top\mathbf{t}+\frac{\lambda}{2}\mathbf{a}^\top\mathbf{K}\mathbf{a}
$$

**정규방정식** — $J(\mathbf{a})$를 $\mathbf{a}$로 미분하여 $0$으로 둔다.

$$
\nabla_\mathbf{a}J=\mathbf{K}\mathbf{K}\mathbf{a}-\mathbf{K}\mathbf{t}+\lambda\mathbf{K}\mathbf{a}=0
\ \Longrightarrow\ \mathbf{K}(\mathbf{K}+\lambda\mathbf{I}_N)\mathbf{a}=\mathbf{K}\mathbf{t}
$$

$\mathbf{K}$가 가역이라 가정하면

$$
\boxed{\ \mathbf{a}=(\mathbf{K}+\lambda\mathbf{I}_N)^{-1}\mathbf{t}\ }
$$

새로운 입력 $\mathbf{x}$에 대한 예측은 특징 벡터를 직접 계산하지 않고 커널만으로 이루어진다.

$$
y(\mathbf{x})=\mathbf{w}^{\star\top}\phi(\mathbf{x})=\mathbf{a}^\top\boldsymbol{\Phi}\phi(\mathbf{x})=\mathbf{k}(\mathbf{x})^\top(\mathbf{K}+\lambda\mathbf{I}_N)^{-1}\mathbf{t},\qquad k_i(\mathbf{x})=k(\mathbf{x}_i,\mathbf{x})
$$

이것이 커널 릿지 회귀의 듀얼 표현이며, 6주차 슬라이드의 듀얼 표현 유도와 동일한 구조이다.
:::
