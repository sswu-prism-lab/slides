# 문제 1 · 실습 — 3중 검사 사후확률

관측 (A+, B+, C−)에 대해 각 클래스의 우도를 곱으로 계산하고 베이즈 정리로 사후확률을 구합니다.

<PyRunner>

```python
import numpy as np

pD = 0.01
sens = np.array([0.9, 0.85, 0.8])    # A, B, C 민감도
spec = np.array([0.95, 0.9, 0.85])   # A, B, C 특이도
obs_pos = np.array([True, True, False])   # 관측: A+, B+, C-

L_D  = np.prod(np.where(obs_pos, sens, 1 - sens))   # P(관측 | D)
L_nD = np.prod(np.where(obs_pos, 1 - spec, spec))   # P(관측 | ~D)
post = L_D * pD / (L_D * pD + L_nD * (1 - pD))
print(f"P(관측 | D)  = {L_D:.4f}")
print(f"P(관측 | ~D) = {L_nD:.5f}")
print(f"P(D | A+,B+,C-) = {post:.4f}  ({post*100:.1f}%)")
```

</PyRunner>

👉 [문제 1로 돌아가기](./problem-1)
