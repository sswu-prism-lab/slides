# 문제 5 · 실습 — `static_cast`와 문자 산술

`3 / 6`이 `0`이 되는 것과, 전위·후위 증가가 문자 산술에서 어떻게 다른지 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    double x = static_cast<double>(3 / 6);
    double y = x *= 2;
    cout << static_cast<char>('a' + ++y) << '\"'
        << static_cast<char>('a' + x++) << '\"';
    cout << endl;
    return 0;
}
```

</CppRunner>

출력은 `b"a"` 입니다. `x`와 `y`는 처음에 모두 `0.0`이고, `++y`로 `'a'+1='b'`, `x++`로 `'a'+0='a'`가 됩니다.

👉 [문제 5로 돌아가기](./problem-05)
