# 문제 6 · 조건 연산자와 문자열 연결

::: info 문제 6 [2점]
아래 코드를 읽고, 출력을 예상하여 작성하세요.

```cpp
string myStr1 = "Sungshin";
string myStr2;
myStr2 = '1' == '2' ? "Hi" : "Bye";
cout << myStr1 + myStr2 << endl;
```
:::

::: details 풀이 및 해설
조건 연산자 `?:`는 산술/비교 연산자보다 **우선순위가 낮으므로** `'1' == '2'`가 먼저 평가됩니다.

- `'1' == '2'`: 두 문자의 ASCII값 `49`와 `50`은 다르므로 `false`.
- 따라서 `myStr2 = "Bye"`.
- `myStr1 + myStr2` = `"Sungshin" + "Bye"` = `"SungshinBye"`.

$$\boxed{\texttt{SungshinBye}}$$

👉 [실습(C++)에서 확인하기](./lab-06)
:::
