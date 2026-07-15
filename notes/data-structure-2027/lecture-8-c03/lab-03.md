# 문제 3 · 실습 — 전위 순회

문제의 트리를 그대로 만들어, 전위 순회(루트 → 왼쪽 → 오른쪽)의 방문 순서를 확인합니다.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

struct Node {
    char key;
    Node* left;
    Node* right;
    Node(char k) : key(k), left(nullptr), right(nullptr) {}
};

void preorder(Node* r, string& out) {
    if (!r) return;
    out += r->key; out += ' ';   // 노드를 먼저 방문
    preorder(r->left, out);      // 그다음 왼쪽
    preorder(r->right, out);     // 마지막 오른쪽
}

int main() {
    Node* A = new Node('A'); Node* B = new Node('B'); Node* C = new Node('C');
    Node* D = new Node('D'); Node* F = new Node('F');
    Node* G = new Node('G'); Node* H = new Node('H');
    A->left = B;  A->right = C;
    B->left = D;
    C->left = F;  C->right = G;
    F->left = H;

    string out;
    preorder(A, out);
    cout << "전위 순회: " << out << endl;
    return 0;
}
```

</CppRunner>

출력은 `A B D C F H G` 입니다.

👉 [문제 3으로 돌아가기](./problem-03)
