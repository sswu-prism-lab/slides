---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff' # Sets a custom hex background color
title: AML - Lecture 1
info: |
  ## Advanced Machine Learning Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
---

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.jpeg" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">Advanced Machine Learning</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 01: Course Introduction</p>

  <p style="color:#1a1a2e; font-size: 1.5rem; margin-top: 5rem;">Wonjun Ko, Ph.D.</p>

  <div style="color:#1a1a2e; margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p style="color:#1a1a2e; font-size: 1.25rem; margin-top: 2.5rem;">Spring 2027</p>
</div>

---
layout: prism
heading: Course Schedule
---

<div class="absolute left-10 right-10" style="top: 1rem; bottom: 5rem; display: grid; grid-template-columns: 1fr 1fr; column-gap: 5rem; align-items: center;">
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W01</span> <span style="color:#111;">Course Introduction</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W02</span> <span style="color:#9aa0a6;">Preliminaries</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W03</span> <span style="color:#9aa0a6;">Probabilistic Distributions</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W04</span> <span style="color:#9aa0a6;">Linear Regression Models</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W05</span> <span style="color:#9aa0a6;">Linear Classification Models</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W06</span> <span style="color:#9aa0a6;">Kernel Methods</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W07</span> <span style="color:#9aa0a6;">Midterm Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W08</span> <span style="color:#9aa0a6;">Midterm Exam</span></p>
  </div>
  <div>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W09</span> <span style="color:#9aa0a6;">Graphical Models</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W10</span> <span style="color:#9aa0a6;">Mixture Models</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W11</span> <span style="color:#9aa0a6;">Approximate Inference</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W12</span> <span style="color:#9aa0a6;">Sampling Methods</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W13</span> <span style="color:#9aa0a6;">Continuous Latent Variables</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W14</span> <span style="color:#9aa0a6;">Final Review</span></p>
    <p style="margin: 1rem 0; font-size: 1.3rem;"><span style="color:#4a6fa5; font-weight:bold;">W15</span> <span style="color:#9aa0a6;">Final Exam</span></p>
  </div>
</div>

---
layout: prism
heading: Who am I?
---

<div class="absolute top-0 right-5">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/fig_01_01.JPG" style="height: 11rem; border-radius: 4px;" />
</div>

- Education
  - Ph.D. in Brain and Cognitive Engineering (Sep. 2017 ~ Aug. 2022)
    - Ph.D. Dissertation Title: Deep Representation Learning in Biomedicine
  - B.Sc. in Physics (Mar. 2013 ~ Feb. 2017)

- Work Experience
  - Data Scientist (Aug. 2022 ~ Aug. 2023)
    - Senior researcher, R&D/M&T Data Analytics, Data Intelligence, SK hynix Inc.
  - Assistant Professor (Sep. 2023 ~ Current)
    - School of AI Convergence, Sungshin Women's University
    - 수정관 A-704; [e-mail](mailto:wjko@sungshin.ac.kr){style="color:#c2410c;"}; [Website](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline;"}

- Research Interests
  - Topological deep learning; Bayesian deep learning
  - 28 papers (16 papers as the main author) in biomedicine-related fields
    - [Google Scholar](https://scholar.google.com/citations?user=mzssJTUAAAAJ&hl=ko&oi=ao){style="color:#4285F4;"} | [ORCiD](https://orcid.org/0000-0001-7496-9007){style="color:#A6CE39;"}
  - New Basic Research Project (Outstanding Young Scientist) Program, National Research Foundation, Ministry of Science and ICT, Korea Government (about $400,000 over three years)

---
layout: prism
heading: What I Studied - Brain Signal Representation
---

<div class="absolute top-0 left-5">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/fig0.png" style="height: 23rem; border-radius: 4px;" />
</div>

<div class="absolute top-0 right-5">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/fig1.png" style="height: 10rem; border-radius: 4px;" />
</div>

<div class="absolute bottom-0 right-5">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/fig2.png" style="height: 8rem; border-radius: 4px;" />
</div>

---
layout: prism
heading: What I Studied - Neuroimaging Analysis
---

<div class="absolute top-0 left-20">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/fig3.png" style="height: 12rem; border-radius: 4px;" />
</div>

<div class="absolute bottom-0 left-15">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/fig5.png" style="height: 11rem; border-radius: 4px;" />
</div>

<div class="absolute bottom-0 right-15">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/fig4.png" style="height: 11.5rem; border-radius: 4px;" />
</div>

---
layout: prism
heading: What I Studied - Biomedical Data Mining
---

<div class="absolute top-0 left-35">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/fig6.png" style="height: 10rem; border-radius: 4px;" />
</div>

<div class="absolute bottom-0 left-15">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/fig7.png" style="height: 13rem; border-radius: 4px;" />
</div>

<div class="absolute bottom-0 right-15">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/fig8.png" style="height: 13rem; border-radius: 4px;" />
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
