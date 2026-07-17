---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 8
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-8-ko/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Data Structures and Applications</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 08: Sorting Algorithms</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">Wonjun Ko, Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">Fall 2027</p>
</div>

---
layout: prism
heading: The Sorting Problem
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- To solve a huge range of tasks, we rely on [sorting]{.hl} algorithms:
  - *Input:* a sequence of $n$ numbers $(a_1, a_2, \ldots, a_n)$.
  - *Output:* a permutation (reordering) $(a_1', a_2', \ldots, a_n')$ of the input such that $a_1' \leq a_2' \leq \cdots \leq a_n'$.

- The input is usually an $n$-element array, though it may be represented some other way, such as a linked list.

- Many computer scientists consider sorting to be the [most fundamental problem]{.hl} in the study of algorithms:
  - applications inherently need to sort information, and algorithms often use sorting as a key subroutine;
  - many important design techniques — and engineering trade-offs — first appear in sorting algorithms.

---
layout: prism
heading: Ten Sorting Algorithms, Three Groups
---

<div class="absolute left-8 right-8" style="top: 6.5rem;">

We study [10 sorting algorithms]{.hl}, categorized into three groups by their properties. This week (W08) covers the first two groups; the special group appears later.

<div class="grid grid-cols-3 gap-6" style="margin-top: 2.2rem;">
<div>
  <div style="background:#3f6f8f; color:#fff; text-align:center; padding:0.7rem; border-radius:8px; font-weight:600;">Easy Algorithms</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.9rem;">Selection Sort</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.7rem;">Bubble Sort</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.7rem;">Insertion Sort</div>
  <p style="text-align:center; margin-top:1.4rem; color:#5c60a8; font-weight:600;">$\mathcal{O}(N^2)$</p>
</div>
<div>
  <div style="background:#3f6f8f; color:#fff; text-align:center; padding:0.7rem; border-radius:8px; font-weight:600;">General-Purpose</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.9rem;">Merge Sort</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.7rem;">Quick Sort</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.7rem;">Heap Sort</div>
  <div style="text-align:center; border:1px solid #c9d3dc; border-radius:6px; padding:0.5rem; margin-top:0.7rem;">Shell Sort</div>
  <p style="text-align:center; margin-top:0.9rem; color:#5c60a8; font-weight:600;">$\mathcal{O}(N \log N)$</p>
</div>
<div>
  <div style="background:#8a9099; color:#fff; text-align:center; padding:0.7rem; border-radius:8px; font-weight:600;">Special Algorithms</div>
  <div style="text-align:center; border:1px solid #d7d7d7; border-radius:6px; padding:0.5rem; margin-top:0.9rem; color:#9aa0a6;">Counting Sort</div>
  <div style="text-align:center; border:1px solid #d7d7d7; border-radius:6px; padding:0.5rem; margin-top:0.7rem; color:#9aa0a6;">Radix Sort</div>
  <div style="text-align:center; border:1px solid #d7d7d7; border-radius:6px; padding:0.5rem; margin-top:0.7rem; color:#9aa0a6;">Bucket Sort</div>
  <p style="text-align:center; margin-top:1.4rem; color:#9aa0a6; font-weight:600;">$\mathcal{O}(N)$ &nbsp;(later)</p>
</div>
</div>

</div>

---
layout: prism
heading: A Common Test Array
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Throughout this lecture we sort the same 10-element array into ascending order, so you can compare how each algorithm reaches the goal:

<div class="arr"><span class="lbl">A[…]</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>

<div class="arr"><span class="lbl">sorted A[…]</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

- Every algorithm below ships with a runnable `<CppRunner>` demo that prints its intermediate steps, so the process — not just the result — is visible.

- All demos share one helper that prints the current array state:

```cpp
void printArray(const vector<int>& a) {
    for (int x : a) cout << x << " ";
    cout << "\n";
}
```

---
layout: prism
heading: "Selection Sort (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [Selection sort]{.hl} (선택 정렬) is one of the easiest sorting algorithms.

- It repeatedly finds the [maximum]{.hl} element of the unsorted region and swaps it with the [last]{.hl} position of that region (symmetrically, one can select the minimum and place it first).

- "Find the maximum element" is proportional to the size of the sublist, so selection sort takes $\mathcal{O}(N^2)$ for *any* arbitrary input.

</div>
<div>

<div style="height: 2.5rem;"></div>

```text
selectionSort(A[], n):
    // shrink the unsorted region
    for last ← n-1 downto 1:
        // find the max of A[0..last]
        m ← argmax(A[0..last])
        // move it to the boundary
        swap(A[m], A[last])
```

</div>
</div>

---
layout: prism
heading: "Selection Sort (2/3) — Tracing"
---

<div style="margin-top: 1.4rem;">

<div class="arr"><span class="lbl">A[…]</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c hlmax">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">swap max (73) with last</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">15</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">find max (65) except last</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">15</span><span class="c">3</span><span class="c hlmax">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">swap max (65) with last</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">15</span><span class="c">3</span><span class="c">11</span><span class="c">20</span><span class="c">29</span><span class="c done">65</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">… repeat …</span><span class="c">8</span><span class="c">3</span><span class="c">11</span><span class="c">15</span><span class="c">20</span><span class="c">29</span><span class="c">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">sorted A[…]</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

</div>

<p style="margin-top: 1.4rem; color:#6b7280; font-size: 0.95rem;">Each pass fixes one more element (shaded) at the right end of the array.</p>

---
layout: prism
heading: "Selection Sort (3/3) — DIY"
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
    for (int i = n - 1; i > 0; i--) {   // boundary of unsorted region
        int max_idx = i;                // assume last is the max
        for (int j = 0; j < i; j++)     // scan A[0..i-1]
            if (arr[j] > arr[max_idx]) max_idx = j;
        swap(arr[max_idx], arr[i]);     // put the max at the boundary
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
heading: "Bubble Sort (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [Bubble sort]{.hl} (버블 정렬) is based on a similar idea to selection sort — move the maximum to the end — but in a slightly different way.

- It compares [adjacent]{.hl} elements from left to right and swaps them whenever they are out of order, so the largest element "bubbles up" to the last position each pass.

- If a whole pass makes no swaps, the array is already sorted and we can stop early ($\mathcal{O}(N)$ best case).

</div>
<div>

<div style="height: 2rem;"></div>

```text
bubbleSort(A[], n):
    for last ← n-1 downto 1:
        // bubble the max toward 'last'
        for i ← 0 to last-1:
            if A[i] > A[i+1]:
                swap(A[i], A[i+1])
```

</div>
</div>

---
layout: prism
heading: "Bubble Sort (2/3) — Tracing"
---

<div style="margin-top: 1.2rem;">

<div class="arr"><span class="lbl">A[…]</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">after pass 1 (73 bubbles up)</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">after pass 2 (65 bubbles up)</span><span class="c">8</span><span class="c">31</span><span class="c">3</span><span class="c">48</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span><span class="c done">65</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">… repeat …</span><span class="c">3</span><span class="c">8</span><span class="c">20</span><span class="c">11</span><span class="c">15</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>
<div class="arr"><span class="lbl">sorted A[…]</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

</div>

<p style="margin-top: 1.4rem; color:#6b7280; font-size: 0.95rem;">Adjacent comparisons sweep left to right; after each pass one more maximum is locked at the right end.</p>

---
layout: prism
heading: "Bubble Sort (3/3) — DIY"
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
    for (int i = 0; i < n - 1; i++) {        // one max settled per pass
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++)  // compare adjacent pairs
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        cout << "pass " << i + 1 << ": ";
        printArray(arr);
        if (!swapped) break;                 // already sorted: stop early
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
heading: "Insertion Sort (1/3)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [Insertion sort]{.hl} (삽입 정렬) grows a sorted prefix one element at a time.

- At step $i$, elements $A[0..i-1]$ are already ordered; we take the new element $A[i]$ and [insert]{.hl} it into its correct position, shifting larger elements one step to the right.

- If the input is [almost sorted]{.hl}, few shifts occur and insertion sort runs in roughly $\mathcal{O}(N)$ — a property exploited later by Shell sort.

</div>
<div>

<div style="height: 3.5rem;"></div>

```text
insertionSort(A[], n):
    for i ← 1 to n-1:
        // insert A[i] into the
        // sorted prefix A[0..i]
        insert A[i] appropriately
```

</div>
</div>

---
layout: prism
heading: "Insertion Sort (2/3) — Tracing"
---

<div style="margin-top: 1.2rem;">

<div class="arr"><span class="lbl">A[…]</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">6 elements ordered (prefix)</span><span class="c done">3</span><span class="c done">8</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span><span class="c hlmax">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">insert 20 (shift 31,48,65,73)</span><span class="c done">3</span><span class="c done">8</span><span class="c done">20</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">sorted A[…]</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

</div>

<p style="margin-top: 1.6rem; color:#6b7280; font-size: 0.95rem;">Every element larger than the key (here, larger than 20) slides one step right to open a slot for the insertion.</p>

---
layout: prism
heading: "Insertion Sort (3/3) — DIY"
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
        int key = arr[i];             // element to insert
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {   // shift larger elements right
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;             // drop key into its slot
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
heading: "Merge Sort (1/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Selection, bubble, and insertion sort all take $\mathcal{O}(N^2)$ — [not practical]{.hl} at scale. [Merge sort]{.hl} (병합 정렬) takes $\mathcal{O}(N \log N)$ for [both]{.hl} the best and worst cases.

- Merge sort [divides]{.hl} the input list into two halves, [sorts them independently]{.hl}, and finally [merges them]{.hl}.
  - Each half is itself sorted by merge sort, so the algorithm is [recursive]{.hl}.

- Merge sort needs an additional array `tmp[…]`, so it is [space-consuming]{.hl}.
  - A sort that needs no extra space is called [in-place sorting]{.hl} (내부 정렬); merge sort is *not* in-place.

---
layout: prism
heading: "Merge Sort (2/4) — Divide and Merge"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- `mergeSort` splits at the half-point `q`, recurses on each side, then calls `merge`.

- `merge` walks two sorted runs with indices `i` and `j`, always copying the smaller front element into `tmp`, then copies `tmp` back into `A[p..r]`.

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
heading: "Merge Sort (3/4) — Tracing"
---

<div style="margin-top: 1.4rem;">

<div class="arr"><span class="lbl">A[…]</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">divide in half</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c">15</span></div>
<div class="arr"><span class="lbl">sort each half</span><span class="c done">3</span><span class="c done">8</span><span class="c done">31</span><span class="c done">48</span><span class="c done">73</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">65</span></div>
<div class="arr"><span class="lbl">merge them</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

</div>

<p style="margin-top: 1.6rem; color:#6b7280; font-size: 0.95rem;">Two sorted runs (left <code>3 8 31 48 73</code>, right <code>11 15 20 29 65</code>) are combined by repeatedly taking the smaller front element.</p>

---
layout: prism
heading: "Merge Sort (4/4) — DIY"
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
    while (i < n1 && j < n2)                     // take the smaller front
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];
    while (i < n1) arr[k++] = L[i++];            // leftover left run
    while (j < n2) arr[k++] = R[j++];            // leftover right run
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
heading: "Quick Sort (1/4)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Merge sort solves small problems recursively and then [post-processes]{.hl} (merges). [Quick sort]{.hl} (퀵 정렬) flips the order: it [pre-processes]{.hl} first, then solves small problems recursively.

- Quick sort picks a [criterion]{.hl} (pivot) element, partitions the array into two groups — elements [smaller]{.hl} than the pivot and elements [larger or equal]{.hl} — and finally sorts each group.

- Quick sort takes $\mathcal{O}(N \log N)$ on average.
  - The worst case is $\mathcal{O}(N^2)$ (think about *when* that happens!), yet quick sort is [widely used in practice]{.hl}.

---
layout: prism
heading: "Quick Sort (2/4) — Partition"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- `partition` maintains three regions: area I (`< x`), area II (`≥ x`), and area III (undecided).

- Index `i` ends area I; `j` scans area III. Whenever `A[j] < x`, we grow area I by swapping `A[++i]` with `A[j]`.

- Finally the pivot is swapped into position `i+1`, the boundary between the two groups.

</div>
<div>

```text
quickSort(A[], p, r):
    if p < r:
        q ← partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

partition(A[], p, r):
    x ← A[r]              // pivot
    i ← p-1               // end of area I
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
heading: "Quick Sort (3/4) — Tracing"
---

<div style="margin-top: 1.4rem;">

<div class="arr"><span class="lbl">A[…], pivot x = A[r] = 15</span><span class="c">8</span><span class="c">31</span><span class="c">48</span><span class="c">73</span><span class="c">3</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">11</span><span class="c hlmax">15</span></div>
<div class="arr"><span class="lbl">smaller than 15 go left</span><span class="c done">8</span><span class="c done">3</span><span class="c done">11</span><span class="c hlmax">15</span><span class="c">31</span><span class="c">65</span><span class="c">20</span><span class="c">29</span><span class="c">48</span><span class="c">73</span></div>
<div class="arr"><span class="lbl">sort each group recursively</span><span class="c done">3</span><span class="c done">8</span><span class="c done">11</span><span class="c done">15</span><span class="c done">20</span><span class="c done">29</span><span class="c done">31</span><span class="c done">48</span><span class="c done">65</span><span class="c done">73</span></div>

</div>

<p style="margin-top: 1.6rem; color:#6b7280; font-size: 0.95rem;">After one partition, the pivot 15 sits in its final position; everything to its left is smaller, everything to its right is larger.</p>

---
layout: prism
heading: "Quick Sort (4/4) — DIY"
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
    int x = arr[r];                 // pivot = last element
    int i = p - 1;                  // end of "smaller" region
    for (int j = p; j <= r - 1; j++)
        if (arr[j] < x)
            swap(arr[++i], arr[j]);
    swap(arr[i + 1], arr[r]);       // put pivot at the boundary
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
heading: "Heap Sort (1/3)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- [Heap sort]{.hl} (힙 정렬) uses the [heap]{.hl} data structure for sorting.
  - It first [builds a max-heap]{.hl} from the given list.
  - Then it repeatedly [removes the maximum]{.hl} (the root) and percolates down, one element at a time.

- Storing the largest removed element just past the shrinking heap boundary sorts the array [in place]{.hl}.

- Heap sort takes $\mathcal{O}(N \log N)$ for the worst case and $\mathcal{O}(N)$ for the best case.

---
layout: prism
heading: "Heap Sort (2/3) — Build and Extract"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- An array is viewed as a complete binary tree: node `i` has children `2i+1` and `2i+2`.

- `buildHeap` (percolate-down) makes every subtree a max-heap, starting from the last internal node.

- Then, `n-1` times, swap the root (the max) with the last heap element and re-heapify the smaller heap.

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
heading: "Heap Sort (3/3) — DIY"
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

// percolate down: keep the max-heap property of subtree rooted at i
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
    for (int i = n / 2 - 1; i >= 0; i--)   // build max-heap
        heapify(arr, n, i);
    cout << "after buildHeap: "; printArray(arr);
    for (int i = n - 1; i > 0; i--) {      // extract max repeatedly
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
heading: "Shell Sort (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Insertion sort is nearly $\mathcal{O}(N)$ when the input is [almost sorted]{.hl}. [Shell sort]{.hl} (셸 정렬) exploits this by [pre-processing]{.hl} the input so no element is far from where it belongs.

- Using a decreasing [gap sequence]{.hl} $h_0 > h_1 > \cdots > 1$ (갭 수열):
  1. divide the list into sublists spaced `h` apart,
  2. insertion-sort each sublist,
  3. repeat with a smaller gap until `h = 1`.

- Shell sort reaches $\mathcal{O}(N^{1.25})$ for the best case.

</div>
<div>

<div style="height: 2rem;"></div>

```text
shellSort(A[]):
    for h ← h0, h1, …, 1:   // gap sequence
        for k ← 0 to h-1:
            // insertion sort on
            // A[k, k+h, k+2h, …]
            stepInsertionSort(A, k, h)
```

</div>
</div>

---
layout: prism
heading: "Shell Sort (2/2) — DIY"
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
    for (int h = n / 2; h > 0; h /= 2) {       // shrinking gap sequence
        for (int i = h; i < n; i++) {          // gapped insertion sort
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
heading: Summary — Complexities at a Glance
---

<div style="margin-top: 1.6rem;">

| Algorithm | Best | Average | Worst | In-place | Group |
|---|---|---|---|---|---|
| Selection | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | yes | Easy |
| Bubble | $\mathcal{O}(N)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | yes | Easy |
| Insertion | $\mathcal{O}(N)$ | $\mathcal{O}(N^2)$ | $\mathcal{O}(N^2)$ | yes | Easy |
| Merge | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | no | General |
| Quick | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N^2)$ | yes | General |
| Heap | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | $\mathcal{O}(N \log N)$ | yes | General |
| Shell | $\mathcal{O}(N^{1.25})$ | — | $\mathcal{O}(N^2)$ | yes | General |

</div>

<p style="margin-top: 1.4rem; color:#6b7280; font-size: 0.95rem;">Easy algorithms are simple but quadratic; general-purpose algorithms achieve $\mathcal{O}(N \log N)$ through divide-and-conquer or heaps.</p>

---
layout: prism
heading: "DIY: Quick Sort in Practice"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Quick sort shows [excellent average performance]{.hl}, which is why it is so heavily used in the field.

- Its drawback is the $\mathcal{O}(N^2)$ [worst case]{.hl} — but such inputs rarely occur in practice, so programmers still reach for it constantly.

- Think it through: [when]{.hl} does quick sort actually hit its $\mathcal{O}(N^2)$ worst case?
  - Try an already-sorted array with the last-element pivot in the demo above, and watch how the partitions become unbalanced.

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
