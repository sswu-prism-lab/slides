# 문제 2 · 실습 — 계수 정렬은 정수 키에만

계수 정렬<span class="gloss">counting sort</span>이 **값을 배열 인덱스로 사용**하는 방식임을 확인합니다. 그래서 정수 키에는 잘 동작하지만 실수 키에는 쓸 수 없습니다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

// 0 이상 정수 키에 대한 계수 정렬
vector<int> countingSort(const vector<int>& a, int maxVal) {
    vector<int> count(maxVal + 1, 0);
    for (int x : a) count[x]++;          // 값을 인덱스로 사용
    vector<int> out;
    for (int v = 0; v <= maxVal; ++v)
        while (count[v]-- > 0) out.push_back(v);
    return out;
}

int main() {
    vector<int> a = {4, 2, 2, 8, 3, 3, 1};
    vector<int> sorted = countingSort(a, 8);
    cout << "정렬 결과: ";
    for (int x : sorted) cout << x << ' ';
    cout << '\n';
    cout << "실수 키(예: 3.14)는 count[3.14] 처럼 인덱스로 쓸 수 없어 계수 정렬 불가\n";
    return 0;
}
```

</CppRunner>

`count[x]++` 처럼 값 자체를 인덱스로 써야 하므로, 키는 반드시 유한 범위의 정수여야 합니다. `count[3.14]`는 성립하지 않으므로 실수 배열은 계수 정렬로 정렬할 수 없습니다.

👉 [문제 2로 돌아가기](./problem-02)
