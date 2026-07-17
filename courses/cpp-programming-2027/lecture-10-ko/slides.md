---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 10 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-10/
---
<style>
.dark .slidev-page,
.dark .slidev-layout,
.dark .slide-container,
.dark #slide-content,
.dark .slidev-nav-go-container {
  background: #000000 !important;
}
.tikz-fig {
  background: #ffffff;
  border-radius: 8px;
  padding: 0.4rem 0.6rem;
}
</style>

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.png" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">C++ 프로그래밍</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">10주차: 배열</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">2027년 가을학기</p>
</div>

---
layout: prism
heading: "요약: 함수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 함수는 [반환값 유형]{.hl}, [함수 이름]{.hl}, [매개변수]{.hl}, [함수 몸체]{.hl}로 구성됩니다.
  - [함수 헤더]{.hl}에서 반환값 유형, 함수 이름, 매개변수를 지정합니다.
  - 함수 헤더에 선언된 변수를 [형식 매개변수]{.hl}라 하며, 호출자가 넘겨주는 값을 [인수]{.hl}라고 합니다.

- [반환값 유형]{.hl}은 함수가 반환하는 값의 데이터 유형입니다.
  - [값 반환 함수]{.hl}는 값을 반환합니다.
  - [void 함수]{.hl}는 아무것도 반환하지 않습니다(예: `srand`).

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w10/cpp-w10-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "요약: void 함수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [void 함수]{.hl}는 값을 반환하지 않습니다.

- `void` 함수에는 `return`문이 필요하지 않지만, 함수의 실행을 끝내고 호출자로 되돌아가기 위해 `return;` 만 단독으로 사용할 수 있습니다.

- `printGrade`는 아무것도 반환하지 않으면서 점수에 해당하는 등급을 출력합니다.

</div>
<div>

<CppRunner stdin="85">

```cpp
#include <iostream>
using namespace std;

// Print grade for the score
void printGrade(double score) {
    if (score >= 90.0)      cout << 'A' << endl;
    else if (score >= 80.0) cout << 'B' << endl;
    else if (score >= 70.0) cout << 'C' << endl;
    else if (score >= 60.0) cout << 'D' << endl;
    else                    cout << 'F' << endl;
}

int main() {
    cout << "Enter a score: ";
    double score;
    cin >> score;
    cout << "The grade is ";
    printGrade(score);
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "요약: 값에 의한 인수 전달"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 함수를 호출할 때 인수는 매개변수로 [값에 의해]{.hl} 전달되며, 함수는 그 매개변수 값을 가지고 기능을 수행합니다.

- 인수가 호출된 함수로 전달될 때, 각 인수는 *순서대로* 대응되는 매개변수에 대입됩니다.
  - 이를 [매개변수 순차 결합]{.hl}이라고 합니다.

- 복사본이 전달되므로, 함수 내부에서 매개변수를 변경해도 호출자의 인수에는 영향을 주지 **않습니다**.

---
layout: prism
heading: "요약: 참조에 의한 인수 전달"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 매개변수는 [참조에 의해]{.hl} 전달될 수 있으며, 이때 형식 매개변수는 인수의 [별칭]{.hl}이 됩니다.

- 참조로 전달된 매개변수를 함수 내부에서 변경하면, 인수 값도 함께 변경됩니다.

- [참조 변수]{.hl}는 원 변수에 대한 별칭으로 동작합니다. 데이터 유형 뒤(또는 이름 앞)에 `&`를 붙여 선언합니다.

</div>
<div>

<div style="height: 5rem;"></div>

```cpp
int count = 1;
int& r = count;   // or: int &r = count;

