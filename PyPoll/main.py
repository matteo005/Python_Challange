import os
import csv

#Create all Lists, Dictionary and values to store info
rep = []
repvotes = {}
TotalVotes = 0
WinCount = 0

# Module for reading CSV files
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        #Count total votes
        TotalVotes += 1
        
        #Get the names of Candidates from column 3
        Candidates = row[2]

        #Run through Candidates and append only 1 instance of each
        if Candidates not in rep:        
            rep.append(Candidates)
            
            #Create dictionary to store the vote counts for each Candidate
            repvotes[Candidates] = 0
        #Add one vote to the candidate count
        repvotes[Candidates] += 1


    print("         Election Results")
    print("------------------------------")
    print(f"Total Votes: {TotalVotes}")
    print("------------------------------")
        

    for candidate in repvotes:

        #Get vote count from each Candidate and calculate percentage
        votes = repvotes.get(candidate)
        VotePercent = float(votes)/float(TotalVotes)*100

        # Determine winning vote count and candidate
        if (votes > WinCount):
            WinCount = votes
            Winner = candidate

        print(f"{candidate}: {VotePercent:.3f}% ({votes})")
    print("------------------------------")
    print(f"Winner: {Winner}\n")