---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 8 (KO)
download: true
info: |
  ## 자료구조실습 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-8/
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
.arr {
  display: flex;
  gap: 4px;
  margin: 0.35rem 0;
  font-family: 'JetBrains Mono', Consolas, monospace;
  align-items: center;
}
.arr .lbl {
  min-width: 12rem;
  font-family: seriph, serif;
  color: #6b7280;
  font-size: 0.85rem;
  text-align: right;
  padding-right: 0.6rem;
}
.arr .c {
  min-width: 2.1rem;
  text-align: center;
  padding: 0.22rem 0;
  border: 1px solid #94a3b8;
  border-radius: 5px;
  font-size: 0.95rem;
}
.arr .hlmax { background: #5c60a8; color: #fff; border-color: #5c60a8; }
.arr .done  { background: #d9e0f2; color: #3a3f6b; border-color: #a7b0d8; }
</style>

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.png" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">자료구조실습</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">8주차: 정렬 알고리즘</p>

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
heading: 정렬 문제
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 아주 다양한 문제를 해결하기 위해 우리는 [정렬]{.hl} 알고리즘에 의존합니다:
  - *입력:* $n$개의 수로 이루어진 수열 $(a_1, a_2, \ldots, a_n)$.
  - *출력:* 입력을 재배열한 순열 $(a_1', a_2', \ldots, a_n')$ 로, $a_1' \leq a_2' \leq \cdots \leq a_n'$ 를 만족.

- 입력은 보통 $n$개 원소를 담은 배열이지만, 연결 리스트처럼 다른 방식으로 표현될 수도 있습니다.

- 많은 컴퓨터 과학자들은 정렬을 알고리즘 연구에서 [가장 근본적인 문제]{.hl}로 여깁니다:
  - 응용 문제 자체가 정보 정렬을 필요로 하는 경우가 많고, 알고리즘도 정렬을 핵심 서브루틴으로 자주 사용합니다;
  - 여러 중요한 설계 기법과 공학적 트레이드오프가 정렬 알고리즘에서 처음 등장합니다.

---
layout: prism
heading: 10가지 정렬 알고리즘, 세 그룹
---

<div class="absolute left-8 right-8" style="top: 6.5rem;">

우리는 성질에 따라 세 그룹으로 분류한 [10가지 정렬 알고리즘]{.hl}을 배웁니다. 이번 주(W08)에는 앞의 두 그룹을 다루고, 특수 그룹은 이후에 다룹니다.

<div class="grid grid-cols-3 gap-6" style="margin-top: 2.2rem;">
<div>
  <div style="background:#3f6f8f; color:#fff; text-align:center; padding:0.7rem; border-radius:8px; font-weight:600;">쉬운 알고리즘</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.9rem;">선택 정렬</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.7rem;">버블 정렬</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.7rem;">삽입 정렬</div>
  <p style="text-align:center; margin-top:1.4rem; color:#5c60a8; font-weight:600;">$\mathcal{O}(N^2)$</p>
</div>
<div>
  <div style="background:#3f6f8f; color:#fff; text-align:center; padding:0.7rem; border-radius:8px; font-weight:600;">범용 알고리즘</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.9rem;">병합 정렬</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.7rem;">퀵 정렬</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.7rem;">힙 정렬</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.7rem;">셸 정렬</div>
  <p style="text-align:center; margin-top:0.9rem; color:#5c60a8; font-weight:600;">$\mathcal{O}(N \log N)$</p>
</div>
<div>
  <div style="background:#8a9099; color:#fff; text-align:center; padding:0.7rem; border-radius:8px; font-weight:600;">특수 알고리즘</div>
  <div style="text-align:center; border:1px solid #d7d7d7; border-radius:6px; padding:0.5rem; margin-top:0.9rem; color:#9aa0a6;">계수 정렬</div>
  <div style="text-align:center; border:1px solid #d7d7d7; border-radius:6px; padding:0.5rem; margin-top:0.7rem; color:#9aa0a6;">기수 정렬</div>
  <div style="text-align:center; border:1px solid #d7d7d7; border-radius:6px; padding:0.5rem; margin-top:0.7rem; color:#9aa0a6;">버킷 정렬</div>
  <p style="text-align:center; margin-top:1.4rem; color:#9aa0a6; font-weight:600;">$\mathcal{O}(N)$ &nbsp;(추후)</p>
</div>
</div>

</div>

---
layout: prism
heading: 공통 테스트 배열
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 이 강의 전체에서 동일한 10개 원소 배열을 오름차순으로 정렬하여, 각 알고리즘이 목표에 도달하는 방식을 비교할 수 있게 합니다:

<div class="arr"><span class="lbl">A[…]</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>

<div class="arr"><span class="lbl">정렬된 A[…]</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

- 아래의 모든 알고리즘에는 중간 단계를 출력하는 실행 가능한 `<CppRunner>` 데모가 딸려 있어, 결과뿐 아니라 과정까지 눈으로 확인할 수 있습니다.

- 모든 데모는 현재 배열 상태를 출력하는 하나의 헬퍼를 공유합니다:

```cpp
void printArray(const vector<int>& a) {
    for (int x : a) cout << x << " ";
    cout << "\n";
}
```

---
layout: prism
heading: "선택 정렬 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [선택 정렬]{.hl} (selection sort)은 가장 쉬운 정렬 알고리즘 중 하나입니다.

- 정렬되지 않은 영역에서 [최댓값]{.hl} 원소를 반복적으로 찾아 그 영역의 [마지막]{.hl} 위치와 교환합니다 (대칭적으로, 최솟값을 선택해 맨 앞에 두어도 됩니다).

- "최댓값 원소 찾기"는 부분 리스트의 크기에 비례하므로, 선택 정렬은 *임의의* 입력에 대해 $\mathcal{O}(N^2)$ 이 걸립니다.

</div>
<div>

<div style="height: 2.5rem;"></div>

```text
selectionSort(A[], n):
    // 정렬 안 된 영역을 줄여 나감
    for last ← n-1 downto 1:
        // A[0..last]의 최댓값 찾기
        m ← argmax(A[0..last])
        // 경계 위치로 이동
        swap(A[m], A[last])
```

</div>
</div>

---
layout: prism
heading: "선택 정렬 (2/3) — 추적"
---

<div style="margin-top: 1.4rem;">

<div class="arr"><span class="lbl">A[…]</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c hlmax">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">최댓값(73)을 마지막과 교환</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">15</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">마지막 제외하고 최댓값(65) 찾기</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">15</span><span class="c">3</span><span class="c hlmax">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">최댓값(65)을 마지막과 교환</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">15</span><span class="c">3</span><span class="c">11</span><span class="c">20</span><span class="c">29</span><span class="c done">65</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">… 반복 …</span><span class="c">8</span><span class="c">3</span><span class="c">11</span><span class="c">15</span><span class="c">20</span><span class="c">29</span><span class="c">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">정렬된 A[…]</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

</div>

<p style="margin-top: 1.4rem; color:#6b7280; font-size: 0.95rem;">매 패스마다 배열 오른쪽 끝에 원소 하나가 더 확정(음영 표시)됩니다.</p>

---
layout: prism
heading: "선택 정렬 (3/3) — DIY"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArray(const vector<int>& a) {
    for (int x : a) cout << x << " ";
    cout << "\n";
}

void selectionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = n - 1; i > 0; i--) {   // 정렬 안 된 영역의 경계
        int max_idx = i;                // 마지막을 최댓값으로 가정
        for (int j = 0; j < i; j++)     // A[0..i-1] 훑기
            if (arr[j] > arr[max_idx]) max_idx = j;
        swap(arr[max_idx], arr[i]);     // 최댓값을 경계에 놓기
        cout << "pass " << n - i << ": ";
        printArray(arr);
    }
}

int main() {
    vector<int> arr = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    cout << "Original: "; printArray(arr);
    selectionSort(arr);
    cout << "Sorted:   "; printArray(arr);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "버블 정렬 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [버블 정렬]{.hl} (bubble sort)은 선택 정렬과 비슷한 발상 — 최댓값을 끝으로 옮긴다 — 에 기반하지만 방식이 조금 다릅니다.

- 왼쪽에서 오른쪽으로 [인접한]{.hl} 원소를 비교하여 순서가 어긋날 때마다 교환하므로, 매 패스마다 가장 큰 원소가 마지막 위치로 "떠오릅니다".

- 한 패스 전체에서 교환이 한 번도 없으면 배열은 이미 정렬된 것이므로 조기 종료할 수 있습니다 (최선의 경우 $\mathcal{O}(N)$).

</div>
<div>

<div style="height: 2rem;"></div>

```text
bubbleSort(A[], n):
    for last ← n-1 downto 1:
        // 최댓값을 'last'로 떠올림
        for i ← 0 to last-1:
            if A[i] > A[i+1]:
                swap(A[i], A[i+1])
```

</div>
</div>

---
layout: prism
heading: "버블 정렬 (2/3) — 추적"
---

<div style="margin-top: 1.2rem;">

<div class="arr"><span class="lbl">A[…]</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">패스 1 이후 (73이 떠오름)</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">패스 2 이후 (65가 떠오름)</span><span class="c">8</span><span class="c">31</span><span class="c">3</span><span class="c">48</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span><span class="c done">65</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">… 반복 …</span><span class="c">3</span><span class="c">8</span><span class="c">20</span><span class="c">11</span><span class="c">15</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">정렬된 A[…]</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

</div>

<p style="margin-top: 1.4rem; color:#6b7280; font-size: 0.95rem;">인접 비교가 왼쪽에서 오른쪽으로 훑고 지나가며, 매 패스 후 최댓값 하나가 오른쪽 끝에 고정됩니다.</p>

---
layout: prism
heading: "버블 정렬 (3/3) — DIY"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArray(const vector<int>& a) {
    for (int x : a) cout << x << " ";
    cout << "\n";
}

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {        // 패스마다 최댓값 하나 확정
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++)  // 인접한 쌍 비교
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        cout << "pass " << i + 1 << ": ";
        printArray(arr);
        if (!swapped) break;                 // 이미 정렬됨: 조기 종료
    }
}

