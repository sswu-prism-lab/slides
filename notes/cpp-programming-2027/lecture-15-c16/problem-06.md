# 문제 6 · 전역 변수의 초기값

::: info 문제 6 [2점]
아래 코드를 읽고, 출력을 예상하여 작성하세요.

```cpp
#include <iostream>
using namespace std;

int y;

int main() {
    cout << y;
}
```
:::

::: details 풀이 및 해설
`y`는 함수 밖에 선언된 **전역 변수<span class="gloss">global variable</span>**입니다. 전역 변수(및 정적 저장 기간을 갖는 변수)는 명시적 초기화가 없어도 **0으로 자동 초기화<span class="gloss">zero-initialization</span>**됩니다.

> 참고: 함수 안의 지역 변수는 초기화하지 않으면 쓰레기 값을 갖지만, 전역 변수는 규칙적으로 `0`이 됩니다.

따라서 출력은

$$\boxed{0}$$

👉 [실습(C++)에서 확인하기](./lab-06)
:::
