# 기초 · 재귀 · C++ · 복잡도

중간고사 범위의 출발점입니다. 재귀 프로그래밍의 규칙, 자료구조를 C++로 구현하기 위한 클래스·포인터 문법, 알고리즘의 성능을 따지는 복잡도 분석, 그리고 이 모든 것을 감싸는 추상 데이터 타입(ADT)과 표준 템플릿 라이브러리(STL)를 차례로 정리합니다.

## 재귀 프로그래밍의 규칙

재귀 프로그래밍<span class="gloss">recursive programming</span>은 함수가 자기 자신을 다시 호출하여 문제를 푸는 방식입니다. 올바르게 동작하는 재귀는 다음 4가지 규칙을 지켜야 합니다.

1. **기본 상태<span class="gloss">base cases</span>.** 재귀 호출 없이 곧바로 풀 수 있는 기본 상태를 반드시 정의해야 한다.
2. **진행<span class="gloss">making progress</span>.** 재귀 호출이 진행됨에 따라, 반드시 기본 상태를 향해 계속 나아가야 한다.
3. **설계 규칙<span class="gloss">design rule</span>.** 모든 재귀 호출은 (일단) 올바르게 작동한다고 가정하고 설계한다.
4. **복리 규칙<span class="gloss">compound interest rule</span>.** 불필요하게 재귀 프로그래밍을 사용해서는 안 된다(같은 계산을 중복해서 되풀이하지 말 것).

## C++ 클래스 및 포인터 문법

자료구조를 직접 구현하려면 C++의 클래스와 포인터 문법이 바탕이 됩니다. 아래 예시에서 클래스<span class="gloss">class</span> 이름은 `IntCell`이며, 하나의 정수를 저장하는 메모리 셀을 흉내 냅니다.

- `public` 아래의 멤버<span class="gloss">member</span>들은 클래스 바깥에서 접근할 수 있는 반면, `private` 멤버들은 클래스 내부에서만 접근할 수 있다.
- `public` 멤버 중 클래스와 이름이 똑같은 함수 2개는 각각 인수 없는 생성자<span class="gloss">constructor</span>와 인수 있는 생성자이며, 틸드<span class="gloss">tilde</span>(`~`) 뒤에 이름이 같은 함수는 소멸자이다.
- 생성자는 클래스를 실체화<span class="gloss">instantiation</span>할 때 실행되고, 소멸자는 프로그램이 종료되거나 실체화된 객체<span class="gloss">object</span>를 명시적으로 제거할 때 실행된다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class IntCell { // simulating an integer memory cell
public:
    IntCell() { // constructor
        storedValue = 0;
    }
    IntCell(int initialValue) { // constructor with parameter
        storedValue = initialValue;
    }
    ~IntCell() {} // destructor
    int read() { // return the stored value
        return storedValue;
    }
    void write(int x) { // change the stored value to x
        storedValue = x;
    }
private:
    int storedValue;
};

