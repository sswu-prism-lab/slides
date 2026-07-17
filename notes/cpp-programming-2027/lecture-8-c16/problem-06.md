# 문제 6 · 문자열과 삼항 연산

::: info 문제 6 [2점]
아래 코드를 읽고, 출력을 예상하여 작성하세요.

```cpp
string myString = "Sungshin";
char n = 'a' < 'z' ? 'b' : 'c';
myString += n;
cout << myString << endl;
```
:::

::: details 풀이 및 해설
문자 비교는 **아스키 코드값**으로 이뤄집니다. `'a'`는 `97`, `'z'`는 `122`이므로 `'a' < 'z'`는 **참**입니다.

1. 삼항 연산자가 참 가지를 택해 `n = 'b'`
2. `myString += n`은 문자열 뒤에 문자 `'b'`를 이어 붙임 → `"Sungshin"` + `'b'` = `"Sungshinb"`

따라서 출력은 `Sungshinb` 입니다.

$$\boxed{\texttt{Sungshinb}}$$

👉 [실습(C++)에서 확인하기](./lab-06)
:::
