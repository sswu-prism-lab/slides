# 문제 13 · 실습 — 화폐 최소 개수 거스름돈

큰 화폐부터 최대한 사용하는 탐욕 알고리즘으로, 입력 금액을 만드는 데 필요한 최소 화폐 개수와 내역을 출력합니다. 입력 예시 17,630원을 그대로 사용합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main(){
    int coins[] = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
    int nc = sizeof(coins) / sizeof(coins[0]);

    int amount = 17630;                  // 입력 금액
    int original = amount, count = 0;

    cout << "입력 금액: " << original << "원\n";
    for(int i = 0; i < nc; i++){
        int use = amount / coins[i];     // 이 단위를 몇 장 쓰는가
        if(use > 0){
            cout << "  " << coins[i] << "원 " << use << "개\n";
            count += use;
            amount %= coins[i];
        }
    }
    cout << "총 화폐 개수 = " << count << "개\n";
    return 0;
}
```

</CppRunner>

👉 [문제 13으로 돌아가기](./problem-13)
