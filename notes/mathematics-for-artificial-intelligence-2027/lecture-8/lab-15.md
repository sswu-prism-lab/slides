# 문제 15 · 실습 — 베이즈 정리로 사후확률 계산

두 주머니의 우도를 조합으로 구하고 베이즈 정리로 $P(A\mid \text{모두 빨강})$을 계산합니다.

<PyRunner>

```python
from math import comb
from fractions import Fraction

pA = pB = Fraction(1, 2)
red_A = Fraction(comb(5, 2), comb(8, 2))   # 10/28
red_B = Fraction(comb(2, 2), comb(8, 2))   # 1/28

post = pA * red_A / (pA * red_A + pB * red_B)
print(f"P(모두 빨강 | A) = {red_A} = {float(red_A):.4f}")
print(f"P(모두 빨강 | B) = {red_B} = {float(red_B):.4f}")
print(f"P(A | 모두 빨강) = {post} = {float(post):.4f}")
```

</PyRunner>

👉 [문제 15로 돌아가기](./problem-15)
