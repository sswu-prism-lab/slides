# 문제 6 · 실습 — 문자열과 삼항 연산

`'a' < 'z'`가 아스키 코드값 비교로 참이 되어 `'b'`가 문자열에 붙는 과정을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string myString = "Sungshin";
    char n = 'a' < 'z' ? 'b' : 'c';
    myString += n;
    cout << myString << endl;
    return 0;
}
```

</CppRunner>

출력은 `Sungshinb` 입니다.

👉 [문제 6으로 돌아가기](./problem-06)
