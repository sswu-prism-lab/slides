# 문제 4 · 실습 — 지수방정식 풀이

$5^{2x-1}=125$에서 밑을 $5$로 통일해 지수를 비교하고, 로그로 직접 $x$를 구합니다.

<PyRunner>

```python
import numpy as np

# 5^(2x-1) = 125  ->  2x-1 = log_5(125)  ->  x = (log_5(125)+1)/2
exp_val = np.log(125) / np.log(5)   # = 3
x = (exp_val + 1) / 2
print(f"2x-1 = log_5(125) = {exp_val:.4f}")
print(f"x = {x:.4f}")
print("검산 5^(2x-1) =", 5 ** (2 * x - 1))
```

</PyRunner>

👉 [문제 4로 돌아가기](./problem-04)
