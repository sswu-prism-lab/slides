# 문제 4 · 실습 — 참조 전달과 출력 예측

`double& x`는 `num`의 별칭이므로, 함수 안의 변경이 `main`의 `num`에 그대로 반영됩니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void multiplication(double& x) {
    x *= 4;              // x 는 num 의 별칭 → num 이 바뀐다
}

int main() {
    double num = 2.0;
    multiplication(num);
    cout << num;
    return 0;
}
```

</CppRunner>

출력은 `8` 입니다. (`2.0 * 4 = 8.0`, 소수부가 0이라 `8`로 출력)

👉 [문제 4로 돌아가기](./problem-04)
