# 문제 7 · 원형 큐

::: info 문제 7 [3점]
원형 큐<span class="gloss">circular queue</span>가 일반적인 선형 큐와 비교하여 가지고 있는 장점(1점)을 서술하고, 삽입(`enqueue`)과 제거(`dequeue`) 연산의 수행 방식을 서술(각 1점)하시오.
:::

::: details 풀이 및 해설
**장점(1점).** 배열로 구현한 **선형 큐**는 `dequeue`가 반복되면 `front`가 계속 오른쪽으로 이동하여, 배열 앞쪽의 **빈 칸을 재사용하지 못합니다.** 뒤쪽(`rear`)이 배열 끝에 닿으면 앞이 비어 있어도 "가득 참"으로 판단되는 **거짓 오버플로**가 생기고, 이를 피하려면 원소를 앞으로 밀어야 해 $\mathcal{O}(N)$이 듭니다.

**원형 큐**는 배열의 끝과 처음을 논리적으로 이어 붙여, 뒤쪽이 끝에 닿으면 **다시 배열 앞쪽의 빈 칸을 재사용**합니다. 덕분에 원소 이동 없이 **배열 전체를 낭비 없이** 쓸 수 있는 것이 가장 큰 장점입니다.

**삽입 `enqueue`(1점).** `rear`를 원형으로 한 칸 전진시킨 뒤 그 칸에 원소를 넣습니다.

$$\text{rear} \leftarrow (\text{rear} + 1) \bmod \text{capacity},\qquad \text{arr[rear]} \leftarrow x$$

**제거 `dequeue`(1점).** `front`가 가리키는 원소를 꺼낸 뒤 `front`를 원형으로 한 칸 전진시킵니다.

$$x \leftarrow \text{arr[front]},\qquad \text{front} \leftarrow (\text{front} + 1) \bmod \text{capacity}$$

$$\boxed{\text{나머지 연산}(\bmod\ \text{capacity})\text{으로 인덱스를 순환시켜 빈 칸을 재사용, 두 연산 모두 } \mathcal{O}(1)}$$

가득 참/비어 있음은 원소 개수를 세거나 한 칸을 비워 두는 방식으로 구분합니다.
:::
