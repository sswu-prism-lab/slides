# 문제 15 · 실습 — 최대 증가 방향 (그래디언트)

$(1,1)$ 에서의 그래디언트를 유한차분으로 구하고, 정규화하여 최대 증가 방향 $(0,-1)$ 을 확인합니다.

<PyRunner>

```python
import numpy as np

u = lambda x, y: x / (x**2 + y**2)
p = np.array([1., 1.])
eps = 1e-6

grad = []
for i in range(2):
    e = np.zeros(2); e[i] = eps
    grad.append((u(*(p + e)) - u(*(p - e))) / (2*eps))
grad = np.array(grad)

print("∇u(1,1)        =", np.round(grad, 6))                 # (0, -0.5)
print("단위 증가방향  =", np.round(grad / np.linalg.norm(grad), 6))  # (0, -1)
```

</PyRunner>

👉 [문제 15로 돌아가기](./problem-15)
