import enum

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

class HostilityLevel(enum.Enum):
    FRIENDLY = "FRIENDLY"
    NEUTRAL = "NEUTRAL"
    HOSTILE = "HOSTILE"

def display_costs():
    print("\nCosts for each ability score:")
    for score in score_costs:
        print(str(score) + ": " + str(score_costs[score]))