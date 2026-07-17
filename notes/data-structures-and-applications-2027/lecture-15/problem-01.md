# 문제 1 · 깊이 우선 탐색과 자료구조

::: info 문제 1 [1점]
아래 문장이 참이면 O, 거짓이면 X로 답하세요.

> 깊이 우선 탐색<span class="gloss">depth-first search</span>은 큐<span class="gloss">queue</span> 자료구조에 기반해서 구현된다.
:::

::: details 풀이 및 해설
**거짓**입니다.

깊이 우선 탐색<span class="gloss">depth-first search</span>(DFS)은 한 방향으로 갈 수 있는 데까지 깊이 들어갔다가, 막히면 되돌아와 다른 가지를 탐색합니다. 이 "되돌아오기"는 **후입선출**<span class="gloss">last-in first-out</span> 구조인 스택<span class="gloss">stack</span>이 자연스럽게 처리합니다.

- **재귀 구현**: 함수 호출 스택<span class="gloss">call stack</span>이 곧 스택 역할을 합니다.
- **반복 구현**: 명시적 스택에 정점을 넣고 꺼내며 탐색합니다.

반면 큐<span class="gloss">queue</span>는 **선입선출**<span class="gloss">first-in first-out</span> 구조로, 시작점에서 가까운 정점부터 층층이 방문하는 너비 우선 탐색<span class="gloss">breadth-first search</span>(BFS)에 사용됩니다.

| 탐색 | 자료구조 | 방문 순서 |
| --- | --- | --- |
| DFS | 스택 (재귀/명시적) | 깊이 우선 |
| BFS | 큐 | 너비(층) 우선 |

따라서 "DFS가 큐에 기반한다"는 문장은 DFS와 BFS를 뒤바꾼 서술입니다.

$$\boxed{\text{X (거짓)}}$$

👉 [실습(C++)에서 확인하기](./lab-01)
:::
