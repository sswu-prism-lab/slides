# 문제 4 · 큐 구현의 두 가지 방법

::: info 문제 4 [2점]
큐<span class="gloss">queue</span>를 구현할 수 있는 두 가지 방법을 연산이 일어나는 위치에 대해 중점적으로 서술(각 1점)하시오.
:::

::: details 풀이 및 해설
큐는 **선입선출(FIFO)** 구조로, 삽입(`enqueue`)은 **뒤쪽(rear)**에서, 삭제(`dequeue`)는 **앞쪽(front)**에서 일어납니다. 삽입과 삭제가 **서로 다른 끝**에서 일어난다는 점이 스택과 다릅니다.

**(1) 배열<span class="gloss">array</span> 기반(순환 배열) 구현**

- `front`와 `rear` 두 인덱스를 두고, `enqueue`는 `rear`를 전진시켜 그 칸에 원소를 넣고, `dequeue`는 `front`가 가리키는 원소를 꺼낸 뒤 `front`를 전진시킵니다.
- 인덱스가 배열 끝에 닿으면 나머지 연산 $(\bmod\ \text{capacity})$으로 처음으로 되돌려 빈 칸을 재사용합니다(원형 큐). 두 연산 모두 원소 이동 없이 $\mathcal{O}(1)$입니다.

**(2) 연결 리스트<span class="gloss">linked list</span> 기반 구현**

- 리스트의 **head를 front**, **tail을 rear**로 삼아 두 포인터를 모두 유지합니다.
- `enqueue`는 **tail 뒤에 새 노드를 붙이고** tail을 갱신, `dequeue`는 **head 노드를 떼어내고** head를 다음으로 옮깁니다.
- 앞과 뒤를 각각 head/tail로 직접 가리키므로 두 연산 모두 $\mathcal{O}(1)$이며 크기 제한이 없습니다.

$$\boxed{\text{삽입은 뒤(rear/tail), 삭제는 앞(front/head) — 서로 다른 양 끝에서 발생}}$$
:::
