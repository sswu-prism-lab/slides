# 문제 11 · 배열을 힙으로 만들기

::: info 문제 11 [4점]
원소 $N$개를 가지는 임의의 입력 배열<span class="gloss">array</span>을 힙<span class="gloss">heap</span> 자료구조로 바꿀 때의 시간복잡도를 서술(1점)하고, 그 이유에 대해 설명(3점)하시오.
:::

::: details 풀이 및 해설
**시간복잡도(1점).** 상향식 `buildHeap`(아래에서 위로 `percolateDown`)을 쓰면

$$\boxed{\text{buildHeap} = \mathcal{O}(N)}$$

즉 **선형 시간**입니다.

**이유(3점).** `buildHeap`은 배열을 완전 이진 트리로 보고, **마지막 내부 노드(인덱스 $\lfloor N/2\rfloor$ 부근)부터 루트까지** 각 노드에 대해 `percolateDown`(아래로 내리며 힙 성질 회복)을 수행합니다. 한 노드의 `percolateDown` 비용은 그 노드의 **높이 $h$에 비례**합니다.

얼핏 보면 노드마다 $\mathcal{O}(\log N)$이니 총 $\mathcal{O}(N\log N)$처럼 보이지만, 이는 **과대평가**입니다. 핵심은 **대부분의 노드가 트리 아래쪽에 몰려 있어 높이가 작다**는 점입니다.

- 높이가 $h$인 노드는 최대 $\lceil N/2^{\,h+1}\rceil$개 존재합니다. (잎에 가까울수록 노드 수가 많고 높이는 작음)
- 따라서 전체 비용은 각 노드의 높이 합에 비례합니다.

$$
\sum_{h=0}^{\lfloor \log N\rfloor} \left\lceil \frac{N}{2^{\,h+1}} \right\rceil \cdot h
\;\le\; N \sum_{h=0}^{\infty} \frac{h}{2^{\,h+1}}
\;=\; \frac{N}{2}\sum_{h=0}^{\infty}\frac{h}{2^{\,h}}
$$

여기서 급수 $\displaystyle\sum_{h=0}^{\infty} \frac{h}{2^{\,h}} = 2$ 로 **상수에 수렴**합니다. 그러므로

$$
\sum_{h} \left\lceil \frac{N}{2^{\,h+1}} \right\rceil h \;\le\; \frac{N}{2}\cdot 2 \;=\; N \;=\; \mathcal{O}(N).
$$

즉, 높은 노드는 비용이 크지만 그 개수가 매우 적고(루트는 단 1개), 개수가 많은 잎 근처 노드는 비용이 거의 0이라, **높이의 총합이 $\mathcal{O}(N)$으로 억눌려** 전체가 선형 시간이 됩니다.

(참고: 원소를 하나씩 `insert`로 넣는 방식은 각 삽입이 $\mathcal{O}(\log N)$이라 총 $\mathcal{O}(N\log N)$이 됩니다. `buildHeap`이 더 빠릅니다.)

👉 [실습(C++)에서 확인하기](./lab-11)
:::
