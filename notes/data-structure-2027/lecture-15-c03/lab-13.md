# 문제 13 · 실습 — 가위-바위-보 판정

컴퓨터의 선택을 난수로 뽑고(재현을 위해 시드 고정), 여러 개의 사용자 입력에 대해 승패를 한 줄 판정식 $(\text{user}-\text{comp})\bmod 3$ 으로 출력합니다.

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

// 0=가위, 1=바위, 2=보
string name(int x){ return x==0 ? "가위" : x==1 ? "바위" : "보"; }

string judge(int user, int comp){
    int diff = (user - comp + 3) % 3;
    if(diff == 0) return "무승부";
    if(diff == 1) return "승";      // user가 이김
    return "패";
}

int main(){
    srand(42);                       // 결정적 출력을 위한 고정 시드
    int userInputs[] = {0, 1, 2, 1, 0};   // 데모용 사용자 입력들

    for(int u : userInputs){
        int comp = rand() % 3;       // 컴퓨터의 임의 선택 — O(1)
        cout << "사용자: " << name(u)
             << " / 컴퓨터: " << name(comp)
             << "  ->  " << judge(u, comp) << "\n";
    }
    cout << "\n한 판 판정은 반복문 없이 상수 시간 = O(1)\n";
    return 0;
}
```

</CppRunner>

👉 [문제 13으로 돌아가기](./problem-13)
