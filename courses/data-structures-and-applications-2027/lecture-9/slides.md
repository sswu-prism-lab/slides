---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 9
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-9-ko/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Data Structures and Applications</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 09: Sorting Algorithms (Review)</p>

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
heading: "Recap: Sorting Algorithms"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- In this lecture we [review]{.hl} the sorting algorithms covered so far, tracing each one step by step and running a working C++ implementation.

- The first group are the [comparison-based]{.hl} sorts, which order elements only by comparing them:

<div class="sub-item">

[Selection]{.hl}, [Bubble]{.hl}, [Insertion]{.hl}, [Merge]{.hl}, [Quick]{.hl}, [Heap]{.hl}, and [Shell]{.hl} sort.

</div>

- The second group exploit special [properties of the data]{.hl} (their range or digit structure) to break the $O(N \log N)$ comparison lower bound:

<div class="sub-item">

[Counting]{.hl}, [Radix]{.hl}, and [Bucket]{.hl} sort.

</div>

---
layout: prism
heading: "Selection Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- On each pass, [select the maximum]{.hl} element among those not yet placed and move it to the back of the unsorted region.

- After placing the maximum at the last position, we exclude that position and repeat on the shrinking prefix.

- Every pass scans the whole unsorted region, so the running time is $O(N^2)$ regardless of the input.

<div class="theorem-box">
<div class="theorem-box-title">One pass</div>
<div class="theorem-box-body">

`8 31 48 15 3 11 20 29 65 73` → the maximum `73` is already last, so the next pass places `65`, then `48`, and so on.

</div>
</div>

---
layout: prism
heading: "DIY: Selection Sort"
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
        int maxIdx = 0;                          // find max in a[0..last]
        for (int i = 1; i <= last; ++i)
            if (a[i] > a[maxIdx]) maxIdx = i;
        swap(a[maxIdx], a[last]);                // send it to the back
        cout << "max -> pos " << last << ": "; printArr(a);
    }
    cout << "Sorted:  "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Bubble Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Scan the list from [left to right]{.hl}, comparing each pair of adjacent elements.

- If the left element is larger than the right one, [swap]{.hl} them; the largest element gradually "bubbles up" to the end.

- After each full pass the last (largest) element is in place and is excluded from the next pass; the running time is $O(N^2)$.

<div class="theorem-box">
<div class="theorem-box-title">First pass</div>
<div class="theorem-box-body">

Starting from `8 31 48 73 3 65 20 29 11 15`, the value `73` travels rightward past every smaller neighbour until it reaches the last cell.

</div>
</div>

---
layout: prism
heading: "DIY: Bubble Sort"
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
        for (int i = 0; i < n - 1 - pass; ++i)       // compare adjacent pairs
            if (a[i] > a[i + 1]) { swap(a[i], a[i + 1]); swapped = true; }
        cout << "after pass " << pass + 1 << ": "; printArr(a);
        if (!swapped) break;                          // already sorted
    }
    cout << "Sorted:  "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Insertion Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Keep the front of the list [sorted]{.hl}, and grow it one element at a time.

- To add the next element, shift every larger element in the sorted prefix one place to the [right]{.hl}, then drop the new element into the gap.

- It is $O(N^2)$ in the worst case, but very fast on nearly-sorted data.

<div class="theorem-box">
<div class="theorem-box-title">Inserting the 7th element</div>
<div class="theorem-box-body">

With `3 8 31 48 65 73` already sorted, inserting `20` shifts `31 48 65 73` right and places `20` right after `8`.

</div>
</div>

---
layout: prism
heading: "DIY: Insertion Sort"
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
        while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; --j; }  // shift larger elements right
        a[j + 1] = key;                                          // drop key into the gap
        cout << "insert " << key << ": "; printArr(a);
    }
    cout << "Sorted:  "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Merge Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- A [divide-and-conquer]{.hl} sort: split `A[p..r]` at the midpoint `q`, sort both halves recursively, then [merge]{.hl} them.

- The merge walks two pointers `i` and `j` across the halves, copying the smaller front element into a temporary buffer `tmp[]`, then copies `tmp[]` back.

- Because the split is always balanced, merge sort runs in $O(N \log N)$ time for [every]{.hl} input.

<div class="theorem-box">
<div class="theorem-box-title">Merging two sorted halves</div>
<div class="theorem-box-body">

`3 8 31 48 73` and `11 15 20 29 65` merge into `3 8 11 15 20 29 31 48 65 73`.

</div>
</div>

