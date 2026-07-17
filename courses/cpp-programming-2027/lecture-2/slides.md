---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 2
download: true
info: |
  ## C++ Programming Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-2-ko/
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
  <h1 style="color:#5c60a8; font-size: 3.5rem; font-weight: bold; margin: 0rem;">C++ Programming</h1>
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 02: Introduction to Computers and C++</p>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.5rem; margin-top: 5rem;">Wonjun Ko, Ph.D.</p>

  <div class="text-gray-800 dark:text-gray-100" style="margin-top: 1.5rem; line-height: 1.3;">
    <p style="margin: 0;">Assistant Professor</p>
    <p style="margin: 0;">School of AI Convergence</p>
    <p style="margin: 0;">Sungshin Women's University</p>
  </div>

  <p class="text-gray-800 dark:text-gray-100" style="font-size: 1.25rem; margin-top: 2.5rem;">Fall 2027</p>
</div>

---
layout: prism
heading: Grading for Attendance (10%)
---

<style>
.slidev-layout ul > li {
  margin-top: 1.8em;
}
</style>

- Attendance counts for [10%]{.hl} of the final grade, with a simple rule for late arrivals.
  - Checking in within [30 minutes]{.hl} of the class starting is recorded as a *tardiness*, not an absence.

- There is *no penalty* for the first two [absences]{.hl} and the first two instances of [tardiness]{.hl}.

- Penalties then accumulate:
  - `-5%` from the third absence; four or more absences may result in a grade of [F]{.hl}.
  - `-1%` from the third tardiness.

---
layout: prism
heading: What is a Computer?
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0rem;">
<div>

- A computer's components are interconnected by a [bus]{.hl}; in personal computers the bus is built into the [motherboard]{.hl}.

- **System units** — CPU, main memory, storage devices.

- **Input devices** — keyboard, mouse, microphone.

- **Output devices** — monitor, speaker.

</div>
<div>

<div style="height: 0rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image2.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Digital and Analogue
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- [Digital is simple!]{.hl}
  - Every signal can be expressed by a limited number of digits (numbers).

- [Digital is efficient!]{.hl}
  - Digits can be easily stored, transmitted, and copied.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image3.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Binary
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- For computers, [binary]{.hl} is the most efficient way to express numbers, thanks to:
  - simplicity of representation, reliability, logic operations, digital noise immunity, and low cost and complexity.

- A computer's memory stores data as electrical charges that represent binary states.
  - The *presence* of charge represents `1`, and its *absence* represents `0`.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image4.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Bit and Byte
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.3em;
}
</style>

- Bits can represent a [character]{.hl} via character-bit pattern pairs.
  - `01100001` for `a` and `01000100` for `d`.

- Bits can represent the [color]{.hl} of a pixel as a combination of Red-Green-Blue.
  - `R:11111111 G:11111111 B:11111111` for white; `R:11111111 G:11111111 B:00000000` for yellow.

- Bits can represent [sound]{.hl} by sampling and discretizing the wave form.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image5.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Binary Operations in CPU
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

- **Adding A and B** — a full adder combines two bits and a carry-in.

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

<div style="margin-top: 0.6rem; text-align: center; color:#9aa0a6; font-size: 0.9rem;">Multiplying A0A1 and B0B1</div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image6.png" class="tikz-fig" style="width: 100%; margin-top: 0.3rem;" />

</div>
</div>

