# 문제 5 · 실습 — 단순 연결 리스트 역순

세 개의 포인터 `prev`, `cur`, `next`로 링크 방향을 뒤집어, 한 번의 순회($\mathcal{O}(N)$)로 리스트를 역순으로 만듭니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node {
    int v;
    Node* next;
    Node(int x) : v(x), next(nullptr) {}
};

Node* reverse(Node* head) {         // O(N) 시간, O(1) 공간
    Node* prev = nullptr;
    while (head) {
        Node* nxt = head->next;     // 다음 노드 기억
        head->next = prev;          // 링크 뒤집기
        prev = head;                // 한 칸 전진
        head = nxt;
    }
    return prev;                     // 새 head
}

void print(Node* h) {
    for (; h; h = h->next) cout << h->v << " ";
    cout << "\n";
}

int main() {
    Node* head = nullptr;
    for (int i = 5; i >= 1; i--) {   // 1 2 3 4 5 만들기
        Node* n = new Node(i);
        n->next = head; head = n;
    }
    cout << "원본: "; print(head);
    head = reverse(head);
    cout << "역순: "; print(head);
    return 0;
}
```

</CppRunner>

`1 2 3 4 5`가 `5 4 3 2 1`로 뒤집힙니다.

👉 [문제 5로 돌아가기](./problem-05)
