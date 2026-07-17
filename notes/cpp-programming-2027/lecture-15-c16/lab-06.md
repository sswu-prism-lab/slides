# 문제 6 · 실습 — 전역 변수의 초기값

전역 변수가 초기화 없이도 `0`이 됨을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int y;

int main() {
    cout << y;
}
```

</CppRunner>

출력은 `0` 입니다. 전역 변수는 자동으로 0으로 초기화됩니다.

👉 [문제 6으로 돌아가기](./problem-06)
