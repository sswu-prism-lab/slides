# 문제 4 · 실습 — $x^{\sin x}$ 미분 수치검증

해석적 도함수 $f'(x)=x^{\sin x}\!\left(\cos x\ln x+\dfrac{\sin x}{x}\right)$ 를 중앙차분<span class="gloss">central difference</span>으로 검증합니다.

<PyRunner>

```python
import numpy as np

def f(x):
    return x**np.sin(x)

def fprime(x):                       # 해석적 도함수
    return x**np.sin(x) * (np.cos(x)*np.log(x) + np.sin(x)/x)

x, h = 1.7, 1e-6
numeric = (f(x + h) - f(x - h)) / (2*h)
print(f"해석적 f'({x}) = {fprime(x):.8f}")
print(f"수치적 f'({x}) = {numeric:.8f}")
```

</PyRunner>

👉 [문제 4로 돌아가기](./problem-04)
