# 문제 6 · 레드-블랙 트리 삽입

::: info 문제 6 [2점]
아래 레드-블랙 트리<span class="gloss">red-black tree</span>에서 키 `7`이 삽입되고 균형을 맞추기까지의 과정을 그래프 모양과 함께 그리시오.

<svg viewBox="0 0 560 300" width="440" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="삽입 전 레드-블랙 트리">
  <g stroke="#333" stroke-width="2">
    <line x1="280" y1="40" x2="170" y2="110"/>
    <line x1="280" y1="40" x2="400" y2="110"/>
    <line x1="170" y1="110" x2="100" y2="180"/>
    <line x1="170" y1="110" x2="240" y2="180"/>
    <line x1="400" y1="110" x2="470" y2="180"/>
    <line x1="100" y1="180" x2="60" y2="250"/>
    <line x1="240" y1="180" x2="300" y2="250"/>
  </g>
  <g stroke="#000" stroke-width="2">
    <circle cx="280" cy="40" r="19" fill="#1b1b1b"/>
    <circle cx="170" cy="110" r="19" fill="#e01b1b"/>
    <circle cx="400" cy="110" r="19" fill="#1b1b1b"/>
    <circle cx="100" cy="180" r="19" fill="#1b1b1b"/>
    <circle cx="240" cy="180" r="19" fill="#1b1b1b"/>
    <circle cx="470" cy="180" r="19" fill="#e01b1b"/>
    <circle cx="60" cy="250" r="19" fill="#e01b1b"/>
    <circle cx="300" cy="250" r="19" fill="#e01b1b"/>
  </g>
  <g fill="#fff" font-family="sans-serif" font-size="15" font-weight="700" text-anchor="middle" dominant-baseline="central">
    <text x="280" y="40">10</text>
    <text x="170" y="110">5</text>
    <text x="400" y="110">13</text>
    <text x="100" y="180">3</text>
    <text x="240" y="180">6</text>
    <text x="470" y="180">15</text>
    <text x="60" y="250">2</text>
    <text x="300" y="250">8</text>
  </g>
</svg>

(빨강 = 붉은 원, 검정 = 검은 원. 루트 10은 검정입니다.)
:::

::: details 풀이 및 해설
### 1단계 — 이진 탐색 트리 규칙으로 삽입 위치 찾기

새 키 `7`은 항상 **빨강**<span class="gloss">red</span>으로 삽입합니다. 루트부터 내려갑니다.

- `7 < 10` → 왼쪽으로 (5)
- `7 > 5` → 오른쪽으로 (6)
- `7 > 6` → 오른쪽으로 (8)
- `7 < 8` → 8의 **왼쪽 자식**으로 삽입

<svg viewBox="0 0 560 330" width="440" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="7 삽입 직후, 이중 빨강 위반">
  <g stroke="#333" stroke-width="2">
    <line x1="280" y1="40" x2="170" y2="110"/>
    <line x1="280" y1="40" x2="400" y2="110"/>
    <line x1="170" y1="110" x2="100" y2="180"/>
    <line x1="170" y1="110" x2="240" y2="180"/>
    <line x1="400" y1="110" x2="470" y2="180"/>
    <line x1="100" y1="180" x2="60" y2="250"/>
    <line x1="240" y1="180" x2="300" y2="250"/>
    <line x1="300" y1="250" x2="255" y2="315" stroke="#e01b1b" stroke-width="3"/>
  </g>
  <g stroke="#000" stroke-width="2">
    <circle cx="280" cy="40" r="19" fill="#1b1b1b"/>
    <circle cx="170" cy="110" r="19" fill="#e01b1b"/>
    <circle cx="400" cy="110" r="19" fill="#1b1b1b"/>
    <circle cx="100" cy="180" r="19" fill="#1b1b1b"/>
    <circle cx="240" cy="180" r="19" fill="#1b1b1b"/>
    <circle cx="470" cy="180" r="19" fill="#e01b1b"/>
    <circle cx="60" cy="250" r="19" fill="#e01b1b"/>
    <circle cx="300" cy="250" r="19" fill="#e01b1b"/>
    <circle cx="255" cy="315" r="19" fill="#e01b1b" stroke="#7a0f0f" stroke-width="3"/>
  </g>
  <g fill="#fff" font-family="sans-serif" font-size="15" font-weight="700" text-anchor="middle" dominant-baseline="central">
    <text x="280" y="40">10</text>
    <text x="170" y="110">5</text>
    <text x="400" y="110">13</text>
    <text x="100" y="180">3</text>
    <text x="240" y="180">6</text>
    <text x="470" y="180">15</text>
    <text x="60" y="250">2</text>
    <text x="300" y="250">8</text>
    <text x="255" y="315">7</text>
  </g>
