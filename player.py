class Player:
    """class to represent player and their stats"""

    stats = {}

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

    def generate_stats(self):
        """allow player to generate stats using budget"""
        print("Generate stats")

    def set_stats(self, stats_dict):
        """set player stats"""
        print("Set stats")

    def __init__(self):
        """constructor"""
        super().__init__()

        #get user to select stats
        self.generate_stats()

        #update stats
        self.set_stats({"test":"test"})