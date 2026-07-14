# 문제 3 · 실습 — 기대 손실 기반 결정 경계

각 위치에서 두 예측의 기대 손실을 비교해 결정이 바뀌는 경계점을 수치로 찾습니다.

<PyRunner>

```python
import numpy as np

def N(x, m, s):
    return np.exp(-(x - m)**2 / (2 * s*s)) / np.sqrt(2 * np.pi * s*s)

pC1, pC2 = 0.4, 0.6
# 기대 손실: predict C1 -> p(C2|x),  predict C2 -> 5 p(C1|x)
# C1로 결정: p(C2|x) < 5 p(C1|x)  <=>  p(x|C2)p(C2) < 5 p(x|C1)p(C1)
x = np.linspace(-8, 12, 20001)
risk_C1 = N(x, 3, 2) * pC2                 # ∝ p(C2|x)
risk_C2 = 5 * N(x, 1, 1) * pC1             # ∝ 5 p(C1|x)
decide_C1 = risk_C1 < risk_C2

# 결정이 바뀌는 경계점 찾기
switch = np.where(np.diff(decide_C1.astype(int)) != 0)[0]
bounds = [(x[i] + x[i+1]) / 2 for i in switch]
print("결정 경계점 x =", [f"{b:+.3f}" for b in bounds], "  (이론값: -2.281, +2.948)")
print(f"C1로 결정하는 구간: {bounds[0]:+.3f} < x < {bounds[1]:+.3f}")
for xt in [-4, 0, 8]:
    d = "C1" if (N(xt,3,2)*pC2 < 5*N(xt,1,1)*pC1) else "C2"
    print(f"  x={xt:+.1f} -> {d}")
```

</PyRunner>

👉 [문제 3로 돌아가기](./problem-03)