</svg>

이제 **7(빨강)–8(빨강)** 이 부모–자식으로 나란히 빨강이 되어 **이중 빨강 위반**<span class="gloss">red-red violation</span>이 생깁니다.

### 2단계 — 케이스 판정

- 새 노드 `z = 7`, 부모 `= 8`(빨강), 조부모 `= 6`(검정)
- 삼촌<span class="gloss">uncle</span> = 6의 왼쪽 자식 = **nil(검정)**

삼촌이 검정이므로 **회전**<span class="gloss">rotation</span>으로 해결합니다. 부모 8은 조부모 6의 **오른쪽** 자식이고, `z(7)`은 부모 8의 **왼쪽** 자식이므로 이는 **오른쪽-왼쪽(RL) 케이스**입니다.

### 3단계 — 회전과 재색칠

RL 케이스는 두 번의 회전이 필요합니다.

1. **부모 8에서 우회전**<span class="gloss">right rotation</span>: 7이 위로 올라가 6의 오른쪽 자식이 되고, 8은 7의 오른쪽 자식이 됩니다. → 이제 6–7–8이 한쪽으로 정렬된 RR 형태.
2. **조부모 6에서 좌회전**<span class="gloss">left rotation</span>: 7이 다시 위로 올라가 부분 트리의 꼭대기가 되고, 6은 7의 왼쪽 자식, 8은 7의 오른쪽 자식이 됩니다.
3. **재색칠**<span class="gloss">recolor</span>: 새 꼭대기 7 → **검정**, 두 자식 6·8 → **빨강**.

결과적으로 5의 오른쪽 자식이 **7(검정)** 이 되고, 7의 두 자식은 **6(빨강)·8(빨강)** 이 됩니다.

<svg viewBox="0 0 560 300" width="440" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="회전과 재색칠 후 완성된 레드-블랙 트리">
  <g stroke="#333" stroke-width="2">
    <line x1="280" y1="40" x2="170" y2="110"/>
    <line x1="280" y1="40" x2="400" y2="110"/>
    <line x1="170" y1="110" x2="100" y2="180"/>
    <line x1="170" y1="110" x2="240" y2="180"/>
    <line x1="400" y1="110" x2="470" y2="180"/>
    <line x1="100" y1="180" x2="60" y2="250"/>
    <line x1="240" y1="180" x2="200" y2="250"/>
    <line x1="240" y1="180" x2="300" y2="250"/>
  </g>
  <g stroke="#000" stroke-width="2">
    <circle cx="280" cy="40" r="19" fill="#1b1b1b"/>
    <circle cx="170" cy="110" r="19" fill="#e01b1b"/>
    <circle cx="400" cy="110" r="19" fill="#1b1b1b"/>
    <circle cx="100" cy="180" r="19" fill="#1b1b1b"/>
    <circle cx="240" cy="180" r="19" fill="#1b1b1b"/>
    <circle cx="470" cy="180" r="19" fill="#e01b1b"/>
    <circle cx="60" cy="250" r="19" fill="#e01b1b"/>
    <circle cx="200" cy="250" r="19" fill="#e01b1b"/>
    <circle cx="300" cy="250" r="19" fill="#e01b1b"/>
  </g>
  <g fill="#fff" font-family="sans-serif" font-size="15" font-weight="700" text-anchor="middle" dominant-baseline="central">
    <text x="280" y="40">10</text>
    <text x="170" y="110">5</text>
    <text x="400" y="110">13</text>
    <text x="100" y="180">3</text>
    <text x="240" y="180">7</text>
    <text x="470" y="180">15</text>
    <text x="60" y="250">2</text>
    <text x="200" y="250">6</text>
    <text x="300" y="250">8</text>
  </g>
</svg>

루트에서 어떤 리프로 가든 검정 노드 수(검정 높이<span class="gloss">black height</span>)가 같아지고, 빨강이 연속되지 않아 레드-블랙 트리의 성질이 다시 만족됩니다.

$$\boxed{\text{5의 오른쪽 자식 } 7(\text{검정}),\ 7.\text{left}=6(\text{빨강}),\ 7.\text{right}=8(\text{빨강})}$$

👉 [실습(C++)에서 확인하기](./lab-06)
:::
