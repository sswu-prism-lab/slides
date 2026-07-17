# 문제 1 · 실습 — DFS는 스택 기반

깊이 우선 탐색<span class="gloss">depth-first search</span>을 **명시적 스택**으로 구현해, DFS가 스택 자료구조로 자연스럽게 동작함을 확인합니다. (큐로 바꾸면 너비 우선 탐색이 됩니다.)

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// 인접 리스트로 표현한 무방향 그래프
vector<vector<int>> adj = {
    {1, 2},    // 0
    {0, 3, 4}, // 1
    {0},       // 2
    {1},       // 3
    {1}        // 4
};

int main() {
    int start = 0, n = adj.size();
    vector<bool> visited(n, false);
    stack<int> st;                 // DFS는 스택 기반
    st.push(start);

    cout << "DFS 방문 순서: ";
    while (!st.empty()) {
        int u = st.top(); st.pop();
        if (visited[u]) continue;
        visited[u] = true;
        cout << u << ' ';
        // 작은 번호를 먼저 방문하도록 역순으로 push
        for (int i = adj[u].size() - 1; i >= 0; --i)
            if (!visited[adj[u][i]]) st.push(adj[u][i]);
    }
    cout << '\n';
    return 0;
}
```

</CppRunner>

출력은 `DFS 방문 순서: 0 1 3 4 2` 입니다. 한 정점에서 갈 수 있는 데까지 깊이 들어갔다가 막히면 스택에서 이전 정점을 꺼내 되돌아옵니다. 큐로 바꾸면 층별로 방문하는 BFS가 됩니다.

👉 [문제 1로 돌아가기](./problem-01)
