# 문제 7 · 실습 — 복소수 방정식의 근

이차방정식 $z^2-2iz+1=0$ 의 근을 구하고 $z+\dfrac1z=2i$ 를 만족하는지 확인합니다.

<PyRunner>

```python
import numpy as np

# z^2 - 2i z + 1 = 0  ->  계수 [1, -2i, 1]
roots = np.roots([1, -2j, 1])
for z in roots:
    print(f"z = {z:.6f}   z + 1/z = {z + 1/z:.6f}")

print("이론값 (1±√2)i =",
      f"{(1 + np.sqrt(2))*1j:.6f},", f"{(1 - np.sqrt(2))*1j:.6f}")
```

</PyRunner>

👉 [문제 7로 돌아가기](./problem-07)
