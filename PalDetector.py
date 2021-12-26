# This is a simple palindrome tester from scratch
if __name__ == "__main__":
    # The usrString takes an input from the user
    usrString = input("Input a word to see if it's a palindrome:")
    print(usrString)
    # The complicated code is only necessary if the input is at least length 2
    if len(usrString) > 1:
        # The frontHalfLength takes the first half of the string regardless if the string is odd or even
        frontHalfLength = len(usrString) // 2
        # The backHalfLength takes the back half of the string and disregards the middle character if the string is an odd length
        backHalfLength = len(usrString) // 2 if len(usrString) % 2 == 0 else ((len(usrString) // 2) + 1)
        a = usrString[:frontHalfLength]
        b = usrString[backHalfLength:]
        i = 0
        for each in a:
            if each == b[len(b) - i - 1]:
                pal = True
                i += 1
            else:
                pal = False
                break
        if pal:
            print("Your word is a palindrome!")
        elif not pal:
            print("Your word is not a palindrome")
    # Are words of length one a palindrome?
    elif len(usrString) == 1:
        print("Your word is a palindrome!")
    # Blank input handling
    else:
        print("Your input was blank")
