"Import Resources"
import csv

"Create the path"
with open ('PyBank/Resources/budget_data.csv') as file:
    reader = csv.reader(file)
# Exclude the header row
    header = next(reader)
    
    # Initialize variables
    total_months = 0
    net_profit_losses = 0
    previous_profit_loss = 0
    changes = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]
    
    # Iterate over the rows
    for row in reader:
        # Count the total number of months
        total_months += 1
        
        # Calculate the net total of "Profit/Losses"
        profit_loss = int(row[1])
        net_profit_losses += profit_loss
        
        # Calculate the changes in "Profit/Losses"
        change = profit_loss - previous_profit_loss
        changes.append(change)
        previous_profit_loss = profit_loss
            
        # Find the greatest increase and decrease in profits
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

# Calculate the average change in profits
average_change = sum(changes) / len(changes)

variable = (                                                           
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
print(variable)    

with open('financial_analysis.txt', "w") as txt_file:
    txt_file.write(variable)