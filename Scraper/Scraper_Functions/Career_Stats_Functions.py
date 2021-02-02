import bs4
from Players import Player_CareerStats
from Scraper_Functions.Gather_Player_Urls import Get_HTML_Document
from Scraper_Functions.CSV_Handler import *

'''
HTML Classes for each table on stats pages:

Table Container: <div> d3-l-col__col-12 nfl-t-stats--table flex-wrap
Table Title (ex. 'Passing'): <h3> d3-o-section-sub-title
Overall Table: <div> d3-o-table--horizontal-scroll
Year Text: <td> nfl-t-stats__col-? selected
Remaining Column Data: <td> nfl-t-stats__col-?


'''





def Extract_Career_Stats(link):
    #make lists in lists, with header being first element of those lists
    soup = Get_HTML_Document(link)
    season_stats_tables = soup.select('table td')
    print(season_stats_tables)
    total_career_stats_tables = soup.select('table tfoot')
    print(total_career_stats_tables)
    for table in season_stats_tables:
        print(table.text)
    for table in total_career_stats_tables:
        print(table.text)
