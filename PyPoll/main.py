import csv

# Create the path
with open('PyPoll/Resources/election_data.csv') as file:
    reader = csv.reader(file)
    # Exclude the header row
    header = next(reader)
    
    # Initialize variables
    total_votes = 0
    candidates = {}
    winner = ""
    winner_votes = 0
    
    # Iterate over each row in the CSV
    for row in reader:
        # Count the total number of votes
        total_votes += 1
        
        # Get the candidate from the row
        candidate = row[2]
        
        # If the candidate is not in the dictionary, add them with an initial vote count of 1
        if candidate not in candidates:
            candidates[candidate] = 1
        # If the candidate is already in the dictionary, increment their vote count
        else:
            candidates[candidate] += 1

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Iterate over the candidates and calculate their percentage of votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check if the candidate has more votes than the current winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
print("---------------------------------")