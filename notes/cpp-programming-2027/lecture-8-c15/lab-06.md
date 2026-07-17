# 문제 6 · 실습 — 조건 연산자와 문자열 연결

`'1' == '2'`가 거짓이 되어 `myStr2`에 `"Bye"`가 담기는 과정을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string myStr1 = "Sungshin";
    string myStr2;
    myStr2 = '1' == '2' ? "Hi" : "Bye";
    cout << myStr1 + myStr2 << endl;
    return 0;
}
```

</CppRunner>

출력은 `SungshinBye` 입니다.

👉 [문제 6으로 돌아가기](./problem-06)
