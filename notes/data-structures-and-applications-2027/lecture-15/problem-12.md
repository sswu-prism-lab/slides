# 문제 12 · 더블 해싱

::: info 문제 12 [4점]
해시 테이블<span class="gloss">hash table</span>의 충돌<span class="gloss">collision</span> 해결 방법 중 **더블 해싱**<span class="gloss">double hashing</span>에 대해 서술하세요.
:::

::: details 풀이 및 해설
### 개방 주소법의 한 종류

더블 해싱<span class="gloss">double hashing</span>은 충돌이 났을 때 테이블 내의 다른 빈 슬롯을 찾아 저장하는 **개방 주소법**<span class="gloss">open addressing</span>의 한 방식입니다. 핵심은 **탐사 간격**<span class="gloss">probe step</span>을 **두 번째 해시 함수**로 정한다는 점입니다.

`i`번째 탐사 위치는 다음과 같습니다.

$$\text{slot}(k, i) = \bigl(h_1(k) + i \cdot h_2(k)\bigr) \bmod m \qquad (i = 0, 1, 2, \dots)$$

- `h1(k)`: 최초 슬롯을 정하는 1차 해시.
- `h2(k)`: 충돌 시 몇 칸씩 건너뛸지를 정하는 2차 해시.

### 선형·2차 탐사와의 차이

| 방법 | 탐사식 | 문제점 |
| --- | --- | --- |
| 선형 탐사<span class="gloss">linear probing</span> | `h1(k) + i` | 1차 군집화<span class="gloss">primary clustering</span> |
| 2차 탐사<span class="gloss">quadratic probing</span> | `h1(k) + c₁i + c₂i²` | 2차 군집화<span class="gloss">secondary clustering</span> |
| 더블 해싱 | `h1(k) + i·h2(k)` | 위 두 군집화 완화 |

선형·2차 탐사는 최초 슬롯이 같으면 이후 탐사 경로도 같아 원소가 뭉치는 **군집화**가 생깁니다. 더블 해싱은 **키마다 탐사 간격이 달라져** 경로가 흩어지므로 군집화를 크게 줄입니다.

### h2가 만족해야 할 조건

모든 슬롯을 빠짐없이 탐사하려면 2차 해시가 다음을 만족해야 합니다.

- `h2(k) ≠ 0` (간격이 0이면 제자리만 반복).
- `h2(k)`와 테이블 크기 `m`이 **서로소**<span class="gloss">coprime</span>여야 합니다. 그래야 `i`가 커질 때 모든 슬롯을 한 번씩 방문합니다. (예: `m`을 소수로 잡고 `h2(k) = 1 + (k \bmod (m-1))` 로 설계.)

$$\boxed{\text{slot}(k, i) = \bigl(h_1(k) + i \cdot h_2(k)\bigr) \bmod m,\quad \gcd(h_2(k), m)=1}$$

👉 [실습(C++)에서 더블 해싱 삽입 보기](./lab-12)
:::
