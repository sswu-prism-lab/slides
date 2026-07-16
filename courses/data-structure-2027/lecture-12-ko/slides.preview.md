---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 12 (KO)
download: true
info: |
  ## 자료구조 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-12/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">자료구조</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">12주차: 해시 테이블</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">2027년 봄학기</p>
</div>

---
layout: prism
heading: 과목 커리큘럼
---

<div class="absolute left-10 right-10" style="top: 0rem; bottom: 0rem; display: grid; grid-template-columns: 1.2fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">과목 소개</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">기초 수학과 C++ 세부사항</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">알고리즘 분석</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">리스트, 스택, 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">원형 큐와 우선순위 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">트리와 트라이</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">힙</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">그래프와 가중치 그래프</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">집합과 맵</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span class="text-gray-900 dark:text-gray-100">해시 테이블</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">알고리즘 설계 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: "요약: 동치 관계"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 집합 $S$에서 [관계]{.hl}<sup>relation</sup> $R$은 모든 원소 쌍 $(a, b)$, $a, b \in S$에 대해 $a\ R\ b$가 *참* 혹은 *거짓*으로 결정된다.
  - $a\ R\ b$가 참이면, $a$가 $b$와 *관계된다*고 한다.

- [동치 관계]{.hl}<sup>equivalence relation</sup>는 세 가지 성질을 만족하는 관계 $R$이다:

<div class="sub-item-enum">

1. *재귀성.* $a\ R\ a$, $\forall a \in S$.
2. *대칭성.* $a\ R\ b$일 필요충분조건은 $b\ R\ a$이다.
3. *전이성.* $a\ R\ b$와 $b\ R\ c$는 $a\ R\ c$를 내포한다.

</div>

- $\leq$ 관계는 동치 관계가 *아니다*: 재귀성과 전이성은 있지만 대칭성이 없다 ($a \leq b$가 $b \leq a$를 내포하지 않는다).

- 전기적 연결은 동치 관계*이다* — 재귀적이고, 대칭적이며, 전이적이다.

---
layout: prism
heading: 해시 테이블
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- `find` 연산은 배열에서 $\mathcal{O}(N)$, 자가-조정 이진 트리에서 $\mathcal{O}(\log N)$의 시간이 필요하다.
  - 원소를 $\mathcal{O}(1)$ 시간에 `find`할 수 있을까?

- [해시 테이블]{.hl}<sup>hash tables</sup>의 구현은 흔히 [해싱]{.hl}<sup>hashing</sup>이라 불린다 — 삽입, 삭제, 탐색을 *평균적으로 상수 시간*에 수행하는 기법이다.

- 원소들 사이의 *순서*를 요구하는 연산은 효율적으로 지원되지 않는다. 예를 들어 `findMin`, `findMax`, `print`는 선형 시간에 수행되지 않는다.

- 오늘은 해시 테이블 자료구조에 대해 다룬다:
  - 해시 테이블을 구현하는 여러 방법을 살펴보고,
  - 이 방법들을 분석적으로 비교한다.

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">일반적 아이디어</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">일반적 아이디어</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">해시 함수</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">개별 체이닝</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">연결 리스트 없는 해시 테이블</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">최악의 경우 O(1) 접근을 갖는 해시 테이블</span></p>
  </div>

</div>

---
layout: prism
heading: 일반적 아이디어
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 이상적인 해시 테이블 자료구조는 단지 원소들을 담는 고정된 크기의 *배열*일 뿐이다.

- 보통 탐색은 원소의 일부분에 대해 수행되며, 이 부분을 [키]{.hl}<sup>key</sup>라고 한다.

- 각 키는 `0`부터 `tableSize - 1` 범위의 숫자로 대응되어 적절한 위치(cell)에 놓인다.
  - 이 대응을 [해시 함수]{.hl}<sup>hash function</sup>라고 하며, 이상적으로는 계산이 간단해야 하고 서로 다른 두 키가 서로 다른 위치를 갖도록 해야 한다.

