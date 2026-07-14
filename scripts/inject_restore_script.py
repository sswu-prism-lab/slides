#!/usr/bin/env python3
"""
Slidev로 빌드된 각 강의 덱의 index.html에, 사이트 최상위 404.html이 넘겨준
"진짜 요청 경로"를 복원하는 작은 스크립트를 삽입합니다.

GitHub Pages는 사이트 전체에서 최상위 404.html 하나만 인식하기 때문에,
특정 슬라이드 번호(예: .../lecture-2/4)로 직접 접속하거나 새로고침하면
404.html이 대신 응답합니다. 그 404.html은 원래 주소를 sessionStorage에
저장해두고 해당 강의 덱의 index.html로 이동시키는데, 이 스크립트가 그
index.html이 로드되는 시점에 저장해둔 진짜 주소로 다시 바꿔치기해서
Slidev 라우터가 올바른 슬라이드를 보여주게 합니다.

사용법: python3 inject_restore_script.py <index.html 경로>
"""

import sys

SNIPPET = """<script>
(function () {
  var redirect = sessionStorage.getItem('slidev-redirect-path');
  if (redirect) {
    sessionStorage.removeItem('slidev-redirect-path');
    var current = location.pathname + location.search + location.hash;
    if (redirect !== current) {
      history.replaceState(null, '', redirect);
    }
  }
})();
</script>
"""


def main():
    if len(sys.argv) < 2:
        print("usage: inject_restore_script.py <index.html path>", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    if "slidev-redirect-path" in html:
        print(f"  (이미 삽입되어 있음, 건너뜀: {path})")
        return

    if "<head>" not in html:
        print(f"  ! <head> 태그를 찾지 못함: {path}", file=sys.stderr)
        sys.exit(1)

    html = html.replace("<head>", "<head>\n" + SNIPPET, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  복원 스크립트 삽입 완료: {path}")


if __name__ == "__main__":
    main()
