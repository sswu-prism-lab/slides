# 문제 9 · 요소의 주소와 값 반환

::: info 문제 9 [3점]
아래 문제를 풀기 위한 코드 혹은 의사알고리즘<span class="gloss">pseudo-algorithm</span>을 작성하세요.

임의의 배열과 배열의 크기보다 작은 정수를 입력으로 받아 그 정수의 요소의 주소와 값을 반환하는 함수
:::

::: details 풀이 및 해설
입력으로 받은 정수 `index`를 배열의 인덱스로 사용합니다. 배열이 `index < 크기`를 만족하므로 `list[index]`는 유효한 요소입니다.

- **요소의 주소**: `&list[index]` (또는 `list + index`).
- **요소의 값**: `list[index]` (또는 `*(list + index)`).

**의사알고리즘**

```
함수 findElement(list, index):
    주소 ← &list[index]     // 요소가 저장된 메모리 주소
    값   ← list[index]      // 그 주소에 담긴 값
    return (주소, 값)
```

C++에서는 값 하나만 `return`할 수 있으므로, 주소와 값을 함께 돌려주려면 **포인터/참조 매개변수로 결과를 채워 주거나** `pair`(또는 구조체)로 묶어 반환합니다. 주소와 값의 관계는

$$\text{주소} = \&\,list[index], \qquad \text{값} = *(\&\,list[index]) = list[index]$$

$$\boxed{\text{주소} = \&list[index],\ \ \text{값} = list[index]}$$

👉 [실습(C++)에서 확인하기](./lab-09)
:::
