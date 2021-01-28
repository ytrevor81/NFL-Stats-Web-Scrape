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
        self.search_for_retired_players = ["https://www.nfl.com/players/retired/a", "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjE5OQ==",
        "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjI5OQ==", "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjM5OQ==", "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjQ5OQ==",
        "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjU5OQ==", "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjY5OQ==", "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjc5OQ==",
        "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjg5OQ==", "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjk5OQ==", "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjEwOTk=",
        "https://www.nfl.com/players/retired/a?query=a&after=c2ltcGxlLWN1cnNvcjExOTk=",
        "https://www.nfl.com/players/retired/b", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjE5OQ==",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjI5OQ==", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjM5OQ==", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjQ5OQ==",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjU5OQ==", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjY5OQ==", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjc5OQ==",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjg5OQ==", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjk5OQ==", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjEwOTk=",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjExOTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjEyOTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjEzOTk=",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjE0OTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjE1OTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjE2OTk=",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjE3OTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjE4OTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjE5OTk=",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjIwOTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjIxOTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjIyOTk=",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjIzOTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjI0OTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjI1OTk=",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjI2OTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjI3OTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjI4OTk=",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjI5OTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjMwOTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjMxOTk=",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjMyOTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjMzOTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjM0OTk=",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjM1OTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjM2OTk=", "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjM3OTk=",
        "https://www.nfl.com/players/retired/b?query=b&after=c2ltcGxlLWN1cnNvcjM4OTk=",
        "https://www.nfl.com/players/retired/c", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjE5OQ==",
        "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjI5OQ==", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjM5OQ==", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjQ5OQ==",
        "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjU5OQ==", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjY5OQ==", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjc5OQ==",
        "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjg5OQ==", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjk5OQ==", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjEwOTk=",
        "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjExOTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjEyOTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjEzOTk=",
        "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjE0OTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjE1OTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjE2OTk=",
        "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjE3OTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjE4OTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjE5OTk=",
        "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjIwOTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjIxOTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjIyOTk=",
        "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjIzOTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjI0OTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjI1OTk=",
        "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjI2OTk=", "https://www.nfl.com/players/retired/c?query=c&after=c2ltcGxlLWN1cnNvcjI3OTk=",
        "https://www.nfl.com/players/retired/d", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjE5OQ==",
        "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjI5OQ==", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjM5OQ==", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjQ5OQ==",
        "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjU5OQ==", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjY5OQ==", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjc5OQ==",
        "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjg5OQ==", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjk5OQ==", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjEwOTk=",
        "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjExOTk=", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjEyOTk=", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjEzOTk=",
        "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjE0OTk=", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjE1OTk=", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjE2OTk=",
        "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjE3OTk=", "https://www.nfl.com/players/retired/d?query=d&after=c2ltcGxlLWN1cnNvcjE4OTk=",
        "https://www.nfl.com/players/retired/e", "https://www.nfl.com/players/retired/e?query=e&after=c2ltcGxlLWN1cnNvcjk5", "https://www.nfl.com/players/retired/e?query=e&after=c2ltcGxlLWN1cnNvcjE5OQ==",
        "https://www.nfl.com/players/retired/e?query=e&after=c2ltcGxlLWN1cnNvcjI5OQ==", "https://www.nfl.com/players/retired/e?query=e&after=c2ltcGxlLWN1cnNvcjM5OQ==", "https://www.nfl.com/players/retired/e?query=e&after=c2ltcGxlLWN1cnNvcjQ5OQ==",
        "https://www.nfl.com/players/retired/e?query=e&after=c2ltcGxlLWN1cnNvcjU5OQ==", "https://www.nfl.com/players/retired/e?query=e&after=c2ltcGxlLWN1cnNvcjY5OQ=="]

    def basic_stats_urls(self): #Read urls from csv file and return a list of urls
    #return list
        pass

    def stats_urls(self): #Read urls from csv file and return a list of urls AND ADDS STATS AS AN EXTRA ENDPOINT
    #return list
        pass
