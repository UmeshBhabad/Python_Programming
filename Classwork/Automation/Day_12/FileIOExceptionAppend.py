# Append

# Main Method
def main():
    try:
        fobj = open("Hello.txt", "a")                           # opening file for append operation
        print("File gets sucessfully opened")

        fobj.write("Python Automation")

        fobj.close()                                            # closing file

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

# Start of program
if __name__ == "__main__":
    main()