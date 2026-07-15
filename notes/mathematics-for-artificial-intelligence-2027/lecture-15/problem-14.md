# 문제 14 · 행렬함수의 도함수

::: info 문제 14 [3점]
함수 $\mathbf{F}(t)$에 대해 $\dfrac{d\mathbf{F}}{dt}$를 구하시오.

$$
\mathbf{F}(t)=\begin{pmatrix}
e^{2t} & t^3\\
\sin t & \dfrac{1}{t+1}
\end{pmatrix}
$$
:::

::: details 풀이 및 해설
행렬값 함수<span class="gloss">matrix-valued function</span>의 도함수는 각 성분을 $t$에 대해 따로 미분하여 얻는다.

- $\dfrac{d}{dt}e^{2t}=2e^{2t}$,
- $\dfrac{d}{dt}t^3=3t^2$,
- $\dfrac{d}{dt}\sin t=\cos t$,
- $\dfrac{d}{dt}\dfrac{1}{t+1}=-\dfrac{1}{(t+1)^2}$.

따라서

$$
\boxed{\;\frac{d\mathbf{F}}{dt}=\begin{pmatrix}
2e^{2t} & 3t^2\\
\cos t & -\dfrac{1}{(t+1)^2}
\end{pmatrix}\;}
$$

👉 [실습(Python)에서 확인하기](./lab-14)
:::
