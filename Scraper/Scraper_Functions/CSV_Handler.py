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
