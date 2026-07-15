# 문제 10 · 실습 — 고윳값과 고유벡터

`numpy.linalg.eig` 로 고윳값 $2,3$ 과 고유벡터를 구합니다. 고유벡터는 상수배까지만 결정되므로 정규화된 형태로 출력됩니다.

<PyRunner>

```python
import numpy as np

A = np.array([[2., 1.],
              [0., 3.]])
w, v = np.linalg.eig(A)

for i in range(len(w)):
    vec = v[:, i]
    print(f"고윳값 λ = {w[i]:.0f},  고유벡터 = {np.round(vec, 4)}")

print("λ=2 -> (1,0),  λ=3 -> (1,1) 방향 (정규화 시 0.7071)")
```

</PyRunner>

👉 [문제 10으로 돌아가기](./problem-10)
