# 문제 7 · 포인터 산술

::: info 문제 7 [2점]
아래 코드를 읽고, 출력을 예상하여 작성하세요.

```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 1; // int는 4바이트
    int* pNum = &num; // 주소 00FF00
    cout << pNum + num;
}
```
:::

::: details 풀이 및 해설
**포인터 산술**<span class="gloss">pointer arithmetic</span>에서 포인터에 정수를 더하면, 실제로는 *가리키는 자료형의 크기만큼* 배수로 번지가 이동합니다.

$$\texttt{pNum} + n \;=\; \texttt{pNum} + n \times \texttt{sizeof(int)} \text{ 바이트}$$

값을 대입하면
- `pNum = 00FF00`, `num = 1`, `sizeof(int) = 4`
- 이동 바이트 = `num × 4 = 1 × 4 = 4`
- 결과 번지 = `00FF00 + 4 = 00FF04`

`pNum + num`은 여전히 포인터이므로, `cout`은 이 주소값 `00FF04`를 출력합니다. (단순히 `00FF00 + 1 = 00FF01`이 아니라는 점이 핵심입니다.)

$$\boxed{\texttt{00FF04}}$$

👉 [실습(C++)에서 확인하기](./lab-07)
:::
