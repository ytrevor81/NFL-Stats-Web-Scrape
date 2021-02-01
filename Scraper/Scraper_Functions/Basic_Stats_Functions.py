import bs4
from Players import *
from Scraper_Functions.Gather_Player_Urls import Get_HTML_Document
from Scraper_Functions.CSV_Handler import Write_ActivePlayer_Basic_Stats, Write_RetiredPlayer_Basic_Stats

ActivePlayer = ActivePlayer()
RetiredPlayer = RetiredPlayer()

def Store_Values_for_ActivePlayer(name, team, link, div_tag_position_number, div_soup_list):
    ActivePlayer.name = name
    ActivePlayer.team = team
    ActivePlayer.Get_Player_Id(link)
    ActivePlayer.Get_Position_and_Number(div_tag_position_number)
    ActivePlayer.Get_ActivePlayer_Basic_Stats_From_Soup_List(div_soup_list)

def Store_Values_for_RetiredPlayer(div_hof_tag, name, link, div_tag_position, div_soup_list):
    RetiredPlayer.In_Hall_Of_Fame(div_hof_tag)
    RetiredPlayer.name = name
    RetiredPlayer.Get_Player_Id(link)
    RetiredPlayer.Get_Position(div_tag_position)
    RetiredPlayer.Get_RetiredPlayer_Basic_Stats_From_Soup_List(div_soup_list)

def Extract_ActivePlayer_Basic_Stats(link, filename):
    soup = Get_HTML_Document(link)
    h1_tag_fullname = soup.find('h1', {'class': "nfl-c-player-header__title"}) #filters only <h1> tags
    div_tag_position_number = soup.find('div', {'class': "nfl-c-player-header__player-data nfl-u-hide-empty"}) #filters only <span> tags
    anchor_tag_team = soup.find('a', {'class': "nfl-o-cta--link"}) #filters only <a> tags
    div_tag_basicstats = soup.find_all('div', {'class': "nfl-c-player-info__value"}) #filters only <div> tags

    player_team = ActivePlayer.NoneType_HTMLText_Error_Handler(anchor_tag_team)

    Store_Values_for_ActivePlayer(h1_tag_fullname.text, player_team, link, div_tag_position_number, div_tag_basicstats)
    Write_ActivePlayer_Basic_Stats(ActivePlayer, filename)

def Extract_RetiredPlayer_Basic_Stats(link, filename):
    soup = Get_HTML_Document(link)
    div_hof_tag = soup.find('div', {'class': "nfl-c-player-header__career-status nfl-u-hide-empty"}) #filters only <h1> tags
    h1_tag_fullname = soup.find('h1', {'class': "nfl-c-player-header__title"}) #filters only <h1> tags
    div_tag_position = soup.find('div', {'class': "nfl-c-player-header__player-data nfl-u-hide-empty"}) #filters only <span> tags
    div_tag_basicstats = soup.find_all('div', {'class': "nfl-c-player-info__value"}) #filters only <div> tags

    Store_Values_for_RetiredPlayer(div_hof_tag, h1_tag_fullname.text, link, div_tag_position, div_tag_basicstats)
    Write_RetiredPlayer_Basic_Stats(RetiredPlayer, filename)

def Extract_Basic_Stats(link, filename):
    if filename == "Active_Player_Basic_Stats.csv":
        Extract_ActivePlayer_Basic_Stats(link, filename)
    elif filename == "Retired_Player_Basic_Stats.csv":
        Extract_RetiredPlayer_Basic_Stats(link, filename)
