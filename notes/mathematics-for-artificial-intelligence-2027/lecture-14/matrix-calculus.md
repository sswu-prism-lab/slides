# 행렬 미분 · 야코비와 헤시안

> 기말 범위 12주차 요약. 입력·출력이 스칼라·벡터·행렬인 함수들의 도함수 표기법과, 그 대표인 야코비 행렬·헤시안, 그리고 자주 쓰는 행렬 미분 항등식을 정리한다.

## 함수 종류별 도함수의 모양

미분의 대상이 스칼라냐 벡터냐 행렬이냐에 따라 도함수의 모양(스칼라·벡터·행렬)이 달라진다.

### 스칼라 인수 벡터 함수

- 스칼라를 받아 벡터를 돌려주는 함수 $\mathbf{f}(x):\mathbb{R}\mapsto\mathbb{R}^m$를 **벡터값 함수**<span class="gloss">vector-valued function</span>라 한다. 그 예가 매개변수 곡선<span class="gloss">parametric curve</span>이다.

$$
\mathbf{f}(t)=t \cos(t)\,\hat{\mathbf{x}}+t\sin(t)\,\hat{\mathbf{y}}+t\,\hat{\mathbf{z}}
$$

- 이 함수의 도함수를 **접벡터**<span class="gloss">tangent vector</span>라 하며, 각 성분을 미분한 열벡터이다.

$$
\frac{\partial\mathbf{f}}{\partial x}=\begin{bmatrix}
\partial f_0/\partial x\\
\partial f_1/\partial x\\
\vdots\\
\partial f_{n-1}/\partial x
\end{bmatrix}
$$

### 벡터 인수 스칼라 함수

- 벡터를 받아 스칼라를 돌려주는 스칼라장 $f:\mathbb{R}^m\mapsto\mathbb{R}$의 도함수는 그래디언트이며, 행렬 미분 표기법에서는 **행벡터**로 쓴다.

$$
\frac{\partial f}{\partial \mathbf{x}}=\left[ \frac{\partial f}{\partial x_0} \quad \frac{\partial f}{\partial x_1} \quad \cdots \quad \frac{\partial f}{\partial x_{m-1}} \right]
$$

::: info 도함수의 모양 정리
- 스칼라 인수 벡터 함수의 도함수는 **열벡터**(접벡터).
- 벡터 인수 스칼라 함수의 도함수는 **행벡터**(그래디언트).
- 벡터 인수 벡터 함수 $\mathbf{f}:\mathbb{R}^m\mapsto\mathbb{R}^n$의 도함수는 **행렬**(야코비 행렬).
:::

### 벡터 인수 벡터 함수와 행렬 함수

- 벡터 인수 벡터 함수의 도함수는 행렬이며, 각 행이 성분 함수의 그래디언트이다.

$$
\frac{\partial \mathbf{f}}{\partial \mathbf{x}}=\begin{bmatrix}
\frac{\partial f_0}{\partial x_0} & \cdots & \frac{\partial f_0}{\partial x_{m-1}}\\
\vdots & \ddots & \vdots\\
\frac{\partial f_{n-1}}{\partial x_0} & \cdots & \frac{\partial f_{n-1}}{\partial x_{m-1}}
\end{bmatrix}=\begin{bmatrix}
\nabla f_0(\mathbf{x})^\top\\
\vdots\\
\nabla f_{n-1}(\mathbf{x})^\top
\end{bmatrix}
$$

- 스칼라를 받아 행렬을 돌려주는 함수 $\mathbf{F}:\mathbb{R}\mapsto\mathbb{R}^{n\times m}$의 도함수(각 성분을 미분)를 **접행렬**<span class="gloss">tangent matrix</span>이라 하고, 행렬을 받아 스칼라를 돌려주는 함수 $f(\mathbf{X}):\mathbb{R}^{n\times m}\mapsto\mathbb{R}$의 도함수를 **기울기 행렬**<span class="gloss">gradient matrix</span>이라 한다.

