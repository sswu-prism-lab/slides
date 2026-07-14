# 문제 6 · 실습 — 정규방정식 풀기

설계 행렬로 정규방정식 $(\mathbf{X}^\top\mathbf{X})\mathbf{w}=\mathbf{X}^\top\mathbf{t}$를 풀어 회귀 계수를 구합니다.

<PyRunner>

```python
import numpy as np

data = np.array([(1, 2), (2, 4), (4, 3), (5, 6)], float)
x, t = data[:, 0], data[:, 1]

X = np.column_stack([np.ones(len(x)), x])   # 설계 행렬 [1, x]
w = np.linalg.solve(X.T @ X, X.T @ t)       # (X^T X) w = X^T t
print("정규방정식  (X^T X) w = X^T t")
print("X^T X =\n", X.T @ X)
print("X^T t =", X.T @ t)
print(f"\nw0 = {w[0]:.4f},  w1 = {w[1]:.4f}")
print(f"회귀 직선:  t_hat = {w[1]:.2f} x + {w[0]:.2f}")
```

</PyRunner>

👉 [문제 6로 돌아가기](./problem-06)
