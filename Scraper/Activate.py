from Players import *
from Urls import *
from Scraper_Functions.Gather_Player_Urls import *

Urls = Urls()
Player = Player()

with open("Player_Urls.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Player_URL'])

Individual_Player_Links(Urls.search_for_active_players[0], "Player_Urls.csv") #THIS WILL BE DONE IN A FOR LOOP, SO PRINT SOME MESSAGES WHEN FULL PROCESS BEGINS


#This will begin the scraper store data in csv
