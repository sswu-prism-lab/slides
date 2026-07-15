# 문제 4 · 실습 — 좌향 힙 병합

두 좌향 힙을 실제로 병합해 결과 트리와 각 노드의 널 경로 길이(npl)를 출력합니다. 트리는 오른쪽 자식을 위로, 왼쪽 자식을 아래로 눕혀 그립니다(들여쓰기가 깊을수록 아래 층).

<CppRunner>

```cpp
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

struct Node {
    int key, npl;
    Node *left, *right;
    Node(int k): key(k), npl(0), left(nullptr), right(nullptr) {}
};

int npl(Node* h){ return h ? h->npl : -1; }

// 입력 힙들의 npl을 먼저 정확히 계산
int computeNpl(Node* h){
    if(!h) return -1;
    int l = computeNpl(h->left), r = computeNpl(h->right);
    return h->npl = min(l, r) + 1;
}

Node* merge(Node* a, Node* b){
    if(!a) return b;
    if(!b) return a;
    if(a->key > b->key) swap(a, b);         // 작은 루트가 a
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
    // 힙 A: 루트 4
    Node* a = N(4);
    a->left = N(19); a->left->left = N(27); a->left->left->left = N(43);
    a->left->right = N(20);
    a->right = N(8);  a->right->left = N(12);
    a->right->left->left = N(15); a->right->left->right = N(25);

    // 힙 B: 루트 6
    Node* b = N(6);
    b->left = N(8); b->left->left = N(14);
    b->right = N(7);

    computeNpl(a);
    computeNpl(b);

    Node* m = merge(a, b);
    cout << "병합 결과 (오른쪽=위, 왼쪽=아래):\n\n";
    show(m, 0);
    cout << "\n루트 = " << m->key << ", 루트 npl = " << m->npl << "\n";
    return 0;
}
```

</CppRunner>

👉 [문제 4로 돌아가기](./problem-04)