---
layout: prism
heading: Hierarchy of Programming Language (1/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image8.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.8rem; text-align: center; color:#9aa0a6; font-size: 1rem; font-style: italic;">"Can't you see? Neo is here."</div>

</div>
<div>

<div style="height: 1rem;"></div>

<div style="display:flex; flex-direction:column; gap:0.9rem;">
  <div style="border:2px solid #4a6fa5; border-radius:6px; padding:0.9rem; text-align:center; font-size:1.3rem;" class="text-gray-900 dark:text-gray-100">High-level languages</div>
  <div style="border:2px solid #4a6fa5; border-radius:6px; padding:0.9rem; text-align:center; font-size:1.3rem;" class="text-gray-900 dark:text-gray-100">Assembly language</div>
  <div style="border:2px solid #4a7c8c; background:#4a7c8c; border-radius:6px; padding:0.9rem; text-align:center; font-size:1.3rem; color:#ffffff;">Machine language</div>
  <div style="border:2px solid #4a6fa5; border-radius:6px; padding:0.9rem; text-align:center; font-size:1.3rem;" class="text-gray-900 dark:text-gray-100">Hardware</div>
</div>

</div>
</div>

---
layout: prism
heading: Hierarchy of Programming Language (2/3)
---

<div class="flex justify-center" style="margin-top: 1.5rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image9.png" class="tikz-fig" style="width: 70%;" />
</div>

---
layout: prism
heading: Hierarchy of Programming Language (3/3)
---

<div class="flex justify-center" style="margin-top: 1.5rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image10.png" class="tikz-fig" style="width: 70%;" />
</div>

---
layout: prism
heading: We Need High-Level Language (1/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- [Machine language]{.hl} is a binary-based language that a machine can understand directly.

- It is *not* human friendly.

- It is [hardware-dependent]{.hl}!

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image11.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: We Need High-Level Language (2/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- [Assembly language]{.hl} is a one-to-one correspondence from a binary machine instruction to more human-friendly *mnemonics*.

- It is still quite hard for programmers to develop big, structured programs.

- It is still [hardware-dependent]{.hl}.

</div>
<div>

<div style="height: 2rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image12.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: We Need High-Level Language (3/3)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- [High-level language]{.hl} is easy and efficient.

- It gets away from the hardware, so one code base can be used for many different computers.

- It provides strong [abstraction]{.hl} from the details of the computer, giving higher programming efficiency.

- It is mostly composed of natural-language elements, therefore easier to understand.

</div>
<div>

<div style="height: 1rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image14.png" class="tikz-fig" style="width: 100%;" />

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image13.png" class="tikz-fig" style="width: 100%; margin-top: 0.5rem;" />

</div>
</div>

---
layout: prism
heading: Visual Studio and Visual Studio Code
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [Visual Studio Code]{.hl}
  - a lightweight code editor
  - cross-platform
  - requires fewer system resources
  - favoured by web developers, but not limited to them
  - free and open-source

</div>
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [Visual Studio]{.hl}
  - a full-fledged integrated development environment
  - originally Windows-only
  - heavier
  - often used for enterprise-level application development
  - free for the Community Edition

</div>
</div>

---
layout: prism
heading: VS Code for Windows PC (1/7)
---

- Download the [VS Code]{.hl} installer from the official website and start the setup.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image19.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: VS Code for Windows PC (2/7)
---

- Accept the license agreement and choose the installation location.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image20.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: VS Code for Windows PC (3/7)
---

- Select the additional tasks (add to PATH, context-menu entries) and finish the installation.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image21.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: VS Code for Windows PC (4/7)
---

- Open the [Extensions]{.hl} view and install the C/C++ extension pack.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image22.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: VS Code for Windows PC (5/7)
---

- Install a compiler (e.g. [MinGW-w64]{.hl}) and make sure it is on your system PATH.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image23.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: VS Code for Windows PC (6/7)
---

<div style="margin-bottom: 0.6rem;">

- Create a `.cpp` file, type the program, and run it with `Ctrl + F5`.

</div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main()
{
    // Print some sentences in the console!
    cout << "Hello, World!" << endl;
    cout << "Programming is Fun!" << endl;
    cout << "Fundamentals First" << endl;
    cout << "Problem Driven" << endl;
    cout << (10.5 + 2 * 3) / (45 - 3.5) << endl;
    /*
       Another comment style
       Typically used for multiple comment lines
    */
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: VS Code for Windows PC (7/7)
---

- The program output appears in the integrated [terminal]{.hl} at the bottom of the window.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image24.png" class="tikz-fig" style="width: 62%;" />
</div>

---
layout: prism
heading: VS Code for Mac PC (1/9)
---

- Download [VS Code]{.hl} for macOS and drag the app into the Applications folder.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image25.png" class="tikz-fig" style="width: 60%;" />
</div>

---
layout: prism
heading: VS Code for Mac PC (2/9)
---

- Install the [C/C++]{.hl} extension and related tools from the Extensions view.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image26.png" class="tikz-fig" style="width: 60%;" />
</div>

---
layout: prism
heading: VS Code for Mac PC (3/9)
---

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image28.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">1. Create a folder</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image27.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">2. Select the folder</div>

</div>
</div>

---
layout: prism
heading: VS Code for Mac PC (4/9)
---

- Open the working folder in VS Code so the editor treats it as your project.

<div class="flex justify-center" style="margin-top: 1rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image29.png" class="tikz-fig" style="width: 60%;" />
</div>

---
layout: prism
heading: VS Code for Mac PC (5/9)
---

<div style="margin-bottom: 0.5rem;">

- With `Command + Space`, search "terminal", then verify the compiler. If `clang` is missing, run `xcode-select --install`. Write the code and save it as `hello.cpp` with `Command + S`.

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
    // Print some sentences in the console!
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
heading: VS Code for Mac PC (6/9)
---

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image31.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">Select "Run in Terminal"</div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image30.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">Select "Edit in settings.json"</div>

</div>
</div>

<div class="flex justify-center" style="margin-top: 0.6rem;">
  <img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image32.png" class="tikz-fig" style="width: 42%;" />
</div>

---
layout: prism
heading: VS Code for Mac PC (7/9)
---

- Configure the build task and settings so VS Code knows how to compile with `clang++`.

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
heading: VS Code for Mac PC (8/9)
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

- Paste this code into the generated `tasks.json` and save it with `Command + S`.

- Build the program with `Command + Shift + B`.

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image35.png" class="tikz-fig" style="width: 100%; margin-top: 0.5rem;" />

</div>
</div>

---
layout: prism
heading: VS Code for Mac PC (9/9)
---

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image36.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">1. Build with <code>Command + Shift + B</code></div>

</div>
<div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image37.png" class="tikz-fig" style="width: 100%;" />

<div style="margin-top: 0.5rem; text-align:center; color:#9aa0a6;">2. Run with right-click or <code>Command + Option + N</code></div>

</div>
</div>

---
layout: prism
heading: Simple Code (1/2)
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.5rem;">
<div>

<CppRunner>

```cpp
#include <iostream>

using namespace std;

int main()
{
    // Print some sentences in console!
    cout << "Hello, World!" << endl;
    cout << "Programming is Fun!" << endl;
    cout << "Fundamentals First" << endl;
    cout << "Problem Driven" << endl;
    cout << (10.5 + 2 * 3) / (45 - 3.5) << endl;
    /*
       Another comment style
       Typically used for multiple comment lines
    */

    return 0;
}
```

</CppRunner>

</div>
<div>

<div class="sub-item">

- `#include <iostream>` is a [preprocessor directive]{.hl} that includes the `iostream` library into this program.

- `int`, `main`, `return`, `using` are among the [keywords]{.hl} (reserved words) in this program.

- `using namespace std;` uses the standard namespace (e.g. `cout`, `endl`).

- `//` starts a [line comment]{.hl}; `/* ... */` is a [block comment]{.hl}.

- `return 0;` — the `0` indicates the program terminated with a successful exit.

</div>

</div>
</div>

---
layout: prism
heading: Simple Code (2/2)
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 3px 14px; line-height: 1.2; }
.slidev-layout table { font-size: 0.92em; margin-top: 1rem; }
</style>

Special characters seen in a typical C++ program:

| Character | Name | Description |
| --- | --- | --- |
| `#` | Pound sign | Used in `#include` to denote a preprocessor directive. |
| `<>` | Opening and closing angle brackets | Enclose a library name when used with `#include`. |
| `()` | Opening and closing parentheses | Used with functions such as `main()`. |
| `{}` | Opening and closing braces | Denote a block to enclose statements. |
| `//` | Double slashes | Precede a comment line. |
| `<<` | Stream insertion operator | Outputs to the console. |
| `" "` | Opening and closing quotation marks | Wrap a string (a sequence of characters). |
| `;` | Semicolon | Marks the end of a statement. |

---
layout: prism
heading: Programming Style and Documentation
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 2rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.6em;
}
</style>

- Good programming style and proper documentation make a program [easy to read]{.hl} and help programmers [prevent errors]{.hl}.

- Use comments for introducing each major step and to explain anything that is difficult to read.

- A consistent [indentation]{.hl} style makes programs clear and easy to read, debug, and maintain.

</div>
<div>

<div style="height: 3rem;"></div>

<img src="https://raw.githubusercontent.com/sswu-prism-lab/slides/main/images/cpp/cpp-2027/w02/cpp-w02-image39.png" class="tikz-fig" style="width: 100%;" />

</div>
</div>

---
layout: prism
heading: Programming Errors
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- Programming errors fall into three types:
  - [Syntax errors]{.hl} — detected by the compiler.
  - [Runtime errors]{.hl} — cause the program to abort while running.
  - [Logic errors]{.hl} — the program runs but produces wrong results.

- Missing a closing brace, a semicolon, or quotation marks, and misspelling names are common beginner mistakes.

</div>
<div>

<div style="height: 1rem;"></div>

Syntax error (missing closing quote):

```cpp
cout << "Programming is Fun! << endl;
return 0;
```

Runtime error (division by zero):

```cpp
int i = 4;
int j = 0;
cout << i / j << endl;
```

</div>
</div>

---
layout: prism
heading: "Elementary Programming: ComputingArea"
---

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main()
{
    double radius;
    double area;
    // Step 1: Read in radius
    radius = 20;
    // Step 2: Compute area
    area = radius * radius * 3.14159;
    // Step 3: Display the area
    cout << "The area is " << area << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Elementary Programming: ComputeAverage"
---

<CppRunner stdin="1 2 3">

```cpp
#include <iostream>
using namespace std;

int main()
{
    // Prompt the user to enter three numbers
    double number1, number2, number3;
    cout << "Enter three numbers: ";
    cin >> number1 >> number2 >> number3;
    // Compute average
    double average = (number1 + number2 + number3) / 3;
    // Display result
    cout << "The average of " << number1 << " " << number2 << " "
         << number3 << " is " << average << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Identifiers and Variables
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 0.9em;
}
</style>

- [Identifiers]{.hl} are the names of elements such as variables and functions.
  - a sequence of letters, digits, and underscores (`_`);
  - must start with a letter or an underscore;
  - cannot be a reserved word;
  - can be of any length (compilers may impose limits).

- [Variables]{.hl} represent values that may change while the program runs.

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
heading: Assignment Statements
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- An [assignment statement]{.hl} designates a value for a variable, written `variable = expression;`.

- In C++, an assignment can also be used as an [expression]{.hl}.

- An [expression]{.hl} represents a computation over values, variables, and operators that evaluates to a value.

</div>
<div>

<div style="height: 1rem;"></div>

```cpp
int y = 1;             // assign 1 to y
double radius = 1.0;   // assign 1.0 to radius
int x = 5 * (3 / 2);   // assign expression to x
x = y + 1;             // assign y + 1 to x
area = radius * radius * 3.14159;
```

</div>
</div>

---
layout: prism
heading: Named Constants
---

<div style="margin-bottom: 0.5rem;">

- A [named constant]{.hl} is an identifier that represents a permanent value: `const datatype CONSTANTNAME = value;`. By convention, constants are named in uppercase.

</div>

<CppRunner stdin="20">

```cpp
#include <iostream>
using namespace std;

int main()
{
    const double PI = 3.14159;
    // Step 1: Read in radius
    double radius;
    cout << "Enter a radius: ";
    cin >> radius;
    // Step 2: Compute area
    double area = radius * radius * PI;
    // Step 3: Display the area
    cout << "The area is ";
    cout << area << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: Numerical Data Types
---

<style>
.slidev-layout table th, .slidev-layout table td { padding: 2px 12px; line-height: 1.15; }
.slidev-layout table { font-size: 0.8em; margin-top: 0.8rem; }
</style>

| Name | Synonym | Range | Storage Size |
| --- | --- | --- | --- |
| `short` | `short int` | $-2^{15}$ to $2^{15}-1$ (−32,768 to 32,767) | 16-bit signed |
| `unsigned short` | `unsigned short int` | 0 to $2^{16}-1$ (65,535) | 16-bit unsigned |
| `int` | `signed` | $-2^{31}$ to $2^{31}-1$ | 32-bit signed |
| `unsigned` | `unsigned int` | 0 to $2^{32}-1$ (4,294,967,295) | 32-bit unsigned |
| `long` | `long int` | $-2^{31}$ to $2^{31}-1$ | 32-bit signed |
| `unsigned long` | `unsigned long int` | 0 to $2^{32}-1$ | 32-bit unsigned |
| `float` | | ±1.4E−45 to ±3.4028235E+38 | 32-bit IEEE 754 |
| `double` | | ±4.9E−324 to ±1.7976931348623157E+308 | 64-bit IEEE 754 |
| `long double` | | ±3.37E−4932 to ±1.18E+4932 | 80-bit |

---
layout: prism
heading: Numerical Operators
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout table th, .slidev-layout table td { padding: 3px 12px; }
.slidev-layout table { font-size: 0.9em; }
</style>

| Operator | Name | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `34 + 1` | 35 |
| `-` | Subtraction | `34.0 - 0.1` | 33.9 |
| `*` | Multiplication | `300 * 30` | 9000 |
| `/` | Division | `1.0 / 2.0` | 0.5 |
| `%` | Modulus | `20 % 3` | 2 |

</div>
<div>

Operator precedence trace of `3 + 4 * 4 + 5 * (4 + 3) - 1`:

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
heading: Various Operators
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout table th, .slidev-layout table td { padding: 2px 10px; }
.slidev-layout table { font-size: 0.82em; }
</style>

**Augmented assignment operators**

| Operator | Name | Example | Equivalent |
| --- | --- | --- | --- |
| `+=` | Addition assignment | `i += 8` | `i = i + 8` |
| `-=` | Subtraction assignment | `i -= 8` | `i = i - 8` |
| `*=` | Multiplication assignment | `i *= 8` | `i = i * 8` |
| `/=` | Division assignment | `i /= 8` | `i = i / 8` |
| `%=` | Modulus assignment | `i %= 8` | `i = i % 8` |

</div>
<div>

<style>
.slidev-layout table th, .slidev-layout table td { padding: 2px 10px; }
.slidev-layout table { font-size: 0.82em; }
</style>

**Increment and decrement operators** (assume `i = 1`)

| Operator | Name | Description | Example |
| --- | --- | --- | --- |
| `++var` | preincrement | increment, use *new* value | `int j = ++i;` → `j` is 2, `i` is 2 |
| `var++` | postincrement | increment, use *original* value | `int j = i++;` → `j` is 1, `i` is 2 |
| `--var` | predecrement | decrement, use *new* value | `int j = --i;` → `j` is 0, `i` is 0 |
| `var--` | postdecrement | decrement, use *original* value | `int j = i--;` → `j` is 1, `i` is 0 |

</div>
</div>

---
layout: prism
heading: Numeric Type Conversions
---

<div style="margin-bottom: 0.4rem;">

- C++ can convert a value from one type to another explicitly with a [casting]{.hl} operator: `static_cast<type>(value)`. Casting from a smaller range to a larger one is [widening]{.hl}; from a larger range to a smaller one is [narrowing]{.hl}.

</div>

<CppRunner>

```cpp
#include <iostream>
using namespace std;

int main()
{
    int i = 34.7;      // narrowing: i becomes 34
    double f = i;      // widening: f is now 34
    double g = 34.3;   // g becomes 34.3
    int j = g;         // narrowing: j is now 34

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
heading: "Do It Yourself! (1/2) — Mad Lib"
---

<div style="margin-bottom: 0.4rem;">

- Prompt the user for adjectives and nouns, then insert them into a premade story template.

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
heading: "Do It Yourself! (2/2) — Base Conversion"
---

<div style="margin-bottom: 0.4rem;">

- Read a decimal number and print its base-2 (binary), base-3 (ternary), …, base-9 (nonary) representations.

</div>

<CppRunner stdin="24">

```cpp
#include <iostream>
#include <string>
using namespace std;

// Convert a nonnegative integer to the given base (2..9)
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

# ***Thank you!***
<br></br>

_Contact:_ [wjko@sungshin.ac.kr](mailto:wjko@sungshin.ac.kr){style="color:#c2410c; font-family: 'JetBrains Mono', Consolas, monospace;"}

_Website:_ [https://sswu-prism-lab.github.io/](https://sswu-prism-lab.github.io/){style="background: linear-gradient(90deg, rgb(188,90,93), rgb(242,221,134), rgb(111,142,114), rgb(75,85,210), rgb(119,94,145)); -webkit-background-clip: text; background-clip: text; color: transparent; -webkit-text-fill-color: transparent; text-decoration: underline; font-family: 'JetBrains Mono', Consolas, monospace;"}