- 위치의 수는 유한하지만 키는 사실상 무한히 많으므로 이는 명백히 불가능하다 — 따라서 키를 위치들 사이에 *균등하게 분산시키는* 해시 함수를 찾고자 한다.

---
layout: prism
heading: 일반적 아이디어 — 완벽한 상황
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 오른쪽 테이블은 전형적인 *완벽한* 상황이다 — 모든 키가 자기만의 위치에 놓인다.

- 이것이 해싱의 기본 아이디어이다.

- 남은 문제는 함수를 선택하고, 두 키가 같은 값으로 해시될 때 어떻게 할지 결정하고, 테이블 크기를 정하는 것이다.
  - 두 키가 같은 값으로 해시되는 것을 [충돌]{.hl}<sup>collision</sup>이라고 한다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w12-01.svg" class="tikz-fig" style="width: 62%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: 해시 함수
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 키가 정수라면, 키에 바람직하지 않은 성질이 없는 한 `key mod tableSize`를 반환하는 것이 일반적으로 타당하다.
  - 테이블 크기가 $10$이고 모든 키가 0으로 끝난다면, 표준적인 해시 함수는 좋지 않은 선택이다.
  - 이런 상황을 피하기 위해, 보통 테이블 크기를 [소수]{.hl}<sup>prime</sup>로 두는 것이 좋다.

- *임의의* 정수 키에 대해 이 함수는 계산이 간단하고 키를 균등하게 분산시킨다.
  - 키가 문자열일 때는 문자들의 ASCII 값을 결합할 수 있다.

- 테이블 크기가 크면, 단순한 합산은 분산이 좋지 않다.
  - 테이블 크기가 $10007$(소수)이고 키가 8개 이하의 문자라면, 합은 $0$에서 $1016$까지만 도달할 수 있다 (ASCII 문자는 최대 $127$이고, $127 \times 8 = 1016$이다).

---
layout: prism
heading: "해시 함수 — 문자 합산"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 첫 번째 시도는 단순히 키에 있는 모든 문자의 ASCII 값을 더한다.

- 두 번째 시도는 처음 세 문자에 가중치를 준다: $\texttt{key}[0] + 27\,\texttt{key}[1] + 729\,\texttt{key}[2]$.

- 안타깝게도, 영어는 무작위가 *아니다*.
  - $26^3$개의 세 문자 조합 중, 큰 사전에서는 오직 $2851$개의 서로 다른 조합만 나타난다 — 따라서 충돌이 전혀 없어도 테이블의 약 $28\%$만 도달할 수 있다.

</div>
<div>

```cpp
int hash(const string& key,
         int tableSize) {
    int hashVal = 0;
    for (char ch : key)
        hashVal += ch;
    return hashVal % tableSize;
}
```

<div style="height: 1.2rem;"></div>

```cpp
int hash(const string& key,
         int tableSize) {
    return (key[0] + 27 * key[1]
          + 729 * key[2]) % tableSize;
}
```

</div>
</div>

---
layout: prism
heading: "해시 함수 — 호너의 규칙"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 세 번째 시도는 키의 *모든* 문자를 포함하며 일반적으로 분산이 잘 될 것으로 기대할 수 있다.

- 아래 코드는 [호너의 규칙]{.hl}<sup>Horner's rule</sup>을 사용해 키를 $37$진수로 취급하여 다항 함수를 계산한다.

- 이는 극도로 단순하다는 장점이 있으며 상당히 빠르다.

</div>
<div>

<div style="height: 3rem;"></div>

```cpp
unsigned int hash(const string& key,
                  int tableSize) {
    unsigned int hashVal = 0;
    for (char ch : key)
        hashVal = 37 * hashVal + ch;
    return hashVal % tableSize;
}
```

</div>
</div>

---
layout: prism
heading: 개별 체이닝
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>


