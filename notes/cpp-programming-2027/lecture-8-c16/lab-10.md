# 문제 10 · 실습 — `while`·`continue`와 6의 배수 합

`continue`로 6의 배수가 아닌 값을 건너뛰고, 6의 배수(`6, 12, 18`)만 더하는 과정을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 0, sum = 0;
    while (num < 20) {
        num++;
        if (!((num % 2 == 0) && (num % 3 == 0)))
            continue;              // 6의 배수가 아니면 건너뜀
        sum += num;
    }
    cout << "num = " << num << ", sum = " << sum << endl;
    return 0;
}
```

</CppRunner>

출력은 `num = 20, sum = 36` 입니다. (`6 + 12 + 18 = 36`)

👉 [문제 10으로 돌아가기](./problem-10)
