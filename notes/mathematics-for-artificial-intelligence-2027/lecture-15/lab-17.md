# 문제 17 · 실습 — 복소함수의 극값 ($|z|=1$)

단위원 위 여러 점에서 $|f(z)|$ 를 계산하여 값이 항상 $\tfrac12$ 로 일정함을 확인합니다.

<PyRunner>

```python
import numpy as np

theta = np.linspace(0, 2*np.pi, 9)   # 단위원 위의 점 z = e^{iθ}
z = np.exp(1j * theta)
f = z / (1 + np.abs(z)**2)           # |z|=1 이므로 분모는 항상 2
mag = np.abs(f)

print("|f(z)| 값들 =", np.round(mag, 6))
print(f"극댓값 = {mag.max():.4f},  극솟값 = {mag.min():.4f}")   # 둘 다 0.5
```

</PyRunner>

👉 [문제 17로 돌아가기](./problem-17)
