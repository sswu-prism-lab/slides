# 문제 13 · 실습 — 그래디언트 $\nabla h(1,2,3)$

유한차분으로 편미분을 근사하여 $\nabla h(1,2,3)=(2,4,6)$ 을 확인합니다.

<PyRunner>

```python
import numpy as np

h = lambda x, y, z: x**2 + y**2 + z**2
p = np.array([1., 2., 3.])
eps = 1e-6

grad = []
for i in range(3):                   # 각 축 방향 중앙차분
    e = np.zeros(3); e[i] = eps
    grad.append((h(*(p + e)) - h(*(p - e))) / (2*eps))

print("∇h(1,2,3) =", np.round(grad, 6))   # (2, 4, 6)
```

</PyRunner>

👉 [문제 13으로 돌아가기](./problem-13)
