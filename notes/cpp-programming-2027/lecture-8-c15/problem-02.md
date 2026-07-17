# 문제 2 · 문자형의 정수 형변환 가능 여부

::: info 문제 2 [1점]
아래 문장이 옳으면 O, 틀리면 X로 답하세요.

문자<span class="gloss">character</span> 자료형은 정수형<span class="gloss">int</span>으로의 형변환이 불가능하다.
:::

::: details 풀이 및 해설
**답: X**

`char`는 사실 **정수 계열<span class="gloss">integral type</span>** 자료형입니다. 각 문자는 내부적으로 ASCII 코드값(정수)으로 저장되므로, `int`로의 형변환이 자유롭게 일어납니다. 오히려 산술 연산에서는 자동으로 `int`로 **승격**됩니다.

```cpp
char c = 'A';
int n = c;          // 암시적 변환: n == 65
cout << 'A' + 1;    // 66 (int 로 승격되어 출력)
```

따라서 "형변환이 불가능하다"는 문장은 틀렸습니다.

$$\boxed{\text{X}}$$
:::
