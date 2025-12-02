from random import randrange
from typing import List

class BankAccount:
    """
    Bank account management.
    """
    all_account_numbers: List[int] = []
    last_account_number = 999

    def __init__(self, name: str) -> None:
        BankAccount.last_account_number += 1
        an = BankAccount.last_account_number
        self.account_number: int = an
        BankAccount.all_account_numbers.append(an)
        self.name = name
        self.balance : float = 0

    def display(self) -> None:
        """
        Show account balance.
        :return:
        """
        print(40 * "_")
        print(f"Hi, {self.name}\nYour current balance: {self.balance}")
        print(40 * "_")

    def deposit(self) -> None:
        """
        Increase account balance.
        :return:
        """
        amount = float(input("Please enter amount to deposit: "))
        self.balance += amount
        self.display()

    def withdraw(self) -> None:
        """
        Withdraw from bank account.
        :return:
        """
        amount = float(input("Please enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
        self.display()
def main():
    acc1 = BankAccount("Ghafar Mohammadi")
    print(f"accunt_number: {acc1.account_number}")
    acc1.display()

    while True:
        choice = int(input("Enter:\n1 to see your balance\n2 to deposit\n3 to witdraw\n4 to exit\n\t your choice: "))

        if choice == 1:
            acc1.display()
        elif choice == 2:
            acc1.deposit()
        elif choice == 3:
            acc1.withdraw()
        elif choice == 4:
            break
        else:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
#----------------------------------
print(40 * "*")

ac1 = BankAccount("A")
print(ac1.all_account_numbers)
ac2 = BankAccount("B")
print(ac2.all_account_numbers)
ac3 = BankAccount("C")
print(ac3.all_account_numbers)

print("account number 1: ", ac1.account_number)
print("account number 2: ", ac2.account_number)
print("account number 3: ", ac3.account_number)