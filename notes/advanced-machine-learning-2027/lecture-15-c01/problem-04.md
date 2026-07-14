# 문제 4 · 커널 방법론 (듀얼 표현)

::: info 문제 4 [4점]
아래 커널 기반 회귀 모델의 목적함수의 듀얼 표현<span class="gloss">dual representation</span>을 구하시오.

$$
J(\mathbf{w})=\frac{1}{2}\sum_{i=1}^N\big(t_i-\mathbf{w}^\top\phi(\mathbf{x}_i)\big)^2+\frac{\lambda}{2}\|\mathbf{w}\|^2
$$
:::

::: details 풀이 및 해설
$\nabla_\mathbf{w}J=0$에서 $\mathbf{w}=\sum_i a_i\phi(\mathbf{x}_i)=\boldsymbol{\Phi}^\top\mathbf{a}$, $a_i=\tfrac1\lambda(t_i-\mathbf{w}^\top\phi(\mathbf{x}_i))$. 이를 대입하고 그램 행렬 $\mathbf{K}=\boldsymbol{\Phi}\boldsymbol{\Phi}^\top$ ($K_{ij}=k(\mathbf{x}_i,\mathbf{x}_j)$)을 도입하면

$$
J(\mathbf{a})=\frac12\mathbf{a}^\top\mathbf{K}\mathbf{K}\mathbf{a}-\mathbf{a}^\top\mathbf{K}\mathbf{t}+\frac12\mathbf{t}^\top\mathbf{t}+\frac\lambda2\mathbf{a}^\top\mathbf{K}\mathbf{a}
$$

$\nabla_\mathbf{a}J=0$을 정리하면 정규방정식

$$
\boxed{\ \mathbf{a}=(\mathbf{K}+\lambda\mathbf{I}_N)^{-1}\mathbf{t}\ }
$$

를 얻고, 예측은 $y(\mathbf{x})=\mathbf{k}(\mathbf{x})^\top(\mathbf{K}+\lambda\mathbf{I}_N)^{-1}\mathbf{t}$, $k_i(\mathbf{x})=k(\mathbf{x}_i,\mathbf{x})$로 커널만으로 계산된다.
:::
