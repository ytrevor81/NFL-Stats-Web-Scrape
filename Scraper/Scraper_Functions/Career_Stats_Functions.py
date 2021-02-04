import bs4
from Players import Player_CareerStats
from Scraper_Functions.Gather_Player_Urls import Get_HTML_Document
from Scraper_Functions.CSV_Handler import Write_Career_Stats

Player = Player_CareerStats()

def Category_List(soup):
    ''' Returns ["Passing", "Rushing", ...] '''
    table_title_tags = soup.find_all('h3', {'class': "d3-o-section-sub-title"})
    category_list = [x.text.replace('\n', '').replace(' ', '') for x in table_title_tags]
    return category_list

def Class_List(table_soup):
    raw_class_list = []
    data_columns = table_soup.find_all_next('td')
    for x in data_columns:
        raw_class_list.append(x['class'])
    flat_list = []
    for sublist in raw_class_list:
        for item in sublist:
            flat_list.append(item)
    class_list = [flat_list[i] for i in range(len(flat_list)) if flat_list[i] != flat_list[i - 1]]
    return class_list

def Player_Stats(table_soup):
    ''' Returns a list of lists of lists, separated by category and stats within those categories '''
    all_player_data = []
    for table in table_soup:
        rows = table.find_all('tr')
        list_data_row = []
        for row in rows:
            list_of_lists = row.find_all('td')
            list_data_row.append(list_of_lists)
        remove_empty_lists = []
        for x in list_data_row:
            if len(x) > 0:
                remove_empty_lists.append(x)
        player_data = []
        for x in remove_empty_lists:
            text_from_table = [i.text.replace("\n", "").replace(" ", "") for i in x]
            player_data.append(text_from_table)
        all_player_data.append(player_data)
    return all_player_data

def Populate_Empty_Element(stats_list):
    populated_list = []
    for list in stats_list:
        populate = ["--" if stat == "" else stat for stat in list]
        populated_list.append(populate)
    return populated_list

def Stat_Category_Dictionary(title_list, player_stats_list):
    pass

def Extract_Career_Stats(link, passingfilename, rushingfilename, receivingfilename, fumblesfilename, defensefilename, kickingfilename, puntingfilename, kickreturnsfilename, puntreturnsfilename):
    soup = Get_HTML_Document(link)
    categories = Category_List(soup)
    print(categories)
    tables = soup.find_all('div', {'class': "d3-o-table--horizontal-scroll"})
    player_stats = Player_Stats(tables)
    print(len(player_stats))

    categories_with_stats = zip(categories, player_stats)
    for category_with_stats in categories_with_stats:
        category = category_with_stats[0]
        stats = Populate_Empty_Element(category_with_stats[1]) #if element is '', change to '--'
        if category == "Defense":
            Player.defense = stats
        elif category == "Fumbles":
            Player.fumbles = stats
    Write_Career_Stats(Player, passingfilename, rushingfilename, receivingfilename, fumblesfilename, defensefilename, kickingfilename, puntingfilename, kickreturnsfilename, puntreturnsfilename)
