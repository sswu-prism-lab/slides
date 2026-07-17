# 문제 5 · 실습 — `bool` 변환과 문자 산술

`'a'`가 `true`로 변환되고, 문자 산술과 후위 증가가 어떻게 평가되는지 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    bool a = 'a'; // 'a'의 ASCII값: 97
    int b = a ? 1 : 2;
    cout << 'a' + b++ << "\n"
        << static_cast<char>('a' + b++) << endl;
    return 0;
}
```

</CppRunner>

출력은 두 줄로 `98` 과 `c` 입니다.

👉 [문제 5로 돌아가기](./problem-05)
