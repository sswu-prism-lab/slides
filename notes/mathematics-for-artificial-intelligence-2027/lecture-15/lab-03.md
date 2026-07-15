# 문제 3 · 실습 — 조건부 확률 (비복원 추출)

이론값 $6/11$ 을 대규모 몬테카를로 시뮬레이션<span class="gloss">Monte Carlo</span>으로 확인합니다.

<PyRunner>

```python
import numpy as np
from fractions import Fraction

# 첫 공이 빨강일 때 남은 11개 중 파랑 6개
theory = Fraction(6, 11)

rng = np.random.default_rng(0)
box = ['R']*4 + ['B']*6 + ['G']*2   # 빨강4, 파랑6, 녹색2
hit = tot = 0
for _ in range(200000):
    a, b = rng.choice(len(box), size=2, replace=False)
    if box[a] == 'R':               # 조건: 첫 공이 빨강
        tot += 1
        hit += (box[b] == 'B')      # 두번째가 파랑

print(f"이론값 P = {theory} = {float(theory):.4f}")
print(f"시뮬레이션 P = {hit/tot:.4f}")
```

</PyRunner>

👉 [문제 3으로 돌아가기](./problem-03)
