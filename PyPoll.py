print("hello world")
# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recived votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#--file_to_load = 'resources/election_results.csv'
#open the election results
#--election_data = open(file_to_load, 'r')

# perfporm analysius
# close the file
#--election_data.close()

#without using open and close statements
#--with open(file_to_load) as election_data:

    #-print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
#read the file object with the reader function
    file_reader = csv.reader(election_data)
 #print each row in the csv file
    #for row in file_reader:
     #print(row)

    #print header row
    headers = next(file_reader)
    print(headers)

    # Print the file object.
     #print(election_data)

import datetime
now = datetime.datetime.now()
print("the time is right", now)
# or
import datetime as dt
now = dt.datetime.now()
print("the time right now is", now)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
    txt_file.write("Counties in the Election")
    txt_file.write("\n------------------------")
    txt_file.write("\nArapahaoe\nDenver\nJefferson")
    # or txt_file.write("arapahaoe, Denver, Jefferson")


#===================================================================================

#add out dependencies
import csv
import os
# Assign a variable for the file to load from the path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize total vote counter.
total_votes = 0

#Declare a new list
candidate_option = []

#declare an emtpy dictionary to associate vote count with candidate
candidate_votes = {}

#winning candiate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # 2. increment the total votes by 1
        total_votes += 1
        #Print candidates name from each row
        candidate_name = row[2]
        #add candidate that is printed to the candidate_options list we just created
        #candidate_option.append(candidate_name)
        # If the candidate name does not match any existing candidate in the list, add it to list of candidate
        if candidate_name not in candidate_option:
            #add candidate name to candadate list
            candidate_option.append(candidate_name)
            # begin tracking candidate votes for each candidate
            candidate_votes[candidate_name] = 0
        # add a vote to that candidates name
        candidate_votes[candidate_name] += 1
    #determine the percentage of votes for each canbdidate
    for candidate_name in candidate_votes:
        #retieve vote count of candidate
        votes = candidate_votes[candidate_name]
        #calculate percentaghe of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes 
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    # Print out winning candidate, vote percentage and vote count
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)

# 3. Print the candidates votes
print(candidate_votes)

==========================================================================
#add out dependencies
import csv
import os
# Assign a variable for the file to load from the path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize total vote counter.
total_votes = 0

#Declare a new list
candidate_option = []

#declare an emtpy dictionary to associate vote count with candidate
candidate_votes = {}

#winning candiate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # 2. increment the total votes by 1
        total_votes += 1
        #Print candidates name from each row
        candidate_name = row[2]
        #add candidate that is printed to the candidate_options list we just created
        #candidate_option.append(candidate_name)
        # If the candidate name does not match any existing candidate in the list, add it to list of candidate
        if candidate_name not in candidate_option:
            #add candidate name to candadate list
            candidate_option.append(candidate_name)
            # begin tracking candidate votes for each candidate
            candidate_votes[candidate_name] = 0
        # add a vote to that candidates name
        candidate_votes[candidate_name] += 1
#save result to text file
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes = {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    #save final vote count to text file
    txt_file.write(election_results)
    #determine the percentage of votes for each canbdidate
    for candidate_name in candidate_votes:
        #retieve vote count of candidate
        votes = candidate_votes[candidate_name]
        #calculate percentaghe of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes 
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        # Print out winning candidate, vote percentage and vote count
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)



