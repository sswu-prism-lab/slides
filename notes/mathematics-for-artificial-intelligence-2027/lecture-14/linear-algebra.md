# 선형대수 · 텐서와 행렬

> 기말 범위 9–10주차 요약. 데이터를 담는 그릇인 **텐서**부터, 벡터의 크기·내적·사영·외적, 그리고 정방행렬의 행렬식·역행렬·고윳값까지 정리한다.

## 스칼라, 벡터, 행렬, 텐서

- **스칼라**<span class="gloss">scalar</span>는 하나의 성분<span class="gloss">component</span>만을 가진 수치이다. $7$, $-3$, $\pi$ 등이 스칼라이며, 관습적으로 $x$처럼 표기한다.
- **벡터**<span class="gloss">vector</span>는 여러 성분으로 이루어진 배열<span class="gloss">array</span>이다. 명시하지 않는 한 벡터는 **열벡터**<span class="gloss">column vector</span>를 의미하며 $\mathbf{x}$로 표기하고, $i$번째 성분을 $x_i$로 쓴다. 행과 열을 바꾸는 연산($\top$)을 **전치**<span class="gloss">transpose</span>라 한다.

$$
\mathbf{x}=\begin{bmatrix} x_0\\ x_1\\ x_2 \end{bmatrix}
\qquad
\mathbf{x}^\top = \begin{bmatrix} x_0 & x_1 & x_2 \end{bmatrix}
$$

- 기하적으로 벡터의 각 성분은 좌표축을 따라 나아간 거리로 해석된다. 기계학습에서는 각 성분이 데이터의 **특징**<span class="gloss">feature</span>을 나타내며, 이런 벡터를 **특징 벡터**<span class="gloss">feature vector</span>라 한다. 가능한 특징들이 모인 집합을 **특징 공간**<span class="gloss">feature space</span>이라 한다.
- **행렬**<span class="gloss">matrix</span>은 수치들의 2차원 배열이다. $\mathbf{X}$로 표기하고, $i$번째 행·$j$번째 열의 원소를 $x_{i,j}$로 쓴다. 열벡터는 열이 하나, 행벡터는 행이 하나인 행렬로 볼 수 있다.
- 랭크<span class="gloss">rank</span>가 셋 이상인 수학적 객체를 **텐서**<span class="gloss">tensor</span>라 한다.

::: info 텐서의 랭크
스칼라는 랭크 0-텐서, 벡터는 랭크 1-텐서, 행렬은 랭크 2-텐서이다. 즉 텐서는 스칼라·벡터·행렬을 일반화한 개념이다.
:::

## 텐서 산술 연산

### 크기와 단위 벡터

- 기하적으로 벡터는 방향과 길이를 가지며, 그 길이를 **크기**<span class="gloss">magnitude</span>라 한다. $n$개의 성분을 가진 벡터의 크기는 피타고라스의 정리와 연관되며 다음과 같다.

$$
\|\mathbf{x}\|=\sqrt{x_0^2 + x_1^2 + \cdots + x_{n-1}^2}
$$

- 벡터를 그 크기로 나누면 방향은 같고 크기가 $1$인 **단위 벡터**<span class="gloss">unit vector</span>가 된다.

$$
\hat{\mathbf{x}}=\frac{\mathbf{x}}{\|\mathbf{x}\|}
$$

### 내적과 사영

- 두 벡터 $\mathbf{x}$, $\mathbf{y}$의 **내적**<span class="gloss">inner product, dot product</span>은 다음과 같이 정의된다($\theta$는 두 벡터 사이의 각).

$$
\mathbf{x}\cdot\mathbf{y}=\langle \mathbf{x}, \mathbf{y}\rangle=\mathbf{x}^\top \mathbf{y}=\sum_{k=0}^{n-1}x_k y_k=\|\mathbf{x}\| \|\mathbf{y}\| \cos \theta
$$

