# 문제 9 · 실습 — 조각 구간

조각 구간 $S=\{z:f(z)\ge u\}$를 구하고 후보의 수락 여부를 판정합니다.

<PyRunner>

```python
import numpy as np
f = lambda z: 1 - np.abs(z)                      # (정규화된) 밀도, z in [-1,1]
z0, u = 0.5, 0.2
print(f"f(z0={z0}) = {f(z0)}   (u={u} 이하이어야 슬라이스 유효: OK)")
half = 1 - u                                     # S = {z: f(z) >= u} = {|z| <= 1-u}
print(f"조각 구간 S = [-{half}, {half}]")
zc = -0.7
print(f"후보 z*={zc}: f(z*)={f(zc):.1f} >= u={u} ?  ->  {'수락 (ACCEPT)' if f(zc) >= u else '거부 (REJECT)'}")
```

</PyRunner>

👉 [문제 09로 돌아가기](./problem-09)
