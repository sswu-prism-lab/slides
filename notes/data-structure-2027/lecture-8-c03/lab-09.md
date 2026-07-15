# 문제 9 · 실습 — 큐 2개로 스택 구현

두 개의 큐로 스택을 만듭니다. `push`는 그냥 넣고($\mathcal{O}(1)$), `pop`은 마지막 하나만 남기고 다른 큐로 옮겨 top을 꺼냅니다($\mathcal{O}(N)$).

<CppRunner>

```cpp
#include <iostream>
#include <queue>
using namespace std;

class StackWith2Queues {
    queue<int> q1, q2;
public:
    void push(int x) {          // O(1)
        q1.push(x);
    }
    int pop() {                 // O(N)
        while (q1.size() > 1) { q2.push(q1.front()); q1.pop(); }
        int top = q1.front(); q1.pop();
        swap(q1, q2);           // 역할 교환
        return top;
    }
    bool empty() { return q1.empty(); }
};

int main() {
    StackWith2Queues s;
    for (int i = 1; i <= 5; i++) { s.push(i); cout << "push " << i << "\n"; }

    cout << "pop 순서: ";
    while (!s.empty()) cout << s.pop() << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

`1,2,3,4,5`를 넣고 꺼내면 `5 4 3 2 1` 순으로 나와, LIFO(후입선출)가 성립함을 볼 수 있습니다.

👉 [문제 9로 돌아가기](./problem-09)
