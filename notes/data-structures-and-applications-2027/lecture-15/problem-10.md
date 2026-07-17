# 문제 10 · 안정 정렬

::: info 문제 10 [3점]
안정성을 유지하는 정렬<span class="gloss">stable sort</span>에 대해 설명하고, 그 예시를 서술하세요.
:::

::: details 풀이 및 해설
### 정의

**안정 정렬**<span class="gloss">stable sort</span>이란, **키가 같은 원소들의 상대적 순서**가 정렬 전과 후에 그대로 보존되는 정렬을 말합니다.

예를 들어 (이름, 점수) 쌍을 점수 기준으로 정렬할 때, 점수가 같은 두 사람은 원래 입력에 있던 앞뒤 순서 그대로 유지됩니다. 이는 **여러 기준으로 차례차례 정렬**(예: 점수 정렬 후 다시 다른 키로 정렬)할 때 이전 정렬 결과를 망치지 않아 매우 중요합니다.

예시로, 키가 같은 원소를 앞의 것은 `a1`, 뒤의 것은 `a2`라 하면

$$\text{입력: } \dots a_1 \dots a_2 \dots \;\Rightarrow\; \text{안정 정렬 후에도 } a_1 \text{가 } a_2 \text{보다 앞}$$

### 안정 / 불안정 정렬 예시

| 안정<span class="gloss">stable</span> | 불안정<span class="gloss">unstable</span> |
| --- | --- |
| 병합 정렬<span class="gloss">merge sort</span> | 선택 정렬<span class="gloss">selection sort</span> |
| 삽입 정렬<span class="gloss">insertion sort</span> | 퀵 정렬<span class="gloss">quicksort</span> |
| 버블 정렬<span class="gloss">bubble sort</span> | 힙 정렬<span class="gloss">heap sort</span> |
| 계수 정렬<span class="gloss">counting sort</span> · 기수 정렬<span class="gloss">radix sort</span> | |

불안정 정렬도 같은 키의 순서까지 신경 쓰면 안정화할 수 있지만(예: 원래 인덱스를 보조 키로 추가), 추가 비용이 듭니다. C++ 표준 라이브러리는 안정 정렬로 `std::stable_sort`를, 일반(불안정 가능) 정렬로 `std::sort`를 제공합니다.

$$\boxed{\text{같은 키 원소의 상대 순서를 보존하는 정렬} \;(\text{예: 병합·삽입·계수 정렬})}$$

👉 [실습(C++)에서 `std::stable_sort` 시연 보기](./lab-10)
:::
