# 문제 5 · 실습 — 몫의 미분 수치검증

해석적 도함수 $f'(x)=\dfrac{e^{3x}(3x^2-2x+3)}{(x^2+1)^2}$ 를 중앙차분으로 검증합니다.

<PyRunner>

```python
import numpy as np

def f(x):
    return np.exp(3*x) / (x**2 + 1)

def fprime(x):                       # 해석적 도함수
    return np.exp(3*x) * (3*x**2 - 2*x + 3) / (x**2 + 1)**2

for x in [0.0, 0.5, 1.2]:
    h = 1e-6
    numeric = (f(x + h) - f(x - h)) / (2*h)
    print(f"x={x}:  해석 f'={fprime(x):.6f}   수치 f'={numeric:.6f}")
```

</PyRunner>

👉 [문제 5로 돌아가기](./problem-05)
