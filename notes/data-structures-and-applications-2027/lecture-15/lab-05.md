# 문제 5 · 실습 — 이진 트리 중위 순회

문제 5의 트리 구조를 그대로 만들고(위치 라벨 A~G), 중위 순회<span class="gloss">inorder traversal</span> 결과를 출력합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node {
    char label;
    Node *left = nullptr, *right = nullptr;
    Node(char c) : label(c) {}
};

// 왼쪽 → 자기 자신 → 오른쪽
void inorder(Node* t) {
    if (!t) return;
    inorder(t->left);
    cout << t->label << ' ';
    inorder(t->right);
}

int main() {
    // 문제 5의 트리 구조 (위치 라벨 A~G)
    Node* A = new Node('A'); // 루트
    Node* B = new Node('B'); Node* C = new Node('C');
    Node* D = new Node('D'); Node* E = new Node('E');
    Node* F = new Node('F'); Node* G = new Node('G');
    A->left = B;  A->right = C;
    B->left = D;                 // B의 오른쪽 없음
    C->left = E;  C->right = F;
    E->left = G;                 // E의 오른쪽 없음

    cout << "중위 순회: ";
    inorder(A);
    cout << '\n';
    return 0;
}
```

</CppRunner>

출력은 `중위 순회: D B A G E C F` 입니다. 각 노드에서 왼쪽 서브트리를 모두 방문한 뒤 자기 자신, 그다음 오른쪽 서브트리를 방문합니다.

👉 [문제 5로 돌아가기](./problem-05)
