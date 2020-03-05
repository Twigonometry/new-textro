"""main game engine that displays text messages to screen"""

import utils
import player
import NPCs.bandit as bandit
import Encounters.encounter as encounter
import world_engine as world

#necessary background variables
hostility = utils.HostilityLevel
location_type = world.LocationType

def main():
    print("Hello New Metro")
    main_player = player.Player()
    print("Character created")
    bandit1 = bandit.Bandit("Bandit", "Human", 22, 30, hostility.HOSTILE, "Wrench", 1, (8, 1), 1, True, "Catapult", 1, (6, 1), 1, None, {1: 14, 2: 14, 3: 10, 4: 8, 5: 8, 6: 8}, {})
    bandit2 = bandit.Bandit("Bandit", "Human", 22, 30, hostility.HOSTILE, "Wrench", 1, (8, 1), 1, True, "Catapult", 1, (6, 1), 1, None, {1: 14, 2: 14, 3: 10, 4: 8, 5: 8, 6: 8}, {})
    bandit3 = bandit.Bandit("NotBandit", "Human", 22, 30, hostility.NEUTRAL, "Wrench", 1, (8, 1), 1, True, "Catapult", 1, (6, 1), 1, None, {1: 14, 2: 14, 3: 10, 4: 8, 5: 8, 6: 8}, {})
    initial_encounter = encounter.Encounter(main_player, [bandit1, bandit2, bandit3], [30, 30, 5], location_type.INDOORS)
    #initial_encounter = encounter.Encounter(main_player, [bandit1, bandit2], [30, 30], location_type.INDOORS)
    #initial_encounter = encounter.Encounter(main_player, [bandit3], [5], location_type.INDOORS)

if __name__ == '__main__':
    main()