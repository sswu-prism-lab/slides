# 문제 13 · 실습 — 지역·정적 지역·전역 변수

같은 함수를 세 번 호출하며 세 종류 변수의 값이 어떻게 달라지는지 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int g = 100;   // 전역 변수: 프로그램 전체에서 접근

void counter() {
    int local = 0;               // 지역: 호출마다 새로 생성·초기화
    static int staticLocal = 0;  // 정적 지역: 최초 1회 초기화, 값 유지
    local++;
    staticLocal++;
    cout << "local=" << local
         << ", staticLocal=" << staticLocal
         << ", global=" << g << endl;
}

int main() {
    counter();
    counter();
    counter();
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다. `local`은 매번 `1`로 되돌아가지만, `staticLocal`은 `1 → 2 → 3`으로 누적되고 `global`은 계속 `100`입니다.

```
local=1, staticLocal=1, global=100
local=1, staticLocal=2, global=100
local=1, staticLocal=3, global=100
```

👉 [문제 13으로 돌아가기](./problem-13)
