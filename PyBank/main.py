import csv

inputFile = "C:/Users/bvkka/Desktop/python-challenge/PyBank/budget_data.csv"
outputFile = "C:/Users/bvkka/Desktop/python-challenge/PyBank/outputResult.txt"


totalMonths = 0
totalAmount = 0
profitLosses = []
change = []
date =[]







with open(inputFile) as budgetData:
    reader=csv.DictReader(budgetData)

    for row in reader:
        totalMonths = totalMonths + 1
        totalAmount = totalAmount + int(row["Profit/Losses"])
        profitLosses.append(int(row["Profit/Losses"]))
        date.append(row["Date"])

    for i in range(len(profitLosses)-1):
           change.append(profitLosses[i+1]-profitLosses[i])


greatestIncrease = max(change)
greatestDecrease = min(change)

dateIncrease = change.index(greatestIncrease)+1
dateDecrease = change.index(greatestDecrease)+1

high_month = date[dateIncrease]
low_month = date[dateDecrease]



print("totalMonths:" + str(totalMonths))  
print("totalAmount:" + str(totalAmount))
print("change:" + str(change))
print("averageChange: " + str(round(sum(change)/len(change),2)))
print(f"Greatest Increase in Profits: {date[dateIncrease]} (${(str(greatestIncrease))})")
print(f"Greatest Decrease in Profits: {date[dateDecrease]} (${(str(greatestDecrease))})")      




with open(outputFile,'w') as file:
    file.write("Total Months: %d\n" % totalMonths)
    file.write("Total: $%d\n" % totalAmount)
    file.write("Average Change: $" + str(round(sum(change)/len(change),2))) 
    file.write("Greatest Increase in Revenue: " + str(high_month) + " ($" + str(greatestIncrease) + ")")
    file.write("Greatest Decrease in Revenue: " + str(low_month) + " ($" + str(greatestDecrease) + ")")


   