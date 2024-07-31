import os
import csv

#Set the path to the CSV file
csv_path = os.path.join("PyBank", "Resources", "budget_data.csv")

#Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_changes = []
months = []

#Read the CSV file
with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file)

    #skip the header row
    header = next(csv_reader)

    #Iterate over each row in the CSV file
    for row in csv_reader:
            #Extract the month and profit/loss from the current row
            month = row[0]
            profit_loss = int(row[1])
            
            #Update the total number of months
            total_months += 1

            #Update the total profit/loss
            total_profit_loss += profit_loss
            
            #Calculate the change in profit/loss from the previous month
            if total_months > 1:
                  change = profit_loss - previous_profit_loss
                  profit_changes.append(change)
                  months.append(month)

            #Update the previous profit/loss for the next iterations
            previous_profit_loss = profit_loss

#Calculate the average change in profit/loss
average_change = sum(profit_changes) / len(profit_changes)

#Find the greatest increase and decrease in profit/loss
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

#Find the corresponding months for the greatest increase and decrease
increase_month = months[profit_changes.index(greatest_increase)]
decrease_month = months[profit_changes.index(greatest_decrease)]

#Create the 'analysis' folder if it doesn't exist
output_dir = os.path.join("PyBank", "analysis")
os.makedirs(output_dir, exist_ok=True)

#Generate the financial analysis report
report = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n"
)

print(report)