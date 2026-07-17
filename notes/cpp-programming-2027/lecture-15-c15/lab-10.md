# 문제 10 · 실습 — 문자 포인터 결합 함수 오류

본문의 `pChar1`/`pChar2`를 매개변수 이름 `pC1`/`pC2`로 맞춘 수정본입니다.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

string combineChars(char* pC1, char* pC2) {
    string result;
    result += *pC1;   // pChar1 -> pC1
    result += *pC2;   // pChar2 -> pC2
    return result;
}

int main() {
    char a = 'H', b = 'i';
    char* pA = &a;
    char* pB = &b;
    string result = combineChars(pA, pB);
    cout << result << endl;
    return 0;
}
```

</CppRunner>

출력은 `Hi` 입니다.

👉 [문제 10으로 돌아가기](./problem-10)
