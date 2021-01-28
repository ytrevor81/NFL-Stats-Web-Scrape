from Players import *
from Urls import *
from Scraper_Functions.Gather_Player_Urls import Individual_Player_Links
from Scraper_Functions.CSV_Handler import Create_CSV_Player_Urls


Urls = Urls()
Player = Player()

Create_CSV_Player_Urls("Active_Player_Urls.csv", "Retired_Player_Urls.csv")

count = 1
for link in Urls.search_for_active_players:
    Individual_Player_Links(link, "Active_Player_Urls.csv")
    print('Processed pics for %d out of %d links' % (count, len(Urls.search_for_active_players)))
    count+=1



#This will begin the scraper store data in csv
