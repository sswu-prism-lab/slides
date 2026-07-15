# 문제 13 · 가위-바위-보 프로그램

::: info 문제 13 [5점]
*가위-바위-보* 중 하나를 임의로 선택해서, 사용자의 입력과 비교하여 승패를 출력하는 프로그램의 의사알고리즘<span class="gloss">pseudoalgorithm</span>을 작성(4점)하고, 이것의 시간복잡도<span class="gloss">time complexity</span>를 계산(1점)해서 서술하시오.
:::

::: details 풀이 및 해설

**의사알고리즘**

가위=0, 바위=1, 보=2 로 인코딩한다. 승패는 $(\text{user} - \text{comp}) \bmod 3$ 하나로 판정할 수 있다.

```text
RockPaperScissors(user):            // user ∈ {0,1,2}
    comp ← Random(0, 2)             // 컴퓨터가 임의 선택
    diff ← (user - comp + 3) mod 3
    if diff = 0:
        return "무승부"
    else if diff = 1:               // user가 comp를 이기는 경우
        return "승"
    else:                           // diff = 2
        return "패"
```

판정 규칙의 근거: 각 손은 자기보다 "하나 앞"(가위→보, 바위→가위, 보→바위)을 이긴다. 이를 순환 구조로 보면 $(\text{user}-\text{comp})\bmod 3$ 가 $0$이면 비김, $1$이면 승, $2$이면 패가 된다. 그래서 여러 개의 `if`로 아홉 가지 경우를 나열하지 않고 **한 줄로** 판정할 수 있다.

**시간복잡도**

임의 선택(난수 생성), 뺄셈, 나머지 연산, 비교가 모두 **입력 크기와 무관한 상수 시간** 연산이다. 반복문·재귀가 없다.

$$\boxed{\text{시간복잡도} = \mathcal{O}(1)}$$

여러 판을 $n$번 반복한다면 전체는 $\mathcal{O}(n)$ 이 되지만, 한 판의 승패 판정 자체는 항상 $\mathcal{O}(1)$ 이다.

👉 [실습(C++)에서 확인하기](./lab-13)
:::
