# Main Method
def main():
    try:                                                        # File opened
        open("Demo.txt", "r")
        print("File gets sucessfully opened")
        
    except FileNotFoundError:                                   # File not present
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

# Start of program
if __name__ == "__main__":
    main()