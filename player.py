class Player:
    """class to represent player and their stats"""

    stats = {}

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