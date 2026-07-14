# 문제 9 · 실습 — 중요도 표집

중요도 가중치 $w=f/g=2x$로 $\mathbb{E}_p[x^2]$을 근사하고 참값 0.5와 비교합니다.

<PyRunner>

```python
import numpy as np
x = np.array([0.2, 0.4, 0.6, 0.8])
w = 2*x / 1.0                          # 중요도 가중치 f/g = 2x
h = x**2                              # h(x) = x^2
est = np.mean(w * h)                  # 기본 IS 추정 (f,g 모두 정규화)
print(f"표본 x = {x}")
print(f"가중치 w = 2x = {w}")
print(f"IS 추정 (1/M)Σ w h = {est:.4f}")
print(f"참값 E_p[x^2] = ∫ x^2 · 2x dx = 1/2 = 0.5")
print(f"오차 = {abs(est-0.5):.4f}  (표본 4개라 오차가 있음)")
```

</PyRunner>

👉 [문제 09로 돌아가기](./problem-09)
