---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 2 (KO)
download: true
info: |
  ## C++ 프로그래밍 강의 슬라이드 (한국어판)
  Pattern Recognition and Intelligent System Modeling Lab, 성신여자대학교
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-2/
---
<style>
.dark .slidev-page,
.dark .slidev-layout,
.dark .slide-container,
.dark #slide-content,
.dark .slidev-nav-go-container {
  background: #000000 !important;
}
.tikz-fig {
  background: #ffffff;
  border-radius: 8px;
  padding: 0.4rem 0.6rem;
}
</style>

<div class="absolute top-0 left-0 right-0 border-t border-gray-300"></div>

<div class="absolute top-4 left-6 flex items-center gap-3">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo.png" class="dark:hidden" style="height: 4rem;" />
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/general/sswu_logo_dark.png" class="hidden dark:block" style="height: 4rem;" />
</div>

<div class="h-full flex flex-col items-center justify-center text-center px-10" style="padding-top: 4rem;">
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">C++ 프로그래밍</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">2주차: 컴퓨터와 C++ 소개</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">고원준 (Wonjun Ko), Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">조교수</p>
    <p style="margin: 0;">인공지능융합학부</p>
    <p style="margin: 0;">성신여자대학교</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">2027년 가을학기</p>
</div>

---
layout: prism
heading: 출석 평가 (10%)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- 출석은 최종 성적의 [10%]{.hl}를 차지하며, 지각에 대해서는 간단한 규칙이 적용됩니다.
  - 수업 시작 후 [30분]{.hl} 이내에 출석 체크를 하면 결석이 아니라 *지각*으로 기록됩니다.

- 처음 두 번의 [결석]{.hl}과 처음 두 번의 [지각]{.hl}에는 *불이익이 없습니다*.

- 그 이후부터는 감점이 누적됩니다:
  - 세 번째 결석부터 `-5%`이며, 결석이 네 번 이상이면 [F]{.hl} 학점을 받을 수 있습니다.
  - 세 번째 지각부터 `-1%`입니다.

---
layout: prism
heading: 컴퓨터란 무엇인가?
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- 컴퓨터의 구성 요소들은 [버스(bus)]{.hl}로 서로 연결되어 있으며, 개인용 컴퓨터에서는 이 버스가 [메인보드]{.hl}에 내장되어 있습니다.

- **시스템 유닛** — CPU, 주기억장치, 저장 장치.

- **입력 장치** — 키보드, 마우스, 마이크.

- **출력 장치** — 모니터, 스피커.

</div>
<div>

<div style="height: 0rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 디지털과 아날로그
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- [디지털은 단순합니다!]{.hl}
  - 모든 신호는 제한된 개수의 숫자(digit)로 표현할 수 있습니다.

- [디지털은 효율적입니다!]{.hl}
  - 숫자는 쉽게 저장, 전송, 복사할 수 있습니다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image3.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 이진법
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- 컴퓨터에게 [이진법(binary)]{.hl}은 숫자를 표현하는 가장 효율적인 방식이며, 그 이유는 다음과 같습니다:
  - 표현의 단순함, 신뢰성, 논리 연산, 디지털 잡음 내성, 그리고 낮은 비용과 복잡도.

- 컴퓨터의 메모리는 데이터를 이진 상태를 나타내는 전하로 저장합니다.
  - 전하가 *있으면* `1`, *없으면* `0`을 나타냅니다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image4.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 비트와 바이트
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- 비트는 문자-비트 패턴 쌍을 통해 [문자]{.hl}를 표현할 수 있습니다.
  - `a`는 `01100001`, `d`는 `01000100`.

- 비트는 Red-Green-Blue의 조합으로 픽셀의 [색]{.hl}을 표현할 수 있습니다.
  - 흰색은 `R:11111111 G:11111111 B:11111111`, 노란색은 `R:11111111 G:11111111 B:00000000`.

- 비트는 파형을 샘플링하고 이산화하여 [소리]{.hl}를 표현할 수 있습니다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image5.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: CPU에서의 이진 연산
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
table th, table td { padding: 1px 12px; line-height: 1.15; text-align: center; }
table { font-size: 0.85em; }
</style>

