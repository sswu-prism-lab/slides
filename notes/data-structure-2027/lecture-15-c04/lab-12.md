# 문제 12 · 실습 — 허프만 코드 생성

빈도표로부터 허프만 트리를 만들고, 각 문자의 코드와 총 비트 수(가중 경로 길이)를 출력합니다. 매번 가장 작은 두 노드를 꺼내 합치며, 먼저 꺼낸(더 작은) 노드를 왼쪽(`0`)에 둡니다.

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <string>
using namespace std;

struct Node {
    int weight;
    char ch;                 // 내부 노드는 '\0'
    Node *left, *right;
    Node(int w, char c): weight(w), ch(c), left(nullptr), right(nullptr) {}
    Node(int w, Node* l, Node* r): weight(w), ch('\0'), left(l), right(r) {}
};

void collect(Node* n, string code, vector<pair<char,string>>& out){
    if(!n->left && !n->right){ out.push_back({n->ch, code}); return; }
    collect(n->left,  code + "0", out);
    collect(n->right, code + "1", out);
}

int main(){
    vector<pair<char,int>> freq = {
        {'a',19},{'b',13},{'c',24},{'d',2},{'e',1},{'f',8},{'g',12}
    };

    int seq = 0;
    auto cmp = [](const pair<pair<int,int>,Node*>& x,
                  const pair<pair<int,int>,Node*>& y){ return x.first > y.first; };
    priority_queue<pair<pair<int,int>,Node*>,
                   vector<pair<pair<int,int>,Node*>>, decltype(cmp)> pq(cmp);
    for(auto& f : freq) pq.push({{f.second, seq++}, new Node(f.second, f.first)});

    while(pq.size() > 1){
        auto A = pq.top(); pq.pop();     // 더 작은 쪽 = 왼쪽
        auto B = pq.top(); pq.pop();
        int w = A.first.first + B.first.first;
        pq.push({{w, seq++}, new Node(w, A.second, B.second)});
    }
    Node* root = pq.top().second;

    vector<pair<char,string>> codes;
    collect(root, "", codes);

    int total = 0, fmap[128] = {0};
    for(auto& f : freq) fmap[(int)f.first] = f.second;
    cout << "문자 | 빈도 | 코드\n";
    for(auto& c : codes){
        cout << "  " << c.first << "  |  " << fmap[(int)c.first]
             << "  | " << c.second << "\n";
        total += fmap[(int)c.first] * (int)c.second.size();
    }
    cout << "\n총 비트 수(가중 경로 길이) = " << total << " bit\n";
    return 0;
}
```

</CppRunner>

👉 [문제 12로 돌아가기](./problem-12)
