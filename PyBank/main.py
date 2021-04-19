import os
import csv

#Create all Lists needed
Months = []
Profits = []
Change = []

# Module for reading CSV files
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        #Fill Lists with data
        Months.append(row[0])
        Profits.append(int(row[1]))

    for i in range(len(Profits)-1):

        Change.append(Profits[i+1]-Profits[i])

print(sum(Change))
print(len(Change))
avg_change = sum(Change)/len(Change)
print(avg_change)

print(f"Total Months:  {len(Months)}")
print(f"Total: ${sum(Profits)}")


