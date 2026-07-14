# 문제 5 · 라그랑제 승수법

::: info 문제 5 — 라그랑제 승수법
아래와 같은 다변수함수가 주어졌다.

$$
f(x,y,z)=x^2+y^2+z^2
$$

아래의 제약 조건 하에서, 위 다변수함수의 최적점과 최솟값, 최댓값을 구하라.

$$
g(x,y,z)=x+y+2z-4=0
$$

헤세 행렬<span class="gloss">Hessian matrix</span>이 양의 정부호<span class="gloss">positive definite</span>라면 정류점은 최소가 되고, 그렇지 않다면 최대가 되는 사실을 사용하라.

---

라그랑제 승수법을 적용하여 라그랑제 함수를 구성한 후, 각 변수들에 대해 미분하여 얻은 연립방정식을 풀어야 한다.

$$
\mathcal{L}(x,y,z,\lambda)=f(x,y,z)+\lambda\,g(x,y,z)
$$

헤세 행렬을 구하여 부호를 판별하여야 한다.

$$
\mathbf{H}=\begin{pmatrix}
\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} & \frac{\partial^2 f}{\partial x \partial z} \\[2pt]
\frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} & \frac{\partial^2 f}{\partial y \partial z} \\[2pt]
\frac{\partial^2 f}{\partial z \partial x} & \frac{\partial^2 f}{\partial z \partial y} & \frac{\partial^2 f}{\partial z^2}
\end{pmatrix}
$$
:::

::: details 풀이 및 해설
**라그랑제 함수** 구성:

$$
\mathcal{L}(x,y,z,\lambda)=x^2+y^2+z^2+\lambda(x+y+2z-4)
$$

**연립방정식** — 각 변수로 편미분하여 $0$으로 둔다.

$$
\frac{\partial\mathcal{L}}{\partial x}=2x+\lambda=0,\quad
\frac{\partial\mathcal{L}}{\partial y}=2y+\lambda=0,\quad
\frac{\partial\mathcal{L}}{\partial z}=2z+2\lambda=0
$$

따라서 $x=-\tfrac{\lambda}{2}$, $y=-\tfrac{\lambda}{2}$, $z=-\lambda$. 제약 $x+y+2z=4$에 대입하면

$$
-\tfrac{\lambda}{2}-\tfrac{\lambda}{2}-2\lambda=4\ \Longrightarrow\ -3\lambda=4\ \Longrightarrow\ \lambda=-\tfrac{4}{3}
$$

**정류점**:

$$
\boxed{\ (x,y,z)=\left(\tfrac{2}{3},\ \tfrac{2}{3},\ \tfrac{4}{3}\right)\ }
$$

이 점에서의 함수값:

$$
f=\left(\tfrac{2}{3}\right)^2+\left(\tfrac{2}{3}\right)^2+\left(\tfrac{4}{3}\right)^2=\frac{4+4+16}{9}=\frac{24}{9}=\boxed{\dfrac{8}{3}}\approx 2.667
$$

**헤세 행렬**:

$$
\mathbf{H}=\begin{pmatrix}2&0&0\\0&2&0\\0&0&2\end{pmatrix}=2\mathbf{I}
$$

고윳값이 모두 $2>0$이므로 $\mathbf{H}$는 **양의 정부호**이고, 따라서 정류점은 **최솟값** $\tfrac{8}{3}$이다.

**최댓값에 대하여** — 제약 평면 위에서 원점으로부터 멀어지면 $x^2+y^2+z^2\to\infty$이므로 **유한한 최댓값은 존재하지 않는다**. 기하학적으로 이 문제는 평면 $x+y+2z=4$까지의 최단 거리의 제곱을 구하는 것과 같으며, 그 값이 $\tfrac{8}{3}$이다 (평면까지의 거리 $\tfrac{4}{\sqrt{6}}$의 제곱).
:::
