# 문제 8 · 실습 — Kadane 알고리즘

배열 `{1, -2, 3, 5, -4, 2, 5}`에 대해 Kadane 알고리즘으로 `dp`를 채우고 최대 부분합<span class="gloss">maximum subarray</span>을 구합니다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> a = {1, -2, 3, 5, -4, 2, 5};
    int n = a.size();
    vector<int> dp(n);
    dp[0] = a[0];
    for (int i = 1; i < n; ++i)
        dp[i] = max(a[i], dp[i-1] + a[i]);   // 여기서 끝나는 최대 부분합

    cout << "dp: ";
    for (int x : dp) cout << x << ' ';
    cout << '\n';

    int best = *max_element(dp.begin(), dp.end());
    cout << "최대 부분합: " << best << '\n';
    return 0;
}
```

</CppRunner>

출력:

```
dp: 1 -1 3 8 4 6 11
최대 부분합: 11
```

`dp` 열이 문제의 "최대 부분합"과 정확히 일치하며, 그 최댓값 `11`이 정답입니다(부분 배열 `{3, 5, -4, 2, 5}`).

👉 [문제 8로 돌아가기](./problem-08)
