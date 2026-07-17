# 문제 9 · 실습 — `switch`와 삼항 연산자

`--x + ++y`가 `1`이 되어 `case 1`이 실행되고, `z`가 `1`이 되는 과정을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 2, y = -1, z;
    switch (--x + ++y) {
        case 0: z = x == 1 ? 1 : -1; break;
        case 1: z = (x * y) <= 0 ? 1 : -1; break;
        default: z = y > -1 ? 1 : -1;
    }
    cout << "x=" << x << ", y=" << y << ", z=" << z << endl;
    return 0;
}
```

</CppRunner>

출력은 `x=1, y=0, z=1` 입니다.

👉 [문제 9로 돌아가기](./problem-09)
