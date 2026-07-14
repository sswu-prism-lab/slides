# 문제 6 · 실습 — 라플라스 근사 곡선

최빈값과 곡률을 구해 가우시안 근사 $q(\theta)=\mathcal{N}(2,1/2)$를 원래 밀도와 비교합니다.

<PyRunner>

```python
import numpy as np

g = lambda u: u**4 / 4 + u**2          # 지수부 -g,  u = θ-2
theta0, gpp = 2.0, 2.0                  # g'(0)=0 -> θ0=2 ; g''(0)=2
print(f"최빈값 θ0 = {theta0},  g''(θ0) = {gpp},  분산 = 1/g'' = {1/gpp}")
print(" θ    p_true  p_laplace")
for th in np.linspace(0, 4, 9):
    p_true = np.exp(-g(th - 2))
    p_lap  = np.exp(-(th - 2)**2)       # exp(-1/2 g'' u^2) = exp(-u^2)
    print(f"{th:4.1f}   {p_true:6.3f}   {p_lap:6.3f}")
print("라플라스 근사 q(θ) = N(2, 1/2)")
```

</PyRunner>

👉 [문제 6로 돌아가기](./problem-6)
