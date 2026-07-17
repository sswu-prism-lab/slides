# 문제 15 · 스택 클래스 UML과 구현

::: info 문제 15 [5점]
아래 스택<span class="gloss">stack</span> 자료구조에 대한 설명을 토대로, 스택을 클래스로 정의하기 위한 UML<span class="gloss">Unified Modelling Language</span> 다이어그램을 그린 후, 스택 클래스에 대한 코드 혹은 의사알고리즘을 작성하시오.

> 스택은 임의의 배열이며, 삽입과 삭제가 반드시 하나의 위치에서만 이루어지는 자료구조이다. 스택은 먼저 입력된 요소가 나중에 출력되는 후입선출<span class="gloss">last in, first out</span>의 특성을 가진다. 스택에는 다음 5가지 행동<span class="gloss">action</span>이 들어갈 수 있다.
> 1. 새로운 요소를 입력하는 `push`
> 2. 요소를 제거하는 `pop`
> 3. 다음에 제거될 요소를 출력하는 `top`
> 4. 현재 스택의 사이즈를 반환하는 `getSize`
> 5. 현재 스택이 비어있는지 여부를 반환하는 `isEmpty`
:::

::: details 풀이 및 해설
### UML 클래스 다이어그램

배열 `arr`과 최상단 인덱스 `topIndex`를 비공개(`-`) 필드로 두고, 5가지 행동을 공개(`+`) 메서드로 둡니다. (`-`는 private, `+`는 public을 뜻합니다.)

```
+------------------------------------+
|               Stack                |
+------------------------------------+
| - arr : int[]                      |
| - topIndex : int                   |
+------------------------------------+
| + push(value : int) : void         |
| + pop() : int                      |
| + top() : int                      |
| + getSize() : int                  |
| + isEmpty() : bool                 |
+------------------------------------+
```

| 구분 | 이름 | 설명 |
| --- | --- | --- |
| 필드 | `arr` | 요소를 담는 배열 |
| 필드 | `topIndex` | 최상단 요소의 인덱스(비었으면 `-1`) |
| 메서드 | `push(value)` | `topIndex`를 1 늘리고 그 자리에 값 저장 |
| 메서드 | `pop()` | 최상단 요소를 반환하고 `topIndex`를 1 줄임 |
| 메서드 | `top()` | 최상단 요소를 반환(제거하지 않음) |
| 메서드 | `getSize()` | 요소 개수 = `topIndex + 1` 반환 |
| 메서드 | `isEmpty()` | `topIndex == -1` 여부 반환 |

### 스택 클래스 코드

삽입·삭제가 모두 `topIndex` 한 위치에서만 일어나므로 후입선출이 자연스럽게 성립합니다.

```cpp
class Stack {
private:
    int arr[100];      // 요소 배열
    int topIndex;      // 최상단 인덱스, 비었으면 -1
public:
    Stack() : topIndex(-1) {}

    void push(int value) { arr[++topIndex] = value; }  // 넣고 위로
    int  pop()           { return arr[topIndex--]; }   // 빼고 아래로
    int  top()           { return arr[topIndex]; }     // 최상단 확인
    int  getSize()       { return topIndex + 1; }
    bool isEmpty()       { return topIndex == -1; }
};
```

`push` → `pop` 순서로 여러 값을 넣고 빼면 **가장 나중에 넣은 값이 가장 먼저** 나옵니다.

👉 [실습(C++)에서 확인하기](./lab-15)
:::
