# 문제 10 · 주성분 분석

::: info 문제 10 [5점]
아래와 같은 관측값이 주어졌을 때, 제 1 주성분<span class="gloss">principal component</span>을 구하시오.

$$
\{(3,1),(1,3),(0,0),(2,2)\}
$$
:::

::: details 풀이 및 해설
**평균**: $\bar{\mathbf{x}}=\left(\tfrac{3+1+0+2}{4},\tfrac{1+3+0+2}{4}\right)=(1.5,1.5)$.

**중심화**: $(1.5,-0.5),(-0.5,1.5),(-1.5,-1.5),(0.5,0.5)$.

**공분산 행렬** ($N=4$):

$$
\mathbf{S}=\frac14\begin{pmatrix}5&1\\1&5\end{pmatrix}=\begin{pmatrix}1.25&0.25\\0.25&1.25\end{pmatrix}
$$

**고윳값** — $\det(\mathbf{S}-\lambda I)=(1.25-\lambda)^2-0.25^2=0\Rightarrow 1.25-\lambda=\pm0.25\Rightarrow \lambda=1.5\ \text{또는}\ 1$.

**제1 주성분** — 최대 고윳값 $\lambda_1=1.5$에 대응하는 고유벡터. $(\mathbf{S}-1.5I)\mathbf{v}=0$에서 $-0.25v_1+0.25v_2=0\Rightarrow v_1=v_2$이므로

$$
\boxed{\ \mathbf{v}_1\propto(1,1),\quad \tfrac{1}{\sqrt2}(1,1)\ }\qquad(\lambda_1=1.5)
$$

데이터가 $(0,0)$과 $(3,1),(2,2)$처럼 대각선 $(1,1)$ 방향으로 가장 넓게 퍼져 있어 자연스러운 결과다.

👉 [실습(Python)에서 공분산·고유분해 계산](./lab-10)
:::
