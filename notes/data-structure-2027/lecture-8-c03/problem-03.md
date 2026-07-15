# 문제 3 · 전위 순회

::: info 문제 3 [2점]
전위 순회<span class="gloss">preorder traversal</span>에 대해 서술하고(1점), 아래 트리를 전위 순회하였을 때의 방문 순서를 나열(1점)하시오.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w08c03-01.svg" alt="전위 순회 대상 트리" style="max-width: 360px;" />
  <figcaption class="cap">문제 3의 이진 트리</figcaption>
</figure>
:::

::: details 풀이 및 해설
**전위 순회**는 각 노드에서 다음 순서를 재귀적으로 따르는 깊이 우선 순회입니다.

$$\text{루트(자기 자신)} \;\rightarrow\; \text{왼쪽 서브트리} \;\rightarrow\; \text{오른쪽 서브트리}$$

즉 **노드를 먼저 방문(출력)한 뒤** 왼쪽, 오른쪽 자식 서브트리를 같은 방식으로 순회합니다.

주어진 트리의 구조는 다음과 같습니다.

```
        A
      /   \
     B     C
    /     / \
   D     F   G
        /
       H
```

전위 순회를 따라가면

1. 루트 `A` 방문
2. `A`의 왼쪽 서브트리: `B` → 그 왼쪽 `D`
3. `A`의 오른쪽 서브트리: `C` → 그 왼쪽 `F` → `F`의 왼쪽 `H` → 다시 `C`의 오른쪽 `G`

$$\boxed{A \;\to\; B \;\to\; D \;\to\; C \;\to\; F \;\to\; H \;\to\; G}$$

👉 [실습(C++)에서 확인하기](./lab-03)
:::
