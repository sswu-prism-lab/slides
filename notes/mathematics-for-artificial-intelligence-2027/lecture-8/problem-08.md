# 문제 8 · 가설검정

::: info 문제 8 [2점]
우리가 새롭게 개발한 안테나가 기존의 안테나보다 더 수신율이 좋은지 여부를 가설 검정하고자 한다. 이때 귀무가설과 대안가설을 서술(1점)하고, 양꼬리·한꼬리 검정 중 어느 것을 선택해야 하는지 이유와 함께 서술(1점)하시오.
:::

::: details 풀이 및 해설
새 안테나의 수신율을 $\mu_{\text{new}}$, 기존 안테나의 수신율을 $\mu_{\text{old}}$라 하자.

**귀무가설<span class="gloss">null hypothesis</span>** $H_0$: 새 안테나가 더 좋지 않다(차이가 없다).

$$
H_0:\ \mu_{\text{new}} = \mu_{\text{old}} \quad(\text{또는 } \mu_{\text{new}}\le \mu_{\text{old}}).
$$

**대안가설<span class="gloss">alternative hypothesis</span>** $H_1$: 새 안테나가 더 좋다.

$$
H_1:\ \mu_{\text{new}} > \mu_{\text{old}}.
$$

**검정 방향**: 우리가 확인하려는 것은 "더 좋은지"라는 **한쪽 방향**의 주장뿐입니다. 단순히 "다른지"가 아니라 "$\mu_{\text{new}}>\mu_{\text{old}}$인지"만 관심 대상이므로, 기각역을 분포의 오른쪽 한쪽에만 두는 **한꼬리(단측) 검정**<span class="gloss">one-tailed test</span>을 선택해야 합니다.

$$
\boxed{\;H_0:\mu_{\text{new}}=\mu_{\text{old}},\quad H_1:\mu_{\text{new}}>\mu_{\text{old}},\quad \text{한꼬리(단측) 검정}\;}
$$

방향성이 있는 대안가설이므로 같은 유의수준에서 단측 검정이 양측 검정보다 검정력이 높아, 개선 효과를 더 민감하게 탐지할 수 있습니다.
:::
