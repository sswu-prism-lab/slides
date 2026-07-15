# 미분 · 도함수와 그래디언트

> 기말 범위 11주차 요약. 기울기와 도함수의 정의에서 출발해 미분법, 편미분, 그리고 다변수로의 확장인 그래디언트와 연쇄법칙을 정리한다.

## 기울기와 도함수

- 직선 $y=ax+b$에서 $a$는 **기울기**<span class="gloss">slope</span>, $b$는 $y$절편<span class="gloss">intercept</span>이다. 두 점 $(x_1,y_1)$, $(x_0,y_0)$를 알면 $a=\dfrac{y_1-y_0}{x_1-x_0}$이며, 기울기는 $x$가 변할 때 $y$가 얼마나 변하는지를 말해 준다.
- 곡선의 두 점을 지나는 직선을 할선<span class="gloss">secant line</span>, 한 점에서 곡선에 접하는 직선을 **접선**<span class="gloss">tangent line</span>이라 한다. 극대점·극소점에서 접선의 기울기는 $0$에 접근하며, 접선의 기울기가 $0$인 점을 **정류점**<span class="gloss">stationary point</span>이라 한다.
- 곡선 위 점 $x$에서 접선의 기울기를 그 점에서의 **도함수**<span class="gloss">derivative</span>라 한다. 곡선 $y=f(x)$의 두 점 사이 기울기 $\dfrac{\Delta y}{\Delta x}=\dfrac{f(x_1)-f(x_0)}{x_1-x_0}$에서 $x_1=x_0+h$로 치환한 뒤 $h\to0$의 극한을 취해 도함수를 정의한다.

::: info 도함수의 정의
$$
\frac{dy}{dx}=f'(x)\equiv\lim_{h\rightarrow0}\frac{f(x+h)-f(x)}{h}
$$

이는 $x$가 극히 미세하게 변할 때 함수값이 어떻게 변하는지를 나타낸다. $f'(x)$를 다시 미분한 것이 **이계도함수**<span class="gloss">second derivative</span> $f''(x)=d^2y/dx^2$이고, 일반적으로 $n$계도함수도 정의된다.
:::

- 미분 연산자는 **선형 연산자**이므로 덧셈·뺄셈으로 결합된 식의 미분은 개별 도함수의 합·차가 된다.

$$
\frac{d}{dx}(f(x)\pm g(x))=f'(x)\pm g'(x)
$$

## 미분법

주요 **미분법**<span class="gloss">differentiation rule</span>을 정리하면 다음과 같다.

