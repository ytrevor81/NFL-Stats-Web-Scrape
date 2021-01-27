import bs4, requests, time

def Get_HTML_Document(url):
    try:
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text,'lxml')
        return soup
    except Exception as e:
        print(e)
