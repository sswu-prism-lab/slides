# 문제 14 · 얕은 복사와 깊은 복사

::: info 문제 14 [4점]
아래 제시어에 대한 설명을 예시와 함께 서술하시오.

> 얕은 복사<span class="gloss">shallow copy</span>와 깊은 복사<span class="gloss">deep copy</span>
:::

::: details 풀이 및 해설
포인터로 동적 메모리를 가리키는 객체를 복사할 때 두 방식이 갈립니다.

**얕은 복사**는 멤버 값(포인터 변수 자체)을 그대로 복사합니다. 포인터가 담고 있는 **주소만** 복사되므로, 원본과 복사본이 **같은 메모리를 공유**하게 됩니다. C++이 기본으로 제공하는 복사 생성자·대입 연산자가 이렇게 동작합니다. 문제점은 (1) 한쪽에서 내용을 바꾸면 다른 쪽도 바뀌고, (2) 소멸자에서 같은 메모리를 두 번 `delete`하여 오류(이중 해제)가 날 수 있다는 것입니다.

**깊은 복사**는 **새로운 메모리를 따로 할당한 뒤 내용을 복사**합니다. 원본과 복사본이 서로 독립된 메모리를 가지므로 위 문제가 없습니다. 동적 자원을 가진 클래스는 복사 생성자를 직접 정의해 깊은 복사를 구현해야 합니다.

```cpp
class DeepArray {
public:
    int* data;
    int size;
    DeepArray(int s) : size(s) { data = new int[size]; }

    // 깊은 복사 생성자: 새 메모리를 할당해 값을 옮김
    DeepArray(const DeepArray& other) : size(other.size) {
        data = new int[size];                       // 별도 메모리
        for (int i = 0; i < size; i++)
            data[i] = other.data[i];                // 값 복사
    }
    ~DeepArray() { delete[] data; }
};
```

- 얕은 복사라면 `b = a` 후 `b.data`와 `a.data`가 같은 주소 → `b`를 바꾸면 `a`도 바뀌고 소멸 시 이중 해제.
- 위처럼 깊은 복사를 하면 `a`와 `b`가 독립적이어서 서로 영향을 주지 않습니다.

👉 [실습(C++)에서 확인하기](./lab-14)
:::
