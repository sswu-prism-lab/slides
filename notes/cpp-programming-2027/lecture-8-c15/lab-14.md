# 문제 14 · 실습 — 라이프니츠 공식으로 π 근사

빈칸을 채운 완성 코드입니다. `n = 100000` 항까지 더해 π를 근사합니다.

<CppRunner stdin="100000">

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    double sum = 0.0;

    for (int i = 1; i <= n; i++) {
        // 빈칸 1: 각 항을 부호와 함께 합산
        sum += ((i % 2 == 1) ? 1.0 : -1.0) / (2 * i - 1);
    }
    // 빈칸 2: 급수 합에 4를 곱해 π 계산
    double pi = 4 * sum;

    cout << fixed << setprecision(6) << pi << endl;
    return 0;
}
```

</CppRunner>

출력은 `3.141583` 입니다. 라이프니츠 급수는 수렴이 느려 항 수를 크게 늘려도 정확도가 서서히 좋아집니다.

👉 [문제 14로 돌아가기](./problem-14)
