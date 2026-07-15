# 문제 10 · 고윳값과 고유벡터

::: info 문제 10 [3점]
다음 행렬에 대해 고윳값<span class="gloss">eigenvalue</span>과 각 고윳값에 해당하는 고유벡터<span class="gloss">eigenvector</span>를 구하시오.

$$
\begin{pmatrix}
2 & 1\\
0 & 3
\end{pmatrix}
$$
:::

::: details 풀이 및 해설
$A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$ 의 특성방정식<span class="gloss">characteristic equation</span> $\det(A-\lambda I)=0$ 을 세운다.

$$
\det\begin{pmatrix}2-\lambda&1\\0&3-\lambda\end{pmatrix}=(2-\lambda)(3-\lambda)=0.
$$

(상삼각행렬이므로 대각 성분이 곧 고윳값이다.) 따라서

$$
\lambda_1=2,\qquad \lambda_2=3.
$$

**$\lambda_1=2$** — $(A-2I)\mathbf{v}=\begin{pmatrix}0&1\\0&1\end{pmatrix}\mathbf{v}=\mathbf 0$ 에서 $v_2=0$, $v_1$ 은 자유변수이므로

$$
\mathbf{v}_1=\begin{pmatrix}1\\0\end{pmatrix}.
$$

**$\lambda_2=3$** — $(A-3I)\mathbf{v}=\begin{pmatrix}-1&1\\0&0\end{pmatrix}\mathbf{v}=\mathbf 0$ 에서 $-v_1+v_2=0$, 즉 $v_1=v_2$ 이므로

$$
\mathbf{v}_2=\begin{pmatrix}1\\1\end{pmatrix}.
$$

$$
\boxed{\;\lambda_1=2,\ \mathbf v_1=\begin{pmatrix}1\\0\end{pmatrix};\qquad \lambda_2=3,\ \mathbf v_2=\begin{pmatrix}1\\1\end{pmatrix}\;}
$$

고유벡터는 상수배까지만 결정되므로, 수치 라이브러리는 이를 단위벡터로 정규화하여 $\mathbf v_2\approx(0.707,\,0.707)$ 처럼 출력한다.

👉 [실습(Python)에서 확인하기](./lab-10)
:::
