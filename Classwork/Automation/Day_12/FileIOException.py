
# Main Method
def main():
    # Exception Handling
    try:
        open("Demo.txt")                                        # opens file in default read mode if present
        print("File gets sucessfully opened")
        
    except FileNotFoundError:                                   # file not present
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

# Starter
if __name__ == "__main__":
    main()