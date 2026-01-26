# Design a Python application that creates two threads named Thread1 and Thread2.
'''
Thread1 should display numbers from 1 to 50.

Thread2 should display numbers from 50 to I in reverse order.

Ensure that:

    Thread2 starts execution only after Thread1 has completed.

Use appropriate thread synchronization
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
# Function Name :   DisplayNum
# Description   :   display numbers from 1 to 50.
# Input         :   None
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def DisplayNum():
    print("TID :", threading.get_ident())

    for i in range(1, 51):
        print(i , end = "\t")
    print()

###########################################################################
#
# Function Name :   DisplayReverse
# Description   :   display numbers from 50 to 1 in reverse order.
# Input         :   None
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def DisplayReverse():
    print("TID :", threading.get_ident())
    
    for i in range(50, 0, -1):
        print(i , end = "\t")
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

    t1 = threading.Thread(target = DisplayNum)
    t2 = threading.Thread(target = DisplayReverse)

    end_time = time.time()

    t1.start()
    t1.join()

    t2.start()    
    t2.join()

    print("Execution time :", end_time - start_time)

###########################################################################
#
#   Starter for main method
#
###########################################################################

if __name__ == "__main__":
    main()