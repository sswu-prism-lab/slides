<script setup>
defineProps({
  heading: { type: String, default: '' }
})
</script>

<template>
  <div class="relative h-full">
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
      {{ $slidev.nav.currentPage }}/{{ $slidev.nav.total }}
    </div>
  </div>
</template>

<style>
.slidev-layout ul {
  list-style: none;
  padding-left: 1.3em;
  margin: 0;
}
.slidev-layout ul > li {
  position: relative;
  margin: 0.35em 0;
}
.slidev-layout ul > li::before {
  content: "•";
  color: #6b74b3;
  position: absolute;
  left: -1.2em;
}
.slidev-layout ul ul > li::before {
  content: "▶";
  font-size: 0.75em;
  color: #6b74b3;
}
.slidev-layout ul ul ul > li::before {
  content: "✓";
  color: #6b74b3;
}
</style>