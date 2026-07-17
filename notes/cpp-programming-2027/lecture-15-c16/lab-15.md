# 문제 15 · 실습 — `BankAccount` 클래스 구현과 데모

UML로 표현한 `BankAccount` 클래스를 실제로 구현하고, 입금·출금·이자 적용을 시연합니다.

<CppRunner>

```cpp
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    string accountNumber;
    string accountHolder;
    double balance;
    static double annualInterestRate;   // 모든 계좌가 공유하는 연이율

public:
    BankAccount(string accountNumber, string accountHolder, double balance) {
        this->accountNumber = accountNumber;
        this->accountHolder = accountHolder;
        this->balance = balance;
    }
    void deposit(double amount)  { if (amount > 0) balance += amount; }
    void withdraw(double amount) { if (amount > 0 && balance >= amount) balance -= amount; }
    void addInterest()           { balance += balance * annualInterestRate; }

    string getAccountHolder() const { return accountHolder; }
    double getBalance() const       { return balance; }
    static double getAnnualInterestRate()       { return annualInterestRate; }
    static void setAnnualInterestRate(double r) { annualInterestRate = r; }
};

double BankAccount::annualInterestRate = 0.05;   // 정적 멤버 정의·초기화

int main() {
    BankAccount acc("123-456", "홍길동", 1000.0);
    cout << acc.getAccountHolder() << " 초기 잔액: " << acc.getBalance() << endl;

    acc.deposit(500);
    cout << "500 입금 후 잔액 : " << acc.getBalance() << endl;

    acc.withdraw(200);
    cout << "200 출금 후 잔액 : " << acc.getBalance() << endl;

    cout << "연이율 : " << BankAccount::getAnnualInterestRate() * 100 << "%" << endl;
    acc.addInterest();
    cout << "이자 적용 후 잔액: " << acc.getBalance() << endl;
    return 0;
}
```

</CppRunner>

출력은 다음과 같습니다. 잔액은 `1000 → 1500 → 1300 → 1300 × 1.05 = 1365`로 변합니다.

```
홍길동 초기 잔액: 1000
500 입금 후 잔액 : 1500
200 출금 후 잔액 : 1300
연이율 : 5%
이자 적용 후 잔액: 1365
```

👉 [문제 15로 돌아가기](./problem-15)
