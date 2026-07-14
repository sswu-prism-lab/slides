# 문제 2 · 기댓값과 분산

::: info 문제 2 — 기본 확률 법칙들
두 개의 동전을 각각 던져서 앞면이 나올 확률이 서로 독립적으로 다르게 설정되어 있다. 첫 번째 동전은 공정한 동전이며, 두 번째 동전은 편향된 동전으로 앞면이 나올 확률이 $75\%$이다.

이 때, 공정한 주사위를 던져서 나온 눈의 수를 $X$라고 정의하고, $X$만큼 첫 번째 동전을 던져 나온 앞면의 갯수를 $Y$, $X$만큼 두 번째 동전을 던져 나온 앞면의 갯수를 $Z$라고 하자.

$Y$, $Z$, $Y+Z$의 기댓값<span class="gloss">expectation</span>과 분산<span class="gloss">variance</span>을 구하시오.

---

이항 분포, 기댓값, 분산, 공분산의 정의를 사용해야 한다.

$$
\begin{gathered}
\mathbb{E}[f]=\sum_x p(x)f(x)\quad\text{(이산 분포)}\qquad
\mathrm{var}[f]=\mathbb{E}[f(x)^2]-\mathbb{E}[f(x)]^2\\[2pt]
\mathrm{cov}[x,y]=\mathbb{E}_{x,y}[xy]-\mathbb{E}[x]\mathbb{E}[y]\qquad
\mathrm{Bin}(m\mid N,\mu)=\binom{N}{m}\mu^m (1-\mu)^{N-m}\\[2pt]
\text{앞면이 } m \text{번 관찰된 이항 분포:}\quad \mathbb{E}[m]=N\mu,\quad \mathrm{var}[m]=N\mu(1-\mu)
\end{gathered}
$$
:::

::: details 풀이 및 해설
공정한 주사위이므로 $P(X=k)=\tfrac{1}{6}$ $(k=1,\ldots,6)$이고, 조건부 확률변수는 다음과 같다.

$$
\begin{gathered}
Y\mid X=k\sim\mathrm{Bin}(k,\tfrac{1}{2})\Rightarrow \mathbb{E}[Y\mid X]=\tfrac{X}{2},\quad \mathrm{var}[Y\mid X]=\tfrac{X}{4}\\
Z\mid X=k\sim\mathrm{Bin}(k,\tfrac{3}{4})\Rightarrow \mathbb{E}[Z\mid X]=\tfrac{3X}{4},\quad \mathrm{var}[Z\mid X]=\tfrac{3X}{16}
\end{gathered}
$$

**기댓값** — 전확률(반복 기댓값)에 의해 $\mathbb{E}[Y]=\mathbb{E}\!\left[\mathbb{E}[Y\mid X]\right]$이다. $X$가 공정한 주사위이므로 $\mathbb{E}[X]=\tfrac{1+\cdots+6}{6}=\tfrac{7}{2}$, $\mathrm{var}[X]=\mathbb{E}[X^2]-\mathbb{E}[X]^2=\tfrac{35}{12}$.

$$
\mathbb{E}[Y]=\tfrac{1}{2}\mathbb{E}[X]=\frac{7}{4},\qquad
\mathbb{E}[Z]=\tfrac{3}{4}\mathbb{E}[X]=\frac{21}{8},\qquad
\mathbb{E}[Y+Z]=\frac{35}{8}
$$

**분산** — 전분산 공식 $\mathrm{var}[Y]=\mathbb{E}\!\left[\mathrm{var}[Y\mid X]\right]+\mathrm{var}\!\left(\mathbb{E}[Y\mid X]\right)$를 사용한다.

$$
\mathrm{var}[Y]=\mathbb{E}\!\left[\tfrac{X}{4}\right]+\mathrm{var}\!\left[\tfrac{X}{2}\right]=\tfrac{\mathbb{E}[X]}{4}+\tfrac{\mathrm{var}[X]}{4}=\frac{77}{48}
$$

$$
\mathrm{var}[Z]=\mathbb{E}\!\left[\tfrac{3X}{16}\right]+\mathrm{var}\!\left[\tfrac{3X}{4}\right]=\tfrac{3\mathbb{E}[X]}{16}+\tfrac{9\,\mathrm{var}[X]}{16}=\frac{147}{64}
$$

**합의 분산** — $\mathrm{var}[Y+Z]=\mathrm{var}[Y]+\mathrm{var}[Z]+2\,\mathrm{cov}[Y,Z]$이며, 공분산은 조건부 공분산 분해로 계산한다.

$$
\mathrm{cov}[Y,Z]=\underbrace{\mathbb{E}\!\left[\mathrm{cov}[Y,Z\mid X]\right]}_{=\,0\ (Y,Z\text{ 조건부 독립})}+\mathrm{cov}\!\left(\mathbb{E}[Y\mid X],\mathbb{E}[Z\mid X]\right)=\mathrm{cov}\!\left[\tfrac{X}{2},\tfrac{3X}{4}\right]=\tfrac{3}{8}\mathrm{var}[X]=\frac{35}{32}
$$

$$
\therefore\ \mathrm{var}[Y+Z]=\frac{77}{48}+\frac{147}{64}+2\cdot\frac{35}{32}=\boxed{\dfrac{1169}{192}}\approx 6.089
$$

정리하면 $\mathbb{E}[Y]=\tfrac74,\ \mathbb{E}[Z]=\tfrac{21}{8},\ \mathbb{E}[Y+Z]=\tfrac{35}{8}$, $\mathrm{var}[Y]=\tfrac{77}{48},\ \mathrm{var}[Z]=\tfrac{147}{64},\ \mathrm{var}[Y+Z]=\tfrac{1169}{192}$.

👉 [실습(Python)에서 몬테카를로로 검증하기](./lab-02)
:::
