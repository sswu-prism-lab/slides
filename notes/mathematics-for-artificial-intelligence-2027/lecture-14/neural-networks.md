# 신경망 · 데이터 흐름

> 기말 범위 13주차 요약. 앞선 선형대수와 미분이 어떻게 하나의 신경망으로 합쳐지는지를 본다. 퍼셉트론의 순전파, 이미지에 쓰이는 합성곱(CNN), 그리고 학습을 담당하는 역전파와 경사하강법을 정리한다.

## 퍼셉트론과 순전파

- 전통적인 신경망에서 입력값은 수치들의 벡터, 즉 **특징 벡터**<span class="gloss">feature vector</span>로 다뤄진다. 입력 하나가 벡터 하나이므로, 입력이 여러 개면 행렬로 표현하는 것이 자연스럽다.
- **퍼셉트론**<span class="gloss">perceptron</span> 또는 **순방향 신경망**<span class="gloss">feedforward neural network</span>은 층과 층 사이의 가중치들을 행렬로 저장한다. 층 $i$의 노드가 $n$개, 층 $i-1$의 출력이 $m$개이면 가중치 행렬 $\mathbf{W}_i$는 $n\times m$ 행렬이다.
- 한 노드의 출력(활성화 값)은 입력들의 가중합에 바이어스를 더하고 비선형 **활성화 함수** $\sigma$를 적용한 것이다.

$$
\sigma\!\left(b + \sum_{i=1}^{n} w_i x_i\right)
$$

::: info 층 단위 순전파
층 $i-1$의 출력 벡터 $\mathbf{a}_{i-1}$에 가중치 행렬 $\mathbf{W}_i$를 곱하고 바이어스 $\mathbf{b}_i$를 더한 뒤 활성화 함수를 적용하면 층 $i$의 출력 $\mathbf{a}_i$가 된다.

$$
\mathbf{a}_i=\sigma (\mathbf{W}_i \mathbf{a}_{i-1}+\mathbf{b}_i)
$$

즉 각 층은 **상관변환**($\mathbf{W}\mathbf{a}+\mathbf{b}$) 뒤에 비선형 함수를 씌운 것이다.
:::

- 활성화 함수로 층 사이에는 보통 **ReLU**를, 최종 의사결정 층에는 출력을 $0$과 $1$ 사이로 사상하는 **시그모이드**<span class="gloss">sigmoid</span> 계열을 쓴다. 시그모이드는 $\sigma(z)=\dfrac{1}{1+e^{-z}}$이며 그 도함수는 $\sigma'(z)=\sigma(z)(1-\sigma(z))$로 간단해 역전파에 유리하다.

<PyRunner>

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# 입력 노드 3개 -> 출력 노드 2개인 한 층의 순전파
np.random.seed(0)
W = np.array([[0.2, -0.4, 0.1],
              [0.7,  0.3, -0.5]])   # (2 x 3) 가중치
b = np.array([0.1, -0.2])          # 바이어스
a_prev = np.array([1.0, 2.0, -1.0])  # 이전 층 출력

z = W @ a_prev + b                 # 상관변환 Wa + b
a = sigmoid(z)                     # 활성화

print("가중합 z =", np.round(z, 4))
print("활성화 a = σ(z) =", np.round(a, 4))
print("σ'(z) = a(1-a) =", np.round(a * (1 - a), 4))
```

</PyRunner>

## 합성곱 신경망 (CNN)

- **합성곱 신경망**<span class="gloss">convolutional neural network; CNN</span>은 합성곱 층으로 데이터의 공간적 관계를 포착한다. 주로 2차원 배열로 표현된 이미지를 분석하며, 이미지 텐서는 $\mathbb{R}^{H\times W\times C}$($H$=높이, $W$=너비, $C$=채널)로 표현된다. 회색조 이미지는 $C=1$, 원색 이미지는 $C=3$이다.
- **합성곱**<span class="gloss">convolution</span> 연산 $\star$은 한 함수를 다른 함수 위에서 밀며 이동하는 방식으로, 연속 정의역에서는 다음과 같이 정의된다. 다만 기계학습은 이산 정의역<span class="gloss">discrete domain</span>을 다루므로 실제로 적분하는 경우는 드물다.

$$
(f\star g)(t)\equiv \int_{-\infty}^{\infty}f(\tau) g(t-\tau)\,d\tau
$$

- 입력 위를 이동하는 값들의 집합 $g$를 **커널**<span class="gloss">kernel</span>이라 한다. 이산 2차원 합성곱은 커널을 입력 위 각 위치에 겹쳐 성분별로 곱한 뒤 합한다.

::: info CNN의 주요 개념
- **영 패딩**<span class="gloss">zero padding</span>: 합성곱은 출력 크기를 줄이므로, 입력과 같은 크기를 유지하려면 가장자리에 $0$을 덧댄다.
- **보폭**<span class="gloss">stride</span>: 커널이 한 번에 움직이는 칸 수.
- **풀링**<span class="gloss">pooling</span>: 채널은 유지하며 높이·너비를 줄인다. 구간 안에서 최댓값을 취하면 **최대 풀링**<span class="gloss">max pooling</span>, 평균을 취하면 평균 풀링<span class="gloss">average pooling</span>이다. 정보 손실이 따르므로 상황에 맞게 쓴다.
- **평탄화**<span class="gloss">flattening</span>: 마지막에 텐서를 벡터로 펴서 퍼셉트론에 입력해 최종 의사결정을 내린다.
:::

<PyRunner>

```python
import numpy as np

