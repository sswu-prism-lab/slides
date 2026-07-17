# 문제 8 · 실습 — 배열을 뒤집은 새 배열 반환

원 배열은 그대로 두고, 순서를 거꾸로 한 새 배열을 만들어 반환합니다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

// 원 배열(const 참조)은 읽기만 하고, 새 배열을 만들어 반환
vector<int> reversed(const vector<int>& list) {
    vector<int> result(list.size());
    for (size_t i = 0; i < list.size(); i++)
        result[i] = list[list.size() - 1 - i];
    return result;
}

int main() {
    vector<int> a = {1, 2, 3, 4, 5};
    vector<int> b = reversed(a);

    cout << "원 배열   : ";
    for (int x : a) cout << x << " ";
    cout << "\n뒤집은 배열: ";
    for (int x : b) cout << x << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다. 원 배열이 그대로 보존됨을 확인할 수 있습니다.

```
원 배열   : 1 2 3 4 5
뒤집은 배열: 5 4 3 2 1
```

👉 [문제 8로 돌아가기](./problem-08)
