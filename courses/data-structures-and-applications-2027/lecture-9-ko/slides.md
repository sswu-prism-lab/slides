---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 9 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-9/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">자료구조실습</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">9주차: 정렬 알고리즘 (복습)</p>

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
heading: "요약: 정렬 알고리즘"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 이번 강의에서는 지금까지 다룬 정렬 알고리즘들을 [복습]{.hl}하며, 각 알고리즘을 한 단계씩 따라가고 동작하는 C++ 구현을 직접 실행해 봅니다.

- 첫 번째 그룹은 원소를 서로 비교하기만 해서 순서를 정하는 [비교 기반]{.hl} 정렬입니다:

<div class="sub-item">

[선택]{.hl}, [버블]{.hl}, [삽입]{.hl}, [병합]{.hl}, [퀵]{.hl}, [힙]{.hl}, [셸]{.hl} 정렬.

</div>

- 두 번째 그룹은 데이터의 [특성]{.hl}(값의 범위나 자릿수 구조)을 활용하여 $O(N \log N)$ 이라는 비교 정렬의 하한을 뛰어넘습니다:

<div class="sub-item">

[계수]{.hl}, [기수]{.hl}, [버킷]{.hl} 정렬.

</div>

---
layout: prism
heading: "선택 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 매 회마다 아직 자리가 정해지지 않은 원소들 중에서 [최댓값을 선택]{.hl}하여 정렬되지 않은 구간의 가장 뒤로 보냅니다.

- 최댓값을 마지막 자리에 놓은 뒤에는 그 자리를 제외하고, 줄어든 앞부분에 대해 같은 과정을 반복합니다.

- 매 회마다 정렬되지 않은 구간 전체를 훑기 때문에, 입력과 무관하게 수행 시간은 $O(N^2)$ 입니다.

<div class="theorem-box">
<div class="theorem-box-title">한 회의 진행</div>
<div class="theorem-box-body">

`8 31 48 15 3 11 20 29 65 73` → 최댓값 `73` 이 이미 마지막에 있으므로, 다음 회에서는 `65` 를, 그 다음에는 `48` 을 놓는 식으로 진행됩니다.

</div>
</div>

---
layout: prism
heading: "DIY: 선택 정렬"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArr(const vector<int>& a) { for (int x : a) cout << x << ' '; cout << '\n'; }

