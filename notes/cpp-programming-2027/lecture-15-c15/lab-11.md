# 문제 11 · 실습 — Person 클래스 오류

`person1 -> printInfo;`에 호출 괄호 `()`를 붙인 수정본입니다.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

class Person {
public:
    string name;
    int age;

    Person(string name, int age) {
        this->name = name;
        this->age = age;
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
    Person* person1 = new Person("Wonjun", 28);
    person1->printInfo();   // printInfo -> printInfo()
    delete person1;
    return 0;
}
```

</CppRunner>

출력은 `이름: Wonjun, 나이: 28, 사람 수: 1` 입니다.

👉 [문제 11로 돌아가기](./problem-11)
