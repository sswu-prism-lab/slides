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

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-6 left-10 flex items-center gap-3">
  <img src="/images/bs_05_c.jpg" class="h-12" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10">
  <h1 class="text-5xl font-bold" style="color:#5c60a8;">Advanced Machine Learning</h1>
  <p class="text-2xl mt-3" style="color:#9aa0a6;">Week 01: Course Introduction</p>

  <p class="text-2xl mt-20" style="color:#1a1a2e;">Wonjun Ko, Ph.D.</p>

  <div class="mt-6 leading-relaxed" style="color:#1a1a2e;">
    <p>Assistant Professor</p>
    <p>School of AI Convergence</p>
    <p>Sungshin Women's University</p>
  </div>

  <p class="mt-10 text-xl" style="color:#1a1a2e;">Spring 2027</p>
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
