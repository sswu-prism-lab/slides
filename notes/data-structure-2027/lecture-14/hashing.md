# 해싱 (Hashing)

맵(map)과 해시 테이블<span class="gloss">hash table</span>은 키를 통해 값을 빠르게 찾기 위한
자료구조이다. 이 절에서는 맵의 개념부터 시작해, 충돌을 해결하는 두 축인 **개별 체이닝**과
**개방 주소**, 그리고 최악의 경우에도 성능을 보장하기 위한 **진보된 해시 테이블**까지
정리한다.

## 맵

- 맵<span class="gloss">map</span>은 키<span class="gloss">key</span>와 그 값<span class="gloss">value</span>을 정연하게<span class="gloss">ordered</span> 저장하기 위해 사용된다.
- 키는 반드시 유일해야 하지만, 여러 키가 같은 값을 사상<span class="gloss">mapping</span>할(가리킬) 수 있다.
  - 값들은 유일할 필요가 없다.
- 맵 안의 키들은 논리적으로 정렬된<span class="gloss">logically sorted</span> 순서로 유지된다.
- 맵은 *쌍*<span class="gloss">pair</span>으로 초기화된 집합처럼 작동하되, 다양한 비교 함수들은 오직 키에만 적용된다.
- 일반적으로 자가-수선이 가능한 이진 탐색 트리 자료구조가 맵의 구현에 사용된다.
  - C++에서는 `map` STL을 위해 레드-블랙 트리<span class="gloss">red-black tree</span>가 사용되었다.
- C++의 `map` STL은 일반적인 맵 컨테이너를 지원한다.

## 해시 테이블

- 해시 테이블<span class="gloss">hash table</span>은 `find`, `insert`, `remove` 연산을 $\mathcal{O}(1)$에 수행 가능한 자료구조이다.
- 이상적인 해시 테이블은 원소들을 담는 **고정된 크기의 배열**이며, 탐색은 원소의 키에서 수행된다.
- 각각의 키는 `0`부터 `tableSize - 1` 사이의 숫자로 적절한 위치<span class="gloss">cell</span>에 대응된다.
  - 이 대응은 해시 함수<span class="gloss">hash function</span>로 이루어진다.
  - 해시 함수는 계산하기 간단해야 하고, 서로 구분되는 키들은 서로 다른 위치에 대응되어야 한다.
  - 대부분 공간은 유한하고 키값은 사실상 무수히 많으므로 완전한 대응은 명백히 불가능하다. 따라서 위치들 사이에 키값을 **적절히 분산**시키는 해시 함수를 찾아야 한다.

### 해시 함수의 선택

- 입력 키값이 정수형이고 특수한 문제가 없다면, `key % tableSize` 를 사용하는 것이 일반적으로 타당한 전략이다.
  - 보통 테이블 크기는 소수<span class="gloss">prime number</span>로 하는 것이 좋다.
  - 이 함수는 계산이 간단함과 동시에 키들을 균등하게 분산시킨다.
- 키값이 문자열일 수도 있으며, 이 경우 문자열의 아스키<span class="gloss">ASCII</span>값을 사용할 수 있다.
  - 문자열에 대한 해시 함수로는 보통 호너 규칙<span class="gloss">Horner's rule</span>에 기반한 다항 함수<span class="gloss">polynomial function</span>를 사용한다.
- 해시 함수를 결정했다면, 서로 다른 키가 같은 위치에 대응되는 경우, 즉 **충돌**<span class="gloss">collision</span>을 반드시 고려해야 한다.

## 개별 체이닝

개별 체이닝<span class="gloss">separate chaining</span>은 같은 해시값을 가지는 원소들을 하나의
테이블 안에 **연결 리스트**로 묶어 보관하는 방식이다.

- `find` 연산: 해시 함수로 순회할 리스트를 찾은 뒤, 그 위치에 연결된 리스트를 탐색한다.
- `insert` 연산: 원소가 들어갈 위치를 찾고, 새로운 원소라면 그 위치의 연결 리스트에 추가한다.
- 연결 리스트 대신 다른 방법으로도 충돌을 해소할 수 있다.
  - 이진 탐색 트리나 또다른 해시 테이블을 체이닝에 사용할 수도 있다.

