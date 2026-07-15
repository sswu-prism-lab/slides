# 문제 6 · 실습 — 프림 알고리즘

7개 정점 무향 가중치 그래프에 프림 알고리즘을 적용해, 트리에 편입되는 간선을 순서대로 출력하고 총 가중치를 계산합니다. $A{=}0,\dots,G{=}6$.

<CppRunner>

```cpp
#include <iostream>
#include <climits>
using namespace std;

int main(){
    const int n = 7;                 // A..G
    const int INF = INT_MAX;
    int W[7][7];
    for(int i=0;i<n;i++) for(int j=0;j<n;j++) W[i][j] = INF;
    auto add = [&](int u,int v,int w){ W[u][v]=W[v][u]=w; };
    // A0 B1 C2 D3 E4 F5 G6
    add(0,1,7); add(0,3,5); add(1,2,8); add(1,3,9); add(1,4,7);
    add(2,4,5); add(3,4,15); add(3,5,6); add(4,5,8); add(4,6,9); add(5,6,11);

    const char* name = "ABCDEFG";
    bool inTree[7] = {false};
    int dist[7], parent[7];
    for(int i=0;i<n;i++){ dist[i]=INF; parent[i]=-1; }
    dist[0] = 0;                      // A에서 시작

    int total = 0;
    for(int it=0; it<n; it++){
        int u = -1;
        for(int v=0; v<n; v++)
            if(!inTree[v] && (u==-1 || dist[v] < dist[u])) u = v;
        inTree[u] = true;
        if(parent[u] != -1){
            cout << "간선 " << name[parent[u]] << "-" << name[u]
                 << " (가중치 " << dist[u] << ") 추가\n";
            total += dist[u];
        }
        for(int v=0; v<n; v++)
            if(!inTree[v] && W[u][v] != INF && W[u][v] < dist[v]){
                dist[v] = W[u][v]; parent[v] = u;
            }
    }
    cout << "\nMST 총 가중치 = " << total << "\n";
    return 0;
}
```

</CppRunner>

👉 [문제 6으로 돌아가기](./problem-06)
