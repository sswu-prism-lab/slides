# 문제 1 · 실습 — 베이즈 정리로 진단 확률 계산

검사 횟수에 따라 사후확률 $P(D\mid n\text{개 양성})$가 어떻게 변하는지 직접 계산해 봅니다.

<PyRunner>

```python
import numpy as np

# 민감도(sensitivity)=P(+|D), 특이도(specificity)=P(-|not D)
p_D, sens, spec = 0.005, 0.95, 0.90
p_notD = 1 - p_D
p_pos_D = sens              # P(+|D)
p_pos_notD = 1 - spec       # P(+|not D) = 위양성률

def posterior(n):           # n번 연속 양성일 때 P(D | n개 양성)
    like_D = p_pos_D ** n
    like_notD = p_pos_notD ** n
    return like_D * p_D / (like_D * p_D + like_notD * p_notD)

print(f"검사 1회 양성 -> P(D|+)   = {posterior(1):.4f}")
print(f"검사 4회 양성 -> P(D|4+)  = {posterior(4):.4f}")
print("\n반복 검사가 위양성을 걸러내며 사후확률이 4.6% -> 97.6%로 상승합니다.")
```

</PyRunner>

👉 [문제 1로 돌아가기](./problem-01)
