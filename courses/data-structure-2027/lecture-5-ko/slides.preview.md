---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: DS - Lecture 5 (KO)
download: true
info: |
  ## 자료구조 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/data-structure-2027/lecture-5/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">5주차: 원형 큐와 우선순위 큐</p>

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
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span class="text-gray-900 dark:text-gray-100">원형 큐와 우선순위 큐</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">트리와 트라이</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">중간 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">중간고사</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">힙</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">그래프와 가중치 그래프</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">집합과 맵</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">해시 테이블</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">알고리즘 설계 기법</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">기말 리뷰</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">기말고사</span></p>
  </div>
</div>

---
layout: prism
heading: "요약: 리스트 모델"
---

- 우리는 $A_0, A_1, A_2, \ldots, A_{N-1}$ 형태의 일반적인 리스트를 다루며, 그 *크기*는 $N$이다.
  - 크기가 $0$인 리스트를 [비어있는 리스트]{.hl}라고 한다.
  - 비어있는 리스트를 제외하면, $A_i$는 $A_{i-1}$ $(i < N)$에 *후행*(succeed)하고 $A_{i-1}$은 $A_i$ $(i > 0)$에 *선행*(precede)한다.
  - 리스트에서 원소 $A_i$의 [위치]{.hl}는 $i$이며, 첫 번째 원소는 $A_0$, 마지막 원소는 $A_{N-1}$이다.

- 이러한 정의와 함께 리스트 ADT에 대한 연산들의 집합을 생각할 수 있다:
  - `printList`와 `makeEmpty`는 이름 그대로의 분명한 일을 한다.
  - `find`는 어떤 항목이 처음으로 나타나는 위치를 반환한다.
  - `insert`와 `remove`는 특정 위치에서 원소를 삽입하거나 제거한다.
  - `findKth`는 특정 위치의 원소를 반환한다.

- 어떤 함수가 적절한지에 대한 해석과 특이한 경우의 처리는 전적으로 프로그래머에게 달려 있다(예를 들어 `next`와 `previous`를 추가할 수 있다).

---
layout: prism
heading: "요약: 스택 모델"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [스택]{.hl}은 삽입과 삭제가 오직 한 위치 — *리스트의 가장 끝*, 즉 [탑]{.hl}이라 불리는 곳 — 에서만 수행되도록 제한된 리스트이다.
  - 후입선출(Last-In-First-Out, LIFO) 특성을 가진다.

- 기본 연산은 삽입에 해당하는 `push`와 가장 최근에 삽입된 원소를 삭제하는 `pop`이다.

- 가장 최근에 삽입된 원소는 `pop` 이전에 `top` 연산을 통해 확인할 수 있다.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-01.svg" class="tikz-fig" style="width: 55%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "요약: 큐 모델"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [큐]{.hl} 역시 리스트이지만, 삽입은 한쪽 끝에서 이루어지는 반면 삭제는 *반대쪽 끝*, 즉 [프론트]{.hl}라 불리는 곳에서 수행된다.
  - 선입선출(First-In-First-Out, FIFO) 특성을 가진다.

- 기본 연산은 삽입에 해당하는 `push`와 가장 먼저 삽입된 원소를 삭제하는 `pop`이다.

- 가장 먼저 삽입된 원소는 `pop` 이전에 `front` 연산을 통해 확인할 수 있다.

<div style="margin-top: 2rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-02.svg" class="tikz-fig" style="width: 70%; margin: 0 auto;" />
</div>

---
layout: prism
heading: 원형 큐와 우선순위 큐
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- 이번 강의에서는 큐 자료구조의 두 가지 변형된 버전을 다룬다.

- 이러한 두 가지 변형 큐를 이용하면 다양한 문제에 대해 효율적이고 효과적인 알고리즘을 설계할 수 있다.
  - 우리가 살펴볼 자료구조들은 컴퓨터 과학에서 가장 *근사한* 것들에 속한다.

