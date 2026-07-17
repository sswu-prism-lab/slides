# 문제 9 · 실습 — 임의 위치에 정수 삽입

`rand() % size`로 배열 크기보다 작은 위치를 고른 뒤, 뒤쪽 원소를 밀어 값을 끼워넣습니다. `srand(1)`로 결정적으로 실행합니다.

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

// arr(원소 size개, 용량 충분)의 임의 위치에 value 삽입, 새 크기 반환
int insertAtRandom(int arr[], int size, int value) {
    int pos = rand() % size;             // 0 ~ size-1 중 임의 위치
    for (int i = size; i > pos; i--)     // pos 이후를 한 칸씩 뒤로
        arr[i] = arr[i - 1];
    arr[pos] = value;                    // 임의 위치에 삽입
    cout << "삽입 위치: " << pos << endl;
    return size + 1;
}

int main() {
    srand(1);                            // 결정적 실행
    int arr[10] = {10, 20, 30, 40, 50};
    int size = 5;
    size = insertAtRandom(arr, size, 99);
    for (int i = 0; i < size; i++) cout << arr[i] << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

출력은
```
삽입 위치: 3
10 20 30 99 40 50
```
입니다. (위치 `3`은 `srand(1)` 기준으로 결정적입니다.)

👉 [문제 9로 돌아가기](./problem-09)
