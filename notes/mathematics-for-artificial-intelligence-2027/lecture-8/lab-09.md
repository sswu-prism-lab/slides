# 문제 9 · 실습 — 포아송 확률의 대소 비교

$\lambda=7$에서 $P(X=5)$와 $P(X=9)$를 직접 계산해 대소를 비교합니다.

<PyRunner>

```python
from math import exp, factorial

lam = 7
def pois(k):
    return exp(-lam) * lam ** k / factorial(k)

p5, p9 = pois(5), pois(9)
print(f"P(X=5) = {p5:.4f}")
print(f"P(X=9) = {p9:.4f}")
print(f"비율 P(X=5)/P(X=9) = {p5 / p9:.4f}")
print("결론:", "P(X=5) > P(X=9)" if p5 > p9 else "P(X=5) < P(X=9)")
```

</PyRunner>

👉 [문제 9로 돌아가기](./problem-09)
