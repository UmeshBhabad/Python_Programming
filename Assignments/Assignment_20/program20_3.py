# Design a Python application that creates two threads named EvenList and OddList.
'''
Both threads should accept a list of integers as input.

The EvenList thread should:

Extract all even elements from the list.

Calculate and display their sum.

The OddList thread should:

Extract all odd elements from the list.

Calculate and display their sum.

Threads should run concurrently.
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
# Function Name :   EvenList
# Description   :   display the sum of even elements
# Input         :   None
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def EvenList(Lst):
    print("TID :", threading.get_ident())
    
    sum = 0

    for i in Lst:
        if i % 2 == 0:
            sum += i

    print("sum of even elements :", sum)

###########################################################################
#
# Function Name :   OddList
# Description   :   display the sum of odd elements
# Input         :   None
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def OddList(Lst):
    print("TID :", threading.get_ident())
    
    sum = 0

    for i in Lst:
        if i % 2 == 1:
            sum += i

    print("sum of odd elements :", sum)

###########################################################################
#
#   Main Method
#
###########################################################################

def main():
    print("PID of main :", os.getpid())
    print("PPID of main :", os.getppid())

    Data = list()

    print("Enter the number of elements :")
    Length = int(input())

    print("Enter elements :")
    for _ in range(Length):
        Val = int(input())

        Data.append(Val)

    print("Elements :")
    print(Data)

    start_time = time.time()

    t1 = threading.Thread(target = EvenList, args = (Data,))
    t2 = threading.Thread(target = OddList, args = (Data,))

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