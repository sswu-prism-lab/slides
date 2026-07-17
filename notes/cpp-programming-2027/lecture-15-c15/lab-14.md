# 문제 14 · 실습 — 얕은 복사와 깊은 복사

깊은 복사 생성자를 정의하면 복사본이 별도 메모리를 가지므로, 한쪽을 바꿔도 다른 쪽에 영향이 없습니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class DeepArray {
public:
    int* data;
    int size;
    DeepArray(int s) : size(s) {
        data = new int[size];
        for (int i = 0; i < size; i++) data[i] = i + 1;   // 1,2,3
    }
    // 깊은 복사: 새 메모리를 할당해 값을 복사
    DeepArray(const DeepArray& other) : size(other.size) {
        data = new int[size];
        for (int i = 0; i < size; i++) data[i] = other.data[i];
    }
    ~DeepArray() { delete[] data; }
};

int main() {
    DeepArray a(3);
    DeepArray b = a;      // 깊은 복사 생성자 호출
    b.data[0] = 99;       // b 만 바뀌어야 함
    cout << "a.data[0] = " << a.data[0] << endl;  // 1 (영향 없음)
    cout << "b.data[0] = " << b.data[0] << endl;  // 99
    return 0;
}
```

</CppRunner>

출력은
```
a.data[0] = 1
b.data[0] = 99
```
입니다. 얕은 복사였다면 `a`와 `b`가 같은 배열을 공유해 `a.data[0]`도 `99`가 되었을 것입니다.

👉 [문제 14로 돌아가기](./problem-14)
