from Players import *
from Urls import *
from Scraper_Functions.Gather_Player_Urls import *

Urls = Urls()
Player = Player()

print(Get_HTML_Document(Urls.search_for_active_players[0]))


#This will begin the scraper store data in csv
