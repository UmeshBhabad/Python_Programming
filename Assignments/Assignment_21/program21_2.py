# Design a Python application that creates two threads.
'''
Thread 11 should calculate and display the maximum element from an list.

Thread 2 should calculate and display the minimum element from the same list.

The list should be accepted from the user.
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
# Function Name :   Maximum
# Description   :   display the maximum element from an list
# Input         :   list
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def Maximum(Lst):
    print("TID :", threading.get_ident())

    Max = Lst[0]

    for i in Lst:
        if i > Max:
            Max = i

    print("Maximum element", Max)


###########################################################################
#
# Function Name :   NonPrime
# Description   :   display the minimum element from an list.
# Input         :   list
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def Minimum(Lst):
    print("TID :", threading.get_ident())

    Min = Lst[0]

    for i in Lst:
        if i < Min:
            Min = i

    print("Maximum element", Min)

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

    t1 = threading.Thread(target = Maximum, args = (Data,))
    t2 = threading.Thread(target = Minimum, args = (Data,))

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