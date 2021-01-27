import bs4, requests, time

# NFL does not have stats for all players
def Check_for_Stats_Webpage(player,stats_type):
    profile_url = 'http://www.nfl.com/players/'+player.url_name+"/"
    res = requests.get(profile_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')

    Has_Stats_Page = False
    for div in soup.find_all('div',{'id':'player-profile-tabs'}):
        if stats_type in div.text:
            Has_Stats_Page = True
    return Has_Stats_Page
        
