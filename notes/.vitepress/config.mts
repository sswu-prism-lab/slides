import { defineConfig } from 'vitepress'

// PRISM Lab lecture *notes* site (note-style weeks: W07, W08, W14, W15).
// Slide weeks stay in Slidev under courses/; this VitePress site is deployed
// to GitHub Pages under /slides/notes/ alongside them.
export default defineConfig({
  title: 'PRISM Lab Lecture Notes',
  description: 'Advanced Machine Learning — lecture notes and worked problem sets',
  lang: 'ko-KR',
  base: '/slides/notes/',
  cleanUrls: true,
  ignoreDeadLinks: true,
  markdown: {
    math: true,
  },
  themeConfig: {
    outline: { level: [2, 3], label: '목차' },
    docFooter: { prev: '이전', next: '다음' },
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Advanced Machine Learning 2027', link: '/advanced-machine-learning-2027/' },
    ],
    sidebar: {
      '/advanced-machine-learning-2027/': [
        {
          text: '고급 기계학습 (2027)',
          items: [
            { text: '개요', link: '/advanced-machine-learning-2027/' },
          ],
        },
        {
          text: 'W07 · 중간고사 예제 문제',
          collapsed: false,
          items: [
            { text: '소개', link: '/advanced-machine-learning-2027/lecture-7/' },
            { text: '문제 1 · 기본 확률 법칙', link: '/advanced-machine-learning-2027/lecture-7/problem-01' },
            { text: '문제 2 · 기댓값과 분산', link: '/advanced-machine-learning-2027/lecture-7/problem-02' },
            { text: '문제 3 · 베이지안 결정 이론', link: '/advanced-machine-learning-2027/lecture-7/problem-03' },
            { text: '문제 4 · 최대가능도추정', link: '/advanced-machine-learning-2027/lecture-7/problem-04' },
            { text: '문제 5 · 라그랑제 승수법', link: '/advanced-machine-learning-2027/lecture-7/problem-05' },
            { text: '문제 6 · 최소제곱법', link: '/advanced-machine-learning-2027/lecture-7/problem-06' },
            { text: '문제 7 · 선형 판별 함수', link: '/advanced-machine-learning-2027/lecture-7/problem-07' },
            { text: '문제 8 · 확률적 분류 모델', link: '/advanced-machine-learning-2027/lecture-7/problem-08' },
            { text: '문제 9 · 라플라스 근사법', link: '/advanced-machine-learning-2027/lecture-7/problem-09' },
            { text: '문제 10 · 커널 방법론', link: '/advanced-machine-learning-2027/lecture-7/problem-10' },
          ],
        },
        {
          text: 'W07 · 실습 (Python)',
          collapsed: false,
          items: [
            { text: '문제 1 실습', link: '/advanced-machine-learning-2027/lecture-7/lab-01' },
            { text: '문제 2 실습', link: '/advanced-machine-learning-2027/lecture-7/lab-02' },
            { text: '문제 3 실습', link: '/advanced-machine-learning-2027/lecture-7/lab-03' },
            { text: '문제 6 실습', link: '/advanced-machine-learning-2027/lecture-7/lab-06' },
            { text: '문제 7 실습', link: '/advanced-machine-learning-2027/lecture-7/lab-07' },
            { text: '문제 9 실습', link: '/advanced-machine-learning-2027/lecture-7/lab-09' },
          ],
        },
      ],
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/sswu-prism-lab/slides' },
    ],
  },
})
