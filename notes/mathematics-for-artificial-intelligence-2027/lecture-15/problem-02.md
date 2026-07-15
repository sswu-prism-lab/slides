# 문제 2 · 매클로린 급수 (합성함수)

::: info 문제 2 [1점]
아래 두 함수 $f(x)$, $g(x)$에 대해 $f\circ g(x)$의 매클로린 급수<span class="gloss">Maclaurin series</span>를 $\sum$을 사용한 일반항으로 표현하시오.

$$
f(x)=\sin x,\qquad g(x)=x^3+2x
$$
:::

::: details 풀이 및 해설
$f\circ g(x)=\sin(g(x))=\sin(x^3+2x)$ 이다.

사인 함수의 매클로린 급수는 다음과 같다.

$$
\sin u=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)!}\,u^{2k+1}
=u-\frac{u^3}{3!}+\frac{u^5}{5!}-\cdots
$$

여기에 $u=g(x)=x^3+2x$ 를 그대로 대입하면 (합성함수의 급수는 안쪽 함수를 변수 자리에 대입하여 얻는다)

$$
\boxed{\;\sin(x^3+2x)=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)!}\,(x^3+2x)^{2k+1}\;}
$$

참고로 $g(0)=0$ 이므로 $x=0$ 근방에서 잘 정의되며, 낮은 차수를 전개하면

$$
\sin(x^3+2x)=(x^3+2x)-\frac{(x^3+2x)^3}{6}+\cdots
=2x+x^3-\frac{4}{3}x^3+\cdots
$$

와 같이 실제 매클로린 계수와 일치한다.

👉 [실습(Python)에서 확인하기](./lab-02)
:::
