# 문제 7 · 실습 — 거부 표집

거부 상수 $k=\max p/q$를 구하고 후보의 수락 여부를 판정합니다.

<PyRunner>

```python
import numpy as np
p = lambda x: 6*x*(1-x)                          # 목표 밀도
q = 1.0                                          # Uniform[0,1] 밀도
xs = np.linspace(0, 1, 100001)
k = (p(xs)/q).max()
print(f"거부 상수 k = max p(x)/q(x) = {k:.3f}  (x=0.5에서 최대)")
xc, u = 0.8, 0.2
ratio = p(xc)/(k*q)
print(f"후보 x=0.8: p(x)={p(xc):.3f}, 수락 임계 p/(k q)={ratio:.3f}")
print(f"u=0.2 <= {ratio:.3f} ?  ->  {'수락 (ACCEPT)' if u <= ratio else '거부 (REJECT)'}")
```

</PyRunner>

👉 [문제 07로 돌아가기](./problem-07)
