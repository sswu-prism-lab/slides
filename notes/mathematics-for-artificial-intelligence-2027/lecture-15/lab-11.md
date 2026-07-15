# 문제 11 · 실습 — 전치의 성질 $(AB)^\top=B^\top A^\top$

두 방식으로 계산한 결과가 $\begin{pmatrix}0&-5\\9&17\end{pmatrix}$ 로 일치하는지 확인합니다.

<PyRunner>

```python
import numpy as np

A = np.array([[1, 2, 0],
              [-1, 3, 2]])
B = np.array([[2, 1],
              [-1, 4],
              [0, 3]])

lhs = (A @ B).T        # (AB)^T
rhs = B.T @ A.T        # B^T A^T
print("(AB)^T =\n", lhs)
print("B^T A^T =\n", rhs)
print("두 결과 일치:", np.array_equal(lhs, rhs))
```

</PyRunner>

👉 [문제 11로 돌아가기](./problem-11)
