# 문제 10 · 더블 해싱

::: info 문제 10 [3점]
더블 해싱<span class="gloss">double hashing</span>에 대해, 장점과 함께 서술하시오.
:::

::: details 풀이 및 해설

**더블 해싱이란**

개방 주소법<span class="gloss">open addressing</span>의 한 종류로, 충돌<span class="gloss">collision</span>이 일어났을 때 **두 번째 해시 함수**로 계산한 간격만큼 건너뛰며 빈 자리를 찾는다. $i$번째 시도 위치는

$$h(k, i) = \big(h_1(k) + i\cdot h_2(k)\big) \bmod m$$

이다. 여기서 $h_1$ 은 시작 위치, $h_2$ 는 **탐사 간격(step)** 을 결정한다. 흔히 $h_2(k)=R-(k\bmod R)$ ($R$은 테이블 크기보다 작은 소수) 형태로 두고, $h_2(k)\ne 0$ 이 되도록 한다.

**동작**

$h_1(k)$ 자리가 비어 있지 않으면 $h_1(k)+h_2(k),\ h_1(k)+2h_2(k),\ \dots$ 를 차례로 시도한다. 테이블 크기 $m$ 이 **소수**이고 $h_2(k)$ 가 $m$ 과 서로소이면 $m$개의 칸을 모두 방문하므로 빈 자리가 있으면 반드시 찾는다.

**장점**

- **군집화(clustering) 억제**: 선형 조사<span class="gloss">linear probing</span>의 **1차 군집화**(연속된 칸이 뭉치는 현상)와, 2차 조사<span class="gloss">quadratic probing</span>의 **2차 군집화**(같은 초기 위치의 키들이 같은 탐사 순열을 공유하는 현상)를 모두 피한다.
- 탐사 간격 $h_2(k)$ 가 **키마다 달라지므로**, 같은 $h_1$ 값을 갖는 키라도 서로 다른 탐사 경로를 따른다. 그 결과 실제 성능이 **이상적인 균일 해싱(uniform hashing)에 가장 가깝다.**
- 적재율<span class="gloss">load factor</span>이 높아도 상대적으로 탐사 횟수가 적어 성능 저하가 완만하다.

$$\boxed{h(k,i)=\big(h_1(k)+i\,h_2(k)\big)\bmod m,\quad h_2(k)\ne 0,\ \gcd(h_2(k),m)=1}$$
:::
