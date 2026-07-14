# 문제 3 · 실습 — 피셔 투영 벡터

클래스 내 산포 행렬과 $\mathbf{w}\propto\mathbf{S}_\mathrm{W}^{-1}(\mathbf{m}_2-\mathbf{m}_1)$을 계산합니다.

<PyRunner>

```python
import numpy as np
C1 = np.array([[2, 3], [3, 3], [3, 2]], float)
C2 = np.array([[6, 5], [7, 8], [8, 6]], float)
m1, m2 = C1.mean(0), C2.mean(0)
SW = (C1 - m1).T @ (C1 - m1) + (C2 - m2).T @ (C2 - m2)
w = np.linalg.inv(SW) @ (m2 - m1)
print("m1 =", m1, "  m2 =", m2, "\nS_W =\n", SW)
print(f"w ∝ {w}  ->  정수비 {np.round(w / w.min()).astype(int)}  = (3, 1)")
```

</PyRunner>

👉 [문제 03로 돌아가기](./problem-03)
