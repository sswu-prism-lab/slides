# 문제 8 · 개행까지 문자 입력받기

::: info 문제 8 [3점]
아래 문제를 풀기 위한 코드 혹은 의사알고리즘<span class="gloss">pseudo-algorithm</span>을 작성하세요.

> 사용자가 개행(`'\n'`)할 때까지 문자를 하나씩 입력받아 배열<span class="gloss">list</span>에 차례대로 입력하는 함수<span class="gloss">function</span>
:::

::: details 풀이 및 해설
문자를 **하나씩** 읽어야 하므로 `cin.get(char)`을 사용합니다. 읽은 문자가 개행 `'\n'`이면 멈추고, 아니면 배열의 다음 칸에 저장합니다. 배열 용량을 넘지 않도록 개수도 함께 관리합니다.

```cpp
// list: 저장할 배열, capacity: 배열 용량
// 반환값: 실제 입력된 문자 개수
int inputChars(char list[], int capacity) {
    int count = 0;
    char c;
    while (count < capacity && cin.get(c)) {  // 문자를 하나씩 입력
        if (c == '\n') break;                 // 개행이면 종료
        list[count] = c;                      // 차례대로 저장
        count++;
    }
    return count;
}
```

핵심 아이디어(의사알고리즘)

1. `count`를 0으로 둔다.
2. 문자 `c`를 하나 입력받는다.
3. `c`가 `'\n'`이면 반복을 멈춘다.
4. 아니면 `list[count]`에 `c`를 저장하고 `count`를 1 늘린다.
5. 배열이 가득 차거나 입력이 끝날 때까지 2\~4를 반복한다.

👉 [실습(C++)에서 확인하기](./lab-08)
:::