키 `81, 1, 0, 64, 4, 25, 36, 16, 49, 9` 를 크기 10짜리 테이블에
`key % 10` 으로 넣으면, 같은 나머지를 가지는 키들이 한 위치에서 리스트로 이어진다.
(원문 tikz 그림은 SVG로 변환되지 않아 아래 표로 대신한다.)

| 위치 | 연결 리스트 |
| :--: | :-- |
| 0 | 0 |
| 1 | 81 → 1 |
| 4 | 64 → 4 |
| 5 | 25 |
| 6 | 36 → 16 |
| 9 | 49 → 9 |

나머지 위치(2, 3, 7, 8)는 비어 있다.

### 적재율

- 적재율<span class="gloss">load factor</span> $\lambda$ 는 해시 테이블 안에 원소가 얼마나 들어 있는지에 대한 비율이다.
  - 개별 체이닝에서 **리스트의 평균 길이**는 $\lambda$ 가 된다.
  - 따라서 탐색 비용은 대략 $\mathcal{O}(1 + \lambda)$ 로, $\lambda$ 를 상수 수준으로 유지하면 평균 $\mathcal{O}(1)$ 이 된다.

### 실습 — 개별 체이닝 해시 테이블

`vector<list<int>>` 로 체이닝 해시 테이블을 구현한다. 삽입 후 표시하고,
`25`(존재)와 `50`(부재)에 대해 탐색·삭제를 시도한다.

<CppRunner>

```cpp
#include <iostream>
#include <list>
#include <vector>
#include <iterator>
#include <algorithm>
using namespace std;

class HashTable {
public:
    HashTable(int size) : tableSize(size) {   // 해시 테이블 초기화
        table.resize(tableSize);
    }
    void insertItem(int key) {                // 키 삽입
        int index = hashFunction(key);
        table[index].push_back(key);
    }
    void deleteItem(int key) {                // 키 삭제
        int index = hashFunction(key);
        auto& cell = table[index];
        auto it = find(cell.begin(), cell.end(), key);
        if (it != cell.end()) {
            cell.erase(it);
            cout << key << " deleted from hash table\n";
        }
        else
            cout << key << " not found in hash table\n";
    }
    bool searchItem(int key) {                // 키 탐색
        int index = hashFunction(key);
        auto& cell = table[index];
        auto it = find(cell.begin(), cell.end(), key);
        if (it != cell.end()) {
            cout << key << " found in hash table\n";
            return true;
        }
        else {
            cout << key << " not found in hash table\n";
            return false;
        }
    }
    void displayHashTable() {                 // 테이블 출력
        for (int i = 0; i < tableSize; i++) {
            cout << i;
            for (auto x : table[i])
                cout << " --> " << x;
            cout << endl;
        }
    }

private:
    int tableSize;
    vector<list<int>> table;   // 각 위치마다 연결 리스트를 둔다
    int hashFunction(int key) {
        return key % tableSize;
    }
};

int main() {
    int keys[] = {81, 1, 0, 64, 4, 25, 36, 16, 49, 9};
    int n = sizeof(keys) / sizeof(keys[0]);
    HashTable hashTable(10);

    for (int i = 0; i < n; i++)
        hashTable.insertItem(keys[i]);

    hashTable.displayHashTable();
    hashTable.searchItem(25); hashTable.searchItem(50);
    hashTable.deleteItem(25); hashTable.deleteItem(50);
    hashTable.displayHashTable();
    return 0;
}
```

</CppRunner>

## 개방 주소

개별 체이닝처럼 리스트를 매다는 대신, **비어 있는 다른 위치**를 대체 위치로 사용해
충돌을 해결하는 방식을 개방 주소<span class="gloss">open addressing</span>라 한다.

- $f(0)=0$ 일 때 다음 순서로 위치를 시도한다.

$$h_i(x) = \bigl(hash(x) + f(i)\bigr) \bmod tableSize, \qquad h_0(x), h_1(x), h_2(x), \ldots$$

- 이 함수 $f$ 가 바로 **충돌 해결 전략**이다.
- 모든 데이터가 테이블 안에 들어가므로, 개별 체이닝보다 더 큰 테이블이 필요하다.
  - 일반적으로 적재율은 개별 체이닝과 달리 $\lambda = 0.5$ 보다 낮게 유지한다.
  - 이러한 테이블을 조사 해시 테이블<span class="gloss">probing hash table</span>이라 한다.

### 선형 조사