---
layout: prism
heading: "DIY: Merge Sort"
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
heading: "Quick Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Choose a [pivot]{.hl}, then [partition]{.hl} the list so that every element smaller than the pivot comes before it and every larger element comes after it.

- The pivot is now in its final position; recurse on the left and right partitions.

- Partitioning is $O(N)$; with balanced splits the total cost is $O(N \log N)$ on average (worst case $O(N^2)$).

<div class="theorem-box">
<div class="theorem-box-title">Partition step</div>
<div class="theorem-box-body">

Two indices `i` and `j` sweep inward, swapping elements that are on the wrong side of the pivot.

</div>
</div>

---
layout: prism
heading: "DIY: Quick Sort"
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
heading: "Heap Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- First rearrange the array into a [max-heap]{.hl}, so the largest element sits at the root (index 0).

- Repeatedly swap the root with the [last]{.hl} element of the heap, shrink the heap by one, and [sift down]{.hl} the new root to restore the heap property.

- Building the heap is $O(N)$ and each of the $N$ removals costs $O(\log N)$, so heap sort is $O(N \log N)$.

<div class="theorem-box">
<div class="theorem-box-title">Array as a heap</div>
<div class="theorem-box-body">

For index `i`, the children live at `2i+1` and `2i+2`; sifting down repeatedly swaps a node with its larger child.

</div>
</div>

---
layout: prism
heading: "DIY: Heap Sort"
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
    for (int i = n / 2 - 1; i >= 0; --i) siftDown(a, i, n);   // build max-heap
    cout << "Max-heap: "; printArr(a);
    for (int end = n - 1; end > 0; --end) {
        swap(a[0], a[end]);                                   // largest to the back
        siftDown(a, 0, end);
    }
    cout << "Sorted:   "; printArr(a);
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Shell Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.5em;
}
</style>

- Shell sort generalises insertion sort using a [gap]{.hl} `h`: it insertion-sorts the sub-sequences of elements that are `h` apart.

- Starting from a large gap lets far-apart elements move quickly; the gap [decreases]{.hl} down to `h = 1`, where a final insertion sort finishes the job on an almost-sorted list.

- The running time depends on the gap sequence, but is comfortably better than plain insertion sort in practice.

<div class="theorem-box">
<div class="theorem-box-title">Gap sequence</div>
<div class="theorem-box-body">

Here we use `h = 3` then `h = 1`. After the `h = 3` pass the list is "3-sorted"; the final `h = 1` pass completes the sort.

</div>
</div>