- 남은 주요 프로그래밍 세부사항은 [충돌 해결]{.hl}<sup>collision resolution</sup>이다.

- 삽입되는 원소가 이미 삽입된 원소와 같은 값으로 해시되면 *충돌*이 발생하며 이를 해결해야 한다.

- 첫 번째 전략인 [개별 체이닝]{.hl}<sup>separate chaining</sup>은 같은 값으로 해시되는 모든 원소를 하나의 *리스트*로 유지한다.

- $hash(x) = x \bmod 10$일 때, $\{0,1,4,9,16,25,36,49,64,81\}$을 삽입하면 오른쪽 테이블을 얻는다.

</div>
<div>

<div style="height: 0rem;"></div>

| 위치 | 체인 |
|:----:|:------|
| 0 | $\to 0$ |
| 1 | $\to 81 \to 1$ |
| 4 | $\to 64 \to 4$ |
| 5 | $\to 25$ |
| 6 | $\to 36 \to 16$ |
| 9 | $\to 49 \to 9$ |

</div>
</div>

---
layout: prism
heading: "개별 체이닝 — 연산"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `find`를 수행하려면, 해시 함수로 어떤 리스트를 순회할지 정한 뒤 그 리스트를 탐색한다.

- `insert`를 수행하려면, 해당 리스트를 확인해 원소가 이미 존재하는지 살핀다.
  - 원소가 새로운 것이라면 리스트의 *앞*에 삽입할 수 있다.

- 연결 리스트 외에 어떤 방식이라도 사용할 수 있다 — 이진 탐색 트리나 심지어 또 다른 해시 테이블도 가능하다.
  - 그러나 테이블이 크고 해시 함수가 좋다면 모든 리스트가 짧으므로, 기본적인 개별 체이닝은 단순하게 유지된다.

- 해시 테이블의 [적재율]{.hl}<sup>load factor</sup> $\lambda$는 원소의 개수와 테이블 크기의 비율이다.
  - 개별 체이닝에서 리스트의 평균 길이는 정확히 $\lambda$이므로, 성공적인 `find`는 $\mathcal{O}(1 + \lambda)$의 비용이 든다.

---
layout: prism
heading: "개별 체이닝 — 구현"
---

```cpp
template <typename HashedObj>
class HashTable {
public:
    explicit HashTable(int size = 101);

    bool contains(const HashedObj& x) const {
        auto& whichList = theLists[myhash(x)];
        return find(begin(whichList), end(whichList), x) != end(whichList);
    }

    bool insert(const HashedObj& x) {
        auto& whichList = theLists[myhash(x)];
        if (find(begin(whichList), end(whichList), x) != end(whichList))
            return false;              // 이미 존재함
        whichList.push_back(x);
        if (++currentSize > theLists.size()) rehash();   // 람다 <= 1 유지
        return true;
    }

private:
    vector<list<HashedObj>> theLists;  // 리스트들의 배열
    int currentSize;
    size_t myhash(const HashedObj& x) const {
        static hash<HashedObj> hf;
        return hf(x) % theLists.size();
    }
};
```

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">일반적 아이디어</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">연결 리스트 없는 해시 테이블</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">선형 조사</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">이차 조사</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">더블 해싱</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">재해싱</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">STL에서의 해시 테이블</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">최악의 경우 O(1) 접근을 갖는 해시 테이블</span></p>
  </div>

</div>

---
layout: prism
heading: "선형 조사 — 개방 주소"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- 개별 체이닝은 연결 리스트를 사용한다는 단점이 있다 — 새로운 셀 할당이 느리고 두 번째 자료구조를 필요로 한다.

- 한 대안은 빈 셀을 찾을 때까지 대체 셀을 시도함으로써 연결 리스트 *없이* 충돌을 해결한다.
  - 이 전략을 [개방 주소]{.hl}<sup>open addressing</sup>라고 한다.

- 형식적으로, 셀 $h_0(x), h_1(x), h_2(x), \ldots$가 차례로 시도되며, 여기서