## 야코비 행렬

::: info 야코비 행렬
**야코비 행렬**<span class="gloss">Jacobian matrix</span>은 벡터 인수 벡터 함수 $\mathbf{f}:\mathbb{R}^m\mapsto\mathbb{R}^n$의 도함수로, $(i,j)$ 성분이 $\partial f_i/\partial x_j$인 $n\times m$ 행렬이다.

$$
\mathbf{J}_\mathbf{x} = \frac{\partial \mathbf{f}}{\partial \mathbf{x}}=\begin{bmatrix}
\frac{\partial f_0}{\partial x_0} & \frac{\partial f_0}{\partial x_1} & \cdots & \frac{\partial f_0}{\partial x_{m-1}}\\
\frac{\partial f_1}{\partial x_0} & \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_{m-1}}\\
\vdots & \vdots &\ddots & \vdots\\
\frac{\partial f_{n-1}}{\partial x_0} & \frac{\partial f_{n-1}}{\partial x_1} & \cdots & \frac{\partial f_{n-1}}{\partial x_{m-1}}
\end{bmatrix}
$$

기계학습의 역전파에서 쓰이는 손실 함수<span class="gloss">loss function</span>의 도함수가 바로 이런 벡터 인수 벡터 함수의 도함수이다.
:::

<PyRunner>

```python
import numpy as np

# 유한 차분으로 야코비 행렬 계산: J[i,j] = ∂f_i/∂x_j
def jacobian(f, x, h=1e-6):
    x = np.asarray(x, dtype=float)
    f0 = np.asarray(f(x), dtype=float)
    J = np.zeros((f0.size, x.size))
    for j in range(x.size):
        e = np.zeros_like(x); e[j] = h
        J[:, j] = (f(x + e) - f(x - e)) / (2 * h)
    return J

# f(x,y) = [ x^2 * y , 5x + sin(y) ]
f = lambda v: np.array([v[0]**2 * v[1], 5*v[0] + np.sin(v[1])])
p = np.array([2.0, 1.0])

J = jacobian(f, p)
exact = np.array([[2*p[0]*p[1], p[0]**2],   # [2xy, x^2]
                  [5.0,         np.cos(p[1])]])  # [5, cos y]
print("점 (2,1)에서 수치 야코비 =")
print(np.round(J, 4))
print("해석 야코비 =")
print(np.round(exact, 4))
print("일치:", np.allclose(J, exact))
```

</PyRunner>

## 헤시안 행렬

- 스칼라장 $f(\mathbf{x})$의 그래디언트 $\nabla f$는 다시 벡터 인수 벡터 함수이므로, 그 야코비 행렬을 취하면 **헤시안 행렬**<span class="gloss">Hessian matrix</span>이 된다. 헤시안은 이계 편미분들을 성분으로 갖는다.

$$
\mathbf{H}=\frac{\partial}{\partial\mathbf{x}}\!\left(\frac{\partial f}{\partial\mathbf{x}}\right)^\top,\qquad
H_{ij}=\frac{\partial^2 f}{\partial x_i\,\partial x_j}
$$

- 혼합 편미분의 순서가 무관하므로($\partial^2 f/\partial x_i\partial x_j=\partial^2 f/\partial x_j\partial x_i$) 헤시안은 대칭행렬이다. 정류점에서 헤시안이 양의 정부호이면 극소, 음의 정부호이면 극대, 부호가 섞이면 안장점이다.

<PyRunner>