---
layout: prism
heading: "DIY: Shell Sort"
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
    for (int h = 3; h >= 1; h -= 2) {                 // gaps 3, then 1
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
heading: "Sorting Algorithms That Use Data Properties"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Comparison sorts cannot beat $\Omega(N \log N)$, because they learn about the data only through comparisons.

- When we know something extra about the data — a small integer [range]{.hl}, a fixed number of [digits]{.hl}, or a uniform [distribution]{.hl} — we can sort in [linear time]{.hl}.

- We now review three such algorithms:

<div class="sub-item">

[Counting sort]{.hl} (small integer range), [Radix sort]{.hl} (fixed-width keys), and [Bucket sort]{.hl} (uniformly distributed values).

</div>

---
layout: prism
heading: "Counting Sort — Idea"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Counting sort assumes each element is an integer in a small range $\{0, 1, \ldots, k\}$.

- It works in three phases using a [count array]{.hl} `C`:

<div class="sub-item-enum">

1. Count how many times each value appears: `C[i]` = number of elements equal to `i`.
2. Turn `C` into a [prefix sum]{.hl}, so `C[i]` = number of elements $\leq i$ — this is exactly the final position boundary for value `i`.
3. Scan the input from the [back]{.hl}, placing each element at `B[C[value] - 1]` and decrementing `C[value]`; scanning backwards keeps the sort [stable]{.hl}.

</div>

- With `n` elements over a range of size `k`, the total cost is $O(n + k)$.

---
layout: prism
heading: "Counting Sort — Pseudocode"
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

- The second loop counts, in `C[0..k]`, how often each value `0..k` occurs in `A`.

- The third loop makes `C[i]` hold the number of elements less than or equal to `i`.

- The last loop uses `C` to compute the destination slot in `B` for each element of `A`.

</div>
</div>

---
layout: prism
heading: "DIY: Counting Sort"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Counting sort over an arbitrary integer range [min, max]
void countingSort(vector<int>& A) {
    int n = A.size();
    int maxElement = *max_element(A.begin(), A.end());
    int minElement = *min_element(A.begin(), A.end());
    int k = maxElement - minElement + 1;
    vector<int> C(k, 0), B(n);
    for (int j = 0; j < n; j++) C[A[j] - minElement]++;      // count occurrences
    for (int i = 1; i < k; i++) C[i] += C[i - 1];            // prefix sums
    for (int j = n - 1; j >= 0; j--) {                       // stable placement
        B[C[A[j] - minElement] - 1] = A[j];
        C[A[j] - minElement]--;
    }
    for (int i = 0; i < n; i++) A[i] = B[i];                 // copy back
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
heading: "Radix Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Radix sort orders numbers with up to `k` digits by sorting them [one digit at a time]{.hl}, from the [least]{.hl} significant digit to the most significant.

- Each single-digit pass must be a [stable]{.hl} sort — equal keys keep their previous relative order — so the work done on earlier digits is preserved.

<div class="sub-item">

A stable pass over a single digit is exactly a counting sort with range `0..9`, costing $O(N)$.

</div>

- With `k` digit passes over `N` numbers, the total cost is $O(k \cdot N)$, i.e. linear when `k` is a constant.

---
layout: prism
heading: "DIY: Radix Sort"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printArr(const vector<int>& a) { for (int x : a) cout << x << ' '; cout << '\n'; }

// stable counting sort on the digit selected by 'exp' (1, 10, 100, ...)
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
    for (int exp = 1; exp <= 1000; exp *= 10) {   // 4-digit numbers
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
heading: "Bucket Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Bucket sort assumes the input is `n` real values [uniformly distributed]{.hl} over `[0, 1)`.

- Scatter each value `A[i]` into bucket `B[⌊n·A[i]⌋]`, sort each bucket (e.g. with insertion sort), then concatenate the buckets back into `A`.

- If the values are spread evenly, each bucket holds only a few elements, giving an expected running time of $O(N)$.

<div class="theorem-box">
<div class="theorem-box-title">Example</div>
<div class="theorem-box-body">

With 15 values, `0.38` goes to bucket `⌊15 · 0.38⌋ = 5`, `0.94` to bucket `14`, and so on; each bucket is sorted independently.

</div>
</div>

---
layout: prism
heading: "DIY: Bucket Sort"
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

    vector<vector<double>> B(n);                 // n buckets
    for (double x : a) B[(int)(n * x)].push_back(x);

    int idx = 0;
    for (int i = 0; i < n; i++) {
        sort(B[i].begin(), B[i].end());          // sort each bucket
        for (double x : B[i]) a[idx++] = x;      // concatenate
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
heading: "Homework: Improved Bucket Sort"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A naive bucket sort builds a linked list inside each bucket and often runs out of space when the data is skewed.

- There is a way to implement it [without physically keeping the buckets]{.hl} (no linked lists at all) — and, with that idea, it can even beat quick sort.

<div class="sub-item">

Where counting sort counts individual values, bucket sort counts values in a [range]{.hl}. From those counts we can compute the exact slice of `A[0..n-1]` that each bucket's elements will occupy, and place elements [directly]{.hl} into `A` instead of into separate buckets.

</div>

- Implement this improved bucket sort. Save it as `HW_W09_20XXXXXX.cpp` and upload it to the LMS.

---
layout: prism
heading: "Practice: The K-th Number"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Given `array`, for each command `[i, j, k]`: take the slice from the `i`-th to the `j`-th element (1-indexed), sort it, and report its `k`-th element.

- For `array = [1,5,2,6,3,7,4]` and command `[2,5,3]`: the slice `[5,2,6,3]` sorts to `[2,3,5,6]`, whose 3rd element is `5`.

- Return the answers for all commands.

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
heading: "Practice: The Largest Number"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- Given non-negative integers, concatenate them in some order to form the [largest]{.hl} possible number, and return it as a string.

- Sort the numbers by a custom rule: `a` comes before `b` when the string `a+b` is larger than `b+a`.

- Edge case: if the largest digit is `0`, every number is `0`, so return `"0"`.

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
heading: "Practice: H-Index"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The [H-Index]{.hl} `h` is the largest value such that the researcher has at least `h` papers each cited at least `h` times.

- Sort the citation counts in [descending]{.hl} order; the answer is the largest `i` for which `citations[i-1] >= i`.

- For `citations = [3,0,6,1,5]`, three papers have at least 3 citations, so the H-Index is `3`.

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

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
