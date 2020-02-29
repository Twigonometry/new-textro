"""main game engine that displays text messages to screen"""

import utils
import player
import NPCs.bandit as bandit
import Encounters.encounter as encounter

#necessary background variables
hostility = utils.HostilityLevel

def main():
    print("Hello New Metro")
    main_player = player.Player()
    bandit1 = bandit.Bandit("Bandit", "Human", 22, 30, hostility.HOSTILE, "Wrench", 1, (8, 1), 1, True, "Catapult", 1, (6, 1), 1)
    initial_encounter = encounter.Encounter(main_player, [bandit1], [30])

if __name__ == '__main__':
    main()