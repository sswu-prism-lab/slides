<script setup>
import { useData } from 'vitepress'
import { computed } from 'vue'

// Show on content pages only (not the VitePress "home" hero layout),
// and allow opting out per-page with `pdf: false` in frontmatter.
const { frontmatter } = useData()
const show = computed(
  () => frontmatter.value.layout !== 'home' && frontmatter.value.pdf !== false,
)

function saveAsPdf() {
  // The browser's print dialog offers "Save as PDF" as a destination.
  // A dedicated @media print stylesheet (custom.css) formats the page.
  window.print()
}
</script>

<template>
  <button
    v-if="show"
    class="pdf-fab"
    type="button"
    title="PDF로 저장 / Save as PDF"
    aria-label="Save this page as PDF"
    @click="saveAsPdf"
  >
    <span class="pdf-fab-ico" aria-hidden="true">🖨️</span>
    <span class="pdf-fab-label">PDF</span>
  </button>
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
/* On narrow screens, collapse to an icon-only circle to avoid clutter. */
@media (max-width: 640px) {
  .pdf-fab {
    padding: 11px;
    border-radius: 50%;
  }
  .pdf-fab-label {
    display: none;
  }
}
/* Never render the button itself into the printed PDF. */
@media print {
  .pdf-fab {
    display: none !important;
  }
}
</style>
