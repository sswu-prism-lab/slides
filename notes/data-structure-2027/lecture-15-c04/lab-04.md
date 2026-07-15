# 문제 4 · 실습 — 좌향 힙 병합

두 좌향 힙을 병합해 결과 트리와 각 노드의 널 경로 길이(npl)를 출력합니다. 트리는 오른쪽 자식을 위로, 왼쪽 자식을 아래로 눕혀 그립니다(들여쓰기가 깊을수록 아래 층).

<CppRunner>

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

struct Node {
    int key, npl;
    Node *left, *right;
    Node(int k): key(k), npl(0), left(nullptr), right(nullptr) {}
};

int npl(Node* h){ return h ? h->npl : -1; }

int computeNpl(Node* h){
    if(!h) return -1;
    int l = computeNpl(h->left), r = computeNpl(h->right);
    return h->npl = min(l, r) + 1;
}

Node* merge(Node* a, Node* b){
    if(!a) return b;
    if(!b) return a;
    if(a->key > b->key) swap(a, b);
    a->right = merge(a->right, b);
    if(npl(a->left) < npl(a->right)) swap(a->left, a->right);
    a->npl = npl(a->right) + 1;
    return a;
}

void show(Node* h, int depth){
    if(!h) return;
    show(h->right, depth + 1);
    for(int i = 0; i < depth; i++) cout << "        ";
    cout << h->key << " (npl=" << h->npl << ")\n";
    show(h->left, depth + 1);
}

Node* N(int k){ return new Node(k); }

int main(){
    // 힙 A: 루트 3
    Node* a = N(3);
    a->left = N(10);  a->left->left = N(27); a->left->right = N(28);
    a->right = N(16); a->right->left = N(33);

    // 힙 B: 루트 4
    Node* b = N(4);
    b->left = N(11); b->left->left = N(32); b->left->left->left = N(50);
    b->left->right = N(41);
    b->right = N(12); b->right->left = N(22); b->right->left->left = N(33);

    computeNpl(a);
    computeNpl(b);

    Node* m = merge(a, b);
    cout << "병합 결과 (오른쪽=위, 왼쪽=아래):\n\n";
    show(m, 0);
    cout << "\n루트 = " << m->key
         << ", 루트 npl = " << m->npl
         << ", 좌·우 자식 = " << m->left->key << ", " << m->right->key << "\n";
    return 0;
}
```

</CppRunner>

👉 [문제 4로 돌아가기](./problem-04)
