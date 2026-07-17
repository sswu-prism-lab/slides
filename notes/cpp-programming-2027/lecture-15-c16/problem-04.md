# 문제 4 · 값 전달과 `addition`

::: info 문제 4 [2점]
아래 코드를 읽고, 출력을 예상하여 작성하세요.

```cpp
#include <iostream>
using namespace std;

void addition(double x) {
    x++;
}

int main() {
    double x = 1;
    addition(x);
    cout << x;
}
```
:::

::: details 풀이 및 해설
`addition` 함수의 매개변수 `x`는 **값 전달<span class="gloss">pass by value</span>**로 받습니다. 즉 호출 시 인자의 값이 **복사**되어 전달되므로, 함수 안의 `x`와 `main`의 `x`는 서로 다른 변수입니다.

- `main`에서 `x = 1`.
- `addition(x)` 호출 → 함수 내부의 지역 복사본이 `1 → 2`가 되지만, 함수가 끝나면 사라집니다.
- `main`의 `x`는 그대로 `1`.

따라서 출력은

$$\boxed{1}$$

👉 [실습(C++)에서 확인하기](./lab-04)
:::
