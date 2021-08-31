import csv
from sys import exit
from sys import argv
from cs50 import SQL

# Inserting the database
db = SQL("sqlite:///students.db")

def main():
    # Ensuring there is one argument
    argc = 0
    for i in argv:
        argc += 1
    if argc != 2:
        print("Usage: python roster.py <house>")
        exit(1)

    # Filtering the first, middle, last, and birth columns from the db
    dic = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", argv[1])

    # Looping through the list of dictionaries dc.execute returned
    for field in dic:
        # Checking if the person has a middle name, and printing the right output accordingly
        if field['middle'] == None:
            print(f"{field['first']} {field['last']}, born {field['birth']}")
        else:
            print(f"{field['first']} {field['middle']} {field['last']}, born {field['birth']}")


main()
