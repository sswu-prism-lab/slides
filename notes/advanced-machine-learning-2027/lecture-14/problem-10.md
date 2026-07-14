# 문제 10 · 주성분 분석

::: info 문제 10 — 주성분 분석
아래 3개의 관측값이 주어졌다.

$$
\{(1,0),(0,1),(1,1)\}
$$

이 관측값들의 제 1 주성분을 구하시오.

---

평균을 $\bar{\mathbf{x}}$라 할 때 공분산 행렬은 $\mathbf{S}=\dfrac{1}{N}\sum_{n=1}^{N}(\mathbf{x}_n-\bar{\mathbf{x}})(\mathbf{x}_n-\bar{\mathbf{x}})^\top$이다. 행렬 $A$의 고윳값 $\lambda$는 특성방정식 $\det(A-\lambda I)=0$으로 구하며, $\begin{bmatrix}a&b\\c&d\end{bmatrix}$의 행렬식은 $ad-bc$이다.
:::

::: details 풀이 및 해설
**평균**:

$$
\bar{\mathbf{x}}=\left(\frac{1+0+1}{3},\ \frac{0+1+1}{3}\right)=\left(\tfrac23,\tfrac23\right)
$$

**중심화된 데이터**: $\left(\tfrac13,-\tfrac23\right),\ \left(-\tfrac23,\tfrac13\right),\ \left(\tfrac13,\tfrac13\right)$.

**공분산 행렬** ($N=3$):

$$
\mathbf{S}=\frac13\left[\begin{pmatrix}\tfrac19&-\tfrac29\\-\tfrac29&\tfrac49\end{pmatrix}+\begin{pmatrix}\tfrac49&-\tfrac29\\-\tfrac29&\tfrac19\end{pmatrix}+\begin{pmatrix}\tfrac19&\tfrac19\\\tfrac19&\tfrac19\end{pmatrix}\right]=\frac13\begin{pmatrix}\tfrac23&-\tfrac13\\-\tfrac13&\tfrac23\end{pmatrix}=\begin{pmatrix}\tfrac29&-\tfrac19\\-\tfrac19&\tfrac29\end{pmatrix}
$$

**고윳값** — $\det(\mathbf{S}-\lambda I)=\left(\tfrac29-\lambda\right)^2-\left(\tfrac19\right)^2=0$:

$$
\tfrac29-\lambda=\pm\tfrac19\ \Longrightarrow\ \lambda=\tfrac19\ \text{또는}\ \lambda=\tfrac13
$$

**제1 주성분** — 가장 큰 고윳값 $\lambda_1=\tfrac13$에 대응하는 고유벡터. $(\mathbf{S}-\tfrac13 I)\mathbf{v}=0$에서 $-\tfrac19 v_1-\tfrac19 v_2=0\Rightarrow v_1=-v_2$이므로

$$
\boxed{\ \mathbf{v}_1\propto(1,-1),\quad \text{정규화 } \frac{1}{\sqrt2}(1,-1)\ }\qquad(\lambda_1=\tfrac13)
$$

즉 데이터 분산이 최대인 방향은 $(1,-1)$이다. 두 점 $(1,0),(0,1)$이 이 축을 따라 크게 퍼져 있어 자연스러운 결과다.

👉 [실습(Python)에서 공분산·고유분해 계산](./lab-10)
:::
