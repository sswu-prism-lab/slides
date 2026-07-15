# 문제 7 · 실습 — 이항분포 확률

$B(4,\,0.1)$에서 결함이 정확히 $1$개일 확률을 공식으로 계산하고, 몬테카를로 시뮬레이션으로 확인합니다.

<PyRunner>

```python
import numpy as np
from math import comb

n, p = 4, 0.1
prob = comb(n, 1) * p ** 1 * (1 - p) ** 3
print(f"P(X=1) = C(4,1)·0.1·0.9^3 = {prob:.4f}")

# 시뮬레이션 검증
rng = np.random.default_rng(0)
trials = rng.random((200000, n)) < p        # 결함이면 True
est = np.mean(trials.sum(axis=1) == 1)
print(f"시뮬레이션 추정치     = {est:.4f}")
```

</PyRunner>

👉 [문제 7로 돌아가기](./problem-07)
