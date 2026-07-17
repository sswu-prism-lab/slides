# 문제 10 · 문자 포인터 결합 함수 오류

::: info 문제 10 [3점]
아래 문제를 읽고, 코드에 오류가 있다면 수정하세요. 오류가 없다면 '오류 없음'이라고 서술하세요.

> 아래는 두 문자 변수의 포인터 주소를 선언, 이들을 역참조하여 그 두 문자의 결합을 문자열<span class="gloss">string</span>로 반환하는 코드이다.

```cpp
#include <string>
using namespace std;

string combineChars(char* pC1, char* pC2) {
    string result;
    result += *pChar1;
    result += *pChar2;
    return result;
}

int main() {
    char a = 'H', b = 'i';
    char* pA = &a;
    char* pB = &b;

    string result = combineChars(pA, pB);
}
```
:::

::: details 풀이 및 해설
**오류 있음 — 매개변수 이름 불일치.**

`combineChars`의 매개변수는 `pC1`, `pC2`로 선언되어 있는데, 함수 본문에서는 존재하지 않는 `pChar1`, `pChar2`를 역참조하고 있습니다. 컴파일 시 "선언되지 않은 식별자" 오류가 납니다. 본문의 이름을 매개변수 이름으로 맞춰야 합니다.

```cpp
string combineChars(char* pC1, char* pC2) {
    string result;
    result += *pC1;   // pChar1 -> pC1
    result += *pC2;   // pChar2 -> pC2
    return result;
}
```

이렇게 고치면 `*pC1`은 `'H'`, `*pC2`는 `'i'`가 되어 `result`는 `"Hi"`가 됩니다. (나머지 부분 — 포인터 선언, 역참조로 문자 추가, 반환 등 — 은 올바릅니다.)

👉 [실습(C++)에서 확인하기](./lab-10)
:::
