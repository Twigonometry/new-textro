import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import utils

class NPC:
    """parent class for various NPC classes"""

    #attributes
    name = ""
    health = 0
    speed = 0

    hostility = utils.HostilityLevel

    #combat attributes
    melee_attack_bonus = 0
    melee_damage_die = 0
    melee_damage_bonus = 0

    has_ranged_attack = False
    ranged_attack_bonus = 0
    ranged_damage_die = 0
    ranged_damage_bonus = 0

    def introduce(self):
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

    def __init__(self, health, speed, host, mab, mdd, mdb, hra, rab, rdd, rdb):
        """constructor"""
        super().__init__()
        self.health = health
        self.speed = speed
        self.hostility = host
        self.melee_attack_bonus = mab
        self.melee_damage_die = mdd
        self.melee_damage_bonus
        self.has_ranged_attack = hra
        self.ranged_attack_bonus = rab
        self.ranged_damage_die = rdd
        self.ranged_damage_bonus = rdb