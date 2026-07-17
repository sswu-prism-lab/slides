# 문제 7 · 실습 — 해시 함수 결정성 위반

문제의 해시 함수 `h(x) = x × random(0,10) % m` 처럼 난수를 섞으면, **같은 키인데 매번 다른 슬롯**이 나옵니다. 결정성<span class="gloss">deterministic</span>이 깨져 해시 함수로 쓸 수 없음을 눈으로 확인합니다.

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

// 문제의 나쁜 해시: 난수를 곱해 슬롯을 정함 (결정성 위반)
int badHash(int x, int m) {
    double r = (rand() % 1001) / 100.0;   // 0.00 ~ 10.00 사이 "임의 실수"
    return (int)(x * r) % m;
}

int main() {
    srand(1);
    int m = 13, key = 42;
    cout << "같은 키 " << key << " 를 세 번 해싱한 슬롯:\n";
    for (int t = 1; t <= 3; ++t)
        cout << "  " << t << "회차 -> slot " << badHash(key, m) << '\n';
    cout << "같은 키인데 슬롯이 매번 달라 저장한 값을 다시 찾을 수 없음\n";
    return 0;
}
```

</CppRunner>

출력(예):

```
같은 키 42 를 세 번 해싱한 슬롯:
  1회차 -> slot 12
  2회차 -> slot 11
  3회차 -> slot 9
같은 키인데 슬롯이 매번 달라 저장한 값을 다시 찾을 수 없음
```

같은 키 `42`가 매 호출마다 다른 슬롯으로 갑니다. 저장할 때의 슬롯과 조회할 때의 슬롯이 달라 값을 찾을 수 없으므로, 이 함수는 해시 함수로 부적절합니다. (좋은 해시는 결정적·균등·빠름이어야 합니다.)

👉 [문제 7로 돌아가기](./problem-07)
