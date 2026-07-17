# 문제 11 · 실습 — `Car` 클래스 오류 수정

수정본을 실행하여 생성된 인스턴스 개수(`2`)가 출력되는지 확인합니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Car {
public:
    static int sum;
    Car(int n, double g);
    void show();
    static void showSum();     // 정적 함수로

private:
    int num;
    double gas;
};

int Car::sum = 0;              // 정적 멤버 정의·초기화

Car::Car(int n, double g) {    // 생성자: void 제거
    num = n;
    gas = g;
    sum++;                     // 인스턴스 개수 증가
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

</CppRunner>

출력은 `2` 입니다. 생성자가 호출될 때마다 `sum`이 증가하여, 두 개의 `Car`가 만들어졌음을 보여 줍니다.

👉 [문제 11로 돌아가기](./problem-11)
