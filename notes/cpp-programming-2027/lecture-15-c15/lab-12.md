# 문제 12 · 실습 — 인스턴스 멤버와 클래스 멤버

인스턴스 멤버 `id`는 객체마다 다르고, 클래스(정적) 멤버 `total`은 모든 객체가 공유합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Counter {
public:
    int id;              // 인스턴스 멤버: 객체마다 별도
    static int total;    // 클래스 멤버: 모두가 공유
    Counter() {
        total++;         // 공유값 증가
        id = total;      // 이 객체만의 번호
    }
};
int Counter::total = 0;  // 정적 멤버 정의

int main() {
    Counter a, b, c;
    cout << "a.id=" << a.id << ", b.id=" << b.id << ", c.id=" << c.id << endl;
    cout << "공유되는 total=" << Counter::total << endl;
    return 0;
}
```

</CppRunner>

출력은
```
a.id=1, b.id=2, c.id=3
공유되는 total=3
```
입니다. `id`는 객체마다 다르지만 `total`은 하나만 존재합니다.

👉 [문제 12로 돌아가기](./problem-12)
