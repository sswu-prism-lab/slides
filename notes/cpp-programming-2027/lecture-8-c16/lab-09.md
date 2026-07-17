# 문제 9 · 실습 — `switch` 문과 후위 증가

`switch` 조건식에서 두 후위 증가가 계산되고, 어떤 `case`도 아닌 `default`가 실행되는 과정을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 1, y = -1, z;
    switch (x++ + y++) {
        case 2: z = x == 2 ? 1 : -1; break;
        case 1: z = (x * y) > 0 ? 1 : -1; break;
        default: z = y < -1 ? 1 : -1;
    }
    cout << "x = " << x << ", y = " << y << ", z = " << z << endl;
    return 0;
}
```

</CppRunner>

출력은 `x = 2, y = 0, z = -1` 입니다. 조건식 `1 + (-1) = 0`이라 `default`가 실행되고, `y(0) < -1`이 거짓이라 `z = -1`이 됩니다.

👉 [문제 9로 돌아가기](./problem-09)
