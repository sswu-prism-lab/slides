# 문제 16 · 실습 — 이산 합성곱

`numpy.convolve` 로 $y[n]=(x\star h)[n]=[1,3,4,3,1]$ 을 확인하고, 정의식 직접 합산과 비교합니다.

<PyRunner>

```python
import numpy as np

x = np.array([1, 2, 1])   # x[0..2]
h = np.array([1, 1, 1])   # h[0..2]

y_np = np.convolve(x, h)          # numpy 합성곱
# 정의식 직접 계산: y[n] = sum_k x[k] h[n-k]
y_def = [int(sum(x[k] * h[n-k] for k in range(len(x))
             if 0 <= n-k < len(h))) for n in range(len(x)+len(h)-1)]

print("numpy  y[n] =", y_np)      # [1 3 4 3 1]
print("정의식 y[n] =", y_def)
```

</PyRunner>

👉 [문제 16으로 돌아가기](./problem-16)
