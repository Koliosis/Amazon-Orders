import csv

with open('amazon-orders.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for range(10) in reader:
        print(row['Order Date'])