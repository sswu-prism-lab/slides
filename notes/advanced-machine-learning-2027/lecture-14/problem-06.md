# 문제 6 · 단일 가우시안 변분 추론

::: info 문제 6 — 단일 가우시안 변분 추론
관측치 $x\in\mathbb{R}$이 다음과 같이 생성된다고 가정하자.

$$
p(x\mid\mu)=\mathcal{N}(x\mid\mu,\sigma^2),\ \sigma^2=1,\qquad p(\mu)=\mathcal{N}(\mu\mid\mu_0,\tau_0^2)
$$

이를 변분 분포 $q(\mu)=\mathcal{N}(\mu\mid m,s^2)$로 근사하고자 한다. 이 때 $m$과 $s^2$를 구하시오.

---

ELBO 식은 아래와 같이 정의된다.

$$
\mathcal{L}(m,s^2)=\mathbb{E}_q[\ln p(x\mid\mu)]+\mathbb{E}_q[\ln p(\mu)]-\mathbb{E}_q[\ln q(\mu)]
$$
:::

::: details 풀이 및 해설
가우시안 하에서 각 항의 기댓값을 계산한다($\mathbb{E}_q[\mu]=m$, $\mathbb{E}_q[(\mu-c)^2]=(m-c)^2+s^2$).

$$
\mathbb{E}_q[\ln p(x\mid\mu)]=-\tfrac12\ln(2\pi\sigma^2)-\frac{(x-m)^2+s^2}{2\sigma^2}
$$

$$
\mathbb{E}_q[\ln p(\mu)]=-\tfrac12\ln(2\pi\tau_0^2)-\frac{(m-\mu_0)^2+s^2}{2\tau_0^2}
$$

$$
-\mathbb{E}_q[\ln q(\mu)]=\tfrac12\ln(2\pi s^2)+\tfrac12\quad(\text{엔트로피})
$$

**$m$에 대한 미분** — $\sigma^2=1$을 대입하고 $\partial\mathcal{L}/\partial m=0$:

$$
(x-m)+\frac{\mu_0-m}{\tau_0^2}=0\ \Longrightarrow\ m\left(1+\frac{1}{\tau_0^2}\right)=x+\frac{\mu_0}{\tau_0^2}
$$

$$
\boxed{\ m=\frac{\tau_0^2\,x+\mu_0}{\tau_0^2+1}\ }
$$

**$s^2$에 대한 미분** — $\partial\mathcal{L}/\partial s^2=0$:

$$
-\frac{1}{2\sigma^2}-\frac{1}{2\tau_0^2}+\frac{1}{2s^2}=0\ \Longrightarrow\ \frac{1}{s^2}=1+\frac{1}{\tau_0^2}
$$

$$
\boxed{\ s^2=\frac{1}{1+\tfrac{1}{\tau_0^2}}=\frac{\tau_0^2}{\tau_0^2+1}\ }
$$

**의미** — 정밀도(분산의 역수)가 사전 정밀도 $1/\tau_0^2$와 우도 정밀도 $1/\sigma^2=1$의 합이 되고, 평균은 두 정보의 정밀도 가중 평균이다. 이 모델은 켤레(conjugate)이므로 변분 해가 **정확한 사후분포와 정확히 일치**한다(단일 변수라 근사 오차가 없다).

👉 [실습(Python)에서 ELBO 최대화로 검증](./lab-06)
:::
