# 문제 7 · 트리와 이진 트리의 차이

::: info 문제 7 [3점]
일반적인 트리<span class="gloss">tree</span>와 이진 트리<span class="gloss">binary tree</span>의 차이점을 서술(1점)하고, 두 트리의 노드<span class="gloss">node</span> 구조를 구현할 때의 차이점을 서술(2점)하시오.
:::

::: details 풀이 및 해설
**개념적 차이(1점).**

- **일반 트리**는 한 노드가 가질 수 있는 **자식의 수에 제한이 없습니다.** 자식이 0개일 수도, 여러 개일 수도 있습니다.
- **이진 트리**는 한 노드가 **최대 2개**의 자식만 가지며, 두 자식은 **왼쪽 자식/오른쪽 자식으로 구분(순서가 의미 있음)**됩니다. 자식이 하나뿐이어도 그것이 왼쪽인지 오른쪽인지 구별됩니다.

**노드 구조 구현의 차이(2점).**

이진 트리 노드는 자식 수가 최대 2로 고정이므로, **정확히 두 개의 포인터**를 두면 됩니다.

```cpp
struct BinaryNode {
    T element;
    BinaryNode* left;
    BinaryNode* right;
};
```

반면 일반 트리는 자식 수가 가변이라, 각 노드에 포인터를 몇 개 둘지 미리 정할 수 없습니다. 그래서 보통 **"첫 번째 자식 - 다음 형제(first-child / next-sibling)"** 표현을 씁니다. 즉 노드마다 **자식 하나를 가리키는 링크**와 **바로 옆 형제를 가리키는 링크** 두 개만 두어, 자식이 몇 개든 형제 링크를 따라 연결합니다.

```cpp
struct TreeNode {
    T element;
    TreeNode* firstChild;   // 첫째 자식
    TreeNode* nextSibling;  // 다음 형제
};
```

$$\boxed{\text{이진 트리: }(\text{left},\ \text{right})\text{ 고정 2링크} \quad\text{vs}\quad \text{일반 트리: }(\text{firstChild},\ \text{nextSibling})\text{ 가변 자식 표현}}$$

이처럼 이진 트리는 자식 수가 고정이라 노드 구조가 단순하고, 일반 트리는 가변 자식을 다루기 위해 형제 링크를 이용한 표현이 필요합니다.
:::