$$
h_i(x) = \big(hash(x) + f(i)\big) \bmod tableSize, \qquad f(0) = 0.
$$

- 함수 $f$가 바로 *충돌 해결 전략*이다. 모든 데이터가 테이블 안에 들어가므로, 개별 체이닝보다 더 큰 테이블이 필요하다.

- 일반적으로 적재율은 $\lambda = 0.5$ 미만이어야 하며, 이러한 테이블을 [조사 해시 테이블]{.hl}<sup>probing hash tables</sup>이라고 한다.

---
layout: prism
heading: "선형 조사 — 1차 군집"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

- [선형 조사]{.hl}<sup>linear probing</sup>에서 $f$는 $i$의 선형 함수이며, 보통 $f(i) = i$이다.
  - 이는 빈 셀을 찾기 위해 셀을 순차적으로 시도하는 것과 같다.

- 오른쪽 테이블은 키 $\{89, 18, 49, 58, 69\}$를 삽입한 결과를 보여준다.

- 테이블이 비교적 비어 있어도, 채워진 셀들의 군집이 형성된다.
  - 이것이 [1차 군집]{.hl}<sup>primary clustering</sup>이다: 군집으로 해시되는 키는 여러 번 시도해야 하고 그 뒤 군집에 추가된다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w12-02.svg" class="tikz-fig" style="width: 60%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "선형 조사 — 구현"
---

```cpp
template <typename HashedObj>
class HashTable {
public:
    bool contains(const HashedObj& x) const { return isActive(findPos(x)); }

    bool insert(const HashedObj& x) {
        int currentPos = findPos(x);
        if (isActive(currentPos)) return false;      // 이미 존재함
        array[currentPos] = HashEntry{x, ACTIVE};
        if (++currentSize > array.size() / 2) rehash();   // 람다 < 0.5 유지
        return true;
    }

private:
    enum EntryType { ACTIVE, EMPTY, DELETED };
    struct HashEntry { HashedObj element; EntryType info; };
    vector<HashEntry> array;
    int currentSize;

    int findPos(const HashedObj& x) const {
        int offset = 1, currentPos = myhash(x);
        while (array[currentPos].info != EMPTY && array[currentPos].element != x) {
            currentPos += offset;                    // f(i) = i : 선형 조사
            if (currentPos >= array.size()) currentPos -= array.size();
        }
        return currentPos;
    }
};
```

---
layout: prism
heading: "이차 조사 — 2차 군집"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [이차 조사]{.hl}<sup>quadratic probing</sup>는 선형 조사의 1차 군집을 없앤다.

- 그 충돌 함수는 이차식이며, 널리 쓰이는 선택은 $f(i) = i^2$이다.

- 1차 군집은 제거하지만, *같은* 위치로 해시되는 원소들은 동일한 대체 셀을 조사한다.
  - 이를 [2차 군집]{.hl}<sup>secondary clustering</sup>이라고 한다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w12-03.svg" class="tikz-fig" style="width: 60%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: 더블 해싱
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

- 우리가 살펴볼 마지막 충돌 해결 방법은 [더블 해싱]{.hl}<sup>double hashing</sup>이다.

- 널리 쓰이는 선택은 $f(i) = i \cdot hash_2(x)$로, *두 번째* 해시 함수가 이동 폭을 결정한다.

- 오른쪽 테이블은 $\{89, 18, 49, 58, 69\}$를 삽입하는 동안 $hash_2(x) = x \bmod 9$를 사용한다.
  - $hash_2$는 결코 0이 되어서는 안 되며, 소수 $R < tableSize$에 대해 $R - (x \bmod R)$로 선택하면 잘 동작한다.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w12-04.svg" class="tikz-fig" style="width: 60%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: 재해싱
---

