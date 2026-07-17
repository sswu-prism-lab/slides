# 문제 4 · 실습 — 값 전달과 `addition`

원본 코드를 그대로 실행하여, 값 전달로는 호출자의 변수가 바뀌지 않음을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void addition(double x) {
    x++;
}

int main() {
    double x = 1;
    addition(x);
    cout << x;
}
```

</CppRunner>

출력은 `1` 입니다. 함수 안에서 복사본만 `2`가 되고, `main`의 `x`는 그대로입니다.

👉 [문제 4로 돌아가기](./problem-04)
