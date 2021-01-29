import bs4
from Players import *
from Scraper_Functions.Gather_Player_Urls import Get_HTML_Document
#from Scraper_Functions.CSV_Handler import Write_Active_Player_Basic_Stats, Write_Retired_Player_Basic_Stats

ActivePlayer = ActivePlayer()
RetiredPlayer = RetiredPlayer()




def Extract_Basic_Stats(link, filename):
    soup = Get_HTML_Document(link)
    print(soup)