r = 10;           // count is now 10
```

</div>
</div>

---
layout: prism
heading: "요약: 지역, 전역, 정적 지역 변수"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- C++의 변수는 [지역]{.hl}, [전역]{.hl}, [정적 지역]{.hl} 변수로 나뉩니다. 변수의 [범위]{.hl}는 변수가 참조될 수 있는 프로그램의 영역을 의미합니다.
  - 함수 안에서 정의된 변수는 [지역 변수]{.hl}이며, 기본 값이 없습니다.
  - 모든 함수 외부에서 선언되어 파일 내 모든 함수에서 접근 가능한 변수는 [전역 변수]{.hl}이며, 기본 값은 `0`입니다.

- 함수 실행이 완료되면 그 지역 변수는 메모리에서 사라지는데, 이러한 변수들을 [자동 변수]{.hl}라고 합니다.

- 연속되는 호출 사이에 지역 변수의 값을 유지하기 위해, C++는 프로그램이 끝날 때까지 값을 유지하는 [정적 지역 변수]{.hl}를 제공합니다. `static` 키워드를 사용하여 선언합니다.

```cpp
static int x = 1;   // retains its value across calls
```

---
layout: prism
heading: "DIY_W09: 단계적 상세화"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.4em;
}
</style>

- [단계적 상세화]{.hl}는 큰 문제를 다루기 쉬운 작은 부분 문제로 나누는 구현 방법론입니다.

- 각 부분 문제는 함수를 사용하여 구현될 수 있습니다.

- 실제로 대규모 프로젝트를 진행할 때에는 단계적 상세화가 큰 도움이 됩니다.

- 과연 *어떤 측면에서* 도움이 될지 생각해보세요.

---
layout: prism
heading: "배열 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [배열]{.hl}은 많은 데이터의 모음을 저장할 수 있습니다. C++에서 배열은 같은 유형(예: `int`)의 요소를 고정된 개수만큼 연속된 메모리에 저장하는 [자료구조]{.hl}입니다.
  - 배열의 각 [요소]{.hl}는 [인덱스]{.hl}를 사용하여 접근합니다.

- `num0, num1, …, num99`와 같이 100개의 변수를 선언하는 대신, 100개의 요소를 가지는 하나의 배열 `nums`를 선언하고 `nums[0], nums[1], …, nums[99]`처럼 접근하는 것이 훨씬 쉽습니다.

- 배열의 선언은 요소 유형, 식별자, 크기를 지정합니다.

```cpp
elementType arrayName[SIZE];   // SIZE must be a const
```

<div class="sub-item">

초기화 없이 선언하면 요소는 임의의 값을 가집니다.

</div>

---
layout: prism
heading: "배열 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 초기화된 배열의 요소에 값을 할당하려면 다음 구문을 사용합니다.

```cpp
arrayName[index] = value;
```

- 선언과 값을 단축 형태로 함께 작성할 수도 있습니다.

</div>
<div>

```cpp
double myList[3];
myList[0] = 0.1;
myList[1] = 2.9;
myList[2] = -1.4;
```

<div style="height: 1.5rem;"></div>

```cpp
// shorthand
elementType arrayName[SIZE]
    = {value0, ..., valuek};

double myList[3] = {0.1, 2.9, -1.4};
```

</div>
</div>

---
layout: prism
heading: "배열 (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 선언과 초기화는 *하나의* 문장에서 이루어져야 합니다.

- 선언과 초기화를 동시에 할 때는 배열 크기를 [생략]{.hl}할 수 있습니다.

- 배열의 *일부분*만 초기화할 수도 있으며, 나머지 요소는 `0`으로 설정됩니다.

</div>
<div>

```cpp
double myList[3];
myList = {0.1, 2.9, -1.4}; // syntax error

// size may be omitted
double myList[] = {0.1, 2.9, -1.4};

// partial initialization
double myList[3] = {0.1};
// elements 2 and 3 hold 0
```

</div>
</div>

---
layout: prism
heading: "배열 처리 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 배열 요소는 `for`문으로 처리하는 경우가 많습니다.

- 자주 쓰이는 연산:
  - 입력 값으로 배열 초기화,
  - 임의의 값으로 초기화(`rand() % 100`),
  - 요소 출력.

</div>
<div>

<CppRunner stdin="1 2 3 4 5 6 7 8 9 10">

```cpp
#include <iostream>
using namespace std;

