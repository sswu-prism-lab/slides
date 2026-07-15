# 리스트 · 스택 · 큐

가장 기본적인 선형<span class="gloss">linear</span> 자료구조들입니다. 원소들이 한 줄로 늘어선 리스트에서 출발하여, 삽입·삭제 위치를 한쪽 끝(스택)이나 양 끝(큐)으로 제한하면 어떤 성질이 생기는지, 그리고 각 연산의 시간 복잡도가 구현 방식에 따라 어떻게 달라지는지를 정리합니다.

## 리스트

$A_0, A_1, A_2, \ldots, A_{N-1}$을 원소로 갖는 일반적인 리스트 ADT를 생각해 봅시다(아래에 나열되지 않은 연산도 필요에 따라 메소드<span class="gloss">method</span>로 추가할 수 있음을 기억하세요).

- `printList` — 리스트 전체를 출력하는 것과 같은 분명한 작업을 수행한다.
- `insert`, `remove` — 각각 리스트 안의 특정 위치에 원소를 삽입하거나 삭제한다.
- `findKth` — 특정 위치($k$번째)의 원소를 반환한다.

### 배열 기반 리스트

배열<span class="gloss">array</span> 기반 리스트 구현은 다음과 같은 장단점을 가집니다.

- `printList`는 선형 시간 $\mathcal{O}(N)$, `findKth`는 상수 시간 $\mathcal{O}(1)$에 수행한다(인덱스로 바로 접근).
- `insert`, `remove`는 삽입·삭제가 일어나는 위치에 따라 시간 복잡도<span class="gloss">time complexity</span>가 커질 수 있다. 배열의 마지막 위치에서의 삽입·삭제는 $\mathcal{O}(1)$이지만, 첫 위치에서는 뒤 원소를 모두 밀어야 하므로 $\mathcal{O}(N)$이다. 따라서 최악의 경우 두 연산은 $\mathcal{O}(N)$이다.

배열 기반으로 구현하더라도, 필요에 따라 크기를 늘려 주는 내장 메소드를 추가할 수 있습니다. 아래는 고정 용량 배열로 리스트를 구현한 예시입니다(실행 시 미초기화 값이 나오지 않도록 배열을 `0`으로 초기화했습니다).

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class ArrayList {
public:
    ArrayList(int size = 10) {   // constructor
        arr = new int[size]();    // dynamic allocation (0으로 초기화)
        capacity = size;
    }
    ~ArrayList() {                // destructor
        delete[] arr;
    }
    void insert(int index, int data) {   // insertion
        if (index < 0 || index >= capacity)
            cout << "Index out of range." << endl;
        arr[index] = data;
    }
    void remove(int index) {             // removal
        if (index < 0 || index >= capacity)
            cout << "Index out of range." << endl;
        for (int i = index; i < capacity - 1; i++)
            arr[i] = arr[i + 1];
    }
    int findKth(int k) {                 // find the element
        if (k < 0 || k >= capacity) {
            cout << "Index out of range." << endl;
            return -1;  // return -1 if there is no such case
        }
        return arr[k];
    }
    void printList() {                   // print the elements
        for (int i = 0; i < capacity; i++)
            cout << arr[i] << " ";
        cout << endl;
    }
private:
    int *arr;       // array
    int capacity;   // the maximum capacity
};

