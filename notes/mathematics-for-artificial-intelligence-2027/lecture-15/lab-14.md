# 문제 14 · 실습 — 행렬함수의 도함수 수치검증

성분별 해석적 도함수 행렬을 유한차분으로 검증합니다.

<PyRunner>

```python
import numpy as np

F = lambda t: np.array([[np.exp(2*t), t**3],
                        [np.sin(t),   1/(t + 1)]])
dF = lambda t: np.array([[2*np.exp(2*t), 3*t**2],
                         [np.cos(t),    -1/(t + 1)**2]])

t, h = 0.5, 1e-6
numeric = (F(t + h) - F(t - h)) / (2*h)
print("해석 dF/dt =\n", np.round(dF(t), 6))
print("수치 dF/dt =\n", np.round(numeric, 6))
```

</PyRunner>

👉 [문제 14로 돌아가기](./problem-14)
