# 문제 5 · 이진 트리 중위 순회

::: info 문제 5 [2점]
아래 이진 트리를 중위 순회<span class="gloss">inorder traversal</span>했을 때의 방문 순서를 그래프 모양과 함께 그리시오.

<svg viewBox="0 0 480 300" width="420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="라벨 없는 7노드 이진 트리">
  <g stroke="#333" stroke-width="2">
    <line x1="240" y1="40" x2="150" y2="110"/>
    <line x1="240" y1="40" x2="330" y2="110"/>
    <line x1="150" y1="110" x2="80" y2="185"/>
    <line x1="330" y1="110" x2="255" y2="185"/>
    <line x1="330" y1="110" x2="410" y2="185"/>
    <line x1="255" y1="185" x2="185" y2="260"/>
  </g>
  <g fill="#fff" stroke="#222" stroke-width="2.5">
    <circle cx="240" cy="40" r="22"/>
    <circle cx="150" cy="110" r="22"/>
    <circle cx="330" cy="110" r="22"/>
    <circle cx="80" cy="185" r="22"/>
    <circle cx="255" cy="185" r="22"/>
    <circle cx="410" cy="185" r="22"/>
    <circle cx="185" cy="260" r="22"/>
  </g>
</svg>

원본 트리에는 노드에 값이 없으므로, 아래 풀이에서는 위치에 라벨(A~G)을 붙여 설명합니다.
:::

::: details 풀이 및 해설
### 위치 라벨 부여

각 노드의 위치에 라벨을 붙이면 다음과 같습니다.

<svg viewBox="0 0 480 300" width="420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="위치 라벨 A~G를 붙인 이진 트리">
  <g stroke="#333" stroke-width="2">
    <line x1="240" y1="40" x2="150" y2="110"/>
    <line x1="240" y1="40" x2="330" y2="110"/>
    <line x1="150" y1="110" x2="80" y2="185"/>
    <line x1="330" y1="110" x2="255" y2="185"/>
    <line x1="330" y1="110" x2="410" y2="185"/>
    <line x1="255" y1="185" x2="185" y2="260"/>
  </g>
  <g fill="#eef4ff" stroke="#3b6db3" stroke-width="2.5">
    <circle cx="240" cy="40" r="22"/>
    <circle cx="150" cy="110" r="22"/>
    <circle cx="330" cy="110" r="22"/>
    <circle cx="80" cy="185" r="22"/>
    <circle cx="255" cy="185" r="22"/>
    <circle cx="410" cy="185" r="22"/>
    <circle cx="185" cy="260" r="22"/>
  </g>
  <g fill="#16324f" font-family="sans-serif" font-size="20" font-weight="700" text-anchor="middle" dominant-baseline="central">
    <text x="240" y="40">A</text>
    <text x="150" y="110">B</text>
    <text x="330" y="110">C</text>
    <text x="80" y="185">D</text>
    <text x="255" y="185">E</text>
    <text x="410" y="185">F</text>
    <text x="185" y="260">G</text>
  </g>
</svg>

- **A**: 루트
- A의 왼쪽 자식 **B**, 오른쪽 자식 **C**
- B의 왼쪽 자식 **D** (B의 오른쪽 자식 없음)
- C의 왼쪽 자식 **E**, 오른쪽 자식 **F**
- E의 왼쪽 자식 **G** (E의 오른쪽 자식 없음)

### 중위 순회 규칙

중위 순회<span class="gloss">inorder traversal</span>는 각 노드에서 **왼쪽 서브트리 → 자기 자신 → 오른쪽 서브트리** 순으로 방문합니다.

```
inorder(A)
 ├ inorder(B)
 │   ├ inorder(D) → D
 │   └ 방문 B
 ├ 방문 A
 └ inorder(C)
     ├ inorder(E)
     │   ├ inorder(G) → G
     │   └ 방문 E
     ├ 방문 C
     └ inorder(F) → F
```

왼쪽부터 차례로 확정하면

$$\boxed{D \to B \to A \to G \to E \to C \to F}$$

👉 [실습(C++)에서 중위 순회 확인하기](./lab-05)
:::
