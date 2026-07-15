<script setup>
import { ref, onMounted } from 'vue'

// C++ 실습 러너.
// 파이썬(PyRunner)이 브라우저 내 Pyodide로 도는 것과 달리, C++는 브라우저에서
// 바로 돌릴 표준 런타임이 없으므로 원격 컴파일 API(Wandbox)에 코드를 보내
// 실제 g++로 컴파일·실행한 결과(표준 출력)를 받아 보여줍니다.
//   - STL / 포인터 / 템플릿 / new·delete 전부 실제 g++ 의미론으로 동작합니다.
//   - CORS 를 지원하므로 정적 GitHub Pages 에서도 fetch 가 가능합니다.
//   - 코드는 아래 "✎ 코드 수정" 으로 직접 고쳐 다시 실행할 수 있습니다.
const props = defineProps({
  // 필요 시 <CppRunner compiler="gcc-13.2.0" options="warning,gnu++17"> 로 재지정 가능
  compiler: { type: String, default: 'gcc-13.2.0' },
  options: { type: String, default: 'warning,gnu++17' },
  stdin: { type: String, default: '' },
})

const API = 'https://wandbox.org/api/compile.json'
// 지정한 컴파일러가 은퇴(retire)했을 때를 대비한 폴백 순서.
const COMPILERS = [props.compiler, 'gcc-13.2.0', 'gcc-head']

const codeEl = ref(null)      // 하이라이트된 정적 코드(슬롯)
const editing = ref(false)
const editableCode = ref('')  // 편집용 textarea 내용
const stdinText = ref(props.stdin)
const output = ref('')
const status = ref('')        // '' | 'ok' | 'error'
const running = ref(false)

function readSlot() {
  const c = codeEl.value
  if (!c) return ''
  const node = c.querySelector('pre code, code')
  return (node ? node.textContent : c.textContent || '').replace(/\n$/, '')
}

onMounted(() => { editableCode.value = readSlot() })

async function compileOn(compiler, code) {
  const res = await fetch(API, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      code, compiler, options: props.options,
      stdin: stdinText.value || '', save: false,
    }),
  })
  return res
}

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
          body: JSON.stringify({
            code, compiler, options: props.options,
            stdin: stdinText.value || '', save: false,
          }),
        })
      } catch (e) { lastErr = e.message; continue }
      if (res.ok) { data = await res.json(); break }
      lastErr = `HTTP ${res.status}` // 알 수 없는 컴파일러 등 → 다음 폴백 시도
    }
    if (!data) throw new Error(lastErr || '요청 실패')

    let out = ''
    if (data.compiler_error && data.compiler_error.trim()) {
      out += '── 컴파일 오류 ──\n' + data.compiler_error.trimEnd() + '\n'
    }
    const prog = (data.program_output || '') + (data.program_error || '')
    if (prog.trim()) out += prog.replace(/\n$/, '')
    if (!out.trim()) out = '(출력이 없습니다)'
    output.value = out
    status.value = data.compiler_error && data.compiler_error.trim() ? 'error' : 'ok'
  } catch (e) {
    output.value =
      (e.name === 'AbortError'
        ? '요청 시간이 초과되었습니다. 잠시 후 다시 시도해 주세요.'
        : '실행 실패: ' + e.message) +
      '\n(이 실습은 인터넷 연결과 원격 컴파일 서버 wandbox.org 를 사용합니다.)'
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
    <textarea
      v-show="editing"
      v-model="editableCode"
      class="cpp-runner-edit"
      spellcheck="false"
      rows="12"
    ></textarea>

    <div class="cpp-runner-bar">
      <button class="cpp-runner-btn" :disabled="running" @click="run">
        {{ running ? '컴파일 중…' : '▶ 실행 (C++)' }}
      </button>
      <button class="cpp-runner-edit-btn" :disabled="running" @click="toggleEdit">
        {{ editing ? '↩ 원본 보기' : '✎ 코드 수정' }}
      </button>
    </div>

    <pre
      v-if="output"
      class="cpp-runner-output"
      :class="{ 'is-error': status === 'error' }"
    >{{ output }}</pre>
  </div>
</template>

<style scoped>
.cpp-runner {
  text-align: left;
  margin: 1rem 0;
  width: 100%;
}
.cpp-runner-edit {
  width: 100%;
  box-sizing: border-box;
  font-family: var(--vp-font-family-mono, monospace);
  font-size: 0.82em;
  line-height: 1.5;
  padding: 0.8em 1em;
  border: 1px solid #4a7294;
  border-radius: 8px;
  background: var(--vp-c-bg-alt);
  color: var(--vp-c-text-1);
  resize: vertical;
}
.cpp-runner-bar {
  display: flex;
  gap: 0.5em;
  margin-top: 0.5em;
  flex-wrap: wrap;
}
.cpp-runner-btn {
  background: #4a7294; /* ssdarkblue — C++ 실습 구분색 */
  color: white;
  border: none;
  padding: 0.35em 1.1em;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
  font-size: 0.9em;
}
.cpp-runner-btn:disabled { opacity: 0.6; cursor: default; }
.cpp-runner-edit-btn {
  background: transparent;
  color: #4a7294;
  border: 1px solid #4a7294;
  padding: 0.35em 0.9em;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.86em;
}
.cpp-runner-edit-btn:disabled { opacity: 0.6; cursor: default; }
.cpp-runner-output {
  background: #eef3f8;
  border: 1px solid #4a7294;
  color: #14243a;
  padding: 0.6em 0.9em;
  border-radius: 6px;
  margin-top: 0.6em;
  white-space: pre-wrap;
  font-size: 0.82em;
}
.cpp-runner-output.is-error {
  background: #fbeeee;
  border-color: #b2452a;
  color: #5a1b10;
}
.dark .cpp-runner-output { background: #10202f; color: #dce8f4; }
.dark .cpp-runner-output.is-error { background: #2a1512; color: #f4dcd6; }
</style>
