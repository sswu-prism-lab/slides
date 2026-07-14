# 문제 5 · 피셔 선형 판별

::: info 문제 5 [6점]
아래와 같은 두 클래스 데이터셋에 대해, 피셔의 선형 판별<span class="gloss">Fisher's linear discriminant</span>을 적용하여 최적의 선형 투영 벡터 $\mathbf{w}$를 구하시오.

$$
\mathbf{x}_1=\{(2,3),(3,3),(3,2)\},\qquad
\mathbf{x}_2=\{(6,5),(7,8),(8,6)\}
$$
:::

::: details 풀이 및 해설
**클래스 평균**:

$$
\mathbf{m}_1=\left(\tfrac{8}{3},\tfrac{8}{3}\right),\qquad
\mathbf{m}_2=\left(7,\tfrac{19}{3}\right),\qquad
\mathbf{m}_2-\mathbf{m}_1=\left(\tfrac{13}{3},\tfrac{11}{3}\right)
$$

**클래스 내 산포 행렬** $\mathbf{S}_{\mathrm{W}}=\sum_{\mathcal{C}_1}(\mathbf{x}-\mathbf{m}_1)(\mathbf{x}-\mathbf{m}_1)^\top+\sum_{\mathcal{C}_2}(\mathbf{x}-\mathbf{m}_2)(\mathbf{x}-\mathbf{m}_2)^\top$:

$$
\mathbf{S}_{\mathrm{W}}=\begin{pmatrix}\tfrac{2}{3}&-\tfrac{1}{3}\\[2pt]-\tfrac{1}{3}&\tfrac{2}{3}\end{pmatrix}+\begin{pmatrix}2&1\\1&\tfrac{14}{3}\end{pmatrix}=\begin{pmatrix}\tfrac{8}{3}&\tfrac{2}{3}\\[2pt]\tfrac{2}{3}&\tfrac{16}{3}\end{pmatrix}
$$

**역행렬** — $\det\mathbf{S}_{\mathrm{W}}=\tfrac{8}{3}\cdot\tfrac{16}{3}-\left(\tfrac{2}{3}\right)^2=\tfrac{124}{9}$이므로

$$
\mathbf{S}_{\mathrm{W}}^{-1}=\frac{9}{124}\begin{pmatrix}\tfrac{16}{3}&-\tfrac{2}{3}\\[2pt]-\tfrac{2}{3}&\tfrac{8}{3}\end{pmatrix}=\frac{3}{124}\begin{pmatrix}16&-2\\-2&8\end{pmatrix}
$$

**투영 벡터**:

$$
\mathbf{w}\propto\mathbf{S}_{\mathrm{W}}^{-1}(\mathbf{m}_2-\mathbf{m}_1)=\frac{3}{124}\begin{pmatrix}16&-2\\-2&8\end{pmatrix}\begin{pmatrix}\tfrac{13}{3}\\[2pt]\tfrac{11}{3}\end{pmatrix}=\begin{pmatrix}\tfrac{3}{2}\\[2pt]\tfrac{1}{2}\end{pmatrix}\ \propto\ \boxed{\begin{pmatrix}3\\1\end{pmatrix}}
$$

즉 최적 투영 방향은 $\mathbf{w}\propto(3,1)^\top$이다. (필요하면 $\mathbf{w}/\|\mathbf{w}\|=(3,1)/\sqrt{10}$로 정규화한다.)

👉 [실습(Python)에서 산포 행렬과 $\mathbf{w}$ 계산](./lab-5)
:::
