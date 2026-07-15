# 문제 12 · 분류 성능 지표

::: info 문제 12 [3점]
어떤 데이터셋의 정답 레이블<span class="gloss">label</span>이 $[1,0,0,1,1,1,0,1,1,1]$이고, 어떤 기계학습 모델이 예측한 레이블이 $[0,1,1,1,1,0,1,0,1,0]$이라 하자. 이 모델의 재현율<span class="gloss">recall</span>, 정밀도<span class="gloss">precision</span>, F1 점수<span class="gloss">F1 score</span>(각 1점)를 구하시오. (레이블 $1$이 "양성"을 의미한다.)
:::

::: details 풀이 및 해설
각 표본을 정답/예측 조합으로 분류합니다($1$=양성).

| # | 정답 | 예측 | 판정 |
|---|---|---|---|
| 1 | 1 | 0 | FN |
| 2 | 0 | 1 | FP |
| 3 | 0 | 1 | FP |
| 4 | 1 | 1 | TP |
| 5 | 1 | 1 | TP |
| 6 | 1 | 0 | FN |
| 7 | 0 | 1 | FP |
| 8 | 1 | 0 | FN |
| 9 | 1 | 1 | TP |
| 10 | 1 | 0 | FN |

따라서 $\text{TP}=3,\ \text{FP}=3,\ \text{FN}=4$입니다.

$$
\text{recall} = \frac{\text{TP}}{\text{TP}+\text{FN}} = \frac{3}{3+4} = \frac{3}{7}\approx 0.4286.
$$

$$
\text{precision} = \frac{\text{TP}}{\text{TP}+\text{FP}} = \frac{3}{3+3} = \frac{1}{2} = 0.5.
$$

$$
\text{F1} = \frac{2\cdot\text{TP}}{2\cdot\text{TP}+\text{FP}+\text{FN}} = \frac{6}{6+3+4} = \frac{6}{13}\approx 0.4615.
$$

$$
\boxed{\;\text{recall}=\tfrac{3}{7},\quad \text{precision}=\tfrac{1}{2},\quad \text{F1}=\tfrac{6}{13}\approx 0.4615\;}
$$

👉 [실습(Python)에서 확인하기](./lab-12)
:::
