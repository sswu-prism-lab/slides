# 함수

3주차의 함수 해석을 정리한다. 함수의 엄밀한 정의와 성질에서 시작해, 실함수·복소함수·다변수함수를 살펴보고, 함수의 그래프와 이동(평행·대칭·확대축소·회전)으로 마무리한다.

## 함수의 정의와 성질

- 집합 $X$에서 $Y$로의 함수<span class="gloss">function</span> $f:X\mapsto Y$는 각 $x\in X$를 유일한 $y=f(x)\in Y$로 대응시키는 규칙이다. 이때 $y$는 $x$의 상<span class="gloss">image</span>, $x$는 $y$의 원상<span class="gloss">preimage</span>, $X$는 정의역<span class="gloss">domain</span>, $Y$는 공역<span class="gloss">codomain</span>이라 한다.
- 엄밀하게는 함수를 순서쌍<span class="gloss">ordered pair</span>의 집합, 즉 사상<span class="gloss">mapping</span>으로 본다. 예를 들어 $f(x)=x^2$는 $f=\{(x,x^2)\mid x\in\mathbb{R}\}$이다.

$$
f=\{(x, y)\mid x\in X\wedge y\in Y\}\ \text{ s.t. }\ (x, y)\in f \wedge (x, y')\in f\ \Rightarrow\ y=y'
$$

- 함수의 대응 방식에 따라 다음과 같이 분류한다.

::: info 단사 · 전사 · 전단사
- 일대일<span class="gloss">one-to-one</span> 또는 단사<span class="gloss">injective</span>: $x_i\neq x_j \Rightarrow f(x_i)\neq f(x_j)$ (서로 다른 두 점이 같은 상을 갖지 않음).
- 위로의 함수<span class="gloss">onto</span> 또는 전사<span class="gloss">surjective</span>: $f(X)=Y$ (공역의 모든 원소가 상으로 나타남).
- 일대일 대응<span class="gloss">one-to-one correspondence</span> 또는 전단사<span class="gloss">bijective</span>: 단사이면서 전사. 이때 역함수<span class="gloss">inverse function</span> $f^{-1}:Y\mapsto X$가 유일하게 존재한다.
:::

- 항등함수<span class="gloss">identity function</span> $i_X(x)=x$와 합성함수<span class="gloss">composite function</span> $g\circ f$는 다음과 같다.

$$
i_X(x)=x\ (x\in X),\qquad (g\circ f)(x) = g(f(x))\quad (f:X\mapsto Y,\ g:Y\mapsto Z)
$$

- 정의역의 부분마다 다른 식을 쓰는 것을 조각적 정의<span class="gloss">piecewise definition</span>라 한다. 절댓값 함수와 부호함수<span class="gloss">sign function</span>가 그 예이다.

$$
|x|=\begin{cases} x & (x\geq 0)\\ -x & (\text{그 외}) \end{cases},\qquad
\operatorname{sgn}(x)=\begin{cases} +1 & (x>0) \\ 0 & (x=0)\\ -1 & (\text{그 외}) \end{cases}
$$

- 집합 $X$의 관계<span class="gloss">relation</span> $R$은 $X\times X$의 부분집합이다. 다음 세 성질을 만족하는 관계를 동치 관계<span class="gloss">equivalence relation</span>라 한다.

$$
\text{반사적: } xRx,\qquad \text{대칭적: } xRy\Rightarrow yRx,\qquad \text{전이적: } xRy\wedge yRz\Rightarrow xRz
$$

- 함수의 주요 성질: 연속성<span class="gloss">continuity</span>($\lim_{x\to a}f(x)=f(a)$), 미분 가능성<span class="gloss">differentiability</span>(미분 가능하면 연속), 단조성<span class="gloss">monotonicity</span>, 주기성<span class="gloss">periodicity</span>, 대칭성<span class="gloss">symmetry</span>.

$$
\text{단조 증가: } x_1<x_2\Rightarrow f(x_1)\leq f(x_2),\qquad \text{단조 감소: } x_1<x_2\Rightarrow f(x_1)\geq f(x_2)
$$

<PyRunner>

```python
# 유한 집합에서의 단사/전사 판정과 합성함수
X = [1, 2, 3]
Y = [1, 2, 3, 4]
f = {1: 2, 2: 4, 3: 1}            # f: X -> Y

images = list(f.values())
inj = len(set(images)) == len(images)   # 상이 모두 다르면 단사
sur = set(images) == set(Y)             # 공역을 모두 덮으면 전사
print(f"f = {f}")
print(f"단사(injective)? {inj},  전사(surjective)? {sur}")

# 합성함수 g∘f,  g(y) = y^2
g = lambda y: y**2
print("g∘f =", {x: g(f[x]) for x in X})
```

</PyRunner>

## 실함수 · 복소함수 · 다변수함수

- 실함수<span class="gloss">real-valued function</span>는 실수 집합의 부분집합을 정의역, 실수 집합을 공역으로 하는 함수이며, 그 그래프 $\{(x,f(x))\mid x\in D\}$는 평면의 부분집합이다.
- 일차함수<span class="gloss">linear function</span> $f(x)=ax+b$는 기울기(도함수) $a$, $x$절편 $-\tfrac{b}{a}$, $y$절편 $b$를 가지며 단조·일대일 대응이다. 다항함수<span class="gloss">polynomial function</span>의 한 예로 물리·공학에서 중요한 르장드르 함수<span class="gloss">Legendre function</span>가 있다.

$$
P_n(x)=\frac{1}{2^n n!}\frac{\mathrm{d}^n}{\mathrm{d}x^n}(x^2-1)^n
$$

- 공역이 연속이 아닌 함수를 이산함수<span class="gloss">discrete function</span>라 하며, 계단 함수<span class="gloss">step function</span> $u(x)$와 디랙-델타 함수<span class="gloss">Dirac-delta function</span> $\delta_n(x)$가 그 예이다.

$$
u(x)=\begin{cases} 1 & (x\geq 0)\\ 0 & (\text{그 외}) \end{cases},\qquad
\delta_n(x)=\begin{cases} \tfrac{n}{2} & \left(|x|\leq \tfrac{1}{n}\right)\\ 0 & (\text{그 외}) \end{cases}
$$

- 복소함수<span class="gloss">complex-valued function</span>는 정의역과 공역이 복소수 집합으로 확장된 함수이다. 어떤 영역에서 복소 미분 가능하면 그 영역에서 해석성<span class="gloss">analyticity</span>을 가진다고 하며(실함수의 미분 가능성보다 엄격한 조건), 이러한 함수를 홀로모픽 함수<span class="gloss">holomorphic function</span>라 한다.
- 다변수함수<span class="gloss">multivariate function</span>는 둘 이상의 독립변수로 값이 정해지는 함수로, 편미분<span class="gloss">partial differentiation</span>을 정의할 수 있다. 예를 들어 $z=f(x,y)=x^2-y^2$의 편도함수는 다음과 같다.

$$
\frac{\partial z}{\partial x}=2x,\qquad \frac{\partial z}{\partial y}=-2y
$$

<PyRunner>

```python
import numpy as np

# 편미분의 수치 근사 (중심 차분).  z = f(x, y) = x^2 - y^2
f = lambda x, y: x**2 - y**2
h = 1e-6
x0, y0 = 3.0, 2.0

df_dx = (f(x0+h, y0) - f(x0-h, y0)) / (2*h)
df_dy = (f(x0, y0+h) - f(x0, y0-h)) / (2*h)

print(f"∂z/∂x at ({x0},{y0}) = {df_dx:.4f}   (해석해 2x = {2*x0})")
print(f"∂z/∂y at ({x0},{y0}) = {df_dy:.4f}  (해석해 -2y = {-2*y0})")
```

</PyRunner>

## 함수의 그래프와 이동

- **평행 이동**<span class="gloss">translation</span>은 수평·수직 두 방향으로 나뉜다. 수평 이동<span class="gloss">horizontal shift</span>은 $y=f(x-h)$로, $h>0$이면 오른쪽으로 $h$만큼 이동한다. 수직 이동<span class="gloss">vertical shift</span>은 $y=f(x)+k$로, $k>0$이면 위로 $k$만큼 이동한다.

$$
y = f(x-h)\ (\text{수평}),\qquad y = f(x) + k\ (\text{수직})
$$

- **대칭 이동**<span class="gloss">reflection</span>은 축을 기준으로 함수를 뒤집는다. $x$축 대칭은 치역의 부호를, $y$축 대칭은 정의역의 부호를 반대로 한다.

$$
y=-f(x)\ (x\text{축 대칭}),\qquad y=f(-x)\ (y\text{축 대칭})
$$

- **확대**<span class="gloss">scaling</span>와 **축소**<span class="gloss">dilation</span>는 상수를 곱해 그래프를 늘리거나 줄인다. 수직 방향은 $y=af(x)$, 수평 방향은 $y=f(bx)$이다.

$$
y=af(x):\ |a|>1\ \text{확대},\ 0<|a|<1\ \text{축소},\qquad
y=f(bx):\ |b|>1\ \text{수평 축소},\ 0<|b|<1\ \text{수평 확대}
$$

- **회전**<span class="gloss">rotation</span>은 순서쌍 $(x,y)$를 각도 $\theta$만큼 돌려 $(x',y')$을 얻으며, 이는 벡터<span class="gloss">vector</span>에 회전 행렬을 곱한 것과 같다.

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix},\qquad
\begin{aligned} x'&=x\cos\theta - y\sin\theta \\ y'&=x\sin\theta + y\cos\theta \end{aligned}
$$

<PyRunner>

```python
import numpy as np

# 기본 함수 f(x) = x^2 에 각종 이동을 적용
x = np.linspace(-2, 2, 5)
f = lambda t: t**2

print("x        :", x)
print("f(x)=x^2 :", f(x))
print("f(x-1)   :", f(x - 1))   # 오른쪽으로 평행 이동
print("f(x)+1   :", f(x) + 1)   # 위로 평행 이동
print("-f(x)    :", -f(x))      # x축 대칭
print("f(-x)    :", f(-x))      # y축 대칭
print("2*f(x)   :", 2*f(x))     # y축 방향 2배 확대
```

</PyRunner>

<PyRunner>

```python
import numpy as np

# 회전 변환: (1, 0) 을 90도 회전하면 (0, 1)
theta = np.pi / 2
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
v = np.array([1.0, 0.0])

print("회전 행렬 R(90°) =\n", np.round(R, 3))
print("R v =", np.round(R @ v, 3))

# 단위허수 i 의 행렬 표현이 90도 회전과 같음을 확인
i_mat = np.array([[0, -1], [1, 0]])
print("i 의 행렬 표현 == R(90°) ? ", np.allclose(R, i_mat))
```

</PyRunner>
