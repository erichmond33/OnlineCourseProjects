from cs50 import get_string
from sys import exit


def main():
    # Intitating the card number string
    card_number = ""
    # ensuring the string is all numbers
    while (card_number.isdigit() == False):
        card_number = get_string("Number: ")

        # Checking luhn's algorithm
    if(luhns_algo(card_number) == False):
        print("INVALID")
        exit(0)

    # Checking the length
    if (len(card_number) == 13):
        # checking the first character
        if (card_number[0] == "4"):
            #print(card_number[0])
            print("VISA")
        else:
            print("INVALID")

    elif (len(card_number) == 15):
        # checking the first and second character
        if ((card_number[0] == "3") and ((card_number[1] == "4") or (card_number[1] == "7"))):
            print("AMEX")
            #print(card_number[0], card_number[1])
        else:
            print("INVALID")

    elif (len(card_number) == 16):
        # checking the first character
        if (card_number[0] == "4"):
            print("VISA")
            #print(card_number[0])
        # checking the first and second character
        elif ((card_number[0] == "5") and ((card_number[1] == "5") or (card_number[1] == "1") or (card_number[1] == "2") or (card_number[1] == "3") or (card_number[1] == "4"))):
            print("MASTERCARD")
            #print(card_number[0], card_number[1])
        else:
            print("INVALID")


    else:
        print("INVALID")
        exit(0)

    exit(1)


def luhns_algo(card_number):

    # useless vairbles to impliment the algo
    temp_var = 0
    temp_var2 = 0
    # The final varible to determine whether the card is legit
    final_var = 0

    # looping through the card numbers backwards by two and skipping the first number
    for i in range(len(card_number) - 2, -1, -2):
        # Multiplying each number by 2
        temp_var = int(card_number[i]) * 2
        # Adding each individual digit to final var
        if (temp_var > 9):
            for j in range(2):
                temp_var2 = str(temp_var)[j]
                final_var += int(temp_var2)

        else:
            final_var += temp_var
    # looping through the rest of the numbers
    for k in range(len(card_number) - 1, -1, -2):
        # Adding them to final var
        final_var += int(card_number[k])
    # Checking to see if the last digete of final var is 0
    if (final_var % 10 == 0):
        return True
    else:
        return False
    # END OF ALGO


main()