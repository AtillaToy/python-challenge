import os
import csv


filepath = os.path.join("Resources","election_data.csv")

canNames = []
canVotes = []

with open(filepath, newline='') as csvfile:

    votecsv = csv.reader(csvfile, delimiter=',')
    next(votecsv)

    for row in votecsv:
        if row[2] not in canNames:
            canNames.append(row[2])
            canVotes.append(1)
        else:
            canVotes[canNames.index(row[2])] = canVotes[canNames.index(row[2])] + 1
                
print(canNames)
print(canVotes)

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(sum(canVotes)))
print("-------------------------")

for i in range (0,len(canNames)):
    percentvote = canVotes[i] / sum(canVotes) * 100
    print (canNames[i] + ": " + str(round(percentvote, 5)) + "% (" + str(canVotes[i]) + ")")

print("-------------------------")
print("Winner: " + canNames[canVotes.index(max(canVotes))])


result = open("result.txt", "w") 
result.write("Election Results \n")
result.write("-------------------------\n")
result.write("Total Votes: " + str(sum(canVotes)) + "\n")
result.write("-------------------------\n")

for i in range (0,len(canNames)):
    percentvote = canVotes[i] / sum(canVotes) * 100
    result.write(canNames[i] + ": " + str(round(percentvote, 5)) + "% (" + str(canVotes[i]) + ")"+ "\n")

result.write("-------------------------\n")
result.write("Winner: " + canNames[canVotes.index(max(canVotes))]+ "\n")
result.close() 