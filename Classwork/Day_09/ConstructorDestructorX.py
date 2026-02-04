import gc

class Demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

# Allocate Memory to object
obj1 = Demo()
obj2 = Demo()

# Use the object

# Deallocate Memory to object
del obj1                                 # delete object
del obj2

gc.collect()                            # request to the garbage collector

print("End of application")