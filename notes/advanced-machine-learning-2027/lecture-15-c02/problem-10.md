# 문제 10 · 주성분 분석

::: info 문제 10 [5점]
아래와 같은 관측값이 주어졌을 때, 제 1 주성분<span class="gloss">principal component</span>을 구하시오.

$$
\{(2,0),(0,2),(3,1),(1,3)\}
$$
:::

::: details 풀이 및 해설
**평균**: $\bar{\mathbf{x}}=\left(\tfrac{2+0+3+1}{4},\tfrac{0+2+1+3}{4}\right)=(1.5,1.5)$.

**중심화**: $(0.5,-1.5),(-1.5,0.5),(1.5,-0.5),(-0.5,1.5)$.

**공분산 행렬** ($N=4$):

$$
\mathbf{S}=\frac14\begin{pmatrix}5&-3\\-3&5\end{pmatrix}=\begin{pmatrix}1.25&-0.75\\-0.75&1.25\end{pmatrix}
$$

**고윳값** — $\det(\mathbf{S}-\lambda I)=(1.25-\lambda)^2-0.75^2=0\Rightarrow 1.25-\lambda=\pm0.75\Rightarrow \lambda=2\ \text{또는}\ 0.5$.

**제1 주성분** — 최대 고윳값 $\lambda_1=2$에 대응하는 고유벡터. $(\mathbf{S}-2I)\mathbf{v}=0$에서 $-0.75v_1-0.75v_2=0\Rightarrow v_1=-v_2$이므로

$$
\boxed{\ \mathbf{v}_1\propto(1,-1),\quad \tfrac{1}{\sqrt2}(1,-1)\ }\qquad(\lambda_1=2)
$$

데이터가 $(2,0),(3,1)$과 $(0,2),(1,3)$처럼 $(1,-1)$ 방향으로 가장 넓게 퍼져 있어 자연스러운 결과다.

👉 [실습(Python)에서 공분산·고유분해 계산](./lab-10)
:::
