# 문제 8 · 확률적 분류 모델

::: info 문제 8 — 확률적 분류 모델
두 클래스 $\mathcal{C}_1$과 $\mathcal{C}_2$에 대해, 각 사전확률은 $0.5$로 같고, 클래스 조건부 밀도는 다음과 같은 이변량 정규분포를 따른다.

$$
p(\mathbf{x}\mid\mathcal{C}_1)\sim\mathcal{N}\!\left(\binom{1}{1},\begin{pmatrix}1&0\\0&1\end{pmatrix}\right),\qquad
p(\mathbf{x}\mid\mathcal{C}_2)\sim\mathcal{N}\!\left(\binom{1}{1},\begin{pmatrix}2&1\\1&2\end{pmatrix}\right)
$$

이 모델의 결정 경계를 명확히 유도하고, 그 경계가 선형인지 아닌지를 판단하시오.

두 클래스 밀도의 공분산 행렬이 단위 행렬<span class="gloss">identity matrix</span>로 같다고 가정하면 결정 경계가 어떻게 바뀌는지 기술하고, 그 경계가 선형인지 아닌지를 판단하시오.

---

선형 판별 분석<span class="gloss">linear discriminant analysis</span> 문제에서 공분산이 같지 않은 경우에 관한 문제이다. 우선 공분산이 같지 않은 경우 분류기가 어떻게 변하는지 기술한 다음 각 값을 대입하면 되며, 공분산이 같다고 가정하면 문제가 LDA를 모델링하는 것으로 간단해진다.
:::

::: details 풀이 및 해설
사전확률이 같고 $0$–$1$ 손실을 가정하면, 결정 규칙은 우도(로그 판별식) 비교로 귀결된다. 각 클래스의 로그 판별식은

$$
g_k(\mathbf{x})=-\tfrac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_k)^\top\boldsymbol{\Sigma}_k^{-1}(\mathbf{x}-\boldsymbol{\mu}_k)-\tfrac{1}{2}\ln|\boldsymbol{\Sigma}_k|+\ln p(\mathcal{C}_k)
$$

경계는 $g_1(\mathbf{x})=g_2(\mathbf{x})$이다. **두 평균이 $\boldsymbol{\mu}_1=\boldsymbol{\mu}_2=(1,1)^\top$로 같다는 점**이 핵심이다.

**(1) 공분산이 다른 경우 (QDA)** — $\boldsymbol{\Sigma}_1=\mathbf{I}$, $\boldsymbol{\Sigma}_2=\begin{pmatrix}2&1\\1&2\end{pmatrix}$. 평균이 같으므로 선형항이 소거되고 순수 이차형식만 남는다. $\mathbf{u}=\mathbf{x}-\boldsymbol{\mu}$라 하면

$$
\mathbf{u}^\top\!\left(\boldsymbol{\Sigma}_1^{-1}-\boldsymbol{\Sigma}_2^{-1}\right)\mathbf{u}=\ln\frac{|\boldsymbol{\Sigma}_2|}{|\boldsymbol{\Sigma}_1|}
$$

$|\boldsymbol{\Sigma}_2|=3$, $\boldsymbol{\Sigma}_2^{-1}=\tfrac{1}{3}\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$이므로

$$
\boldsymbol{\Sigma}_1^{-1}-\boldsymbol{\Sigma}_2^{-1}=\begin{pmatrix}1&0\\0&1\end{pmatrix}-\tfrac{1}{3}\begin{pmatrix}2&-1\\-1&2\end{pmatrix}=\tfrac{1}{3}\begin{pmatrix}1&1\\1&1\end{pmatrix}
$$

$$
\boxed{\ \tfrac{1}{3}\big[(x_1-1)+(x_2-1)\big]^2=\ln 3\ }
$$

이는 $\mathbf{x}$에 대한 **이차식**이므로 결정 경계는 **비선형**(정확히는 $(x_1-1)+(x_2-1)=\pm\sqrt{3\ln3}$ 형태의 평행한 두 직선 쌍)이다. 공분산이 서로 다르면 이차항이 소거되지 않아 QDA가 되어 경계가 곡선(또는 이 경우처럼 한 방향의 이차식)이 된다.

**(2) 공분산을 둘 다 $\mathbf{I}$로 가정** — 이제 $\boldsymbol{\Sigma}_1=\boldsymbol{\Sigma}_2=\mathbf{I}$이므로 이차항이 완전히 소거되어 LDA가 된다. 판별 방향은

$$
\mathbf{w}=\boldsymbol{\Sigma}^{-1}(\boldsymbol{\mu}_1-\boldsymbol{\mu}_2)=\mathbf{I}\cdot\mathbf{0}=\mathbf{0}
$$

그런데 두 평균마저 같으므로 두 클래스의 분포가 **완전히 동일**해진다. 따라서 모든 $\mathbf{x}$에서 $p(\mathbf{x}\mid\mathcal{C}_1)=p(\mathbf{x}\mid\mathcal{C}_2)$이고 사후확률도 사전확률($0.5$)로 같아, **의미 있는 결정 경계가 존재하지 않는다**(어느 클래스로 분류해도 기대 위험이 동일). 형식적으로는 $\mathbf{w}=\mathbf{0}$인 퇴화된 선형 경계로, 데이터로는 두 클래스를 구분할 수 없다.
:::
