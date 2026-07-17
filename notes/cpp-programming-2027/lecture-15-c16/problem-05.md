# 문제 5 · 배열 이름의 역참조 `*myList`

::: info 문제 5 [2점]
아래 코드를 읽고, 출력을 예상하여 작성하세요.

```cpp
#include <iostream>
using namespace std;

int main() {
    int myList[3] = {1, 2, 3}; // 주소: 00FF13
    cout << *myList;
}
```
:::

::: details 풀이 및 해설
배열 이름 `myList`는 대부분의 식에서 **첫 번째 요소의 주소**(`&myList[0]`)로 변환됩니다. 즉 `myList`는 `00FF13`을 가리킵니다.

이를 역참조<span class="gloss">dereference</span>한 `*myList`는 그 주소에 저장된 값, 곧 `myList[0]`과 같습니다.

$$*myList \;=\; myList[0] \;=\; 1$$

따라서 출력은

$$\boxed{1}$$

👉 [실습(C++)에서 확인하기](./lab-05)
:::
