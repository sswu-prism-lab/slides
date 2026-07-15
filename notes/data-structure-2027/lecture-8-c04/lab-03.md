# 문제 3 · 실습 — 후위 순회

문제의 트리를 그대로 만들어, 후위 순회(왼쪽 → 오른쪽 → 루트)의 방문 순서를 확인합니다.

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

void postorder(Node* r, string& out) {
    if (!r) return;
    postorder(r->left, out);     // 왼쪽 먼저
    postorder(r->right, out);    // 그다음 오른쪽
    out += r->key; out += ' ';   // 마지막에 자기 자신
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
    postorder(A, out);
    cout << "후위 순회: " << out << endl;
    return 0;
}
```

</CppRunner>

출력은 `D B H F G C A` 입니다.

👉 [문제 3으로 돌아가기](./problem-03)
