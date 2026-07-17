# 문제 15 · `BankAccount` UML 클래스 다이어그램

::: info 문제 15 [5점]
아래 클래스 코드를 Unified Modeling Language (UML) 클래스 다이어그램을 이용하여 표현한 후, 각 데이터 필드 및 함수에 대해 간단히 설명하시오.

**BankAccount.h**

```cpp
#include <string>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    string accountHolder;
    double balance;
    static double annualInterestRate;

public:
    BankAccount(string accountNumber, string accountHolder, double balance);

    void deposit(double amount);
    void withdraw(double amount);
    void addInterest();

    string getAccountNumber() const;
    void setAccountNumber(string accountNumber);
    string getAccountHolder() const;
    void setAccountHolder(string accountholder);
    double getBalance() const;
    void setBalance(double balance);
    static double getAnnualInterestRate();
    static void setAnnualInterestRate(double interestRate);
};
```

**BankAccount.cpp**

```cpp
#include "BankAccount.h"

double BankAccount::annualInterestRate = 0.05;

BankAccount::BankAccount(string accountNumber, string accountHolder, double balance) {
    this -> accountNumber = accountNumber;
    this -> accountHolder = accountHolder;
    this -> balance = balance;
}

void BankAccount::deposit(double amount) {
    if (amount > 0)
        balance += amount;
}

void BankAccount::withdraw(double amount) {
    if (amount > 0 && balance >= amount)
        balance -= amount;
}

void BankAccount::addInterest() {
    balance += balance * annualInterestRate;
}

// getter / setter (생략) ...
```
:::

::: details 풀이 및 해설
UML 클래스 다이어그램은 **클래스 이름 / 데이터 필드(속성) / 함수(연산)** 의 3칸으로 그립니다. 접근 지정자는 `-`(private), `+`(public)로, **정적 멤버는 밑줄(또는 `{static}`)** 로 표시하며, 형식은 `이름 : 타입` 순으로 씁니다.

```
┌─────────────────────────────────────────────────────────┐
│                       BankAccount                        │
├─────────────────────────────────────────────────────────┤
│ - accountNumber : string                                 │
│ - accountHolder : string                                 │
│ - balance : double                                       │
│ - annualInterestRate : double   {static}                 │
├─────────────────────────────────────────────────────────┤
│ + BankAccount(accountNumber : string,                    │
│               accountHolder : string,                    │
│               balance : double)                          │
│ + deposit(amount : double) : void                        │
│ + withdraw(amount : double) : void                       │
│ + addInterest() : void                                   │
│ + getAccountNumber() : string   {const}                  │
│ + setAccountNumber(accountNumber : string) : void        │
│ + getAccountHolder() : string   {const}                  │
│ + setAccountHolder(accountholder : string) : void        │
│ + getBalance() : double   {const}                        │
│ + setBalance(balance : double) : void                    │
│ + getAnnualInterestRate() : double   {static}            │
│ + setAnnualInterestRate(interestRate : double) : void   {static} │
└─────────────────────────────────────────────────────────┘
```

**데이터 필드(모두 `private`)**

| 필드 | 타입 | 설명 |
| --- | --- | --- |
| `accountNumber` | `string` | 계좌 번호 |
| `accountHolder` | `string` | 예금주 이름 |
| `balance` | `double` | 현재 잔액 |
| `annualInterestRate` | `static double` | 연이율. 모든 계좌가 공유하는 정적 멤버(`0.05`로 초기화) |

**함수(모두 `public`)**

| 함수 | 설명 |
| --- | --- |
| `BankAccount(...)` | 생성자. 계좌 번호·예금주·초기 잔액을 받아 필드를 설정 |
| `deposit(amount)` | 입금. 금액이 양수일 때만 잔액에 더함 |
| `withdraw(amount)` | 출금. 금액이 양수이고 잔액이 충분할 때만 잔액에서 뺌 |
| `addInterest()` | 잔액에 `연이율`만큼 이자를 더함 (`balance += balance * annualInterestRate`) |
| `getAccountNumber() const` | 계좌 번호 반환 (상수 함수) |
| `setAccountNumber(...)` | 계좌 번호 변경 |
| `getAccountHolder() const` | 예금주 반환 (상수 함수) |
| `setAccountHolder(...)` | 예금주 변경 |
| `getBalance() const` | 잔액 반환 (상수 함수) |
| `setBalance(...)` | 잔액 변경 |
| `getAnnualInterestRate()` | 연이율 반환 (정적 함수) |
| `setAnnualInterestRate(...)` | 연이율 변경 (정적 함수) |

`get`/`set` 함수는 `private` 필드를 외부에서 안전하게 읽고 쓰게 하는 **접근자(getter)·설정자(setter)** 이며, 값을 바꾸지 않는 `get` 함수들은 `const`로, 특정 객체가 아닌 클래스 전체에 관한 `annualInterestRate` 관련 함수는 `static`으로 선언되어 있습니다.

👉 [실습(C++)에서 확인하기](./lab-15)
:::
