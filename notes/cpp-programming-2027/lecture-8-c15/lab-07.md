# 문제 7 · 실습 — 최소공배수

0을 입력할 때까지 정수를 받아 가장 큰 두 수의 최소공배수를 구합니다. 입력은 `12 18 8 0`입니다.

<CppRunner stdin="12 18 8 0">

```cpp
#include <iostream>
using namespace std;

long long gcd(long long a, long long b) {
    while (b) { long long t = a % b; a = b; b = t; }
    return a;
}

int main() {
    long long largest = 0, second = 0, x;
    while (cin >> x) {
        if (x == 0) break;              // 0 이면 입력 종료
        if (x > largest) {              // 가장 큰 두 수 추적
            second = largest;
            largest = x;
        } else if (x > second) {
            second = x;
        }
    }
    long long lcm = largest / gcd(largest, second) * second;
    cout << "큰 두 수: " << largest << ", " << second << endl;
    cout << "최소공배수: " << lcm << endl;
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다.

```
큰 두 수: 18, 12
최소공배수: 36
```

👉 [문제 7로 돌아가기](./problem-07)