- 테이블이 너무 가득 차면 연산이 너무 오래 걸리고, 이차 조사의 경우 삽입이 *실패*할 수도 있다.
  - 이는 많은 제거가 삽입과 뒤섞일 때도 발생할 수 있다.

- 해결책은 약 *두 배* 큰 새로운 테이블을 (새로운 해시 함수와 함께) 만들고, 기존 테이블 전체를 훑어, 삭제되지 않은 각 원소를 새로운 해시값에 다시 삽입하는 것이다.
  - 이 전체 연산을 [재해싱]{.hl}<sup>rehashing</sup>이라고 한다. 이는 비싼 연산으로 수행 시간이 $\mathcal{O}(N)$이지만, 매우 드물게 일어나므로 *분할 상환* 비용은 작다.

<div class="theorem-box">
<div class="theorem-box-title">예시</div>
<div class="theorem-box-body">

$h(x) = x \bmod 7$을 사용하는 크기 $7$의 선형 조사 테이블에 $13, 15, 24, 6$을 삽입한다. $23$을 삽입하면 테이블이 $70\%$를 넘게 차므로, 크기 $17$의 새 테이블이 만들어진다 — 이는 두 배 이상 크기 중 첫 번째 소수이다.

</div>
</div>

---
layout: prism
heading: STL에서의 해시 테이블
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- C++은 해시 테이블 자료구조를 구현하는 두 가지 표준 라이브러리 컨테이너를 제공한다: [`unordered_set`]{.hl}과 [`unordered_map`]{.hl}.

- (균형 이진 탐색 트리인) `set`과 `map`과 달리, 이들은 원소를 특정한 순서로 유지하지 *않지만* 평균 $\mathcal{O}(1)$ 연산을 제공한다.

<div style="height: 1rem;"></div>

```cpp
#include <unordered_set>
#include <unordered_map>

unordered_set<string> words;              // 해시 집합
unordered_map<string, int> wordCount;     // 해시 맵 (키 -> 값)
```

---
layout: prism
heading: 목차
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">일반적 아이디어</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">연결 리스트 없는 해시 테이블</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">최악의 경우 O(1) 접근을 갖는 해시 테이블</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">완전 해싱</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">뻐꾸기 해싱</span></p>
  </div>

</div>

---
layout: prism
heading: "완전 해싱 — 동기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 지금까지의 해시 테이블은 적절한 적재율에서 삽입, 제거, 탐색에 대해 *평균적으로* $\mathcal{O}(1)$ 비용을 제공한다.

- 우리는 *최악의 경우* $\mathcal{O}(1)$ 비용을 원한다.
  - 라우터의 하드웨어 조회 테이블이나 메모리 캐시 같은 응용에서는 탐색이 정해진 완료 시간을 가져야 한다.

- 단순화를 위해, $N$개의 원소를 모두 미리 알고 있다고 가정하자.

- 개별 체이닝 구현이 각 리스트가 최대 상수 개의 원소만 갖도록 보장할 수 있다면, 그것으로 충분하다.
  - 리스트를 더 많이 만들수록 리스트는 평균적으로 짧아진다 — 따라서 충분히 많은 리스트가 있으면 충돌이 *전혀* 없을 것으로 기대할 수 있다.

---
layout: prism
heading: "완전 해싱 — 2단계 구조"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 충돌이 없음을 보장할 만큼 리스트 수 $M$을 충분히 크게 선택한다; 충돌이 감지되면 테이블을 비우고 다른 독립적인 해시 함수로 다시 시도한다.

- 이론적으로 $M$은 상당히 커야 하며 — 구체적으로 $M = \Omega(N^2)$ — 따라서 $N^2$개의 리스트를 사용하는 것은 비실용적이다.

- 실용적으로는, 각 *빈*에서의 충돌을 연결 리스트 대신 추가적인 해시 테이블을 사용해 해결한다.
  - 각 빈에는 원소가 몇 개 없으므로, 빈의 두 번째 해시 테이블은 빈 크기의 *제곱*으로 만들 수 있으며, 이는 높은 확률로 충돌이 없도록 유지한다.

