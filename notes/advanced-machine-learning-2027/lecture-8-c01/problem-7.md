# 문제 7 · 커널 방법론 (듀얼 표현)

::: info 문제 7 [4점]
아래 커널 기반 회귀 모델의 목적함수의 듀얼 표현<span class="gloss">dual representation</span>을 구하시오.

$$
J(\mathbf{w})=\frac{1}{2}\sum_{i=1}^N\big(t_i-\mathbf{w}^\top\phi(\mathbf{x}_i)\big)^2+\frac{\lambda}{2}\|\mathbf{w}\|^2
$$
:::

::: details 풀이 및 해설
**최적해의 형태** — $J$를 $\mathbf{w}$로 미분하여 $0$으로 둔다.

$$
\nabla_\mathbf{w}J=-\sum_{i=1}^N\big(t_i-\mathbf{w}^\top\phi(\mathbf{x}_i)\big)\phi(\mathbf{x}_i)+\lambda\mathbf{w}=0
$$

$$
\therefore\ \mathbf{w}=\sum_{i=1}^N a_i\,\phi(\mathbf{x}_i)=\boldsymbol{\Phi}^\top\mathbf{a},\qquad a_i=\frac{1}{\lambda}\big(t_i-\mathbf{w}^\top\phi(\mathbf{x}_i)\big)
$$

즉 해는 특징 벡터들의 선형 결합이다.

**듀얼 표현** — $\mathbf{w}=\boldsymbol{\Phi}^\top\mathbf{a}$를 대입하고 그램 행렬 $\mathbf{K}=\boldsymbol{\Phi}\boldsymbol{\Phi}^\top$ ($K_{ij}=k(\mathbf{x}_i,\mathbf{x}_j)$)를 도입하면

$$
J(\mathbf{a})=\frac{1}{2}\mathbf{a}^\top\mathbf{K}\mathbf{K}\mathbf{a}-\mathbf{a}^\top\mathbf{K}\mathbf{t}+\frac{1}{2}\mathbf{t}^\top\mathbf{t}+\frac{\lambda}{2}\mathbf{a}^\top\mathbf{K}\mathbf{a}
$$

**정규방정식** — $\nabla_\mathbf{a}J=\mathbf{K}\mathbf{K}\mathbf{a}-\mathbf{K}\mathbf{t}+\lambda\mathbf{K}\mathbf{a}=0$을 정리하면

$$
\boxed{\ \mathbf{a}=(\mathbf{K}+\lambda\mathbf{I}_N)^{-1}\mathbf{t}\ }
$$

새 입력 $\mathbf{x}$의 예측은 커널만으로 $y(\mathbf{x})=\mathbf{k}(\mathbf{x})^\top(\mathbf{K}+\lambda\mathbf{I}_N)^{-1}\mathbf{t}$, $k_i(\mathbf{x})=k(\mathbf{x}_i,\mathbf{x})$로 계산된다.
:::
