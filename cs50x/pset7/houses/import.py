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
        print("Usage: python import.py <file.csv>")
        exit(1)

    # Reading the csv file
    with open(argv[1], "r") as people:
        reader = csv.DictReader(people)
        # Looping each Row
        for row in reader:
            # Spliting the name column into a list of each word
            split = row['name'].split()
            # Checking if the person has a middle name, and inserting NULL for their middle name if they don't
            if len(split) == 3:
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", split[0], split[1], split[2], row['house'], row['birth'])
            elif len(split) == 2:
                db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", split[0], None, split[1], row['house'], row['birth'])


main()

