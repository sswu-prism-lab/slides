# 문제 6 · 실습 — 라플라스 붕괴와 정확한 값

최빈값에서 곡률이 0이라 표준 라플라스가 붕괴함을 보이고, 정확한 값 $\tfrac12\Gamma(1/4)$을 수치적분과 비교합니다.

<PyRunner>

```python
import numpy as np
from math import gamma

# Z = ∫ exp(-(x^2-4x+4)^2) dx = ∫ exp(-(x-2)^4) dx,  u = x-2
# 최빈값 x0 = 2.  지수 h(u)=u^4 -> h''(0)=0 : 2차(가우시안) 라플라스 붕괴.
xx = np.linspace(-6, 10, 2_000_001)
Z_num = np.sum(np.exp(-(xx - 2)**4)) * (xx[1] - xx[0])
Z_exact = 0.5 * gamma(0.25)
print("최빈값 x0 = 2,  h(u) = u^4,  h''(0) = 0")
print("2차 곡률이 0이라 표준 가우시안 라플라스 근사는 직접 적용 불가 (분산 -> 무한).")
print(f"정확한 값 Z = (1/2)Γ(1/4) = {Z_exact:.4f}")
print(f"수치적분  Z = {Z_num:.4f}")
```

</PyRunner>

👉 [문제 6로 돌아가기](./problem-6)
