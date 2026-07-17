# 문제 14 · 클래스의 역할

::: info 문제 14 [4점]
아래 문제를 읽고, 각 문제의 제시어에 대한 설명을 예시와 함께 서술하시오.

C++에서 클래스<span class="gloss">class</span>의 역할에 대해 서술하시오.
:::

::: details 풀이 및 해설
**클래스**는 서로 관련된 **데이터(멤버 변수)** 와 그 데이터를 다루는 **함수(멤버 함수)** 를 하나로 묶어 새로운 **사용자 정의 자료형**을 만드는 설계 틀입니다. 객체 지향 프로그래밍의 기본 단위로, 다음과 같은 역할을 합니다.

- **캡슐화<span class="gloss">encapsulation</span>**: 데이터와 그 데이터를 조작하는 함수를 한 단위로 묶습니다.
- **정보 은닉<span class="gloss">information hiding</span>**: `private` 멤버로 내부 데이터를 감추고, `public` 멤버 함수(인터페이스)를 통해서만 접근하게 하여 잘못된 사용을 막습니다.
- **추상화·재사용**: 하나의 클래스로부터 여러 **객체(인스턴스)** 를 찍어낼 수 있어, 같은 구조를 반복 정의하지 않고 재사용합니다. 이는 현실의 개념(자동차, 계좌 등)을 코드로 모델링하는 틀이 됩니다.

**예시**

```cpp
class Student {
private:
    string name;
    int score;        // 외부에서 직접 못 건드림
public:
    Student(string n, int s) : name(n), score(s) {}
    void setScore(int s) {          // 유효성 검사를 거친 안전한 변경
        if (s >= 0 && s <= 100) score = s;
    }
    void show() const { cout << name << ": " << score << endl; }
};
```

`score`는 `private`이라 직접 대입할 수 없고, `setScore`를 통해서만 0~100 범위로 안전하게 바뀝니다. 이렇게 데이터와 동작을 묶고 접근을 통제하는 것이 클래스의 핵심 역할입니다.

👉 [실습(C++)에서 확인하기](./lab-14)
:::
