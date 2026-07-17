# 문제 14 · 바젤 급수로 π 근사

::: info 문제 14 [3점]
아래 원주율 $\pi$를 근사<span class="gloss">approximation</span>하기 위한 공식(오일러 급수<span class="gloss">Euler's series</span>)을 구현한 코드의 빈칸을 채우세요.

$$\pi = \sqrt{\,6\left(1 + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \cdots + \frac{1}{n^2}\right)}$$

```cpp
cout << "정수 n을 입력하세요: ";
int n;
cin >> n;
double sum = 0.0;

// 오일러 급수 표현, 빈칸을 채우세요.
for (int i = 1; i <= n; i++) {
    /* 각 항을 합산합니다.
    빈칸 1
    */
}
/* 급수를 바탕으로 π 값을 계산합니다.
빈칸 2
*/
```
:::

::: details 풀이 및 해설
이 급수는 **바젤 문제**<span class="gloss">Basel problem</span>의 결과로, 제곱수 역수의 합이 다음과 같이 알려져 있습니다.

$$\sum_{k=1}^{\infty}\frac{1}{k^2} = 1 + \frac{1}{2^2} + \frac{1}{3^2} + \cdots = \frac{\pi^2}{6}$$

양변을 정리하면 $\pi^2 = 6\sum \frac{1}{k^2}$, 따라서 $\pi = \sqrt{6\sum \frac{1}{k^2}}$ 입니다. 그러므로

- **빈칸 1** — 각 항 $\dfrac{1}{i^2}$을 `sum`에 누적. 정수 나눗셈을 피하려고 분자를 `1.0`(실수)으로 둡니다.

```cpp
sum += 1.0 / (static_cast<double>(i) * i);   // = 1 / i^2
```

- **빈칸 2** — 누적된 합에 6을 곱하고 제곱근을 취해 π를 계산·출력. `sqrt`를 쓰려면 `<cmath>`가 필요합니다.

```cpp
double pi = sqrt(6.0 * sum);
cout << "근사한 pi = " << pi << endl;
```

$$\boxed{\texttt{sum += 1.0 / (double)(i) / i;}\qquad \texttt{pi = sqrt(6.0 * sum);}}$$

`n`이 커질수록 $\sqrt{6\sum}$가 실제 $\pi = 3.14159\ldots$에 가까워집니다. (예: `n = 100000`이면 약 `3.14158`)

👉 [실습(C++)에서 확인하기](./lab-14)
:::
