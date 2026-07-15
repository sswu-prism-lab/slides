# 수와 연산 · 집합 · 복소수

2주차에서 다룬 수 체계의 기초를 정리한다. 진법과 지수·로그, 합·곱 연산자, 집합론의 기본 연산, 수열과 급수, 그리고 복소수를 순서대로 살펴본다.

## 진법

- $n$진법<span class="gloss">base $n$</span>은 수를 셀 때 자릿수가 올라가는 단위의 기준을 $n$으로 하는 셈법이다. 우리가 흔히 쓰는 것은 $10$진법이고, 컴퓨터 과학에서는 주로 $2$진법을 쓴다.
- 임의의 자연수 $a$와 $n\geq 2$에 대해 다음과 같이 표현할 수 있으며, 이 표현은 존재성<span class="gloss">existence</span>과 유일성<span class="gloss">uniqueness</span>을 가진다.

$$
a = a_k n^k + a_{k-1}n^{k-1}+\cdots+a_1 n+a_0,\qquad 0\leq a_0, a_1,\cdots, a_k<n,\ a_k\neq 0
$$

- 이를 $a=\overline{a_k a_{k-1}\cdots a_1 a_0}_{(n)}$로 표기하며, $10$진법은 아래첨자를 생략한다.
- **진법 변환**은 변환하려는 수를 목표 진법 수로 나누어 가며 생기는 나머지를 역순으로 나열해 수행한다. 예를 들어 $10$진수 $345$를 $7$진법으로 바꾸는 과정은 다음과 같다.

$$
\begin{aligned}
345 \div 7 &= 49 \ \cdots\ 2 \\
49 \div 7 &= 7 \ \cdots\ 0 \\
7 \div 7 &= 1 \ \cdots\ 0 \\
1 \div 7 &= 0 \ \cdots\ 1
\end{aligned}
\qquad\Longrightarrow\qquad 345_{(10)} = 1002_{(7)}
$$

- 유리수·무리수·복소수 진법도 정의할 수 있다.

<PyRunner>

```python
def to_base(a, n):
    if a == 0:
        return "0"
    digits = []
    while a > 0:
        digits.append(a % n)   # 나머지를 모으고
        a //= n
    return "".join(str(d) for d in reversed(digits))  # 역순으로 나열

for a, n in [(345, 7), (13, 2), (100, 5)]:
    print(f"{a}(10) = {to_base(a, n)}({n})")

# 역변환으로 검증: 7진수 1002 -> 10진수
s = "1002"
val = sum(int(d) * 7**i for i, d in enumerate(reversed(s)))
print("1002(7) =", val, "(10)")
```

</PyRunner>

## 지수와 로그

- 임의의 수 $A$를 $N$번 거듭해 곱한 것을 $A^N$으로 표기한다. 지수<span class="gloss">exponent</span>는 다음 성질을 가진다.

$$
X^A X^B = X^{A+B},\qquad \frac{X^A}{X^B} = X^{A-B},\qquad (X^A)^B=X^{AB}
$$

$$
X^N+X^N = 2X^N\neq X^{2N},\qquad 2^N + 2^N = 2^{N+1}
$$

- 로그<span class="gloss">log</span>는 지수의 역연산으로 다음과 같이 정의된다.

$$
X^A=B\ \Leftrightarrow\ \log_X B=A
$$

  - 컴퓨터 과학에서는 밑을 $2$로, 자연과학·공학에서는 $e\approx 2.718$(자연로그 $\ln$)을, 경제학·일상에서는 $10$(상용로그)을 약속한다.
- 정의로부터 다음 성질이 유도된다.

$$
\log_A B = \frac{\log_C B}{\log_C A}\ (A,B,C>0,\ A\neq 1),\qquad \log AB = \log A +\log B,\qquad \log \frac{A}{B} = \log A - \log B
$$

$$
\log (A^B) = B\log A,\qquad \log X < X\ (\forall X>0),\qquad \log 1 = 0,\ \log 2 = 1,\ \log 1024 = 10\ (\text{밑 } 2)
$$

## 합 연산과 곱 연산

- 합 연산자 $\sum$와 곱 연산자 $\prod$는 다음과 같이 정의된다.

