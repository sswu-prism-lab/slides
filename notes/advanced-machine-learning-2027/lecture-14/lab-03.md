# 문제 3 · 실습 — k-평균 1회 반복

E 단계(할당)와 M 단계(평균 갱신)를 코드로 재현합니다.

<PyRunner>

```python
import numpy as np
X = np.array([1, 2, 4, 5], float)
mu = np.array([1., 5.])                                   # 초기 프로토타입
assign = np.abs(X[:, None] - mu[None, :]).argmin(1)       # E: 가까운 쪽에 할당
mu_new = np.array([X[assign == k].mean() for k in range(2)])  # M: 군집 평균
for k in range(2):
    print(f"군집 {k+1}: {X[assign==k]}  ->  새 프로토타입 {mu_new[k]}")
print(f"갱신 결과: mu1={mu_new[0]}, mu2={mu_new[1]}")
```

</PyRunner>

👉 [문제 03로 돌아가기](./problem-03)
