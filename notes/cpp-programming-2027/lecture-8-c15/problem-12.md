# 문제 12 · 정수형 난수 생성 방식

::: info 문제 12 [2점]
C++에서 정수형 난수<span class="gloss">random number</span>를 생성하는 방식에 대해 서술하시오.
:::

::: details 풀이 및 해설
**핵심 개념**: 컴퓨터의 난수는 실제로는 **씨앗값<span class="gloss">seed</span>**에서 출발해 정해진 규칙으로 만들어지는 **의사 난수<span class="gloss">pseudo-random number</span>**입니다.

**1) 전통적 방식 (`<cstdlib>`)**
- `rand()`: `0`부터 `RAND_MAX`까지의 정수 난수를 반환합니다.
- `srand(seed)`: 난수열의 **씨앗값**을 설정합니다. 같은 씨앗이면 항상 같은 난수열이 나옵니다.
- 매 실행마다 다른 난수를 원하면 `srand(time(0))`처럼 현재 시각을 씨앗으로 씁니다.
- 특정 범위 `[a, b]`의 정수는 나머지 연산으로 만듭니다.

```cpp
#include <cstdlib>
#include <ctime>
srand(time(0));            // 씨앗 설정(매 실행마다 다르게)
int r = rand() % 6 + 1;    // 1 ~ 6 사이의 정수
```

**2) 현대적 방식 (`<random>`, C++11 이상)**
- 난수 **엔진**(`mt19937`, 메르센 트위스터 등)과 **분포**(`uniform_int_distribution`)를 조합해 품질 좋은 난수를 얻습니다.

```cpp
#include <random>
mt19937 gen(1234);                          // 엔진 + 씨앗
uniform_int_distribution<int> dist(1, 6);   // 1 ~ 6 균등 분포
int r = dist(gen);
```

**정리**: 씨앗을 설정하고(`srand` 또는 엔진 초기화), 난수 생성 함수(`rand()` 또는 분포 객체)를 호출한 뒤, 필요한 범위로 변환하여 정수형 난수를 얻습니다.
:::
