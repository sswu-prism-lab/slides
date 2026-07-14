# 문제 3 · 피셔 선형 판별

::: info 문제 3 [4점]
아래와 같은 두 클래스 데이터셋에 대해, 피셔의 선형 판별<span class="gloss">Fisher's linear discriminant</span>을 적용하여 최적의 선형 투영 벡터 $\mathbf{w}$를 구하시오.

$$
\mathbf{x}_1=\{(2,3),(3,3),(3,2)\},\qquad \mathbf{x}_2=\{(6,5),(7,8),(8,6)\}
$$
:::

::: details 풀이 및 해설
클래스 평균 $\mathbf{m}_1=(\tfrac83,\tfrac83)$, $\mathbf{m}_2=(7,\tfrac{19}{3})$, $\mathbf{m}_2-\mathbf{m}_1=(\tfrac{13}{3},\tfrac{11}{3})$. 클래스 내 산포 행렬은

$$
\mathbf{S}_{\mathrm{W}}=\begin{pmatrix}\tfrac83&\tfrac23\\[2pt]\tfrac23&\tfrac{16}{3}\end{pmatrix},\qquad \det\mathbf{S}_{\mathrm{W}}=\tfrac{124}{9},\qquad \mathbf{S}_{\mathrm{W}}^{-1}=\frac{3}{124}\begin{pmatrix}16&-2\\-2&8\end{pmatrix}
$$

$$
\mathbf{w}\propto\mathbf{S}_{\mathrm{W}}^{-1}(\mathbf{m}_2-\mathbf{m}_1)=\begin{pmatrix}\tfrac32\\[2pt]\tfrac12\end{pmatrix}\ \propto\ \boxed{(3,\ 1)}
$$

즉 최적 투영 방향은 $\mathbf{w}\propto(3,1)^\top$이다(정규화 시 $(3,1)/\sqrt{10}$).

👉 [실습(Python)에서 계산하기](./lab-03)
:::
