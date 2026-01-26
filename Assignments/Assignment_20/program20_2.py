# Design a Python application that creates two threads named EvenFactor and OddFactor.
'''
Both threads should accept one integer number as a parameter.

The EvenFactor thread should:

Identify all even factors of the given number.

Calculate and display the sum of even factors.

The OddFactor thread should:

Identify all odd factors of the given number.

Calculate and display the sum of odd factors.

After both threads complete execution, the main thread should display the message:

"Exit from main"
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
# Function Name :   EvenFactors
# Description   :   Calculate and display the sum of even factors.
# Input         :   int
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def EvenFactors(No):
    print("TID :", threading.get_ident())

    sum = 0

    for i in range(1, (No // 2) + 1):
        if No % i == 0:
            if i % 2 == 0:
                sum += i

    print("Sum of even factors :", sum)
        

###########################################################################
#
# Function Name :   OddFactors
# Description   :   Calculate and display the sum of odd factors.
# Input         :   int
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def OddFactors(No):
    print("TID :", threading.get_ident())

    sum = 0

    for i in range(1, (No // 2) + 1):
        if No % i == 0:
            if i % 2 == 1:
                sum += i

    print("Sum of odd factors :", sum)

###########################################################################
#
#   Main Method
#
###########################################################################

def main():
    print("PID of main :", os.getpid())
    print("PPID of main :", os.getppid())

    print("Enter the number :")
    Val = int(input())

    start_time = time.time()

    t1 = threading.Thread(target = EvenFactors, args = (Val,))
    t2 = threading.Thread(target = OddFactors, args = (Val, ))

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