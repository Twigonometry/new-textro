from random import randint
import utils

class Player:
    """class to represent player and their stats"""

    #stats dictionary
    #1: strength, 2: dexterity, 3: constitution, 4: intelligence, 5: wisdom, 6: charisma
    stats = {}

    def set_stats_manual(self):
        """let user set stats manually. if user uses up all their budget, set remaining stats to 8"""
        budget = 27
        self.stats = {}

        print("Set your stats below")
        while len(self.stats) < 6:
            if budget == 0:
                #iterate over keys 1 to 6, if no value present set to 8
                print("\nNo budget left, setting remaining stats to 8")
                for i in range(1, 7):
                    if not i in self.stats.keys():
                        self.stats[i] = 8
            else:
                print("\nBudget remaining: ", budget)

                #input validation
                stat_choice = 0
                while stat_choice < 1 or stat_choice > 8:
                    try:
                        stat_choice = int(input("1. Set Strength\n2. Set Dexterity\n3. Set Constitution\n4. Set Intelligence\n5. Set Wisdom\n6. Set Charisma\n7. View point costs\n8. Quit\n"))
                    except:
                        print("Enter an integer between 1 and 8\n")
                
                #assigning stat value
                if stat_choice in self.stats.keys():
                    print("\nStat already assigned")
                elif stat_choice < 7:
                    stat_value = 0
                    while stat_value < 8 or stat_value > 15:
                        try:
                            stat_value = int(input("\nAssign a " + utils.stats_name_map[stat_choice] + " score between 8 & 15\n"))
                        except:
                            print("Enter an integer between 8 and 15\n")
                    stat_cost = utils.score_costs[stat_value]
                    if stat_cost <= budget:
                        self.stats[stat_choice] = stat_value
                        budget -= stat_cost
                elif stat_choice == 7:
                    utils.display_costs()
                else:
                    break
        
        if len(self.stats) == 6:
            print("\nStats:")
            for i in range(1, 7):
                print(utils.stats_name_map[i] + ": " + str(self.stats[i]))

    def roll_4d6(self):
        """roll 4d6, drop the lowest. if total < 8, reroll"""
        rolls = []
        for i in range(4):
            rolls.append(randint(1,6))
        #print("4 rolls: ", rolls)
        rolls.remove(min(rolls))
        #print("3 highest: ", rolls)
        if sum(rolls) < 8:
            #print("Too low, reroll!")
            rolls = self.roll_4d6()
        return rolls

    def set_stats_random(self):
        """roll for user stats"""
        print("Rolling for stats...")
        self.stats = {}
        for i in range(1, 7):
            self.stats[i] = sum(self.roll_4d6())
            print(utils.stats_name_map[i] + ": " + str(self.stats[i]))

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