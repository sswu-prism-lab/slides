# 문제 11 · Person 클래스 오류

::: info 문제 11 [3점]
아래 문제를 읽고, 코드에 오류가 있다면 수정하세요. 오류가 없다면 '오류 없음'이라고 서술하세요.

> 아래는 주소록 코드의 초기 버전으로, 이름, 나이를 저장하고 저장된 사람 수를 기록하는 코드이다.

```cpp
#include <iostream>
#include <string>
using namespace std;

class Person {
public:
    string name;
    int age;

    Person(string name, int age) {
        this -> name = name;
        this -> age = age;
        numPerson++;
    }

    void printInfo() {
        cout << "이름: " << name
        << ", 나이: " << age
        << ", 사람 수: " << numPerson << endl;
    }
private:
    static int numPerson;
};

int Person::numPerson = 0;

int main() {
    Person *person1 = new Person("Wonjun", 28);
    person1 -> printInfo;
    delete person1;
}
```
:::

::: details 풀이 및 해설
**오류 있음 — 멤버 함수 호출에 괄호 `()`가 빠짐.**

`main`의 `person1 -> printInfo;`는 함수를 **호출**하지 않고 멤버 함수의 이름만 쓴 문장입니다. 호출하려면 인자 목록을 뜻하는 소괄호 `()`가 반드시 있어야 합니다.

```cpp
int main() {
    Person *person1 = new Person("Wonjun", 28);
    person1->printInfo();   // printInfo -> printInfo()
    delete person1;
}
```

이렇게 고치면 `printInfo()`가 실행되어 `이름: Wonjun, 나이: 28, 사람 수: 1`이 출력됩니다.

나머지 부분은 올바릅니다. `this->name = name;`로 매개변수와 멤버를 구분한 점, 정적 멤버 `numPerson`을 클래스 밖에서 `int Person::numPerson = 0;`으로 정의·초기화한 점, `private` 정적 멤버를 멤버 함수 안에서 접근한 점 모두 정상입니다.

👉 [실습(C++)에서 확인하기](./lab-11)
:::
