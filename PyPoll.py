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

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row only
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes +=1
        #Get the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match and existing candidate...
        if candidate_name not in candidate_options:
            #Add the candidate name to candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote each time the loop counts that candidate
        candidate_votes[candidate_name] += 1

#Save results as a text file
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #After printing final vote count to the terminal save the final vote count
    txt_file.write(election_results)


    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count and percentages
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
    

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning percent = vote percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)    
    #save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

