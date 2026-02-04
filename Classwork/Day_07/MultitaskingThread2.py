import threading

def Display():
    print("Inside Display function : ", threading.get_ident())    # thread id

def main():
    print("Inside main : ", threading.get_ident())      # main thread id
    
    t = threading.Thread(target = Display)
    t.start()
    
    print("End of main")

if __name__ == "__main__":
    main()