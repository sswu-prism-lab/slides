# 문제 9 · 실습 — 거부 표집

거부 상수 $k$, 후보의 채택 여부, 평균 표집 횟수를 계산합니다.

<PyRunner>

```python
import numpy as np
f = lambda x: 1.5*(1 - x**2)     # 목표 밀도 (정규화됨)
g = 1.0                          # Uniform[0,1]
xs = np.linspace(0, 1, 100001)
k = (f(xs)/g).max()
print(f"거부 상수 k = max f/g = {k:.3f}  (x=0에서 최대)")
xc, u = 0.25, 0.8
ratio = f(xc)/(k*g)
print(f"후보 x=0.25: f(x)={f(xc):.4f}, 수락 임계 f/(k g)={ratio:.4f}")
print(f"u=0.8 <= {ratio:.4f} ?  ->  {'수락 (ACCEPT)' if u<=ratio else '거부 (REJECT)'}")
print(f"평균 표집 횟수 = k = {k}  (수락 확률 1/k = {1/k:.3f})")
```

</PyRunner>

👉 [문제 09로 돌아가기](./problem-09)
