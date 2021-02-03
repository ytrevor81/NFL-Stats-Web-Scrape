import bs4
from Players import Player_CareerStats
from Scraper_Functions.Gather_Player_Urls import Get_HTML_Document
from Scraper_Functions.CSV_Handler import *

'''
HTML Classes for each table on stats pages:

Table Container: <div> nfl-o-roster
Table Title (ex. 'Passing'): <h3> d3-o-section-sub-title
Overall Table: <div> d3-o-table--horizontal-scroll
Year Text: <td> nfl-t-stats__col-? selected
Remaining Column Data: <td> nfl-t-stats__col-?


'''

def Stat_Category_Dictionary(title_list, table_soup_list):
    pass

def passInList(listhere):
       return (', '.join(listhere))

def Extract_Career_Stats(link):
    #make lists in lists, with header being first element of those lists
    ############################ THAT'S IT
    rawclassList = []
    soup = Get_HTML_Document(link)
    table_title_tags = soup.find_all('h3', {'class': "d3-o-section-sub-title"})
    table_titles = [x.text.replace('\n', '').replace(' ', '') for x in table_title_tags]
    print(table_titles)

    table_bodies = soup.find('div', {'class': "d3-o-table--horizontal-scroll"})
    data_columns = table_bodies.find_all_next('td')
    for x in data_columns:
        rawclassList.append(x['class'])
    flat_list = []
    for sublist in rawclassList:
        for item in sublist:
            flat_list.append(item)
    classList = []
    for x in flat_list:
        if x not in classList:
            classList.append(x)
    print(classList) #keep if duplicate after another class
    #EACH CLASS REPRESENTS ITS CORRESPONDING CATEGORY. KEEP THEM IN ORIGINAL ORDER AND LINK WITH A DICTIONARY

    pure_data = table_bodies.find_all('td', {'class': classList[0]})
    rows = table_bodies.find_all('tr')
    list_data_row = []
    for row in rows:
        listiflists = row.find_all('td')
        list_data_row.append(listiflists)
    another_list = []
    for x in list_data_row:
        if len(x) > 0:
            another_list.append(x)
    triple_list_time = []
    for x in another_list:
        text_from_table = [i.text.replace("\n", "").replace(" ", "") for i in x]
        triple_list_time.append(text_from_table)
    print(triple_list_time)

    ############################### THATS IT

    #print([x.text.replace("\n", "").replace(" ", "") for x in list_data_row])




    #raw_text = [x.text for x in pure_data]
    #filtered_text = [x.replace("\n", "").replace(" ", "") for x in raw_text]
    #print(filtered_text)
    #print(len(filtered_text))









    #season_stats_tables = soup.find_all('tbody')
    #experiment = [x.text.replace("\n", ",") for x in season_stats_tables]
    #experiment = [x.split('\n') for x in season_stats_tables]
    #print(experiment)
    #willthiswork = [x.split(',') for x in experiment]

    #print(season_stats_tables)
    #table_row_strings = [x.text.replace('\n', '') for x in season_stats_tables]
    #print(table_row_strings)
    #print([x.text.replace('\n', '').replace(' ', '') for x in season_stats_tables])
    #total_career_stats_tables = soup.select('table tfoot')
    #print([x.text.replace('\n', '').replace(' ', ',') for x in total_career_stats_tables])
    #for table in season_stats_tables:
    #    print(table.text)
    #for table in total_career_stats_tables:
    #    print(table.text)
