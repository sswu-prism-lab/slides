# 문제 7 · 정적 멤버와 `Foo`

::: info 문제 7 [2점]
아래 코드를 읽고, 출력을 예상하여 작성하세요.

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
:::

::: details 풀이 및 해설
`myNum`은 **정적 멤버<span class="gloss">static member</span>**로, 모든 객체가 **하나의 값을 공유**합니다. 반면 `yourNum`은 객체마다 따로 갖는 인스턴스 멤버로 `1`로 초기화됩니다.

연산 순서를 따라가면:

- 초기값: `Foo::myNum = 0`.
- `Foo foo1;` → 생성자에서 `myNum--` → `myNum = -1`.
- `Foo foo2;` → 생성자에서 `myNum--` → `myNum = -2`.
- `foo1.yourNum` = `1`.
- `foo2.myNum` = 공유되는 `myNum` = `-2`.

따라서 `foo1.yourNum + foo2.myNum = 1 + (-2) = -1`.

$$\boxed{-1}$$

👉 [실습(C++)에서 확인하기](./lab-07)
:::
