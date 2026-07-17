# 문제 11 · 실습 — 버킷 정렬

`[0, 1)` 구간에 균등 분포<span class="gloss">uniform distribution</span>한 실수 배열을 버킷 정렬<span class="gloss">bucket sort</span>로 정렬합니다. 값을 버킷에 고르게 분산 → 각 버킷 정렬 → 이어 붙이기의 세 단계를 확인하세요.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// [0, 1) 구간에 균등 분포한 실수에 대한 버킷 정렬
vector<double> bucketSort(vector<double> a) {
    int n = a.size();
    vector<vector<double>> buckets(n);
    for (double x : a)                 // 값에 비례해 버킷 배정
        buckets[(int)(n * x)].push_back(x);
    for (auto& b : buckets)            // 각 버킷 내부 정렬
        sort(b.begin(), b.end());
    vector<double> out;                // 버킷 순서대로 이어 붙임
    for (auto& b : buckets)
        for (double x : b) out.push_back(x);
    return out;
}

int main() {
    vector<double> a = {0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68};
    vector<double> s = bucketSort(a);
    cout << "정렬 결과: ";
    for (double x : s) cout << x << ' ';
    cout << '\n';
    return 0;
}
```

</CppRunner>

출력은 `정렬 결과: 0.12 0.17 0.21 0.23 0.26 0.39 0.68 0.72 0.78 0.94` 입니다. 값이 `[0,1)`에 고르게 퍼져 있어 각 버킷에 원소가 골고루 나뉘고, 이때 평균 시간 복잡도는 O(n)입니다. 값이 한 구간에 몰리면 한 버킷에 집중되어 O(n²)까지 나빠집니다.

👉 [문제 11로 돌아가기](./problem-11)
