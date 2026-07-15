# 문제 11 · 전치행렬 $(AB)^\top=B^\top A^\top$

::: info 문제 11 [3점]
다음 두 행렬 $A$와 $B$에 대해, $(AB)^\top$과 $B^\top A^\top$을 구하시오.

$$
A=\begin{pmatrix}
1 & 2 & 0\\
-1 & 3 & 2
\end{pmatrix},\qquad
B=\begin{pmatrix}
2 & 1\\
-1 & 4\\
0 & 3
\end{pmatrix}
$$
:::

::: details 풀이 및 해설
**곱 $AB$ 계산** — $A$는 $2\times3$, $B$는 $3\times2$ 이므로 $AB$는 $2\times2$ 이다.

$$
AB=\begin{pmatrix}
1\cdot2+2\cdot(-1)+0\cdot0 & 1\cdot1+2\cdot4+0\cdot3\\
-1\cdot2+3\cdot(-1)+2\cdot0 & -1\cdot1+3\cdot4+2\cdot3
\end{pmatrix}
=\begin{pmatrix}0 & 9\\ -5 & 17\end{pmatrix}.
$$

전치하면

$$
(AB)^\top=\begin{pmatrix}0 & -5\\ 9 & 17\end{pmatrix}.
$$

**$B^\top A^\top$ 계산** — $B^\top=\begin{pmatrix}2&-1&0\\1&4&3\end{pmatrix}$, $A^\top=\begin{pmatrix}1&-1\\2&3\\0&2\end{pmatrix}$ 이므로

$$
B^\top A^\top=\begin{pmatrix}
2\cdot1+(-1)\cdot2+0\cdot0 & 2\cdot(-1)+(-1)\cdot3+0\cdot2\\
1\cdot1+4\cdot2+3\cdot0 & 1\cdot(-1)+4\cdot3+3\cdot2
\end{pmatrix}
=\begin{pmatrix}0 & -5\\ 9 & 17\end{pmatrix}.
$$

두 결과가 일치하여 전치의 성질 $(AB)^\top=B^\top A^\top$ 을 확인할 수 있다.

$$
\boxed{\;(AB)^\top=B^\top A^\top=\begin{pmatrix}0 & -5\\ 9 & 17\end{pmatrix}\;}
$$

👉 [실습(Python)에서 확인하기](./lab-11)
:::
