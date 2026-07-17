# 문제 11 · 실습 — `while`·`break` 조기 종료

`num = 1`에서 곧바로 `break`가 실행되어 `sum`이 한 번도 더해지지 않는 것을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 0, sum = 0;
    while (num < 20) {
        num++;
        if (!((num % 4 == 0) || (num % 6 == 0)))
            break;                 // num=1에서 조건 참 → 즉시 종료
        sum += num;
    }
    cout << "num = " << num << ", sum = " << sum << endl;
    return 0;
}
```

</CppRunner>

출력은 `num = 1, sum = 0` 입니다.

👉 [문제 11로 돌아가기](./problem-11)
