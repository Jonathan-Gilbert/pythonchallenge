# import poll
import os
import csv

# Correct the path to the CSV file (fixed typo from 'PyPull' to 'PyPoll')
csvpath = os.path.join("PyPoll", 'Resources', 'election_data.csv')

# Open and read the CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    # Declare variables
    votes = []
    county = []
    candidates = []
    
    # Initialize vote counters
    Charles_Casper_Stockham_votes = 0
    Diana_DeGette_votes = 0
    Raymon_Anthony_Doane_votes = 0

    # Read each row of data after the header
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    # Total vote count
    total_votes = len(votes)

    # Votes by person
    for candidate in candidates:
        if candidate == "Charles Casper Stockham":
            Charles_Casper_Stockham_votes += 1
        elif candidate == "Diana DeGette":
            Diana_DeGette_votes += 1
        elif candidate == "Raymon Anthony Doane":
            Raymon_Anthony_Doane_votes += 1

    # Print results
    # print(f"Total Votes: {total_votes}")
    # print(f"Charles Casper Stockham: {Charles_Casper_Stockham_votes}")
    # print(f"Diana DeGette: {Diana_DeGette_votes}")
    # print(f"Raymon Anthony Doane: {Raymon_Anthony_Doane_votes}")

    #Percentages
    Charles_Casper_Stockham_percent = round(((Charles_Casper_Stockham_votes / total_votes) * 100), 3)
    Diana_DeGette_percent = round(((Diana_DeGette_votes / total_votes) * 100), 3)
    Raymon_Anthony_Doane_percent = round(((Raymon_Anthony_Doane_votes / total_votes) * 100), 3)
    print(Charles_Casper_Stockham_percent)
    print(Diana_DeGette_percent)
    print(Raymon_Anthony_Doane_percent)

    #Winner
    if Charles_Casper_Stockham_percent > max(Diana_DeGette_percent, Raymon_Anthony_Doane_percent):
        winner = "Charles_Casper_Stockham"
    elif Diana_DeGette_percent > max(Charles_Casper_Stockham_percent, Raymon_Anthony_Doane_percent):
        winner = "Diana_DeGette"
    else:
        winner = "Raymon_Anthony_Stockham"
    
    #print statemnts
        # Print Statements
    print(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')


    # Output to a text file
    file = open("output.txt","w")
    file.write(f'''Election Results
-----------------------------------
Total Votes: {total_votes}
-----------------------------------
Charles_Casper_Stockham_percent: {Charles_Casper_Stockham_percent}% ({Charles_Casper_Stockham_votes})
Diana_DeGette: {Diana_DeGette_percent}% ({Diana_DeGette_votes})
Raymon_Anthony_Doane: {Raymon_Anthony_Doane_percent}% ({Raymon_Anthony_Doane_votes})
-----------------------------------
Winner: {winner}
-----------------------------------''')

    file.close()