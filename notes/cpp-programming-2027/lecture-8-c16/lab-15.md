# 문제 15 · 실습 — 정 n각형 넓이로 π 근사

단위원에 내접한 정 n각형에 몬테-카를로 시뮬레이션으로 점을 던져 넓이를 추정하고, 그 값을 π의 근삿값으로 봅니다. `srand(1)`로 결과를 **결정적**으로 재현합니다. 예시 입력은 변의 수 `180` 입니다.

<CppRunner stdin="180">

```cpp
#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;                        // 정 n각형의 변의 수
    const int N = 1000000;           // 몬테카를로 표본 수
    const double PI = acos(-1.0);
    double apothem = cos(PI / n);    // 단위원에 내접한 정 n각형의 변까지 거리
    srand(1);                        // 결정적 재현
    int inside = 0;
    for (int t = 0; t < N; t++) {
        double px = 2.0 * rand() / RAND_MAX - 1.0;   // [-1, 1]
        double py = 2.0 * rand() / RAND_MAX - 1.0;   // [-1, 1]
        bool in = true;
        for (int i = 0; i < n; i++) {
            double beta = (2 * i + 1) * PI / n;      // 각 변의 바깥 방향
            if (px * cos(beta) + py * sin(beta) > apothem) { in = false; break; }
        }
        if (in) inside++;
    }
    double area = 4.0 * inside / N;   // [-1,1]^2 넓이 = 4
    cout << "정 " << n << "각형 넓이(추정) = " << area << endl;
    cout << "근사한 pi = " << area << endl;
    return 0;
}
```

</CppRunner>

입력 `180`에 대한 출력은 다음과 같습니다.

```
정 180각형 넓이(추정) = 3.14226
근사한 pi = 3.14226
```

변의 수 `n`이 커질수록 정 n각형이 단위원에 가까워져 넓이가 $\pi = 3.14159\ldots$에 수렴합니다.

👉 [문제 15로 돌아가기](./problem-15)
