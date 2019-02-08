import csv
import re

words = ['Payment', 'Adjustment', 'Return']
more_words = 'RAPPI'


def main():
    try:
        with open('./Chase0218_Activity20170126_20190126_20190126.csv', 'r') as csv_file, open('./not_sales.csv', 'w') as not_sales, open('./sales.csv', 'w') as sales:
            costs = csv.reader(csv_file, delimiter=',')
            x = csv.writer(not_sales)
            y = csv.writer(sales)
            y.writerow(
                       ['Transaction Date',
                        'Post Date',
                        'Description',
                        'Category',
                        'Type',
                        'Amount']
            )
            x.writerow(
                       ['Transaction Date',
                        'Post Date',
                        'Description',
                        'Category',
                        'Type',
                        'Amount']
             )

            for line in costs:
                if 'Sale' in line:
                    string = r' '.join(line)
                    print(string.strip())
                    print(re.search('^[+-]', string))
                    # x.writerow(string.strip())

                else:
                    y.writerow(line[-2:-1])
                    # print(line[:-1])

    except IOError as e:
        print("Can't open file...")


if __name__ == '__main__':
    main()
