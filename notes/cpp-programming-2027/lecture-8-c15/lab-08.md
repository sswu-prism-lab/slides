# 문제 8 · 실습 — 직각삼각형 출력

입력 `4`에 대해 별의 개수가 `4, 3, 2, 1`로 줄어드는 직각삼각형을 `setw` 없이 출력합니다.

<CppRunner stdin="4">

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int row = n; row >= 1; row--) {   // 별 개수: n → 1
        for (int col = 0; col < row; col++)
            cout << '*';
        cout << '\n';
    }
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다.

```
****
***
**
*
```

👉 [문제 8로 돌아가기](./problem-08)
