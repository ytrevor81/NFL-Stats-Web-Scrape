import csv, bs4, re

class Player(object):
    def __init__(self):
        self.name = None
        self.url_name = None
        self.player_id = None
        self.current_status = None
        self.years_played = None
        self.number = None
        self.position = None
