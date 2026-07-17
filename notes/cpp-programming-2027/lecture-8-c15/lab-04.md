# 문제 4 · 실습 — 전위/후위 증가와 부작용

전위/후위 증가의 부작용을 추적해 비교식이 거짓(`0`)이 됨을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    double a = 3.7, b = 2.3;
    double c = ++a + b++;
    cout << ((++a + b++) < c) << endl;
    return 0;
}
```

</CppRunner>

출력은 `0` 입니다. (`c = 7.0`, 비교식의 좌변 `= 9.0`, `9.0 < 7.0`은 거짓)

👉 [문제 4로 돌아가기](./problem-04)
