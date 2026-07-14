# 문제 4 · 실습 — 결측치 EM 2회

공분산이 $I$이므로 결측치를 현재 $\mu$로 채우고 열 평균으로 갱신하는 과정을 두 번 반복합니다.

<PyRunner>

```python
import numpy as np
M = np.array([[1,2],[2,np.nan],[np.nan,3],[4,5],[5,4]], float)
mu = np.array([2., 2.])
print(f"초기 mu = ({mu[0]}, {mu[1]})")
for it in range(2):
    F = M.copy()
    miss = np.isnan(F)
    F[miss] = np.take(mu, np.where(miss)[1])   # E 단계: 결측치를 mu로 채움 (cov=I)
    mu = F.mean(0)                              # M 단계: 열 평균
    print(f"iter {it+1}: mu = ({mu[0]:.4f}, {mu[1]:.4f})")
```

</PyRunner>

👉 [문제 04로 돌아가기](./problem-04)
