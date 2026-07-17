# 문제 9 · 실습 — 요소의 주소와 값 반환

인덱스로 지정한 요소의 **주소**와 **값**을 함께 돌려줍니다. 실제 주소값은 실행마다 달라지므로, 여기서는 배열 시작 주소로부터의 **오프셋(바이트)**으로 결정적으로 보여 줍니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// 배열과 (크기보다 작은) 인덱스를 받아 그 요소의 주소와 값을 돌려주는 함수
void findElement(int* list, int index, int** outAddr, int* outValue) {
    *outAddr = &list[index];   // 요소의 주소
    *outValue = list[index];   // 요소의 값
}

int main() {
    int list[5] = {10, 20, 30, 40, 50};
    int index = 2;

    int* addr;
    int value;
    findElement(list, index, &addr, &value);

    cout << "인덱스 " << index << "의 값 : " << value << endl;
    cout << "배열 시작 주소로부터의 오프셋(바이트) : "
         << (char*)addr - (char*)list << endl;
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다. `int`가 4바이트이므로 인덱스 2의 오프셋은 `2 × 4 = 8`입니다.

```
인덱스 2의 값 : 30
배열 시작 주소로부터의 오프셋(바이트) : 8
```

👉 [문제 9로 돌아가기](./problem-09)
