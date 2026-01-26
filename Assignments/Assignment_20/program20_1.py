# Design a Python application that creates two separate threads named Even and Odd.
'''
The Even thread should display the first 10 even numbers.

The Odd thread should display the first 10 odd numbers.

Both threads should execute independently using the threading module.

Ensure proper thread creation and execution.
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

def DisplayEven():
    print("TID :", threading.get_ident())

    for i in range(2, 21, 2):
        print(i, end = "\t")
    print()

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

def DisplayOdd():
    print("TID :", threading.get_ident())
    
    for i in range(1, 21, 2):
        print(i, end = "\t")
    print()

###########################################################################
#
#   Main Method
#
###########################################################################

def main():
    print("PID of main :", os.getpid())
    print("PPID of main :", os.getppid())

    start_time = time.time()

    t1 = threading.Thread(target = DisplayEven)
    t2 = threading.Thread(target = DisplayOdd)

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