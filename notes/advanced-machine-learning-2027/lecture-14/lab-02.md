# 문제 2 · 실습 — 베이즈망 전수 계산

다섯 이진 변수의 결합확률을 모두 나열해 $p(B=1\mid E=1)$을 직접 구하고, $p(B=1)$과 같음(콜라이더로 인한 독립)을 확인합니다.

<PyRunner>

```python
import numpy as np
from itertools import product

pA1, pB1 = 0.3, 0.4
pC1 = {(1,1):0.9, (1,0):0.6, (0,1):0.5, (0,0):0.1}   # p(C=1|A,B)
pD1 = {1:0.7, 0:0.2}                                  # p(D=1|A)
pE1 = {1:0.8, 0:0.3}                                  # p(E=1|D)

num = den = 0.0
for A, B, C, D, E in product([0, 1], repeat=5):
    j  = (pA1 if A else 1-pA1) * (pB1 if B else 1-pB1)
    j *= (pC1[(A,B)] if C else 1-pC1[(A,B)])
    j *= (pD1[A] if D else 1-pD1[A])
    j *= (pE1[D] if E else 1-pE1[D])
    if E == 1:
        den += j
        if B == 1:
            num += j
print(f"p(E=1)     = {den:.4f}")
print(f"p(B=1,E=1) = {num:.4f}")
print(f"p(B=1|E=1) = {num/den:.4f}")
print(f"참고: p(B=1)={pB1} 과 동일 -> 콜라이더 C(미관측)로 B와 E는 독립")
```

</PyRunner>

👉 [문제 02로 돌아가기](./problem-02)
