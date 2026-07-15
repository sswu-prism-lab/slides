# 문제 1 · 실습 — 진법 변환

$1995$를 $3$으로 반복해서 나눈 나머지로 3진법 표현을 만들고, 다시 10진법으로 검산합니다.

<PyRunner>

```python
n = 1995
q, digits = n, []
while q > 0:
    digits.append(q % 3)   # 나머지 저장
    q //= 3
base3 = ''.join(str(d) for d in reversed(digits))
print(f"1995(10) = {base3}(3)")
print("검산(3진 -> 10진):", int(base3, 3))
```

</PyRunner>

👉 [문제 1로 돌아가기](./problem-01)
