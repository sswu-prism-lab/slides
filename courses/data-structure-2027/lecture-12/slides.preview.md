---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 12
download: true
info: |
  ## Data Structure Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Data Structure</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 12: Hash Tables</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">Wonjun Ko, Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">Spring 2027</p>
</div>

---
layout: prism
heading: Course Schedule
---

<div class="absolute left-10 right-10" style="top: 0rem; bottom: 0rem; display: grid; grid-template-columns: 1.2fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#9aa0a6;">Course Introduction</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">Basic Mathematics and C++ Details</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">Algorithm Analysis</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">Lists, Stacks, and Queues</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">Circular Queues and Priority Queues</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">Trees and Tries</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">Midterm Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">Midterm Exam</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">Heaps</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">Graphs and Weighted Graphs</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">Sets and Maps</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span class="text-gray-900 dark:text-gray-100">Hash Tables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Algorithm Design Techniques</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: "Recap: Equivalence Relations"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A [relation]{.hl} $R$ is defined on a set $S$ if for every pair $(a, b)$ with $a, b \in S$, the statement $a\ R\ b$ is either *true* or *false*.
  - If $a\ R\ b$ is true, we say $a$ is *related* to $b$.

- An [equivalence relation]{.hl} is a relation $R$ satisfying three properties:

<div class="sub-item-enum">

1. *Reflexive.* $a\ R\ a$, $\forall a \in S$.
2. *Symmetric.* $a\ R\ b$ if and only if $b\ R\ a$.
3. *Transitive.* $a\ R\ b$ and $b\ R\ c$ imply $a\ R\ c$.

</div>

- The $\leq$ relation is *not* an equivalence relation: it is reflexive and transitive, but not symmetric ($a \leq b$ does not imply $b \leq a$).

- Electrical connectivity *is* an equivalence relation — it is reflexive, symmetric, and transitive.

---
layout: prism
heading: Hash Tables
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- A `find` operation requires $\mathcal{O}(N)$ for an array and $\mathcal{O}(\log N)$ for a self-adjusting binary tree.
  - Can we `find` elements in $\mathcal{O}(1)$ time?

- The implementation of [hash tables]{.hl} is frequently called [hashing]{.hl} — a technique for performing insertions, deletions, and finds in *constant average time*.

- Operations that require any *ordering* among the elements are not supported efficiently, e.g. `findMin`, `findMax`, and `print` in linear time.

- Today, we discuss the hash table data structure:
  - see several methods of implementing the hash table, and
  - compare these methods analytically.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">General Idea</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">General Idea</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Hash Function</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Separate Chaining</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Hash Tables without Linked Lists</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Hash Tables with Worst-Case O(1) Access</span></p>
  </div>

</div>

---
layout: prism
heading: General Idea
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The ideal hash table data structure is merely an *array* of some fixed size containing the items.

- Generally a search is performed on some part of the item, and this part is called the [key]{.hl}.

- Each key is mapped into some number in the range `0` to `tableSize - 1` and placed in the appropriate cell.
  - This mapping is called a [hash function]{.hl}, which ideally should be simple to compute and should ensure that any two distinct keys get different cells.

- Since there are finitely many cells but a virtually inexhaustible supply of keys, this is clearly impossible — so we seek a hash function that *distributes the keys evenly* among the cells.

---
layout: prism
heading: General Idea — A Perfect Situation
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The table at right is typical of a *perfect* situation — every key lands in its own cell.

- This is the basic idea of hashing.

- The remaining problems are: choosing a function, deciding what to do when two keys hash to the same value, and deciding on the table size.
  - Two keys hashing to the same value is known as a [collision]{.hl}.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w12-01.svg" class="tikz-fig" style="width: 62%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: Hash Function
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- If the keys are integers, returning `key mod tableSize` is generally reasonable, unless the keys have some undesirable property.
  - If the table size is $10$ and every key ends in zero, the standard hash function is a bad choice.
  - To avoid such situations, it is often a good idea to keep the table size [prime]{.hl}.

- For *random* integer keys this function is simple to compute and distributes the keys evenly.
  - When keys are strings, we can combine the ASCII values of the characters.

