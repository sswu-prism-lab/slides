# 문제 7 · 실습 — 최소공배수와 최대공약수

유클리드 호제법으로 최대공약수(GCD)를 구하고, 관계식으로 최소공배수(LCM)를 계산합니다. 예시 입력은 두 정수 `12 18` 입니다.

<CppRunner stdin="12 18">

```cpp
#include <iostream>
using namespace std;

int gcd(int a, int b) {      // 유클리드 호제법
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int main() {
    int a, b;
    cin >> a >> b;
    int g = gcd(a, b);
    int l = a / g * b;       // LCM = a*b/gcd (오버플로 피하려 먼저 나눔)
    cout << "최대공약수(GCD): " << g << endl;
    cout << "최소공배수(LCM): " << l << endl;
    return 0;
}
```

</CppRunner>

입력 `12 18`에 대한 출력은 다음과 같습니다.

```
최대공약수(GCD): 6
최소공배수(LCM): 36
```

👉 [문제 7로 돌아가기](./problem-07)
