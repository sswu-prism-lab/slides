# 문제 3 · `setprecision` 출력 예측

::: info 문제 3 [1점]
아래 코드를 읽고, 출력을 예상하여 작성하세요.

```cpp
cout << setprecision(4) << 12.34567 << endl;
```
:::

::: details 풀이 및 해설
`fixed`나 `scientific` 조작자 없이 쓰인 기본 부동소수점 형식에서 `setprecision(n)`은 소수점 이하 자릿수가 아니라 **전체 유효숫자<span class="gloss">significant digits</span>의 개수**를 지정합니다.

`setprecision(4)`이므로 `12.34567`을 **유효숫자 4자리**로 반올림합니다.

$$12.34\underline{5}67 \;\rightarrow\; 12.35$$

다섯째 유효숫자 `5`에서 반올림되어 `12.35`가 됩니다.

$$\boxed{\texttt{12.35}}$$

👉 [실습(C++)에서 확인하기](./lab-03)
:::