- **A와 B의 덧셈** — 전가산기(full adder)는 두 비트와 자리올림 입력(carry-in)을 합산합니다.

| A | B | Cin | Cout | S |
| - | - | --- | ---- | - |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image7.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.6rem; text-align: center; color:#9aa0a6; font-size: 0.9rem;">A0A1과 B0B1의 곱셈</div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image6.png" class="tikz-fig" style="width: 100%; margin-top: 0.3rem;" />

</div>
</div>

---
layout: prism
heading: 프로그래밍 언어의 계층 (1/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image8.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.8rem; text-align: center; color:#9aa0a6; font-size: 1rem; font-style: italic;">"안 보여? 네오가 여기 있잖아."</div>

</div>
<div>

<div style="height: 1rem;"></div>

<div style="display:flex; flex-direction:column; gap:0.9rem;">
  <div style="border:2px solid #4a6fa5; border-radius:6px; padding:0.9rem; text-align:center; font-size:1.3rem;" class="text-gray-900 dark:text-gray-100">고급 언어</div>
  <div style="border:2px solid #4a6fa5; border-radius:6px; padding:0.9rem; text-align:center; font-size:1.3rem;" class="text-gray-900 dark:text-gray-100">어셈블리 언어</div>
  <div style="border:2px solid #4a7c8c; background:#4a7c8c; border-radius:6px; padding:0.9rem; text-align:center; font-size:1.3rem; color:#ffffff;">기계어</div>
  <div style="border:2px solid #4a6fa5; border-radius:6px; padding:0.9rem; text-align:center; font-size:1.3rem;" class="text-gray-900 dark:text-gray-100">하드웨어</div>
</div>

</div>
</div>

---
layout: prism
heading: 프로그래밍 언어의 계층 (2/3)
---

<div class="flex justify-center" style="margin-top: 1.5rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image9.png" class="tikz-fig" style="width: 70%;" />
</div>

---
layout: prism
heading: 프로그래밍 언어의 계층 (3/3)
---

<div class="flex justify-center" style="margin-top: 1.5rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image10.png" class="tikz-fig" style="width: 70%;" />
</div>

---
layout: prism
heading: 고급 언어가 필요하다 (1/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [기계어]{.hl}는 기계가 직접 이해할 수 있는 이진법 기반 언어입니다.

- 기계어는 사람에게 *친화적이지 않습니다*.

- 기계어는 [하드웨어에 의존적입니다]{.hl}!

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image11.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 고급 언어가 필요하다 (2/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [어셈블리 언어]{.hl}는 이진 기계 명령어를 사람에게 좀 더 친화적인 *니모닉(mnemonic)*으로 일대일 대응시킨 것입니다.

- 하지만 프로그래머가 크고 구조화된 프로그램을 개발하기에는 여전히 꽤 어렵습니다.

- 여전히 [하드웨어에 의존적입니다]{.hl}.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image12.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 고급 언어가 필요하다 (3/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [고급 언어]{.hl}는 쉽고 효율적입니다.

- 하드웨어에서 벗어나므로, 하나의 코드로 여러 다른 컴퓨터에서 사용할 수 있습니다.

- 컴퓨터의 세부 사항으로부터 강력한 [추상화]{.hl}를 제공하여 더 높은 프로그래밍 효율을 제공합니다.

- 대부분 자연어 요소로 구성되어 있어 이해하기가 더 쉽습니다.

</div>
<div>

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image14.png" class="tikz-fig" style="width: 100%;" />

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image13.png" class="tikz-fig" style="width: 100%; margin-top: 0.5rem;" />

</div>
</div>

---
layout: prism
heading: Visual Studio와 Visual Studio Code
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [Visual Studio Code]{.hl}
  - 가벼운 코드 편집기
  - 크로스 플랫폼
  - 더 적은 시스템 자원 요구
  - 웹 개발자들이 선호하지만, 그들에게만 국한되지는 않음
  - 무료이며 오픈 소스

</div>
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [Visual Studio]{.hl}
  - 완전한 기능을 갖춘 통합 개발 환경(IDE)
  - 원래는 Windows 전용
  - 더 무거움
  - 주로 기업 수준의 애플리케이션 개발에 사용됨
  - Community Edition은 무료

</div>
</div>

---
layout: prism
heading: Windows PC를 위한 VS Code (1/7)
---

- 공식 웹사이트에서 [VS Code]{.hl} 설치 프로그램을 내려받아 설치를 시작합니다.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image19.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: Windows PC를 위한 VS Code (2/7)
---

- 라이선스 계약에 동의하고 설치 위치를 선택합니다.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image20.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: Windows PC를 위한 VS Code (3/7)
---

- 추가 작업(PATH에 추가, 컨텍스트 메뉴 항목)을 선택하고 설치를 마칩니다.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image21.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: Windows PC를 위한 VS Code (4/7)
---

- [확장(Extensions)]{.hl} 뷰를 열고 C/C++ 확장 팩을 설치합니다.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image22.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: Windows PC를 위한 VS Code (5/7)
---

- 컴파일러(예: [MinGW-w64]{.hl})를 설치하고 시스템 PATH에 포함되어 있는지 확인합니다.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image23.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: Windows PC를 위한 VS Code (6/7)
---

<div style="margin-bottom: 0.6rem;">

- `.cpp` 파일을 만들고 프로그램을 입력한 뒤 `Ctrl + F5`로 실행합니다.

</div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main()
{
    // 콘솔에 몇 개의 문장을 출력해 봅시다!
    cout << "Hello, World!" << endl;
    cout << "Programming is Fun!" << endl;
    cout << "Fundamentals First" << endl;
    cout << "Problem Driven" << endl;
    cout << (10.5 + 2 * 3) / (45 - 3.5) << endl;
    /*
       또 다른 주석 스타일
       보통 여러 줄에 걸친 주석에 사용됩니다
    */
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Windows PC를 위한 VS Code (7/7)
---

- 프로그램 출력은 창 하단의 통합 [터미널]{.hl}에 나타납니다.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image24.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: Mac PC를 위한 VS Code (1/9)
---

- macOS용 [VS Code]{.hl}를 내려받아 앱을 응용 프로그램(Applications) 폴더로 끌어다 놓습니다.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image25.png" class="tikz-fig" style="width: 60%;" />
</div>

---
layout: prism
heading: Mac PC를 위한 VS Code (2/9)
---

- 확장 뷰에서 [C/C++]{.hl} 확장과 관련 도구들을 설치합니다.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image26.png" class="tikz-fig" style="width: 60%;" />
</div>

---
layout: prism
heading: Mac PC를 위한 VS Code (3/9)
---

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image28.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">1. 폴더 생성</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image27.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">2. 폴더 선택</div>

</div>
</div>

---
layout: prism
heading: Mac PC를 위한 VS Code (4/9)
---

- 작업 폴더를 VS Code에서 열어 편집기가 이를 프로젝트로 인식하도록 합니다.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image29.png" class="tikz-fig" style="width: 60%;" />
</div>

---
layout: prism
heading: Mac PC를 위한 VS Code (5/9)
---

<div style="margin-bottom: 0.5rem;">

- `Command + Space`로 "terminal"을 검색한 뒤 컴파일러를 확인합니다. `clang`이 없다면 `xcode-select --install`을 실행합니다. 코드를 작성하고 `Command + S`로 `hello.cpp`라는 이름으로 저장합니다.

</div>

```text
clang --version
xcode-select --install
```

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main()
{
    // 콘솔에 몇 개의 문장을 출력해 봅시다!
    cout << "Hello, World!" << endl;
    cout << "Programming is Fun!" << endl;
    cout << "Fundamentals First" << endl;
    cout << "Problem Driven" << endl;
    cout << (10.5 + 2 * 3) / (45 - 3.5) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Mac PC를 위한 VS Code (6/9)
---

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image31.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">"Run in Terminal" 선택</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image30.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">"Edit in settings.json" 선택</div>

</div>
</div>

<div class="flex justify-center" style="margin-top: 0.6rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image32.png" class="tikz-fig" style="width: 42%;" />
</div>

---
layout: prism
heading: Mac PC를 위한 VS Code (7/9)
---

- 빌드 작업과 설정을 구성하여 VS Code가 `clang++`로 컴파일하는 방법을 알 수 있도록 합니다.

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image34.png" class="tikz-fig" style="width: 100%;" />

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image33.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Mac PC를 위한 VS Code (8/9)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<style>
.slidev-layout pre { font-size: 0.62rem; line-height: 1.15; }
</style>

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "type": "cppbuild",
      "label": "C/C++: clang++ build active file",
      "command": "/usr/bin/clang++",
      "args": [
        "-fdiagnostics-color=always",
        "-g",
        "${fileBasename}",
        "-std=c++17",
        "-o",
        "${fileDirname}/Build/${fileBasenameNoExtension}"
      ],
      "options": { "cwd": "${fileDirname}" },
      "problemMatcher": ["$gcc"],
      "group": { "kind": "build", "isDefault": true },
      "detail": "compiler: /usr/bin/clang++"
    }
  ]
}
```

</div>
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- 생성된 `tasks.json`에 이 코드를 붙여넣고 `Command + S`로 저장합니다.

- `Command + Shift + B`로 프로그램을 빌드합니다.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image35.png" class="tikz-fig" style="width: 100%; margin-top: 0.5rem;" />

</div>
</div>

---
layout: prism
heading: Mac PC를 위한 VS Code (9/9)
---

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image36.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">1. <code>Command + Shift + B</code>로 빌드</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image37.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">2. 마우스 오른쪽 버튼 또는 <code>Command + Option + N</code>으로 실행</div>

</div>
</div>

---
layout: prism
heading: 간단한 코드 (1/2)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<CppRunner>

```cpp
#include <iostream>

using namespace std;

int main()
{
    // 콘솔에 몇 개의 문장을 출력해 봅시다!
    cout << "Hello, World!" << endl;
    cout << "Programming is Fun!" << endl;
    cout << "Fundamentals First" << endl;
    cout << "Problem Driven" << endl;
    cout << (10.5 + 2 * 3) / (45 - 3.5) << endl;
    /*
       또 다른 주석 스타일
       보통 여러 줄에 걸친 주석에 사용됩니다
    */

    return 0;
}
```

</CppRunner>

</div>
<div>

<div class="sub-item">

- `#include <iostream>`는 `iostream` 라이브러리를 이 프로그램에 포함시키는 [전처리기 지시자]{.hl}입니다.

- `int`, `main`, `return`, `using`은 이 프로그램에서 사용된 [키워드]{.hl}(예약어)에 속합니다.

- `using namespace std;`는 표준 네임스페이스(예: `cout`, `endl`)를 사용합니다.

- `//`는 [줄 주석]{.hl}을 시작하고, `/* ... */`은 [블록 주석]{.hl}입니다.

- `return 0;` — 여기서 `0`은 프로그램이 성공적으로 종료되었음을 나타냅니다.

</div>

</div>
</div>

---
layout: prism
heading: 간단한 코드 (2/2)
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 3px 14px; line-height: 1.2; }
.slidev-layout table { font-size: 0.92em; margin-top: 1rem; }
</style>

일반적인 C++ 프로그램에서 볼 수 있는 특수 문자:

| 문자 | 이름 | 설명 |
| --- | --- | --- |
| `#` | 파운드 기호 | `#include`에서 전처리기 지시자를 나타내는 데 사용됩니다. |
| `<>` | 여는 꺾쇠와 닫는 꺾쇠 | `#include`와 함께 사용될 때 라이브러리 이름을 감쌉니다. |
| `()` | 여는 괄호와 닫는 괄호 | `main()`과 같은 함수에 사용됩니다. |
| `{}` | 여는 중괄호와 닫는 중괄호 | 문장을 감싸는 블록을 나타냅니다. |
| `//` | 이중 슬래시 | 주석 줄 앞에 붙습니다. |
| `<<` | 스트림 삽입 연산자 | 콘솔로 출력합니다. |
| `" "` | 여는 따옴표와 닫는 따옴표 | 문자열(문자의 나열)을 감쌉니다. |
| `;` | 세미콜론 | 문장의 끝을 나타냅니다. |

---
layout: prism
heading: 프로그래밍 스타일과 문서화
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- 좋은 프로그래밍 스타일과 적절한 문서화는 프로그램을 [읽기 쉽게]{.hl} 만들고 프로그래머가 [오류를 예방]{.hl}하는 데 도움을 줍니다.

- 각 주요 단계를 소개하거나 읽기 어려운 부분을 설명하기 위해 주석을 사용하세요.

- 일관된 [들여쓰기]{.hl} 스타일은 프로그램을 명확하게 만들어 읽고, 디버깅하고, 유지보수하기 쉽게 합니다.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image39.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: 프로그래밍 오류
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- 프로그래밍 오류는 세 가지 유형으로 나뉩니다:
  - [구문 오류(Syntax errors)]{.hl} — 컴파일러가 감지합니다.
  - [런타임 오류(Runtime errors)]{.hl} — 실행 중에 프로그램이 중단되게 합니다.
  - [논리 오류(Logic errors)]{.hl} — 프로그램은 실행되지만 잘못된 결과를 냅니다.

- 닫는 중괄호, 세미콜론, 따옴표를 빠뜨리거나 이름의 철자를 틀리는 것은 초보자가 흔히 하는 실수입니다.

</div>
<div>

<div style="height: 1rem;"></div>

구문 오류 (닫는 따옴표 누락):

```cpp
cout << "Programming is Fun! << endl;
return 0;
```

런타임 오류 (0으로 나누기):

```cpp
int i = 4;
int j = 0;
cout << i / j << endl;
```

</div>
</div>

---
layout: prism
heading: "기초 프로그래밍: ComputingArea"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main()
{
    double radius;
    double area;
    // 1단계: 반지름 입력받기
    radius = 20;
    // 2단계: 넓이 계산하기
    area = radius * radius * 3.14159;
    // 3단계: 넓이 출력하기
    cout << "The area is " << area << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "기초 프로그래밍: ComputeAverage"
---

<CppRunner stdin="1 2 3">

```cpp
#include <iostream>
using namespace std;

int main()
{
    // 사용자에게 세 개의 숫자를 입력하도록 안내
    double number1, number2, number3;
    cout << "Enter three numbers: ";
    cin >> number1 >> number2 >> number3;
    // 평균 계산
    double average = (number1 + number2 + number3) / 3;
    // 결과 출력
    cout << "The average of " << number1 << " " << number2 << " "
         << number3 << " is " << average << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 식별자와 변수
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [식별자(Identifiers)]{.hl}는 변수나 함수와 같은 요소들의 이름입니다.
  - 문자, 숫자, 밑줄(`_`)의 나열이며;
  - 반드시 문자나 밑줄로 시작해야 하고;
  - 예약어가 될 수 없으며;
  - 길이에 제한이 없습니다(컴파일러가 제한을 둘 수는 있음).

- [변수(Variables)]{.hl}는 프로그램이 실행되는 동안 변경될 수 있는 값을 나타냅니다.

</div>
<div>

<div style="height: 2rem;"></div>

```cpp
int i, j;
i = 1;
j = 2;

double radius;
radius = 20;

double radius = 2.0;
int i = 1, j = 2;
```

</div>
</div>

---
layout: prism
heading: 대입문
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [대입문(assignment statement)]{.hl}은 변수에 값을 지정하며, `variable = expression;` 형태로 작성됩니다.

- C++에서 대입은 [수식(expression)]{.hl}으로도 사용될 수 있습니다.

- [수식(expression)]{.hl}은 값, 변수, 연산자에 대한 계산을 나타내며 하나의 값으로 평가됩니다.

</div>
<div>

<div style="height: 1rem;"></div>

```cpp
int y = 1;             // y에 1을 대입
double radius = 1.0;   // radius에 1.0을 대입
int x = 5 * (3 / 2);   // 수식을 x에 대입
x = y + 1;             // y + 1을 x에 대입
area = radius * radius * 3.14159;
```

</div>
</div>

---
layout: prism
heading: 명명된 상수
---

<div style="margin-bottom: 0.5rem;">

- [명명된 상수(named constant)]{.hl}는 영구적인 값을 나타내는 식별자입니다: `const datatype CONSTANTNAME = value;`. 관례상 상수는 대문자로 명명합니다.

</div>

<CppRunner stdin="20">

```cpp
#include <iostream>
using namespace std;

int main()
{
    const double PI = 3.14159;
    // 1단계: 반지름 입력받기
    double radius;
    cout << "Enter a radius: ";
    cin >> radius;
    // 2단계: 넓이 계산하기
    double area = radius * radius * PI;
    // 3단계: 넓이 출력하기
    cout << "The area is ";
    cout << area << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: 수치 자료형
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 2px 12px; line-height: 1.15; }
.slidev-layout table { font-size: 0.8em; margin-top: 0.8rem; }
</style>

| 이름 | 동의어 | 범위 | 저장 크기 |
| --- | --- | --- | --- |
| `short` | `short int` | $-2^{15}$ ~ $2^{15}-1$ (−32,768 ~ 32,767) | 16비트 부호 있음 |
| `unsigned short` | `unsigned short int` | 0 ~ $2^{16}-1$ (65,535) | 16비트 부호 없음 |
| `int` | `signed` | $-2^{31}$ ~ $2^{31}-1$ | 32비트 부호 있음 |
| `unsigned` | `unsigned int` | 0 ~ $2^{32}-1$ (4,294,967,295) | 32비트 부호 없음 |
| `long` | `long int` | $-2^{31}$ ~ $2^{31}-1$ | 32비트 부호 있음 |
| `unsigned long` | `unsigned long int` | 0 ~ $2^{32}-1$ | 32비트 부호 없음 |
| `float` | | ±1.4E−45 ~ ±3.4028235E+38 | 32비트 IEEE 754 |
| `double` | | ±4.9E−324 ~ ±1.7976931348623157E+308 | 64비트 IEEE 754 |
| `long double` | | ±3.37E−4932 ~ ±1.18E+4932 | 80비트 |

---
layout: prism
heading: 수치 연산자
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout table th, .slidev-layout table td { padding: 3px 12px; }
.slidev-layout table { font-size: 0.9em; }
</style>

| 연산자 | 이름 | 예시 | 결과 |
| --- | --- | --- | --- |
| `+` | 덧셈 | `34 + 1` | 35 |
| `-` | 뺄셈 | `34.0 - 0.1` | 33.9 |
| `*` | 곱셈 | `300 * 30` | 9000 |
| `/` | 나눗셈 | `1.0 / 2.0` | 0.5 |
| `%` | 나머지 | `20 % 3` | 2 |

</div>
<div>

`3 + 4 * 4 + 5 * (4 + 3) - 1`의 연산자 우선순위 추적:

```text
3 + 4 * 4 + 5 * (4 + 3) - 1
3 + 4 * 4 + 5 * 7 - 1     (1) parentheses first
3 + 16    + 5 * 7 - 1     (2) multiplication
3 + 16    + 35    - 1     (3) multiplication
19        + 35    - 1     (4) addition
54                - 1     (5) addition
53                        (6) subtraction
```

</div>
</div>

---
layout: prism
heading: 다양한 연산자
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout table th, .slidev-layout table td { padding: 2px 10px; }
.slidev-layout table { font-size: 0.82em; }
</style>

**복합 대입 연산자**

| 연산자 | 이름 | 예시 | 등가 표현 |
| --- | --- | --- | --- |
| `+=` | 덧셈 대입 | `i += 8` | `i = i + 8` |
| `-=` | 뺄셈 대입 | `i -= 8` | `i = i - 8` |
| `*=` | 곱셈 대입 | `i *= 8` | `i = i * 8` |
| `/=` | 나눗셈 대입 | `i /= 8` | `i = i / 8` |
| `%=` | 나머지 대입 | `i %= 8` | `i = i % 8` |

</div>
<div>

<style>
.slidev-layout table th, .slidev-layout table td { padding: 2px 10px; }
.slidev-layout table { font-size: 0.82em; }
</style>

**증가와 감소 연산자** (`i = 1`이라고 가정)

| 연산자 | 이름 | 설명 | 예시 |
| --- | --- | --- | --- |
| `++var` | 전위 증가 | 증가시키고 *새* 값 사용 | `int j = ++i;` → `j`는 2, `i`는 2 |
| `var++` | 후위 증가 | 증가시키되 *원래* 값 사용 | `int j = i++;` → `j`는 1, `i`는 2 |
| `--var` | 전위 감소 | 감소시키고 *새* 값 사용 | `int j = --i;` → `j`는 0, `i`는 0 |
| `var--` | 후위 감소 | 감소시키되 *원래* 값 사용 | `int j = i--;` → `j`는 1, `i`는 0 |

</div>
</div>

---
layout: prism
heading: 수치 자료형 변환
---

<div style="margin-bottom: 0.4rem;">

- C++는 [형변환(casting)]{.hl} 연산자 `static_cast<type>(value)`를 사용하여 한 자료형의 값을 다른 자료형으로 명시적으로 변환할 수 있습니다. 작은 범위에서 큰 범위로 변환하는 것은 [확장(widening)]{.hl}이고, 큰 범위에서 작은 범위로 변환하는 것은 [축소(narrowing)]{.hl}입니다.

</div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main()
{
    int i = 34.7;      // 축소: i는 34가 됨
    double f = i;      // 확장: f는 이제 34
    double g = 34.3;   // g는 34.3이 됨
    int j = g;         // 축소: j는 이제 34
    cout << "i = " << i << endl;
    cout << "f = " << f << endl;
    cout << "g = " << g << endl;
    cout << "j = " << j << endl;
    cout << "static_cast<int>(1.7) = " << static_cast<int>(1.7) << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "직접 해보기! (1/2) — Mad Lib"
---

<div style="margin-bottom: 0.4rem;">

- 사용자에게 형용사와 명사를 입력받은 뒤, 미리 만들어 둔 이야기 템플릿에 삽입해 봅시다.

</div>

<CppRunner stdin="remote island old keeper">

```cpp
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string adj1, noun1, adj2, noun2;
    cout << "Enter an adjective: ";  cin >> adj1;
    cout << "Enter a noun: ";        cin >> noun1;
    cout << "Enter an adjective: ";  cin >> adj2;
    cout << "Enter a noun: ";        cin >> noun2;

    cout << "\n--- Your Story ---\n";
    cout << "Once upon a time, on a " << adj1 << " " << noun1
         << ", there lived a " << adj2 << " " << noun2 << "." << endl;
    cout << "Every day, the " << noun2 << " gazed across the "
         << adj1 << " " << noun1 << " and dreamed of adventure." << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "직접 해보기! (2/2) — 진법 변환"
---

<div style="margin-bottom: 0.4rem;">

- 10진수를 입력받아 2진법(binary), 3진법(ternary), …, 9진법(nonary) 표현을 출력해 봅시다.

</div>

<CppRunner stdin="24">

```cpp
#include <iostream>
#include <string>
using namespace std;

// 음이 아닌 정수를 주어진 진법(2..9)으로 변환
string toBase(int n, int base)
{
    if (n == 0) return "0";
    string digits;
    while (n > 0) {
        digits = char('0' + n % base) + digits;
        n /= base;
    }
    return digits;
}

int main()
{
    int n;
    cout << "Enter a decimal number: ";
    cin >> n;
    for (int base = 2; base <= 9; base++)
        cout << n << " in base " << base << ": " << toBase(n, base) << endl;
    return 0;
}
```

</CppRunner>

---
layout: center
class: text-center
---

# ***감사합니다!***
<br></br>

_연락처:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_웹사이트:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