- 각도가 $\pi/2$이면 내적은 $0$이고, 이때 두 벡터가 **직교**<span class="gloss">orthogonal</span>한다고 한다. 내적은 교환법칙·분배법칙은 성립하나 결합법칙은 성립하지 않는다.
- **사영**<span class="gloss">projection</span>은 한 벡터가 다른 벡터 방향으로 얼마나 나아가는지를 계산한다. $\mathbf{y}$에 대한 $\mathbf{x}$의 사영은 다음과 같으며, 직교인 벡터들의 사영은 항상 $0$이다.

$$
\operatorname{proj}_{\mathbf{y}} \mathbf{x}=\frac{\mathbf{x}\cdot\mathbf{y}}{\|\mathbf{y}\|^2}\mathbf{y}
$$

### 외적과 성분별 곱

- 내적은 스칼라지만 **외적**<span class="gloss">outer product</span>은 행렬이 되며, 두 벡터의 차원이 달라도 정의된다. 성분이 $m$개인 $\mathbf{x}$와 $n$개인 $\mathbf{y}$의 외적($\mathbf{x}\mathbf{y}^\top$)은 다음과 같다.

$$
\mathbf{x}\mathbf{y}^\top=\begin{bmatrix}
x_0y_0 & x_0y_1 & \cdots & x_0 y_{n-1}\\
x_1y_0 & x_1y_1 & \cdots & x_1 y_{n-1}\\
\vdots & \vdots & \ddots & \vdots\\
x_{m-1}y_0 & x_{m-1}y_1 & \cdots & x_{m-1} y_{n-1}
\end{bmatrix}
$$

- 차원이 같은 두 행렬 $\mathbf{X}$, $\mathbf{Y}$에 대해 성분별 곱인 **아다마르 곱**<span class="gloss">Hadamard product</span> $\mathbf{Z}=\mathbf{X}\odot\mathbf{Y}$는 $z_{ij}=x_{ij}y_{ij}$로 정의된다.

<PyRunner>

```python
import numpy as np

x = np.array([4.0, 1.0])
y = np.array([3.0, 4.0])

dot = x @ y                              # 내적 x·y
mag_x, mag_y = np.linalg.norm(x), np.linalg.norm(y)
cos_t = dot / (mag_x * mag_y)            # cosθ = x·y / (||x|| ||y||)
proj = (dot / (y @ y)) * y               # y에 대한 x의 사영
outer = np.outer(x, y)                   # 외적 xy^T (행렬)

print(f"내적  x·y      = {dot:.1f}")
print(f"||x||={mag_x:.3f}, ||y||={mag_y:.3f}, cosθ={cos_t:.3f}")
print(f"사영  proj_y x = {proj}")
print("외적  x y^T =")
print(outer)
```

</PyRunner>

## 행렬곱과 정방행렬

- 행렬곱 $\mathbf{XY}$는 왼쪽 행렬의 열 수와 오른쪽 행렬의 행 수가 같아야 하며, $\mathbf{X}$의 행벡터를 $\mathbf{Y}$의 열벡터와 내적한 것이다. 결과 $\mathbf{Z}=\mathbf{XY}$는 $z_{i,j}=\sum_{k}x_{i,k}y_{k,j}$이다. 행렬곱은 결합·분배법칙은 만족하나 교환법칙은 성립하지 않는다($\mathbf{XY}\neq\mathbf{YX}$).
- 행렬에 열벡터를 곱하면 또 다른 열벡터가 나온다. 즉 행렬은 한 공간의 점을 다른 공간으로 **사상**<span class="gloss">mapping</span>하는 수단이다. 행과 열의 크기가 $n$으로 같은 **정방행렬**<span class="gloss">square matrix</span>은 $\mathbb{R}^n$에서 $\mathbb{R}^n$으로의 사상이다.
- 행렬 변환 $\mathbf{W}$와 이동<span class="gloss">translation</span> $\mathbf{b}$로 직선을 직선으로 보내는 **상관변환**<span class="gloss">affine transformation</span> $\mathbf{y}=\mathbf{W}\mathbf{x}+\mathbf{b}$를 정의할 수 있다. **뉴럴 네트워크의 각 층이 바로 상관변환이다.**
- 정방행렬에서는 **대각합**<span class="gloss">trace</span> $\operatorname{tr}(\mathbf{A})=\sum_i a_{i,i}$과 거듭제곱 $\mathbf{A}^n$이 정의된다. 대각 성분이 $1$이고 나머지가 $0$인 **단위행렬**<span class="gloss">identity matrix</span> $\mathbf{I}_n$은 행렬 곱셈의 항등원이다.