$$
\sum_{k=i}^{j}a_k = a_i + a_{i+1} + \cdots + a_j,\qquad \prod_{k=i}^{j}a_k = a_i a_{i+1}\cdots a_j
$$

- 두 연산자는 각각 다음 성질을 가진다.

$$
\sum_{k=1}^{n}(a_k\pm b_k)=\sum_{k=1}^{n}a_k \pm \sum_{k=1}^{n}b_k,\qquad \sum_{k=1}^{n}c\, a_k = c\sum_{k=1}^{n}a_k,\qquad \sum_{k=1}^{n}c = cn
$$

$$
\prod_{k=1}^{n}(a_k b_k) = \left(\prod_{k=1}^{n}a_k\right)\left(\prod_{k=1}^{n}b_k\right),\qquad \left(\prod_{k=1}^{n}a_k\right)^m=\prod_{k=1}^{n}a_k^m,\qquad \prod_{k=1}^{n}c=c^n
$$

<PyRunner>

```python
import numpy as np

# 로그 밑 변환 공식으로 log_2 B 계산: log_2 B = ln B / ln 2
for B in [1, 2, 1024]:
    print(f"log2({B}) = {np.log(B)/np.log(2):.4f}")

# 합 연산자로 라이프니츠 급수를 계산해 pi/4 근사
n = np.arange(0, 100000)
s = np.sum((-1.0)**n / (2*n + 1))     # 1 - 1/3 + 1/5 - 1/7 + ...
print(f"\n4 x (부분합) = {4*s:.6f},  np.pi = {np.pi:.6f}")
```

</PyRunner>

## 집합

- 집합<span class="gloss">set</span> $A$에 원소<span class="gloss">element</span> $a$가 속하면 $a\in A$, 아니면 $a\notin A$로 쓴다. 모임<span class="gloss">collection</span>·족<span class="gloss">family</span>은 집합의 동의어이다.
- $\{x:\cdots\}$는 조건 $\cdots$을 만족하는 모든 $x$의 집합이며, 원소가 없는 집합을 공집합<span class="gloss">empty set</span> $\emptyset$이라 한다.
- $A$의 모든 원소가 $B$의 원소이면 $A$를 $B$의 부분집합<span class="gloss">subset</span>이라 하고 $A\subset B$로 표기한다.

$$
A\subset B \ \Leftrightarrow\ (x\in A \Rightarrow x \in B,\ \forall x)
$$

- $A$의 모든 부분집합을 모은 집합을 멱집합<span class="gloss">power set</span> $\mathcal{P}(A)$라 한다. 원소가 $m$개이면 $|\mathcal{P}(A)|=2^m$이다.

$$
A=\{0, 1, 2\}\ \Rightarrow\ \mathcal{P}(A)=\{\emptyset, \{0\}, \{1\}, \{2\}, \{0, 1\}, \{0, 2\}, \{1, 2\}, \{0, 1, 2\} \}
$$

- 합집합<span class="gloss">union</span>·교집합<span class="gloss">intersection</span>·차집합<span class="gloss">set difference</span>은 다음과 같다.

$$
A\cup B=\{x: x\in A\vee x\in B\},\qquad A\cap B=\{x: x\in A\wedge x\in B\},\qquad B\setminus A=\{x: x\in B\wedge x\notin A\}
$$

- $A\cap B=\emptyset$이면 두 집합은 서로소<span class="gloss">disjoint set</span>이며, $A\subset X$일 때 $X\setminus A$를 $A$의 여집합<span class="gloss">complement</span>이라 한다.

::: info 분배 법칙과 드 모르간의 법칙
분배 법칙<span class="gloss">distributive law</span>:

$$
A\cup(B\cap C)=(A\cup B)\cap (A\cup C),\qquad A\cap (B\cup C)=(A\cap B)\cup (A\cap C)
$$

드 모르간의 법칙<span class="gloss">De Morgan's laws</span> ($A,B\subset X$):

$$
X\setminus (A\cup B)=(X\setminus A)\cap (X\setminus B),\qquad X\setminus (A\cap B)=(X\setminus A)\cup (X\setminus B)
$$
:::

