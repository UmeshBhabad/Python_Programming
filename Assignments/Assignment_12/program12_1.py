# Write a program which that accepts one character and checks whether it is vowel or not.

###########################################################################
#
# Function Name :   ChkVowel
# Description   :   used to check if given character is vowel or not.
# Input         :   str
# Output        :   bool
# Author        :   Umesh Shivaji Bhabad
# Date          :   21/01/2026
#
###########################################################################

def ChkVowel(char):
    if(len(char) > 1 or len(char) < 1):
        print("Wrong Input")
        return 

    if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u') or (char == 'A') or (char == 'E') or (char == 'I') or (char == 'O') or (char == 'U'):
        return True
    else:
        return False

def main():
    bRet = False

    print("Enter the Character :")
    Val = input()

    bRet = ChkVowel(Val)

    if(bRet):
        print("Vowel")
    else:
        print("Not a Vowel")

if __name__ == "__main__":
    main()