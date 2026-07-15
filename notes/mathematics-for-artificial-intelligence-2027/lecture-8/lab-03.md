# 문제 3 · 실습 — 비복원 조합 확률

순차적으로 뽑는 확률과 조합으로 계산한 확률이 같은지 확인합니다.

<PyRunner>

```python
from math import comb
from fractions import Fraction

# 순차 확률: 첫 번째 회원 6/10, 두 번째 회원 5/9
seq = Fraction(6, 10) * Fraction(5, 9)
# 조합 확률: C(6,2)/C(10,2)
comb_p = Fraction(comb(6, 2), comb(10, 2))

print(f"순차 확률   = {seq}  = {float(seq):.4f}")
print(f"조합 확률   = {comb_p}  = {float(comb_p):.4f}")
print(f"두 방법 일치? {seq == comb_p}")
```

</PyRunner>

👉 [문제 3으로 돌아가기](./problem-03)
