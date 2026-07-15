# 문제 9 · 실습 — 베이즈 정리 (공장 불량품)

사후확률 $P(A\mid D)=\dfrac{4}{19}$ 을 정확한 분수 계산과 몬테카를로<span class="gloss">Monte Carlo</span>로 확인합니다.

<PyRunner>

```python
import numpy as np
from fractions import Fraction

pA, pB = Fraction(4, 10), Fraction(6, 10)
dA, dB = Fraction(2, 100), Fraction(5, 100)
post = pA*dA / (pA*dA + pB*dB)
print(f"이론값 P(A|불량) = {post} = {float(post):.4f}")

rng = np.random.default_rng(0)
N = 500000
fromA = rng.random(N) < 0.4
defect = np.where(fromA, rng.random(N) < 0.02, rng.random(N) < 0.05)
print(f"시뮬레이션 P(A|불량) = {fromA[defect].mean():.4f}")
```

</PyRunner>

👉 [문제 9로 돌아가기](./problem-09)
