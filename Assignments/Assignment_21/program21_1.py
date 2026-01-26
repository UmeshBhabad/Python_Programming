# Design a Python application that creates two threads named Prime and NonPrime.
'''
Both threads should accept a list of integers.

The Prime thread should display all prime numbers from the list.

The NonPrime thread should display all non-prime numbers from the list.
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
# Function Name :   isprime
# Description   :   used to check if the given number is prime or not
# Input         :   int
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def isPrime(No):
    for i in range(2, (No // 2) + 1):
        if No % i == 0:
            return False
    return True

###########################################################################
#
# Function Name :   prime
# Description   :   display all prime numbers from the list
# Input         :   list
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def Prime(Lst):
    print("TID :", threading.get_ident())

    bFlag = True
    Ele = []

    print("Prime elements :")
    for i in Lst:
        bFlag = isPrime(i)

        if bFlag == True:
            Ele.append(i)
    
    print(Ele)


###########################################################################
#
# Function Name :   NonPrime
# Description   :   display all non-prime numbers from the list.
# Input         :   list
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def NonPrime(Lst):
    print("TID :", threading.get_ident())
    
    bFlag = False
    Ele = []

    print("Non Prime elements :")
    for i in Lst:
        bFlag = isPrime(i)

        if bFlag == False:
            Ele.append(i)

    print(Ele)

###########################################################################
#
#   Main Method
#
###########################################################################

def main():
    print("PID of main :", os.getpid())
    print("PPID of main :", os.getppid())
    
    Data = []
    
    print("Enter the number of elements :")
    Length = int(input())

    print("Enter elements :")
    for _ in range(Length):
        Val = int(input())

        Data.append(Val)

    start_time = time.time()

    t1 = threading.Thread(target = Prime, args = (Data,))
    t2 = threading.Thread(target = NonPrime, args = (Data, ))

    end_time = time.time()

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