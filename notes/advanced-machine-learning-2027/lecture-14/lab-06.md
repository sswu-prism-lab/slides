# 문제 6 · 실습 — 변분 해 검증

닫힌 해 $m, s^2$를 계산하고, 켤레 사후분포 및 ELBO 격자 최대점과 일치함을 확인합니다.

<PyRunner>

```python
import numpy as np
mu0, tau2, x, sig2 = 0.0, 2.0, 3.0, 1.0        # 예시 값
# 변분 해 (일반식): s^2 = 1/(1/tau0^2 + 1/sig^2),  m = s^2 (mu0/tau0^2 + x/sig^2)
s2 = 1 / (1/tau2 + 1/sig2)
m  = s2 * (mu0/tau2 + x/sig2)
print(f"변분 해:  m = {m:.4f},  s^2 = {s2:.4f}")
prec = 1/tau2 + 1/sig2                          # 켤레라 정확한 사후분포와 동일
print(f"정확 사후: mean = {(mu0/tau2 + x/sig2)/prec:.4f},  var = {1/prec:.4f}")
mm = np.linspace(0, 4, 401); ss = np.linspace(0.05, 2, 401)
Mg, Sg = np.meshgrid(mm, ss)
E = (-0.5*((x-Mg)**2 + Sg)/sig2 - 0.5*((Mg-mu0)**2 + Sg)/tau2
     + 0.5*np.log(Sg) - 0.5*np.log(sig2) - 0.5*np.log(tau2) + 0.5 - 0.5*np.log(2*np.pi))
i = np.unravel_index(E.argmax(), E.shape)
print(f"ELBO 최대(격자탐색): m = {Mg[i]:.3f},  s^2 = {Sg[i]:.3f}")
```

</PyRunner>

👉 [문제 06로 돌아가기](./problem-06)
