import os
import csv
#total = 0
monthsarray = []
profit = []
diff = []

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        monthsarray.append(row[0])
        #total += int(row[1])
        profit.append(int(row[1]))
    #print(len(profit))
    for x in range(len(profit)):
        if x + 1 < len(monthsarray):
            #print(profit[x])
            difference = profit[x + 1] - profit[x]
            diff.append(difference) 
            #print(profit[x])
        #elif x > months:
            #print("Done")
        #diff = profit[x+1] - profit[x]
        #print(diff)

increase = max(diff)
increasepos = diff.index(max(diff))
decrease = min(diff)
decreasepos = diff.index(min(diff))
months = len(monthsarray)
increasemonth = monthsarray[increasepos+1]
decreasemonth = monthsarray[decreasepos+1]
total = sum(profit)

#print(len(monthsarray))
#print(total)
averagechange = sum(diff) / len(diff)
#print(averagechange)
#print(increase)
#print(decrease)
#print(monthsarray[increasepos+1])
#print(monthsarray[decreasepos+1])



output_path = os.path.join("bankoutput.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------"])
    csvwriter.writerows([
    [f"Total Months:  {months}"],
    [f"Total: ${total}"],
    [f"Average Change: ${averagechange}"],
    [f"Greatest Increase in Profits: {increasemonth} (${increase})"],
    [f"Greatest Decrease in Profits: {decreasemonth} (${decrease})"]
    ])


with open(output_path, 'r') as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=',')
    for row in csvreader2:
        print(row)

