<script setup>
import { ref } from 'vue'

const codeEl = ref(null)
const output = ref('')
const running = ref(false)
const pyodideReady = ref(false)
let pyodide = null

async function ensurePyodide() {
  if (pyodide) return pyodide

  if (!window.loadPyodide) {
    await new Promise((resolve, reject) => {
      const script = document.createElement('script')
      script.src = 'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js'
      script.onload = resolve
      script.onerror = () => reject(new Error('Failed to load Pyodide script'))
      document.head.appendChild(script)
    })
  }

  pyodide = await window.loadPyodide({
    indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.1/full/',
  })
  await pyodide.loadPackage('numpy')
  pyodideReady.value = true
  return pyodide
}

async function run() {
  if (running.value) return
  running.value = true
  output.value = pyodideReady.value ? '' : '⏳ Loading Python runtime (only needed once)...'

  try {
    const py = await ensurePyodide()
    const code = codeEl.value ? codeEl.value.textContent.trim() : ''

    let buffer = ''
    py.setStdout({
      batched: (s) => {
        buffer += s + '\n'
        output.value = buffer
      },
    })
    py.setStderr({
      batched: (s) => {
        buffer += s + '\n'
        output.value = buffer
      },
    })

    await py.runPythonAsync(code)
  } catch (e) {
    output.value += '\n[Error] ' + e.message
  } finally {
    running.value = false
  }
}
</script>

<template>
  <div class="py-runner">
    <div ref="codeEl" class="py-runner-code"><slot /></div>
    <button class="py-runner-btn" :disabled="running" @click="run">
      {{ running ? (pyodideReady ? 'Running…' : 'Loading Python…') : '▶ Run' }}
    </button>
    <pre v-if="output" class="py-runner-output">{{ output }}</pre>
  </div>
</template>

<style scoped>
.py-runner {
  text-align: left;
  margin: 1rem 0;
  width: 100%;
}
.py-runner-btn {
  background: #4ba08f;
  color: white;
  border: none;
  padding: 0.35em 1.1em;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
  font-size: 0.9em;
  margin-top: 0.4em;
}
.py-runner-btn:disabled {
  opacity: 0.6;
  cursor: default;
}
.py-runner-output {
  background: #f2f9f7;
  border: 1px solid #4ba08f;
  color: #1a1a2e;
  padding: 0.6em 0.9em;
  border-radius: 6px;
  margin-top: 0.6em;
  white-space: pre-wrap;
  font-size: 0.82em;
}
.dark .py-runner-output {
  background: #0f1f1c;
  color: #e6f4f1;
}
</style>