---
layout: prism
heading: "완전 해싱 — 예시"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- 첫 번째 해시 테이블은 10개의 빈을 가진다:
  - 빈 1, 3, 5, 7은 비어 있다.
  - 빈 0, 4, 8은 원소 하나를 가지며 — 두 번째 테이블은 위치 하나를 갖는다.
  - 빈 2, 6은 원소 둘을 가지며 — 두 번째 테이블은 위치 넷을 갖는다.
  - 빈 9는 원소 셋을 가지며 — 두 번째 테이블은 위치 아홉을 갖는다.

- 각 두 번째 테이블은 충돌이 없어질 때까지 서로 다른 해시 함수로 구성된다. 이 방식이 [완전 해싱]{.hl}<sup>perfect hashing</sup>이다.
  - 두 번째 크기 $= (\text{빈 크기})^2$.

</div>
<div>

<div style="height: 0rem;"></div>

| 빈 | 원소 | 2차 테이블 크기 |
|:---:|:-----:|:--------------:|
| 0 | 1 | 1 |
| 2 | 2 | 4 |
| 4 | 1 | 1 |
| 6 | 2 | 4 |
| 8 | 1 | 1 |
| 9 | 3 | 9 |

</div>
</div>

---
layout: prism
heading: "뻐꾸기 해싱 — 아이디어"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- [뻐꾸기 해싱]{.hl}<sup>cuckoo hashing</sup>에서, $N$개의 원소와 (각각 절반 이상 비어 있는) *두* 개의 테이블, 그리고 각 원소에 한 테이블에서의 위치를 배정하는 두 개의 독립적인 해시 함수를 가진다고 하자.
  - 불변식: 원소는 항상 두 위치 중 하나에 저장되므로, `find`는 오직 *두* 개의 셀만 확인한다 — 최악의 경우 $\mathcal{O}(1)$.

- 알고리즘 자체는 단순하다:
  - 새 원소 $A$를 삽입하려면, 먼저 이미 존재하지 않는지 확인한다.
  - 첫 번째 해시 함수를 사용하여, 그 첫 번째 테이블 위치가 비어 있으면 원소를 놓는다.
  - 이후의 원소 $B$가 이미 찬 위치로 가야 한다면, $B$가 그 자리를 *선점*하여 $A$를 밀어내며, $A$는 자신의 두 번째 해시 위치를 사용해 두 번째 테이블로 이동한다.

- 밀려난 원소는 다시 또 다른 원소를 밀어낼 수 있다 — 마치 뻐꾸기 새끼가 다른 새끼들을 둥지 밖으로 밀어내듯이.

---
layout: prism
heading: "뻐꾸기 해싱 — 순환"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem; grid-template-columns: 1.2fr 1fr;">
<div>

- $A{:}(0,2)$, $B{:}(0,0)$, $C{:}(1,4)$, $D{:}(1,0)$, $E{:}(3,2)$, $F{:}(3,4)$를 삽입하면 오른쪽의 두 테이블을 얻는다 ($X{:}(y,z)$는 $X$의 두 해시 위치를 나타낸다).

- 이제 $G{:}(1,2)$를 삽입하면 원소들이 *끝없이* 밀려나고, 대체되고, 다시 밀려나게 된다 — 이것이 [순환]{.hl}<sup>cycle</sup>이다.

- 핵심 질문: 순환이 생길 확률은 얼마이며, 성공적인 삽입을 위한 밀어내기 횟수의 기댓값은 얼마인가?
  - 적재율이 $0.5$ 미만이면 순환은 매우 드물다; $0.5$ 이상이면 순환 가능성이 급격히 커지고 뻐꾸기 해싱은 잘 동작하지 않는다.

</div>
<div>

<div style="height: 0.5rem;"></div>

<div class="grid grid-cols-2 gap-3">
<div>

