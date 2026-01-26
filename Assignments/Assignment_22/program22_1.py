# Write a Python program to implement a class named Demo with the following specifications:
'''
The class should contain two instance variables: nol and no2.

The class should contain one class variable named Value.

Define a constructor (__init__) that accepts two parameters and initializes the instance variables.

Implement two instance methods:

    Fun()-displays the values of instance variables nol and no2.

    Gun()-displays the values of instance variables nol and no2.

Create two objects of the Demo class as follows:

    Objl = Demo (11, 21)

    Obj2 = Demo (51, 101)

Call the instance methods in the given sequence:

    Objl.Fun()

    Obj2.Fun()

    Objl.Gun()

    Obj2.Gun()
'''

class Demo:
    Value = 10

    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B

    def fun(self):
        print("Inside fun")
        print("Instance Variable No1 :", self.No1)
        print("Instance Variable No2 :", self.No2)

    def gun(self):
        print("Inside gun")
        print("Instance Variable No1 :", self.No1)
        print("Instance Variable No2 :", self.No2)

def main():
    Val1 = 0
    Val2 = 0

    print("Enter the first number :")
    Val1 = int(input())

    print("Enter the second number :")
    Val2 = int(input())
    
    Obj1 = Demo(Val1, Val2)
    Obj2 = Demo(10, 50)

    Obj1.fun()

    Obj2.fun()

    Obj1.gun()

    Obj2.gun()

if __name__ == "__main__":
    main()