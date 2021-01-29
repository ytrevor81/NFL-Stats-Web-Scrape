import csv, bs4, re

class ActivePlayer(object):
    def __init__(self):
        self.name = None
        self.player_id = None
        self.experience = None
        self.number = None
        self.position = None
        self.team = None
        self.height = None
        self.weight = None
        self.age = None
        self.college = None

class RetiredPlayer(ActivePlayer):
    def __init__(self):
        self.hall_of_fame = False
