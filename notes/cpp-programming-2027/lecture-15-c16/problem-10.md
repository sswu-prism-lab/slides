# 문제 10 · `addByPointer` 오류 수정

::: info 문제 10 [3점]
아래 문제를 읽고, 각 물음에 답하세요.

아래는 두 정수 변수의 포인터 주소를 선언, 이들을 역참조하여 그 두 수의 합을 반환하는 함수를 코딩한 것이다. 아래 코드에 오류가 있다면 수정하시오.

```cpp
#include <iostream>
using namespace std;

int addByPointer(int& pX, pY) {
    return *pX + *pY;
}

int main() {
    int x = 1, y = 2;
    int* pX = &x, pY = &y;

    result = addByPointer(pX, pY);
}
```
:::

::: details 풀이 및 해설
함수 본문에서 `*pX + *pY`처럼 **역참조**를 하므로 두 매개변수는 **포인터**여야 합니다. 다음 네 곳이 잘못되었습니다.

1. **매개변수 `int& pX`** — 참조가 아니라 포인터여야 함 → `int* pX`.
2. **매개변수 `pY`** — 타입이 빠져 있음 → `int* pY`.
3. **`int* pX = &x, pY = &y;`** — 이 선언에서 `pY`는 `int*`가 아니라 `int`가 됨(별표는 `pX`에만 적용). → `int* pX = &x, *pY = &y;`.
4. **`result = ...`** — `result`가 선언되지 않음 → `int result = ...`.

**수정된 코드**

```cpp
#include <iostream>
using namespace std;

int addByPointer(int* pX, int* pY) {   // ① ② 포인터 매개변수
    return *pX + *pY;
}

int main() {
    int x = 1, y = 2;
    int* pX = &x, *pY = &y;            // ③ pY 도 포인터로

    int result = addByPointer(pX, pY); // ④ 타입 명시
    cout << result << endl;            // (확인용 출력)
}
```

수정 후 `*pX + *pY = 1 + 2 = 3`.

$$\boxed{result = 3}$$

👉 [실습(C++)에서 확인하기](./lab-10)
:::
