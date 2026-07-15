# 문제 6 · 실습 — 멱집합의 원소 개수

집합을 실제로 만들어 원소 개수를 세고, 멱집합의 크기 $2^{|S|}$를 계산합니다.

<PyRunner>

```python
# x in N0 (0,1,2,...), 조건 x < 50
S = {2 * x + 1 for x in range(50)}
n = len(S)
print(f"집합 S = {{2x+1 : x<50}} 의 원소 개수 |S| = {n}")
print(f"가장 작은 원소 = {min(S)}, 가장 큰 원소 = {max(S)}")
print(f"멱집합의 원소 개수 = 2^{n} = {2 ** n}")
```

</PyRunner>

👉 [문제 6으로 돌아가기](./problem-06)
