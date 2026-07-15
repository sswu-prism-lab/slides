# 문제 14 · 집합 조건의 충족 여부

::: info 문제 14 [4점]
임의의 집합 $A$, $B$, $C$가 다음 세 조건을 동시에 만족할 수 있는지 확인하시오.

1. $A\cup B = A\cup C$
2. $A\cap B = A\cap C$
3. $B\neq C$
:::

::: details 풀이 및 해설
결론부터 말하면 **동시에 만족할 수 없습니다**. 조건 1, 2가 성립하면 반드시 $B=C$가 되어 조건 3과 모순되기 때문입니다.

**증명**: 흡수법칙 $B=B\cap(A\cup B)$에서 출발합니다.

$$
\begin{aligned}
B &= B\cap(A\cup B) \\
&= B\cap(A\cup C) &&(\because A\cup B=A\cup C)\\
&= (B\cap A)\cup(B\cap C) &&(\text{분배법칙})\\
&= (A\cap C)\cup(B\cap C) &&(\because A\cap B=A\cap C)\\
&= (A\cup B)\cap C &&(\text{분배법칙})\\
&= (A\cup C)\cap C &&(\because A\cup B=A\cup C)\\
&= C. &&(\text{흡수법칙})
\end{aligned}
$$

따라서 조건 1, 2가 성립하면 $B=C$이며, 이는 조건 3 $B\neq C$와 모순입니다.

$$
\boxed{\;\text{세 조건을 동시에 만족하는 } A,B,C\text{는 존재하지 않는다.}\;}
$$

👉 [실습(Python)에서 확인하기](./lab-14)
:::