- If the table size is large, a naive sum distributes poorly.
  - With table size $10007$ (prime) and keys of eight or fewer characters, the sum can only reach $0$ to $1016$ (an ASCII character is at most $127$, and $127 \times 8 = 1016$).

---
layout: prism
heading: "Hash Function — Summing Characters"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A first attempt simply adds up the ASCII values of all characters in the key.

- A second attempt weights the first three characters: $\texttt{key}[0] + 27\,\texttt{key}[1] + 729\,\texttt{key}[2]$.

- Unfortunately, English is *not* random.
  - Of $26^3$ three-character combinations, a large dictionary reveals only $2851$ distinct ones — so even with no collisions only about $28\%$ of the table can be reached.

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
heading: "Hash Function — Horner's Rule"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- A third attempt involves *all* characters in the key and can generally be expected to distribute well.

- The code computes a polynomial function using [Horner's rule]{.hl}, treating the key as a base-$37$ number.

- It has the merit of extreme simplicity and is reasonably fast.

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
heading: Separate Chaining
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The main programming detail left is [collision resolution]{.hl}.

- If an inserted element hashes to the same value as an already inserted element, we have a *collision* and must resolve it.

- The first strategy, [separate chaining]{.hl}, keeps a *list* of all elements that hash to the same value.

- With $hash(x) = x \bmod 10$, inserting $\{0,1,4,9,16,25,36,49,64,81\}$ gives the table at right.

</div>
<div>

<div style="height: 0.5rem;"></div>

| Cell | Chain |
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
heading: "Separate Chaining — Operations"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- To perform a `find`, we use the hash function to determine which list to traverse, then search that list.

- To perform an `insert`, we check the appropriate list to see whether the element is already present.
  - If the element is new, it can be inserted at the *front* of the list.

- Any scheme could be used besides linked lists — a binary search tree or even another hash table would work.
  - But if the table is large and the hash function is good, all lists are short, so basic separate chaining stays simple.

- The [load factor]{.hl} $\lambda$ of a hash table is the ratio of the number of elements to the table size.
  - For separate chaining, the average length of a list is exactly $\lambda$, so a successful `find` costs $\mathcal{O}(1 + \lambda)$.

---
layout: prism
heading: "Separate Chaining — Implementation"
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
            return false;              // already present
        whichList.push_back(x);
        if (++currentSize > theLists.size()) rehash();   // keep lambda <= 1
        return true;
    }

private:
    vector<list<HashedObj>> theLists;  // the array of lists
    int currentSize;
    size_t myhash(const HashedObj& x) const {
        static hash<HashedObj> hf;
        return hf(x) % theLists.size();
    }
};
```

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">General Idea</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Hash Tables without Linked Lists</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Linear Probing</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Quadratic Probing</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Double Hashing</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Rehashing</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Hash Tables in the STL</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Hash Tables with Worst-Case O(1) Access</span></p>
  </div>

</div>

---
layout: prism
heading: "Linear Probing — Open Addressing"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- Separate chaining has the disadvantage of using linked lists — allocating new cells is slow and requires a second data structure.

- An alternative resolves collisions *without* linked lists by trying alternative cells until an empty one is found.
  - This strategy is known as [open addressing]{.hl}.

- Formally, cells $h_0(x), h_1(x), h_2(x), \ldots$ are tried in succession, where

$$
h_i(x) = \big(hash(x) + f(i)\big) \bmod tableSize, \qquad f(0) = 0.
$$

- The function $f$ is the *collision resolution strategy*. Because all data go inside the table, a bigger table is needed than for separate chaining.

- Generally the load factor should be below $\lambda = 0.5$; we call these [probing hash tables]{.hl}.

---
layout: prism
heading: "Linear Probing — Primary Clustering"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- In [linear probing]{.hl}, $f$ is a linear function of $i$, typically $f(i) = i$.
  - This amounts to trying cells sequentially in search of an empty cell.

- The table at right shows the result of inserting keys $\{89, 18, 49, 58, 69\}$.

- Even when the table is relatively empty, blocks of occupied cells form.
  - This is [primary clustering]{.hl}: any key hashing into the cluster needs several attempts and then adds to the cluster.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w12-02.svg" class="tikz-fig" style="width: 60%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "Linear Probing — Implementation"
---

```cpp
template <typename HashedObj>
class HashTable {
public:
    bool contains(const HashedObj& x) const { return isActive(findPos(x)); }

