# 문제 14 · 실습 — 클래스의 역할

클래스가 데이터와 함수를 묶고(캡슐화) `private` 필드를 보호하는(정보 은닉) 모습을 확인합니다.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

// 데이터(name, score)와 그를 다루는 함수를 하나로 묶은 설계 틀
class Student {
private:
    string name;
    int score;      // 외부에서 직접 접근 불가
public:
    Student(string n, int s) : name(n), score(s) {}
    void setScore(int s) {              // 유효성 검사를 거친 안전한 변경
        if (s >= 0 && s <= 100) score = s;
    }
    void show() const {
        cout << name << ": " << score << "점" << endl;
    }
};

int main() {
    Student a("김철수", 85);
    a.show();
    a.setScore(95);
    a.show();
    a.setScore(200);   // 범위를 벗어난 값 → 무시됨
    a.show();
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다. `200`은 범위를 벗어나 무시되므로, 잘못된 값으로부터 데이터가 보호됩니다.

```
김철수: 85점
김철수: 95점
김철수: 95점
```

👉 [문제 14로 돌아가기](./problem-14)
