import csv

inputFile = "C:/Users/bvkka/Desktop/python-challenge/PyPoll/election_data.csv"
outputFile = "C:/Users/bvkka/Desktop/python-challenge/PyPoll/outputResult.txt"

totalVotes = 0
candidates = []

vote_counts = []
election_data = ['1', '2']



with open(inputFile, newline = "") as electionData:
    csvreader=csv.reader(electionData,delimiter=",")
    line = next(csvreader,None)
    for line in csvreader:
        totalVotes = totalVotes + 1
        candidate = line[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1

                
        else:
            candidates.append(candidate)
            vote_counts.append(1)
               
   
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0
    
    
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/totalVotes*100
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]
   
    percentages = [round(i,2) for i in percentages]
    
    # Summary print test of election results
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {totalVotes}")
    print("--------------------------")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("--------------------------")
    print(f"Winner:  {winner}")
    print("--------------------------")

  
with open(outputFile,'w') as file:
    
    file.write("Election Results\n")
    file.write("-----------------------------\n")
    file.write(f"Total Votes:  {totalVotes}\n")
    file.write("-----------------------------\n")
    for count in range(len(candidates)):
        file.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
    file.write("-----------------------------\n")
    file.write(f"Winner:  {winner}\n")
    file.write("-----------------------------\n")
    
    
    file.close()



