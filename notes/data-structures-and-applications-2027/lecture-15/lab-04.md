# 문제 4 · 실습 — 네트워크(연결 요소) 개수

인접 행렬로 주어진 그래프에서 DFS로 연결 요소<span class="gloss">connected component</span>의 개수를 셉니다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int n;
vector<vector<int>> computers;
vector<bool> visited;

void dfs(int u) {
    visited[u] = true;
    for (int v = 0; v < n; ++v)
        if (computers[u][v] == 1 && !visited[v])
            dfs(v);
}

int countNetworks() {
    visited.assign(n, false);
    int cnt = 0;
    for (int i = 0; i < n; ++i)
        if (!visited[i]) {   // 새 탐색 시작 = 새 연결 요소
            ++cnt;
            dfs(i);
        }
    return cnt;
}

int main() {
    n = 3;
    computers = {{1, 1, 0},
                 {1, 1, 0},
                 {0, 0, 1}};
    cout << countNetworks() << '\n';
    return 0;
}
```

</CppRunner>

출력은 `2` 입니다. `0`·`1`번이 한 네트워크, `2`번이 홀로 한 네트워크입니다. 아직 방문하지 않은 정점에서 DFS를 새로 시작한 횟수가 곧 네트워크 개수입니다.

👉 [문제 4로 돌아가기](./problem-04)
