# Design a Python application that creates three threads named Small, Capital, and Digits.
'''
All threads should accept a string as input.

The Small thread should count and display the number of lowercase characters.

The Capital thread should count and display the number of uppercase characters.

The Digits thread should count and display the number of numeric digits.

Each thread must also display:

    1. Thread ID

    2. Thread Name
'''

###########################################################################
#
#   Import Built-in Modules
#
###########################################################################

import os
import threading
import time

###########################################################################
#
# Function Name :   DisplayEven
# Description   :   display the first 10 even numbers
# Input         :   None
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def Small(Str):
    print("TID :", threading.get_ident())

    Count = 0

    print("Length of string :", len(Str))

    for i in range(len(Str)):
        if Str[i] >= 'a' and Str[i] <= 'z':
            print(Str[i], end = "\t")
            Count += 1
    print()

    print("Count of Small letters :", Count)
    


###########################################################################
#
# Function Name :   DisplayOdd
# Description   :   display the first 10 odd numbers
# Input         :   None
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def Capital(Str):
    print("TID :", threading.get_ident())

    Count = 0

    print("Length of string :", len(Str))

    for i in range(len(Str)):
        if Str[i] >= 'A' and Str[i] <= 'Z':
            print(Str[i], end = "\t")
            Count += 1
    print()

    print("Count of Capital letters :", Count)

###########################################################################
#
#   Main Method
#
###########################################################################

def main():
    print("PID of main :", os.getpid())
    print("PPID of main :", os.getppid())

    print("Enter the String :")
    Val = input()

    start_time = time.time()

    t1 = threading.Thread(target = Small, args = (Val,))
    t2 = threading.Thread(target = Capital, args = (Val,))

    end_time = time.time()

    print("Thread name :", t1.name)
    print("Thread name :", t2.name)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Execution time :", end_time - start_time)

###########################################################################
#
#   Starter for main method
#
###########################################################################

if __name__ == "__main__":
    main()