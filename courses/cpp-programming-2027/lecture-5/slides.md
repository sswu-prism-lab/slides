---
theme: seriph
themeConfig:
  primary: '#5c60a8'
background: '#ffffff'
title: CPP - Lecture 5
download: true
info: |
  ## C++ Programming Lecture Slides
  Pattern Recognition and Intelligent System Modeling Lab, Sungshin Women's University
class: text-center
transition: slide-left
mdc: true
otherLangUrl: /slides/cpp-programming-2027/lecture-5-ko/
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
  <p style="color:#9aa0a6; font-size: 1.5rem; margin-top: 0.25rem;">Week 05: Strings, Formatting, and File I/O</p>

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
heading: "Recap: switch Statements"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [`switch`]{.hl} statement selects among many cases based on the value of a single expression; each `case` ends with `break`, and `default` handles all other values.

<div style="height: 1rem;"></div>

```cpp
switch (switch-expression) {
    case value1: statement(s)1;
                 break;
    case value2: statement(s)2;
                 break;
    // ...
    case valueN: statement(s)N;
                 break;
    default:     statement(s)-for-default;
}
```

---
layout: prism
heading: "Recap: Conditional Expressions"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1.5rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- The [ternary operator]{.hl} `? :` forms a conditional expression: `boolean-expression ? expression1 : expression2`.

- It uses *three* operands and is the only ternary operator in C++.

- The two snippets on the right are equivalent.

</div>
<div>

<div style="height: 2rem;"></div>

```cpp
if (x > 0)
    y = 1;
else
    y = -1;

// equivalent conditional expression
y = x > 0 ? 1 : -1;
```

</div>
</div>

---
layout: prism
heading: "Recap: Mathematical Functions"
---

<style>
.slidev-layout ul > li {
  margin-top: 0.8em;
}
</style>

- `min`, `max`, and `abs` are defined in the [`cstdlib`]{.hl} header; the trigonometric, exponent, and rounding functions are in the [`cmath`]{.hl} header.

<div class="grid grid-cols-2 gap-6" style="margin-top: 1rem;">
<div>

| `cmath` function | Description |
|---|---|
| `sin/cos/tan(r)` | trig. of an angle in radians |
| `asin/acos/atan(a)` | inverse trig., result in radians |
| `exp(x)` | $e^x$ |
| `log(x)` / `log10(x)` | natural / base-10 logarithm |
| `pow(a, b)` | $a^b$ |
| `sqrt(x)` | square root, $x \geq 0$ |

</div>
<div>

| Rounding | Description |
|---|---|
| `ceil(x)` | round *up* to nearest integer (as `double`) |
| `floor(x)` | round *down* to nearest integer (as `double`) |

</div>
</div>

---
layout: prism
heading: "Recap: Character"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- Most computers use [ASCII]{.hl}, an 8-bit encoding for letters, digits, punctuation, and control characters. A `char` is 1 byte.

```cpp
char ch = 'a';
cout << ++ch; // 'b'
```

</div>
<div>

| Function | Returns `true` if the char is … |
|---|---|
| `isdigit(ch)` | a digit |
| `isalpha(ch)` | a letter |
| `isalnum(ch)` | a letter or digit |
| `islower(ch)` | a lowercase letter |
| `isupper(ch)` | an uppercase letter |
| `isspace(ch)` | a whitespace character |
| `tolower(ch)` | *returns* the lowercase form |
| `toupper(ch)` | *returns* the uppercase form |

</div>
</div>

---
layout: prism
heading: "DIY_W04: Base-20 Digit Converter"
---

- Read a single base-20 digit and convert it to decimal. If a lowercase letter is entered, warn that it was auto-converted to uppercase. (Digits `0`–`9` map to `0`–`9`; letters `A`–`J` map to `10`–`19`.)

<CppRunner stdin="A">

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    // Input a base-20 digit.
    cout << "한 자리 20진수를 입력하세요: ";
    char inputNum;
    cin >> inputNum;

    /* The input digit should be a digit or a letter between
       a ~ j or A ~ J. */
    if (isdigit(inputNum)
        || (toupper(inputNum) >= 65 && toupper(inputNum) < 75)) {
        if (isdigit(inputNum)) {
            cout << "입력한 20진수 " << inputNum << "은/는 10진수 "
                 << inputNum << "입니다.";
        }
        else if (islower(inputNum)) {
            cout << "입력한 알파벳 " << inputNum << "은/는 "
                 << static_cast<char>(toupper(inputNum))
                 << "으로 자동으로 변환되었습니다." << endl;
            cout << static_cast<char>(toupper(inputNum))
                 << "은/는 10진수 " << static_cast<int>(toupper(inputNum)) - 55
                 << "입니다.";
        }
        else {
            cout << "입력한 20진수 " << inputNum
                 << "은/는 10진수 " << static_cast<int>(inputNum) - 55 << "입니다.";
        }
    }
    else {
        cout << "입력 20진수에 오류가 있습니다.";
    }
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "The string Type (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- A [string]{.hl} is a *sequence* of characters, whereas a `char` represents only one character.

