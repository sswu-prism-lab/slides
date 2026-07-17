# 문제 13 · 실습 — 상수 변수와 상수 포인터

상수 변수는 값 변경 불가, 상수 포인터(`int* const`)는 대상 변경 불가(값은 변경 가능), 상수를 가리키는 포인터(`const int*`)는 대상 변경 가능(값은 변경 불가)입니다. (주석 처리된 줄은 컴파일 오류가 나는 예입니다.)

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX = 100;     // 상수 변수: 값 변경 불가
    cout << "MAX = " << MAX << endl;
    // MAX = 200;            // 오류

    int x = 10, y = 20;

    int* const p = &x;       // 상수 포인터: 대상 고정
    *p = 15;                 // 대상의 값은 변경 가능
    cout << "x = " << x << " (상수 포인터로 값 변경)" << endl;
    // p = &y;               // 오류: 다른 주소로 변경 불가

    const int* q = &x;       // 상수를 가리키는 포인터
    q = &y;                  // 대상은 변경 가능
    cout << "*q = " << *q << " (다른 대상으로 이동)" << endl;
    // *q = 30;              // 오류: 대상의 값 변경 불가
    return 0;
}
```

</CppRunner>

출력은
```
MAX = 100
x = 15 (상수 포인터로 값 변경)
*q = 20 (다른 대상으로 이동)
```
입니다.

👉 [문제 13으로 돌아가기](./problem-13)
