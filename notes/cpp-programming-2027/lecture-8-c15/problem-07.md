# 문제 7 · 최소공배수 의사알고리즘

::: info 문제 7 [2점]
아래 문제를 풀기 위한 의사알고리즘<span class="gloss">pseudo-algorithm</span>을 작성하세요.

사용자가 0을 입력할 때까지 양의 정수를 입력받은 후, 큰 두 수의 최소공배수<span class="gloss">least common multiple</span>를 출력하시오.
:::

::: details 풀이 및 해설
핵심은 (1) 0이 나올 때까지 반복 입력하며 **가장 큰 두 수**를 추적하고, (2) 두 수의 **최대공약수<span class="gloss">GCD</span>**를 이용해 최소공배수를 구하는 것입니다.

$$\text{lcm}(a,b) = \frac{a \times b}{\gcd(a,b)}$$

**의사알고리즘**

```
largest ← 0, second ← 0
반복:
    x 를 입력받는다
    만약 x == 0 이면 반복 종료
    만약 x > largest 이면
        second ← largest
        largest ← x
    아니고 x > second 이면
        second ← x

g ← gcd(largest, second)        // 유클리드 호제법
lcm ← largest / g × second
lcm 을 출력
```

**유클리드 호제법**으로 최대공약수를 구합니다.

```
gcd(a, b):
    b 가 0이 아닌 동안 반복:
        t ← a mod b
        a ← b
        b ← t
    a 를 반환
```

`12, 18, 8, 0`을 입력하면 큰 두 수는 `18`과 `12`이고 $\gcd(18,12)=6$이므로 $\text{lcm}=\dfrac{18\times 12}{6}=36$.

$$\boxed{\text{lcm}(18, 12) = 36}$$

👉 [실습(C++)에서 확인하기](./lab-07)
:::
