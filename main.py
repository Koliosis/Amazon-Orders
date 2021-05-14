import csv

with open('amazon-orders.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    sum = 0
    str_list = []
    int_list = []
    for row in reader:
        str_list.append(row['Total Charged'])
    my_ints = [float(l[1:]) for l in str_list]
    print(my_ints)
    total = 0
    for i in my_ints:
        total += i
    print(total)
        # sum += row['Total Charged']