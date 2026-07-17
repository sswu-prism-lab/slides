# 문제 1 · 반환값 없는 함수 (O/X)

::: info 문제 1 [1점]
아래 문장을 읽고 O/X로 답하세요.

> C++에서 데이터를 반환하지 않는 함수<span class="gloss">function</span>도 존재한다.
:::

::: details 풀이 및 해설
**정답: O**

C++에는 반환값이 없는 함수를 위한 `void` 반환형이 있습니다. 반환형이 `void`인 함수는 값을 돌려주지 않고, 함수 안에서 `return;`(값 없는 return)으로 끝내거나 그냥 함수 본문이 끝나면 반환됩니다.

```cpp
void greet() {           // 반환값 없음
    cout << "Hello";
    return;              // 값을 반환하지 않는 return (생략 가능)
}
```

따라서 "데이터를 반환하지 않는 함수도 존재한다"는 참입니다.

$$\boxed{\text{O}}$$
:::
