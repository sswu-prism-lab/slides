# 문제 3 · 베이지안 결정 이론

::: info 문제 3 — 베이지안 결정 이론
입력 데이터 $x$에 대해 두 클래스 $\mathcal{C}_1$, $\mathcal{C}_2$ 각각의 조건부 확률 밀도함수가 아래와 같다.

$$
p(x\mid\mathcal{C}_1)\sim\mathcal{N}(1,1^2),\qquad p(x\mid\mathcal{C}_2)\sim\mathcal{N}(3,2^2)
$$

클래스의 사전 확률은 $p(\mathcal{C}_1)=0.4$, $p(\mathcal{C}_2)=0.6$으로 주어지며 아래와 같이 손실 함수가 주어진다.

| 실제 / 예측 | $\hat{\mathcal{C}}_1$ | $\hat{\mathcal{C}}_2$ |
| :---: | :---: | :---: |
| $\mathcal{C}_1$ | $0$ | $5$ |
| $\mathcal{C}_2$ | $1$ | $0$ |

이 때, 최적 결정 규칙을 수식으로 정의하고, 최적 결정 경계를 구하기 위한 방정식을 세우시오.

---

이진 분류의 기대 손실<span class="gloss">expected loss</span>을 이용해야 한다.

$$
\mathbb{E}[L]=\sum_k L_{kj}\,p(\mathcal{C}_k\mid x)
$$
:::

::: details 풀이 및 해설
각 예측에 대한 기대 손실을 계산한다.

$\hat{\mathcal{C}}_1$로 예측하는 경우:

$$
L(\mathcal{C}_1,\hat{\mathcal{C}}_1)p(\mathcal{C}_1\mid x)+L(\mathcal{C}_2,\hat{\mathcal{C}}_1)p(\mathcal{C}_2\mid x)=0\cdot p(\mathcal{C}_1\mid x)+1\cdot p(\mathcal{C}_2\mid x)=p(\mathcal{C}_2\mid x)
$$

$\hat{\mathcal{C}}_2$로 예측하는 경우:

$$
L(\mathcal{C}_1,\hat{\mathcal{C}}_2)p(\mathcal{C}_1\mid x)+L(\mathcal{C}_2,\hat{\mathcal{C}}_2)p(\mathcal{C}_2\mid x)=5\,p(\mathcal{C}_1\mid x)
$$

**최적 결정 규칙** — 기대 손실이 더 작은 쪽으로 결정하므로, $\mathcal{C}_1$으로 결정할 조건은

$$
p(\mathcal{C}_2\mid x)<5\,p(\mathcal{C}_1\mid x)\quad\Longleftrightarrow\quad \frac{p(\mathcal{C}_2\mid x)}{p(\mathcal{C}_1\mid x)}<5
$$

**결정 경계** — 베이즈 정리로 사후비를 우도·사전으로 바꾸고 밀도를 대입한다.

$$
\frac{p(\mathcal{C}_2\mid x)}{p(\mathcal{C}_1\mid x)}=\frac{p(x\mid\mathcal{C}_2)p(\mathcal{C}_2)}{p(x\mid\mathcal{C}_1)p(\mathcal{C}_1)}=\frac{\mathcal{N}(3,2^2)\times0.6}{\mathcal{N}(1,1^2)\times0.4}<5
$$

양변에 로그를 취하고 정리하면 (경계는 등호):

$$
\boxed{\ \ln(0.75)-\frac{(x-3)^2}{8}+\frac{(x-1)^2}{2}-\ln(5)<0\ }
$$

이 부등식을 정리하면 이차식 $3x^2-2x-\left(5+8\ln\tfrac{5}{0.75}\right)=0$이 되어, 두 경계점

$$
x\approx -2.281,\qquad x\approx 2.948
$$

을 얻는다. 분산이 작아 밀도가 뾰족한 $\mathcal{C}_1$이 중앙 구간을 지배하므로, **두 점 사이에서는 $\mathcal{C}_1$, 바깥에서는 $\mathcal{C}_2$** 로 결정한다. (손실이 비대칭이라 경계가 두 밀도의 단순 교점과는 다르다는 점에 유의.)

👉 [실습(Python)에서 결정 경계 재현하기](./lab-03)
:::
