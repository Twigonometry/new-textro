import utils

class NPC:
    """parent class for various NPC classes"""

    #attributes
    name = ""
    race = ""
    health = 0
    speed = 0

    hostility = utils.HostilityLevel

    #combat attributes
    melee_weapon_name = ""
    melee_attack_bonus = 0
    melee_damage_die = (0, 0)
    melee_damage_bonus = 0

    has_ranged_attack = False
    ranged_weapon_name = ""
    ranged_attack_bonus = 0
    ranged_damage_die = (0, 0)
    ranged_damage_bonus = 0

    def display_stats(self):
        print("NPC Name: ", self.name)
        print("Race: ", self.race)
        print("Health: ", self.health)
        print("Speed: ", self.speed)

        mdd = self.melee_damage_die
        mdb = self.melee_damage_bonus
        mab = self.melee_attack_bonus

        md_bonus = ""
        if mdb > 0:
            md_bonus = " +" + str(mab)
        elif mdb < 0:
            md_bonus = " -" + str(mab)

        ma_bonus = ""
        if mab > 0:
            ma_bonus = " +" + str(mab)
        elif mab < 0:
            ma_bonus = " -" + str(mab)
        else:
            ma_bonus = " +0"

        print("\nMelee attacks:\n" + self.melee_weapon_name 
        + " (" + str(mdd[1]) + "d" + str(mdd[0]) + md_bonus + ", " + ma_bonus + " to hit)")

        if self.has_ranged_attack:
            rdd = self.ranged_damage_die
            rdb = self.melee_damage_bonus
            rab = self.melee_attack_bonus

            rd_bonus = ""
            if rdb > 0:
                rd_bonus = " +" + str(rab)
            elif rdb < 0:
                rd_bonus = " -" + str(rab)

            ra_bonus = ""
            if rab > 0:
                ra_bonus = " +" + str(rab)
            elif rab < 0:
                ra_bonus = " -" + str(rab)
            else:
                ra_bonus = " +0"

            print("\nRanged attacks:\n" + self.ranged_weapon_name 
            + " (" + str(rdd[1]) + "d" + str(rdd[0]) + rd_bonus + ", " + ra_bonus + " to hit)")

    def introduce(self, quantity, location_type):
        """introduce the NPC in the story;
        description may vary based on current location of player;
        also asks player what their next action is"""

    def interact(self, player):
        """method for interacting with player;
        is called when player chooses to/is forced to start encounter with NPC
        defines extra dialogue options and paths to combat/social/skill encounters"""

    def fight(self, player):
        """defines strategy for NPC in combat with player;
        behaviour may include chasing player down, retreating at certain HP etc;
        should generate a dynamic combat story throughout"""

    def __init__(self, name, race, health, speed, host, mwn, mab, mdd, mdb, hra, rwn, rab, rdd, rdb):
        """constructor"""
        super().__init__()
        self.name = name
        self.race = race
        self.health = health
        self.speed = speed
        self.hostility = host
        self.melee_weapon_name = mwn
        self.melee_attack_bonus = mab
        self.melee_damage_die = mdd
        self.melee_damage_bonus
        self.has_ranged_attack = hra
        self.ranged_weapon_name = rwn
        self.ranged_attack_bonus = rab
        self.ranged_damage_die = rdd
        self.ranged_damage_bonus = rdb