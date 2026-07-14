# 문제 8 · 실습 — 중요도 표집

중요도 가중치 $w=p/q$로 기댓값을 근사하고 참값과 비교합니다.

<PyRunner>

```python
import numpy as np
x = np.array([0.5, 1.5])
w = 2*np.exp(-2*x) / np.exp(-x)                  # 중요도 가중치 p/q = 2 e^{-x}
print(f"중요도 가중치 w = {w.round(4)}")
print(f"기본 추정   (1/M) Σ w_i x_i      = {np.mean(w*x):.4f}")
print(f"자기정규화  Σ w_i x_i / Σ w_i    = {np.sum(w*x)/np.sum(w):.4f}")
print(f"참값 E_p[x] = 1/2 = 0.5  (표본 2개라 오차가 큼)")
```

</PyRunner>

👉 [문제 08로 돌아가기](./problem-08)
