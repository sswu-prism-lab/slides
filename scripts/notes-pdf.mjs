#!/usr/bin/env node
/**
 * 빌드된 VitePress 노트 사이트(dist/notes)를 순회하며 각 페이지를 PDF로 렌더링해
 * 같은 경로에 <파일>.pdf 로 저장합니다. 테마의 "PDF 다운로드" 버튼이 이 파일을 가리킵니다.
 *
 *   실행: node scripts/notes-pdf.mjs
 *   전제: `vitepress build notes` 후 dist/notes/ 가 존재하고, playwright(-chromium)가 설치되어 있음.
 *
 * page.pdf() 는 기본적으로 print 미디어로 렌더링하므로 custom.css 의 `@media print`
 * 규칙(네비/사이드바/버튼 숨김, 단일 컬럼, 라이트 배경)이 그대로 적용됩니다.
 */
import http from 'node:http'
import fs from 'node:fs'
import path from 'node:path'

// CI에서는 레포 devDependency인 playwright-chromium을, 로컬/기타 환경에서는 playwright를 사용.
let chromium
try { ({ chromium } = await import('playwright-chromium')) }
catch { ({ chromium } = await import('playwright')) }

const DIST = path.resolve('dist')             // 사이트 루트 (GitHub Pages 배포 루트)
const NOTES = path.join(DIST, 'notes')
const BASE = '/slides'                          // 프로젝트 저장소 base (user.github.io/slides/)
const PORT = 4327

if (!fs.existsSync(NOTES)) {
  console.error(`[notes-pdf] ${NOTES} 가 없습니다. 먼저 'vitepress build notes' 를 실행하세요.`)
  process.exit(1)
}

const MIME = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.mjs': 'text/javascript',
  '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif',
  '.webp': 'image/webp', '.woff': 'font/woff', '.woff2': 'font/woff2', '.ttf': 'font/ttf',
  '.otf': 'font/otf', '.eot': 'application/vnd.ms-fontobject', '.ico': 'image/x-icon',
  '.map': 'application/json', '.txt': 'text/plain',
}

// 정적 서버: /slides/<rest> -> dist/<rest>
const server = http.createServer((req, res) => {
  try {
    let url = decodeURIComponent(req.url.split('?')[0].split('#')[0])
    if (url.startsWith(BASE)) url = url.slice(BASE.length)
    let fp = path.join(DIST, url)
    if (fp.endsWith(path.sep) || url.endsWith('/') || url === '') fp = path.join(fp, 'index.html')
    if (!fs.existsSync(fp)) {
      if (fs.existsSync(fp + '.html')) fp = fp + '.html'
      else if (fs.existsSync(path.join(fp, 'index.html'))) fp = path.join(fp, 'index.html')
    }
    if (!fs.existsSync(fp) || fs.statSync(fp).isDirectory()) { res.statusCode = 404; res.end('404'); return }
    res.setHeader('Content-Type', MIME[path.extname(fp).toLowerCase()] || 'application/octet-stream')
    fs.createReadStream(fp).pipe(res)
  } catch (e) { res.statusCode = 500; res.end(String(e)) }
})

// dist/notes 아래의 모든 .html (404.html·assets 제외) 을 페이지 목록으로 수집
function walk(dir) {
  let out = []
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name)
    if (e.isDirectory()) { if (e.name === 'assets') continue; out = out.concat(walk(p)) }
    else if (e.name.endsWith('.html') && e.name !== '404.html') out.push(p)
  }
  return out
}

const pages = walk(NOTES)
await new Promise((r) => server.listen(PORT, r))

const browser = await chromium.launch()
const page = await browser.newPage()
let ok = 0
for (const html of pages) {
  const rel = path.relative(DIST, html).split(path.sep).join('/')   // notes/.../foo.html
  let route = '/' + rel.replace(/\.html$/, '')                       // /notes/.../foo (or /notes/.../index)
  route = route.replace(/\/index$/, '/')                             // 인덱스는 디렉터리 경로로
  const url = `http://localhost:${PORT}${BASE}${route}`
  const pdfPath = html.replace(/\.html$/, '.pdf')                    // dist/notes/.../foo.pdf
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 })
    // 서버 렌더된 수식(mjx-container)이 이미 정적으로 들어있음. 폰트/레이아웃 안정화만 잠깐 대기.
    await page.waitForTimeout(300)
    await page.pdf({
      path: pdfPath, format: 'A4', printBackground: true,
      margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' },
    })
    ok++
  } catch (e) {
    console.error(`[notes-pdf] 실패: ${route} -> ${e.message}`)
  }
}
await browser.close()
await new Promise((r) => server.close(r))
console.log(`[notes-pdf] 완료: ${ok}/${pages.length} 페이지 PDF 생성 (dist/notes/**/*.pdf)`)
