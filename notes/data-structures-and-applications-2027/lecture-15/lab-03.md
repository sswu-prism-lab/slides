# 문제 3 · 실습 — 주식가격 단조 스택

`prices = [1, 2, 3, 2, 3]`에 대해 단조 스택<span class="gloss">monotonic stack</span>으로 각 시점의 "가격이 떨어지지 않은 기간"을 O(n)에 구합니다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

// 단조 스택으로 "가격이 떨어지지 않은 기간(초)"을 O(n)에 계산
vector<int> stockSpans(const vector<int>& prices) {
    int n = prices.size();
    vector<int> answer(n, 0);
    stack<int> st;                       // 아직 하락을 못 만난 시점의 인덱스
    for (int i = 0; i < n; ++i) {
        // 스택 위 시점보다 지금 가격이 더 낮으면 그 시점의 기간 확정
        while (!st.empty() && prices[st.top()] > prices[i]) {
            int j = st.top(); st.pop();
            answer[j] = i - j;           // i에서 하락 → 기간 = i-j
        }
        st.push(i);
    }
    // 끝까지 하락이 없던 시점: 남은 초 수
    while (!st.empty()) {
        int j = st.top(); st.pop();
        answer[j] = (n - 1) - j;
    }
    return answer;
}

int main() {
    vector<int> prices = {1, 2, 3, 2, 3};
    vector<int> ans = stockSpans(prices);
    for (int x : ans) cout << x << ' ';
    cout << '\n';
    return 0;
}
```

</CppRunner>

출력은 `4 3 1 1 0` 입니다. 가격이 같을 때(`prices[top] > prices[i]`가 거짓)는 꺼내지 않아 "떨어지지 않은" 것으로 처리하는 점이 핵심입니다.

👉 [문제 3으로 돌아가기](./problem-03)
