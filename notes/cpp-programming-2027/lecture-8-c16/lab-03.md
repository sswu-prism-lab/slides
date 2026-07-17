# 문제 3 · 실습 — 정수 나눗셈과 연산자 우선순위

`4 / 6`이 정수 나눗셈으로 `0`이 되는 과정을 눈으로 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << 2 + (4 / 6) * 4 - 2 << endl;
    return 0;
}
```

</CppRunner>

출력은 `0` 입니다. `4 / 6`이 `0`이라 `0 * 4 = 0`, `2 + 0 - 2 = 0`이 됩니다.

👉 [문제 3으로 돌아가기](./problem-03)
