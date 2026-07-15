# 문제 8 · 실습 — 매개변수 미분 $dy/dx$ 수치검증

해석적 결과 $\dfrac{dy}{dx}=\dfrac{3t^2e^{t^3}}{2t+\cos t}$ 를 $\dfrac{\Delta y}{\Delta x}$ 로 검증합니다.

<PyRunner>

```python
import numpy as np

x = lambda t: t**2 + np.sin(t)
y = lambda t: np.exp(t**3)
dydx = lambda t: 3*t**2 * np.exp(t**3) / (2*t + np.cos(t))   # 해석적

t, h = 0.8, 1e-6
numeric = (y(t + h) - y(t - h)) / (x(t + h) - x(t - h))
print(f"해석 dy/dx(t={t}) = {dydx(t):.6f}")
print(f"수치 dy/dx(t={t}) = {numeric:.6f}")
```

</PyRunner>

👉 [문제 8로 돌아가기](./problem-08)
