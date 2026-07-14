# 문제 7 · 실습 — 피셔 판별 경계 계산

클래스 내 산포 행렬 $\mathbf{S}_\mathrm{W}$와 판별 방향 $\mathbf{w}$, 결정 경계를 계산합니다.

<PyRunner>

```python
import numpy as np

C1 = np.array([[0, 0], [1, 0], [0, 1]], float)
C2 = np.array([[2, 1], [3, 1], [2, 2]], float)
m1, m2 = C1.mean(0), C2.mean(0)

SW = (C1 - m1).T @ (C1 - m1) + (C2 - m2).T @ (C2 - m2)   # 클래스 내 산포 행렬
w = np.linalg.inv(SW) @ (m2 - m1)                        # w ∝ S_W^-1 (m2 - m1)
thr = w @ ((m1 + m2) / 2)                                # 두 평균 중점 투영 = 임곗값

print("m1 =", m1, "  m2 =", m2)
print("S_W =\n", SW)
print(f"w  ∝ {w}")
s = 2.0                                                  # 정수비로: (2.5, 2) x 2 = (5, 4)
print(f"결정 경계:  {w[0]*s:.0f} x1 + {w[1]*s:.0f} x2 = {thr*s:.0f}")
print("즉  5 x1 + 4 x2 = 10  (w^T x < 10 이면 C1, 아니면 C2)")
```

</PyRunner>

👉 [문제 7로 돌아가기](./problem-07)
