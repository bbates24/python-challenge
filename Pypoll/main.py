import csv 
from statistics import mean
Total = 0.0
percentchange = 0.0
voters_candidates = []
votes_per_candidate = []
with open('Pypoll/Resources/election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]')
            Total = Total + int(row[1])
            votes_per_candidate.append(int(row[1]))
            line_count += 1
    with open ("Pypoll/analysis/output.txt","w") as out_file: 
        print(f'Processed {line_count} lines.')
        out_file.write(f'Processed {line_count} lines.\n')
        print (Total)
        out_file.write (str(Total)+ "\n")
        print (mean(voters_candidates))
        out_file.write (str(mean(votes_per_candidate))+ "\n")