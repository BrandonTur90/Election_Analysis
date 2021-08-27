# The Data we need to retrieve
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes 
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

#import CSV and OS modules
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Candidate options
candidate_options = []
#Candidate votes
candidate_votes = {}
#Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    #to do: read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row only
    headers = next(file_reader)
    print(headers)


    # Print each row in the CSV file.
    for row in file_reader:
        #print(row)
        total_votes +=1
        #Print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match and existing candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote each time the loop counts that candidate
        candidate_votes[candidate_name] += 1

# Find the percentage for each candidate
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of vote.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. primt the candidate name and percentage of votes.
    print(f'{candidate_name}: received {vote_percentage:.1f}% of the vote.')

    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning percent = vote percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name


# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)    

