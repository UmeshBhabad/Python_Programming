# Write a Python program to implement a class named BankAccount with the following requirements:
'''
The class should contain two instance variables:

    Name (Account holder name)

    Amount (Account balance)

The class should contain one class variable:

    ROI (Rate of Interest), initialized to 10.5

Define a constructor (__init__) that accepts Name and initial Amount.

Implement the following instance methods:

    Display() - displays account holder name and current balance

    Deposit()- accepts an amount from the user and adds it to balance

    Withdraw() - accepts an amount from the user and subtracts it from balance (Ensure withdrawal is allowed only if sufficient balance exists)

    CalculateInterest() - calculates and returns interest using formula:

    Interest = (Amount * ROI) / 100

Create multiple objects and demonstrate all methods.
'''

class BankAccount:
    ROI = 10.5

    def __init__(self, name, balance):
        self.Name = name
        self.Amount = balance
    
    def Display(self):
        print(f"Account holder name : {self.Name}.")
        print(f"Current Account balance : {self.Amount}")

    def Deposit(self, amount):
        self.Amount += amount

    def Withdraw(self, amount):
        if self.Amount < amount:
            print("Insufficient Balance")
            return
        self.Amount -= amount

    def CalculateInterest(self):
        Interest = 0

        Interest = (self.Amount * BankAccount.ROI) / 100

        return Interest

def main():
    Ret = 0

    Obj1 = BankAccount("Umesh Shivaji Bhabad", 1000)

    Obj1.Display()
    Obj1.Deposit(500)
    Obj1.Display()
    Obj1.Withdraw(800)
    Obj1.Display()
    Ret = Obj1.CalculateInterest()
    print("Interest :",Ret)

    Obj2 = BankAccount("Ishant Suryawanshi", 2000)

    Obj2.Display()
    Obj2.Deposit(1000)
    Obj2.Display()
    Obj2.Withdraw(400)
    Obj2.Display()
    Ret = Obj2.CalculateInterest()
    print("Interest :",Ret)

if __name__ == "__main__":
    main()