int main() {
    IntCell* m;          // * indicates that m is a pointer
    m = new IntCell{0};  // dynamic allocation
    m->write(5);
    cout << "Cell contents: " << m->read() << endl;
    delete m;            // garbage collection
    return 0;
}
```

</CppRunner>

위의 두 생성자는 초기화 리스트<span class="gloss">initialization list</span>를 사용하여 다음과 같이 하나로 줄여서 표현할 수도 있습니다. 이때 생성자는 `initialValue`라는 값을 입력으로 받으며, 입력이 따로 지정되지 않으면 `0`이 부여되고, `storedValue`에 `initialValue`가 할당됩니다.

```cpp
IntCell(int initialValue = 0): storedValue{initialValue} {}
```

### 포인터와 동적 메모리 할당

C++에서 포인터<span class="gloss">pointer</span>는 다른 객체가 메모리 상에 존재하는 주소<span class="gloss">address</span>를 저장하는 변수입니다. 위 예시의 `IntCell* m;`은 `IntCell` 객체의 주소를 담는 포인터 변수를 선언한 것입니다. 포인터가 왜 필요한지는 메모리 관리와 맞닿아 있습니다.

- 배열 등 임의의 변수를 선언할 때 고정된 크기로 선언하면, 변수가 실제로 다 쓰이지 않을 경우 낭비되는 공간이 생긴다.
- 고정 배열을 포함한 대부분의 일반 변수는 스택<span class="gloss">stack</span>에 저장되는데, 이 크기를 초과하면 스택 오버플로우<span class="gloss">stack overflow</span>가 발생하여 운영체제가 프로그램을 강제로 종료한다.
- 동적 메모리 할당<span class="gloss">dynamic memory allocation</span>은 프로그램 실행 중에 필요한 메모리를 운영체제에 요청하는 방식으로, 스택이 아니라 힙<span class="gloss">heap</span>처럼 운영체제가 관리하는 훨씬 더 큰 공간에서 할당된다.
- `new`를 사용하여 변수를 동적 할당하고, `delete`를 사용하여 할당된 메모리를 다시 운영체제에 반환한다.

## 알고리즘 분석

알고리즘의 실행 시간 $T(N)$을 다른 함수 $f(N)$과 견주어 그 성장률<span class="gloss">growth rate</span>을 표현하는 방법에는 다음 4가지가 있습니다.

- $T(N)=\mathcal{O}(f(N))$ — 양의 상수<span class="gloss">constants</span> $c, n_0$가 존재하여 $N\geq n_0$일 때 $T(N)\leq c\,f(N)$이면 성립. 즉 $T(N)$의 성장률이 $f(N)$의 성장률보다 작거나 같음을 의미한다. 이때 $f(N)$은 $T(N)$의 상계<span class="gloss">upper bound</span>이고, 반대로 $f(N)=\Omega(T(N))$이므로 $T(N)$은 $f(N)$의 하계<span class="gloss">lower bound</span>이다.
- $T(N)=\Omega(g(N))$ — 양의 상수 $c, n_0$가 존재하여 $N\geq n_0$일 때 $T(N)\geq c\,g(N)$이면 성립(하계).
- $T(N)=\Theta(h(N))$ — $T(N)=\mathcal{O}(h(N))$이면서 동시에 $T(N)=\Omega(h(N))$일 때, 그리고 그때에만 성립(상·하계가 같음).
- $T(N)=o(p(N))$ — 임의의 양의 상수 $c$에 대해 어떤 $n_0$가 존재하여 $N>n_0$일 때 $T(N)<c\,p(N)$이면 성립(엄격히 더 느린 성장).

### 빅-오 표기법

실제 알고리즘 분석에서는 상계를 나타내는 빅-오 표기법<span class="gloss">big-Oh notation; $\mathcal{O}(\cdot)$</span>을 주로 사용합니다.

- 예를 들어 $g(N)=2N^2$이라면 $g(N)=\mathcal{O}(N^4)$, $g(N)=\mathcal{O}(N^3)$, $g(N)=\mathcal{O}(N^2)$이 모두 기술적으로는 올바르지만, 가장 촘촘한 마지막 옵션 $\mathcal{O}(N^2)$이 가장 좋은 답이다.
- 일반적으로 알고리즘 분석은 따로 언급되지 않는 한 **최악의 경우**에 대해 수행한다.

엄밀한 수학적 정의를 매번 그대로 적용하기보다는, 알려진 몇 가지 결과를 토대로 빠르게 분석할 수 있습니다.

- 단일 `for`문은 $\mathcal{O}(N)$이며, 중첩 `for`문<span class="gloss">nested for loop</span>은 $\mathcal{O}(N^2)$, $\mathcal{O}(N^3)$처럼 점점 늘어난다. 반면 나란히 있는 연속 `for`문<span class="gloss">consecutive for loop</span>은 복잡도<span class="gloss">complexity</span>가 변하지 않는다(더 큰 쪽이 지배).
- 조건문은 분기에 따라 결과가 달라질 수 있으며, 재귀 프로그램도 경우의 수를 따져 보아야 한다.

아래 실습은 중첩 `for`문의 안쪽 연산 횟수가 입력 크기 $N$에 대해 $N^2$으로 늘어나는 것을 직접 세어 보여 줍니다. $N$을 2배로 키우면 연산 횟수가 4배가 되는 것을 확인해 보세요.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    int sizes[] = {1, 2, 4, 8};
    for (int N : sizes) {
        long count = 0;
        for (int i = 0; i < N; i++)      // O(N)
            for (int j = 0; j < N; j++)  // O(N) -> 합쳐서 O(N^2)
                count++;
        cout << "N=" << N << " -> inner ops = " << count << endl;
    }
    return 0;
}
```

</CppRunner>

## 추상 데이터 타입과 표준 템플릿 라이브러리

- 추상 데이터 타입<span class="gloss">abstract data type; ADT</span>은 연산<span class="gloss">operation</span>들과 함께 있는 객체<span class="gloss">object</span>들의 집합이다.
- ADT는 수학적 추상화이며, 그 정의에는 연산의 집합이 실제로 **어떻게 구현되는지**에 대한 언급이 없다. 즉 "무엇을 하는가"만 규정하고 "어떻게 하는가"는 감춘다.
- C++ 언어는 자주 쓰이는 자료구조 ADT의 구현을 표준으로 포함하며, 이를 표준 템플릿 라이브러리<span class="gloss">standard template library; STL</span>라고 한다.
- 보통 STL에 내장되어 있는 자료구조를 컬렉션<span class="gloss">collection</span> 또는 컨테이너<span class="gloss">container</span>라고 부른다.

가장 기본적인 컨테이너인 `vector`(가변 크기 배열)를 예로 들어, ADT가 제공하는 연산만으로 자료를 다루는 모습을 실습으로 확인해 봅니다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v;               // 크기가 자동으로 늘어나는 배열 컨테이너
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    cout << "size: " << v.size() << endl;
    cout << "v[1]: " << v[1] << endl;
    v.pop_back();                // 마지막 원소 제거
    cout << "after pop_back, size: " << v.size() << endl;
    return 0;
}
```

</CppRunner>
