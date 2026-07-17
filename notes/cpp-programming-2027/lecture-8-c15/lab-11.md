# 문제 11 · 실습 — `break`가 있는 `while` 루프

`num = 20`에서 한 번 누적한 뒤 `num = 19`에서 `break`로 빠져나오는 과정을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 20, sum = 0;
    while (num > 0) {
        if (!((num % 4 == 0) || (num % 6 == 0)))
            break;
        sum += num;
        num--;
    }
    cout << "num=" << num << ", sum=" << sum << endl;
    return 0;
}
```

</CppRunner>

출력은 `num=19, sum=20` 입니다.

👉 [문제 11로 돌아가기](./problem-11)
