# 문제 12 · 실습 — 함수 오버로딩

같은 이름 `add`가 인자의 타입·개수에 따라 다른 함수로 호출되는 것을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// 같은 이름 add — 매개변수(개수/타입)가 달라 서로 다른 함수로 공존
int add(int a, int b)          { return a + b; }
double add(double a, double b) { return a + b; }
int add(int a, int b, int c)   { return a + b + c; }

int main() {
    cout << add(1, 2) << endl;       // int 2개 버전
    cout << add(1.5, 2.5) << endl;   // double 2개 버전
    cout << add(1, 2, 3) << endl;    // int 3개 버전
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다.

```
3
4
6
```

호출할 때 넘긴 인자의 타입·개수에 맞는 `add`가 각각 선택됩니다.

👉 [문제 12로 돌아가기](./problem-12)
