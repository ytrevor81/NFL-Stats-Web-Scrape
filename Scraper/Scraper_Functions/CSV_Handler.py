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
