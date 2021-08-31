import csv
from sys import exit
from sys import argv


def main():
    # Vairbles used for counting how many times a STR occurs back to back
    repeats = 0
    max_repeats = 0

    # Reading the DNA
    with open(argv[2], "r") as sequences:
        dna_string = sequences.read()

    # Reading the csv into a dictionary
    with open(argv[1], "r") as small:
        dict = csv.DictReader(small)

        # Making a copy of a single row to compare to the other rows later
        for row in dict:
            dict2 = row.copy()
        # Filling the copied row with garbage
        for x in range(0, len(dict.fieldnames)):
            dict2[dict.fieldnames[x]] = False

        # Looping through each STR
        for j in range(1, len(dict.fieldnames)):
            # Looping through the DNA
            for i in range(0, len(dna_string)):
                # Checking if the bit of DNA we are looking at currently is each to the current STR
                if dict.fieldnames[j] in dna_string[i:i + len(dict.fieldnames[j])]:
                    # Burner vairble... it is basically repeats but used in the recursive function
                    str_count = 0
                    # calling the recursive function to see how many times each found STR repeats back to back
                    repeats = str_check(dict.fieldnames, dna_string, j, i, str_count)
                    # Keeping track of with repeat is the highest
                    if (repeats > max_repeats):
                        max_repeats = repeats

            # Returns us to the top of the file so we can loop it again
            small.seek(0)
            # Checking to see if anyone's STR counts are equal to the max_repeats vairble
            for row in dict:
                if (row[dict.fieldnames[j]] == str(max_repeats)):
                    # if so then we need to update our copied row
                    dict2[dict.fieldnames[j]] = str(max_repeats)

            # Clearing the vairble
            max_repeats = 0

        # Comparing the STR values of every person to the STR values of the current DNA sequence
        compare_dict(dict2, dict, small)


# Checks how many times a string repeats back to back
def str_check(fieldnames, dna_string, j, i, str_count):
    # Base: If it doesn't repeat stop
    if fieldnames[j] not in dna_string[i: i + len(fieldnames[j])]:
        return str_count
    # If the next bit of dna is equal to the current STR then add one to the count, and call itself again
    elif fieldnames[j] in dna_string[i: i + len(fieldnames[j])]:
        str_count += 1

        # Note that when this is called recursivly i is updated
        return str_check(fieldnames, dna_string, j, i + len(fieldnames[j]), str_count)


# This compares the STR values ONLY of the copied dictionary and all the real dictionary values
def compare_dict(dict2, dict, small):
    # This determines if all of the STRs are equal later in the code
    key = 0

    # GOing to the top of the file
    small.seek(0)
    # Looping the rows of the dictionary
    for row in dict:
        # Looping over each STR value
        for i in range(1, len(dict.fieldnames)):
            # If the current persons STR value is equal to the current STR vaule of the DNA sequence
            if (row[dict.fieldnames[i]] == dict2[dict.fieldnames[i]]):
                # Add 1 to key to note that one STR value is the same
                key += 1
        # After one person, check to see if the number of STR values that were correct is equal to the total number of STR values. If so then that is our guy
        if (key == len(dict.fieldnames) - 1):
            print(row['name'])
            exit(0)

        # Clearing the key after each person
        key = 0

    print("No Match")
    exit(1)


main()