## 행렬식과 역행렬

- 정방행렬의 **행렬식**<span class="gloss">determinant</span>은 행렬을 하나의 스칼라로 사상하는 함수 $\operatorname{det}(\mathbf{A})\in\mathbb{R}$이다. 주요 성질은 다음과 같다.
  - 모두 $0$인 행/열이 있거나 동일한 두 행이 있으면 $\operatorname{det}(\mathbf{A})=0$.
  - 삼각행렬·대각행렬이면 $\operatorname{det}(\mathbf{A})=\prod_{i}a_{i,i}$이고, 단위행렬은 $\operatorname{det}(\mathbf{I})=1$.
  - $\operatorname{det}(\mathbf{A}\mathbf{B})=\operatorname{det}(\mathbf{A})\operatorname{det}(\mathbf{B})$, $\operatorname{det}(\mathbf{A}^\top)=\operatorname{det}(\mathbf{A})$.
- 소행렬<span class="gloss">minor matrix</span> $\mathbf{A}_{ij}$($i$행·$j$열 제거)와 여인수<span class="gloss">cofactor</span> $C_{ij}=(-1)^{i+j}\operatorname{det}(\mathbf{A}_{ij})$를 이용한 **여인수 전개**<span class="gloss">cofactor expansion</span>로 행렬식을 구한다.

$$
\operatorname{det}(\mathbf{A})=\sum_{j=0}^{n-1}a_{0,j}C_{0j},
\qquad
\operatorname{det}\begin{bmatrix} a & b \\ c & d \end{bmatrix}=ad-bc
$$

::: info 역행렬과 특이행렬
행렬식의 주요 용도는 **역행렬**<span class="gloss">inverse matrix</span>의 존재 판정이다. 역행렬 $\mathbf{A}^{-1}$은 $\mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=\mathbf{I}$를 만족하며, 존재하면 $\operatorname{det}(\mathbf{A}^{-1})=1/\operatorname{det}(\mathbf{A})$, $(\mathbf{AB})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$이 성립한다. 역행렬이 없는 행렬(즉 $\operatorname{det}(\mathbf{A})=0$)을 **특이행렬**<span class="gloss">singular matrix</span>이라 한다.
:::

<PyRunner>

```python
import numpy as np

A = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0],
              [7.0, 8.0, 10.0]])       # det≠0 이 되도록 (7,8,10)

det = np.linalg.det(A)
inv = np.linalg.inv(A)

print(f"det(A) = {det:.4f}  (0이 아니므로 비특이 → 역행렬 존재)")
print("A^-1 =")
print(np.round(inv, 4))
print("A·A^-1 = I 확인:", np.allclose(A @ inv, np.eye(3)))
print(f"det(A^-1) = {np.linalg.det(inv):.4f}  vs  1/det(A) = {1/det:.4f}")
```

</PyRunner>

## 특수 정방행렬과 부호

- $\mathbf{A}^\top=\mathbf{A}$이면 **대칭행렬**<span class="gloss">symmetric matrix</span>, $\mathbf{A}\mathbf{A}^\top=\mathbf{A}^\top\mathbf{A}=\mathbf{I}$이면 **직교행렬**<span class="gloss">orthogonal matrix</span>이다. 직교행렬은 $\mathbf{A}^{-1}=\mathbf{A}^\top$이고 $\operatorname{det}(\mathbf{A})=\pm1$이다.
- 임의의 $\mathbf{x}\neq\mathbf{0}$에 대해 대칭행렬 $\mathbf{A}$가 $\mathbf{x}^\top\mathbf{A}\mathbf{x}>0$이면 **양의 정부호**<span class="gloss">positive definite</span>, $\geq0$이면 양의 준정부호<span class="gloss">positive semidefinite</span>이다. 부등호를 뒤집으면 음의 (준)정부호가 된다.

## 고윳값과 고유벡터

