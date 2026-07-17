# 문제 8 · 실습 — 개행까지 문자 입력받기

`cin.get(c)`로 문자를 하나씩 읽어 개행이나 입력 끝을 만날 때까지 배열에 담습니다. 입력으로 `Hello`를 줍니다.

<CppRunner stdin="Hello">

```cpp
#include <iostream>
using namespace std;

// 개행('\n')이나 입력 끝을 만날 때까지 문자를 하나씩 배열에 저장
int inputChars(char list[], int capacity) {
    int count = 0;
    char c;
    while (count < capacity && cin.get(c)) {
        if (c == '\n') break;      // 개행이면 종료
        list[count++] = c;         // 차례대로 저장
    }
    return count;
}

int main() {
    char list[100];
    int n = inputChars(list, 100);
    cout << "입력된 문자 수: " << n << endl;
    cout << "저장된 내용: ";
    for (int i = 0; i < n; i++) cout << list[i];
    cout << endl;
    return 0;
}
```

</CppRunner>

출력은
```
입력된 문자 수: 5
저장된 내용: Hello
```
입니다. 입력에 개행이 있으면 그 지점에서 저장을 멈춥니다.

👉 [문제 8로 돌아가기](./problem-08)
