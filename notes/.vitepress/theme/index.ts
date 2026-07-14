import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import PyRunner from './PyRunner.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // Reuse the same interactive Python runner used in the Slidev decks.
    app.component('PyRunner', PyRunner)
  },
} satisfies Theme