    bool insert(const HashedObj& x) {
        int currentPos = findPos(x);
        if (isActive(currentPos)) return false;      // already present
        array[currentPos] = HashEntry{x, ACTIVE};
        if (++currentSize > array.size() / 2) rehash();   // keep lambda < 0.5
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
            currentPos += offset;                    // f(i) = i : linear probing
            if (currentPos >= array.size()) currentPos -= array.size();
        }
        return currentPos;
    }
};
```

---
layout: prism
heading: "Quadratic Probing — Secondary Clustering"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [Quadratic probing]{.hl} eliminates the primary clustering of linear probing.

- Its collision function is quadratic; the popular choice is $f(i) = i^2$.

- Although it removes primary clustering, elements that hash to the *same* position probe the same alternative cells.
  - This is known as [secondary clustering]{.hl}.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w12-03.svg" class="tikz-fig" style="width: 60%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: Double Hashing
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.0em;
}
</style>

- The last collision resolution method we examine is [double hashing]{.hl}.

- A popular choice is $f(i) = i \cdot hash_2(x)$, so a *second* hash function determines the step size.

- The table at right uses $hash_2(x) = x \bmod 9$ while inserting $\{89, 18, 49, 58, 69\}$.
  - $hash_2$ must never evaluate to zero, and choosing it as $R - (x \bmod R)$ for a prime $R < tableSize$ works well.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w12-04.svg" class="tikz-fig" style="width: 60%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: Rehashing
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- If the table gets too full, operations take too long, and for quadratic resolution insertions might even *fail*.
  - This can also happen when many removals are intermixed with insertions.

- The solution is to build another table about *twice* as big (with a new hash function), scan the entire original table, and re-insert each non-deleted element at its new hash value.

<div class="theorem-box">
<div class="theorem-box-title">Example</div>
<div class="theorem-box-body">

Insert $13, 15, 24, 6$ into a linear-probing table of size $7$ with $h(x) = x \bmod 7$. Inserting $23$ would make the table over $70\%$ full, triggering a new table of size $17$ — the first prime at least twice as large.

</div>
</div>

- This entire operation is called [rehashing]{.hl}. It is expensive: the running time is $\mathcal{O}(N)$, but it occurs so infrequently that its *amortized* cost is small.

---
layout: prism
heading: Hash Tables in the STL
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- C++ provides two standard-library containers that instantiate the hash table data structure: [`unordered_set`]{.hl} and [`unordered_map`]{.hl}.

- Unlike `set` and `map` (which are balanced binary search trees), these keep items in *no* particular order but offer $\mathcal{O}(1)$ average operations.

<div style="height: 1rem;"></div>

```cpp
#include <unordered_set>
#include <unordered_map>

