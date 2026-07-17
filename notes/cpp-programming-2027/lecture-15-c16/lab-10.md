# 문제 10 · 실습 — `addByPointer` 오류 수정

수정본을 실행하여 두 포인터가 가리키는 값의 합이 제대로 반환되는지 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int addByPointer(int* pX, int* pY) {   // 포인터 매개변수
    return *pX + *pY;
}

int main() {
    int x = 1, y = 2;
    int* pX = &x, *pY = &y;            // pY 도 포인터

    int result = addByPointer(pX, pY); // 타입 명시
    cout << result << endl;
    return 0;
}
```

</CppRunner>

출력은 `3` 입니다. `*pX + *pY = 1 + 2 = 3`.

👉 [문제 10으로 돌아가기](./problem-10)
