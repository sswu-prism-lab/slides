# 문제 7 · 선형 판별 함수

::: info 문제 7 — 선형 판별 함수
두 클래스의 데이터가 각각 다음과 같이 주어졌다.

$$
\mathbf{x}_1=\{(0,0),(1,0),(0,1)\},\qquad \mathbf{x}_2=\{(2,1),(3,1),(2,2)\}
$$

이 때, 피셔 선형 판별<span class="gloss">Fisher's linear discriminant</span>을 적용하여 결정 경계를 구하라.

임의의 $2\times2$ 행렬 $\begin{pmatrix} a & b\\ c & d \end{pmatrix}$의 역행렬은 $\dfrac{1}{ad-bc}\begin{pmatrix} d & -b\\ -c & a \end{pmatrix}$로 구한다.

---

피셔 선형 판별을 구하기 위해 클래스 간 분산<span class="gloss">between class variance</span>과 클래스 내 분산<span class="gloss">within class variance</span>을 사용해야 한다.

$$
\begin{gathered}
\mathbf{S}_{\mathrm{B}}=(\mathbf{m}_2-\mathbf{m}_1)(\mathbf{m}_2-\mathbf{m}_1)^{\top}\\
\mathbf{S}_{\mathrm{W}}=\sum_{n\in\mathcal{C}_1}(\mathbf{x}_n-\mathbf{m}_1)(\mathbf{x}_n-\mathbf{m}_1)^{\top}+\sum_{n\in\mathcal{C}_2}(\mathbf{x}_n-\mathbf{m}_2)(\mathbf{x}_n-\mathbf{m}_2)^{\top}
\end{gathered}
$$

이후 분류기 매개변수를 $\mathbf{w}\propto\mathbf{S}_{\mathrm{W}}^{-1}(\mathbf{m}_2-\mathbf{m}_1)$로 찾고, 두 클래스 평균을 투영한 중심점이 결정 경계가 된다.
:::

::: details 풀이 및 해설
**클래스 평균**:

$$
\mathbf{m}_1=\tfrac{1}{3}\big[(0,0)+(1,0)+(0,1)\big]=\left(\tfrac{1}{3},\tfrac{1}{3}\right),\qquad
\mathbf{m}_2=\left(\tfrac{7}{3},\tfrac{4}{3}\right),\qquad
\mathbf{m}_2-\mathbf{m}_1=(2,1)
$$

**클래스 내 산포 행렬** — 두 클래스가 동일한 삼각형 배치를 가지므로 각 클래스의 산포가 같다.

$$
\sum_{n\in\mathcal{C}_1}(\mathbf{x}_n-\mathbf{m}_1)(\mathbf{x}_n-\mathbf{m}_1)^\top=\begin{pmatrix}\tfrac{2}{3}&-\tfrac{1}{3}\\[2pt]-\tfrac{1}{3}&\tfrac{2}{3}\end{pmatrix}
\;=\;\sum_{n\in\mathcal{C}_2}(\mathbf{x}_n-\mathbf{m}_2)(\mathbf{x}_n-\mathbf{m}_2)^\top
$$

$$
\mathbf{S}_{\mathrm{W}}=\begin{pmatrix}\tfrac{4}{3}&-\tfrac{2}{3}\\[2pt]-\tfrac{2}{3}&\tfrac{4}{3}\end{pmatrix}
$$

**역행렬** — $\det\mathbf{S}_{\mathrm{W}}=\tfrac{16}{9}-\tfrac{4}{9}=\tfrac{12}{9}=\tfrac{4}{3}$이므로

$$
\mathbf{S}_{\mathrm{W}}^{-1}=\frac{3}{4}\begin{pmatrix}\tfrac{4}{3}&\tfrac{2}{3}\\[2pt]\tfrac{2}{3}&\tfrac{4}{3}\end{pmatrix}=\begin{pmatrix}1&\tfrac{1}{2}\\[2pt]\tfrac{1}{2}&1\end{pmatrix}
$$

**판별 방향**:

$$
\mathbf{w}\propto\mathbf{S}_{\mathrm{W}}^{-1}(\mathbf{m}_2-\mathbf{m}_1)=\begin{pmatrix}1&\tfrac{1}{2}\\[2pt]\tfrac{1}{2}&1\end{pmatrix}\begin{pmatrix}2\\1\end{pmatrix}=\begin{pmatrix}\tfrac{5}{2}\\2\end{pmatrix}\ \propto\ \begin{pmatrix}5\\4\end{pmatrix}
$$

**결정 경계** — 두 평균의 중점 $\tfrac{1}{2}(\mathbf{m}_1+\mathbf{m}_2)=\left(\tfrac{4}{3},\tfrac{5}{6}\right)$을 $\mathbf{w}$로 투영한 값이 임곗값이 된다. $\mathbf{w}=(5,4)$로 두면

$$
\mathbf{w}^\top\mathbf{x}=\mathbf{w}^\top\!\left(\tfrac{4}{3},\tfrac{5}{6}\right)=5\cdot\tfrac{4}{3}+4\cdot\tfrac{5}{6}=10
$$

$$
\boxed{\ 5x_1+4x_2=10\ }
$$

이 직선을 기준으로 $\mathbf{w}^\top\mathbf{x}<10$이면 $\mathcal{C}_1$, $>10$이면 $\mathcal{C}_2$로 분류한다.

👉 [실습(Python)에서 산포 행렬과 경계 계산](./lab-07)
:::
