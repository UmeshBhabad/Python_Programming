# Design a Python application where multiple threads update a shared variable.
'''
Use a Lock to avoid race conditions.

Each thread should increment the shared counter multiple times.

Display the final value of the counter after all threads complete execution.
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
#   Global Variable
#
###########################################################################

Val = 10

lobj = threading.Lock() 

###########################################################################
#
# Function Name :   Update
# Description   :   display the first 10 odd numbers
# Input         :   None
# Output        :   None
# Author        :   Umesh Shivaji Bhabad
# Date          :   25/01/2026
#
###########################################################################

def Update():
    print("TID :", threading.get_ident())

    global Val

    for i in range(5):
        with lobj:
            Val += 10
        print("Updated Value :", Val)

    

###########################################################################
#
#   Main Method
#
###########################################################################

def main():
    print("PID of main :", os.getpid())
    print("PPID of main :", os.getppid())

    global Val

    start_time = time.time()

    

    t1 = threading.Thread(target = Update)
    t2 = threading.Thread(target = Update)
    t3 = threading.Thread(target = Update)
    t4 = threading.Thread(target = Update)
    t5 = threading.Thread(target = Update)

    end_time = time.time()

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    print("Execution time :", end_time - start_time)

###########################################################################
#
#   Starter for main method
#
###########################################################################

if __name__ == "__main__":
    main()