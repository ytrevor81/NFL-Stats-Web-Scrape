import bs4
from Players import *
from Scraper_Functions.Gather_Player_Urls import Get_HTML_Document
from Scraper_Functions.CSV_Handler import Write_Active_Player_Basic_Stats

ActivePlayer = ActivePlayer()
RetiredPlayer = RetiredPlayer()

def Get_Basic_Stats_From_Soup_List(soup_list):
    html_text_list = []
    for tag in soup_list:
        html_text_list.append(tag.text)
    return html_text_list

def Get_Player_Id(link):
    player_id_tuple = link.partition("https://www.nfl.com/players/")
    player_id = player_id_tuple[2].replace("/", "")
    return player_id

def Get_Position_and_Number(soup_tag):
    remove_link_breaks_and_dot = soup_tag.replace("\n", "").replace("•", "").replace(" ", "")
    position_number_tuple = remove_link_breaks_and_dot.partition("#")
    position = position_number_tuple[0] #'QB'
    number = position_number_tuple[1] + position_number_tuple[2] #'#17'
    return [position, number] #['QB', '#17']


def Extract_Basic_Stats(link, filename):
    soup = Get_HTML_Document(link)
    h1_tag_fullname = soup.find('h1', {'class': "nfl-c-player-header__title"}) #filters only <h1> tags
    div_tag_position_number = soup.find('div', {'class': "nfl-c-player-header__player-data nfl-u-hide-empty"}) #filters only <span> tags
    anchor_tag_team = soup.find('a', {'class': "nfl-o-cta--link"}) #filters only <a> tags
    div_tag_basicstats = soup.find_all('div', {'class': "nfl-c-player-info__value"}) #filters only <div> tags

    position_and_number = Get_Position_and_Number(div_tag_position_number.text)
    basic_stats_list = Get_Basic_Stats_From_Soup_List(div_tag_basicstats)

    ActivePlayer.player_id = Get_Player_Id(link)
    ActivePlayer.name = h1_tag_fullname.text
    ActivePlayer.team = anchor_tag_team.text
    ActivePlayer.position = position_and_number[0]
    ActivePlayer.number = position_and_number[1]
    ActivePlayer.height = basic_stats_list[0]
    ActivePlayer.weight = basic_stats_list[1]
    ActivePlayer.experience = basic_stats_list[4] + " years"
    ActivePlayer.age = basic_stats_list[6]
    ActivePlayer.college = basic_stats_list[5]

    Write_Active_Player_Basic_Stats(ActivePlayer)
