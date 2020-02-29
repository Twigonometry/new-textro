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
    skills = {
        "MELEE": False,
        "CLIMBING": False,
        "RANGED": False,
        "STEALTH": False,
        "INVESTIGATION": False,
        "HISTORY": False,
        "SURVIVAL": False,
        "INSIGHT": False,
        "PERCEPTION": False,
        "MEDICINE": False,
        "INTIMIDATION": False,
        "DECEPTION": False,
        "PERSUASION": False,
        "PERFORMANCE": False
    }

    #other statistics
    health = 0
    speed = 0
    disease_resistance = 0
    carry_cap = 0

    name = ""

    def set_abils_manual(self):
        """let user set ability scores manually;
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
            print("Ability scores assigned!")

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
        print("\nRolling for ability scores...")
        self.abils = {}
        for i in range(1, 7):
            self.abils[i] = sum(self.roll_4d6())
            print(utils.abils_name_map[i] + ": " + str(self.abils[i]))

    def display_abils(self):
        print("\nAbility scores:")
        for i in range(1, 7):
            print(utils.abils_name_map[i] + ": " + str(self.abils[i]))

    def display_skills(self):
        print("\nSkills:")

        for key in self.skills:
            abil_category = utils.skills_category_map[key]
            trained = self.skills[key]

            if trained:
                modifier = str(utils.score_mods[self.abils[abil_category]] + 2) + " (trained)"
            else:
                modifier = str(utils.score_mods[self.abils[abil_category]])

            print(key + ":= Modifier: " + modifier)

    def display_stats(self):
        print("\nCharacter Name: ", self.name)
        print("\nHP: ", self.health)
        print("Speed: ", self.speed)
        print("Disease Resistance: ", self.disease_resistance)
        print("Carrying Capacity: ", self.carry_cap)
        self.display_abils()
        self.display_skills()

    def pick_trained_skills(self):
        print("\nPick two trained skills")
        print("Strength-based skills:\n1. Melee Combat\n2. Climbing\n")
        print("Dexterity-based skills:\n3. Ranged Combat\n4. Stealth\n")
        print("Intelligence-based skills:\n5. Investigation\n6. History\n")
        print("Wisdom-based skills:\n7. Survival\n8. Insight\n9. Perception\n10. Medicine\n")
        print("Charisma-based skills:\n11. Intimidation\n12. Deception\n13. Persuasion\n14. Performance\n")
        
        first_choice = 0
        while first_choice < 1 or first_choice > 14:
            try:
                first_choice = int(input("Pick your first skill\n"))
            except:
                print("Enter an integer between 1 and 14")
        
        second_choice = 0
        while second_choice < 1 or second_choice > 14 or first_choice == second_choice:
            try:
                second_choice = int(input("Pick a different second skill\n"))
            except:
                print("Enter an integer between 1 and 14")

        #setting skills to be trained
        self.skills[utils.skills_name_map[first_choice]] = True
        self.skills[utils.skills_name_map[second_choice]] = True

        print("Skills selected!")

    def abils_choice(self):
        """set player ability scores"""
        print("Decide how to assign your ability scores")
        method = ""
        while method != "1" and method != "2":
            method = input("1. Assign manually\n2. Assign randomly\n")
        if method == "1":
            self.set_abils_manual()
            self.display_abils()
        else:
            self.set_abils_random()

    def generate_stats(self):
        """generate remaining stats that are dependent on player ability scores"""
        self.health = 10 + sum(utils.die_roll(8, 2, single_mod=0)) + utils.score_mods[self.abils[3]]
        self.speed = 30 + utils.score_mods[self.abils[2]]
        self.disease_resistance = sum(utils.die_roll(4, 1)) + utils.score_mods[self.abils[3]]
        self.carry_cap = 20 + utils.score_mods[self.abils[1]]

    def __init__(self):
        """constructor"""
        super().__init__()

        print("Create your character to explore New Metro")
        self.name = input("Enter your name\n")

        #assign ability scores
        self.abils_choice()

        #pick skills
        self.pick_trained_skills()

        #generate remaining stats
        self.generate_stats()

        self.display_stats()