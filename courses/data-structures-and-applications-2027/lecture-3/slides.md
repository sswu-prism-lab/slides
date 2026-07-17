---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DSA - Lecture 3
download: true
info: |
  ## Data Structures and Applications Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structures-and-applications-2027/lecture-3-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 03: Online Judges and C++ Practice</p>

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
heading: Online Judges and C++ Practice
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- This week we step away from theory and get our hands on real practice tools:

  - Where to write and run C++ online: [online compilers]{.hl} such as OnlineGDB.

  - Where to practice: [online judges]{.hl} and coding-test sites (Baekjoon, Programmers, CodeSignal).

  - A quick tour of the [C++ building blocks]{.hl} — `if`, `for`, `vector`, `stack`, `queue`, `string`, and `sort` — that we need to solve real problems.

  - Six [worked coding-test problems]{.hl}, each solved with a running C++ program driven by sample input.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Online Tools and Judges</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Online C++ Compilers</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Online Coding-Test Sites</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">A Sample Judge Session</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ Building Blocks</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Worked Coding-Test Problems</span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">DIY Practice</span></p>
  </div>

</div>

---
layout: prism
heading: Online C++ Compiler
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- An [online compiler]{.hl} lets us write, compile, and run C++ directly in the browser — no local toolchain needed.

- [OnlineGDB]{.hl} is a convenient choice: it supports C, C++, and many other languages, plus an interactive debugger.
  - <code>https://www.onlinegdb.com</code>

- Any other online compiler works equally well — pick whichever you prefer.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w03/dsa-w03-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Online Coding-Test Sites
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [Baekjoon Online Judge]{.hl} — `https://www.acmicpc.net`
  - The *Problems → Algorithm Classification* tab groups problems by type; a curated set for the Samsung SW aptitude test is provided.

- [Programmers]{.hl} — `https://school.programmers.co.kr`
  - The *Coding Test → High-Score Kit* tab groups problems by algorithm; a curated set for the Kakao coding test is provided.

- [CodeSignal]{.hl} — `https://codesignal.com`
  - Presented in English; offers problem sets aimed at interviews with international companies.

---
layout: prism
heading: A Sample Judge Session
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- A typical judge page shows the [problem statement]{.hl} on the left and an [editor]{.hl} on the right.

- You complete a `solution` function, hit *Run* to test against the samples, then *Submit* to score against the hidden test cases.

- Below we re-solve the same problems here with a live `<CppRunner>`, feeding the sample input through *stdin*.

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/dsa/dsa-2027/w03/dsa-w03-image3.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Online Tools and Judges</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">C++ Building Blocks</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>if</code> statements and <code>for</code> loops</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>vector</code>, <code>stack</code>, and <code>queue</code></span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;"><code>string</code> and <code>sort</code></span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Worked Coding-Test Problems</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">DIY Practice</span></p>
  </div>

</div>

---
layout: prism
heading: "if Statements"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- An [`if` statement]{.hl} lets a program choose an alternative path of execution.

- A [one-way `if`]{.hl} executes its action *if and only if* the condition is `true`:

```cpp
if (boolean-expression) {
    statement(s);
}
```

- Let us code an even/odd number checker.

</div>
<div>

<CppRunner stdin="7">

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;                 // read one integer
    if (n % 2 == 0)           // one-way if
        cout << n << " is even\n";
    if (n % 2 != 0)
        cout << n << " is odd\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "for Loop"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [`for` loop]{.hl} gives a concise syntax that can replace a `while` loop:

```cpp
for (initial-action;
     loop-condition;
     action-after-each-iteration) {
    statement(s);
}
```

