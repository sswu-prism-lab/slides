# 문제 2 · 계수 정렬과 실수 배열

::: info 문제 2 [1점]
아래 문장이 참이면 O, 거짓이면 X로 답하세요.

> 계수 정렬<span class="gloss">counting sort</span>은 실수<span class="gloss">real number</span>로 이루어진 배열에 대해서 적용할 수 있다.
:::

::: details 풀이 및 해설
**거짓**입니다.

계수 정렬<span class="gloss">counting sort</span>은 각 키 값을 **배열의 인덱스**로 사용해 그 값이 몇 번 등장했는지 세는 방식입니다. 따라서 키가 반드시 **정수**<span class="gloss">integer</span>(또는 유한한 정수 범위로 사상 가능한 값)여야 합니다.

실수<span class="gloss">real number</span>는

- 인덱스로 직접 쓸 수 없고(`count[3.14]`는 불가),
- 어떤 구간이든 무한히 많은 값이 존재하여 계수 배열의 크기를 정할 수 없습니다.

그래서 실수 배열은 계수 정렬로 정렬할 수 없습니다. 실수를 다루려면 값의 범위를 구간(버킷)으로 나누는 버킷 정렬<span class="gloss">bucket sort</span>이나 비교 기반 정렬<span class="gloss">comparison sort</span>을 씁니다.

$$\boxed{\text{X (거짓)}}$$

👉 [실습(C++)에서 확인하기](./lab-02)
:::
