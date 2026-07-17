# 문제 10 · 실습 — `continue`와 무한 루프

원본 코드는 `num`이 `1`에 갇혀 무한 루프에 빠집니다. 여기서는 반복 횟수 안전장치(원본에는 없음)를 넣어 그 상태를 관찰합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int num = 0, sum = 0;
    long guard = 0;
    while (num < 15) {
        if (++guard > 5) {   // 안전장치: 실제 코드에는 없음(무한 루프 증명용)
            cout << "...continue 로 인해 num 이 1 에서 갇혀 무한 반복." << '\n';
            break;
        }
        cout << "[반복 " << guard << "] num=" << num << ", sum=" << sum << '\n';
        if (!((num % 2 == 0) && (num % 3 == 0)))
            continue;        // num=1 부터 여기서 계속 되돌아감
        sum += num;
        num++;
    }
    cout << "최종(무한 루프 상태): num=" << num << ", sum=" << sum << endl;
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다. `num`이 `1`이 된 뒤로는 `continue`만 반복되어 값이 변하지 않습니다.

```
[반복 1] num=0, sum=0
[반복 2] num=1, sum=0
[반복 3] num=1, sum=0
[반복 4] num=1, sum=0
[반복 5] num=1, sum=0
...continue 로 인해 num 이 1 에서 갇혀 무한 반복.
최종(무한 루프 상태): num=1, sum=0
```

👉 [문제 10으로 돌아가기](./problem-10)
