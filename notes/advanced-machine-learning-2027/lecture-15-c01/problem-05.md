# 문제 5 · 확률적 그래프 모델 그리기 (생성형 분류기)

::: info 문제 5 [4점]
$N$개의 관측된 데이터-레이블 쌍 $(\mathbf{x}_n,y_n)$에 대해, 아래의 간단한 생성형 분류기의 확률적 그래프 모델<span class="gloss">probabilistic graphical model</span>을 그리시오. $\pi$는 레이블 분포의 비율에 대한 가설이며, 데이터 벡터 $\mathbf{x}_n$은 $D$차원이다($\mathbf{x}_n=[x_{n1},\ldots,x_{nD}]$). 분류기 매개변수 $\boldsymbol{\theta}$는 각 특징 차원마다 클래스 수 $C$만큼 존재한다($\boldsymbol{\theta}_d=[\theta_{d1},\ldots,\theta_{dC}]$). 각 노드는 스칼라값이 되도록 그리시오.

$$
p(\mathbf{x},y\mid\boldsymbol{\theta})=p(y\mid\pi)\prod_{d=1}^{D}p(x_{d}\mid y,\boldsymbol{\theta}_d)
$$
:::

::: details 풀이 및 해설
이는 **나이브 베이즈 생성형 분류기**의 그래프 모델이다. $\pi\to y_n\to x_{nd}$이고 $\theta_d\to x_{nd}$이다. 관측 변수 $x_{nd}$만 음영으로 표시하고, 반복 구조는 판으로 나타낸다.

<svg viewBox="0 0 470 300" width="100%" style="max-width:470px; font-family:serif;">
  <defs>
    <marker id="ah2" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#4a7294"/>
    </marker>
  </defs>
  <!-- N plate -->
  <rect x="118" y="30" width="150" height="238" rx="8" fill="none" stroke="#9aa0a6"/>
  <text x="250" y="258" font-size="15" fill="#6b7280">N</text>
  <!-- D plate (overlaps N on the right; both index x_nd) -->
  <rect x="150" y="150" width="250" height="86" rx="8" fill="none" stroke="#9aa0a6" stroke-dasharray="4 3"/>
  <text x="384" y="228" font-size="15" fill="#6b7280">D</text>
  <!-- edges -->
  <line x1="78" y1="70" x2="162" y2="70" stroke="#4a7294" marker-end="url(#ah2)"/>
  <line x1="190" y1="92" x2="190" y2="168" stroke="#4a7294" marker-end="url(#ah2)"/>
  <line x1="322" y1="190" x2="216" y2="190" stroke="#4a7294" marker-end="url(#ah2)"/>
  <!-- nodes -->
  <circle cx="55" cy="70" r="22" fill="#eef2f6" stroke="#4a7294"/><text x="55" y="76" font-size="16" text-anchor="middle">π</text>
  <circle cx="190" cy="70" r="22" fill="#eef2f6" stroke="#4a7294"/><text x="190" y="76" font-size="14" text-anchor="middle">y_n</text>
  <circle cx="190" cy="190" r="24" fill="#4a7294" stroke="#33536b"/><text x="190" y="195" font-size="11" text-anchor="middle" fill="#fff">x_nd</text>
  <circle cx="344" cy="190" r="22" fill="#eef2f6" stroke="#4a7294"/><text x="344" y="195" font-size="13" text-anchor="middle">θ_d</text>
</svg>

**구성 요소 정리**

- **노드**: 레이블 비율 가설 $\pi$, 레이블 $y_n$, 관측 특징 $x_{nd}$(음영), 특징별 매개변수 $\theta_d$. (각 노드는 스칼라.)
- **간선**: $\pi\to y_n$, $y_n\to x_{nd}$, $\theta_d\to x_{nd}$.
- **판(plate)**:
  - $N$ 판 — $y_n$과 $x_{nd}$를 감싼다(데이터 반복).
  - $D$ 판 — $x_{nd}$와 $\theta_d$를 감싼다(특징 차원 반복). $\theta_d$는 모든 $n$에 공유되므로 $N$ 판 **밖**에 있어야 하고, $x_{nd}$는 두 인덱스를 모두 가지므로 두 판이 겹치도록 그린다.
- **음영**: 관측 변수 $x_{nd}$만 채운다. $\pi$는 판 밖의 전역 매개변수다.
:::
