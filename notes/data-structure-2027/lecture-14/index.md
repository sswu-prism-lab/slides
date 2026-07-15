# 자료구조 · 기말고사 요약 (W14)

기말 범위의 핵심 주제를 한 곳에 모은 정리 노트입니다. 고급 힙 자료구조부터
그래프 알고리즘, 서로소 집합, 해시 테이블, 그리고 대표적인 알고리즘 설계 기법까지
차례로 다룹니다. 각 주제 페이지에는 개념 정리와 함께 **실제로 컴파일되는 C++ 실습**을
넣어 두었으니, 정의를 눈으로만 읽지 말고 코드를 직접 돌려 보며 감을 잡는 것을 권합니다.

| 주제 | 내용 |
| --- | --- |
| [d-힙 · 좌향 힙](./advanced-heaps) | d-heap, leftist heap, null path length, merge |
| [그래프 · 최단 경로 · 최소 신장 트리](./graphs) | graph, Dijkstra, Prim, Kruskal |
| [동적 동치 · 서로소 집합](./disjoint-sets) | union-find, union by size/rank, path compression |
| [맵 · 해시 테이블 · 충돌 처리](./hashing) | hashing, 분리 연쇄법, 개방 주소법 |
| [알고리즘 설계 기법](./algorithm-design) | greedy, divide & conquer, DP, randomized, backtracking |

::: tip 사용법
각 페이지의 실습 상자(`<CppRunner>`)는 브라우저에서 원격 컴파일 서버로 **실제 g++**
를 실행해 표준출력 결과를 보여 줍니다. 코드를 자유롭게 고쳐 가며 입력을 바꿔 보고,
출력이 어떻게 달라지는지 관찰하면 자료구조와 알고리즘의 동작 원리가 훨씬 또렷해집니다.
:::

> 제작: 성신여자대학교 AI융합학부 고원준 (<a href="mailto:wjko@sungshin.ac.kr" class="rainbow-link">wjko@sungshin.ac.kr</a>)
