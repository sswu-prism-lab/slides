---
theme: default
title: AML - Lecture 1
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
---

# Advanced Machine Learning

Lecture 1

<div class="pt-5">
  <span class="opacity-70">Wonjun Ko, Ph.D.<br>Assistant Professor<br>School of AI Convergence<br>Sungshin Women's University</span>
</div>

<div class="pt-3">
  <span class="opacity-50">Spring 2027</span>
</div>

---

# Today's Topics

<v-clicks>

- Introduction to representation learning
- EEG / fMRI data structures
- Statistical mechanics perspective on deep learning
- Live demo

</v-clicks>

---

# Math example (KaTeX)

TeX 문법 그대로 씁니다 — 별도 변환 없이:

$$
\mathcal{L}(\theta) = -\sum_{i=1}^{N} y_i \log \hat{y}_i(\theta) + \lambda \|\theta\|_2^2
$$

인라인 수식도 가능해요: 자유 에너지는 $F = U - TS$ 로 정의됩니다.

---

# Image example

이미지 파일은 `public/` 폴더에 넣고, 슬라이드에서는 `/파일명`으로 참조하세요.

```md
![EEG electrode layout](/eeg-layout.png)
```

<!--
public/eeg-layout.png 파일을 실제로 넣으시면 이 슬라이드에 이미지가 나타납니다.
-->

---

# Step-by-step reveal (click animation)

<v-click>

**Step 1.** Raw EEG signal is collected from multiple channels.

</v-click>

<v-click>

**Step 2.** Signal is decomposed into frequency bands (e.g., theta, alpha, beta).

</v-click>

<v-click>

**Step 3.** A graph neural network models inter-channel relationships.

</v-click>

---
layout: center
class: text-center
---

# Thank you!

Contact: wjko@sungshin.ac.kr
