import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import utils

class NPC:
    """parent class for various NPC classes"""

    #attributes
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

    def interact(self, player):
        """method for interacting with player
        defines extra dialogue options and paths to combat/social/skill encounters"""