unordered_set<string> words;              // a hash set
unordered_map<string, int> wordCount;     // a hash map (key -> value)
```

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">General Idea</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Hash Tables without Linked Lists</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Hash Tables with Worst-Case O(1) Access</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Perfect Hashing</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Cuckoo Hashing</span></p>
  </div>

</div>

---
layout: prism
heading: "Perfect Hashing — Motivation"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The hash tables so far give $\mathcal{O}(1)$ cost *on average* for insertions, removes, and searches with reasonable load factors.

- We would like $\mathcal{O}(1)$ *worst-case* cost.
  - In applications such as hardware lookup tables for routers and memory caches, the search must have a definite completion time.

- Suppose, for simplicity, that all $N$ items are known in advance.

- If a separate-chaining implementation could guarantee each list has at most a constant number of items, we would be done.
  - As we make more lists, the lists become shorter on average — so with enough lists we might expect *no* collisions at all.

---
layout: prism
heading: "Perfect Hashing — Two-Level Scheme"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Choose the number of lists $M$ large enough to guarantee no collisions; if a collision is detected, clear the table and retry with a different, independent hash function.

- Theoretically $M$ must be quite large — specifically $M = \Omega(N^2)$ — so using $N^2$ lists is impractical.

- Practically, we resolve the collisions in each *bin* by using additional hash tables instead of linked lists.
  - Because each bin has only a few items, the secondary hash table for a bin can be *quadratic* in the bin size, keeping it collision-free with high probability.

---
layout: prism
heading: "Perfect Hashing — Example"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- The primary hash table has ten bins:
  - Bins 1, 3, 5, 7 are empty.
  - Bins 0, 4, 8 have one item — a secondary table with one position.
  - Bins 2, 6 have two items — a secondary table with four positions.
  - Bin 9 has three items — a secondary table with nine positions.

- Each secondary table is built with a different hash function until it is collision-free. This scheme is [perfect hashing]{.hl}.

</div>
<div>

<div style="height: 0.5rem;"></div>

| Bin | Items | 2nd table size |
|:---:|:-----:|:--------------:|
| 0 | 1 | 1 |
| 2 | 2 | 4 |
| 4 | 1 | 1 |
| 6 | 2 | 4 |
| 8 | 1 | 1 |
| 9 | 3 | 9 |

<div class="sub-item">

Secondary size $= (\text{bin size})^2$.

</div>

</div>
</div>

---
layout: prism
heading: "Cuckoo Hashing — Idea"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- In [cuckoo hashing]{.hl}, suppose we have $N$ items, *two* tables (each more than half empty), and two independent hash functions, each assigning an item a position in one table.
  - The invariant: an item is always stored in one of its two locations, so a `find` checks only *two* cells — worst-case $\mathcal{O}(1)$.

- The algorithm itself is simple:
  - To insert a new item $A$, first make sure it is not already there.
  - Use the first hash function; if that first-table location is empty, place the item.
  - If a later item $B$ must go to an occupied location, it *preemptively* takes that spot, displacing $A$, which then moves to the second table using its second hash location.

- The displaced item may in turn displace another — like a cuckoo chick pushing others out of the nest.

---
layout: prism
heading: "Cuckoo Hashing — Cycles"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- After inserting $A{:}(0,2)$, $B{:}(0,0)$, $C{:}(1,4)$, $D{:}(1,0)$, $E{:}(3,2)$, $F{:}(3,4)$ we obtain the two tables at right ($X{:}(y,z)$ gives $X$'s two hash locations).

- Now inserting $G{:}(1,2)$ forces items to be displaced, replaced, and displaced *forever* — a [cycle]{.hl}.

- Key questions: what is the probability of a cycle, and what is the expected number of displacements for a successful insertion?

- If the load factor is below $0.5$, a cycle is very unlikely; at $0.5$ or above it becomes drastically more likely and cuckoo hashing works poorly.

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
heading: "DIY: Separate Chaining"
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

    for (int k : keys) {                      // insert at front of chain
        auto& L = table[myhash(k)];
        L.push_front(k);
    }

    for (int i = 0; i < TS; i++) {            // print every slot's chain
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
heading: "DIY: Linear Probing"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int TS = 10;                            // table size

int main() {
    vector<int> table(TS, -1);                // -1 marks an empty slot
    int keys[] = {89, 18, 49, 58, 69};

    for (int k : keys) {                       // f(i) = i : linear probing
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
heading: "DIY_W12: Various Hashing Algorithms"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Many more advanced hashing algorithms exist beyond those covered today.

- [Hopscotch hashing]{.hl} improves classic linear probing by *bounding* the maximal probe-sequence length by a constant optimized to the computer's architecture.

- [Universal hashing]{.hl} chooses the hash function *randomly* so that, provably, items are distributed uniformly among the array slots.

- [Extendible hashing]{.hl} allows a search to be performed in as few as *two* disk accesses — useful when data reside on disk.

- Find and study these algorithms.

---
layout: prism
heading: "HW_W12: Try a Coding Test"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- We have studied various data structures and are now prepared to program.

- Select *three* coding-test problems and solve them.
  - You may take problems from websites, books, etc.

- Copy and paste each problem together with your answer.
  - Solve them *by yourself*; if a problem is too hard, leave it blank rather than cheating.

- Upload the PDF file to the LMS as `20XXXXXX_HW_W12.pdf`.

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
