from Urls import *
from Scraper_Functions.Gather_Player_Urls import Extract_Individual_Player_Links
from Scraper_Functions.CSV_Handler import Create_CSV_Player_Urls, Create_CSV_Basic_Stats, Create_CSV_Player_Career_Stats
from Scraper_Functions.Basic_Stats_Functions import Extract_Basic_Stats
from Scraper_Functions.Career_Stats_Functions import Extract_Career_Stats


## ---- Create Urls object and fetch all query links for active and retired players. This is required to begin downloading individual player links ---- ##
Urls = Urls()
active_player_query_links = Urls.active_player_query_links #These query links are needed to download individual player links
retired_player_query_links = Urls.retired_player_query_links
## ---- ---- ##


## ---- CSV File Creation Functions ---- ##
Create_CSV_Player_Urls("Active_Player_Urls.csv", "Retired_Player_Urls.csv") #Create your file name in the parameters of the following functions
Create_CSV_Basic_Stats("Active_Player_Basic_Stats.csv", "Retired_Player_Basic_Stats.csv")
Create_CSV_Player_Career_Stats("ActivePlayer_Passing_Stats.csv",
                                     "ActivePlayer_Rushing_Stats.csv",
                                     "ActivePlayer_Receiving_Stats.csv",
                                     "ActivePlayer_Fumbles_Stats.csv",
                                     "ActivePlayer_Defense_Stats.csv",
                                     "ActivePlayer_Kicking_Stats.csv",
                                     "ActivePlayer_Punting_Stats.csv",
                                     "ActivePlayer_KickReturns_Stats.csv",
                                     "ActivePlayer_PuntReturns_Stats.csv")
Create_CSV_Player_Career_Stats("RetiredPlayer_Passing_Stats.csv",
                                     "RetiredPlayer_Rushing_Stats.csv",
                                     "RetiredPlayer_Receiving_Stats.csv",
                                     "RetiredPlayer_Fumbles_Stats.csv",
                                     "RetiredPlayer_Defense_Stats.csv",
                                     "RetiredPlayer_Kicking_Stats.csv",
                                     "RetiredPlayer_Punting_Stats.csv",
                                     "RetiredPlayer_KickReturns_Stats.csv",
                                     "RetiredPlayer_PuntReturns_Stats.csv")
## ---- ---- ##


## ---- Storing all individual player links, in order to later access their basic stats and career stats ---- ##
count = 1
print("Downloading query links for active players...wait for message after 100 links have been processed")
for link in active_player_search_links:
    Extract_Individual_Player_Links(link, "Active_Player_Urls.csv")
    print('Stored active player links for %d out of %d query links' % (count, len(active_player_search_links)))
    count+=1

count = 1
print("Downloading query links for retired players...wait for message after 100 links have been processed")
for link in retired_player_search_links:
    Extract_Individual_Player_Links(link, "Retired_Player_Urls.csv")
    print('Stored retired player links for %d out of %d query links' % (count, len(retired_player_search_links)))
    count+=1
## ---- ---- ##


## ---- Fetching all player links into a usable list: First, the their initial link is used to fetch basic stats. Then, we need to add a '/stats/ endpoint to each link to process career stats ---- ##
individual_active_player_links = Urls.basic_stats_urls("Active_Player_Urls.csv") #list of all player urls. Example: "https://www.nfl.com/players/deshaun-watson/"
individual_retired_player_links = Urls.basic_stats_urls("Retired_Player_Urls.csv")
individual_active_player_stats_links = Urls.stats_urls(individual_active_player_links) # Example: https://www.nfl.com/players/deshaun-watson/stats/
individual_retired_player_stats_links = Urls.stats_urls(individual_retired_player_links)
## ---- ---- ##


## ---- Storing all individual player basic stats and career ---- ##
count = 1
print("Downloading basic stats for active players...wait for message after 100 players have been processed")
for link in individual_active_player_links:
    Extract_Basic_Stats(link, "Active_Player_Basic_Stats.csv")
    if count % 100 == 0:
        print('Basic stats completed for %d out of %d active players' % (count, len(individual_active_player_links)))
    count+=1

count = 1
print("Downloading basic stats for retired players...wait for message after 100 players have been processed")
for link in individual_retired_player_links:
    Extract_Basic_Stats(link, "Retired_Player_Basic_Stats.csv")
    if count % 100 == 0:
        print('Basic stats completed for %d out of %d retired players' % (count, len(individual_retired_player_links)))
    count+=1

count = 1
print("Downloading career stats for active players...wait for message after 100 players have been processed")
for link in individual_active_player_stats_links:
    Extract_Career_Stats(link,
                         "ActivePlayer_Passing_Stats.csv",
                         "ActivePlayer_Rushing_Stats.csv",
                         "ActivePlayer_Receiving_Stats.csv",
                         "ActivePlayer_Fumbles_Stats.csv",
                         "ActivePlayer_Defense_Stats.csv",
                         "ActivePlayer_Kicking_Stats.csv",
                         "ActivePlayer_Punting_Stats.csv",
                         "ActivePlayer_KickReturns_Stats.csv",
                         "ActivePlayer_PuntReturns_Stats.csv")
    if count % 100 == 0:
        print('Career stats completed for %d out of %d active players' % (count, len(individual_active_player_stats_links)))
    count+=1

count = 1
print("Downloading career stats for retired players...wait for message after 100 players have been processed")
for link in individual_retired_player_stats_links:
    Extract_Career_Stats(link,
                     "RetiredPlayer_Passing_Stats.csv",
                     "RetiredPlayer_Rushing_Stats.csv",
                     "RetiredPlayer_Receiving_Stats.csv",
                     "RetiredPlayer_Fumbles_Stats.csv",
                     "RetiredPlayer_Defense_Stats.csv",
                     "RetiredPlayer_Kicking_Stats.csv",
                     "RetiredPlayer_Punting_Stats.csv",
                     "RetiredPlayer_KickReturns_Stats.csv",
                     "RetiredPlayer_PuntReturns_Stats.csv")
    if count % 100 == 0:
        print('Career stats completed for %d out of %d retired players' % (count, len(individual_retired_player_stats_links)))
    count+=1
