import csv
#All Urls used for scraping

class Urls(object):
    def __init__(self):
        self.search_for_active_players = ["https://www.nfl.com/players/active/a", "https://www.nfl.com/players/active/a?query=a&after=c2ltcGxlLWN1cnNvcjk5",
        "https://www.nfl.com/players/active/b", "https://www.nfl.com/players/active/b?query=b&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/b?query=b&after=c2ltcGxlLWN1cnNvcjE5OQ==",
        "https://www.nfl.com/players/active/c", "https://www.nfl.com/players/active/c?query=c&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/c?query=c&after=c2ltcGxlLWN1cnNvcjE5OQ==",
        "https://www.nfl.com/players/active/d", "https://www.nfl.com/players/active/d?query=d&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/e", "https://www.nfl.com/players/active/f",
        "https://www.nfl.com/players/active/f?query=f&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/g", "https://www.nfl.com/players/active/g?query=g&after=c2ltcGxlLWN1cnNvcjk5",
        "https://www.nfl.com/players/active/h", "https://www.nfl.com/players/active/h?query=h&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/h?query=h&after=c2ltcGxlLWN1cnNvcjE5OQ==",
        "https://www.nfl.com/players/active/i", "https://www.nfl.com/players/active/j", "https://www.nfl.com/players/active/j?query=j&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/k",
        "https://www.nfl.com/players/active/l", "https://www.nfl.com/players/active/l?query=l&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/m", "https://www.nfl.com/players/active/m?query=m&after=c2ltcGxlLWN1cnNvcjk5",
        "https://www.nfl.com/players/active/m?query=m&after=c2ltcGxlLWN1cnNvcjE5OQ==", "https://www.nfl.com/players/active/n", "https://www.nfl.com/players/active/o", "https://www.nfl.com/players/active/p",
        "https://www.nfl.com/players/active/p?query=p&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/q", "https://www.nfl.com/players/active/r", "https://www.nfl.com/players/active/r?query=r&after=c2ltcGxlLWN1cnNvcjk5",
        "https://www.nfl.com/players/active/s", "https://www.nfl.com/players/active/s?query=s&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/s?query=s&after=c2ltcGxlLWN1cnNvcjE5OQ==",
        "https://www.nfl.com/players/active/t", "https://www.nfl.com/players/active/t?query=t&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/u", "https://www.nfl.com/players/active/v",
        "https://www.nfl.com/players/active/w", "https://www.nfl.com/players/active/w?query=w&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/active/w?query=w&after=c2ltcGxlLWN1cnNvcjE5OQ==",
        "https://www.nfl.com/players/active/x", "https://www.nfl.com/players/active/y", "https://www.nfl.com/players/active/z"]
        self.base_retired_players = "https://www.nfl.com/players/retired/"

    def retired_search_url_builder(self): #impossible to manually place all retired player's search urls in a list, so this will process them
        pass

    def search_for_retired_players(self): #returns a list of processed retired players search urls
        #self.retired_search_url_builder()
        #return list
        pass

    def basic_stats_urls(self): #Read urls from csv file and return a list of urls
    #return list
        pass

    def stats_urls(self): #Read urls from csv file and return a list of urls AND ADDS STATS AS AN EXTRA ENDPOINT
    #return list
        pass