- Let us code an odd-number printer.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main() {
    // print the odd numbers in [1, 20]
    for (int i = 1; i <= 20; i++)
        if (i % 2 == 1)
            cout << i << " ";
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "vector Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- C++ provides a generic [`vector`]{.hl} class for storing a list of objects (`#include <vector>`).
  - `vector<int> v;` &nbsp; `vector<string> w;`

- Let us build a `string` vector `["s","u","n","g","s","h","i","n"]`, print it, change the first `"s"` to `"S"`, and print again.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> v = {"s","u","n","g","s","h","i","n"};
    for (auto& c : v) cout << c;
    cout << "\n";
    v[0] = "S";                 // change the first element
    for (auto& c : v) cout << c;
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "stack Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The generic [`stack`]{.hl} class (`#include <stack>`) is a LIFO container.
  - `push(x)` add on top &nbsp; `pop()` remove top
  - `top()` peek &nbsp; `size()` &nbsp; `empty()`

- Let us push `1, 3, 5, 7, 9`, then `pop` three times and watch the `top`.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    for (int x : {1, 3, 5, 7, 9}) s.push(x);
    cout << "size = " << s.size() << "\n";
    for (int i = 0; i < 3; i++) {
        cout << "top = " << s.top() << ", pop\n";
        s.pop();
    }
    cout << "top after 3 pops = " << s.top() << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "queue Class"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The generic [`queue`]{.hl} class (`#include <queue>`) is a FIFO container.
  - `push(x)` add at back &nbsp; `pop()` remove front
  - `front()` peek &nbsp; `size()` &nbsp; `empty()`

- Let us enqueue `"Hi","my","name","is","Gildong."`, then `pop` three times and watch the `front`.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main() {
    queue<string> q;
    for (string w : {"Hi","my","name","is","Gildong."})
        q.push(w);
    cout << "size = " << q.size() << "\n";
    for (int i = 0; i < 3; i++) {
        cout << "front = " << q.front() << ", pop\n";
        q.pop();
    }
    cout << "front after 3 pops = " << q.front() << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "string Data Type"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- C++ provides a [`string`]{.hl} type (`#include <string>`).
  - `append` / `insert` add content
  - `at(i)` or `[i]` access a character
  - `length` returns the size &nbsp; `substr` slices

- Let us build `"C++ Programming"`, append `" is fun!"`, read the first character, and print it character by character.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string str = "C++ Programming";
    str.append(" is fun!");
    cout << str << "\n";
    cout << "first char: " << str[0] << "\n";
    cout << "length: " << str.length() << "\n";
    for (char c : str) cout << c << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "sort Algorithm"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- The standard [`sort`]{.hl} algorithm (`#include <algorithm>`) orders a range in place.
  - `sort(v.begin(), v.end())` — *ascending*
  - `sort(v.rbegin(), v.rend())` — *descending*

- Let us copy `[0,8,2,3,9,1,5]` into `v1, v2, v3`, sort `v2` ascending and `v3` descending, then print all three.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v1 = {0, 8, 2, 3, 9, 1, 5};
    vector<int> v2 = v1, v3 = v1;
    sort(v2.begin(), v2.end());    // ascending
    sort(v3.rbegin(), v3.rend());  // descending
    for (auto* v : {&v1, &v2, &v3}) {
        for (int x : *v) cout << x << ' ';
        cout << "\n";
    }
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Online Tools and Judges</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ Building Blocks</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">Worked Coding-Test Problems</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">No Consecutive Duplicates &nbsp;·&nbsp; Valid Parentheses &nbsp;·&nbsp; Stock Prices <span style="color:#9aa0a6;">(stack)</span></span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Feature Development &nbsp;·&nbsp; Processes &nbsp;·&nbsp; Trucks on a Bridge <span style="color:#9aa0a6;">(queue)</span></span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">DIY Practice</span></p>
  </div>

</div>

---
layout: prism
heading: "No Consecutive Duplicates — Problem"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- An array `arr` of digits (`0`–`9`) is given. Remove [consecutive duplicates]{.hl}, keeping only the first of each run, and return the remaining numbers *in order*.

- Which C++ pieces do we need? — `if`, `for`, `vector`, and the [`stack`]{.hl} ADT (`push`, `top`).

<div class="theorem-box">
<div class="theorem-box-title">Approach</div>
<div class="theorem-box-body">

Feed `arr` into a stack one element at a time; use `top()` to check the most recent element and skip any element equal to it. The kept elements form the answer.

</div>
</div>

| `arr` | `answer` |
|-------|----------|
| `[1, 1, 3, 3, 0, 1, 1]` | `[1, 3, 0, 1]` |
| `[4, 4, 4, 3, 3]` | `[4, 3]` |

---
layout: prism
heading: "No Consecutive Duplicates — Solution"
---

<CppRunner stdin="7
1 1 3 3 0 1 1">

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    stack<int> s;
    s.push(arr[0]);                 // first element always kept
    answer.push_back(arr[0]);
    for (int i = 1; i < (int)arr.size(); i++)
        if (s.top() != arr[i]) {    // a new value appears
            s.push(arr[i]);
            answer.push_back(arr[i]);
        }
    return answer;
}

int main() {
    int n; cin >> n;                // number of elements
    vector<int> arr(n);
    for (auto& x : arr) cin >> x;
    for (int x : solution(arr)) cout << x << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Feature Development — Problem"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- Each feature has a progress and a daily speed; a feature ships once progress reaches `100`. A feature can only ship *together with, or after,* every earlier feature in the list.

- Given `progresses` and `speeds`, return how many features ship on each deployment day. Uses `if`, `for`, `while`, `vector`, and the [`queue`]{.hl} ADT.

<div class="theorem-box">
<div class="theorem-box-title">Approach</div>
<div class="theorem-box-body">

Convert each feature to the number of days it still needs, and enqueue them in order. Walk the queue from the front: every later feature that finishes no later than the current front ships on the same day; a longer one starts a new deployment day.

</div>
</div>

| `progresses` | `speeds` | `return` |
|--------------|----------|----------|
| `[93, 30, 55]` | `[1, 30, 5]` | `[2, 1]` |
| `[95, 90, 99, 99, 80, 99]` | `[1, 1, 1, 1, 1, 1]` | `[1, 3, 2]` |

---
layout: prism
heading: "Feature Development — Solution"
---

<CppRunner stdin="3
93 30 55
1 30 5">

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;
    for (int i = 0; i < (int)progresses.size(); i++) {
        int days = 100 - progresses[i];
        // ceil division: add 1 more day if there is a remainder
        days = days / speeds[i] + (days % speeds[i] != 0);
        q.push(days);
    }
    int day = q.front(), cnt = 1; q.pop();
    while (!q.empty()) {
        int cur = q.front(); q.pop();
        if (day >= cur) cnt++;                 // ships together
        else { answer.push_back(cnt); cnt = 1; day = cur; }
    }
    answer.push_back(cnt);
    return answer;
}

int main() {
    int n; cin >> n;
    vector<int> progresses(n), speeds(n);
    for (auto& x : progresses) cin >> x;
    for (auto& x : speeds) cin >> x;
    for (int x : solution(progresses, speeds)) cout << x << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Valid Parentheses — Problem"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A string `s` of `(` and `)` is [balanced]{.hl} when every `(` is later closed by a matching `)`. Return `true` if balanced, else `false`.

- Which C++ pieces do we need? — `if`, `for`, `string`, and the [`stack`]{.hl} ADT (`push`, `pop`, `empty`).

<div class="theorem-box">
<div class="theorem-box-title">Approach</div>
<div class="theorem-box-body">

Scan left to right. Push on `(`. On `)`, the stack must be non-empty — pop a matching `(`; otherwise the string is invalid. At the end the stack must be empty.

</div>
</div>

| `s` | `answer` |
|-----|----------|
| `"()()"` &nbsp; `"(())()"` | `true` |
| `")()("` &nbsp; `"(()("` | `false` |

---
layout: prism
heading: "Valid Parentheses — Solution"
---

<CppRunner stdin="4
()()
(())()
)()(
(()(">

```cpp
#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool solution(string s) {
    stack<char> st;
    for (char& c : s) {
        if (c == '(') st.push(c);       // opening
        else {                          // closing
            if (st.empty()) return false;
            st.pop();
        }
    }
    return st.empty();                  // nothing left unmatched
}

int main() {
    int t; cin >> t;                    // number of test strings
    while (t--) {
        string s; cin >> s;
        cout << s << " -> " << (solution(s) ? "true" : "false") << "\n";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Processes — Problem"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- A print queue runs processes in FIFO order, but a process only runs if none of the waiting processes has a *higher* priority; otherwise it goes to the back. Given `priorities` and a `location`, return the [running order]{.hl} of the process at that index.

- Uses `if`, `while`, the [`queue`]{.hl} ADT, and `sort`.

<div class="theorem-box">
<div class="theorem-box-title">Approach</div>
<div class="theorem-box-body">

Enqueue each process as `(original index, priority)`. Sort the priorities descending as a reference. Repeatedly inspect the front: if a higher priority is still waiting, requeue it; otherwise run it (count it) and, if it is our target index, report the count.

</div>
</div>

| `priorities` | `location` | `return` |
|--------------|:---:|:---:|
| `[2, 1, 3, 2]` | `2` | `1` |
| `[1, 1, 9, 1, 1, 1]` | `0` | `5` |

---
layout: prism
heading: "Processes — Solution"
---

<CppRunner stdin="6
1 1 9 1 1 1
0">

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int solution(vector<int> priorities, int location) {
    queue<pair<int,int>> q;                   // (index, priority)
    for (int i = 0; i < (int)priorities.size(); i++)
        q.push({i, priorities[i]});
    sort(priorities.rbegin(), priorities.rend());  // descending reference

    int answer = 0, idx = 0;
    while (!q.empty()) {
        auto cur = q.front(); q.pop();
        if (cur.second < priorities[idx]) {   // someone better waits
            q.push(cur);
        } else {                              // run it
            answer++;
            idx++;
            if (cur.first == location) return answer;
        }
    }
    return answer;
}

int main() {
    int n; cin >> n;
    vector<int> priorities(n);
    for (auto& x : priorities) cin >> x;
    int location; cin >> location;
    cout << solution(priorities, location) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Trucks on a Bridge — Problem"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.0em;
}
</style>

- Trucks cross a one-lane bridge in order. The bridge holds `bridge_length` trucks and at most `weight` total. Each time step advances every truck one unit. Return the [total time]{.hl} for all trucks to cross.

- Uses `if`, `while`, and the [`queue`]{.hl} ADT — here the *bridge itself* is modeled as a queue.

<div class="theorem-box">
<div class="theorem-box-title">Approach</div>
<div class="theorem-box-body">

Keep a queue of length `bridge_length` representing bridge slots (a `0` means an empty slot). Each tick: advance time, drop the truck leaving the far end, and if the incoming truck fits under the weight limit push it on, else push a `0`.

</div>
</div>

| `bridge_length` | `weight` | `truck_weights` | `return` |
|:---:|:---:|:---|:---:|
| `2` | `10` | `[7, 4, 5, 6]` | `8` |
| `100` | `100` | `[10]` | `101` |

---
layout: prism
heading: "Trucks on a Bridge — Solution"
---

<CppRunner stdin="2 10
4
7 4 5 6">

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0, idx = 0, sum = 0;
    queue<int> bridge;                              // trucks currently on bridge
    while (true) {
        if (idx == (int)truck_weights.size()) {     // all trucks entered
            answer += bridge_length;                // last truck crosses
            break;
        }
        answer++;                                   // one time step
        if ((int)bridge.size() == bridge_length) {  // a truck leaves the far end
            sum -= bridge.front(); bridge.pop();
        }
        int tmp = truck_weights[idx];
        if (sum + tmp <= weight) {                  // enough capacity
            sum += tmp; bridge.push(tmp); idx++;
        } else {
            bridge.push(0);                         // empty slot, just wait
        }
    }
    return answer;
}

int main() {
    int bridge_length, weight, n;
    cin >> bridge_length >> weight >> n;
    vector<int> truck_weights(n);
    for (auto& x : truck_weights) cin >> x;
    cout << solution(bridge_length, weight, truck_weights) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Stock Prices — Problem"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Given per-second `prices`, for each second report how many seconds the price [did not drop]{.hl} (i.e. until the first later moment with a strictly lower price, or to the end).

- Which C++ pieces do we need? — `if`, `for`, `while`, and the [`stack`]{.hl} ADT.

<div class="theorem-box">
<div class="theorem-box-title">Approach</div>
<div class="theorem-box-body">

Keep a stack of *indices* whose answer is still open. When the price at time `i` is lower than the price at a stacked index `j`, the drop for `j` happens now, so its answer is `i - j`; pop it. Indices left on the stack never dropped, so their answer runs to the end.

</div>
</div>

| `prices` | `return` |
|----------|----------|
| `[1, 2, 3, 2, 3]` | `[4, 3, 1, 1, 0]` |

---
layout: prism
heading: "Stock Prices — Solution"
---

<CppRunner stdin="5
1 2 3 2 3">

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> solution(vector<int> prices) {
    int n = prices.size();
    vector<int> answer(n);
    stack<int> s;                       // indices with an open answer
    for (int i = 0; i < n; i++) {
        while (!s.empty() && prices[s.top()] > prices[i]) {
            answer[s.top()] = i - s.top();   // price dropped now
            s.pop();
        }
        s.push(i);
    }
    while (!s.empty()) {                // never dropped: run to the end
        answer[s.top()] = n - 1 - s.top();
        s.pop();
    }
    return answer;
}

int main() {
    int n; cin >> n;
    vector<int> prices(n);
    for (auto& x : prices) cin >> x;
    for (int x : solution(prices)) cout << x << ' ';
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Homework — HW_W03"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- Use any coding-test resource you like — Baekjoon, Programmers, or a curated set. The six Programmers problems solved in class are *excluded*.

- Find and solve [three problems]{.hl} that use a list, a stack, or a queue. Using additional data structures or algorithms is perfectly fine.

- For each, capture the [problem]{.hl}, your [solution code]{.hl}, and the [test result]{.hl}, and paste them into a Hangul or Word document.
  - Try to solve them yourself without looking at published solutions.
  - If you run out of time, submitting your own honest attempt — even if it does not pass — earns full credit.

- Save as `HW_03_20XXXXXX.pdf` and upload to the LMS.

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Online Tools and Judges</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">C++ Building Blocks</span></p>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">Worked Coding-Test Problems</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">DIY Practice</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Circular Linked List &nbsp;·&nbsp; Doubly Linked List Removal</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">Knight Moves &nbsp;·&nbsp; Postfix Evaluation</span></p>
  </div>

</div>

---
layout: prism
heading: "DIY: Is the Linked List Circular?"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int data; Node* next; Node(int d) : data(d), next(nullptr) {} };

// Floyd's cycle detection: slow moves 1, fast moves 2 steps.
bool isCircular(Node* head) {
    if (!head) return false;
    Node* slow = head;
    Node* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;   // pointers meet => cycle
    }
    return false;
}

int main() {
    Node* a = new Node(1); Node* b = new Node(2); Node* c = new Node(3);
    Node* d = new Node(4); Node* e = new Node(5);
    a->next = b; b->next = c; c->next = d; d->next = e;
    cout << "linear list: " << (isCircular(a) ? "circular" : "not circular") << "\n";
    e->next = c;                          // link tail back to node 3
    cout << "after cycle: " << (isCircular(a) ? "circular" : "not circular") << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY: Removing a Node (Doubly Linked List)"
---

<div style="height: 0.2rem;"></div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

struct Node { int data; Node* prev; Node* next; Node(int d) : data(d), prev(nullptr), next(nullptr) {} };

struct DoublyList {
    Node* head = nullptr;
    void push_back(int v) {
        Node* n = new Node(v);
        if (!head) { head = n; return; }
        Node* t = head; while (t->next) t = t->next;
        t->next = n; n->prev = t;
    }
    void remove(int val) {
        for (Node* temp = head; temp; temp = temp->next) {
            if (temp->data != val) continue;
            if (!temp->prev) { head = temp->next; if (head) head->prev = nullptr; }       // head
            else if (!temp->next) { temp->prev->next = nullptr; }                          // tail
            else { temp->prev->next = temp->next; temp->next->prev = temp->prev; }         // middle
            delete temp; return;
        }
    }
    void print() { for (Node* t = head; t; t = t->next) cout << t->data << ' '; cout << "\n"; }
};

int main() {
    DoublyList L;
    for (int x : {10, 20, 30, 40, 50}) L.push_back(x);
    cout << "initial:   "; L.print();
    L.remove(30); cout << "remove 30: "; L.print();
    L.remove(10); cout << "remove 10: "; L.print();
    L.remove(50); cout << "remove 50: "; L.print();
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "DIY: Knight Moves"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.4rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- On an `8 × 8` board a knight moves in an [L-shape]{.hl} and may not leave the board.

- Given a square such as `A1` or `D4`, print how many moves the knight can make.
  - `A1` &rarr; `2` &nbsp;&nbsp; `D4` &rarr; `8`

- Check all eight candidate offsets and count those that stay on the board.

</div>
<div>

<CppRunner stdin="A1
D4">

```cpp
#include <iostream>
#include <string>
using namespace std;

int knightMoves(const string& pos) {
    int col = pos[0] - 'A';       // 0..7
    int row = pos[1] - '1';       // 0..7
    int dc[] = {1, 1,-1,-1, 2, 2,-2,-2};
    int dr[] = {2,-2, 2,-2, 1,-1, 1,-1};
    int count = 0;
    for (int k = 0; k < 8; k++) {
        int nc = col + dc[k], nr = row + dr[k];
        if (nc >= 0 && nc < 8 && nr >= 0 && nr < 8)
            count++;
    }
    return count;
}

int main() {
    string in;
    while (cin >> in)
        cout << in << " -> " << knightMoves(in) << "\n";
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "DIY: Postfix Evaluation"
---

<div style="height: 0.2rem;"></div>

<CppRunner stdin="23+4*
95-2*">

```cpp
#include <iostream>
#include <string>
#include <stack>
#include <cctype>
using namespace std;

bool isOperator(char c) { return c == '+' || c == '-' || c == '*' || c == '/'; }

int performOperation(char op, int a, int b) {
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return a / b;
        default:  return 0;
    }
}

int evaluatePostfix(const string& expr) {
    stack<int> s;
    for (char c : expr) {
        if (isdigit(c)) s.push(c - '0');           // operand
        else if (isOperator(c)) {                  // apply to top two
            int op2 = s.top(); s.pop();
            int op1 = s.top(); s.pop();
            s.push(performOperation(c, op1, op2));
        }
    }
    return s.top();
}

int main() {
    string expr;
    while (cin >> expr)                            // e.g. 23+4* means (2+3)*4
        cout << expr << " = " << evaluatePostfix(expr) << "\n";
    return 0;
}
```

</CppRunner>

---
layout: center
class: text-center
---

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