```python
import numpy as np

# 유한 차분 헤시안: H[i,j] = ∂²f / ∂x_i∂x_j
def hessian(f, x, h=1e-4):
    x = np.asarray(x, dtype=float); n = x.size
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            ei = np.zeros(n); ei[i] = h
            ej = np.zeros(n); ej[j] = h
            H[i, j] = (f(x+ei+ej) - f(x+ei-ej) - f(x-ei+ej) + f(x-ei-ej)) / (4*h*h)
    return H

# f(x,y) = x^2 + y^2 + 3xy  ->  H = [[2,3],[3,2]] (상수)
f = lambda v: v[0]**2 + v[1]**2 + 3*v[0]*v[1]
H = hessian(f, np.array([1.0, 1.0]))
print("헤시안 H =")
print(np.round(H, 3))
print("대칭 여부:", np.allclose(H, H.T))
print("고윳값:", np.round(np.linalg.eigvalsh(H), 3),
      "-> 부호 혼재이면 안장점")
```

</PyRunner>

## 행렬 미분 항등식

- $f$, $g$를 벡터 $\mathbf{x}$를 받아 스칼라를 돌려주는 함수, $a$를 $\mathbf{x}$에 무관한 스칼라라 하면 기본 항등식은 다음과 같다.

$$
\frac{\partial}{\partial\mathbf{x}}(af)=a\frac{\partial f}{\partial\mathbf{x}},\qquad
\frac{\partial}{\partial\mathbf{x}}(f+g)=\frac{\partial f}{\partial\mathbf{x}}+\frac{\partial g}{\partial\mathbf{x}}
$$

$$
\frac{\partial}{\partial\mathbf{x}}(fg)=f\frac{\partial g}{\partial\mathbf{x}}+g\frac{\partial f}{\partial\mathbf{x}},\qquad
\frac{\partial}{\partial\mathbf{x}}(f\circ g)=\frac{\partial f}{\partial g}\frac{\partial g}{\partial\mathbf{x}}
$$

- $\mathbf{x}$에 무관한 상수 벡터 $\mathbf{a}$에 대해 선형형식의 미분과, 벡터값 함수의 곱셈 항등식이 성립한다.

$$
\frac{\partial}{\partial\mathbf{x}}(\mathbf{a}^\top\mathbf{x})=\mathbf{a}^\top,\qquad
\frac{\partial}{\partial\mathbf{x}}(\mathbf{f}^\top\mathbf{g})=\mathbf{f}^\top\frac{\partial\mathbf{g}}{\partial\mathbf{x}}+\mathbf{g}^\top\frac{\partial\mathbf{f}}{\partial\mathbf{x}}
$$

::: info 역전파의 핵심 — 벡터 함수의 연쇄법칙
스칼라 인수 벡터 함수와 벡터 인수 벡터 함수 모두에 대해 상수배·상수행렬배·합·연쇄법칙이 성립한다.

$$
\frac{\partial}{\partial x}(\mathbf{A}\mathbf{f})=\mathbf{A}\frac{\partial\mathbf{f}}{\partial x},\qquad
\frac{\partial}{\partial\mathbf{x}}(\mathbf{f}\circ\mathbf{g})=\frac{\partial\mathbf{f}}{\partial\mathbf{g}}\frac{\partial\mathbf{g}}{\partial\mathbf{x}}
$$

마지막 연쇄법칙(야코비의 곱)이 신경망 역전파의 수학적 뼈대이다.
:::

## 성분별 연산의 도함수

- 두 벡터의 덧셈 $\mathbf{f}=\mathbf{a}+\mathbf{b}$의 야코비는 $\partial\mathbf{f}/\partial\mathbf{a}=\mathbf{I}$, $\partial\mathbf{f}/\partial\mathbf{b}=\mathbf{I}$이다. 뺄셈이면 $\partial\mathbf{f}/\partial\mathbf{b}=-\mathbf{I}$이다.
- 성분별 곱셈 $f_i=a_i b_i$의 야코비는 대각행렬이 된다(비대각 성분은 서로 무관하므로 $0$).

$$
\frac{\partial \mathbf{f}}{\partial\mathbf{a}}=\operatorname{diag}(b_0,\ldots,b_{n-1}),
\qquad
\frac{\partial \mathbf{f}}{\partial\mathbf{b}}=\operatorname{diag}(a_0,\ldots,a_{n-1})
$$
