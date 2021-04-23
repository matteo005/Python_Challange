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

# Print out the Formated Max Profit Increase and Decreases
# print(FormatedIncrease)    
# print(FormatedDecrease)

# #Print out the Formated Max Months Increase and Decreases
# print(Months[MonthIncrease])
# print(Months[MonthDecrease])

#Total up the Change List
#print(sum(Change))
#Count how many values there are in the Change List
#print(len(Change))

#Format Total Profit amount
TotalProfit = "$""{:,}".format(sum(Profits))

#Get the Average for Change
AvgChange = round(sum(Change)/len(Change),2)
AvgChangeFormated = "$""{:,}".format(AvgChange)



print("                Financial Analysis")
print("--------------------------------------------------")
print(f"Total Months:  {len(Months)}")
print(f"Total: {TotalProfit}")
print(f"Average Change: {AvgChangeFormated}")
print(f"Greatest Increase in Profits: {Months[MonthIncrease]} {FormatedIncrease}")
print(f"Greatest Increase in Profits: {Months[MonthDecrease]} {FormatedDecrease}")
print("--------------------------------------------------")


    #Create PyBank.txt file
with open("PyBank.txt", "w") as file:

    # # Write all values
    file.write("                        Financial Analysis")
    file.write("\n")
    file.write("----------------------------------------------------------------")
    file.write("\n")
    file.write(f"Total Months:  {len(Months)}")
    file.write("\n")
    file.write(f"Total: {TotalProfit}")
    file.write("\n")
    file.write(f"Average Change: {AvgChangeFormated}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits was on: {Months[MonthIncrease]} for ({FormatedIncrease})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits was on: {Months[MonthDecrease]} for ({FormatedDecrease})")
    file.write("\n")
    file.write("----------------------------------------------------------------")