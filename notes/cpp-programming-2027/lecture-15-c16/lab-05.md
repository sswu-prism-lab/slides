# 문제 5 · 실습 — 배열 이름의 역참조 `*myList`

`*myList`가 첫 번째 요소 `myList[0]`과 같음을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int myList[3] = {1, 2, 3};
    cout << *myList;
}
```

</CppRunner>

출력은 `1` 입니다. 배열 이름은 첫 요소의 주소이므로, 이를 역참조하면 `myList[0]`인 `1`이 됩니다.

👉 [문제 5로 돌아가기](./problem-05)
