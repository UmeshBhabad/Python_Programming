# One Function can call Another Function
def fun():
    print("Inside fun")

def gun():
    print("Inside gun")

def main():
    fun()
    gun()

if __name__ == "__main__":
    main()