| 종류 | 미분법 |
| :---: | --- |
| 상수 | $\dfrac{d}{dx}c=0$ |
| 거듭제곱 | $\dfrac{d}{dx}ax^n=nax^{n-1}$ |
| 합 | $\dfrac{d}{dx}(f\pm g)=f'\pm g'$ |
| 곱 | $\dfrac{d}{dx}(fg)=f'g+fg'$ |
| 몫 | $\dfrac{d}{dx}\!\left(\dfrac{f}{g}\right)=\dfrac{f'g-fg'}{g^2}$ |
| 연쇄 | $\dfrac{d}{dx}f\circ g=f'(g(x))\,g'(x)$ |
| 삼각 | $\dfrac{d}{dx}\sin x=\cos x,\;\dfrac{d}{dx}\cos x=-\sin x,\;\dfrac{d}{dx}\tan x=\sec^2 x$ |
| 지수 | $\dfrac{d}{dx}a^{g(x)}=\ln(a)\,g'(x)\,a^{g(x)}$ |
| 로그 | $\dfrac{d}{dx}\log_b g(x)=\dfrac{g'(x)}{g(x)\ln b}$ |

- 특히 지수함수의 도함수는 자기 자신이다: $\dfrac{d}{dx}e^x=e^x$, 그리고 $\dfrac{d}{dx}e^{g(x)}=g'(x)e^{g(x)}$. 자연로그는 $\dfrac{d}{dx}\ln x=\dfrac{1}{x}$이다.

::: info 곱 법칙과 연쇄법칙
$$
\frac{d}{dx}f(x)g(x)=f'(x)g(x)+f(x)g'(x),
\qquad
\frac{d}{dx}f(g(x))=f'(g(x))\,g'(x)
$$

합성함수에 적용하는 **연쇄법칙**<span class="gloss">chain rule</span>은 역전파 알고리즘에 기초한 뉴럴 네트워크가 의존하는 핵심 규칙이다.
:::

- 정류점에서 곡선이 극솟값인지 극댓값인지를 판단할 수 있다. 국소 극솟값 중 가장 작은 값이 **전역 극솟값**<span class="gloss">global minimum</span>, 국소 극댓값 중 가장 큰 값이 전역 극댓값이다. 극점이 아닌 정류점을 **변곡점**<span class="gloss">inflection point</span>이라 하고, 다변수 함수에서는 **안장점**<span class="gloss">saddle point</span>이라 한다.

<PyRunner>

```python
import numpy as np

# 수치 미분: 중심 차분 (f(x+h)-f(x-h)) / (2h)
def deriv(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

f = lambda x: x**3 - 2*x        # f(x)=x^3-2x,  f'(x)=3x^2-2
for x in [-1.0, 0.0, 1.0, 2.0]:
    num = deriv(f, x)
    exact = 3*x**2 - 2
    print(f"x={x:+.1f}:  수치 f'={num:+.5f}   해석 3x²-2={exact:+.1f}")

# 삼각·지수·로그의 도함수도 같은 방식으로 확인
print("\nd/dx sin(x) at π/3 :", round(deriv(np.sin, np.pi/3), 5),
      "vs cos =", round(np.cos(np.pi/3), 5))
print("d/dx e^x  at 1     :", round(deriv(np.exp, 1.0), 5),
      "vs e^1 =", round(np.e, 5))
```

</PyRunner>

## 편미분

- 변수가 둘 이상인 함수 $f(x,y)$나 $f(x_0,\ldots,x_n)$에는 **편미분**<span class="gloss">partial derivative</span>을 쓴다. 편미분은 다른 변수를 상수로 고정한 채 한 변수에 대해서만 미분한 것으로, $\partial$ 기호를 쓴다. 예를 들어 $f(x,y,z)=x^2+y^2+z^2+3xyz$이면

$$
\frac{\partial f}{\partial x}=2x+3yz,\qquad
\frac{\partial f}{\partial y}=2y+3xz,\qquad
\frac{\partial f}{\partial z}=2z+3xy
$$

- 편도함수의 편도함수(혼합 편미분)도 취할 수 있다. 위 함수에서

$$
\frac{\partial^2}{\partial x\,\partial y}f(x,y,z)=3z
$$

- $x$, $y$가 각각 $x(r,s)$, $y(r,s)$의 함수일 때 $f$의 $r$, $s$에 대한 편도함수는 각 변수에 연쇄법칙을 적용해 구한다.

$$
\frac{\partial f}{\partial r}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial r}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial r},
\qquad
\frac{\partial f}{\partial s}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial s}+\frac{\partial f}{\partial y}\frac{\partial y}{\partial s}
$$

## 그래디언트

- 다변수 함수 $f(\mathbf{x})$는 벡터 $\mathbf{x}=(x,y,z)$를 하나의 스칼라로 사상한다. 이렇게 벡터를 받아 스칼라를 돌려주는 함수를 **스칼라장**<span class="gloss">scalar field</span>이라 한다.
- **그래디언트**<span class="gloss">gradient</span>는 벡터를 받는 함수의 도함수로, 편미분을 $n$차원으로 확장한 것이다. $\nabla$(델, 나블라) 연산자를 쓴다.

::: info 그래디언트의 정의
$$
\nabla f(\mathbf{x})=\nabla f(x_0, x_1,\ldots,x_n)\equiv \begin{bmatrix}
\dfrac{\partial f}{\partial x_0}\\[4pt]
\dfrac{\partial f}{\partial x_1}\\[2pt]
\vdots\\
\dfrac{\partial f}{\partial x_n}
\end{bmatrix}
$$

그래디언트는 각 방향으로의 편미분을 성분으로 갖는 벡터이며, 함수값이 가장 가파르게 증가하는 방향을 가리킨다. 경사하강법은 이 반대 방향($-\nabla f$)으로 이동한다.
:::

<PyRunner>

```python
import numpy as np

# 수치 그래디언트: 각 성분마다 중심 차분
def grad(f, x, h=1e-6):
    x = np.asarray(x, dtype=float)
    g = np.zeros_like(x)
    for i in range(x.size):
        e = np.zeros_like(x); e[i] = h
        g[i] = (f(x + e) - f(x - e)) / (2 * h)
    return g

# f(x,y,z) = x^2 + y^2 + z^2 + 3xyz
f = lambda v: v[0]**2 + v[1]**2 + v[2]**2 + 3*v[0]*v[1]*v[2]
p = np.array([1.0, 2.0, 3.0])

num = grad(f, p)
exact = np.array([2*p[0] + 3*p[1]*p[2],     # 2x+3yz
                  2*p[1] + 3*p[0]*p[2],     # 2y+3xz
                  2*p[2] + 3*p[0]*p[1]])    # 2z+3xy
print("점 (1,2,3)에서")
print("수치 ∇f =", np.round(num, 4))
print("해석 ∇f =", exact)
print("일치 여부:", np.allclose(num, exact))
```

</PyRunner>
