"""PROGRAM:01"""

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print("The car is starting.")

car1 = Car("Tesla", "White")

car1.start()



"""PROGRAM:02"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Alchemist", "Paulo Coelho")
book3 = Book("The Art of letting go", "Nick.Trenton")

book1.display_info()
book2.display_info()
book3.display_info()



"""PROGRAM:03"""

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        print("Addition:", self.num1 + self.num2)

    def subtraction(self):
        print("Subtraction:", self.num1 - self.num2)

    def multiplication(self):
        print("Multiplication:", self.num1 * self.num2)

    def division(self):
        print("Division:", self.num1 / self.num2)

calc = Calculator(40,20)

calc.addition()
calc.subtraction()
calc.multiplication()
calc.division()



"""PROGRAM:04"""

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Amount withdrawn:", amount)

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

account1 = BankAccount("Heer", 10000)

account1.deposit(2000)
account1.withdraw(1000)
account1.display_balance()