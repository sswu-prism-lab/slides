# 문제 12 · 실습 — 더블 해싱

`(h1(k) + i·h2(k)) % m` 탐사식으로 키를 삽입하는 더블 해싱<span class="gloss">double hashing</span>을 구현합니다. 충돌이 나면 2차 해시 `h2`가 정한 간격만큼 건너뛰며 빈 슬롯을 찾습니다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int M = 13;                 // 테이블 크기(소수)
int h1(int k) { return k % M; }   // 1차 해시
int h2(int k) { return 1 + (k % (M - 1)); } // 2차 해시: 0이 아니고 M과 서로소

int main() {
    vector<int> table(M, -1);     // -1 = 빈 슬롯
    vector<int> keys = {18, 41, 22, 59, 32, 31, 73};

    for (int k : keys) {
        int i = 0, slot;
        // (h1 + i*h2) % M 로 빈 슬롯을 찾을 때까지 탐사
        do {
            slot = (h1(k) + i * h2(k)) % M;
            ++i;
        } while (table[slot] != -1);
        table[slot] = k;
        cout << "키 " << k << " -> slot " << slot
             << " (탐사 " << i << "회, h1=" << h1(k) << ", h2=" << h2(k) << ")\n";
    }

    cout << "\n최종 테이블:\n";
    for (int s = 0; s < M; ++s) {
        cout << "  [" << s << "] ";
        if (table[s] == -1) cout << ".";
        else cout << table[s];
        cout << '\n';
    }
    return 0;
}
```

</CppRunner>

출력:

```
키 18 -> slot 5 (탐사 1회, h1=5, h2=7)
키 41 -> slot 2 (탐사 1회, h1=2, h2=6)
키 22 -> slot 9 (탐사 1회, h1=9, h2=11)
키 59 -> slot 7 (탐사 1회, h1=7, h2=12)
키 32 -> slot 6 (탐사 1회, h1=6, h2=9)
키 31 -> slot 0 (탐사 2회, h1=5, h2=8)
키 73 -> slot 8 (탐사 1회, h1=8, h2=2)
```

키 `31`은 `h1=5`로 이미 `18`이 차지한 슬롯 5와 충돌합니다. 그러면 `h2=8` 간격으로 건너뛰어 `(5 + 1·8) % 13 = 0`번 슬롯에 저장됩니다. `h2(k)`가 0이 아니고 `M`과 서로소<span class="gloss">coprime</span>여야 이렇게 모든 슬롯을 탐사할 수 있습니다.

👉 [문제 12로 돌아가기](./problem-12)
