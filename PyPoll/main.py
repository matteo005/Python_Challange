import os
import csv

#Create all Lists needed
Candidates = []
Votes = []
rep = []



# Module for reading CSV files
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        #Fill Lists with data
        Candidates.append(str(row[2]))
        Votes.append(int(row[0]))

for i in Candidates:
    if i not in rep:        
        rep.append(i)
for i in rep:
    print(i)

