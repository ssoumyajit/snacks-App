import csv
with open('snacks1.csv',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'column names are {", ".join(row)}')
            break
    print(f'Processed {line_count} lines.')
