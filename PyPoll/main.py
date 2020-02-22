import os
import csv
import math

totalvote = 0
#votes = {}
votesforkhan = 0
votesforcorrey = 0
votesforli = 0
votesforotooley = 0


election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        totalvote += 1
        if row[2] == "Khan":
            votesforkhan += 1
        elif row[2] == "Correy":
            votesforcorrey += 1
        elif row[2] == "Li":
            votesforli += 1
        elif row[2] == "O'Tooley":
            votesforotooley += 1
        #votes.append(row[2])

#votes.value_count()
votes = [votesforkhan, votesforcorrey, votesforli, votesforotooley]
names = ["Khan", "Correy", "Li", "O'Tooley"]
mostvoted = votes.index(max(votes))
winner = names[mostvoted]


khanpercent = (votesforkhan / totalvote) * 100
correypercent = (votesforcorrey / totalvote) * 100
lipercent = (votesforli / totalvote) * 100
otooleypercent = (votesforotooley / totalvote) * 100

khanpercent = float("{0:.3f}".format(khanpercent))
correypercent = float("{0:.3f}".format(correypercent))
lipercent = float("{0:.3f}".format(lipercent))
otooleypercent = float("{0:.3f}".format(otooleypercent))

#print(totalvote)
#print(votesforkhan)
#print("%.3f" % khanpercent)
#print(votesforcorrey)
#print(correypercent)
#print(votesforli)
#print(lipercent)
#print(votesforotooley)
#print(otooleypercent)
#print(winner)

out_csv = os.path.join("polloutput.csv")
with open(out_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerows([
        ["Election Results"],
        ["---------------------------"],
        [f"Total Votes: {totalvote}"],
        ["---------------------------"],
        [f"{names[0]}: {khanpercent}% {votes[0]}"],
        [f"{names[1]}: {correypercent}% {votes[1]}"],
        [f"{names[2]}: {lipercent}% {votes[2]}"],
        [f"{names[3]}: {otooleypercent}% {votes[3]}"],
        ["---------------------------"],
        [f"Winner: {winner}"],
        ["---------------------------"]
    ])

with open(out_csv, 'r') as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',')
    for row in csvreader2:
        print(row)

