class Player:
    """class to represent player and their stats"""

    #stats dictionary
    #1: strength, 2: dexterity, 3: constitution, 4: intelligence, 5: wisdom, 6: charisma
    stats = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    }

    #costs of assigning each score
    score_costs = {
        "8": 0,
        "9": 1,
        "10": 2,
        "11": 3,
        "12": 4,
        "13": 5,
        "14": 7,
        "15": 9
    }

    #modifiers for each score
    score_mods = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 5,
        21: 5,
        22: 6,
        23: 6,
        24: 7,
        25: 7,
        26: 8,
        27: 8,
        28: 9,
        29: 9,
        30: 10
    }

    def display_costs(self):
        print("Costs for each ability score:")
        for score in self.score_costs:
            print(score + ": " + str(self.score_costs[score]))

    def set_stats_manual(self):
        """let user set stats manually"""
        print("Set your stats below")

    def set_stats_random(self):
        """roll for user stats"""
        print("Rolling for stats...")

    def stats_choice(self):
        """set player stats"""
        print("Here you can assign your ability scores")
        method = ""
        while method != "1" and method != "2":
            method = input("1. Assign manually\n2. Assign randomly\n")
        if method == "1":
            self.set_stats_manual()
        else:
            self.set_stats_random()

    def __init__(self):
        """constructor"""
        super().__init__()

        #create user stats
        self.stats_choice()