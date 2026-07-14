# 문제 7 · 실습 — k-평균과 왜곡

E·M 단계를 재현하고 새 프로토타입에서 뒤틀림 척도 $J$를 계산합니다.

<PyRunner>

```python
import numpy as np
X = np.array([(1,1),(1,3),(3,1),(3,3),(8,8),(8,10)], float)
mu = np.array([[1,1],[10,10]], float)
d = ((X[:,None,:]-mu[None,:,:])**2).sum(2)
a = d.argmin(1)
mu_new = np.array([X[a==k].mean(0) for k in range(2)])
J = sum(((X[a==k]-mu_new[k])**2).sum() for k in range(2))
for k in range(2):
    pts = [tuple(p) for p in X[a==k].astype(int).tolist()]
    print(f"군집 {k+1}: {pts} -> {tuple(mu_new[k].tolist())}")
print(f"새 프로토타입: mu1={tuple(mu_new[0].tolist())}, mu2={tuple(mu_new[1].tolist())}")
print(f"뒤틀림 척도 J = {J}")
```

</PyRunner>

👉 [문제 07로 돌아가기](./problem-07)
