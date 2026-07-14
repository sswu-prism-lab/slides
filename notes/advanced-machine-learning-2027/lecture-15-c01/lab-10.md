# 문제 10 · 실습 — PCA 고유분해

공분산 행렬의 고유분해로 제1 주성분을 계산합니다.

<PyRunner>

```python
import numpy as np
D = np.array([(3,1),(1,3),(0,0),(2,2)], float)
S = ((D-D.mean(0)).T @ (D-D.mean(0))) / len(D)
v, V = np.linalg.eigh(S)
print(f"평균={D.mean(0)}\n공분산 S=\n{S}\n고윳값={v.round(4)}")
print(f"제1 주성분 (λ={v[-1]:.4f}) = {V[:,-1].round(4)}  (∝ (1, 1)/√2)")
```

</PyRunner>

👉 [문제 10로 돌아가기](./problem-10)
