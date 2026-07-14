# 문제 6 · 최소제곱법

::: info 문제 6 — 최소제곱법
어떤 데이터셋 $\{(x_i, t_i)\mid i=1,\ldots,N\}$에 대해, 다음과 같은 선형 회귀<span class="gloss">linear regression</span> 모델이 있다.

$$
t_i=w_1 x_i+w_0+\epsilon_i,\qquad \epsilon_i\sim\mathcal{N}(0,\sigma^2)
$$

이 때, 각 매개변수 $w_1$, $w_0$가 최소제곱법<span class="gloss">least square method</span>을 통해 다음의 목적함수를 최소화하여 얻어진다고 가정하자.

$$
J(w_0,w_1)=\sum_{i=1}^{N}(t_i-w_1 x_i-w_0)^2
$$

이 때, 각 매개변수를 추정하는 정규 방정식<span class="gloss">normal equation</span>을 행렬 형태로 명확히 작성하라. 데이터셋이 아래와 같이 주어진 경우, 회귀 매개변수를 추정하라.

$$
\{(x_i,t_i)\}=\{(1,2),(2,4),(4,3),(5,6)\}
$$

---

정규방정식을 유도하려면 목적함수를 각 매개변수로 미분한 결과를 $0$으로 두어 정리하여야 한다.
:::

::: details 풀이 및 해설
**정규방정식 유도** — $J$를 $w_0$, $w_1$에 대해 각각 편미분하여 $0$으로 둔다.

$$
\frac{\partial J}{\partial w_0}=-2\sum_i (t_i-w_1 x_i-w_0)=0,\qquad
\frac{\partial J}{\partial w_1}=-2\sum_i x_i(t_i-w_1 x_i-w_0)=0
$$

정리하면 다음 연립방정식(정규방정식)이 된다.

$$
\begin{pmatrix} N & \sum_i x_i \\ \sum_i x_i & \sum_i x_i^2 \end{pmatrix}
\begin{pmatrix} w_0 \\ w_1 \end{pmatrix}=
\begin{pmatrix} \sum_i t_i \\ \sum_i x_i t_i \end{pmatrix}
$$

설계 행렬 $\mathbf{X}=\begin{pmatrix}1 & x_1\\ \vdots & \vdots\\ 1 & x_N\end{pmatrix}$을 쓰면 $\mathbf{X}^\top\mathbf{X}\,\mathbf{w}=\mathbf{X}^\top\mathbf{t}$, 즉 $\mathbf{w}=(\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{t}$이다.

**수치 대입** — $N=4$, $\sum x_i=12$, $\sum x_i^2=1+4+16+25=46$, $\sum t_i=15$, $\sum x_i t_i=2+8+12+30=52$.

$$
\begin{pmatrix} 4 & 12 \\ 12 & 46 \end{pmatrix}\begin{pmatrix} w_0 \\ w_1 \end{pmatrix}=\begin{pmatrix} 15 \\ 52 \end{pmatrix}
$$

$$
w_1=\frac{N\sum x_i t_i-\sum x_i\sum t_i}{N\sum x_i^2-(\sum x_i)^2}=\frac{4\cdot52-12\cdot15}{4\cdot46-12^2}=\frac{28}{40}=\boxed{0.7}
$$

$$
w_0=\frac{\sum t_i-w_1\sum x_i}{N}=\frac{15-0.7\cdot12}{4}=\frac{6.6}{4}=\boxed{1.65}
$$

따라서 추정된 회귀 직선은 $\hat{t}=0.7\,x+1.65$이다.

👉 [실습(Python)에서 정규방정식 풀기](./lab-06)
:::
