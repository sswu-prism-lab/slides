# 문제 6 · 실습 — 배열 이름과 `&배열`

실제 번지는 실행 환경마다 다르지만, `&myList`·`myList`·`&myList[0]`이 **같은 시작 주소**를 가리킨다는 사실은 항상 성립합니다. 이를 확인해 봅시다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int myList[3] = {1, 2, 3};   // 문제에서는 시작 주소가 00FF13
    cout << boolalpha;
    // 세 표현식은 자료형은 달라도 가리키는 주소값이 같다
    cout << ( (void*)&myList == (void*)myList )     << endl;
    cout << ( (void*)myList  == (void*)&myList[0] )  << endl;
    return 0;
}
```

</CppRunner>

출력은
```
true
true
```
입니다. 따라서 `cout << &myList`는 배열이 시작하는 주소를 출력하며, 문제의 가정에서는 `00FF13`이 됩니다.

👉 [문제 6으로 돌아가기](./problem-06)
