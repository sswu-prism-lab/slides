# 문제 11 · `Car` 클래스 오류 수정

::: info 문제 11 [3점]
아래 문제를 읽고, 각 물음에 답하세요.

아래는 생성자를 통해 자동차 번호와 연료량을 설정하며 생성된 인스턴스의 개수를 출력하는 코드이다. 아래 코드에 오류가 있다면 수정하시오.

```cpp
#include <iostream>
using namespace std;

class Car {
public:
    static int sum;
    Car(int n, double g);
    void show();
    void showSum();

private:
    int num;
    double gas;
};

void Car::Car(int n, double g) {
    num = n;
    gas = g;
}

void Car::showSum() {
    cout << sum << endl;
}

void Car::show() {
    cout << num << " " << gas << endl;
}

int main() {
    Car car1(1234, 20.5);
    Car car2(4567, 30.5);
    Car::showSum();
}
```
:::

::: details 풀이 및 해설
"생성된 인스턴스의 개수"를 세어 출력하려는 코드입니다. 이 목적과 문법을 함께 보면 네 곳이 잘못되었습니다.

1. **`void Car::Car(...)`** — 생성자는 반환형이 없음 → `void`를 제거해 `Car::Car(...)`.
2. **정적 멤버 `sum`의 정의 누락** — `static int sum;`은 선언일 뿐이므로 클래스 밖에서 한 번 정의·초기화해야 함 → `int Car::sum = 0;`.
3. **인스턴스 개수가 세어지지 않음** — 생성자에서 `sum`을 증가시켜야 개수가 유지됨 → 생성자에 `sum++;` 추가.
4. **`Car::showSum()` 정적 호출** — 객체 없이 클래스 이름으로 호출하므로 `showSum`은 정적 함수여야 함 → 선언을 `static void showSum();`으로.

**수정된 코드**

```cpp
#include <iostream>
using namespace std;

class Car {
public:
    static int sum;
    Car(int n, double g);
    void show();
    static void showSum();     // ④ 정적 함수로

private:
    int num;
    double gas;
};

int Car::sum = 0;              // ② 정적 멤버 정의·초기화

Car::Car(int n, double g) {    // ① void 제거
    num = n;
    gas = g;
    sum++;                     // ③ 인스턴스 개수 증가
}

void Car::showSum() {
    cout << sum << endl;
}

void Car::show() {
    cout << num << " " << gas << endl;
}

int main() {
    Car car1(1234, 20.5);
    Car car2(4567, 30.5);
    Car::showSum();
}
```

두 개의 `Car`가 생성되므로 출력은

$$\boxed{2}$$

👉 [실습(C++)에서 확인하기](./lab-11)
:::
