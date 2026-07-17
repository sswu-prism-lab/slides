# 문제 4 · 참조 전달과 출력 예측

::: info 문제 4 [2점]
아래 코드를 읽고, 출력을 예상하여 작성하세요.

```cpp
#include <iostream>
using namespace std;

void multiplication(double& x) {
    x *= 4;
}

int main() {
    double num = 2.0;
    multiplication(num);
    cout << num;
}
```
:::

::: details 풀이 및 해설
매개변수 `double& x`는 **참조 전달**<span class="gloss">pass by reference</span>입니다. `x`는 `main`의 `num`을 복사한 것이 아니라 `num` 자체의 별칭이므로, 함수 안에서 `x`를 바꾸면 `num`도 함께 바뀝니다.

1. `num = 2.0`
2. `multiplication(num)` 호출 → `x`는 `num`의 별칭
3. `x *= 4` → `num`이 `2.0 * 4 = 8.0`이 됨
4. `cout << num` → `8` 출력 (소수부가 0이므로 `8`)

$$\boxed{8}$$

👉 [실습(C++)에서 확인하기](./lab-04)
:::
