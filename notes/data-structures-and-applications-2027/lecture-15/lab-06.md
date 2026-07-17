# 문제 6 · 실습 — 자가 균형 트리(std::set)

C++ 표준 라이브러리의 `std::set`은 내부적으로 **레드-블랙 트리**<span class="gloss">red-black tree</span>로 구현됩니다. 키 `7`을 삽입해도 삽입 과정에서 자동으로 회전·재색칠이 일어나 균형이 유지되고, 중위 순회는 항상 오름차순임을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
#include <set>
using namespace std;

int main() {
    // std::set 은 내부적으로 레드-블랙 트리(자가 균형 BST)로 구현됨
    set<int> tree = {10, 5, 13, 3, 6, 15, 2, 8};
    cout << "삽입 전 (중위=오름차순): ";
    for (int x : tree) cout << x << ' ';
    cout << '\n';

    tree.insert(7);   // 삽입 시 내부에서 회전·재색칠로 균형 유지
    cout << "7 삽입 후 (중위=오름차순): ";
    for (int x : tree) cout << x << ' ';
    cout << '\n';
    return 0;
}
```

</CppRunner>

출력:

```
삽입 전 (중위=오름차순): 2 3 5 6 8 10 13 15
7 삽입 후 (중위=오름차순): 2 3 5 6 7 8 10 13 15
```

`7`이 8의 왼쪽에 들어간 뒤 RL 회전과 재색칠(7→검정, 6·8→빨강)로 균형을 되찾습니다. 라이브러리는 내부 색·회전을 숨기지만, 중위 순회가 여전히 정렬 상태라는 것으로 트리가 올바르게 유지됨을 확인할 수 있습니다.

👉 [문제 6으로 돌아가기](./problem-06)
