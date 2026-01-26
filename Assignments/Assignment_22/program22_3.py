# Write a Python program to implement a class named Arithmetic with the following characteristics:
'''
The class should contain two instance variables: Valuel and Value2.

Define a constructor (__init__) that initializes all instance variables to 0.

Implement the following instance methods:

    Accept()-accepts values for Valuel and Value2 from the user.

    Addition() - returns the addition of Valuel and Value2.

    Subtraction () returns the subtraction of Valuel and Value2.

    Multiplication() - returns the multiplication of Valuel and Value2.

    Division() returns the division of Valuel and Value 2 (handle division by zero properly).

Create multiple objects of the Arithmetic class and invoke all the instance methods.
'''

class Arithematic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter first number :")
        self.Value1 = int(input())

        print("Enter second number :")
        self.Value2 = int(input())    

    def Addition(self):
        return self.Value1 + self.Value2
        
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 == 0:
            print("Cannot divide by zero.")
            return 

        return self.Value1 + self.Value2

def main():
    Ret = 0.0

    Obj1 = Arithematic()

    Obj1.Accept()

    Ret = Obj1.Addition()
    print("Addition :", Ret)

    Ret = Obj1.Substraction()
    print("Substraction :", Ret)

    Ret = Obj1.Multiplication()
    print("Multiplication :", Ret)

    Ret = Obj1.Division()
    print("Division :", Ret)

if __name__ == "__main__":
    main()