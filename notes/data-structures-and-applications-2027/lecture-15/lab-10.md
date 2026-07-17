# 문제 10 · 실습 — 안정 정렬 vs 불안정 정렬

같은 키(점수)를 가진 원소들의 상대 순서가 어떻게 되는지, 안정 정렬<span class="gloss">stable sort</span>인 `std::stable_sort`와 불안정 정렬인 선택 정렬<span class="gloss">selection sort</span>을 비교합니다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct Rec { string name; int score; };

// 직접 구현한 선택 정렬 — 대표적인 불안정 정렬
void selectionSort(vector<Rec>& a) {
    int n = a.size();
    for (int i = 0; i < n; ++i) {
        int m = i;
        for (int j = i + 1; j < n; ++j)
            if (a[j].score < a[m].score) m = j;
        swap(a[i], a[m]);   // 멀리 있는 원소와 교환 → 같은 키 순서 깨질 수 있음
    }
}

int main() {
    // 점수가 같은 원소: A·C·F(3점), B·E(1점) — 입력 순서에 주목
    vector<Rec> data = {
        {"A", 3}, {"B", 1}, {"C", 3}, {"D", 2}, {"E", 1}, {"F", 3}
    };

    vector<Rec> s1 = data;
    stable_sort(s1.begin(), s1.end(),
                [](const Rec& x, const Rec& y){ return x.score < y.score; });

    vector<Rec> s2 = data;
    selectionSort(s2);

    cout << "원본           : ";
    for (auto& r : data) cout << r.name << r.score << ' ';
    cout << '\n';
    cout << "stable_sort(안정): ";
    for (auto& r : s1) cout << r.name << r.score << ' ';
    cout << "   <- 3점은 A C F 순서 유지\n";
    cout << "선택 정렬(불안정): ";
    for (auto& r : s2) cout << r.name << r.score << ' ';
    cout << "   <- 3점이 C A F 로 뒤바뀜\n";
    return 0;
}
```

</CppRunner>

출력:

```
원본           : A3 B1 C3 D2 E1 F3
stable_sort(안정): B1 E1 D2 A3 C3 F3    <- 3점은 A C F 순서 유지
선택 정렬(불안정): B1 E1 D2 C3 A3 F3    <- 3점이 C A F 로 뒤바뀜
```

`stable_sort`는 점수가 같은 A·C·F의 입력 순서를 그대로 보존하지만, 선택 정렬은 먼 원소와 교환하는 과정에서 A와 C의 순서를 뒤바꿉니다. 이것이 안정성의 차이입니다.

👉 [문제 10으로 돌아가기](./problem-10)
