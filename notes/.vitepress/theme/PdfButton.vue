<script setup>
import { useData, withBase } from 'vitepress'
import { computed } from 'vue'

// 각 노트 페이지에는 빌드 시(Playwright, scripts/notes-pdf.mjs) 미리 생성해 둔
// 동일 경로의 .pdf 파일이 있습니다. 이 버튼은 그 파일을 바로 내려받습니다.
const { page, frontmatter } = useData()

const show = computed(
  () => frontmatter.value.layout !== 'home' && frontmatter.value.pdf !== false,
)

// relativePath 예: "mathematics-for-artificial-intelligence-2027/lecture-8/problem-01.md"
// → 같은 경로의 .pdf (base = /slides/notes/) 로 링크
const pdfHref = computed(() =>
  withBase((page.value.relativePath || 'index.md').replace(/\.md$/, '.pdf')),
)
const pdfName = computed(() => pdfHref.value.split('/').pop() || 'note.pdf')
</script>

<template>
  <a
    v-if="show"
    class="pdf-fab"
    :href="pdfHref"
    :download="pdfName"
    title="이 페이지를 PDF로 다운로드 / Download this page as PDF"
    aria-label="Download this page as PDF"
  >
    <span class="pdf-fab-ico" aria-hidden="true">⬇</span>
    <span class="pdf-fab-label">PDF</span>
  </a>
</template>

<style scoped>
.pdf-fab {
  position: fixed;
  right: 22px;
  bottom: 22px;
  z-index: 40;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 9px 15px;
  border: none;
  border-radius: 999px;
  background: #4a7294; /* ssdarkblue, matches the notes brand */
  color: #fff;
  font-size: 0.86rem;
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.22);
  transition: background 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
}
.pdf-fab:hover {
  background: #3172b7; /* ssblue */
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.28);
}
.pdf-fab:active {
  transform: translateY(1px);
}
.pdf-fab-ico {
  font-size: 1rem;
  line-height: 1;
}
/* 좁은 화면에서는 아이콘만 표시 */
@media (max-width: 640px) {
  .pdf-fab {
    padding: 11px;
    border-radius: 50%;
  }
  .pdf-fab-label {
    display: none;
  }
}
/* 생성되는 PDF(인쇄 미디어)에는 버튼 자체가 찍히지 않도록 */
@media print {
  .pdf-fab {
    display: none !important;
  }
}
</style>