int main() {
    vector<int> arr = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    cout << "Original: "; printArray(arr);
    bubbleSort(arr);
    cout << "Sorted:   "; printArray(arr);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "삽입 정렬 (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [삽입 정렬]{.hl} (insertion sort)은 정렬된 접두부를 한 번에 원소 하나씩 키워 나갑니다.

- $i$번째 단계에서 원소 $A[0..i-1]$ 은 이미 정렬되어 있고, 새 원소 $A[i]$ 를 가져와 큰 원소들을 한 칸씩 오른쪽으로 밀면서 올바른 위치에 [삽입]{.hl}합니다.

- 입력이 [거의 정렬되어]{.hl} 있으면 이동이 거의 없어 삽입 정렬은 대략 $\mathcal{O}(N)$ 으로 동작합니다 — 셸 정렬이 나중에 이용하는 성질입니다.

</div>
<div>

<div style="height: 3.5rem;"></div>

```text
insertionSort(A[], n):
    for i ← 1 to n-1:
        // A[i]를 정렬된 접두부
        // A[0..i]에 삽입
        insert A[i] appropriately
```

</div>
</div>

---
layout: prism
heading: "삽입 정렬 (2/3) — 추적"
---

<div style="margin-top: 1.2rem;">

<div class="arr"><span class="lbl">A[…]</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">6개 원소 정렬됨 (접두부)</span><span class="c done">3</span><span class="c done">8</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span><span class="c hlmax">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">20 삽입 (31,48,65,73 밀기)</span><span class="c done">3</span><span class="c done">8</span><span class="c done">20</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">정렬된 A[…]</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

</div>

<p style="margin-top: 1.6rem; color:#6b7280; font-size: 0.95rem;">키(여기서는 20)보다 큰 원소는 모두 한 칸씩 오른쪽으로 밀려나 삽입할 자리를 만듭니다.</p>

---
layout: prism
heading: "삽입 정렬 (3/3) — DIY"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArray(const vector<int>& a) {
    for (int x : a) cout << x << " ";
    cout << "\n";
}

void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];             // 삽입할 원소
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {   // 큰 원소들을 오른쪽으로 밀기
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;             // 키를 제자리에 넣기
        cout << "insert arr[" << i << "]=" << key << ": ";
        printArray(arr);
    }
}

