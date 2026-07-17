# 문제 13 · `for` 반복 범위 오류 수정

::: info 문제 13 [3점]
수정이는 아래 코드에서 사용자로부터 임의의 수 10개를 입력으로 받은 후, 양수의 합 `pSum`과 음수의 합 `nSum`을 출력하고자 한다. 아래 코드에 오류가 있는지 확인하고 수정하시오. (오류가 없으면 '오류 없음'이라고 쓰시오.)

```cpp
int number, pSum = 0, nSum = 0;
cout << "10개의 숫자를 입력하세요: " << endl;
for (int i = 0; i <= 10; ++i) {
    cin >> number;
    if (number > 0)
        pSum += number;
    else
        nSum += number;
}
cout << "양수의 합: " << pSum << endl;
cout << "음수의 합: " << nSum << endl;
```
:::

::: details 풀이 및 해설
**오류가 있습니다.** 반복 범위가 잘못되었습니다.

`for (int i = 0; i <= 10; ++i)`는 `i`가 `0, 1, 2, …, 10`으로 **총 11번** 반복합니다. 그 결과 숫자를 10개가 아니라 **11개** 읽어, 입력을 하나 더 요구하게 됩니다. "10개를 입력받는다"는 요구와 어긋나는 **경계 오류**<span class="gloss">off-by-one error</span>입니다.

조건을 `i < 10`으로 바꾸면 `i`가 `0..9`로 정확히 10번 반복합니다.

**수정본**

```cpp
int number, pSum = 0, nSum = 0;
cout << "10개의 숫자를 입력하세요: " << endl;
for (int i = 0; i < 10; ++i) {      // i <= 10 → i < 10 : 정확히 10번 반복
    cin >> number;
    if (number > 0)
        pSum += number;
    else
        nSum += number;
}
cout << "양수의 합: " << pSum << endl;
cout << "음수의 합: " << nSum << endl;
```

$$\boxed{\texttt{for (int i = 0; i <= 10; ++i)} \;\rightarrow\; \texttt{for (int i = 0; i < 10; ++i)}}$$

> 참고: 입력값이 `0`이면 양수도 음수도 아니지만 위 코드는 `else`에서 `nSum`에 더합니다. 문제의 핵심 오류는 반복 횟수이므로 그 부분을 바로잡는 것이 정답이며, 엄밀히 하려면 `else if (number < 0)`로 `0`을 제외할 수 있습니다.

👉 [실습(C++)에서 확인하기](./lab-13)
:::