- To represent a string of characters we use the data type [`string`]{.hl}.

```cpp
string message = "Programming is fun";
```

- `string` is not a primitive type but an [object type]{.hl}: `message` is a string object with the contents `Programming is fun`.

- `string` is a predefined class in the `<string>` header — `#include <string>`.

---
layout: prism
heading: "The string Type (2/2)"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 1rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The functions of the `string` class are invoked from a specific string instance — they are [instance functions]{.hl}.

```cpp
string message = "Sungshin";
// check the length of the string
// find the third character of the string
```

</div>
<div>

<div style="height: 1.5rem;"></div>

| Function | Description |
|---|---|
| `length()` | number of characters in the string |
| `size()` | same as `length()` |
| `at(index)` | the character at the specified index |

</div>
</div>

---
layout: prism
heading: "String Index and Subscript Operator"
---

- `s.at(index)` retrieves a character in string `s`, where `index` is between `0` and `s.length() - 1`. For convenience, C++ also provides the [subscript operator]{.hl} `stringName[index]`.

<div style="display:flex; justify-content:center; margin: 1.2rem 0;">
<table style="border-collapse: collapse; font-family: 'JetBrains Mono', Consolas, monospace; font-size: 0.9rem;">
<tr>
  <td style="border:none; padding:2px 6px;">Indices</td>
  <td style="border:1px solid #888; padding:2px 8px;">0</td><td style="border:1px solid #888; padding:2px 8px;">1</td><td style="border:1px solid #888; padding:2px 8px;">2</td><td style="border:1px solid #888; padding:2px 8px;">3</td><td style="border:1px solid #888; padding:2px 8px;">4</td><td style="border:1px solid #888; padding:2px 8px;">5</td><td style="border:1px solid #888; padding:2px 8px;">6</td><td style="border:1px solid #888; padding:2px 8px;">7</td><td style="border:1px solid #888; padding:2px 8px;">8</td><td style="border:1px solid #888; padding:2px 8px;">9</td><td style="border:1px solid #888; padding:2px 8px;">10</td><td style="border:1px solid #888; padding:2px 8px;">11</td><td style="border:1px solid #888; padding:2px 8px;">12</td><td style="border:1px solid #888; padding:2px 8px;">13</td>
</tr>
<tr>
  <td style="border:none; padding:2px 6px;">message</td>
  <td style="border:1px solid #888; padding:2px 8px;">W</td><td style="border:1px solid #888; padding:2px 8px;">e</td><td style="border:1px solid #888; padding:2px 8px;">l</td><td style="border:1px solid #888; padding:2px 8px;">c</td><td style="border:1px solid #888; padding:2px 8px;">o</td><td style="border:1px solid #888; padding:2px 8px;">m</td><td style="border:1px solid #888; padding:2px 8px;">e</td><td style="border:1px solid #888; padding:2px 8px;">&nbsp;</td><td style="border:1px solid #888; padding:2px 8px;">t</td><td style="border:1px solid #888; padding:2px 8px;">o</td><td style="border:1px solid #888; padding:2px 8px;">&nbsp;</td><td style="border:1px solid #888; padding:2px 8px;">C</td><td style="border:1px solid #888; padding:2px 8px;">+</td><td style="border:1px solid #888; padding:2px 8px;">+</td>
</tr>
</table>
</div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string message = "Welcome to C++";
    cout << "length = " << message.length() << endl; // 14
    cout << "at(0)  = " << message.at(0) << endl;     // W
    cout << "at(13) = " << message.at(13) << endl;    // +

    string s = message;
    s[0] = 'P';                      // subscript operator (write)
    cout << "s[0]   = " << s[0] << endl; // P
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Concatenating Strings"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- C++ provides `+` for [concatenating]{.hl} two strings, and the augmented `+=` operator also concatenates.

- It is *illegal* to concatenate two string literals:

```cpp
string cities = "London" + "Paris"; // error
```

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1 = "Welcome ", s2 = "to C++";
    string s3 = s1 + s2;          // + operator
    cout << s3 << endl;

    string message = "Welcome to C++";
    message += " and programming is fun"; // += operator
    cout << message << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Comparing Strings"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The relational operators `==`, `!=`, `<`, `<=`, `>`, `>=` compare two strings.

