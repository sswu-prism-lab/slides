<script setup>
defineProps({
  heading: { type: String, default: '' }
})
</script>

<template>
  <div class="slidev-layout relative h-full">
    <div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

    <div class="absolute top-6 left-10 flex items-center gap-3">
      <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/bs_05_c_cropped.png" style="height: 3.5rem;" />
      <h1 style="color:#6b74b3; font-size: 2.25rem; font-weight: bold; margin: 0;">{{ heading }}</h1>
    </div>

    <div class="absolute left-10 right-10" style="top: 6rem; bottom: 5rem; overflow: auto;">
      <slot />
    </div>

    <div class="absolute bottom-6 left-10 flex items-center gap-3">
      <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/PRISM.png" style="height: 3rem;" />
    </div>

    <div class="absolute bottom-6 right-10" style="font-size: 1rem; color:#333;">
      {{ $slidev.nav.currentPage - 1 }}/{{ $slidev.nav.total - 2 }}
    </div>
  </div>
</template>

<style>
.slidev-layout ul,
.slidev-layout ul ul,
.slidev-layout ul ul ul {
  list-style: none;
  padding-left: 3.3em;
  margin: 0;
}

/* 1단계(최상위) 항목: 섹션 사이 여백 + 불릿 크기 키움 */
.slidev-layout ul > li {
  position: relative;
  margin: 1.2em 0 0 0;
  padding: 0;
  line-height: 1.35;
}
.slidev-layout ul > li:first-child {
  margin-top: 0;
}
.slidev-layout ul > li::before {
  content: "●";
  color: #6b74b3;
  position: absolute;
  left: -1.5em;
  font-size: 1em; /* ← 1단계 불릿만 키움 */
}

/* 2단계 항목: 글자 크기 축소 */
.slidev-layout ul ul > li {
  margin: 0;
  font-size: 0.9em;
  left: -2em
}
.slidev-layout ul ul > li::before {
  content: "▶";
  font-size: 1em;
  color: #6b74b3;
}

/* 3단계 항목: 글자 크기 더 축소 */
.slidev-layout ul ul ul > li {
  margin: 0;
  font-size: 0.8em;
  left: -2.5em
}
.slidev-layout ul ul ul > li::before {
  content: "✔";
  color: #6b74b3;
}

.slidev-layout li > p {
  margin: 0;
}

.hl {
  color: #5c60a8;
  font-style: italic;
  font-weight: 600;
}

.sub-item {
  position: relative;
  margin: 0;
  padding-left: 1.3em;
  font-size: 0.9em;
  left: 3.8em;
  width: calc(100% - 5.3em); /* left(4em) + padding-left(1.3em)만큼 빼서 오른쪽 끝에 안 넘치게 */
  box-sizing: border-box;
  overflow-wrap: break-word;
}
.sub-item::before {
  content: "▶";
  font-size: 1em;
  color: #6b74b3;
  position: absolute;
  left: 0;
}

/* sub-item 안의 문단(<p>) 기본 여백 제거 → 세로 간격도 없어짐 */
.sub-item p {
  margin: 0;
}

.subsub-item {
  position: relative;
  margin: 0;
  padding-left: 1.4em;
  font-size: 0.8em;
  left: 5.9em;
  width: calc(100% - 7.3em);
  box-sizing: border-box;
  overflow-wrap: break-word;
}
.subsub-item::before {
  content: "✔";
  color: #6b74b3;
  position: absolute;
  left: 0;
}
.subsub-item p {
  margin: 0;
}

/* 수식 사이의 여백 */
.slidev-layout .katex-display {
  margin: -0.3em 0;
}

/* 이미지 가운데 정렬을 위해 */
.img-center {
  display: block;
  margin: 1rem auto;
}

/* 이미지 가로 배치를 위해 */
.img-row {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.3rem;
  margin: 1rem auto;
  width: 100%;
}
.img-row img {
  flex: 1 1 0;
  min-width: 0;
  width: auto;
  max-width: 100%;
  height: auto;
  object-fit: contain;
}

/* Theorem 박스 */
.theorem-box {
  border: 1px solid #4ba08f;
  border-radius: 8px;
  margin: 1.5rem auto; /* 좌우를 auto로 → 가운데 정렬 */
  width: 85%; /* 원하는 비율로 조절 */
  overflow: hidden;
}
.theorem-box-title {
  background: #4ba08f;
  color: white;
  font-weight: bold;
  font-size: 1.1em;
  padding: 0.6rem 1.2rem;
}
.theorem-box-body {
  background: #f2f9f7;
  padding: 1rem 1.2rem;
  text-align: justify;
}
.theorem-box-body p {
  margin: 0.5em 0;
}
</style>