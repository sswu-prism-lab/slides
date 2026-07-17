# 문제 14 · 실습 — 바젤 급수로 π 근사

빈칸을 채운 완성본입니다. 제곱수 역수의 합에 6을 곱하고 제곱근을 취해 π를 근사합니다. 예시 입력은 항의 개수 `100000` 입니다.

<CppRunner stdin="100000">

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    cout << "정수 n을 입력하세요: ";
    int n;
    cin >> n;
    double sum = 0.0;

    // 오일러(바젤) 급수: 1 + 1/2^2 + 1/3^2 + ... + 1/n^2
    for (int i = 1; i <= n; i++) {
        sum += 1.0 / (static_cast<double>(i) * i);   // 빈칸 1: 각 항 1/i^2
    }
    double pi = sqrt(6.0 * sum);                     // 빈칸 2: π = sqrt(6 * 합)
    cout << "\n근사한 pi = " << pi << endl;
    return 0;
}
```

</CppRunner>

입력 `100000`에 대한 출력은 다음과 같습니다.

```
정수 n을 입력하세요: 
근사한 pi = 3.14158
```

`n`을 키울수록 실제 $\pi = 3.14159\ldots$에 더 가까워집니다.

👉 [문제 14로 돌아가기](./problem-14)
