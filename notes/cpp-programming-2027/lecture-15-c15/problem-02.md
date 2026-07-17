# 문제 2 · 멤버 선택 연산자 (O/X)

::: info 문제 2 [1점]
아래 문장을 읽고 O/X로 답하세요.

> C++ 포인터<span class="gloss">pointer</span>로부터 객체 멤버에 접근하기 위한 속기 멤버 선택 연산자<span class="gloss">shorthand member selection operator</span>는 `=>`로 쓴다. (아래는 예시)

```cpp
string* pString = &myString;
pString => substr(0, 3);
```
:::

::: details 풀이 및 해설
**정답: X**

포인터를 통해 객체의 멤버에 접근하는 속기 연산자는 `=>`가 아니라 **화살표 연산자 `->`** 입니다. `=>`는 C++에 존재하지 않는 표기입니다.

`pPtr->member`는 `(*pPtr).member`의 축약형으로, 포인터를 역참조한 뒤 멤버를 선택하는 것과 같습니다. 예시 코드는 다음처럼 고쳐야 합니다.

```cpp
string* pString = &myString;
pString->substr(0, 3);       // (*pString).substr(0, 3) 와 동일
```

따라서 문장은 거짓입니다.

$$\boxed{\text{X} \;(\;\texttt{=>} \rightarrow \texttt{->}\;)}$$
:::
