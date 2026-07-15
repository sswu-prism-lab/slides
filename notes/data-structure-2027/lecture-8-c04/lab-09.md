# 문제 9 · 실습 — 배열 하나로 스택 2개

한 배열의 **양쪽 끝**에서 두 스택이 마주 보며 자라도록 구현합니다. 모든 연산은 인덱스만 바꾸므로 $\mathcal{O}(1)$입니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class TwoStacks {
    int* arr; int cap; int top1; int top2;
public:
    TwoStacks(int n) : cap(n) { arr = new int[n]; top1 = -1; top2 = n; }
    ~TwoStacks() { delete[] arr; }

    bool full() { return top1 + 1 >= top2; }          // 두 top이 만나면 가득 참
    bool push1(int x) { if (full()) return false; arr[++top1] = x; return true; }
    bool push2(int x) { if (full()) return false; arr[--top2] = x; return true; }
    int  pop1() { return arr[top1--]; }
    int  pop2() { return arr[top2++]; }
    bool empty1() { return top1 < 0; }
    bool empty2() { return top2 >= cap; }
};

int main() {
    TwoStacks ts(6);
    ts.push1(10); ts.push1(20); ts.push1(30);   // 스택1: 왼쪽에서
    ts.push2(99); ts.push2(88);                 // 스택2: 오른쪽에서

    cout << "스택1 pop: "; while (!ts.empty1()) cout << ts.pop1() << " "; cout << "\n";
    cout << "스택2 pop: "; while (!ts.empty2()) cout << ts.pop2() << " "; cout << "\n";
    return 0;
}
```

</CppRunner>

스택1은 `30 20 10`, 스택2는 `88 99` 순으로 나와 각각 독립적인 LIFO로 동작함을 확인할 수 있습니다.

👉 [문제 9로 돌아가기](./problem-09)
