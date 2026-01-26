# Design a Python application that creates two threads.
'''
Thread 1 should compute the sum of elements from a list.

Thread 2 should compute the product of elements from the same list.

Return the results to the main thread and display them.
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
# Function Name :   SumElement
# Description   :   compute the sum of elements from a list.
# Input         :   list
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def SumElement(Lst):
    print("TID :", threading.get_ident())

    sum = 0

    for i in Lst:
        sum += i

    print("sum of elements", sum)

###########################################################################
#
# Function Name :   ProductElement
# Description   :   compute the product of elements from a list.
# Input         :   list
# Output        :   int
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def ProductElement(Lst):
    print("TID :", threading.get_ident())
    
    product = 1

    for i in Lst:
        product *= i

    print("Product of elements", product)

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

    t1 = threading.Thread(target = SumElement, args = (Data,))
    

    t2 = threading.Thread(target = ProductElement, args = (Data, ))

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