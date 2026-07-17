# 문제 7 · 실습 — 포인터 산술

`pNum + num`은 단순 정수 덧셈이 아니라 `num × sizeof(int)` 바이트만큼 이동합니다. 가정한 시작 주소 `00FF00`으로 계산 결과를 재현해 봅니다.

<CppRunner>

```cpp
#include <iostream>
#include <cstdint>
#include <iomanip>
using namespace std;

int main() {
    int num = 1;                     // int 는 4바이트
    uintptr_t pNum = 0x00FF00;       // 가정된 주소

    // 포인터에 정수를 더하면 (정수 × 자료형 크기) 바이트만큼 이동
    uintptr_t result = pNum + num * sizeof(int);

    cout << "이동 바이트 수: " << num * sizeof(int) << endl;
    cout << hex << uppercase << setw(6) << setfill('0') << result << endl;
    return 0;
}
```

</CppRunner>

출력은
```
이동 바이트 수: 4
00FF04
```
입니다. `00FF00`에 `1 × 4 = 4`바이트를 더해 `00FF04`가 됩니다.

👉 [문제 7로 돌아가기](./problem-07)
