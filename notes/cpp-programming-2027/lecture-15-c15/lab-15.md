# 문제 15 · 실습 — 스택 클래스 UML과 구현

UML로 설계한 `Stack` 클래스를 구현하고, `push`/`pop`으로 후입선출(LIFO)을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Stack {
private:
    int arr[100];      // 요소 배열
    int topIndex;      // 최상단 인덱스, 비었으면 -1
public:
    Stack() : topIndex(-1) {}
    void push(int value) { arr[++topIndex] = value; }
    int  pop()           { return arr[topIndex--]; }
    int  top()           { return arr[topIndex]; }
    int  getSize()       { return topIndex + 1; }
    bool isEmpty()       { return topIndex == -1; }
};

int main() {
    Stack s;
    cout << boolalpha;
    cout << "isEmpty: " << s.isEmpty() << endl;   // 비어 있음
    s.push(10); s.push(20); s.push(30);           // 10,20,30 순으로 삽입
    cout << "getSize: " << s.getSize() << endl;
    cout << "top: " << s.top() << endl;           // 마지막에 넣은 30
    cout << "pop: " << s.pop() << endl;           // 30 (LIFO)
    cout << "pop: " << s.pop() << endl;           // 20
    cout << "getSize: " << s.getSize() << endl;
    cout << "isEmpty: " << s.isEmpty() << endl;
    return 0;
}
```

</CppRunner>

출력은
```
isEmpty: true
getSize: 3
top: 30
pop: 30
pop: 20
getSize: 1
isEmpty: false
```
입니다. 가장 나중에 넣은 `30`이 가장 먼저 나오는 후입선출을 확인할 수 있습니다.

👉 [문제 15로 돌아가기](./problem-15)
