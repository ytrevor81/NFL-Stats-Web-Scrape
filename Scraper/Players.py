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

    def NoneType_HTMLText_Error_Handler(self, soup_tag):
        '''Returns '--' if no text is present in the html tag, as to avoid an error'''
        try:
            no_error = soup_tag.text
            return no_error
        except AttributeError:
            return "--"

    def Get_Player_Id(self, link):
        player_id_tuple = link.partition("https://www.nfl.com/players/")
        player_id = player_id_tuple[2].replace("/", "")
        self.player_id = player_id

    def Get_Position_and_Number(self, soup_tag):
        soup_text = self.NoneType_HTMLText_Error_Handler(soup_tag)
        if soup_text == "--":
            self.position = "--"
            self.number = "--"
        else:
            remove_line_breaks_and_dot = soup_text.replace("\n", "").replace("•", "").replace(" ", "")
            position_number_tuple = remove_line_breaks_and_dot.partition("#")
            position = position_number_tuple[0] #'QB'
            number = position_number_tuple[1] + position_number_tuple[2] #'#17'
            self.position = position
            self.number = number

    def Get_ActivePlayer_Basic_Stats_From_Soup_List(self, soup_list):
        basic_stats_list = []
        for stat in soup_list:
            basic_stats_list.append(stat.text)
        self.height = basic_stats_list[0]
        self.weight = basic_stats_list[1]
        self.experience = basic_stats_list[4] + " years"
        self.age = basic_stats_list[6]
        self.college = basic_stats_list[5]


class RetiredPlayer(ActivePlayer):
    def __init__(self):
        self.hall_of_fame = None

    def Get_Position(self, soup_tag):
        soup_text = self.NoneType_HTMLText_Error_Handler(soup_tag)
        if soup_text == "--":
            self.position = "--"
        else:
            position = soup_text.replace("\n", "").replace(" ", "")
            if position == "":
                self.position = "--"
            else:
                self.position = position

    def Get_RetiredPlayer_Basic_Stats_From_Soup_List(self, soup_list):
        basic_stats_list = []
        for tag in soup_list:
            stat = self.NoneType_HTMLText_Error_Handler(tag)
            if stat == "" or stat == " years":
                stat = "--"
            basic_stats_list.append(stat)
        self.height = basic_stats_list[0]
        self.weight = basic_stats_list[1]
        self.college = basic_stats_list[5]

    def In_Hall_Of_Fame(self, div_hof_tag):
        hall_of_fame_status = self.NoneType_HTMLText_Error_Handler(div_hof_tag)
        if hall_of_fame_status == "HALL OF FAME":
            self.hall_of_fame = "True"
        else:
            self.hall_of_fame = "False"
