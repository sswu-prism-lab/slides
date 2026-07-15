import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import { h } from 'vue'
import PyRunner from './PyRunner.vue'
import CppRunner from './CppRunner.vue'
import PdfButton from './PdfButton.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  // Render the default layout, then inject a floating "Save as PDF" button
  // into the built-in `layout-bottom` slot so it appears on every notes page.
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'layout-bottom': () => h(PdfButton),
    })
  },
  enhanceApp({ app }) {
    // Reuse the same interactive Python runner used in the Slidev decks.
    app.component('PyRunner', PyRunner)
    // C++ 실습 러너 (원격 컴파일 API, 자료구조 노트용).
    app.component('CppRunner', CppRunner)
  },
} satisfies Theme
