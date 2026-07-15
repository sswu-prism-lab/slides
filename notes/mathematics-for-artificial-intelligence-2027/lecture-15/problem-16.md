# 문제 16 · 이산 합성곱

::: info 문제 16 [4점]
이산 정의역에서 $x[n]$, $h[n]$이 아래와 같이 정의될 때, $y[n]=(x\star h)[n]$을 구하시오.

$$
x[n]=\begin{cases}
1 & \text{if } n=0,2\\
2 & \text{if } n=1\\
0 & \text{otherwise}
\end{cases},\qquad
h[n]=\begin{cases}
1 & \text{if } n=0,1,2\\
0 & \text{otherwise}
\end{cases}
$$
:::

::: details 풀이 및 해설
이산 합성곱<span class="gloss">discrete convolution</span>의 정의는

$$
y[n]=(x\star h)[n]=\sum_{k}x[k]\,h[n-k]
$$

이다. 수열로 나타내면 $x=[\,1,\,2,\,1\,]$ (인덱스 $0,1,2$), $h=[\,1,\,1,\,1\,]$ 이다. 각 $n$에 대해 겹치는 항을 더한다.

$$
\begin{aligned}
y[0]&=x[0]h[0]=1\cdot1=1,\\
y[1]&=x[0]h[1]+x[1]h[0]=1+2=3,\\
y[2]&=x[0]h[2]+x[1]h[1]+x[2]h[0]=1+2+1=4,\\
y[3]&=x[1]h[2]+x[2]h[1]=2+1=3,\\
y[4]&=x[2]h[2]=1\cdot1=1.
\end{aligned}
$$

따라서 $n=0,1,2,3,4$ 에서

$$
\boxed{\;y[n]=[\,1,\ 3,\ 4,\ 3,\ 1\,]\;}
$$

👉 [실습(Python)에서 확인하기](./lab-16)
:::