int main() {
    ArrayList list;
    list.insert(0, 3); list.insert(1, 7); list.insert(2, 4);
    list.printList();
    cout << list.findKth(2) << endl;
    list.remove(2);
    list.printList();
    return 0;
}
```

</CppRunner>

### 연결 리스트

삽입과 삭제가 리스트 전반에서, 특히 리스트의 첫 번째 위치에서 자주 일어난다면 배열은 좋은 선택이 아닙니다. 이때 대체제로 연결 리스트<span class="gloss">linked list</span>를 사용할 수 있습니다. 원소들이 메모리 상에 인접하여 저장되지 않도록 하고, 각 노드가 다음 노드의 주소를 포인터로 가리키게 만들어 삽입·삭제에서 발생하던 $\mathcal{O}(N)$을 피합니다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-02.svg" alt="단순 연결 리스트: 각 노드가 다음 노드를 가리키고 마지막 노드는 nullptr을 가리킨다" style="max-width: 460px;" />
  <figcaption class="cap">단순 연결 리스트 — 각 노드가 다음 노드의 주소를 가리키며, 마지막 노드는 <code>nullptr</code>을 가리킨다. 중간 삽입·삭제는 포인터만 바꾸면 된다.</figcaption>
</figure>

배열 기반 리스트와 견주어 복잡도가 정반대로 뒤바뀝니다.

- `printList`는 배열 기반과 마찬가지로 $\mathcal{O}(N)$이다.
- `findKth`는 배열과 달리 앞에서부터 포인터를 따라가야 하므로 $\mathcal{O}(N)$이다.
- 반면 `insert`, `remove`는 (위치를 알고 있다면) 포인터만 고치면 되므로 $\mathcal{O}(1)$이다.

다만 **마지막 원소의 삭제**는 약간 까다롭습니다. 마지막 직전 원소를 찾아 `nullptr`과 연결시켜 주어야 하는데, 다음 노드만 가리키는 단순 연결 리스트<span class="gloss">singly linked list</span>에서는 마지막 직전 원소를 찾기가 어렵기 때문입니다.

### 이중 연결 리스트

모든 노드가 다음 노드뿐 아니라 **직전 노드**와도 연결되도록 리스트를 수정할 수 있으며, 이를 이중 연결 리스트<span class="gloss">doubly linked list</span>라고 합니다. 각 노드가 `prev`와 `next` 두 개의 포인터를 가지므로, 마지막 직전 원소를 찾는 것과 같은 양방향 탐색이 쉬워집니다. 또한 삽입·삭제 시 조건 분기를 줄이기 위해, 항상 비어 있는 머리 노드<span class="gloss">head node</span>와 꼬리 노드<span class="gloss">tail node</span>를 양 끝에 두는 기법을 쓸 수 있습니다.

아래는 머리·꼬리 포인터를 유지하는 이중 연결 리스트 구현입니다. 각 연산이 `prev`/`next`를 어떻게 조정하는지 따라가 보세요.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Node {
public:
    int data; Node* prev; Node* next;   // To avoid spacing
    Node(int data): data(data), prev(nullptr), next(nullptr) {}  // doubly linked
};

class DoublyLinkedList {
public:
    DoublyLinkedList(): head(nullptr), tail(nullptr) {}   // constructor
    ~DoublyLinkedList() {                                  // destructor
        while (head) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }
    void insert(int index, int data) {   // insertion
        Node* newNode = new Node(data);
        if (index == 0) {
            if (head) {
                head->prev = newNode;
                newNode->next = head;
            }
            head = newNode;
            if (!tail)
                tail = newNode;
            return;
        }
        Node* temp = head;
        for (int i = 0; i < index - 1 && temp; i++)
            temp = temp->next;
        if (temp) {
            newNode->next = temp->next;
            newNode->prev = temp;
            if (temp->next)
                temp->next->prev = newNode;
            temp->next = newNode;
            if (temp == tail)
                tail = newNode;
        }
        else {
            cout << "Index out of range." << endl;
            delete newNode;
        }
    }
    void remove(int index) {   // removal
        Node* temp = head;
        int key = 0;
        while (temp != nullptr) {
            if (key == index) {
                if (temp->prev)
                    temp->prev->next = temp->next;
                if (temp->next)
                    temp->next->prev = temp->prev;
                if (temp == head)
                    head = temp->next;
                if (temp == tail)
                    tail = temp->prev;
                delete temp;
                return;
            }
            temp = temp->next;
            key++;
        }
    }
    int findKth(int k) {   // find the element
        Node* temp = head;
        int index = 0;
        while (temp != nullptr && index < k) {
            temp = temp->next;
            index++;
        }
        if (temp != nullptr && index == k)
            return temp->data;
        else {
            cout << "Index out of range." << endl;
            return -1;  // not found
        }
    }
    void printList() {   // print the elements
        for (Node* temp = head; temp != nullptr; temp = temp->next)
            cout << temp->data << " ";
        cout << endl;
    }
private:
    Node* head; Node* tail;   // head and tail pointer
};

int main() {
    DoublyLinkedList dll;
    dll.insert(0, 3); dll.insert(1, 2); dll.insert(2, 4); dll.insert(3, 6);
    dll.printList();
    cout << dll.findKth(3) << endl;
    dll.remove(0);
    dll.printList();
    return 0;
}
```

</CppRunner>

C++ STL에서는 `vector`가 배열 기반 리스트를, `list`가 이중 연결 리스트를 지원합니다. 두 컨테이너의 삽입·접근 방식 차이를 확인해 봅니다.

<CppRunner>

```cpp
#include <vector>
#include <list>
#include <iostream>
using namespace std;

int main() {
    vector<int> v; list<int> l;
    v.push_back(1); v.push_back(2); v.push_back(3); v.pop_back();
    cout << v[1] << endl;                 // 인덱스 접근: O(1)
    l.push_front(1); l.push_front(2); l.push_front(3); l.pop_front();
    cout << l.front() << endl;            // 앞에서 삽입/삭제: O(1)
    return 0;
}
```