- 색인 집합<span class="gloss">index set</span> $I$에 대해 색인<span class="gloss">indexed</span>된 모임 $\{A_i:i\in I\}$의 합집합·교집합은 다음과 같이 일반화된다.

$$
\bigcup_{i\in I}A_i=\{x:\exists i\in I \text{ s.t. } x\in A_i\},\qquad \bigcap_{i\in I}A_i=\{x:\forall i\in I,\ x\in A_i\}
$$

- **수 체계**는 자연수<span class="gloss">natural number</span> $\mathbb{N}$(페아노 공리계<span class="gloss">Peano's axioms</span>로 정의)에서 시작해 확장된다.

$$
\mathbb{N}_0=\mathbb{N}\cup\{0\},\quad \mathbb{Z}=\{x:n\pm x=0,\ \forall n\in\mathbb{N}_0\},\quad \mathbb{Q}=\left\{x:x=\tfrac{m}{n},\ m,n\in\mathbb{Z},\ n\neq 0\right\}
$$

  - 무리수<span class="gloss">irrational number</span> $\mathbb{I}$는 정수비로 나타낼 수 없는 수이고, 실수<span class="gloss">real number</span> $\mathbb{R}=\mathbb{Q}\cup\mathbb{I}$이며, 허수단위 $i\equiv\sqrt{-1}$에 대해 복소수<span class="gloss">complex number</span> $\mathbb{C}=\{a+bi:a,b\in\mathbb{R}\}$이다.
- 볼록 집합<span class="gloss">convex set</span> $A$는 $tx+(1-t)y\in A\ (\forall x,y\in A,\ t\in[0,1])$을 만족하는 집합으로, 두 점을 잇는 선분이 항상 집합에 포함된다. 최적화·기계학습<span class="gloss">machine learning</span>에서 서포트 벡터 머신<span class="gloss">support vector machine</span>의 결정 경계 문제 등 볼록 최적화의 기반이 된다.

<PyRunner>

```python
from itertools import combinations

A = {0, 1, 2}
B = {1, 2, 3}
print("A ∪ B =", A | B)
print("A ∩ B =", A & B)
print("B \\ A =", B - A)

# 멱집합 구성
elems = sorted(A)
power = [set(c) for r in range(len(elems)+1) for c in combinations(elems, r)]
print(f"\n|P(A)| = {len(power)} (= 2^{len(elems)})")
print("P(A) =", [sorted(s) for s in power])
```

</PyRunner>

## 수열과 급수

- 수열<span class="gloss">sequence</span>은 자연수 집합을 정의역으로 하는 함수로 $\{x_n\}_{n=1}^{\infty}$처럼 표기한다. 대표적인 수열은 다음과 같다.

$$
\text{등차수열}\ a_n=a+(n-1)d,\qquad \text{등비수열}\ a_n=ar^{n-1},\qquad \text{조화수열}\ a_n=\frac{a}{1+a(n-1)d}
$$

- 피보나치 수열<span class="gloss">Fibonacci sequence</span>은 점화식과 일반항으로 다음과 같이 주어진다.

$$
F_1=1,\ F_2=1,\ F_{n+2}=F_{n+1} + F_n,\qquad F_n = \frac{1}{\sqrt{5}}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right]
$$

::: info Thm. 피보나치 수열의 이웃한 두 항은 항상 서로소이다
$\gcd(a,a+b)=\gcd(a,b)$이므로

$$
\gcd(F_{k+1}, F_{k+2})=\gcd(F_{k+1}, F_{k+1}+F_k)=\gcd(F_{k+1}, F_{k})
$$

$n=1$에서 $\gcd(F_1,F_2)=1$이고, $\gcd(F_k,F_{k+1})=1$을 가정하면 위 식에 의해 $\gcd(F_{k+1},F_{k+2})=1$. 따라서 수학적 귀납법으로 $\gcd(F_n,F_{n+1})=1,\ \forall n\in\mathbb{N}$. $\blacksquare$
:::

- 수열 $\{a_n\}$의 부분합 $S_n=\sum_{k=1}^n a_k$의 극한<span class="gloss">limit</span>을 급수<span class="gloss">series</span>라 한다.

