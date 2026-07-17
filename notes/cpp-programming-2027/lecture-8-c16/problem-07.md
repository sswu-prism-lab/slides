# 문제 7 · 최소공배수와 최대공약수

::: info 문제 7 [2점]
아래 문제를 풀기 위한 의사알고리즘<span class="gloss">pseudo-algorithm</span>을 작성하세요.

임의의 두 정수를 입력받아 최소공배수<span class="gloss">LCM</span>와 최대공약수<span class="gloss">GCD</span>를 출력.
:::

::: details 풀이 및 해설
핵심은 **유클리드 호제법**<span class="gloss">Euclidean algorithm</span>으로 최대공약수(GCD)를 구한 뒤, 관계식

$$\text{LCM}(a,b) = \frac{a \times b}{\gcd(a,b)}$$

로 최소공배수(LCM)를 얻는 것입니다. (곱한 뒤 나누면 오버플로 위험이 있으므로 `a / g * b`처럼 먼저 나누는 편이 안전합니다.)

**의사알고리즘**

```
1. 두 정수 a, b를 입력받는다.
2. GCD 계산 (유클리드 호제법):
     x ← a, y ← b
     y가 0이 아닌 동안 반복:
         t ← x mod y
         x ← y
         y ← t
     반복이 끝나면 x가 최대공약수 g
3. 최소공배수 l ← (a / g) * b
4. g(최대공약수)와 l(최소공배수)를 출력한다.
```

예를 들어 `a = 12, b = 18`이면 $\gcd = 6$, $\text{lcm} = 12/6 \times 18 = 36$ 입니다.

$$\boxed{\gcd(12,18)=6,\quad \text{lcm}(12,18)=36}$$

👉 [실습(C++)에서 확인하기](./lab-07)
:::
