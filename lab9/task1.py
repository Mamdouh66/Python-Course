class Account:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance is ${self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.__balance}.")
        else:
            print("Withdrawal amount must be positive and no more than the balance.")

    def get_balance(self):
        return self.__balance

    def __del__(self):
        print(f"Account {self.name} is being deleted.")

    def display_account_details(self):
        vip_status = "(VIP)" if self.get_balance() > 10000 else ""
        print(f"Account name: {self.name}\nBalance: ${self.get_balance()} {vip_status}")


if __name__ == "__main__":
    name = input("Enter the account holder's name: ")
    account = Account(name)

    while True:
        print("\nChoose an Option:")
        print("1 - deposit")
        print("2 - withdraw")
        print("3 - Display balance")
        print("4 - Exit")
        choice = input("Option: ")

        match (choice):
            case "1":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            case "2":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            case "3":
                print(f"Current balance: ${account.get_balance()}")
            case "4":
                account.display_account_details()
                break
            case _:
                print("Invalid option, please try again.")

    del account
