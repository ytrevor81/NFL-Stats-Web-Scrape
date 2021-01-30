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
        writer.writerow(['Player_Id', 'Full_Name', 'Position', 'Teams_Played_On', 'Height', 'Weight', 'Experience', 'Age', 'College', 'Hall_Of_Fame'])

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