int main() {
    vector<int> a = {8, 31, 48, 15, 3, 11, 20, 29, 65, 73};
    int n = a.size();
    cout << "Initial: "; printArr(a);
    for (int last = n - 1; last > 0; --last) {
        int maxIdx = 0;                          // a[0..last] 에서 최댓값 찾기
        for (int i = 1; i <= last; ++i)
            if (a[i] > a[maxIdx]) maxIdx = i;
        swap(a[maxIdx], a[last]);                // 가장 뒤로 보냄
        cout << "max -> pos " << last << ": "; printArr(a);
    }
    cout << "Sorted:  "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "버블 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 리스트를 [왼쪽에서 오른쪽으로]{.hl} 훑으며, 인접한 두 원소를 차례로 비교합니다.

- 왼쪽 원소가 오른쪽 원소보다 크면 서로 [교환]{.hl}합니다. 가장 큰 원소가 마치 거품처럼 점차 끝으로 "떠오르게" 됩니다.

- 한 회를 마칠 때마다 마지막(가장 큰) 원소가 제자리에 놓이고 다음 회에서는 제외됩니다. 수행 시간은 $O(N^2)$ 입니다.

<div class="theorem-box">
<div class="theorem-box-title">첫 번째 회</div>
<div class="theorem-box-body">

`8 31 48 73 3 65 20 29 11 15` 에서 시작하면, 값 `73` 이 자기보다 작은 이웃들을 모두 지나 오른쪽으로 이동하여 마지막 칸에 도달합니다.

</div>
</div>

---
layout: prism
heading: "DIY: 버블 정렬"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArr(const vector<int>& a) { for (int x : a) cout << x << ' '; cout << '\n'; }

int main() {
    vector<int> a = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    int n = a.size();
    cout << "Initial: "; printArr(a);
    for (int pass = 0; pass < n - 1; ++pass) {
        bool swapped = false;
        for (int i = 0; i < n - 1 - pass; ++i)       // 인접한 쌍 비교
            if (a[i] > a[i + 1]) { swap(a[i], a[i + 1]); swapped = true; }
        cout << "after pass " << pass + 1 << ": "; printArr(a);
        if (!swapped) break;                          // 이미 정렬됨
    }
    cout << "Sorted:  "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "삽입 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 리스트의 앞부분을 [정렬된]{.hl} 상태로 유지하며, 한 번에 한 원소씩 그 부분을 늘려 나갑니다.

- 다음 원소를 추가하려면, 정렬된 앞부분에서 그보다 큰 원소들을 모두 한 칸씩 [오른쪽]{.hl}으로 밀고, 생긴 빈자리에 새 원소를 넣습니다.

- 최악의 경우 $O(N^2)$ 이지만, 거의 정렬된 데이터에서는 매우 빠릅니다.

<div class="theorem-box">
<div class="theorem-box-title">7번째 원소 삽입하기</div>
<div class="theorem-box-body">

`3 8 31 48 65 73` 이 이미 정렬된 상태에서 `20` 을 삽입하면, `31 48 65 73` 이 오른쪽으로 밀리고 `20` 이 `8` 바로 뒤에 놓입니다.

</div>
</div>

---
layout: prism
heading: "DIY: 삽입 정렬"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArr(const vector<int>& a) { for (int x : a) cout << x << ' '; cout << '\n'; }

int main() {
    vector<int> a = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    int n = a.size();
    cout << "Initial: "; printArr(a);
    for (int i = 1; i < n; ++i) {
        int key = a[i], j = i - 1;
        while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; --j; }  // 큰 원소들을 오른쪽으로 밀기
        a[j + 1] = key;                                          // 빈자리에 key 삽입
        cout << "insert " << key << ": "; printArr(a);
    }
    cout << "Sorted:  "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "병합 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [분할 정복]{.hl} 방식의 정렬입니다: `A[p..r]` 을 중간 지점 `q` 에서 나누고, 두 절반을 재귀적으로 정렬한 뒤 [병합]{.hl}합니다.

- 병합 과정에서는 두 절반을 가리키는 포인터 `i` 와 `j` 를 옮겨 가며, 더 작은 앞쪽 원소를 임시 버퍼 `tmp[]` 로 복사하고, 그런 다음 `tmp[]` 를 다시 되돌려 복사합니다.

- 분할이 항상 균등하게 이루어지므로, 병합 정렬은 [모든]{.hl} 입력에 대해 $O(N \log N)$ 시간에 동작합니다.

<div class="theorem-box">
<div class="theorem-box-title">정렬된 두 절반 병합하기</div>
<div class="theorem-box-body">

`3 8 31 48 73` 과 `11 15 20 29 65` 가 `3 8 11 15 20 29 31 48 65 73` 으로 병합됩니다.

</div>
</div>

---
layout: prism
heading: "DIY: 병합 정렬"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArr(const vector<int>& a) { for (int x : a) cout << x << ' '; cout << '\n'; }

void merge(vector<int>& a, int p, int q, int r) {
    vector<int> tmp;
    int i = p, j = q + 1;
    while (i <= q && j <= r) tmp.push_back(a[i] <= a[j] ? a[i++] : a[j++]);
    while (i <= q) tmp.push_back(a[i++]);
    while (j <= r) tmp.push_back(a[j++]);
    for (int k = 0; k < (int)tmp.size(); ++k) a[p + k] = tmp[k];
}

void mergeSort(vector<int>& a, int p, int r) {
    if (p >= r) return;
    int q = (p + r) / 2;
    mergeSort(a, p, q);
    mergeSort(a, q + 1, r);
    merge(a, p, q, r);
    cout << "merge [" << p << "," << r << "]: "; printArr(a);
}

int main() {
    vector<int> a = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    cout << "Initial: "; printArr(a);
    mergeSort(a, 0, a.size() - 1);
    cout << "Sorted:  "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "퀵 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [피벗]{.hl}을 하나 고른 뒤, 피벗보다 작은 원소는 모두 앞에, 큰 원소는 모두 뒤에 오도록 리스트를 [분할]{.hl}합니다.

- 이제 피벗은 최종 위치에 놓였으므로, 왼쪽과 오른쪽 분할에 대해 재귀적으로 반복합니다.

- 분할은 $O(N)$ 이며, 분할이 균등하다면 평균 총비용은 $O(N \log N)$ 입니다(최악의 경우 $O(N^2)$).

<div class="theorem-box">
<div class="theorem-box-title">분할 단계</div>
<div class="theorem-box-body">

두 인덱스 `i` 와 `j` 가 안쪽으로 이동하면서, 피벗을 기준으로 잘못된 쪽에 있는 원소들을 서로 교환합니다.

</div>
</div>

---
layout: prism
heading: "DIY: 퀵 정렬"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArr(const vector<int>& a) { for (int x : a) cout << x << ' '; cout << '\n'; }

int partition(vector<int>& a, int lo, int hi) {
    int pivot = a[hi], i = lo - 1;
    for (int j = lo; j < hi; ++j)
        if (a[j] < pivot) { ++i; swap(a[i], a[j]); }
    swap(a[i + 1], a[hi]);
    return i + 1;
}

void quickSort(vector<int>& a, int lo, int hi) {
    if (lo >= hi) return;
    int p = partition(a, lo, hi);
    cout << "pivot " << a[p] << ": "; printArr(a);
    quickSort(a, lo, p - 1);
    quickSort(a, p + 1, hi);
}

int main() {
    vector<int> a = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    cout << "Initial: "; printArr(a);
    quickSort(a, 0, a.size() - 1);
    cout << "Sorted:  "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "힙 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 먼저 배열을 [최대 힙]{.hl}으로 재배치하여, 가장 큰 원소가 루트(인덱스 0)에 오도록 합니다.

- 루트를 힙의 [마지막]{.hl} 원소와 반복적으로 교환하고, 힙의 크기를 하나 줄인 뒤, 새로운 루트를 [아래로 내려보내며]{.hl} 힙 성질을 회복시킵니다.

- 힙을 만드는 데 $O(N)$, 그리고 $N$ 번의 제거가 각각 $O(\log N)$ 이 들므로, 힙 정렬은 $O(N \log N)$ 입니다.

<div class="theorem-box">
<div class="theorem-box-title">힙으로서의 배열</div>
<div class="theorem-box-body">

인덱스 `i` 에 대해 자식은 `2i+1` 과 `2i+2` 에 위치합니다. 아래로 내려보내기는 노드를 더 큰 자식과 반복적으로 교환합니다.

</div>
</div>

---
layout: prism
heading: "DIY: 힙 정렬"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArr(const vector<int>& a) { for (int x : a) cout << x << ' '; cout << '\n'; }

void siftDown(vector<int>& a, int i, int n) {
    while (true) {
        int l = 2 * i + 1, r = 2 * i + 2, large = i;
        if (l < n && a[l] > a[large]) large = l;
        if (r < n && a[r] > a[large]) large = r;
        if (large == i) break;
        swap(a[i], a[large]);
        i = large;
    }
}

int main() {
    vector<int> a = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    int n = a.size();
    cout << "Initial:  "; printArr(a);
    for (int i = n / 2 - 1; i >= 0; --i) siftDown(a, i, n);   // 최대 힙 구성
    cout << "Max-heap: "; printArr(a);
    for (int end = n - 1; end > 0; --end) {
        swap(a[0], a[end]);                                   // 가장 큰 원소를 뒤로
        siftDown(a, 0, end);
    }
    cout << "Sorted:   "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "셸 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 셸 정렬은 [간격]{.hl} `h` 를 이용해 삽입 정렬을 일반화합니다: `h` 만큼 떨어진 원소들로 이루어진 부분 수열을 삽입 정렬합니다.

- 큰 간격에서 시작하면 멀리 떨어진 원소들이 빠르게 이동할 수 있으며, 간격은 `h = 1` 까지 점점 [줄어들어]{.hl}, 마지막 삽입 정렬이 거의 정렬된 리스트에 대해 작업을 마무리합니다.

- 수행 시간은 간격 수열에 따라 달라지지만, 실제로는 단순 삽입 정렬보다 훨씬 낫습니다.

<div class="theorem-box">
<div class="theorem-box-title">간격 수열</div>
<div class="theorem-box-body">

여기서는 `h = 3` 다음에 `h = 1` 을 사용합니다. `h = 3` 회를 마치면 리스트는 "3-정렬" 상태가 되고, 마지막 `h = 1` 회가 정렬을 완성합니다.

</div>
</div>

---
layout: prism
heading: "DIY: 셸 정렬"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArr(const vector<int>& a) { for (int x : a) cout << x << ' '; cout << '\n'; }

int main() {
    vector<int> a = {3, 20, 48, 11, 1, 33, 29, 4, 31, 65, 73, 8, 66, 25, 15};
    int n = a.size();
    cout << "Initial: "; printArr(a);
    for (int h = 3; h >= 1; h -= 2) {                 // 간격 3, 그다음 1
        for (int i = h; i < n; ++i) {
            int key = a[i], j = i;
            while (j >= h && a[j - h] > key) { a[j] = a[j - h]; j -= h; }
            a[j] = key;
        }
        cout << "h = " << h << ":   "; printArr(a);
    }
    cout << "Sorted:  "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "데이터 특성을 이용하는 정렬 알고리즘"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 비교 정렬은 오직 비교를 통해서만 데이터에 대한 정보를 얻기 때문에 $\Omega(N \log N)$ 을 뛰어넘을 수 없습니다.

- 데이터에 대해 무언가를 더 알고 있을 때 — 작은 정수 [범위]{.hl}, 고정된 [자릿수]{.hl}, 또는 균등한 [분포]{.hl} — 우리는 [선형 시간]{.hl}에 정렬할 수 있습니다.

- 이제 그런 알고리즘 세 가지를 복습합니다:

<div class="sub-item">

[계수 정렬]{.hl}(작은 정수 범위), [기수 정렬]{.hl}(고정 너비 키), [버킷 정렬]{.hl}(균등하게 분포된 값).

</div>

---
layout: prism
heading: "계수 정렬 — 아이디어"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 계수 정렬은 각 원소가 작은 범위 $\{0, 1, \ldots, k\}$ 안의 정수라고 가정합니다.

- [카운트 배열]{.hl} `C` 를 사용하여 세 단계로 동작합니다:

<div class="sub-item-enum">

1. 각 값이 몇 번 나타나는지 셉니다: `C[i]` = 값이 `i` 인 원소의 개수.
2. `C` 를 [누적합]{.hl}으로 바꾸어, `C[i]` 가 값이 $\leq i$ 인 원소의 개수가 되게 합니다 — 이것이 바로 값 `i` 의 최종 위치 경계입니다.
3. 입력을 [뒤에서부터]{.hl} 훑으며, 각 원소를 `B[C[value] - 1]` 에 놓고 `C[value]` 를 하나 줄입니다. 뒤에서부터 훑으면 정렬이 [안정적으로]{.hl} 유지됩니다.

</div>

- 범위 크기가 `k` 이고 원소가 `n` 개일 때, 총비용은 $O(n + k)$ 입니다.

---
layout: prism
heading: "계수 정렬 — 의사코드"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

```text
countingSort(A[0..n-1]):
  // A[i] in {0, 1, ..., k}
  for i <- 0 to k
      C[i] <- 0
  for j <- 0 to n-1
      C[A[j]]++
  for i <- 1 to k
      C[i] <- C[i] + C[i-1]
  for j <- n-1 downto 0
      B[C[A[j]] - 1] <- A[j]
      C[A[j]]--
  return B
```

</div>
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 두 번째 반복문은 `A` 에서 각 값 `0..k` 가 몇 번 나타나는지를 `C[0..k]` 에 셉니다.

- 세 번째 반복문은 `C[i]` 가 `i` 보다 작거나 같은 원소의 개수를 갖도록 만듭니다.

- 마지막 반복문은 `C` 를 이용해 `A` 의 각 원소가 `B` 에서 들어갈 목적지 자리를 계산합니다.

</div>
</div>

---
layout: prism
heading: "DIY: 계수 정렬"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 임의의 정수 범위 [min, max] 에 대한 계수 정렬
void countingSort(vector<int>& A) {
    int n = A.size();
    int maxElement = *max_element(A.begin(), A.end());
    int minElement = *min_element(A.begin(), A.end());
    int k = maxElement - minElement + 1;
    vector<int> C(k, 0), B(n);
    for (int j = 0; j < n; j++) C[A[j] - minElement]++;      // 등장 횟수 세기
    for (int i = 1; i < k; i++) C[i] += C[i - 1];            // 누적합
    for (int j = n - 1; j >= 0; j--) {                       // 안정적으로 배치
        B[C[A[j] - minElement] - 1] = A[j];
        C[A[j] - minElement]--;
    }
    for (int i = 0; i < n; i++) A[i] = B[i];                 // 다시 복사
}

void printArray(const vector<int>& arr) {
    for (size_t i = 0; i < arr.size(); i++) cout << arr[i] << " ";
    cout << endl;
}

int main() {
    vector<int> arr = {1, 5, 3, 3, 5, 2, 1, 5, 3, 4};
    cout << "Original array: "; printArray(arr);
    countingSort(arr);
    cout << "Sorted array:   "; printArray(arr);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "기수 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 기수 정렬은 최대 `k` 자릿수의 수들을, [가장 낮은]{.hl} 자릿수부터 가장 높은 자릿수까지 [한 자리씩]{.hl} 정렬하여 순서를 정합니다.

- 각 한 자리 정렬은 반드시 [안정]{.hl} 정렬이어야 하며 — 같은 키는 이전의 상대적 순서를 유지 — 그래야 앞선 자릿수에서 한 작업이 보존됩니다.

<div class="sub-item">

한 자릿수에 대한 안정 정렬은 정확히 범위 `0..9` 의 계수 정렬이며, $O(N)$ 이 듭니다.

</div>

- `N` 개의 수에 대해 `k` 번의 자릿수 정렬을 하므로, 총비용은 $O(k \cdot N)$, 즉 `k` 가 상수일 때 선형입니다.

---
layout: prism
heading: "DIY: 기수 정렬"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArr(const vector<int>& a) { for (int x : a) cout << x << ' '; cout << '\n'; }

// 'exp'(1, 10, 100, ...) 로 선택된 자릿수에 대한 안정 계수 정렬
void countingByDigit(vector<int>& a, int exp) {
    int n = a.size();
    vector<int> out(n), C(10, 0);
    for (int i = 0; i < n; i++) C[(a[i] / exp) % 10]++;
    for (int i = 1; i < 10; i++) C[i] += C[i - 1];
    for (int i = n - 1; i >= 0; i--) {
        int d = (a[i] / exp) % 10;
        out[C[d] - 1] = a[i];
        C[d]--;
    }
    a = out;
}

int main() {
    vector<int> a = {123, 2154, 222, 4, 283, 1560, 1061, 2150};
    cout << "Initial:      "; printArr(a);
    for (int exp = 1; exp <= 1000; exp *= 10) {   // 4자리 수
        countingByDigit(a, exp);
        cout << "by digit " << exp << ":  "; printArr(a);
    }
    cout << "Sorted:       "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "버킷 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 버킷 정렬은 입력이 `[0, 1)` 범위에 [균등하게 분포된]{.hl} `n` 개의 실수값이라고 가정합니다.

- 각 값 `A[i]` 를 버킷 `B[⌊n·A[i]⌋]` 에 흩뿌린 뒤, 각 버킷을 정렬하고(예: 삽입 정렬), 버킷들을 다시 `A` 로 이어 붙입니다.

- 값이 고르게 퍼져 있으면 각 버킷에 원소가 몇 개밖에 담기지 않아, 기댓값 기준 수행 시간이 $O(N)$ 이 됩니다.

<div class="theorem-box">
<div class="theorem-box-title">예시</div>
<div class="theorem-box-body">

값이 15개일 때, `0.38` 은 버킷 `⌊15 · 0.38⌋ = 5` 로, `0.94` 는 버킷 `14` 로 가는 식입니다. 각 버킷은 독립적으로 정렬됩니다.

</div>
</div>

---
layout: prism
heading: "DIY: 버킷 정렬"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    vector<double> a = {.38, .94, .48, .73, .99, .43, .55, .15,
                        .85, .84, .81, .71, .17, .10, .02};
    int n = a.size();
    cout << fixed << setprecision(2);
    cout << "Initial:";
    for (double x : a) cout << ' ' << x;
    cout << '\n';

    vector<vector<double>> B(n);                 // n개의 버킷
    for (double x : a) B[(int)(n * x)].push_back(x);

    int idx = 0;
    for (int i = 0; i < n; i++) {
        sort(B[i].begin(), B[i].end());          // 각 버킷 정렬
        for (double x : B[i]) a[idx++] = x;      // 이어 붙이기
    }

    cout << "Sorted: ";
    for (double x : a) cout << ' ' << x;
    cout << '\n';
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "과제: 개선된 버킷 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 소박한 버킷 정렬은 각 버킷 안에 연결 리스트를 만들어, 데이터가 한쪽으로 치우치면 공간이 부족해지는 경우가 많습니다.

- [버킷을 물리적으로 유지하지 않고]{.hl}(연결 리스트를 전혀 만들지 않고) 구현할 수 있는 방법이 있으며 — 그 아이디어를 활용하면 퀵 정렬보다도 빨라질 수 있습니다.

<div class="sub-item">

계수 정렬이 개별 값을 센다면, 버킷 정렬은 특정 [범위]{.hl}의 값을 셉니다. 그 개수로부터 각 버킷의 원소들이 차지할 `A[0..n-1]` 의 정확한 구간을 계산하여, 원소를 별도의 버킷이 아닌 `A` 에 [직접]{.hl} 넣을 수 있습니다.

</div>

- 이 개선된 버킷 정렬을 구현해 보세요. `HW_W09_20XXXXXX.cpp` 로 저장한 뒤 LMS에 업로드하세요.

---
layout: prism
heading: "실습: K번째 수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `array` 가 주어졌을 때, 각 명령 `[i, j, k]` 에 대해: `i` 번째부터 `j` 번째까지의 구간(1-인덱스)을 잘라 정렬한 뒤, 그 `k` 번째 원소를 구합니다.

- `array = [1,5,2,6,3,7,4]` 이고 명령이 `[2,5,3]` 일 때: 구간 `[5,2,6,3]` 을 정렬하면 `[2,3,5,6]` 이 되고, 그 3번째 원소는 `5` 입니다.

- 모든 명령에 대한 답을 반환합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array,
                     vector<vector<int>> commands) {
    vector<int> answer;
    for (auto& c : commands) {
        int i = c[0], j = c[1], k = c[2];
        vector<int> sub(array.begin() + i - 1,
                        array.begin() + j);
        sort(sub.begin(), sub.end());
        answer.push_back(sub[k - 1]);
    }
    return answer;
}

int main() {
    vector<int> array = {1, 5, 2, 6, 3, 7, 4};
    vector<vector<int>> commands =
        {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
    for (int x : solution(array, commands))
        cout << x << ' ';        // 5 6 3
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: 가장 큰 수"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 음이 아닌 정수들이 주어졌을 때, 이들을 적절한 순서로 이어 붙여 만들 수 있는 [가장 큰]{.hl} 수를 문자열로 반환합니다.

- 사용자 정의 규칙으로 수들을 정렬합니다: 문자열 `a+b` 가 `b+a` 보다 크면 `a` 가 `b` 앞에 옵니다.

- 예외 처리: 가장 큰 자릿수가 `0` 이면 모든 수가 `0` 이므로, `"0"` 을 반환합니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string solution(vector<int> numbers) {
    vector<string> s;
    for (int n : numbers) s.push_back(to_string(n));
    sort(s.begin(), s.end(),
         [](const string& a, const string& b) {
             return a + b > b + a;
         });
    if (s[0] == "0") return "0";
    string ans;
    for (auto& x : s) ans += x;
    return ans;
}

int main() {
    cout << solution({6, 10, 2}) << endl;      // 6210
    cout << solution({3, 30, 34, 5, 9}) << endl; // 9534330
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "실습: H-Index"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [H-Index]{.hl} `h` 는 연구자가 `h` 번 이상 인용된 논문을 `h` 편 이상 가지고 있는 최대 값입니다.

- 인용 횟수를 [내림차순]{.hl}으로 정렬하면, 답은 `citations[i-1] >= i` 를 만족하는 가장 큰 `i` 입니다.

- `citations = [3,0,6,1,5]` 일 때, 3편의 논문이 3회 이상 인용되었으므로 H-Index는 `3` 입니다.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> citations) {
    sort(citations.rbegin(), citations.rend());
    int h = 0;
    for (int i = 0; i < (int)citations.size(); i++)
        if (citations[i] >= i + 1) h = i + 1;
    return h;
}

int main() {
    cout << solution({3, 0, 6, 1, 5}) << endl;  // 3
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
