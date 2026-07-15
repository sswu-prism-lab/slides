# 문제 14 · 실습 — 조건을 만족하는 집합 전수조사

$4$원소 전체집합의 모든 부분집합 조합을 탐색해, 세 조건을 동시에 만족하는 $(A,B,C)$가 존재하는지 확인합니다.

<PyRunner>

```python
from itertools import product

U = range(4)
def all_subsets():
    for bits in product([0, 1], repeat=4):
        yield frozenset(i for i in U if bits[i])

subsets = list(all_subsets())
found = None
for A in subsets:
    for B in subsets:
        for C in subsets:
            if (A | B) == (A | C) and (A & B) == (A & C) and B != C:
                found = (A, B, C)
print(f"탐색한 (A,B,C) 조합 수 = {len(subsets) ** 3}")
print("세 조건을 동시에 만족하는 (A,B,C) 존재? ", found is not None)
print("=> 조건 1,2가 성립하면 항상 B=C 이므로 반례가 없습니다.")
```

</PyRunner>

👉 [문제 14로 돌아가기](./problem-14)
