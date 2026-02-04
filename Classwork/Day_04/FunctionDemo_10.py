# One Function can call Another Function

def fun():
    print("Inside fun")

def gun():
    print("Inside gun")
    fun()

def main():
    gun()

if __name__ == "__main__":
    main()