- Comparison proceeds by their corresponding characters, [one by one from left to right]{.hl}.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1 = "ABC";
    string s2 = "ABE";
    cout << (s1 == s2) << endl; // 0 (false)
    cout << (s1 != s2) << endl; // 1 (true)
    cout << (s1 >  s2) << endl; // 0 (false)
    cout << (s1 >= s2) << endl; // 0 (false)
    cout << (s1 <  s2) << endl; // 1 (true)
    cout << (s1 <= s2) << endl; // 1 (true)
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Reading Strings"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- A string can be read from the keyboard with `cin`, but `cin >> s` stops at the first *whitespace* — so `New York` cannot be read as one string.

```cpp
string city;
cin >> city; // reads only up to the first space
```

- C++ provides [`getline`]{.hl} in the `<string>` header for reading a whole line:

```cpp
getline(cin, s, delimitCharacter)
```

- The [delimiter]{.hl} (구분 문자) is read but *not* stored in the string. The third argument `delimitCharacter` has a default of `'\n'`, so `getline(cin, city);` reads a full line.

---
layout: prism
heading: "Practice: Order Two Cities"
---

Read two city names (each possibly containing spaces) with `getline`, then print them in alphabetical order.

<CppRunner stdin="Seoul
Busan">

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string city1, city2;
    cout << "Enter the first city: ";
    getline(cin, city1);
    cout << "Enter the second city: ";
    getline(cin, city2);

    cout << "The cities in alphabetical order are ";
    if (city1 < city2)
        cout << city1 << " " << city2 << endl;
    else
        cout << city2 << " " << city1 << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Practice: Lottery Program (1/2)"
---

<style>
.slidev-layout ul > li {
  margin-top: 1em;
}
</style>

- The lottery program generates a random two-digit number, prompts the user for a two-digit number, and determines whether the user wins.

- The award [rules]{.hl}:
  - exact-order match of the lottery number → **$10,000**
  - all digits match (any order) → **$3,000**
  - one digit matches → **$1,000**

```cpp
#include <iostream>
#include <string>   // for using strings
#include <ctime>    // for time function
#include <cstdlib>  // for rand and srand functions
using namespace std;
```

---
layout: prism
heading: "Practice: Lottery Program (2/2)"
---

<div style="height: 0.2rem;"></div>

<CppRunner stdin="36">

```cpp
#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
using namespace std;

int main() {
    string lottery;
    srand(1); // fixed seed for a reproducible run (was srand(time(0)))
    int digit = rand() % 10;                    // Generate first digit
    lottery += static_cast<char>(digit + '0');
    digit = rand() % 10;                        // Generate second digit
    lottery += static_cast<char>(digit + '0');

    // Prompt the user to enter a guess
    cout << "Enter your lottery pick (two digits): ";
    string guess;
    cin >> guess;

    cout << "The lottery number is " << lottery << endl;

    // Check the guess
    if (guess == lottery)
        cout << "Exact match: you win $10,000" << endl;
    else if (guess[1] == lottery[0] && guess[0] == lottery[1])
        cout << "Match all digits: you win $3,000" << endl;
    else if (guess[0] == lottery[0] || guess[0] == lottery[1]
             || guess[1] == lottery[0] || guess[1] == lottery[1])
        cout << "Match one digit: you win $1,000" << endl;
    else
        cout << "Sorry, no match" << endl;

    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Formatting Console Output"
---

<style>
.slidev-layout ul > li {
  margin-top: 2.2em;
}
</style>

- We can use [stream manipulators]{.hl} (스트림 조정자) to display formatted output on the console.

- C++ provides functions for formatting how a value is displayed; these are the stream manipulators, included in the [`iomanip`]{.hl} header file.

```cpp
#include <iomanip>
```

---
layout: prism
heading: "setprecision(n) Manipulator"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- [`setprecision(n)`]{.hl} specifies the total number of digits displayed for a floating-point number.

- It remains in effect until the precision is changed again.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double number = 12.34567;
    cout << setprecision(3) << number << " "
         << setprecision(4) << number << " "
         << setprecision(5) << number << " "
         << setprecision(6) << number << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "fixed Manipulator"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- A large floating-point number is displayed in *scientific notation* by default (e.g. `2.32123e+08`).

- The [`fixed`]{.hl} manipulator forces nonscientific notation with 6 digits after the decimal point, and combines with `setprecision` to change that count.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << 232123434.357 << endl;         // 2.32123e+08
    cout << fixed << 232123434.357 << endl; // 232123434.357000

    double monthlyPayment = 345.4567;
    double totalPayment = 78676.887234;
    cout << setprecision(2)
         << monthlyPayment << endl
         << totalPayment << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "showpoint Manipulator"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- The [`showpoint`]{.hl} manipulator, together with `setprecision`, displays a fixed number of digits after the decimal point — trailing zeros are kept.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << setprecision(6);
    cout << 1.23 << endl;              // 1.23
    cout << showpoint << 1.23 << endl; // 1.23000
    cout << showpoint << 123.0 << endl;// 123.000
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "setw(width) Manipulator"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.1em;
}
</style>

- By default `cout` uses just as many positions as needed. [`setw(width)`]{.hl} specifies the *minimum* number of columns for the next output only.

- If an item needs more space than `width`, the width is automatically increased.

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << setw(8) << "C++"  << setw(6) << 101 << endl;
    cout << setw(8) << "Java" << setw(6) << 101 << endl;
    cout << setw(8) << "HTML" << setw(6) << 101 << endl;
    // width too small -> automatically increased
    cout << setw(8) << "Programming" << "#" << setw(2) << 101 << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "left and right Manipulators"
---

<div class="grid grid-cols-2 gap-4" style="margin-top: 0.8rem;">
<div>

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- `setw` uses [right]{.hl} justification by default.

- The [`left`]{.hl} manipulator left-justifies the output; the [`right`]{.hl} manipulator right-justifies it. (The `|` marks the field edges below.)

</div>
<div>

<CppRunner>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << right;
    cout << "|" << setw(8) << 1.23   << "|" << endl;
    cout << "|" << setw(8) << 351.34 << "|" << endl;

    cout << left;
    cout << "|" << setw(8) << 1.23   << "|" << endl;
    cout << "|" << setw(8) << 351.34 << "|" << endl;
    return 0;
}
```

