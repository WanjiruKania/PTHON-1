# ENCAPSULATION

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

        def get_balance(self):
            return self.__balance

            def deposit(self, amount):
                self.__balance+= amount

acct = BankAccount(1000)
print(acct.get_balance())
acct.deposit(100)