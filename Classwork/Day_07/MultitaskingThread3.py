import threading

def Display():
    print("Inside Display function : ", threading.get_ident())    # thread id

    for i in range(100):
        print("Inside Display")
        
def main():
    print("Inside main : ", threading.get_ident())      # main thread id
    
    t = threading.Thread(target = Display)
    t.start()
    
    print("End of main")

if __name__ == "__main__":
    main()