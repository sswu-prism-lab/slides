# 문제 8 · 동치 관계의 세 가지 성질

::: info 문제 8 [2점]
동치 관계<span class="gloss">equivalence relation</span>가 가지는 3가지 성질을 서술(1점)하고, 예시를 서술(1점)하시오.
:::

::: details 풀이 및 해설

**세 가지 성질**

집합 $S$ 위의 관계 $\sim$ 가 다음 세 성질을 모두 만족하면 **동치 관계**라 한다.

1. **반사성<span class="gloss">reflexive</span>**: 모든 $a\in S$ 에 대해 $a \sim a$.
2. **대칭성<span class="gloss">symmetric</span>**: $a \sim b$ 이면 $b \sim a$.
3. **추이성<span class="gloss">transitive</span>**: $a \sim b$ 이고 $b \sim c$ 이면 $a \sim c$.

$$\boxed{\text{동치 관계} \iff \text{반사성} \;\wedge\; \text{대칭성} \;\wedge\; \text{추이성}}$$

**예시**

- **상등(등호) 관계** $a = b$: 자기 자신과 같고($a=a$), 대칭이며($a=b\Rightarrow b=a$), 추이적($a=b,\,b=c\Rightarrow a=c$)이다.
- **법 $n$ 합동** $a \equiv b \pmod{n}$ ($a-b$ 가 $n$의 배수): 예컨대 $n=3$ 이면 $\{\dots,-3,0,3,6,\dots\}$, $\{\dots,1,4,7,\dots\}$, $\{\dots,2,5,8,\dots\}$ 세 개의 동치 클래스로 정수 전체를 분할한다.
- 그 밖에 "같은 학과에 속함", "같은 나머지를 가짐" 등도 세 성질을 만족하는 동치 관계다.

동치 관계는 항상 집합을 **서로소인 동치 클래스들로 분할(partition)** 한다는 점이 핵심이다.
:::
