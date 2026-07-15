# 문제 5 · 실습 — 인접 행렬에서 간선 목록 뽑기

인접 행렬을 그대로 저장하고, $-\infty$(여기서는 매우 작은 수로 표현)가 아닌 성분을 훑어 방향 간선 목록을 출력합니다.

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    const int NEG = -1000000;   // -무한대 표시
    const int n = 4;
    int A[4][4] = {
        {   7,   0,   4, NEG},
        {  -4, NEG,   2,   1},
        { NEG,   3,   5,   1},
        { NEG,   6,   0, NEG}
    };

    cout << "방향 간선 (v_i -> v_j : 가중치)\n";
    int cnt = 0;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            if(A[i][j] != NEG){
                cout << "  v" << (i+1) << " -> v" << (j+1)
                     << " : " << A[i][j]
                     << (i == j ? "   (자기 루프)" : "") << "\n";
                cnt++;
            }
    cout << "총 간선 수 = " << cnt << "  (자기 루프 포함)\n";
    return 0;
}
```

</CppRunner>

👉 [문제 5로 돌아가기](./problem-05)
