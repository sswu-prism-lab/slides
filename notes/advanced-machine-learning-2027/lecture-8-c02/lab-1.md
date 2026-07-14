# 문제 1 · 실습 — 2중 검사 사후확률

관측 (T1+, T2−)에 대해 각 클래스의 우도를 곱으로 계산하고 베이즈 정리로 사후확률을 구합니다.

<PyRunner>

```python
import numpy as np

pD = 0.005
sens = np.array([0.98, 0.95])   # T1, T2 민감도
spec = np.array([0.97, 0.96])   # T1, T2 특이도
obs_pos = np.array([True, False])   # 관측: T1+, T2-

L_D  = np.prod(np.where(obs_pos, sens, 1 - sens))
L_nD = np.prod(np.where(obs_pos, 1 - spec, spec))
post = L_D * pD / (L_D * pD + L_nD * (1 - pD))
print(f"P(관측 | D)  = {L_D:.4f}")
print(f"P(관측 | ~D) = {L_nD:.4f}")
print(f"P(D | T1+,T2-) = {post:.5f}  ({post*100:.3f}%)")
```

</PyRunner>

👉 [문제 1로 돌아가기](./problem-1)
