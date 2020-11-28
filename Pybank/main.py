import csv 
from statistics import mean
Total = 0.0
Averagechange = 0.0
Maxprofit = []
Minprofit = []
Profitloss = []

with open('Pybank/Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} {row[1]}')
            Total = Total + int(row[1])
            Profitloss.append(int(row[1]))
            line_count += 1
    print(f'Processed {line_count} lines.')
    print (Total)

    print (mean(Profitloss))