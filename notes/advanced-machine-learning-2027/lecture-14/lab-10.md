# 문제 10 · 실습 — PCA 고유분해

공분산 행렬의 고유분해로 제1 주성분을 계산합니다.

<PyRunner>

```python
import numpy as np
D = np.array([[1,0],[0,1],[1,1]], float)
xbar = D.mean(0)
S = ((D - xbar).T @ (D - xbar)) / len(D)         # 공분산 (1/N)
vals, vecs = np.linalg.eigh(S)                   # 고윳값 오름차순
print(f"평균 x̄ = {xbar}")
print("공분산 S =\n", S)
print(f"고윳값 = {vals.round(4)}")
print(f"제1 주성분 (λ={vals[-1]:.4f}) = {vecs[:,-1].round(4)}  (∝ (1, -1)/√2)")
```

</PyRunner>

👉 [문제 10로 돌아가기](./problem-10)