| Table 1 | |
|:---:|:---:|
| 0 | $A$ |
| 1 | $D$ |
| 2 | |
| 3 | $F$ |
| 4 | |

</div>
<div>

| Table 2 | |
|:---:|:---:|
| 0 | $B$ |
| 1 | |
| 2 | $E$ |
| 3 | |
| 4 | $C$ |

</div>
</div>

</div>
</div>

---
layout: prism
heading: "DIY: 개별 체이닝"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <list>
using namespace std;

const int TS = 10;
int myhash(int x) { return x % TS; }        // hash(x) = x mod 10

int main() {
    vector<list<int>> table(TS);
    int keys[] = {89, 18, 49, 58, 69};

    for (int k : keys) {                      // 체인의 앞에 삽입
        auto& L = table[myhash(k)];
        L.push_front(k);
    }
    for (int i = 0; i < TS; i++) {            // 각 슬롯의 체인 출력
        cout << i << ":";
        for (int v : table[i]) cout << " -> " << v;
        cout << "\n";
    }
    int target = 58;                          // find(58)
    auto& L = table[myhash(target)];
    bool found = false;
    for (int v : L) if (v == target) found = true;
    cout << "find(" << target << ") = " << (found ? "true" : "false") << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY: 선형 조사"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int TS = 10;                            // 테이블 크기

int main() {
    vector<int> table(TS, -1);                // -1은 빈 슬롯을 표시
    int keys[] = {89, 18, 49, 58, 69};

    for (int k : keys) {                       // f(i) = i : 선형 조사
        int pos = k % TS, probes = 0;
        while (table[pos] != -1) { pos = (pos + 1) % TS; probes++; }
        table[pos] = k;
        cout << "insert " << k << " -> slot " << pos
             << " (" << probes << " collision(s))\n";
    }

    cout << "---- final table ----\n";
    for (int i = 0; i < TS; i++)
        cout << i << ": " << (table[i] == -1 ? string("-") : to_string(table[i])) << "\n";

    int t = 58, pos = t % TS, steps = 0;       // find(58)
    while (table[pos] != -1 && table[pos] != t) { pos = (pos + 1) % TS; steps++; }
    cout << "find(" << t << ") -> " << (table[pos] == t ? "found" : "missing")
         << " after " << steps << " probe(s)" << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY_W12: 다양한 해싱 알고리즘"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 오늘 다룬 것 외에도 더 진보된 해싱 알고리즘이 많이 존재한다.

- [홉스코치 해싱]{.hl}<sup>Hopscotch hashing</sup>은 최대 조사 시퀀스 길이를 컴퓨터 구조에 최적화된 상수로 *제한*하여 고전적인 선형 조사를 개선한다.

- [보편 해싱]{.hl}<sup>Universal hashing</sup>은 해시 함수를 *무작위로* 선택하여, 원소들이 배열 슬롯 사이에 균일하게 분산됨을 증명 가능하게 보장한다.

- [확장성 해싱]{.hl}<sup>Extendible hashing</sup>은 탐색을 단 *두* 번의 디스크 접근으로 수행할 수 있게 한다 — 데이터가 디스크에 있을 때 유용하다.

- 이 알고리즘들을 찾아 공부해 보시오.

---
layout: prism
heading: "HW_W12: 코딩 테스트 풀어보기"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 우리는 다양한 자료구조를 공부했고, 이제 프로그래밍할 준비가 되었습니다.

- *세 개의* 코딩 테스트 문제를 선택해서 풀어 보세요.
  - 웹사이트, 책 등에서 문제를 가져와도 됩니다.

- 각 문제와 여러분의 답을 함께 복사해서 붙여넣으세요.
  - *스스로* 풀어 보세요; 문제가 너무 어렵다면 부정행위를 하기보다는 빈칸으로 남겨 두세요.

- PDF 파일을 `20XXXXXX_HW_W12.pdf`로 LMS에 업로드하세요.

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
