# 문제 12 · 실습 — 재현율·정밀도·F1

혼동행렬<span class="gloss">confusion matrix</span>의 TP, FP, FN을 세어 세 지표를 계산합니다.

<PyRunner>

```python
import numpy as np

y  = np.array([1, 0, 0, 1, 1, 1, 0, 1, 1, 1])   # 정답
yh = np.array([0, 1, 1, 1, 1, 0, 1, 0, 1, 0])   # 예측

TP = int(np.sum((y == 1) & (yh == 1)))
FP = int(np.sum((y == 0) & (yh == 1)))
FN = int(np.sum((y == 1) & (yh == 0)))

recall = TP / (TP + FN)
precision = TP / (TP + FP)
f1 = 2 * precision * recall / (precision + recall)

print(f"TP={TP}, FP={FP}, FN={FN}")
print(f"recall    = {recall:.4f}  (= 3/7)")
print(f"precision = {precision:.4f}  (= 1/2)")
print(f"F1        = {f1:.4f}  (= 6/13)")
```

</PyRunner>

👉 [문제 12로 돌아가기](./problem-12)
