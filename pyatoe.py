class BankAccount:
    def __init__(self):
        self.__balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнено: {amount}. Текущий баланс: {self.__balance}.")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Ошибка: недостаточно средств на счете.")
        elif amount > 0:
            self.__balance -= amount
            print(f"Снято: {amount}. Текущий баланс: {self.__balance}.")
        else:
            print("Сумма снятия должна быть положительной.")

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
account.withdraw(30)
account.withdraw(80)
print(f"Текущий баланс: {account.get_balance()}")
