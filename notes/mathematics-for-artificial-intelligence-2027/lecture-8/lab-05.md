# 문제 5 · 실습 — 로그 방정식의 해 확인

후보 $x=16$과 $x=\frac{1}{16}$에서 $\log_x 16$과 $\log_{16}x$가 실제로 같은지 확인합니다.

<PyRunner>

```python
import numpy as np

# log_x 16 = log_16 x  =>  t = log_16 x,  1/t = t  =>  t = ±1  =>  x = 16, 1/16
for x in [16, 1/16]:
    lhs = np.log(16) / np.log(x)   # log_x(16)
    rhs = np.log(x) / np.log(16)   # log_16(x)
    print(f"x = {x:>7}: log_x(16) = {lhs:+.4f}, log_16(x) = {rhs:+.4f}, "
          f"일치? {np.isclose(lhs, rhs)}")
```

</PyRunner>

👉 [문제 5로 돌아가기](./problem-05)
