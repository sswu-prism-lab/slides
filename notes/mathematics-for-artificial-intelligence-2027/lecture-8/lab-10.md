# 문제 10 · 실습 — 매클로린 급수 수치 근사

일반항 $\sum \frac{(-1)^n}{(2n)!}x^{2n-1}$의 부분합이 $\cos x / x$에 수렴하는지 $x=1$에서 확인합니다.

<PyRunner>

```python
from math import cos, factorial

x = 1.0
partial = sum((-1) ** n * x ** (2 * n - 1) / factorial(2 * n) for n in range(6))
exact = cos(x) / x
print(f"부분합(항 6개) = {partial:.6f}")
print(f"cos(x)/x      = {exact:.6f}")
print(f"오차          = {abs(partial - exact):.2e}")
```

</PyRunner>

👉 [문제 10으로 돌아가기](./problem-10)
