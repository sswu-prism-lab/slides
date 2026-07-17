# 문제 1 · 예약어와 식별자

::: info 문제 1 [1점]
아래 문장을 읽고 O/X로 답하세요.

C++에서 예약어<span class="gloss">reserved word</span>는 식별자<span class="gloss">identifier</span>로 사용할 수 있다.
:::

::: details 풀이 및 해설
답은 **X** 입니다.

**예약어**(키워드<span class="gloss">keyword</span>)는 `int`, `for`, `return`, `class`처럼 언어가 문법적으로 특별한 의미를 갖도록 미리 예약해 둔 단어입니다. 컴파일러가 이를 문법 요소로 해석하기 때문에, 변수·함수·클래스 등의 **이름(식별자)으로는 사용할 수 없습니다.**

```cpp
int int = 3;      // 오류: 'int'는 예약어라 변수 이름이 될 수 없음
int return = 1;   // 오류: 'return'도 마찬가지
int count = 3;    // OK: 'count'는 예약어가 아니므로 식별자로 사용 가능
```

따라서 "예약어를 식별자로 사용할 수 있다"는 서술은 틀렸습니다.

$$\boxed{\text{X}}$$
:::
