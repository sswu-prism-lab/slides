# 문제 3 · 라그랑제 승수법

::: info 문제 3 [4점]
함수 $f(x,y)=x^2+2y^2$에 대해, 제약 조건 $x+y=3$ 하에서 최적점을 구하고 이 최적점이 최대인지 최소인지 판별하시오.
:::

::: details 풀이 및 해설
라그랑제 함수 $\mathcal{L}=x^2+2y^2+\lambda(x+y-3)$의 정류 조건:

$$
\frac{\partial\mathcal{L}}{\partial x}=2x+\lambda=0,\qquad
\frac{\partial\mathcal{L}}{\partial y}=4y+\lambda=0
$$

두 식에서 $2x=4y\Rightarrow x=2y$. 제약 $x+y=3$에 대입하면 $2y+y=3\Rightarrow y=1,\ x=2$.

$$
\boxed{\ (x,y)=(2,1),\qquad f=2^2+2\cdot1^2=6\ }
$$

**판별** — 제약 $x=3-y$를 대입한 $\tilde f(y)=(3-y)^2+2y^2=3y^2-6y+9$는 $\tilde f''=6>0$(아래로 볼록)이므로 정류점은 **최소**이다. (제약 위에서 $y\to\pm\infty$면 $f\to\infty$이므로 최댓값은 없다.) 목적함수의 헤세 $\mathbf{H}=\mathrm{diag}(2,4)$가 양의 정부호인 것과도 일치한다.

👉 [실습(Python)에서 확인하기](./lab-3)
:::