- 이번 강의에서는 이 두 가지 자료구조를 다루고 구현한다:

<div class="sub-item-enum">

1. [원형 큐]{.hl} 추상 데이터 타입과 그 구현을 소개한다.
2. 기초적인 [힙]{.hl} 추상 데이터 타입을 소개한다.
3. [우선순위 큐]{.hl} 추상 데이터 타입과 그 구현을 소개한다.

</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">원형 큐 ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">원형 큐 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">원형 큐의 구현</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">양방향 큐</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">STL에서의 <code>deque</code></span></p>
    <p style="margin: 2rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">우선순위 큐 ADT</span></p>
  </div>

</div>

---
layout: prism
heading: "원형 큐 모델 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 배열 기반 큐 구현에는 한 가지 약점이 있다: `pop` 연산을 수행하면 사용하지 않는 공간이 남게 된다.

- [원형 큐]{.hl}는 *링 버퍼*라고도 불리며, 고정된 크기의 단일 버퍼를 그 양 끝이 연결된 것처럼 사용한다.

- 이 자료구조는 원형으로 배열된 형태를 나타내며, 연산은 *선입선출* 원칙을 따르되 저장 공간을 효율적으로 활용한다.

- 큐의 크기는 고정되어 있으며, 구현의 첫 단계에서 결정된다.

</div>
<div>

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-03.svg" class="tikz-fig" style="width: 90%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "원형 큐 모델 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 큐의 시작과 끝은 서로 감겨 원을 이룬다.

- 원형 큐는 보통 첫 번째와 마지막 원소를 추적하기 위해 `front`와 `rear` 두 개의 포인터를 사용한다.
  - `front` 포인터는 큐의 *시작* 부분을 가리킨다.
  - `rear` 포인터는 큐의 *끝* 부분을 가리킨다.

- 선형 큐와 마찬가지로, 이 구조는 각각 `push`와 `pop`에 해당하는 [`enqueue`]{.hl}와 [`dequeue`]{.hl} 연산을 가진다.

- `front`는 원소를 큐에서 제거하지 않고 가장 앞 원소를 반환한다.

---
layout: prism
heading: 원형 큐의 구현
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 구현은 큐 역할을 하는 고정된 크기의 배열과, `front`, `rear` 두 개의 포인터를 함께 사용한다.
  - 이 두 포인터는 `-1`과 같은 특수한 값으로 초기화된다.

- 배열은 끝에 도달하면 처음으로 *되감기며* — 여기서 *원형*이라는 이름이 유래한다.

- 포인터 값을 기준으로 큐가 비어 있는지 또는 가득 찼는지 확인할 수 있어, [오버플로우]{.hl}와 [언더플로우]{.hl}를 모두 쉽게 처리할 수 있다.

- 원형 큐는 원소가 제거된 공간을 재사용하여 선형 큐의 공간 낭비 문제를 없앤다.

- 삽입과 제거 연산에 대해 [$\mathcal{O}(1)$]{.hl}의 시간복잡도를 제공한다.

---
layout: prism
heading: "원형 큐 — 구현"
---

```cpp
class CircularQueue {
public:
    explicit CircularQueue(int capacity)
        : arr(capacity), cap(capacity), front(-1), rear(-1) {}

    bool isEmpty() const { return front == -1; }
    bool isFull()  const { return (rear + 1) % cap == front; }

    void enqueue(int x) {              // rear에 삽입
        if (isFull()) return;          // 오버플로우
        if (isEmpty()) front = 0;
        rear = (rear + 1) % cap;       // 되감기
        arr[rear] = x;
    }
private:
    vector<int> arr;
    int cap, front, rear;
    // ... dequeue()와 getFront()는 다음 슬라이드에
};
```

---
layout: prism
heading: "원형 큐 — dequeue와 front"
---

<div style="height: 1.5rem;"></div>

