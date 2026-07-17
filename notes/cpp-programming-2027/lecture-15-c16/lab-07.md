# 문제 7 · 실습 — 정적 멤버와 `Foo`

정적 멤버 `myNum`이 두 객체에서 공유되어 `-2`까지 줄어드는 과정을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Foo {
public:
    static int myNum;
    int yourNum = 1;
    Foo() {
        myNum--;
    };
};

int Foo::myNum = 0;

int main() {
    Foo foo1;
    Foo foo2;
    cout << foo1.yourNum + foo2.myNum;
}
```

</CppRunner>

출력은 `-1` 입니다. `foo1`, `foo2` 생성으로 공유되는 `myNum`이 `-2`가 되고, `1 + (-2) = -1`입니다.

👉 [문제 7로 돌아가기](./problem-07)
