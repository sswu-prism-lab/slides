# 문제 3 · 라그랑제 승수법 (3변수)

::: info 문제 3 [4점]
함수 $f(x,y,z)=x^2+2y^2+3z^2$에 대해, 제약 조건 $x+y+z=1$ 하에서 최적점을 구하고 이 최적점이 최대인지 최소인지 판별하시오.
:::

::: details 풀이 및 해설
라그랑제 함수 $\mathcal{L}=x^2+2y^2+3z^2+\lambda(x+y+z-1)$의 정류 조건:

$$
2x+\lambda=0,\qquad 4y+\lambda=0,\qquad 6z+\lambda=0
$$

따라서 $x=-\tfrac{\lambda}{2},\ y=-\tfrac{\lambda}{4},\ z=-\tfrac{\lambda}{6}$. 제약에 대입하면

$$
-\lambda\left(\tfrac{1}{2}+\tfrac{1}{4}+\tfrac{1}{6}\right)=1\ \Longrightarrow\ -\lambda\cdot\tfrac{11}{12}=1\ \Longrightarrow\ \lambda=-\tfrac{12}{11}
$$

$$
\boxed{\ (x,y,z)=\left(\tfrac{6}{11},\tfrac{3}{11},\tfrac{2}{11}\right)\ }
$$

$$
f=\left(\tfrac{6}{11}\right)^2+2\left(\tfrac{3}{11}\right)^2+3\left(\tfrac{2}{11}\right)^2=\frac{36+18+12}{121}=\frac{66}{121}=\boxed{\dfrac{6}{11}}\approx0.545
$$

**판별** — 목적함수의 헤세 $\mathbf{H}=\mathrm{diag}(2,4,6)$은 고윳값이 모두 양수(양의 정부호)이므로 정류점은 **최소**이다. 제약 평면 위에서 원점에서 멀어지면 $f\to\infty$이므로 유한한 최댓값은 없다.

👉 [실습(Python)에서 확인하기](./lab-3)
:::