int main() {
    vector<int> arr = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    cout << "Original: "; printArray(arr);
    insertionSort(arr);
    cout << "Sorted:   "; printArray(arr);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "병합 정렬 (1/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 선택, 버블, 삽입 정렬은 모두 $\mathcal{O}(N^2)$ 이 걸려 대규모에서는 [실용적이지 않습니다]{.hl}. [병합 정렬]{.hl} (merge sort)은 최선과 최악 [양쪽]{.hl} 모두 $\mathcal{O}(N \log N)$ 이 걸립니다.

- 병합 정렬은 입력 리스트를 두 개의 반으로 [나누고]{.hl}, [각각 독립적으로 정렬]{.hl}한 뒤, 마지막에 [병합]{.hl}합니다.
  - 각 반쪽도 병합 정렬로 정렬되므로 이 알고리즘은 [재귀적]{.hl}입니다.

- 병합 정렬은 추가 배열 `tmp[…]` 가 필요하므로 [공간을 많이 씁니다]{.hl}.
  - 추가 공간이 필요 없는 정렬을 [제자리 정렬]{.hl} (in-place sorting, 내부 정렬)이라고 하는데, 병합 정렬은 제자리 정렬이 *아닙니다*.

---
layout: prism
heading: "병합 정렬 (2/4) — 분할과 병합"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `mergeSort` 는 중간 지점 `q` 에서 나눠 각 쪽을 재귀 호출한 뒤 `merge` 를 호출합니다.

- `merge` 는 두 개의 정렬된 구간을 인덱스 `i` 와 `j` 로 훑으며 항상 더 작은 앞쪽 원소를 `tmp` 로 복사하고, 그 다음 `tmp` 를 `A[p..r]` 로 되돌려 복사합니다.

</div>
<div>

```text
mergeSort(A[], p, r):
    if p < r:
        q ← (p+r)/2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

merge(A[], p, q, r):
    i ← p; j ← q+1; t ← 0
    while i ≤ q and j ≤ r:
        if A[i] ≤ A[j]: tmp[t++] ← A[i++]
        else:           tmp[t++] ← A[j++]
    copy leftovers, then tmp → A[p..r]
```

</div>
</div>

---
layout: prism
heading: "병합 정렬 (3/4) — 추적"
---

<div style="margin-top: 1.4rem;">

<div class="arr"><span class="lbl">A[…]</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">절반으로 나누기</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">각 절반 정렬</span><span class="c done">3</span><span class="c done">8</span><span class="c done">31</span><span class="c done">48</span><span class="c done">73</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">65</span></div>
<div class="arr"><span class="lbl">병합</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

</div>

<p style="margin-top: 1.6rem; color:#6b7280; font-size: 0.95rem;">두 개의 정렬된 구간(왼쪽 <code>3 8 31 48 73</code>, 오른쪽 <code>11 15 20 29 65</code>)을 더 작은 앞쪽 원소를 반복해서 취하며 합칩니다.</p>

---
layout: prism
heading: "병합 정렬 (4/4) — DIY"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArray(const vector<int>& a) {
    for (int x : a) cout << x << " ";
    cout << "\n";
}

void merge(vector<int>& arr, int p, int q, int r) {
    int n1 = q - p + 1, n2 = r - q;
    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[p + i];
    for (int j = 0; j < n2; j++) R[j] = arr[q + 1 + j];
    int i = 0, j = 0, k = p;
    while (i < n1 && j < n2)                     // 더 작은 앞쪽 원소 취하기
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < n1) arr[k++] = L[i++];            // 왼쪽 구간 잔여분
    while (j < n2) arr[k++] = R[j++];            // 오른쪽 구간 잔여분
}

