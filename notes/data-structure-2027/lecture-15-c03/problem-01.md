# 문제 1 · 연결 리스트 역순의 성능

::: info 문제 1 [3점]
단순 연결 리스트<span class="gloss">simple linked list</span>의 원소를 전부 역순으로 바꾸는 경우의 성능을 서술(1점)하고, 개선 방안을 서술(2점)하시오.
:::

::: details 풀이 및 해설

**성능**

단순(단방향) 연결 리스트는 각 노드가 **다음 노드로 향하는 포인터 하나만** 가진다. 따라서 어떤 노드에서 "이전 노드"로 되돌아갈 방법이 없다.

- 순진하게 "각 원소를 마지막 자리로 옮긴다"는 식으로 접근하면, 매번 리스트 끝을 다시 찾아 이동해야 하므로 $\mathcal{O}(N^2)$ 이 든다.
- 제대로 구현하더라도 리스트 전체를 최소 한 번은 순회해야 하므로 역순화 자체의 하한은 $\mathcal{O}(N)$ 이다.

$$\boxed{\text{올바른 역순화의 시간복잡도} = \mathcal{O}(N),\quad \text{추가 공간} = \mathcal{O}(1)}$$

**개선 방안**

1. **제자리(in-place) 포인터 뒤집기** — 세 개의 포인터(`prev`, `cur`, `next`)를 이용해 리스트를 **한 번만** 순회하면서 각 노드의 `next` 포인터를 앞 노드로 바꿔 준다. 시간 $\mathcal{O}(N)$, 추가 공간 $\mathcal{O}(1)$ 로 최적이다.

   ```text
   prev ← NULL
   cur  ← head
   while cur ≠ NULL:
       next ← cur.next
       cur.next ← prev      // 방향을 뒤집는다
       prev ← cur
       cur  ← next
   head ← prev
   ```

2. **이중 연결 리스트<span class="gloss">doubly linked list</span> 사용** — 각 노드가 `prev`, `next`를 모두 가지면, 원소를 실제로 옮기지 않고 **탐색 방향만 바꿔** 역순으로 순회할 수 있다(꼬리 포인터 유지 시 $\mathcal{O}(1)$ 로 역방향 접근 시작 가능). 다만 포인터가 하나 늘어 저장 공간 부담이 커진다.

핵심은 "각 노드를 옮기지 말고 **포인터만 조작**한다"는 것이며, 이렇게 하면 $\mathcal{O}(N^2)$ 이 $\mathcal{O}(N)$ 으로 개선된다.
:::
