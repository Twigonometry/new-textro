from random import randint
import utils

class Player:
    """class to represent player and their stats"""

    #abilities dictionary
    #1: strength, 2: dexterity, 3: constitution, 4: intelligence, 5: wisdom, 6: charisma
    abils = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    #skills dictionaries for each ability. boolean value represents whether player is trained in skill
    str_skills = {
        "MELEE": False,
        "CLIMBING": False
    }

    dex_skills = {
        "RANGED": False,
        "STEALTH": False
    }

    int_skills = {
        "INVESTIGATION": False,
        "HISTORY": False
    }

    wis_skills = {
        "SURVIVAL": False,
        "INSIGHT": False,
        "PERCEPTION": False,
        "MEDICINE": False
    }

    cha_skills = {
        "INTIMIDATION": False,
        "DECEPTION": False,
        "PERSUASION": False,
        "PERFORMANCE": False
    }

    #other statistics
    health = 0
    disease_resistance = 0
    speed = 0
    carry_cap = 0

    def set_abils_manual(self):
        """let user set ability scores manually
        if user uses up all their budget, set remaining scores to 8"""
        budget = 27
        self.abils = {}

        print("\nSet your ability scores below")
        while len(self.abils) < 6:
            if budget == 0:
                #iterate over keys 1 to 6, if no value present set to 8
                print("\nNo budget left, setting remaining ability scores to 8")
                for i in range(1, 7):
                    if not i in self.abils.keys():
                        self.abils[i] = 8
            else:
                print("\nBudget remaining: ", budget)

                #input validation
                abil_choice = 0
                while abil_choice < 1 or abil_choice > 8:
                    try:
                        abil_choice = int(input("1. Set Strength\n2. Set Dexterity\n3. Set Constitution\n4. Set Intelligence\n5. Set Wisdom\n6. Set Charisma\n7. View point costs\n8. Quit\n"))
                    except:
                        print("Enter an integer between 1 and 8\n")
                
                #assigning ability score
                if abil_choice in self.abils.keys():
                    print("\nAbility score already assigned")
                elif abil_choice < 7:
                    abil_value = 0
                    while abil_value < 8 or abil_value > 15:
                        try:
                            abil_value = int(input("\nAssign a " + utils.abils_name_map[abil_choice] + " score between 8 & 15\n"))
                        except:
                            print("Enter an integer between 8 and 15\n")
                    abil_cost = utils.score_costs[abil_value]
                    if abil_cost <= budget:
                        self.abils[abil_choice] = abil_value
                        budget -= abil_cost
                elif abil_choice == 7:
                    utils.display_costs()
                else:
                    break
        
        if len(self.abils) == 6:
            print("\nAbility scores:")
            for i in range(1, 7):
                print(utils.abils_name_map[i] + ": " + str(self.abils[i]))

    def roll_4d6(self):
        """roll 4d6, drop the lowest. if total < 8, reroll"""
        rolls = []

        #roll die
        for i in range(4):
            rolls.append(randint(1,6))

        #drop lowest and reroll
        rolls.remove(min(rolls))
        if sum(rolls) < 8:
            rolls = self.roll_4d6()
            
        return rolls

    def set_abils_random(self):
        """roll for user ability scores"""
        print("Rolling for ability scores...")
        self.abils = {}
        for i in range(1, 7):
            self.abils[i] = sum(self.roll_4d6())
            print(utils.abils_name_map[i] + ": " + str(self.abils[i]))

    def abils_choice(self):
        """set player ability scores"""
        print("Here you can assign your ability scores")
        method = ""
        while method != "1" and method != "2":
            method = input("1. Assign manually\n2. Assign randomly\n")
        if method == "1":
            self.set_abils_manual()
        else:
            self.set_abils_random()

    def __init__(self):
        """constructor"""
        super().__init__()

        #assign ability scores
        self.abils_choice()