# 문제 10 · `continue`와 무한 루프

::: info 문제 10 [2점]
아래 코드의 `num`, `sum`은 어떤 값을 갖는지 쓰시오.

```cpp
int num = 0, sum = 0;
while (num < 15) {
    if (!((num % 2 == 0) && (num % 3 == 0)))
        continue;
    sum += num;
    num++;
}
```
:::

::: details 풀이 및 해설
`num++`이 `continue`보다 **뒤에** 있는 것이 함정입니다.

**1) `num = 0`**
- 조건: `!((0%2==0) && (0%3==0))` = `!(true && true)` = `!true` = **false** → `continue` 안 함
- `sum += 0` → `sum = 0`, `num++` → `num = 1`

**2) `num = 1`**
- 조건: `!((1%2==0) && (1%3==0))` = `!(false && false)` = `!false` = **true** → `continue`
- `continue`가 실행되면 `num++`에 도달하지 못하고 `num`은 계속 `1`

이후 매 반복마다 `num`이 `1`에 갇혀 조건이 항상 참이 되어 `continue`만 반복됩니다. 즉 **무한 루프**에 빠지며 프로그램이 끝나지 않습니다.

$$\boxed{\text{무한 루프} \;\Rightarrow\; num = 1,\; sum = 0 \text{ 에서 멈추지 않음}}$$

올바르게 값을 누적하려면 `num++`을 `continue`보다 앞에 두거나 `for`문을 사용해야 합니다.

👉 [실습(C++)에서 확인하기](./lab-10)
:::