- 정방행렬 $\mathbf{A}$는 벡터를 같은 공간의 다른 벡터로 사상한다. 영벡터가 아닌 $\mathbf{v}$와 스칼라 $\lambda$가

$$
\mathbf{A}\mathbf{v}=\lambda\mathbf{v}
$$

를 만족하면, $\mathbf{v}$를 $\mathbf{A}$의 **고유벡터**<span class="gloss">eigenvector</span>, $\lambda$를 그 **고윳값**<span class="gloss">eigenvalue</span>이라 한다. 기하적으로 $\mathbf{A}$는 고유벡터의 방향을 바꾸지 않고 확대·축소만 한다.

::: info 특성 방정식
$\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$를 정리하면 $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$이다. $\mathbf{v}\neq\mathbf{0}$이려면 $\mathbf{A}-\lambda\mathbf{I}$가 특이행렬이어야 하므로 다음 **특성 방정식**<span class="gloss">characteristic equation</span>이 성립한다.

$$
\operatorname{det}(\mathbf{A}-\lambda\mathbf{I})=0
$$

$n\times n$ 행렬의 특성 다항식은 $n$차 다항식이므로 고윳값은 (중복 포함) 최대 $n$개다.
:::

<PyRunner>

```python
import numpy as np

A = np.array([[2.0, 0.0],
              [0.0, 3.0]])            # 대각행렬: 고윳값이 대각 성분 2, 3
vals, vecs = np.linalg.eig(A)

print("고윳값 :", np.round(vals, 4))
print("고유벡터(열):")
print(np.round(vecs, 4))

for i in range(len(vals)):
    v = vecs[:, i]
    lhs, rhs = A @ v, vals[i] * v      # Av 와 λv 비교
    print(f"λ={vals[i]:.1f}:  Av={np.round(lhs,3)}  λv={np.round(rhs,3)}  ->",
          np.allclose(lhs, rhs))
```

</PyRunner>

## 벡터 노름과 거리

- **벡터 노름**<span class="gloss">vector norm</span>은 벡터를 $0$ 이상의 실수로 사상한다. $L_p$-노름은 $\|\mathbf{x}\|_p \equiv \left(\sum_i |x_i|^p\right)^{1/p}$로 정의된다.
  - 벡터의 크기는 $L_2$-노름 $\|\mathbf{x}\|_2=\sqrt{\mathbf{x}^\top\mathbf{x}}$이며, 그 밖에 $\|\mathbf{x}\|_1=\sum_i|x_i|$, $\|\mathbf{x}\|_\infty=\max_i|x_i|$가 있다.
  - $\mathbf{x}$를 $\mathbf{x}-\mathbf{y}$로 대체하면 거리가 된다. $L_2$는 유클리드 거리<span class="gloss">Euclidean distance</span>, $L_1$은 맨해튼 거리<span class="gloss">Manhattan distance</span>, $L_\infty$는 체비셰프 거리<span class="gloss">Chebyshev distance</span>이다. $L_1$·$L_2$ 노름은 딥러닝의 정칙화<span class="gloss">regularizer</span>로 자주 쓰인다.
- 여러 특징의 상호 변동은 **공분산**<span class="gloss">covariance</span>으로 본다. 데이터 행렬 $\mathbf{X}$(행=샘플, 열=특징)의 공분산 행렬 $\mathbf{\Sigma}$는 다음과 같다.

$$
\Sigma_{i, j}=\frac{1}{n-1}\sum_{k=0}^{n-1}(x_{k,i}-\bar{\mathbf{x}}_i)(x_{k, j}-\bar{\mathbf{x}}_j)
$$

- 공분산으로 **마할라노비스 거리**<span class="gloss">Mahalanobis distance</span> $D_M=\sqrt{(\mathbf{x}-\mathbf{y})^\top \mathbf{\Sigma}^{-1}(\mathbf{x}-\mathbf{y})}$를 정의한다. 두 확률 분포의 거리로는 **쿨백-라이블러 발산**<span class="gloss">Kullback-Leibler divergence</span> $D_{\mathrm{KL}}(P\|Q)=\sum_x P(x)\log\frac{P(x)}{Q(x)}$을 쓰며, 대칭적이지 않다.
