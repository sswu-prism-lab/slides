# 문제 6 · 실습 — 역함수 검증

$f^{-1}(x)=\dfrac{\ln x-1}{2}$ 가 실제로 $f(x)=e^{2x+1}$ 의 역함수인지 $f(f^{-1}(x))=x$ 로 확인합니다.

<PyRunner>

```python
import numpy as np

f = lambda x: np.exp(2*x + 1)
finv = lambda x: (np.log(x) - 1) / 2

for x in [0.5, 1.0, 3.0]:
    print(f"x={x}:  f(finv(x))={f(finv(x)):.6f}   finv(f(x))={finv(f(x)):.6f}")
```

</PyRunner>

👉 [문제 6으로 돌아가기](./problem-06)
