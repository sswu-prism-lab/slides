<script setup>
import { ref, onMounted } from 'vue'

// 슬라이드용 C++ 실습 러너. 파이썬(PyRunner)이 브라우저 내 Pyodide로 도는 것과 달리,
// C++는 원격 컴파일 서버(Wandbox)에 코드를 보내 실제 g++로 컴파일·실행한 표준출력을 받습니다.
// STL/포인터/템플릿/new·delete 전부 실제 의미론으로 동작하며, CORS를 지원해 정적 배포에서도 fetch 가능합니다.
const props = defineProps({
  compiler: { type: String, default: 'gcc-13.2.0' },
  options: { type: String, default: 'warning,gnu++17' },
  stdin: { type: String, default: '' },
})

const API = 'https://wandbox.org/api/compile.json'
const COMPILERS = [props.compiler, 'gcc-13.2.0', 'gcc-head']

const codeEl = ref(null)
const editing = ref(false)
const editableCode = ref('')
const output = ref('')
const status = ref('')
const running = ref(false)

function readSlot() {
  const c = codeEl.value
  if (!c) return ''
  const node = c.querySelector('pre code, code')
  return (node ? node.textContent : c.textContent || '').replace(/\n$/, '')
}
onMounted(() => { editableCode.value = readSlot() })

async function run() {
  if (running.value) return
  running.value = true
  status.value = ''
  output.value = '⏳ 원격 서버에서 컴파일·실행 중…'
  const code = editing.value ? editableCode.value : readSlot()
  const ctrl = new AbortController()
  const timer = setTimeout(() => ctrl.abort(), 25000)
  try {
    let data = null, lastErr = ''
    for (const compiler of [...new Set(COMPILERS)]) {
      let res
      try {
        res = await fetch(API, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          signal: ctrl.signal,
          body: JSON.stringify({ code, compiler, options: props.options, stdin: props.stdin || '', save: false }),
        })
      } catch (e) { lastErr = e.message; continue }
      if (res.ok) { data = await res.json(); break }
      lastErr = `HTTP ${res.status}`
    }
    if (!data) throw new Error(lastErr || '요청 실패')
    let out = ''
    if (data.compiler_error && data.compiler_error.trim())
      out += '── 컴파일 오류 ──\n' + data.compiler_error.trimEnd() + '\n'
    const prog = (data.program_output || '') + (data.program_error || '')
    if (prog.trim()) out += prog.replace(/\n$/, '')
    if (!out.trim()) out = '(출력이 없습니다)'
    output.value = out
    status.value = data.compiler_error && data.compiler_error.trim() ? 'error' : 'ok'
  } catch (e) {
    output.value = (e.name === 'AbortError'
      ? '요청 시간이 초과되었습니다. 다시 시도해 주세요.'
      : '실행 실패: ' + e.message) + '\n(인터넷 연결과 wandbox.org 를 사용합니다.)'
    status.value = 'error'
  } finally {
    clearTimeout(timer)
    running.value = false
  }
}
function toggleEdit() {
  if (!editing.value) editableCode.value = readSlot()
  editing.value = !editing.value
}
</script>

<template>
  <div class="cpp-runner">
    <div v-show="!editing" ref="codeEl" class="cpp-runner-code"><slot /></div>
    <textarea v-show="editing" v-model="editableCode" class="cpp-runner-edit" spellcheck="false" rows="8"></textarea>
    <div class="cpp-runner-bar">
      <button class="cpp-runner-btn" :disabled="running" @click="run">
        {{ running ? '컴파일 중…' : '▶ Run (C++)' }}
      </button>
      <button class="cpp-runner-edit-btn" :disabled="running" @click="toggleEdit">
        {{ editing ? '↩ 원본' : '✎ 수정' }}
      </button>
    </div>
    <pre v-if="output" class="cpp-runner-output" :class="{ 'is-error': status === 'error' }">{{ output }}</pre>
  </div>
</template>

<style scoped>
.cpp-runner { text-align: left; margin: 0.2rem auto; width: 92%; }
.cpp-runner-code { font-size: 0.62em; }
.cpp-runner-code :deep(pre), .cpp-runner-code :deep(code) { font-size: 1em !important; line-height: 1.15 !important; }
.cpp-runner-edit {
  width: 100%; box-sizing: border-box; font-family: 'JetBrains Mono', Consolas, monospace;
  font-size: 0.62em; line-height: 1.3; padding: 0.5em 0.7em; border: 1px solid #4a7294;
  border-radius: 6px; background: #fafafa; color: #1a1a2e; resize: vertical;
}
.cpp-runner-bar { display: flex; gap: 0.4em; margin-top: 0.35em; }
.cpp-runner-btn {
  background: #4a7294; color: #fff; border: none; padding: 0.12em 0.9em;
  border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.62em;
}
.cpp-runner-btn:disabled { opacity: 0.6; cursor: default; }
.cpp-runner-edit-btn {
  background: transparent; color: #4a7294; border: 1px solid #4a7294;
  padding: 0.12em 0.7em; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 0.58em;
}
.cpp-runner-output {
  background: #eef3f8; border: 1px solid #4a7294; color: #14243a;
  padding: 0.35em 0.7em; border-radius: 6px; margin-top: 0.45em;
  white-space: pre-wrap; font-size: 0.6em; max-height: 8.5rem; overflow: auto;
}
.cpp-runner-output.is-error { background: #fbeeee; border-color: #b2452a; color: #5a1b10; }
</style>
