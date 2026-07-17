# 문제 15 · 실습 — 10진수 → 8진수 변환 오류 수정

세 가지 오류(문자 변환 `+ '0'`, `while` 반복, 자릿수 뒤집기)를 고친 수정본입니다. 입력은 `100`입니다.

<CppRunner stdin="100">

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    cout << "10진수 입력: ";
    int dec;
    cin >> dec;

    string oct;
    if (dec == 0) oct = "0";
    while (dec > 0) {
        oct += static_cast<char>(dec % 8 + '0');  // 오류1: + '0'
        dec /= 8;                                 // 오류2: while 반복
    }
    reverse(oct.begin(), oct.end());              // 오류3: 자릿수 뒤집기
    cout << "변환된 8진수: " << oct << endl;
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다. ($100 = 1\times 64 + 4\times 8 + 4$)

```
10진수 입력: 변환된 8진수: 144
```

👉 [문제 15로 돌아가기](./problem-15)
