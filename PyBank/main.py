import os
import csv


filepath = os.path.join("budget_data.csv")

monthcount = 0
total = 0
previous = 0
delta = 0
deltas = []
avgd = 0.0
imonth = ""
dmonth = ""

with open(filepath, newline='') as csvfile:

    budgetcsv = csv.reader(csvfile, delimiter=',')
    next(budgetcsv)

    for row in budgetcsv:
        monthcount = monthcount + 1
        total = total + int(row[1])
        if monthcount > 1:
            delta = int(row[1]) - int(previous)
            deltas.append(delta)
            previous = int(row[1])
            if delta == max(deltas):
                imonth = row[0]
            if delta == min(deltas):
                dmonth = row[0]
        else:
            previous = int(row[1])
        if row[0] == None:
            break

avgd = sum(deltas) / len(deltas)

print("Total Months: " + str(monthcount))
print("Total: $" + str(total))
print("Average  Change: $" + str(round(avgd, 2)))
print("Greatest Increase in Profits: " + str(imonth) + " ($" + str(max(deltas)) + ")")
print("Greatest Decrease in Profits: " + str(dmonth) + " ($" + str(min(deltas)) + ")")

bankreport = open("bankreport.txt", "w") 
bankreport.write("Total Months: " + str(monthcount) + "\n")
bankreport.write("Total: $" + str(total)  + "\n")
bankreport.write("Average  Change: $" + str(round(avgd, 2)) + "\n")
bankreport.write("Greatest Increase in Profits: " + str(imonth) + " ($" + str(max(deltas)) + ")" + "\n")
bankreport.write("Greatest Decrease in Profits: " + str(dmonth) + " ($" + str(min(deltas)) + ")" + "\n")