int main() {
    const int ARRAY_SIZE = 10;
    double myList[ARRAY_SIZE];

    // Initialize array from input
    cout << "Enter " << ARRAY_SIZE << " values: ";
    for (int i = 0; i < ARRAY_SIZE; i++)
        cin >> myList[i];

    // Print the array elements
    for (int i = 0; i < ARRAY_SIZE; i++)
        cout << myList[i] << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "배열 처리 (2/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 그 밖에 자주 쓰이는 배열 연산:
  - 배열을 요소 단위로 복사,
  - 모든 요소의 합,
  - 최댓값 구하기,
  - 최댓값 요소의 *가장 작은* 인덱스 구하기.

- *가장 큰* 인덱스를 구하려면 어떻게 해야 할까요?

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int ARRAY_SIZE = 6;
    double myList[ARRAY_SIZE] = {2, 9, 5, 4, 8, 9};
    double list[ARRAY_SIZE];

    for (int i = 0; i < ARRAY_SIZE; i++)   // copy
        list[i] = myList[i];

    double total = 0;                      // sum
    for (int i = 0; i < ARRAY_SIZE; i++)
        total += myList[i];

    double max = myList[0];                // max + index
    int indexOfMax = 0;
    for (int i = 1; i < ARRAY_SIZE; i++)
        if (myList[i] > max) {
            max = myList[i];
            indexOfMax = i;
        }

    cout << "Sum = " << total << endl;
    cout << "Max = " << max << endl;
    cout << "Smallest index of max = " << indexOfMax << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "배열 처리 (3/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [섞기]{.hl}: `i`를 마지막 인덱스부터 `1`까지 감소시키며, `[0, i]` 범위의 임의의 `j`를 골라 `myList[i]`와 `myList[j]`를 교환합니다.

- [시프트 이동]{.hl}: 모든 요소를 한 칸씩 왼쪽으로 이동시키고, 첫 요소를 비워진 마지막 자리로 옮깁니다.

```cpp
// shuffle (sketch)
for (int i = ARRAY_SIZE - 1; i > 0; i--) {
    int j = rand() % (i + 1);
    swap(myList[i], myList[j]);
}
```

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int ARRAY_SIZE = 6;
    double myList[ARRAY_SIZE] = {1, 2, 3, 4, 5, 6};

    // Shift elements left; wrap first element to the last
    double temp = myList[0];        // retain the first element
    for (int i = 1; i < ARRAY_SIZE; i++)
        myList[i - 1] = myList[i];
    myList[ARRAY_SIZE - 1] = temp;  // fill in the last position

    cout << "After left shift: ";
    for (int i = 0; i < ARRAY_SIZE; i++)
        cout << myList[i] << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: 함수로 배열 전달 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 배열 인수가 함수로 전달될 때, 배열의 [시작 주소]{.hl}가 함수의 배열 매개변수로 전달됩니다.

- 매개변수는 길이 정보를 담지 않으므로, 크기는 별도로 전달합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void printArray(int list[], int arraySize); // prototype

int main() {
    int numbers[5] = {1, 4, 3, 6, 8};
    printArray(numbers, 5);   // invoke the function
    cout << endl;
    return 0;
}

void printArray(int list[], int arraySize) {
    for (int i = 0; i < arraySize; i++)
        cout << list[i] << " ";
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: 함수로 배열 전달 (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 스칼라 인수(`x`)는 [값에 의해]{.hl} 전달됩니다. `m` 내부에서 매개변수를 변경해도 `x`는 바뀌지 **않습니다**.

- 배열 인수(`y`)는 매개변수와 저장 공간을 공유하므로, `numbers[0] = 5555`는 `y[0]`을 실제로 변경 **합니다**.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void m(int, int[]);

int main() {
    int x = 1;      // a single int value
    int y[10];      // an array of int values
    y[0] = 1;       // initialize y[0]

    m(x, y);        // invoke m with x and y

    cout << "x is " << x << endl;
    cout << "y[0] is " << y[0] << endl;
    return 0;
}

void m(int number, int numbers[]) {
    number = 1001;      // new value to number
    numbers[0] = 5555;  // new value to numbers[0]
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: const로 배열 인수 보호하기"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 함수가 배열 매개변수의 값을 변경하지 못하게 하려면, 매개변수를 [`const`]{.hl} 배열 매개변수로 선언합니다.

- `const` 배열 매개변수를 변경하려는 시도는 컴파일러가 잡아냅니다.
  - `list[0] = 100;`의 주석을 해제하면 *컴파일 오류*가 발생합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void p(const int list[], int arraySize) {
    // list[0] = 100;  // Compile error: list is const!
    cout << "Read-only first element: "
         << list[0] << endl;
}

int main() {
    int numbers[5] = {1, 4, 3, 6, 8};
    p(numbers, 5);
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: 함수로부터의 배열 반환"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

// newList is the reversal of list
void reverse(const int list[], int newList[], int size) {
    for (int i = 0, j = size - 1; i < size; i++, j--)
        newList[j] = list[i];
}

void printArray(const int list[], int size) {
    for (int i = 0; i < size; i++)
        cout << list[i] << " ";
}

int main() {
    const int SIZE = 6;
    int list[] = {1, 2, 3, 4, 5, 6};
    int newList[SIZE];

    reverse(list, newList, SIZE);

    cout << "The original array: ";
    printArray(list, SIZE);
    cout << endl;

    cout << "The reversed array: ";
    printArray(newList, SIZE);
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "배열 탐색 — 선형 탐색"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [탐색]{.hl}은 배열에서 특정 요소를 찾는 작업입니다.

- [선형 탐색]{.hl}에서는 찾고자 하는 값([키]{.hl})을 배열 요소와 처음부터 끝까지 하나씩 비교합니다. 일치하는 요소가 발견되면 그 인덱스를, 그렇지 않으면 `-1`을 반환합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int linearSearch(const int list[], int key, int arraySize) {
    for (int i = 0; i < arraySize; i++)
        if (key == list[i])
            return i;
    return -1;
}

int main() {
    int list[] = {1, 4, 3, 6, 8, 2, 9};
    cout << "index of 6: " << linearSearch(list, 6, 7) << endl;
    cout << "index of 5: " << linearSearch(list, 5, 7) << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "배열 탐색 — 이진 탐색 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [이진 탐색]{.hl}은 [정렬]{.hl}된 배열에서만 동작합니다. 키를 중앙 요소와 비교하여 탐색 범위를 좁혀 갑니다.
  - 키가 중앙값보다 *작으면* 앞쪽 절반에서 탐색합니다.
  - 키가 중앙값과 *같으면* 값을 찾은 것이며 탐색을 종료합니다.
  - 키가 중앙값보다 *크면* 뒤쪽 절반에서 탐색합니다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w10/cpp-w10-image23.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "배열 탐색 — 이진 탐색 (2/2)"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int binarySearch(const int list[], int key, int listSize) {
    int low = 0;
    int high = listSize - 1;

    while (high >= low) {
        int mid = (low + high) / 2;
        if (key < list[mid])
            high = mid - 1;
        else if (key == list[mid])
            return mid;
        else
            low = mid + 1;
    }

    return -low - 1;   // not found: insertion point encoded
}

int main() {
    int list[] = {2, 4, 7, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79};
    cout << "index of 11: " << binarySearch(list, 11, 13) << endl;
    cout << "search  12 : " << binarySearch(list, 12, 13) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "배열 정렬 — 선택 정렬"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [선택 정렬]{.hl}은 배열에서 가장 작은 수를 찾아 첫 번째 요소와 교환한 뒤, 첫 요소를 제외한 나머지에 대해 같은 과정을 반복합니다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w10/cpp-w10-image26.png" class="tikz-fig" style="width: 100%;" />

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void selectionSort(double list[], int listSize) {
    for (int i = 0; i < listSize - 1; i++) {
        // Find the minimum in list[i..listSize-1]
        double currentMin = list[i];
        int currentMinIndex = i;

        for (int j = i + 1; j < listSize; j++)
            if (currentMin > list[j]) {
                currentMin = list[j];
                currentMinIndex = j;
            }

        // Swap if necessary
        if (currentMinIndex != i) {
            list[currentMinIndex] = list[i];
            list[i] = currentMin;
        }
    }
}

int main() {
    double list[] = {2, 9, 5, 4, 8, 1, 6};
    selectionSort(list, 7);
    for (int i = 0; i < 7; i++) cout << list[i] << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "2차원 배열"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 표나 행렬 데이터는 [2차원 배열]{.hl}로 표현할 수 있습니다.

- 2차원 배열은 다음 구문으로 선언합니다.

```cpp
elementType arrayName[ROW_SIZE][COLUMN_SIZE];
```

```cpp
int m[4][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {10, 11, 12}
};
```

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w10/cpp-w10-image27.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: "2차원 배열 처리 (1/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 2차원 배열을 처리할 때는 보통 [중첩 `for`]{.hl}문을 사용합니다.

- 행에 대한 바깥쪽 반복문과 열에 대한 안쪽 반복문을 이용해 각 요소를 임의의 값(`rand() % 100`)으로 초기화합니다.

- 고정된 시드(`srand(1)`)를 쓰면 출력이 재현 가능합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    srand(1);
    const int ROW_SIZE = 3, COLUMN_SIZE = 4;
    int matrix[ROW_SIZE][COLUMN_SIZE];

    // Initialize with random values
    for (int row = 0; row < ROW_SIZE; row++)
        for (int column = 0; column < COLUMN_SIZE; column++)
            matrix[row][column] = rand() % 100;

    for (int row = 0; row < ROW_SIZE; row++) {
        for (int column = 0; column < COLUMN_SIZE; column++)
            cout << matrix[row][column] << " ";
        cout << endl;
    }
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "2차원 배열 처리 (2/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 배열을 행 단위로 출력합니다.

- 중첩 반복문으로 *모든* 요소의 합을 구합니다.

- 열을 바깥쪽, 행을 안쪽에서 반복하여 *각 열*의 합을 구합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int ROW_SIZE = 3, COLUMN_SIZE = 4;
    int matrix[ROW_SIZE][COLUMN_SIZE] = {
        {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}
    };

    int total = 0;
    for (int row = 0; row < ROW_SIZE; row++) {
        for (int column = 0; column < COLUMN_SIZE; column++) {
            cout << matrix[row][column] << " ";
            total += matrix[row][column];
        }
        cout << endl;
    }
    cout << "Total sum is " << total << endl;

    for (int column = 0; column < COLUMN_SIZE; column++) {
        int colTotal = 0;
        for (int row = 0; row < ROW_SIZE; row++)
            colTotal += matrix[row][column];
        cout << "Sum for column " << column << " is " << colTotal << endl;
    }
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "2차원 배열 처리 (3/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [합이 가장 큰 행]{.hl}을 찾습니다.

- `maxRow`를 `0`번 행의 합으로 초기화한 뒤, 이후 각 행의 합을 이와 비교하며 가장 큰 행의 인덱스를 추적합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int ROW_SIZE = 3, COLUMN_SIZE = 4;
    int matrix[ROW_SIZE][COLUMN_SIZE] = {
        {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}
    };

    int maxRow = 0, indexOfMaxRow = 0;
    for (int column = 0; column < COLUMN_SIZE; column++)
        maxRow += matrix[0][column];   // sum of first row

    for (int row = 1; row < ROW_SIZE; row++) {
        int totalOfThisRow = 0;
        for (int column = 0; column < COLUMN_SIZE; column++)
            totalOfThisRow += matrix[row][column];
        if (totalOfThisRow > maxRow) {
            maxRow = totalOfThisRow;
            indexOfMaxRow = row;
        }
    }

    cout << "Row " << indexOfMaxRow
         << " has the maximum sum of " << maxRow << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "2차원 배열 처리 (4/4)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 2차원 배열 [섞기]{.hl}: 모든 셀 `(i, j)`에 대해 임의의 셀 `(i1, j1)`을 골라 두 값을 교환합니다.

- 고정된 시드(`srand(1)`)를 쓰면 섞인 결과가 결정적이며 재현 가능합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    srand(1);
    const int ROW_SIZE = 3, COLUMN_SIZE = 4;
    double matrix[ROW_SIZE][COLUMN_SIZE] = {
        {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}
    };

    for (int i = 0; i < ROW_SIZE; i++)
        for (int j = 0; j < COLUMN_SIZE; j++) {
            int i1 = rand() % ROW_SIZE;
            int j1 = rand() % COLUMN_SIZE;
            double temp = matrix[i][j];   // swap (i,j) and (i1,j1)
            matrix[i][j] = matrix[i1][j1];
            matrix[i1][j1] = temp;
        }

    for (int i = 0; i < ROW_SIZE; i++) {
        for (int j = 0; j < COLUMN_SIZE; j++)
            cout << matrix[i][j] << " ";
        cout << endl;
    }
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: 2차원 배열을 함수에 전달"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 2차원 배열을 함수에 전달할 때는 매개변수의 유형 선언에서 [열의 크기]{.hl}를 반드시 지정해야 합니다.

- 행의 크기는 비워 둘 수 있으며(`a[][COLUMN_SIZE]`), 별도의 인수로 전달합니다.

</div>
<div>

<CppRunner stdin="1 2 3 4 5 6 7 8 9 10 11 12">

```cpp
#include <iostream>
using namespace std;

const int COLUMN_SIZE = 4;

int sum(const int a[][COLUMN_SIZE], int rowSize) {
    int total = 0;
    for (int row = 0; row < rowSize; row++)
        for (int column = 0; column < COLUMN_SIZE; column++)
            total += a[row][column];
    return total;
}

int main() {
    const int ROW_SIZE = 3;
    int m[ROW_SIZE][COLUMN_SIZE];
    cout << "Enter " << ROW_SIZE << " rows and "
         << COLUMN_SIZE << " columns: " << endl;
    for (int i = 0; i < ROW_SIZE; i++)
        for (int j = 0; j < COLUMN_SIZE; j++)
            cin >> m[i][j];
    cout << "Sum of all elements is " << sum(m, ROW_SIZE) << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: 시험 답안 채점"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    const int NUMBER_OF_STUDENTS = 8;
    const int NUMBER_OF_QUESTIONS = 10;

    // Students' answers to the questions
    char answers[NUMBER_OF_STUDENTS][NUMBER_OF_QUESTIONS] = {
        {'A','B','A','C','C','D','E','E','A','D'},
        {'D','B','A','B','C','A','E','E','A','D'},
        {'E','D','D','A','C','B','E','E','A','D'},
        {'C','B','A','E','D','C','E','E','A','D'},
        {'A','B','D','C','C','D','E','E','A','D'},
        {'B','B','E','C','C','D','E','E','A','D'},
        {'B','B','A','C','C','D','E','E','A','D'},
        {'E','B','E','C','C','D','E','E','A','D'}
    };

    // Key to the questions
    char keys[] = {'D','B','D','C','C','D','A','E','A','D'};

    // Grade all answers
    for (int i = 0; i < NUMBER_OF_STUDENTS; i++) {
        int correctCount = 0;
        for (int j = 0; j < NUMBER_OF_QUESTIONS; j++)
            if (answers[i][j] == keys[j])
                correctCount++;
        cout << "Student " << i << "'s correct count is "
             << correctCount << endl;
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "다차원 배열"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- C++는 [임의 차원]{.hl}의 배열을 허용합니다.

- 2차원 배열 선언을 일반화하면 3차원 이상의 배열도 선언하고 초기화할 수 있습니다.

- `scores[6][5][2]`는 6명의 학생에 대해, 각 학생의 5개 시험을 2개 부분(객관식과 서술형)으로 담을 수 있습니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    double scores[6][5][2] = {
        {{7.5,20.5},{9.0,22.5},{15,33.5},{13,21.5},{15,2.5}},
        {{4.5,21.5},{9.0,22.5},{15,34.5},{12,20.5},{14,9.5}},
        {{6.5,30.5},{9.4,10.5},{11,33.5},{11,23.5},{10,2.5}},
        {{6.5,23.5},{9.4,32.5},{13,34.5},{11,20.5},{16,7.5}},
        {{8.5,26.5},{9.4,52.5},{13,36.5},{13,24.5},{16,2.5}},
        {{9.5,20.5},{9.4,42.5},{13,31.5},{12,20.5},{16,6.5}}
    };

    cout << "scores[0][0][0] = " << scores[0][0][0] << endl;
    cout << "scores[5][4][1] = " << scores[5][4][1] << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "HW_W10: 버블 정렬 후 이진 탐색"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.3rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [버블 정렬]{.hl}은 선택 정렬과 유사하지만, 최댓값/최솟값을 찾는 과정이 약간 다릅니다.

- 버블 정렬로 1차원 배열을 정렬한 뒤, 이진 탐색으로 키를 찾으세요.
  - `binarySearch`만 구현하면 됩니다(`main`은 필요 없음).

- `HW_W10_20XXXXXX.cpp`로 저장하여 LMS에 업로드하세요.

```text
bubbleSort(A[], n):
    for last <- n-1 downto 1:
        for i <- 0 to last-1:
            if (A[i] > A[i+1]):
                swap(A[i], A[i+1])
```

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

void bubbleSort(int A[], int n) {
    for (int last = n - 1; last >= 1; last--)
        for (int i = 0; i <= last - 1; i++)
            if (A[i] > A[i + 1]) {
                int t = A[i]; A[i] = A[i + 1]; A[i + 1] = t;
            }
}

int binarySearch(const int list[], int key, int listSize) {
    int low = 0, high = listSize - 1;
    while (high >= low) {
        int mid = (low + high) / 2;
        if (key < list[mid])      high = mid - 1;
        else if (key == list[mid]) return mid;
        else                       low = mid + 1;
    }
    return -low - 1;
}

int main() {
    int A[] = {5, 2, 9, 1, 7, 3};
    bubbleSort(A, 6);
    for (int i = 0; i < 6; i++) cout << A[i] << " ";
    cout << endl;
    cout << "index of 7: " << binarySearch(A, 7, 6) << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
