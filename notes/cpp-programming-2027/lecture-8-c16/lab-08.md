# 문제 8 · 실습 — 직각삼각형 별 출력

이중 반복문으로 `i`번째 줄에 별 `i`개를 찍습니다. `setw` 없이 별 개수만으로 모양을 만듭니다. 예시 입력은 `4` 입니다.

<CppRunner stdin="4">

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {       // 줄(행)
        for (int j = 1; j <= i; j++)     // 그 줄의 별 개수
            cout << '*';
        cout << '\n';
    }
    return 0;
}
```

</CppRunner>

입력 `4`에 대한 출력은 다음과 같습니다.

```
*
**
***
****
```

👉 [문제 8로 돌아가기](./problem-08)
