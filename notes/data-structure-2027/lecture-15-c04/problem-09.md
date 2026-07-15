# 문제 9 · 트리 기반 서로소 집합의 문제점과 개선

::: info 문제 9 [4점]
아래 배열<span class="gloss">array</span>은 트리 기반 서로소 집합<span class="gloss">disjoint set</span>을 구현한 결과이다. 이를 트리 형태로 그리고(2점), 이 서로소 집합이 가지는 문제점과 개선 방안을 서술(2점)하시오.

<figure class="fig">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/ds/ds-w15c04-02.svg" alt="서로소 집합을 나타내는 배열" style="max-width: 520px;" />
  <figcaption class="cap">인덱스 0~7의 부모 배열(값 −1은 루트를 뜻함)</figcaption>
</figure>
:::

::: details 풀이 및 해설

**배열 읽기**

배열의 각 칸은 그 노드의 **부모 인덱스**이고, 값 $-1$ 은 루트를 뜻한다.

| 인덱스 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 부모 | −1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 |

7은 6을, 6은 5를, …, 1은 0을 부모로 가리키므로 하나의 긴 **사슬(chain)** 이다.

**트리 형태**

```text
0  (루트)
│
1
│
2
│
3
│
4
│
5
│
6
│
7
```

**문제점**

union을 아무 순서로나(항상 한쪽을 다른 쪽 밑에 붙이는 식으로) 수행하면, 이렇게 **한 줄로 늘어진 편향 트리**가 만들어진다. 이때 트리의 높이가 $\mathcal{O}(N)$ 이 되어, 어떤 원소의 대표원을 찾는 `find` 연산이 루트까지 $\mathcal{O}(N)$ 만큼 거슬러 올라가야 한다. 사실상 연결 리스트와 다를 바 없어, 트리로 구현한 이점이 사라진다.

$$\boxed{\text{편향 트리} \Rightarrow \text{높이 } \mathcal{O}(N),\ \text{find}=\mathcal{O}(N)}$$

**개선 방안**

1. **랭크(또는 크기)에 의한 합집합<span class="gloss">union by rank/size</span>**: union할 때 **낮은(작은) 트리를 높은(큰) 트리 밑에 붙인다.** 이렇게 하면 트리 높이가 $\mathcal{O}(\log N)$ 이하로 유지된다.
2. **경로 압축<span class="gloss">path compression</span>**: `find` 도중 거쳐 간 모든 노드를 **곧바로 루트에 직접 연결**한다. 이후의 `find` 가 훨씬 짧아진다.

두 기법을 함께 쓰면 $m$번 연산의 총 비용이 $\mathcal{O}(m\,\alpha(N))$ 으로, $\alpha$ 는 극도로 느리게 자라는 역-아커만 함수라 사실상 **연산당 상수 시간**에 가깝다.

$$\boxed{\text{랭크에 의한 합집합 + 경로 압축} \Rightarrow \text{연산당 사실상 }\mathcal{O}(\alpha(N))\approx\mathcal{O}(1)}$$
:::
