# 문제 8 · 덱으로 스택과 큐 구현

::: info 문제 8 [3점]
양방향 큐<span class="gloss">double ended queue</span>(덱<span class="gloss">deque</span>)이 앞 삽입(`enqueueFront`), 뒤 삽입(`enqueueRear`), 앞 제거(`dequeueFront`), 뒤 제거(`dequeueRear`)의 4가지 연산을 포함한다고 생각해보자. 이 연산들 중 하나씩만 제거해서 각각 스택<span class="gloss">stack</span>과 큐를 구현하는 방법과 이유를 서술(각 1.5점)하시오.
:::

::: details 풀이 및 해설
덱은 양쪽 끝에서 삽입·삭제가 모두 가능한 가장 일반적인 형태입니다. 연산을 제한하면 스택이나 큐로 특수화할 수 있습니다.

**스택(LIFO) 구현 — 1.5점.**

- 삽입과 삭제가 **같은 한쪽 끝**에서만 일어나야 합니다. 예를 들어 **뒤쪽만** 사용하도록 `enqueueRear`(push)와 `dequeueRear`(pop)만 남기고, **앞쪽 연산(`enqueueFront`, `dequeueFront`)은 쓰지 않습니다.**
- **이유:** 마지막에 뒤로 넣은 원소가 곧바로 뒤에서 나오므로 **후입선출(LIFO)**이 성립합니다. (대칭적으로 앞쪽 두 연산만 남겨도 스택이 됩니다.)

**큐(FIFO) 구현 — 1.5점.**

- 삽입과 삭제가 **서로 반대쪽 끝**에서 일어나야 합니다. 예를 들어 **뒤로 넣고 앞에서 빼도록** `enqueueRear`(뒤 삽입)와 `dequeueFront`(앞 제거)만 남기고, **`enqueueFront`, `dequeueRear`는 쓰지 않습니다.**
- **이유:** 뒤로 들어온 원소가 앞쪽까지 밀려가 먼저 들어온 것부터 나오므로 **선입선출(FIFO)**이 성립합니다.

$$\boxed{\text{스택: 한쪽 끝만 사용(예 } enqueueRear + dequeueRear)\quad\text{큐: 양 끝을 반대로 사용(예 } enqueueRear + dequeueFront)}$$

핵심은 **스택은 삽입·삭제가 같은 끝**, **큐는 삽입·삭제가 반대 끝**이라는 점이며, 덱의 4연산 중 필요 없는 쪽을 배제하여 각각을 얻습니다.
:::
