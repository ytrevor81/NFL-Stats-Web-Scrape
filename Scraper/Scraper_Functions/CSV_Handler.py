import csv

def Write_Player_Links(filename, links_list): #only for base player url links
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        for link in links_list:
            writer.writerow([link])

def Create_CSV_Player_Urls(filename1, filename2):
    with open(filename1, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Active_Player_Url'])
    with open(filename2, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Retired_Player_Url'])

def Create_CSV_Basic_Stats(filename1, filename2):
    with open(filename1, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Full_Name', 'Position', 'Number', 'Current_Team', 'Height', 'Weight', 'Experience', 'Age', 'College'])
    with open(filename2, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Full_Name', 'Position', 'Height', 'Weight', 'College', 'Hall_Of_Fame'])

def Create_CSV_Career_Stats(filename1, filename2):
    with open(filename1, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Active_Player_Url'])
    with open(filename2, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Retired_Player_Url'])

def Create_CSV_Player_Career_Stats(passingfile, rushingfile, receivingfile, fumblesfile, defensefile, kickingfile, puntingfile, kickreturnsfile, puntreturnsfile):
    '''Each player's total combined stats will be the last input, but the year will be 'Total', and Team will be --'''
    with open(passingfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Year', 'Team', 'Games_Played', 'Attempts', 'Completions', 'Completion_Percentage', 'Yards', 'Average', 'Long', 'TDs', 'INTs', 'First_Downs', 'First_Down_Percentage', 'Passes_Over_Twenty_Yards', 'Passes_Over_Forty_Yards', 'Sacks', 'Sack_Yards', 'Passer_Rating'])
    with open(rushingfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Year', 'Team', 'Games_Played', 'Attempts', 'Yards', 'Average', 'Long', 'TDs', 'First_Downs', 'First_Down_Percentage', 'Rushes_Over_Twenty_Yards', 'Rushes_Over_Forty_Yards', 'Fumbles'])
    with open(receivingfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Year', 'Team', 'Games_Played', 'Receptions', 'Yards', 'Average', 'Long', 'TDs', 'First_Downs', 'First_Down_Percentage', 'Receptions_Over_Twenty_Yards', 'Receptions_Over_Forty_Yards'])
    with open(fumblesfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Year', 'Team', 'Games_Played', 'Fumbles', 'Fumbles_Lost', 'Forced_Fumbles', 'Own_Recovery', 'Opposing_Recovery', 'TDs'])
    with open(defensefile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Year', 'Team', 'Games_Played', 'Tackles', 'Solo_Tackles', 'Assisted_Tackles', 'Sacks', 'Sack_Yards', 'Safties', 'Passes_Deflected', 'INTs', 'TDs', 'INT_Yards', 'Average', 'Long'])
    with open(kickingfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Year', 'Team', 'Games_Played', 'Kicks_1_to_19_Yards', 'Kicks_20_to_29_Yards', 'Kicks_30_to_39_Yards', 'Kicks_40_to_49_Yards', 'Kicks_Over_50', 'FGs', 'FG_Attempts', 'Percentage'])
    with open(puntingfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Year', 'Team', 'Games_Played', 'Punts', 'Yards', 'Long', 'Average', 'Punts_Blocked', 'Returns', 'Return_Yards', 'Punts_In_20', 'Net_Average'])
    with open(kickreturnsfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Year', 'Team', 'Games_Played', 'Returns', 'Yards', 'Average', 'Long', 'TDs', 'Returns_Over_Twenty_Yards', 'Returns_Over_Forty_Yards', 'Fair_Catches', 'Fumbles'])
    with open(puntreturnsfile, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Player_Id', 'Year', 'Team', 'Games_Played', 'Returns', 'Yards', 'Average', 'Long', 'TDs', 'Returns_Over_Twenty_Yards', 'Returns_Over_Forty_Yards', 'Fair_Catches', 'Fumbles'])

def CSV_Url_List(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        return [x for i in reader for x in i]

def Write_ActivePlayer_Basic_Stats(player_class, filename):
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([player_class.player_id,
                         player_class.name,
                         player_class.position,
                         player_class.number,
                         player_class.team,
                         player_class.height,
                         player_class.weight,
                         player_class.experience,
                         player_class.age,
                         player_class.college])


def Write_RetiredPlayer_Basic_Stats(player_class, filename):
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([player_class.player_id,
                         player_class.name,
                         player_class.position,
                         player_class.height,
                         player_class.weight,
                         player_class.college,
                         player_class.hall_of_fame])

def Write_Career_Stats(player_class, passingfilename, rushingfilename, receivingfilename, fumblesfilename, defensefilename, kickingfilename, puntingfilename, kickreturnsfilename, puntreturnsfilename):
    pass