$$
\lim_{n\rightarrow\infty}S_n=\lim_{n\rightarrow\infty}\sum_{k=1}^{n}a_k
$$

  - 극한값이 실수로 수렴<span class="gloss">converge</span>하면 급수가 수렴한다고 하고, 그렇지 않으면 발산<span class="gloss">diverge</span>한다고 한다. 급수는 "부분합의 극한"이지 "무한 번 더하는 것"이 아니며, 리만 재배열 정리<span class="gloss">Riemann rearrangement theorem</span>가 그 차이를 보여준다.
- **테일러 급수**<span class="gloss">Taylor series</span>는 함수 $f(x)$를 점 $a$ 주변에서 다항식의 합으로 전개한다. $a=0$인 경우를 매클로린 급수<span class="gloss">Maclaurin series</span>라 한다.

$$
f(x)\approx f(a) + f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^2+\frac{f'''(a)}{3!}(x-a)^3+\cdots
$$

- 전개 차수가 높을수록 원래 함수에 가까워진다. 예를 들어 $\sin x$의 매클로린 전개는 다음과 같다.

$$
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}
$$

## 복소수

- 복소수 $z=a+bi\ (a,b\in\mathbb{R},\ i\equiv\sqrt{-1})$에서 $\Re(z)=a$를 실수부, $\Im(z)=b$를 허수부라 한다. 켤레복소수<span class="gloss">complex conjugate</span>와 절댓값<span class="gloss">absolute value</span>은 다음과 같다.

$$
\bar{z}\equiv\Re(z)-i\,\Im(z)=a-bi,\qquad |z|\equiv\sqrt{z\bar{z}}=\sqrt{a^2+b^2}
$$

- 복소수의 덧셈과 곱셈은 다음과 같이 정의되며, 둘 다 결합법칙<span class="gloss">associative property</span>·교환법칙<span class="gloss">commutative property</span>을 만족하고 항등원·역원이 존재한다(곱셈의 역원 $z^{-1}=\bar{z}/|z|^2$).

$$
(a+bi)+(c+di)=(a+c)+(b+d)i,\qquad (a+bi)(c+di)=(ac-bd)+(ad+bc)i
$$

- 복소수는 행렬 표현<span class="gloss">matrix representation</span>으로도 나타낼 수 있다. 특히 단위허수 $i$의 행렬 표현은 회전 행렬<span class="gloss">rotation matrix</span>과 같다.

$$
z = a+bi \ \longleftrightarrow\ \begin{pmatrix} a & -b \\ b & a \end{pmatrix},\qquad i \ \longleftrightarrow\ \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}=\begin{pmatrix} \cos\frac{\pi}{2} & -\sin\frac{\pi}{2} \\ \sin\frac{\pi}{2} & \cos\frac{\pi}{2} \end{pmatrix}
$$

  - 이를 일반화하면 $i^n$은 각도 $\frac{n\pi}{2}$의 회전에 대응하며, $i^0=1,\ i^1=i,\ i^2=-1,\ i^3=-i,\ i^4=1$로 주기 $4$를 갖는다.
- 극형식<span class="gloss">polar form</span>은 편각 $\theta$를 이용해 $z=|z|(\cos\theta+i\sin\theta)$로 쓴다. 제1사분면에서는 $\theta=\arctan(b/a)$이며(일반적으로는 $\arctan2$를 사용), 여기서 오일러 공식<span class="gloss">Euler's formula</span>을 얻는다.

$$
e^{ix}\equiv \cos x + i \sin x,\qquad \text{(cf. }e^{i\pi}+1=0\text{)}
$$

<PyRunner>

```python
import numpy as np
from math import gcd

# 피보나치 수열과 이웃 항의 서로소성
F = [1, 1]
for _ in range(10):
    F.append(F[-1] + F[-2])
print("피보나치 F =", F)
print("이웃 항 gcd =", [gcd(F[i], F[i+1]) for i in range(len(F)-1)])

# 복소수 i^n 의 주기성과 오일러 공식
print("\ni^n 의 주기성:")
for n in range(5):
    print(f"  i^{n} = {np.round(1j**n, 2)}")
print("오일러 공식 e^(iπ)+1 =", np.round(np.exp(1j*np.pi) + 1, 4))
```

</PyRunner>
