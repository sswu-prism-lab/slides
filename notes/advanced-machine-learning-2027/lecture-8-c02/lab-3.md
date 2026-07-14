# 문제 3 · 실습 — 3변수 라그랑제 최적점

정류 조건 $2x=4y=6z=-\lambda$와 제약을 선형 연립방정식으로 풀어 최적점과 최솟값을 확인합니다.

<PyRunner>

```python
import numpy as np

# 2x=λ, 4y=λ, 6z=λ, x+y+z=1
A = np.array([[2, 0, 0, 1], [0, 4, 0, 1], [0, 0, 6, 1], [1, 1, 1, 0]], float)
b = np.array([0, 0, 0, 1], float)
x, y, z, lam = np.linalg.solve(A, b)
print(f"(x, y, z) = ({x:.4f}, {y:.4f}, {z:.4f})   (= 6/11, 3/11, 2/11)")
print(f"f = {x**2 + 2*y**2 + 3*z**2:.4f}   (= 6/11 = {6/11:.4f})")
print("헤세 diag(2,4,6) 양의 정부호 -> 최소")
```

</PyRunner>

👉 [문제 3로 돌아가기](./problem-3)
