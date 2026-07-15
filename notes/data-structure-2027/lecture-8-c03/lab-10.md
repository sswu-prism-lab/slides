# 문제 10 · 실습 — AVL 트리 균형 수선

AVL 트리는 삽입할 때마다 회전으로 **스스로 균형을 유지**합니다. 문제의 키들을 넣으면, `35` 삽입 순간 좌-우(LR) 이중 회전이 일어나 `37`이 루트가 됩니다.

<CppRunner>

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct Node { int key, h; Node *l, *r; Node(int k):key(k),h(1),l(nullptr),r(nullptr){} };
int H(Node* n)  { return n ? n->h : 0; }
int BF(Node* n) { return n ? H(n->l) - H(n->r) : 0; }
void upd(Node* n){ n->h = 1 + max(H(n->l), H(n->r)); }

Node* rotR(Node* y){ Node* x=y->l; y->l=x->r; x->r=y; upd(y); upd(x); return x; }
Node* rotL(Node* x){ Node* y=x->r; x->r=y->l; y->l=x; upd(x); upd(y); return y; }

Node* insert(Node* n, int k) {
    if (!n) return new Node(k);
    if (k < n->key) n->l = insert(n->l, k);
    else if (k > n->key) n->r = insert(n->r, k);
    else return n;
    upd(n);
    int b = BF(n);
    if (b > 1  && k < n->l->key) return rotR(n);                 // LL
    if (b < -1 && k > n->r->key) return rotL(n);                 // RR
    if (b > 1  && k > n->l->key){ n->l = rotL(n->l); return rotR(n); } // LR
    if (b < -1 && k < n->r->key){ n->r = rotR(n->r); return rotL(n); } // RL
    return n;
}

void show(Node* n, int depth) {   // 오른쪽이 위로, 들여쓰기 = 깊이
    if (!n) return;
    show(n->r, depth + 1);
    for (int i = 0; i < depth; i++) cout << "    ";
    cout << n->key << "\n";
    show(n->l, depth + 1);
}

int main() {
    int keys[] = {40, 20, 55, 17, 37, 70, 15, 38, 30, 35};
    Node* root = nullptr;
    for (int k : keys) root = insert(root, k);
    cout << "루트: " << root->key << "\n";
    cout << "트리 구조(오른쪽이 위):\n";
    show(root, 0);
    return 0;
}
```

</CppRunner>

루트가 `37`로 출력되며, 모든 키를 넣어도 AVL이 항상 균형을 유지함을 확인할 수 있습니다.

👉 [문제 10으로 돌아가기](./problem-10)