```cpp
int dequeue() {                    // front에서 제거
    if (isEmpty()) return -1;      // 언더플로우
    int x = arr[front];
    if (front == rear)             // 마지막 원소였던 경우
        front = rear = -1;         // 비어있는 상태로 초기화
    else
        front = (front + 1) % cap; // 되감기
    return x;
}

int getFront() const {             // 제거 없이 확인
    return isEmpty() ? -1 : arr[front];
}
```

---
layout: prism
heading: "DIY: 원형 큐"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class CircularQueue {
public:
    explicit CircularQueue(int capacity)
        : arr(capacity), cap(capacity), front(-1), rear(-1) {}
    bool isEmpty() const { return front == -1; }
    bool isFull()  const { return (rear + 1) % cap == front; }
    void enqueue(int x) {
        if (isFull()) { cout << "overflow\n"; return; }
        if (isEmpty()) front = 0;
        rear = (rear + 1) % cap;
        arr[rear] = x;
    }
    int dequeue() {
        if (isEmpty()) return -1;
        int x = arr[front];
        if (front == rear) front = rear = -1;
        else front = (front + 1) % cap;
        return x;
    }
private:
    vector<int> arr;
    int cap, front, rear;
};

int main() {
    CircularQueue q(4);              // 용량 4, 최대 3개 보관
    for (int v : {10, 20, 30}) q.enqueue(v);
    cout << "dequeue -> " << q.dequeue() << "\n";   // 10이 빠짐
    q.enqueue(40);                   // 비워진 자리 재사용 (되감기)
    q.enqueue(50);                   // 오버플로우 (가득 참)
    cout << "drain -> ";
    while (!q.isEmpty()) cout << q.dequeue() << " "; // 20 30 40
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 양방향 큐 모델
---

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- [양방향 큐]{.hl}는 흔히 [덱]{.hl}(*"deck"*으로 발음)이라 불리며, 프론트와 리어 양쪽 끝에서 모두 삽입과 제거를 허용하도록 큐를 일반화한 것이다.

- 리어에서만 삽입하고 프론트에서만 제거하는 단순한 큐와 달리, 덱은 `enqueueFront`, `enqueueRear`, `dequeueFront`, `dequeueRear`의 네 가지 주요 연산을 지원한다.

- 이러한 다재다능함 덕분에 덱은 일반 큐로는 너무 제한적인 다양한 응용에 적합하다.

<div style="margin-top: 1.5rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-04.svg" class="tikz-fig" style="width: 70%; margin: 0 auto;" />
</div>

---
layout: prism
heading: "DIY: 원형 큐를 이용한 덱 구현"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.6rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 원형 큐 구현에서 출발하여, `enqueue`와 `dequeue`를 적절하게 변형하라.

- `enqueueFront`와 `dequeueRear`를 추가하라.
  - 처음과 마지막 원소를 간단하게 확인할 수 있다.

- 테스트 코드를 따라가며 출력될 값을 예측하라.

</div>
<div>

```cpp
int main() {
    Deque dq(10);
    dq.enqueueFront(3);
    dq.enqueueFront(4);
    dq.enqueueRear(11);
    dq.enqueueFront(6);
    dq.dequeueRear();
    dq.dequeueRear();
    cout << dq.front() << endl;
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: "STL에서의 deque"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- C++는 일반적 [`deque`]{.hl} 클래스를 지원한다.

<div class="sub-item">

`#include <deque>`

</div>

<div class="sub-item">

`deque<elementType> dequeName;`

</div>

- `push_front`, `push_back`, `pop_front`, `pop_back`, 그리고 `[]`를 이용한 인덱싱을 지원한다.

</div>
<div>

```cpp
#include <iostream>
#include <deque>
using namespace std;
int main() {
    deque<int> dq;
    dq.push_front(3);
    dq.push_front(4);
    dq.push_back(11);
    dq.push_front(6);
    dq.pop_back();
    dq.pop_front();
    cout << dq[0] << endl;
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: Table of Contents
---
<div style="margin-top: 1.5rem; margin-left: 3rem">

<div>
    <p style="margin: 0.8rem 0; font-size: 1.3rem;"><span style="color:#DBE3EA; font-weight:bold;">원형 큐 ADT</span></p>
    <p style="margin: 0 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">우선순위 큐 ADT</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">우선순위 큐 모델</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">단순 구현</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">이진 힙</span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 0 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">STL에서의 <code>queue</code></span></p>
      <p class="text-gray-900 dark:text-gray-100" style="margin: 0 0 1rem 1.5rem; font-size: 1.1rem;"><span style="font-size:0.75em;">우선순위 큐의 응용</span></p>
  </div>

</div>

---
layout: prism
heading: 우선순위 큐 모델
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [우선순위 큐]{.hl}는 최소한 두 가지 연산을 허용한다: 이름 그대로의 일을 하는 [`insert`]{.hl}와, 최소 원소를 찾아 반환하고 제거하는 [`removeMin`]{.hl}이다.
  - `insert`는 큐의 `push`에 해당한다.
  - `removeMin`은 큐의 `pop`에 해당하는 우선순위 큐의 연산이다.

- 대부분의 자료구조와 마찬가지로, 필요에 따라 다른 연산을 추가할 수 있지만 이는 확장일 뿐 기본 모델의 일부는 아니다.

- 우선순위 큐는 운영체제, 정렬, 탐욕 알고리즘 등 다양한 응용을 가진다.

<div style="margin-top: 1.2rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-05.svg" class="tikz-fig" style="width: 62%; margin: 0 auto;" />
</div>

---
layout: prism
heading: "단순 구현 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- 우선순위 큐를 구현하는 몇 가지 분명한 방법이 있다.
  - 단순한 *연결 리스트*: 프론트에 삽입하면 $\mathcal{O}(1)$이지만, 최소값을 삭제하려면 리스트를 순회하여 $\mathcal{O}(N)$이 든다.
  - *정렬된 리스트*: `insert`는 비용이 크지만($\mathcal{O}(N)$), `removeMin`은 저렴하다($\mathcal{O}(1)$).

- 또 다른 방법은 [이진 탐색 트리]{.hl}를 사용하는 것이다.
  - 이 경우 두 연산 모두 평균 $\mathcal{O}(\log N)$의 실행 시간을 가진다.
  - 삽입은 무작위이고 삭제는 그렇지 않더라도 성립한다.

</div>
<div>

<div style="height: 1.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-06.svg" class="tikz-fig" style="width: 75%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "단순 구현 (2/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 우리가 제거하는 원소는 오직 최소값뿐임을 상기하자.

- *왼쪽* 서브트리의 노드를 반복적으로 제거하면 오른쪽 서브트리가 무거워지면서 트리의 균형을 해치는 것처럼 보인다.
  - 최악의 경우, `removeMin`이 왼쪽 서브트리를 다 소진하고 나면 오른쪽 서브트리는 마땅히 있어야 할 개수의 최대 두 배에 이르는 원소를 가진다.

- 탐색 트리를 사용하는 것은 과잉일 수 있다 — 필요하지 않은 수많은 연산까지 지원하기 때문이다.

- 우리는 *링크 없이*, 두 연산 모두 최악의 경우 [$\mathcal{O}(\log N)$]{.hl} 시간에 우선순위 큐를 구현할 수 있다(삽입은 평균적으로 상수 시간을 소모한다).

---
layout: prism
heading: 이진 힙
---

<style>
.slidev-layout ul > li {
  margin-top: 2em;
}
</style>

- 우리가 사용할 구현은 [이진 힙]{.hl}으로 알려져 있으며, 이를 간단히 *힙*이라 부른다.

- 우선순위 큐 구현에 매우 흔하게 사용되기 때문에, 이 맥락에서는 별다른 수식어 없이 *힙*이라고만 하면 일반적으로 이 자료구조를 가리킨다.

- 이진 탐색 트리와 마찬가지로, 힙은 [구조 성질]{.hl}과 [힙-순서 성질]{.hl}이라는 두 가지 성질을 가진다.

- 힙에서 수행되는 연산은 이 성질들 중 하나를 없앨 수 있으므로, 힙 연산은 모든 힙 성질이 다시 유지될 때까지 종료되어서는 안 된다.

---
layout: prism
heading: "구조 성질 (1/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 힙은 *완전히 차 있는* 이진 트리이며, 다만 가장 아래 레벨은 왼쪽에서 오른쪽으로 채워지는 예외가 허용된다.
  - 이 규칙이 [구조 성질]{.hl}이다.
  - 이러한 트리를 [완전 이진 트리]{.hl}라고 한다.

- 높이 $h$의 완전 이진 트리는 $2^h$개에서 $2^{h+1}-1$개 사이의 노드를 가진다.
  - 이는 높이가 [$\mathcal{O}(\log N)$]{.hl}임을 내포한다.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-07.svg" class="tikz-fig" style="width: 100%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "구조 성질 (2/2)"
---

- 완전 이진 트리는 매우 규칙적이기 때문에 [배열]{.hl}로 표현할 수 있으며, 링크가 필요하지 않다. ($0$번째 원소는 비워 둠에 유의하라.)
  - 배열 위치 $i$의 임의의 원소에 대해, 왼쪽 자식은 위치 $2i$에, 오른쪽 자식은 그 다음 칸인 $2i+1$에 있고, 부모는 $\lfloor i/2 \rfloor$에 있다.

- 트리를 순회하는 연산은 매우 간단하며 대단히 빠르게 수행될 가능성이 높다.
  - 유일한 단점은 최대 힙 크기를 미리 추정해야 한다는 것이지만, 보통 이는 문제가 되지 않는다.

- 힙은 배열과 현재 힙 크기를 나타내는 정수로 구성된다.

<div style="margin-top: 1rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-08.svg" class="tikz-fig" style="width: 82%; margin: 0 auto;" />
</div>

---
layout: prism
heading: 힙-순서 성질
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 연산이 빠르게 수행될 수 있도록 하는 성질이 바로 [힙-순서 성질]{.hl}이다.

- 최소값을 빠르게 찾고자 하므로, 가장 작은 원소가 *루트*에 있어야 한다.
  - 모든 서브트리 또한 힙이라면, 임의의 노드는 그 모든 자손보다 작다.

- 힙-순서 성질: 루트를 제외한 모든 노드 $X$에 대해, $X$의 부모에 있는 키는 $X$의 키보다 작다(또는 같다).

</div>
<div>

<div style="height: 2.5rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-09.svg" class="tikz-fig" style="width: 100%; margin: 0 auto;" />

</div>
</div>

---
layout: prism
heading: "힙 연산 — insert (1/2)"
---

- 원소 $X$를 삽입하려면, 다음으로 가능한 위치에 *공간*(hole)을 만든다(그렇지 않으면 트리가 완전해지지 않는다).
  - $X$를 힙 순서를 위반하지 않고 그 공간에 넣을 수 있다면, 그렇게 하고 끝낸다.
  - 그렇지 않으면 공간의 부모에 있는 원소를 공간으로 밀어 내려 공간을 루트 방향으로 올려보내며, $X$를 놓을 수 있을 때까지 계속한다.

- 이 일반적인 전략이 [스며오르기]{.hl}이다: 새 원소는 올바른 위치를 찾을 때까지 힙 위로 스며올라간다.

- 스며오르기를 반복적인 *교환*으로 구현할 수도 있지만, 교환은 여러 번의 할당이 필요하므로 밀어 내리는 편이 더 저렴하다.

- 새 원소가 최소값이어서 루트까지 끝까지 스며올라가는 경우, 삽입은 최대 [$\mathcal{O}(\log N)$]{.hl} 시간이 걸릴 수 있다.

---
layout: prism
heading: "힙 연산 — insert (2/2)"
---

<div style="margin-top: 0rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-10.svg" class="tikz-fig" style="width: 50%; margin: 0 auto;" />
</div>

<div class="sub-item" style="margin-top: 1rem;">

$14$를 삽입하기: 공간이 마지막 위치에서 스며올라가, 부모($13$)가 더 작아지는 자리를 $14$가 찾을 때까지 올라간다.

</div>

---
layout: prism
heading: "힙 연산 — removeMin (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- `removeMin` 연산은 삽입과 매우 유사하게 처리된다.

- 최소값이 제거되면 *루트*에 공간이 생긴다. 힙이 하나 작아지므로 마지막 원소 $X$는 힙의 어딘가로 옮겨져야 한다.
  - $X$를 그 공간에 놓을 수 있다면 끝낸다.
  - 그럴 가능성은 낮으므로, 공간의 두 자식 중 *더 작은* 쪽을 공간으로 밀어 올려 공간을 한 레벨 아래로 내리고, $X$가 들어맞을 때까지 반복한다.

- 이 일반적인 전략이 [스며내리기]{.hl}이다.

- 이 연산의 최악 실행 시간은 [$\mathcal{O}(\log N)$]{.hl}이다.

---
layout: prism
heading: "힙 연산 — removeMin (2/2)"
---

<div style="margin-top: 0rem;">
<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w05-11.svg" class="tikz-fig" style="width: 65%; margin: 0 auto;" />
</div>

<div class="sub-item" style="margin-top: 1rem;">

$13$을 제거하기: 마지막 원소($31$)가 루트의 공간을 채운 뒤, 각 레벨에서 더 작은 자식을 지나 힙 순서가 회복될 때까지 스며내려간다.

</div>

---
layout: prism
heading: "이진 힙 — insert (스며오르기)"
---

<div style="height: 0rem;"></div>

```cpp
class BinaryHeap {                       // 최소 힙, 1-인덱스 배열
public:
    explicit BinaryHeap(int capacity = 100)
        : array(capacity + 1), currentSize(0) {}
    bool isEmpty() const { return currentSize == 0; }
    const int& findMin() const { return array[1]; }
    void insert(int x) {                 // O(log N)
        if (currentSize == (int)array.size() - 1)
            array.resize(array.size() * 2);
        int hole = ++currentSize;        // 끝에 새 공간
        array[0] = x;                    // 보초값으로 루프 종료
        for (; x < array[hole / 2]; hole /= 2)
            array[hole] = array[hole / 2];   // 부모를 아래로 밀기
        array[hole] = x;                 // x를 놓기
    }
private:
    vector<int> array;
    int currentSize;
    void percolateDown(int hole);        // 다음 슬라이드에
};
```

---
layout: prism
heading: "이진 힙 — deleteMin과 buildHeap"
---

<div style="height: 0.3rem;"></div>

```cpp
void deleteMin() {                       // O(log N)
    if (isEmpty()) return;
    array[1] = array[currentSize--];     // 마지막 원소를 루트로 이동
    percolateDown(1);
}
void buildHeap() {                       // O(N): 제자리에서 힙 구성
    for (int i = currentSize / 2; i > 0; i--)
        percolateDown(i);
}
void percolateDown(int hole) {
    int child, tmp = array[hole];
    for (; hole * 2 <= currentSize; hole = child) {
        child = hole * 2;                // 왼쪽 자식
        if (child != currentSize && array[child + 1] < array[child])
            child++;                     // 더 작은 자식 선택
        if (array[child] < tmp) array[hole] = array[child];
        else break;
    }
    array[hole] = tmp;
}
```

---
layout: prism
heading: "DIY: 이진 힙 (insert / deleteMin)"
---

<CppRunner>

```cpp
#include <iostream>
#include <vector>
using namespace std;

class BinaryHeap {                       // 최소 힙, 1-인덱스
public:
    explicit BinaryHeap(int capacity = 100)
        : array(capacity + 1), currentSize(0) {}
    bool isEmpty() const { return currentSize == 0; }
    int findMin() const { return array[1]; }
    void insert(int x) {
        int hole = ++currentSize;
        array[0] = x;                    // 보초값
        for (; x < array[hole / 2]; hole /= 2)
            array[hole] = array[hole / 2];
        array[hole] = x;
    }
    void deleteMin() {
        array[1] = array[currentSize--];
        percolateDown(1);
    }
private:
    vector<int> array;
    int currentSize;
    void percolateDown(int hole) {
        int child, tmp = array[hole];
        for (; hole * 2 <= currentSize; hole = child) {
            child = hole * 2;
            if (child != currentSize && array[child + 1] < array[child]) child++;
            if (array[child] < tmp) array[hole] = array[child];
            else break;
        }
        array[hole] = tmp;
    }
};

int main() {
    BinaryHeap h;
    for (int v : {13, 21, 16, 24, 31, 19, 68, 65, 26, 32})
        h.insert(v);
    cout << "sorted by repeated deleteMin: ";
    while (!h.isEmpty()) {               // 힙 정렬 순서
        cout << h.findMin() << " ";
        h.deleteMin();
    }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "STL에서의 queue"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- C++는 우선순위 큐 자료구조를 지원하는 일반적 [`priority_queue`]{.hl} 클래스를 제공한다.

<div class="sub-item">

`#include <queue>`

</div>

<div class="sub-item">

`priority_queue<elementType> pqName;`

</div>

- 기본적으로 *최대 힙*이다: `top`은 가장 큰 원소를 반환한다.

</div>
<div>

```cpp
#include <iostream>
#include <queue>
using namespace std;
int main() {
    priority_queue<int> pq;
    pq.push(4);
    pq.push(1);
    pq.push(10);
    while (!pq.empty()) {
        cout << pq.top() << endl;
        pq.pop();
    }
    return 0;
}
```

</div>
</div>

---
layout: prism
heading: "DIY: STL priority_queue"
---

<CppRunner>

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    // 기본: 최대 힙 (가장 큰 값이 위로)
    priority_queue<int> maxpq;
    for (int v : {4, 1, 10, 3, 7}) maxpq.push(v);
    cout << "max-heap order: ";
    while (!maxpq.empty()) { cout << maxpq.top() << " "; maxpq.pop(); }
    cout << "\n";

    // greater<> 비교자를 통한 최소 힙
    priority_queue<int, vector<int>, greater<int>> minpq;
    for (int v : {4, 1, 10, 3, 7}) minpq.push(v);
    cout << "min-heap order: ";
    while (!minpq.empty()) { cout << minpq.top() << " "; minpq.pop(); }
    cout << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "응용 — 운영체제"
---


- 운영체제에서 우선순위 큐는 프로세스와 작업을 그 [우선순위]{.hl}에 따라 관리하는 효과적인 방법이다.
  - 주된 목적은 성능과 응답성을 최적화하기 위해 우선순위가 높은 작업이 낮은 작업보다 먼저 수행되도록 보장하는 것이다.

- 대표적인 응용 중 하나는 프로세스의 [스케쥴링]{.hl}이다.
  - [우선순위 스케쥴링]{.hl}에서는 각 프로세스에 우선순위 레벨이 할당되며, 스케쥴러는 이 레벨을 기준으로 우선순위 큐에서 프로세스를 선택한다.

- 이러한 방식은 *선제적*이거나 *비선제적*일 수 있다:

<div class="sub-item-enum">

1. *선제적*: 실행 중인 프로세스보다 높은 우선순위를 가진 새 프로세스가 도착하면, 현재 프로세스는 선점(일시 중단)되어 큐에 다시 추가되고 새 프로세스가 먼저 실행된다.
2. *비선제적*: 더 높은 우선순위의 프로세스가 도착하더라도 실행 중인 프로세스는 끝까지 완료되며, 새 프로세스는 그다음에 실행된다.

</div>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
