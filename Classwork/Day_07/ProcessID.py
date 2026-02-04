
import os

def main():
    print("PID of running process is : ", os.getpid())  # process id

    print("PID of parent process is : ", os.getppid())  # parent process id

if __name__ == "__main__":
    main()