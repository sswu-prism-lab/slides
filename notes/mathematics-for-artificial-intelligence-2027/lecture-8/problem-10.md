# 문제 10 · 매클로린 급수

::: info 문제 10 [3점]
$\dfrac{\cos x}{x}$의 매클로린 급수<span class="gloss">Maclaurin series</span>를 구하고(2점), 이를 $\sum$ 기호를 사용하여 일반항으로 표현(1점)하시오.
:::

::: details 풀이 및 해설
$\cos x$의 매클로린 급수는 잘 알려져 있습니다.

$$
\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}x^{2n}.
$$

양변을 $x$로 나누면(각 항을 $x$로 나눔)

$$
\frac{\cos x}{x} = \frac{1}{x} - \frac{x}{2!} + \frac{x^3}{4!} - \frac{x^5}{6!} + \cdots.
$$

일반항으로 정리하면

$$
\boxed{\;\frac{\cos x}{x} = \sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}\,x^{2n-1}\;}
$$

입니다. 첫 항이 $x^{-1}$이므로 엄밀히는 $x=0$에서 특이점을 갖는 로랑<span class="gloss">Laurent</span> 급수이지만, $\cos x$의 급수를 항별로 $x$로 나눈 형태로 표현됩니다.

👉 [실습(Python)에서 확인하기](./lab-10)
:::
