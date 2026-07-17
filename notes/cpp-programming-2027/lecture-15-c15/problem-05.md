# 문제 5 · 정적 지역 변수와 전역 변수

::: info 문제 5 [2점]
아래 코드를 읽고, 출력을 예상하여 작성하세요.

```cpp
#include <iostream>
using namespace std;

int y;

void func() {
    static int z = 4;
    z += 2;
    cout << y + z << endl;
}

int main() {
    func();
    y = 4;
    func();
}
```
:::

::: details 풀이 및 해설
두 가지 개념이 핵심입니다.

- **전역 변수**<span class="gloss">global variable</span> `int y;`는 명시적 초기화가 없어 `0`으로 초기화됩니다.
- **정적 지역 변수**<span class="gloss">static local variable</span> `static int z = 4;`는 **최초 한 번만** 초기화되고, 함수 호출이 끝나도 값이 유지됩니다.

**첫 번째 `func()` 호출** (`main`에서 `y`는 아직 `0`)
- `z`는 `4`로 초기화된 뒤 `z += 2` → `z = 6`
- `y + z = 0 + 6 = 6` 출력

그 뒤 `main`에서 `y = 4`로 변경.

**두 번째 `func()` 호출**
- `z`는 다시 초기화되지 **않고** 이전 값 `6`을 유지 → `z += 2` → `z = 8`
- `y + z = 4 + 8 = 12` 출력

$$\boxed{\begin{aligned}&6\\&12\end{aligned}}$$

👉 [실습(C++)에서 확인하기](./lab-05)
:::
