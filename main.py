import csv
import re
import sys

HEADER = ["Transaction Date",  "Post Date", "Description", "Category", "Type", "Amount"]
PATTERN = "RAPPI"

if len(sys.argv) != 2:
    print("Usage: main.py path-to-csv-file")
    exit(1)

try:
    with open(sys.argv[1], "r") as csv_file, open("rappi_sales.csv", 'w', newline='') as w:
        try:
            transactions = csv.reader(csv_file, delimiter=",")
            rappi_transactions = csv.writer(w)
            rappi_transactions.writerow(HEADER)
            for row in transactions:
                row2 = " ".join(row)
                print(f"{row}\t\t{row2}")
                m = re.search(PATTERN, row2)
                if m:
                    rappi_transactions.writerow(row)
                    print(row)
        except csv.Error as e:
            sys.exit(f"{e}")
except FileNotFoundError:
    print("File not found")
except IOError:
    print("ioerror")


def main():
    pass


if __name__ == "__main__":
    main()
