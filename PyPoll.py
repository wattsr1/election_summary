# Add our dependancies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize the total vote count to 0
total_votes = 0
# Candidate options
candidate_options = []
# Declare and empty dictionary for canditate votes
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1

    # Print the candidates name from each row
        candidate_name = row[2]
    # Determine if the name is already in the list
        if candidate_name not in candidate_options:

    # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
    # Begin tracking the candidate votes
            candidate_votes[candidate_name] = 0

    # Add a vote to that candidates count
        candidate_votes[candidate_name] += 1
        
# Determine the percentage of votes for each candidate by looping though the counts
#Iterate through the candidate lists
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Determine the winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #Set the winning_candidate equal to the candidates name.
        winning_candidate = candidate_name
#To do: print out the winning candidate, vote count and percentage to terminal

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------")

print(winning_candidate_summary)

# Print votes and candidate list
#print(total_votes)
#print(candidate_options)
#print(candidate_votes)


#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The total number of votes each candidate won
#5 The winner of the election based on popular votes.
