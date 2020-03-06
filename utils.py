import enum
from random import randint

#names for abilities, by number
abils_name_map = {
    1: "Strength",
    2: "Dexterity",
    3: "Constitution",
    4: "Intelligence",
    5: "Wisdom",
    6: "Charisma"
}

#names for skills, by number
skills_name_map = {
    1: "MELEE",
    2: "CLIMBING",
    3: "RANGED",
    4: "STEALTH",
    5: "INVESTIGATION",
    6: "HISTORY",
    7: "SURVIVAL",
    8: "INSIGHT",
    9: "PERCEPTION",
    10: "MEDICINE",
    11: "INTIMIDATION",
    12: "DECEPTION",
    13: "PERSUASION",
    14: "PERFORMANCE"
}

#mapping skills to their ability category, by number
skills_category_map = {
    "MELEE": 1,
    "CLIMBING": 1,
    "RANGED": 2,
    "STEALTH": 2,
    "INVESTIGATION": 4,
    "HISTORY": 4,
    "SURVIVAL": 5,
    "INSIGHT": 5,
    "PERCEPTION": 5,
    "MEDICINE": 5,
    "INTIMIDATION": 6,
    "DECEPTION": 6,
    "PERSUASION": 6,
    "PERFORMANCE": 6
}

#costs of assigning each score
score_costs = {
    8: 0,
    9: 1,
    10: 2,
    11: 3,
    12: 4,
    13: 5,
    14: 7,
    15: 9
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

def get_score_mod(score):
    """looks up modifier for a score, with validated input"""
    if score < 2:
        return score_mods[1]
    elif score > 29:
        return score_mods[30]
    else:
        return score_mods[score]

def die_roll(n, m, **kwargs):
    """roll an n-sided die m times;
    kwargs can specify a single modifier to apply to all rolls
    or an m-array of modifiers to apply in turn
    adv param grants advantage if True, dis param grants disadvantage if True
    advantage rolls twice and picks highest, disadvantage rolls twice and picks lowest"""

    rolls = []

    #getting advantage and disadvantage, cancel out if both present
    adv = False
    dis = False
    if 'adv' in kwargs:
        adv = kwargs.get('adv')
    if 'dis' in kwargs:
        dis = kwargs.get('dis')
    if adv and dis:
        adv = False
        dis = False

    #roll with single modifier applied to all rolls
    if 'single_mod' in kwargs:
        single_mod = kwargs.get('single_mod')
        for i in range(m):
            if adv:
                temp_rolls = []
                print("Rolling with advantage!")
                temp_rolls.append(randint(1, n) + single_mod)
                temp_rolls.append(randint(1, n) + single_mod)
                print(temp_rolls)
                rolls.append(max(temp_rolls))
            elif dis:
                print("Rolling with disadvantage!")
                temp_rolls = []
                temp_rolls.append(randint(1, n) + single_mod)
                temp_rolls.append(randint(1, n) + single_mod)
                print(temp_rolls)
                rolls.append(min(temp_rolls))
            else:
                rolls.append(randint(1, n) + single_mod)

    #roll with array of different modifiers
    elif 'mod_array' in kwargs:
        mod_array = kwargs.get('mod_array')
        if len(mod_array) != m:
            print("Number of modifiers must equal number of dice")
        else:
            for mod in mod_array:
                if adv:
                    print("Rolling with advantage!")
                    temp_rolls = []
                    temp_rolls.append(randint(1, n) + mod)
                    temp_rolls.append(randint(1, n) + mod)
                    print(temp_rolls)
                    rolls.append(max(temp_rolls))
                elif dis:
                    print("Rolling with disadvantage!")
                    temp_rolls = []
                    temp_rolls.append(randint(1, n) + mod)
                    temp_rolls.append(randint(1, n) + mod)
                    print(temp_rolls)
                    rolls.append(min(temp_rolls))
                else:
                    rolls.append(randint(1, n) + mod)

    #no modifier provided
    else:
        for i in range(m):
            if adv:
                print("Rolling with advantage!")
                temp_rolls = []
                temp_rolls.append(randint(1, n))
                temp_rolls.append(randint(1, n))
                print(temp_rolls)
                rolls.append(max(temp_rolls))
            elif dis:
                print("Rolling with disadvantage!")
                temp_rolls = []
                temp_rolls.append(randint(1, n))
                temp_rolls.append(randint(1, n))
                print(temp_rolls)
                rolls.append(min(temp_rolls))
            else:
                rolls.append(randint(1, n))

    return rolls

def skill_check(skill, skill_dict, target, kwargs):
    """roll 1d20 with a modifier and compare to target number, return True/False;
    if skill is present in player/NPC's skills dictionary, use its modifier;
    kwargs adv and dis represent advantage and disadvantage (true/false values)"""

    modifier = 0

    if skill in skill_dict:
        modifier = skill_dict[skill]

    #advantage/disadvantage
    adv = False
    dis = False
    if 'adv' in kwargs:
        adv = kwargs.get('adv')
    if 'dis' in kwargs:
        dis = kwargs.get('dis')
    
    result = die_roll(20, 1, single_mod=modifier, adv=adv, dis=dis)
    
    if result >= target:
        return True
    else:
        return False

#enum for NPC hostility
class HostilityLevel(enum.Enum):
    FRIENDLY = "FRIENDLY"
    NEUTRAL = "NEUTRAL"
    HOSTILE = "HOSTILE"

class NPCSize(enum.Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"

def display_costs():
    print("\nCosts for each ability score:")
    for score in score_costs:
        print(str(score) + ": " + str(score_costs[score]))

def main():
    print("Gambling...")
    print("1d8\n", die_roll(8, 1, adv=False))
    print("1d6 + 1\n", die_roll(6, 1, single_mod=1))
    print("3d20 + 3\n", die_roll(20, 3, single_mod=3, adv=True))
    print("4d8 with modifiers 1, 2, 3, 4\n", die_roll(8, 4, mod_array=[1, 2, 3, 4], dis=True))
    print("4d8 with modifiers 1, 2, 3, 4\n", die_roll(8, 4, mod_array=[1, 2, 3, 4], adv=True, dis=True))
    print("2d4 with not enough mods!\n", die_roll(4, 2, mod_array=[1], adv=True, dis=True))

if __name__ == '__main__':
    main()