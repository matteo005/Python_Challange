import os
import csv

#Create all Lists needed
Months = []
Profits = []
Change = []
GreatIncrease = []
GreatDecrease = []


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

    #Run Through all the Profits and append it to the Change list
    for i in range(len(Profits)-1):

        Change.append(Profits[i+1]-Profits[i])

#Find Greatest Increase and Decrease from Profits
GreatIncrease = max(Change)
GreatDecrease = min(Change)
FormatedIncrease = "$""{:,}".format(GreatIncrease)
FormatedDecrease = "$""{:,}".format(GreatDecrease)


#Find the corresponding monthst to each Greatest Increase and Decrease 
MonthIncrease = Change.index(max(Change)) +1
MonthDecrease = Change.index(min(Change)) +1

print(FormatedIncrease)    
print(FormatedDecrease)

print(Months[MonthIncrease])
print(Months[MonthDecrease])



#Total up the Change List
#print(sum(Change))
#Count how many values there are in the Change List
#print(len(Change))

#Get the Average for Change
AvgChange = round(sum(Change)/len(Change),2)
AvgChangeFormated = "$""{:,}".format(AvgChange)

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months:  {len(Months)}")
print(f"Total: ${sum(Profits)}")
print(f"Average Change: {AvgChangeFormated}")


