# 문제 3 · $d$-힙의 부모·자식 인덱스

::: info 문제 3 [2점]
$d$-힙<span class="gloss">d-heap</span>에서, 루트<span class="gloss">root</span>, 리프<span class="gloss">leaf</span> 노드가 아닌 $i$번째 노드의 부모<span class="gloss">parent</span> 인덱스와 자식<span class="gloss">child</span> 인덱스는 어떻게 정의되는지 서술(각 1점)하시오.
:::

::: details 풀이 및 해설

$d$-힙은 각 노드가 최대 $d$개의 자식을 갖는 완전 $d$-진 트리를 **배열**에 저장한 것이다. 인덱스를 **1부터** 시작한다고 하면(루트가 1번), $i$번 노드에 대해 다음이 성립한다.

**부모 인덱스**

$$\boxed{\text{parent}(i) = \left\lceil \dfrac{i-1}{d} \right\rceil = \left\lfloor \dfrac{i-2}{d} \right\rfloor + 1}$$

**자식 인덱스**

$i$번 노드의 $d$개 자식은 연속한 칸을 차지한다.

$$\boxed{\text{children}(i) = d(i-1)+2,\ d(i-1)+3,\ \dots,\ d(i-1)+d+1 = d\,i+1}$$

즉 첫째 자식은 $d(i-1)+2$, 마지막 자식은 $di+1$ 이다.

**검산**($d=2$, 즉 이진 힙)

- 자식: $2(i-1)+2 = 2i$ 와 $2i+1$ → 익숙한 좌·우 자식 공식과 일치.
- 부모: $\left\lfloor (i-2)/2 \right\rfloor + 1$. 예를 들어 $i=5$ 이면 $\lfloor 3/2\rfloor+1 = 2$, $i=4$ 이면 $\lfloor 2/2\rfloor+1 = 2$ → 4·5번의 부모가 2번으로 맞다.

(만약 0-기반 인덱스를 쓴다면 $\text{parent}(i)=\left\lfloor (i-1)/d \right\rfloor$, $\text{children}(i)=di+1,\dots,di+d$ 가 된다.)
:::
