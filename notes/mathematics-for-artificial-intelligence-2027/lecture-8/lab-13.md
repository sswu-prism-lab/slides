# 문제 13 · 실습 — 단위원 위의 복소근

$\theta=k\pi/3$에서 $z=e^{i\theta}$가 $\lVert z\rVert=1$과 $\mathfrak{I}(z^3)=0$을 만족하는지 확인합니다.

<PyRunner>

```python
import numpy as np

print("k   z                        |z|     Im(z^3)")
for k in range(6):
    theta = k * np.pi / 3
    z = np.cos(theta) + 1j * np.sin(theta)
    im3 = (z ** 3).imag
    print(f"{k}   {z.real:+.3f}{z.imag:+.3f}i        {abs(z):.3f}   {im3:+.3f}")
print("\n6개 근 모두 |z|=1 이고 Im(z^3)=0 (수치오차 범위 내)")
```

</PyRunner>

👉 [문제 13으로 돌아가기](./problem-13)
