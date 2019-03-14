#!/usr/bin/python3

"""
  This script is used to change a decimal
  IPv4 Address into a binary IPv4 Address.
"""

# Define a function that changes decimal into
# binary.

def decToBin(dec):

    # List to hold the binary.

    binaryList = []

    # String for the whole binary octet.
    final = ""

    # Test to see if the decimal is equal to or more
    # than 128 (2^7).

    if dec >= 128:

        # TRUE - Remove 128 from the decimal's value.
        # Then add a 1 to the binary list.

        dec = dec - 128
        binaryList.append("1")
    
    else:

        # FALSE - Keep the decimal's value and add
        # 0 to the binary list.

        binaryList.append("0")

    # Test to see if the decimal is equal to or more
    # than 64 (2^6).

    if dec >= 64:

        # TRUE - Remove 64 from the decimal's value.
        # Then add a 1 to the binary list.

        dec = dec - 64
        binaryList.append("1")
    
    else:

        # FALSE - Keep the decimal's value and add
        # 0 to the binary list.

        binaryList.append("0")

    # Test to see if the decimal is equal to or more
    # than 32 (2^5).

    if dec >= 32:

        # TRUE - Remove 32 from the decimal's value.
        # Then add a 1 to the binary list.

        dec = dec - 32
        binaryList.append("1")
    
    else:

        # FALSE - Keep the decimal's value and add
        # 0 to the binary list.

        binaryList.append("0")

    # Test to see if the decimal is equal to or more
    # than 16 (2^4).

    if dec >= 16:

        # TRUE - Remove 16 from the decimal's value.
        # Then add a 1 to the binary list.

        dec = dec - 16
        binaryList.append("1")
    
    else:

        # FALSE - Keep the decimal's value and add
        # 0 to the binary list.

        binaryList.append("0")

    # Test to see if the decimal is equal to or more
    # than 8 (2^3).

    if dec >= 8:

        # TRUE - Remove 8 from the decimal's value.
        # Then add a 1 to the binary list.

        dec = dec - 8
        binaryList.append("1")
    
    else:

        # FALSE - Keep the decimal's value and add
        # 0 to the binary list.

        binaryList.append("0")

    # Test to see if the decimal is equal to or more
    # than 4 (2^2).

    if dec >= 4:

        # TRUE - Remove 4 from the decimal's value.
        # Then add a 1 to the binary list.

        dec = dec - 4
        binaryList.append("1")
    
    else:

        # FALSE - Keep the decimal's value and add
        # 0 to the binary list.

        binaryList.append("0")

    # Test to see if the decimal is equal to or more
    # than 2 (2^1).

    if dec >= 2:

        # TRUE - Remove 2 from the decimal's value.
        # Then add a 1 to the binary list.

        dec = dec - 2
        binaryList.append("1")
    
    else:

        # FALSE - Keep the decimal's value and add
        # 0 to the binary list.

        binaryList.append("0")

    # Test to see if the decimal is equal to or more
    # than 1 (2^0).

    if dec >= 1:

        # TRUE - Remove 1 from the decimal's value.
        # Then add a 1 to the binary list.

        dec = dec - 1
        binaryList.append("1")
    
    else:

        # FALSE - Keep the decimal's value and add
        # 0 to the binary list.

        binaryList.append("0")

    # Cycle through the binary list and create a string
    # containing the binary octet.

    for i in binaryList:
        final += str(i)

    # Return the binary octet string.

    return final
        
# Get the user's decimal IPv4 Address.

# Prompt the user for the first, second,
# third, and fourth octet of their
# address individually.

firstOct = int(input("Please enter the first octet of your address >> "))
secondOct = int(input("Please enter the second octet of your address >> "))
thirdOct = int(input("Please enter the third octet of your address >> "))
fourthOct = int(input("Please enter the fourth octet of your address >> "))

# Pass each of the octets through the function
# created earlier in this script and save the
# returned string.

firstBin = decToBin(firstOct)
secondBin = decToBin(secondOct)
thirdBin = decToBin(thirdOct)
fourthBin = decToBin(fourthOct)

# Print out the final binary IPv4 Address.

print("\nThe decimal IPv4 Address " + str(firstOct) + "." +
                                    str(secondOct) + "." +
                                    str(thirdOct) + "." +
                                    str(fourthOct) +
      " is:\n")
print(firstBin + "." +
      secondBin + "." +
      thirdBin + "." +
      fourthBin)

# User input because this is a CLI script.
userExit = input()

