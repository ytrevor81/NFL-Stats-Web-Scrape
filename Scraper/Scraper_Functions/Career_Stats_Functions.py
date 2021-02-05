import bs4
from Players import Player_CareerStats
from Scraper_Functions.Gather_Player_Urls import Get_HTML_Document
from Scraper_Functions.CSV_Handler import Write_Career_Stats

def Category_List(player_class, soup):
    ''' Returns ["Passing", "Rushing", ...] '''
    table_title_tags = soup.find_all('h3', {'class': "d3-o-section-sub-title"})
    if len(table_title_tags) == 0:
        player_class.has_stats = False
        return False
    else:
        category_list = [x.text.replace('\n', '').replace(' ', '') for x in table_title_tags]
        return category_list

def Player_Stats(link, player_class, table_soup):
    ''' Returns a list of lists of lists, separated by category and stats within those categories '''
    if player_class.has_stats == False:
        return False
    else:
        player_class.Get_Player_Id(link)
        all_player_data = []
        for table in table_soup:
            rows = table.find_all('tr')
            table_foot = table.find_all('tfoot')
            list_data_row = []
            for row in rows:
                list_of_lists = row.find_all('td')
                list_data_row.append(list_of_lists)
            for career_total in table_foot:
                list_of_career_total_lists = career_total.find_all('th')
                list_data_row.append(list_of_career_total_lists)
            remove_empty_lists = []
            for x in list_data_row:
                if len(x) > 0:
                    remove_empty_lists.append(x)
            player_data = []
            for x in remove_empty_lists:
                text_from_table = [i.text.replace("\n", "").replace(" ", "") for i in x]
                input_player_id = [player_class.player_id] + text_from_table
                player_data.append(input_player_id)
            all_player_data.append(player_data)
        return all_player_data

def Populate_Empty_Element(stats_list):
    populated_list = []
    for list in stats_list:
        populate = ["--" if stat == "" else stat for stat in list]
        populated_list.append(populate)
    return populated_list

def Assign_To_Player_Class(link, player_class, categories_list, player_stats_list):
    if player_class.has_stats:
        categories_with_stats = zip(categories_list, player_stats_list)
        for category_with_stats in categories_with_stats:
            category = category_with_stats[0]
            stats = Populate_Empty_Element(category_with_stats[1]) #if element is '', change to '--'
            if category == "Passing":
                player_class.passing = stats
            elif category == "Rushing":
                player_class.rushing = stats
            elif category == "Receiving":
                player_class.receiving = stats
            elif category == "Fumbles":
                player_class.fumbles = stats
            elif category == "Defense":
                player_class.defense = stats
            elif category == "Kicking":
                player_class.kicking = stats
            elif category == "Punting":
                player_class.punting = stats
            elif category == "KickReturn":
                player_class.kickreturns = stats
            elif category == "PuntReturn":
                player_class.puntreturns = stats
    else:
        pass

def Get_Table_Soup(player_class, soup): #this grabs each table on a player's stats webpage (ex: https://www.nfl.com/players/tom-brady/stats/)
    tables = soup.find_all('div', {'class': "d3-o-table--horizontal-scroll"})
    if len(tables) == 0:
        player_class.has_stats = False
        return False
    else:
        return tables

def Extract_Career_Stats(link, passingfilename, rushingfilename, receivingfilename, fumblesfilename, defensefilename, kickingfilename, puntingfilename, kickreturnsfilename, puntreturnsfilename):
    Player = Player_CareerStats() #initialize Player_CareerStats class each time a new player is processed
    soup = Get_HTML_Document(link)
    categories = Category_List(Player, soup)
    tables = Get_Table_Soup(Player, soup)
    player_stats = Player_Stats(link, Player, tables)
    Assign_To_Player_Class(link, Player, categories, player_stats)
    Write_Career_Stats(Player, passingfilename, rushingfilename, receivingfilename, fumblesfilename, defensefilename, kickingfilename, puntingfilename, kickreturnsfilename, puntreturnsfilename)