</CppRunner>

</div>
</div>

---
layout: prism
heading: "Writing to a File"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.2em;
}
</style>

- To write data to a file, include the [`<fstream>`]{.hl} header and declare a variable of the [`ofstream`]{.hl} type.

```cpp
#include <fstream>
ofstream output;
```

- Invoke `open` to specify a file — this creates the file in the current directory; if it already exists, its contents are destroyed and a new file is created.

```cpp
output.open("numbers.txt");
```

- When done, invoke `close`:

```cpp
output.close();
```

---
layout: prism
heading: "Practice: Simple File Output"
---

The program writes three numbers to `numbers.txt`, then reads them back so the result is visible in the sandbox.

<CppRunner>

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream output;
    output.open("numbers.txt");             // Create a file
    output << 95 << " " << 56 << " " << 34; // Write numbers
    output.close();                         // close file
    cout << "Done" << endl;

    // Read it back so the output is visible in the sandbox
    ifstream input("numbers.txt");
    int a, b, c;
    input >> a >> b >> c;
    input.close();
    cout << "File contents: " << a << " " << b << " " << c << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "Reading from a File"
---

<style>
.slidev-layout ul > li {
  margin-top: 1.4em;
}
</style>

- To read data from a file, declare a variable of the [`ifstream`]{.hl} type and open a file:

```cpp
ifstream input;
input.open("numbers.txt");
```

- We can also create the file input object and open the file in a single statement:

```cpp
ifstream input("numbers.txt");
```

---
layout: prism
heading: "Practice: Simple File Input"
---

To make the example self-contained, we first create `numbers.txt`, then read the three scores back and sum them.

<CppRunner>

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    // First create numbers.txt so there is something to read
    ofstream output("numbers.txt");
    output << 95 << " " << 56 << " " << 34;
    output.close();

    ifstream input;
    input.open("numbers.txt");   // Open a file
    int score1, score2, score3;
    input >> score1;             // Read data
    input >> score2;
    input >> score3;

    cout << "Total score is " << score1 + score2 + score3 << endl;
    input.close();               // Close file
    cout << "Done" << endl;
    return 0;
}
```

</CppRunner>

---
layout: prism
heading: "HW_W05: Random City Name"
---

Generate a random 6-letter "city" (1 uppercase + 5 lowercase), then print it in alphabetical order with a city name entered by the user. Save as `HW_W05_20XXXXXX.cpp` and upload to the LMS.

<CppRunner stdin="Seoul">

```cpp
#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int main() {
    srand(1); // fixed seed for a reproducible run

    // 1 uppercase letter + 5 lowercase letters
    string generated;
    generated += static_cast<char>('A' + rand() % 26);
    for (int i = 0; i < 5; i++)
        generated += static_cast<char>('a' + rand() % 26);

    cout << "Input a city name: ";
    string city;
    getline(cin, city);

    cout << "The randomly generated city name is \"" << generated << "\"" << endl;
    cout << "The cities in alphabetical order are ";
    if (city < generated)
        cout << "\"" << city << "\" and \"" << generated << "\"" << endl;
    else
        cout << "\"" << generated << "\" and \"" << city << "\"" << endl;

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
