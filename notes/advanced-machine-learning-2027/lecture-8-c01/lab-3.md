# 문제 3 · 실습 — 라그랑제 최적점

정류 조건을 선형 연립방정식으로 풀고, 제약 위에서 함수값이 최소임을 확인합니다.

<PyRunner>

```python
import numpy as np

# 정류 조건: 2x=λ, 4y=λ, x+y=3  (미지수 x,y,λ)
A = np.array([[2, 0, 1], [0, 4, 1], [1, 1, 0]], float)
b = np.array([0, 0, 3], float)
x, y, lam = np.linalg.solve(A, b)
print(f"(x, y) = ({x:.3f}, {y:.3f}),  λ = {lam:.3f},  f = {x**2 + 2*y**2:.3f}")
print("제약 위 f(y) = (3-y)^2 + 2y^2 :")
for yv in [-1, 0, 1, 2, 3]:
    print(f"  y={yv:+d}: f={(3-yv)**2 + 2*yv**2}")
print("헤세 diag(2,4) 양의 정부호 -> 최소")
```

</PyRunner>

👉 [문제 3로 돌아가기](./problem-3)
