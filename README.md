# python-challenge
This challenge is to utilize the skills I learned from python, by analyzing the data provided for two python challenges.

# PyBank
In the first challenge I am to analyze the financial script records in the csv called budget_data.csv. 
I needed to get;
The total number of months, 
The net "Profit/Losses" over the entire period, 
The changes in "Profit/Losses" over the entire period and average those changes
The greatest increase in profits
The greatest decrease in profits. 

# Method
First I imported the CSV. Then I used 'open' to open my csv file named budget_data.csv. I used the next to skip the header row. 
The next step was to initialize the variables. I did this by defining their functions. For example total_months will keep track of the number of months. 
After this I proceeded to the iterations over the rows. I used the for loop for this. The total_months is incremented by 1 for each row, the profit_loss value is extracted from the second column of the row and converted to an integer, the net_profit_losses is updated by adding the current profit_loss value, and the change is calculated as the difference between the current profit_loss and the previous profit_loss. The changes list is updated with the change value, and the previous_profit_loss is updated with the current profit_loss. Also, the greatest_increase and greatest_decrease values are updated if a new maximum or minimum change value is found.
Then the next step is I calculated the average by the sum and the length of the changes. 
Then I printed the analysis results.

# PyPoll
In the second challenge I am to modernize the vote-counting process. I’m given the data from the poll called election_data.csv.
I need to; Calculate the total number of votes, Complete a list of candidates who received votes, Calculate the percentage of votes each candidate won, The winner based on the popular vote.

# Method
After importing the csv file, I initialized the variables. Similar to the previous challenge I used the variables to initialize and store data. I then used the for loop to iterate the total number of votes. Within the loop, the total_votes are incremented by 1 for each row. The candidate’s name is extracted from the third column of the row and stored in the candidate variable. If the candidate is not already in the candidate’s dictionary, they are added with an initial vote count of 1. If the candidate is already in the dictionary, their vote count is increased by 1.

# Errors
I did have some mistakes after I found out I needed to output my results in txt. I had to get help from the BCA assitant. He gave me the starting code for the text I just need to create my pathways and while doing so I accidently output into my csv file. I was able to re-download and correct that error.  