</CppRunner>

### 리스트 연산별 시간 복잡도

| 연산 | 배열 기반 리스트 | 연결 리스트 |
| --- | --- | --- |
| `printList` | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| `findKth` | $\mathcal{O}(1)$ | $\mathcal{O}(N)$ |
| `insert` (위치 확보 시) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |
| `remove` (위치 확보 시) | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ |

## 스택

스택<span class="gloss">stack</span>은 삽입과 삭제가 탑<span class="gloss">top</span>이라 불리는 한쪽 끝에서만 수행되도록 제한된 리스트로, 후입선출<span class="gloss">last-in first-out; LIFO</span>의 성질을 가집니다. 나중에 넣은 원소가 먼저 나오는 구조입니다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-04.svg" alt="스택 구조: 원소가 아래에서 위로 쌓이고 top에서만 삽입·삭제가 일어난다" style="max-width: 200px;" />
  <figcaption class="cap">스택 — 원소가 아래에서 위로 쌓이며, 삽입·삭제는 모두 <code>top</code>에서만 일어난다(LIFO).</figcaption>
</figure>

- 리스트의 `insert`에 해당하는 `push`, `remove`에 해당하는 `pop` 연산을 가지며, 다음에 제거될(맨 위) 원소를 반환하는 `top` 연산을 포함한다.
- 스택도 결국 하나의 리스트이므로, 배열 기반 리스트나 연결 리스트 모두 스택을 구현하는 데 사용할 수 있다.
- 대부분의 현대적인 기계는 스택 연산을 하드웨어 수준에서 기본적으로 포함한다.

아래는 연결 리스트로 스택을 구현한 예시입니다. `push`는 새 노드를 맨 앞(top)에 붙이고, `pop`은 맨 앞 노드를 떼어 냅니다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class Node {
public:
    int data; Node* next;   // single link
    Node(int data): data(data), next(nullptr) {}
};

class Stack {
public:
    Stack(): topNode(nullptr) {}   // constructor
    ~Stack() {                      // destructor
        while (topNode != nullptr) {
            Node* temp = topNode;
            topNode = topNode->next;
            delete temp;
        }
    }
    void push(int data) {   // insertion
        Node* newNode = new Node(data);
        newNode->next = topNode;
        topNode = newNode;
    }
    void pop() {            // removal
        if (topNode == nullptr)
            cout << "Stack is empty" << endl;
        Node* temp = topNode;
        topNode = topNode->next;
        int poppedData = temp->data;
        delete temp;
    }
    int top() {             // find the top element
        if (topNode == nullptr) {
            cout << "Stack is empty" << endl;
            return -1; // if the stack is empty
        }
        return topNode->data;
    }
private:
    Node* topNode;
};

int main() {
    Stack s;
    s.push(10); s.push(20); s.push(30);
    cout << s.top() << endl;
    s.pop(); cout << s.top() << endl;
    return 0;
}
```

</CppRunner>

C++의 `stack` STL은 스택 컨테이너를 그대로 지원합니다. 위와 똑같은 동작을 STL로 간결하게 쓸 수 있습니다.

<CppRunner>

```cpp
#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> s;
    s.push(10);
    s.push(20);
    s.push(30);
    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    return 0;
}
```

</CppRunner>

## 큐

큐<span class="gloss">queue</span>는 삽입이 일어나는 곳과 반대편, 즉 프론트<span class="gloss">front</span>에서 삭제가 수행되도록 제한된 리스트로, 선입선출<span class="gloss">first-in first-out; FIFO</span>의 성질을 가집니다. 먼저 들어온 원소가 먼저 나오는, 줄 서기와 같은 구조입니다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-05.svg" alt="큐 구조: 한쪽 front에서 삭제, 반대쪽에서 삽입이 일어난다" style="max-width: 460px;" />
  <figcaption class="cap">큐 — 뒤쪽에서 삽입하고 앞쪽 <code>front</code>에서 삭제한다(FIFO).</figcaption>
</figure>

- `push`, `pop` 외에도, 곧 삭제될(맨 앞) 원소를 확인하는 `front` 연산을 포함한다.
- 큐도 배열 기반 리스트, 연결 리스트를 모두 사용하여 구현할 수 있다.

C++의 `queue` STL은 큐 컨테이너를 지원합니다.

<CppRunner>

```cpp
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    q.push(10); q.push(20); q.push(30);
    cout << q.front() << endl;
    q.pop(); cout << q.front() << endl;
    return 0;
}
```

</CppRunner>

## 원형 큐

배열 기반 큐에는 한 가지 약점이 있습니다. `push`와 `pop`이 계속 활발하게 일어나면, 앞쪽에서 빠져나간 자리(배열 앞부분)가 사용되지 않은 채 남아 공간이 낭비된다는 점입니다. 원형 큐<span class="gloss">circular queue</span>는 링 버퍼<span class="gloss">ring buffer</span>라고도 불리며, **양 끝이 연결된 고정 크기 배열**로 이 문제를 해결합니다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-06.svg" alt="원형 큐(링 버퍼): 양 끝이 연결된 원형 배열에서 front와 rear가 회전한다" style="max-width: 300px;" />
  <figcaption class="cap">원형 큐(링 버퍼) — 배열의 끝이 처음과 이어져, <code>front</code>와 <code>rear</code>가 원을 따라 회전하며 빈 앞자리를 재사용한다.</figcaption>
</figure>

- `front`와 `rear`라는 두 변수로 데이터가 존재하는 첫 부분과 마지막 부분을 표시한다.
- 비어 있는 상태에서는 두 변수 모두 `-1`과 같은 특수한 값을 가진다.
- 원형 큐에서는 종종 삽입과 제거를 `push`, `pop`이 아니라 `enqueue`, `dequeue`로 부른다.
- 인덱스를 계산할 때 `(rear + 1) % bufferSize`처럼 **나머지 연산**을 사용하여, 배열의 끝을 넘어가면 다시 처음으로 되돌아오게 만든다. 가득 찬 상태는 `(rear + 1) % bufferSize == front`로 판정한다.

<CppRunner>

```cpp
#include <iostream>
using namespace std;

