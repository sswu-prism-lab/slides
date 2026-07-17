# 문제 4 · 실습 — 삼항 연산자와 후위 증가

후위 증가 `a++`가 조건식과 삼항 가지에서 어떻게 평가되는지 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 3, b = 3;
    int c = a++ == b ? a++ : a--;
    cout << c << endl;
    cout << "참고) a = " << a << endl;   // 최종 a 값
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다.

```
4
참고) a = 5
```

조건 `a++ == b`가 `3 == 3`으로 참이 되어 참 가지 `a++`(값 `4`)가 `c`에 들어갑니다.

👉 [문제 4로 돌아가기](./problem-04)
