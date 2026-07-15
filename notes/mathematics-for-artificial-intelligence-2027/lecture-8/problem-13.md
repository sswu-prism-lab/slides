# 문제 13 · 복소수의 근

::: info 문제 13 [4점]
집합 $\{z:\lVert z\rVert=1,\ \mathfrak{I}(z^3)=0,\ \forall z\in\mathbb{C}\}$의 원소(들)를 찾으시오. ($\mathfrak{I}$는 허수부를 의미한다.)
:::

::: details 풀이 및 해설
$\lVert z\rVert=1$이므로 $z=e^{i\theta}=\cos\theta+i\sin\theta$로 둘 수 있습니다. 그러면

$$
z^3 = e^{i3\theta} = \cos 3\theta + i\sin 3\theta.
$$

허수부가 $0$이라는 조건 $\mathfrak{I}(z^3)=\sin 3\theta = 0$에서

$$
3\theta = k\pi \quad\Longrightarrow\quad \theta = \frac{k\pi}{3},\quad k=0,1,2,3,4,5.
$$

각 $\theta$에 대응하는 $z$는 다음과 같습니다(단위원 위의 6등분점, 즉 $1$의 여섯 제곱근).

$$
\begin{aligned}
&\theta=0: && 1 \\
&\theta=\tfrac{\pi}{3}: && \tfrac{1}{2}+\tfrac{\sqrt{3}}{2}i \\
&\theta=\tfrac{2\pi}{3}: && -\tfrac{1}{2}+\tfrac{\sqrt{3}}{2}i \\
&\theta=\pi: && -1 \\
&\theta=\tfrac{4\pi}{3}: && -\tfrac{1}{2}-\tfrac{\sqrt{3}}{2}i \\
&\theta=\tfrac{5\pi}{3}: && \tfrac{1}{2}-\tfrac{\sqrt{3}}{2}i
\end{aligned}
$$

$$
\boxed{\;z\in\left\{\pm 1,\ \pm\tfrac{1}{2}\pm\tfrac{\sqrt{3}}{2}i\right\}\ (\text{총 } 6\text{개})\;}
$$

이는 $z^3$이 실수, 즉 $z^3=\pm 1$인 점들로, $1$의 세 제곱근과 그 반수를 합한 여섯 개의 점입니다.

👉 [실습(Python)에서 확인하기](./lab-13)
:::
