# 문제 5 · 단순 연결 리스트 역순

::: info 문제 5 [3점]
단순 연결 리스트<span class="gloss">simple linked list</span>의 원소를 전부 역순으로 바꾸는 경우의 성능을 서술(1점)하고, 개선 방안을 서술(2점)하시오.
:::

::: details 풀이 및 해설
**성능(1점).** 단방향 리스트는 **뒤에서 앞으로 거슬러 갈 수 없습니다.** 그래서 소박하게 접근하면, 예컨대 "$i$번째 노드를 찾아 뒤쪽 노드와 값을 맞바꾸는" 식으로 매번 head부터 인덱스를 세며 훑게 되어 접근마다 $\mathcal{O}(N)$, 전체 $\mathcal{O}(N^2)$이 들 수 있습니다.

$$\text{소박한 역순} = \mathcal{O}(N^2)$$

**개선 방안(2점).** 값을 옮기지 말고 **링크(next 포인터)의 방향 자체를 뒤집으면** 한 번의 순회로 끝납니다. 세 개의 포인터 `prev`, `cur`, `next`를 두고, 노드를 하나씩 지나가며 `cur->next`를 `prev` 쪽으로 되돌립니다.

```
prev = null
cur  = head
while cur != null:
    next = cur->next      # 다음 노드 기억
    cur->next = prev      # 링크 방향 뒤집기
    prev = cur            # 한 칸 전진
    cur  = next
head = prev               # prev 가 새 head
```

- 각 노드를 정확히 한 번씩만 방문하므로 **시간 $\mathcal{O}(N)$**, 추가 포인터 몇 개만 쓰므로 **공간 $\mathcal{O}(1)$**입니다.

$$\boxed{\text{소박한 방식 }\mathcal{O}(N^2) \;\longrightarrow\; \text{세 포인터 in-place 뒤집기 }\mathcal{O}(N),\ \mathcal{O}(1)\text{ 공간}}$$

(근본적으로 뒤로 이동이 필요한 작업이 잦다면 처음부터 **이중 연결 리스트<span class="gloss">doubly linked list</span>**로 두는 것도 개선책입니다.)

👉 [실습(C++)에서 확인하기](./lab-05)
:::
