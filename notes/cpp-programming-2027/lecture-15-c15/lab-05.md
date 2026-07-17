# 문제 5 · 실습 — 정적 지역 변수와 전역 변수

`static int z`는 최초 한 번만 초기화되고 값이 유지됩니다. 전역 `y`는 `0`으로 시작합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int y;                    // 전역 변수 → 0 으로 초기화

void func() {
    static int z = 4;     // 최초 1회만 초기화, 값 유지
    z += 2;
    cout << y + z << endl;
}

int main() {
    func();               // y=0, z: 4→6 → 6
    y = 4;
    func();               // y=4, z: 6→8 → 12
    return 0;
}
```

</CppRunner>

출력은
```
6
12
```
입니다.

👉 [문제 5로 돌아가기](./problem-05)
