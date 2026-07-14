# 문제 2 · 실습 — 몬테카를로로 기댓값·분산 검증

해석적으로 구한 기댓값·분산을 대량 시뮬레이션으로 검증합니다. `▶ Run`을 누르면 두 결과가 거의 일치함을 확인할 수 있습니다.

<PyRunner>

```python
import numpy as np

# 해석적 결과
EX, VX = 3.5, 35/12
EY, EZ = EX/2, 3*EX/4
VY = EX/4 + VX/4
VZ = 3*EX/16 + 9*VX/16
covYZ = (3/8) * VX
VYZ = VY + VZ + 2 * covYZ
print("[해석적]")
print(f"  E[Y]={EY:.4f}  E[Z]={EZ:.4f}  E[Y+Z]={EY+EZ:.4f}")
print(f"  var[Y]={VY:.4f}  var[Z]={VZ:.4f}  cov[Y,Z]={covYZ:.4f}  var[Y+Z]={VYZ:.4f}")

# 몬테카를로 검증
rng = np.random.default_rng(0)
n = 2_000_000
X = rng.integers(1, 7, n)                 # 공정한 주사위
Y = rng.binomial(X, 0.5)                   # 공정한 동전 X번
Z = rng.binomial(X, 0.75)                  # 편향된 동전 X번
print("\n[몬테카를로]")
print(f"  E[Y]={Y.mean():.4f}  E[Z]={Z.mean():.4f}  E[Y+Z]={(Y+Z).mean():.4f}")
print(f"  var[Y]={Y.var():.4f}  var[Z]={Z.var():.4f}  cov[Y,Z]={np.cov(Y,Z)[0,1]:.4f}  var[Y+Z]={(Y+Z).var():.4f}")
```

</PyRunner>

👉 [문제 2로 돌아가기](./problem-02)
