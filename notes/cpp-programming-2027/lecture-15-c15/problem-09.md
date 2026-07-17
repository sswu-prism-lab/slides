# 문제 9 · 임의 위치에 정수 삽입

::: info 문제 9 [3점]
아래 문제를 풀기 위한 코드 혹은 의사알고리즘<span class="gloss">pseudo-algorithm</span>을 작성하세요.

> 임의의 정수로 이루어진 배열, 임의의 정수를 입력으로 받아, 배열의 크기보다 작은 임의<span class="gloss">random</span>의 위치에 정수를 끼워넣는 함수
:::

::: details 풀이 및 해설
"배열의 크기보다 작은 임의의 위치"란 `0` 이상 `size` 미만의 무작위 인덱스를 뜻하므로 `rand() % size`로 고릅니다. 삽입은 그 위치부터 뒤쪽 원소들을 **한 칸씩 뒤로 밀어** 자리를 만든 다음, 그 자리에 값을 넣습니다. 배열에는 원소가 늘어날 여유 공간이 있어야 합니다.

```cpp
#include <cstdlib>   // rand()

// arr: 원소 size개가 들어있는 배열(용량은 충분)
// value: 끼워넣을 정수
// 반환값: 삽입 후의 새 크기
int insertAtRandom(int arr[], int size, int value) {
    int pos = rand() % size;             // 0 ~ size-1 중 임의 위치
    for (int i = size; i > pos; i--) {   // pos 이후 원소를 뒤로 이동
        arr[i] = arr[i - 1];
    }
    arr[pos] = value;                    // 임의 위치에 삽입
    return size + 1;
}
```

핵심 아이디어(의사알고리즘)

1. `pos = rand() % size` 로 삽입 위치를 무작위로 정한다. (항상 `size`보다 작음)
2. 마지막 원소부터 `pos`까지, 각 원소를 오른쪽으로 한 칸 옮긴다.
3. 비워진 `arr[pos]`에 `value`를 넣는다.
4. 배열 크기가 1 늘어난다.

👉 [실습(C++)에서 확인하기](./lab-09)
:::
