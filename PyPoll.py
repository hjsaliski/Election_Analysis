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