- 선형 조사<span class="gloss">linear probing</span>에서 $f$ 는 $i$ 의 선형 함수로, 보통 $f(i)=i$ 를 사용한다.
  - 비어 있는 위치를 찾기 위해 한 칸씩 아래로 내려가는 방식이다.
- 아래 그림은 $89 \rightarrow 18 \rightarrow 49 \rightarrow 58 \rightarrow 69$ 를 $h(x)=x \bmod 10$ 으로 삽입한 결과이다.
- 테이블이 어느 정도 비어 보여도, 원소가 들어간 위치들의 군집<span class="gloss">block</span>이 만들어지기 시작한다.
  - 이러한 현상을 1차 군집<span class="gloss">primary clustering</span>이라 하며, 군집 안으로 해시된 키들은 충돌 해결을 위해 계속 클러스터 끝에 붙는다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-33.svg" alt="선형 조사로 89, 18, 49, 58, 69를 삽입한 해시 테이블" style="max-width: 300px;" />
  <figcaption class="cap">선형 조사: 49→0, 58→1, 69→2, 18→8, 89→9 (군집이 형성된다)</figcaption>
</figure>

### 실습 — 선형 조사 해시 테이블

`vector<int>` 배열과 점유 여부 `vector<bool>` 로 선형 조사를 구현한다.
비어 있는 위치를 만날 때까지 `(index + 1) % tableSize` 로 한 칸씩 내려간다.
출력은 위 그림과 정확히 일치한다.

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class HashTable {
public:
    HashTable(int size) : tableSize(size), emptySlot(size) {
        table.resize(tableSize, emptySlot);
        occupied.resize(tableSize, false);
    }
    void insertItem(int key) {                 // 선형 조사로 빈 위치 찾아 삽입
        int index = hashFunction(key);
        int startIndex = index;
        while (occupied[index]) {
            index = (index + 1) % tableSize;
            if (index == startIndex) {
                cout << "Hash table is full, cannot insert " << key << endl;
                return;
            }
        }
        table[index] = key;
        occupied[index] = true;
    }
    void deleteItem(int key) {                  // 선형 조사로 키를 찾아 삭제
        int index = hashFunction(key);
        int startIndex = index;
        while (occupied[index]) {
            if (table[index] == key) {
                table[index] = emptySlot;
                occupied[index] = false;
                cout << key << " deleted from hash table\n";
                return;
            }
            index = (index + 1) % tableSize;
            if (index == startIndex) break;
        }
        cout << key << " not found in hash table\n";
    }
    bool searchItem(int key) {                  // 선형 조사로 키 탐색
        int index = hashFunction(key);
        int startIndex = index;
        while (occupied[index]) {
            if (table[index] == key) {
                cout << key << " found in hash table\n";
                return true;
            }
            index = (index + 1) % tableSize;
            if (index == startIndex) break;
        }
        cout << key << " not found in hash table\n";
        return false;
    }
    void displayHashTable() {
        for (int i = 0; i < tableSize; i++) {
            cout << i;
            if (occupied[i])
                cout << " --> " << table[i];
            else
                cout << " --> " << "empty";
            cout << endl;
        }
    }

private:
    int tableSize;
    int emptySlot;
    vector<int> table;
    vector<bool> occupied;
    int hashFunction(int key) {
        return key % tableSize;
    }
};

