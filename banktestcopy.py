class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.01, 1000)

    def make_deposit(self, amount):
        self.account.deposit (amount)

    def make_withdrawal(self, amount):
        self.account.withdraw (amount)

    def display_user_balance(self):
        self.account.display_account_info()

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        (other_user).account.balance += amount
        print (str(amount))




class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = 0.01
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    def display_account_info(self):
        print('Balance:' + str(+self.balance))

    def yield_interest(self):
        if (self.balance>0):
            self.balance = self.balance + (self.balance* 0.01)


guido = User('Guido', 'mcleocrel@gmail.com')
guida = User('Guida', 'guidinha@gmail.com')

guido.transfer_money(guida,100)
guido.display_user_balance()
guida.display_user_balance()