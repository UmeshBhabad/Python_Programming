import gc

class Demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

# Allocate Memory to object
obj = Demo()

# Use the object

# Deallocate Memory to object
del obj                                 # delete object

gc.collect()                            # request to the garbage collector

print("End of application")