# 문제 11 · 실습 — 배열을 힙으로 만들기

`buildHeap`은 **마지막 내부 노드부터 루트까지** `percolateDown`을 수행해, 임의 배열을 $\mathcal{O}(N)$에 최소 힙으로 바꿉니다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void percolateDown(vector<int>& a, int i, int n) {
    int tmp = a[i], child;
    for (; 2 * i + 1 < n; i = child) {
        child = 2 * i + 1;                               // 왼쪽 자식
        if (child + 1 < n && a[child + 1] < a[child]) child++;  // 더 작은 자식
        if (a[child] < tmp) a[i] = a[child];             // 자식을 끌어올림
        else break;
    }
    a[i] = tmp;
}

void buildHeap(vector<int>& a) {
    int n = a.size();
    for (int i = n / 2 - 1; i >= 0; i--)                 // 마지막 내부 노드부터
        percolateDown(a, i, n);
}

int main() {
    vector<int> a = {9, 4, 7, 1, 8, 3, 6, 2, 5, 0};
    cout << "입력 배열: ";
    for (int x : a) cout << x << " ";
    cout << "\n";

    buildHeap(a);

    cout << "min-heap 배열: ";
    for (int x : a) cout << x << " ";
    cout << "\n루트(최솟값): " << a[0] << endl;
    return 0;
}
```

</CppRunner>

임의로 섞인 배열이 최소 힙(부모 ≤ 자식)으로 재배열되고, 루트가 최솟값 `0`이 됩니다.

👉 [문제 11로 돌아가기](./problem-11)