void mergeSort(vector<int>& arr, int p, int r) {
    if (p < r) {
        int q = p + (r - p) / 2;
        mergeSort(arr, p, q);
        mergeSort(arr, q + 1, r);
        merge(arr, p, q, r);
        cout << "merge [" << p << "," << r << "]: ";
        printArray(arr);
    }
}

int main() {
    vector<int> arr = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    cout << "Original: "; printArray(arr);
    mergeSort(arr, 0, arr.size() - 1);
    cout << "Sorted:   "; printArray(arr);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "퀵 정렬 (1/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 병합 정렬은 작은 문제를 재귀적으로 풀고 나서 [후처리]{.hl}(병합)합니다. [퀵 정렬]{.hl} (quick sort)은 순서를 뒤집습니다: 먼저 [전처리]{.hl}한 다음, 작은 문제를 재귀적으로 풉니다.

- 퀵 정렬은 [기준]{.hl}(피벗) 원소를 고르고, 배열을 두 그룹 — 피벗보다 [작은]{.hl} 원소와 [크거나 같은]{.hl} 원소 — 으로 분할한 뒤, 각 그룹을 정렬합니다.

- 퀵 정렬은 평균적으로 $\mathcal{O}(N \log N)$ 이 걸립니다.
  - 최악의 경우는 $\mathcal{O}(N^2)$ 이지만(*언제* 그런지 생각해 보세요!), 퀵 정렬은 [실무에서 널리 쓰입니다]{.hl}.

---
layout: prism
heading: "퀵 정렬 (2/4) — 분할"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- `partition` 은 세 영역을 유지합니다: 영역 I (`< x`), 영역 II (`≥ x`), 영역 III (미결정).

- 인덱스 `i` 는 영역 I의 끝을 나타내고, `j` 는 영역 III를 훑습니다. `A[j] < x` 일 때마다 `A[++i]` 와 `A[j]` 를 교환하여 영역 I를 키웁니다.

- 마지막으로 피벗을 두 그룹의 경계인 위치 `i+1` 로 교환해 넣습니다.

</div>
<div>

```text
quickSort(A[], p, r):
    if p < r:
        q ← partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

partition(A[], p, r):
    x ← A[r]              // 피벗
    i ← p-1               // 영역 I의 끝
    for j ← p to r-1:
        if A[j] < x:
            swap(A[++i], A[j])
    swap(A[i+1], A[r])
    return i+1
```

</div>
</div>

---
layout: prism
heading: "퀵 정렬 (3/4) — 추적"
---

<div style="margin-top: 1.4rem;">

<div class="arr"><span class="lbl">A[…], 피벗 x = A[r] = 15</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c hlmax">15</span></div>
<div class="arr"><span class="lbl">15보다 작으면 왼쪽으로</span><span class="c done">8</span><span class="c done">3</span><span class="c done">11</span><span class="c hlmax">15</span><span class="c">31</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">48</span><span class="c">73</span></div>
<div class="arr"><span class="lbl">각 그룹을 재귀적으로 정렬</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

</div>

<p style="margin-top: 1.6rem; color:#6b7280; font-size: 0.95rem;">한 번의 분할 이후 피벗 15는 최종 위치에 놓이며, 왼쪽은 모두 더 작고 오른쪽은 모두 더 큽니다.</p>

---
layout: prism
heading: "퀵 정렬 (4/4) — DIY"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArray(const vector<int>& a) {
    for (int x : a) cout << x << " ";
    cout << "\n";
}

int partition(vector<int>& arr, int p, int r) {
    int x = arr[r];                 // 피벗 = 마지막 원소
    int i = p - 1;                  // "작은" 영역의 끝
    for (int j = p; j <= r - 1; j++)
        if (arr[j] < x)
            swap(arr[++i], arr[j]);
    swap(arr[i + 1], arr[r]);       // 피벗을 경계에 놓기
    return i + 1;
}

void quickSort(vector<int>& arr, int p, int r) {
    if (p < r) {
        int q = partition(arr, p, r);
        cout << "pivot " << arr[q] << " fixed at index " << q << ": ";
        printArray(arr);
        quickSort(arr, p, q - 1);
        quickSort(arr, q + 1, r);
    }
}

int main() {
    vector<int> arr = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    cout << "Original: "; printArray(arr);
    quickSort(arr, 0, arr.size() - 1);
    cout << "Sorted:   "; printArray(arr);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "힙 정렬 (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [힙 정렬]{.hl} (heap sort)은 정렬에 [힙]{.hl} 자료구조를 사용합니다.
  - 먼저 주어진 리스트로부터 [최대 힙을 만듭니다]{.hl}.
  - 그런 다음 [최댓값(루트)을 제거]{.hl}하고 아래로 내리는 작업을 원소 하나씩 반복합니다.

- 제거한 가장 큰 원소를 줄어드는 힙 경계 바로 뒤에 저장하면 배열이 [제자리에서]{.hl} 정렬됩니다.

- 힙 정렬은 최악의 경우 $\mathcal{O}(N \log N)$, 최선의 경우 $\mathcal{O}(N)$ 이 걸립니다.

---
layout: prism
heading: "힙 정렬 (2/3) — 만들기와 추출"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 배열을 완전 이진 트리로 봅니다: 노드 `i` 의 자식은 `2i+1` 과 `2i+2` 입니다.

- `buildHeap` (아래로 내리기)은 마지막 내부 노드부터 시작해 모든 서브트리를 최대 힙으로 만듭니다.

- 그런 다음 `n-1` 번, 루트(최댓값)를 마지막 힙 원소와 교환하고 줄어든 힙을 다시 힙 상태로 만듭니다.

</div>
<div>

```text
heapSort(A[]):
    buildHeap(A)              // max-heap
    for i ← n-1 downto 1:
        swap(A[0], A[i])      // max → end
        percolateDown(A, 0, i)

percolateDown(A, i, n):
    largest ← i
    l ← 2i+1;  r ← 2i+2
    if l<n and A[l]>A[largest]: largest ← l
    if r<n and A[r]>A[largest]: largest ← r
    if largest ≠ i:
        swap(A[i], A[largest])
        percolateDown(A, largest, n)
```

</div>
</div>

---
layout: prism
heading: "힙 정렬 (3/3) — DIY"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArray(const vector<int>& a) {
    for (int x : a) cout << x << " ";
    cout << "\n";
}

// 아래로 내리기: i를 루트로 하는 서브트리의 최대 힙 성질 유지
void heapify(vector<int>& arr, int n, int i) {
    int largest = i, l = 2 * i + 1, r = 2 * i + 2;
    if (l < n && arr[l] > arr[largest]) largest = l;
    if (r < n && arr[r] > arr[largest]) largest = r;
    if (largest != i) {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = n / 2 - 1; i >= 0; i--)   // 최대 힙 만들기
        heapify(arr, n, i);
    cout << "after buildHeap: "; printArray(arr);
    for (int i = n - 1; i > 0; i--) {      // 최댓값 반복 추출
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
        cout << "max -> index " << i << ": ";
        printArray(arr);
    }
}

int main() {
    vector<int> arr = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    cout << "Original: "; printArray(arr);
    heapSort(arr);
    cout << "Sorted:   "; printArray(arr);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "셸 정렬 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- 삽입 정렬은 입력이 [거의 정렬되어]{.hl} 있으면 거의 $\mathcal{O}(N)$ 입니다. [셸 정렬]{.hl} (shell sort)은 어떤 원소도 제자리에서 멀리 떨어지지 않도록 입력을 [전처리]{.hl}하여 이 점을 활용합니다.

- 감소하는 [갭 수열]{.hl} $h_0 > h_1 > \cdots > 1$ (gap sequence)을 사용하여:
  1. 리스트를 `h` 만큼 떨어진 부분 리스트들로 나누고,
  2. 각 부분 리스트를 삽입 정렬하고,
  3. `h = 1` 이 될 때까지 더 작은 갭으로 반복합니다.

- 셸 정렬은 최선의 경우 $\mathcal{O}(N^{1.25})$ 에 도달합니다.

</div>
<div>

<div style="height: 2rem;"></div>

```text
shellSort(A[]):
    for h ← h0, h1, …, 1:   // gap sequence
        for k ← 0 to h-1:
            // A[k, k+h, k+2h, …]에
            // 대한 삽입 정렬
            stepInsertionSort(A, k, h)
```

</div>
</div>

---
layout: prism
heading: "셸 정렬 (2/2) — DIY"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArray(const vector<int>& a) {
    for (int x : a) cout << x << " ";
    cout << "\n";
}

void shellSort(vector<int>& arr) {
    int n = arr.size();
    for (int h = n / 2; h > 0; h /= 2) {       // 줄어드는 갭 수열
        for (int i = h; i < n; i++) {          // 갭 간격 삽입 정렬
            int temp = arr[i], j;
            for (j = i; j >= h && arr[j - h] > temp; j -= h)
                arr[j] = arr[j - h];
            arr[j] = temp;
        }
        cout << "gap = " << h << ": ";
        printArray(arr);
    }
}

int main() {
    vector<int> arr = {8, 31, 48, 73, 3, 65, 20, 29, 11, 15};
    cout << "Original: "; printArray(arr);
    shellSort(arr);
    cout << "Sorted:   "; printArray(arr);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 요약 — 한눈에 보는 복잡도
---

<div style="margin-top: 1.6rem;">

| 알고리즘 | 최선 | 평균 | 최악 | 제자리 | 그룹 |
|---|---|---|---|---|---|
| 선택 | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | 예 | 쉬움 |
| 버블 | $\mathcal{O}(N)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | 예 | 쉬움 |
| 삽입 | $\mathcal{O}(N)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | 예 | 쉬움 |
| 병합 | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | 아니오 | 범용 |
| 퀵 | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N^2)$ | 예 | 범용 |
| 힙 | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | 예 | 범용 |
| 셸 | $\mathcal{O}(N^{1.25})$ | — | $\mathcal{O}(N^2)$ | 예 | 범용 |

</div>

<p style="margin-top: 1.4rem; color:#6b7280; font-size: 0.95rem;">쉬운 알고리즘은 단순하지만 제곱 시간이고, 범용 알고리즘은 분할 정복이나 힙을 통해 $\mathcal{O}(N \log N)$ 을 달성합니다.</p>

---
layout: prism
heading: "DIY: 실전 퀵 정렬"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- 퀵 정렬은 [뛰어난 평균 성능]{.hl}을 보이며, 그래서 실무에서 그토록 많이 쓰입니다.

- 단점은 $\mathcal{O}(N^2)$ [최악의 경우]{.hl}지만, 그런 입력은 실제로는 드물어서 프로그래머들은 여전히 퀵 정렬을 끊임없이 찾습니다.

- 곰곰이 생각해 보세요: 퀵 정렬은 [언제]{.hl} 실제로 $\mathcal{O}(N^2)$ 최악의 경우에 도달할까요?
  - 위 데모에서 마지막 원소를 피벗으로 하여 이미 정렬된 배열을 시도해 보고, 분할이 어떻게 불균형해지는지 살펴보세요.

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
