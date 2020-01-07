import csv
import re
import sys

words = ["Payment", "Adjustment", "Return"]
pattern = "RAPPI"

if len(sys.argv) != 2:
    print("Usage: main.py path-to-csv-file")
    exit(1)

try:
    with open(sys.argv[1], "r") as csv_file:
        transactions = csv.reader(csv_file, delimiter=",")
        for row in transactions:
            row = ",".join(row)
            match = re.search(pattern, row)
            if match:
                print(row)
except FileNotFoundError as file_not_found:
    print("File not found")
except IOError as io_error:
    print("ioerror")


def main():
    print("Main")


if __name__ == "__main__":
    main()
