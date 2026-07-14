# 문제 2 · 실습 — 이차 다항식 회귀

설계 행렬 $[1,x,x^2]$로 정규방정식을 풀어 $w_0,w_1,w_2$를 구합니다.

<PyRunner>

```python
import numpy as np
data = np.array([(0, 1), (1, 2), (2, 1), (3, 4)], float)
x, t = data[:, 0], data[:, 1]
X = np.column_stack([np.ones(len(x)), x, x**2])   # [1, x, x^2]
w = np.linalg.solve(X.T @ X, X.T @ t)
print("X^T X =\n", X.T @ X, "\nX^T t =", X.T @ t)
print(f"w0 = {w[0]:.3f},  w1 = {w[1]:.3f},  w2 = {w[2]:.3f}")
print(f"예측값 = {(X @ w).round(3)}   (관측 t = {t})")
```

</PyRunner>

👉 [문제 02로 돌아가기](./problem-02)