# 유효(valid) 2D 합성곱: 커널을 입력 위에서 밀며 성분곱-합
def conv2d(I, K):
    kh, kw = K.shape
    oh, ow = I.shape[0] - kh + 1, I.shape[1] - kw + 1
    out = np.zeros((oh, ow))
    for i in range(oh):
        for j in range(ow):
            out[i, j] = np.sum(I[i:i+kh, j:j+kw] * K)
    return out

I = np.array([[0,1,1,1,0,0,0],
              [0,0,1,1,1,0,0],
              [0,0,0,1,1,1,0],
              [0,0,0,1,1,0,0],
              [0,0,1,1,0,0,0],
              [0,1,1,0,0,0,0],
              [1,1,0,0,0,0,0]], float)
K = np.array([[1,0,1],[0,1,0],[1,0,1]], float)   # 3x3 커널

out = conv2d(I, K)
print("I ⋆ K (5x5) =")
print(out.astype(int))
print("최대 풀링(2x2, stride 2) 좌상단 =",
      out[:2, :2].max())
```

</PyRunner>

## 역전파와 경사하강법

- **역전파**<span class="gloss">backpropagation</span>는 딥러닝 학습의 사실상 표준<span class="gloss">de facto standard</span>이다. 신경망 학습은 본질적으로 **손실 함수**<span class="gloss">loss function</span>를 최소화하는 최적화 문제이다. 손실 함수는 가중치·바이어스를 입력받아 성능과 관련한 값을 출력한다.
- 가중치·바이어스를 묶은 매개변수를 벡터 $\boldsymbol{\theta}$로 표기하면 손실은 $L=L(\boldsymbol{\theta};\mathbf{x},y)$이다. 역전파는 이 손실의 그래디언트 $\nabla L(\boldsymbol{\theta};\mathbf{x},y)$를 (연쇄법칙으로) 구해, 손실이 가장 작아지는 방향을 찾는다.

::: info 경사하강법 갱신 공식
$$
\mathbf{W}\leftarrow\mathbf{W}-\eta\,\Delta \mathbf{W},\qquad
\mathbf{b}\leftarrow\mathbf{b}-\eta\,\Delta \mathbf{b}
$$

여기서 $\Delta\mathbf{W}$, $\Delta\mathbf{b}$는 손실 함수를 가중치·바이어스로 편미분한 그래디언트이고, $\eta$는 **학습률**<span class="gloss">learning rate</span>로 한 번의 갱신에서 극소점 쪽으로 얼마나 이동할지를 정한다. 그래디언트의 반대 방향으로 반복 이동하면 손실의 극소점에 다가간다.
:::

<PyRunner>

```python
import numpy as np

def sigmoid(z): return 1.0 / (1.0 + np.exp(-z))

# 단일 시그모이드 뉴런을 경사하강으로 학습 (OR에 가까운 목표)
X = np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
y = np.array([0., 1., 1., 1.])
w = np.zeros(2); b = 0.0; eta = 0.5

for step in range(2000):
    z = X @ w + b
    a = sigmoid(z)                     # 순전파
    err = a - y                        # dL/dz  (제곱오차·시그모이드 결합)
    grad_w = X.T @ (err * a * (1 - a)) # 연쇄법칙: dL/dw
    grad_b = np.sum(err * a * (1 - a))
    w -= eta * grad_w                  # 경사하강 갱신
    b -= eta * grad_b

pred = sigmoid(X @ w + b)
print("학습된 w =", np.round(w, 3), " b =", round(b, 3))
print("예측 =", np.round(pred, 3))
print("MSE =", round(np.mean((pred - y)**2), 5))
```

</PyRunner>
