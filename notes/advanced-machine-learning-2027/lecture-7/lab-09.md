# 문제 9 · 실습 — 라플라스 근사 vs 수치적분

라플라스 근사로 얻은 정규화 상수 $Z$를 수치적분 결과와 비교합니다.

<PyRunner>

```python
import numpy as np

# p(x) ∝ exp(-3x^2 - x^4).  f(x) = 3x^2 + x^4 를 최소화 -> 최빈값
# f'(x) = 6x + 4x^3 = 2x(3 + 2x^2) = 0  ->  실근 x0 = 0
x0 = 0.0
fpp = 6 + 12 * x0**2                       # f''(x0) = 6
# 라플라스: exp(-f) ≈ exp(-1/2 f''(x0) x^2),  ∫ = sqrt(2π / f'')
Z_laplace = np.sqrt(2 * np.pi / fpp)       # = sqrt(pi/3)

xx = np.linspace(-6, 6, 2_000_001)
Z_true = np.sum(np.exp(-3 * xx**2 - xx**4)) * (xx[1] - xx[0])   # 수치적분

print(f"최빈값 x0        = {x0}")
print(f"f''(x0)          = {fpp}")
print(f"Z (라플라스 근사) = sqrt(2*pi/6) = sqrt(pi/3) = {Z_laplace:.4f}")
print(f"Z (수치적분)      = {Z_true:.4f}")
print(f"상대 오차         = {abs(Z_laplace - Z_true)/Z_true*100:.1f}%  (x^4 항 무시로 인한 과대추정)")
```

</PyRunner>

👉 [문제 9로 돌아가기](./problem-09)
