# 문제 3 · 상수 함수를 정의할 수 있는 대상

::: info 문제 3 [1점]
아래 문제를 읽고 O/X로 답하세요.

오직 인스턴스 멤버 함수<span class="gloss">instance member function</span>만이 상수 함수<span class="gloss">const function</span>로 정의될 수 있다.
:::

::: details 풀이 및 해설
**답: `O`**

상수 함수는 함수 선언 뒤에 `const`를 붙인 멤버 함수로, 자신의 객체(`this`가 가리키는 대상)의 멤버를 수정하지 않겠다는 약속입니다.

- **정적 멤버 함수<span class="gloss">static member function</span>**: 특정 객체에 속하지 않아 `this` 포인터가 없으므로 `const`를 붙일 수 없습니다.
- **전역 함수(자유 함수)**: 애초에 객체의 멤버가 아니므로 `const` 상수 함수가 될 수 없습니다.

따라서 `const`를 붙여 상수 함수로 만들 수 있는 것은 **인스턴스(비정적) 멤버 함수뿐**입니다.

$$\boxed{\text{O (참)}}$$
:::