int main() {
    int keys[] = {89, 18, 49, 58, 69};
    int n = sizeof(keys) / sizeof(keys[0]);
    HashTable hashTable(10);

    for (int i = 0; i < n; i++)
        hashTable.insertItem(keys[i]);

    hashTable.displayHashTable();
    return 0;
}
```

</CppRunner>

### 이차 조사

- 이차 조사<span class="gloss">quadratic probing</span>는 선형 조사의 1차 군집을 없애기 위해 제안된 방식이다.
- 충돌 함수가 제곱식<span class="gloss">quadratic</span>이며, 보통 $f(i)=i^2$ 를 사용한다.
- 이차 조사가 1차 군집은 없애지만, 같은 위치로 해시되는 원소들은 결국 같은 조사 순서를 밟게 된다.
  - 이러한 현상을 2차 군집<span class="gloss">secondary clustering</span>이라 한다.

같은 키 $89, 18, 49, 58, 69$ 를 $f(i)=i^2$ 로 넣으면, 선형 조사와 달리
49→0, 58→2, 69→3, 18→8, 89→9 처럼 충돌 원소가 한 칸씩이 아니라 $1, 4, 9, \ldots$ 만큼
떨어진 위치로 흩어진다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-34.svg" alt="이차 조사로 삽입한 해시 테이블" style="max-width: 300px;" />
  <figcaption class="cap">이차 조사: 49→0, 58→2, 69→3, 18→8, 89→9</figcaption>
</figure>

### 더블 해싱

- 1차·2차 군집을 모두 없애기 위해 제안된 방법이 더블 해싱<span class="gloss">double hashing</span>이다.
- 더블 해싱에서는 $f(i) = i \cdot hash_2(x)$ 를 선택한다.
- 일반적으로 $hash_2$ 함수는 $hash_1$ 의 나머지 연산자 숫자보다 약간 작은 수를 쓴다.
  - 즉 $hash_1(x) = x \bmod M$, $hash_2(x) = x \bmod N$ 일 때 $N < M$ 으로 고르는 것이 일반적이다.
- 다만 소수인 $N$ 을 찾기 어려운 경우가 있으므로 대안을 쓰기도 한다.
  - $hash_2(x) = N - (x \bmod N)$
  - 아래 그림은 2번째 해시 함수로 $7 - (x \bmod 7)$ 을 사용한 결과이다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-fin-35.svg" alt="더블 해싱으로 삽입한 해시 테이블" style="max-width: 300px;" />
  <figcaption class="cap">더블 해싱: 69→0, 58→3, 49→6, 18→8, 89→9</figcaption>
</figure>

### 재해싱

- 개방 주소 방식은 테이블이 점점 가득 차면 연산 시간이 너무 길어지고, 심지어 이차 조사는 삽입에 실패할 수 있다.
- 이 현상은 보통 삽입과 제거가 번갈아 이루어질 때 발생한다.
- 이 경우 기존의 2배 크기인 새 테이블을 (적절한 새 해시 함수와 함께) 만들고, 기존 테이블을 전체적으로 훑어 새 테이블에 다시 삽입한다.
- 예: 원소 $13, 15, 24, 6$ 을 선형 조사로 $h(x) = x \bmod 7$, 크기 7짜리 테이블에 삽입한다고 하자.
  - $23$ 을 넣으면 적재율이 70%를 넘으므로 새 테이블이 만들어진다.
  - 새 테이블 크기는 $17$ 인데, 이는 기존 크기의 2배 이상에서 처음 등장하는 소수이기 때문이다.
- 이 전체 연산을 재해싱<span class="gloss">rehashing</span>이라 한다.
  - 재해싱은 $\mathcal{O}(N)$ 의 수행 시간을 가진다.
- C++의 `unordered_set`, `unordered_map` STL은 해시 테이블 컨테이너를 지원한다.

::: tip 충돌 해결 전략 비교

| 전략 | $f(i)$ | 특징 | 군집 |
| :-- | :-- | :-- | :-- |
| 개별 체이닝 | — (리스트) | $\lambda$ 를 1 근처까지 허용 | 없음 |
| 선형 조사 | $i$ | 구현이 간단 | 1차 군집 |
| 이차 조사 | $i^2$ | 1차 군집 제거 | 2차 군집 |
| 더블 해싱 | $i \cdot hash_2(x)$ | 군집을 거의 제거 | 거의 없음 |

:::

## 진보된 해시 테이블

- 해시 테이블이 적절한 적재율과 알맞은 해시 함수를 가지면, **평균적으로** 삽입·제거·탐색에 $\mathcal{O}(1)$ 을 기대할 수 있다.
- **최악의 경우에도** $\mathcal{O}(1)$ 을 얻기 위해 몇몇 진보된 해시 테이블 알고리즘이 제안되었다.

### 완전 해싱

완전 해싱<span class="gloss">perfect hashing</span>에서는 문제를 간단히 하기 위해 앞으로 입력될
$N$ 개의 원소를 미리 알고 있다고 가정한다.

- 개별 체이닝 구현에서 각 리스트의 길이가 정해진 상수 이하임이 보장된다면 그대로 쓰면 된다.
  - 리스트를 더 많이 만들면 평균적으로 각 리스트는 짧아지고, 충분히 많으면 합리적으로 높은 확률로 충돌이 없다고 기대할 수 있다.
- 원소가 $N$ 개일 때 충돌 확률을 극단적으로 낮추려면 테이블 크기가 $\Omega(N^2)$ 이어야 한다.
  - 이는 매우 비실용적이므로, 연결 리스트 대신 **2단계 해시**를 쓴다: 먼저 원소를 첫 번째 해시 테이블에 넣고, **충돌이 일어난 위치에서만** 추가적인 해시 테이블을 달아 충돌 확률을 크게 낮춘다.

원문 예시(첫 번째 해시 테이블의 각 위치와 두 번째 해시 테이블 크기)를 표로 정리하면 다음과 같다.
(원문 tikz 그림은 SVG로 변환되지 않아 표로 대신한다.)

| 첫 번째 테이블 위치 | 원소 수 $m$ | 두 번째 테이블 크기 $m^2$ |
| :--: | :--: | :--: |
| 1, 3, 5, 7 | 0 | (비어 있음) |
| 0, 4, 8 | 1 | 1 |
| 2, 6 | 2 | 4 |
| 9 | 3 | 9 |

- 각 두 번째 해시 테이블은 크기를 $m^2$ 로 잡으므로 그 안에서는 충돌이 없는 해시 함수를 사용할 수 있다.
- 각 위치의 원소 수 $m$ 은 작으므로 $\sum m^2$ 전체는 여전히 $\mathcal{O}(N)$ 공간에 머문다.

### 뻐꾸기 해싱

뻐꾸기 해싱<span class="gloss">cuckoo hashing</span>은 $N$ 개의 원소에 대해 각각 절반 이상 비어 있는
**2개의 테이블**과, 원소를 각 테이블의 서로 다른 위치로 해싱하는 **2개의 해시 함수**를 사용한다.

- 앞으로 입력될 원소를 미리 알 필요가 없다.
- 원소는 반드시 두 테이블 중 하나의 위치에 저장되도록 유지된다.

수행 방식은 비교적 단순하다.

- 새 원소 $A$ 를 넣기 전에 이미 들어 있지 않은지 확인한다.
- 첫 번째 해시 함수의 위치가 비어 있으면 그대로 넣는다.
- 새 원소 $B$ 가 이미 차 있는 위치로 가야 한다면, $B$ 를 첫 번째 테이블에 우선 놓는다.
  - 이를 위해 그 자리의 $A$ 를 밀어내고(뻐꾸기가 알을 밀어내듯), $A$ 는 자신의 두 번째 해시 위치를 사용해 두 번째 테이블로 이동한다.

예를 들어 각각 5칸짜리 테이블 2개가 있고, $X:(y,z)$ 가 원소 $X$ 의 첫·두 번째 해시
위치를 뜻할 때 다음을 삽입한다고 하자.

$$A:(0,2) \rightarrow B:(0,0) \rightarrow C:(1,4) \rightarrow D:(1,0) \rightarrow E:(3,2) \rightarrow F:(3,4)$$

결과는 다음과 같다.

| 위치 | Table 1 | Table 2 |
| :--: | :--: | :--: |
| 0 | $A$ | $B$ |
| 1 | $D$ | |
| 2 | | $E$ |
| 3 | $F$ | |
| 4 | | $C$ |

- 여기서 새 원소 $G:(1,2)$ 를 삽입하려 하면, 모든 원소가 제거되고 재배치되고 다시 제거되는 과정이 끝없이 반복된다.
  - 이러한 현상을 *순환*<span class="gloss">cycle</span>이라 한다.
- 앞으로 어떤 원소가 들어올지 모르므로, 순환이 생길 확률을 낮게 유지하는 조건이 중요하다.
- 수리적으로 테이블 적재율이 $0.5$ 이하이면 순환 확률은 매우 낮아진다.
  - 적재율이 $0.5$ 이상이면 순환 확률이 극단적으로 상승하며, 이 경우 뻐꾸기 해싱은 좋은 전략이 아니다.

::: warning 정리
- 평균 $\mathcal{O}(1)$ 은 적절한 적재율·해시 함수만으로 얻을 수 있다.
- 최악의 경우까지 보장하려면 완전 해싱(2단계)·뻐꾸기 해싱 같은 진보된 기법이 필요하며, 그 대가로 여분의 공간이나 낮은 적재율($\lambda \le 0.5$)을 요구한다.
:::
