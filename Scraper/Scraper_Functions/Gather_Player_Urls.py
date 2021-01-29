import bs4, requests
from Scraper_Functions.CSV_Handler import Write_Player_Links

def Get_HTML_Document(url):
    try:
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        return soup
    except Exception as e:
        print("Error: " + str(e))

def Extract_Individual_Player_Links(url, filename):
    links = [] #useable links will be placed in here
    soup = Get_HTML_Document(url) #raw HTML source code od Url
    anchor_tags = soup.find_all('a', {'class': "d3-o-player-fullname nfl-o-cta--link"}) #filters only <a> tags
    for tag in anchor_tags:
        complete_link = "https://www.nfl.com" + tag['href'] #extracts the raw link in each <a> tag
        links.append(complete_link)
    Write_Player_Links(filename, links)
