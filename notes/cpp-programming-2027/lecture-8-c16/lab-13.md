# 문제 13 · 실습 — `for` 반복 범위 오류 수정

수정본(`i < 10`)은 숫자를 정확히 10개만 읽습니다. 예시 입력은 10개의 수 `3 -2 5 -8 1 -4 7 -6 2 -9` 입니다. (원본의 `i <= 10`은 11개를 요구했습니다.)

<CppRunner stdin="3 -2 5 -8 1 -4 7 -6 2 -9">

```cpp
#include <iostream>
using namespace std;

int main() {
    int number, pSum = 0, nSum = 0;
    cout << "10개의 숫자를 입력하세요: " << endl;
    for (int i = 0; i < 10; ++i) {     // 수정: i <= 10 → i < 10
        cin >> number;
        if (number > 0)
            pSum += number;
        else
            nSum += number;
    }
    cout << "양수의 합: " << pSum << endl;
    cout << "음수의 합: " << nSum << endl;
    return 0;
}
```

</CppRunner>

입력 `3 -2 5 -8 1 -4 7 -6 2 -9`에 대한 출력은 다음과 같습니다.

```
10개의 숫자를 입력하세요: 
양수의 합: 18
음수의 합: -29
```

양수 `3+5+1+7+2 = 18`, 음수 `-2-8-4-6-9 = -29`로 정확히 10개를 읽어 합산합니다.

👉 [문제 13으로 돌아가기](./problem-13)
