# 문제 4 · 최소제곱법 (이차 다항식 회귀)

::: info 문제 4 [6점]
아래와 같은 이차 다항식 형태의 회귀<span class="gloss">regression</span> 모델이 있다.

$$
t=w_0+w_1 x+w_2 x^2
$$

다음과 같은 데이터가 주어졌을 때 최소제곱법을 이용하여 $w_0$, $w_1$, $w_2$를 구하시오.

$$
\{(x_i,t_i)\}=\{(0,1),(1,2),(2,1),(3,4)\}
$$
:::

::: details 풀이 및 해설
설계 행렬 $\mathbf{X}$의 $i$번째 행을 $[\,1,\ x_i,\ x_i^2\,]$로 두면 정규방정식은 $\mathbf{X}^\top\mathbf{X}\,\mathbf{w}=\mathbf{X}^\top\mathbf{t}$이다.

$$
\mathbf{X}=\begin{pmatrix}1&0&0\\1&1&1\\1&2&4\\1&3&9\end{pmatrix},\qquad \mathbf{t}=\begin{pmatrix}1\\2\\1\\4\end{pmatrix}
$$

필요한 합: $\sum x=6,\ \sum x^2=14,\ \sum x^3=36,\ \sum x^4=98,\ \sum t=8,\ \sum x t=16,\ \sum x^2 t=42$.

$$
\mathbf{X}^\top\mathbf{X}=\begin{pmatrix}4&6&14\\6&14&36\\14&36&98\end{pmatrix},\qquad
\mathbf{X}^\top\mathbf{t}=\begin{pmatrix}8\\16\\42\end{pmatrix}
$$

이 $3\times3$ 연립방정식을 풀면

$$
\boxed{\ w_0=1.3,\qquad w_1=-0.7,\qquad w_2=0.5\ }
$$

즉 $\hat t=0.5x^2-0.7x+1.3$이며, 각 점에서의 예측값은 $(1.3,\ 1.1,\ 1.9,\ 3.7)$이다.

👉 [실습(Python)에서 정규방정식 풀기](./lab-4)
:::
