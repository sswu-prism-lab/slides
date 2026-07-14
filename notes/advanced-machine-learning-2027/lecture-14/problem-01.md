# 문제 1 · 확률적 그래프 모델 그리기 (LDA)

::: info 문제 1 — 확률적 그래프 모델 그리기
아래와 같은 생성 모델 식을 토대로 이에 대응하는 그래프 모델을 그리시오. $w_{dn}$은 관측값이다.

$$
\begin{aligned}
&\alpha,\ \beta,\\
&\theta_d\mid\alpha\sim\mathrm{Dir}(\alpha),\quad d=1,\ldots,D,\\
&\phi_k\mid\beta\sim\mathrm{Dir}(\beta),\quad k=1,\ldots,K,\\
&z_{dn}\mid\theta_d\sim\mathrm{Mult}(\theta_d),\quad n=1,\ldots,N_d,\\
&w_{dn}\mid z_{dn},\boldsymbol{\phi}\sim\mathrm{Mult}(\phi_{z_{dn}})
\end{aligned}
$$

---

확률적 그래프 모델을 그리는 과정에서는 각 확률 분포가 어떤 모양을 따르는지는 크게 상관하지 않는다. 위 생성 모델은 잠재 디리클레 할당<span class="gloss">latent Dirichlet allocation; LDA</span> 모델이다.
:::

::: details 풀이 및 해설
생성 순서 $\alpha\to\theta_d\to z_{dn}\to w_{dn}\leftarrow\phi_k\leftarrow\beta$를 따라 방향 그래프를 그리고, **판(plate)** 으로 반복 구조를 표현한다. 관측 변수 $w_{dn}$만 **음영(shaded)** 처리한다.

<svg viewBox="0 0 640 340" width="100%" style="max-width:640px; background:transparent; font-family:serif;">
  <defs>
    <marker id="ah" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#4a7294"/>
    </marker>
  </defs>
  <!-- plates -->
  <rect x="118" y="46" width="416" height="150" rx="8" fill="none" stroke="#9aa0a6"/>
  <text x="524" y="188" font-size="15" fill="#6b7280">D</text>
  <rect x="252" y="72" width="282" height="98" rx="8" fill="none" stroke="#9aa0a6"/>
  <text x="524" y="162" font-size="15" fill="#6b7280">N_d</text>
  <rect x="382" y="236" width="120" height="78" rx="8" fill="none" stroke="#9aa0a6"/>
  <text x="492" y="306" font-size="15" fill="#6b7280">K</text>
  <!-- edges -->
  <line x1="78" y1="121" x2="150" y2="121" stroke="#4a7294" marker-end="url(#ah)"/>
  <line x1="200" y1="121" x2="275" y2="121" stroke="#4a7294" marker-end="url(#ah)"/>
  <line x1="325" y1="121" x2="418" y2="121" stroke="#4a7294" marker-end="url(#ah)"/>
  <line x1="558" y1="275" x2="466" y2="275" stroke="#4a7294" marker-end="url(#ah)"/>
  <line x1="443" y1="253" x2="443" y2="145" stroke="#4a7294" marker-end="url(#ah)"/>
  <!-- nodes -->
  <circle cx="55" cy="121" r="22" fill="#eef2f6" stroke="#4a7294"/><text x="55" y="127" font-size="16" text-anchor="middle">α</text>
  <circle cx="176" cy="121" r="22" fill="#eef2f6" stroke="#4a7294"/><text x="176" y="127" font-size="14" text-anchor="middle">θ_d</text>
  <circle cx="300" cy="121" r="22" fill="#eef2f6" stroke="#4a7294"/><text x="300" y="127" font-size="13" text-anchor="middle">z_dn</text>
  <circle cx="443" cy="121" r="22" fill="#4a7294" stroke="#33536b"/><text x="443" y="127" font-size="12" text-anchor="middle" fill="#fff">w_dn</text>
  <circle cx="443" cy="275" r="22" fill="#eef2f6" stroke="#4a7294"/><text x="443" y="281" font-size="14" text-anchor="middle">φ_k</text>
  <circle cx="580" cy="275" r="22" fill="#eef2f6" stroke="#4a7294"/><text x="580" y="281" font-size="16" text-anchor="middle">β</text>
</svg>

**구성 요소 정리**

- **노드(확률 변수)**: 하이퍼파라미터 $\alpha,\beta$, 문서별 주제 분포 $\theta_d$, 주제별 단어 분포 $\phi_k$, 잠재 주제 배정 $z_{dn}$, 관측 단어 $w_{dn}$.
- **간선(의존성)**: $\alpha\to\theta_d$, $\theta_d\to z_{dn}$, $z_{dn}\to w_{dn}$, $\beta\to\phi_k$, $\phi_k\to w_{dn}$.
- **판(plate)**:
  - $D$ 판 — $\theta_d$와 그 안의 단어들을 감싼다(문서 반복).
  - $N_d$ 판 — $z_{dn}, w_{dn}$을 감싼다(문서 $d$ 안의 단어 반복). $D$ 판 내부에 중첩된다.
  - $K$ 판 — $\phi_k$를 감싼다(주제 반복).
- **음영**: 관측 변수 $w_{dn}$만 채워서 표시한다. $\alpha,\beta$는 상수(하이퍼파라미터)이므로 판 밖에 둔다.
:::
