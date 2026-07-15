# 문제 6 · 실습 — 다익스트라 알고리즘

7개 정점 유향 가중치 그래프에서 $v_3$ 을 시작점으로 최단 거리를 계산하고, 각 정점까지의 거리와 경로를 출력합니다. 배열에서 $v_1{=}0,\dots,v_7{=}6$ 으로 둡니다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main(){
    const int n = 7;
    const int INF = INT_MAX;
    vector<vector<pair<int,int>>> adj(n);   // adj[u] = {(v, w), ...}
    auto add = [&](int u, int v, int w){ adj[u-1].push_back({v-1, w}); };
    // 유향 간선
    add(3,2,2); add(3,4,5); add(2,1,4); add(2,4,1); add(4,5,3);
    add(1,5,6); add(5,6,2); add(4,6,7); add(5,7,8); add(6,7,4);

    int src = 3 - 1;                        // 시작점 v3
    vector<int> dist(n, INF), prev(n, -1);
    vector<bool> done(n, false);
    dist[src] = 0;

    for(int it = 0; it < n; it++){
        int u = -1;
        for(int v = 0; v < n; v++)
            if(!done[v] && dist[v] != INF && (u == -1 || dist[v] < dist[u])) u = v;
        if(u == -1) break;
        done[u] = true;
        for(auto& e : adj[u]){
            int v = e.first, w = e.second;
            if(dist[u] + w < dist[v]){ dist[v] = dist[u] + w; prev[v] = u; }
        }
    }

    cout << "v3 로부터의 최단 거리와 경로:\n";
    for(int v = 0; v < n; v++){
        cout << "  v" << (v+1) << " : 거리 " << dist[v] << ",  경로 ";
        vector<int> path;
        for(int x = v; x != -1; x = prev[x]) path.push_back(x);
        for(int i = (int)path.size()-1; i >= 0; i--)
            cout << "v" << (path[i]+1) << (i ? " -> " : "");
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

👉 [문제 6으로 돌아가기](./problem-06)
