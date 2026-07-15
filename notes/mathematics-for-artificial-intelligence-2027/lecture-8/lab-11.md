# 문제 11 · 실습 — 합성함수 값 계산

$h(x)=f(g(x))=\sqrt{2x^2+1}$을 정의하고 $h(2)$를 계산합니다.

<PyRunner>

```python
import numpy as np

f = lambda t: np.sqrt(2 * t + 3)
g = lambda x: x ** 2 - 1
h = lambda x: f(g(x))          # = sqrt(2x^2 + 1)

xs = np.linspace(-3, 3, 7)
print("정의역: 모든 실수 (2x^2+1 >= 1 > 0 이므로 근호 안이 항상 양수)")
print("표본값 h(x):", np.round(h(xs), 3))
print(f"h(2) = {h(2):.0f}")
```

</PyRunner>

👉 [문제 11로 돌아가기](./problem-11)
