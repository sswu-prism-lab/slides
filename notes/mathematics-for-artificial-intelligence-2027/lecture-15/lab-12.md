# 문제 12 · 실습 — 이계 편미분 수치검증

해석적 결과 $\dfrac{\partial^2 f}{\partial x\,\partial y}=\cos(xy)-xy\sin(xy)+6x^2y$ 를 유한차분으로 검증합니다.

<PyRunner>

```python
import numpy as np

f = lambda x, y: np.sin(x*y) + x**3 * y**2

def mixed_numeric(x, y, h=1e-4):     # 혼합 편미분의 중앙차분
    return (f(x+h, y+h) - f(x+h, y-h)
            - f(x-h, y+h) + f(x-h, y-h)) / (4*h*h)

analytic = lambda x, y: np.cos(x*y) - x*y*np.sin(x*y) + 6*x**2*y

x, y = 0.7, 1.3
print(f"해석적 f_xy({x},{y}) = {analytic(x, y):.6f}")
print(f"수치적 f_xy({x},{y}) = {mixed_numeric(x, y):.6f}")
```

</PyRunner>

👉 [문제 12로 돌아가기](./problem-12)
