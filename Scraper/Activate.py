from Urls import *
from Scraper_Functions.Gather_Player_Urls import Extract_Individual_Player_Links
from Scraper_Functions.CSV_Handler import Create_CSV_Player_Urls, Create_CSV_Basic_Stats
from Scraper_Functions.Basic_Stats_Functions import Extract_Basic_Stats


Urls = Urls()

#active_player_query_links = Urls.active_player_query_links
#retired_player_query_links = Urls.retired_player_query_links


## ---- CSV File Creation Functions ---- ##
#Create_CSV_Player_Urls("Active_Player_Urls.csv", "Retired_Player_Urls.csv") #Create your file name in the parameters of the following functions
Create_CSV_Basic_Stats("Active_Player_Basic_Stats.csv", "Retired_Player_Basic_Stats.csv")
## ---- ---- ##

#count = 1
#for link in active_player_search_links:
#    Extract_Individual_Player_Links(link, "Active_Player_Urls.csv")
#    print('Stored active player links for %d out of %d query links' % (count, len(active_player_search_links)))
#    count+=1

#count = 1
#for link in retired_player_search_links:
#    Extract_Individual_Player_Links(link, "Retired_Player_Urls.csv")
#    print('Stored retired player links for %d out of %d query links' % (count, len(retired_player_search_links)))
#    count+=1

#individual_active_player_links = Urls.basic_stats_urls("Active_Player_Urls.csv") #list of all player urls
#individual_retired_player_links = Urls.basic_stats_urls("Retired_Player_Urls.csv")
#individual_active_player_stats_links = Urls.stats_urls(individual_active_player_links)
#individual_retired_player_stats_links = Urls.stats_urls(individual_retired_player_links)



for link in ["https://www.nfl.com/players/kurt-warner/", "https://www.nfl.com/players/al-applegate/", "https://www.nfl.com/players/joe-namath/", "https://www.nfl.com/players/a-j-greene/", "https://www.nfl.com/players/bill-gutteron/"]:
    Extract_Basic_Stats(link, "Retired_Player_Basic_Stats.csv")

#count = 1
#for link in individual_active_player_links:
#    Extract_Basic_Stats(link, "Active_Player_Basic_Stats.csv")
#    if count % 100 == 0:
#        print('Basic stats completed for %d out of %d active players' % (count, len(individual_active_player_links)))
#    count+=1

#count = 1
#for link in individual_retired_player_links:
#    Extract_Basic_Stats(link, "Retired_Player_Basic_Stats.csv")
#    if count % 100 == 0:
#        print('Basic stats completed for %d out of %d retired players' % (count, len(retired_player_search_links)))
#    count+=1
