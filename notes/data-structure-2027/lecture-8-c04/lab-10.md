# 문제 10 · 실습 — AVL 트리 균형 수선

문제의 키들을 AVL에 삽입하면, `35` 삽입 순간 노드 `10`에서 우-우(RR) 단일 좌회전이 일어나 균형이 회복됩니다. 최종 루트는 `40`입니다.

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
    int keys[] = {40, 10, 55, 7, 20, 70, 17, 30, 35};
    Node* root = nullptr;
    for (int k : keys) root = insert(root, k);
    cout << "루트: " << root->key << "\n";
    cout << "트리 구조(오른쪽이 위):\n";
    show(root, 0);
    return 0;
}
```

</CppRunner>

루트가 `40`으로 출력되며, `35`를 넣는 순간 자동으로 좌회전이 일어나 균형이 유지됩니다.

👉 [문제 10으로 돌아가기](./problem-10)
