# 문제 3 · 실습 — `setprecision` 출력 예측

기본 부동소수점 형식에서 `setprecision`이 유효숫자 개수를 지정한다는 것을 직접 확인합니다.

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << setprecision(4) << 12.34567 << endl;
    return 0;
}
```

</CppRunner>

출력은 `12.35` 입니다.

👉 [문제 3으로 돌아가기](./problem-03)
