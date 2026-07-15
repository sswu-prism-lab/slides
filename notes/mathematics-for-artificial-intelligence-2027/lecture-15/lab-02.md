# 문제 2 · 실습 — 매클로린 급수로 $\sin(x^3+2x)$ 근사

일반항 급수의 부분합이 실제 $\sin(x^3+2x)$ 값에 수렴하는지 확인합니다.

<PyRunner>

```python
import numpy as np, math

def maclaurin(x, N):          # 부분합: k=0..N-1
    u = x**3 + 2*x
    return sum((-1)**k / math.factorial(2*k + 1) * u**(2*k + 1)
               for k in range(N))

for x in [0.1, 0.3, 0.5]:
    approx = maclaurin(x, 8)
    exact = np.sin(x**3 + 2*x)
    print(f"x={x}:  급수합={approx:.10f}   sin(x^3+2x)={exact:.10f}")
```

</PyRunner>

👉 [문제 2로 돌아가기](./problem-02)