class CircularQueue {
public:
    CircularQueue(int size) {   // constructor
        bufferSize = size;
        queue = new int[bufferSize];
        front = -1; // to denote the first element
        rear = -1;  // to denote the last element
    }
    ~CircularQueue() {          // destructor
        delete[] queue;
    }
    bool isFull() {
        return (rear + 1) % bufferSize == front;
    }
    bool isEmpty() {
        return front == -1;
    }
    void enqueue(int value) {   // insertion
        if (isFull()) {
            cout << "Queue is full.";
            return;
        }
        if (isEmpty())
            front = rear = 0;
        else
            rear = (rear + 1) % bufferSize;
        queue[rear] = value;
    }
    void dequeue() {            // removal
        if (isEmpty())
            cout << "Queue is empty.";
        int data = queue[front];
        if (front == rear)
            front = rear = -1; // Queue became empty
        else
            front = (front + 1) % bufferSize;
    }
    void printQueue() {         // print the elements
        if (isEmpty())
            cout << "Queue is empty.";
        int i = front;
        do {
            cout << queue[i] << " ";
            i = (i + 1) % bufferSize;
        }
        while (i != (rear + 1) % bufferSize);
        cout << endl;
    }
private:
    int front; int rear; int bufferSize; int *queue;
};

int main() {
    CircularQueue cq(5);
    cq.enqueue(1); cq.enqueue(2); cq.enqueue(3); cq.enqueue(4);
    cq.printQueue();
    cq.dequeue();
    cq.printQueue();
    cq.enqueue(5); cq.enqueue(6); cq.enqueue(7); // Queue is full.
    cq.printQueue();
    return 0;
}
```

</CppRunner>

원형 큐를 조금 변형하면, 삽입과 삭제가 양 끝에서 모두 일어날 수 있는 양방향 큐<span class="gloss">double-ended queue</span> 자료구조를 설계할 수 있으며, 이를 덱<span class="gloss">deque</span>이라고도 합니다. 덱은 프론트에서의 삽입·삭제를 수행하는 `enqueueFront`, `dequeueFront`와, 리어<span class="gloss">rear</span>에서의 삽입·삭제를 수행하는 `enqueueRear`, `dequeueRear`의 4가지 연산을 기본적으로 포함합니다.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-mid-07.svg" alt="양방향 큐(덱): front와 rear 양쪽 끝에서 모두 삽입·삭제가 가능하다" style="max-width: 460px;" />
  <figcaption class="cap">양방향 큐(덱) — 앞쪽(<code>front</code>)과 뒤쪽(<code>rear</code>) 양 끝에서 모두 삽입·삭제가 가능하다.</figcaption>
</figure>

C++ STL의 `deque`는 덱 컨테이너를 지원합니다.

<CppRunner>

```cpp
#include <iostream>
#include <deque>
using namespace std;

int main() {
    deque<int> dq;
    dq.push_front(3); dq.push_front(4);
    dq.push_back(11); dq.push_front(6);
    dq.pop_back();
    dq.pop_front();
    cout << dq[0] << endl;
    return 0;
}
```

</CppRunner>
